from typing import Any, TypeVar

from pydantic import BaseModel
from pydantic.fields import Field

Model = TypeVar("Model", bound="BaseModel")


class Entity(BaseModel):
    identifier: Any
    blueprint: Any
    title: Any
    team: str | None | list[Any] = []
    properties: dict[str, Any] = {}
    relations: dict[str, Any] = {}


class BlueprintRelation(BaseModel):
    many: bool
    required: bool
    target: str
    title: str | None


class Blueprint(BaseModel):
    identifier: str
    title: str | None
    team: str | None
    properties_schema: dict[str, Any] = Field(alias="schema")
    relations: dict[str, BlueprintRelation]
