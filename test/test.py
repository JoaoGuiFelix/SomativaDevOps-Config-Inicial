import pytest
from httpx import AsyncClient
from unittest.mock import patch
from src.main import app


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_read_root_mocked():
    with patch("src.main.random.randint", return_value=28282):
        async with AsyncClient(app=app, base_url="http://test") as ac:
            response = await ac.get("/test1")
    assert response.status_code == 200
    assert response.json() == {"teste": True, "num_aleatorio": 28282}
