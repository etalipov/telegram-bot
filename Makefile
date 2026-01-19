format_fix:
	uv run ruff format .

lint_fix:
	uv run ruff check . --fix

lint_check:
	uv run ruff check .

format_check:
	uv run ruff format --check .

types:
	uv run mypy .