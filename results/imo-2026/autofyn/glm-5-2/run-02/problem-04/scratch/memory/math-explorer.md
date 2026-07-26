# Per-role rules for math-explorer

ALWAYS: read the crux corpus via the documented field names — `technique`, `how_used`, `domain`, `subtopic` (NO `crux_move` / `statement` field exists; querying those returns blank). Read `crux_moves_documentation.md` fully before any corpus query (round 1).

ALWAYS: probe the answer numerically with a game-tree BFS BEFORE forming the leading conjecture. For imo-2026-04 the integer-grid BFS falsified two plausible conjectures (dyadic-only AND dense-rational) and pinned the real answer (theta = 180/N). Pure-retrieval intuition would have been wrong; the BFS was the truth-maker (round 1).

ALWAYS: when the operation resembles a Euclidean/subtractive game on a triple with an integer relation, the L1-norm monovariant on the auxiliary coefficient vector is the transferable engine — see aimo-0440. Search the corpus for "monovariant" + "coefficient" / "linear relation" (round 1).

NEVER: trust surface-level analogy for the answer. The imo-2026-04 problem is dressed as geometry but the answer is a number-theoretic torsion condition (theta = 180/N); the synthetic-geometry toolkit is a dead end (round 1).

NEVER: assume symmetry theta <-> 180-theta. The Mulan game is asymmetric (Mulan picks alpha, Shan-Yu discards); only theta=90 is self-dual (round 1).
ALWAYS: verify the angle transform numerically before using it — the dispatch's stated child form "{alpha,B,180-beta}" was WRONG (doesn't sum to 180); correct is {alpha,B,180-alpha-B} and {beta,C,alpha+B} (round 1).
REMOVED (round 1, was WRONG): the claim "winning set is 3-smooth reciprocals 180/(2^a*3^b), n=5 is a loss" — this was the defense explorer's outlier conjecture, DISPROVEN by the outliner, reviewer, and the constructive explorer's exact integer-grid attractor. The SOLVED answer (reviewer APPROVED) is theta = 180/N for ALL integer N >= 2; theta=36 (N=5) is a WIN. Do not re-propose 3-smooth.
REMOVED (round 1, was WRONG): "trust fine-grid (steps>=20) game-tree search" — fine-grid search PRODUCED the wrong 3-smooth answer, because ANY fixed degree-grid cannot represent non-integer theta (e.g. 180/7) and mislabels it. The reliable engine is the least-fixpoint attractor with modular theta-arithmetic (180/theta integer), NOT grid search.
