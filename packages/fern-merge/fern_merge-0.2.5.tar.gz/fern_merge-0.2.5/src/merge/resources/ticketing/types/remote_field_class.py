# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .field_format_enum import FieldFormatEnum
from .field_type_enum import FieldTypeEnum
from .item_schema import ItemSchema


class RemoteFieldClass(pydantic.BaseModel):
    id: typing.Optional[str]
    display_name: typing.Optional[str]
    remote_key_name: typing.Optional[str]
    description: typing.Optional[str]
    is_custom: typing.Optional[bool]
    is_required: typing.Optional[bool]
    field_type: typing.Optional[FieldTypeEnum]
    field_format: typing.Optional[FieldFormatEnum]
    field_choices: typing.Optional[typing.List[str]]
    item_schema: typing.Optional[ItemSchema]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
