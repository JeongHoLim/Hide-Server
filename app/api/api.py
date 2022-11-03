from fastapi import APIRouter

from .endpoints.request import router

api_router = APIRouter()
api_router.include_router(router)
