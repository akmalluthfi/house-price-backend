from fastapi import APIRouter
from app.core.db import SessionDep
from app.models.house import House, PaginatedHouseResponse, HouseRequest, HouseResponse
from app.models.location import Location
from sqlmodel import select
from sqlalchemy import func
from app.core.model_loader import model, enc, scaler


router = APIRouter(prefix="/houses", tags=["houses"])


@router.get("/", response_model=PaginatedHouseResponse)
def index(session: SessionDep, page: int = 1) -> PaginatedHouseResponse:
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


@router.post("/predict", response_model=HouseResponse)
def index(request: HouseRequest, session: SessionDep) -> HouseResponse:
    location = session.get(Location, request.location_id)
    request.location_id = enc[location.district]

    features = [list(request.model_dump(by_alias=True).values())]
    X_scaled = scaler.transform(features)

    pred = model.predict(X_scaled)

    return HouseResponse(
        **request.model_dump(exclude=["location_id"]),
        location=location.model_dump(),
        price=pred[0]
    )
