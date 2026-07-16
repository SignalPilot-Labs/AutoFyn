# proof-reviewer role memory

ALWAYS: the ranker (.autofyn/approach_ranker.py) is an MCP server with no CLI; call
record_outcome by importing the module in python3 and using getattr(fn,'fn',fn) to
unwrap the mcp.tool() decorator (worked round 1).
ALWAYS: current.md must be Read via the Read tool before Write even if you already
cat'd it via Bash — the harness tracks Read-state separately (round 1).
