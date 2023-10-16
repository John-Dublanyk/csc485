import pytest
from projects.hw13.hw13 import evaluate_strength

"""We will be testing the for 1. strong password, 2. weak password, 3. no password, 4. super strong password all
complex characters, 5. good password"""


@pytest.mark.parametrize("input_password, expected_result", [
    ("J0hnd@b", True),  # A strong password
    ("password123", False),  # A weak password
    ("", False),  # An empty password
    ("!@#$", True),  # All special characters (super strong)
    ("J%H&D#B", True),  # A mix of characters and special symbols (good)
])
def test_evaluate_strength(input_password, expected_result):
    result = evaluate_strength(input_password)
    assert result == expected_result, f"Expected {'strong' if expected_result else 'weak'}, but got {'strong' if result else 'weak'} "
