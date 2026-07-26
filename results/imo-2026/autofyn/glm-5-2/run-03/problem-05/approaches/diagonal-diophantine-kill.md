# diagonal-diophantine-kill

**Problem (IMO 2026 P5).** Determine all functions `f : R_{>0} -> R_{>0}` such that
```
            sqrt( (x² + f(y)²) / 2 )  >=  (f(x) + y)/2  >=  sqrt( x · f(y) )        (◆)
```
for every `x, y > 0`.

**Answer.** `f(x) = x + c` for an arbitrary constant `c >= 0`.

---

## Status
solved

## Approaches tried
- Round 1: `(L+R, L−R)` sign-decomposition → master bound `(★)` → two-forward-orbit Diophantine kill (Kronecker density for irrational displacement ratios, exact-zero Frobenius lattice point for rational ratios), with the `d1 = 0` edge case closed by a maximal-fixed-interval + boundary-perturbation reduction that re-enters the main kill. All cases settled; construction verified. — solved.

## Current best
Complete rigorous proof. The edge case `d1 = 0 < d2` flagged by the outline-reviewer is closed by Lemma 4 (perturbation reduction): a maximal interval of fixed points has a finite right endpoint, at which continuity-at-a-zero plus maximality force positive-displacement points with arbitrarily small displacement, reducing to the main kill with both displacements strictly positive.

## Full proof

### 0. Notation and the two cheap structural facts

Write the **displacement** `g(t) := f(t) - t`, so `f(t) = t + g(t)`. The inequality `(◆)` becomes, after squaring both nonneg sides, the pair of conditions
```
L(x,y) := 2(x² + f(y)²) - (f(x) + y)²  >=  0,        (L)
R(x,y) := (f(x) + y)² - 4·x·f(y)        >=  0.        (R)
```
(Both sides of each inequality in `(◆)` are nonnegative — square roots and an average of positive numbers — so squaring is legitimate.)

**Lemma 1 (cheap diagonal collapse — `(C1)` and `(C2)`).** *Every solution satisfies*
```
(C1)   f(f(y)) = 2 f(y) - y   for all y > 0,
(C2)   g(y) >= 0              for all y > 0.
```
*Moreover `g` is constant on each forward orbit and `fⁿ(y) = y + n·g(y)` for all `n >= 0`.*

*Proof.* Put `x = f(y)` in `(◆)`. The outer pair `(x, f(y)) = (f(y), f(y))` becomes equal; for an equal pair the QM, AM, and GM all coincide at `f(y)`. Concretely `sqrt((f(y)² + f(y)²)/2) = f(y)` and `sqrt(f(y)·f(y)) = f(y)`, so `(◆)` reads
```
f(y)  >=  (f(f(y)) + y)/2  >=  f(y),
```
forcing `(f(f(y)) + y)/2 = f(y)`, i.e. `f(f(y)) = 2 f(y) - y`. This is `(C1)`.

Rewrite `(C1)` via `f(t) = t + g(t)`: `f(f(y)) = f(y) + g(f(y)) = y + g(y) + g(f(y))`, while `2 f(y) - y = y + 2 g(y)`; hence `g(f(y)) = g(y)`. So `g` is invariant under `f`. The linear recurrence `a_{n+1} = 2 a_n - a_{n-1}` (with `a_0 = y`, `a_1 = f(y) = y + g(y)`, obtained from `(C1)` with `y` replaced by `fⁿ⁻¹(y)`) has characteristic polynomial `(r-1)²`, giving `a_n = y + n·g(y)`, i.e. `fⁿ(y) = y + n·g(y)`; and `g(fⁿ(y)) = g(y)` by invariance.

If `g(y) < 0`, then `fⁿ(y) = y + n·g(y) -> -∞` as `n -> ∞`, so `fⁿ(y) < 0` for large `n`, contradicting `fⁿ(y) ∈ R_{>0}` (the codomain, since `f` maps `R_{>0}` to `R_{>0}`). Hence `g(y) >= 0`. This is `(C2)`. ∎

So `f(y) >= y` everywhere, with equality iff `y` is a fixed point. This is forced and free; it is necessary, not sufficient — the whole remaining task is to show `g` is globally constant.

### 1. The `(L+R, L−R)` sign-decomposition and the master bound `(★)`

**Lemma 2 (the two identities).** *With `g(t) = f(t) - t`,*
```
L(x,y) + R(x,y) = 2 (x - f(y))²,                                    (I)
L(x,y) - R(x,y) = 2 (g(y) - g(x))·(x + f(y) + f(x) + y).           (II)
```
*In particular `x + f(y) + f(x) + y = 2x + 2y + g(x) + g(y) > 0` for all `x, y > 0` (each of `x, f(x), y, f(y)` is positive).*

*Proof.* Identity (I) is completing the square on the QM-vs-GM gap:
```
L + R = [2(x² + f(y)²) - (f(x)+y)²] + [(f(x)+y)² - 4 x f(y)]
      = 2(x² - 2 x f(y) + f(y)²) = 2 (x - f(y))².
```
For (II), expand `L - R` and complete a different square — the difference of two squares `(x + f(y))² - (f(x) + y)²`:
```
L - R = 2(x² + f(y)²) - 2(f(x) + y)² + 4 x f(y)
      = 2[(x² + 2 x f(y) + f(y)²) - (f(x) + y)²]
      = 2[(x + f(y))² - (f(x) + y)²]
      = 2[(x + f(y)) - (f(x) + y)]·[(x + f(y)) + (f(x) + y)].
```
The first bracket is `(x - f(x)) + (f(y) - y) = -g(x) + g(y) = g(y) - g(x)`; the second is `x + f(y) + f(x) + y`. This is (II). ∎

(Both identities were checked symbolically with sympy by the outline-reviewer and re-derived in prose above.)

**Lemma 3 (master bound `(★)`).** *The original inequality `(◆)` is equivalent to*
```
(★)   |g(x) - g(y)| · (2x + 2y + g(x) + g(y))  <=  (x - y - g(y))²    for all x, y > 0.
```

*Proof.* For real numbers `a, b`, the conditions `a >= 0` and `b >= 0` are together equivalent to `a + b >= 0` and `|a - b| <= a + b` (the forward direction is `|a-b| <= max(a,b) <= a+b`; conversely `-(a+b) <= a-b <= a+b` gives `-2b <= 0` and `-2a <= 0`). Apply this to `a = L(x,y)`, `b = R(x,y)`:

`(L) ∧ (R)  <=>  L + R >= 0  ∧  |L - R| <= L + R.`

By (I), `L + R = 2 (x - f(y))² = 2 (x - y - g(y))² >= 0` always. By (II), `|L - R| = 2 |g(y) - g(x)| · (x + f(y) + f(x) + y) = 2 |g(x) - g(y)| · (2x + 2y + g(x) + g(y))`. The condition `|L - R| <= L + R` thus becomes
```
2 |g(x) - g(y)| · (2x + 2y + g(x) + g(y))  <=  2 (x - y - g(y))²,
```
which, on dividing by `2`, is `(★)`. ∎

The factor `2x + 2y + g(x) + g(y)` is strictly positive for all `x, y > 0` (positivity of `x, y, f(x), f(y)`), so `(★)` carries the full strength of `(◆)`.

### 2. The Diophantine kill (both displacements strictly positive)

Throughout this section assume there exist `a, b > 0` with
```
0 < d1 := g(a) < d2 := g(b).
```
By Lemma 1, the forward orbits `a + n·d1` (`n >= 0`) and `b + m·d2` (`m >= 0`) carry `g`-values `d1` and `d2` respectively. Substitute `x = a + n·d1`, `y = b + m·d2` into `(★)`; since `g(x) = d1`, `g(y) = d2`:
```
(d2 - d1)·(2a + 2n·d1 + 2b + 2m·d2 + d1 + d2)  <=  (a - b + n·d1 - (m+1)·d2)².    (★★★)
```
Set `u_{n,m} := n·d1 - (m+1)·d2`, so the RHS is `(a - b + u_{n,m})²`, while the LHS equals
`(d2 - d1)·(2a + 2b + d1 + d2 + 2n·d1 + 2m·d2)`, which tends to `+∞` as `n, m -> ∞` (both `d1, d2 > 0`).

#### 2.1. Irrational ratio `d1/d2 ∉ Q`

**Lemma 4 (density on the nonneg grid).** *If `α > 0` is irrational, the set `{n·α - m : n, m ∈ Z_{>=0}}` is dense in `R`. Moreover the witnessing pairs can be taken with `n` and `m` both arbitrarily large.*

*Proof.* This is the one-dimensional Kronecker / Weyl equidistribution theorem (knowledge_base.md, "Kronecker / Weyl equidistribution"): for irrational `α`, the sequence of fractional parts `{ {k·α} : k >= 1 }` is dense in `[0, 1)`. Fix a target `T ∈ R` and `ε > 0`, and a lower bound `M`. Write `T = ⌊T⌋ + {T}`. By Kronecker, there are arbitrarily large integers `k` with `{k·α}` within `ε` (in the circle metric) of `{T}`; choose `k > M`. Then `k·α - ⌊k·α⌋ = {k·α}` is within `ε` of `{T} = T - ⌊T⌋`, so `k·α - (⌊k·α⌋ - ⌊T⌋)` is within `ε` of `T`. Set `n := k` and `m := ⌊k·α⌋ - ⌊T⌋`. For `k` large enough (which we are free to demand, since the equidistribution theorem yields arbitrarily large `k`), `m = ⌊k·α⌋ - ⌊T⌋ -> +∞` (because `α > 0`), so `m >= M` as well. Both `n, m >= M`, and `|n·α - m - T| < ε`. ∎

Apply Lemma 4 with `α = d1/d2` (irrational) to the target `T := (b - a)/d2 + 1` (so that `u_{n,m} = d2·(n·α - m - 1)` lands within `d2·ε` of `d2·(T - 1) = b - a`). We obtain a sequence `(n_j, m_j)` with `n_j, m_j -> ∞` and `u_{n_j, m_j} -> b - a`, hence the RHS of `(★★★)` satisfies `(a - b + u_{n_j, m_j})² -> 0`. The LHS tends to `+∞`. For `j` large enough, LHS `>` RHS, contradicting `(★★★)`. Contradiction. ∎

#### 2.2. Rational ratio `d1/d2 = p/q ∈ Q`

Write `d1/d2 = p/q` in lowest terms with `p, q` positive integers; `p < q` since `d1 < d2`, and `p >= 1` since `d1 > 0`. For each integer `k >= 1` set
```
n := k·q,    m := k·p - 1   (>= 0, since p >= 1 and k >= 1).
```
Then `n·d1 - (m+1)·d2 = k·q·d1 - k·p·d2 = k·(q·d1 - p·d2) = 0` (because `d1/d2 = p/q`), so the RHS of `(★★★)` is the constant `(a - b)²`. The LHS is
```
(d2 - d1)·(2a + 2b + d1 + d2 + 2k·q·d1 + 2(k·p - 1)·d2)  ->  +∞   as k -> ∞.
```
For `k` large enough the LHS exceeds the constant `(a - b)²`, contradicting `(★★★)`. Contradiction. ∎

(One may recognize `k ↦ (kq, kp-1)` as the exact-zero lattice point of the linear form `n·d1 - (m+1)·d2` — the one-dimensional Frobenius/coin-problem degenerate case; it is exact because the ratio is rational.)

**Conclusion of Section 2.** Two points with strictly positive unequal displacements `0 < d1 < d2` cannot coexist.

### 3. The edge case `d1 = 0 < d2` (the reviewer's flag)

Assume now that `g(a) = 0` for some `a > 0` (a fixed point) and `g(b) = d2 > 0` for some `b > 0`. We reduce this to the main kill of Section 2.

**Lemma 5 (continuity at a zero).** *If `g(a) = 0`, then `g(x) -> 0` as `x -> a`.*

*Proof.* Set `y = a` in `(★)`. Since `g(y) = 0`, the bound reads
```
g(x) · (2x + 2a + g(x))  <=  (x - a)²        for all x > 0.
```
For `|x - a| < a/2` we have `x > a/2 > 0`, so `2x + 2a + g(x) >= 2x + 2a > a + 2a = 3a > 0` (using `g(x) >= 0` from `(C2)`). Hence `0 <= g(x) <= (x - a)² / (3a) -> 0` as `x -> a`. ∎

We now distinguish two sub-cases.

**Sub-case (i): for every `ε > 0` there is `x ∈ (a - ε, a + ε)` with `g(x) > 0`.** Pick a sequence `x_n -> a` with `g(x_n) > 0` (possible by assumption; `g >= 0` rules out the alternative sign). By Lemma 5, `g(x_n) -> 0`, so for `n` large `0 < g(x_n) < d2`. Renaming `x_n ↦ a` and `g(x_n) ↦ d1`, we are exactly in the situation `0 < d1 < d2` of Section 2 — contradiction.

**Sub-case (ii): `g ≡ 0` on some open interval `I` around `a`.** Let `I_{max} = (α, β)` be the maximal open interval containing `a` on which `g ≡ 0` (the union of all such intervals, itself open and connected, hence an open interval). We have `0 <= α < a < β <= ∞`.

*Claim.* `β < ∞`.

*Proof of claim.* Suppose `β = ∞`, i.e. `g ≡ 0` on `(α, ∞)`. Since `g(b) = d2 > 0`, the point `b` does not lie in `(α, ∞)`, so `b <= α`. (If `α = 0` this is automatic, as `b > 0`.) The forward orbit of `b` is `b + n·d2 -> +∞` as `n -> ∞` (since `d2 > 0`); for all large `n`, `b + n·d2 > α`, so `b + n·d2 ∈ (α, ∞)` and thus `g(b + n·d2) = 0`. But by orbit invariance (Lemma 1), `g(b + n·d2) = g(b) = d2 > 0` — contradiction. Hence `β < ∞`. ∎

Now consider the right endpoint `β` (note `β > a > 0`, so `β` lies in the domain).

*Claim.* `g(β) = 0`.

*Proof.* Take `y ∈ I_{max} = (α, β)` (so `g(y) = 0`) and `x = β` in `(★)`:
```
|g(β) - 0| · (2β + 2y + g(β) + 0)  <=  (β - y - 0)² = (β - y)².
```
Let `y -> β⁻`. The LHS tends to `g(β) · (4β + g(β))` (nonnegative), the RHS tends to `0`. So `g(β)·(4β + g(β)) <= 0`. Since `g(β) >= 0` and `4β + g(β) >= 4β > 0`, this forces `g(β) = 0`. ∎

*Claim.* `g` is not identically zero on any interval `(β, β + ε)`, `ε > 0`.

*Proof.* If `g ≡ 0` on `(β, β + ε)`, then (together with `g ≡ 0` on `I_{max}` and `g(β) = 0`) we would have `g ≡ 0` on `(α, β + ε)`, an open interval strictly containing `I_{max} = (α, β)`, contradicting the maximality of `I_{max}`. ∎

Combining: for every `ε > 0` there exists `x ∈ (β, β + ε)` with `g(x) > 0` (since `g >= 0` everywhere and `g` is not identically zero on `(β, β + ε)`). Pick a sequence `x_n -> β⁺` with `g(x_n) > 0`. By Lemma 5 (applied at the zero `β`), `g(x_n) -> 0`. For `n` large, `0 < g(x_n) < d2`. Renaming `x_n ↦ a` and `g(x_n) ↦ d1`, we are again in the situation `0 < d1 < d2` of Section 2 — contradiction.

Both sub-cases (i) and (ii) reduce to the (already contradictory) main kill. **The edge case `d1 = 0 < d2` is therefore also impossible.** ∎

### 4. `g` is constant

Suppose `g` is not constant. Then there exist `a, b > 0` with `g(a) ≠ g(b)`; renaming, take `g(a) < g(b)`. By `(C2)`, `g(a) >= 0`, so `0 <= d1 := g(a) < d2 := g(b)`.

- If `d1 > 0`, Section 2 (Lemma 4 + Frobenius) gives a contradiction.
- If `d1 = 0`, Section 3 (perturbation reduction) gives a contradiction.

Both cases are impossible, so `g` is constant: `g ≡ c` for some `c >= 0` (by `(C2)`). Hence `f(x) = x + c`, `c >= 0`.

### 5. Construction (every `c >= 0` works)

**Lemma 6 (sufficiency).** *For every constant `c >= 0`, the function `f(x) = x + c` satisfies `(◆)`.*

*Proof.* With `f(x) = x + c`, the middle term is `(f(x) + y)/2 = (x + y + c)/2 = AM(x, y + c)`, the arithmetic mean of the pair `(x, y + c)`. The leftmost term is `sqrt((x² + f(y)²)/2) = sqrt((x² + (y+c)²)/2) = QM(x, y + c)`, the quadratic mean of the same pair; the rightmost is `sqrt(x · f(y)) = sqrt(x · (y + c)) = GM(x, y + c)`, the geometric mean. The chain `(◆)` is thus exactly
```
QM(x, y + c)  >=  AM(x, y + c)  >=  GM(x, y + c),
```
i.e. the standard **QM ≥ AM ≥ GM** chain (knowledge_base.md, "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases") applied to the positive pair `(x, y + c)`. Positivity holds: `x > 0` and `y + c > 0` (since `y > 0`, `c >= 0`). Direct algebra also confirms equality-of-both-squared-differences: both `L(x,y)` and `R(x,y)` reduce to the single square `(x - y - c)² >= 0` (verified by expansion:
`L = 2(x² + (y+c)²) - (x + y + c)² = (x - y - c)²`,
`R = (x + y + c)² - 4x(y + c) = (x - y - c)²`;
the common value is nonnegative, with equality iff `x = y + c`, i.e. `x = f(y)`).

The codomain condition `f : R_{>0} -> R_{>0}` forces `c >= 0`: for `c >= 0`, `x + c > 0` for all `x > 0`; for `c < 0`, `x + c <= 0` whenever `x <= -c`, outside the codomain. ∎

### 6. Conclusion

Combining Sections 4 (necessity: `g ≡ c`, `c >= 0`) and 5 (sufficiency: every `c >= 0` works), the set of all solutions of `(◆)` is exactly
```
                    f(x) = x + c,    c ∈ R,  c >= 0.                              ∎
```

## Promotable lemmas

- **Lemma 1 (diagonal collapse):** `f(f(y)) = 2 f(y) - y`, `g := f - id >= 0`, `g` is constant on forward orbits, `fⁿ(y) = y + n·g(y)`. Proved in §0. (Shared by every approach; candidate for `lemmas/diagonal-collapse.md`.)
- **Lemma 2 (`(L+R, L−R)` identities):** `L+R = 2(x - f(y))²`, `L−R = 2(g(y)−g(x))·(x+f(y)+f(x)+y)`. Proved in §1.
- **Lemma 3 (master bound `(★)`):** `(◆)` is equivalent to `|g(x)−g(y)|·(2x+2y+g(x)+g(y)) <= (x − y − g(y))²`. Proved in §1. (Shared with `lipschitz-connectedness`; candidate for `lemmas/master-bound.md`.)
- **Lemma 4 (nonneg-grid Kronecker density):** for irrational `α > 0`, `{n·α − m : n, m ∈ Z_{>=0}}` is dense in `R`, with arbitrarily large witnesses. Proved in §2.1.
- **Lemma 5 (continuity at a zero):** `g(a)=0 ⇒ g(x) -> 0` as `x -> a`. Proved in §3.
