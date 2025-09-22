import pytest
from httpx import AsyncClient
from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


@pytest.mark.asyncio
async def test_read_root():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/test1")
    assert response.status_code == 200
    data = response.json()
    assert "teste" in data
    assert "num_aleatorio" in data
    assert isinstance(data["num_aleatorio"], int)
