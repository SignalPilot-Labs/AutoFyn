# Lemma: FE-collapse (certified round 1)

**Statement.** If f: R_>0 → R_>0 satisfies the chain
√((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y)) for all x,y>0, then
  f(f(y)) = 2f(y) − y   for all y>0.

**Proof.** Substitute x=f(y)>0. The left member becomes √((f(y)²+f(y)²)/2)=√(f(y)²)=f(y); the right
member becomes √(f(y)·f(y))=f(y). The chain becomes f(y) ≥ (f(f(y))+y)/2 ≥ f(y), so the middle is
squeezed to f(y), giving f(f(y))=2f(y)−y. ∎

Certified: reviewer verified the substitution and squeeze; used in orbit-distance Part II.
