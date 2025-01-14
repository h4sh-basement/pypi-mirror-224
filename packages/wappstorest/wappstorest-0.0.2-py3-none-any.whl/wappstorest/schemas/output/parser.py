# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:33:46+00:00

from __future__ import annotations

import uuid
import datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Extra, Field, constr


class Assigned(Enum):
    unassigned = 'unassigned'
    admin = 'admin'


class WarningItem(BaseModel):
    message: str | None = None
    data: dict[str, Any] | None = None
    code: int | None = None


class Meta(BaseModel):
    class Config:
        extra = Extra.forbid

    id: uuid.UUID | None = None
    type: str | None = None
    version: constr(regex=r'(\d+)\.(\d+)') | None = None
    manufacturer: uuid.UUID | Assigned | None = None
    owner: uuid.UUID | Assigned | None = None
    created: datetime.datetime | Literal['not_available'] | None = None
    updated: datetime.datetime | Literal['not_available'] | None = None
    changed: datetime.datetime | Literal['not_available'] | None = None
    application: uuid.UUID | None = None
    revision: int | None = None
    trace: str | None = None
    oem: str | None = None
    deprecated: bool | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    size: int | None = None
    path: str | None = None
    parent: uuid.UUID | None = None
    error: dict[str, Any] | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None
    warning: list[WarningItem] | None = None
    parent_name: dict[str, Any] | None = None
    read_only: bool | None = None
    original_id: uuid.UUID | None = None
    alert: list[uuid.UUID] | None = None
    contract: list[uuid.UUID] | None = None


class Operation(Enum):
    table = 'table'
    message = 'message'


class Message(BaseModel):
    false_message: str | None = None
    true_message: str


class Version(Enum):
    field_2_1 = '2.1'
    field_2_1_1 = '2.1'


class Condition(Enum):
    lessThan = 'lessThan'
    field_ = '<'
    lessOrEqualThan = 'lessOrEqualThan'
    field__ = '<='
    moreThan = 'moreThan'
    field__1 = '>'
    moreOrEqualThan = 'moreOrEqualThan'
    field___1 = '>='
    equal = 'equal'
    field___2 = '=='
    different = 'different'
    field___3 = '!='
    contains = 'contains'
    field__2 = '='
    always = 'always'
    default = 'default'


class Color(BaseModel):
    condition:  Condition | None = None
    value: str | None = None
    conditionValue: str | None = None


class Column(BaseModel):
    data: str | None = None
    title: str | None = None
    colors: list[Color] | None = None


class Table(BaseModel):
    class Config:
        extra = Extra.forbid

    service: str
    version:  Version | None = None
    parser: str | None = None
    columns: list[Column] | None = None


class Example(BaseModel):
    success: bool | None = None
    input: Any | None = None
    output: Any | None = None


class Parser(BaseModel):
    class Config:
        extra = Extra.forbid

    meta: Meta = Field(..., title='meta-2.1')
    name: str | None = None
    operation: Operation
    message:  Message | None = None
    table:  Table | None = None
    example:  Example | None = None
    to_parse: Any | None = None
