# Lemma: Antipode equivalence — OM = ON ⟺ A* on perp-bisector of BC

**Setup.** Place `A = 0 ∈ ℂ`. Let `O` be the circumcentre of `△AKL` and `A* := 2O − A = 2O`
the antipode of `A` on `⊙(AKL)`. Let `M, N` be any points; write `X·Y := Re(X·Ȳ)`,
`|X|² = X·X`. (In the problem `M = b/2, N = c/2`, midpoints of `AB, AC`.)

**Statement.** With `B = b, C = c`:
```
OM = ON  ⟺  A*B = A*C  ⟺  A*·(c − b) = (|c|² − |b|²)/2  ⟺  A* on the perpendicular bisector of BC.
```
Moreover (antipode–power bridge) for the circle `ω = ⊙(AKL)` with centre `O`, radius `R = |O−A|`,
and diameter `AA*`, every point `X` satisfies `(X−A)·(X−A*) = |X−O|² − R² = pow_ω(X)`; hence with
`A = 0`, `OM = ON ⟺ pow_ω(B) − pow_ω(C) = (AB² − AC²)/2`.

**Proof.** Expand differences of squared distances:
`OM² − ON² = |O − M|² − |O − N|² = O·(N − M)·2 ... ` concretely with `M=b/2,N=c/2`,
`OM² − ON² = (|O|² − O·b + |b|²/4) − (|O|² − O·c + |c|²/4) = O·(c − b) + (|b|²−|c|²)/4`,
so `OM = ON ⟺ O·(c−b) = (|c|²−|b|²)/4`.
`A*B² − A*C² = |A*−b|² − |A*−c|² = 2A*·(c−b) + (|b|²−|c|²)`, so
`A*B = A*C ⟺ A*·(c−b) = (|c|²−|b|²)/2`. Since `A* = 2O`, `A*·(c−b) = 2 O·(c−b)`, and the two
right-hand conditions coincide. The perp-bisector of `BC` is `{X : (X−(b+c)/2)·(c−b)=0}`, and
`(b+c)·(c−b)` has real part `|c|²−|b|²`, giving the last equivalence. For the bridge, expand
`(X−A)·(X−A*) = (X−A)·(X−2O+A) = |X−O|² − |O−A|²` using `A*=2O−A`. ∎

**Certification (proof-reviewer, round 2).** Both squared-distance expansions re-derived and
correct; the `A*=2O` cancellation is exact; the perp-bisector and power-of-a-point identities
check out. Verified numerically in `repro_antipode.py` (|OM−ON| and |A*B−A*C| vanish together
< 1e-12). Certified for reuse. Certified from approach `antipode-perp-bisector` Step 1.
