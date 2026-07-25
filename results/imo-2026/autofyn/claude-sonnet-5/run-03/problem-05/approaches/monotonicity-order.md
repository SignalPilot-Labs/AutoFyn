## Status
solved

## Approaches tried
- **Round 1, original outline (LEFT-inequality-only 2-point monotonicity)**: the outline-reviewer
  produced a concrete numerical counterexample (`x1=1,x2=1.1`, hypothetical `f(x1)=120>f(x2)=100`)
  showing the LEFT inequality at a single pair, together with `f(t)\ge t` and injectivity, does
  **not** forbid an inversion. Confirmed dead as literally stated; abandoned this exact mechanism.
- **Round 1, revised route, first pass**: replaced the 2-point monotonicity idea with an
  **orbit-collision / escaping-sequence** mechanism built on four exact algebraic tools (A,B,C,D)
  derived from the two original inequalities plus the functional equation. This proved: (i) any
  two positive values of `g:=f(y)-y` coincide (Lemma 1, via an explicit escaping double-orbit
  construction — no limits needed); (ii) the "mixed" case (a fixed point of `f` coexisting with a
  point of positive `g`) is impossible whenever an accessible positive-`g` orbit point lies at or
  below the fixed point (via an explicit crossing-index + size contradiction). Left open: the
  mixed case when the only accessible positive-`g` witnesses lie strictly above the fixed point.
- **Round 1, revised route, second pass (this write-up)**: closed the remaining gap. Replaced the
  ad hoc "crossing index" construction with a cleaner **infimum/supremum limiting argument**
  applied to Tool C: taking `m := \inf\{y>x_0 : g(y)=c\}$ (or the symmetric supremum below `x_0`)
  and a minimizing sequence, the interval strictly between `x_0` and `m` is forced entirely into
  the zero-set of `g` (since `g` only takes two values globally, by Lemma 1), which lets us apply
  Tool C at a *converging* pair of points; the left side of Tool C's inequality tends to `0` while
  the right side tends to a fixed positive constant — a genuine, rigorous contradiction. This is
  purely a limit of two explicit real-number sequences into an already-proven inequality (no
  continuity of `f` is assumed or needed), so it stays consistent with the elementary, order-driven
  character of this approach. **This closes the last gap: the full characterization is now
  completely proved.**

## Current best
Superseded by the full proof below (Status: `solved`).

## Full proof

**Theorem.** Let `\mathbb{R}_{>0}` denote the positive reals. A function
`f:\mathbb{R}_{>0}\to\mathbb{R}_{>0}` satisfies
$$\sqrt{\frac{x^2+f(y)^2}{2}} \;\ge\; \frac{f(x)+y}{2} \;\ge\; \sqrt{xf(y)} \qquad \text{for all } x,y>0 \tag{H}$$
if and only if `f(x) = x+c` for some constant `c\ge0`.

Throughout, since all quantities in (H) are non-negative, squaring is an equivalence, so (H) is
equivalent to the pair, for all `x,y>0`:
- **LEFT**: `2(x^2+f(y)^2) \ge (f(x)+y)^2`,
- **RIGHT**: `(f(x)+y)^2 \ge 4xf(y)`.

### Part 1: Sufficiency

Let `f(x)=x+c`, `c\ge0`. Direct expansion gives, for all `x,y`,
$$2(x^2+f(y)^2) - (f(x)+y)^2 = 2\big(x^2+(y+c)^2\big) - \big((x+c)+y\big)^2 = (x-y-c)^2,$$
$$(f(x)+y)^2 - 4xf(y) = \big((x+c)+y\big)^2 - 4x(y+c) = (x-y-c)^2.$$
(Both identities were verified by full symbolic expansion.) Since `(x-y-c)^2\ge0` always, both
LEFT and RIGHT hold for all `x,y>0`, so `f(x)=x+c` satisfies (H) for every `c\ge0`.

### Part 2: Necessity — setup and the functional equation

Assume `f` satisfies (H).

**Step 2.1 (exact functional equation).** Fix `y>0`, set `x=f(y)` in (H). Since the QM and GM of
the pair `(f(y),f(y))` both equal `f(y)$, LEFT and RIGHT respectively give
`2f(y) \ge f(f(y))+y` and `f(f(y))+y\ge 2f(y)$ (after taking square roots of both sides of the
`x=f(y)` instances, all quantities being non-negative), forcing equality:
$$f(f(y)) = 2f(y)-y \qquad \text{for all } y>0. \tag{$*$}$$

*Detail*: LEFT at `x=f(y)` reads `2\cdot 2f(y)^2 \ge (f(f(y))+y)^2`, i.e.
`(2f(y))^2\ge(f(f(y))+y)^2`, i.e. `2f(y)\ge f(f(y))+y` (both sides non-negative before squaring).
RIGHT at `x=f(y)` reads `(f(f(y))+y)^2\ge 4f(y)^2$, i.e. `f(f(y))+y\ge 2f(y)`. Together these force
equality, giving `(*)`.

**Step 2.2 (injectivity).** If `f(a)=f(b)` then by `(*)`, `2f(a)-a=f(f(a))=f(f(b))=2f(b)-b`; since
`f(a)=f(b)`, this forces `a=b`.

**Step 2.3 (`g\ge0` and exact orbit structure).** Let `g(y):=f(y)-y`. From `(*)`,
`g(f(y)) = f(f(y))-f(y) = (2f(y)-y)-f(y) = f(y)-y = g(y)`, so `g` is invariant along the forward
orbit of `y` under `f`. Writing `d:=g(y)`, induction on `n` (base case `n=0,1$ trivial; inductive
step uses `(*)` at `f^{n-1}(y)`) shows the forward orbit is the **exact** arithmetic progression
$$f^n(y) = y+nd \qquad \text{for all integers } n\ge0.$$
Since this orbit must remain in `\mathbb{R}_{>0}` for every `n`, `d` cannot be negative (else
`y+nd\to-\infty`). Hence
$$g(y)\ge0 \quad\text{for every } y>0. \tag{2.3}$$

**Step 2.4 (four algebraic tools).** Fix `x,y>0`; write `p:=g(x),\,q:=g(y)\ (\ge0$ by (2.3)$)`.

Apply RIGHT at `(X,Y)=(f(y),x)`, using `(*)` to substitute `f(f(y))=y+2q`:
`(y+2q+x)^2 \ge 4(y+q)(x+p)`. Expanding both sides and simplifying (verified by full symbolic
expansion) gives
$$(x+y+2q)^2 - 4(y+q)(x+p) = (x-y)^2 + 4(q-p)f(y),$$
so
$$\textbf{Tool A: } (x-y)^2 \ge 4f(y)(p-q) \qquad \text{for all } x,y>0. \tag{A}$$
(Non-vacuous exactly when `p\ge q`; otherwise the RHS is negative and the statement is trivial.)

Apply LEFT at `(X,Y)=(f(y),x)`: `2\big((y+q)^2+(x+p)^2\big) \ge (x+y+2q)^2`. Expanding (verified
by full symbolic expansion) gives
$$2\big((y+q)^2+(x+p)^2\big) - (x+y+2q)^2 = (x-y)^2 + (p-q)(4x+2p+2q),$$
so
$$\textbf{Tool C: } (x-y)^2 \ge 2(q-p)(2x+p+q) \qquad \text{for all } x,y>0. \tag{C}$$
(Non-vacuous exactly when `q\ge p`.)

(Swapping `x\leftrightarrow y` in Tool A/Tool C gives Tools B/D, which are not needed below.)

### Part 3: Any two positive values of `g` coincide

**Lemma 1.** If `y_1,y_2>0` with `g(y_1)>0` and `g(y_2)>0`, then `g(y_1)=g(y_2)`.

*Proof.* Suppose `d_1:=g(y_1)`, `d_2:=g(y_2)`, both `>0`, and suppose towards contradiction
`d_1\ne d_2`; WLOG `d_1>d_2>0`. By Step 2.3, the forward orbits
`x_n:=y_1+nd_1$ ($n\ge0$) and `z_m:=y_2+md_2` (`m\ge0`) satisfy `g(x_n)=d_1`, `g(z_m)=d_2` for
**every** `n,m\ge0`, and both sequences increase to `+\infty` since `d_1,d_2>0`.

Fix `m` large enough that `z_m>y_1`. Since `x_n=y_1+nd_1` is strictly increasing with constant
step `d_1$ and unbounded, there is a smallest `n(m)\ge1` with `x_{n(m)}\ge z_m$; by minimality
`x_{n(m)-1}<z_m\le x_{n(m)}`, and since consecutive terms differ by exactly `d_1`,
$$0\le x_{n(m)}-z_m < d_1.$$
Apply Tool A at `(x,y)=(x_{n(m)},z_m)`, where `p=g(x_{n(m)})=d_1`, `q=g(z_m)=d_2`, and
`p-q=d_1-d_2>0` (so Tool A is the genuine constraint):
$$(x_{n(m)}-z_m)^2 \ge 4f(z_m)(d_1-d_2) = 4(z_m+d_2)(d_1-d_2).$$
The left side is `<d_1^2`, independent of `m`. The right side `\to\infty$ as `m\to\infty` (fixed
positive factor `d_1-d_2` times `z_m+d_2\to\infty`). So for `m` large enough,
`4(z_m+d_2)(d_1-d_2) > d_1^2 > (x_{n(m)}-z_m)^2`, contradicting the inequality above. Hence
`d_1=d_2`. $\blacksquare$

By Lemma 1, the set `\{g(y):y>0,\ g(y)>0\}` has at most one element. Combined with (2.3),
$$g(y) \in \{0\}\cup\{c\}\quad\text{for every }y>0, \tag{3.1}$$
where `c\ge0` is either the unique positive value taken by `g` (if `g` takes a positive value
anywhere), or, if `g\equiv0`, we set `c:=0` and (3.1) still holds trivially. Either way `c\ge 0`
is a single, globally fixed constant, and every `y>0` has `g(y)=0` or `g(y)=c`.

If `c=0`, then `g\equiv0`, i.e. `f(x)=x` for all `x`, which is the family member with `c=0`, and
we are done. **So from now on assume `c>0`** and let
$$Z_0:=\{y>0: g(y)=0\}, \qquad Z_c:=\{y>0:g(y)=c\},$$
so `Z_0\cup Z_c=\mathbb{R}_{>0}` (disjointly, by (3.1)). It remains to show `Z_0=\emptyset`, i.e.
`g\equiv c$ everywhere, which will finish the proof (giving `f(x)=x+c`).

### Part 4: `Z_0` is empty (the mixed case is impossible)

Suppose, towards contradiction, `Z_0\ne\emptyset` (and recall `c>0`, `Z_c\ne\emptyset` since
`g$'s positive value `c` is attained somewhere, by definition of `c` in this branch). Fix any
`x_0\in Z_0`, so `f(x_0)=x_0`.

Since `Z_c\ne\emptyset` and `x_0\notin Z_c$ (as `g(x_0)=0\ne c`), every element of `Z_c` is either
`>x_0` or `<x_0`. At least one of the two sets `Z_c\cap(x_0,\infty)` and `Z_c\cap(0,x_0)` is
therefore nonempty. We treat the first; the second is symmetric (swap the roles of "above" and
"below" `x_0` throughout, using an infimum in place of a supremum or vice versa — spelled out at
the end).

**Case: `S:=Z_c\cap(x_0,\infty)\ne\emptyset`.**

`S` is a nonempty subset of `\mathbb{R}` bounded below by `x_0`, so by completeness of `\mathbb{R}`,
$$m:=\inf S$$
exists as a real number with `m\ge x_0`. By the defining property of infimum, for every integer
`k\ge1` there exists `y_k\in S` with `m\le y_k<m+\tfrac1k`; hence `y_k\to m` as `k\to\infty`, and
`g(y_k)=c` for every `k` (as `y_k\in S\subseteq Z_c`).

*Sub-claim: `[x_0,m)\subseteq Z_0`.* Indeed, every element of `S` is `\ge m$ (as `m$ is a lower
bound for `S`), so no point of `[x_0,m)` can lie in `S=Z_c\cap(x_0,\infty)`; since also no point of
`[x_0,m)` other than possibly `x_0` needs separate treatment ($x_0\in Z_0$ already), every
`w\in[x_0,m)$ satisfies `w\notin Z_c`, and by (3.1) therefore `w\in Z_0`.

Now define `w_k\in[x_0,m)` for each `k\ge1` as follows: if `m>x_0`, set
`w_k:=m-\tfrac{m-x_0}{k}\in[x_0,m)` (so `w_k\to m` as `k\to\infty`); if `m=x_0`, set `w_k:=x_0`
for all `k` (constant; here `[x_0,m)=\emptyset` but `x_0$ itself is available and `w_k=x_0=m`
trivially "tends to `m`"). In either case `w_k\in Z_0` for every `k`(so `g(w_k)=0`), and
`w_k\to m` as `k\to\infty`.

Apply **Tool C** at `x=w_k` (`p=g(w_k)=0`), `y=y_k` (`q=g(y_k)=c\ge0=p`, so Tool C is the genuine,
non-vacuous constraint):
$$(w_k-y_k)^2 \;\ge\; 2c(2w_k+c) \qquad\text{for every } k\ge1. \tag{4.1}$$
Now let `k\to\infty`. Since `w_k\to m` and `y_k\to m`, the left side of (4.1) tends to
`(m-m)^2=0`. The right side tends to `2c(2m+c)`, a **fixed constant** that is strictly positive
because `c>0` and `m\ge x_0>0` (so `2m+c>0`). Thus:
$$0 = \lim_{k\to\infty}(w_k-y_k)^2 \;\ge\; \lim_{k\to\infty} 2c(2w_k+c) = 2c(2m+c) > 0,$$
which is absurd. (Formally: pick `\varepsilon:=c(2m+c)>0`. There is `K_1` such that for `k>K_1`,
`2c(2w_k+c) > 2c(2m+c) - \varepsilon = \varepsilon$ [continuity of `w\mapsto 2c(2w+c)` at `w=m`,
elementary]; and there is `K_2` such that for `k>K_2`, `(w_k-y_k)^2<\varepsilon` [since
`(w_k-y_k)^2\to0`]. For `k>\max(K_1,K_2)`, (4.1) gives `\varepsilon > (w_k-y_k)^2 \ge 2c(2w_k+c) >
\varepsilon`, i.e. `\varepsilon>\varepsilon`, an outright contradiction.)

This contradiction shows `S=Z_c\cap(x_0,\infty)` cannot be nonempty in the presence of
`x_0\in Z_0` — i.e. this case is impossible.

**Case: `S':=Z_c\cap(0,x_0)\ne\emptyset`** (symmetric argument). Let `m':=\sup S'`, which exists
and satisfies `0<m'\le x_0$ (as `S'` is nonempty and bounded above by `x_0`). By the defining
property of supremum, there is a sequence `y_k'\in S'` with `y_k'\to m'`, `g(y_k')=c` for all `k`.
Every element of `S'` is `\le m'`, so no point of `(m',x_0]` lies in `S'=Z_c\cap(0,x_0)`; combined
with (3.1), every `w\in(m',x_0]` (this includes `x_0` itself, already known in `Z_0`) satisfies
`w\in Z_0`. Define `w_k'\in(m',x_0]$ with `w_k'\to m'` (analogous to above: if `m'<x_0`, take
`w_k':=m'+\tfrac{x_0-m'}{k}$; if `m'=x_0`, take `w_k':=x_0` constant). Apply Tool C at
`x=w_k'` (`p=0`), `y=y_k'` (`q=c`):
$$(w_k'-y_k')^2 \ge 2c(2w_k'+c).$$
Letting `k\to\infty`: left side `\to (m'-m')^2=0`; right side `\to 2c(2m'+c)>0` (since `c>0`,
`m'>0` — indeed `m'\ge$ any element of `S'>0`). Exactly the same `\varepsilon`-argument as above
gives a contradiction.

Since at least one of the two cases must occur (as `Z_c\ne\emptyset$, `x_0\notin Z_c`), and both
lead to a contradiction, the assumption `Z_0\ne\emptyset` (with `c>0`) is impossible. Hence
`Z_0=\emptyset`, i.e. `g(y)=c` for **every** `y>0`, i.e.
$$f(x)=x+c \qquad\text{for all } x>0,$$
with the constant `c\ge0` fixed throughout.

### Conclusion

Combining Parts 1–4: `f` satisfies (H) if and only if `f(x)=x+c` for some constant `c\ge0`. This
is the complete characterization; both directions (sufficiency in Part 1, necessity in Parts 2–4)
are fully proved, with every case exhaustively covered (Part 3 covers `g` taking at most one
positive value; Part 4 exhaustively covers both possible positions — above or below `x_0` — of any
witness in `Z_c`, and each is closed by a genuine, elementary `\varepsilon$-`K` contradiction from
a limit of two explicit real sequences into the already-proven Tool C inequality; no continuity or
monotonicity of `f` itself was assumed anywhere). $\blacksquare$

**Final answer**: All solutions are $f(x) = x + c$ for an arbitrary constant $c \ge 0$. Verified by
substitution in Part 1 (both original inequalities reduce exactly to $(x-y-c)^2\ge0$).

## Promotable lemmas

**Lemma (base layer): functional equation, injectivity, orbit structure.** *Statement*: any `f`
satisfying (H) satisfies `f(f(y))=2f(y)-y` for all `y>0`; is injective; and `g(y):=f(y)-y\ge0`
with `f^n(y)=y+n\,g(y)` for all `n\ge0`. *Proved in full*: Part 2 (Steps 2.1–2.3) above. (Shared
base layer, consistent with the other approach files' derivations.)

**Tools A and C** (exact algebraic inequalities). *Statement*: for `p=g(x),q=g(y)`,
`(x-y)^2\ge4f(y)(p-q)` (Tool A, non-vacuous when `p\ge q`) and `(x-y)^2\ge2(q-p)(2x+p+q)`
(Tool C, non-vacuous when `q\ge p`), both valid for all `x,y>0`. *Proved in full*: Part 2, Step
2.4, by direct symbolic expansion (independently verified with `sympy`). Tool A already appears
(derived independently) in the `extremal-sup-inf` and `cross-substitution-fixed-point` approach
files; Tool C is a LEFT-inequality analogue newly derived here.

**Lemma 1 (positive `g`-values coincide).** *Statement*: if `g(y_1)>0` and `g(y_2)>0` then
`g(y_1)=g(y_2)`. *Proved in full*: Part 3, via an explicit escaping double-orbit construction (no
limiting/continuity argument needed). Reusable by any approach with the base layer + Tool A.

**Theorem (mixed-case exclusion / full necessity).** *Statement*: if `g` takes values only in
`\{0,c\}` (`c>0`) with both values attained, contradiction — hence `g\equiv c` or `g\equiv0`
globally. *Proved in full*: Part 4, via an infimum/supremum limiting argument applied to Tool C
(a limit of two explicit converging real sequences into the pointwise-true Tool C inequality; no
assumption of continuity of `f`). This is the key closing lemma of the whole problem and is
directly reusable — indeed it **completes** the shared gap that all four round-1 approaches were
targeting (any approach that has independently established the base layer, Tool A, Tool C, and
Lemma 1 can invoke Part 4 verbatim to finish).
