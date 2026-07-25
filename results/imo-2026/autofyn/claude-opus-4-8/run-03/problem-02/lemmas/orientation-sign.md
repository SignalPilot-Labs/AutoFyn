# Lemma (Orientation Sign) — coordinate-free; **CERTIFIED (round 2, proof-reviewer)**

> Certification: proof-reviewer verified every step from scratch — Lemma I (interior ⟹ positive
> barycentric), Lemma B (betweenness sign), Fact 0 (midpoint area-halving), and the four target-sign
> chains — with no numeric or continuity appeal in any load-bearing step; the directed upgrade
> (same sign + equal unsigned magnitude in (0,π) ⟹ literal directed equality) is valid. End-to-end
> numeric cross-check: uniform signs (−,−,+,+) over 11,739 admissible configurations. This closes the
> round-1 orientation gap of coordinate-identity. Importable by any approach.

Load-bearing lemma that upgrades the problem's **unsigned** angle equalities to
**correctly-oriented directed** equalities, using only the interiority/betweenness
hypotheses. Stated with cross products / signed areas only (no coordinates), so it is
importable by any approach (coordinate-identity, synthetic-sigma-spiral).

Throughout, for plane vectors `u = (u1,u2)`, `v = (v1,v2)` write the scalar cross product
`cross(u,v) = u1 v2 − u2 v1`, and for points `P,Q,R` write `cross(PQ,PR) := cross(Q−P,R−P)`
and the signed area `[PQR] = ½·cross(PQ,PR)`. Signed area is alternating and cyclic:
`[PQR]=[QRP]=[RPQ]=−[QPR]`. A triangle is *nondegenerate* iff its vertices are not
collinear, i.e. `[·]≠0`.

Orientation convention (WLOG): orient the plane so that `[ABC] > 0` (the plane's two
orientations are interchangeable; fix the one making `ABC` positively oriented). Every sign
below is stated relative to this single convention and is therefore parameter-free.

---

## Setup (the problem's configuration)

`ABC` a triangle; `M`, `N` the midpoints of `AB`, `AC`. `K` strictly interior to `△BMC`,
`L` strictly interior to `△BNC`. `K` lies inside the (nonreflex) angle `∠LBA` and `L` lies
inside the (nonreflex) angle `∠ACK`. Unsigned angle hypotheses: `∠LBK = ∠LNC` and
`∠LCK = ∠BMK` (each a genuine angle in `(0,π)`).

## Statement

Under this setup, with `[ABC]>0`:

1. **Fixed reference signs.**
   `cross(BA,BC) = −2[ABC] < 0`,   `cross(CA,CB) = +2[ABC] > 0`,
   `cross(NB,NC) = +[ABC] > 0`,   `cross(MB,MC) = +[ABC] > 0`.

2. **Target signs.**
   `cross(BK,BL) < 0`  and  `cross(NC,NL) < 0`  (same sign);
   `cross(CL,CK) > 0`  and  `cross(MB,MK) > 0`  (same sign).

3. **Directed upgrade.** Consequently the unsigned equalities upgrade to the *directed*
   equalities
   `arg((L−B)/(K−B)) = arg((L−N)/(C−N))`   and   `arg((K−C)/(L−C)) = arg((K−M)/(B−M))`,
   equivalently
   `Im[(L−B)(C−N)·conj((K−B)(L−N))] = 0`   and   `Im[(K−C)(B−M)·conj((L−C)(K−M))] = 0`,
   the ratios in each equality being *positive* reals (orientation sign `ε=+1`).

---

## Auxiliary facts

**Fact 0 (midpoint area halving).** If `N` is the midpoint of `AC` then `[NBC] = ½[ABC]`;
if `M` is the midpoint of `AB` then `[MBC] = ½[ABC]`.
*Proof.* `[NBC] = ½ cross(N−B, C−B)`. With `N = ½(A+C)`,
`N−B = ½(A−B) + ½(C−B)`, so by bilinearity and `cross(C−B,C−B)=0`,
`cross(N−B,C−B) = ½ cross(A−B,C−B) = 2·½[ABC]·... `; precisely
`cross(N−B,C−B) = ½ cross(A−B,C−B) = ½·2[ABC] = [ABC]` (since `[ABC]=½cross(A−B,C−B)`), hence
`[NBC]=½[ABC]`. The `M` statement is identical with `M=½(A+B)`:
`M−C = ½(A−C)+½(B−C)`, `cross(M−C,B−C)=½cross(A−C,B−C)=[ACB]·...` giving `[MBC]=½[ABC]`
after the cyclic reordering `cross(A−C,B−C)=2[CAB]=2[ABC]` and `cross(M−C,B−C)=[ABC]`. ∎

From Fact 0 and `[PQR]=½cross(PQ,PR)` (with cyclic/alternating reorderings) the four
**fixed reference signs** of Statement 1 follow:
`cross(BA,BC)=cross(A−B,C−B)=2[BAC]=−2[ABC]<0`;
`cross(CA,CB)=cross(A−C,B−C)=2[CAB]=+2[ABC]>0`;
`cross(NB,NC)=cross(B−N,C−N)=2[NBC]=+[ABC]>0`;
`cross(MB,MC)=cross(B−M,C−M)=2[MBC]=+[ABC]>0`.

**Lemma B (betweenness sign lemma).** Let `y, z` be linearly independent plane vectors and
`w = β y + γ z` with `β>0`, `γ>0`. Then `cross(y,w)=γ·cross(y,z)` and `cross(w,z)=β·cross(y,z)`.
Hence `cross(y,w)`, `cross(w,z)`, `cross(y,z)` are all nonzero and share one sign.
*Proof.* Bilinearity of `cross` and `cross(y,y)=cross(z,z)=0` give the two identities.
`cross(y,z)≠0` by independence; `β,γ>0`, so all three are nonzero with the common sign of
`cross(y,z)`. ∎

**Lemma I (interior ⟹ positive combination).** If `X` is strictly interior to nondegenerate
`△VYZ` then `X−V = β(Y−V) + γ(Z−V)` with `β>0`, `γ>0`.
*Proof.* Barycentric coordinates by signed areas: put
`α=[XYZ]/[VYZ]`, `β=[VXZ]/[VYZ]`, `γ=[VYX]/[VYZ]`. The identity
`[XYZ]+[VXZ]+[VYX]=[VYZ]` (expand each signed area and cancel) gives `α+β+γ=1`, and a direct
expansion gives `X = αV+βY+γZ`. `X` strictly interior means it is strictly on the interior
side of each of the three edge-lines, i.e. `[XYZ],[VXZ],[VYX]` all have the same sign as
`[VYZ]`; hence `α,β,γ>0`. Subtracting `V=αV+βV+γV` (using `α+β+γ=1`) yields
`X−V=β(Y−V)+γ(Z−V)`. ∎

**Ray betweenness (definition).** "Ray `VX` lies strictly between rays `VY` and `VZ`" means
`X−V = β(Y−V)+γ(Z−V)` with `β,γ>0`. By Lemma I this holds whenever `X` is interior to
`△VYZ`; and it is exactly the literal meaning of "`X` inside the nonreflex angle `∠YVZ`".

---

## Proof of the target signs (Statement 2)

**`cross(BK,BL) < 0`.**
(i) `K∈int△BMC`. The edge `BM` lies on line `AB` (`M` is the midpoint of `AB`, so
`B,M∈AB`), and the opposite vertex is `C`. By Lemma I applied at vertex `B` of `△BMC`,
`K−B = β(M−B)+γ(C−B)` with `β,γ>0`; since `M−B=½(A−B)`, this is
`K−B = (β/2)(A−B)+γ(C−B)`, a positive combination of `A−B` and `C−B`. By Lemma B (with
`y=A−B`, `z=C−B`), `cross(BA,BK)` shares the sign of `cross(BA,BC)=−2[ABC]<0`. So
`cross(BA,BK)<0`.
(ii) `K` inside `∠LBA` ⟹ ray `BK` strictly between rays `BA`, `BL`, i.e.
`K−B = β'(A−B)+γ'(L−B)` with `β',γ'>0`. By Lemma B (with `y=A−B`, `z=L−B`),
`cross(BA,BK)` and `cross(BK,BL)` share the sign of `cross(BA,BL)`. Hence
`cross(BK,BL)` has the same sign as `cross(BA,BK)`, which is `<0` by (i). Therefore
`cross(BK,BL) < 0`.

**`cross(NC,NL) < 0`.**
`L∈int△BNC`. By Lemma I at vertex `N`, ray `NL` is strictly between rays `NB`, `NC`:
`L−N = β(B−N)+γ(C−N)` with `β,γ>0`. By Lemma B (with `y=B−N`, `z=C−N`), `cross(NB,NL)`,
`cross(NL,NC)`, `cross(NB,NC)` share one sign, namely the sign of `cross(NB,NC)=+[ABC]>0`.
Thus `cross(NL,NC)>0`, and by antisymmetry `cross(NC,NL) = −cross(NL,NC) < 0`.

**`cross(CL,CK) > 0`.**
(i') `L∈int△BNC`. Edge `CN` lies on line `AC` (`N` midpoint of `AC`), opposite vertex `B`.
By Lemma I at `C`, `L−C = β(N−C)+γ(B−C)` with `β,γ>0`; `N−C=½(A−C)` makes this a positive
combination of `A−C` and `B−C`. By Lemma B, `cross(CA,CL)` shares the sign of
`cross(CA,CB)=+2[ABC]>0`, so `cross(CA,CL)>0`.
(ii') `L` inside `∠ACK` ⟹ ray `CL` strictly between rays `CA`, `CK`:
`L−C=β'(A−C)+γ'(K−C)`, `β',γ'>0`. By Lemma B, `cross(CA,CL)` and `cross(CL,CK)` share one
sign; hence `cross(CL,CK)>0`.

**`cross(MB,MK) > 0`.**
`K∈int△BMC`. By Lemma I at vertex `M`, ray `MK` between rays `MB`, `MC`:
`K−M=β(B−M)+γ(C−M)`, `β,γ>0`. By Lemma B, `cross(MB,MK)`, `cross(MK,MC)`, `cross(MB,MC)`
share one sign, namely that of `cross(MB,MC)=+[ABC]>0`. So `cross(MB,MK)>0`. ∎ (Statement 2)

*Remark (no reflex ambiguity).* Each hypothesis "`X` inside angle `∠YVZ`" is read as the
nonreflex angle: `∠LBA,∠ACK∈(0,π)` since the bounding rays are never opposite
(`B,L,A` and `A,C,K` are non-collinear triples in an admissible configuration), so
"strictly between" is the literal reading with no `+π` alternative. This is the only reading
consistent with the hypotheses being nondegenerate angular-containment statements.

## Proof of the directed upgrade (Statement 3)

Fix the first equality; the second is identical with `(B,K)↔(C,L)`, `(N,C)↔(M,B)`.
For nonzero complex `z1,z2`, `sign( Im[z2·conj(z1)] ) = sign( arg(z2/z1) )` and
`|arg(z2/z1)|` equals the unsigned angle between the vectors `z1,z2` (a value in `[0,π]`).

Put `α := arg((L−B)/(K−B))` and `α' := arg((L−N)/(C−N))`, both in `(−π,π)`.
- `sign α = sign Im[(L−B)conj(K−B)] = sign cross(K−B, L−B) = sign cross(BK,BL) < 0`.
- `sign α' = sign Im[(L−N)conj(C−N)] = sign cross(C−N, L−N) = sign cross(NC,NL) < 0`.

So `α, α'` have the same (negative) sign. Their absolute values are the unsigned angles
`∠LBK` and `∠LNC`, both in `(0,π)` and equal by hypothesis. Two real numbers in `(−π,0)`
with equal absolute value are equal; hence `α = α'`, i.e.
`arg((L−B)/(K−B)) = arg((L−N)/(C−N))`.
Therefore `arg[ (L−B)(C−N) / ((K−B)(L−N)) ] = α − α' = 0`, so the ratio is a positive real
and its imaginary part vanishes: `Im[(L−B)(C−N)·conj((K−B)(L−N))] = 0` with `ε=+1`.

The second equality is proved verbatim with `cross(CL,CK)>0`, `cross(MB,MK)>0` in place of
the two negative signs (both `arg` values then lie in `(0,π)`, equal absolute values force
equality), giving `Im[(K−C)(B−M)·conj((L−C)(K−M))] = 0`. ∎

---

## Notes
- Coordinate-free: every step uses only signed areas / cross products and the barycentric
  characterisation of triangle interior. No coordinates, no continuity, no numerics.
- The `σ`-symmetry `(B↔C, M↔N, K↔L)` is a **reflection**, hence reverses plane orientation;
  that is exactly why the second pair of target signs is `+` while the first is `−`. To avoid
  any sign-flip bookkeeping this proof derives the second pair *directly* (same two lemmas at
  `C` and `M`) rather than transporting the first pair through `σ`.
- Symbolic verification of the fixed signs and the two half-vector identities
  `cross(N−B,C−B)=½cross(A−B,C−B)`, `cross(M−C,B−C)=½cross(A−C,B−C)`: exact-zero residual
  (sympy). Numeric confirmation of the target signs over interior configurations: exceptionless
  (round-2 explorers, 83 and 97 configs; and one interior branch checked in this build). These
  are cross-checks only; the proof above is self-contained.
