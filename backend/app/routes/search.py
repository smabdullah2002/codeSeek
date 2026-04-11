from fastapi import APIRouter
from pydantic import BaseModel

from core.embedding import embed_query
from db.search import search_similar_chunks

router = APIRouter()

class SearchQuery(BaseModel):
    query: str
    top_k: int = 5
    

@router.post("/search")
async def search(data: SearchQuery):
    # 1. embed query
    query_embedding = embed_query(data.query)

    # 2. search DB
    results = await search_similar_chunks(query_embedding, top_k=data.top_k)

    return {"results": results}