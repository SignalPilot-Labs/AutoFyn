# Build report — extremal-sup-inf, imo-2026-05, round 1

Status: **solved**.

The outline's proposed sup/inf-of-a-minimizing-sequence mechanism turned out to be too weak on
its own (it only gives a local bound near the attaining point, not global constancy). While
investigating why, I found a strictly stronger use of the already-verified Tool (A)/(B): since
these are identities valid for ALL real x,y>0 (not just orbit-related pairs), plugging in
x = y+ε for a genuine real perturbation ε→0 immediately forces g(y):=f(y)-y to be **continuous**
everywhere — a purely algebraic consequence of the hypothesis, no continuity of f assumed a
priori. This single move (Step 5 in the proof) unlocks everything else:

- continuity + injectivity (already proved) ⟹ f is monotonic (classical IVT theorem); f(y)≥y
  rules out decreasing, so f is strictly increasing (Step 6).
- f strictly increasing + the orbit AP structure f^n(y)=y+n·g(y) forces g non-decreasing
  (Step 7), via a straightforward "unbounded divergence" contradiction.
- A "crossing lemma" (Step 8): if a<b and g(a),g(b)>0, then g(a)=g(b), via a minimal escaping
  orbit index argument.
- A zero-set dichotomy (Step 9): the zero set of g is either empty or all of R_{>0} (using
  downward-closedness of the zero set under the monotonicity from Step 7, plus continuity at the
  boundary point s=sup(zero set)). Combined with the crossing lemma, this forces g to be a
  single global constant c≥0 in both cases.

This fully closes the "orbit-local → global constant" gap that all four round-1 approaches were
aimed at. Sufficiency of f(x)=x+c (c≥0) is verified directly against the ORIGINAL (un-squared)
inequality via the SOS identities (x-y-c)^2≥0 for both the left (QM) and right (GM) sides —
checked symbolically with sympy for safety, and the derivation of Tool A's algebra was also
checked symbolically; all match the written proof exactly (diff = 0).

Final answer: f(x) = x + c for any constant c ≥ 0, and this is the complete solution set.

File written: /home/agentuser/repo/results/imo-2026-05/approaches/extremal-sup-inf.md
(Status: solved, full proof included, promotable lemmas listed for reviewer certification —
especially the "continuity from Tool A/B via real perturbation" lemma and the
"non-decreasing + crossing lemma + zero-set dichotomy ⟹ global constant" lemma, both reusable
beyond this specific approach/problem).
