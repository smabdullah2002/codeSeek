from fastapi import APIRouter
from routes import ingest, search, health

api_router = APIRouter()

api_router.include_router(health.router, prefix="", tags=["health"])
api_router.include_router(ingest.router, prefix="", tags=["ingest"])
api_router.include_router(search.router, prefix="", tags=["search"])
