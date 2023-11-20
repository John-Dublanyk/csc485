"""compute_complexity- testable things:
Complexity Calculation- test to see if characters calculate to the right rating
Input data- Test's valid inputs
Evaluate_Strength-
Passwords- Test for valid inputs
Strength- Test the strenght of the password
Boundary- test a complexity rating exactly equal to the strength_threshold """

import pytest
from csc485.csc485.projects.hw14.password_utilities import compute_complexity


def test_compute_complexity_no_complex_chars():
    """Test with no complex characters"""
    password = "johndublanyk"
    assert compute_complexity(password) == 0.0

def test_compute_complexity_with_complex_chars():
    """Test with some complex characters"""
    password = "J0hn@dub"
    expected_result = 12.5
    assert compute_complexity(password) == pytest.approx(expected_result)

def test_compute_complexity_empty_password():
    """Testing no password"""
    password = " "
    assert compute_complexity(password) == 0.0

def test_compute_complexity_all_complex_chars():
    """This test has all complex characters"""
    password = "@#$$"
    assert compute_complexity(password) == 100.0
