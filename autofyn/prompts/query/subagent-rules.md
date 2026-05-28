## Per-role Rules

Read `/tmp/memory/{AGENT_NAME}.md` before starting — it contains rules specific to your role from prior rounds. If the file doesn't exist, create it. Follow these rules like the Rules in run_state.md. If a per-role rule conflicts with the global Rules in run_state.md, the global Rules win.

After finishing your work, if you learned something non-obvious, append to `/tmp/memory/{AGENT_NAME}.md`:

```
ALWAYS: <do this> (because <what happened>, round {ROUND_NUMBER})
NEVER: <do this> (because <what happened>, round {ROUND_NUMBER})
```

Only write rules about codebase quirks, patterns that broke, or techniques that worked. Skip if the round was routine. Cap 30 — if the file already has 30 rules, drop the least useful one before adding a new one.