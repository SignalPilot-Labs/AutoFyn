# proof-reviewer — per-role rules

ALWAYS: re-derive each approach's single load-bearing inequality independently and stress-test it numerically over random samples respecting the derivation's constraints (e.g. 20k samples of (a,b,s,yn) for the EXP kill) — this caught nothing this run but is the only way to earn an APPROVE on a claimed `solved` (round 1).
ALWAYS: cross-check that a claimed reduction has real content by testing it against a known NON-solution (f(y)=2y broke both (*) and the FE; a two-valued h broke (†) numerically) — a vacuously-true reduction would pass sympy identity checks but prove nothing (round 1).
ALWAYS: call record_outcome via `python3 -c` importing `.autofyn/approach_ranker.py`; the @mcp.tool()-decorated functions are plain callables (use `.fn` if wrapped) — there is no CLI, running the script bare prints nothing (round 1).
NEVER: certify a lemma file without checking its stated hypothesis matches what the proof uses — orbit-invariance/h-nonnegative correctly hypothesize only the FE, not the full (†); a lemma hypothesizing less than its proof needs would poison importers (round 1).
