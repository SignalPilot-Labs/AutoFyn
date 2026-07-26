# cross-inequalities (IMO 2026 P5)

**Statement.** For `f:R_{>0}→R_{>0}` satisfying `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y))` for all `x,y>0`,
```
(I)    2·x·f(y)  ≤  y² + f(x)²,
(II)   2·y·f(x)  ≤  x² + f(y)²,
```
for all `x,y>0`.

**Proof (non-circular).** Let `A:=(f(x)+y)/2` (the AM of the pair `(y,f(x))`). By the universal QM-AM-GM chain on `(y,f(x))` (no hypothesis on `f` beyond `f>0`): `A ∈ I₂ := [√(yf(x)), √((y²+f(x)²)/2)]`. By the problem's hypothesis: `A ∈ I₁ := [√(xf(y)), √((x²+f(y)²)/2)]`. The single witness `A∈I₁∩I₂` gives `√(xf(y))=G₁ ≤ A ≤ Q₂=√((y²+f(x)²)/2)` (so `2xf(y)≤y²+f(x)²`, (I)) and `√(yf(x))=G₂ ≤ A ≤ Q₁=√((x²+f(y)²)/2)` (so `2yf(x)≤x²+f(y)²`, (II)). The upper bound `A≤Q₂` used is the *universal* QM≥AM on `(y,f(x))`, not the swapped left hypothesis. ∎

**Caveat (proven in `swap-cross-inequalities`).** This lemma is a *consequence* of the hypotheses but is strictly weaker than the master bound (★): its orbit amplification is asymptotically an AM-GM-level identity (degree-2 slack `=(nd₁−md₂)²≥0`), and its local two-sided bound squeezes `g` only at zeros of `g`, not at nonzero points. It cannot by itself force `g` constant; use `master-bound` instead.

**Certified:** round 1, proof-reviewer. sorry-free; statement correct and no stronger than proved; the weakness caveat is part of the lemma's reusable documentation.
