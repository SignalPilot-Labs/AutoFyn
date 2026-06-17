# Custom Subagents

AutoFyn ships a team of subagents — explorers, planners, builders, reviewers —
and the orchestrator routes work to them by role. You can **add your own** by
putting a `.autofyn/subagents.json` file in your repo, to tailor the team to a
domain the built-in agents don't cover (ML research, formal proofs, data work).

- Add a new agent, and it joins the run.
- Reuse a built-in name, and your version replaces it.
- AutoFyn reads the file when it clones your repo — edit it, and the next run
  picks it up. No UI step, no rebuild.

## Quick start

Add a folder `.autofyn/` to your repo with two files.

**`.autofyn/subagents.json`** — one agent:

```json
[
  {
    "name": "data-explorer",
    "type": "explore",
    "description": "Profiles datasets and reports schema, size, and quality issues. Call before any data work.",
    "model": "sonnet",
    "tools": ["Read", "Glob", "Grep", "Bash"],
    "prompt_file": ".autofyn/subagents/data-explorer.md",
    "needs_run_state": true
  }
]
```

**`.autofyn/subagents/data-explorer.md`** — what the agent does (this becomes its
system prompt):

```markdown
You are the data-explorer. Profile the datasets in this repo and report what
you find — schema, row counts, missing values, anomalies. Do not modify data.

Write your report to `/tmp/round-{ROUND_NUMBER}/data-explorer.md` so the next
agent can read it.
```

Commit both, start a run, and the orchestrator will call `data-explorer` during
the explore phase. That's the whole feature.

## The fields

| Field | Required | What it is |
|-------|----------|------------|
| `name` | yes | The agent's name. Reuse a built-in name to replace it. |
| `type` | yes | Its phase — `explore`, `plan`, `build`, or `review`. Decides when it runs. |
| `description` | yes | *When to call it.* The orchestrator routes on this, so write a clear "call this when…". |
| `model` | yes | `opus` or `sonnet`. (On a sonnet run everything runs on sonnet to save cost.) |
| `tools` | yes | The agent's tools. The built-ins are `Bash`, `Edit`, `Glob`, `Grep`, `Read`, `WebFetch`, `WebSearch`, `Write`. You can also list any MCP tool you've wired in for the repo (Settings → MCP servers) by its `mcp__<server>__<tool>` name. The one exception: the session-gate tools (`mcp__session_gate__*`) are reserved for the orchestrator and rejected here. |
| `prompt_file` | yes | Path (inside your repo) to the agent's prompt. |
| `needs_run_state` | yes | `true` to let the agent read the run's goal/rules and remember lessons across rounds. Use `true` for most agents. |
| `needs_verification` | no | Defaults `false`. Set `true` only for a **build** agent that writes code — it adds a "run the typechecker/linter/tests" step. Leave it off (or omit it) for anything that isn't producing code to verify. |

## Two things to know

**Your prompt is the agent's job description.** Write `prompt_file` as the
agent's role and instructions. AutoFyn adds the shared context (environment, git
rules, and — when you set the `needs_*` flags — the run state and verification
checklist). End it by telling the agent to write its report to
`/tmp/round-{ROUND_NUMBER}/<your-agent-name>.md`; that's how the next agent in
the round receives the handoff (`{ROUND_NUMBER}` is filled in at runtime).

**Planners and reviewers have a contract.** If your agent is a `plan` agent (it
replaces or acts like the built-in `architect`), its output is a *spec*, and the
first line must say whether that spec needs review:

```
Spec review: required
```

Use `required` for anything non-trivial, `skip` for small mechanical work — the
orchestrator reads this to decide whether to run a reviewer before the build. If
your agent is a `review` agent, end with one of `APPROVE`, `CHANGES REQUESTED`,
or `RETHINK` — the verdict the orchestrator routes on (approve → done, changes →
back to the builder, rethink → back to the planner).

## A few rules

- The file is validated when AutoFyn reads it, and a bad entry **stops the run
  with a clear error** — so you find out immediately, not mid-way.
- `prompt_file` must stay inside your repo (no absolute paths, no `..`).
- `tools` is your agent's allowlist — the built-ins plus any MCP tool you've
  wired in for the repo — except the reserved `mcp__session_gate__*` tools;
  `model` only `opus`/`sonnet`.
- Up to 32 custom agents, and no duplicate names.

## In the dashboard

After a repo's first run, its custom agents show up in **Settings → Subagents**
with a `USER` badge (built-in ones show `CORE`), and you can toggle any of them
on or off per repo. Before that first run, only the built-in agents appear.

---

Want a fuller example? A repo can replace the whole pipeline — see how a
math-proof team overrides explore/plan/build/review by name to solve theorem
problems instead of writing code. The pattern is the same: name your agents,
write their prompts, and let the orchestrator route by description.
