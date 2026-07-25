# Lemma L14 — Two-part top-cut closure (c_n = 1 case of the lower bound)

**Status:** CERTIFIED (proof-reviewer, round 5). Source: alternating-sum-potential §4 Case 2b.
Re-derived and numerically verified (0 violations over 20000 random legal configs, n = 2,3,4).

**Statement.** Let H := 2^{n-1} and let {a, b} be a two-part split of the top block, a + b = 2^n,
a ≥ b (so a ≥ H, b ≤ H). Let R be any multiset all of whose parts are ≤ H, and put
B := {a, b} ⊔ R. Then
  S(B) ≥ S(R).
In particular, when R is a refinement of P_{n-1} with S(R) ≥ 1 (the lower-bound statement one
level down), S(B) ≥ 1 — i.e. β(B) ≤ 2^n − 1 — so the entire c_n = 1 slice of the lower bound is
closed.

**Proof.**
*Case a = b = H.* The top group is {H, H}; N_{{H,H}}(t) ∈ {0, 2} is even for all t, so by L9
(self-pairing) the XOR overlap W = 0 and S(B) = S({H,H}) + S(R) − 2W = 0 + S(R) = S(R). ∎

*Case a > H.* Then a is the unique part exceeding H (b ≤ H and every part of R is ≤ H), so by
L6/A0 and the truncation identity L6, with e := (a − H)^+ = a − H,
  S(B) = e + S(B_low),   B_low := {H, b} ⊔ R.
Key exact identity: since a = 2^n − b, e = a − H = (2^n − b) − 2^{n-1} = 2^{n-1} − b = H − b.
Apply the L3 XOR split to B_low with groups {H, b} and R:
  S(B_low) = S({H,b}) + S(R) − 2W,   W := meas{ N_{{H,b}} odd ∧ N_R odd } ≥ 0.
Here S({H,b}) = H − b (as H ≥ b), and N_{{H,b}}(t) is odd exactly on t ∈ [b, H) (there it equals
1; it is 2 on [0,b) and 0 on [H,∞)), so
  W ≤ meas{ N_{{H,b}} odd } = meas[b, H) = H − b.
Combining with e = H − b,
  S(B) = e + S(B_low) = (H−b) + (H−b) + S(R) − 2W = 2(H−b) + S(R) − 2W ≥ S(R),
using W ≤ H − b. ∎

**Scope note.** This closes c_n ≤ 1 (top block uncut = L8/Case 1, or cut into two parts = here);
the residual lower-bound gap is now exactly c_n ≥ 2 and e < 1 (top block cut into ≥ 3 parts). The
pointwise slack W ≤ S(Q_low) that makes this proof work is TIGHT at the cascade (c_n ≥ 2), where
it loses — so c_n ≥ 2 genuinely needs the global coupling to the lower block's surplus S(R) − 1.
