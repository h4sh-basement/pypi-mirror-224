# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:28:46+00:00

from __future__ import annotations

import uuid
from enum import Enum

from pydantic import BaseModel, Extra, conint, constr


class NetworkItem(BaseModel):
    class Config:
        extra = Extra.allow

    id: list[uuid.UUID] | uuid.UUID | None = None


class FactoryResetItem(BaseModel):
    class Config:
        extra = Extra.forbid

    reset_manufacturer: bool | None = None
    reset_owner: bool | None = None


class BillHistoricalEnum(Enum):
    owner = 'owner'
    manufacturer = 'manufacturer'
    creator_manufacturer = 'creator_manufacturer'


class PointEnum(Enum):
    dynamic = 'dynamic'


class DailyLimitItem(BaseModel):
    class Config:
        extra = Extra.forbid

    point: conint(ge=0) | PointEnum | None = None
    iot_traffic: conint(ge=0) | None = None
    request: conint(ge=0) | None = None
    request_time: conint(ge=0) | None = None


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


class Creator(BaseModel):
    class Config:
        extra = Extra.allow

    network:  NetworkItem | None = None
    quantity: conint(ge=1) | None = None
    manufacturer_as_owner: bool | None = None
    factory_reset:  FactoryResetItem | None = None
    test_mode: bool | None = None
    product: str | None = None
    bill_owner: bool | None = None
    bill_user: uuid.UUID | constr(
        regex=r'(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    ) | None = None
    bill_historical: BillHistoricalEnum | uuid.UUID | constr(
        regex=r'(?:[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&\'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'
    ) | None = None
    daily_limit:  DailyLimitItem | None = None
    kickoff: bool | None = None
    meta:  MetaItem | None = None
