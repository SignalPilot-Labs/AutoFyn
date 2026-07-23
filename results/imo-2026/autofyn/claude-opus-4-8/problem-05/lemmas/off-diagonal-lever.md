# Lemma `off-diagonal-lever` (∗)

**Statement.** For any f:(0,∞)→(0,∞) satisfying the P5 sandwich (†), writing g:=f−id,
  (a−b)² + 2(a+b)g(a) + g(a)² ≥ 4a·g(b)   for all a,b>0.

**Proof.** Squaring the right half of (†) gives (R²) (f(x)+y)²≥4x f(y). Substitute f=id+g at
(x,y)=(a,b): the exact identity (a+g(a)+b)²−4a(b+g(b)) = (a−b)²+2(a+b)g(a)+g(a)²−4a g(b) (both sides
expand to the same polynomial, sympy-verified) and (R²)≥0 give the claim.

**Certified** (proof-reviewer, round 1): identity sympy-verified to 0.
