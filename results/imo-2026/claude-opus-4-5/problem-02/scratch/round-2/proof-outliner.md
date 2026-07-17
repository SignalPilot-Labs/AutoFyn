## imo-2026-02

complex-identity: revise
Target: Prove OM = ON where O is circumcenter of triangle AKL, M = midpoint(AB), N = midpoint(AC)
Technique: Complex algebra with decoupling parameterization + explicit polynomial certificate
Skeleton:
  1. Setup: A=0, B=b, C=c, M=b/2, N=c/2 in complex plane — standard coordinates
  2. From C1, parameterize k = b(1−μe^{−iα}), l = c(1−νe^{iα}) with μ,ν>0 — by directed-angle encoding
  3. Show C2 factors as C2 = μ|c|²·C2_q where C2_q = Fν² + Gν + H₂ is quadratic in ν ONLY — direct expansion
  4. Show C3 factors as C3 = ν|b|²·C3_q where C3_q = Fμ² + Gμ + H₃ is quadratic in μ ONLY — direct expansion
  5. Note F and G are identical in both; compute F = 2Im(b̄c·e^{iα}), H₂ = F/2−|b|²sinα, H₃ = F/2−|c|²sinα
  6. Define target T = |k|²[d,l] − |l|²[d,k] + D·(|c|²−|b|²)/2 where d=b−c, [·,·]=Im, D=Im(k̄l) — circumcenter formula
  7. Verify the polynomial identity F·T = c²(S+μH₂)·C2_q − b²(S+νH₃)·C3_q where S=Im(bc̄) — symbolic expansion
  8. On V(C2_q)∩V(C3_q): RHS=0, so F·T=0. Since F=2Im(b̄c·e^{iα})≠0 for valid configs, T=0 — ideal membership
  9. T=0 is equivalent to OM=ON — Step 6 reformulation
Key lemmas (claim + mechanism):
  - Decoupling: C2_q has no μ, C3_q has no ν — because the μ factor in k−b and ν factor in l−c each factor out completely after expanding the Im(·)=0 condition
  - Certificate identity: F·T = c²(S+μH₂)·C2_q − b²(S+νH₃)·C3_q — verified by direct polynomial expansion (CAS confirms LHS−RHS=0 symbolically for general b,c,α)
  - F≠0: F=0 would force e^{iα} ∥ b̄c, meaning K,L,A collinear or degenerate — contradicts K inside △BMC, L inside △BNC
Open gaps: Steps 3-5 (derive decoupling), Step 7 (verify certificate expansion)
Cases to cover: none (single identity, no casework)
Watch out for: The certificate has factor F in front; must verify F≠0 for valid configurations (Step 8)

---

power-balance: advance
Target: Same as above (OM = ON)
Technique: Power of a point + same decoupling certificate
Justification: This approach is structurally equivalent to complex-identity after the explorer breakthrough. The power formulation P(M)=P(N) is just T=0 rewritten. Rather than duplicate the certificate proof, merge insights: advance power-balance by importing the certificate from complex-identity once proved.
Action: Do not build separately; wait for complex-identity to close the gap, then import the certificate.

---

sigma-symmetry: drop
Justification: The B↔C symmetry only gives OM=ON trivially for isoceles triangles. Extending to general ABC via "algebraic identity principle" or continuity requires the same polynomial identity that complex-identity now proves directly. No independent value — subsumed by the certificate approach.

---

dot-product-identity: drop
Justification: The dot product reformulation Re((c−b)·Ō)=(|c|²−|b|²)/4 is exactly the target T=0. This approach had no route to close the gap; the decoupling + certificate from complex-identity now provides that route. Subsumed.

---

## Build set

build set: complex-identity

## Rationale

The explorers' discovery is decisive: the decoupling of C2 and C3 into univariate quadratics, plus the explicit polynomial certificate F·T = c²(S+μH₂)·C2_q − b²(S+νH₃)·C3_q, closes the algebraic gap. This is a finite verification (polynomial expansion), not numerical evidence.

Only complex-identity needs building. The skeleton above gives the builder a clear 9-step path. Power-balance adds nothing new — same gap, same certificate. The other two approaches (sigma-symmetry, dot-product-identity) are subsumed and should be dropped from active consideration.

One approach to solved this round.
