# FastAPI entrypoint with comments and synthetic data API

from fastapi import FastAPI, Depends
from synthetic_data.messages import generate_synthetic_messages
from synthetic_data.github_issues import generate_synthetic_github_issues
from synthetic_data.code_snippets import generate_synthetic_code_snippets
from synthetic_data.doc_summary import generate_synthetic_doc_summary
from synthetic_data.tasks import generate_synthetic_tasks

from db.deps import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from db.crud import create_message, get_messages
from db.schemas import MessageCreate, MessageRead
from typing import List

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

@app.get("/messages", response_model=List[MessageRead])
async def list_messages(limit: int = 10, db: AsyncSession = Depends(get_db)):
    return await get_messages(db, limit=limit)