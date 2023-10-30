import pytest
from csc485.projects.hw13.hw13 import compute_complexity, evaluate_strength
"""First we are testing to see what a strong password with only special characters does.
 second we look for a strong password with bot normal and special character.
 third look at weak password woth just normal characters, looking for it not to pass.
 forth we see what happesn when you add numbers to the password, hopping it does not pass
 fifth we are make sure no password is not accepted."""

def evaluate_strength(password):

    if not isinstance(password, str):
        msg = f"Error: Attempted password '{password}' must be a string!"
        raise TypeError(msg)

    strength_threshold = 50.0
    complexity = compute_complexity(password)

    if complexity > strength_threshold:
        return True
    else:
        return False



def compute_complexity(data):

    return 60.0


@pytest.mark.parametrize("password, expected_result", [
    ("^##^^^", True),
    ("Jo^^^^h@@", True),
    ("john", False),
    ("john123", False),
    (" ", False),
])
def test_evaluate_strength(password, expected_result):
    assert evaluate_strength(password) == expected_result