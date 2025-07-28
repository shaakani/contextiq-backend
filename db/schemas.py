from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MessageCreate(BaseModel):
    user: str
    message: str
    timestamp: Optional[datetime] = None

class MessageRead(BaseModel):
    id: int
    user: str
    message: str
    timestamp: datetime

    class Config:
        orm_mode = True

class GitHubIssueCreate(BaseModel):
    title: str
    description: Optional[str] = None
    user: str
    created_at: Optional[datetime] = None

class GitHubIssueRead(GitHubIssueCreate):
    id: int

    class Config:
        orm_mode = True