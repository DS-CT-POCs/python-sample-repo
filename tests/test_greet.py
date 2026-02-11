"""Tests for greet module."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.greet import greet, farewell


def test_greet_with_name():
    assert greet("Alice") == "Hello, Alice!"


def test_greet_with_salutation():
    assert greet("Bob", "Hi") == "Hi, Bob!"


def test_greet_default():
    assert greet() == "Hello, World!"
    assert greet("") == "Hello, World!"


def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"


def test_farewell_empty_name():
    """When name is empty, farewell uses greet and returns 'Goodbye, World!'."""
    assert farewell("") == "Goodbye, World!"
