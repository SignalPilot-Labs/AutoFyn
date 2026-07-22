# IMO 2026 — Claude Code solution logs

Solutions to all six IMO 2026 problems produced in interactive Claude Code sessions
(model: `claude-fable-5`), as opposed to the autofyn-orchestrated runs in the sibling
directories. Because these were single-session runs rather than harness runs, there are
no `logs.jsonl` / `approaches/` / `lemmas/` artifacts; each problem folder contains:

- `solution.md` — the complete written solution
- `verification.md` — verification log: adversarial review verdict and numeric checks
- `verification.py` — numeric verification script, where applicable (problems 3–6)

| Problem | Folder | Verification |
|---------|--------------|--------------|
| 1 | `problem-01/` | step-by-step audit |
| 2 | `problem-02/` | step-by-step audit |
| 3 | `problem-03/` | audit + script |
| 4 | `problem-04/` | audit + script |
| 5 | `problem-05/` | audit + script |
| 6 | `problem-06/` | audit + script |

Source of truth at time of upload: `~/codeAlpine/imo26/fable-runs/` (2026-07-22).
