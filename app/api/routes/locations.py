from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.location import Location
from sqlmodel import select

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("/", response_model=list[Location])
def index(session: SessionDep, q: str | None = None) -> list[Location]:
    query = select(Location)

    if q:
        query = query.where(Location.district.ilike(f"%{q}%"))

    results = session.exec(query).all()
    return results
