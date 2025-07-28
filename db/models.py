from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user = Column(String, index=True)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.now(timezone.utc))

class GitHubIssue(Base):
    __tablename__ = "github_issues"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    user = Column(String(100), index=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))