import pytest
from myfile import odd_even

def test_pass():
    assert odd_even(2) == 1

def test_fail():
    assert odd_even(3) == 0
