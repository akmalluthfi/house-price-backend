from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.location import Location
from sqlmodel import select

router = APIRouter(prefix="/locations", tags=["locations"])


@router.get("/", response_model=list[Location])
def index(session: SessionDep) -> list[Location]:
    results = session.exec(select(Location)).all()
    return results
