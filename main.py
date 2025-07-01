# FastAPI entrypoint with comments and synthetic data API

from fastapi import FastAPI
from synthetic_data import generate_synthetic_messages

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
