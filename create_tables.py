from sqlalchemy.ext.asyncio import create_async_engine
from db.models import Base  # 👈 import your model

DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # adjust path if needed

engine = create_async_engine(DATABASE_URL, echo=True)

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    import asyncio
    asyncio.run(init_models())