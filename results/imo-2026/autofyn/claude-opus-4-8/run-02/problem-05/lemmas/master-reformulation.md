# Lemma: Master reformulations (A′),(B′) (certified round 1)

**Statement.** For f: R_>0→R_>0 and g=f−id, the two squared forms of the chain,
(A) 2(x²+f(y)²) ≥ (f(x)+y)² and (B) (f(x)+y)² ≥ 4x f(y), are exactly equivalent (for all x,y>0) to
- (A′) (x−y)² + 4y·g(y) + 2g(y)² − 2(x+y)·g(x) − g(x)² ≥ 0,
- (B′) (x−y)² + g(x)² + 2(x+y)·g(x) − 4x·g(y) ≥ 0.

**Proof.** Substitute f(x)=x+g(x), f(y)=y+g(y) into (A),(B) and expand; sympy confirms both
differences are identically 0. ∎

Certified: reviewer sympy-verified (A′,B′ diffs = 0). From bound-pinch; reusable by any approach.
