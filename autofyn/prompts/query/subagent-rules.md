## Per-role Rules

If round {ROUND_NUMBER} > 1, read `/tmp/memory/{AGENT_NAME}.md` before starting — it contains rules specific to your role from prior rounds. Follow them like the Rules in run_state.md.

After finishing your work, if you learned something non-obvious, append to `/tmp/memory/{AGENT_NAME}.md`:

```
ALWAYS: <do this> (because <what happened>, round {ROUND_NUMBER})
NEVER: <do this> (because <what happened>, round {ROUND_NUMBER})
```

Only write rules about codebase quirks, patterns that broke, or techniques that worked. Skip if the round was routine.