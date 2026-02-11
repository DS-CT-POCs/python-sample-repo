"""
General utility functions.
"""

from .math_ops import add


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp value between min_val and max_val (inclusive)."""
    if value < min_val:
        return min_val
    if value > max_val:
        return max_val
    return value


def sum_list(arr: list[float]) -> float:
    """
    Sum a list of numbers. Uses math_ops.add for consistency.
    TODO: Support Decimal for financial use and avoid float drift.
    """
    if not isinstance(arr, list):
        return 0.0
    result = 0.0
    for n in arr:
        result = add(result, n)
    return result


def is_positive_integer(value: object) -> bool:
    """
    Return True if value is a positive integer.
    FIXME: Consider moving to a dedicated validation module.
    """
    return isinstance(value, int) and value > 0
