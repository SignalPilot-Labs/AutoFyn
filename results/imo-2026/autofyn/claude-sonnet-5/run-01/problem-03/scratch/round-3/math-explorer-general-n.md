## imo-2026-03 (lens: generalization to all n≥3, both directions)

- Distinct openings:
  1. **[STRONGEST — verified, ready to hand to a builder] Case (i)'s top-level bound
     (form A) generalizes to ALL n via a clean 1-variable hybrid optimization, with NO
     need for `dyadic-cascade-induction`'s n=2-specific "exact 2-element residual"
     trick.** Setting up the induction with strong IH (form A *and* form B both proved
     at level m-1 — form A is the IH, form B is already proved at every level directly,
     non-inductively), take Case (i)'s residual `{a_2,...,a_k}` (sum `S-a_1`) after XY
     bisects `a_1`. Instead of using only form A (too lossy — this is exactly the
     "gap 5" counterexample the round-2 builder found) or only form B, use the trivial
     fact that `e(residual) ≤ min(e_{m-1}(S-a_1), a_2/2^{m-1})` (both bounds hold
     simultaneously, so their min does too — no new lemma needed, just combine what's
     already proved), then note this is monotone increasing in `a_2`, so it is
     maximized (over LB's choice of `a_2 ≤ a_1/2`, the Case-(i) cap) at the boundary
     `a_2 = a_1/2`, giving `φ(a_1) := min(e_{m-1}(1-a_1), a_1/2^m)` (`S=1` WLOG). This
     is now a **pure 1-variable calculus problem** (max of min of one decreasing, one
     increasing affine-in-`a_1` function) independent of `m`'s residual size. I solved
     it exactly by hand and verified both algebraically and numerically (see below):
     the crossing point is **exactly** `a_1* = 2^m/(2^{m+1}-1)` — the dyadic value —
     and `φ(a_1*) = 1/(2^{m+1}-1) = e_m` **exactly**, for every `m` tested (checked
     `m=1..6` both by exact-`Fraction` algebra and by a 2000-point grid search). This
     is a genuine, general, non-case-specific closure of Case (i)'s form-A gap for
     **all** `n`, and it directly exhibits the self-similar structure asked about: the
     extremal residual `(a_2,...) = (a_1^*/2, a_1^*/4,...)` **is exactly the scaled
     dyadic partition at level m-1**, i.e. Case (i)'s inductive step literally peels the
     top piece and recurses into a scaled copy of the same extremal problem one level
     down. Recommend the outliner replace the "n=2-only, exact-formula" version of
     Case (i)'s closure with this general argument — it is strictly stronger, no more
     work, and removes one whole item from the open-gaps list for every `n`.
  2. **[Negative but sharp — a genuine dead end, save the next round from re-deriving
     it] The analogous naive 2-candidate generalization FAILS for Case (ii) at m=3.**
     I tried the direct analogue: XY's two candidates are (c) bisect `a_1`→residual
     `{a_2,...}` and (a) match `a_1→a_2`→residual `{a_1-a_2,a_3,...}`; bound each via
     `min(form A, form B)` and take the min of the two candidates, then optimize over
     `(a_1,a_2)` only (ignoring finer residual structure). This DOES reproduce the
     n=2 answer correctly in the specific 1-parameter slice where `a_2→a_1/2^+`
     (matches the known n=2 fact that the sup `1/7` is approached only at the
     Case-(i)/(ii) boundary, never attained inside Case ii). But a full numerical grid
     search at `m=3` (`e_2=1/7` known, target `e_3=1/15`) finds this crude bound
     **exceeds the target inside Case (ii) proper**: at `(a_1,a_2,a_3)≈(1/3,1/3,1/3)`
     (near-uniform three pieces) the bound evaluates to `≈0.081 > 1/15≈0.067`. I then
     directly computed the TRUE game value at that exact point by hand (not the crude
     bound): the raw multiset `{1/3,1/3,1/3}` has `e=1/3`, but XY, with 3 cuts
     available, need only **bisect ONE of the three 1/3-pieces** (`1/3→{1/6,1/6}`,
     1 cut) to reach `{1/3,1/3,1/6,1/6}`, giving `e = 1/3−1/3+1/6−1/6 = 0` — far under
     target. So the true value is fine; **the crude form-A/form-B bound is simply too
     lossy in the "near-uniform pieces" regime**, because it only ever considers ties
     between the top piece and its immediate neighbor, never ties among lower-ranked
     pieces (which is exactly where the real action is when the top few pieces are
     close in value). **Conclusion: the 2-candidate ("bisect-top" / "match-top-to-2nd")
     strategy family that fully closes Case (i) does NOT suffice for Case (ii) at
     general `m`; XY's real strategy needs to consider ties among ANY comparable pair
     of pieces (matching the vertex lemma's full generality), not just the top two.**
     This sharpens (does not just restate) the "casework blows up" worry in the
     dispatch: it is not merely combinatorial explosion of hand cases, it is that the
     specific *strategy family* used for Case (i) is provably insufficient for Case (ii)
     — a genuinely different mechanism is needed there, not just "more of the same
     casework, patiently done."
  3. **Self-similarity / strengthened-IH framing (the recursive backbone worth
     building the outline around).** The natural stronger induction hypothesis is not
     just "`max_LB min_XY e ≤ e_m·S`" (a bound) but a full **value-function
     characterization**: "for every `≤(m+1)`-piece configuration, XY's best response
     achieves exactly [some explicit formula], with the *unique* maximizer over LB's
     choices being the dyadic partition." Opening 1 shows this strengthened IH,
     applied only through its two already-available consequences (form A, form B),
     suffices for Case (i); Opening 2 shows it does not (in that crude form) suffice
     for Case (ii). The natural next strengthening to scout (not developed further
     here, left for the outliner) is either (a) a genuine **potential/weight function**
     `Φ = Σ w_i a_i` with a *uniform per-cut decrease* bound tight enough to swallow the
     near-uniform regime automatically (this is exactly what `potential-weighting-
     upper-bound.md` was reaching for and abandoned as an unresolved "central open
     gap" — my finding above is concrete evidence this route, not the two-candidate
     casework route, is the one that generalizes for Case (ii)), or (b) recursing with
     a *pairing/matching* argument over the WHOLE multiset at once (XY greedily creates
     as many exactly-equal pairs as its cut budget allows, each contributing exactly 0
     to `e` by Lemma P — the near-uniform counterexample above is precisely a case
     where this pairing view finds the answer trivially, in one cut, while the
     top-two-only view badly overestimates).

- Candidate technique(s): strong induction on `n` (the `m`-indexed "Level m" claim
  already set up in `dyadic-cascade-induction.md`) — Case (i) is now generalizable by a
  clean calculus argument (Opening 1); Case (ii) needs either a geometric-weight
  potential-function invariant (KB "Invariants & monovariants"; the abandoned
  `potential-weighting-upper-bound` approach) or a pairing/matching argument over the
  whole multiset exploiting Lemma P more globally than "top-two only." Also relevant:
  Pólya's "strengthen the hypothesis before inducting" (KB "Problem-Solving
  Heuristics"), since the successful Case (i) argument required carrying BOTH form A
  and form B as the induction hypothesis, not either alone.

- Cheap-kill candidates: near-uniform / small-spread configurations are structurally
  *easy* for XY (one bisection of any near-tied piece drives `e` toward 0 fast via
  Lemma P) — so a real proof should not need heavy casework there; the hard regime is
  genuinely concentrated near the dyadic ratio-2 cascade. This narrows where a general
  argument needs to work hard (near dyadic points) vs. where a crude bound already
  suffices (spread-out configurations), which could substantially prune the case
  analysis if the outliner builds the induction around "distance from the dyadic
  shape" rather than raw sign-regimes of `a_1,a_2,a_3`.

- Knowledge-base entries to use: "General Proof Methods — Induction" (strong induction,
  the right variable is `n`/level `m`); "Problem-Solving Heuristics (Pólya) —
  Generalize: a stronger, cleaner statement is sometimes easier to prove by induction
  (induction loading)" — directly describes what's needed for Case (ii); "Invariants &
  monovariants" (potential-function per-move-decrease framing, Combinatorics section).

- Analogous past problems (cruxes): filtered `crux_moves_documentation.md` →
  `domain=combinatorics`, subtopics `games-and-strategy`, `induction-and-construction`,
  `extremal-principle`. The 39 `games-and-strategy` cruxes are mostly combinatorial
  games (pairing/blocking strategies, parity invariants) and none is a direct
  stick-cutting/cake-division analogue (no crux problem involves cutting an interval and
  alternately claiming pieces — checked directly against `past_problems_database.json`
  by keyword search for "stick"/"cake"/"claim... piece", no real hit). The genuinely
  useful analogues are **structural**, from `induction-and-construction` and
  `extremal-principle`, not from `games-and-strategy`:
  - **`aimo-0438`** (self-similar peeling induction on a lattice-diamond partition
    problem): "Set up an induction on the size parameter by peeling off one canonical
    outer layer whose removal leaves a scaled-down copy of the same region one size
    smaller" — exactly the mechanism behind Opening 1/3: peeling `a_1` (via bisection)
    leaves a residual that IS a scaled copy of the level-`(m-1)` extremal problem.
    Directly analogous in spirit (not in subject matter).
  - **`aimo-0965`** (isosceles-triangle dissection count, `extremal-principle`):
    "Choose the extremal (longest) member... as the pivot of the induction step... the
    two central pieces' strict inequality provides exactly the slack that pays for the
    pivot object" — structurally the SAME shape as Opening 1's calculation: two
    inequalities (there: two odd-sized sub-arc bounds; here: form A and form B) combine
    with exactly enough slack to make the induction close with equality at one specific
    extremal configuration, not more, not less. Good template for how to write up
    Opening 1 rigorously (a "peel the extremal pivot, IH provides exactly the needed
    slack" writeup pattern).
  - **`aimo-0361`** (max-friendship graph problem, `extremal-principle`): "Set up an
    extremal-count recurrence by peeling a fixed-size substructure and iterate it to a
    closed-form bound compared against the conjectured optimum" — same overall shape
    (recurrence `g(n) ≤ max(f(n), peel-cost + g(n-k))`, iterated and compared to a
    closed-form target) as the `e_n = e_{n-1}/(2+e_{n-1})` recursion here, useful as a
    template for how the write-up of the *whole* induction (not just Case i) should be
    organized once Case (ii) is closed.
  None of these are subject-matter analogues (no crux corpus problem is a cake/stick
  alternating-claim game), so treat them as *technique* hints to adapt, not as a
  worked template to copy directly.

- Prior progress: `dyadic-cascade-induction` has fully closed the upper bound at n=1
  and n=2 (Case i and Case ii both, at n=2 only). `elementary-exchange-smoothing` has a
  genuine but narrow-scope local-uniqueness result near the dyadic point at n=2, Case
  ii, conditional on an imported (unproved) fact. Both certified lemmas (Lemma G, Lemma
  P) are fully general (any `n`) and already reusable for the general-`n` push — no
  further work needed there. **New this round:** Opening 1 above is verified, general
  (all `n`) progress on Case (i)'s previously-open "gap 5" (form-A promotion) — not yet
  written into any approach file; recommend the outliner assign a builder to formalize
  it (it is a short, clean calculus argument, much shorter than the n=2 hand casework
  it replaces).

- Dead ends (do not retry): (1) the n=2 "exact 2-element/3-element closed-form residual"
  trick from `dyadic-cascade-induction` — confirmed by this round's Opening 1 to be
  unnecessary even at n=2 (a strictly more general argument exists) and confirmed by the
  problem's own structure to not scale to residuals with >2 elements (no exact closed
  form is available there) — do not try to extend it verbatim to n=3. (2) The naive
  "min of the same two Case-(i)-style candidate strategies (bisect-a1 / match-a1-a2),
  bounded via `min(form A, form B)` on each" for Case (ii) at general `m` — confirmed
  by direct computation (Opening 2) to give a bound that exceeds the target at
  near-uniform configurations at `m=3`, even though the true game value there is far
  below target; the bound is too lossy, not the theorem false. Any approach that tries
  to literally reuse Case (i)'s machinery unchanged for Case (ii) at `m≥3` will hit this
  same wall. (3) `potential-weighting-upper-bound.md`'s and
  `concavity-minimax-duality.md`'s approaches remain unstarted (Status: unsolved, no
  work this round) — not dead per se, but both flagged by their own files as high-risk/
  abstract with the central mechanism ("uniform per-move potential decrease" /
  "stationarity forces ratio 2") never actually carried out; my Opening 2 finding is
  evidence the potential-function route (not the casework route) is the one actually
  needed for Case (ii), so this approach should be *reprioritized upward*, not
  abandoned.

- Small-case / intuition notes (labeled as conjecture where not proved):
  - **[Proved, not conjecture]** `e_n = e_{n-1}/(2+e_{n-1})` is algebraically consistent
    with `e_n = 1/(2^{n+1}-1)` (direct substitution check, exact).
  - **[Proved this round, Opening 1]** Case (i)'s form-A top-level bound `e ≤ e_m·S`
    holds for **all** `m`, with the extremal `a_1` exactly `2^m/(2^{m+1}-1)` and the
    optimal residual shape exactly the scaled dyadic partition at level `m-1` — verified
    both by exact-`Fraction` algebra (closed form) and by grid search, `m=1..6`.
  - **[Conjecture, evidence only]** The near-uniform-configuration counterexample
    (Opening 2) suggests the "hard"/tight region of the whole optimization is a genuine
    neighborhood of the dyadic ratio-2 cascade and nowhere else — i.e. a proof
    strategy that only needs to work hard near the dyadic point (à la
    `elementary-exchange-smoothing`'s local-uniqueness argument, generalized to all
    `m`) and can dispatch everything else with a cheap uniform bound, is plausible and
    would avoid combinatorial casework blowup — but this has only been checked at one
    point (`m=3`, uniform triple) and is not a proof of "only the dyadic neighborhood is
    hard" in general.
