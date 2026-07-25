# Lemma L6 — At-most-one-large-shard (A0) and the truncation identity (A1)

**Status:** CERTIFIED (proof-reviewer, round 3). Numerically verified: 0 violations of A0 and
0 mismatches of A1 over 120000 random ≤n-cut refinements of P_n, n = 1..4.
Source: induction-peel Lemmas A0, A1 (equivalently global-max-peel's band decomposition (‡)).

Throughout, P_n = {2^0, 2^1, …, 2^n} (superincreasing), H := 2^{n-1}, and B is any refinement of
P_n by any number of split operations (each shard of an original part 2^j has value ≤ 2^j).

**Lemma A0 (at most one part above H).** At most one part of B exceeds H = 2^{n-1}.
**Proof.** A shard of 2^j with j ≤ n−1 has value ≤ 2^{n-1} = H, so does not exceed H. Two shards
of 2^n each exceeding H = 2^{n-1} would sum to > 2^n, contradicting that all shards of 2^n sum to
exactly 2^n. Hence at most one part (a shard of 2^n, or the uncut 2^n itself) exceeds H. ∎

Let p* be the unique part exceeding H if it exists, e := (max part − H)^+ = (p* − H)^+
(so 0 ≤ e ≤ 2^n − H = H), and B_low := B with p* (if it exists) replaced by the value H; every
part of B_low is ≤ H.

**Lemma A1 (truncation identity).** S(B) = e + S(B_low).
**Proof.** By L3, S(B) = meas{t>0 : N_B(t) odd}; split the integral at H.
- For t > H: by A0 the only part that can exceed t (> H) is p*, so N_B(t) = 1 for t < p* and 0
  otherwise, giving meas{t > H : N_B odd} = meas{H < t < p*} = (p* − H)^+ = e.
- For 0 < t < H: replacing p* (> H) by H leaves unchanged whether that part exceeds t (both p* > t
  and H > t), and no other part changes, so N_B(t) = N_{B_low}(t). Since every part of B_low is ≤ H,
  N_{B_low}(t) = 0 for t > H, hence meas{t < H : N_B odd} = meas{t>0 : N_{B_low} odd} = S(B_low).
Adding the two bands (t = H is null) gives S(B) = e + S(B_low). ∎

**Consequence.** Since S(B_low) ≥ 0 (L5), S(B) ≥ e; in particular e ≥ 1 ⟹ S(B) ≥ 1.
