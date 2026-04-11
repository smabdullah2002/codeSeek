import json

from database import db


def _to_pgvector_literal(values):
    # pgvector accepts text input in the format: [0.1,0.2,...]
    return "[" + ",".join(str(float(v)) for v in values) + "]"


async def insert_chunks(chunks, embeddings):
    query = """
    INSERT INTO code_chunks 
    (file_path, chunk_id, chunk_type, name, content, embedding, metadata)
    VALUES ($1, $2, $3, $4, $5, $6::vector, $7::jsonb)
    """
    
    async with db.pool.acquire() as connection:
        for chunk, embedding in zip(chunks, embeddings):
            await connection.execute(
                query,
                chunk["file_path"],
                chunk["chunk_id"],
                chunk["chunk_type"],
                chunk["name"],
                chunk["content"],
                _to_pgvector_literal(embedding),
                json.dumps(chunk["metadata"]),
            )

            