# Lemma: D0-irreducible

**Statement.** The cubic
```
D₀(L) = b·lx·v − b·ly·u + 2·lx²·ly − lx²·v − 2·lx·ly·u + 2·ly³ − 3·ly²·v + ly·u² + ly·v²
```
is irreducible over `Q[b,u,v,lx,ly]`. Consequently `(D₀)` is a height-one prime in the UFD `Q[b,u,v,lx,ly]`, and the discrete valuation `v_{D₀}` is well-defined.

**Proof.** As a polynomial in `ly` over `Q(b,u,v,lx)` (leading coefficient `2`, a unit in `Q`), `D₀` is a cubic; it is reducible iff it has a root in `Q(b,u,v,lx)`. `sympy.factor(D₀, domain=QQ.frac_field(b,u,v,lx))` returns `D₀` unfactored, so it has no linear-in-`ly` factor. The content (gcd of the `ly`-coefficients `2, −3v, −bu+2lx²−2lxu+u²+v², blxv−lx²v`) is `1`, so `D₀` is primitive; by Gauss's lemma no factor of `ly`-degree 0 exists either. Cross-check: at `b=1,u=0,v=2,lx=−2`, `D₀` becomes `2(ly³−3ly²+6ly−6)`, irreducible over `Q` (rational-root candidates `±1,±2,±3,±6` are all non-roots). ∎

**Reviewer note (round 2).** Independently re-verified: `sp.factor(D0, domain=QQ.frac_field(b,u,v,lx))` returns `D₀` unfactored; specialization `b=1,u=0,v=2,lx=−2` gives `2(ly³−3ly²+6ly−6)`, irreducible by rational-root test.

**Source.** `analytic-resultant-cert` Section 4 (Lemma 2). Reviewer-certified round 2.
