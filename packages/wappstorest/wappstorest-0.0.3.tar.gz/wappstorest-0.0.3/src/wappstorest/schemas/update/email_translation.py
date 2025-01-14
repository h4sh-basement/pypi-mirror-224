# generated by datamodel-codegen:
#   filename:  <stdin>
#   timestamp: 2023-02-17T08:30:12+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Extra, constr


class MetaItem(BaseModel):
    class Config:
        extra = Extra.allow

    id: str | None = None
    trace: str | None = None
    redirect: constr(regex=r'^[0-9a-zA-Z_-]+$', min_length=1, max_length=200) | None = None
    icon: str | None = None
    tag: list[constr(min_length=2, max_length=20)] | None = None
    tag_by_user: list[constr(min_length=2, max_length=20)] | None = None
    name_by_user: constr(max_length=100) | None = None


class EmailTranslation(BaseModel):
    class Config:
        extra = Extra.allow

    language: constr(regex=r'^[0-9a-zA-Z/-]{1,20}$') | None = None
    translation: dict[str, Any] | None = None
    meta:  MetaItem | None = None
    name: str | None = None
    publish: bool | None = None
