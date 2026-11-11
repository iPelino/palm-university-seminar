---
name: "Demo 1: students in debt (new feature)"
about: Adds get_students_in_debt with tests. Click, review the text, submit.
title: "Add get_students_in_debt"
labels: []
---

@claude

**Task:** Act as a careful Python developer on this team. Add a function
`get_students_in_debt(min_balance: float) -> list[str]` to `palm/fees.py`
that returns the emails of students whose balance is greater than
`min_balance`, sorted alphabetically. Open a pull request.

**Context:** The data is in the `fees` table (see `palm/db.py`). Follow every
rule in AGENTS.md.

**References:** Match the style of `get_student_balance` in `palm/fees.py`:
a `?` placeholder, the path from `PALM_DB_PATH`, and a short docstring.
Do not build SQL with an f-string.

**Done when:** new tests in `tests/test_fees.py` cover the normal case and an
empty result, and `python -m pytest` passes.
