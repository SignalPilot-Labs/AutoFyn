# Lemma EF-OG-reformulation (‡) — group-split of the odd/even competition (certified round 8)

**Setup.** Stray a=0 lower-bound setup: F = R_n-fragments (ΣF = 2^n), G = non-R_n pieces (ΣG = 2^n − 1);
D = 2^{n+1} − 1 = ΣF + ΣG. Sort all pieces weakly decreasing; O, E = odd-/even-rank mass; A = O − E =
D − 2E (§4.4.1). Split by group: O = O_F + O_G, E = E_F + E_G (subscript = group of the piece at that
rank, fixed by any tie-break).

**Statement.** **A ≥ 1 ⟺ E_F ≤ O_G** (even-rank fragment mass ≤ odd-rank G mass). (‡)
Corollary (all-F-odd): **E_F = 0 ⟹ A ≥ 1** (in fact A = 1 + 2O_G).

**Proof.** ΣG = O_G + E_G, so E − ΣG = (E_F + E_G) − (O_G + E_G) = E_F − O_G, independent of tie-break
(E and ΣG are). Since ΣG = 2^n − 1 = (D−1)/2: A = D − 2E ≥ 1 ⟺ E ≤ (D−1)/2 = ΣG ⟺ E_F − O_G ≤ 0. The
corollary: E_F = 0 ⟹ E_F ≤ O_G (O_G ≥ 0) ⟹ A ≥ 1; then A = D − 2E = D − 2(ΣG − O_G) = 1 + 2O_G. ∎

**Verification.** Identities A = D − 2E and E − ΣG = E_F − O_G, and the equivalence A ≥ 1 ⟺ E_F ≤ O_G,
machine-checked over thousands of random sorted arrangements at n = 3,4,5 (0 failures). Tie-break
independent. Reusable for any lower-bound approach.
