# outline-reviewer — IMO 2026 P5 (round 1)

## Verdicts

### `orbit-close-encounter` — CHANGES REQUESTED (the leader; build)

**Technique sound?** Yes. The algebraic/orbit-AP framing is the right route: `(star)` is a genuine cross-level-set constraint (verified: `(f(x)+y)^2 - 4 x f(y)` expands exactly to `(x-y)^2 + 2(x+y)g(x) + g(x)^2 - 4 x g(y)`), the close-encounter contradiction is the correct uniqueness mechanism, and it handles wild `g` purely algebraically (no continuity/measurability).

**Step (A) — `g` takes at most one positive value — SOUND.** Verified numerically: a wild `g` taking two positive values `c_a < c_b` on two forward APs violates `(star)` at a close encounter (`4 t (c_b - c_a) <= (5/4) c_a^2` contradicts `t -> infty`). The close-encounter lemma (G-A1) is standard and correct:
- Irrational ratio `p/q`: Kronecker/Weyl equidistribution gives `<= epsilon`-close meetings at unbounded `t`. Sound.
- Rational ratio `p/q = P/Q`: `d = gcd(c_a, c_b) <= c_a`. Distinct residue classes mod `d` (same class = collision = `c_a = c_b`, excluded) have minimal line-distance `delta <= d/2 <= c_a/2`, achieved periodically at unbounded `t`. So `epsilon = c_a/2` is always attainable. **The outliner's worry "distinct residue classes must not collide" is already handled: they don't (distinct classes), and `delta <= c_a/2` holds because `d <= c_a`.** G-A1 is closeable as written; the builder just needs to state the `d <= c_a` step.
- Orientation (G-A2): verified — `(star)` puts `g(y)` on the LHS (`4 x g(y)`), so to get the binding `4 t c_b <= ... + 4 t c_a` we set `y = B_m in L_{c_b}`, `x = A_n in L_{c_a}`. The swapped direction is trivially true. Correct as the outline has it.

**Step (B) — fixed point forces `g equiv 0` — has a REAL algebraic flaw in the entirely-above subcase, but is REPAIRABLE.** The flaw:
- The straddle subcase gives `c >= 16 x_0` cleanly (orbit point within `c/2` of `x_0`, `(dagger)` => `c <= (c/2)^2/(4 x_0)` => `c >= 16 x_0`). Sound.
- The entirely-above subcase derivation `c <= (a-x_0)^2/(4 x_0) <= (c-x_0)^2/(4 x_0)` (giving `(c/x_0)^2 - 6(c/x_0) + 1 >= 0`, root `3+2sqrt2`) is **invalid**: the second inequality requires `a <= c`, but `a` is the orbit seed and `a - x_0` can be arbitrarily large relative to `c` (backward propagation is NOT available — `f` is not surjective). So the `3+2sqrt2` lower bound is unjustified.
- Consequently G-B2's geometric growth factor `3+2sqrt2` is wrong as derived.

**The repair (the builder must implement this):** Once (A) gives `g in {0, c}`, the cover iteration does NOT need the `3+2sqrt2` lower bound at all. From `(dagger)` and (A): where `(y-x_0)^2/(4 x_0) < c`, i.e. `|y - x_0| < 2 sqrt(c x_0)`, we have `g(y) < c`, hence `g(y) = 0` (by (A)). So the zero-region around `x_0` has radius `2 sqrt(c x_0)` (NOT `2(sqrt2+1) x_0`). Pick a new fixed point `x_1` near the right end `x_0 + 2 sqrt(c x_0)`; iterate. The right endpoint satisfies `x_{k+1} = x_k + 2 sqrt(c x_k)`, which diverges (`x_k ~ c k^2`, **quadratic** growth, not geometric). I verified numerically (c=0.5, x_0=1: right endpoint reaches ~200 in 20 steps, diverging). `bigcup_k (0, x_k) = R_{>0}`, so `g equiv 0`. This works for ANY `c > 0`, with no lower bound needed. **G-B1 and G-B2 collapse into a single, simpler step: zero-region radius `2 sqrt(c x_0)` + quadratic cover growth.** Abandon the `3+2sqrt2` / `16 x_0` straddle-vs-entirely-above detour entirely.

**One more point the builder must verify in (B):** the cover iteration must start from a fixed point. If no fixed point exists, then `g > 0` everywhere (by (A), `g equiv c > 0`), which is the `f(x) = x + c` family — no (B) needed. (B) only runs when a fixed point exists, which is exactly the mixed `{0, c}` case to exclude. This case split is implicit and the builder should state it.

**Also note:** even without the cover iteration, the FULL `(star)` forbids the entirely-above mixed case directly — at a near-orbit point `x` with `g(x) = 0` and orbit point `y` with `g(y) = c`, `(star)` reads `4 x c <= (x - y)^2`, violated when `x` is close to `y` (verified numerically: x=9.9, y=10, c=0.5 gives LHS=19.8 > RHS=0.01). This is an alternative (B) route the builder may use; the cover iteration is cleaner.

### `gm-lipschitz-partition` — CHANGES REQUESTED (build, but the builder must PIVOT off the partition path)

**Fact 5 is a real, verified instrument:** `|g(z) - g(y)| <= (sqrt(f(z)) - sqrt(f(y)))^2` follows rigorously from the RHS inequality at `x = f(z)` and `x = f(y)` plus the iterate identity. Worth certifying as a lemma.

**The partition path (Step 5) is DOOMED as a standalone uniqueness route — G1 is not closeable with Fact 5 alone, and the original inequality does NOT save it.** I verified:
- The quadratic self-bound `u_i <= (h + u_i)^2/(4a)` has two branches: small (`u_i <= ~h^2/(4a)`) and large (`u_i >= ~4a`). Fact 5 alone permits the large branch.
- The proposed rescue (invoke the original `(star)` at a near-jump pair) does NOT yield a contradiction: at `|x - y| = h -> 0` with `g(y) - g(x) ~ 4a`, `(star)` reduces to `16 a x <= (g(x) - h)^2 ~ g(x)^2`, i.e. `g(x) >= 4 sqrt(a x)` — **satisfied, not contradicted**, when `g` is large. So a single large jump is self-consistent with the original inequality.
- Globally, the large branch corresponds to `g` taking (at least) two values differing by `~4a`. Ruling that out is exactly step (A) of `orbit-close-encounter`. So G1's closure REQUIRES importing (A) (and then (B) for the `{0, c}` mixed case). The partition via Fact 5 adds nothing to uniqueness once (A)+(B) are in hand.

**Diversity concern (flag for the orchestrator):** once the builder imports (A)+(B) to close G1, this approach is `orbit-close-encounter` with a redundant Fact 5. The two are not genuinely distinct framings — they share the (A)+(B) wall. The Fact 5 instrument can prove (A) via a different route (Fact 5 + close-encounter: at a close encounter of two orbits, `|c_1 - c_2| <= (c_1 - c_2)^2/(4 y)` => `4 y <= |c_1 - c_2|`, contradiction as `y -> infty`), which is a real alternative to the direct `(star)` proof of (A). But the (B) step is identical. So this is "one framing, two instruments for (A)", not two framings.

**Builder instructions:**
1. Abandon the partition-to-constancy path (Step 5 as written). It cannot close.
2. Use Fact 5 to prove (A) via the Fact-5+close-encounter route (sketched above), OR simply import (A) from `orbit-close-encounter`'s builder.
3. Use the cover iteration (zero-region radius `2 sqrt(c x_0)`, quadratic growth) for (B), same as `orbit-close-encounter`.
4. Propose Fact 5 for lemma certification — it is a real, importable derived inequality.

### `asymptotic-vanishing-coefficient` — RETHINK (do not build)

**Fatal flaw: the technique cannot prove this problem as outlined.** The core move (write `g = c + h`, send a variable to infinity, kill the `h`-coefficient `2 x h(x) - 4 x h(y)`) is structurally thwarted because the constant-`c` residual `(x - y - c)^2` is the AM-GM gap of the constant solution — it is non-negative and `~ x^2`-dominant at infinity, swallowing the `O(x)` `h`-perturbation. I verified ALL three candidate closures fail:
- **(G-1b) iterate-equality point `x = f(y)`:** TAUTOLOGY (`0 >= 0`). Verified by substitution using `h(f(y)) = h(y)` (orbit-invariance). The outline already flags this; confirmed.
- **(G-1c) extremal-value / orbit-shift of the maximizer:** ALSO TAUTOLOGY. If `y` is the orbit-predecessor of `x_n` (so `f(y) = x_n`, `h(y) = h(x_n) = M`), then `(x_n - y - c) = h(y) = M` and the whole expression collapses to `0 >= 0` by the same algebra as (b). If `y` is NOT orbit-related to `x_n`, the square `(x_n - y - c)^2` is large and dominates — no constraint on `h`. So (c) either reduces to (b) (tautology) or is dominated (no info).
- **(G-1a) differencing orbit-shifted instances:** the `n^2 (c + h(s))^2` leading term grows; canceling it requires the iterate-equality partner, which is the tautological (b). So (a) reduces to (b).

**The LHS (RMS) inequality does NOT help:** I verified its constant-`c` residual is ALSO `(x - y - c)^2` (same leading term), so switching sides doesn't escape the obstruction.

**G-0 (boundedness on a ray) is also a real, separate obstruction:** the compact bound `M([a,b]) ~ b^2/(4a)` grows with `b`, so there is no uniform ray bound from `(star star)` alone; without a fixed point the global quadratic bound is unavailable. The extremal-value reframe needs `sup h < infty`, which G-0 does not supply.

This is not a fixable gap — it is the wrong technique. The inequality is structurally a perturbed AM-GM identity whose perturbation is invisible both at infinity (swallowed by `x^2`) and at the equality point (cancels to `0`). Send back to the outliner for a fundamental reframe. The outliner's contingency (`extremal-self-amplification` as a new slug) would need a genuinely different gap functional — NOT a leading-coefficient-vanishing argument on either the GM or RMS side, both of which have the same `(x - y - c)^2` leading term.

## Diversity assessment

The field has effectively collapsed to ONE framing: orbit-AP + close-encounter (for (A)) + cover-iteration (for (B)). `gm-lipschitz-partition` and `orbit-close-encounter` share the (A)+(B) wall and differ only in the (A) instrument (Fact 5 vs direct `(star)`); `asymptotic-vanishing-coefficient` is a different framing but is doomed. **Next round, the outliner should propose >=1 approach attacking (B) — the shared wall — from a genuinely different framing** (e.g., a proof of "fixed point => `g equiv 0`" that avoids the cover iteration, or a route that avoids close-encounter entirely, perhaps via the LHS/RMS side in a non-leading-coefficient way, or a transport argument along backward iterates if any can be salvaged).

## Build set

`orbit-close-encounter` (repair (B) per the `2 sqrt(c x_0)` zero-region + quadratic cover growth; close G-A1 with the `d <= c_a` step; abandon the `3+2sqrt2` detour). `gm-lipschitz-partition` (certify Fact 5 as a lemma; abandon the partition path; use Fact 5 + close-encounter for (A) and the cover iteration for (B)). One builder each. Both builders should propose the shared `iterate-and-orbit` preamble lemma for certification if not yet filed.

build set: orbit-close-encounter, gm-lipschitz-partition
