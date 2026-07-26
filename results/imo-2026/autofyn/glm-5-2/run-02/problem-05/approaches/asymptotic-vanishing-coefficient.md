# asymptotic-vanishing-coefficient

## Status
partial

## Approaches tried
- (round 1) Crux-corpus route (adapt aimo-0234): write `f(x) = x + c + h(x)` with `h` a bounded error to be killed, plug into the squared GM inequality `(star)`, and send a free variable to infinity so the bounded error `h` is dominated and the coefficient it multiplies is forced to vanish, pinning `h equiv 0` (i.e. `g equiv c`). **Obstruction identified and flagged as the load-bearing gap (G-1): the constant-`c` residual `(x - y - c)^2` in `(star)` is non-negative and `~ x^2`-dominant at infinity, so it SWALLOWS the `h`-perturbation under the naive `x -> infty`. The approach's hard step is to find a normalization (likely differencing two orbit-shifted instances of `(star)`, or evaluating at the iterate-equality point `x = f(y)`) that cancels the leading `(x - y - c)^2` term and leaves `h` as the leading coefficient.** Fallback if G-1 proves fatal: reframe to the extremal-value / supremum self-amplification argument (adapt aimo-0787), which evaluates at a maximizer of `|h|` rather than sending a variable to infinity.

## Current best
The expansion of `(star)` around the candidate constant `c` (where `g(x) = c + h(x)`): `(star) = (x - y - c)^2 + h(x)(2(x + y + c) + h(x)) - 4 x h(y) >= 0`. The leading term `(x - y - c)^2 >= 0` is the constant-`c` residual (the AM-GM gap of `(x, f(y))` when `g equiv c`); it vanishes exactly at the iterate-equality point `x = f(y) = y + c + h(y)` (where it becomes `h(y)^2`). The `h`-perturbation appears linearly in `2(x + y + c) h(x) - 4 x h(y)`, the leading `h`-coefficient. Killing this coefficient at infinity pins `h equiv 0`. The gap is the isolation step.

## Proof plan (skeleton)

**Notation.** `g(x) := f(x) - x`, `g(x) >= 0`. Write `g(x) = c + h(x)` where `c >= 0` is a candidate constant (e.g. `c = g(x_*)` at some reference point, or `c = limsup g`, or `c = inf g`) and `h` is the deviation. Target: prove `h equiv 0` on `R_{>0}`, equivalently `g` constant.

### Step 0 — Existence (DONE, certified-able)
`f(x) = x + c`, `c >= 0`: both inequalities reduce to AM-GM / QM-AM on `(x, f(y))`. *(Knowledge_base: "Standard inequalities — AM-GM, QM-AM".)*

### Step 1 — Iterate + orbit + `g >= 0` (DONE, shared with the other approaches)
`x = f(y)` forces equality => `f(f(y)) = 2f(y) - y` => `g(f(y)) = g(y)` => `f^n(y) = y + n g(y)` (forward AP) => `g >= 0` (positivity) and `f` injective. Hence `h` is ALSO orbit-invariant: `h(f(y)) = g(f(y)) - c = g(y) - c = h(y)`. *(Knowledge_base: "Functional equations"; "Invariants & monovariants".)*

### Step 2 — The `g`-form of the GM inequality (DONE, algebra verified)
Squared RHS inequality: `(f(x) + y)^2 >= 4 x f(y)`. With `f = id + g`:
> **(star)** `4 x g(y) <= (x - y)^2 + 2(x + y) g(x) + g(x)^2` (all `x, y > 0`).

Constant-`c` residual: setting `g equiv c` makes `(star)` an identity `(x - y - c)^2 >= 0` (since `(x-y)^2 + 2(x+y)c + c^2 - 4 x c = (x-y-c)^2 = (x - f(y))^2 >= 0`, equality at `x = y + c = f(y)`). *(Knowledge_base: "SOS / completing the square"; "Standard inequalities — equality cases".)*

### Step 3 — Expand `(star)` around `g = c + h` (DONE)
Substitute `g(x) = c + h(x)`, `g(y) = c + h(y)` into `(star)`:
> **(star-h)** `(x - y - c)^2 + h(x) [2(x + y + c) + h(x)] - 4 x h(y) >= 0`.

Derivation: the `c`-part is `(x - y - c)^2`; the `h`-part is `2(x + y) h(x) + 2 c h(x) + h(x)^2 - 4 x h(y) = h(x)(2(x + y + c) + h(x)) - 4 x h(y)`. The leading `h`-coefficient is `2(x + y + c) h(x) - 4 x h(y) ~ 2 x h(x) - 4 x h(y) = 2 x (h(x) - 2 h(y))` for `x` large. (Builder to verify the expansion term-by-term.)

### Step 4 — Establish that `h` is bounded (GAP G-0 — prerequisite for the limit)
Before sending any variable to infinity, establish that `h` (equivalently `g`) is bounded on the relevant domain, so the limit argument is legitimate. **No continuity / measurability is known a priori.**

Candidate mechanism (shared with `gm-lipschitz-partition` Step 4): from the swap `(star star): 4 y g(x) <= (x - y)^2 + 2(x + y) g(y) + g(y)^2`, fix `y = a` (any reference point), let `x in [a, b]`: `g(x) <= ((x - a)^2 + 2(x + a) g(a) + g(a)^2) / (4 a) <= M([a, b])` finite. So `g`, hence `h = g - c`, is bounded on every compact `[a, b]`. For the limit argument we additionally need `g` bounded on a RAY `[a, infty)`: this is NOT automatic and is a genuine sub-gap.

**Gap G-0 (load-bearing prerequisite).** Prove `g` is bounded above on a ray (or on all of `R_{>0}`), or else restrict the limit argument to a regime where only compact boundedness is needed. Candidate: use the LHS (RMS) inequality in `g`-form, which gives an upper bound on `f(x)` of order `sqrt(2(x^2 + f(y)^2)) - y`; combined with `f >= id` this may bound `g` on rays. The explorer's regularity-route `(dagger)` gives `g(y) <= (y - x_0)^2 / (4 x_0)` (global, quadratic) IF a fixed point `x_0` exists — but this approach does NOT assume a fixed point. The builder must either (i) prove `g` bounded on rays from the raw inequalities, or (ii) design the limit in Step 5 to use only compact boundedness (e.g. send `x -> infty` along a sequence with `g(x)` known-bounded by the compact bound applied to growing compacts — but this requires `g` bounded on each compact `[a, X_n]`, which is already established, with bound `M([a, X_n]) ~ X_n^2 / (4a)` growing, NOT bounded). Flag: the compact bound GROWS with the interval, so it does NOT give a uniform bound on a ray. This is a real obstruction.

### Step 5 — Kill the `h`-coefficient by sending a variable to infinity (GAP G-1 — the load-bearing crux)
**The naive move (DOES NOT WORK as-is, flagged):** send `x -> infty` with `y` fixed in `(star-h)`. The leading term `(x - y - c)^2 ~ x^2` (positive, `O(x^2)`) dominates; the `h`-terms are `O(x)` (if `h` bounded). So the inequality is trivially satisfied for large `x` and yields no constraint on `h`. **This is the obstruction the crux-corpus explorer flagged:** "which variable to send to infinity and which squared inequality to use so the deviation survives as the leading term rather than being swallowed by the `x^2` term."

**Gap G-1 (the load-bearing crux).** Find a normalization / differencing that cancels the leading `(x - y - c)^2` term and leaves the `h`-coefficient `2 x h(x) - 4 x h(y)` as the leading term. Three candidates for the builder to attempt:
- **(G-1a) Difference of two orbit-shifted instances.** Evaluate `(star-h)` at `(x, y) = (f^n(s), t)` for fixed `s, t` and `n` large. Using orbit-invariance `h(f^n(s)) = h(s)` and `f^n(s) = s + n g(s) = s + n(c + h(s))`, the leading `(x - y - c)^2 = (s + n(c + h(s)) - y - c)^2 ~ n^2 (c + h(s))^2` grows. Difference this against `(star-h)` at `(x, y) = (f^n(s), f^n(s) - c)` (the iterate-equality partner) — the builder must check whether the `n^2` leading terms cancel, leaving an `n`-linear residual involving `h(s) - h(t)` that forces `h(s) = h(t)`. (Risk: this may reduce to a tautology, as the iterate-equality point gives `h(y)^2 >= 0`.)
- **(G-1b) Evaluate at the iterate-equality point `x = f(y)`.** Then `(x - y - c) = h(y)`, so `(x - y - c)^2 = h(y)^2`, and `h(x) = h(f(y)) = h(y)` (orbit-invariance). Plugging into `(star-h)`: `h(y)^2 + h(y)(2(f(y) + y + c) + h(y)) - 4 f(y) h(y) >= 0`. The builder simplifies (using `f(y) = y + c + h(y)`): this reduces to `0 >= 0` — a tautology. So the equality point gives nothing (as expected: `x = f(y)` is the AM-GM equality case). Not viable.
- **(G-1c) Reframe as extremal-value / supremum self-amplification (aimo-0787 port — the FALLBACK if G-1a fails).** Let `M = sup_{x > 0} h(x)` (could be `+ infty` if G-0 fails; assume G-0 gives `M < infty` for now). Take a sequence `x_n` with `h(x_n) -> M`. Evaluate `(star-h)` at `(x, y) = (x_n, y)` with `y` chosen so `h(y)` is small (e.g. `y` near a minimizer of `h`, or `y = x_n` itself — tautology). The builder must derive a self-referential inequality of the form `M <= M - (positive)` (the max reappears amplified by the `h(x)`-coefficient `2(x + y + c)`, which for large `x_n` exceeds the `4 x_n h(y)` term), forcing `M <= 0` and symmetrically `inf h >= 0`, hence `h equiv 0`. This is the genuine aimo-0234-adjacent move (the "bounded error killed by the leading coefficient at the extremal point") but adapted via aimo-0787's maximum-principle shape rather than a literal `x -> infty` limit.

### Step 6 — Conclusion
If G-1 closes (any of (a), (b), (c)): `h equiv 0`, so `g equiv c`, so `f(x) = x + c` with `c >= 0`. Existence: Step 0. **Final answer: `f(x) = x + c` for any constant `c >= 0`.**

## Key lemmas (claim + mechanism)
- `(star)` in `g`-form — because `(f(x) + y)^2 - 4 x f(y)` expands and collects to `(x - y)^2 + 2(x + y) g(x) + g(x)^2 - 4 x g(y)`.
- Constant-`c` residual `(x - y - c)^2` — because the `c`-part of `(star)` is `(x - y)^2 + 2(x + y)c + c^2 - 4 x c = (x - y - c)^2`, the squared AM-GM gap of `(x, y + c) = (x, f(y))`.
- `(star-h)` expansion — because substituting `g = c + h` and collecting by `h`-degree separates the constant residual from the linear-in-`h` coefficient `2(x + y + c) h(x) - 4 x h(y)`.
- Orbit-invariance of `h` — because `g(f(y)) = g(y)` (Step 1) and `c` is constant, so `h(f(y)) = g(f(y)) - c = g(y) - c = h(y)`.
- (G-0) boundedness of `g` — because `(star star)` at `y = a` bounds `g(x)` for `x in [a, b]` linearly in `g(a)`; a RAY bound needs the RMS side or a separate argument.
- (G-1) coefficient-vanishing — because the leading `(x - y - c)^2` is the AM-GM gap of the constant solution and must be canceled (by differencing orbit-shifted instances) or bypassed (by evaluating at the `h`-extremal point) to expose the `h`-coefficient `2 x h(x) - 4 x h(y)` whose vanishing pins `h equiv 0`.

## Open gaps
- **G-0** (Step 4): boundedness of `g` (hence `h`) on a RAY, not just on compacts. The compact bound `M([a, b]) ~ b^2 / (4a)` grows with `b`, so it is not a uniform ray bound. Without a ray bound, the `x -> infty` limit in Step 5 is illegitimate. Candidate: use the RMS inequality or the global quadratic bound from a fixed point (if one exists). This is the "exactly what boundedness the inequality itself supplies" gap the dispatch named.
- **G-1** (Step 5, the load-bearing crux): find the normalization that isolates `2 x h(x) - 4 x h(y)` as the leading term so its coefficient vanishes. Candidate (a) (differencing orbit-shifted instances) is the most faithful to aimo-0234 but may reduce to a tautology; candidate (c) (extremal-value / aimo-0787 reframing) is the fallback. The builder must report which candidate closes.
- **G-2** (Step 5): if G-1 closes via (c) (extremal value), the builder must establish that `M = sup h` is finite (G-0) AND attained or approximable, AND close the self-referential inequality `M <= M - (positive)` rigorously. Maximum-principle arguments on non-compact domains (here `R_{>0}`) require transport of the extremal point via the orbit-AP, which adds a layer.

## Cases to cover
- `h equiv 0` (`g equiv c`, the target): the argument's conclusion.
- `g equiv 0` (`c = 0`): covered (take `c = 0` as the candidate constant; `h = g`).
- Wild / non-measurable `g`: the extremal-value reframing (c) REQUIRES `sup h` to be approached by a sequence (no measurability needed, only the definition of sup), so it handles wild `g` IF G-0 supplies a finite `M`. The differencing approach (a) is purely algebraic and handles wild `g` directly.

## Watch out for
- The naive `x -> infty` move DOES NOT WORK: `(x - y - c)^2 ~ x^2` dominates and the inequality is trivially satisfied. Do not present a proof that sends `x -> infty` in `(star-h)` without first canceling the leading term.
- The iterate-equality point `x = f(y)` is a TAUTOLOGY in `(star-h)` (reduces to `0 >= 0`): the AM-GM equality case. Do not build a step on it.
- The orbit grows (`f^n(y) = y + n g(y) -> infty`), so any "send `n -> infty`" along the orbit makes bounds GROW, not shrink — the literal aimo-0710 positivity squeeze does not carry over (the crux-corpus explorer noted this). Do not attempt an orbit-telescoping squeeze.
- Do not assume `g` is continuous, differentiable, or measurable — the approach must work for wild `g` (or restrict to a class and handle the wild case via the algebraic differencing (a)).
- If G-1 proves fatal after the builder's attempt, this approach should be REVISED into the extremal-value framing (candidate (c)) as a new slug `extremal-self-amplification`, NOT abandoned — the aimo-0234 / aimo-0787 shape is genuinely distinct from the Lipschitz and the orbit-close-encounter framings.
