# FastAPI entrypoint with comments and synthetic data API

from fastapi import FastAPI
from synthetic_data.messages import generate_synthetic_messages
from synthetic_data.github_issues import generate_synthetic_github_issues
from synthetic_data.code_snippets import generate_synthetic_code_snippets
from synthetic_data.doc_summary import generate_synthetic_doc_summary
from synthetic_data.tasks import generate_synthetic_tasks

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