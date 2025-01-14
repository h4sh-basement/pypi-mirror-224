from ..definition import UnicatDefinition
from ..error import UnicatError


def create_definition(
    unicat,
    *,
    name=None,
    label=None,
    classes=None,
    fields=None,
    titlefield=None,
    childdefinitions=None,
    **kwargs,
):
    properties = {**kwargs}
    if name is not None:
        properties["name"] = name
    if label is not None and type(label) is dict:
        properties["label"] = label
    if classes is not None and type(classes) is not str:
        properties["classes"] = [
            class_.gid if hasattr(class_, "gid") else class_ for class_ in classes
        ]
    if fields is not None and type(fields) is not str:
        properties["fields"] = [
            field.gid if hasattr(field, "gid") else field for field in fields
        ]
    if titlefield is not None:
        properties["titlefield"] = (
            titlefield.gid if hasattr(titlefield, "gid") else titlefield
        )
    if childdefinitions is not None and type(childdefinitions) is not str:
        properties["childdefinitions"] = [
            childdefinition.gid if hasattr(childdefinition, "gid") else childdefinition
            for childdefinition in childdefinitions
        ]
    success, result = unicat.api.call("/definitions/create", properties)
    if not success:
        raise UnicatError("create_definition", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition(
    unicat,
    definition,
    *,
    name=None,
    label=None,
    classes=None,
    fields=None,
    titlefield=None,
    childdefinitions=None,
    **kwargs,
):
    properties = {**kwargs}
    if name is not None:
        properties["name"] = name
    if label is not None and type(label) is dict:
        properties["label"] = label
    if classes is not None and type(classes) is not str:
        properties["classes"] = [
            class_.gid if hasattr(class_, "gid") else class_ for class_ in classes
        ]
    if fields is not None and type(fields) is not str:
        properties["fields"] = [
            field.gid if hasattr(field, "gid") else field for field in fields
        ]
    if titlefield is not None:
        properties["titlefield"] = (
            titlefield.gid if hasattr(titlefield, "gid") else titlefield
        )
    if childdefinitions is not None and type(childdefinitions) is not str:
        properties["childdefinitions"] = [
            childdefinition.gid if hasattr(childdefinition, "gid") else childdefinition
            for childdefinition in childdefinitions
        ]
    properties["definition"] = definition.gid
    success, result = unicat.api.call("/definitions/modify", properties)
    if not success:
        raise UnicatError("modify_definition", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_modify_layout(
    unicat,
    definition,
    *,
    name=None,
    root=None,
    components=None,
):
    layout_properties = {}
    if name is not None:
        layout_properties["name"] = name
    if root is not None:
        layout_properties["root"] = root
    if components is not None and type(components) is dict:
        layout_properties["components"] = components
    success, result = unicat.api.call(
        "/definitions/layouts/modify",
        {**layout_properties, "definition": definition.gid},
    )
    if not success:
        raise UnicatError("modify_definition_modify_layout", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_add_class(unicat, definition, class_):
    success, result = unicat.api.call(
        "/definitions/classes/add",
        {"definition": definition.gid, "class": class_.gid},
    )
    if not success:
        raise UnicatError("modify_definition_add_class", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_remove_class(unicat, definition, class_):
    success, result = unicat.api.call(
        "/definitions/classes/remove",
        {"definition": definition.gid, "class": class_.gid},
    )
    if not success:
        raise UnicatError("modify_definition_remove_class", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_add_field(unicat, definition, field):
    success, result = unicat.api.call(
        "/definitions/fields/add",
        {"definition": definition.gid, "field": field.gid},
    )
    if not success:
        raise UnicatError("modify_definition_add_field", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_remove_field(unicat, definition, field):
    success, result = unicat.api.call(
        "/definitions/fields/remove",
        {"definition": definition.gid, "field": field.gid},
    )
    if not success:
        raise UnicatError("modify_definition_remove_field", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_fieldlist_add_field(unicat, definition, fieldlist_key, field):
    success, result = unicat.api.call(
        "/definitions/fieldlists/fields/add",
        {
            "definition": definition.gid,
            "fieldlist_key": fieldlist_key,
            "field": field.gid,
        },
    )
    if not success:
        raise UnicatError("modify_definition_fieldlist_add_field", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_fieldlist_remove_field(unicat, definition, fieldlist_key, field):
    success, result = unicat.api.call(
        "/definitions/fieldlists/fields/remove",
        {
            "definition": definition.gid,
            "fieldlist_key": fieldlist_key,
            "field": field.gid,
        },
    )
    if not success:
        raise UnicatError("modify_definition_fieldlist_remove_field", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_add_childdefinition(unicat, definition, childdefinition):
    success, result = unicat.api.call(
        "/definitions/childdefinitions/add",
        {"definition": definition.gid, "childdefinition": childdefinition.gid},
    )
    if not success:
        raise UnicatError("modify_definition_add_childdefinition", result)
    return UnicatDefinition(unicat, result["definition"])


def modify_definition_remove_childdefinition(unicat, definition, childdefinition):
    success, result = unicat.api.call(
        "/definitions/childdefinitions/remove",
        {"definition": definition.gid, "childdefinition": childdefinition.gid},
    )
    if not success:
        raise UnicatError("modify_definition_remove_childdefinition", result)
    return UnicatDefinition(unicat, result["definition"])


def commit_definition(unicat, new_or_working_copy):
    success, result = unicat.api.call(
        "/definitions/commit", {"definition": new_or_working_copy.gid}
    )
    if not success:
        raise UnicatError("commit_definition", result)
    if (
        result["definition"] != new_or_working_copy.gid
        and new_or_working_copy.gid in unicat.api.data["definitions"]
    ):
        del unicat.api.data["definitions"][new_or_working_copy.gid]
    return UnicatDefinition(unicat, result["definition"])


def save_as_new_definition(unicat, working_copy):
    success, result = unicat.api.call(
        "/definitions/save_as_new", {"definition": working_copy.gid}
    )
    if not success:
        raise UnicatError("save_as_new_definition", result)
    return UnicatDefinition(unicat, result["definition"])


def delete_definition(unicat, definition):
    success, result = unicat.api.call(
        "/definitions/delete", {"definition": definition.gid}
    )
    if not success:
        raise UnicatError("delete_definition", result)
    if definition.gid in unicat.api.data["definitions"]:
        del unicat.api.data["definitions"][definition.gid]
    return True
