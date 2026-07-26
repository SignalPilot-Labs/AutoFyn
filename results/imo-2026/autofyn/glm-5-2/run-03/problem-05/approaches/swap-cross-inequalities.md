# swap-cross-inequalities — imo-2026-05

## Status
partial

## Approaches tried
- (Round 1) Attempted the full route: (a) derive the off-diagonal cross-inequalities `2x·f(y) <= y² + f(x)²` and `2y·f(x) <= x² + f(y)²` non-circularly via the interval-intersection logic of the two swapped sandwiches; (b) squeeze `g := f − id` to a constant from them (with the cheap kill `(C1)+(C2)` as auxiliary). Outcome:
  - **Gap (a) — CLOSED, non-circular.** The cross-inequalities are derived cleanly from the single fact that the original middle term `A = (f(x)+y)/2` lies in the GM–QM interval `I₁` of the pair `(x, f(y))` (this is the hypothesis) AND in the GM–QM interval `I₂` of the pair `(y, f(x))` (this is the *universal* QM–AM–GM chain, true for all positive reals, no hypothesis on `f` beyond `f > 0`). From `A ∈ I₁ ∩ I₂` one reads off `G₁ ≤ Q₂` and `G₂ ≤ Q₁`, i.e. exactly the two cross-inequalities. No circularity: the bound used is `A ≤ Q₂`, which is QM ≥ AM on the pair `(y, f(x))` — a universal inequality — NOT the swapped left hypothesis (which the outline-reviewer correctly flagged as circular). See Lemma 1 below.
  - **Gap (b) — DEAD ENDED.** The cross-inequalities do NOT force `g` constant. Three independent obstructions, each verified:
    1. **Orbit amplification of the single cross-inequality** `2x·f(y) <= y² + f(x)²` on the two forward orbits `x = a + n·d₁`, `y = b + m·d₂` (carrying `g = d₁, d₂` by (C1)) has degree-2 leading term `(n·d₁ − m·d₂)² ≥ 0` (verified symbolically) — a perfect square, i.e. asymptotic AM-GM. The bound is saturated at leading order, so no growth contradiction.
    2. **Orbit amplification of the summed cross-inequality** has degree-2 leading term `2(n·d₁ − m·d₂)² ≥ 0` (verified) — again AM-GM level, no contradiction.
    3. **Local squeeze.** Writing the cross-inequality as a pointwise two-sided bound on `g(x) − g(y)`,
       `(L)  2·√(y·f(x)) − √(2·(x² + f(y)²))  ≤  g(x) − g(y)  ≤  √(2·(y² + f(x)²)) − 2·√(x·f(y))  (U)`,
       the bound has slack `g(y)²/(2y)` (resp. `g(x)²/(2x)`) at points where `g > 0`. So at a **zero** of `g` one recovers the local quadratic bound `g(x) ≤ (x−b)²/(2b)` (the same local control the master bound `(★)` gives — see Lemma 2), but at a **nonzero** point the slack is a *positive constant* and the bound yields only boundedness, not a squeeze to zero. The two-sided bound therefore cannot force continuity at nonzero points, and hence cannot force `g` constant.
    4. **Structural reason.** The cross-inequality bound on `g(x) − g(y)` has **no amplifying linear factor**: its LHS is the constant `g(x) − g(y)` and its RHS tends back to `g(x) − g(y)` as one moves out on orbits (the slack is `O(1/Y) → 0`). Contrast the master bound `(★)` `|g(x)−g(y)|·(2x+2y+g(x)+g(y)) ≤ (x−y−g(y))²`, whose LHS carries the **linearly growing** factor `2x+2y+…` while the RHS stays bounded — that growing factor is what makes `(★)`'s orbit amplification yield a contradiction. The cross-inequalities lack it, so they are strictly **weaker** than `(★)` and cannot substitute for it.
  - Conclusion of this round: the cross-inequality *derivation* is a genuine lemma (Lemma 1), but the framing cannot close the constancy-of-`g` gap. The route is `partial`, not `solved`. If a later round wants to revive this framing, it must import an *external* amplifying mechanism (the master bound `(★)`, or continuity) — at which point the framing collapses into `diagonal-diophantine-kill` / `lipschitz-connectedness`. The genuinely-new contribution of this approach is therefore Lemma 1 alone.

## Current best
**Lemma 1 (cross-inequalities, proven non-circularly).** For every `f : R_{>0} → R_{>0}` satisfying the problem's inequalities and every `x, y > 0`,
`2x·f(y) ≤ y² + f(x)²`  and  `2y·f(x) ≤ x² + f(y)²`.

Mechanism: `A := (f(x)+y)/2` is the AM of the pair `(y, f(x))`, so by the **QM–AM–GM chain** (knowledge-base "Standard inequalities") `A ∈ [√(y·f(x)), √((y²+f(x)²)/2)] =: I₂` *unconditionally*; and the problem's left+right inequalities place `A ∈ [√(x·f(y)), √((x²+f(y)²)/2)] =: I₁`. Hence `A ∈ I₁ ∩ I₂`, so the two intervals intersect. For two real intervals `[a₁, b₁], [a₂, b₂]` to intersect, one needs `a₁ ≤ b₂` and `a₂ ≤ b₁`. Applying this: `√(x·f(y)) ≤ √((y²+f(x)²)/2)` (i.e. `2x·f(y) ≤ y² + f(x)²`) and `√(y·f(x)) ≤ √((x²+f(y)²)/2)` (i.e. `2y·f(x) ≤ x² + f(y)²`). Non-circular because the upper bound `A ≤ √((y²+f(x)²)/2)` used here is the *universal* QM ≥ AM on `(y, f(x))`, not the swapped left hypothesis.

**Open gap (gap b, dead-ended).** The cross-inequalities are too weak to force `g := f − id` constant: orbit amplification is asymptotically an AM-GM-level identity (perfect-square leading term), and the local two-sided bound squeezes only at zeros of `g` (recovering the `(★)`-at-a-zero local bound `g(x) ≤ (x−b)²/(2b)`) but not at nonzero points. The bound lacks the amplifying linear factor that makes the master bound `(★)` work, so it is strictly weaker. Recorded so no later round re-attempts the pure cross-inequality forcing.

## Full proof
Not present: the approach reaches a non-circular lemma (Lemma 1) but does not close the constancy of `g`, so it does not solve the problem. The full solution must pass through an amplifying mechanism (the master bound `(★)`, or continuity + connectedness) — see the `diagonal-diophantine-kill` and `lipschitz-connectedness` approaches.

---

### Lemma 1 (cross-inequalities) — full proof

**Setup.** Let `f : R_{>0} → R_{>0}` satisfy, for all `x, y > 0`,
`(L) √((x² + f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y))  (R).`
Fix `x, y > 0` and define
`A := (f(x) + y)/2,   B := (f(y) + x)/2,`
`G₁ := √(x·f(y)),   Q₁ := √((x² + f(y)²)/2),   G₂ := √(y·f(x)),   Q₂ := √((y² + f(x)²)/2).`

**Step 1 — `A` is the AM of the pair `(y, f(x))`.** By definition `A = (f(x) + y)/2`, the arithmetic mean of the two positive numbers `y` and `f(x)`.

**Step 2 — universal placement `A ∈ I₂ := [G₂, Q₂]`.** The **QM–AM–GM chain** (knowledge_base: "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal configuration") applied to the pair `(y, f(x))` of positive reals gives
`G₂ = √(y·f(x)) ≤ (y + f(x))/2 = A ≤ √((y² + f(x)²)/2) = Q₂,`
i.e. `A ∈ I₂`. This uses only `y > 0, f(x) > 0` (the latter from the codomain) and standard inequalities; it is independent of the hypothesis on `f`.

**Step 3 — hypothesis placement `A ∈ I₁ := [G₁, Q₁]`.** The problem's inequalities (L) and (R) read exactly `G₁ ≤ A ≤ Q₁`, i.e. `A ∈ I₁`.

**Step 4 — interval intersection forces the cross-inequalities.** From Steps 2–3, `A ∈ I₁ ∩ I₂`, so `I₁ ∩ I₂ ≠ ∅`. For two compact real intervals `[a₁, b₁]` and `[a₂, b₂]`, nonemptiness of the intersection is equivalent to `max(a₁, a₂) ≤ min(b₁, b₂)`; in particular it implies `a₁ ≤ b₂` and `a₂ ≤ b₁`. (Indeed `a₁ ≤ A ≤ b₂` and `a₂ ≤ A ≤ b₁` directly, since the single point `A` witnesses the intersection.) Applying `a₁ = G₁, b₂ = Q₂` (i.e. `G₁ ≤ A` and `A ≤ Q₂`):
`G₁ ≤ Q₂  ⟺  √(x·f(y)) ≤ √((y² + f(x)²)/2)  ⟺  2x·f(y) ≤ y² + f(x)².   (I)`
Applying `a₂ = G₂, b₁ = Q₁` (i.e. `G₂ ≤ A` and `A ≤ Q₁`):
`G₂ ≤ Q₁  ⟺  √(y·f(x)) ≤ √((x² + f(y)²)/2)  ⟺  2y·f(x) ≤ x² + f(y)².   (II)`
This is the pair of off-diagonal cross-inequalities. ∎ (Lemma 1)

**Non-circularity check (the outline-reviewer's flag).** The reviewer observed that deriving `(I)` from the *swapped left hypothesis* `(f(y)+x)² ≤ 2(y² + f(x)²)` is circular: that hypothesis expands to `2x·f(y) ≤ 2y² + 2f(x)² − f(y)² − x²`, which is *weaker* than `(I)`, and closing the gap between the two would require `f(x)² − x² ≥ f(y)² − y²` for all `x, y` — i.e. `f(t)² − t²` constant, the conclusion in disguise. The derivation above does **not** use the swapped left hypothesis. It uses `A ≤ Q₂`, which is the *universal* QM ≥ AM inequality on the pair `(y, f(x))` (true for all positive `y, f(x)`, no hypothesis on `f`), combined with the original right hypothesis `G₁ ≤ A`. The single point `A` lying simultaneously below `Q₂` (universal) and above `G₁` (hypothesis) forces `G₁ ≤ Q₂`. No ordering of two lower bounds is invoked, so the "two lower bounds on one quantity" fallacy (flagged dead in the explorer report) is avoided.

---

### Lemma 2 (local control at a zero) — what the cross-inequalities DO give

Assume the shared cheap kill `(C1) f(f(y)) = 2f(y) − y` (from specializing `x = f(y)`, the interval-collapse / QM=AM=GM equality case) and `(C2) g(y) := f(y) − y ≥ 0` (from positivity of all forward iterates `fⁿ(y) = y + n·g(y)`); see the explorer report for the free derivation.

**Claim.** If `g(b) = 0` (i.e. `f(b) = b`), then for all `x > 0`,
`g(x) ≤ (x − b)² / (2b).`

**Proof.** The cross-inequality `(II)` `2y·f(x) ≤ x² + f(y)²` with `y = b`, `f(y) = f(b) = b` reads
`2b·f(x) ≤ x² + b²,   i.e.   2b(x + g(x)) ≤ x² + b²,`
`2b·g(x) ≤ x² − 2bx + b² = (x − b)²,`
`g(x) ≤ (x − b)² / (2b).` ∎

This is precisely the local quadratic decay at a zero that the master bound `(★)` also yields (set `y = b` in `(★)`: `g(x)·(2x + 2b + g(x)) ≤ (x − b)²`, which implies `g(x) ≤ (x−b)²/(2b+2x+g(x)) ≤ (x−b)²/(2b)`). So at zeros the cross-inequalities recover exactly the `(★)`-at-a-zero bound — and no more.

**Why this does not extend to nonzero points.** At a point `a` with `g(a) = α > 0`, the cross-inequality `(II)` with `y = a` gives
`2a·g(x) ≤ (x − a)² + g(a)² = (x−a)² + α²`
(from `2a·f(x) ≤ x² + f(a)² = x² + (a + α)² = x² + a² + 2aα + α²`, i.e. `2a(x + g(x)) ≤ x² + a² + 2aα + α²`, i.e. `2a·g(x) ≤ (x−a)² + α²`). As `x → a` the RHS tends to `α² > 0`, so the bound reads `g(x) ≤ α + α²/(2a)` near `a` — local **boundedness**, not continuity, and not a squeeze to `α`. The slack `α²/(2a)` is a positive constant; it does not vanish. Hence the cross-inequalities cannot prove continuity at nonzero points, and the connectedness argument (approach `lipschitz-connectedness`) cannot be mounted from them.

---

### Why the orbit amplification fails (gap (b), the dead end)

Suppose `g` is not constant. By `(C2)` `g ≥ 0`; pick `a, b` with `0 ≤ d₁ := g(a) < d₂ := g(b)`. By `(C1)`-invariance, the orbit points `x = a + n·d₁` (carrying `g = d₁`, `f(x) = x + d₁ = a + (n+1)d₁`) and `y = b + m·d₂` (carrying `g = d₂`, `f(y) = y + d₂ = b + (m+1)d₂`) are admissible for all `n, m ≥ 0`.

**Single cross-inequality `(I)` `2x·f(y) ≤ y² + f(x)²` on orbits.** With the substitutions above the slack `y² + f(x)² − 2x·f(y)` expands (verified by direct symbolic expansion) to a polynomial in `n, m` whose **degree-2 part** is
`d₁²·n² − 2·d₁·d₂·n·m + d₂²·m² = (n·d₁ − m·d₂)² ≥ 0.`
So at leading (quadratic) order the slack is a perfect square — exactly AM-GM strength. The cross-inequality is saturated at leading order and cannot produce a growth contradiction (the leading term does not become negative along any sequence).

**Summed cross-inequality `2x·f(y) + 2y·f(x) ≤ x² + y² + f(x)² + f(y)²` on orbits.** The slack expands (verified symbolically) to a polynomial whose degree-2 part is
`2·(n·d₁ − m·d₂)² ≥ 0,`
again a perfect square (twice one). No growth contradiction.

Equivalently, the degree-2 part of either slack is `≥ 0` for *all* `(n, m)`, so the cross-inequality is at AM-GM level on orbits: it cannot be violated asymptotically by any choice of `(n, m)`. Compare with the master bound `(★)`, whose orbit form has a LHS growing *linearly* in `n, m` (the factor `2x + 2y + g(x) + g(y) ~ 2n·d₁ + 2m·d₂`) against a *bounded* RHS `(a − b + n·d₁ − (m+1)·d₂)²`, which is arranged to stay bounded by Kronecker / exact-lattice choice of `(n, m)`. The cross-inequality has **no such linearly growing factor**: its "LHS vs RHS" structure is `const ≤ const + O(1/Y)`, with the slack tending to zero — an asymptotic identity, not a contradiction.

**Structural diagnosis.** The cross-inequality `2x·f(y) ≤ y² + f(x)²` is the AM-GM of the pair `(y, f(x))` *with one entry replaced* — it is the "GM of `(x, f(y))` ≤ QM of `(y, f(x))`" cross term, and on orbits both pairs are arithmetic progressions, so asymptotically the inequality is exactly AM-GM. It carries no off-diagonal linear amplification. Therefore the pure cross-inequality framing **cannot** close the constancy of `g`: one must bring in an amplifying mechanism external to the four QM/AM/GM bounds — i.e. the master bound `(★)` (whose linear factor is the amplification) or a continuity/connectedness argument (which the cross-inequalities cannot power at nonzero points).

---

### Construction (shared, verified)

For `f(x) = x + c`, `c ≥ 0`:
- middle term `A = (x + y + c)/2` is the AM of the pair `(x, y + c)`;
- (L) is **QM ≥ AM** on `(x, y + c)`: `√((x² + (y+c)²)/2) ≥ (x + y + c)/2`;
- (R) is **AM ≥ GM** on `(x, y + c)`: `(x + y + c)/2 ≥ √(x·(y+c))`;
both hold for `x > 0, y + c > 0`, i.e. `c ≥ 0` (and `c < 0` violates the codomain `f(x) > 0` for small `x`).
Verified.

The cross-inequalities are also satisfied by the construction (as they must be, since the construction satisfies the original hypotheses): `2x(y+c) ≤ y² + (x+c)²` reduces to `0 ≤ (x−y)² + c²` ✓, and symmetrically.

---

### Verdict

The framing delivers a **non-circular Lemma 1** (the cross-inequalities, derived from the interval intersection of the hypothesis interval `I₁` and the universal QM–AM–GM interval `I₂`) and **Lemma 2** (local quadratic control at zeros, recovering the `(★)`-at-a-zero bound). It does **not** deliver the constancy of `g`: gap (b) is a genuine dead end (orbit amplification is asymptotically an AM-GM-level identity; the local two-sided bound squeezes only at zeros). The approach is `partial`. To solve the problem one must import an amplifying mechanism — the master bound `(★)` (→ `diagonal-diophantine-kill`) or continuity + connectedness (→ `lipschitz-connectedness`) — at which point the cross-inequality framing is subsumed. Lemma 1 is offered for certification as a reusable lemma.

## Promotable lemmas
- **Lemma 1 (cross-inequalities).** For every `f : R_{>0} → R_{>0}` satisfying the problem's inequalities and all `x, y > 0`: `2x·f(y) ≤ y² + f(x)²` and `2y·f(x) ≤ x² + f(y)²`. Proven non-circularly above (the bound used is the *universal* QM ≥ AM on the pair `(y, f(x))`, not the swapped left hypothesis). Candidate for `results/imo-2026-05/lemmas/cross-inequalities.md`. Note: this lemma is a *consequence* of the hypotheses but, as shown in this approach, is by itself too weak to force `g` constant; it is reusable as a derived inequality, not as a substitute for the master bound `(★)`.
