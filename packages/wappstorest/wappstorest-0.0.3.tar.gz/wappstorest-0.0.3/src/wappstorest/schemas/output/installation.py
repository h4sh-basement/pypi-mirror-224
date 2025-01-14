# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:32:05+00:00

from __future__ import annotations

import uuid
import datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Extra, Field, constr


class Background(Enum):
    no_background = 'no_background'
    pending = 'pending'
    not_paid = 'not_paid'
    running = 'running'
    crashed = 'crashed'
    restarting = 'restarting'
    error = 'error'
    failed = 'failed'
    stopped = 'stopped'
    completed = 'completed'
    no_more_points = 'no_more_points'
    not_started = 'not_started'


class Version(Enum):
    uninstalled = 'uninstalled'
    not_updated = 'not updated'
    disabled = 'disabled'
    updated = 'updated'
    editor = 'editor'


class Payment(Enum):
    free = 'free'
    owned = 'owned'
    pending = 'pending'
    paid = 'paid'
    not_paid = 'not_paid'


class Status(BaseModel):
    class Config:
        extra = Extra.forbid

    background:  Background | None = None
    version:  Version | None = None
    payment:  Payment | None = None


class Description(BaseModel):
    class Config:
        extra = Extra.forbid

    general: str | None = None
    foreground: str | None = None
    background: str | None = None
    widget: str | None = None
    version: str | None = None


class Payment1(BaseModel):
    free: bool | None = None
    status: str | None = None
    application_product_id: uuid.UUID | None = None
    created: datetime.datetime | None = None
    current_period_end: datetime.datetime | None = None
    current_period_start: datetime.datetime | None = None
    pending: dict[str, Any] | None = None


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


class Meta1(BaseModel):
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


class OauthItem(BaseModel):
    class Config:
        extra = Extra.forbid

    client_id: uuid.UUID
    name: str | None = None
    expires: bool | None = None
    expired: bool
    active: bool
    installation_id: uuid.UUID
    meta: Meta1 = Field(..., title='meta-2.1')


class Meta2(BaseModel):
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


class OauthConnectItem(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str | None = None
    api: uuid.UUID
    installation: uuid.UUID
    token: str
    secret_token: str | None = None
    params: dict[str, Any] | None = None
    meta: Meta2 = Field(..., title='meta-2.1')
    access_token_creation: dict[str, Any] | None = None


class Installation(BaseModel):
    class Config:
        extra = Extra.forbid

    application: uuid.UUID
    version_id: uuid.UUID
    title: str | None = None
    name: str | None = None
    author: str | None = None
    supported_features: list[str]
    version_app: constr(regex=r'\d+(\.\d+)*') | None = None
    session_user: bool
    native: bool | None = None
    name_folder: str | None = None
    icon: uuid.UUID | None = None
    uninstallable: bool | None = None
    upgrade: bool | None = None
    ignore_this_notification: list[str] | None = None
    token_installation: str
    extsync: bool
    permit_to_send_email: bool | None = None
    permit_to_send_sms: bool | None = None
    no_start_background: bool | None = None
    session: uuid.UUID | None = None
    status: Status
    description: Description | None = None
    payment: Payment1
    meta: Meta = Field(..., title='meta-2.1')
    oauth: list[OauthItem | uuid.UUID]
    oauth_connect: list[OauthConnectItem | uuid.UUID]
