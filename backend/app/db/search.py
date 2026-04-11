from database import db


def _to_pgvector_literal(values):
    return "[" + ",".join(str(float(v)) for v in values) + "]"


async def search_similar_chunks(query_embedding, top_k=5):
    query = """
    SELECT file_path, content, chunk_type, name,
           1 - (embedding <=> $1::vector) AS similarity
    FROM code_chunks
    ORDER BY embedding <=> $1::vector
    LIMIT $2;
    """
    
    async with db.pool.acquire() as connection:
        result = await connection.fetch(
            query,
            _to_pgvector_literal(query_embedding),
            top_k,
        )
    return [dict(r) for r in result]