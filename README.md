# palm-university-seminar

Demo repo for the seminar talk "Software Engineering & the AI Ecosystem".
A small Python + SQLite tuition-balance app, set up to show two of the five
agentic engineering terms in action.

| Term | Where it lives in this repo |
|---|---|
| Context engineering | `AGENTS.md` (shared rules for every AI tool) and `CLAUDE.md` (points Claude to them) |
| Loop engineering | `.github/workflows/claude.yml` (an @claude mention triggers an agent) and `.github/workflows/ci.yml` (tests run on every PR) |

## Run it locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
python -m palm.db          # creates palm.db with three demo students
python -m pytest -v        # 4 tests, including a SQL-injection check
```

## One-time setup on GitHub

1. Install the Claude GitHub App on this repo: https://github.com/apps/claude
2. On your own computer, run `claude setup-token` (uses your Claude subscription, no API key).
3. In the repo: Settings > Secrets and variables > Actions > New repository secret,
   name it `CLAUDE_CODE_OAUTH_TOKEN` and paste the token.
4. Optional: Settings > Branches > add a rule for `main` that requires a pull request
   and the `CI / test` check to pass. This is the harness that keeps the loop safe.

## Live demo script

1. **Context engineering.** Open `AGENTS.md`. Point out that these are the rules from
   the Frankenstein repo slide, now committed so every teammate's AI reads the same context.
2. **Trigger the loop.** Issues > New issue, then pick **Demo 1: students in debt** (or any template below)
   from the list (don't start a blank issue). The template fills in the title
   and the full request: Task, Context, References and "Done when". Show the audience
   that text: it is the prompt the agent receives. Submit it. The `@claude` at the top
   of the issue body is what triggers the workflow.
   Note: the template only appears in the list once these files are merged into `main`.
3. **Watch the agent.** Actions tab > "Claude Code" run. Claude reads AGENTS.md, writes
   the function and tests on a branch, and replies on the issue with a link to open the PR.
4. **The harness checks it.** Open the PR. The CI workflow runs the tests automatically.
5. **Human review.** Check it follows AGENTS.md (`?` placeholder, no hardcoded path, tests
   added). Ask for changes with `@claude ...` in a PR comment to show iteration.

`--max-turns 10` in `claude.yml` is the loop's stop condition.

## Ready-made demo issues

Each one is a full TCREI-style request with `@claude` already in it. Pick it from
Issues > New issue, show the text, submit. No typing needed.

| Template | What Claude does | Opens a PR? |
|---|---|---|
| Demo 1: students in debt | Adds `get_students_in_debt` + tests | Yes |
| Demo 2: record a payment | Adds `record_payment` with validation + tests | Yes |
| Demo 3: total outstanding fees | Adds `get_total_outstanding` + tests (quickest feature) | Yes |
| Demo 4: fix case-sensitive email lookup | Fixes a real bug, explains the cause first | Yes |
| Demo 5: command-line balance check | Adds `palm/cli.py` + tests + README update | Yes |
| Demo 6: security review | Reviews `palm/` against AGENTS.md and OWASP, comments only | No (fastest) |

Tips:
- Run one at a time during the talk. Demos 1 to 4 all edit `palm/fees.py`, so merging
  several of their PRs can cause merge conflicts. Close the ones you don't merge.
- Do a trial run of the template you plan to use before the seminar and keep that PR
  open as a backup to show if the live run is slow.
