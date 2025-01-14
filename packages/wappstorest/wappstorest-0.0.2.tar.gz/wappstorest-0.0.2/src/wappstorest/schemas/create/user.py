# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:37:44+00:00

from __future__ import annotations

import uuid
import datetime
from enum import Enum

from pydantic import BaseModel, Extra, Field, constr


class ProviderItem(BaseModel):
    class Config:
        extra = Extra.forbid

    name: str
    picture: str | None = None
    type: str


class PublicEnum(Enum):
    nickname = 'nickname'
    first_name = 'first_name'
    last_name = 'last_name'
    email = 'email'
    phone = 'phone'
    role = 'role'


class Status(Enum):
    pending = 'pending'
    refused = 'refused'
    accepted = 'accepted'
    send = 'send'
    not_sent = 'not_sent'
    archive = 'archive'


class OtherEmailItem(BaseModel):
    contact: constr(regex=r'^\S+@\S+\.\S+$') | None = None
    status: Status | None = None
    last_update: datetime.datetime | None = None


class OtherSm(BaseModel):
    contact: str | None = None
    status: Status | None = None
    last_update: datetime.datetime | None = None


class Type(Enum):
    soft = 'soft'
    strong = 'strong'


class Ban(BaseModel):
    type: Type
    begin_ban: datetime.datetime | None = None
    end_ban: datetime.datetime
    motivation: str


class Meta(BaseModel):
    class Config:
        extra = Extra.allow

    id: uuid.UUID | None = None
    trace: str | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None


class User(BaseModel):
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
    friend: bool | None = None
    blocked: bool | None = None
    provider: list[ProviderItem] | None = None
    public: list[PublicEnum] | None = None
    verified_email: bool | None = None
    verified_sms: bool | None = None
    other_email: list[OtherEmailItem] | None = None
    other_sms: list[OtherSm] | None = None
    admin: bool | None = None
    founder: bool | None = None
    ban: Ban | None = None
    meta: Meta | None = Field(None, title='meta-2.1')
