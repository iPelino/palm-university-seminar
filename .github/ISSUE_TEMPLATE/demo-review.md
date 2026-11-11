---
name: "Demo 6: security review, no code changes (fastest)"
about: Claude reviews the code against AGENTS.md and replies in a comment. Good backup if time is short.
title: "Review palm/ against our rules and OWASP"
labels: []
---

@claude

**Task:** Act as a security-minded reviewer on this team. Review the code in
`palm/` and reply in a comment on this issue. Do not change any files and do
not open a pull request.

**Context:** Check the code against every rule in AGENTS.md and against the
OWASP guidance on SQL injection.

**References:** For each finding, give the file and line, the rule it relates
to, and a one-line suggestion. If everything follows the rules, say so and
explain which lines show it.

**Done when:** one comment with a short list of findings, or a clear
statement that none were found.
