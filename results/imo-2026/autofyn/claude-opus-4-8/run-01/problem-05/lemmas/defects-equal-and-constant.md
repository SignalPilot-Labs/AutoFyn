# Lemma `defects-equal-and-constant`

**Statement.** For any f:(0,∞)→(0,∞) satisfying the P5 sandwich (†), g:=f−id is a constant c≥0.

**Proof.** By `sandwich-collapse`, g≥0, orbits are APs fⁿ(y)=y+n g(y) with g constant on each orbit.
By `off-diagonal-lever`, (a−b)²+2(a+b)g(a)+g(a)²≥4a g(b).
(i) *All positive defects equal.* If g(a)=s>0, g(b)=t>0, take Aₖ=a+k s→∞ and interleave
Bₖ=b+⌊(Aₖ−b)/t⌋·t so 0≤Aₖ−Bₖ<t; the lever at (Aₖ,Bₖ) gives 4Aₖ t<t²+4Aₖ s+s², so t≤s in the
limit; symmetry gives s=t. Hence g(y)∈{0,c} for a single c≥0.
(ii) *No coexistence.* If c>0, Z={g=0}, P={g=c}: the lever at (z∈Z,b∈P) gives the cross-constraint
(b−z)²≥4cz, which makes both Z and P open (with the explicit radii ε=min(z/2,2√(cz)) for Z and
ε=min(b/2,√(cb)) for P). By connectedness of (0,∞) one of Z,P is empty. Thus g≡0 or g≡c.

**Certified** (proof-reviewer, round 1): interleaving limit and both openness inequality chains
independently checked (algebra + numerics).
