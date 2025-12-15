from fastapi import APIRouter

from src.api.items import routes as items_routes
from src.api.numbers import routes as numbers_routes

v1_routes: APIRouter = APIRouter(prefix="/v1")

v1_routes.include_router(numbers_routes)
v1_routes.include_router(items_routes)
__all__ = ("v1_routes",)
