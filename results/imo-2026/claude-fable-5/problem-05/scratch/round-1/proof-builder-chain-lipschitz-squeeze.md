# Build report — chain-lipschitz-squeeze (round 1, imo-2026-05)

## Result
Status: **solved** (candidate — awaiting proof-reviewer). Full proof written to
`results/imo-2026-05/approaches/chain-lipschitz-squeeze.md`.

## What was done
- Filled the outline into a complete prose proof of the full characterization:
  solutions are exactly f(x) = x + c, c ≥ 0.
- **GAP 1 closed, with a simplification.** The outline proposed bounding the deficit via
  p − q ≤ (t + t²/(4m))/(2√m) and p ≥ √m, yielding t²/(4m) + t³/(16m²). Instead, the same
  division that produces bound (A) gives p − q ≤ t/(2q) directly (from 2pq ≤ 2q² + t),
  so the deficit t(p−q)/(2p) ≤ t²/(4pq) < t²/(4f(z)) since pq > q² = f(z). Result:
  symmetric two-sided bound t − t²/(4m) ≤ f(z+t) − f(z) ≤ t + t²/(4m) whenever f(z) ≥ m —
  no cubic term, no √m constants.
- **GAP 2 closed.** Telescoping written as explicit finite sums over the partition
  z_k = y + kT/n; uniform m = f(y) justified at every piece by the strict monotonicity
  proved in Step 2.2(B) (order of derivation is sound: monotonicity comes from (B1),
  which precedes the uniform bound). The limit is replaced by an Archimedean argument:
  |f(y+T) − f(y) − T| ≤ T²/(4mn) for all n forces the difference to be 0.
- **Reviewer notes addressed.** (a) c < 0 exclusion now states −c/2 > 0 explicitly.
  (b) Every squaring/division step states positivity, via an explicitly named
  "squaring principle" (A ≥ B ⟺ A² ≥ B² for A, B ≥ 0) invoked at each use.
- No continuity, monotonicity, or differentiability assumed anywhere; monotonicity is
  derived in Step 2.2(B).
- All load-bearing algebra re-verified in sympy (Part 1 SOS identities, (A) squaring,
  deficit identity, telescoped sums) and a 10^4-sample numeric check of (*) for the
  claimed family. These checks are auxiliary; the written proof stands on its own.

## Promotable lemmas (for reviewer to certify into results/imo-2026-05/lemmas/)
1. **chain-inequality**: 2√(f(y₁)f(y₂)) ≤ 2f(y₂) + y₁ − y₂ for all y₁, y₂ > 0
   (Step 2.1). At y₁ = y₂ it yields the functional equation f(f(y)) = 2f(y) − y used by
   both orbit approaches — certifying this covers their shared Step 2.1–2.2 reduction.
2. **increment-bounds**: f strictly increasing and t − t²/(4f(z)) ≤ f(z+t) − f(z) ≤
   t + t²/(4f(z)) for all z, t > 0 (Step 2.2).

## Spec concerns
None. The problem statement in problems.jsonl matches what was proved
(characterization; both verification and uniqueness delivered). One reading note for the
reviewer: Part 1's parenthetical about c < 0 within the family is a completeness remark,
not part of uniqueness — uniqueness (Part 2, Step 2.4) independently proves c ≥ 0 for
any solution.
