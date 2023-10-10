import pytest
from projects.hw12.hw12 import compute_complexity

@pytest.mark.parametrize('password, expected_complexity', [
    ('johndub123', 0.0),
    ('j0hn@ub1!', 14.285714285714286),
    ('!^^&', 100.0),
    ('', 0.0),
])
def test_compute_complexity(password, expected_complexity):
    """
    Test the complexity computation for the password cases.
    """
    result = compute_complexity(password)
    assert result == expected_complexity, f"Expected complexity: {expected_complexity}, but got {result} for password: '{password}'"

