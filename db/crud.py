from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from db.models import Message  # ✅ from your db/models.py
from db.schemas import MessageCreate  # ✅ from your flat schemas.py file
from datetime import datetime

async def create_message(db: AsyncSession, msg: MessageCreate):
    db_msg = Message(
        user=msg.user,
        message=msg.message,
        timestamp=msg.timestamp or datetime.utcnow()
    )
    db.add(db_msg)
    await db.commit()
    await db.refresh(db_msg)
    return db_msg

async def get_messages(db: AsyncSession, limit: int = 10):
    result = await db.execute(
        select(Message).order_by(Message.timestamp.desc()).limit(limit)
    )
    return result.scalars().all()