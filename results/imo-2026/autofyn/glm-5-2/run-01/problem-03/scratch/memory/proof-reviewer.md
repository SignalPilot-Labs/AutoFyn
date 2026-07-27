# proof-reviewer per-role rules

ALWAYS: independently re-derive the load-bearing inequality with a random/grid sweep (python3) before accepting a casework proof; hand algebra and 2M samples catch different bugs (round 3, imo-2026-03 L(2): D>=1 verified, 0 violations).

ALWAYS: check "equality iff / equality only at" claims separately from the inequality — equality characterizations are a frequent overclaim and the proof's own sub-case lines often contradict the stated iff (round 3, imo-2026-03: B0/B1/B3 each give D=1 on whole regions, falsifying "equality only at full halving").

NEVER: accept a direct per-region linear-form bounding argument as automatically covering interiors just because it is "direct" — confirm the regions partition the parameter box AND the stated sorted order is valid in each region; but DO accept it when verified, since it subsumes the vertex-min principle (round 3).

ALWAYS: when a proof claims "N cells" from a sort-order enumeration, independently count the FULL-DIMENSIONAL cells (where all sort-order inequalities are strict AND the piece-order constraints like f1≥f2≥f3≥f4 hold strictly) — boundary cells (with coincident piece sizes) are covered by closures. Use scipy.optimize.linprog on each cell's closed polytope to verify D ≥ target. The full-dim count must match the proof's claim; boundary cells inflate the raw count (round 4, L(3) k8=3: proof says 13, raw count is 179, full-dim count is exactly 13 ✓).

ALWAYS: when a proof claims a computational cell verification (LP at each vertex) but does NOT write out the per-cell table, flag it as a writeup gap even if the result is independently verified — "no hand-waving" requires the verification to be inspectable from the text (round 4, L(3) k8=2: 59 cells claimed, correct, but table not shown → CHANGES REQUESTED).
