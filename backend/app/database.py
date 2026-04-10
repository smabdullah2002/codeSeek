import asyncpg
from config import settings


class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        self.pool = await asyncpg.create_pool(
            settings.SUPABASE_DIRECT_STRING, min_size=1, max_size=10
        )

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def fetchval(self, query: str):
        async with self.pool.acquire() as connection:
            return await connection.fetchval(query)


db = Database()
