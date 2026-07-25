## Status
solved

## Approaches tried
- (round 1, cold start) Attempted the sup/inf limiting argument sketched in the outline: take a
  minimizing sequence for `m = inf g`, pass to the limit in Tool (A). This showed `m` is attained
  when the minimizing sequence has a finite positive limit point, but produced only a *local*
  bound `g(y) ≤ m + (y-x*)^2/(4(x*+m))` near the attaining point `x*` — not strong enough by
  itself to force `g ≡ m` globally (the bound blows up as `y` moves away from `x*`). This local
  bound alone is **not sufficient** and is superseded below.
- (round 1, same session) Discovered that Tool (A) — `(x-y)^2 ≥ 4f(y)(g(x)-g(y))`, which is an
  identity valid for **all** `x,y>0` (not just orbit-related pairs) — already gives, by taking
  `x = y+ε` for a genuine real perturbation `ε→0`, a *quadratic Lipschitz* bound that forces `g`
  to be **continuous** everywhere. This is a much sharper tool than the sup/inf-of-a-sequence
  idea in the original outline, and it is what actually closes the gap: continuity + injectivity
  (already proved) force `f` to be strictly monotonic, `f(y)≥y` forces "increasing" not
  "decreasing," and then a discrete orbit/crossing argument plus a case analysis on the zero-set
  of `g` forces global constancy. Full proof below — **worked, closes the gap completely.**

## Current best
Superseded by the full proof below (Status: solved).

## Full proof

Throughout, `f:\mathbb R_{>0}\to\mathbb R_{>0}` satisfies, for all `x,y>0`,
$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{x f(y)}. \qquad (\star)$$

We prove: **`(\star)` holds for all `x,y>0` if and only if `f(x) = x+c` for some constant `c\ge 0`.**

### Part 1 — Necessity: every solution has the form `f(x)=x+c`, `c\ge 0`

**Step 1 (Exact functional equation).** Fix `y>0` and substitute `x=f(y)` (legal since
`f(y)>0`) into `(\star)`. The left (QM) term becomes
`\sqrt{(f(y)^2+f(y)^2)/2}=f(y)`, and the right (GM) term becomes `\sqrt{f(y)\cdot f(y)}=f(y)`.
So `(\star)` reads
$$ f(y) \;\ge\; \frac{f(f(y))+y}{2} \;\ge\; f(y), $$
forcing equality throughout:
$$ f(f(y)) = 2f(y)-y \qquad \text{for all } y>0. \tag{$*$} $$

**Step 2 (Injectivity).** If `f(a)=f(b)`, apply `(*)` at `y=a` and `y=b`: `f(f(a))=2f(a)-a` and
`f(f(b))=2f(b)-b`. Since `f(a)=f(b)`, the left sides agree, so `2f(a)-a=2f(b)-b`, and since
`f(a)=f(b)` this collapses to `a=b`. So `f` is injective.

**Step 3 (`g:=f-\mathrm{id}` is nonnegative and orbit-invariant).** Define `g(y):=f(y)-y` for
`y>0`. Rewrite `(*)` as `f(f(y)) = f(y) + g(y)`, i.e.
$$ g(f(y)) = f(f(y)) - f(y) = \big(2f(y)-y\big) - f(y) = f(y)-y = g(y). $$
So `g(f(y))=g(y)` for every `y>0`. Consequently, defining the forward orbit `y_0=y`,
`y_{n+1}=f(y_n)`, induction gives `g(y_n)=g(y)` for all `n\ge 0` (base case trivial; if
`g(y_n)=g(y)` then `g(y_{n+1})=g(f(y_n))=g(y_n)=g(y)`), and then
$$ y_{n+1}=f(y_n)=y_n+g(y_n)=y_n+g(y) \implies y_n = y+n\,g(y) \quad\text{for all } n\ge 0. \tag{AP}$$
Since every `y_n=f^n(y)` must lie in `\mathbb R_{>0}` (as `f` maps into `\mathbb R_{>0}`), if
`g(y)<0` then `y_n=y+n g(y)\to-\infty`, eventually negative — contradiction. Hence
$$ g(y)\ge 0 \quad\text{for all } y>0. \tag{NN}$$

**Step 4 (Tool A/B — an unconditional algebraic identity for all `x,y>0`).** Apply the
right-hand (GM) inequality of `(\star)`, `(f(u)+v)^2\ge 4uf(v)`, at `u=f(y)`, `v=x` (legal, as
`f(y)>0`):
$$ \big(f(f(y))+x\big)^2 \;\ge\; 4\,f(y)\,f(x). $$
By `(*)`, `f(f(y))=2f(y)-y = y+2g(y)`. Write `p=g(x)`, `q=g(y)`, so `f(x)=x+p`, `f(y)=y+q`.
Substituting and expanding:
$$ (x+y+2q)^2 \;\ge\; 4(y+q)(x+p). $$
Expand both sides:
$$ (x+y)^2+4q(x+y)+4q^2 \;\ge\; 4xy+4yp+4qx+4pq. $$
Since `(x+y)^2-4xy=(x-y)^2`, the left side minus the right side is
$$ (x-y)^2 + 4q(x+y)+4q^2-4yp-4qx-4pq = (x-y)^2+4qy+4q^2-4yp-4pq = (x-y)^2+4(q-p)(y+q). $$
So the inequality `(f(f(y))+x)^2\ge 4f(y)f(x)` is exactly equivalent to
$$ (x-y)^2 \;\ge\; 4(p-q)(y+q) = 4\big(g(x)-g(y)\big)\,f(y). \tag{A}$$
This holds for **all** `x,y>0` (it used only `(\star)` at the single legal pair `(f(y),x)` and
the exact identity `(*)`; no further hypothesis). Swapping the names `x\leftrightarrow y` in this
universally-quantified statement gives the twin inequality, valid for all `x,y>0`:
$$ (x-y)^2 \;\ge\; 4\big(g(y)-g(x)\big)\,f(x). \tag{B}$$

**Step 5 (`g` is continuous).** Fix `y>0` and let `\varepsilon` be any real number with
`|\varepsilon|<y` (so `y+\varepsilon>0`). Apply (A) with `x=y+\varepsilon`:
$$ \varepsilon^2 \;\ge\; 4f(y)\big(g(y+\varepsilon)-g(y)\big) \implies g(y+\varepsilon)\le
g(y)+\frac{\varepsilon^2}{4f(y)}. $$
Apply (B) with `x=y+\varepsilon`:
$$ \varepsilon^2 \;\ge\; 4f(y+\varepsilon)\big(g(y)-g(y+\varepsilon)\big) \implies
g(y+\varepsilon)\ge g(y)-\frac{\varepsilon^2}{4f(y+\varepsilon)}. $$
By (NN), `f(t)=t+g(t)\ge t` for every `t>0`; in particular, for `|\varepsilon|<y/2` we get
`f(y+\varepsilon)\ge y+\varepsilon> y/2>0`, so
$$ \frac{\varepsilon^2}{4f(y+\varepsilon)} \le \frac{\varepsilon^2}{2y}. $$
Combining the two bounds, for `0<|\varepsilon|<y/2`,
$$ g(y)-\frac{\varepsilon^2}{2y} \;\le\; g(y+\varepsilon) \;\le\; g(y)+\frac{\varepsilon^2}{4f(y)}. $$
Both bracketing terms `\to 0` as `\varepsilon\to 0` (they are elementary rational functions of
the real number `\varepsilon`, evaluated at fixed `y,f(y)>0`), so by the squeeze theorem
`g(y+\varepsilon)\to g(y)` as `\varepsilon\to 0`. This holds at every `y>0`, so **`g` is
continuous on `\mathbb R_{>0}`**, and hence so is `f=\mathrm{id}+g`. (No hypothesis of continuity
of `f` was ever assumed; this continuity is *derived* purely from the algebraic consequence (A),
(B) of `(\star)`, applied to arbitrary real perturbations `\varepsilon`, not to orbit points.)

**Step 6 (`f` is strictly increasing).** `f` is continuous (Step 5) and injective (Step 2) on the
interval `\mathbb R_{>0}`. By the classical theorem that *a continuous injective real-valued
function on an interval is strictly monotonic* (proved via the Intermediate Value Theorem: if
`f` were not monotonic there would be points `a<b<c` with `f(b)` not between `f(a)` and `f(c)`;
then IVT applied on `[a,b]` or `[b,c]` would produce a point where `f` repeats a value already
attained, contradicting injectivity), `f` is either strictly increasing or strictly decreasing on
`\mathbb R_{>0}`.

Suppose `f` were strictly decreasing. Fix any `y_0>0`. For `y>y_0`, strict decrease gives
`f(y)<f(y_0)`; but `(NN)` gives `f(y)\ge y`. So `y\le f(y)<f(y_0)` for every `y>y_0`, i.e.
`f(y_0)` is a finite fixed upper bound for all `y>y_0` — false, since `y` ranges over all reals
greater than `y_0`, unbounded above. (Concretely, take `y=f(y_0)+1>y_0$: then `y\le f(y)<f(y_0)`
forces `f(y_0)+1\le f(y)<f(y_0)`, i.e. `f(y_0)+1<f(y_0)`, absurd.) This contradiction rules out
"decreasing." Hence **`f` is strictly increasing** on `\mathbb R_{>0}`.

**Step 7 (`g` is non-decreasing).** We show: for all `a<b`, `g(a)\le g(b)`.

Suppose not: `a<b` but `p:=g(a)>q:=g(b)\ge 0`. Since `f` is strictly increasing (Step 6) and, by
composition, so is every iterate `f^n` (a composition of strictly increasing functions is
strictly increasing), `a<b` implies `f^n(a)<f^n(b)` for every `n\ge 0`. By (AP) from Step 3,
`f^n(a)=a+np` and `f^n(b)=b+nq`. So for every `n\ge0`,
$$ a+np < b+nq \iff n(p-q) < b-a. $$
Since `p>q`, `p-q>0` is a fixed positive number, so the left side `\to+\infty` as `n\to\infty`,
while the right side `b-a` is fixed — contradiction for large `n`. Hence no such `a<b` with
`g(a)>g(b)` exists, i.e. **`g` is non-decreasing**: `a\le b \implies g(a)\le g(b)`.

**Step 8 (Crossing Lemma: two points with strictly positive `g`-values and `a<b` force
`g(a)=g(b)`).** Let `0<a<b` with `g(a)=q>0` and `g(b)=p>0`. By Step 7, `q\le p`. We show `q<p` is
impossible, forcing `q=p`.

Suppose `q<p`. Since `q>0`, the arithmetic progression `f^n(a)=a+nq$ (Step 3, (AP)) is strictly
increasing and unbounded, so `\{n\ge 1 : a+nq>b\}` is a nonempty set of positive integers (by the
Archimedean property); let `n_0` be its minimum. By minimality of `n_0`, `f^{n_0}(a)=a+n_0q>b`
strictly. Also `g(f^{n_0}(a))=g(a)=q` (orbit invariance, Step 3). Since `b<f^{n_0}(a)`, Step 7
(non-decreasing) gives
$$ g(b) \;\le\; g(f^{n_0}(a)) = q, \quad\text{i.e.}\quad p\le q, $$
contradicting `q<p`. Hence `q=p`, proving the Crossing Lemma: **whenever `a<b` and
`g(a),g(b)>0`, `g(a)=g(b)`.**

**Step 9 (Global constancy of `g`).** Let `Z:=\{t>0 : g(t)=0\}$.

*Claim: `Z` is "downward closed"*: if `t\in Z` and `0<t'\le t` then `t'\in Z`. Indeed, Step 7 gives
`g(t')\le g(t)=0`, and `g(t')\ge0` by (NN), so `g(t')=0`.

**Case (i): `Z=\emptyset`.** Then `g(t)>0` for every `t>0`. Take any `0<a<b`. Both `g(a)>0` and
`g(b)>0`, so the Crossing Lemma (Step 8) applies directly: `g(a)=g(b)`. Since `a<b` were
arbitrary positive reals, `g` is constant on `(0,\infty)`; call this constant `c`. Since `Z=\emptyset`, `c>0$.

**Case (ii): `Z\ne\emptyset`.** We show `Z=(0,\infty)`, i.e. `g\equiv 0`.

Suppose instead `Z\ne(0,\infty)`, so there is some `t_1\notin Z$, i.e. `g(t_1)>0`. Since `Z` is
downward closed and nonempty, it is bounded above (if `Z` were unbounded above, downward
closedness together with any `t>0` having some `z\in Z$ with `z>t$ would force `t\in Z`, i.e.
`Z=(0,\infty)`, excluded). Let `s:=\sup Z\in(0,\infty)$ (finite, as just argued; positive since
`Z` is a nonempty subset of `(0,\infty)`).

For any `t<s`, since `s=\sup Z`, `t` is not an upper bound of `Z`, so there is `z\in Z` with
`z>t`; downward closedness (`t<z\in Z`) gives `t\in Z`. Hence `(0,s)\subseteq Z`, i.e. `g\equiv0`
on `(0,s)`. By continuity of `g` (Step 5), `g(s)=\lim_{t\to s^-}g(t)=0`, so `s\in Z` as well.

For `t>s`: since `s=\sup Z`, no element of `Z` exceeds `s`, so `t\notin Z`, i.e. `g(t)>0`.

Now pick any `b_1,b_2` with `s<b_1<b_2`; both have `g(b_1),g(b_2)>0`, so the Crossing Lemma
(Step 8) gives `g(b_1)=g(b_2)`. As `b_1,b_2>s` were arbitrary, `g$ is constant, say `\equiv p'`,
on `(s,\infty)`, with `p'>0` (since `g(t)>0` for every `t>s`). But continuity of `g` at `s$ gives
$$ g(s) = \lim_{t\to s^+} g(t) = p'. $$
Since `g(s)=0` (shown above) and `p'>0`, this is a contradiction.

So the assumption `Z\ne(0,\infty)` (with `Z\ne\emptyset`) is impossible: **`Z=(0,\infty)`**, i.e.
`g\equiv 0`. This is the constant `c=0` case.

**Conclusion of Part 1.** Cases (i) and (ii) exhaust all possibilities for `Z=\{t:g(t)=0\}`
(either empty or not), and in both cases `g$ is a single global constant `c\ge0` (with `c>0` in
Case (i), `c=0` in Case (ii)). Hence
$$ f(x) = x+c \quad\text{for all } x>0, \text{ for some constant } c\ge 0. $$

### Part 2 — Sufficiency: `f(x)=x+c`, `c\ge0`, satisfies `(\star)` for all `x,y>0`

Let `f(x)=x+c` with `c\ge0` fixed, and let `x,y>0`. Write `A=x`, `B=y+c=f(y)`; note `A,B>0` and
`f(x)=x+c=A+c`... we verify the two squared inequalities directly (equivalent to `(\star)` since
all three quantities in `(\star)` are nonnegative — `\sqrt{\cdot}\ge0` always, and
`(f(x)+y)/2>0` since `f(x),y>0` — and squaring is monotonic on `[0,\infty)`).

**Left inequality** (`(x^2+f(y)^2)/2 \ge \big((f(x)+y)/2\big)^2`, i.e. `2x^2+2f(y)^2\ge(f(x)+y)^2`):
With `f(x)=x+c`, `f(y)=y+c`,
$$ 2x^2+2(y+c)^2 - (x+c+y)^2. $$
Set `A=x`, `B=y+c`; then `f(x)+y = A+B`, and
$$ 2A^2+2B^2-(A+B)^2 = A^2-2AB+B^2=(A-B)^2 = \big(x-(y+c)\big)^2 = (x-y-c)^2 \;\ge\;0. $$
So `2x^2+2f(y)^2 \ge (f(x)+y)^2`, i.e. the left inequality of `(\star)` holds, with equality iff
`x=y+c`.

**Right inequality** (`\big((f(x)+y)/2\big)^2 \ge xf(y)`, i.e. `(f(x)+y)^2\ge4xf(y)`):
$$ (x+c+y)^2-4x(y+c) = \big(x+(y+c)\big)^2-4x(y+c) = \big(x-(y+c)\big)^2 = (x-y-c)^2 \;\ge\; 0. $$
So `(f(x)+y)^2\ge4xf(y)`, i.e. the right inequality of `(\star)` holds, again with equality iff
`x=y+c`.

Since both squared inequalities hold for all `x,y>0` and all quantities involved are
nonnegative, taking square roots (monotonic on `[0,\infty)`) gives
$$ \sqrt{\frac{x^2+f(y)^2}{2}} \ge \frac{f(x)+y}{2} \ge \sqrt{xf(y)} \qquad \text{for all } x,y>0. $$
So `f(x)=x+c` satisfies `(\star)` for every constant `c\ge0`. (This also confirms the family is
genuinely infinite and that `c=0`, i.e. `f=\mathrm{id}`, is only one member — matching the
necessity proof's two cases.)

### Final answer

$$ \boxed{f(x) = x+c \text{ for all } x>0, \text{ where } c \text{ is an arbitrary constant } c\ge 0} $$

is exactly the set of functions `f:\mathbb R_{>0}\to\mathbb R_{>0}` satisfying
`\sqrt{(x^2+f(y)^2)/2}\ge(f(x)+y)/2\ge\sqrt{xf(y)}` for all `x,y>0`. Necessity is Part 1 (Steps
1–9); sufficiency, verified directly by substitution into the original (un-squared) inequality,
is Part 2. `\blacksquare`

## Promotable lemmas

- **Exact FE**: `f(f(y)) = 2f(y)-y` for all `y>0` (Step 1). Proved by substituting `x=f(y)` into
  the hypothesis, collapsing both bounds to `f(y)` exactly.
- **Injectivity**: `f(a)=f(b)\implies a=b` (Step 2), immediate from the FE.
- **`g(y):=f(y)-y \ge 0`, orbit-invariance `g(f(y))=g(y)`, exact AP orbit `f^n(y)=y+n\,g(y)`**
  (Step 3). Proved from the FE alone plus positivity of `f`.
- **Tool (A)/(B)**: `(x-y)^2 \ge 4f(y)(g(x)-g(y))` and `(x-y)^2\ge4f(x)(g(y)-g(x))`, valid for
  *all* `x,y>0` (Step 4). Derived by applying the RIGHT/GM inequality at `(f(y),x)` and
  eliminating `f(f(y))` via the FE; the second follows by relabeling `x\leftrightarrow y`.
- **Continuity of `g` (hence `f`) from Tool (A)/(B) alone** (Step 5): a genuinely new,
  general-purpose technique — an algebraic "quadratic-Lipschitz" consequence of a functional
  inequality forces continuity of the derived function `g`, without ever assuming continuity of
  `f` a priori. Reusable in other FE-with-inequality problems.
- **`f` strictly increasing** (Step 6): from continuity + injectivity (classical IVT-based
  monotonicity theorem) + `f(y)\ge y$ ruling out "decreasing."
  - **`g` non-decreasing (Step 7)** and the **Crossing Lemma** (Step 8: `a<b`, `g(a),g(b)>0`
  `\implies g(a)=g(b)`, via a minimal-index escaping-orbit argument) and the **zero-set dichotomy**
  (Step 9: the zero set of `g` is either empty or all of `\mathbb R_{>0}`, using downward
  closedness + continuity at the boundary `s=\sup Z`) together give global constancy of `g`.
  This full Steps 5–9 chain is the reusable "promote local/orbit constancy to global constancy"
  mechanism for this problem.
