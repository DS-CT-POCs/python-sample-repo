"""Tests for utils module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.utils import clamp, sum_list, is_positive_integer


def test_clamp():
    assert clamp(10, 0, 5) == 5
    assert clamp(-1, 0, 5) == 0
    assert clamp(3, 0, 5) == 3
    assert clamp(0, 0, 5) == 0  # edge: value equals lower bound
    assert clamp(5, 0, 5) == 5  # edge: value equals upper bound


def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0


def test_is_positive_integer():
    assert is_positive_integer(1) is True
    assert is_positive_integer(0) is False
    assert is_positive_integer(-1) is False
