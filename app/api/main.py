from fastapi import APIRouter
from app.api.routes import locations, houses

api_router = APIRouter()
api_router.include_router(locations.router)
api_router.include_router(houses.router)
