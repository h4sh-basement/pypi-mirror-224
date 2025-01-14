# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:26:36+00:00

from __future__ import annotations

import uuid
from enum import Enum
from typing import Any

from pydantic import BaseModel, Extra, Field, constr


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


class RestrictionItem(BaseModel):
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


class IdEnum(Enum):
    global_ = 'global'
    parent_owner = 'parent_owner'
    parent_manufacturer = 'parent_manufacturer'


class Meta(BaseModel):
    class Config:
        extra = Extra.allow

    id: uuid.UUID | constr(
        regex=r'(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    ) | IdEnum | None = None
    trace: str | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None


class PermissionItem(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str | None = None
    message: str | None = None
    propagate: bool | None = None
    restriction: list[RestrictionItem] | None = None
    meta: Meta | None = Field(None, title='meta-2.1')


class Meta1(BaseModel):
    class Config:
        extra = Extra.allow

    id: uuid.UUID | None = None
    trace: str | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None


class Acl(BaseModel):
    class Config:
        extra = Extra.allow

    owner: str | None = None
    manufacturer: uuid.UUID | None = None
    permission: list[PermissionItem | str] | None = None
    meta: Meta1 | None = Field(None, title='meta-2.1')
