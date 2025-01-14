# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:34:03+00:00

from __future__ import annotations

import uuid
import datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Extra, Field, constr


class FromItem(BaseModel):
    class Config:
        extra = Extra.forbid

    type: str
    filter: list | None = None
    automatically_accept: bool | None = None


class Application(BaseModel):
    class Config:
        extra = Extra.forbid

    sharing: bool | None = None
    permitted: list[uuid.UUID] | None = None


class Method(BaseModel):
    create: bool | None = None
    update: bool | None = None
    retrieve: bool | None = None
    delete: bool | None = None


class State(BaseModel):
    class Config:
        extra = Extra.forbid

    min_state: float | None = None
    max_state: float | None = None


class Installation(BaseModel):
    class Config:
        extra = Extra.forbid

    shareable: bool | None = None


class File(BaseModel):
    background: bool | None = None


class AclAttribute(Enum):
    parent_name = 'parent_name'


class Restriction(BaseModel):
    class Config:
        extra = Extra.forbid

    child: str | None = None
    create: list[str] | None = None
    application:  Application | None = None
    method:  Method | None = None
    time: dict[str, Any] | None = None
    state:  State | None = None
    installation:  Installation | None = None
    file:  File | None = None
    acl_attributes: list[AclAttribute] | None = None


class ToItem(BaseModel):
    class Config:
        extra = Extra.forbid

    type: str
    filter: list | None = None
    restriction: Restriction | None = None


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


class PermissionRule(BaseModel):
    class Config:
        extra = Extra.forbid

    apply_to_old: bool | None = None
    from_: list[FromItem] = Field(..., alias='from')
    to: list[ToItem]
    meta: Meta = Field(..., title='meta-2.1')
