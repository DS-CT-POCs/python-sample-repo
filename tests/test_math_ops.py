"""Tests for math_ops module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.math_ops import add, multiply, square


def test_add():
    assert add(1, 2) == 3
    assert add(0, 0) == 0


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-1, 3) == -3


def test_square():
    assert square(5) == 25
    assert square(0) == 0
