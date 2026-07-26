# imo-2026-05 — IMO 2026 P5

## Status
solved

## Approaches tried
- `orbit-close-encounter` — **worked** (APPROVE, round 1). Algebraic/orbit-AP framing: rewrite inequalities in `g = f − id` form to get two-point constraint `(star)`; combine with orbit-AP invariance `g∘f = g` to force (A) `g` takes at most one positive value (close-encounter lemma: Kronecker for irrational ratio, Bézout for rational; `(star)` at close encounter gives uniform bound `x ≤ 9c_a²/(16(c_b−c_a))`, contradicting `x → ∞`), and (B) a fixed point forces `g ≡ 0` (maximal-connected-component argument: zero-region radius `2√(cs)` around each fixed point; boundary-push drives `α → 0, β → ∞`). Existence via AM-GM + QM-AM on `(x, f(y))`. Complete rigorous proof. Two minor cosmetic errors (Step 0 QM²−AM² gap formula off by factor 2; Step 2 "(star star) trivially true" glib justification) — neither load-bearing.
- `gm-lipschitz-partition` — **solved** (APPROVE, round 2 re-review). Fact 5 `|g(z)−g(y)| ≤ (√f(z)−√f(y))²` is a genuine new instrument (correctly proven, Step 3). Part (A) via Fact 5 + close-encounter: Fact 5 at a `c_a/2`-close encounter of two positive-value orbits forces `δ = c_b − c_a ≤ (ε+δ)²/(4 t_k) → 0`, contradiction. Part (B): the round-1 rightward-only cover-iteration gap is **closed** by replacing it with the maximal-connected-component boundary-push argument (same `(†)` zero-region radius `2√(cs)`): `S = {g=0}` is open; the component `I = (α,β)` containing `x_0` has `β = ∞` (else `s → β⁻` gives `s + 2√(cs) → β + 2√(cβ) > β`) and `α = 0` (else `s → α⁺` gives `s − 2√(cs) → α − 2√(cα) < α`), hence `g ≡ 0`. No uncovered interval; no hand-waving at limits. Existence via AM-GM + QM-AM. Final answer `f(x) = x + c, c ≥ 0`, both directions proven. Builder's Status header underclaimed `partial`; true Status `solved`.
- `asymptotic-vanishing-coefficient` — not built (RETHINK by outline-reviewer: the `(x−y−c)²` leading term swallows the `h`-perturbation; wrong technique).

## Current best
Complete rigorous proof (from `orbit-close-encounter`). The answer is `f(x) = x + c` for any constant `c ≥ 0`.

## Full proof

**Notation.** Write `g(x) := f(x) − x`, so `f(x) = x + g(x)`. Throughout, `ℝ₊ = (0, ∞)`.

We must determine all `f : ℝ₊ → ℝ₊` satisfying

$$\sqrt{\frac{x^{2}+f(y)^{2}}{2}}\;\ge\;\frac{f(x)+y}{2}\;\ge\;\sqrt{x\,f(y)}\qquad(\forall x,y>0).\tag{P}$$

**Claim.** The solutions are exactly `f(x) = x + c` with `c ≥ 0` a constant.

---

### Step 0 — Existence (the family `f(x)=x+c` works)

Let `f(x) = x + c`, `c ≥ 0`. Then `f(y) = y + c`, and the middle term of (P) is

$$\frac{f(x)+y}{2}=\frac{x+c+y}{2}=\frac{x+f(y)}{2}=\operatorname{AM}\bigl(x,\,f(y)\bigr).$$

The right inequality of (P) is `AM(x, f(y)) ≥ GM(x, f(y)) = √(x·f(y))` (**AM-GM**). The left inequality is `QM(x, f(y)) ≥ AM(x, f(y))` (**QM-AM**), since `√((x² + f(y)²)/2) = QM(x, f(y))`. (Both: *Standard inequalities — AM-GM, QM-AM* in `knowledge_base.md`.) The gaps are perfect squares:

$$\operatorname{AM}(x,f(y))^{2}-\operatorname{GM}(x,f(y))^{2}=\frac{(f(y)-x)^{2}}{4}\ge0,\qquad
\operatorname{QM}(x,f(y))^{2}-\operatorname{AM}(x,f(y))^{2}=\frac{(f(y)-x)^{2}}{4}\ge0.$$

Equality in both holds exactly when `x = f(y)`, i.e. `x = y + c`. Positivity `f: ℝ₊ → ℝ₊` requires `c ≥ 0`. Hence every `f(x)=x+c`, `c ≥ 0`, is a solution.

It remains to prove these are the **only** solutions.

---

### Step 1 — Iterate relation, orbit-AP, `g ≥ 0`, injectivity

**Substitute `x = f(y)` into (P).** At this substitution the LHS becomes `√((f(y)²+f(y)²)/2) = f(y)` and the RHS becomes `√(f(y)·f(y)) = f(y)`. The middle `(f(f(y))+y)/2` is sandwiched: `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`, forcing both inequalities to equality. Hence

$$\boxed{\,f(f(y))=2f(y)-y\,}\qquad(\forall y>0).\tag{1}$$

(*Technique — Functional equations: test the special substitution `x = f(y)` that makes both sides collapse to equality;* `knowledge_base.md`.)

**Consequences of (1).**

(i) `g ∘ f = g`. Indeed `g(f(y)) = f(f(y)) − f(y) = (2f(y)−y) − f(y) = f(y) − y = g(y)`.

(ii) **Forward orbits are arithmetic progressions.** By induction on `n ≥ 0`:

$$f^{n}(y)=y+n\,g(y).$$

Base `n=0` trivial. Step: `f^{n+1}(y) = f(f^{n}(y)) = f^{n}(y) + g(f^{n}(y)) = (y + n g(y)) + g(y) = y + (n+1) g(y)`, using (i). (*Technique — Invariants & monovariants: the displacement `g` is invariant under `f`;* `knowledge_base.md`.)

(iii) **`g ≥ 0`**, i.e. `f(x) ≥ x` for all `x > 0`. For if `g(y) < 0`, then `f^{n}(y) = y + n g(y) → −∞`, in particular `f^{n}(y) ≤ 0` for large `n`, contradicting `f : ℝ₊ → ℝ₊` (the forward orbit must stay in `ℝ₊` since `f` is defined on all of `ℝ₊` and maps to `ℝ₊`).

(iv) **`f` is injective.** If `f(a) = f(b)`, apply `f`: `f(f(a)) = f(f(b))`, so by (1) `2f(a) − a = 2f(b) − b`. Since `f(a) = f(b)`, this gives `a = b`.

---

### Step 2 — Two-point constraints in `g`-form

Square the right inequality of (P), `(f(x)+y)/2 ≥ √(x f(y))`:

$$(f(x)+y)^{2}\ge 4x\,f(y).$$

Substitute `f(t) = t + g(t)` and expand:

$$(x+g(x)+y)^{2}=(x+y)^{2}+2(x+y)g(x)+g(x)^{2}.$$

The right is `4x(y+g(y)) = 4xy + 4x g(y)`. Subtracting `4xy`:

$$(x-y)^{2}+2(x+y)g(x)+g(x)^{2}\;\ge\;4x\,g(y).$$

> **(`star`)** `4x·g(y) ≤ (x−y)² + 2(x+y)g(x) + g(x)²` for all `x, y > 0`.

Swapping `x ↔ y` (the statement (P) holds for all `x, y`, so also with roles exchanged) gives the partner constraint

> **(`star star`)** `4y·g(x) ≤ (x−y)² + 2(x+y)g(y) + g(y)²`.

(*Technique — SOS / completing the square;* `knowledge_base.md`.)

**Tautology within a level set.** If `g(x) = g(y) = c`, then the right-hand side of `(star)` minus `4xc` is

$$(x-y)^{2}+2(x+y)c+c^{2}-4xc=(x-y)^{2}-2c(x-y)+c^{2}=(x-y-c)^{2}\ge0,$$

a tautology. So `(star)` and `(star star)` carry no information *within* a single level set `L_c = {x : g(x)=c}`; all of their content is across distinct level sets. For `c_a < c_b`, `x ∈ L_{c_a}`, `y ∈ L_{c_b}`, the binding constraint is `(star)`:

$$4x\,c_{b}\le(x-y)^{2}+2(x+y)c_{a}+c_{a}^{2}.\tag{2}$$

(The swap `(star star)` is also non-negatively satisfied in this orientation: its minimum over `x` is `4y(c_b − c_a) ≥ 0`.) Uniqueness uses only `(star)`.

---

### Step 3 — (A) `g` takes at most one positive value

Suppose, for contradiction, that `g` takes two distinct positive values `c_a < c_b`. Pick `a, b > 0` with `g(a) = c_a`, `g(b) = c_b`. By Step 1(ii) the forward orbits

$$O_{a}=\{a+n c_{a}:n\ge0\},\qquad O_{b}=\{b+m c_{b}:m\ge0\}$$

are unbounded-above arithmetic progressions, and `g ≡ c_a` on `O_a`, `g ≡ c_b` on `O_b` (by Step 1(i)).

> **Close-encounter lemma.** Let `A = {a + np}_{n≥0}`, `B = {b + mq}_{m≥0}` with `p, q > 0`. Then for every `ε > 0` there exist `n, m ≥ 0` with `A_n, B_m` arbitrarily large and `|A_n − B_m| ≤ ε`, **unless** the two APs collide (i.e. `A_n = B_m` for some `n, m`).

*Proof of the lemma.* Split on the ratio `p/q`.

- **`p/q` irrational.** The fractional parts `{n(p/q) + (a−b)/q}` are dense in `[0,1)` by **Kronecker/Weyl equidistribution** (`knowledge_base.md`). Hence for any `ε > 0` there are arbitrarily large `n` with `{np/q + (a−b)/q} ∈ [0, ε/(2q)]`, i.e. `np + (a−b) = mq + r` for some integer `m ≥ 0` (for `n` large) and `|r| ≤ ε/2`. Then `A_n − B_m = (a−b) + np − mq = r`, so `|A_n − B_m| ≤ ε/2 < ε`, and both `A_n, B_m → ∞`.

- **`p/q` rational.** Write `p/q = P/Q` in lowest terms (`P, Q` coprime positive integers) and set `d := p/P = q/Q > 0` (so `p = Pd, q = Qd`). Every term of `A` is congruent to `a mod d`, every term of `B` is congruent to `b mod d`.
  - *Same residue class* (`a ≡ b mod d`): then `(a − b)/d` is an integer `k_0`. Since `gcd(P, Q) = 1`, **Bézout's identity** (`knowledge_base.md`, *Modular arithmetic / Bézout*) gives integers `n_0, m_0` with `n_0 P − m_0 Q = −k_0`, and the general solution is `(n_0 + tQ, m_0 + tP)` for `t ∈ ℤ`; for large `t` both are `≥ 0`. Then `A_{n_0+tQ} = B_{m_0+tP}` (both equal `a + n_0 Pd + tPQd = b + m_0 Qd + tPQd`), so the APs **collide**.
  - *Distinct residue classes* (`a ≢ b mod d`): no collision is possible. The set of differences is `A_n − B_m = (a−b) + d(nP − mQ)`. By Bézout, `{nP − mQ : n, m ≥ 0}` contains every integer (add `tQ` to `n`, `tP` to `m` to the Bézout solution, taking `t → ∞`). The cyclic distance `δ := min_{k∈ℤ} |(a−b)+dk|` satisfies `0 < δ ≤ d/2` (since `a ≢ b mod d`). Pick `k_*` attaining `δ`. The Bézout solutions `(n_0+tQ, m_0+tP)` to `nP − mQ = k_*` give, for `t → ∞`, points `A_n, B_m → ∞` with `|A_n − B_m| = δ ≤ d/2 ≤ p/2` (as `d = p/P ≤ p` since `P ≥ 1`). ∎ (lemma)

Apply the lemma with `p = c_a, q = c_b, ε = c_a/2`. (The hypothesis of the rational sub-case is satisfied: `d = gcd(c_a, c_b) ≤ c_a` since `d | c_a`, so `δ ≤ d/2 ≤ c_a/2 = ε`.) Two outcomes:

- **Collision outcome** (`A_n = B_m`): the common point `x` lies on both `O_a` and `O_b`, so `g(x) = c_a` and `g(x) = c_b`, contradicting `c_a ≠ c_b`. Immediate contradiction.
- **Close-encounter outcome**: there are `n_k, m_k → ∞` with `x_k := A_{n_k}`, `y_k := B_{m_k}` both `→ ∞`, `|x_k − y_k| ≤ c_a/2`, `g(x_k) = c_a`, `g(y_k) = c_b`.

In the second outcome, plug `x = x_k ∈ L_{c_a}`, `y = y_k ∈ L_{c_b}` into `(star)` (the binding orientation (2); the smaller step `c_a` is in the `g(x)` slot, the larger `c_b` in the `g(y)` slot):

$$4 x_k\, c_b \;\le\; (x_k - y_k)^2 + 2(x_k + y_k) c_a + c_a^2.$$

Bound the right uniformly using `|x_k − y_k| ≤ c_a/2` (so `(x_k − y_k)² ≤ c_a²/4`) and `y_k ≤ x_k + c_a/2` (so `x_k + y_k ≤ 2x_k + c_a/2`, hence `2(x_k + y_k) c_a ≤ 4x_k c_a + c_a²`):

$$4 x_k c_b \;\le\; \frac{c_a^2}{4} + 4 x_k c_a + c_a^2 + c_a^2 \;=\; 4 x_k c_a + \frac{9}{4} c_a^2.$$

(The last `c_a²` is the `g(x)² = c_a²` term.) Therefore

$$4 x_k (c_b - c_a) \;\le\; \frac{9}{4} c_a^2 \qquad\Longrightarrow\qquad x_k \;\le\; \frac{9\,c_a^{2}}{16\,(c_b - c_a)}.$$

The right-hand side is a fixed finite constant (independent of `k`). But `x_k → ∞` by the close-encounter lemma. **Contradiction.**

Both outcomes of the lemma yield a contradiction, so the assumption that `g` takes two distinct positive values is false. ∎ (Part A)

> **Conclusion of Step 3.** `g` takes **at most one** positive value. Since `g ≥ 0` (Step 1(iii)), either `g ≡ 0`, or `g : ℝ₊ → {0, c}` for a single constant `c > 0` (taking both values `0` and `c`), or `g ≡ c > 0`.

---

### Step 4 — (B) A fixed point forces `g ≡ 0`

Assume a **fixed point** exists: `g(x_0) = 0` for some `x_0 > 0` (i.e. `f(x_0) = x_0`). If `g` takes no positive value, then `g ≡ 0` already (Step 1(iii)), and we are done. So suppose, for contradiction, that `g` also takes a positive value `c > 0`. By Step 3,

$$g:\mathbb R_{>0}\to\{0,c\}.$$

**(dagger) — global quadratic upper bound.** Substitute `x = x_0` (so `g(x_0) = 0`) into `(star)`:

$$4 x_0\, g(y) \;\le\; (x_0 - y)^2 + 2(x_0 + y)\cdot 0 + 0^2 = (y - x_0)^2.$$

> **(`dagger`)** `g(y) ≤ (y − x_0)² / (4 x_0)` for all `y > 0`.

**Zero-region around a fixed point.** Let `s > 0` be any fixed point (`g(s) = 0`). Applying `(dagger)` with `s` in place of `x_0`,

$$g(y)\le\frac{(y-s)^2}{4s}\qquad(\forall y>0).\tag{3}$$

If `|y − s| < 2√(cs)`, then `(y−s)²/(4s) < (4cs)/(4s) = c`, so `g(y) < c`. Since `g(y) ∈ {0, c}`, this forces `g(y) = 0`. Hence

$$\bigl(s - 2\sqrt{cs},\; s + 2\sqrt{cs}\bigr)\cap\mathbb R_{>0}\;\subseteq\;S:=\{y>0:g(y)=0\}.\tag{4}$$

In particular `S` is **open** (every point of `S` is the centre of an open interval inside `S`).

**Maximal connected component.** Let `I = (α, β)` be the connected component of the open set `S` that contains `x_0`. (It is an open interval, nonempty since `x_0 ∈ S`.) We show `α = 0` and `β = ∞`.

- **`β = ∞`.** Suppose `β < ∞`. Since `x_0 ∈ I`, by (4) applied at `s = x_0`, `β ≥ x_0 + 2√(cx_0) > 0`. Pick `s ∈ I` arbitrarily close to `β` from below; then `s ∈ S`, so by (4) the whole interval `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊` lies in `S`. This interval is connected and contains `s ∈ I`, hence is contained in the component `I`. Its right endpoint is `s + 2√(cs)`. As `s → β⁻`, this tends to `β + 2√(cβ) > β` (strictly, since `β > 0` and `c > 0`). So for `s` close enough to `β`, `s + 2√(cs) > β`, placing points of `I` strictly to the right of `β` — contradicting the definition of `β` as the supremum of `I`. Hence `β = ∞`.

- **`α = 0`.** Suppose `α > 0`. Pick `s ∈ I` arbitrarily close to `α` from above; then `s ∈ S`, and by (4) the interval `(s − 2√(cs), s + 2√(cs)) ∩ ℝ₊ ⊆ S` is contained in the component `I`. Its left endpoint `s − 2√(cs)` tends to `α − 2√(cα)` as `s → α⁺`, and `α − 2√(cα) < α` (strictly, since `α > 0` and `c > 0`). So for `s` close enough to `α`, `s − 2√(cs) < α`, placing points of `I` strictly to the left of `α` — contradicting the definition of `α` as the infimum of `I`. Hence `α = 0` (the only option, since `S ⊆ ℝ₊`).

Therefore `I = (0, ∞)`, i.e. `S = ℝ₊`, i.e. `g ≡ 0` on all of `ℝ₊`. This contradicts the assumption that `g` takes the positive value `c > 0`. ∎ (Part B)

> **Conclusion of Step 4.** If a fixed point exists, then `g` cannot take any positive value; combined with `g ≥ 0` (Step 1(iii)) this gives `g ≡ 0`, i.e. `f = id` (the case `c = 0`).

---

### Step 5 — Synthesis (uniqueness)

By Step 3, `g` takes at most one positive value. There are two cases.

- **`g` takes no positive value.** Then `g ≥ 0` (Step 1(iii)) forces `g ≡ 0`, so `f(x) = x` (i.e. `c = 0`).
- **`g` takes exactly one positive value `c > 0`.** Then `g : ℝ₊ → {0, c}`.
  - If a fixed point existed, Step 4 would force `g ≡ 0`, contradicting `c > 0`. Hence **no fixed point exists**: `g(x) ≠ 0` for all `x > 0`. Since `g(x) ∈ {0, c}`, this gives `g(x) = c` for all `x > 0`, i.e. `g ≡ c`, and `f(x) = x + c`.

In both cases `f(x) = x + c` for a constant `c ≥ 0`. Together with the existence verification of Step 0, these are exactly the solutions. ∎

---

**Final answer.** The functions `f : ℝ₊ → ℝ₊` satisfying (P) are precisely

$$\boxed{\,f(x)=x+c\quad\text{for an arbitrary constant }c\ge0.\,}$$
