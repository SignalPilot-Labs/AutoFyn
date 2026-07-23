## Status
partial

## Approaches tried

- **Direct QM-AM-GM structural analysis + forced-equality substitution `x = f(y)`.**
  Not yet a full proof, but yielded a rigorously proven sub-lemma and, importantly,
  overturned the dispatch's working hypothesis that the answer is `f(x) = x` alone.
  See "Current best" below — this is genuine forward progress, not a dead end.

- **Guessed `f(x) = x` as the unique answer** (as suggested by the task framing).
  **Refuted.** Both an algebraic identity and a numerical check (20000+ random
  `(x,y)` trials, `python3`) show `f(x) = x + c` satisfies *both* inequalities
  simultaneously for **any constant `c ≥ 0`**, not just `c = 0`. So the answer is
  a one-parameter family, not a single function. Do not re-attempt "prove
  `f(x)=x`" as the target statement — the correct target is "prove `f(x) = x+c`,
  `c ≥ 0`, are exactly the solutions."

- **Tested other simple candidate families numerically** (`f(x)=kx` for `k≠1`,
  `f(x)=x^2`, `f(x)=sqrt(x)`): all **fail** the sandwich for generic `(x,y)` in
  `20000`-trial random checks (many violations, not just numerical noise). These
  are confirmed dead ends — no need to re-test scaling or power-law guesses.

- **Tested non-constant "shift" functions** `f(x) = x + c(x)` where `c(x)` is a
  step function (jump from `1` to `2` at `x=10`) or `x + sin(x) + 2` /
  `x + |sin(x)|` (always `f(x) > x` pointwise): all **fail** numerically with many
  violations. This supports (but does not yet prove) the conjecture that the
  "shift" `d(x) := f(x) - x` must be a **global constant**, not merely pointwise
  nonnegative.

## Current best

**Proven facts** (verified by hand, algebra double-checked with small numeric
sanity tests in `python3`; these are rigorous, not conjectural):

1. **The sandwich is QM(x, f(y)) ≥ AM's competitor ≥ GM(x, f(y)), but the middle
   term is *not* the actual AM(x, f(y))** — it's `(f(x)+y)/2`, which only
   coincides with `AM(x,f(y)) = (x+f(y))/2` when `f(x) - x = f(y) - y`. This is
   the structural crux of the whole problem: the inequality forces `(f(x)+y)/2`
   to live in the interval `[GM(x,f(y)), QM(x,f(y))]`, which always contains
   `AM(x,f(y))`, but is generally a **strictly wider** interval unless `x = f(y)`.

2. **Solution family exists beyond `f(x)=x`:** for any constant `c ≥ 0`,
   `f(x) = x + c` satisfies both inequalities for *all* `x,y > 0`. Proof: if
   `f(t) = t + c` for all `t`, then `f(x) + y = x + c + y = x + f(y)` identically,
   so `(f(x)+y)/2 = (x+f(y))/2 = AM(x, f(y))` exactly, and the required chain
   reduces to the *always-true* QM(x,f(y)) ≥ AM(x,f(y)) ≥ GM(x,f(y)) (ordinary
   QM-AM-GM for the two positive reals `x` and `f(y) = y+c`). Positivity of `f`
   on all of `R_{>0}` forces `c ≥ 0` (else `f(y) = y+c \le 0` for `y` near `0^+`
   when `c<0`). **Numerically confirmed** with `c = 1, 5, 100` — zero violations
   in `200000` random trials each, `lo=0.001, hi=1000`.
   ⇒ The conjectured final answer is **`f(x) = x + c` for an arbitrary constant
   `c ≥ 0`** (this includes `f(x)=x` as the `c=0` case). This is currently a
   verified-necessary-and-sufficient-looking family; the "these all work" direction
   is fully rigorous (proved above), the "these are the only solutions" direction
   is not yet proved.

3. **Forced-equality substitution `x = f(y)` (rigorous lemma).** Plug `x = f(y)`
   into the original chain. Since `x = f(y)`, we get `QM(x,f(y)) = QM(f(y),f(y))
   = f(y)` and `GM(x,f(y)) = GM(f(y),f(y)) = f(y)` — the two outer bounds
   collapse to the *same* value `f(y)`, because QM(a,a) = GM(a,a) = a for any
   `a>0`. This traps the middle term exactly: `f(y) ≥ (f(f(y))+y)/2 ≥ f(y)`,
   forcing equality throughout. Hence
   **`f(f(y)) = 2f(y) - y` for all `y > 0`.** (Fully proved — this is the
   "equality case of QM-AM-GM forces `x=f(y)`" idea the dispatch anticipated,
   and it is exactly the substitution that unlocks the problem, though the
   payoff is a functional equation, not directly `f(y)=y`.)

4. **Consequences of the lemma in (3), all proved:**
   - **Injectivity.** If `f(y₁)=f(y₂)`, apply (3) at both: `2f(y₁)-y₁ =
     f(f(y₁)) = f(f(y₂)) = 2f(y₂)-y₂`; since `f(y₁)=f(y₂)` this gives `y₁=y₂`.
     So `f` is injective.
   - **Orbit is an arithmetic progression.** Let `d(y) := f(y) - y`. From (3),
     `d(f(y)) = f(f(y)) - f(y) = (2f(y)-y) - f(y) = f(y)-y = d(y)`, i.e. `d` is
     invariant along the forward orbit of `y` under `f`. Writing `y_n := f^n(y)`
     (well-defined and positive for every `n ≥ 0` since `f: R_{>0}→R_{>0}`), the
     lemma gives `y_{n+2} = 2y_{n+1} - y_n` for all `n`, i.e. `(y_n)` is an
     arithmetic progression with common difference `d(y) = f(y)-y`:
     `y_n = y + n·d(y)`.
   - **`f(x) ≥ x` for all `x` (proved, not conjectured).** Since `y_n = y +
     n·d(y) > 0` must hold for *every* `n ≥ 0` (each `y_n` is a genuine element
     of `R_{>0}`), if `d(y) < 0` then `y_n → -∞`, contradicting positivity for
     large `n`. Hence `d(y) ≥ 0` for every `y`, i.e. **`f(x) ≥ x` on all of
     `R_{>0}`.**

**Gap-closing route found by the proof-outliner (round 2) — see the "Proof
outline" section below for the full write-up.** Summary: substitute
`x → f(x)` into the **GM inequality** (not the QM one) and use the already-proved
FE `f(f(x)) = 2f(x) - x` to eliminate `f(f(x))`. This produces a clean
"quadratic-defect" inequality `4f(x)(d(x)-d(y)) + (y-x)^2 ≥ 0` for **all**
`x,y > 0` (verified symbolically with `sympy`, exact identity, no approximation).
Applying this inequality along a fine partition of any interval `[a,b]` and
telescoping / letting the mesh `→ 0` (an Archimedean argument, no calculus
needed) forces `d(b) = d(a)` for **every** `a<b`. Combined with the already-proved
`d ≥ 0`, this gives the global constant `c ≥ 0` and finishes the necessity
direction. This route needs only the two facts already proved above (the FE and
`f(x) ≥ x`) — it does **not** need injectivity or the orbit-AP fact, so the
dependency chain is short.

## Proof outline (proof-outliner, round 2)

Spec review: required

Technique: **Direct/constructive characterization proof**, in two directions
(necessity via a forced functional equation + a monotone-defect/telescoping
squeeze; sufficiency via a direct algebraic identity reducing to the classical
QM-AM-GM inequality). The spine of the necessity direction is: (i) a
forced-equality substitution to extract an exact functional equation (already
done, see Current best facts 3–4), then (ii) a **second, different**
substitution into the inequality pair that yields a *quadratic-defect
inequality* bounding `d(x)-d(y) := (f(x)-x)-(f(y)-y)` by `O((y-x)^2)`, then
(iii) a **telescoping/Archimedean squeeze** (partition `[a,b]` into `N` pieces,
sum the local bound, let `N→∞`) that forces `d` to be globally constant. This
last step is the "cheap kill" for the whole gap: it avoids any
continuity/monotonicity/Cauchy-equation machinery — it is pure algebra plus the
Archimedean property of `R`.

Notation: write the two inequalities from the problem as
- **(QM-ineq)**: `2(x^2 + f(y)^2) ≥ (f(x)+y)^2` for all `x,y ∈ R_{>0}` (squares
  of the left `≥` middle part of the chain; valid since both sides are
  manifestly `≥ 0`),
- **(GM-ineq)**: `(f(x)+y)^2 ≥ 4x f(y)` for all `x,y ∈ R_{>0}` (squares of the
  middle `≥` right part; valid since `f(x)+y > 0`).

and `d(t) := f(t) - t` for `t ∈ R_{>0}`.

### Skeleton

1. **(Already proved in Current best, fact 3 — re-verify the derivation is
   legitimate.)** Fix `y0 ∈ R_{>0}` and substitute `x := f(y0)` (a valid
   positive real, since `f: R_{>0}→R_{>0}`) into the *original three-term
   chain* `sqrt((x^2+f(y)^2)/2) ≥ (f(x)+y)/2 ≥ sqrt(xf(y))`. **This is a direct
   computation, not an appeal to "QM(a,b)=GM(a,b) ⟹ a=b" for a general pair**:
   with `x=f(y0)`, both outer expressions collapse *by direct evaluation*,
   because they are QM and GM of the *same value repeated twice*:
   `sqrt((f(y0)^2+f(y0)^2)/2) = sqrt(f(y0)^2) = f(y0)` and
   `sqrt(f(y0)·f(y0)) = f(y0)`. So the chain reads
   `f(y0) ≥ (f(f(y0))+y0)/2 ≥ f(y0)`, forcing equality:
   **`f(f(y)) = 2f(y) - y` for all `y ∈ R_{>0}`.** (FE) — this re-derivation
   confirms the step in the existing "Current best" is valid; no fix needed.
2. **(Already proved, fact 4, third bullet.)** `f(x) ≥ x` for all `x ∈
   R_{>0}` — via the orbit `y_n = y + n·d(y)` (from (FE)) staying positive for
   all `n ≥ 0`, forcing `d(y) ≥ 0`.
3. **(NEW — key lemma, the gap-closer.)** Derive the **quadratic-defect
   inequality**: for all `x,y ∈ R_{>0}`,
   `4 f(x) (d(x) - d(y)) + (y-x)^2 ≥ 0`.  — (E)
   *Mechanism:* take (GM-ineq) and substitute `x → f(x)` (valid, `f(x) ∈
   R_{>0}`): `(f(f(x))+y)^2 ≥ 4 f(x) f(y)`. Replace `f(f(x))` by `2f(x)-x`
   using (FE) from step 1: `(2f(x)-x+y)^2 ≥ 4f(x)f(y)`. Expand and substitute
   `f(x) = x+d(x)`, `f(y) = y+d(y)`; the expansion collapses *exactly* to (E)
   (algebra confirmed symbolically — expanding `(2f(x)-x+y)^2 - 4f(x)f(y)` and
   `4f(x)(d(x)-d(y))+(y-x)^2` in terms of `x,y,d(x),d(y)` gives the identical
   polynomial, difference `= 0`). This uses only step 1's (FE); it does **not**
   need injectivity or the orbit-AP fact.
4. **(NEW — the finishing squeeze.)** Fix arbitrary `a<b` in `R_{>0}`. For
   each positive integer `N`, set `Δ = (b-a)/N` and `x_i = a+iΔ`,
   `i=0,\dots,N` (so `x_0=a`, `x_N=b`). Apply (E) to consecutive pairs:
   - with `x`-slot `=x_i`, `y`-slot `=x_{i+1}`: `d(x_{i+1})-d(x_i) ≤
     Δ^2/(4f(x_i))`;
   - with `x`-slot `=x_{i+1}`, `y`-slot `=x_i`: `d(x_i)-d(x_{i+1}) ≤
     Δ^2/(4f(x_{i+1}))`.
   By step 2, `f(x_i) ≥ x_i ≥ a` and `f(x_{i+1}) ≥ x_{i+1} ≥ a` (all `x_i ∈
   [a,b]`), so **both** local bounds are `≤ Δ^2/(4a)`. Summing the first
   family telescopically over `i=0,\dots,N-1` gives `d(b)-d(a) ≤ N·Δ^2/(4a) =
   (b-a)^2/(4aN)`; summing the second gives `d(a)-d(b) ≤ (b-a)^2/(4aN)`. Both
   bounds hold for **every** `N`, and `(b-a)^2/(4aN) → 0` as `N → ∞` while
   `d(b)-d(a)` is a fixed real number — so both `d(b)-d(a) ≤ 0` and `d(a)-d(b)
   ≤ 0`, forcing **`d(a) = d(b)`**. Since `a<b` were arbitrary, `d` is
   constant on all of `R_{>0}`: `d(x) ≡ c` for some `c ∈ R`. By step 2, `c ≥
   0`. Hence **`f(x) = x + c` for all `x`, some constant `c ≥ 0`.** This
   closes the necessity direction.
5. **(Sufficiency — already proved, fact 2; restate as the construction half
   of the answer.)** For any `c ≥ 0`, check `f(x) = x+c` satisfies the
   original chain for all `x,y>0`: since `f(x)+y = x+c+y = x+f(y)` identically,
   the middle term `(f(x)+y)/2` equals `AM(x,f(y)) = (x+f(y))/2` *exactly*, so
   the required chain `QM(x,f(y)) ≥ (f(x)+y)/2 ≥ GM(x,f(y))` becomes the
   *classical* QM-AM-GM inequality for the two positive reals `x` and `f(y) =
   y+c` (positive because `c ≥ 0` and `y>0`), which is always true (KB:
   "Standard inequalities: AM-GM ... equality cases"). Also check `c ≥ 0` is
   *necessary just for `f` to map into `R_{>0}`*: if `c<0`, taking `x < -c`
   (possible since `x` ranges over all of `R_{>0}`) gives `f(x) = x+c \le 0
   \notin R_{>0}`, contradiction — an independent, one-line confirmation of
   `c ≥ 0` that cross-checks step 4's conclusion.
6. **Conclude.** The complete solution set is
   **`{ f : R_{>0}→R_{>0} \mid f(x) = x+c \text{ for all } x, \text{ for some
   constant } c ≥ 0 }`.**
   State this explicitly as the final answer (per CLAUDE.md's "Verify final
   answers" rule) and note both directions (steps 1–4 = necessity /
   upper-bound-on-solution-set direction; step 5 = sufficiency /
   construction direction) are covered, as required for a "determine all
   functions" problem.

### Key lemmas (claim + mechanism)

- **(FE) `f(f(y)) = 2f(y)-y`** — because substituting `x=f(y)` makes both the
  QM and GM outer terms of the original chain literally equal to `f(y)` (QM
  and GM of a value repeated twice are trivially that value), sandwiching the
  middle term into forced equality. (Already proved; re-verified here as
  legitimate.)
- **`f(x) ≥ x`** — because the forward orbit `y_n = y+n·d(y)` generated by
  iterating (FE) must stay in `R_{>0}` for every `n≥0`; a negative common
  difference `d(y)<0` would eventually make `y_n<0`. (Already proved.)
- **(E) `4f(x)(d(x)-d(y)) + (y-x)^2 ≥ 0`** — because substituting `x→f(x)`
  into the GM-inequality and eliminating `f(f(x))` via (FE) turns a
  *product/GM-type* inequality into a *quadratic form in `d(x)-d(y)`*; this is
  the algebraic mechanism that converts the qualitative fact `d≥0` into a
  quantitative *local* bound on how much `d` can vary between two points, with
  the bound shrinking like `(y-x)^2` (i.e. `d` behaves like a function with
  "zero derivative" in a difference-quotient sense, without assuming
  continuity).
- **`d(a)=d(b)` for all `a<b`** — because summing the local bound (E) over a
  fine partition of `[a,b]` telescopes to a bound `≤ (b-a)^2/(4aN)` on
  `d(b)-d(a)` (and symmetrically on `d(a)-d(b)`) that is valid for *every*
  partition size `N` and tends to `0`; a fixed real number bounded above by a
  sequence `→0` must be `≤0` (Archimedean property of `R`), giving both
  inequalities and hence equality. This is the actual crux of the whole "why
  is `d` a global constant" question — it is *not* a continuity or
  monotonicity argument but a direct quantitative squeeze.
- **Sufficiency identity `f(x)+y = x+f(y)` for `f(x)=x+c`** — because
  `f(t)=t+c` is an *additive shift*, so `f(x)+y` and `x+f(y)` are both
  literally `x+y+c`; this collapses the required 3-term sandwich to the
  textbook QM-AM-GM inequality for `(x, f(y))`, which needs no further work.

### Cases to cover

None beyond the two directions (necessity / sufficiency) — there is no
casework in `x` or `y`; the argument in step 4 is uniform over all `a<b ∈
R_{>0}`. The only "case" is `c=0` vs `c>0`, but both are handled uniformly by
`c ≥ 0` throughout (no special sub-case needed; `f(x)=x` is just `c=0`).

### Watch out for (anticipated gaps the builder must not skip)

- **Domain of validity of the partition argument (step 4):** all `x_i ∈
  [a,b] ⊂ R_{>0}`, so `f(x_i)` and `f(x_i) ≥ x_i ≥ a > 0` are legitimate
  applications of step 2 — no issue at the left endpoint since `a>0` strictly
  (the domain excludes `0`).
- **Do not conflate (E) with the earlier "QM=GM forces `x=f(y)`" special
  substitution** — (E) comes from a *different* substitution (`x→f(x)` in the
  GM-inequality, using (FE) to simplify), not from re-doing step 1. Keep the
  two derivations clearly separate in the write-up so the reviewer can check
  each independently.
- **State explicitly that (E) requires only (FE), not injectivity** — this
  keeps the logical dependency graph small and avoids the builder wasting
  effort re-proving or re-invoking injectivity/orbit-AP facts that are not
  needed for the necessity conclusion (they're independently true and can be
  mentioned as auxiliary corollaries of (FE), but are not on the critical
  path).
- **Sufficiency direction must be written out algebraically** (not just
  "clearly satisfies") per CLAUDE.md's no-hand-waving rule: show `f(x)+y =
  x+f(y)` as an identity, invoke the *named* QM-AM-GM theorem from
  `knowledge_base.md`, and separately verify `c≥0` is required for `f` to map
  into `R_{>0}` (this closes the loop that `c<0` is excluded both by step 4's
  proof and by the domain/codomain constraint, which is a good consistency
  check to include in the final write-up).
- **Final answer statement:** per CLAUDE.md, state the answer explicitly:
  `f(x) = x+c` for `x ∈ R_{>0}`, for an arbitrary but fixed real constant `c ≥
  0`. Do not just say "these all work" — write the full characterization
  (`iff`) explicitly and note both directions are proved.
- **Double-check inequality labeling.** `(QM-ineq)` (the left `≥` middle part
  of the chain) is used only in step 1 (via the `x=f(y)` substitution done
  there implicitly through the full chain) — it is not needed again for steps
  3–4, which use only `(GM-ineq)`. Confirm the builder does not need to
  re-derive anything from `(QM-ineq)` beyond step 1; everything past that
  point rides on `(GM-ineq)` + `(FE)`.

---

## Full proof

(none yet — see Current best and the Proof outline above for the proved
sub-lemmas and the closed gap; the necessity direction now has a complete
outlined argument (steps 1–4 above, with all algebra verified symbolically),
and the sufficiency direction is already fully proved (step 5 / Current best
fact 2). What remains is for the proof-builder to write up steps 3–4 as a
fully rigorous, prose proof — with careful epsilon/N bookkeeping in step 4 —
and assemble all six steps into the final `results/imo-2026-05.md` "Full
proof" section.)

---

### Notes for the outliner (knowledge base / crux corpus / technique)

**Knowledge-base entries to use** (`knowledge_base.md`):
- *"Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases
  pin down the extremal configuration."* — directly the mechanism in step 3
  above (QM(a,a)=GM(a,a)=a forces equality when `x=f(y)`).
- *"Functional equations: test special values, check injectivity/surjectivity."*
  — used for the `x=f(y)` substitution and the resulting injectivity proof.
- Pólya heuristics *"Specialize"* / *"Introduce a substitution / change of
  variables"* — exactly how the `x=f(y)` move and the `d(y)=f(y)-y` change of
  variable were found.
- *"Meta-Strategy: Always check small cases first..."* — the numerical
  `python3` sweep is what caught the `f(x)=x+c` family (a case the dispatch's
  framing missed).

**Crux corpus (algebra domain, `functional-equations` and
`inequalities-SOS-and-convexity` subtopics, per `crux_moves_documentation.md`
field names `technique`/`how_used`/`domain`/`subtopic`):**
- Searched `past_crux_moves_database.json` (772 algebra cruxes) for
  AM-GM/sandwich/equality-case techniques. No problem in the corpus has the
  same two-sided QM/AM/GM-sandwich-of-a-functional-value structure. The
  closest thematic matches, neither a strong structural analog:
  - `aimo-0761` (ISL 2017 A8 flavor): "For every `x,y` with
    `(f(x)+y)(f(y)+x)>0`, `f(x)+y=f(y)+x`; prove `f(x)+y ≤ f(y)+x` when `x>y`."
    Uses the substitution `g(x) = x - f(x)` (our `d(x) = f(x)-x` up to sign) and
    a long order/interval argument to force `g` non-decreasing. **Relevant
    inspiration** for the "prove `d(x)` is constant/monotone" gap above, but
    the hypothesis structure (an implication over all reals, no positivity
    constraint) is different enough that its machinery cannot be transplanted
    directly — treat as a hint for the *style* of argument (compare `x+y`
    against `g(x)`), not a template to copy.
  - `aimo-0008` (Bulgaria, `f(x)f(y)≥f(xy)`, `f(x+y)≥f(x)+f(y)`, `f(a)=a` for
    some rational `a>1` `⟹ f(x)=x` everywhere): crux move is *"sandwiching
    against a known exact value at a large point, splitting that point
    additively and letting the superadditive inequality force each summand to
    be tight."* Thematically about forcing equality via a sandwich, but the
    hypotheses (multiplicative + superadditive on `Q_{>0}`) are unrelated to
    our QM/GM sandwich. Weak analogy only — mainly useful as a reminder that
    "equality-forcing via a sandwich at a cleverly chosen point" is a proven
    winning pattern in this corpus.
  - No problem found with the specific `sqrt((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥
    sqrt(xf(y))` shape or anything close; this appears to be a genuinely novel
    (2026) construction for the corpus. **Verdict: no strongly analogous crux
    exists — do not force a match.**

**Cheap-kill / pruning notes:**
- `x=f(y)` substitution is the single highest-value cheap move (one line,
  yields the exact functional equation `f(f(y))=2f(y)-y`, plus injectivity for
  free). Do this first.
- The orbit-positivity argument (`f(x) ≥ x` globally) is another cheap,
  fully rigorous consequence — worth stating as a lemma before attacking the
  harder "d is globally constant" step.
- Symmetric substitution `y = f(x)` was checked and gives **no new
  information** — it only reproduces the trivial identities `2(x-F)^2 ≥ 0` and
  `(F-x)^2 ≥ 0` (where `F=f(x)`), already implied by the `f(f(y))=2f(y)-y`
  lemma. Do not spend outline budget re-deriving from this substitution.
- Setting `x=y` also gives no new information: the middle term becomes exactly
  `AM(x,f(x))`, so the chain is just the trivial QM-AM-GM fact for the pair
  `(x,f(x))`. Confirmed by direct computation — dead end, skip.

**Small-case / intuition notes (labeled as conjecture except where proved
above):**
- Conjectured final answer: **`f(x) = x + c` for any real constant `c ≥ 0`**
  (this is the full solution set — a one-parameter family, not just the
  identity). The `c ≥ 0` restriction and the "sufficiency" direction are
  proved; "these are the only solutions" is conjectural, strongly supported by
  numeric falsification of every other tested family (scalings, powers,
  non-constant shifts).
- The numeric check script pattern (for the outliner/builder to reuse if
  useful for sanity-checking any proposed characterization):
  `python3 -c "import random, math; ... check f against
  sqrt((x**2+f(y)**2)/2) >= (f(x)+y)/2 >= sqrt(x*f(y)) over random (x,y) in
  (0.001,1000)"` — cheap way to falsify wrong guesses before investing in a
  written proof.
