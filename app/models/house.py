from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
from pydantic import BaseModel


if TYPE_CHECKING:
    from .location import Location


class House(SQLModel, table=True):
    __tablename__: str = "houses"

    id: int | None = Field(default=None, primary_key=True)
    price: int
    bedroom: int
    bathroom: int
    land_area: int
    building_area: int
    carport: int

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
