## Status
solved

## Approaches tried
- **Order-rigidity route (this file).** Original plan was: prove `f` nondecreasing (GAP 1),
  deduce `d=f−id` nondecreasing, then kill a threshold by a near-threshold R-violation.
  Outcome of the literal monotonicity-first plan: **BLOCKED, as the outline-reviewer flagged.**
  The sandwich `2√(x f(y))−y ≤ f(x) ≤ √(2x²+2f(y)²)−y` and the "f = sup-envelope" idea both
  require a value `y` with `f(y)` near a prescribed target (surjectivity/denseness of range(f)),
  which is NOT available; `f ≥ increasing sup` does not make `f` increasing. Marching on `D_L`
  to force `d` nondecreasing likewise only kills *two distinct positive values* (needs the
  smaller value `>0`), not monotonicity. So monotonicity of `f` is a genuine wall on this route.
- **Pivot that COMPLETES the problem — order/separation rigidity (this file).** Instead of
  ordering the graph of `f`, I order the *level sets* of `d`. After the marching lemma pins
  `d` to at most one positive value `b`, the fixed-point set `F={d=0}` and the shift set
  `G={d=b}` partition `(0,∞)`. A single raw inequality (L applied at `(q,p)`) shows **both `F`
  and `G` are open**, and connectedness of `(0,∞)` forbids a partition into two nonempty open
  sets — so one is empty. This retires the whole problem without ever proving `f` monotone.
  Outcome: **COMPLETE.** (This is an order-topology packaging; it corroborates orbit-crossing's
  endgame rather than using a separate mechanism — the honest situation is that all routes meet
  at the F/G-separation crux, and the monotonicity-first packaging cannot avoid it.)

## Current best
Full proof below. Answer: **f(x) = x + c for a constant c ≥ 0, and nothing else.**

## Full proof

Throughout, `f : ℝ_{>0} → ℝ_{>0}`. The hypothesis is, for all `x,y > 0`,
$$\sqrt{\tfrac{x^2+f(y)^2}{2}} \;\ge\; \tfrac{f(x)+y}{2} \;\ge\; \sqrt{x\,f(y)}. \tag{$\star$}$$

**Squared form.** All three expressions in ($\star$) are positive (as `f>0`, `x,y>0`), so
squaring the two inequalities is reversible and equivalent to
$$\textbf{(L)}\quad 2\bigl(x^2+f(y)^2\bigr) \ge \bigl(f(x)+y\bigr)^2, \qquad
\textbf{(R)}\quad \bigl(f(x)+y\bigr)^2 \ge 4\,x\,f(y), \qquad \forall x,y>0.$$
Indeed, for positive reals `u,v`, `u ≥ v ⟺ u² ≥ v²`; (L) is the left inequality of ($\star$)
squared and multiplied by `4`, (R) is the right one squared and multiplied by `4`. We use (L),(R).

---

### Part 1 — Existence (the family `f(x)=x+c`, `c≥0`, works) and forced `c≥0`

Let `f(x)=x+c` with `c` a real constant. For `f` to map `ℝ_{>0}` into `ℝ_{>0}` we need
`x+c>0` for every `x>0`; letting `x→0⁺` forces `c ≥ 0`, and conversely `c≥0 ⟹ x+c ≥ x>0`.
So the admissible constants are exactly `c ≥ 0`.

Now verify ($\star$) for such `f`. Compute the two defects (completing the square; the
"Sum of squares / completing the square" technique, `knowledge_base.md` §Algebra):
$$\bigl(f(x)+y\bigr)^2 - 4x\,f(y) = (x+c+y)^2 - 4x(y+c) = \bigl((x-y)-c\bigr)^2,$$
$$2\bigl(x^2+f(y)^2\bigr) - \bigl(f(x)+y\bigr)^2 = 2x^2+2(y+c)^2-(x+c+y)^2 = \bigl((x-y)-c\bigr)^2.$$
Both identities are verified symbolically (sympy: each difference simplifies to `0`). Since
`((x−y)−c)² ≥ 0`, both (R) and (L) hold, hence ($\star$) holds. So every `f(x)=x+c` with
`c ≥ 0` is a solution. ∎ (Part 1)

The rest of the proof shows these are the *only* solutions. Fix an arbitrary solution `f`.

---

### Part 2 — Structural lemmas (hold for every solution `f`)

**Lemma A (self-composition).** `f(f(y)) = 2f(y) − y` for all `y>0`.

*Proof.* Put `x = f(y)` (legal, `f(y)>0`). In (R): `(f(f(y))+y)² ≥ 4 f(y)·f(y) = 4f(y)²`;
since both sides are positive, `f(f(y))+y ≥ 2f(y)`. In (L): `2(f(y)²+f(y)²) ≥ (f(f(y))+y)²`,
i.e. `4f(y)² ≥ (f(f(y))+y)²`, so `2f(y) ≥ f(f(y))+y`. The two give `f(f(y))+y = 2f(y)`. ∎

**Lemma B (injectivity).** `f` is injective. (`knowledge_base.md` §Functional equations:
"check injectivity".)

*Proof.* If `f(y₁)=f(y₂)`, apply Lemma A to both: `2f(y₁)−y₁ = f(f(y₁)) = f(f(y₂)) = 2f(y₂)−y₂`.
As `f(y₁)=f(y₂)`, this gives `y₁=y₂`. ∎

**Lemma C (orbit arithmetic and `d≥0`).** Write `d(y) := f(y) − y`. Then:
(i) `d(f(y)) = d(y)`;  (ii) `fⁿ(y) = y + n·d(y)` for all integers `n ≥ 0`;  (iii) `d(y) ≥ 0`.

*Proof.* (i) `d(f(y)) = f(f(y)) − f(y) = (2f(y)−y) − f(y) = f(y)−y = d(y)` by Lemma A.
(ii) Induction on `n`. `n=0`: `f⁰(y)=y`. `n=1`: `f(y)=y+d(y)`. Assume `fⁿ(y)=y+n·d(y)`; by (i)
iterated, `d(fⁿ(y)) = d(y)`, so `f^{n+1}(y) = f(fⁿ(y)) = fⁿ(y) + d(fⁿ(y)) = y + n·d(y) + d(y)
= y + (n+1)d(y)`. (iii) Every iterate `fⁿ(y) = y + n·d(y)` is a value of `f` (for `n≥1`),
hence positive; letting `n→∞`, `y + n·d(y) > 0` for all `n` forces `d(y) ≥ 0`. ∎

Thus every solution satisfies `f(x) ≥ x`, and `d(x)=f(x)−x ≥ 0`.

---

### Part 3 — Marching Lemma: `d` takes at most one positive value

**Lemma D.** There is no pair `p,q` with `d(p) > d(q) > 0`. Equivalently, the set of values
`{ d(x) : x>0, d(x)>0 }` has at most one element.

*Proof.* Suppose, for contradiction, `d(p) = a` and `d(q) = b` with `a > b > 0`.

For any two points `s,t>0`, apply (R) at `(x,y) = (f(s), t)`. Here `x=f(s)=s+d(s)`,
`f(x)=f(f(s)) = 2f(s)−s = s+2d(s)` (Lemma A), and `f(y)=f(t)=t+d(t)`. Then (R) reads
$$\bigl(s+2d(s)+t\bigr)^2 \;\ge\; 4\,(s+d(s))\,(t+d(t)).$$
We use this with `s := Q_n := f^n(q)` and `t := P_m := f^m(p)`. By Lemma C, `d(Q_n)=b`,
`Q_n = q+nb`, and `d(P_m)=a`, `P_m=p+ma`. Substituting `d(s)=b`, `d(t)=a`:
$$\bigl(Q_n + 2b + P_m\bigr)^2 \;\ge\; 4\,(Q_n+b)\,(P_m+a).$$
Rearranging (verified by sympy: the difference of the two sides equals the expression below),
$$\bigl(P_m - Q_n\bigr)^2 \;\ge\; 4\,(a-b)\,(Q_n + b). \tag{$\dagger$}$$

Now fix `n` large and choose `m = \lfloor (Q_n - p)/a \rfloor` (nonnegative for large `n`,
since `Q_n = q+nb → ∞`). Then `P_m = p+ma` satisfies `P_m ≤ Q_n < P_m + a`, hence
`0 ≤ Q_n − P_m < a`, so the left side of ($\dagger$) obeys `(P_m − Q_n)² < a²`. The right side
is `4(a−b)(Q_n+b) = 4(a−b)(q + (n+1)b) → +∞` as `n→∞`, because `a−b>0` and `b>0`. For `n`
large enough `4(a−b)(Q_n+b) > a²`, contradicting ($\dagger$). This proves Lemma D.
(The mechanism is the extremal "keep two arithmetic-progression orbits within a bounded gap
while their common target grows linearly"; the bounded square term cannot dominate the linear
right-hand side — `knowledge_base.md` §Combinatorics, extremal principle.) ∎

**Consequence.** By Lemma C(iii) every value `d(x)` is `≥0`, and by Lemma D the *positive*
values of `d` are all equal. Hence there is a constant `b ≥ 0` such that `d(x) ∈ {0, b}` for
every `x>0` (take `b` = the unique positive value if one occurs; if `d≡0`, set `b=0`).

---

### Part 4 — Endgame: the level sets of `d` cannot coexist

Define
$$F := \{ x>0 : d(x)=0 \} = \{ x : f(x)=x \}, \qquad G := \{ x>0 : d(x)=b \}.$$
By Part 3, `F ∪ G = (0,∞)` and `F ∩ G = ∅` when `b>0`. If `b=0` then `d≡0` and `f(x)=x`,
which is the family with `c=0` — done. So assume `b>0`; we must rule out `F,G` both nonempty.

Suppose `p ∈ F` and `q ∈ G`, so `f(p)=p` and `f(q)=q+b`. Apply **(L) at `(x,y)=(q,p)`**:
$$2\bigl(q^2 + f(p)^2\bigr) \ge \bigl(f(q)+p\bigr)^2 \;\Longleftrightarrow\; 2(q^2+p^2) \ge (q+b+p)^2.$$
Expanding (sympy-verified) this is exactly
$$\boxed{\;(p-q)^2 \;\ge\; b^2 + 2b\,(p+q).\;} \tag{II}$$
Since `b,p,q>0`, the right side is `≥ b²`, so **(II)** gives the clean separation
$$|\,p - q\,| \;\ge\; b \qquad \text{for every } p\in F,\; q\in G. \tag{Sep}$$

**`F` is open.** Let `p∈F`. By (Sep) no point of `G` lies within distance `b` of `p`. Put
`δ = \min(b,p)/2 > 0`. For `x ∈ (p-δ, p+δ)` we have `x > p-δ ≥ p/2 > 0`, so `x∈(0,∞)=F∪G`,
and `|x-p| < δ ≤ b/2 < b`, so `x∉G` by (Sep). Hence `x∈F`. Thus `(p-δ,p+δ) ⊆ F`: `F` is open.

**`G` is open.** Let `q∈G`. By (Sep) no point of `F` lies within distance `b` of `q`. Put
`δ = \min(b,q)/2 > 0`. For `x ∈ (q-δ, q+δ)` we have `x > q/2 > 0`, so `x∈F∪G`, and
`|x-q| < δ ≤ b/2 < b`, so `x∉F` by (Sep). Hence `x∈G`. Thus `(q-δ,q+δ) ⊆ G`: `G` is open.

So `F` and `G` are open, disjoint, and cover `(0,∞)`. But `(0,∞)` is an interval, hence
**connected**, so it cannot be written as the union of two disjoint nonempty open sets
(definition of connectedness). Therefore `F` and `G` cannot both be nonempty.

**Conclusion.** Exactly one of `F`, `G` is all of `(0,∞)`:
- if `F=(0,∞)`, then `f(x)=x` for all `x` (this is `c=0`);
- if `G=(0,∞)`, then `f(x)=x+b` for all `x` (this is `c=b>0`).

In every case `f(x) = x + c` for a constant `c ≥ 0`. Together with Part 1 (each such `f` is a
solution and `c≥0` is forced by positivity), we conclude:

$$\boxed{\; f(x) = x + c,\quad c \ge 0 \ \text{constant} \;}$$

are **exactly** the functions satisfying ($\star$). ∎

---

**Answer verification (final check).** For `f(x)=x+c`, `c≥0`, both defects equal `((x−y)−c)²≥0`
(Part 1, sympy-verified), so ($\star$) holds; and `f(x)=x+c>0` on `(0,∞)` iff `c≥0`. The
characterization is thus verified by direct substitution, as required for a `compute_and_prove`
/ `characterization` answer.

## Promotable lemmas

- **Lemma A (self-composition):** every solution of ($\star$) satisfies `f(f(y))=2f(y)−y`.
  Proved in Part 2 by setting `x=f(y)` in (R) and (L). Reusable across all approaches.
- **Lemma C (orbit arithmetic):** `d(y):=f(y)−y` satisfies `d∘f=d`, `fⁿ(y)=y+n·d(y)`, `d≥0`.
  Proved in Part 2. Reusable.
- **Lemma D (≤1 positive value of `d`):** no `p,q` with `d(p)>d(q)>0`; hence `d(x)∈{0,b}`.
  Proved in Part 3 by the orbit-marching argument on inequality ($\dagger$). This is the shared
  crux with orbit-crossing; certifying it once lets every approach import it.
- **Separation/openness endgame (Part 4):** if `d(x)∈{0,b}` with `b>0`, then `F={d=0}` and
  `G={d=b}` are both open (via (II): `|p−q|≥b`), so connectedness of `(0,∞)` forces one empty.
  Reusable to close the `{0,b}` residual in any approach.
