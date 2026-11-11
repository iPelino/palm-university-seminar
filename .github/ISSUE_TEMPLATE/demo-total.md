---
name: "Demo 3: total outstanding fees (small feature)"
about: Adds get_total_outstanding. The quickest feature demo. Click, review the text, submit.
title: "Add get_total_outstanding"
labels: []
---

@claude

**Task:** Act as a careful Python developer on this team. Add a function
`get_total_outstanding() -> float` to `palm/fees.py` that returns the sum of
all student balances. Open a pull request.

**Context:** Balances are in the `fees` table (see `palm/db.py`). Follow every
rule in AGENTS.md. An empty table should return `0.0`, not `None`.

**References:** Match the style of `get_student_balance` in `palm/fees.py`:
the path from `PALM_DB_PATH` and a short docstring.

**Done when:** tests in `tests/test_fees.py` check the total for the seed data
(1650.50) and for an empty table, and `python -m pytest` passes.
