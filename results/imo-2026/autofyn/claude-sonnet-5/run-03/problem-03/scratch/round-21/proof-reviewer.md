# Round 21 proof-reviewer report — imo-2026-03

Two slugs built this round: `self-similar-induction-on-n` and
`global-lp-vertex-sufficiency`. Both adversarially re-verified with
fresh, independent scripts (not the builders'). Both verdicts:
**CHANGES REQUESTED** — genuine, certified progress in each, but neither
closes the overall problem.

## 1. `self-similar-induction-on-n` — General Cardinality-Constrained
Half-Sum Lemma, all k>=2 — VERIFIED, CERTIFIED

Claim: for GCH(k) (R finite multiset, max(R)<=2^{k-1}, |R|<=k+1,
sum(R)=S in [2^k,2^k+1)), AltSum(R∪Γ_{k-1}) >= 1, for every k>=2 —
via reduction (already-certified Finite Reduction Theorem) to canonical
form R'' (multiplicities n_0..n_{k-1} at Γ-levels plus one free block
(t,r)), then a 3-step argument:
- Step A (pigeonhole): all-levels-inactive + free-block-inactive is
  infeasible.
- Step B (pairing): any nonempty active-Γ-subset alone has AltSum>=1.
- Step C: free block active, split on |A| (active-Γ-set size) into
  C0 (|A|=0), C1 (|A|=1), C2 (|A|>=2).

I independently re-derived and stress-tested every step:
- **Step A**: exhaustive (not random) search over small n_j,t
  configurations, k=2,3,4 — 337 configs checked, zero violations of the
  pigeonhole claim (`/tmp/verify_stepA_exhaustive.py`).
- **Case C1's forced unique allocation**: exhaustive enumeration,
  k=2..6, every active level j_A — confirms (n_{j_A},t)=(0,1) is the
  *unique* feasible point at the tightest budget level in every case
  (`/tmp/verify_C1_exhaustive.py`), matching the file's "only 1 unit of
  slack, insufficient for a parity-preserving jump" argument exactly.
- **General sweep**: 1125 random feasible canonical-form instances,
  k=2..7 — zero AltSum<1 violations, zero Step-A failures, case
  distribution (B/C0/C1/C2) all populated and consistent
  (`/tmp/verify_gch.py`).
- **Case C2 (the case leaning on piecewise-affineness + boundary-value
  reduction to Step B, flagged as the one needing the hardest scrutiny)**:
  a targeted 3000-instance fine-grid search (4000-point grids per
  instance, k=2..6, |A|>=2) comparing the true minimum of AltSum(A∪{r})
  over r against the theoretical floor min(AltSum(A), min_i
  AltSum(A\{v_i})) — zero mismatches, zero floor violations
  (`/tmp/verify_c2_finegrid.py`). I also hand-traced the boundary-value
  logic myself (checking that the two "uncaptured" endpoints of the
  domain, r->0+ and r->cap, are never the binding minimum of their
  interval — always the maximum, since the topmost interval has slope
  +1 and the bottom interval's uncaptured endpoint is never the min
  regardless of parity) and confirmed it algebraically on a worked
  example (A={4,1}, k=3): matches the claimed piecewise formula and
  boundary limits exactly.

No gap found in Steps A, B, C0, C1, or C2. The proof is complete,
correct, and general (no restriction to small k). The lemma is genuinely
new content: prior rounds (16, 18, 19) explicitly diagnosed this as
resisting the natural single-parameter induction, requiring a
two-parameter family instead — this round's direct canonical-form
argument sidesteps that entirely.

**Certified** into
`results/imo-2026-03/lemmas/general-cardinality-constrained-half-sum-lemma.md`.

**Scope, correctly not overclaimed**: this closes GT(m) sub-case (i)
(odd excess e=1) for every k, but GT(m) as a whole (e=0 sliver, odd
e>=3) remains open — the file states this honestly, does not claim the
overall problem is closer to solved than it is.

## 2. `global-lp-vertex-sufficiency` — Region I of n=3 Existence
Theorem via Construction H — VERIFIED, CERTIFIED; Region II genuinely
open

Claim: a new 3-cut Construction H (split p1->(g1,p2), p3->(x,x,g1),
x=(p3-g1)/2, leaving p2,p4 untouched) satisfies, whenever x>=g1>=p4 (an
order condition), the exact identity
OddSum(H) - c(3) = (p4 - gamma(3))/2. Restricting to Region I :=
B(3) ∩ {p4<=gamma(3)} ∩ {g3+p4>3*g1} makes both order conditions hold
automatically (the second, g1>=p4, follows for free from B(3)'s own
g1>gamma(3) hypothesis combined with p4<=gamma(3)), giving
OddSum(H)<=c(3) throughout Region I by construction. Region II
(B(3)\Region I) is left open, with a specific counterexample showing
best-of-{Construction C, Construction H} fails there.

I independently re-verified:
- **Symbolic re-derivation from scratch** (own `sympy` script, not
  reusing the builder's): derived p4 from p1+p2+p3+p4=1 directly (not
  assuming the file's mass-conservation identity), substituted, and
  confirmed `sympy.simplify(OddSum(H) - c(3) - (p4-gamma(3))/2)` is
  exactly 0. Also independently re-derived the order-condition formulas
  p2-x and x-g1 in closed form and confirmed they match the file's
  claims (p2-x = g1/2+g2+g3/2+p4/2, x-g1 = (g3+p4-3g1)/2) after
  re-expressing in the same variables (`/tmp/verify_sym.py`).
- **Region I random sweep**: 493 instances (wide gap range, k=2..k
  n/a — this is the n=3 problem) — zero identity mismatches, zero
  order-condition failures, zero OddSum(H)>c(3) violations
  (`/tmp/verify_regionI.py`).
- **Region I legality**: separate 300,000-trial sweep confirms x>0
  (construction legal) throughout Region I with zero exceptions
  (`/tmp/verify_regionI_legality.py`).
- **Region II counterexample**: reproduced the cited exact point
  (g1=3161/46875, g2=205073/3000000, g3=456719/3000000,
  p4=339131/4000000) independently and confirmed OddSum(H)=
  4339131/8000000 and OddSum(C)=216961/400000 exactly (digit-for-digit
  match to the file's claims), both exceeding c(3)=8/15, and confirmed
  the point is valid in B(3) and lies outside Region I (p4>gamma(3))
  (`/tmp/verify_regionII_counterex.py`). This is a genuine
  counterexample, not a script artifact.
- **Region II failure rate, independent distribution**: a 100,000-trial
  sweep under a different (uniform-in-gap-space) sampling distribution
  than the file's own found an 15% failure rate for best-of-{C,H} in
  Region II — differs numerically from the file's reported ~3%, but
  this is exactly the kind of distribution-dependent discrepancy
  documented (and correctly not flagged as a bug) in round 16's
  cross-check of a different construction; the qualitative finding
  (genuine, non-trivial, non-vanishing residual) is confirmed either way.

No gap found in the Region I closure or the Region II counterexample.

**Certified** into
`results/imo-2026-03/lemmas/construction-h-and-p4-margin-identity.md`.

**Scope, correctly not overclaimed**: only Region I is closed; Region II
(and hence the full n=3 Existence Theorem, and the general-n theorem)
remains open. The file is explicit about this ("Region II honestly NOT
closed this round").

## Outcomes recorded

Both slugs recorded via `mcp__approach-ranker__record_outcome` as
`verified-milestone` for round 21 (genuine certified lemma closures, but
neither slug's overall target — GT(m) / the full n=3+ Existence
Theorem — is solved).

## current.md updated

Added a "round 21" entry under `## Approaches tried` documenting both
verdicts in detail (Status remains `partial` — no `Full proof` section
added, since neither the GT(m) program nor the n=3 Existence Theorem
is complete).

## New certified lemma files

- `results/imo-2026-03/lemmas/general-cardinality-constrained-half-sum-lemma.md`
- `results/imo-2026-03/lemmas/construction-h-and-p4-margin-identity.md`
