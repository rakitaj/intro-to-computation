import pytest
from recursion import *

def factorial_harness(n, expected):
    assert Recursive.factorial(n) == expected
    assert Iterative.factorial(n) == expected

def test_factorial_simple():
    factorial_harness(0, 1)
    factorial_harness(1, 1)
    factorial_harness(2, 2)
    factorial_harness(3, 6)
    factorial_harness(4, 24)

@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24)
])
def test_factorial_parameterized(test_input, expected):
    assert Recursive.factorial(test_input) == expected
    assert Iterative.factorial(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13)
])
def test_fibonacci(test_input, expected):
    assert Recursive.fibonacci(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [
    ("", True),
    ("a", True),
    ("aa", True),
    ("ab", False),
    ("bob", True),
    ("abc", False),
    ("abba", True),
    ("abcd", False),
    ("radar", True),
    ("apple", False)
])
def test_palindrome(test_input, expected):
    assert Recursive.palindrome(test_input) == expected
