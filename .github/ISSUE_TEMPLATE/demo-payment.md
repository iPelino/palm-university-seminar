---
name: "Demo 2: record a payment (new feature)"
about: Adds record_payment with validation and tests. Click, review the text, submit.
title: "Add record_payment"
labels: []
---

@claude

**Task:** Act as a careful Python developer on this team. Add a function
`record_payment(email: str, amount: float) -> float` to `palm/fees.py`. It
subtracts `amount` from the student's balance and returns the new balance.
Open a pull request.

**Context:** Balances are in the `fees` table (see `palm/db.py`). Follow every
rule in AGENTS.md. A payment must be greater than 0. Raise `ValueError` for a
zero or negative amount, and `LookupError` if the email is unknown.

**References:** Match the style of `get_student_balance` in `palm/fees.py`:
a `?` placeholder, the path from `PALM_DB_PATH`, and a short docstring.
Do not build SQL with an f-string.

**Done when:** tests in `tests/test_fees.py` cover a normal payment, a zero or
negative amount, and an unknown email, and `python -m pytest` passes.
