import random
from src.main import *
from unittest.mock import patch
import pytest

def test_root():
    result = root()
    yield result
    assert result == {"message" "Hello": "World"}

def read_root():
    with patch('randon.randint', return_value=28282):
        result = read_root()
        yield result

    assert result == {"teste": True, "num_aleatorio":28282}
