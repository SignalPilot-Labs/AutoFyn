## Status
solved

## Approaches tried
- `complex-number-argument-bash` (round 3) — **Closed the final gap and
  completed the proof.** (A) Proved the orientation/sign-matching gap in
  full: introduced a clean "Master Fact" toolkit (a point is in the open
  cone spanned by two independent vectors iff it's a strictly-positive
  linear combination of them; substituting one strictly-positive
  combination into another yields another one; and the sign of the
  relevant cross products is then read off directly by bilinearity) and
  used it to show, directly from the containment hypotheses (K inside
  △BMC, L inside △BNC, K inside ∠LBA, L inside ∠ACK — with **no**
  additional unproven assumptions), that all three Dictionary-Lemma vector
  pairs used to build `eq1,eq2,eq3` have matching rotational sense
  (`ε1=ε2=+`) — settling the dichotomy in favor of "encodes the equality",
  never the supplement, at *every* valid configuration for *every* triangle
  shape `q>0`, not just the numeric witness. (B) As a bonus, the same
  toolkit gives a fully rigorous, non-generic, non-continuity replacement
  for the genericity Step 5: `D≠0` follows because `D=0` together with
  `eq1=0` and `l1≠1` forces `K=(0,0)=B` (via two homogeneous linear forms
  in `(k1,k2)` whose determinant is `-|A-B|²|A-C|² < 0`, hence never
  singular) — contradicting `K` strictly interior to `△BMC`; `D2≠0`
  follows because `D2 = -cross(K-B,A-C)`, computed exactly (via the same
  toolkit) to be strictly negative for every valid `K`. This **replaces**
  the earlier resultant/Bezout/continuity argument (which had one honestly
  flagged residual gap) with a fully closed, elementary, exact argument —
  no exceptional cases, no genericity, no analysis needed. With the
  orientation gap and the genericity gap both closed, and Step 4's identity
  independently verified last round, the full chain **eq1=eq2=eq3=0 encode
  (i)-(iii) ⟹ K on cubic X=0 ⟹ Fn_num_raw·D2=D·X·Llin=0 on
  {X=0,eq2_num=0} ⟹ Fn_num_raw=0 (since D2≠0) ⟹ O_x=p/2+1/4 (since
  D≠0⟹D3≠0⟹Fn_den_raw≠0) ⟹ OM=ON (Lemma 0)** is complete and rigorous.
  **Status: solved.**
- `complex-number-argument-bash` (round 2) — Re-derived the entire chain
  (eq1/eq2/eq3, L-elimination, cubic locus X) from scratch in a fresh
  `sympy` script, confirming the outline-reviewer's independent
  re-derivation exactly (same `D`, same `X` up to overall sign, same
  degree-2-in-`l1`/degree-3-in-`(k1,k2)` `eq2_num`). **Closed the Step-4
  polynomial-identity gap**: performed the polynomial division of
  `Fn_num_raw` (numerator of `O_x-(p/2+1/4)`) by `eq2_num` in `l1` directly
  (not the round-2 explorer's unverified cofactor formula, which the
  outline-reviewer had shown does not reproduce), obtaining an EXACT
  polynomial identity (`sympy.expand` of LHS−RHS is the zero polynomial):
  `Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·L(k1,k2,l1,p,q)` with a new, simpler
  cofactor `L` and the same `D2 = −k1q+k2p−k2` as the (superseded) explorer
  claim, but a genuinely different, correctly-verified relationship (no
  stray denominators — confirmed a bona fide polynomial identity in
  `ℤ[p,q,k1,k2,l1]`, not merely a rational-function one). Also established
  `D_circ` (of `A,K,L`) `= 2·D3/D` where `D3` is exactly the second factor
  of the target's denominator, so `D3≠0` is automatic from `A,K,L`
  noncollinear (a standing hypothesis, since `O` is given to exist) together
  with `D≠0`. Handled the genericity exclusions `D≠0, D2≠0` via a
  Bezout/continuity argument (irreducibility of `X`, linearity of `D,D2`,
  nonvanishing resultants, existence of a genuine continuum of admissible
  configurations via the implicit function theorem anchored at the numeric
  witness). **Did not fully close** the orientation/sign-matching gap:
  derived the exact dichotomy governing it (matching vs. mismatched
  rotational sense between the two vector pairs in each Dictionary Lemma
  application forces either `θ1=θ2` or `θ1+θ2=π`) and gave a partial
  betweenness-of-rays argument, but did not complete the case-by-case
  verification at all three vertices `B,C,N,M` within the time budget —
  recorded honestly as the remaining open gap. Net: the field's headline
  computational gap (Step 4) is now genuinely closed with a verified exact
  identity; one targeted gap remains.
- `complex-number-argument-bash` (round 1) — WLOG coordinates, angle-equality
  ⇒ polynomial (Dictionary Lemma) translation, elimination of L via (i),
  substitution into (iii) giving a fixed cubic curve `X(k1,k2,p,q)=0` that K
  must lie on. Independently re-verified correct by the round-1 reviewer
  (matching sympy re-derivation, term for term). Final closure (showing the
  target `O_x = p/2+1/4` vanishes on the variety cut out by `X=0` and the
  `eq2`-derived condition) not completed — open computational gap. A second,
  independent gap (orientation/sign-matching for the Dictionary Lemma's
  vector pairings, needed to confirm eq1/eq2/eq3 encode the problem's actual
  angle hypotheses and not a sign-flipped variant) is also open. Worked —
  real progress, gap remains. CHANGES REQUESTED.

## Current best

### Setup: coordinates (WLOG)

Since `OM = ON` is a statement invariant under similarity transformations
(translation, rotation, uniform scaling) of the whole configuration, we may
fix coordinates by placing
```
B = (0,0),  C = (1,0),  A = (p,q),  q > 0.
```
This is a valid normalization: any triangle `ABC` can be brought to this
form by a unique orientation-preserving similarity, and similarities
preserve all the hypotheses (angle equalities, containments) and the
conclusion (`OM=ON`, an equality of two lengths, is preserved by a global
length-scaling and by isometries). Write `K=(k1,k2)`, `L=(l1,l2)` for the
unknowns. Then
```
M = midpoint(A,B) = (p/2, q/2),    N = midpoint(A,C) = ((p+1)/2, q/2).
```

### Lemma 0 (proved, certified `lemmas/nine-point-center-reduction.md`)

Let `N9` be the nine-point center of `ABC`. For any point `P`,
`PM² − PN² = (2P − M − N)·(N − M)`. Since `M`, `N` are both midpoints of
sides of `ABC`, both lie on the nine-point circle, so `N9M = N9N`. Applying
the identity at `P = O` and `P = N9` and subtracting:
```
OM² − ON² = 2(O − N9)·(N − M).
```
Since `M`, `N` are midpoints of `AB`, `AC`, `MN` is the midline of `ABC`
parallel to `BC`, so `N − M ∥ C − B`. Hence
```
OM = ON  ⟺  (O − N9)·(C − B) = 0.
```
In our coordinates `C − B = (1,0)`, so the target reduces to `O_x = (N9)_x`.
The nine-point center is the circumcenter of the medial triangle
`M,N,(1/2,0)`; `M,N` share `y`-coordinate `q/2`, so the perpendicular
bisector of `MN` is the vertical line `x = (M_x+N_x)/2 = p/2+1/4`, on which
`N9` lies. Hence the target is exactly
```
O_x = p/2 + 1/4.   (★)
```

### Dictionary Lemma (proved, certified
`lemmas/dictionary-lemma-equal-signed-angle.md`)

For nonzero planar vectors `u,v,w,z` define `cross(u,v)=u_1v_2-u_2v_1`,
`dot(u,v)=u_1v_1+u_2v_2`. If `u,v` make signed angle `θ1` (magnitude in
`(0,π)`, sign `ε1=±1` recording whether `v` is CCW (`+`) or CW (`−`) from
`u`) and `w,z` make signed angle `θ2` (magnitude in `(0,π)`, sign `ε2`),
then, since `cross(u,v)=ε1|u||v|\sinθ_1`, `dot(u,v)=|u||v|\cosθ_1` (dot is
orientation-independent — `dot(u,v)=dot(v,u)`), expanding
```
cross(u,v)dot(w,z) − cross(w,z)dot(u,v)
  = |u||v||w||z|·(ε1\sinθ_1\cosθ_2 − ε2\sinθ_2\cosθ_1).
```
- If `ε1=ε2=:ε` (matching rotational sense), this is
  `ε|u||v||w||z|\sin(θ_1−θ_2)`, and since `θ_1,θ_2∈(0,π)⟹θ_1−θ_2∈(-π,π)`,
  the equation `cross(u,v)dot(w,z)=cross(w,z)dot(u,v)` (†) forces
  `θ_1=θ_2`. Conversely `θ_1=θ_2` gives (†).
- If `ε1=-ε2` (mismatched sense), the same computation gives
  `ε1|u||v||w||z|\sin(θ_1+θ_2)`, so (†) instead forces `θ_1+θ_2=π`
  (the only solution of `\sin(θ1+θ2)=0` in `(0,2π)`), i.e. (†) would encode
  the SUPPLEMENT of the intended equality, not the equality itself.

**Consequence.** (†) is equivalent to the intended equality `θ1=θ2` *only*
when the two vector pairs used are chosen with the same rotational sense.
This sign bookkeeping is the content of the "second open gap" below.

Applying (†) with the pairings chosen in round 1 (retained; see the gap
discussion below for the still-open verification that they are the
sense-matched choice) to hypotheses (i), (ii), (iii):

```
eq1 := cross(K-B,A-B)·dot(A-C,L-C) − cross(A-C,L-C)·dot(K-B,A-B) = 0.   (i)
eq2 := cross(L-B,K-B)·dot(L-N,C-N) − cross(L-N,C-N)·dot(L-B,K-B) = 0.  (ii)
eq3 := cross(L-C,K-C)·dot(B-M,K-M) − cross(B-M,K-M)·dot(L-C,K-C) = 0. (iii)
```

### Step 1: eliminate `L` using `eq1` (re-verified from scratch, round 2)

Expanding, `eq1` is jointly linear in `(l1,l2)`, with the coefficient of
`l2` equal to `−D` where
```
D := k1p² − k1p − k1q² + 2k2pq − k2q,
```
and solving `eq1=0` for `l2` gives
```
l2 = -[ -2k1l1pq + k1l1q + 2k1pq - k1q + k2l1p² - k2l1p - k2l1q² - k2p² + k2p + k2q² ] / D =: -l2_num/D,
```
valid whenever `D ≠ 0`. **[Round-2 reviewer correction: the earlier
displayed formula `l2 = l2_num/D` (without the leading minus sign) does
NOT satisfy `eq1=0` — confirmed by independent `sympy` check; the correct
formula has an overall minus sign as displayed here. This was a sign typo
in the write-up only; the downstream artifacts `X`, `eq2_num`,
`Fn_num_raw`, and identity (‡) below were independently re-derived from
scratch by the round-2 reviewer using the correct sign and all matched
exactly, so no downstream computation is affected. See
`lemmas/closing-polynomial-identity-step4.md`.]** Substitution back into
`eq1` and simplification gives identically `0` (checked symbolically, with
the corrected sign): `eq1|_{l2=-l2_num/D} = 0`.

### Step 2: substitute into `eq3` — the cubic locus for `K` (re-verified)

Substituting `l2=l2_num/D` into `eq3` and clearing the denominator (which
introduces a factor `D` in the denominator of `eq3`, cleared by multiplying
through) gives a polynomial `eq3_num(k1,k2,l1,p,q)`, degree `1` in `l1`,
which factors (checked by `sympy.factor`, confirmed exactly, matching the
round-1/outline-reviewer computation) as
```
eq3_num = (l1 − 1)(p²+q²)·X(k1,k2,p,q),
```
where
```
X := 2k1³q − 2k1²k2p + 2k1²k2 − 2k1²pq − k1²q + 2k1k2²q + 2k1k2p² − 2k1k2p
     − 2k1k2q² + 2k1pq − k1q − 2k2³p + 2k2³ + 2k2²pq − 3k2²q − k2p² + k2p + k2q².
```
(This `X` is the negative of the round-1 file's `X`; the sign is
immaterial, `X=0` is the same curve. `X` is verified irreducible over
`ℚ(p,q)[k1,k2]` by `sympy.factor_list`, single factor of multiplicity `1`.)

**Branch `l1=1`.** Substituting `l1=1` into the Step-1 formula for `l2`
gives `l2=0` identically, so `L=(1,0)=C`. This branch makes `∠LCK` (in
hypothesis (iii)) undefined and is excluded by the hypothesis that `L` lies
strictly inside triangle `BNC` (an open region not containing vertex `C`).
This is a genuine spurious root introduced by clearing a denominator, not a
valid configuration.

**Branch `X(k1,k2,p,q)=0`.** Since the `l1=1` branch is excluded, every
valid configuration has `K=(k1,k2)` on the fixed cubic curve `X=0`,
depending only on the shape of `ABC`, independent of `L`.

### Step 3: `eq2` as a residual condition on `l1` (re-verified)

Substituting the Step-1 formula for `l2` into `eq2` and clearing
denominators (`D²`) gives `eq2_num(k1,k2,l1,p,q)`, degree `2` in `l1`, total
degree `3` in `(k1,k2)` (this round's independent recomputation matches the
outline-reviewer's value of `3`, not the round-1 file's earlier claim of
`6` — the round-1 figure was a minor bookkeeping slip, not load-bearing).

### Step 4 — closing the polynomial identity (round 2, closed)

Write the circumcenter of `A=(p,q),K=(k1,k2),L=(l1,l2_num/D)` via the
standard formula
```
D_circ = 2[A_x(K_y−L_y) + K_x(L_y−A_y) + L_x(A_y−K_y)],
O_x·D_circ = (A_x²+A_y²)(K_y−L_y) + (K_x²+K_y²)(L_y−A_y) + (L_x²+L_y²)(A_y−K_y),
```
substitute `L_y = l2_num/D`, and let `Fn_num_raw` be the numerator (cleared
of all denominators) of `O_x − (p/2+1/4)`, i.e.
```
Fn_num_raw / Fn_den_raw  =  O_x − (p/2 + 1/4),
```
after combining to a single fraction (`sympy.together`/`fraction`) and
clearing common factors. Direct computation (this round, fresh) gives
```
Fn_den_raw = 4·D·D3(k1,k2,l1,p,q),
```
for an explicit polynomial `D3` (degree `1` in `l1`), and moreover
```
D_circ|_{l2=l2_num/D} = 2·D3 / D.
```
Since `D_circ ≠ 0` is *automatic* — the problem defines `O` as the
circumcenter of `A,K,L`, so `A,K,L` are noncollinear throughout, i.e.
`D_circ ≠ 0` holds at every actual configuration of the problem — the
identity `D_circ = 2D3/D` shows `D3 ≠ 0` follows from `D_circ≠0` together
with `D≠0` (handled below). So the only extra genericity condition needed
for `Fn_num_raw/Fn_den_raw` to be a valid representation of `O_x−(p/2+1/4)`
is `D≠0`.

**The closing identity.** Performing polynomial division of `Fn_num_raw`
(regarded as a degree-`2` polynomial in `l1`, with coefficients rational
functions of `k1,k2,p,q`) by `eq2_num` (also degree `2` in `l1`) — i.e.
writing `Fn_num_raw = q0·eq2_num + (r1·l1+r0)` with
`q0 = a2/b2` (`a2,b2` the leading `l1²`-coefficients of `Fn_num_raw,
eq2_num` respectively) and `r1,r0` the resulting remainder coefficients —
and simplifying each of `q0,r1,r0` by `sympy.cancel`, gives
```
q0 = (k2−q)/D2,     D2 := −k1q + k2p − k2,
```
and, after fully factoring `r1,r0` (this round, fresh computation, verified
by direct `sympy.expand`), **both `r1` and `r0` factor exactly as
`D·X·(linear in k1,k2,p,q)/D2`.** Explicitly, with
```
E1 := −2k1pq + k1q + k2p² − k2p − k2q²,
E0 := k1p²q + k1pq − k1q³ − k1q − k2p² + 2k2pq² + k2p,
```
one has `r1 = D·X·E1/D2`, `r0 = D·X·E0/D2`, i.e. writing
`Llin := E1·l1 + E0`, the division `Fn_num_raw = q0·eq2_num + (r1 l1+r0)`
reads, after multiplying through by `D2` to clear the one denominator
present:
```
Fn_num_raw·D2 − (k2−q)·eq2_num  =  D·X·Llin.        (‡)
```
**This is an exact polynomial identity in `ℤ[p,q,k1,k2,l1]`** — verified by
expanding both sides in `sympy` and confirming their difference is the zero
polynomial (`sympy.expand(LHS-RHS) == 0`), not a numerical or
rational-function check. (This supersedes the round-2 explorer's earlier,
unverified cofactor claim, which the outline-reviewer correctly showed does
not reproduce; identity (‡) above is freshly and independently re-derived
in this round and directly checked.)

**Consequence.** At any point with `X(k1,k2,p,q)=0` (the cubic locus for
`K`, Step 2) and `eq2_num(k1,k2,l1,p,q)=0` (hypothesis (ii), Step 3), the
right side of (‡) vanishes, so `Fn_num_raw·D2 = 0`. If in addition `D2 ≠ 0`,
this forces `Fn_num_raw = 0`; combined with `D≠0` (hence `Fn_den_raw≠0`,
by the discussion above), we get `O_x − (p/2+1/4) = Fn_num_raw/Fn_den_raw =
0`, i.e. **`O_x = p/2+1/4` exactly — the target (★).**

### Step 5: genericity exclusions `D≠0`, `D2≠0`

`D = k1(p²−p−q²) + k2(2pq−q)` and `D2 = −k1q + k2(p−1)` are each linear
(non-identically-zero) polynomials in `(k1,k2)` for every valid triangle
(`q>0`): the coefficient pair of `D` is `(p²−p−q², 2pq−q)`, which cannot
both vanish for `q>0` (if `2pq−q=0` then `q(2p-1)=0` forces `p=1/2`, giving
`p²-p-q² = -1/4-q^2 \ne 0` for `q>0`); the coefficient pair of `D2` is
`(-q,p-1)`, and `q\ne0` alone rules out both vanishing. So `\{D=0\}` and
`\{D2=0\}` are each genuine lines in the `(k1,k2)`-plane for every valid
triangle.

`X` is irreducible of degree `3` over `ℚ(p,q)[k1,k2]` (verified by
`sympy.factor_list`), so it cannot have a linear polynomial (over
`ℚ(p,q)`) as a factor; consequently `\mathrm{resultant}(X,D,k_2)` and
`\mathrm{resultant}(X,D2,k_2)`, computed symbolically in `k_1,p,q`, are
each a **nonzero** polynomial (verified directly: `sympy.expand` of each
resultant is not the zero polynomial). A nonzero polynomial in `(k1,p,q)`
vanishes only on a proper (lower-dimensional) subvariety, so: for all
`(p,q)` outside a further proper algebraic exceptional set (a genericity
condition on the *shape* of `ABC`, not on `K,L`), the resultant, viewed as
a polynomial in `k1` alone, is not identically zero, so `X=0` and `D=0`
(respectively `D2=0`) share only finitely many common points `(k1,k2)`.

For the finitely many exceptional shapes of `ABC` excluded above, and for
the finitely many points on the (otherwise 1-dimensional) real cubic curve
`X=0` where `D=0` or `D2=0` even for a generic triangle, we invoke
continuity: the admissible set of configurations `(K,L)` for a *fixed*
triangle `ABC` — those satisfying `eq1=eq2=eq3=0` and all four strict
containment hypotheses (`K` inside `∠LBA`, `L` inside `∠ACK`, `K` inside
`△BMC`, `L` inside `△BNC`) — is nonempty (round-1/round-2 numerical
witnesses on three independent triangles exhibit explicit points satisfying
all seven conditions to `10`+ significant figures) and, since the four
containment conditions are *open* conditions (strict interior membership is
preserved under small perturbations) while `eq1=eq2=eq3=0` cuts out (by the
`4`-unknowns-minus-`3`-equations count, confirmed by the numerics) a curve
of real dimension `1` near any smooth point, the Implicit Function Theorem
applied at a numeric witness (whose Jacobian is generically nonsingular,
consistent with the isolated-root numerics of the witnesses used throughout
this project) produces an actual open arc of exact solutions through a true
zero nearby, on which the strict containments continue to hold by
openness. Thus the admissible configurations for the fixed triangle form,
near any witness, a genuine continuum (an interval's worth of real
parameter values), not merely isolated points. Since `\{D=0\}\cup\{D2=0\}`
meets the cubic curve `X=0` in only finitely many points (shown above,
outside the further finite exceptional set of triangle shapes — and for
those exceptional shapes the same finiteness can be re-derived by
specializing `(p,q)` and re-running the resultant computation, since the
resultants are honest nonzero polynomials and only fail to be "generic in
`k1`" on a further lower-dimensional set, an argument that bottoms out
after finitely many strata), the continuum of admissible configurations
cannot be entirely contained in the exceptional finite set. So `O_x −
(p/2+1/4)`, a function that is continuous (indeed real-analytic) on the
admissible arc wherever `D_circ\ne0` (always true, since `O` is assumed to
exist), vanishes on a dense subset (the complement of a finite set within a
connected continuum) and is continuous everywhere on the arc, hence
vanishes identically on the whole admissible arc for the given triangle —
**including at any point where `D=0` or `D2=0`.** This closes Step 5.

(We record honestly that the very last stratification step — re-running
the finiteness argument for the finitely-many exceptional triangle shapes
where the resultant might vanish identically in `k1` — is asserted by the
same mechanism rather than executed explicitly triangle-shape by
triangle-shape; this is standard genericity bookkeeping, not a
computational gap in the main identity, but we flag it for full
transparency.)

### Numeric witness (sanity check only, not a proof step)

`A=(0.35,0.9), B=(0,0), C=(1,0)`, `K≈(0.1790,0.2390), L≈(0.6848,0.2514)`.
Direct evaluation gives `eq1≈-1.3×10⁻⁵`, `X≈2.9×10⁻⁵` (both consistent with
zero given the witness's 4-decimal precision), `D≈-0.250`, `D2≈-0.316`
(both comfortably bounded away from `0`, consistent with the genericity
argument above), and `O_x≈0.425=p/2+1/4` exactly as predicted.

### Orientation/sign-matching — CLOSED (round 3)

See the "Master Fact" toolkit and its application, given in full in the
`## Full proof` section below (§3). Result: at every valid configuration,
all three Dictionary-Lemma applications have matching rotational sense
(`ε1=ε2=+`), so `eq1,eq2,eq3` as defined above correctly encode hypotheses
(i),(ii),(iii) (not their supplements). The same toolkit also gives a
fully elementary, non-generic proof of `D≠0` and `D2≠0` (§3, replacing the
round-2 resultant/continuity argument for Step 5, which is superseded).

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

For any point `P`, `PM²-PN²=(2P-M-N)\cdot(N-M)`. Since `M,N` both lie on
the nine-point circle (midpoints of sides), the nine-point centre `N9`
satisfies `N9M=N9N`; applying the identity at `P=O` and `P=N9` and
subtracting gives `OM²-ON²=2(O-N9)\cdot(N-M)`. Since `M,N` are the
midpoints of `AB,AC`, `N-M \parallel C-B`, so
```
OM=ON  ⟺  (O-N9)\cdot(C-B)=0.
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
CW (so `cross(u,v)=ε1|u||v|\sinθ_1`, `dot(u,v)=|u||v|\cosθ_1`), and
similarly `θ2,ε2` for `w,z`. Then, expanding,
```
cross(u,v)\,dot(w,z) - cross(w,z)\,dot(u,v)
   = |u||v||w||z|\,(ε1\sinθ_1\cosθ_2-ε2\sinθ_2\cosθ_1).
```
If `ε1=ε2` this is `ε1|u||v||w||z|\sin(θ_1-θ_2)`; since `θ_1,θ_2∈(0,π)`,
`θ_1-θ_2\in(-π,π)`, so `θ_1=θ_2 \Rightarrow` the right side (hence the
left) is `0`. **We only use this direction** (equality of angles implies
the polynomial identity); the converse and the mismatched-sign case are
not needed below now that the sign-matching is settled directly (§3).

Define, exactly as in earlier rounds,
```
eq1 := cross(K-B,A-B)\,dot(A-C,L-C) - cross(A-C,L-C)\,dot(K-B,A-B),
eq2 := cross(L-B,K-B)\,dot(L-N,C-N) - cross(L-N,C-N)\,dot(L-B,K-B),
eq3 := cross(L-C,K-C)\,dot(B-M,K-M) - cross(B-M,K-M)\,dot(L-C,K-C).
```
By construction, `eq1` is built from the pair `(K-B,A-B)` (spanning
`∠KBA`) and the pair `(A-C,L-C)` (spanning `∠ACL`); `eq2` from
`(L-B,K-B)` (`∠LBK`) and `(L-N,C-N)` (`∠LNC`); `eq3` from `(L-C,K-C)`
(`∠LCK`) and `(B-M,K-M)` (`∠BMK`) — literally the six angles named in the
hypotheses `∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK`.

### §3. Orientation-matching and non-degeneracy (the round-3 closure)

**Master Fact.** Let `v,w` be linearly independent planar vectors.
1. *(Cone criterion.)* If `u=sv+tw` with `s,t>0` then, by bilinearity of
   `cross`, `cross(v,u)=t\cdot cross(v,w)` and `cross(u,w)=s\cdot
   cross(v,w)`; since `s,t>0`, **both `cross(v,u)` and `cross(u,w)` have
   the same sign as `cross(v,w)`** (which is nonzero as `v,w` are
   independent).
2. *(Substitution.)* If `u=sv+tw` (`s,t>0`) and `w=av+bx` (`a,b>0`,
   `v,x` independent), substituting gives `u=(s+ta)v+(tb)x` with
   `s+ta>0`, `tb>0`: **a positive combination of `v,w` in which one
   vector is itself replaced by a positive combination remains a positive
   combination.**

**Geometric input.** For a point `Y` and two points `X,Z` with `Y,X,Z`
non-collinear, the (necessarily non-reflex, `<π`) angle `∠XYZ` has open
interior exactly `\{Y+sv+tw : s,t>0\}` with `v=X-Y,w=Z-Y` (standard: the
interior of a non-reflex angle is the open convex cone spanned by its two
bounding rays). Likewise, for a non-degenerate triangle `XYZ`, a point `P`
is strictly interior **iff** `P=\alpha X+\beta Y+\gamma Z` with
`\alpha,\beta,\gamma>0`, `\alpha+\beta+\gamma=1` (standard barycentric
characterization: the open triangle is the intersection of the three open
half-planes each bounded by a side-line and containing the opposite
vertex, and this positivity of barycentric coordinates is exactly that
condition). In particular, at vertex `Y=X'` of a triangle `X'Y'Z'`
(relabelling to keep `Y` for the vertex in question), an interior point
`P` satisfies `P-Y = \beta(Y_1-Y)+\gamma(Y_2-Y)` for the other two
vertices `Y_1,Y_2`, some `\beta,\gamma>0` — i.e. `P-Y` is a positive
combination of `Y_1-Y,Y_2-Y`.

Also record two facts used repeatedly, both immediate from midpoint
collinearity: for **any** point `W`, `M-W=\tfrac12(A-W)+\tfrac12(B-W)`
and `N-W=\tfrac12(A-W)+\tfrac12(C-W)` (pure vector algebra, `M,N` being
midpoints).

We now translate every hypothesis into a positive-combination statement
and push it through the Master Fact.

**(a) `cross(A-C,K-C)>0`.** `K` interior to `△BMC` (vertices `B,M,C`), at
vertex `C`: `K-C=\alpha(B-C)+\beta(M-C)`, `\alpha,\beta>0`. Substitute
`M-C=\tfrac12(A-C)+\tfrac12(B-C)`:
`K-C = \tfrac{\beta}{2}(A-C) + (\alpha+\tfrac{\beta}{2})(B-C)`,
coefficients `\tfrac{\beta}{2}>0,\ \alpha+\tfrac\beta2>0`. By the cone
criterion (with `v=A-C,\,w=B-C`), `cross(A-C,K-C)` has the sign of
`cross(A-C,B-C)`. Direct computation: `A-C=(p-1,q)`, `B-C=(-1,0)`, so
`cross(A-C,B-C)=(p-1)\cdot0-q\cdot(-1)=q>0`. Hence
```
cross(A-C,K-C) > 0.               (a)
```

**(b) `cross(L-B,A-B)>0`.** `L` interior to `△BNC` (vertices `B,N,C`), at
vertex `B`: `L-B=\alpha'(N-B)+\beta'(C-B)`, `\alpha',\beta'>0`. Substitute
`N-B=\tfrac12(A-B)+\tfrac12(C-B)`:
`L-B=\tfrac{\alpha'}{2}(A-B)+(\tfrac{\alpha'}2+\beta')(C-B)`, both
coefficients `>0`. By the cone criterion (`v=A-B,w=C-B`), `cross(A-B,L-B)`
has the sign of `cross(A-B,C-B)`. Compute: `A-B=(p,q)`, `C-B=(1,0)`,
`cross(A-B,C-B)=p\cdot0-q\cdot1=-q<0`, so `cross(A-B,L-B)<0`, i.e.
```
cross(L-B,A-B) = -cross(A-B,L-B) > 0.      (b)
```

**(c) `cross(K-B,A-B)>0` and `cross(L-B,K-B)>0` (eq1's and eq2's first
pair).** `K` interior to `∠LBA` means `K-B=s(L-B)+t(A-B)`, `s,t>0`. By
the cone criterion (`v=L-B,w=A-B`) using (b) — `cross(L-B,A-B)>0` — we get
`cross(L-B,K-B)` and `cross(K-B,A-B)` both have the sign of
`cross(L-B,A-B)`, i.e. both are `>0`:
```
cross(K-B,A-B) > 0,     cross(L-B,K-B) > 0.      (c)
```

**(d) `cross(A-C,L-C)>0` and `cross(L-C,K-C)>0` (eq1's and eq3's second/
first pair).** `L` interior to `∠ACK` means `L-C=e(A-C)+f(K-C)`, `e,f>0`.
By the cone criterion (`v=A-C,w=K-C`) using (a) — `cross(A-C,K-C)>0` — we
get `cross(A-C,L-C)` and `cross(L-C,K-C)` both have the sign of
`cross(A-C,K-C)`, i.e. both `>0`:
```
cross(A-C,L-C) > 0,     cross(L-C,K-C) > 0.      (d)
```

**(e) `cross(L-N,C-N)>0` (eq2's second pair).** `L` interior to `△BNC`, at
vertex `N`: `L-N=a(B-N)+b(C-N)`, `a,b>0`. By the cone criterion
(`v=B-N,w=C-N`), `cross(L-N,C-N)=a\cdot cross(B-N,C-N)`, sign matches
`cross(B-N,C-N)`. Compute with `N=((p+1)/2,q/2)`: `B-N=(-(p+1)/2,-q/2)`,
`C-N=((1-p)/2,-q/2)`,
```
cross(B-N,C-N) = \Big(-\tfrac{p+1}2\Big)\Big(-\tfrac q2\Big)
                 - \Big(-\tfrac q2\Big)\Big(\tfrac{1-p}2\Big)
               = \tfrac{q(p+1)}4+\tfrac{q(1-p)}4 = \tfrac q2 > 0.
```
Hence
```
cross(L-N,C-N) > 0.               (e)
```

**(f) `cross(B-M,K-M)>0` (eq3's second pair).** `K` interior to `△BMC`, at
vertex `M`: `K-M=c(B-M)+d(C-M)`, `c,d>0`. By the cone criterion,
`cross(B-M,K-M)=d\cdot cross(B-M,C-M)`, sign matches `cross(B-M,C-M)`.
With `M=(p/2,q/2)`: `B-M=(-p/2,-q/2)`, `C-M=(1-p/2,-q/2)`,
```
cross(B-M,C-M) = \Big(-\tfrac p2\Big)\Big(-\tfrac q2\Big)
                 -\Big(-\tfrac q2\Big)\Big(1-\tfrac p2\Big)
               = \tfrac{pq}4+\tfrac q2-\tfrac{pq}4 = \tfrac q2 > 0,
```
so
```
cross(B-M,K-M) > 0.               (f)
```

**Conclusion of §3, part 1 (orientation match).** Comparing:
- `eq1`'s pairs `(K-B,A-B)` and `(A-C,L-C)`: both `cross>0` by (c),(d).
- `eq2`'s pairs `(L-B,K-B)` and `(L-N,C-N)`: both `cross>0` by (c),(e).
- `eq3`'s pairs `(L-C,K-C)` and `(B-M,K-M)`: both `cross>0` by (d),(f).

Since `sign(cross(u,v))=\varepsilon_1` and `sign(cross(w,z))=\varepsilon_2`
in the Dictionary Lemma's notation (as `\sin\theta_1,\sin\theta_2>0`
always), all three pairs used have `\varepsilon_1=\varepsilon_2=+1`.
By §2's Dictionary Lemma (the direction we use: matching sign and equal
unsigned angle `⟹` the polynomial vanishes), the hypotheses
`∠KBA=∠ACL`, `∠LBK=∠LNC`, `∠LCK=∠BMK` give exactly
```
eq1 = 0,     eq2 = 0,     eq3 = 0.
```
**This closes the orientation/sign-matching gap in full: `eq1,eq2,eq3`
(as literally defined in §2, unchanged from prior rounds) correctly encode
hypotheses (i)-(iii), for every valid configuration of every triangle
`ABC` (`q>0`), not merely at a numeric witness.**

**Conclusion of §3, part 2 (non-degeneracy: `D≠0`, `D2≠0`).** Expanding
`eq1` as a polynomial in `l1,l2` (direct algebra) gives exactly
```
eq1 = S\cdot(l1-1) - D\cdot l2,
```
where
```
D := k1p^2-k1p-k1q^2+2k2pq-k2q,   S := 2k1pq-k1q-k2p^2+k2p+k2q^2
```
(both linear homogeneous in `(k1,k2)`; verified by direct expansion —
`S` is literally the coefficient of `l1` in `eq1` and `D` (up to sign) is
the coefficient of `l2`, and the constant term of `eq1` is exactly `-S`,
so `eq1` factors as displayed).

*Claim: `D\ne0`.* Suppose `D=0`. Since `L` is strictly interior to
`△BNC`, `L\ne C`, so `l1\ne1`. From `eq1=0` (established above) and
`eq1=S(l1-1)-D\cdot l2=S(l1-1)` (as `D=0`), and `l1-1\ne0`, we get `S=0`.
So `D=S=0` — two homogeneous linear equations in `(k1,k2)`. Their
coefficient determinant is
```
\det\begin{pmatrix}p^2-p-q^2 & 2pq-q\\ 2pq-q & -p^2+p+q^2\end{pmatrix}
 = -(p^2-p-q^2)^2-(2pq-q)^2 = -(p^2+q^2)\big((p-1)^2+q^2\big)
 = -|A-B|^2|A-C|^2,
```
(direct algebraic expansion/factorization, verified symbolically) which
is strictly negative since `A\ne B,\,A\ne C` (non-degenerate triangle).
So the determinant is nonzero, forcing the **only** solution of `D=S=0` to
be `(k1,k2)=(0,0)`, i.e. `K=B`. But `K` is strictly interior to `△BMC`,
and `B` is a vertex of that triangle, hence not in its open interior —
contradiction. **So `D\ne0`.**

*Claim: `D2\ne0`, where `D2:=-k1q+k2p-k2`.* Direct computation shows
`D2 = -cross(K-B,A-C)` (expand `cross((k1,k2),(p-1,q)) = k1q-k2(p-1) =
k1q-k2p+k2=-D2`, so `D2=-cross(K-B,A-C)`). Now use `K-B=\tfrac\beta2(A-B)
+\gamma(C-B)` from part (a)'s barycentric expansion (`K` interior to
`△BMC` at vertex `B`: `K-B=\beta(M-B)+\gamma(C-B)`,
`M-B=\tfrac12(A-B)`, `\beta,\gamma>0`). By bilinearity,
```
cross(K-B,A-C) = \tfrac\beta2\,cross(A-B,A-C) + \gamma\,cross(C-B,A-C).
```
Compute `cross(A-B,A-C)=cross((p,q),(p-1,q))=pq-q(p-1)=q>0` and
`cross(C-B,A-C)=cross((1,0),(p-1,q))=q-0=q>0`. So
`cross(K-B,A-C)=q(\tfrac\beta2+\gamma)>0` (as `\beta,\gamma,q>0`), hence
```
D2 = -cross(K-B,A-C) < 0.
```
**So `D2\ne0`** (in fact `D2<0`) at every valid configuration.

These replace the round-2 resultant/Bezout/continuity argument for Step 5
entirely, with a direct, elementary, exact derivation requiring no
genericity assumptions, no exceptional-shape bookkeeping, and no analysis.

### §4. Elimination — cubic locus for `K` (re-verified, round 2 and round
3; unchanged from prior rounds since `eq1,eq2,eq3` are unchanged)

Since `D\ne0` (§3), solving `eq1=0` for `l2` (equivalently, from
`eq1=S(l1-1)-D\,l2=0`) gives
```
l2 = \frac{S(l1-1)}{D} = -\frac{l2\_num}{D}
```
for the explicit polynomial `l2\_num` recorded earlier in this file
(`l2\_num = -S\cdot(l1-1)\cdot(-1)`, matching the corrected Step-1 formula
above — this is the same elimination as before, now justified by `D\ne0`
proven directly rather than assumed generic).

Substituting this `l2` into `eq3=0` and clearing the (now legitimately
nonzero) denominator `D` gives, exactly as computed and independently
re-verified in round 2 (`sympy.factor`, matching term for term):
```
eq3\_num = (l1-1)(p^2+q^2)\cdot X(k1,k2,p,q),
```
with `X` the explicit irreducible cubic given above. Since `l1\ne1`
(`L\ne C`, as noted) and `p^2+q^2>0` (`A\ne B`), `eq3=0` forces
```
X(k1,k2,p,q) = 0.               (locus)
```

Substituting the same `l2` into `eq2=0` and clearing the denominator `D^2`
gives `eq2\_num(k1,k2,l1,p,q)=0` (Step 3 above, re-verified, degree `2` in
`l1`).

### §5. The closing identity (proved, certified,
`lemmas/closing-polynomial-identity-step4.md`; independently re-derived
from scratch by the round-2 reviewer)

Let `Fn\_num\_raw` be the numerator (in lowest terms) of `O_x-(p/2+1/4)`
for the circumcentre `O` of `A,K,L` (with `l2` eliminated as above), and
`Fn\_den\_raw` its denominator. Direct computation (re-verified twice,
independently) gives `Fn\_den\_raw = 4\cdot D\cdot D3` for an explicit
polynomial `D3`, and, writing `D\_circ` for (twice) the signed area of
`A,K,L` (with `l2` eliminated),
```
D\_circ = 2\cdot D3/D.
```
Since `O` is given as the circumcentre of **triangle** `AKL`, `A,K,L` are
non-collinear, so `D\_circ\ne0` always; combined with `D\ne0` (§3), this
gives **`D3\ne0`**, hence `Fn\_den\_raw=4DD3\ne0` always. So
`O_x-(p/2+1/4) = Fn\_num\_raw/Fn\_den\_raw` is a genuine (non-`0/0`)
fraction, and it equals `0` iff `Fn\_num\_raw=0`.

With
```
D2 = -k1q+k2p-k2,\quad E1=-2k1pq+k1q+k2p^2-k2p-k2q^2,
E0 = k1p^2q+k1pq-k1q^3-k1q-k2p^2+2k2pq^2+k2p,
```
the following is an exact polynomial identity in `ℤ[p,q,k1,k2,l1]`
(verified by direct symbolic expansion — `sympy.expand` of the difference
is the zero polynomial — independently re-derived twice from the raw
definitions, not copy-checked):
```
Fn\_num\_raw\cdot D2 - (k2-q)\cdot eq2\_num = D\cdot X\cdot(E1\,l1+E0).      (‡)
```

### §6. Closing the proof

At the valid configuration: `X=0` (§4, locus) and `eq2\_num=0` (§4). By
(‡), the right side vanishes, so `Fn\_num\_raw\cdot D2=0`. Since `D2\ne0`
(§3), **`Fn\_num\_raw=0`**. Combined with `Fn\_den\_raw\ne0` (§5),
```
O_x - (p/2+1/4) = Fn\_num\_raw/Fn\_den\_raw = 0,
```
i.e. `O_x = p/2+1/4` — exactly the target `(★)` of §1. By Lemma 0 (§1),
this is equivalent to `OM=ON`. **∎**

### Summary of what is proved and how

Every step above is either (i) elementary vector/coordinate algebra
verified symbolically and reproducible by direct hand computation (§0,
§1, the cross-product computations in §3, the factorization in §4), (ii) a
short, self-contained geometric lemma proved from the standard
barycentric/cone characterization of triangle- and angle-interior (the
Master Fact and its application in §3), or (iii) the single deep
polynomial identity (‡) of §5, independently verified twice by direct
symbolic expansion (`sympy.expand(LHS-RHS)==0`) with no numerical
approximation and no free/unproven parameters. No step relies on
generic-position assumptions, continuity arguments, or the numeric
witness (which was used only as a sanity check throughout, never as a
proof step). All four containment hypotheses and the three angle
hypotheses are used explicitly and are load-bearing (three angle
hypotheses → `eq1,eq2,eq3`; `K∈△BMC`, `L∈△BNC` → the barycentric
expansions in §3(a),(e),(f) and the `D\ne0`/`D2\ne0` proofs; `K∈∠LBA`,
`L∈∠ACK` → §3(c),(d)). This is a complete, rigorous proof.

## Promotable lemmas

**Closing polynomial identity (Step 4).** With `D,D2,X,eq2_num,Fn_num_raw`
as defined above (all explicit polynomials in `k1,k2,l1,p,q`, arising from
the WLOG frame `B=(0,0),C=(1,0),A=(p,q)` and the Dictionary-Lemma
translation of hypotheses (i)-(iii)), and
```
E1 = −2k1pq + k1q + k2p² − k2p − k2q²,
E0 = k1p²q + k1pq − k1q³ − k1q − k2p² + 2k2pq² + k2p,
```
the identity
```
Fn_num_raw·D2 − (k2−q)·eq2_num = D·X·(E1·l1+E0)
```
holds as an exact polynomial identity in `ℤ[p,q,k1,k2,l1]`, verified by
direct symbolic expansion (`sympy.expand` of the difference is `0`). This
is a purely algebraic fact about the specific polynomials `D,D2,X,
eq2_num,Fn_num_raw` defined in Steps 1–4 above, self-contained and
reproducible from those definitions; promotable as a certified lemma for
this approach's continued use (and for `symmetric-vector-decomposition-sigma`
or any other approach that reaches the same or an affinely-equivalent
target variety, e.g. via the noted algebraic isomorphism with
`homothety-doubling-target`'s target).

**`D_circ = 2D3/D` relation.** The circumcenter denominator of `A,K,L`
(with `L_y` eliminated via Step 1) equals `2D3/D`, where `D3` is the second
factor of `Fn_den_raw` — hence `D_circ\ne0` (guaranteed since `O` is
assumed to exist) together with `D\ne0` automatically gives `D3\ne0`,
reducing the genericity bookkeeping needed for Step 4/5 to the single
condition `D\ne0` (plus `D2\ne0` for the division in (‡) to make sense).
Small but reusable simplification for anyone re-deriving this chain.

**Master Fact (positive-combination / cone-sign toolkit) — proved in full
in §3 of the Full proof above.** For linearly independent planar vectors
`v,w`: (1) if `u=sv+tw` with `s,t>0` then `cross(v,u)` and `cross(u,w)`
both have the sign of `cross(v,w)` (bilinearity); (2) if additionally
`w=av+bx` with `a,b>0` (`v,x` independent), substituting gives `u` as a
positive combination of `v,x`. Combined with the standard cone/barycentric
characterizations of "interior of an angle" and "interior of a triangle",
this converts *any* strict-containment hypothesis of this shape (a point
inside a triangle or inside an angle spanned by two named rays) directly
into a definite-sign cross-product inequality, with no reference to a
numeric witness and no genericity assumption. Used here to (i) settle the
orientation/sign-matching gap for the Dictionary Lemma (§3, "Conclusion of
§3, part 1") and (ii) give elementary, exact proofs that `D\ne0` and
`D2\ne0` (§3, "part 2"), replacing a resultant/continuity argument.
General-purpose: reusable for any olympiad configuration proof that needs
to convert containment/betweenness hypotheses into signed cross-product
data (e.g. to fix the orientation convention in a Dictionary-Lemma-style
translation of an angle equality into algebra).
