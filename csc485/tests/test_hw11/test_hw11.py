import pytest
from projects.hw11.hw11 import get_formal_name


@pytest.mark.parametrize('fruit', 'expected_name', [
    ('apple', 'Malus domestica'),
    ('pear', 'Pyrus'),
    ('banana', 'Musa acuminata'),
    ('grape', 'Vitis vinifera'),

])
def test_get_formal_name(fruit, expected_name):
    result = get_formal_name(fruit)
    assert result == expected, f"Expected '{expected_name}' but got '{result}' for {fruit}"
