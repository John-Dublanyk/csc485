import pytest
from projects.hw10.fruit_query import is_it_a_fruit

def test_apple_is_a_fruit():
    """Test if 'apple' is recognized as a fruit."""
    assert is_it_a_fruit('apple') == True

def test_pear_is_a_fruit():
    """Test if 'pear' is recognized as a fruit."""
    assert is_it_a_fruit('pear') == True

def test_banana_is_not_a_fruit():
    """Test if 'BAnanna' is not recognized as a fruit."""
    assert is_it_a_fruit('BAnanna') == False

def test_empty_string_is_not_a_fruit():
    """Test if an empty string is not recognized as a fruit."""
    assert is_it_a_fruit('') == False

def test_cherry_is_not_a_fruit():
    """Test if 'cherry' is not recognized as a fruit."""
    assert is_it_a_fruit('cherry') == False
