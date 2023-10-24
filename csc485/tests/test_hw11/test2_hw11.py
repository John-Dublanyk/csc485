import pytest
from csc485.csc485.projects.hw11.hw11 import get_formal_name


@pytest.mark.parametrize('expected_name', [
    ('apple', 'Malus domestica'),
    ('pear', 'Pyrus'),
    ('banana', 'Musa acuminata'),
    ('grape', 'Vitis vinifera'),
    ('strawberry', 'Fragaria × ananassa'),
    ('kiwi', 'Actinidia deliciosa'),
    ('cherry', 'Prunus avium'),
])
def test_get_formal_name(expected_name):
    fruit, expected_name = expected_name
    result = get_formal_name(fruit)
    assert result == expected_name, f"Expected '{expected_name}' but got '{result}' for {fruit}"