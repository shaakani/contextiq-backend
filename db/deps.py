
from db.database import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession
from typing import AsyncGenerator

# This explicitly tells FastAPI (and linters) that this is an async generator yielding a session.

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session