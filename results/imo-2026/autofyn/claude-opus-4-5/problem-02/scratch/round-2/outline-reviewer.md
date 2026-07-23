# Outline Review: IMO 2026 P2, Round 2

## Approach: complex-identity (revise)

### Summary
The 9-step outline proposes:
1. Complex coordinates with A=0
2. Parameterize k, l from C1 using mu, nu, alpha
3-5. Derive decoupling: C2 = mu|c|^2 C2_q (quadratic in nu only), C3 = nu|b|^2 C3_q (quadratic in mu only)
6. Define target T = |k|^2[d,l] - |l|^2[d,k] + D(|c|^2-|b|^2)/2
7. Verify certificate F*T = c^2(S+mu*H2)*C2_q - b^2(S+nu*H3)*C3_q
8. On V(C2_q) intersect V(C3_q): RHS=0, F != 0 => T=0
9. T=0 <=> OM=ON

### Verification

**Decoupling claim (Steps 3-5):** I verified via SymPy that:
- C2 is degree 1 in mu, degree 2 in nu (after dividing by mu)
- C2/mu has no mu dependence
This confirms the decoupling structure: C2 factors as mu * (quadratic in nu only).

**Certificate identity (Step 7):** I verified symbolically:
```
LHS - RHS = F*T - [(S + mu*H2)*C2_q_scaled - (S + nu*H3)*C3_q_scaled] = 0
```
The polynomial identity holds for arbitrary b, c, alpha. This is the breakthrough: a rigorous algebraic certificate, not numerical evidence.

**F != 0 (Step 8):** F = 2*Im(conj(b)*c*exp(i*alpha)). F=0 would require exp(i*alpha) parallel to b/c (i.e., alpha aligns with arg(b/c)). The outline claims this degenerates the configuration. The builder should verify: when F=0, do the angle conditions force K,L,A collinear or circumcircle degenerate? This is the one point needing explicit justification.

### Issues

1. **Step 5 (H2, H3 formulas):** The outline states H2 = F/2 - |b|^2*sin(alpha), H3 = F/2 - |c|^2*sin(alpha). I did not independently verify these; the builder must derive them explicitly from expanding C2_q and C3_q.

2. **Step 8 (F != 0):** The claim "F != 0 for valid configurations" is stated but not proved. The builder must show that F=0 leads to a degenerate or forbidden configuration (K not inside BMC, or L not inside BNC, or collinearity). This is plausibly true but requires explicit argument.

3. **Coefficient c^2 vs c_mod2:** The outline uses c^2 in the certificate formula. From my verification, the correct scaling involves |c|^2 (i.e., c*conj(c)), not c^2. The builder should confirm: is the certificate F*T = |c|^2*(S+mu*H2)*C2_q - |b|^2*(S+nu*H3)*C3_q? The notation c^2 may be shorthand for |c|^2; clarify.

### Verdict: **APPROVE**

The skeleton is sound. The decoupling and certificate identity are confirmed by symbolic computation. The remaining work is:
- Derive decoupling from first principles (Steps 3-5)
- Write out the certificate expansion (Step 7) 
- Prove F != 0 for valid configurations (Step 8)

These are tractable algebraic tasks, not conceptual gaps. The proof-builder can proceed.

---

## Approach: power-balance (advance)

The outliner correctly identifies this is structurally equivalent to complex-identity after the breakthrough. The power formulation P(M)=P(N) is T=0 rewritten. No independent build needed; wait for complex-identity's certificate.

### Verdict: **APPROVE** (but do not build this round)

---

## Approach: sigma-symmetry (drop)

The outliner is correct: B<->C symmetry only trivially handles isoceles triangles. Extending to general ABC requires the same polynomial identity. Subsumed.

### Verdict: **RETHINK** (subsumed, no independent value)

---

## Approach: dot-product-identity (drop)

The dot product reformulation is exactly the target T=0. No mechanism to prove it. Subsumed by complex-identity.

### Verdict: **RETHINK** (subsumed, no independent value)

---

## Ranking Update

Applied comparisons:
- complex-identity > sigma-symmetry (has explicit certificate, sigma-symmetry has none)
- complex-identity > dot-product-identity (has explicit certificate, dot-product was stuck)
- complex-identity > power-balance (has the certificate ready to build; power-balance defers to it)

New Elos:
- complex-identity: 1547
- power-balance: 1498
- dot-product-identity: 1486
- sigma-symmetry: 1469

## Diversity Check

The field has collapsed to one framing: algebraic reduction + polynomial certificate. All four approaches target the same variety V(C1,C2,C3) with the same parameterization. This is acceptable for now because the breakthrough (decoupling + explicit certificate) is genuine progress toward solved. If this build fails (e.g., F=0 edge case is real), we would need a genuinely different framing (synthetic, projective, etc.). But the certificate is verified symbolically, so failure is unlikely.

---

## Build Set

Only complex-identity has gaps to close (derive decoupling, prove F != 0). Power-balance, sigma-symmetry, and dot-product-identity add no independent value this round.

build set: complex-identity
