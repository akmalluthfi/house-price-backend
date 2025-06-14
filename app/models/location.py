from typing import TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from pydantic import BaseModel

if TYPE_CHECKING:
    from .house import House


class Location(SQLModel, table=True):
    __tablename__: str = "locations"

    id: int | None = Field(default=None, primary_key=True)
    district: str

    houses: list["House"] = Relationship(back_populates="location")


class LocationResponse(BaseModel):
    id: int | None = None
    district: str
