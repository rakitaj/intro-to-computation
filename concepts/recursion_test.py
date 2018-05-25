import pytest
from recursion import *

def recursions_harness(n, expected):
    assert Recursive.factorial(n) == expected
    assert Iterative.factorial(n) == expected

def test_recursion():
    recursions_harness(0, 1)
    recursions_harness(1, 1)
    recursions_harness(2, 2)
    recursions_harness(3, 6)
    recursions_harness(4, 24)

@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24)
])
def test_recursion(test_input, expected):
    assert Recursive.factorial(test_input) == expected
    assert Iterative.factorial(test_input) == expected
