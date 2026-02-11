# python-sample-repo

A small Python sample repository for RAG ingestion and query tests. It provides simple modules and functions (aligned with the JS sample repo) so an agent can answer questions about behavior, usage, and TODOs.

## License

MIT. See [LICENSE](LICENSE).

## Modules and functions

### `src/math_ops.py`

- **`add(a, b)`** — Returns the sum of two numbers.
- **`multiply(a, b)`** — Returns the product of two numbers.
- **`square(n)`** — Returns `n * n` (uses `multiply` internally).

### `src/greet.py`

- **`greet(name=None, salutation='Hello')`** — Returns a greeting string. If `name` is missing or empty, returns a "Hello, World!" style message.
- **`farewell(name)`** — Returns a goodbye message (uses `greet` with `'Goodbye'`).

### `src/utils.py`

- **`clamp(value, min_val, max_val)`** — Clamps `value` between `min_val` and `max_val` (inclusive).
- **`sum_list(arr)`** — Sums a list of numbers (uses `math_ops.add`).
- **`is_positive_integer(value)`** — Returns `True` if `value` is a positive integer.

### `src/__init__.py`

Re-exports all public functions for `from src import ...`.

## Running tests and examples

- **Run tests (no deps):** `python tests/run_tests.py` (from repo root).
- **Run tests (pytest):** `pytest tests/` or `python -m pytest tests/` (requires `pip install pytest`).
- **Run usage example:** `python examples/usage.py` (from repo root).

No other dependencies required for the simple test runner or examples.

## TODOs and issues

See [TODO.md](TODO.md) for planned improvements. In-code TODOs/FIXMEs appear in `src/utils.py`.
