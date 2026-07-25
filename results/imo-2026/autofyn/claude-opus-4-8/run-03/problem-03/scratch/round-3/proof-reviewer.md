# Proof-reviewer report — imo-2026-03 (IMO 2026 P3), round 3

Problem: determine largest c LB can guarantee. Claimed answer c(n) = 2^n/(2^{n+1}−1),
D_n = 2^{n+1}−1. This is a compute-and-prove / find-all: `solved` REQUIRES both a proven lower
bound (LB strategy) AND a proven upper bound (XY strategy). No approach delivers both, so none is
`solved`. All three make genuine, verified, rigorous progress → all CHANGES REQUESTED (partial).

Method: I re-derived every new load-bearing claim from scratch and verified each numerically
(peel-max 0/20000; A0 0 violations, A1 0/120000 mismatches; Lemma H 0/138158 with h≥1;
Case-1 φ-telescoping 0/40000; G(n) min S = 1 for n=1,2,3). Imports L2/L3 re-read and correct.

---

## Approach 1 — induction-peel
**Verdict: CHANGES REQUESTED. True Status: partial (matches builder's claim — no overclaim).**

Correct and rigorous this round:
- **Lemma A0** (≤1 part of B exceeds H = 2^{n-1}): re-derived, correct (shards of 2^{j≤n-1} ≤ H;
  two shards of 2^n over H would sum > 2^n). CERTIFIED as L6.
- **Lemma A1** truncation identity S(B) = e + S(B_low): re-derived via L3 integral split at H,
  correct; numerics 0 mismatch. CERTIFIED as L6. Consequence e ≥ 1 ⟹ S ≥ 1 is valid and cleanly
  one-lines Case 1 (e = 2^{n-1} ≥ 1).
- Base case n=1, and the whole e ≥ 1 regime: complete.
- Upper-bound recursion (R), part-count fix, base case (via S ≥ 0 / P2), and the descriptive
  MATCH/BISECT S-effect: correct as stated.

Gaps (correctly flagged, not overclaimed):
- **Open gap 1 (A-res):** S(B_low) ≥ 1 − e for e < 1. Genuinely open; builder verifies the
  interval bounds are too weak. This is the shared field crux.
- **Open gap 2:** the two MATCH/BISECT branch inequalities U_{k−1}(c(A)) ≤ s/D_k. Open.

Note: the MATCH/BISECT "exact effect" is a correct but informal/descriptive observation (S(A_M)
is the alternating sum of the resulting multiset — true by definition; equal adjacent twins cancel
by L4). It is not a crisp standalone theorem and feeds a still-open gap → NOT certified.

## Approach 2 — alternating-sum-potential
**Verdict: CHANGES REQUESTED. True Status: partial (matches builder's claim).**

Correct and rigorous this round:
- **Peel-max (P2)** S(P) = b_(1) − S(P∖{b_(1)}): correct. CERTIFIED as L5 (shared with approach 3).
- **Lemma φ-monotone** a_0 ≤ φ_1 ≤ … ≤ φ_n: re-derived, correct.
- **Generalized Case 1 (φ-telescoping):** for any ratio-≥2 set with top part uncut, a_n is strict
  global max (a_n > Σ_{i<n} a_i ≥ sum of all other pieces), so S(B) = a_n − S(C) ≥ a_n − Σ_{i<n}a_i
  = φ_n ≥ a_0. Fully rigorous, exact (φ_n=1) for dyadic; numerics 0/40000. CERTIFIED as L8. This is
  a strict generalization of the round-2 dyadic Case (i).

Gaps (correctly flagged):
- **G1:** binding lower-bound Case 2 overlap bound S(Q)+S(C)−2W ≥ a_0 (needs a cut-budget cap on
  W; trivial W ≤ min is too weak). Open — same shared crux.
- **G2:** general upper bound (Lemma D / amortized charging). Only the exact dyadic cascade witness
  is established (S=1, n=1..6, verified). Open.

## Approach 3 — global-max-peel
**Verdict: CHANGES REQUESTED. True Status: partial (matches builder's honest claim).**

Correct and rigorous this round:
- **Lemma P (peel-max):** correct (= L5).
- **Band confinement + identity (‡)** S(B) = h + S_low(B_n) + S(Rest) − 2W with W confined to
  t < 2^{n-1}: re-derived from L3 XOR + A0, correct; numerics 0/80000.
- **Lemma H (unconditional):** h ≥ 1 ⟹ S(B) ≥ 1. Re-derived: W ≤ min(S_low, S(Rest)) ⟹ bracket
  ≥ |S_low − S(Rest)| ≥ 0 ⟹ S(B) ≥ h ≥ 1. No IH used. Fully rigorous; 0/138158 violations.
  CERTIFIED as L7. Its Corollary gives a one-line induction-free proof of the entire field Case 1
  plus every high-band Case 2 — a genuine, clean unification.
- Base case n=1: complete.

Gaps (honestly flagged, including self-criticism that peeling does NOT escape the crux):
- **GAP-LB:** sub-case c_n ≥ 1 AND h < 1 — the low-band overlap budget cap on W. Open — identical
  to A-res / G1.
- **Upper bound:** not attempted (out of scope). Honestly disclosed.

This approach is a valid, live population member: Lemma H is a real deliverable, not a duplicate.
It does not attempt the upper bound, but that does not make it broken — partial, not RETHINK.

---

## Certified lemmas this round (into results/imo-2026-03/lemmas/)
- **L5** peel-max identity (from global-max-peel Lemma P / alt-sum P2). ADMITTED.
- **L6** A0 (≤1 large shard) + A1 truncation identity (from induction-peel). ADMITTED.
- **L7** unconditional high-band inequality Lemma H (from global-max-peel). ADMITTED.
- **L8** generalized Case-1 φ-telescoping (from alternating-sum-potential). ADMITTED.
- **REJECTED:** induction-peel "MATCH/BISECT exact-effect" — descriptive, not a crisp standalone
  statement, and feeds a still-open gap. The underlying facts are correct but not certifiable as a
  reusable lemma in current form.

## Combined state / crux flag for the orchestrator
Both live lower-bound gaps (A-res, G1, GAP-LB) are the SAME statement — a cut-budget cap on the
low-band overlap W in the small-top-shard sub-case (e<1 / h<1). This is now 3 rounds on the same
wall, and the upper bound is a second shared wall (no one-pass rule; needs branch inequalities or a
validated charging). Per CLAUDE.md plateau guidance, next round should put ≥1 approach on a
genuinely different framing (e.g. attack the upper bound directly / a non-potential formulation),
not another variation that hits the same low-band-W wall one step later.
