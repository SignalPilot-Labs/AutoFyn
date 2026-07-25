## Status
solved

## Approaches tried
- **Round 1, attempt 1.** Built the full shared base layer (FE, injectivity, orbit AP structure,
  sufficiency of `f(x)=x+c`) and the two cross tools (A),(B) from scratch, matching the
  outline-reviewer's independent re-derivation exactly (verified again here with sympy).
  Attempted the outline's "second orbit instance" elimination programme: fed Tool (A) with
  iterated orbit points of both `x0` and `y0`, obtaining a two-parameter family of inequalities
  and, in the case `g(y0)>0` with `g(x0)/g(y0)` irrational, closed it completely via a from-scratch
  finite pigeonhole (Dirichlet/Kronecker) density argument. This closed the "irrational-ratio"
  sub-case, but honestly left `g(y0)=0` (fixed point) and rational-ratio sub-cases open, so was
  recorded as `partial`.
- **Round 1, attempt 2 (this attempt, supersedes attempt 1).** Realized that Tool A/B, applied
  directly with `x` a small perturbation of `y` (not an orbit point), give a **local
  quadratic (Lipschitz-squared) bound** `|g(x)-g(y)| \le (x-y)^2/(4\min(f(x),f(y)))` for
  **every** pair `x,y>0` — no orbit-linking needed at all. Chaining this bound along a fine
  equal-spaced partition of the segment `[\min(x,y),\max(x,y)]` and using the triangle inequality
  gives, for every positive integer `N`, `|g(x)-g(y)| \le (x-y)^2/(4\min(x,y)\,N)`; since the left
  side does not depend on `N` and the right side `\to 0` as `N\to\infty`, this forces
  `g(x)=g(y)` **exactly**, for *all* `x,y>0` simultaneously — no case split on orbits, fixed
  points, or rationality of ratios is needed. This closes the approach's target gap completely
  and directly (the orbit/pigeonhole machinery of attempt 1 is no longer needed for the main
  proof, though it remains a valid, independently-checked partial result and is kept below as a
  certified reusable lemma). Combined with the base layer and sufficiency check, this completes
  a full solution of the problem.

## Current best
(superseded — see Full proof below, which is complete)

## Full proof

Throughout, `f:\mathbb R_{>0}\to\mathbb R_{>0}` is a function satisfying, for all `x,y>0`,
```
L(x,y):  2x^2 + 2f(y)^2 \ge (f(x)+y)^2      [from \sqrt{(x^2+f(y)^2)/2} \ge (f(x)+y)/2]
R(x,y):  (f(x)+y)^2 \ge 4x f(y)             [from (f(x)+y)/2 \ge \sqrt{xf(y)}]
```

### Step 1: the functional equation

**Lemma 1.** `f(f(y)) = 2f(y)-y` for all `y>0`.

*Proof.* Set `x=f(y)` in `L`: `2f(y)^2+2f(y)^2 \ge (f(f(y))+y)^2`, i.e. `4f(y)^2 \ge
(f(f(y))+y)^2`. Both `2f(y)` and `f(f(y))+y` are positive (as `f,y>0`), so taking square roots of
`A^2\ge B^2` with `A,B>0` gives `A\ge B`: `2f(y) \ge f(f(y))+y`. Set `x=f(y)` in `R`:
`(f(f(y))+y)^2 \ge 4f(y)^2`, and by the same square-root argument `f(f(y))+y \ge 2f(y)`.
Combining the two inequalities: `f(f(y))+y = 2f(y)`, i.e. `f(f(y)) = 2f(y)-y`. `\blacksquare`

### Step 2: injectivity

**Lemma 2.** `f` is injective.

*Proof.* If `f(a)=f(b)`, then by Lemma 1, `2f(a)-a = f(f(a)) = f(f(b)) = 2f(b)-b = 2f(a)-b`, so
`a=b`. `\blacksquare`

### Step 3: the deviation function `g` and its basic properties

Define `g(y):=f(y)-y` for `y>0`.

**Lemma 3.**
(a) `g(f(y)) = g(y)` for all `y>0`.
(b) For every integer `k\ge 0`, `f^{(k)}(y) = y+k\,g(y)` (where `f^{(k)}` is the `k`-fold
composition of `f`, `f^{(0)}=\mathrm{id}`), and `g(f^{(k)}(y))=g(y)`.
(c) `g(y)\ge 0` for all `y>0`, i.e. `f(y)\ge y`.

*Proof.* (a) `g(f(y)) = f(f(y))-f(y) = (2f(y)-y)-f(y) = f(y)-y = g(y)`, by Lemma 1.

(b) By simultaneous induction on `k`. Base case `k=0`: `f^{(0)}(y)=y=y+0\cdot g(y)` and
`g(f^{(0)}(y))=g(y)` trivially. Inductive step: assume `f^{(k-1)}(y)=y+(k-1)g(y)` and
`g(f^{(k-1)}(y))=g(y)`. Then
`f^{(k)}(y)=f(f^{(k-1)}(y))=f^{(k-1)}(y)+g(f^{(k-1)}(y))=[y+(k-1)g(y)]+g(y)=y+k\,g(y)`, and
`g(f^{(k)}(y))=g(f(f^{(k-1)}(y)))=g(f^{(k-1)}(y))` (by part (a), applied at the point
`z=f^{(k-1)}(y)`) `=g(y)` (by the inductive hypothesis). This completes the induction.

(c) By (b), `f^{(k)}(y)=y+k\,g(y)>0` for every `k\ge0` (since `f` maps `\mathbb R_{>0}` to itself,
every iterate is a positive real). If `g(y)<0`, choosing an integer `k` large enough that
`k\,g(y)<-y` gives `f^{(k)}(y)\le 0`, contradicting `f^{(k)}(y)\in\mathbb R_{>0}`. Hence
`g(y)\ge0`. `\blacksquare`

### Step 4: sufficiency of `f(x)=x+c`

**Lemma 4.** For every constant `c\ge 0`, the function `f(x)=x+c` satisfies both `L` and `R` for
all `x,y>0`.

*Proof.* Substituting `f(x)=x+c` into `R(x,y)`:
```
(x+c+y)^2 - 4x(y+c) = x^2+y^2+c^2+2xy+2xc+2yc - 4xy-4xc = x^2+y^2+c^2-2xy-2xc+2yc = (x-y-c)^2 \ge 0,
```
so `R` holds. Substituting into `L(x,y)`:
```
2x^2+2(y+c)^2-(x+y+c)^2 = 2x^2+2(y+c)^2-x^2-(y+c)^2-2x(y+c) = x^2+(y+c)^2-2x(y+c) = (x-(y+c))^2 \ge0,
```
so `L` holds. `\blacksquare`

### Step 5: the cross tools (A) and (B)

**Lemma 5.** For all `x,y>0`,
```
(A)   (x-y)^2  \ge  4 f(y)\,(g(x)-g(y))
(B)   (x-y)^2  \ge  4 f(x)\,(g(y)-g(x))
```
Both hold unconditionally.

*Proof of (A).* Apply `R` with the pair `(f(y),x)` in the `(x,y)`-slots: `R(f(y),x)` reads
`(f(f(y))+x)^2 \ge 4f(y)f(x)`. By Lemma 1, `f(f(y))=2f(y)-y`, so the left side equals
`(x-y+2f(y))^2`. Write `p:=g(x),\ q:=g(y)`, so `f(x)=x+p,\ f(y)=y+q`. Then
```
(x-y+2f(y))^2 - 4f(y)f(x) = (x+y+2q)^2 - 4(y+q)(x+p).
```
Expanding: `(x+y+2q)^2=(x+y)^2+4q(x+y)+4q^2`, and `4(y+q)(x+p)=4xy+4yp+4qx+4qp`. Subtracting the
second from the first:
```
(x+y)^2-4xy + 4q(x+y)-4yp-4qx-4qp+4q^2
 = (x-y)^2 + 4qy - 4yp + 4q^2 - 4qp                     [the 4qx terms cancel]
 = (x-y)^2 + 4y(q-p) + 4q(q-p)
 = (x-y)^2 + 4(q-p)(y+q)
 = (x-y)^2 - 4(p-q)f(y)                                  [since y+q=f(y)]
```
Since `R(f(y),x)` states this quantity is `\ge 0`, we get `(x-y)^2 \ge 4f(y)(p-q) =
4f(y)(g(x)-g(y))`, which is (A). (Independently verified by direct symbolic expansion with
`sympy`; the two sides agree identically as polynomials in `x,y,p,q`.)

*Proof of (B).* Swap the names `x\leftrightarrow y` throughout (A): `(y-x)^2 \ge
4f(x)(g(y)-g(x))`. Since `(y-x)^2=(x-y)^2`, this is (B). `\blacksquare`

### Step 6: `g` is globally constant

This is the key new step of this approach.

**Lemma 6 (local quadratic bound).** For all `x,y>0`,
```
|g(x)-g(y)| \le \frac{(x-y)^2}{4\min(f(x),f(y))}.
```

*Proof.* From (A): `g(x)-g(y) \le (x-y)^2/(4f(y))`. From (B): `g(y)-g(x) \le (x-y)^2/(4f(x))`,
i.e. `g(x)-g(y) \ge -(x-y)^2/(4f(x))`. Combining,
```
-\frac{(x-y)^2}{4f(x)} \le g(x)-g(y) \le \frac{(x-y)^2}{4f(y)},
```
so `|g(x)-g(y)| \le (x-y)^2 \cdot \max\!\big(1/(4f(x)),\,1/(4f(y))\big) = (x-y)^2/(4\min(f(x),f(y)))`.
`\blacksquare`

**Theorem (global constancy).** `g` is constant on `\mathbb R_{>0}`: there is a constant `c\ge0`
with `g(y)=c` for all `y>0`.

*Proof.* By Lemma 3(c), `f(t)\ge t` for every `t>0`; fix this fact for use below.

Let `x,y>0` be arbitrary with `x\ne y`; we show `g(x)=g(y)`. Set `a:=\min(x,y)>0` and
`b:=\max(x,y)`. For a positive integer `N`, partition `[a,b]` into `N` equal subintervals via the
points `z_i := a + i\,(b-a)/N` for `i=0,1,\dots,N`, so `z_0=a`, `z_N=b`, and each `z_i \in [a,b]`,
in particular `z_i \ge a>0`, so `z_i` is a valid point of `\mathbb R_{>0}`.

For each `i=1,\dots,N`, since `z_{i-1},z_i \ge a` and `f(t)\ge t` for all `t`, we have
`f(z_{i-1})\ge z_{i-1}\ge a` and `f(z_i)\ge z_i \ge a`, hence `\min(f(z_{i-1}),f(z_i)) \ge a`.
Applying Lemma 6 to the pair `(z_{i-1},z_i)` (or `(z_i,z_{i-1})`, the bound is symmetric):
```
|g(z_i)-g(z_{i-1})| \;\le\; \frac{(z_i-z_{i-1})^2}{4\min(f(z_{i-1}),f(z_i))} \;\le\;
\frac{\big((b-a)/N\big)^2}{4a}.
```
(The second inequality holds because increasing the denominator from `\min(f(z_{i-1}),f(z_i))\ge
a` to the possibly larger true value only decreases the fraction — formally, since
`\min(f(z_{i-1}),f(z_i))\ge a>0`, `1/\min(f(z_{i-1}),f(z_i)) \le 1/a`.)

By the triangle inequality, telescoping over `i=1,\dots,N`:
```
|g(b)-g(a)| = \Big|\sum_{i=1}^N \big(g(z_i)-g(z_{i-1})\big)\Big| \;\le\; \sum_{i=1}^N
|g(z_i)-g(z_{i-1})| \;\le\; N\cdot \frac{(b-a)^2/N^2}{4a} = \frac{(b-a)^2}{4aN}.
```
This holds for **every** positive integer `N`. The left side `|g(b)-g(a)|` is a fixed nonnegative
real number not depending on `N`, while the right side `\to 0` as `N\to\infty`. Hence for every
`\varepsilon>0`, choosing `N>(b-a)^2/(4a\varepsilon)` gives `|g(b)-g(a)|<\varepsilon`. Since this
holds for every `\varepsilon>0`, `|g(b)-g(a)|=0`, i.e. `g(a)=g(b)`, i.e. `g(x)=g(y)`.

(This is not an appeal to continuity of `f` or `g` — it is a purely finite, elementary argument:
for each fixed `N` we produce a genuine chain of `N` valid applications of the already-proven
Lemma 6 and sum them via the triangle inequality; the conclusion `g(a)=g(b)` follows from the
elementary real-analysis fact that a fixed nonnegative real number bounded above by a sequence of
positive reals tending to `0` must itself equal `0`.)

Since `x,y>0` were arbitrary, `g` is constant on `\mathbb R_{>0}`. Write `c` for this constant
value; by Lemma 3(c), `c=g(y)\ge0` for any `y`. `\blacksquare`

### Step 7: conclusion

By the Theorem, `f(y) = y+g(y) = y+c` for all `y>0`, for some fixed constant `c\ge 0`. By Lemma 4,
every such function *does* satisfy the original pair of inequalities `L,R` for all `x,y>0`
(equivalently the original inequality
`\sqrt{(x^2+f(y)^2)/2} \ge (f(x)+y)/2 \ge \sqrt{xf(y)}`, since `L,R` are exactly the squared forms
of the two inequalities in the chain, and all quantities involved — `x`, `f(x)+y`, `f(y)`, and
the two square-root expressions — are positive, so squaring/unsquaring is reversible term by
term). Conversely, the derivation of Lemmas 1–3 and the Theorem shows every solution `f` of the
original functional inequality must be of this form. Hence:

**Answer.** The functions `f:\mathbb R_{>0}\to\mathbb R_{>0}` satisfying
`\sqrt{(x^2+f(y)^2)/2} \ge (f(x)+y)/2 \ge \sqrt{xf(y)}` for all `x,y>0` are **exactly**
```
f(x) = x + c,  for some constant c \ge 0.
```

**Verification (explicit substitution into the original inequality).** For `f(x)=x+c` with
`c\ge0`, and any `x,y>0`:
- Right inequality: `(f(x)+y)/2 = (x+y+c)/2`, and
  `\big((x+y+c)/2\big)^2 - xf(y) = \big((x+y+c)^2-4x(y+c)\big)/4 = (x-y-c)^2/4 \ge 0` (computed in
  Lemma 4), so `(f(x)+y)/2 \ge \sqrt{xf(y)}` (both sides nonnegative, and the square of the left
  side minus the square of the right side is `\ge0`, and `(f(x)+y)/2>0`, so the inequality of
  square roots follows).
- Left inequality: `(x^2+f(y)^2)/2 - \big((f(x)+y)/2\big)^2 = \big(2x^2+2(y+c)^2-(x+y+c)^2\big)/4 =
  (x-y-c)^2/4 \ge 0` (computed in Lemma 4), so `\sqrt{(x^2+f(y)^2)/2} \ge (f(x)+y)/2` similarly.

Both reduce exactly to `(x-y-c)^2\ge 0`, confirming `f(x)=x+c` (`c\ge0`) is a solution for every
`c\ge0`, and the Theorem shows no other solutions exist. `\blacksquare`

## Promotable lemmas

- **Lemma 1 (functional equation)** `f(f(y))=2f(y)-y` — proved in full above from `L,R` via the
  substitution `x=f(y)`. Reusable base-layer fact, shared by all approaches to this problem.
- **Lemma 2 (injectivity)** — proved in full above from Lemma 1.
- **Lemma 3 (orbit structure)** `g\circ f=g`, `f^{(k)}(y)=y+kg(y)`, `g\ge0` — proved in full above
  by induction from Lemma 1. Reusable base-layer fact.
- **Lemma 4 (sufficiency of `f(x)=x+c`, `c\ge0`)** — proved in full above by direct algebraic
  expansion of both `L` and `R`; both reduce to `(x-y-c)^2\ge0`.
- **Lemma 5 (Tool A / Tool B, cross inequality)** `(x-y)^2 \ge 4f(y)(g(x)-g(y))` (and the
  `x\leftrightarrow y` swap) — proved in full above from `R(f(y),x)` and Lemma 1, independently
  verified with `sympy`. Load-bearing shared tool with the sibling `extremal-sup-inf` approach.
- **Lemma 6 (local quadratic bound)** `|g(x)-g(y)| \le (x-y)^2/(4\min(f(x),f(y)))` for all
  `x,y>0` — proved in full above by combining Tool A and Tool B pointwise (no orbit-linking or
  continuity assumption needed). This is the key new lemma of this approach.
- **Theorem (global constancy of `g`)** — proved in full above via a finite telescoping/triangle-
  inequality chain along an `N`-point partition of `[\min(x,y),\max(x,y)]`, using only Lemma 6 and
  `f(t)\ge t`; letting `N\to\infty` (in the elementary sense of "bounded above by a sequence
  `\to0`") forces `g(x)=g(y)` exactly for *all* `x,y>0`. This single lemma (Lemma 6 +
  telescoping argument) supersedes the more complicated orbit/Dirichlet-pigeonhole route
  attempted earlier this round, closing the previously-open `q_0=0` and rational-ratio gaps
  automatically, since it makes no reference to orbits at all. Strongly recommended for
  certification into `lemmas/` and reuse/promotion into `current.md`, as it completes the full
  characterization.
- **(Retained from attempt 1, still independently valid but no longer needed for the main proof)
  Lemma 5' (finite pigeonhole density for irrational rotations)**: for `p,q>0` with `p/q`
  irrational, `\{mp-nq : m,n\in\mathbb Z_{\ge0}\}` is dense in `\mathbb R` — proved from scratch
  via an elementary Dirichlet-box argument. General-purpose, reusable beyond this problem, kept
  here for reference though superseded for this proof's purposes by the simpler Lemma 6 route.
