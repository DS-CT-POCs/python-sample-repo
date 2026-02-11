"""
Simple test runner (no pytest required). Run from repo root: python tests/run_tests.py
Used by RAG tests to verify behavior of this sample repo.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.math_ops import add, multiply, square
from src.greet import greet, farewell
from src.utils import clamp, sum_list, is_positive_integer


def run():
    # math_ops
    assert add(1, 2) == 3
    assert multiply(3, 4) == 12
    assert square(5) == 25

    # greet
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", "Hi") == "Hi, Bob!"
    assert greet() == "Hello, World!"

    # utils
    assert clamp(10, 0, 5) == 5
    assert clamp(-1, 0, 5) == 0
    assert sum_list([1, 2, 3]) == 6
    assert is_positive_integer(1) is True and is_positive_integer(0) is False

    print("All tests passed.")


if __name__ == "__main__":
    run()
