# FastAPI entrypoint with comments and synthetic data API

from fastapi import FastAPI, Depends, Query
from synthetic_data.messages import generate_synthetic_messages
from synthetic_data.github_issues import generate_synthetic_github_issues
from synthetic_data.code_snippets import generate_synthetic_code_snippets
from synthetic_data.doc_summary import generate_synthetic_doc_summary
from synthetic_data.tasks import generate_synthetic_tasks

from db.deps import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from db.crud import create_message, get_messages, count_messages, create_github_issue, get_github_issues
from db.schemas import MessageCreate, MessageRead, GitHubIssueCreate, GitHubIssueRead
from db.models import Message
from typing import List, Optional
from datetime import datetime

app = FastAPI(title="ContextIQ Backend API")

@app.get("/")
def read_root():
    return {"message": "Welcome to ContextIQ backend!"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

@app.get("/synthetic/messages")
def get_synthetic_messages(count: int = 10):
    return {"messages": generate_synthetic_messages(num_messages=count)}

@app.get("/synthetic/github-issues")
def get_synthetic_github_issues(count: int = 5):
    return {"issues": generate_synthetic_github_issues(num_issues=count)}

@app.get("/synthetic/code-snippets")
def get_code_snippets(count: int = 5):
    return {"snippets": generate_synthetic_code_snippets(num_snippets=count)}

@app.get("/synthetic/doc-summary")
def get_doc_summary(count: int = 5):
    return {"documents": generate_synthetic_doc_summary(count=count)}

@app.get("/synthetic/tasks")
def get_synthetic_tasks(count: int = 5):
    return {"tasks": generate_synthetic_tasks(num_tasks=count)}

@app.post("/messages", response_model=MessageRead)
async def post_message(message: MessageCreate, db: AsyncSession = Depends(get_db)):
    return await create_message(db, message)

# enhancing messages with pagination and filters
# this now supports get all messages, filter by user, search messages, filter+search, paginate

@app.get("/messages", response_model=List[MessageRead], summary="List Messages")
async def list_messages(
    user: Optional[str] = Query(None, description="Filter by user"),
    search: Optional[str] = Query(None, description="Search message content"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max records to return"),
    db: AsyncSession = Depends(get_db)
):
    return await get_messages(db, user=user, search=search, skip=skip, limit=limit)

@app.get("/messages", summary="List messages with optional filters and pagination")
async def list_messages(
    user: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    messages = await get_messages(db, user=user, search=search, skip=skip, limit=limit)
    total = await count_messages(db, user=user, search=search)
    return {"data": messages, "total": total}

@app.post("/github-issues", response_model=GitHubIssueRead)
async def add_github_issue(issue: GitHubIssueCreate, db: AsyncSession = Depends(get_db)):
    return await create_github_issue(db, issue)

@app.get("/github-issues", response_model=List[GitHubIssueRead])
async def list_github_issues(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_github_issues(db, skip=skip, limit=limit)

@app.post("/test/populate-messages", summary="Populate test messages")
async def populate_test_messages(count: int = 20, db: AsyncSession = Depends(get_db)):
    synthetic = generate_synthetic_messages(num_messages=count)

    for item in synthetic:
        # Ensure timestamp is a Python datetime object
        timestamp = item.get("timestamp")
        if isinstance(timestamp, str):
            timestamp = datetime.fromisoformat(timestamp)
        elif timestamp is None:
            timestamp = datetime.utcnow()

        msg = Message(
            user=item["user"],
            message=item["message"],
            timestamp=timestamp
        )
        db.add(msg)

    await db.commit()
    return {"status": "success", "inserted": len(synthetic)}


