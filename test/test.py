import random
from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asynicio
async def test_root():
    result = await root()
    assert result == {"message" "Hello": "World"}

@pytest.mark.asynicio
async def read_root():
    with patch('randon.randint', return_value=28282):
        result =  await read_root()
    assert result == {"teste": True, "num_aleatorio":28282}
