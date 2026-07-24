## Status
solved

## Approaches tried
- `complex-number-argument-bash` (round 2, final pass) — **APPROVED.**
  Independently re-verified in full by the proof-reviewer: rebuilt every
  symbolic claim from scratch in fresh `sympy` sessions, starting only from
  the raw problem hypotheses (not from the builder's intermediate
  formulas) — Lemma 0's nine-point-center identity, the Dictionary Lemma,
  `eq1,eq2,eq3` from the raw cross/dot definitions, the exact `l2`
  elimination formula (confirming the corrected sign), the cubic locus `X`
  (`eq3_num = -(l1-1)(p²+q²)X`, `X` irreducible), `eq2_num` (degree 2 in
  `l1`, total degree 3 in `(k1,k2)`), the circumcenter formula, `Fn_num_raw`,
  `Fn_den_raw = 4·D·D3`, `D_circ = 2D3/D`, and the closing identity
  `Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·(E1·l1+E0)` — all confirmed to
  match the write-up exactly (`sympy.expand` of every claimed difference is
  the zero polynomial). Also independently re-derived and confirmed every
  cross-product sign fact (a)-(f) in the orientation argument §3 (the
  "Master Fact" cone-sign toolkit applied to the four containment
  hypotheses K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK), confirming `ε1=ε2=+1` for
  all three Dictionary-Lemma pairings (so `eq1=eq2=eq3=0` correctly encode
  hypotheses (i)-(iii), not their supplements) — and confirmed this
  argument is non-circular: it derives sign facts purely from the given
  containment hypotheses on the (fixed, but otherwise arbitrary) valid pair
  `(K,L)`, never from `eq1=eq2=eq3=0` itself. Verified by direct expansion
  that matching orientation (`ε1=ε2`) is in fact load-bearing (mismatched
  orientation would force the supplementary-angle identity instead, not a
  vacuous check). Also independently re-verified the elementary `D≠0`,
  `D2≠0` proofs in §3 (both reduce to sign facts on cross products derived
  the same way, plus one linear-algebra determinant computation, all
  reproduced exactly). Confirmed `problems.jsonl`'s entry for `imo-2026-02`
  has `task: proof_only`, `answer_type: none` — no numeric/expression
  answer to state; "prove `OM=ON`" is the entire deliverable, which the
  proof establishes. No skipped cases, no hand-waving, no genericity/
  continuity residue (§3's elementary argument fully replaces the earlier
  resultant/Bezout/continuity Step 5, closing the one item the round-2
  intermediate review had flagged as "bookkeeping-only"). **Verdict:
  complete, rigorous proof. Status: solved.**
- `complex-number-argument-bash` (round 2, intermediate) — closed the
  Step-4 polynomial identity gap; left the orientation/sign-matching gap
  and a bookkeeping-flagged genericity sub-step open. CHANGES REQUESTED at
  that point — both now closed (see above).
- `symmetric-vector-decomposition-sigma` (round 2) — proved σ-invariance
  of the defining system and that the naive antisymmetry-of-target
  mechanism is provably vacuous (a genuine negative result, reusable
  byproduct lemmas certified). RETHINK for its own mechanism — superseded,
  not needed once `complex-number-argument-bash` closed.
- `nine-point-locus-two-position` (round 1) — Lemma B (O(θ) affine under
  reparametrization) numerically refuted. Dead end — RETHINK.
- `spiral-similarity-radical-axis` (round 1) — exhaustive scan of all
  70 four-point subsets of {A,B,C,M,N,K,L,O} found no concyclic quadruple.
  Dead end — RETHINK.

## Current best
(superseded by Full proof below.)

## Full proof

**Theorem.** Let `ABC` be a triangle, `M,N` the midpoints of `AB,AC`. Let
`K` be interior to `△BMC`, `L` interior to `△BNC`, with `K` interior to
`∠LBA` and `L` interior to `∠ACK`, such that `∠KBA=∠ACL`, `∠LBK=∠LNC`,
`∠LCK=∠BMK`. Let `O` be the circumcentre of `△AKL`. Then `OM=ON`.

### §0. Coordinates

`OM=ON` and all hypotheses are invariant under orientation-preserving
similarity, so we may fix
```
B=(0,0), C=(1,0), A=(p,q), q>0,
```
and write `K=(k1,k2)`, `L=(l1,l2)`. Then `M=(p/2,q/2)`, `N=((p+1)/2,q/2)`.
Throughout, `cross(u,v)=u_xv_y-u_yv_x`, `dot(u,v)=u_xv_x+u_yv_y`.

### §1. Lemma 0 — reduction of the target (proved; certified,
`lemmas/nine-point-center-reduction.md`)

For any point `P`, `PM²-PN²=(2P-M-N)·(N-M)`. Since `M,N` both lie on
the nine-point circle (midpoints of sides), the nine-point centre `N9`
satisfies `N9M=N9N`; applying the identity at `P=O` and `P=N9` and
subtracting gives `OM²-ON²=2(O-N9)·(N-M)`. Since `M,N` are the
midpoints of `AB,AC`, `N-M ∥ C-B`, so
```
OM=ON  ⟺  (O-N9)·(C-B)=0.
```
In our frame `C-B=(1,0)`, so this is `O_x=(N9)_x`. `N9`, being equidistant
from `M,N` (both at height `q/2`), lies on the vertical line
`x=(M_x+N_x)/2=p/2+1/4`. Hence the target is exactly
```
O_x = p/2 + 1/4.   (★)
```

### §2. Dictionary Lemma (proved; certified,
`lemmas/dictionary-lemma-equal-signed-angle.md`)

For nonzero planar vectors `u,v,w,z`, write the unsigned angle between
`u,v` as `θ1∈(0,π)` with sign `ε1=+1` if `v` is CCW from `u`, `ε1=-1` if
CW (so `cross(u,v)=ε1|u||v|sinθ_1`, `dot(u,v)=|u||v|cosθ_1`), and
similarly `θ2,ε2` for `w,z`. Then, expanding,
```
cross(u,v)·dot(w,z) - cross(w,z)·dot(u,v)
   = |u||v||w||z|·(ε1 sinθ_1 cosθ_2 - ε2 sinθ_2 cosθ_1).
```
If `ε1=ε2` this is `ε1|u||v||w||z|sin(θ_1-θ_2)`; since `θ_1,θ_2∈(0,π)`,
`θ_1-θ_2∈(-π,π)`, so `θ_1=θ_2 ⟹` the right side (hence the left) is `0`.
(If `ε1=-ε2`, the identity instead encodes the supplement `θ1+θ2=π` — this
is why orientation-matching, settled in §3, is essential and load-bearing,
not a vacuous formality.)

Define
```
eq1 := cross(K-B,A-B)·dot(A-C,L-C) - cross(A-C,L-C)·dot(K-B,A-B),
eq2 := cross(L-B,K-B)·dot(L-N,C-N) - cross(L-N,C-N)·dot(L-B,K-B),
eq3 := cross(L-C,K-C)·dot(B-M,K-M) - cross(B-M,K-M)·dot(L-C,K-C).
```
`eq1` is built from the pair `(K-B,A-B)` (spanning `∠KBA`) and the pair
`(A-C,L-C)` (spanning `∠ACL`); `eq2` from `(L-B,K-B)` (`∠LBK`) and
`(L-N,C-N)` (`∠LNC`); `eq3` from `(L-C,K-C)` (`∠LCK`) and `(B-M,K-M)`
(`∠BMK`) — literally the six angles named in the hypotheses
`∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK`.

### §3. Orientation-matching and non-degeneracy

**Master Fact.** Let `v,w` be linearly independent planar vectors.
1. *(Cone criterion.)* If `u=sv+tw` with `s,t>0` then, by bilinearity of
   `cross`, `cross(v,u)=t·cross(v,w)` and `cross(u,w)=s·cross(v,w)`; since
   `s,t>0`, both `cross(v,u)` and `cross(u,w)` have the same sign as
   `cross(v,w)` (nonzero, as `v,w` are independent).
2. *(Substitution.)* If `u=sv+tw` (`s,t>0`) and `w=av+bx` (`a,b>0`, `v,x`
   independent), substituting gives `u=(s+ta)v+(tb)x`, `s+ta>0,tb>0`: a
   positive combination of `v,w` remains a positive combination after
   substituting a positive combination for one of the vectors.

**Geometric input.** For non-collinear `Y,X,Z`, the interior of the
non-reflex angle `∠XYZ` is `{Y+sv+tw : s,t>0}`, `v=X-Y,w=Z-Y` (standard:
open convex cone spanned by the bounding rays). For a non-degenerate
triangle `XYZ`, `P` is strictly interior iff `P=αX+βY+γZ`, `α,β,γ>0`,
`α+β+γ=1` (standard barycentric characterization); at vertex `Y`, this
means `P-Y` is a positive combination of the other two vertices' vectors
from `Y`. Also, for any point `W`, `M-W=½(A-W)+½(B-W)` and
`N-W=½(A-W)+½(C-W)` (pure midpoint algebra).

**(a)** `K` interior to `△BMC` at vertex `C`: `K-C=α(B-C)+β(M-C)`,
`α,β>0`; substituting `M-C=½(A-C)+½(B-C)` gives
`K-C=(β/2)(A-C)+(α+β/2)(B-C)`. By the cone criterion,
`cross(A-C,K-C)` has the sign of `cross(A-C,B-C)=(p-1)·0-q·(-1)=q>0`.
So `cross(A-C,K-C)>0`.

**(b)** `L` interior to `△BNC` at vertex `B`: `L-B=α'(N-B)+β'(C-B)`,
`α',β'>0`; substituting `N-B=½(A-B)+½(C-B)` gives
`L-B=(α'/2)(A-B)+(α'/2+β')(C-B)`. So `cross(A-B,L-B)` has the sign of
`cross(A-B,C-B)=p·0-q·1=-q<0`, i.e. `cross(L-B,A-B)>0`.

**(c)** `K` interior to `∠LBA`: `K-B=s(L-B)+t(A-B)`, `s,t>0`. By the cone
criterion (`v=L-B,w=A-B`, `cross(v,w)>0` by (b)): both `cross(L-B,K-B)`
and `cross(K-B,A-B)` have the sign of `cross(L-B,A-B)>0`, hence
`cross(K-B,A-B)>0` and `cross(L-B,K-B)>0`.

**(d)** `L` interior to `∠ACK`: `L-C=e(A-C)+f(K-C)`, `e,f>0`. By the cone
criterion (`v=A-C,w=K-C`, `cross(v,w)>0` by (a)): `cross(A-C,L-C)>0` and
`cross(L-C,K-C)>0`.

**(e)** `L` interior to `△BNC` at vertex `N`: `L-N=a(B-N)+b(C-N)`, `a,b>0`.
`cross(L-N,C-N)=a·cross(B-N,C-N)`. With `N=((p+1)/2,q/2)`,
`cross(B-N,C-N)=q(p+1)/4+q(1-p)/4=q/2>0`. So `cross(L-N,C-N)>0`.

**(f)** `K` interior to `△BMC` at vertex `M`: `K-M=c(B-M)+d(C-M)`, `c,d>0`.
`cross(B-M,K-M)=d·cross(B-M,C-M)`. With `M=(p/2,q/2)`,
`cross(B-M,C-M)=pq/4+q/2-pq/4=q/2>0`. So `cross(B-M,K-M)>0`.

**Conclusion, part 1 (orientation match).** `eq1`'s pairs `(K-B,A-B)`,
`(A-C,L-C)`: both `cross>0` by (c),(d). `eq2`'s pairs `(L-B,K-B)`,
`(L-N,C-N)`: both `cross>0` by (c),(e). `eq3`'s pairs `(L-C,K-C)`,
`(B-M,K-M)`: both `cross>0` by (d),(f). So all three Dictionary-Lemma
applications have `ε1=ε2=+1` — matching rotational sense — at every valid
configuration of every triangle `ABC` (`q>0`), derived purely from the
four containment hypotheses (never from `eq1=eq2=eq3=0` itself, so no
circularity). By §2, the given angle equalities therefore give exactly
```
eq1 = 0,    eq2 = 0,    eq3 = 0.
```

**Conclusion, part 2 (`D≠0`, `D2≠0`).** Expanding `eq1` in `l1,l2` gives
exactly `eq1 = S(l1-1) - D·l2`, where
`D=k1p²-k1p-k1q²+2k2pq-k2q`, `S=2k1pq-k1q-k2p²+k2p+k2q²`.

*`D≠0`*: if `D=0`, then since `L≠C` (strict interior of `△BNC` excludes
the vertex, so `l1≠1`) and `eq1=0`, we get `S(l1-1)=0 ⟹ S=0`. The system
`D=S=0` is linear homogeneous in `(k1,k2)` with determinant
`-(p²+q²)((p-1)²+q²)=-|A-B|²|A-C|²<0` (nonzero, non-degenerate triangle),
so its only solution is `(k1,k2)=(0,0)`, i.e. `K=B` — contradicting `K`
strictly interior to `△BMC` (which excludes the vertex `B`). So `D≠0`.

*`D2≠0`*, `D2:=-k1q+k2p-k2`: `D2=-cross(K-B,A-C)`. From (a)'s expansion at
vertex `B` of `△BMC`, `K-B=β(M-B)+γ(C-B)=(β/2)(A-B)+γ(C-B)`, `β,γ>0`, so
`cross(K-B,A-C)=(β/2)cross(A-B,A-C)+γ·cross(C-B,A-C)=(β/2)q+γq>0` (both
computed `=q`). Hence `D2=-cross(K-B,A-C)<0`, so `D2≠0`.

### §4. Elimination — cubic locus for `K`

Since `D≠0`, `eq1=0` gives `l2=S(l1-1)/D`. Substituting into `eq3=0` and
clearing the denominator `D` gives (verified: `eq3_num=(l1-1)(p²+q²)X` up
to overall sign, where
```
X := 2k1³q-2k1²k2p+2k1²k2-2k1²pq-k1²q+2k1k2²q+2k1k2p²-2k1k2p-2k1k2q²
     +2k1pq-k1q-2k2³p+2k2³+2k2²pq-3k2²q-k2p²+k2p+k2q²
```
irreducible over `ℚ(p,q)[k1,k2]`). Since `l1≠1`, `p²+q²>0`, `eq3=0` forces
```
X(k1,k2,p,q)=0.               (locus)
```
Substituting the same `l2` into `eq2=0` and clearing `D²` gives
`eq2_num(k1,k2,l1,p,q)=0`, degree `2` in `l1`, total degree `3` in
`(k1,k2)`.

### §5. The closing identity (proved, certified,
`lemmas/closing-polynomial-identity-step4.md`)

Let `Fn_num_raw` be the numerator of `O_x-(p/2+1/4)` for the circumcentre
`O` of `A,K,L` (with `l2` eliminated), `Fn_den_raw` its denominator.
`Fn_den_raw=4·D·D3` for an explicit `D3`, and `D_circ=2D3/D` (`D_circ`
twice the signed area of `A,K,L`); since `O` is given to exist,
`A,K,L` are non-collinear, so `D_circ≠0`, hence (with `D≠0`) `D3≠0`, so
`Fn_den_raw≠0` always.

With
```
D2=-k1q+k2p-k2, E1=-2k1pq+k1q+k2p²-k2p-k2q²,
E0=k1p²q+k1pq-k1q³-k1q-k2p²+2k2pq²+k2p,
```
the following is an exact polynomial identity in `ℤ[p,q,k1,k2,l1]`:
```
Fn_num_raw·D2 - (k2-q)·eq2_num = D·X·(E1·l1+E0).      (‡)
```

### §6. Closing the proof

At the valid configuration `X=0` and `eq2_num=0`, so by (‡),
`Fn_num_raw·D2=0`. Since `D2≠0` (§3), `Fn_num_raw=0`. Since
`Fn_den_raw≠0` (§5),
```
O_x - (p/2+1/4) = Fn_num_raw/Fn_den_raw = 0,
```
i.e. `O_x=p/2+1/4` — the target `(★)` of §1. By Lemma 0, this is
equivalent to `OM=ON`. **∎**

### Verification notes (proof-reviewer, round 2 final pass)

Every symbolic claim above was independently re-derived from scratch in
fresh `sympy` scripts, starting only from the raw cross/dot definitions
and the WLOG coordinates — not from the builder's intermediate formulas —
and matched exactly: `eq1,eq2,eq3` expansions, the `l2`-elimination
formula, `X` (irreducibility and exact coefficients), `eq2_num`'s degree
data, `Fn_den_raw=4DD3`, `D_circ=2D3/D`, and the closing identity (‡)
(confirmed `sympy.expand(LHS-RHS)==0`, an exact polynomial identity, not
a rational-function or numerical check). All six cross-product sign
facts (a)-(f) in §3 were independently recomputed and confirmed. The
orientation argument was checked for non-circularity (it uses only the
four containment hypotheses on the given valid `(K,L)`, never
`eq1=eq2=eq3=0`) and for necessity (mismatched orientation would encode
the supplementary-angle identity, not `eq1=0`, so this is a load-bearing
step, not a vacuous formality). `problems.jsonl`'s `imo-2026-02` entry has
`task: proof_only`, `answer_type: none`, confirming no numeric/expression
answer is required — "prove OM=ON" is fully discharged by §0-§6. No gaps,
no hand-waving, no skipped cases, no unresolved genericity/continuity
residue. **Verdict: solved.**
