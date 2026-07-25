# Lemma (d takes at most one positive value)

For every solution f, the set {d(x):d(x)>0} has at most one element; combined with d≥0,
d(x)∈{0,b} for a single b≥0.

**Key identity (R-test).** For p,q>0 with a=d(p), b=d(q), substituting (x,y)=(f(p),q) into R:
$(p+2a+q)^2-4(p+a)(q+b)=(p-q)^2+4(a-b)(p+a)$, so R ⟺ $(p-q)^2\ge4(b-a)(p+a)$.

**Proof.** If distinct positive a<b occur at p₀,q₀, the orbits Pₘ=p₀+ma (d=a), Qₙ=q₀+nb (d=b) are
admissible. With a>0, Pₘ→∞; choosing n=⌊(Pₘ−q₀)/b⌋ gives 0≤Pₘ−Qₙ<b, so LHS<b², while the R-test
RHS 4(b−a)(Pₘ+a)→∞. Contradiction. ∎

Certified round 1 (R-test identity sympy-verified and re-derived).
