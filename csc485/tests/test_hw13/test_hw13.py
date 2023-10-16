"""compute_complexity- testable things:
Complexity Calculation- test to see if characters calculate to the right rating
Input data- Test's valid inputs
Evaluate_Strength-
Passwords- Test for valid inputs
Strength- Test the strenght of the password
Boundary- test a complexity rating exactly equal to the strength_threshold """

import pytest
from projects.hw13.hw13 import compute_complexity


def test_compute_complexity():
    """Test with no complex characters"""
    password1 = "johndublanyk"
    assert compute_complexity.compute_complexity(password1) == 0.0
    """test with some complex characters"""
    password2 = "J0hn@dub"
    assert compute_complexity.compute_complexity(password2) == 42.857142857142854
    """Testing no password"""
    password3 = ""
    assert compute_complexity.compute_complexity(password3) == 0.0
    """This test has all complex characters"""
    password4 = "%^&*"
    assert compute_complexity.compute_complexity(password4) == 100.0
