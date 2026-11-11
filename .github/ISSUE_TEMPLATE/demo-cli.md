---
name: "Demo 5: command-line balance check (new feature)"
about: Adds a small CLI so anyone can check a balance from the terminal. Click, review the text, submit.
title: "Add a command-line balance checker"
labels: []
---

@claude

**Task:** Act as a careful Python developer on this team. Add a command-line
tool in a new file `palm/cli.py` so that
`python -m palm.cli balance amina@palm.edu` prints `Balance for amina@palm.edu: 1200.00`.
For an unknown email, print `No student found for <email>` and exit with code 1.
Open a pull request.

**Context:** Use only the standard library (`argparse`). Follow every rule in
AGENTS.md. Do not add new packages. Reuse `get_student_balance` from
`palm/fees.py` instead of writing a new query.

**References:** Keep the code short and readable for first-year students.

**Done when:** tests in a new file `tests/test_cli.py` cover a known and an
unknown email, the README "Run it locally" section shows the new command, and
`python -m pytest` passes.
