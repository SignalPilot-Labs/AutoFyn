## Status
solved

## Approaches tried
- orbit-distance — SOLVED (reviewer APPROVE, round 1). Derives the FE `f(f(y))=2f(y)-y`, shows
  orbits are arithmetic progressions with orbit-invariant gap `g=f-id ≥ 0`, forces all positive
  gaps equal via a bounded-distance two-orbit comparison (exact residual `4x_k(α-β)+(α-d_k)²`),
  and rules out mixing via a fixed-point covering argument. All algebra reviewer-verified with sympy.
- bound-pinch — partial. Independent analytic envelope/inf-minimizing route. Construction, `f ≥ id`,
  master reformulations (A′)(B′), upper envelope (UENV), propagation lemmas all proved; the constancy
  crux (`g ≤ c everywhere`) reduces to the same bounded-distance comparison and is not closed there.

## Current best
Complete solution: **f(x) = x + c for a constant c ≥ 0**, and these are exactly all solutions.

## Full proof

Squaring both (positive) halves of the chain gives the equivalent, for all x,y>0:
- (A)  2(x² + f(y)²) ≥ (f(x)+y)²
- (B)  (f(x)+y)² ≥ 4x f(y)
Write g(x) := f(x) − x.

### Part I — Construction. For f(x)=x+c:
2(x²+f(y)²)−(f(x)+y)² = (x−y−c)² and (f(x)+y)²−4x f(y) = (x−y−c)² (elementary expansions, sympy-
verified). Both ≥ 0, so the chain holds. If c<0, choosing 0<x<−c gives f(x)<0, violating the
codomain; hence c≥0 is forced, and every c≥0 gives a genuine solution R_>0→R_>0. (This is
QM ≥ AM ≥ GM on {x, f(y)}, equality iff x=y+c.)

### Part II — Functional equation. Put x=f(y)>0. The left member becomes √(f(y)²)=f(y), the right
√(f(y)²)=f(y); the chain reads f(y) ≥ (f(f(y))+y)/2 ≥ f(y), so the middle is squeezed:
  (FE)  f(f(y)) = 2f(y) − y  for all y>0.

### Part III — Orbits are APs; g orbit-invariant; g≥0. From (FE): g(f(y))=f(f(y))−f(y)=f(y)−y=g(y).
For x₀=y, x_{n+1}=f(x_n): (FE) gives x_{n+2}=2x_{n+1}−x_n, so consecutive differences are constant
=g(y), whence f^n(y)=x_n=y+n·g(y) and g(x_n)=g(y). Each x_n∈R_>0; if g(y)<0 then x_n→−∞, impossible.
Hence g(y) ≥ 0, i.e. f(y) ≥ y, for all y>0.

### Part IV — Single-gap crux. Claim: if g(a)=α>0 and g(b)=β>0 then α=β. Set x_k=f^k(a)=a+kα→+∞,
f(x_k)=x_k+α. Let m_k=round((x_k−b)/β)≥0 (for large k), y_k=f^{m_k}(b)=b+m_kβ, so
|d_k|:=|x_k−y_k|≤β/2, f(y_k)=y_k+β. Apply (B) to (x_k,y_k); using y_k=x_k−d_k the residual is exactly
  (f(x_k)+y_k)²−4x_k f(y_k) = 4x_k(α−β) + (α−d_k)² ≥ 0   (sympy-verified identity).
The square (α−d_k)² is bounded (|d_k|≤β/2), while if α<β then 4x_k(α−β)→−∞, forcing the LHS negative
for large k — contradiction. So α≥β; by the symmetric argument (orbit of b out to ∞, point of a's
orbit within α/2) β≥α. Hence α=β. Consequently every positive value of g equals one constant c≥0, and
g(t)∈{0,c} for all t.

### Part V — No mixing. Either f has no fixed point (all g(t)>0, hence all =c>0, so f=x+c), or f has a
fixed point a (g(a)=0). In the latter case suppose some point has positive gap c>0. Apply (A) to (b,a)
with f(a)=a, f(b)=b+c: 2(b²+a²)−(b+c+a)² = (b−a)² − (2c(a+b)+c²) ≥ 0 gives (b−a)² > c², i.e. |b−a|>c
for every positive-gap b. Contrapositive: any s>0 with |s−t|≤c and t a fixed point is itself fixed
(same derivation for any fixed point t). Stepping from a to any target s>0 along the segment
[min(a,s),max(a,s)]⊂(0,∞) in N steps of size |delta|=|s−a|/N≤c shows every point is fixed —
contradicting the existence of a positive gap. Hence g≡0, f=id (c=0).

### Part VI — Conclusion. Every solution is f(x)=x+c with c≥0; conversely each such f solves the chain
(Part I), with both inequalities reducing to (x−y−c)²≥0. Therefore the complete solution set is
  **f(x) = x + c,  c ≥ 0.**  ∎
