---
name: "Demo 4: fix case-sensitive email lookup (bug fix)"
about: A bug report the agent fixes and explains. Click, review the text, submit.
title: "Bug: balance lookup fails for emails with capital letters"
labels: []
---

@claude

**Task:** Act as a careful Python developer on this team. Fix the bug below
and open a pull request. In the PR description, explain the cause first,
then the fix.

**Context:** `get_student_balance("AMINA@palm.edu")` returns `None`, but
`get_student_balance("amina@palm.edu")` returns `1200.0`. Students type their
email in different ways, including extra spaces. Follow every rule in
AGENTS.md: keep the function name `get_student_balance`, because teammates use it.

**References:** Keep the `?` placeholder in the query. Do not build SQL with
an f-string. Keep the change small.

**Done when:** a test shows that `"  AMINA@palm.edu "` returns `1200.0`, all
existing tests still pass, and `python -m pytest` passes.
