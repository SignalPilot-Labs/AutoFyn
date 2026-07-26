# orbit-close-encounter

## Status
solved

## Approaches tried
- (round 1) Regularity route: rewrite both inequalities in `g = f - id` form to get two asymmetric two-point constraints `(star), (star star)`; combine with orbit-AP invariance `g circ f = g` to force (A) `g` takes at most one positive value, and (B) a fixed point forces `g equiv 0`. Purely algebraic, handles wild (non-measurable) `g`. Three sub-gaps flagged: the close-encounter number-theory lemma, the `3 + 2 sqrt 2` straddle algebra, and the interval-cover iteration.
- (round 2) Built the full proof. Closed G-A1 (close-encounter lemma: Kronecker for irrational ratio, Bezout + Frobenius for rational ratio, with `d = c_a / P <= c_a` giving the `c_a/2` bound; the same-residue sub-case is an immediate collision, hence a direct contradiction). Closed G-A2 (orientation: smaller step in the `g(x)` slot, larger in `g(y)`). Replaced the invalid `3+2sqrt2` lower bound (outline-reviewer flagged the `a <= c` surjectivity assumption) by a **maximal-connected-component** argument for Part (B): the zero-region radius `2 sqrt(c s)` around any fixed point `s`, together with `g : R_{>0} -> {0, c}` from Part (A), makes the fixed-point component containing `x_0` both open and (by the boundary-push at `alpha > 0` and `beta < infty`) have `alpha = 0, beta = infty`, hence `g equiv 0`. No iteration / growth-rate analysis needed. Existence via AM-GM + QM-AM on the pair `(x, f(y))`. Full proof below.

## Current best
Complete rigorous proof. The answer is `f(x) = x + c` for any constant `c >= 0`.

## Full proof

**Notation.** Write `g(x) := f(x) - x`, so `f(x) = x + g(x)`. Throughout, `R_{>0} = (0, infty)`.

We must determine all `f : R_{>0} -> R_{>0}` satisfying

$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}\qquad(\forall x,y>0).\tag{P}$$

**Claim.** The solutions are exactly `f(x) = x + c` with `c >= 0` a constant.

---

### Step 0 — Existence (the family `f(x)=x+c` works)

Let `f(x) = x + c`, `c >= 0`. Then `f(y) = y + c`, and the middle term of (P) is

$$\frac{f(x)+y}{2}=\frac{x+c+y}{2}=\frac{x+f(y)}{2}=\operatorname{AM}\bigl(x,\,f(y)\bigr).$$

The right inequality of (P) is `operatorname{AM}(x,f(y)) >= operatorname{GM}(x,f(y)) = sqrt(x f(y))`, which is **AM-GM** on the pair `(x, f(y))`. The left inequality of (P) is `operatorname{QM}(x,f(y)) >= operatorname{AM}(x,f(y))`, which is **QM-AM** on the same pair, since `sqrt((x^2 + f(y)^2)/2) = operatorname{QM}(x,f(y))`. (Both are entries of *Standard inequalities — AM-GM, QM-AM* in `knowledge_base.md`.) Indeed the gaps are perfect squares:

$$\operatorname{QM}(x,f(y))^{2}-\operatorname{AM}(x,f(y))^{2}=\frac{(f(y)-x)^{2}}{4}\ge0,\qquad
\operatorname{AM}(x,f(y))^{2}-\operatorname{GM}(x,f(y))^{2}=\frac{(f(y)-x)^{2}}{4}\ge0.$$

(For the first: $\operatorname{QM}^{2}-\operatorname{AM}^{2}=\frac{x^{2}+f(y)^{2}}{2}-\frac{(x+f(y))^{2}}{4}=\frac{2x^{2}+2f(y)^{2}-(x^{2}+2xf(y)+f(y)^{2})}{4}=\frac{(x-f(y))^{2}}{4}$; the second is the within-pair identity $\operatorname{AM}^{2}-\operatorname{GM}^{2}=\frac{(x-f(y))^{2}}{4}$.)

Equality in both holds exactly when `x = f(y)`, i.e. `x = y + c`. Hence every `f(x)=x+c`, `c >= 0`, is a solution.

It remains to prove these are the **only** solutions.

---

### Step 1 — Iterate relation, orbit-AP, `g >= 0`, injectivity

**Substitute `x = f(y)` into (P).** The right inequality of (P) gives

$$\frac{f(f(y))+y}{2}\ge\sqrt{f(y)\cdot f(y)}=f(y)\quad\Longrightarrow\quad f(f(y))\ge 2f(y)-y,\tag{1a}$$

and the left inequality of (P) gives (the LHS becomes `sqrt((f(y)^2+f(y)^2)/2) = f(y)`)

$$f(y)\ge\frac{f(f(y))+y}{2}\quad\Longrightarrow\quad f(f(y))\le 2f(y)-y.\tag{1b}$$

Combining (1a) and (1b):

$$\boxed{\,f(f(y))=2f(y)-y\,}\qquad(\forall y>0).\tag{1}$$

(*Technique — Functional equations: test the special substitution `x = f(y)` that makes both sides of (P) collapse to equality;* `knowledge_base.md`.)

**Consequences of (1).**

(i) `g circ f = g`. Indeed `g(f(y)) = f(f(y)) - f(y) = (2f(y)-y) - f(y) = f(y) - y = g(y)`.

(ii) **Forward orbits are arithmetic progressions.** By induction on `n >= 0`,

$$f^{n}(y)=y+n\,g(y).$$

Base `n=0` is trivial. Step: `f^{n+1}(y) = f(f^{n}(y)) = f^{n}(y) + g(f^{n}(y)) = (y + n g(y)) + g(y) = y + (n+1) g(y)`, using (i). (*Technique — Invariants & monovariants: the displacement `g` is invariant under `f`;* `knowledge_base.md`.)

(iii) **`g >= 0`**, i.e. `f(x) >= x` for all `x > 0`. For if `g(y) < 0`, then `f^{n}(y) = y + n g(y) -> -infty` as `n -> infty`, in particular `f^{n}(y) <= 0` for large `n`, contradicting `f : R_{>0} -> R_{>0}`.

(iv) **`f` is injective.** If `f(a) = f(b)`, apply `f`: `f(f(a)) = f(f(b))`, so by (1) `2f(a) - a = 2f(b) - b`. Since `f(a) = f(b)`, this gives `a = b`.

---

### Step 2 — Two-point constraints in `g`-form

Square the right inequality of (P), `(f(x)+y)/2 >= sqrt(x f(y))`:

$$(f(x)+y)^{2}\ge 4x\,f(y).$$

Substitute `f(t) = t + g(t)` and expand the left:

$$(x+g(x)+y)^{2}=(x+y)^{2}+2(x+y)g(x)+g(x)^{2}.$$

The right is `4x(y+g(y)) = 4xy + 4x g(y)`. Subtracting `4xy` from both sides,

$$(x-y)^{2}+2(x+y)g(x)+g(x)^{2}\;\ge\;4x\,g(y).$$

> **(`star`)** `quad` `4x,g(y) <= (x-y)^2 + 2(x+y)g(x) + g(x)^2` for all `x, y > 0`.

Swapping `x <-> y` (the statement (P) is symmetric in the quantifiers) gives the partner constraint

> **(`star star`)** `quad` `4y,g(x) <= (x-y)^2 + 2(x+y)g(y) + g(y)^2`.

(*Technique — SOS / completing the square:* `(f(x)+y)^2 - 4xf(y)` is a quadratic form in the deviations;* `knowledge_base.md`.)

**Tautology within a level set.** If `g(x) = g(y) = c`, then the right-hand side of `(`star`)` minus `4xc` is

$$(x-y)^{2}+2(x+y)c+c^{2}-4xc=(x-y)^{2}-2c(x-y)+c^{2}=(x-y-c)^{2}\ge0,$$

a tautology. So `(`star`)` and `(`star star`)` carry no information *within* a single level set `L_c = {x : g(x)=c}`; all of their content is across distinct level sets. For `c_a < c_b`, `x in L_{c_a}`, `y in L_{c_b}`, the binding constraint is `(`star`)`:

$$4x\,c_{b}\le(x-y)^{2}+2(x+y)c_{a}+c_{a}^{2}.\tag{2}$$

(The swap `(`star star`)` with `g(x)=c_a, g(y)=c_b` reads `4y c_a <= (x-y)^2 + 2(x+y)c_b + c_b^2`. Since `c_a < c_b` and `y > 0`, `4y c_a < 4y c_b`; and `(x-y)^2 + 2(x+y)c_b + c_b^2 - 4y c_b = (x-y)^2 + 2c_b(x-y) + c_b^2 = (x - y + c_b)^2 >= 0`, the within-`c_b`-level-set tautology. Hence `4y c_b <=` RHS, so `4y c_a <=` RHS: `(`star star`)` is automatic in this orientation.) We will not need the left (RMS) inequality of (P) again beyond Step 1: uniqueness uses only `(`star`)`.

---

### Step 3 — (A) `g` takes at most one positive value

Suppose, for contradiction, that `g` takes two distinct positive values `c_a < c_b`. Pick `a, b > 0` with `g(a) = c_a`, `g(b) = c_b`. By Step 1(ii) the forward orbits

$$O_{a}=\{a+n c_{a}:n\ge0\},\qquad O_{b}=\{b+m c_{b}:m\ge0\}$$

are unbounded-above arithmetic progressions, and `g equiv c_a` on `O_a`, `g equiv c_b` on `O_b` (by Step 1(i)).

We need a close encounter of these two APs.

> **Close-encounter lemma.** Let `A = {a + np}_{n>=0}`, `B = {b + mq}_{m>=0}` with `p, q > 0`. Then for every `epsilon > 0` there exist `n, m >= 0` with `A_n, B_m` arbitrarily large and `|A_n - B_m| <= epsilon`, **unless** the two APs collide (i.e. `A_n = B_m` for some `n, m`).

*Proof of the lemma.* Split on the ratio `p/q`.

- **`p/q` irrational.** The fractional parts `{n(p/q) + (a-b)/q}` are dense in `[0,1)` by **Kronecker/Weyl equidistribution** (`knowledge_base.md`). Hence for any `epsilon > 0` there are arbitrarily large `n` with `{n p/q + (a-b)/q} in [0, epsilon/(2q)]`, i.e. `n p + (a-b) = m q + r` for some integer `m` and `|r| <= epsilon/2`. Then `A_n - B_m = (a + np) - (b + mq) = (a - b) + np - mq = r`, so `|A_n - B_m| <= epsilon/2 < epsilon`, and both `A_n = a + np -> infty`, `B_m = b + mq -> infty`.

- **`p/q` rational.** Write `p/q = P/Q` in lowest terms (`P, Q` coprime positive integers) and set `d := p/P = q/Q > 0` (so `p = Pd, q = Qd`). Every term of `A` is congruent to `a mod d`, every term of `B` is congruent to `b mod d`.
  - *Same residue class* (`a -= b mod d`): then `(a - b)/d` is an integer `k_0`. Since `gcd(P, Q) = 1`, **Bezout's identity** gives integers `n_0, m_0` with `n_0 P - m_0 Q = k_0`, and the general solution is `(n_0 + tQ, m_0 + tP)` for `t in Z`; for large `t` both are `>= 0`. Then `A_{n_0+tQ} = a + (n_0+tQ) P d = a + n_0 P d + t P Q d` and `B_{m_0+tP} = b + m_0 Q d + t P Q d`, equal since `a - b + (n_0 P - m_0 Q) d = (a-b) + k_0 d = 0`. So the APs **collide**.
  - *Distinct residue classes* (`a !-= b mod d`): no collision is possible (a common point would lie in both classes). The set of differences is `A_n - B_m = (a-b) + d(nP - mQ)`. By Bezout, `{nP - mQ : n, m >= 0}` contains every sufficiently large positive integer and every sufficiently large negative integer (add `tQ` to `n`, `tP` to `m` to the Bezout solution of `nP - mQ = k`, taking `t -> infty`). For any integer `k`, the value `(a - b) + dk` has absolute value `>= delta := min_{k in Z} |(a-b)+dk|`, the cyclic distance from `(a-b)/d` to the nearest integer times `d`; since `a !-= b mod d`, `delta > 0`, and `delta <= d/2`. Pick `k_*` attaining `delta`. The Bezout solutions `(n_0 + tQ, m_0 + tP)` to `nP - mQ = k_*` give, for `t -> infty`, points `A_{n_0+tQ} -> infty`, `B_{m_0+tP} -> infty` with `A_n - B_m = (a-b) + d k_* = +- delta`. So `|A_n - B_m| = delta <= d/2 <= (p/P)/2 <= p/2` (as `P >= 1` and `p = Pd`, hence `d = p/P <= p`). Taking `epsilon = p/2` (here `p = c_a`) gives `|A_n - B_m| <= c_a/2` at arbitrarily large `A_n, B_m`. ∎ (lemma)

Apply the lemma with `p = c_a, q = c_b, epsilon = c_a/2`. Two outcomes:

- **Collision outcome** (`A_n = B_m`): the common point `x` lies on both `O_a` and `O_b`, so `g(x) = c_a` and `g(x) = c_b`, contradicting `c_a != c_b`. Immediate contradiction.
- **Close-encounter outcome**: there are `n_k, m_k -> infty` with `x_k := A_{n_k}`, `y_k := B_{m_k}` both `-> infty`, `|x_k - y_k| <= c_a/2`, `g(x_k) = c_a`, `g(y_k) = c_b`.

In the second outcome, plug `x = x_k in L_{c_a}`, `y = y_k in L_{c_b}` into `(`star`)` (the binding orientation (2); the smaller step `c_a` is in the `g(x)` slot, the larger `c_b` in the `g(y)` slot — verified by (2)):

$$4 x_k\, c_b \;\le\; (x_k - y_k)^2 + 2(x_k + y_k) c_a + c_a^2.$$

Bound the right uniformly using `|x_k - y_k| <= c_a/2` (so `(x_k - y_k)^2 <= c_a^2/4`) and `y_k <= x_k + c_a/2` (so `x_k + y_k <= 2 x_k + c_a/2`, hence `2(x_k + y_k) c_a <= 4 x_k c_a + c_a^2`):

$$4 x_k c_b \;\le\; \frac{c_a^2}{4} + 4 x_k c_a + c_a^2 + c_a^2 \;=\; 4 x_k c_a + \frac{9}{4} c_a^2.$$

(The last `c_a^2` is the `g(x)^2 = c_a^2` term.) Therefore

$$4 x_k (c_b - c_a) \;\le\; \frac{9}{4} c_a^2 \qquad\Longrightarrow\qquad x_k \;\le\; \frac{9\,c_a^{2}}{16\,(c_b - c_a)}.$$

The right-hand side is a fixed finite constant (independent of `k`). But `x_k -> infty` by the close-encounter lemma. **Contradiction.**

Both outcomes of the lemma yield a contradiction, so the assumption that `g` takes two distinct positive values is false. ∎ (Part A)

> **Conclusion of Step 3.** `g` takes **at most one** positive value. Since `g >= 0` (Step 1(iii)), either `g equiv 0`, or `g : R_{>0} -> {0, c}` for a single constant `c > 0` (taking both values `0` and `c`), or `g equiv c > 0`.

---

### Step 4 — (B) A fixed point forces `g equiv 0`

Assume a **fixed point** exists: `g(x_0) = 0` for some `x_0 > 0` (i.e. `f(x_0) = x_0`). If `g` takes no positive value, then `g equiv 0` already (Step 1(iii)), and we are done. So suppose, for contradiction, that `g` also takes a positive value `c > 0`. By Step 3,

$$g:\mathbb R_{>0}\to\{0,c\}.$$

**(dagger) — global quadratic upper bound.** Substitute `x = x_0` (so `g(x_0) = 0`) into `(`star`)`:

$$4 x_0\, g(y) \;\le\; (x_0 - y)^2 + 2(x_0 + y)\cdot 0 + 0^2 = (y - x_0)^2.$$

> **(`dagger`)** `quad` `g(y) <= (y - x_0)^2 / (4 x_0)` for all `y > 0`.

**Zero-region around a fixed point.** Let `s > 0` be any fixed point (`g(s) = 0`). Applying `(`dagger`)` with `s` in place of `x_0`,

$$g(y)\le\frac{(y-s)^2}{4s}\qquad(\forall y>0).\tag{3}$$

If `|y - s| < 2 sqrt(c s)`, then `(y-s)^2/(4s) < (4 c s)/(4s) = c`, so `g(y) < c`. Since `g(y) in {0, c}`, this forces `g(y) = 0`. Hence

$$\bigl(s - 2\sqrt{cs},\; s + 2\sqrt{cs}\bigr)\cap\mathbb R_{>0}\;\subseteq\;S:=\{y>0:g(y)=0\}.\tag{4}$$

In particular `S` is **open** (every point of `S` is the centre of an open interval inside `S`).

**Maximal connected component.** Let `I = (alpha, beta)` be the connected component of the open set `S` that contains `x_0`. (It is an open interval, nonempty since `x_0 in S`.) We show `alpha = 0` and `beta = infty`.

- **`beta = infty`.** Suppose `beta < infty`. Since `beta` is the right endpoint of the component containing `x_0`, and `x_0 in I`, certainly `beta >= x_0 + 2 sqrt(c x_0) > 0` (by (4) applied at `s = x_0`). Pick `s in I` arbitrarily close to `beta` from below; then `s in S`, so by (4) the whole interval `(s - 2 sqrt(c s), s + 2 sqrt(c s))` lies in `S`. This interval is connected and contains `s in I`, hence is contained in the component `I`. Its right endpoint is `s + 2 sqrt(c s)`. As `s -> beta^{-}`, this tends to `beta + 2 sqrt(c beta) > beta` (strictly, since `beta > 0` and `c > 0`). So for `s` close enough to `beta`, `s + 2 sqrt(c s) > beta`, placing points of `I` strictly to the right of `beta` — contradicting the definition of `beta` as the supremum of `I`. Hence `beta = infty`.

- **`alpha = 0`.** Suppose `alpha > 0`. Pick `s in I` arbitrarily close to `alpha` from above; then `s in S`, and by (4) the interval `(s - 2 sqrt(c s), s + 2 sqrt(c s)) subseteq S` is contained in the component `I`. Its left endpoint `s - 2 sqrt(c s)` tends to `alpha - 2 sqrt(c alpha)` as `s -> alpha^{+}`, and `alpha - 2 sqrt(c alpha) < alpha` (strictly, since `alpha > 0` and `c > 0`). So for `s` close enough to `alpha`, `s - 2 sqrt(c s) < alpha`, placing points of `I` strictly to the left of `alpha` — contradicting the definition of `alpha` as the infimum of `I`. Hence `alpha = 0` (the only option, since `S subseteq R_{>0}`).

Therefore `I = (0, infty)`, i.e. `S = R_{>0}`, i.e. `g equiv 0` on all of `R_{>0}`. This contradicts the assumption that `g` takes the positive value `c > 0`. ∎ (Part B)

> **Conclusion of Step 4.** If a fixed point exists, then `g` cannot take any positive value; combined with `g >= 0` (Step 1(iii)) this gives `g equiv 0`, i.e. `f = operatorname{id}` (the case `c = 0`).

---

### Step 5 — Synthesis (uniqueness)

By Step 3, `g` takes at most one positive value. There are two cases.

- **`g` takes no positive value.** Then `g >= 0` (Step 1(iii)) forces `g equiv 0`, so `f(x) = x` (i.e. `c = 0`).
- **`g` takes exactly one positive value `c > 0`.** Then `g : R_{>0} -> {0, c}`.
  - If a fixed point existed, Step 4 would force `g equiv 0`, contradicting `c > 0`. Hence **no fixed point exists**: `g(x) != 0` for all `x > 0`. Since `g(x) in {0, c}`, this gives `g(x) = c` for all `x > 0`, i.e. `g equiv c`, and `f(x) = x + c`.

In both cases `f(x) = x + c` for a constant `c >= 0`. Together with the existence verification of Step 0, these are exactly the solutions. ∎

---

**Final answer.** The functions `f : R_{>0} -> R_{>0}` satisfying (P) are precisely

$$\boxed{\,f(x)=x+c\quad\text{for an arbitrary constant }c\ge0.\,}$$

## Promotable lemmas

1. **`iterate-and-orbit`** (proven in Step 1 above; reviewer-certify pending).
   *Statement.* Let `f : R_{>0} -> R_{>0}` satisfy (P). Set `g(x) := f(x) - x`. Then `f(f(y)) = 2 f(y) - y` for all `y > 0`, equivalently `g(f(y)) = g(y)`; consequently `f^{n}(y) = y + n g(y)` for all `n >= 0` (forward orbits are arithmetic progressions with common difference `g(y)`); `g(y) >= 0` for all `y` (i.e. `f >= operatorname{id}`); and `f` is injective.
   *Where proved:* Step 1 of `results/imo-2026-05/approaches/orbit-close-encounter.md`. This is the shared preamble; the other approaches (`gm-lipschitz-partition`) may import it instead of re-proving.

2. **`two-point-g-constraint`** (proven in Step 2 above; reviewer-certify pending).
   *Statement.* Under the hypotheses of `iterate-and-orbit`, the squared right inequality of (P) is equivalent, for all `x, y > 0`, to `(`star`)`: `4 x g(y) <= (x-y)^2 + 2(x+y) g(x) + g(x)^2`; swapping `x, y` gives `(`star star`)`. Within a level set `g(x) = g(y) = c`, `(`star`)` reduces to the tautology `(x - y - c)^2 >= 0`.
   *Where proved:* Step 2 of the same file.

3. **`fixed-point-zero-region`** (proven in Step 4 above; reviewer-certify pending).
   *Statement.* Under the hypotheses of `iterate-and-orbit`, suppose `g : R_{>0} -> {0, c}` for some `c > 0` (i.e. `g` takes at most one positive value, by the conclusion of Part A). If a fixed point `x_0` (`g(x_0) = 0`) exists, then `(`star`)` at `x = x_0` gives the global bound `(`dagger`)`: `g(y) <= (y - x_0)^2 / (4 x_0)` for all `y > 0`. Consequently every fixed point `s` has an open zero-neighbourhood `(s - 2 sqrt(c s), s + 2 sqrt(c s)) cap R_{>0}` on which `g = 0`. The connected component of the fixed-point set containing `x_0` is then `(0, infty)`, so `g equiv 0`, contradicting `c > 0`. Hence a fixed point and a positive value of `g` cannot coexist.
   *Where proved:* Step 4 of the same file.
