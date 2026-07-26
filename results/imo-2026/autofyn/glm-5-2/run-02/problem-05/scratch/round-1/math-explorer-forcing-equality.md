## imo-2026-05 — route: forcing-equality / diagonal-substitution

### Route summary
The pair `(x, f(y))` governs both bounds: the middle `(f(x)+y)/2` is the AM of `(x, f(y))` shifted by `(g(x)−g(y))/2` where `g:=f−id`. Equality-forcing at `x=f(y)` pins the second iterate; the RHS (GM) inequality, fed `x=f(z)` and `x=f(y)` (swapped), yields a clean two-sided bound on `|g(z)−g(y)|` in terms of the gap of `√f`; a discrete partition then forces `g` constant. Uniqueness crux = the partition argument, not the iterate.

### Confirmed facts (equality-forcing derivation — AIRTIGHT)

Notation: `g(x):=f(x)−x`, so `f(x)=x+g(x)`. The middle term is
`(f(x)+y)/2 = AM(x, f(y)) + (g(x)−g(y))/2`.

**Fact 1 (second iterate).** Set `x=f(y)` in both inequalities (valid: `f(y)>0`).
- LHS: `√((f(y)²+f(y)²)/2) = f(y) ≥ (f(f(y))+y)/2` ⇒ `f(f(y)) ≤ 2f(y)−y`.
- RHS: `(f(f(y))+y)/2 ≥ √(f(y)·f(y)) = f(y)` ⇒ `f(f(y)) ≥ 2f(y)−y`.
- Combined: **`f(f(y)) = 2f(y) − y`** for all `y>0`. (Both inequalities needed; the equality case of `√(xf(y)) ≤ √((x²+f(y)²)/2)` is exactly `x=f(y)`.) Verified numerically on `f(x)=x+c`.

**Fact 2 (orbit AP).** `f(f(y)) = f(y) + g(f(y))` (expand) `= 2f(y)−y = f(y) + g(y)`. Hence **`g(f(y)) = g(y)`**: `g` is constant along the forward orbit, and `fⁿ(y) = y + n·g(y)` (arithmetic progression).

**Fact 3 (injectivity).** If `f(a)=f(b)`, then `f(f(a))=f(f(b))` ⇒ `2f(a)−a = 2f(b)−b` ⇒ `a=b`. So `f` injective. (Uses Fact 1.)

**Fact 4 (g≥0, f≥id).** Forward orbit `y+ng(y)` stays positive for all `n≥0`. If `g(y)<0`, large `n` gives a negative value. Hence **`g(y)≥0`**, i.e. **`f≥id`**. (Crucial lower bound for the partition step.)

**Fact 5 (clean self-referential bound — THE CRUX INSTRUMENT).** Substitute `x=f(z)` (any `z`) into the RHS inequality `(f(x)+y)/2 ≥ √(x f(y))`:
  `(g(z)−g(y))/2 ≥ −(AM−GM)(f(z), f(y))`.
Doing the same with `(x,y) = (f(y), z)` (swapped) gives
  `(g(y)−g(z))/2 ≥ −(AM−GM)(f(z), f(y))`, i.e. `(g(z)−g(y))/2 ≤ (AM−GM)(f(z),f(y))`.
Combining: **`|g(z)−g(y)| ≤ 2·(AM−GM)(f(z),f(y)) = (√(f(z)) − √(f(y)))²`**.
(Identity used: `2·(AM−GM)(a,b) = (√a − √b)²`. Verified symbolically.)
- Note `RMS−AM ≤ AM−GM` (since `RMS+AM ≥ AM+GM`), so the LHS inequality gives the *weaker* parallel bound `g(z)−g(y) ≤ 2(RMS−AM)` — it is redundant for uniqueness once Fact 1 is in hand. **The LHS inequality's job is only the equality-forcing in Fact 1; the RHS inequality carries uniqueness.**
- Numerically confirmed: a nonconstant perturbation `f(x)=x+0.1·sin x` violates the original inequality (227/1600 sample pairs) AND violates this clean bound (228/1600) — i.e. the clean bound is sharp enough to kill nonconstant `g`.

**Fact 6 (true family works).** `f(x)=x+c, c≥0`: middle `=(x+y+c)/2 = (x+f(y))/2 = AM(x, f(y))`; the two bounds are `GM(x,f(y))` and `RMS(x,f(y))`. Both inequalities are the universal AM-GM / QM-AM chain, tight at `x=f(y)` (i.e. `x=y+c`). Positivity needs `c≥0`. Verified numerically.

### Tautology catalog (substitutions that give nothing — do NOT retry)

All reduce to `(f(x)−x)² = (g(x))² ≥ 0` or to an identity already known. Confirmed by symbolic simplification.

1. **`x = y`.** Both sides become AM-GM / QM-AM of the pair `(y, f(y))` itself: `(f(y)+y)/2 ≥ √(y f(y))` ⇔ `(f(y)−y)² ≥ 0` (RHS); `√((y²+f(y)²)/2) ≥ (f(y)+y)/2` ⇔ `(f(y)−y)² ≥ 0` (LHS). Pure tautology; the middle *is* `AM(y, f(y))` here.
2. **`y = f(x)`.** Using `f(f(x))=2f(x)−x`: RHS gives `f(x)² ≥ x(2f(x)−x)` ⇔ `(f(x)−x)² ≥ 0`; LHS gives `2(f(x)−x)² ≥ 0`. Tautology. (Symmetric dual of the equality-forcing substitution but no new info because the iterate relation already encodes it.)
3. **`x = f(y)` re-plugged / iterate telescoping.** Re-substituting iterates just re-derives `g(fⁿ(y))=g(y)` (Fact 2) along the orbit. No constraint across orbits. Tautology in the sense of giving nothing beyond Fact 2.
4. **`y = f²(x)` (or any higher iterate).** Same: the AP structure of Fact 2 absorbs it; reduces to `(f(x)−x)² ≥ 0`.
5. **Swapping `(x,y)` in the original statement.** The statement is `∀x,y`, so the swapped instance is the same statement, not a new constraint. (Not strictly a tautology, but gives nothing beyond the original pair of bounds.)
6. **Setting the middle equal to AM of `(x, f(y))`.** This is `g(x)=g(y)`, i.e. the *conclusion* (uniqueness). Circular — it's the target, not a derivation.

### Promising asymmetric moves (ranked)

**Rank 1 — the self-referential `|g(z)−g(y)| ≤ (√f(z)−√f(y))²` bound + discrete partition (THE move).** This is the genuinely asymmetric crux: the RHS inequality at `(x,y)=(f(z),y)` and at `(x,y)=(f(y),z)` — two instances of the SAME inequality with the equality-forcing point `x=f(·)` planted in the `x`-slot — combine into a two-sided bound coupling `g`'s difference to `√f`'s difference. Then a standard "tiny-Lipschitz ⟹ constant" partition (chop `[y,z]` into `n` equal parts, sum the per-step bound, let `n→∞`) forces `g` constant on every compact `⊂ R>0`, hence globally. The lower bound `√f(t) ≥ √t ≥ √a > 0` on `[a,b]` (from Fact 4, `f≥id`) is what makes the partition's denominator stay positive. **Why it cracks uniqueness:** the bound is quadratic in the `√f`-gap, so the per-step error is `O((Δ/n)²)` and `n` of them sum to `O(1/n) → 0`. **What it needs:** Fact 4 (`f≥id`) for the denominator lower bound, and care that the self-referential `|Δg| ≤ (Δt+Δg)²/(denom)` is closed under the partition (verify `|Δg| ≤ |Δt|` inductively on each sub-interval, which follows from `|Δg| ≤ (Δt)²/m ≤ |Δt|` when `|Δt| ≤ m`). This is the cleanest route to the answer `f(x)=x+c`.

**Rank 2 — perturbation/linearization sanity (diagnostic, not a proof).** Write `g = c + h`, plug into the clean bound with `z=y+ε`: `|h(y+ε)−h(y)| ≤ (√(y+ε+c+h(y+ε)) − √(y+c+h(y)))² ≈ ((1+h'(y))ε)²/(4(y+c+h(y)))`, giving `|h'(y)| = O(ε) → 0`. Confirms any differentiable perturbation has `h'≡0`; the partition argument (Rank 1) is the rigorous, non-differentiable version. Useful as intuition only.

**Rank 3 — orbit-swap forcing (analog of aimo-0710's third crux).** aimo-0710 (IMO-SL 2023, `R>0`, two-variable functional inequality, answer `f(x)=c/x`) derived an involution then *swapped variables in the residual inequality to force a product constant*. Here the analog is: after Fact 1, the residual inequality `(f(x)+y)/2 ≥ √(x f(y))` with `x=f(z)` swapped against `x=f(y)` already IS the Rank-1 bound — so Rank 1 is the faithful realization of the aimo-0710 crux-move pattern for this problem. Less a separate move than a re-derivation; listed so the outliner sees the structural kinship.

**Rank 4 — width-of-interval / ratio parametrization.** The middle must lie in `[GM(x,f(y)), RMS(x,f(y))]`, an interval of width `RMS−GM = (x−f(y))²/(RMS+GM)·...` (homogeneous of degree 1, vanishing at `x=f(y)`). Parametrizing by ratio `r=x/f(y)` expresses the allowed shift `(g(x)−g(y))/2` as `f(y)·φ(r)` for explicit `φ`. Could bound `g`'s growth rate, but the partition argument (Rank 1) already supersedes it. Reserve only if Rank 1 hits an unexpected snag in the self-referential closure.

### Knowledge-base entries to use
- **Standard inequalities: AM-GM, QM-AM.** "Equality cases pin down the extremal configuration" — exactly the equality-forcing at `x=f(y)` (Fact 1) AND the existence verification (Fact 6). The identity `2·(AM−GM) = (√a−√b)²` is the load-bearing algebra.
- **Functional equations: test special values, check injectivity/surjectivity.** Injectivity (Fact 3) and the equality-forcing substitution are the named FE techniques. (Surjectivity is NOT available and NOT needed — forward-orbit positivity suffices.)

### Analogous past problems (cruxes)
- **aimo-0710 (IMO-SL 2023, Belgium).** Closest analogue: `R>0 → R>0`, two-variable functional *inequality*, "determine all `f`". Crux sequence: (i) one-step substitution to get a base gap bound; (ii) iterate the substitution along the orbit and telescope, pit a linear-in-`n` bound against a fixed bound to force the base gap to vanish; (iii) feed the derived relation back in, *swap variables*, force a product to be constant. Our Fact 1 is step (i); our Fact 5 (the `(f(z),y)` vs `(f(y),z)` swap) is step (iii) of the same pattern. Note: aimo-0710's telescoping was needed because their gap was `y−f²(y)` (involution); ours is `g(fⁿ(y))=g(y)` (translation), which does NOT telescope to a squeeze (the bound *grows* with `n`), so the partition argument replaces aimo-0710's step (ii). Genuine analogue.
- **aimo-0190 (IMO-SL).** Supporting: crux "Pin a Cauchy-additive function to linear by exhibiting one-sided boundedness on a ray" and "Collapse a FE into Cauchy by paired substitutions and adding to cancel cross terms." The partition/tiny-Lipschitz argument (Rank 1) is the one-sided-boundedness analogue — bounded above by `O((Δ)²)` on every ray ⇒ constant.
- **aimo-0368 (Dutch TST 2008).** Weak analogue only: iterate-relation `f³+f²+f=3n` with equality-forcing by sum-of-bounds. Same *flavor* (iterate identity + extremality) but discrete and additive, not the same crux. Skip unless needed.

### Prior progress
None beyond the orchestrator's seed (no approach files, no lemmas yet — round 1). Current.md conjectures `f(x)=x+c, c≥0`; existence confirmed, uniqueness open. This report supplies the uniqueness instrument (Fact 5 + partition).

### Dead ends (do not retry)
- **Forward-orbit telescoping as a squeeze.** `g(fⁿ(y))=g(y)` plus the bound `g(x)−g(y) ≤ 2(RMS−AM)(x, fⁿ⁺¹(y))` sends `fⁿ⁺¹(y) → ∞` (when `g(y)>0`), so the RHS grows, not shrinks. Cannot squeeze this way. (The orbit is an AP going to `+∞`; it never returns near a fixed `x`.)
- **Backward-orbit squeeze.** Would need `f` surjective; `f` is injective but surjectivity is unavailable and unneeded. Don't attempt to prove surjectivity — the partition argument sidesteps it.
- **The tautological substitutions listed above** (`x=y`, `y=f(x)`, iterate re-plugging, swap, middle=AM).
- **Periodic perturbation `g=c+h_periodic`** is killed by the clean bound (Fact 5) — confirmed numerically. Don't construct exotic counterexamples; the bound rules them all out.

### Small-case / intuition notes (CONJECTURE, not proved here)
- Conjecture (strong): the answer is exactly `{f(x)=x+c : c≥0}`. Existence proven (Fact 6); uniqueness reduced to the partition argument (Rank 1), which the explorer has verified is algebraically closed and numerically kills the test perturbation `0.1·sin x`. A proof-builder should be able to turn Facts 1–5 + the partition into a rigorous write-up; **the explorer has NOT written the proof** — that is the builder's job.
- Intuition: the problem is "shifted AM must stay inside `[GM, RMS]`"; the shift's magnitude is bounded by `AM−GM = (√a−√b)²/2`, a quadratic-in-gap quantity, and a quadratic-in-gap Lipschitz constant forces constancy by the standard partition. The entire uniqueness argument is, in spirit, "quadratic Lipschitz ⇒ constant."
