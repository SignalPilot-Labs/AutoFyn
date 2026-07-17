# proof-reviewer rules

ALWAYS: when numerically minimizing over cut positions with Nelder-Mead, clip each cut into [eps, piece_len - eps] INSIDE the objective; np.clip(x, eps, None) alone lets cuts escape the piece and produces garbage negative fragments (round 1).
ALWAYS: call record_outcome by importing .autofyn/approach_ranker.py directly in python3 (the MCP tool is not exposed to the reviewer's toolset); the @mcp.tool functions are callable as plain functions (round 1).
ALWAYS: for this stick-cutting game, verify game-value lemmas against exact minimax (memoized recursion on sorted tuples) — cheap up to |M| ~ 8 and catches oddsum-formula errors immediately (round 1).
