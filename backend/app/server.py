from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import db
from base import api_router

app = FastAPI(
    title="codeSeek Backend API",
    version="1.0.0",
    description="API for codeSeek application",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.close()


app.include_router(api_router)
