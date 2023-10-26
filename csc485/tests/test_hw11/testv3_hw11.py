import pytest
from csc485.projects.hw11.hw11 import get_formal_name
""" We are testing for our fruits expected scientific name. 
we provide a list of testable fruits to see if they have a in the dictionarie. """

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