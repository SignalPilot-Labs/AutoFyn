# Lemma: Orbit linearity and nonnegativity of h = f - id

**Statement.** Under the pinch hypotheses (see pinch-identity), with h = f - id:
h(f(y)) = h(y), f^n(y) = y + n h(y) for all n>=1, and h(y) >= 0 for all y>0.

**Proof.** From f(f(y)) = 2 f(y) - y, h(f(y)) = f(f(y)) - f(y) = f(y) - y = h(y). Induction:
f^{n+1}(y) = f^n(f(y)) = f(y) + n h(f(y)) = y + (n+1) h(y). If h(y)<0 then f^n(y) -> -infinity,
contradicting f>0; hence h>=0. ∎

Certified round 1 (proof-reviewer). Used by modulus-telescope and two-sided-orbit.
