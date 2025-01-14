# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:37:10+00:00

from __future__ import annotations

import uuid
from enum import Enum
from pydantic import BaseModel, Extra, Field, conint, constr


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


class Type(Enum):
    private = 'private'
    public = 'public'
    enterprise = 'enterprise'


class MaxNumberNetworkEnum(Enum):
    unlimited = 'unlimited'


class BasePointEnum(Enum):
    unlimited = 'unlimited'


class BaseSm(Enum):
    unlimited = 'unlimited'


class Interval(Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'
    never = 'never'


class RecurringPoint(BaseModel):
    class Config:
        extra = Extra.forbid

    interval: Interval
    interval_count: conint(ge=1)


class Interval1(Enum):
    day = 'day'
    week = 'week'
    month = 'month'
    year = 'year'


class Recurring(BaseModel):
    class Config:
        extra = Extra.forbid

    interval: Interval1
    interval_count: conint(ge=1)


class Tax(BaseModel):
    class Config:
        extra = Extra.allow

    id: uuid.UUID | None = None


class PriceItem(BaseModel):
    class Config:
        extra = Extra.allow

    meta: Meta | None = Field(None, title='meta-2.1')
    name: str | None = None
    unchangeable: bool | None = None
    active: bool | None = None
    free: bool | None = None
    currency: str | None = None
    amount: int | None = None
    prepaid_extra_cost: int | None = None
    topup_extra_cost: int | None = None
    recurring: Recurring | None = None
    tax: Tax | None = None


class Subscription(BaseModel):
    class Config:
        extra = Extra.allow

    meta: Meta | None = Field(None, title='meta-2.1')
    unit_label: constr(min_length=2, max_length=12) | None = None
    description: str | None = None
    name: str
    active: bool | None = None
    free: bool
    change_immediately: bool | None = None
    images: list[str] | None = None
    type: Type
    user: list | None = None
    max_number_network: MaxNumberNetworkEnum | conint(ge=0)
    extra_network: conint(ge=0) | None = None
    base_point: BasePointEnum | conint(ge=0)
    prepaid_point: conint(ge=0) | None = None
    topup_point: conint(ge=0) | None = None
    base_sms: BaseSm | conint(ge=0) | None = None
    prepaid_sms: conint(ge=0) | None = None
    topup_sms: conint(ge=0) | None = None
    recurring_point: RecurringPoint | None = None
    price: list[PriceItem | uuid.UUID] | None = None
