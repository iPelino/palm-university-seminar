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

