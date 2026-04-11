from fastapi import APIRouter
from routes import health
from routes import ingest

api_router = APIRouter()

api_router.include_router(health.router, prefix="", tags=["health"])
api_router.include_router(ingest.router, prefix="", tags=["ingest"])