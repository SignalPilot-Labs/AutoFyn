# proof-reviewer role memory

ALWAYS: the approach_ranker (.autofyn/approach_ranker.py) is a FastMCP server, not a CLI. To call
record_outcome without MCP wiring, import the module and call the raw function object (it stays
callable after @mcp.tool()). Only record slugs actually BUILT this round — recording an unbuilt
sibling bumps its `expanded` and pollutes PUCB; reset it in .ranking.json if you slip. (round 1)

ALWAYS: for the imo-2026-05 sandwich problem, the "quadratic modulus |h(a)-h(b)|<=(a-b)^2/(4 min)
=> h constant" telescope is airtight and needs NO continuity/differentiability; the two-sided modulus
already follows from the RIGHT inequality alone (apply at both endpoints). Verified round 1. (round 1)
