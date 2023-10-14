import pytest
from projects.hw11.hw11 import get_formal_name

"""Testing the fruit name with a fruit's formal name.
 If the fruit matches it's formal name the test will pass. 
 we are testing certain fruits below with formal name."""

@pytest.mark.parametrize('expected_name', [
    ('apple', 'Malus domestica'),
    ('pear', 'Pyrus'),
    ('banana', 'Musa acuminata'),
    ('grape', 'Vitis vinifera'),
])
def test_get_formal_name(expected_name):
    fruit, expected_name = expected_name
    result = get_formal_name(fruit)
    assert result == expected_name, f"Expected '{expected_name}' but got '{result}' for {fruit}"