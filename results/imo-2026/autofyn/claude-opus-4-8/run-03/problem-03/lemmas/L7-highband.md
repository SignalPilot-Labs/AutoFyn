# Lemma L7 — Unconditional high-band inequality (Lemma H)

**Status:** CERTIFIED (proof-reviewer, round 3). Numerically verified: 0 violations over 138158
random configurations with h ≥ 1 (n = 1..4). Source: global-max-peel Lemma H + band confinement.

Let B be a ≤ n-cut refinement of P_n = {2^0,…,2^n}. Decompose B = B_n ⊔ Rest, where B_n is the
refinement of the top part 2^n and Rest is the refinement of {2^0,…,2^{n-1}} (so every part of
Rest is ≤ 2^{n-1}, and Σ Rest = 2^n − 1). Write H := 2^{n-1}, q_1 := max(B_n),
h := max(q_1 − H, 0), and S_low(B_n) := meas{t < H : N_{B_n}(t) odd}.

**Structural facts.**
- (Band confinement of W.) By the XOR corollary of L3, S(B) = S(B_n) + S(Rest) − 2W with
  W = meas{t : N_{B_n}(t) odd ∧ N_{Rest}(t) odd}. Every part of Rest is ≤ H, so N_{Rest}(t) = 0
  for t ≥ H; hence W is confined to t < H, giving W ≤ S_low(B_n) and W ≤ S(Rest).
- (High-band decomposition.) By A0 (L6) at most one part of B_n exceeds H, so for t ≥ H,
  N_{B_n}(t) ∈ {0,1}, equal to 1 exactly on [H, q_1). Thus meas{t > H : N_{B_n} odd} = h and
  S(B_n) = h + S_low(B_n). Substituting: **S(B) = h + S_low(B_n) + S(Rest) − 2W** (identity ‡).

**Lemma H.** If h ≥ 1 then S(B) ≥ 1 — with no induction hypothesis.
**Proof.** From W ≤ min(S_low(B_n), S(Rest)),
S_low(B_n) + S(Rest) − 2W ≥ S_low(B_n) + S(Rest) − 2·min(S_low(B_n), S(Rest)) = |S_low(B_n) − S(Rest)| ≥ 0.
Plugging into (‡): S(B) = h + [S_low(B_n) + S(Rest) − 2W] ≥ h ≥ 1. ∎

**Corollary (top piece uncut).** If B_n = {2^n} (top part uncut), then q_1 = 2^n and
h = 2^n − 2^{n-1} = 2^{n-1} ≥ 1 for n ≥ 1; hence S(B) ≥ 1. This gives a one-line, induction-free
proof of the field's entire "Case 1", plus every Case 2 with a surviving top shard ≥ 2^{n-1}+1.
