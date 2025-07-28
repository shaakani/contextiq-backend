import pytest
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
from httpx import ASGITransport
from main import app
from create_tables import init_models

@pytest.mark.asyncio
async def test_create_and_list_github_issue():
    await init_models()  # 👈 creates tables automatically before test

    async with LifespanManager(app):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            payload = {
                "title": "Test issue", 
                "description": "This is a test issue.",
                "status": "open",
                "user": "test_user"
            }
            response = await ac.post("/github-issues", json=payload)
            assert response.status_code == 200
            data = response.json()
            assert data["title"] == payload["title"]

            list_response = await ac.get("/github-issues")
            assert list_response.status_code == 200
            assert isinstance(list_response.json(), list)
