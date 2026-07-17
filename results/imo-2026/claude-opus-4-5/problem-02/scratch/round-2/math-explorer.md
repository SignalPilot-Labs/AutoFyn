# Math Explorer Report — IMO 2026 P2 (Algebraic Gap Closure)

## imo-2026-02

- **Distinct openings:**
  1. **MAIN FINDING (gap is closed):** Explicit polynomial identity F·T = c²(S+μH₂)·C2_q − b²(S+νH₃)·C3_q verified by SymPy for arbitrary b,c,α. Since C2_q=0 and C3_q=0 on the constraint variety, F·T=0, and F≠0 for valid configs gives T=0 hence OM=ON.
  2. **Decoupling insight:** Under parameterization k=b(1-μe^{-iα}), l=c(1-νe^{iα}) (from C1), the conditions C2 and C3 **fully decouple**: C2 = μ|c|²·C2_q where C2_q = Fν²+Gν+H₂ has NO μ dependence; C3 = ν|b|²·C3_q where C3_q = Fμ²+Gμ+H₃ has NO ν dependence. The same F and G appear in both quadratics.
  3. **Sequential ideal membership proof:** T mod C2_q (as polynomial in ν) gives linear remainder r₁(μ)ν+r₀(μ); then r₁ mod C3_q = 0 and r₀ mod C3_q = 0. This sequential reduction is the machine proof (confirmed general for arbitrary b,c).

- **Candidate technique(s):** Parameterized ideal membership — write k,l via C1 parameterization, reduce the constraint system to two decoupled univariate quadratics, then exhibit an explicit polynomial identity proving T lies in the ideal.

- **Cheap-kill candidates:** The decoupling is the "kill": C2 depends only on ν (after factoring μ), C3 depends only on μ (after factoring ν). This means the variety V(C2,C3) is isomorphic (locally) to a product of two quadratic curves, and T=0 on their intersection follows from the clean certificate.

- **Knowledge-base entries to use:** Circumcenter formula in complex plane (knowledge_base.md "Coordinates / complex / barycentric"); directed angle "ratio is real" encoding; ideal membership via sequential reduction (Groebner/division).

- **Analogous past problems (cruxes):** Not searched (gap is now closed; searching analogues is unnecessary).

- **Prior progress:** Both built approaches (complex-identity, power-balance) established the reformulation OM=ON ↔ T=0 on V(C2,C3). Gap was: prove T=0 algebraically. That gap is now closed with an explicit certificate.

- **Dead ends (do not retry):**
  - Groebner basis in REAL coordinates [kr,ki,lr,li]: T is NOT in the ideal ⟨C1,C2,C3⟩ over ℝ[kr,ki,lr,li]. This fails because the "Im=0" conditions don't capture the full structure of the variety. Do not retry.
  - Direct numerical verification as proof: not accepted by reviewer.

- **Small-case / intuition notes (for builder reference):**
  - For b=2, c=3+i: certificate gives P1=10(μD₂-1)·C2_q, P2=-4(S+νH₃)·C3_q [verified]
  - For b=3, c=1+2i: certificate verified identically
  - For ALL combinations of roots of C2_q AND C3_q: OM-ON < 10^{-14} (22+ tested configs)
  - Vieta's formulas: ν₁+ν₂ = -G/F = μ₁+μ₂ (sum of roots is SAME for both quadratics!) — elegant structural feature

---

## Complete Proof Structure (for proof-builder)

**Notation:** A=0, B=b, C=c in complex plane. M=b/2, N=c/2. R=Re(bc̄), S=Im(bc̄), b²=|b|², c²=|c|².

**Parameterization (from C1):** Set k=b(1-μe^{-iα}), l=c(1-νe^{iα}). Then (k-b)(l-c)/(bc) = μν > 0 ∈ ℝ₊, so C1 holds automatically. Define F = 2(R sinα - S cosα).

**Decoupling theorem:** 
- C2 = Im[(k-b)(2l-c)·conj((l-b)c)] = μc²·C2_q where C2_q = F·ν² + G·ν + H₂ (quadratic in ν, G and F depend only on b,c,α)
- C3 = Im[b(k-c)·conj((l-c)(2k-b))] = νb²·C3_q where C3_q = F·μ² + G·μ + H₃ (quadratic in μ, SAME F and G)
- H₂ = F/2 - b²sinα, H₃ = F/2 - c²sinα

**Algebraic certificate (the key):** The following polynomial identity holds for ALL μ,ν,b,c,α (verified by SymPy):
```
F·T = c²·(S + μH₂)·C2_q − b²·(S + νH₃)·C3_q
```
where T = |k|²[d,l] - |l|²[d,k] + D·(c²-b²)/2 is the target polynomial (T=0 ↔ OM=ON).

**Conclusion:** On the constraint variety (C2_q=0, C3_q=0, μ>0, ν>0), both terms on the RHS vanish, so F·T=0. For valid geometric configurations, F=2Im(b̄c·e^{iα})≠0 (since K,A,L form a non-degenerate triangle). Therefore T=0, i.e., OM=ON. **QED**

**The builder must:**
1. Verify the polynomial identity F·T = c²(S+μH₂)C2_q - b²(S+νH₃)C3_q (symbolic expansion, ~1 second in SymPy)
2. Derive C2_q and C3_q from the angle conditions (show they have same F,G)  
3. Show F≠0 for valid configs (geometrically: F=0 iff A,K,L are collinear, contradicting non-degeneracy)
4. Chain the steps to conclude OM=ON
EOF
echo "Main report written."