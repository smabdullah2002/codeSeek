from fastapi import APIRouter
from pydantic import BaseModel


from core.chunker import chunk_code
from db.queries import insert_chunks
from core.embedding import embed_texts

router = APIRouter()

class CodeInput(BaseModel):
    file_path: str
    content: str


@router.post("/ingest")
async def ingest_code(data: CodeInput):
    # 1. chunk
    chunks = chunk_code(data.content, data.file_path)

    # 2. embeddings
    texts = [c["content"] for c in chunks]
   
    embeddings = embed_texts(texts)

    # 3. store
    await insert_chunks(chunks, embeddings)

    return {"chunks_inserted": len(chunks)}