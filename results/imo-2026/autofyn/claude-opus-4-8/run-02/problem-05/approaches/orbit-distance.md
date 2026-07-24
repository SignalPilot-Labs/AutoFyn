## Status
solved

## Approaches tried
- (this file) orbit-distance: derive the FE, note orbits are arithmetic progressions, force all gaps
  equal by comparing two orbits at BOUNDED distance while both run to +infinity, then split on the
  existence of a fixed point. Round 1: filled to a complete rigorous proof. The one place the outline
  left as "O(1) remainder" is in fact an exact perfect square, so the crux is airtight. Outcome: solved.

## Current best
Answer: **f(x) = x + c for a constant c >= 0**, and this is the entire solution set. The full proof
below is complete and gap-free.

## Full proof

Throughout, "the chain" means the hypothesis: for all `x, y > 0`,
```
        sqrt( (x^2 + f(y)^2) / 2 )   >=   (f(x) + y) / 2   >=   sqrt( x * f(y) ).      (chain)
```
Since `f` maps into `R_>0`, every quantity under a square root and every displayed term is positive,
so we may square each half of the chain without changing its direction. Squaring the left half and
the right half respectively gives the two equivalent polynomial inequalities, valid for all `x, y > 0`:
```
   (A)   2 ( x^2 + f(y)^2 )  >=  ( f(x) + y )^2 ,
   (B)   ( f(x) + y )^2      >=  4 x f(y) .
```
(The squaring is reversible because both sides of each half of the chain are positive: e.g. the right
half `(f(x)+y)/2 >= sqrt(x f(y))` has both sides `>= 0`, so it is equivalent to the square (B); the
left half likewise.) We will use (A) and (B) freely below.

We write `g(x) := f(x) - x` for the "gap" function; note `g` is a priori just a function `R_>0 -> R`.

---

### Part I — The construction (existence half): every `f(x) = x + c`, `c >= 0`, is a solution.

Let `c >= 0` and put `f(x) = x + c`. Since `x > 0` and `c >= 0`, we have `f(x) = x + c > 0`, so `f`
does map `R_>0` into `R_>0`. Now check (A) and (B). With `f(x) = x + c` and `f(y) = y + c`:
```
   2(x^2 + f(y)^2) - (f(x) + y)^2 = 2x^2 + 2(y+c)^2 - (x + c + y)^2 = (x - y - c)^2 ,
   (f(x) + y)^2 - 4 x f(y)        = (x + c + y)^2 - 4x(y + c)      = (x - y - c)^2 .
```
(Both identities are elementary expansions; each right-hand side is `(x - y - c)^2`.) Since a square
is `>= 0`, both (A) and (B) hold for all `x, y > 0`. Hence `f(x) = x + c` satisfies the chain, with
equality throughout exactly when `x = y + c`.

Conceptually this is **QM-AM-GM** applied to the pair `{x, f(y)}`: for `f(x) = x + c` we have
`f(x) + y = x + f(y)`, so the chain reads `QM(x, f(y)) >= AM(x, f(y)) >= GM(x, f(y))`, which is the
standard chain of means (knowledge_base: "Standard inequalities: QM-AM-GM and their equality cases"),
equality iff `x = f(y)`, i.e. `x = y + c`.

We must also record the codomain constraint on `c`. If `c < 0`, pick any `x` with `0 < x < -c`; then
`f(x) = x + c < 0`, contradicting `f : R_>0 -> R_>0`. Hence `c >= 0` is forced. Thus **every**
`c >= 0` gives a solution, and no `c < 0` gives a function into `R_>0`.

This proves that each `f(x) = x + c` with `c >= 0` is a solution. Parts II-VI prove these are the only
solutions.

---

### Part II — The derived functional equation `f(f(y)) = 2 f(y) - y`.

Fix `y > 0` and substitute `x = f(y)` (which is `> 0`, hence a legal value of the variable `x`) into
the chain. In the left member, `sqrt( (x^2 + f(y)^2)/2 )` becomes
`sqrt( (f(y)^2 + f(y)^2)/2 ) = sqrt( f(y)^2 ) = f(y)` (using `f(y) > 0`). In the right member,
`sqrt( x f(y) )` becomes `sqrt( f(y) f(y) ) = f(y)`. The middle member is `(f(f(y)) + y)/2`. So the
chain becomes
```
        f(y)   >=   ( f(f(y)) + y ) / 2   >=   f(y) .
```
The two outer members are equal, so the middle member is squeezed to equal them:
`( f(f(y)) + y ) / 2 = f(y)`, i.e.
```
        f(f(y)) = 2 f(y) - y        for all y > 0.                                    (FE)
```
This is the "degenerate equality substitution" for a means chain (knowledge_base: "Functional
equations: test special values / substitutions", and the equality case of QM-AM-GM). No hand-waving:
both squeezes are forced because the outer terms are literally equal after the substitution.

---

### Part III — Orbits are arithmetic progressions; `g` is orbit-invariant; `g >= 0`.

**Orbit-invariance of `g`.** For any `y > 0`, using (FE),
```
   g(f(y)) = f(f(y)) - f(y) = (2 f(y) - y) - f(y) = f(y) - y = g(y).                  (I)
```
So `g` takes the same value at `y` and at `f(y)`.

**Orbits are arithmetic progressions.** Fix `y > 0` and define its forward orbit by `x_0 = y` and
`x_{n+1} = f(x_n)` for `n >= 0`. Each `x_n` lies in `R_>0` (it is `y > 0` for `n = 0`, and a value of
`f` for `n >= 1`). Applying (FE) at the point `x_n` gives
`x_{n+2} = f(x_{n+1}) = f(f(x_n)) = 2 f(x_n) - x_n = 2 x_{n+1} - x_n`, i.e.
```
        x_{n+2} - x_{n+1} = x_{n+1} - x_n .
```
So the consecutive differences are all equal to `x_1 - x_0 = f(y) - y = g(y)`. By telescoping,
```
        x_n = f^n(y) = y + n * g(y)        for all n >= 0.                            (II)
```
(This is the solution of the linear recurrence `x_{n+2} = 2 x_{n+1} - x_n` with characteristic double
root `1`; equivalently, constant consecutive differences give an arithmetic progression.) In particular,
by (I) and induction, `g(x_n) = g(y)` for every `n`, confirming `g` is constant along the whole orbit.

**Non-negativity `g >= 0`.** Suppose for contradiction `g(y) < 0` for some `y > 0`. Then by (II),
`x_n = y + n g(y) -> -infinity` as `n -> infinity`. But every `x_n` lies in `R_>0`, so `x_n > 0` for
all `n` — impossible. Hence
```
        g(y) >= 0,  i.e.  f(y) >= y,   for all y > 0.                                 (III)
```

**(Bonus) `f` is injective.** If `f(a) = f(b)`, then by (FE)
`2 f(a) - a = f(f(a)) = f(f(b)) = 2 f(b) - b`, so `a = b`. (Not needed below, recorded for completeness.)

---

### Part IV — The crux: all points with positive gap share one gap value.

**Claim.** If `a, b > 0` satisfy `alpha := g(a) > 0` and `beta := g(b) > 0`, then `alpha = beta`.

*Proof.* Consider the two forward orbits. For `k >= 0` set
```
        x_k := f^k(a) = a + k * alpha        (by (II)),
```
so `x_k in R_>0`, `x_k -> +infinity`, `g(x_k) = alpha`, and hence `f(x_k) = x_k + alpha`.

Next we pick, for each large `k`, a point in `b`'s orbit lying within `beta/2` of `x_k`. Define the
integer
```
        m_k := round( (x_k - b) / beta )       (nearest integer, ties either way).
```
By definition of nearest integer, `| (x_k - b)/beta - m_k | <= 1/2`, i.e.
```
        | x_k - (b + m_k beta) | <= beta / 2 .                                        (IV.1)
```
Since `x_k -> +infinity`, we have `(x_k - b)/beta -> +infinity`, so there is `K` with `m_k >= 0` for
all `k >= K` (indeed `m_k >= (x_k - b)/beta - 1/2 -> +infinity`). For `k >= K`, define
```
        y_k := f^{m_k}(b) = b + m_k * beta      (by (II), valid as m_k >= 0),
```
so `y_k in R_>0`, `g(y_k) = beta`, `f(y_k) = y_k + beta`. Put `d_k := x_k - y_k`; by (IV.1),
```
        | d_k | <= beta / 2   for all k >= K.                                         (IV.2)
```

Now apply inequality **(B)** to the ordered pair `(x, y) = (x_k, y_k)` (both are in `R_>0`, so this is
legal). Using `f(x_k) = x_k + alpha`, `f(y_k) = y_k + beta`, and `y_k = x_k - d_k`:
```
   (B)-residual := (f(x_k) + y_k)^2 - 4 x_k f(y_k)
                 = (x_k + alpha + y_k)^2 - 4 x_k (y_k + beta) .
```
Substituting `y_k = x_k - d_k` and expanding (verified symbolically):
```
   (x_k + alpha + (x_k - d_k))^2 - 4 x_k ((x_k - d_k) + beta)
       = 4 x_k (alpha - beta) + (alpha - d_k)^2 .                                     (IV.3)
```
Indeed, expanding `(2 x_k + alpha - d_k)^2 - 4 x_k (x_k - d_k + beta)`
`= 4 x_k^2 + 4 x_k(alpha - d_k) + (alpha - d_k)^2 - 4 x_k^2 + 4 x_k d_k - 4 x_k beta`
`= 4 x_k (alpha - d_k + d_k - beta) + (alpha - d_k)^2 = 4 x_k(alpha - beta) + (alpha - d_k)^2`,
confirming (IV.3). Inequality (B) states that this residual is `>= 0`:
```
        4 x_k (alpha - beta) + (alpha - d_k)^2 >= 0        for all k >= K.            (IV.4)
```

Suppose, for contradiction, that `alpha < beta`. The remainder term `(alpha - d_k)^2` is a bounded
non-negative square: by (IV.2), `|alpha - d_k| <= alpha + |d_k| <= alpha + beta/2`, so
`0 <= (alpha - d_k)^2 <= (alpha + beta/2)^2 =: M`, a constant independent of `k`. Meanwhile
`4 x_k (alpha - beta) -> -infinity` because `alpha - beta < 0` and `x_k -> +infinity`. Hence the
left-hand side of (IV.4) is at most `4 x_k(alpha - beta) + M -> -infinity`, so it is `< 0` for all
sufficiently large `k`, contradicting (IV.4). Therefore `alpha >= beta`.

By the identical argument with the roles of `a` and `b` interchanged (build `x'_k = b + k beta -> ∞`
in `b`'s orbit and `y'_k` in `a`'s orbit within `alpha/2`, then apply (B) to `(x'_k, y'_k)`), we get
`beta >= alpha`. Combining, `alpha = beta`. This proves the Claim. ∎

**Consequence.** All positive values of `g` coincide. Together with (III) (`g >= 0`), there is a single
constant `c >= 0` such that
```
        g(t) in {0, c}   for every t > 0,   and   g(t) = c  whenever g(t) > 0.       (IV.5)
```
(If `g` is identically `0`, take `c = 0`. Otherwise `c` is the common positive gap value from the Claim.)

---

### Part V — No mixing: `f(x) = x + c` for one global constant `c >= 0`.

We split into two exhaustive, disjoint cases according to whether `f` has a fixed point.

**Case A: `f` has no fixed point**, i.e. `g(t) > 0` for all `t > 0`. Then by (IV.5), `g(t) = c` for
every `t`, and `c > 0`. Hence `f(x) = x + c` with `c > 0`. Done in this case.

**Case B: `f` has a fixed point**, i.e. there is `a > 0` with `f(a) = a` (equivalently `g(a) = 0`).
We prove `f = id` (so `c = 0`).

Assume for contradiction that some point has positive gap; by (IV.5) every positive gap equals the same
`c > 0`. We first show:
```
   (V.1)   every point b > 0 with g(b) > 0 satisfies |b - a| > c;
           equivalently, every b > 0 with |b - a| <= c has g(b) = 0 (is a fixed point).
```
To prove (V.1), apply inequality **(A)** to the ordered pair `(x, y) = (b, a)`, using `f(a) = a` and
`f(b) = b + c`:
```
        2 ( b^2 + f(a)^2 ) >= ( f(b) + a )^2
   <=>  2 ( b^2 + a^2 )    >= ( b + c + a )^2 .
```
Expanding the difference of the two sides (verified symbolically):
```
   2(b^2 + a^2) - (b + c + a)^2 = (b - a)^2 - ( 2c(a + b) + c^2 ) ,
```
so (A) at `(b, a)` is equivalent to
```
        (b - a)^2 >= 2c(a + b) + c^2 .
```
Since `a, b > 0` and `c > 0`, the right-hand side satisfies `2c(a + b) + c^2 > c^2`. Therefore
`(b - a)^2 > c^2`, i.e. `|b - a| > c`. This proves the first form of (V.1); the contrapositive is the
second form: if `|b - a| <= c` then `g(b)` cannot be positive, so `g(b) = 0`. This establishes (V.1).

Note (V.1) applies with `a` replaced by ANY fixed point `t` (the derivation only used `f(t) = t`). So:
```
   (V.2)   if t is a fixed point and |s - t| <= c (s > 0), then s is a fixed point.
```

**Covering `(0, infinity)` by fixed points.** Let `F = { t > 0 : f(t) = t }` be the fixed-point set;
`a in F`. We show `F = (0, infinity)`. Take any target `s > 0`; we show `s in F`. The straight segment
between `a` and `s` is `[ min(a, s), max(a, s) ] subset (0, infinity)` (both endpoints are `> 0`).
Choose an integer `N` with `N >= |s - a| / c` (so `N >= 1`), and set the step
`delta := (s - a) / N`, which satisfies `|delta| = |s - a| / N <= c`. Define the chain
```
        t_0 = a,   t_{j+1} = t_j + delta   for j = 0, 1, ..., N - 1,   so   t_N = s.
```
Each `t_j` lies on the segment between `a` and `s`, hence `t_j > 0`. We prove by induction that every
`t_j in F`. Base: `t_0 = a in F`. Step: if `t_j in F`, then `|t_{j+1} - t_j| = |delta| <= c` and
`t_{j+1} > 0`, so by (V.2) (with `t = t_j`, `s = t_{j+1}`) we get `t_{j+1} in F`. Hence `t_N = s in F`.
As `s > 0` was arbitrary, `F = (0, infinity)`, i.e. `f(t) = t` for all `t`.

But that contradicts our assumption that some point has positive gap `c > 0`. Therefore in Case B no
positive-gap point exists: `g equiv 0`, i.e. `f = id` (`c = 0`). Done in this case.

Cases A and B are exhaustive (either `f` has a fixed point or it does not) and each yields
`f(x) = x + c` for a single constant `c >= 0`.

---

### Part VI — Conclusion and verification.

By Part V, every solution `f` of the chain has the form `f(x) = x + c` for some constant `c >= 0`
(the value `c = beta > 0` in Case A, or `c = 0` in Case B). By Part I, every such `f` with `c >= 0`
is indeed a solution and lies in `R_>0 -> R_>0`, while `c < 0` is impossible for a positive codomain.
Substituting `f(x) = x + c` back into the chain reduces (as computed in Part I) both inequalities to
`(x - y - c)^2 >= 0`, confirming the chain holds for all `x, y > 0`.

**Therefore the complete solution set is**
```
        f(x) = x + c,     with c a constant and c >= 0.
```
∎

## Promotable lemmas

- **FE-collapse lemma.** *If `f : R_>0 -> R_>0` satisfies the QM-AM-GM chain
  `sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y))` for all `x,y>0`, then `f(f(y)) = 2f(y) - y` for
  all `y > 0`.* Proved in Part II by substituting `x = f(y)` and using the equality case of QM-AM-GM
  (both outer members collapse to `f(y)`). Reusable by any approach to this problem.

- **AP-orbit lemma.** *Under (FE), for every `y > 0`, `f^n(y) = y + n g(y)` for all `n >= 0`, where
  `g = f - id`; moreover `g(f(y)) = g(y)` (orbit-invariance) and `g >= 0` (from codomain positivity).*
  Proved in Part III.

- **Single-gap (crux) lemma.** *Under the chain, if `g(a), g(b) > 0` then `g(a) = g(b)`; hence
  `g(t) in {0, c}` for a single `c >= 0`.* Proved in Part IV via the bounded-distance two-orbit
  comparison with exact residual `4 x_k(g(a) - g(b)) + (g(a) - d_k)^2`.

## Spec concerns

None. The skeleton was correct in every particular. The only refinement over the outline: the (B)-
residual remainder that the outline called "O(1)" is exactly the perfect square `(alpha - d_k)^2`
(confirmed symbolically), which makes the sign argument fully rigorous rather than asymptotic; and the
Part V covering is done along the straight segment `[min(a,s), max(a,s)]` (bounded away from `0`), which
cleanly avoids any "stepping down to `0`" subtlety. All algebraic identities were verified with sympy.
