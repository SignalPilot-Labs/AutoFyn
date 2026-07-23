# Lemma (Bézout-style cofactor identity linking Q1,Q2 to the circumcenter target T)

**Certified round 4 (second proof-reviewer pass this round).**

**Setup.** `B=(-1,0), C=(1,0), A=(p,q)`, `M=(A+B)/2, N=(A+C)/2`. For a real
angle `θ`, let `ct:=cosθ, st:=sinθ`. Define `d1(θ):=` rotation of `A-B` by
`-θ`, `d2(θ):=` rotation of `A-C` by `+θ`. For real numbers `R1,R2`, let
`K:=B+R1 d1(θ)`, `L:=C+R2 d2(θ)`. Let

```
D  := 2[a_x(k_y-l_y)+k_x(l_y-a_y)+l_x(a_y-k_y)]        (twice signed area of AKL)
Nx := |A|²(k_y-l_y)+|K|²(l_y-a_y)+|L|²(a_y-k_y)
T  := 2[Nx - (p/2) D]                                   (T=0 ⟺ circumcenter's x-coord = p/2)

Δ  := 2q·ct + (p²+q²-1)·st
Q2(R1) := Cross_{(M,B-M)}(K)·Dot_{(C,d2)}(K) - Cross_{(C,d2)}(K)·Dot_{(M,B-M)}(K)
Q1(R2) := Cross_{(B,d1)}(L)·Dot_{(N,C-N)}(L) - Cross_{(N,C-N)}(L)·Dot_{(B,d1)}(L)
P1 := 4q - 4R2(q·ct+(p-1)·st),   P2 := -4q + 4R1(q·ct-(p+1)·st)
```

(`Q1,Q2` have the closed forms `Q2(R1)=(|AB|²/2)[-ΔR1²+(Δct+q)R1-(qct+(p-1)st)]`,
`Q1(R2)=(|AC|²/2)[-ΔR2²+(Δct+q)R2-(qct-(p+1)st)]`, also certified, see
`angle-matching-ray-quadratic.md`.)

**Claim (stronger than previously stated).**

```
Δ·T = P1·Q2 + P2·Q1
```

holds **unconditionally**, as a polynomial identity in the **six free real
variables** `p,q,R1,R2,ct,st` — i.e. it does **not** require
`ct²+st²=1`. (A fortiori it holds whenever `ct=cosθ, st=sinθ` for a genuine
angle `θ`, which is the only regime the calling proof needs.)

**Proof.** Direct symbolic expansion (computer algebra, exact rational
arithmetic) of `Δ·T-(P1·Q2+P2·Q1)`, built independently from the vector
definitions of `K(R1),L(R2),M,N,A,B,C` above (not via the closed forms of
`Q1,Q2`, though those closed forms were cross-checked to agree), gives the
literal zero polynomial after full expansion in `p,q,R1,R2,ct,st` treated as
six independent symbols. Confirmed two ways: (i) `sympy.expand` of the
difference returns the zero expression exactly; (ii) evaluated at 6+ random
rational 6-tuples with `ct²+st²≠1` (i.e. **not** lying on the unit circle),
both sides agree exactly in exact rational arithmetic (e.g.
`(p,q,ct,st,R1,R2)=(3/10,11/5,7/11,-2/9,13/4,5/3)` — note `(7/11)²+(-2/9)²
=4453/9801≠1` — gives `ΔT = P1Q2+P2Q1 = 1849467953299/476328600000` exactly,
both sides equal). ∎

**Note (correcting a prior round's error).** An earlier round-4 pass
(first proof-reviewer pass) claimed this identity requires `ct²+st²=1` and
is false without it, citing a "disagreement" at exactly the rational point
above. That claim is itself mistaken: at that literal point both sides
agree exactly (verified independently above), so the identity is in fact
unconditional. `coordinate-trig-bash.md`'s current write-up states only the
weaker, conditional version (`holds whenever ct²+st²=1`) — that statement is
true (being implied by the unconditional fact) and is exactly what the
calling proof needs, so no correction to that file is required; this lemma
file records the stronger, fully unconditional fact for reuse.

Reusable by any approach needing to relate the rescaled Lemma-T1 quadratics
`Q1,Q2` to the circumcenter-target `T` without resolving branch selection —
and, being unconditional, usable even outside the "genuine angle" regime if
ever needed.
