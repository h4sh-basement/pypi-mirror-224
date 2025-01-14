from uuid import uuid4, UUID
import json
from functools import wraps
from .job import UnicatJob


def gid():
    return str(uuid4())


def maybe_gid(possible_gid):
    possible_gid = str(possible_gid)
    try:
        possible_uuid = UUID(possible_gid, version=4)
    except ValueError:
        return False
    return str(possible_uuid) == possible_gid


def test_false(data):
    return str(data).lower().strip() in (
        "",
        "0",
        "no",
        "n",
        "off",
        "false",
        "f",
        "unchecked",
        "deselected",
        "none",
        "null",
        "undefined",
    )


def test_true(data):
    return not test_false(data)


def _job(func):
    """
    Decorator that handles calls returning jobs.

    The decorated function *MUST* take a first unicat instance argument, and
    *MUST* return a tuple with the job gid (the "job.token" from their result) first,
    and the regular return value second.

    These decorated functions will probably be mutation functions.

    This decorator adds an `return_job` keyword argument (defaults to False) to the
    decorated function.

    If `return_job` is False, we wait for the job to be done, and return the value from
    the decorated function (or raise UnicatError).
    If `return_job` is True, we return a UnicatJob where you can track progress. The
    UnicatJob has a return_value property that holds the return value from the
    decorated function.
    """

    @wraps(func)
    def wrapped(unicat, *args, return_job=False, **kwargs):
        cursor = unicat.api.prepare_for_job()
        job_gid, return_value = func(unicat, *args, **kwargs)
        job = UnicatJob(unicat, cursor, job_gid, return_value)
        if return_job is True:
            return job
        for _ in job.track(poll_interval_in_seconds=1):
            pass
        if job.status != "done" or "error" in job.info:
            raise UnicatError(
                "Job error",
                {
                    "code": 4001,
                    "message": f"Job '{job.name}' error",
                    "info": {"job": job.as_progress_dict()},
                },
            )
        return job.return_value

    return wrapped


class DuckObject:
    """Uses keyword arguments to construct any duck-like object with those attributes.

    ```
    ducklike = DuckObject(walk="waddle", talk="quack")
    assert ducklike.walk == "waddle"
    assert ducklike.talk == "quack"
    assert not hasattr(ducklike, "bill")

    duckquery = DuckObject(
        q="",
        filter=["value", "is", [base_artnr_field.gid, article.base_artnr]]
    )
    print(duckquery.q, duckquery.filter)

    duckrecord = DuckObject(gid="<anything gid-like>")
    print(duckrecord.gid)
    ```
    """

    def __init__(self, **kwargs):
        self.__dict__ = kwargs


class FieldColumns:
    """FieldColumns are needed for class fields, that have nested subfields.

    With FieldColumns, we can flatten a list of fields to a list of columns,
    associated with those fields.

    Each column has a fieldstack, that is a list of the field and nested subfields.
    For a regular field, the fieldstack is just that field.
    A classfield with three subfields will yield three columns, and each column has
    a fieldstack with the classfield first, and then the subfield for that column.
    If that subfield is another classfield, we'll get more columns and deeper
    stackfields.

    Most of the time, you won't need the stackfield in the client code, see also the
    _FieldColumn implementation where we get the 'name' for a column by walking the
    fieldstack.

    Client code can look something like this, for reading from Unicat:

    ```
    columns = FieldColumns(fields, prefix_column_count=3)
    for column in columns:
        column_name = column.name()  # e.g. 'image' or 'dimensions.width__mm'
        column_label = column.label()  # e.g. 'Image' or 'Dimensions\nWidth [mm]'
        column_value = None
        error = None
        try:
            record_field = column.extract_record_field(record.fields[language])
            column_value = record_field.value if record_field else None
        except KeyError:
            error = (
                "Field is not part of this definition. Do not enter data here."
            )
    ```

    FieldColumns can also be used to write to Unicat, when we need a record's fields
    data structure:

    ```
    recordfields_data = {}
    for column in columns:
        fieldvalue = row[column.index].value
        column.update_fields_data(recordfields_data, fieldvalue)
    unicat.mutate.update_record(record, {language: recordfields_data})
    ```
    """

    def __init__(self, fields, prefix_column_count=0):
        self._columns = []
        index = prefix_column_count
        for fieldstack in self._flatten_fields(fields, []):
            self._columns.append(_FieldColumn(index, fieldstack))
            index += 1
        self._iterindex = 0

    def __iter__(self):
        self._iterindex = 0
        return self

    def __next__(self):
        if self._iterindex >= len(self._columns):
            raise StopIteration
        column = self._columns[self._iterindex]
        self._iterindex += 1
        return column

    def _flatten_fields(self, fields, fieldstack):
        flattened_fields = []
        for field in fields:
            if field.type == "class":
                subfieldstack = [*fieldstack, field]
                for subfield in self._flatten_fields(
                    field.class_.fields, subfieldstack
                ):
                    flattened_fields.append(subfield)
            else:
                flattened_fields.append([*fieldstack, field])
        return flattened_fields


class _FieldColumn:
    def __init__(self, index, fieldstack):
        self.index = index
        self.number = index + 1
        self._fieldstack = fieldstack

    def name(self, separator="."):
        return separator.join(field.name for field in self._fieldstack)

    def label(self, language, separator="\n"):
        return separator.join(field.title[language] for field in self._fieldstack)

    def extract_record_field(self, localized_record_fields):
        """Going to Excel (or csv), extract a field from a record.

        This is not converted to a string yet, so that is something you still have to
        handle.

        Don't provide column data, provide the row record.fields[language]

        ```
        for column in columns:
            column_value = None
            try:
                record_field = column.extract_record_field(record.fields[language])
                column_value = record_field.value if record_field else None
                excel.write("A1", f"{column_value}")  # naive conversion to string
            except KeyError:
                comment = (
                    "Field is not part of this definition. Do not enter data here."
                )
        ```
        """
        record_field = localized_record_fields  # initial reference
        for entry in self._fieldstack:
            record_field = record_field[entry.name]  # may raise KeyError
            if not record_field:
                break
        return record_field

    def update_fields_data(self, localized_record_fields_data, value):
        """Coming from Excel (or csv), build fields_data for a record from each column.

        The value should be of the correct type for the field. For a class field, this
        means the 'deepest' field type, so e.g. an integer for dimensions.length__mm.
        For a classlist field, we need a valid JSON data structure.

        Updates the localized_record_fields_data argument.

        localized_record_fields_data looks like record.fields[language], but as a
        json data structure
        localized_record_fields_data starts with a single {}
        value is the value in the cell, pre-converted to the right type

        ```
        fields_data = {}
        for column in columns:
            value = row[column.index].value
            column.update_fields_data(fields_data, value)
        unicat.update_record(gid, language, fields_data)
        ```
        """
        field_data = value
        for entry in reversed(self._fieldstack):
            temp = {entry.name: field_data}
            field_data = temp
        merge_dicts(localized_record_fields_data, field_data)

    @property
    def field(self):
        return self._fieldstack[-1]

    @property
    def fieldstack(self):
        return self._fieldstack


def make_bool(any):
    """
    bool("False") returns true, make_bool("False") doesn't
    """
    if any is None:
        return None
    return test_true(any)


def make_bool_str(any):
    if any is None:
        return None
    return "yes" if test_true(any) else "no"


def make_str(any):
    if any is None or len(any) == 0:
        return None
    if isinstance(any, list):
        return "\n".join(str(line) for line in any)  # normalizes newlines
    return "\n".join(str(any).splitlines())  # normalizes newlines


def make_json_str(any):
    if any is None:
        return None
    return json.dumps(any, indent=2, ensure_ascii=False).replace("},\n", "},")


def make_json(any):
    if any is None:
        return None
    return json.loads(str(any))


def make_int(any):
    if any is None:
        return None
    return int(any)


def make_float(any):
    if any is None:
        return None
    return float(any)


def noop(any):
    return any


def make_str_list(any):
    if any is None or len(any) == 0:
        return None
    if not isinstance(any, list):
        any = str(any).splitlines()
    return [str(line).strip() for line in any]  # each entry must be a string


VALUE_TO_FIELDDATA = {
    "text": make_str,
    "textline": make_str,
    "textlist": make_str_list,
    "number": make_int,
    "decimal": make_float,
    "boolean": make_bool,
    "code": make_str,
    "barcode": make_str,
    "class": make_json,
    "classlist": make_json,
    "image": make_str,
    "imagelist": make_str_list,
    "file": make_str,
    "filelist": make_str_list,
    "record": make_str,
    "recordlist": make_str_list,
    "fieldpicker": make_str,
}

FIELDDATA_TO_VALUE = {
    "text": make_str,
    "textline": make_str,
    "textlist": make_str,
    "number": noop,  # Excel accepts numbers, see also FIELDTYPE_NUMBER_FORMAT
    "decimal": noop,  # Excel accepts numbers, see also FIELDTYPE_NUMBER_FORMAT
    "boolean": make_bool_str,
    "code": make_str,
    "barcode": make_str,
    "class": make_json_str,
    "classlist": make_json_str,
    "image": make_str,
    "imagelist": make_str,
    "file": make_str,
    "filelist": make_str,
    "record": make_str,
    "recordlist": make_str,
    "fieldpicker": make_str,
}


def convert_value_to_fielddata(fieldtype, value):
    """Return a value suitable for writing to Unicat, for list field types this
    means converting newline-separated entries to lists. For class/classlist fields
    we parse the JSON string to product the field data.

    This can raise exceptions when the value doesn't match the type, e.g. converting a
    string to a float.
    """
    return VALUE_TO_FIELDDATA[fieldtype](value)


def convert_fielddata_to_value(fieldtype, fielddata):
    """Return a value suitable for writing in a cell, such as a text or a number.
    Lists will be flattened by stringifying each item and concatenating with \n. For
    class/classlist fields we produce a pretty-printed JSON string.
    """
    return FIELDDATA_TO_VALUE[fieldtype](fielddata)


def merge_dicts(a, b):
    """Merge b into a, returning a.

    a is updated; if you don't want to mutate a, call it as `merge_dicts(dict(a), b)`.
    """
    for key in b:
        if key in a:
            if isinstance(a[key], dict) and isinstance(b[key], dict):
                merge_dicts(a[key], b[key])
            else:
                a[key] = b[key]  # overwrite a
        else:
            a[key] = b[key]
    return a


def diff_record_fields_data(unicat, record, localizedfielddata):
    """Return a version of localizedfielddata that only has data that is different from
    the raw record data.
    """
    localizedrecordfielddata = record._data["fields"]  # raw data
    localized_changed_data = {}
    for language in unicat.languages:
        if language not in localizedfielddata:
            continue
        fielddata = localizedfielddata[language]
        recordfielddata = localizedrecordfielddata[language]
        changed_data = {}
        for name, value in fielddata.items():
            if name not in recordfielddata:  # unknown field, can't update
                continue
            if not value and not recordfielddata[name]:  # None, [] are equivalent
                continue
            if hash_data(value) == hash_data(recordfielddata[name]):  # value unchanged
                continue
            changed_data[name] = value
        if changed_data:
            localized_changed_data[language] = changed_data
    return localized_changed_data


def hash_text(text):  # unicode ok
    hash = 0
    for letter in text:
        hash = (31 * hash + ord(letter)) & 0xFFFFFFFF
    hash = ((hash + 0x80000000) & 0xFFFFFFFF) - 0x80000000
    return ("00000000" + hex(hash)[2:])[-8:]


def hash_data(data):
    return hash_text(json.dumps(data, sort_keys=True))
