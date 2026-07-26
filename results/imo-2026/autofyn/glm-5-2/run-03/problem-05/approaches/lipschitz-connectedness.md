## Status
solved

## Approaches tried
- (round 1) lipschitz-connectedness: derived the master bound (★) from the `(L+R, L−R)` sign-decomposition; used the cheap diagonal kill for `g>=0` and orbit-invariance; extracted `lim_{a→∞} g(a) = β` via Dirichlet nearest-integer approximation by orbit points; deduced the value set of `g` is contained in `{0, β}`; closed the continuity-at-nonzero gap NOT by a naive squeeze (which the reviewer correctly flagged gives only boundedness) but by combining the master bound with the discrete value set to show both level sets `{g=0}` and `{g=β}` are open, finishing by connectedness of `(0,∞)`. Outcome: complete proof.

## Current best
The full characterization is proved: every admissible `f` is `f(x)=x+c`, `c>=0`. The make-or-break gap flagged by the outline-reviewer (continuity at a nonzero point) is closed by a sharper route: rather than squeezing `g(a+h)→α` directly from (★) (which only yields boundedness, since the RHS is `~α²` not `O(h²)`), we use the discrete value set `{0,β}` (itself obtained from the orbit + limit-at-infinity) and show that near a `β`-point the master bound rules out the value `0`, forcing `g=β` on a neighbourhood. No open gaps remain.

## Full proof

We determine all `f : R_{>0} → R_{>0}` satisfying, for every `x, y > 0`,

```
        ⎛ x² + f(y)² ⎞                 ⎽⎺
   √    ⎜ ─────────── ⎟   ≥   (f(x) + y)/2   ≥   √(x·f(y)).
        ⎝     2       ⎠
```

We prove the answer is exactly `f(x) = x + c` for a constant `c ≥ 0`.

---

### 1. Diagonal collapse: the cheap kill (C1) + (C2)

Specialize `x = f(y)` (legitimate, since `f(y) > 0`). The pair `(x, f(y)) = (f(y), f(y))` is then equal; for an equal pair `(a, a)` the three classical means coincide (QM-AM-GM, [knowledge_base: Standard inequalities]):

```
QM = √((a²+a²)/2) = a,   AM = (a+a)/2 = a,   GM = √(a·a) = a.
```

The outer (QM) and inner (GM) bounds of the sandwich therefore both collapse to the same value `f(y)`. The middle term, with `x = f(y)`, reads `(f(f(y)) + y)/2`. Equality throughout forces

```
(C1)   f(f(y)) = 2 f(y) − y     for all y > 0.
```

Introduce the **displacement** `g(y) := f(y) − y`. Since `f(t) = t + g(t)`, equation (C1) becomes

```
f(y) + g(f(y)) = y + 2 g(y)   ⇒   (y + g(y)) + g(f(y)) = y + 2 g(y)   ⇒   g(f(y)) = g(y).
```

So `g` is **invariant along each forward orbit**. Inducting, `f^{n+1}(y) = f(f^n(y)) = f^n(y) + g(f^n(y)) = f^n(y) + g(y)` (orbit-invariance at the orbit point `f^n(y)`), with `f^0(y) = y`; hence

```
   f^n(y) = y + n·g(y)     for all n ≥ 0.                       (orbit)
```

Because every iterate `f^n(y)` must lie in `R_{>0}`, if `g(y) < 0` then `y + n·g(y) → −∞`, a contradiction for large `n`. Therefore

```
(C2)   g(y) ≥ 0     for all y > 0   (hence f(y) ≥ y).
```

This much is forced and free; it is necessary, not yet sufficient.

---

### 2. The master bound (★)

Square both sides of the original sandwich (all quantities are positive, so squaring is monotone on the relevant range). Define the two nonnegative quantities

```
L := 2(x² + f(y)²) − (f(x) + y)² ≥ 0     (the squared QM-AM gap),
R := (f(x) + y)² − 4 x f(y)     ≥ 0      (the squared AM-GM gap).
```

(Nonnegativity of `L, R` is exactly the two given inequalities.) We compute two identities by direct expansion, substituting `f(t) = t + g(t)` throughout (algebra / SOS — [knowledge_base: Sum of squares]):

**(I1)** `L + R = 2(x − f(y))² = 2(x − y − g(y))²`.

*Proof.* `L + R = 2(x² + f(y)²) − 4 x f(y) = 2(x² − 2 x f(y) + f(y)²) = 2(x − f(y))²`. ∎

**(I2)** `L − R = 2 (g(y) − g(x)) (2x + 2y + g(x) + g(y))`.

*Proof.* Expanding `L` and `R` in `g`:
`L = (x−y)² + 4 y g(y) + 2 g(y)² − 2(x+y) g(x) − g(x)²`,
`R = (x−y)² + 2(x+y) g(x) + g(x)² − 4 x g(y)`.
Subtracting, the `(x−y)²` and the `±(x+y)g(x), ±g(x)², ∓xg(y)/yg(y)` terms regroup as
`L − R = 4(x+y)g(y) − 4(x+y)g(x) + 2 g(y)² − 2 g(x)² = (g(y)−g(x))·[4(x+y) + 2(g(x)+g(y))] = 2(g(y)−g(x))(2x+2y+g(x)+g(y))`. ∎
(Both identities verified symbolically with `sympy`.)

The factor `2x + 2y + g(x) + g(y)` rewrites as `x + f(x) + y + f(y)`; each summand is strictly positive (since `x, y, f(x), f(y) ∈ R_{>0}`), so this factor is **unconditionally strictly positive** — no use of `g ≥ 0` is needed here.

Because `L, R ≥ 0`, their difference is bounded in absolute value by their sum: `|L − R| ≤ L + R`. Substituting (I1) and (I2) and dividing by `2`:

```
   (★)   |g(x) − g(y)| · (2x + 2y + g(x) + g(y))  ≤  (x − y − g(y))²    for all x, y > 0.
```

This is the **master bound**. It is the single load-bearing analytic estimate; the whole proof flows from it.

---

### 3. The limit at infinity via Dirichlet nearest-integer

We now split into two terminal branches.

**Branch A — `g` has no positive value.** Then by (C2) `g ≡ 0`, i.e. `f(x) = x`. This is a valid solution (the case `c = 0` of the construction, verified in §5). The proof is complete in this branch.

**Branch B — `g` takes a positive value.** Choose `b > 0` with `β := g(b) > 0`, and write `b_m := b + m·β = f^m(b)` (`m ≥ 0`); by orbit-invariance (§1), `g(b_m) = β` for every `m`. The points `{b_m}_{m≥0}` form an arithmetic progression of spacing `β`.

We extract the limit of `g` at infinity.

**Claim.** `lim_{a → ∞} g(a) = β`.

*Proof of the claim.* Let `a > b` be large. By the nearest-integer / pigeonhole principle (Dirichlet spacing — [knowledge_base: Three-gap / Steinhaus]; in one dimension the orbit `b_m = b + mβ` partitions `(b, ∞)` into intervals of length `β`, so every `a ≥ b` lies within `β/2` of some `b_m` with `m ≥ 0`), choose `m ≥ 0` with `|a − b_m| ≤ β/2`. Apply the master bound (★) with `x = a`, `y = b_m` (so `g(y) = β`):

```
   |g(a) − β| · (2a + 2 b_m + g(a) + β)  ≤  (a − b_m − β)².
```

Set `e := a − b_m`, so `|e| ≤ β/2`. Then `a − b_m − β = e − β ∈ [−3β/2, −β/2]`, hence the right-hand side satisfies `(a − b_m − β)² = (e − β)² ≤ (3β/2)² = 9β²/4`.

For the factor on the left, use `b_m = a − e ≥ a − β/2` (for `a ≥ b`):

```
   2a + 2 b_m + g(a) + β  ≥  2a + 2(a − β/2) + 0 + β  =  4a.
```

(The bound `g(a) ≥ 0` is (C2).) Combining,

```
   |g(a) − β| · 4a  ≤  9β²/4     ⇒     |g(a) − β|  ≤  9β² / (16 a).
```

The right-hand side tends to `0` as `a → ∞`. Hence `g(a) → β`. ∎

---

### 4. The value set of `g` is contained in `{0, β}`

**Claim.** Under Branch B, every positive value of `g` equals `β`. Combined with (C2), the value set of `g` is a subset of `{0, β}`.

*Proof.* Let `y₀ > 0` with `g(y₀) = δ > 0`. Its forward orbit `y₀ + n·δ = f^n(y₀)` (eq. (orbit)) tends to `+∞` as `n → ∞`, and `g(y₀ + n δ) = δ` for every `n` (orbit-invariance). By the claim of §3, `g(t) → β` as `t → ∞`; restricting to the sequence `t = y₀ + n δ` gives `g(y₀ + n δ) → β`. But `g(y₀ + n δ) = δ` identically. Therefore `δ = β`. ∎

---

### 5. Both level sets are open; connectedness finishes

We continue in Branch B (so `β > 0` is fixed and the value set of `g` lies in `{0, β}`). We show that the two level sets

```
   Z := {t > 0 : g(t) = 0},     P := {t > 0 : g(t) = β}
```

are **both open** in `R_{>0}`. (They partition `R_{>0}`, since by §4 every value is `0` or `β`.)

**Openness of `Z`.** Let `a ∈ Z` (`g(a) = 0`). Apply (★) with `y = a`, `x = a + h` (for `h` with `|h| < a/2`, so `x > a/2 > 0`):

```
   |g(a+h) − 0| · (2(a+h) + 2a + g(a+h) + 0)  ≤  (a + h − a − 0)² = h².
```

The factor on the left is `2(a+h) + 2a + g(a+h) ≥ 2(a+h) + 2a ≥ 2·(a/2) + 2a = 3a > 0` (using `g(a+h) ≥ 0` from (C2) and `a+h > a/2`). Hence

```
   g(a+h)  ≤  h² / (3a)   →   0    as h → 0.
```

Since by §4 the value `g(a+h)` is either `0` or `β`, and for `|h|` small enough `h²/(3a) < β` (any positive `β`), we must have `g(a+h) = 0`. Thus `g = 0` on a neighbourhood of `a`; `a` is an interior point of `Z`. So `Z` is open.

**Openness of `P`.** Let `b ∈ P` (`g(b) = β > 0`). Apply (★) with `y = b`, `x = b + h` (for `h` with `b + h > 0`):

```
   |g(b+h) − β| · (2(b+h) + 2b + g(b+h) + β)  ≤  (b + h − b − β)² = (h − β)².            (∗)
```

By §4, `g(b+h) ∈ {0, β}`. We rule out `g(b+h) = 0` for `h` near `0`. Suppose for contradiction `g(b+h) = 0`; then `|g(b+h) − β| = β`, and (∗) becomes

```
   β · (2(b+h) + 2b + 0 + β)  ≤  (h − β)²,
```

i.e. (expanding `(h−β)² = h² − 2βh + β²` and the left `β(4b + 2h + β)`),

```
   4βb + 2βh + β²  ≤  h² − 2βh + β²
   ⇔   4βb + 4βh  ≤  h²
   ⇔   h² − 4βh − 4βb  ≥  0.
```

The quadratic `Q(h) := h² − 4βh − 4βb` has value `Q(0) = −4βb < 0` (since `β, b > 0`), and its two roots are `h = 2β ± 2√(β² + βb)`; because `√(β² + βb) > β`, the smaller root is negative and the larger positive, so `Q(h) < 0` on the open interval `(2β − 2√(β²+βb), 2β + 2√(β²+βb))` containing `0`. (One checks `2β − 2√(β²+βb) > −b`: this is `2√(β²+βb) < 2β + b`, i.e. `4(β²+βb) < 4β² + 4βb + b²`, i.e. `0 < b²`, true.) Hence for every `h` in the nonempty open interval `(2β − 2√(β²+βb), 2β + 2√(β²+βb))` (intersected with `(-b, ∞)`, but the lower endpoint already exceeds `−b`), `Q(h) < 0`, the implication `g(b+h)=0 ⇒ Q(h)≥0` is contradicted, and so `g(b+h) = β`. Thus `g = β` on a neighbourhood of `b`; `b` is an interior point of `P`. So `P` is open.

**Connectedness close.** `R_{>0} = (0, ∞)` is connected (it is an interval; [knowledge_base: General Proof Methods] — the clopen-partition characterization of connectedness). We have exhibited `R_{>0} = Z ∪ P` as a union of two disjoint open sets. By connectedness one of them is empty. In Branch B, `P` is nonempty (it contains `b`), so `Z` is empty and `g ≡ β`. Hence `f(x) = x + β` for a constant `β ≥ 0`.

(If instead Branch A held, `g ≡ 0`, i.e. `f(x) = x`, the same form with `β = 0`.) In either branch, `f(x) = x + c` for some constant `c ≥ 0`.

---

### 6. Construction (sufficiency) and verification

We verify that `f(x) = x + c` with `c ≥ 0` is admissible and that `c ≥ 0` is forced.

For `f(x) = x + c`, the middle term is `(f(x) + y)/2 = (x + c + y)/2 = (x + (y + c))/2`, which is exactly the **arithmetic mean** of the pair `(x, y + c)` (with both entries positive: `x > 0`, and `y + c ≥ y > 0`). The outer bound is

```
   √((x² + f(y)²)/2) = √((x² + (y + c)²)/2) = QM of (x, y + c)  ≥  AM of (x, y + c),
```

and the inner bound is

```
   √(x · f(y)) = √(x · (y + c)) = GM of (x, y + c)  ≤  AM of (x, y + c),
```

both holding by the classical **QM-AM** and **AM-GM** inequalities respectively ([knowledge_base: Standard inequalities]), valid for any positive pair. Hence `f(x) = x + c` satisfies the sandwich for every `x, y > 0`.

The condition `c ≥ 0` is forced by the codomain: `f(x) = x + c > 0` for all `x > 0` iff `c ≥ 0` (if `c < 0`, take `x ↓ 0` to get `f(x) = x + c < 0` for small `x`).

---

### 7. Conclusion

Combining the necessity proved in §§1–5 (`f(x) = x + c`, `c ≥ 0`) with the sufficiency verified in §6, the set of all functions `f : R_{>0} → R_{>0}` satisfying the given double inequality is exactly

```
   ⎧                 ⎫
   ⎨  f(x) = x + c  :  c ≥ 0  ⎬.
   ⎩                 ⎭
```

∎

## Promotable lemmas

1. **Master bound (★).** *Statement:* for any admissible `f`, with `g = f − id`, one has
   `|g(x) − g(y)|·(2x + 2y + g(x) + g(y)) ≤ (x − y − g(y))²` for all `x, y > 0`.
   Proved in §2 of this approach (`results/imo-2026-05/approaches/lipschitz-connectedness.md`). The factor `2x+2y+g(x)+g(y) = x+f(x)+y+f(y) > 0` is unconditionally positive, so (★) holds before the cheap kill. Importable by any approach that needs a single signed estimate from the two squared inequalities.

2. **Diagonal collapse (C1)+(C2).** *Statement:* specializing `x = f(y)` forces `f(f(y)) = 2 f(y) − y` (equivalently `g(f(y)) = g(y)`), hence `f^n(y) = y + n·g(y)`; and positivity of all iterates forces `g ≥ 0`. Proved in §1 here. Shared by all framings.

3. **Orbit-recurrence limit-at-infinity.** *Statement:* if `g(b) = β > 0` for some `b`, then `lim_{a→∞} g(a) = β`, by Dirichlet nearest-integer approximation of `a` by orbit points `b + mβ` within `β/2` and the master bound (giving `|g(a) − β| ≤ 9β²/(16a)`). Proved in §3 here. Consequence used downstream: every positive value of `g` equals `β`.
