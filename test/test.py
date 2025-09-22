from src.main import *
from unittest.mock import patch

def test_root():
    with patch('randon.randint', return_value=28282):
        result = read_root()

    assert result == {"teste": True, "num_aleatorio": 28282}
