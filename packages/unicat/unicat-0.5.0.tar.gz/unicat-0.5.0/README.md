# Unicat client library

Unicat is a Product Information Management SaaS.

This library is still a work in progress, not all Unicat API options are covered yet.

Documentation still needs a bit of work too.


First, connect to Unicat (https://unicat.app):

```
import sys
from unicat import Unicat
from .env import server, project_gid, api_key, local_folder

unicat = Unicat(server, project_gid, api_key, local_folder)
if not unicat.connect():
  print("Invalid connection settings")
  sys.exit(1)
```

Download all assets for the project (you can find them in the local_folder):

```
for asset in unicat.walk_asset_tree():
  if asset.is_file:
    asset.download()
```

Or, write an XML product feed:

```
with open("product-feed.xml", "w", encoding="utf-8") as f:
  f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  f.write('<products>\n')

  for record in unicat.walk_record_tree():
    if record.definition.name != "article":
      continue

    fields = record.fields["nl"]

    artnr = fields["artnr"].value
    price = fields["price"].value
    stock = fields["stock"].value

    f.write(f'  <product artnr="{artnr}" price="{price:%0.02f}" stock="{stock}"/>\n')
  f.write('</products>\n')
```

There's also unicat.mutate, with options to update the Unicat project server-side, like unicat.mutate.create_record, unicat.mutate.modify_field and many more.


## The `unicat` package

The Unicat package is split into reading/traversing and mutating. All mutating methods below are available on the `unicat.mutate` property. They will raise a UnicatError on error.

### Reading methods

```python
def get_record(gid: str, *, force: bool) -> UnicatRecord | None
def get_records(gids: list[str], *, force: bool) -> list[UnicatRecord]
def get_root_record() -> UnicatRecord
def get_asset(gid: str, *, force: bool) -> UnicatAsset | None
def get_asset_by_pathname(pathname: str, *, force: bool) -> UnicatAsset | None
def get_assets(gids: list[str], *, force: bool) -> list[UnicatAsset]
def get_assets_by_pathnames(pathnames: list[str], *, force: bool) -> list[UnicatAsset]
def get_root_asset() -> UnicatAsset
def get_definition(gid: str) -> UnicatDefinition | None
def get_definitions(gids: list[str]) -> list[UnicatDefinition]
def get_definition_by_name(name: str) -> UnicatDefinition | None
def get_definitions_by_name(names: list[str]) -> list[UnicatDefinition]
def get_class(gid: str) -> UnicatClass | None
def get_classes(gids: list[str]) -> list[UnicatClass]
def get_class_by_name(name: str) -> UnicatClass | None
def get_classes_by_name(names: list[str]) -> list[UnicatClass]
def get_field(gid: str) -> UnicatField | None
def get_fields(gids: list[str]) -> list[UnicatField]
def get_field_by_name(name: str) -> UnicatField | None
def get_fields_by_name(names: list[str]) -> list[UnicatField]
def get_query(gid: str) -> UnicatQuery | None
def get_queries(gids: list[str]) -> list[UnicatQuery]
def get_record_query_by_name(name: str) -> UnicatQuery | None
def get_record_queries_by_name(names: list[str]) -> list[UnicatQuery]
def get_asset_query_by_name(name: str) -> UnicatQuery | None
def get_asset_queries_by_name(names: list[str]) -> list[UnicatQuery]
def get_schema_query_by_name(name: str) -> UnicatQuery | None
def get_schema_queries_by_name(names: list[str]) -> list[UnicatQuery]
```

### Traversing methods

```python
def walk_record_children(parent_record: UnicatRecord, channel: gid, ordering: gid) -> Iterator[UnicatRecord]
def walk_record_tree(channel: gid, ordering: gid) -> Iterator[UnicatRecord]
def walk_record_query(language: str, query: UnicatQuery, *, limit: int) -> Iterator[tuple[int, UnicatRecord]]
def walk_asset_children(parent_asset: UnicatAsset) -> Iterator[UnicatAsset]
def walk_asset_tree() -> Iterator[UnicatAsset]
def walk_asset_query(language: str, query: UnicatQuery, *, limit: int) -> Iterator[tuple[int, UnicatAsset]]
def walk_definitions() -> Iterator[UnicatDefinition]
def walk_classes() -> Iterator[UnicatClass]
def walk_fields() -> Iterator[UnicatField]
def walk_schema_query(language: str, query: UnicatQuery, *, limit: int) -> Iterator[tuple[int, UnicatQuery]]
def walk_queries() -> Iterator[UnicatQuery]
```

### Properties

```python
unicat.project: UnicatProject
```

### `UnicatProject` properties & methods

```python
project.gid: gid
project.name: str
project.owner: UnicatUser
project.icon: str  # used to construct /media url
project.status: str
project.languages: list[str]
project.default_language: str
project.channels: dict[str, gid]
project.default_channel: gid
project.channel_name(key: gid) -> str
project.orderings: dict[str, gid]
project.default_ordering: gid
project.ordering_name(key: gid) -> str
project.fieldlists: dict[str, gid]
project.default_fieldlist: gid
project.fieldlist_name(key: gid) -> str
project.members: list[UnicatProjectMember]
```

### `UnicatUser` properties & methods

```python
user.gid: gid
user.username: str
user.name: str
user.avatar: str  # used to construct /media url
```

### `UnicatProjectMember` properties & methods

```python
projectmember.project: UnicatProject
projectmember.user: UnicatUser
projectmember.status: str
projectmember.roles: list[str]
projectmember.options: dict
projectmember.key: str
```

### `UnicatDefinition` properties & methods

```python
definition.gid: gid
definition.original: UnicatDefinition | None
definition.name: str
definition.label: dict[str, str]  # key is language
definition.classes: list[UnicatClass]
definition.classes_as_gids: list[gid]
definition.fields: list[UnicatField]
definition.fields_as_gids: list[gid]
definition.titlefield: UnicatField
definition.fieldlists: dict[str, list[UnicatField]]  # key is fieldlist key
definition.layout: UnicatLayout
definition.childdefinitions: list[UnicatDefinition]
definition.is_base: bool
definition.is_new: bool
definition.is_extended: bool
definition.is_working_copy: bool
definition.is_committed: bool
definition.all_fields: list[UnicatField]
definition.base_classes: list[UnicatClass]
definition.base_fields: list[UnicatField]
definition.all_base_fields: list[UnicatField]
definition.extended_classes: list[UnicatClass]
definition.extended_fields: list[UnicatField]
definition.all_extended_fields: list[UnicatField]
```

### `UnicatClass` properties & methods

```python
class_.gid: gid
class_.original: UnicatClass | None
class_.name: str
class_.label: dict[str, str]  # key is language
class_.fields: list[UnicatField]
class_.fields_as_gids: list[gid]
class_.layout: UnicatLayout
class_.is_new: bool
class_.is_working_copy: bool
class_.is_committed: bool
```

### `UnicatField` properties & methods

```python
field.gid: gid
field.original: UnicatField | None
field.name: str
field.type: str
field.class_: UnicatClass | None
field.options: dict
field.is_localized: bool
field.is_required: bool
field.label: dict[str, str]  # key is language
field.initial: dict[str, str]  # key is language
field.unit: str
field.title: dict[str, str]  # key is language
field.is_new: bool
field.is_working_copy: bool
field.is_committed: bool
```

### `UnicatLayout` properties & methods

```python
layout.gid: gid
layout.original: UnicatLayout | None
layout.name: str
layout.root: gid
layout.components: dict[gid, dict]
layout.is_new: bool
layout.is_working_copy: bool
```

### `UnicatQuery` properties & methods

```python
query.gid: gid
query.type: str  # schema, record, or asset
query.name: str
query.q: str
query.filter: list
```

### `UnicatAsset` properties & methods

```python
asset.gid: gid
asset.pathname: str
asset.path: str
asset.name: str
asset.is_file: bool
asset.type: str
asset.childcount: int
asset.status: str
asset.is_deleted: bool
asset.info: dict
asset.transforms: dict[str, dict] | None
asset.default_transform: dict | None
asset.title: dict[str, str]  # key is language
asset.description: dict[str, str]  # key is language
asset.updated_on: timestamp  # 1610635123.351925
asset.publish() -> str  # public_url
asset.publish_transformed(transform: UnicatTransform | None) -> str  # public_url
asset.download() -> False | None | str  # local_filepath
asset.download_transformed(transform: UnicatTransform | None) -> False | None | str  # local_filepath
```

### `UnicatRecord` properties & methods

```python
record.gid: gid
record.canonical: gid
record.parent: gid
record.backlinks: list[gid]
record.is_link: bool
record.is_deleted: bool
record.treelevel: int
record.path: list[gid]
record.title: dict[str, str]  # key is language
record.channels: list[gid]  # enabled channels only
record.orderings: dict[gid, int]
record.childcount: int
record.definition: UnicatDefinition
record.fields: dict[str, dict[str, UnicatRecordField]]  # key is language, then fieldname
```

### `UnicatRecordField` properties & methods

```python
recordfield.field: UnicatField
recordfield.value: Any
```

A record field can have a value, a reference (record, asset), or it can be nested for class-fields. \
We also support 'list' versions of these.

> Note: this will probably be refactored in an upcoming version \
>       then, it may work like recordfield.label["en"] == "Image" \
>       and, for e.g. image fields, recordfield.value.pathname == "/asset-1-name.svg"

```python
# for values

artnr = record.fields[language]["artnr"]  # a recordfield
artnr.value             # "CMS 225-945"
artnr.field.label       # "Article number"
artnr.field.type        # "textline"

# for references

image = record.fields[language]["image"]  # both recordfield and asset
image.value             # "a0a80c9c-fa1b-4573-ac98-b7b07c81b583"
image.field.label       # "Image"
image.pathname          # "/products/cms225.eps"

# for class fields

dimensions_interior = record.fields[language]["dimensions_interior"]
                        # a recordfield and classfield
dimensions_interior.value               # {"width__mm": 374, …}
dimensions_interior["width__mm"].value  # 374  -- this is a recordfield

# for list values

colors = record.fields[language]["colors"]
colors.value            # ["Red", "Blue"]
colors.field.label      # "Colors"
colors[0].value         # "Red" -- this is just a string

# for list references

images = record.fields[language]["images"]
images.value            # ["a0a80c9c-fa1b-4573-ac98-b7b07c81b583", ]
images.field.label      # "Images"
images[0]               # this is just an asset
images[0].pathname      # "/products/cms225.eps"

# for classlist fields

tablespecs = record.fields[language]["tablespecs"]
tablespecs.value                        # [{"width__mm": 7, …}, …]
tablespecs.field.label                  # "Table specs"
tablespecs[0]                           # this is recordfield-like
tablespecs[0]["width__mm"].value        # 7
tablespecs[0]["width__mm"].field.label  # "Width"
```


### Mutating project settings

```python
def add_language(language: str) -> bool
def remove_language(language: str) -> bool

def create_channel(name: str) -> gid  # gid type is actually a string
def delete_channel(gid: gid) -> bool

def create_ordering(name: str) -> gid
def delete_ordering(gid: gid) -> bool

def create_fieldlist(name: str) -> gid
def delete_fieldlist(gid: gid) -> bool
```

### Mutating definitions

```python
def create_definition(*, name: str, label: dict[str, str], classes: list[UnicatClass], fields: list[UnicatField], titlefield: UnicatField, childdefinitions: list[UnicatDefinition]) -> UnicatDefinition
def modify_definition(definition: UnicatDefinition, *, name: str, label: dict[str, str], classes: list[UnicatClass], fields: list[UnicatField], titlefield: UnicatField, childdefinitions: list[UnicatDefinition]) -> UnicatDefinition
def modify_definition_modify_layout(definition: UnicatDefinition, *, name: str, root: gid, components: dict[gid, dict]) -> UnicatDefinition
def modify_definition_add_class(definition: UnicatDefinition, class_: UnicatClass) -> UnicatDefinition
def modify_definition_remove_class(definition: UnicatDefinition, class_: UnicatClass) -> UnicatDefinition
def modify_definition_add_field(definition: UnicatDefinition, field: UnicatField) -> UnicatDefinition
def modify_definition_remove_field(definition: UnicatDefinition, field: UnicatField) -> UnicatDefinition
def modify_definition_fieldlist_add_field(definition: UnicatDefinition, fieldlist: gid, field: UnicatField) -> UnicatDefinition
def modify_definition_fieldlist_remove_field(definition: UnicatDefinition, fieldlist: gid, field: UnicatField) -> UnicatDefinition
def modify_definition_add_childdefinition(definition: UnicatDefinition, childdefinition: UnicatDefinition) -> UnicatDefinition
def modify_definition_remove_childdefinition(definition: UnicatDefinition, childdefinition: UnicatDefinition) -> UnicatDefinition
def commit_definition(new_or_working_copy: UnicatDefinition) -> UnicatDefinition
def save_as_new_definition(working_copy: UnicatDefinition) -> UnicatDefinition
def delete_definition(definition: UnicatDefinition) -> bool
```

### Mutating classes

```python
def create_class(*, name: str, label: dict[str, str], fields: list[UnicatField]) -> UnicatClass
def modify_class(class_: UnicatClass, *, name: str, label: dict[str, str], fields: list[UnicatField]) -> UnicatClass
def modify_class_modify_layout(class_: UnicatClass, *, name: str, root: gid, components: dict[gid, dict]) -> UnicatClass
def modify_class_add_field(class_: UnicatClass, field: UnicatField) -> UnicatClass
def modify_class_remove_field(class_: UnicatClass, field: UnicatField) -> UnicatClass
def commit_class(new_or_working_copy: UnicatClass) -> UnicatClass
def save_as_new_class(working_copy: UnicatClass) -> UnicatClass
def delete_class(class_: UnicatClass) -> bool
```

### Mutating fields

```python
def create_field(*, name: str, type: str, is_localized: bool, is_required: bool, label: dict, unit: str, initial: dict, options: dict) -> UnicatField
def modify_field(field: UnicatField, *, name: str, type: str, is_localized: bool, is_required: bool, label: dict, unit: str, initial: dict, options: dict) -> UnicatField
def commit_field(new_or_working_copy: UnicatField) -> UnicatField
def save_as_new_field(working_copy: UnicatField) -> UnicatField
def delete_field(field: UnicatField) -> bool
```

### Mutating records

```python
def create_record(parent: UnicatRecord, ordering: gid) -> UnicatRecord
def set_record_definition(record: UnicatRecord, definition: UnicatDefinition) -> UnicatRecord
def extend_record_definition_add_class(record: UnicatRecord, class_: UnicatClass) -> UnicatRecord
def extend_record_definition_add_field(record: UnicatRecord, field: UnicatField) -> UnicatRecord
def update_record(record: UnicatRecord, localizedfielddata: dict) -> UnicatRecord
def set_record_channels(record: UnicatRecord, channels: list[gid], enabled: bool) -> UnicatRecord
def copy_record_channels_from_parent(record: UnicatRecord, channels: list[gid] | None) -> UnicatRecord
def copy_record_channels_down(record: UnicatRecord, channels: list[gid] | None, return_job: Bool = False) -> UnicatRecord | UnicatJob
def copy_record_channels_up(record: UnicatRecord, channels: list[gid] | None) -> UnicatRecord
def set_record_orderings(record: UnicatRecord, orderings: dict) -> UnicatRecord
def link_record(parent: UnicatRecord, record: UnicatRecord, ordering: gid) -> UnicatRecord
def delete_record(record: UnicatRecord) -> UnicatRecord
def undelete_record(record: UnicatRecord) -> UnicatRecord
def permanent_delete_record(record: UnicatRecord, return_job: Bool = False) -> UnicatRecord | UnicatJob
```

### Mutating assets

```python
def upload_asset(localfilepath: Path | str, folderasset: UnicatAsset) -> UnicatAsset
def upload_update_asset(localfilepath: Path | str, asset: UnicatAsset) -> UnicatAsset
def create_asset(parentasset: UnicatAsset, name: str) -> UnicatAsset
def update_asset(asset: UnicatAsset, name: str, title: dict, description: dict) -> UnicatAsset
def delete_asset(asset: UnicatAsset) -> UnicatAsset
def undelete_asset(asset: UnicatAsset) -> UnicatAsset
def permanent_delete_asset(asset: UnicatAsset) -> bool
```

### Mutating queries

```python
def create_query(type: str, name: str, q: str, filter: list) -> UnicatQuery
def update_query(query: UnicatQuery, name: str, q: str, filter: list) -> UnicatQuery
def delete_query(query: UnicatQuery) -> bool
```


### Jobs

Some mutating methods can return a job if requested, so you can choose to wait for completion yourself (`track` method), or ignore it and let it finish in the background some time. The job always has the `return_value` from the (mutating) method available -- this is the "immediately returned" value, not some result from running the actual job (look in `status` and `info` instead).

Usage:

```python
# by default, the method waits for completion before returning
record = unicat.mutate.copy_record_channels_down(record, channels)

# but you can also track progress yourself
job = unicat.mutate.copy_record_channels_down(record, channels, return_job=True)
for status in job.track():
    assert status == job.status
    print(job.name, job.status)
record = job.return_value

# or, return quickly and let the job run unmonitored in the background
job = unicat.mutate.copy_record_channels_down(record, channels, return_job=True)
record = job.return_value
```

#### `UnicatJob` properties & methods

```python
job.gid: gid
job.name: str
job.status: str
job.info: dict
job.created_on: timestamp | None
job.updated_on: timestamp | None
job.progress: dict  # combined gid, name, status, info, and timestamps
job.return_value: Any
def track(timeout_in_seconds: float | None = None, poll_interval_in_seconds: float = 1.0) -> Generator[str]
```


### Error handling

We handle errors with the `UnicatError` exception.

```python
from unicat import Unicat, UnicatError
from config import PROJECT_GID, SECRET_API_KEY, LOCAL_ASSET_FOLDER

unicat = Unicat("https://unicat.app", PROJECT_GID, SECRET_API_KEY, LOCAL_ASSET_FOLDER)
if not unicat.connect():
    raise Exception("Invalid connection settings")

...

try:
    unicat.mutate.update_record(record, {language: fields_data})
except UnicatError as e:
    print(e, e.code, e.message, e.info)
```

The `.code`, `.message`, and `.info` properties match the API error result.


### Asset transform helper

```python
from unicat import UnicatTransform
```

We use this on assets, for publishing and/or downloading transformed versions.

```python
transform = UnicatTransform(resize="fill", width=400, height=300, type="jpg", dpr=2, optimize=True)

public_url = asset.publish_transformed(transform)

transform.merge(UnicatTransform(width=200, height=200, key="thumb")) # keeps type, dpr, etc

local_pathname = asset.download_transformed(transform)
```

A `UnicatTransfrom` accepts any combination of the following arguments.

```text
name
key
force
optimize
resize
width
height
type
hotspot
crop
padding
quality
background
dpr
```

Each argument explained:

    name = "seo-optimized-name"

Default: use source filename \
Use this as the filename instead of the source filename. Mustn't include the extension.

    key = "2x"

Default: auto-generate a key from a hash of the options \
If you make multiple transforms from the same file, you can use keys to individualize them. They are included in the filename after the name and before the extension. A key is prepended by a '@', so we would get /filename@2x.jpg. You can use @'s in filenames and in keys, just make sure that the combinations add up to a unique final filename.

    type = "jpg"

Options: jpg, png, or gif \
Both extension and transformed file type. If you don't specify this, the source extension is used, which can lead to faulty results if it isn't one of the supported file types (jpg, png, or gif).

    force = True

Default: False \
If force isn't enabled, no transformation is done if a file with the transform filename exists and is newer than the source.

    optimize = True

Default: False \
We support pngcrush, jhead, jpegoptim, jpeg-recompress, gifsicle, scour, and svgo to strip down and compress the transformed file. Since this is a time-consuming process, it is disabled by default.

    resize = "fill"

Options: width, height, fit, or fill \
Resizing will always respect the aspect ratio. Placement of the resized source on the canvas is controlled by the width, height, hotspot, crop, and padding options. Images are never scaled up, only down.

    width = 400

Resulting width of the transformed asset, in logical pixels (see also `dpr`).

Value is capped at 5000 pixels.

    height = 300

Resulting height of the transformed asset, in logical pixels (see also `dpr`).

Value is capped at 5000 pixels.

    hotspot = (0.5, 0.5)

Default: 0.5,0.5 (the center) \
The hotspot serves two purposes: first to place the resized image on the canvas with the hotspot as close as possible to the center of the canvas, and second as the centerpoint for the crop transform if one is requested.
The hotspot is given as an x,y coordinate, with values as a fraction of the width and height, respectively. Valid values are 0.0 through 1.0 for each.

    crop = (0.6, 0.6)

Default: don't crop \
Use crop to select an area from the source that will then be resized to be placed on the canvas. The crop is centered on the hotspot.
The crop is given as w,h dimensions, with values as a fraction of the width and height, respectively. Valid values are 0.0 through 1.0 for each.

    padding = (0, "auto", 0, "auto")

Default: `auto`,`auto`,`auto`,`auto` \
Specify padding in the target image. The values are for top, right, bottom, and left padding (clockwise starting at top). If a value is set to `auto`, that padding will grow to fill available space. If two opposing sides have non-`auto` values, they will get at least the specified padding, plus half of the remaining available space each. If you want to anchor the image to the top-right of the canvas, you can specify 0,0,"auto","auto".

Values are capped at 1000 pixels.

    background = "abcdef"

Default: transparent (or white if transformed file doesn't support transparency) \
Specify a background color to use for transparent areas in the source and for any padding added.
There are two predefined options, `transparent` and `white`. Any other background color must be specified as an rgb hex value, similar to CSS but without the \# sign. Use the full 6-character rgb hex, not a CSS shortcut like bbb.

    quality = 82

Default: 100 \
Lower quality leads to smaller filesizes, but higher quality looks better. This is a compromise, use your best judgment.
Allowed values are 0 through 100.

    dpr = 2

Default: 1 \
Device pixel ratio is abbreviated dpr, and is used to indicate the number of physical pixels the device screen has per logical pixel. You always specify the resizing and padding values in logical pixels. Regular screens have a dpr of 1. High resolution or retina screens have a dpr of 2 or 3. We support a max dpr of 4, just in case. A dpr of 2 means that for a requested width of 400, you get a transformed image with 800 (physical) pixels.



### `unicat.utils`

```python
from unicat.utils import *
```


```python
def gid() -> str  # a uuid4

def maybe_gid(possible_gid: Any) -> bool

def test_true(data: Any) -> bool

def test_false(data: Any) -> bool

def make_bool(any: Any) -> bool

def make_bool_str(any: Any) -> str

def make_str(any: Any) -> str

def make_json_str(any: Any) -> str

def make_json(any: Any) -> Any

def make_int(any: Any) -> int

def make_float(any: Any) -> float

def noop(any: Any) -> Any

def make_str_list(any: Any) -> list[str]

def convert_value_to_fielddata(fieldtype: str, value: Any) -> bool | str | Any | int | float | list[str]
    """Return a value suitable for writing to Unicat, for list field types this
    means converting newline-separated entries to lists.
    For class or classlist fields, we produce a JSON data structure.

    This can raise exceptions when the value doesn't match the type, e.g. converting a
    string to a float.
    """

def convert_fielddata_to_value(fieldtype: str, fielddata: Any) -> str | int | float
    """Return a value suitable for writing in a cell, such as a text or a number.
    Lists will be flattened by stringifying each item and concatenating with \n.
    For class or classlist fields, we will have pretty-printed JSON.
    """

def merge_dicts(a: dict, b: dict) -> dict
    """Merge b into a, returning a.

    a is updated; if you don't want to mutate a, call it as `merge_dicts(dict(a), b)`.
    """

def diff_record_fields_data(unicat: Unicat, record: UnicatRecord, localizedfielddata: dict) -> dict  # dict format: d[language][fieldname] = value
    """Return a version of localizedfielddata that only has data that is different from
    the raw record data.
    """

def hash_text(text: str) -> str  # unicode ok

def hash_data(data: Any) -> str  # data must be json-serializable

class DuckObject  # quickly construct an object-like duck from a dict or kwargs, see below

class FieldColumns  # flatten a list of (class-)fields, see below
```


### DuckObject

DuckObjects are used to quickly construct an object-like duck.

Uses keyword arguments to construct any duck-like object with those attributes.

```python
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


### FieldColumns

FieldColumns are needed for class fields, that have nested subfields.

With FieldColumns, we can flatten a list of fields to a list of columns,
associated with those fields.

Each column has a fieldstack, that is a list of the field and nested subfields.
For a regular field, the fieldstack is just that field.
A classfield with three subfields will yield three columns, and each column has
a fieldstack with the classfield first, and then the subfield for that column.
If that subfield is another classfield, we'll get more columns and deeper
stackfields.

For example, you have `[image, dimensions]` as fields, and `dimensions` is of type class, and has subfields `width` and `length`; FieldColumns will give you `[image, dimensions.width, dimensions.length]`, useable for writing to tab-separated files or spreadsheets.

Most of the time, you won't need the stackfield in the client code, see also the
\_FieldColumn implementation where we get the 'name' for a column by walking the
fieldstack.

Client code can look something like this, for reading from Unicat:

```python
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

```python
recordfields_data = {}
for column in columns:
    fieldvalue = row[column.index].value
    column.update_fields_data(recordfields_data, fieldvalue)
unicat.mutate.update_record(record, {language: recordfields_data})
```
