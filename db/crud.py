from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from db.models import Message, GitHubIssue  # ✅ from your db/models.py
from db.schemas import MessageCreate, GitHubIssueCreate  # ✅ from your flat schemas.py file
from datetime import datetime, timezone
from typing import Optional, List

async def create_message(db: AsyncSession, msg: MessageCreate):
    db_msg = Message(
        user=msg.user,
        message=msg.message,
        timestamp=msg.timestamp or datetime.now(timezone.utc)
    )
    db.add(db_msg)
    await db.commit()
    await db.refresh(db_msg)
    return db_msg

async def get_messages(
    db: AsyncSession,
    user: Optional[str] = None,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 10
) -> List[Message]:
    query = select(Message)

    if user:
        query = query.where(Message.user == user)
    
    if search:
        query = query.where(Message.message.ilike(f"%{search}%"))

    query = query.order_by(Message.timestamp.desc()).offset(skip).limit(limit)
    
    result = await db.execute(query)
    return result.scalars().all()

# function to get the total count of filtered messages

async def count_messages(
    db: AsyncSession,
    user: Optional[str] = None,
    search: Optional[str] = None
) -> int:
    query = select(func.count()).select_from(Message)

    if user:
        query = query.where(Message.user == user)
    
    if search:
        query = query.where(Message.message.ilike(f"%{search}%"))

    result = await db.execute(query)
    return result.scalar()

async def create_github_issue(db: AsyncSession, issue: GitHubIssueCreate):
    db_issue = GitHubIssue(
        title=issue.title,
        description=issue.description,
        user=issue.user,
        created_at=issue.created_at or datetime.now(timezone.utc)
    )
    db.add(db_issue)
    await db.commit()
    await db.refresh(db_issue)
    return db_issue

async def get_github_issues(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(GitHubIssue).order_by(GitHubIssue.created_at.desc()).offset(skip).limit(limit)
    )
    return result.scalars().all()