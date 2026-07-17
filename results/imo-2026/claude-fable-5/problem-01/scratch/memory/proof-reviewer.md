# proof-reviewer — per-role rules

ALWAYS: re-derive the single load-bearing identity numerically with sympy/python before reading the prose justification — for gcd/lcm move problems, simulate thousands of random runs and check the claimed invariant/monovariant at EVERY move, not just endpoints (caught nothing round 1 but confirmed two APPROVEs cheaply, round 1).
ALWAYS: when a proof uses gcd-of-multiset with zeros, check the gcd(0,...,0)=0 convention is applied consistently on BOTH sides of every "same divisor set => same gcd" step, and that the two multisets are all-zero simultaneously (this was the most likely gap class in round 1; both builders handled it, round 1).
ALWAYS: create results/<id>/current.md yourself on first review — it does not exist before the first proof-reviewer run (round 1).
NEVER: trust "the schedules are legal moves" in confluence proofs without checking intermediate entries can equal 1 — demand an explicit device (e.g. formal-move projection) or reject (round 1: newman-confluence closed this with Lemma 3; without it the join would be a real gap).
