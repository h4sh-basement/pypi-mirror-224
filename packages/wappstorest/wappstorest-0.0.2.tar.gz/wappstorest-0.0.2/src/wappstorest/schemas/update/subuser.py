# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:37:16+00:00

from __future__ import annotations

import uuid
from enum import Enum

from pydantic import BaseModel, Extra, conint, constr


class MetaItem(BaseModel):
    class Config:
        extra = Extra.allow

    id: uuid.UUID | None = None
    trace: str | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None


class UserDailyLimitItem(BaseModel):
    class Config:
        extra = Extra.forbid

    point: conint(ge=0) | None = None
    document: conint(ge=0) | None = None
    log_row: conint(ge=0) | None = None
    traffic: conint(ge=0) | None = None
    iot_traffic: conint(ge=0) | None = None
    stream_traffic: conint(ge=0) | None = None
    file: conint(ge=0) | None = None
    request: conint(ge=0) | None = None
    request_time: conint(ge=0) | None = None


class NetworkDailyLimitItem(BaseModel):
    class Config:
        extra = Extra.forbid

    point: conint(ge=0) | None = None
    iot_traffic: conint(ge=0) | None = None
    request: conint(ge=0) | None = None
    request_time: conint(ge=0) | None = None


class DynamicLimitEnum(Enum):
    dynamic = 'dynamic'


class DynamicLimit(BaseModel):
    __root__: conint(ge=0) | DynamicLimitEnum


class PointManagementItem(BaseModel):
    base_point: DynamicLimit | None = None
    base_network: DynamicLimit | None = None
    user_daily_limit:  UserDailyLimitItem | None = None
    network_daily_limit:  NetworkDailyLimitItem | None = None


class Subuser(BaseModel):
    class Config:
        extra = Extra.allow

    first_name: str | None = None
    last_name: str | None = None
    email: constr(regex=r'^\S+@\S+\.\S+$') | None = None
    phone: str | None = None
    name: str | None = None
    role: str | None = None
    nickname: str | None = None
    language: str | None = None
    login_username: constr(regex=r'^[0-9a-zA-Z_.]{1,40}$') | None = None
    login_password: str | None = None
    meta:  MetaItem | None = None
    point_management:  PointManagementItem | None = None
