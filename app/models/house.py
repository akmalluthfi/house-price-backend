from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
from pydantic import BaseModel, Field as ModelField
from .location import LocationResponse

if TYPE_CHECKING:
    from .location import Location


class House(SQLModel, table=True):
    __tablename__: str = "houses"

    id: int | None = Field(default=None, primary_key=True)
    price: float
    bedroom: int
    bathroom: int
    land_area: int
    building_area: int

    location_id: int = Field(foreign_key="locations.id")
    location: Optional["Location"] = Relationship(back_populates="houses")


class PaginatedHouseResponse(BaseModel):
    data: list[House]
    page: int
    per_page: int
    total: int
    total_pages: int
    has_next: bool
    has_prev: bool


class HouseRequest(BaseModel):
    bedroom: int = ModelField(ge=0)
    bathroom: int = ModelField(ge=0)
    land_area: int = ModelField(ge=15)
    building_area: int = ModelField(ge=15)
    location_id: int | str = ModelField(ge=0, serialization_alias="location")


class HouseResponse(BaseModel):
    price: float
    bedroom: int
    bathroom: int
    land_area: int
    building_area: int
    location: LocationResponse | None = None
