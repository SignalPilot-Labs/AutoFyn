# Build report — newman-confluence — round 1

## Result
Status: **solved** (claimed). Full proof of both (a) and (b) written to
`results/imo-2026-01/approaches/newman-confluence.md`.

## What was closed

- **GAP 1 (L3, the crux — overlap joinability) — CLOSED, non-circularly, at the integer level.**
  The mechanism is NOT the "unique terminal for 3-boards" induction the outline proposed (which
  the outline-reviewer correctly flagged as circularity-prone). Instead I found (first by a BFS
  schedule search, then proved) an explicit uniform joining schedule:
  - From branch B₁ = {d, mn/d², k} ∪ R (d = gcd(m,n)): one formal move on (d, k) pulls the
    shared place to t = gcd(m,n,k), giving {t, mn/d², dk/t²} ∪ R; then iterate the move on the
    remaining pair to its fixed point {1, E₁} (pair-collapse Lemma 4).
  - From branch B₂ symmetrically: {t, en/t², mk/e²} ∪ R, then pair-collapse to {t, 1, E₂} ∪ R.
  - E₁ = E₂ by the elementary identity gcd(|α−β|, |min(α,β)−γ|) = gcd(|α−β|, |α−γ|) (proved by
    common-divisor-set equality, all zero cases handled), applied per prime only to verify the
    equality of two specific integers.
  - **The coupling trap is avoided by construction:** the joining schedules are fixed sequences
    of integer moves (one schedule serves all primes simultaneously); valuations appear only to
    identify the deterministic endpoint of that single schedule. No board-wide invariant of the
    process is used; the approach never computes M — it remains a genuine confluence proof,
    architecturally disjoint from per-prime-gcd-invariant.
- **Legality of intermediate moves:** handled by the "formal move" device (Lemma 3): a move
  touching an entry 1 fixes the multiset, so formal paths project to real paths by deleting
  stationary steps. This cleanly disposes of the d = 1 / intermediate-1 edge cases.
- **GAP 2 (Newman inline) — CLOSED.** Lemma 6: confluence by strong induction on the single
  nonnegative-integer monovariant N = 2027·P + C (Lemma 1 shows every move strictly decreases
  N, so the induction is well-founded with no lex-order machinery needed), using Lemma 5 at the
  peeled first steps; uniqueness of the terminal multiset follows since terminals have only the
  empty path.
- **GAP 3 (L1, L2, L5 write-ups, m = n and gcd = 1 cases) — CLOSED.** Exhaustive case split
  g > 1 / g = 1 in Lemma 1 (C never increases; drops by exactly 1 in the coprime case); the
  disjoint diamond with the legality sub-check; prime-support persistence (Lemma 2) with the
  three exponent cases; "exactly one entry > 1" from Lemma 2 + C(T) ≤ 1.

## Verification performed (checks, not proof steps)
- Joining scheme end-to-end on 20,000 random triples (primes 2,3,5,7, exponents ≤ 5): 0 fails.
- Difference-gcd identity exhaustively for all exponent triples in 0..8: 0 fails.
- Monovariant N on 5,000 random moves: 0 fails.

## Remaining gaps
None known. Points a reviewer should probe: the zero-pair bookkeeping in Fact D / Fact E, the
multiset-vs-places formalization in Section 0, and the two sub-case splits (u = α vs u = β;
w = α vs w = γ) in Lemma 5 Case 3 — I believe all are airtight.

## Spec concerns
The reviewer's condition "no citing the g_p invariant in a way that collapses the approach" is
met: the only valuation-gcd object is E(x,y), the endpoint of a deterministic 2-place iteration
(Lemma 4), used as the common target of two explicit schedules — not a conserved quantity of the
game. If the proof-reviewer judges even this too close to the rival slug, the honest statement
is: the schedules and the confluence architecture are the content; the E-identification is a
local computation about a pair orbit.
