import pytest
from projects.hw12.hw12 import compute_complexity


#testing johndub123 as a password with no complex characters
#testing john@ub1^ with mutilpe complex characters
#test ^^^@ with all complex characters
@pytest.mark.parametrize('password', [
    'johndub123',
    'john@ub1^',
    '^^^@',

])
def test_compute_complexity(password):
    """
    Testing the complexity for the different password cases, we are looking how complex each possible password can be.
    """
    expected_complexity = {
        'johndub123': 0.0,
        'john@ub1^': 22.22222222222222,
        '^^^@': 100.0,

    }

    result = compute_complexity(password)
    assert result == expected_complexity[password], f"Expected complexity: {expected_complexity[password]}, but got {result} for password: '{password}'"


