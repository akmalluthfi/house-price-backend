from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.location import Location, LocationResponse
from sqlmodel import select

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("", response_model=list[LocationResponse])
def index(
    session: SessionDep, q: str | None = None, limit: int = 10
) -> list[LocationResponse]:
    query = select(Location)

    if q:
        query = query.where(Location.district.ilike(f"%{q}%"))

    results = session.exec(query.limit(limit)).all()
    return results
