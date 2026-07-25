# Proof-builder report — redundant-constraint-antichain (imo-2026-06)

Status: **partial** (one sharp crux gap remaining; everything else fully proven).

## PROVED IN FULL (unconditional)
- **Free lemmas**: Anchor (every term has a prime of P), Gap bound (gap ≤ M, linear growth),
  Distance–prime (shared prime q ⇒ q ≤ |a_i−a_j|).
- **Pairwise-intersecting (Lemma 4)**: any two terms share a prime — immediate from the greedy
  definition at the smaller index.
- **Antichain reduction (Lemma 5–6)**: admissibility at stage n ⟺ meets every ⊆-minimal support;
  every support dominates a global ⊆-minimal support; hence A := {meet all global-minimal
  supports} ⊆ every stage admissible set A_n.
- **NO-TRANSIENT, fully closed (Lemma 7–8)** — the pleasant surprise. Because all terms pairwise
  share a prime, *every* term a_k lies in A (meets every global-minimal support, even future
  ones). Combined with A ⊆ A_n, this forces `a_{n+1} = s(a_n)` (fixed successor on the fixed set A)
  for **all n ≥ 1**. So the sequence is the forward orbit of one fixed map from its first term —
  no reversibility/stabilization argument needed. This dissolves the difficulty the outline feared.
- **Endgame (Lemma 9–Cor 11), conditional on the crux only**: if Π = ∪(minimal supports) is
  finite, A is a union of residues mod L₀ = ∏_{p∈Π} p, the successor map on A is a cyclic shift
  over the m = |ρ(A)| residues, giving `a_{n+m} = a_n + L₀` for ALL n ≥ 1. Explicit T = |ρ(A)|,
  L = L₀. Verified numerically (105 → T=58, L=210 from n=1; matches).

## REMAINING CRUX GAP (single)
**Finite Alphabet:** the family 𝓕 = {primes(a_n)} has finitely many ⊆-minimal elements
(equivalently Π is a finite prime set). This is now the ONLY open step; the outline's separate
"stabilization" and "no-transient" gaps are closed/absorbed.
- Partial progress recorded (§7 of approach file): reformulation via the "small companion"
  (a large-prime minimal support persists iff its small companion set is never dominated); an
  explicit intersecting-family counterexample showing Lemma 4 + Anchor alone do NOT suffice (so
  the crux needs the greedy dynamics, not just structure); pigeonhole reduction to a fixed anchor
  prime p* ∈ P plus the counting tension from Lemma 2 (density ≥ 1/M) vs Lemma 3 (large q rare).
  The step "rarity ⇒ a dominating small-only support must eventually appear" is NOT completed.

## Distinctness from anomaly-count
Kept genuinely order-theoretic: the reduction runs through ⊆-minimal supports and domination, and
the no-transient is obtained from pairwise-intersecting + global-minimal supports — NOT from an
anomaly monovariant or a mod-K residue count. The remaining crux (finite ⊆-minimal antichain) is a
different statement from anomaly-count's "finitely many anomalies," though both concern large
primes. This approach's advantage: it has *only one* gap, and that gap already implies periodicity
from n=1 with no extra endgame.

## Promotable lemmas (for reviewer to certify)
- **Pairwise-intersecting**: gcd(a_i,a_j)>1 ∀ i≠j.
- **No-transient / fixed-successor identity**: a_k ∈ A ∀k and a_{n+1}=s(a_n) ∀n≥1, where
  A = {meet all ⊆-minimal supports}, s = A-successor. ⇒ once A is eventually periodic, exact
  periodicity holds from n=1 with T=|ρ(A)|, L=period(A). Reusable by ANY approach that proves the
  alphabet is finite by any route — it removes the "eventual ⇒ all n" step entirely.
- Anchor, Gap bound, Distance–prime (standard).

## Spec concerns
None. answer_type = none (proof_only); nothing to verify numerically beyond the illustrative
period checks (done).
