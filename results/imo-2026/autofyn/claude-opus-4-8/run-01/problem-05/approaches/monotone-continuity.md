## Status
solved

## Approaches tried
- (round 1, order/topology route) Earned the two-sided squeeze (♦) that gives continuity of `f` at
  every image point and correct ordering of `f` through every image point; established the
  affine-iterate law (★), orbit = arithmetic progression, `g:=f−id ≥ 0` and orbit-invariant; closed
  constancy of `g` via the orbit-interleaving-at-infinity limit (all positive defects equal) and a
  clean **openness + connectedness** finish for the mixed zero/positive case. Full monotonicity and
  continuity of `f` drop out a posteriori once `g` is constant. — worked; complete proof below.

## Current best
Complete proof (below). The order/topology content is genuine: the squeeze (♦) yields continuity of
`f` at image points and the sign law `sign(f(x)−f(t)) = sign(x−t)` for `t∈Im(f)`; the constancy of
`g` is forced by the two-point lever (∗) through an interleaving limit and a connectedness argument
on the partition of `(0,∞)` into two open sets. Answer: **f(x) = x + c, c ≥ 0**.

## Full proof

Throughout write the two hypotheses, for all `x,y>0`, as
- **(L)** `(f(x)+y)/2 ≥ √(x·f(y))`  (AM–GM–type lower bound), and
- **(R)** `√((x²+f(y)²)/2) ≥ (f(x)+y)/2`  (QM-type upper bound).

All quantities `f(x)+y`, `√(x f(y))`, `√((x²+f(y)²)/2)` are positive, so for nonnegative reals
`u ≥ v ⟺ u² ≥ v²`; squaring (L) and (R) is therefore an equivalence, giving the equivalent forms
- **(L²)** `(f(x)+y)² ≥ 4x·f(y)`,
- **(R²)** `2(x² + f(y)²) ≥ (f(x)+y)²`,
both for all `x,y>0`.

**Claim (answer).** The functions satisfying (L) and (R) are exactly
`f(x) = x + c` for a constant `c ≥ 0`, and no others.

---

### Part (a): Sufficiency — every `f(x)=x+c` with `c≥0` works.

First, the codomain constraint. `f` must map into `ℝ_{>0}`. For `f(x)=x+c` we need `x+c>0` for every
`x>0`. If `c<0`, then for any `x∈(0,−c)` we get `x+c<0∉ℝ_{>0}`; so `c≥0` is necessary for `f` to be a
valid function `ℝ_{>0}→ℝ_{>0}`. Conversely if `c≥0` then `x+c>0` for all `x>0`, so `f` is well defined.

Now verify (L²) and (R²). With `f(x)=x+c`, `f(y)=y+c`:

- (L²) surplus:
  `(f(x)+y)² − 4x·f(y) = (x+c+y)² − 4x(y+c)`.
  Expanding, `(x+y+c)² = x²+y²+c²+2xy+2xc+2yc`, and `4x(y+c)=4xy+4xc`, so the surplus is
  `x²+y²+c²+2xy+2xc+2yc − 4xy − 4xc = x²+y²+c² − 2xy − 2xc + 2yc = (x−y−c)²`.
  (Verified in sympy: `(f(x)+y)²−4x f(y)` factors to `(x−y−c)²`.)
  Hence `(f(x)+y)² − 4x f(y) = (x−y−c)² ≥ 0`, i.e. (L²) holds.

- (R²) surplus:
  `2(x²+f(y)²) − (f(x)+y)² = 2x² + 2(y+c)² − (x+(y+c))²`.
  Put `u=y+c`: `2x²+2u²−(x+u)² = 2x²+2u²−x²−2xu−u² = x²−2xu+u² = (x−u)² = (x−y−c)²`.
  (Verified in sympy: same factorization `(x−y−c)²`.)
  Hence `2(x²+f(y)²) − (f(x)+y)² = (x−y−c)² ≥ 0`, i.e. (R²) holds.

Since both squared inequalities hold and squaring was an equivalence, (L) and (R) hold for every
`x,y>0`. So every `f(x)=x+c`, `c≥0`, is a solution. ∎ (a)

---

### Part (b): Necessity — any solution has the form `f(x)=x+c`, `c≥0`.

Fix a solution `f`. We use the abbreviation `g(y):=f(y)−y`.

#### Step 1. The affine-iterate law (★), injectivity, and the orbit is an arithmetic progression.

**(★): `f(f(y)) = 2f(y) − y` for all `y>0`.**
Set `x=f(y)` in the sandwich. Then
`√((x²+f(y)²)/2) = √((f(y)²+f(y)²)/2) = √(f(y)²) = f(y)` and `√(x f(y)) = √(f(y)·f(y)) = f(y)`.
So both outer terms equal `f(y)`, and the sandwich `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)` forces
`(f(f(y))+y)/2 = f(y)`, i.e. `f(f(y)) = 2f(y) − y`. This is (★).

**Injectivity.** Suppose `f(a)=f(b)`. Applying (★) at `a` and `b`, and using
`f(f(a))=f(f(b))` (as `f(a)=f(b)`), we get `2f(a)−a = 2f(b)−b`; combined with `f(a)=f(b)` this gives
`a=b`. So `f` is injective.

**The orbit is an arithmetic progression.** Fix `y>0` and define the iterate sequence
`a_0=y`, `a_{n+1}=f(a_n)` (so `a_n = f^{n}(y) ∈ ℝ_{>0}`, hence `a_n>0` for all `n≥0`).
Applying (★) at `a_n`: `f(f(a_n)) = 2f(a_n)−a_n`, i.e. `a_{n+2} = 2a_{n+1} − a_n`. Thus
`a_{n+2}−a_{n+1} = a_{n+1}−a_n` for every `n`, so `(a_n)` is an arithmetic progression with common
difference `d = a_1 − a_0 = f(y) − y = g(y)`. Therefore
`a_n = y + n·g(y)` for all `n ≥ 0`. **(orbit-AP)**

**`g ≥ 0`.** If `g(y)<0` for some `y`, then `a_n = y + n g(y) → −∞`, so `a_n<0` for large `n`,
contradicting `a_n = f^{n}(y) > 0`. Hence `g(y) ≥ 0`, i.e. `f(y) ≥ y`, for all `y`.

**Orbit-invariance of `g`.** From (★): `g(f(y)) = f(f(y)) − f(y) = (2f(y)−y) − f(y) = f(y) − y = g(y)`.
So `g` is constant along each orbit; by induction `g(a_n) = g(y)` for all `n≥0`.

#### Step 2. The two-sided squeeze (♦): order and continuity at image points.

Let `Im(f) = {f(y): y>0}`. Fix `t ∈ Im(f)`; by injectivity there is a unique `y_0` with `f(y_0)=t`.
By (★), `f(t) = f(f(y_0)) = 2f(y_0) − y_0 = 2t − y_0`, hence `y_0 = 2t − f(t)`.

Apply (L²) and (R²) at the point `(x, y_0)` for arbitrary `x>0`, using `f(y_0)=t`:
- (L²): `(f(x)+y_0)² ≥ 4x t`, and since both sides are nonnegative, `f(x)+y_0 ≥ 2√(xt)`, so
  `f(x) ≥ 2√(xt) − y_0`.
- (R²): `2(x²+t²) ≥ (f(x)+y_0)²`, so `f(x)+y_0 ≤ √(2(x²+t²))`, i.e.
  `f(x) ≤ √(2(x²+t²)) − y_0`.

Subtract `f(t) = 2t − y_0` (so `−y_0 − f(t) = −2t`) from both bounds:
- lower: `f(x) − f(t) ≥ 2√(xt) − y_0 − f(t) = 2√(xt) − 2t = 2√t(√x − √t)`;
- upper: `f(x) − f(t) ≤ √(2(x²+t²)) − y_0 − f(t) = √(2(x²+t²)) − 2t`.

Thus for **all** `x>0` and **all** `t∈Im(f)`:
```
(♦)     2√t(√x − √t)  ≤  f(x) − f(t)  ≤  √(2(x²+t²)) − 2t .
```

**Order through image points.** For `t∈Im(f)`:
- if `x>t` then the lower bound `2√t(√x−√t)>0`, so `f(x)>f(t)`;
- if `x<t` then `2x²+2t²<4t²`, so the upper bound `√(2(x²+t²))−2t<0`, so `f(x)<f(t)`.

Hence `sign(f(x) − f(t)) = sign(x − t)` for every `t∈Im(f)` and every `x>0`. **(sign law)**
In particular, taking both arguments in `Im(f)`, `f` is strictly increasing on `Im(f)`.

**Continuity at image points.** As `x→t`, the lower bound in (♦) tends to `2√t(√t−√t)=0` and the
upper bound tends to `√(2·2t²)−2t = 2t − 2t = 0`. By the squeeze, `f(x)→f(t)` as `x→t`, so `f` is
continuous at every `t∈Im(f)`. **(image-continuity)**

(These are the genuine order/topology facts the sandwich yields directly. Full strict monotonicity
and full continuity of `f` are obtained at the very end as corollaries, once `g` is shown constant.)

#### Step 3. The off-diagonal lever (∗).

Write `f = id + g`. Expanding (L²) with `f(x)=x+g(x)`, `f(y)=y+g(y)` and setting `a=x`, `b=y`:
`(a + g(a) + b)² − 4a(b + g(b)) = (a−b)² + 2(a+b)g(a) + g(a)² − 4a·g(b)`
(the identity is exact; verified in sympy: the two sides expand to the same polynomial). Therefore
(L²) is equivalent to
```
(∗)     (a−b)² + 2(a+b)g(a) + g(a)²  ≥  4a·g(b) ,   for all a,b>0 .
```

#### Step 4. All positive defects are equal.

Suppose `g(a)>0` and `g(b)>0` for some `a,b>0`. Consider the orbits
`A_n = a + n·g(a)` and `B_m = b + m·g(b)` (`n,m≥0`), which by (orbit-AP) lie in `ℝ_{>0}`, and by
orbit-invariance satisfy `g(A_n)=g(a)` and `g(B_m)=g(b)`. Since `g(a)>0`, `A_n→∞`; since `g(b)>0`,
the points `B_m` form an arithmetic progression with step `g(b)` marching to `+∞`.

For each `n` with `A_n ≥ b`, let `m=m(n)` be the largest integer with `B_m ≤ A_n` (it exists because
`B_0=b≤A_n` and `B_m→∞`). Then `B_{m+1} = B_m + g(b) > A_n`, so
```
0 ≤ A_n − B_m < g(b),      hence   (A_n − B_m)² < g(b)² ,   and   B_m ≤ A_n .
```
Apply (∗) with `(a,b) ← (A_n, B_m)`, using `g(A_n)=g(a)`, `g(B_m)=g(b)`:
```
4A_n·g(b) ≤ (A_n − B_m)² + 2(A_n+B_m)g(a) + g(a)²
         < g(b)² + 2(2A_n)g(a) + g(a)²        (using (A_n−B_m)²<g(b)² and B_m≤A_n)
         = g(b)² + 4A_n·g(a) + g(a)² .
```
Divide by `4A_n > 0`:
```
g(b) < g(a) + ( g(b)² + g(a)² ) / (4A_n) .
```
Letting `n→∞` (so `A_n→∞`) gives `g(b) ≤ g(a)`. By symmetry (swap `a` and `b` in the argument),
`g(a) ≤ g(b)`. Hence `g(a)=g(b)`.

Consequently there is a constant `c ≥ 0` such that **`g(y) ∈ {0, c}` for every `y>0`**: if `g` is
identically `0`, take `c=0`; otherwise let `c` be the (unique, by the above) common positive value of
all positive defects, and every `y` has `g(y)=0` or `g(y)=c`.

#### Step 5. Connectedness kills the mixed case ⇒ `g` is constant.

If `c=0`, then `g≡0`. Assume `c>0` and set
`Z = {y>0 : g(y)=0}`,  `P = {y>0 : g(y)=c}`.
By Step 4, `Z ⊔ P = (0,∞)` (disjoint union). We show both `Z` and `P` are open in `(0,∞)`.

The only cross-constraint we need is (∗) evaluated at `(a,b)=(z,β)` with `z∈Z` (so `g(z)=0`) and
`β∈P` (so `g(β)=c`):
`(z−β)² + 2(z+β)·0 + 0² ≥ 4z·c`, i.e.
```
(cross)     (β − z)² ≥ 4c·z ,   for all z∈Z, β∈P .
```

**`Z` is open.** Fix `z∈Z`. By (cross), no `β∈P` satisfies `(β−z)²<4cz`, i.e. every `β∈P` has
`|β−z| ≥ 2√(cz)`. Hence the interval `I = (z − 2√(cz),\ z + 2√(cz)) ∩ (0,∞)` contains no point of
`P`, so `I ⊆ Z`. Since `2√(cz)>0`, `z` is an interior point of `Z`. Thus `Z` is open.

**`P` is open.** Fix `β∈P`. Choose `δ = min(β/2,\ √(2cβ)) > 0`; then `δ ≤ β/2` so `β−δ ≥ β/2>0`, and
`δ² ≤ 2cβ ≤ 4c(β−δ)` (because `2cβ ≤ 4c(β−δ) ⟺ β ≤ 2β−2δ ⟺ δ ≤ β/2`, which holds). Suppose some
`z∈Z` lay in `(β−δ, β+δ)`. Then on one hand `(β−z)² < δ²`, and on the other hand, by (cross),
`(β−z)² ≥ 4cz > 4c(β−δ) ≥ δ²` (using `z > β−δ`), a contradiction. Hence `(β−δ,β+δ)∩Z=∅`, so
`(β−δ,β+δ) ⊆ P`, and `β` is interior to `P`. Thus `P` is open.

Now `(0,∞)` is connected (an interval), and `Z, P` are disjoint open sets with `Z ∪ P = (0,∞)`.
A connected space cannot be partitioned into two nonempty open sets, so `Z=∅` or `P=∅`. If `P=∅`
then `g≡0` (`c` effectively `0`); if `Z=∅` then `g≡c`. In every case `g` is a constant `c≥0`, i.e.
```
f(x) = x + c ,   c ≥ 0 .
```

#### Step 6. Verification and the order/topology corollaries.

By Part (a), `f(x)=x+c` with `c≥0` indeed satisfies (L) and (R) — verified there by the identities
`(f(x)+y)²−4x f(y) = (x−y−c)²` and `2(x²+f(y)²)−(f(x)+y)² = (x−y−c)²`, both `≥0`. So the necessity of
Step 5 combined with the sufficiency of Part (a) shows the solution set is **exactly**
`{f : f(x)=x+c,\ c≥0}`.

Finally, the framing's promise is redeemed as a corollary: with `f(x)=x+c` the function `f` is
strictly increasing and continuous on all of `(0,∞)` (an affine map with slope `1`), consistent with
the sign law and image-continuity of Step 2 (indeed `Im(f)=(c,∞)`, and (♦) there gives exactly the
correct order and continuity). This completes the characterization. ∎

---

**Remark (why (∗) is indispensable).** The functional relation (★) alone — even together with strict
monotonicity and continuity of `f` — does **not** force `g` constant: writing `f=id+g`, (★) is
*equivalent* to the orbit-invariance `g(f(y))=g(y)`, which merely says `g` is constant along the
arithmetic-progression orbits and imposes nothing transversally. The constancy is genuinely produced
by the inequality lever (∗): the interleaving limit of Step 4 (a topological/asymptotic argument on
the orbits) collapses all positive defects to one value, and the connectedness argument of Step 5 (a
purely topological partition argument) removes the remaining mixed possibility. This is why the proof
earns its order/topology content from the squeeze (♦) but must route the final rigidity through (∗).

## Promotable lemmas

- **`fe-star-and-orbit` (Step 1).** For any `f:ℝ_{>0}→ℝ_{>0}` satisfying (L),(R):
  (i) `f(f(y))=2f(y)−y`; (ii) `f` is injective; (iii) with `g=f−id`, `g≥0`; (iv) the orbit
  `f^{n}(y)=y+n·g(y)` is an arithmetic progression and `g(f(y))=g(y)` (orbit-invariance).
  Fully proved above from `x=f(y)` (QM=GM collapse) and orbit positivity.
- **`off-diagonal-lever` (∗) (Step 3).** (L²) is equivalent to
  `(a−b)²+2(a+b)g(a)+g(a)² ≥ 4a g(b)` for all `a,b>0` (exact expansion; sympy-verified).
- **`squeeze-diamond` (♦) (Step 2).** For `t∈Im(f)`: `2√t(√x−√t) ≤ f(x)−f(t) ≤ √(2(x²+t²))−2t`
  for all `x>0`; hence `f` is continuous at every image point and `sign(f(x)−f(t))=sign(x−t)`.
- **`defects-equal-and-constant` (Steps 4–5).** Under (∗)+(orbit-AP): all positive values of `g`
  coincide (interleaving limit), and `{g=0}`, `{g=c}` are both open, so by connectedness of `(0,∞)`
  `g` is constant. These are reusable for the sibling approaches.
