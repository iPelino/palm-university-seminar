# AGENTS.md

Shared rules for every AI coding agent on this repo (Claude, Copilot, Cursor and others).
Humans follow them too. This file is the team's context engineering.

## Stack
- Python 3 + SQLite (standard library `sqlite3`). No ORM.
- Tests use pytest. Run them with: `python -m pytest`

## Rules
1. Never push directly to `main`. Every change goes through a pull request that passes CI.
2. SQL always uses `?` placeholders. Never build SQL with f-strings or string concatenation.
3. The database path comes from the `PALM_DB_PATH` environment variable. Never hardcode a path.
4. Keep agreed names. `get_student_balance(email)` is used by teammates: do not rename it.
5. New packages need review. Ask in the PR before adding anything to `requirements-dev.txt`.

## When you change code
- Add or update a test in `tests/` for every behaviour change.
- Keep changes small: one feature or fix per pull request.
- Explain the cause of a bug in the PR description before the fix.
