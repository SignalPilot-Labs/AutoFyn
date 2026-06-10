# Custom Subagents

AutoFyn ships a set of subagents organized by phase — Explore (`code-explorer`,
`security-explorer`), Plan (`architect`, `debugger`), Build (`backend-dev`,
`frontend-dev`), and Review (`code-reviewer`, `ui-reviewer`, `security-reviewer`,
`spec-reviewer`). The orchestrator routes work to them by role.

A target repo can **bring its own subagents** by dropping a
`.autofyn/subagents.json` file in its root. This lets you tailor the team to a
domain the shipped agents don't cover — ML research, formal proofs, data
pipelines — without changing AutoFyn itself.

- **New agents** defined in the file appear in the run.
- **Same-named agents override** the shipped ones (the repo wins).
- Each agent's prompt body lives in the repo too, so an agent ships with its own
  instructions.

Discovery rides the existing clone: AutoFyn reads the file once per run at
bootstrap, exactly like the `.autofyn/config.yml` overlay. There's no UI step and
no sync — edit the file, and the next run picks it up.

## The file

Put a JSON array of agent definitions at `.autofyn/subagents.json` in your repo
root:

```json
[
  {
    "name": "proof-builder",
    "type": "build",
    "description": "Fills a proof outline into a complete, rigorous proof. Call after the outline is ready.",
    "model": "opus",
    "tools": ["Read", "Write", "Edit", "Glob", "Grep", "Bash"],
    "prompt_file": ".autofyn/subagents/proof-builder.md",
    "needs_run_state": true
  }
]
```

### Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | yes | Unique agent name. Reusing a shipped name overrides that agent. |
| `type` | yes | The phase: `explore`, `plan`, `build`, or `review`. Determines when the orchestrator dispatches it and the card color in the dashboard. |
| `description` | yes | When to call this agent. The orchestrator routes **by description**, so write it as a clear "call this when…". |
| `model` | yes | `opus` or `sonnet`. A tier *request* — on a sonnet run, every agent runs on sonnet regardless (cost-conscious). |
| `tools` | yes | Subset of the allowed tools: `Bash`, `Edit`, `Glob`, `Grep`, `Read`, `WebFetch`, `WebSearch`, `Write`. |
| `prompt_file` | yes | Repo-relative path to the agent's prompt body (a Markdown file). Must stay inside the repo — no absolute paths, no `..`. |
| `needs_run_state` | yes | `true` if the agent should read `/tmp/memory/run_state.md` and keep per-role rules across rounds. |
| `needs_verification` | no | Defaults `false`. `true` appends the verification checklist (typecheck/lint/test) — leave it off for agents with no code to verify. |

### The prompt body

`prompt_file` points to a Markdown file anywhere in the repo (commonly under
`.autofyn/subagents/`). Its contents become the agent's system prompt. AutoFyn
appends the shared fragments (environment, git rules, and — per the `needs_*`
flags — verification and run-state context), so write the body as the agent's
role and instructions.

A subagent receives its dispatch via a report file. By convention, write your
report to `/tmp/round-{ROUND_NUMBER}/<agent-name>.md` so the next agent in the
round can read it — `{ROUND_NUMBER}` is substituted at runtime. Reviewers that
override a shipped reviewer should emit the same verdict vocabulary the
orchestrator routes on: `APPROVE`, `CHANGES REQUESTED`, or `RETHINK`.

## How merging works

The repo's agents are merged over the shipped set, **repo-wins-by-name**:

```
shipped subagents (config/subagents.json)
  ↓ overlaid by
.autofyn/subagents.json (in your repo)
```

A new name is added to the team; a name that matches a shipped agent replaces it
wholesale (including its prompt body). Shipped phase order is preserved. If you
override a shipped reviewer (e.g. `security-reviewer`), that review now runs your
version — be deliberate about it.

## Validation

The file is untrusted (the agent operating on your repo can write it), so every
entry is validated at load and a violation **fails the run fast** with a clear
error. The checks:

- `type` is one of the four phases; `model` is `opus` or `sonnet`.
- `tools` is a subset of the allowed tools above — no arbitrary tool names.
- `prompt_file` is non-empty, repo-relative, and contains no `..` — it cannot
  read files outside the repo. (The sandbox enforces this a second time.)
- No duplicate names, and at most **32** repo agents.

## Seeing them in the dashboard

Repo agents don't show in **Settings → Subagents** until the repo has been run at
least once — AutoFyn records the repo's subagent list at bootstrap, and Settings
reads from that. After the first run, your agents appear with a `REPO` badge
(shipped agents show `CORE`) and can be toggled on or off per repo like any other
subagent.

## Example: a math-proof team

A repo solving olympiad problems might define an explore → outline → review →
build → review pipeline:

```json
[
  { "name": "math-explorer",   "type": "explore", "description": "Reads the problem and prior attempts; reports promising techniques. Call first.", "model": "sonnet", "tools": ["Read", "Write", "Glob", "Grep", "Bash"], "prompt_file": ".autofyn/subagents/math-explorer.md",   "needs_run_state": true },
  { "name": "proof-outliner",  "type": "plan",    "description": "Outlines a proof strategy and the key lemmas. Marks 'Spec review: required' when non-trivial.",  "model": "opus",   "tools": ["Read", "Write", "Glob", "Grep", "Bash"], "prompt_file": ".autofyn/subagents/proof-outliner.md",  "needs_run_state": true },
  { "name": "outline-reviewer","type": "review",  "description": "Reviews a proof outline before details are filled in.", "model": "opus", "tools": ["Read", "Write", "Glob", "Grep", "Bash"], "prompt_file": ".autofyn/subagents/outline-reviewer.md", "needs_run_state": true },
  { "name": "proof-builder",   "type": "build",   "description": "Fills the outline into a complete, rigorous proof.", "model": "opus", "tools": ["Read", "Write", "Edit", "Glob", "Grep", "Bash"], "prompt_file": ".autofyn/subagents/proof-builder.md", "needs_run_state": true },
  { "name": "math-reviewer",   "type": "review",  "description": "Adversarially judges the proof and returns an APPROVE / CHANGES REQUESTED / RETHINK verdict.", "model": "opus", "tools": ["Read", "Write", "Glob", "Grep", "Bash"], "prompt_file": ".autofyn/subagents/math-reviewer.md", "needs_run_state": true }
]
```

Because these override `code-explorer` / `architect` / `spec-reviewer` /
`backend-dev` / `code-reviewer` by name, the orchestrator's role-based routing
picks them up with no further configuration. Use the repo's `CLAUDE.md` to tell
the orchestrator about the domain (e.g. "no build step; the deliverable is a
proof file").
