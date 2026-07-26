## Status
solved

## Approaches tried
- `a-star-cyclicity` — APPROVED (round 2). Complete proof via Gröbner-basis
  ideal-membership certificate. Reflect A across `p.bis(MN)` to get A*; prove
  `O∈p.bis(MN)` directly (equiv. to `A,K,L,A*` concyclic when B≠C) by showing
  `Π := num(O_x − (3P_B+P_C)/4) ∈ ⟨F1,F2⟩` over `Q[p,q,r,P_B,P_C]` (grevlex),
  where F1,F2 encode the two residual angle conditions `∠LBK=β, ∠LCK=γ` via
  `cot∠(s,t)=(s·t)/det(s,t)`. Certificate independently re-verified by the
  reviewer: 6-element Gröbner basis, exact 0 remainder; K,L sine-rule formulas,
  Lemma 1, Lemma 2, the `Δ_num=−(P_B−P_C)·Π` factorisation, the degenerate
  `B=C` case, and the inside-component sufficiency all checked.
- `analytic-resultant` — RETHINK (round 2). Outline only, no proof built; same
  algebraic crux as `a-star`, which already closed it. Strictly dominated.
- `miquel-spiral` — RETHINK (round 2). Numeric gate failed: the conjectured
  spiral/indirect-similarity centre `S₀` and the Miquel point of
  `(AB,AC,BK,CL)` are neither `O` nor on `p.bis(MN)` on any scalene triangle.
  Load-bearing transformation does not exist; kept as a recorded negative.

## Current best
Complete proof (see Full proof). The heart is the exact Gröbner ideal-membership
`Π∈⟨F1,F2⟩` (6-element basis, zero remainder over Q) — a deterministic finite
certificate, uniform over all triangles including the degenerate `B=C` case.

## Full proof

**Notation.** Let the (unsigned) angle alphabet be
`α:=∠KBA=∠ACL, β:=∠LBK=∠LNC, γ:=∠LCK=∠BMK`,
and write `A,B,C` also for the angles of `△ABC` (`A+B+C=π`). The inside
hypotheses fix the ray orderings `BC→BL→BK→BA` at `B` and `CB→CK→CL→CA` at `C`
(counterclockwise), so `∠LBA=α+β`, `∠ACK=α+γ`, and the workhorse triangles have
angle triples `△BMK=(α,γ,π−α−γ)`, `△CNL=(α,β,π−α−β)`.

---

### Lemma 1 (midpoint-cevian cotangent formula)

In `△XYZ`, let `W` be the midpoint of `XY`, `θ=∠XYZ`, `δ=∠YWZ`. Then
`cot∠YXZ = cot θ + 2 cot δ`.

*Proof.* Put `ψ=∠YXZ`. Sine rule in `△XYZ`: `YZ = XY sin ψ / sin(θ+ψ)` (angle at
`Z` is `π−θ−ψ`). In `△YWZ` (`WY=XY/2`, `∠YWZ=δ`, `∠WYZ=θ`): sine rule gives
`YZ = (XY/2) sin δ / sin(θ+δ)`. Equating,
`2 sin ψ sin(θ+δ) = sin δ sin(θ+ψ)`; dividing through by
`sin ψ sin δ sin θ` and collecting yields `cot ψ = cot θ + 2 cot δ`. ∎

Applying Lemma 1 to `△ABK` (`W=M, θ=α, δ=γ`) and `△ACL` (`W=N, θ=α, δ=β`):
`cot∠BAK = cot α + 2 cot γ`, `cot∠LAC = cot α + 2 cot β`. (These make the
cotangent parametrisation below rational.)

---

### Lemma 2 (the point A* and the perpendicular-bisector identity)

Let `D` be the midpoint of `BC` and `F` the foot of the perpendicular from `A`
to `BC`. Set `A* := A + (D−F)`. Then (a) `AA*∥BC` and the perpendicular foot of
`A*` onto `BC` is `D`; (b) `A*` is the reflection of `A` across `p.bis(MN)`, so
`p.bis(AA*) = p.bis(MN)`; (c) `A*=A ⟺ B=C`.

*Proof.* Apply a similarity `B↦(0,0), C↦(P_B+P_C,0), A↦(P_B,1)` where
`P_B:=cot B, P_C:=cot C` (existence: scale the standard placement
`A=(c cos B, c sin B)` by `1/(c sin B)`, using
`sin A = (cot B + cot C) sin B sin C`). Reflections, midpoints, perpendicular
bisectors, cyclicity, and angle equalities are similarity-invariant.

Then `M=(P_B/2,1/2)`, `N=(P_B+P_C/2,1/2)`, `D=((P_B+P_C)/2,0)`, `F=(P_B,0)`,
hence `A*=((P_B+P_C)/2,1)`. So `AA*` is horizontal (`∥BC`) and the foot of `A*`
on `BC` is `D` — (a). The midpoint of `MN` is `((3P_B+P_C)/4,1/2)` and `MN` is
horizontal, so `p.bis(MN)` is the vertical line `x=(3P_B+P_C)/4`; the midpoint of
`AA*` is `((3P_B+P_C)/4,1)`, so `p.bis(AA*)` is the same vertical line — (b).
Finally `A*=A ⟺ (P_B+P_C)/2=P_B ⟺ P_C=P_B ⟺ C=B` — (c). ∎

The conclusion `OM=ON` is equivalent to `O∈p.bis(MN)`, i.e. (Lemma 2) to
`O∈p.bis(AA*)`. When `B≠C` (`A*≠A`) this is equivalent to `A*∈circle(AKL)`,
i.e. to the concyclicity of `A,K,L,A*`. We prove the uniform statement
`O∈p.bis(MN)` directly below; the cyclicity is its geometric reading when
`B≠C`.

---

### Lemma 3 (the crux: `O∈p.bis(MN)` — uniform ideal-membership certificate)

Keep the normalisation of Lemma 2, and put `p:=cot α, q:=cot β, r:=cot γ`. Then

```
A=(P_B,1), B=(0,0), C=(P_B+P_C,0), A*=((P_B+P_C)/2,1),
K=((P_B p+1)/(2(p+r)),  (p−P_B)/(2(p+r))),
L=(P_B+P_C − (P_C p+1)/(2(p+q)),  (p−P_C)/(2(p+q))).
```

*Derivation.* In `△BMK` (`∠MBK=α` since `M∈BA`, `∠BMK=γ`, `∠BKM=π−α−γ`): sine
rule `BK = BM·sin γ/sin(α+γ)`, with `BM=AB/2`. The BK direction is `(cos(B−α),
sin(B−α))` (BA rotated toward BC by α). Using
`sin γ/sin(α+γ) = csc α/(p+r)` and
`cos(B−α)/sin B = cot B cos α + sin α = (P_B p+1)/csc α`, the `csc α` factors
cancel and `K_x = (P_B p+1)/(2(p+r))`, `K_y = (p−P_B)/(2(p+r))`. The L formula
is the C-side analogue from `△CNL`. ∎

The two **remaining hypotheses** — conditions (ii) `∠LBK=β` and (iii)
`∠LCK=γ` (since (i) and the workhorse angles are already built into the
coordinates) — become, via `cot∠(s,t) = (s·t)/det(s,t)`,

```
F1 := num(L·K − q·det(L,K)) = 0,              (C1)
F2 := num((L−C)·(K−C) − r·det(L−C,K−C)) = 0.  (C2)
```

On the inside configuration the counterclockwise order `BC→BL→BK→BA` at `B`
(and `CB→CK→CL→CA` at `C`) gives `det(L,K)>0` and `det(L−C,K−C)>0`, so the
`+q, +r` signs are the unsigned-angle cotangents and (C1),(C2) are exactly
conditions (ii),(iii). `F1,F2 ∈ Z[p,q,r,P_B,P_C]` (degree 4 each); the
denominators `p+r, p+q` are non-zero in the inside configuration (they vanish
only when `α+γ=π` or `α+β=π`, i.e. degenerate workhorse triangles, excluded by
the inside hypotheses).

**The circumcentre.** `O` is determined by
`2 O·(K−A)=|K|²−|A|²`, `2 O·(L−A)=|L|²−|A|²`, a 2×2 linear system; its
solution is a rational function of `p,q,r,P_B,P_C`. By Lemma 2, `p.bis(MN)` is
`x=(3P_B+P_C)/4`. Define `Π := num(O_x − (3P_B+P_C)/4) ∈ Z[p,q,r,P_B,P_C]`
(cleared numerator; degree 6, 68 terms).

**The algebraic certificate (closes the proof).** Compute a Gröbner basis of
`⟨F1,F2⟩` in `Q[p,q,r,P_B,P_C]` (graded reverse-lex order) and reduce `Π` to
normal form. The remainder is **zero**:

```
Π ∈ ⟨F1,F2⟩.
```

This is a finite, deterministic, exact computation over the rationals (no
floating point): `Π` vanishes at every point of `V(F1,F2)`. The Gröbner basis
has 6 elements (degrees 7,7,6,5,4,4); the normal form of `Π` modulo it is `0`.
(Independently re-verified by the proof-reviewer with `sympy.groebner` over
`QQ`, `grevlex`: 6 elements, exact zero remainder.)

The "inside" hypotheses are open inequalities that select the connected
component of `V(F1,F2)` on which all listed angles are the intended positive
interior values (and `det>0` so the signs match); they impose no additional
polynomial equalities. On that component `Π=0`, i.e.
`O_x = (3P_B+P_C)/4`, so `O∈p.bis(MN)`, i.e. `OM=ON`.

*Relation to cyclicity (non-degenerate case `B≠C`).* The four-point concyclicity
determinant `Δ = det[x_i²+y_i², x_i, y_i, 1]_{i∈{A,K,L,A*}}` satisfies, after
clearing denominators, `Δ_num = −(P_B−P_C)·Π` (the factor `P_B−P_C` reflects
that `A*=A` makes the four-point determinant identically zero). Hence when
`B≠C`, `Π=0 ⟺ Δ=0`, i.e. `OM=ON ⟺ A,K,L,A*` concyclic — the geometric content
of the A*-construction. When `B=C`, cyclicity is trivial (`A*=A`) but the
certificate `Π∈⟨F1,F2⟩` still directly gives `OM=ON`. The single ideal-membership
certificate is uniform over all triangles. ∎

---

### Conclusion

By Lemma 3, `O_x=(3P_B+P_C)/4` in the normalisation, i.e. `O∈p.bis(MN)`. Hence
`OM=ON`. ∎
