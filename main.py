# FastAPI entrypoint with comments and synthetic data API

from fastapi import FastAPI
from synthetic_data import generate_synthetic_messages
from github_issues import generate_synthetic_issues
from code_snippets import generate_code_snippets

app = FastAPI(title="ContextIQ Backend API")

@app.get("/")
def read_root():
    """
    Root endpoint - simple welcome message.
    """
    return {"message": "Welcome to ContextIQ backend!"}

@app.get("/ping")
def ping():
    """
    Health check endpoint.
    """
    return {"ping": "pong"}

@app.get("/synthetic/messages")
def get_synthetic_messages(count: int = 10):
    """
    Generate and return synthetic chat messages.
    
    Query parameter:
    - count: number of messages to generate (default 10)
    """
    messages = generate_synthetic_messages(num_messages=count)
    return {"messages": messages}

@app.get("/synthetic/github-issues")
def get_github_issues(count: int = 5):
    """
    Generate and return synthetic GitHub issues.

    Query parameter:
    - count: number of issues to generate (default 5)
    """
    return {"issues": generate_synthetic_issues(num_issues=count)}

@app.get("/synthetic/code-snippets")
def get_code_snippets(count: int = 5):
    """
    Generate and return synthetic code snippets.
    
    Query parameter:
    - count: number of code snippets to generate (default 5)
    """
    snippets = generate_code_snippets(num_snippets=count)
    return {"snippets": snippets}