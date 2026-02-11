"""
Greeting utilities.
"""


def greet(name: str | None = None, salutation: str = "Hello") -> str:
    """
    Return a greeting for the given name.
    If name is missing or empty, returns a 'Hello, World!' style message.
    """
    if not name or not name.strip():
        return f"{salutation}, World!"
    return f"{salutation}, {name.strip()}!"


def farewell(name: str) -> str:
    """Return a farewell message."""
    return greet(name, "Goodbye")
