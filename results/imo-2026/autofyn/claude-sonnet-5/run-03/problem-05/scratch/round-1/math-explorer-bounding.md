## imo-2026-05 (lens: bounding / monotonicity / growth-rate)

- Distinct openings:
  1. **Exact sandwich substitution x=f(y)** (clean, rigorous, no asymptotics needed): plugging
     `(x,y) = (f(y), y)` into the ORIGINAL double inequality collapses both the QM bound and the
     GM bound to the same value `f(y)`, forcing the middle term to equal `f(y)` exactly. This
     yields the **exact functional equation `f(f(y)) = 2f(y) - y` for all y>0** — proved, no gap.
     (See derivation below.) This is the natural "iterate x -> f(x) -> f(f(x))" opening from this
     lens, but it needs no limiting/growth argument at all — it's a one-line sandwich.
  2. **Orbit/arithmetic-progression growth opening**: from `f(f(y))=2f(y)-y`, set `g(y)=f(y)-y`.
     Then `g(f(y))=g(y)` (g is invariant along the forward orbit of y under f), and the forward
     orbit `a_n = f^n(y)` is an *exact* arithmetic progression `a_n = y + n·g(y)`. Since all `a_n`
     must stay positive for all `n≥0` (codomain is `R_{>0}`), the common difference must satisfy
     `g(y) ≥ 0` — i.e. **f(y) ≥ y for every y**, forced purely by a positivity/boundedness-of-orbit
     argument (no analysis needed, just "an AP with negative common difference eventually goes
     negative").
  3. **Growth-rate / asymptotic cross-comparison of two orbits** (attempted, inconclusive so far —
     flagged as the live gap): to show `g` is not just constant along each single orbit but
     **globally** constant, I tried comparing the orbits of two different base points `x,y` (with
     possibly different constants `p=g(x)`, `q=g(y)`) via the original inequality applied at
     `(f^{n}(x), f^{n}(y))` type pairs and letting `n→∞`. At *leading order* both the GM inequality
     and the QM inequality degenerate to plain AM-GM / QM-AM in `p,q` (`p+q ≥ 2√(pq)` and
     `(p+q)² ≤ 2(p²+q²)`), which hold automatically for **any** `p,q≥0` — so leading-order
     asymptotics alone do **not** force `p=q`. A finer (subleading, or differently-scaled index)
     comparison is needed; this is the crux gap to close.
  4. **Direct two-point test (cheap, already run, informative)**: numerically checked whether two
     *specific* points `x0,y0` can carry different constants `c1≠c2` (i.e. `f(x0)=x0+c1`,
     `f(y0)=y0+c2`) and still satisfy the original inequality at both `(x0,y0)` and `(y0,x0)`.
     **Found a numeric example where this succeeds** (`x0≈6.72, y0≈42.37, c1≈7.64, c2≈2.55`) — so
     a naive single-pair (or even single-pair-plus-swap) substitution is *not* enough to rule out
     mixed constants; global constancy of `g` needs the full "for all x,y" quantifier, not two
     points. This is an important warning for the outliner: don't rely on a two-point trick alone.

- **Central finding (important, changes the expected answer)**: the candidate answer is **not**
  simply `f(x)=x`. I verified **exactly** (via `sympy.factor`, not just numerically) that for
  `f(x) = x + c` with any constant `c`, both
  `2x² + 2f(y)² - (f(x)+y)²` and `(f(x)+y)² - 4x·f(y)`
  equal the **same** expression `(x - y - c)²`, which is always `≥ 0`. So **every** function
  `f(x) = x + c` with `c ≥ 0` satisfies the problem's double inequality for *all* `x,y>0` (need
  `c≥0` so that `f(y)=y+c>0` holds even as `y→0+`). `c=0` recovers `f(x)=x`; `c>0` gives new valid
  solutions that the "QM-AM-GM pattern-matching to f(x)=x" instinct misses. **The likely final
  answer is the one-parameter family `f(x) = x + c`, `c ≥ 0`** (still needs a full uniqueness
  proof — see gap above). This should be treated as the leading conjecture, not `f(x)=x` alone.
  Verified with a direct random-pair Monte Carlo scan too (200k trials, `c ∈ {0,0.5,1,2,5}`, no
  violation found).

- Candidate technique(s): iterate-substitution to collapse the inequality to an exact identity
  (opening 1); orbit/AP positivity argument (opening 2, classic "iterate x→f(x)→f(f(x)) growth
  bound" from this lens); telescoping-sum-forces-vanishing arguments (see crux aimo-0710 below)
  adapted from "single bounded orbit forces increments to 0" to "two orbits' asymptotic gap
  forces their slopes to match" — likely the right shape for closing gap 3.

- Cheap-kill candidates: the two-point mixed-constant test (opening 4) is a fast sanity check but
  is NOT by itself a proof technique — it failed to rule out mixed constants on its own, so don't
  present it as a finished kill; it is useful only as a warm-up / sanity probe. No other cheap
  parity/pigeonhole kill is applicable here — this is a real-valued functional inequality problem,
  not combinatorial.

- Knowledge-base entries to use: **"Functional equations: test special values, check
  injectivity/surjectivity"** (general algebra entry) — used for opening 1. **"Standard
  inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur. Equality cases pin down the extremal
  configuration"** — the whole problem IS a QM-AM-GM sandwich in disguise; equality-case analysis
  (opening 1) is exactly this KB entry in action. No other KB entry (linear algebra, NT, geometry)
  is relevant.

- Analogous past problems (cruxes): filtered `algebra` domain, `functional-equations` subtopic
  (263 cruxes total) for inequality/monotonicity/iteration techniques.
  - **`aimo-0710`** (IMO 2016 P5, essentially the sister problem: same domain `R_{>0}->R_{>0}`,
    inequality `x(f(x)+f(y)) ≥ (f(f(x))+y)f(y)`, answer `f(x)=c/x`). **Very strong analogy** —
    same shape of problem (two-variable functional *inequality* on `R_{>0}`, answer a one-parameter
    family, solved by (a) substituting to get an iterate inequality `f^n(y) ≥ f^{n+2}(y)`, then
    (b) **telescoping a sum of nonnegative differences, each individually bounded below by a fixed
    quantity `c₀=y-f²(y)≥0`, against an a-priori upper bound (`y-f^{2m}(y) < y`, using positivity
    of `f`) to force `c₀=0` as `m→∞`**, collapsing the inequality to an exact identity `f²=id`,
    then a final "xf(x) is constant" argument. **This telescoping trick (bound each term below by
    a candidate positive constant, sum m of them, compare to a fixed upper bound, let m→∞ to force
    the constant to 0) is the crux move most likely to adapt to closing our gap 3** — but note the
    target here is different: in aimo-0710 the telescoping forces a quantity to *vanish*
    (`f²=id`); in our problem we instead need it to force a quantity to be *globally constant*
    (not zero), so the adaptation needs a comparison between two orbits' slopes, not a single
    orbit against 0.
  - **`aimo-0399`** (real-valued FE `f(x+y) ≤ y f(x)+f(f(x))`, prove `f(x)=0` for `x≤0`) — uses
    "apply the derived bound twice with roles interchanged and add to cancel a composite term" and
    "drive a free variable to a limit against a linear bound to force a sign" — same *flavor* of
    two-substitution-then-add trick, worth having in mind for gap 3, but the domain (`R`, not
    `R_{>0}`) and target (a sign statement, not full characterization) make it a looser analogy
    than `aimo-0710`.
  - `aimo-1022` (order-implication self-composition, sandwiching an iterate between two of its
    own further iterates) is a weaker tertiary analogy — same "iterate-then-sandwich" flavor but
    for an equality-based FE, not inequality-based; lower priority than the above two.

- Prior progress: none (round 1, fresh problem; `results/imo-2026-05/current.md` is empty/unsolved,
  `sample_approaches` returned 0 approaches).

- Dead ends (do not retry): none recorded yet (nothing has been tried by other agents this round).
  My own dead-end note: leading-order asymptotic comparison of two orbits (opening 3, naive
  version) does NOT by itself force `g` constant — don't re-attempt the *naive* leading-order
  version without a refinement (subleading terms, or a differently-scaled/shifted comparison of
  indices `n` vs `n+k`).

- Small-case / intuition notes (labeled as conjecture where not fully proved):
  - **Proved rigorously**: `f(f(y)) = 2f(y) - y` for all `y>0` (via the exact sandwich
    substitution `x=f(y)`).
  - **Proved rigorously**: `f(y) ≥ y` for all `y>0` (via positivity of the induced arithmetic
    orbit `a_n = y + n(f(y)-y)`, which must stay positive as `n→∞`).
  - **Proved rigorously (exact SOS identity)**: `f(x)=x+c` satisfies the double inequality for
    every `x,y>0`, for any real `c`, with equality iff `x-y=c`; combined with the codomain
    constraint this means every `c ≥ 0` gives a valid solution.
  - **Conjectured** (strong numeric + partial-algebraic support, not yet proved): these
    `f(x)=x+c, c≥0` are the *only* solutions — i.e. `g(y):=f(y)-y` is forced to be one single
    global nonnegative constant. This is the outstanding gap. A naive two-point substitution does
    NOT resolve it (counterexample pair found numerically), so the eventual proof will likely need
    either (a) a global argument via monotonicity of `f` (not yet established — worth checking
    whether monotonicity itself is forced, e.g. via injectivity from `f(f(y))=2f(y)-y` making `f`
    injective — if `f(y1)=f(y2)` then `2f(y1)-y1 = 2f(y2)-y2 ⟹ y1=y2`, so **f is injective**, a
    free extra fact from the lemma, easy corollary, not yet exploited), or (b) an adapted
    telescoping/limiting argument in the style of `aimo-0710`'s Solution 2 comparing `x f(x)`-type
    invariants across two points as `n→∞` rather than a single point against 0.
