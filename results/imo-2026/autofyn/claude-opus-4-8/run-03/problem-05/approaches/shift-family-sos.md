## Status
solved

## Approaches tried
- Algebraic quadratic-form squeeze (round 1, initial outline): reduce both inequalities on a
  general solution to two-variable inequalities in a=d(x), b=d(y) and force a=b directly —
  DEAD END as literally stated. The pointwise sum of the mirrored R-test and L-test collapses
  to `2(f(p)−f(q))² ≥ 0` (sympy-verified identity), so a *separated* two-valued d passes every
  interior pairwise instance; a universal pointwise "a=b" identity is unattainable.
- Quadratic-form squeeze + BOUNDARY-STRADDLE pin (round 1, this build): keep the R-test/L-test
  quadratic-form spine, split exhaustiveness into (Step 1) no two distinct *positive* d-values
  (growth bound from the R-test) and (Step 2) the residual {0,b} case, killed by a straddling
  pair: the raw L- and R-inequalities on a fixed/shift pair have failure bands that force BOTH
  {d=0} and {d=b} to be OPEN, contradicting connectedness of (0,∞). COMPLETE.

## Current best
Full proof below. Answer: **f(x) = x + c for every constant c ≥ 0, and no others.**
No open gaps.

## Full proof

Throughout, `f : ℝ_{>0} → ℝ_{>0}`. The hypothesis is: for all `x, y > 0`,
```
  sqrt( (x² + f(y)²)/2 ) ≥ (f(x)+y)/2 ≥ sqrt( x·f(y) ).            (★)
```

**Answer.** The solutions are exactly the shifts `f(x) = x + c` with a constant `c ≥ 0`.

### 0. Squared form of the hypothesis

All four quantities `sqrt((x²+f(y)²)/2)`, `(f(x)+y)/2`, `sqrt(x f(y))` are strictly positive
(`f > 0`, `x, y > 0`). A chain `u ≥ v ≥ w` of positive reals is equivalent to `u² ≥ v² ≥ w²`
(squaring is an order isomorphism on `[0,∞)`). Hence (★) is equivalent to: for all `x, y > 0`,
```
  L(x,y):  2( x² + f(y)² ) ≥ ( f(x) + y )²                          (upper defect)
  R(x,y):  ( f(x) + y )²  ≥ 4x·f(y)                                 (lower defect)
```
We use `L` and `R` in this squared form for the rest of the proof.

### 1. The existence direction: every `f(x) = x + c` with `c ≥ 0` works

Let `f(t) = t + c` with `c ≥ 0`. For `x, y > 0`:

*R-defect.*  `(f(x)+y)² − 4x f(y) = (x + y + c)² − 4x(y + c)`. Expanding,
`(x+y+c)² = x² + y² + c² + 2xy + 2cx + 2cy`, and `4x(y+c) = 4xy + 4cx`, so the difference is
`x² + y² + c² − 2xy − 2cx + 2cy = (x − y − c)²`. Thus `R(x,y)` holds, with equality iff `x = y + c`.

*L-defect.*  `2(x² + f(y)²) − (f(x)+y)² = 2x² + 2(y+c)² − (x+y+c)²`. Now
`2(y+c)² = 2y² + 4cy + 2c²`, and subtracting `(x+y+c)²` as above gives
`x² + y² + c² − 2xy − 2cx + 2cy = (x − y − c)²`. Thus `L(x,y)` holds, with equality iff `x = y + c`.

Both defects equal the same perfect square `((x−y) − c)² ≥ 0` (Sum-of-squares / completing the
square, knowledge_base.md "Sum of squares (SOS)"; verified symbolically with sympy). Finally the
codomain condition: `f(x) = x + c > 0` for all `x > 0` holds iff `c ≥ 0` (if `c < 0` then
`f(−c/2) = c/2 < 0`). Hence every `f(x) = x + c` with `c ≥ 0` is a valid solution. ∎(existence)

### 2. Structural lemmas (proved for EVERY solution `f`)

**Lemma A (composite identity).** `f(f(y)) = 2f(y) − y` for all `y > 0`.

*Proof.* Fix `y` and put `x = f(y) > 0` in (★).
- From `R(f(y), y)`: `(f(f(y)) + y)² ≥ 4 f(y)·f(y) = 4 f(y)²`. Both `f(f(y)) + y > 0` and
  `2f(y) > 0`, so taking square roots, `f(f(y)) + y ≥ 2f(y)`, i.e. `f(f(y)) ≥ 2f(y) − y`.
- From `L(f(y), y)`: `2( f(y)² + f(y)² ) = 4 f(y)² ≥ (f(f(y)) + y)²`. Taking square roots of the
  two nonnegative sides, `2f(y) ≥ f(f(y)) + y`, i.e. `f(f(y)) ≤ 2f(y) − y`.

The two bounds coincide, so `f(f(y)) = 2f(y) − y`. ∎

**Lemma B (injectivity).** `f` is injective. *Proof.* If `f(a) = f(b)`, then applying `f` again
`f(f(a)) = f(f(b))`, so by Lemma A `2f(a) − a = 2f(b) − b`; using `f(a) = f(b)` this gives `a = b`.
∎ (Not load-bearing below, but recorded.)

**Lemma C (orbit is an arithmetic progression; `d ≥ 0`).** Define `d(y) := f(y) − y`. Then:
1. `d(f(y)) = d(y)` for all `y` (`d` is invariant along the forward orbit).
2. Writing `f⁰(y) = y` and `f^{n+1}(y) = f(f^n(y))`, we have `f^n(y) = y + n·d(y)` for all `n ≥ 0`.
3. `d(y) ≥ 0` for all `y`; equivalently `f(y) ≥ y`.

*Proof.* (1) `d(f(y)) = f(f(y)) − f(y) = (2f(y) − y) − f(y) = f(y) − y = d(y)` by Lemma A.
(2) Induction on `n`. Base `n = 0` is trivial. If `f^n(y) = y + n·d(y)`, then applying (1)
iterated, `d(f^n(y)) = d(y)` (the point `f^n(y)` lies in the orbit, and `d` is unchanged at each
step), so `f^{n+1}(y) = f^n(y) + d(f^n(y)) = y + n·d(y) + d(y) = y + (n+1)·d(y)`.
(3) By (2), `f^n(y) = y + n·d(y)`. Since `f` maps into `ℝ_{>0}`, `f^n(y) > 0` for every `n ≥ 0`.
If `d(y) < 0`, then `y + n·d(y) → −∞`, so `f^n(y) < 0` for large `n` — impossible. Hence `d(y) ≥ 0`.
∎

Because of Lemma C, the whole problem reduces to showing that **`d` is constant**: if `d ≡ c` then
`f(x) = x + c`, and `c = d(y) ≥ 0`. Sections 3–5 prove `d` is constant.

### 3. Two quadratic-form tests

Fix any two points `p, q > 0` and set `a := d(p)`, `b := d(q)`. We record two consequences of
the hypothesis at the point `(x, y) = (f(p), q)`. Note `f(p) = p + a > 0`, and by Lemma C(1)
`d(f(p)) = d(p) = a`.

Substituting `f(x) = x + a`, `f(y) = y + b` and expanding `R` and `L` gives the exact reduced
forms (verified with sympy):
```
  R'(x,y):  (x − y)² + a² + 2a(x+y) − 4b·x ≥ 0
  L'(x,y):  (x − y)² − 2a(x+y) + 4b·y + 2b² − a² ≥ 0.
```
Here `a = d(x)`, `b = d(y)`. Setting `x = f(p) = p + a` (so `d(x) = a`) and `y = q` (`d(y) = b`)
and simplifying (sympy-verified) yields:

**R-test.**  `(p − q)² + 4(a − b)(p + a) ≥ 0.`                                   (I)

**L-test.**  `(p − q)² + 2(b − a)(a + b + 2q) ≥ 0.`                              (II)

*(Remark on the failed "universal pin": adding (I) and (II) gives
`2(p−q)² + 2(a−b)[2(p+a) − (a+b+2q)] = 2[(p−q)+(a−b)]² = 2(f(p)−f(q))² ≥ 0`, an identity carrying
no information. So no pointwise combination of (I),(II) can force `a = b`; the constraint must be
extracted globally, via growth (Section 4) and a boundary straddle (Section 5).)*

### 4. `d` takes at most one positive value

**Claim.** There do not exist two points with *distinct positive* `d`-values.

*Proof.* Suppose for contradiction there are values `0 < a < b` in the range of `d`; pick
`p₀, q₀ > 0` with `d(p₀) = a`, `d(q₀) = b`.

By Lemma C(2), the forward orbit of `p₀` is `p_n := f^n(p₀) = p₀ + n·a`, and each satisfies
`d(p_n) = a` (Lemma C(1) iterated). Likewise the forward orbit of `q₀` is `q₀ + m·b` (`m ≥ 0`),
each with `d`-value `b`.

Fix `n` large enough that `p_n = p₀ + n·a ≥ q₀`. The points `{q₀ + m·b : m ≥ 0}` form an
arithmetic progression with common difference `b > 0` starting at `q₀ ≤ p_n`; hence there is a
unique integer `m ≥ 0` with
```
  q₀ + m·b ≤ p_n < q₀ + (m+1)·b.
```
Put `Q_n := q₀ + m·b`, so `d(Q_n) = b` and `0 ≤ p_n − Q_n < b`.

Apply the R-test (I) to the pair `(p, q) = (p_n, Q_n)`, whose `d`-values are `a` and `b`
respectively:
```
  (p_n − Q_n)² + 4(a − b)(p_n + a) ≥ 0   ⟺   (p_n − Q_n)² ≥ 4(b − a)(p_n + a).
```
The left side is `< b²` (a fixed constant, since `0 ≤ p_n − Q_n < b`). The right side equals
`4(b − a)(p₀ + a + n·a)`, which `→ +∞` as `n → ∞` because `b − a > 0` and `a > 0`. Choosing `n`
so large that `4(b − a)(p₀ + a + n·a) > b²` gives `b² > (p_n − Q_n)² ≥ 4(b−a)(p_n+a) > b²`, a
contradiction. ∎

*(Note this argument genuinely needs the **smaller** value `a > 0`, so that the orbit `p_n` marches
to infinity. The remaining possibility — where the smaller of two distinct `d`-values is `0` — is
exactly the fixed-point/shift coexistence handled in Section 5.)*

By the Claim, the range of `d` contains at most one positive number. Combined with `d ≥ 0`
(Lemma C(3)), the range of `d` is contained in `{0, b}` for some real `b > 0` (or in `{0}`).

### 5. Fixed points and shifts cannot coexist (boundary straddle)

Suppose, for contradiction, that the range of `d` equals `{0, b}` with `b > 0` and **both** values
attained. Partition the domain:
```
  F := { x > 0 : d(x) = 0 } = { x : f(x) = x }   (fixed points),
  G := { x > 0 : d(x) = b } = { x : f(x) = x + b } (shifts by b).
```
Then `F, G` are nonempty, disjoint, and `F ∪ G = (0, ∞)`. We derive a contradiction with the
connectedness of `(0, ∞)` by showing **both `F` and `G` are open**.

We use two raw instances of the hypothesis on a *straddling pair* `x ∈ G`, `p ∈ F`
(so `f(x) = x + b`, `f(p) = p`). These are the reduced forms `L'`, `R'` of Section 3, evaluated
with the appropriate `d`-values (all verified with sympy):

- **L-straddle.** `L(x, p)` with `d(x) = b`, `d(p) = 0`:
  `2(x² + p²) ≥ (x + b + p)²`, equivalently
  ```
    (x − p)² − b(2x + 2p + b) ≥ 0.                                   (L*)
  ```
- **R-straddle.** `R(p, x)` with `d(p) = 0`, `d(x) = b`:
  `(p + x)² ≥ 4p(x + b)`, equivalently
  ```
    (x − p)² − 4b·p ≥ 0.                                             (R*)
  ```

**`F` is open.** Fix `p ∈ F`. Consider the quadratic in `x`
`φ(x) := (x − p)² − b(2x + 2p + b)`. Its discriminant is positive: solving `φ(x) = 0` gives roots
`x = (b + p) ± √(2b(b + 2p))`, so
```
  φ(x) < 0  for all x in the open interval  I_p := ( (b+p) − √(2b(b+2p)),  (b+p) + √(2b(b+2p)) ).
```
The center-check: `(b+p) − √(2b(b+2p)) < p` because `b < √(2b(b+2p))` (indeed
`b² < 2b(b+2p) = 2b² + 4bp` since `b, p > 0`), while `(b+p) + √(2b(b+2p)) > p` trivially. Hence
`I_p` is an open interval containing `p`. Now if some `x ∈ I_p ∩ (0,∞)` belonged to `G`, then
(L*) would give `φ(x) ≥ 0`, contradicting `φ(x) < 0`. Therefore `I_p ∩ (0,∞) ⊆ F`. Since `I_p`
is an open neighborhood of `p`, `p` is an interior point of `F`. As `p ∈ F` was arbitrary, `F` is
open. 

**`G` is open.** Fix `x ∈ G`. Consider the quadratic in `p`
`ψ(p) := (x − p)² − 4b·p`. Solving `ψ(p) = 0` gives roots `p = (2b + x) ± 2√(b(b + x))`, so
```
  ψ(p) < 0  for all p in the open interval  J_x := ( (2b+x) − 2√(b(b+x)),  (2b+x) + 2√(b(b+x)) ).
```
The center-check: `(2b+x) − 2√(b(b+x)) < x` because `b < √(b(b+x))` (indeed
`b² < b(b+x) = b² + bx` since `b, x > 0`), while `(2b+x) + 2√(b(b+x)) > x` trivially. Hence `J_x`
is an open interval containing `x`. Now if some `p ∈ J_x ∩ (0,∞)` belonged to `F`, then (R*) would
give `ψ(p) ≥ 0`, contradicting `ψ(p) < 0`. Therefore `J_x ∩ (0,∞) ⊆ G`. Since `J_x` is an open
neighborhood of `x`, `x` is an interior point of `G`. As `x ∈ G` was arbitrary, `G` is open.

**Contradiction.** `(0, ∞)` is connected; `F` and `G` are nonempty, disjoint, open, and cover it.
A connected space has no partition into two nonempty open sets (definition of connectedness /
knowledge_base.md "Casework/exhaustion" is not needed — this is the topological connectedness of
an interval). This is a contradiction. Hence the case range`(d) = {0, b}` is impossible. ∎

### 6. Conclusion

By Section 4 the range of `d` contains at most one positive value, so it is `⊆ {0, b}` for some
`b > 0`, or `⊆ {0}`. By Section 5 the two values `0` and `b` cannot both occur. Therefore the
range of `d` is a single number `c`:
- if range`(d) = {0}`, then `c = 0`;
- if range`(d) = {b}` (no fixed points), then `c = b > 0`.

In all cases `d(y) = c` for all `y`, i.e. `f(y) = y + c`, and `c = d(y) ≥ 0` by Lemma C(3).

Conversely, Section 1 showed every such `f(x) = x + c` with `c ≥ 0` satisfies (★). Therefore the
complete solution set is
```
  f(x) = x + c,   c ≥ 0  an arbitrary constant,
```
and there are no other solutions. ∎

## Promotable lemmas

- **Lemma A (composite identity).** For every solution `f` of (★), `f(f(y)) = 2f(y) − y`.
  Proved in §2 by setting `x = f(y)`, which makes both bounds of (★) tight. (Shared across all
  four approaches.)
- **Lemma C (orbit AP + nonnegativity).** With `d(y) := f(y) − y`: `d(f(y)) = d(y)`,
  `f^n(y) = y + n·d(y)`, and `d(y) ≥ 0`. Proved in §2. (Shared.)
- **Boundary-straddle openness lemma (this approach's contribution).** If a solution's shift
  `d = f − id` takes only values in `{0, b}` (`b > 0`) with both attained, then both `F = {d=0}`
  and `G = {d=b}` are open in `(0,∞)`: for `p ∈ F` the quadratic `(x−p)² − b(2x+2p+b)` is negative
  on an open interval around `p`, whose points cannot lie in `G` by `L(x,p)`; for `x ∈ G` the
  quadratic `(x−p)² − 4bp` is negative on an open interval around `x`, whose points cannot lie in
  `F` by `R(p,x)`. Connectedness of `(0,∞)` then forbids coexistence. Proved in full in §5.
