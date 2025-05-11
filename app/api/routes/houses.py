from typing import Any
from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.house import House, PaginatedHouseResponse
from sqlmodel import select
from sqlalchemy import func

router = APIRouter(prefix="/houses", tags=["houses"])


@router.get("/", response_model=PaginatedHouseResponse)
def index(session: SessionDep, page: int = 1) -> Any:
    limit = 10
    offset = (page - 1) * limit

    query = select(House).offset(offset).limit(limit)
    results = session.exec(query).all()

    total = session.exec(select(func.count()).select_from(House)).one()
    total_pages = (total + limit - 1) // limit

    return PaginatedHouseResponse(
        data=results,
        page=page,
        per_page=limit,
        total=total,
        total_pages=total_pages,
        has_next=page < total_pages,
        has_prev=page > 1,
    )
