import pytest
from hw2_debugging import merge_sort

def test_single_element():
    assert merge_sort([1]) == [1]

def test_two_elememts():
    assert merge_sort([2, 1]) == [1, 2]

def test_bigger_array():
    assert merge_sort([20, 4, 10, 18, 14, 1, 16, 6, 4, 6, 8, 6, 11, 7, 6, 12, 13, 18, 9, 2]) == [1, 2, 4, 4, 6, 6, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 18, 20]
