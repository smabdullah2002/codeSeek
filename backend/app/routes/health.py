from fastapi import APIRouter
from database import db

router = APIRouter()


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/db-health")
async def db_health():
    try:
        await db.fetchval("SELECT 1")
        return {"status": "ok"}
    except Exception as e:
        return {"status": "error", "details": str(e)}
