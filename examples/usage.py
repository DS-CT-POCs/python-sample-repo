"""
Usage examples for the sample Python repo. Run from repo root: python examples/usage.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import add, square, greet, clamp, sum_list

if __name__ == "__main__":
    print("Math:", add(10, 20), square(7))
    print("Greet:", greet("RAG"))
    print("Clamp 15 to [0,10]:", clamp(15, 0, 10))
    print("Sum [1,2,3,4,5]:", sum_list([1, 2, 3, 4, 5]))
