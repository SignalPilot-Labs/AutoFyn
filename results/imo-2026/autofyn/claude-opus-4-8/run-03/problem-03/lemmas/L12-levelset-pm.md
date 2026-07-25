# Lemma L12 — Level-set (crossing) form of the parity-vs-mean gap

**Status:** CERTIFIED (proof-reviewer, round 5). Derived from L3-type layer decompositions.
Sources: induction-peel §3.4 (R4) and interlacing-bijection §2 (Lemma IB-1) — the two are the
SAME identity, independently derived; re-verified pointwise and numerically (0 mismatches over
3000 random Q_low/C).

**Setup.** Let D(t) be any integer-valued step function on (0,∞) that vanishes for large t
(e.g. D := N_{Q_low} − N_C for an XOR split). For integers j ≥ 1 put
  A_j := meas{ t : D(t) ≥ j },   B_j := meas{ t : D(t) ≤ −j }.

**Identity.**
  ∫_0^∞ 1[D(t) odd] dt − ∫_0^∞ D(t) dt = 2·( Σ_{m≥1} B_{2m−1} − Σ_{m≥1} A_{2m} ).

**Consequence.** With f(d) := 1[d odd] − d,
  (PM)  ∫ 1[D odd] ≥ ∫ D   ⟺   Σ_{m≥1} B_{2m−1} ≥ Σ_{m≥1} A_{2m},
i.e. the (gap-length-weighted) time D spends at ODD NEGATIVE depths dominates the time it spends
at EVEN POSITIVE heights. Equivalent floor/ceiling form: ∫ ⌈D^-/2⌉ ≥ ∫ ⌊D^+/2⌋
(D^± := max(±D,0)).

**Proof.** It suffices to prove the pointwise identity
  f(d) = 2( Σ_{m≥1} 1[d ≤ −(2m−1)] − Σ_{m≥1} 1[d ≥ 2m] )  for every integer d,
then integrate (all sums finite as D is bounded). Layer decomposition of the signed value:
D = Σ_{j≥1}(1[D≥j] − 1[D≤−j]), giving ∫D = Σ_{j≥1}(A_j − B_j). And meas{D=j}=A_j−A_{j+1},
meas{D=−j}=B_j−B_{j+1}, so ∫1[D odd] = Σ_{j odd}(A_j−A_{j+1}) + Σ_{j odd}(B_j−B_{j+1}) =
Σ_{j≥1}(−1)^{j+1}A_j + Σ_{j≥1}(−1)^{j+1}B_j. Subtracting, the coefficient of A_j is
(−1)^{j+1}−1 = 0 (j odd), −2 (j even); of B_j is (−1)^{j+1}+1 = 2 (j odd), 0 (j even). Hence
∫1[D odd] − ∫D = −2Σ_{m≥1}A_{2m} + 2Σ_{m≥1}B_{2m−1}. ∎

**Verification of the pointwise form** (checked termwise): d=0→0; d=1→0; d=2→−2; d=3→−2;
d=4→−4; d=−1→2; d=−2→2; d=−3→4 — all match f(d) = 1[d odd] − d.

**Scope note.** This is an EQUIVALENT recasting of (PM), not a closure: it converts the residual
into a super/sub-level-set (crossing) comparison of the single walk D. The general inequality
Σ B_{2m−1} ≥ Σ A_{2m} remains the OPEN lower-bound crux. Proven sub-cases in this language:
R2 (D ≤ 1 a.e. ⟹ RHS-pile Σ A_{2m} = 0) and L9 (Q_low even ⟹ overlap controlled by C).
