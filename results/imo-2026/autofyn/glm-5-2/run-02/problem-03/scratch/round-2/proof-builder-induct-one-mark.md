# Build report — `induct-one-mark`, imo-2026-03, round 2

## What I proved this round
1. **Retired the certified-false per-mark monovariant** explicitly and permanently (recorded as a NEVER rule with counterexamples: `A=1/3` → bisect gives `A'=1/3` not `1/7`; `A=1/2` → bisect gives `A'=1/4` not `1/5`).
2. **Algebraically verified the Mersenne value recursion (R)/(M)** — `B(n+1)=2B(n)+1` with `B(n)=D(n)`, equivalently `1/V(n+1)=1+1/(2V(n))`, equivalently `A(n+1)=A(n)/(A(n)+2)`. Substitution check for n=1..5 (all match: 7/4, 15/8, 31/16, 63/32, 127/64). Corrected the dispatch's WRONG form `V(n+1)=(1+V(n))/2` (predicts V(2)=5/6, false; verified V(2)=4/7).
3. **Proved the k=0 sub-case of Lemma L(n+1) rigorously** (Opening B): if 0 Xiang marks land in the largest dyadic piece `M`, then `S_odd = M + evensum(R') ≥ M = f(n+1)`, no induction, no interleaving obstruction. Fully closed.
4. **Proved the k=1 sub-case as a clean reduction to `L*(n)`** (sibling pairing-partner's strengthened dual IH, pending certification): `M → (m_1,m_2)`, `m_1` rank 1, `S_odd = m_1 + evensum({m_2}∪R')`, want `≥ M = m_1+m_2` ⟺ `evensum({m_2}∪R') ≥ m_2` = `L*(n)` with `w=m_2 ≤ M/2 = R`'s largest. Conditional on `L*`'s certification.
5. **Cross-checked the dyadic saddle by full grid enumeration**: n=2 (denom 168, 13530 responses) and n=3 (denom 120, 253460 responses) both give xiang-min exactly `f(n)`. Corroborates Lemma L + pair-pile/mirror simultaneously for n=2,3.
6. **Verified the mirror certificate** (reviewer finding 1) for n=1..5: merged partition = pairs `(2^k/D, 2^k/D)` for k=1..n−1 plus three `1/D`'s; oddsum = `f(n)` exactly. This is pairing-partner's lane to certify; I referenced it, did not certify.

## Remaining gaps (honest)
1. **Lemma L general-n, k≥2 sub-case** — OPEN. The multi-aux generalization is FALSE (recorded counterexample). Per-round peeling (D1) is the live reduction; delegated to `pairing-partner`.
2. **Lemma U general-n** — OPEN. Per-mark route retired (dead end); two-regime disjunctive invariant delegated to `two-regime-disjunctive`. The regime-N mechanism must be a sliver/shave (NOT the false `A ≤ 0` pairing — reviewer finding 2: non-dyadic configs give cap ≈ 0.503–0.525 > 1/2).
3. **The value-level `+1` interleaving correction** — UN-CLOSED. No potential accounting identified. Honest conclusion: the value-recursion (R)/(M) is a REPHRASING of (Lemma L + Lemma U) into one algebraic statement, NOT an independent bypass. If L+U both close, (M) follows trivially. Flagged as a UNIFYING CONJECTURE, not a proof.

## Status
`partial` — unchanged at the top level. The round-level recursion did not fire as an independent proof (as the dispatch and explorer anticipated). The honest fallback to (Lemma L + Lemma U) is recorded; both are open and delegated to sibling approaches under construction this round. No overclaiming.

## Spec concerns
- The dispatch recursion `V(n+1)=(1+V(n))/2` is WRONG and I refused to use it; the correct Mersenne form `1/V(n+1)=1+1/(2V(n))` is used throughout. Future dispatches on this problem should use (R)/(M).
- The value-recursion framing is best used as the UNIFYING FRAME for the population (one statement packaging L+U), not as a standalone proof route. The `+1` wall is the same wall as Lemma L's interleaving; a "value-level" proof that doesn't name a potential for the `+1` is not a proof.
- The mirror certificate is a clean, verified, NEW dyadic-cap certificate (cleaner than pair-pile) and SHOULD be certified this round (by pairing-partner per the reviewer's allocation).

## New lemma proposed
- **Lemma L(n+1) k=0 sub-case** (trivial dyadic-untouched case) — recorded in the approach's Promotable lemmas. Small; may not warrant a separate file. The reviewer may certify if useful.
- No NEW game-theoretic lemma certified this round; `L*(n)` and the mirror certificate belong to pairing-partner's lane.

## File touched
- `results/imo-2026-03/approaches/induct-one-mark.md` (revised: round-2 revision appended; round-1 content preserved).
