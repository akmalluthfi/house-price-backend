from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.house import House, PaginatedHouseResponse, HouseRequest, HouseResponse
from app.models.location import Location
from sqlmodel import select
from sqlalchemy import func
from app.core.model_loader import model_pipeline


router = APIRouter(prefix="/houses", tags=["houses"])


@router.get("/", response_model=PaginatedHouseResponse)
def index(session: SessionDep, page: int = 1) -> PaginatedHouseResponse:
    limit = 15
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


@router.post("/predict", response_model=HouseResponse)
def predict(request: HouseRequest, session: SessionDep) -> HouseResponse:
    location = session.get(Location, request.location_id)
    request.location_id = location.district

    features = [request.model_dump(by_alias=True)]
    pred = model_pipeline.predict(features)

    return HouseResponse(
        **request.model_dump(exclude=["location_id"]),
        location=location.model_dump(),
        price=pred[0]
    )
