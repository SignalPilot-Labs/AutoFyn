# Lemma L9 — Self-pairing kills the overlap

**Status:** CERTIFIED (proof-reviewer, round 4). One-line consequence of L3; re-derived
independently. Source: induction-peel §3.3.

**Setup.** For a multiset B_low = Q_low ⊔ C, the L3 XOR corollary gives
  S(B_low) = S(Q_low) + S(C) − 2W,  W := meas{ t : N_{Q_low}(t) odd ∧ N_C(t) odd } ≥ 0.

**Lemma L9.** If S(Q_low) = 0 (equivalently, by L3, N_{Q_low}(t) is even for a.e. t > 0) then
W = 0 and hence S(B_low) = S(C).

**Proof.** The overlap integrand {N_{Q_low} odd ∧ N_C odd} is supported inside {N_{Q_low} odd},
so W ≤ meas{ t : N_{Q_low}(t) odd } = S(Q_low) = 0 (the equality is L3). Since W ≥ 0, W = 0, and
S(B_low) = S(Q_low) + S(C) − 2W = 0 + S(C) − 0 = S(C). ∎

Reusable by every XOR-split lower-bound approach to dispose of the pure-BISECT / self-pairing
boundary (e.g. Q = {2^{n-1}, 2^{n-1}}).
