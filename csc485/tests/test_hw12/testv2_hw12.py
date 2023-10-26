import pytest
from csc485.projects.hw12.hw12 import compute_complexity

"""
I implemented 4 testable items
testing johndub123 as a password with no complex characters, so looking for bad score.
testing john@ub1^ with multiple complex characters, we looking for a weaker score.
test ^^^@ with all complex characters. we are looking for a perfect score.
testing an empty string, this in order to make sure empty strings can not bypass our program
Last test is looking for the threshold of the complexity rating.
"""


@pytest.mark.parametrize('password', [
    'johndub123',
    'john@ub1^',
    '^^^@',
    ' ',
    'Joh@^^h^n^',

])
def test_compute_complexity(password):
    """
    Testing the complexity for the different password cases, we are looking how complex each possible password can be.
    """
    expected_complexity = {
        'johndub123': 0.0,
        'john@ub1^': 22.22222222222222,
        '^^^@': 100.0,
        ' ': 0.0,
        'Joh@^^h^n^': 50.0,


    }

    result = compute_complexity(password)
    assert result == expected_complexity[
        password], f"Expected complexity: {expected_complexity[password]}, but got {result} for password: '{password}'"
