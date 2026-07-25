# Lemma L10 — Matching value identities (β = even-rank sum = ∫⌊N/2⌋) and the β-split

**Status:** CERTIFIED (proof-reviewer, round 4). Derived from certified L3, L4; re-verified
numerically (0 mismatches: β=matching vs even-rank sum vs ∫⌊N/2⌋ over 3000 random multisets;
β-split over 2000 random Q,C). Source: alternating-sum-potential §2a, §5(O3).

For a finite multiset with descending sort y_(1) ≥ … ≥ y_(m), N(t) := #{parts > t}, and
β := max over pairings of Σ_{pairs} min(y_i,y_j) (the L4 quantity, with S = sum − 2β).

**(a) Matching identity.**
  β = Σ_{i≥1} y_(2i)  (even-rank sum)  = ∫_0^∞ ⌊N(t)/2⌋ dt.

**Proof.** By L4 the maximum is attained by the consecutive pairing (y_(1),y_(2)),(y_(3),y_(4)),…,
whose pair-minima are the even-ranked parts y_(2i); hence β = Σ_{i≥1} y_(2i). By layer-cake
(L3) each part y_(2i) = ∫_0^∞ 1[y_(2i) > t] dt, and #{even ranks with y_(2i) > t} =
#{i : 2i ≤ N(t)} = ⌊N(t)/2⌋, so summing gives β = ∫_0^∞ ⌊N(t)/2⌋ dt. ∎

**(b) β-split identity.** For any partition of the parts into sub-multisets Q and C,
  β(Q ⊔ C) = β(Q) + β(C) + W,  W := meas{ t : N_Q(t) odd ∧ N_C(t) odd } ≥ 0.

**Proof.** With N_{Q⊔C} = N_Q + N_C, the elementary floor identity
⌊(a+b)/2⌋ − ⌊a/2⌋ − ⌊b/2⌋ = 1[a odd ∧ b odd] applied pointwise to (a,b)=(N_Q(t),N_C(t)) and
integrated via (a) gives the claim. It is the exact dual of the L3 XOR identity
S(Q⊔C) = S(Q) + S(C) − 2W (indeed S = sum − 2β). ∎

**Remark (for the LB reforge).** When B refines P_n = {2^0,…,2^n} (sum D_n = 2^{n+1}−1), every
refinement has sum D_n, so S(B) = D_n − 2β(B); hence S(B) ≥ 1 ⟺ β(B) ≤ 2^n − 1. This reforge is
correct but does NOT by itself close the lower bound — it is exactly equivalent to the layer-cake
residual S(B) ≥ 1.
