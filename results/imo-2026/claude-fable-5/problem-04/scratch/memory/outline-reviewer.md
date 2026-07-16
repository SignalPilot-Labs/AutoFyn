# Per-role rules: outline-reviewer

ALWAYS: call the ranker by importing it directly — `sys.path.insert(0, '/home/agentuser/repo/.autofyn'); import approach_ranker` then call register_approach/update_ranking as plain functions (it is an MCP server with no CLI; the FastMCP decorator leaves the functions callable, and paths resolve from REPO_ROOT inside the module) (worked, round 2).
ALWAYS: stress-test claimed monovariants on triangles with MULTIPLE simultaneous multiples of θ (e.g. (5θ,4θ,3θ)) — "largest multiple drops" failed exactly there while all the outliner's random-triangle checks passed, because random safe starts rarely produce two multiples at once (round 2).
ALWAYS: verify forcing/invariant algebra with exact Fractions, never floats — residue-mod-θ tests are equality tests and float mod gives false negatives (round 2).
