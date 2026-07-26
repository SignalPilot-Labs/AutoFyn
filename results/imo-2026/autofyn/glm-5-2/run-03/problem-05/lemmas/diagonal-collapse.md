# diagonal-collapse (IMO 2026 P5)

**Statement.** For `f:R_{>0}→R_{>0}` satisfying `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ sqrt(x·f(y))` for all `x,y>0`, define `g(y):=f(y)−y`. Then
```
(C1)   f(f(y)) = 2 f(y) − y     for all y > 0,
(C2)   g(y) ≥ 0                 for all y > 0,
```
`g` is invariant along each forward orbit (`g(f(y))=g(y)`), and `fⁿ(y) = y + n·g(y)` for all `n≥0`.

**Proof.** Specialize `x=f(y)` (legitimate: `f(y)>0`). The outer pair `(x,f(y))=(f(y),f(y))` is equal, so QM=AM=GM all collapse to `f(y)`; the chain reads `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`, forcing `(f(f(y))+y)/2=f(y)`, i.e. (C1). Writing `f(t)=t+g(t)`, (C1) gives `(y+g(y))+g(f(y))=y+2g(y)`, so `g(f(y))=g(y)`. Inducting along the recurrence `a_{n+1}=2a_n−a_{n−1}` (characteristic `(r−1)²`) with `a_0=y, a_1=f(y)=y+g(y)` gives `fⁿ(y)=y+n·g(y)`. If `g(y)<0`, `fⁿ(y)→−∞`, leaving `R_{>0}` — contradiction; hence (C2). ∎

**Certified:** round 1, proof-reviewer. sorry-free, statement matches what is proved, no stronger than established. Shared by all three approaches.
