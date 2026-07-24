## imo-2026-03 (lens: direct attack on the residual middle band, ℓ(F)=2 sub-case (b))

- Distinct openings:
  1. **Cut-budget correction (most promising, new this round).** The middle
     band's setup (Theorem 34's own framing) treats `R'` as capped at `n-2`
     cuts. But mass conservation forces `Total(P) = 2p2-v1-v2 > 0` whenever
     both `v1,v2 < p2` (sub-case (b)'s own defining condition) — and since
     `P` must be an exactly-paired (even-count, ≥2-element) family to keep
     `ℓ(F)=2`, realizing `{v1,v2}∪P` from a single stick `p1` needs **at
     least 3 cuts on p1** (1 to split off `v1`, 2 more to carve the
     remainder into `v2` plus one matched pair). This leaves `R'` with **at
     most `n-3` cuts**, not `n-2` — a strictly tighter true legal domain
     than Theorem 34's stated hypothesis used (this exact correction is
     already flagged generically in `/tmp/memory/math-explorer.md` rule #26
     / run_state.md round-14 note, but had not yet been applied to the
     *current* residual middle band specifically). Fresh numeric check this
     round (see below): with the correct `n-3` cap, **zero violations** in
     20,000+ trials per `n=3..8`; with the looser `n-2` cap Theorem 34's own
     text uses, **genuine violations exist** (exact witness found at n=3).
     Recommendation: redo the middle-band argument with the honest `n-3`
     cap from the start (not as an afterthought) — this shrinks the
     adversary's real degrees of freedom and may make a direct
     vertex-family / cut-count argument tractable where the "arbitrary
     budget" version is provably false.
  2. **Direct induction on the coupled quantity itself**, not on
     `A(R'_{>v})` in isolation. Define `Δ(n,v) := min over legal (≤n-3)-cut
     R' of [A(R') - 2·A(R'_{>v})]` (this is exactly what Theorem 34's proof
     needs a floor on, generalizing its `v1+v2≤p2` special case). Since
     `R'/s` is exactly the `(n-2)`-ladder (tail-self-similarity), `Δ(n,·)`
     rescales to the *same* two-parameter object one level down — i.e. this
     is a genuinely new inductive target (a "thresholded Claim A/B" at level
     `n-2`, not a bare single-variable ceiling). This is NOT the same as
     round 18's "context-free `A(S_{>v})` bound" (already flagged as the
     wrong framing) — it is the *coupled* difference, self-similar in `n`,
     which the Vertex-Minimum Theorem + Odd-Run-Reduction machinery already
     on file could in principle evaluate directly via vertex enumeration at
     the reduced cut cap `n-3`, rather than trying to bound each piece
     (`A(R')`, `A(R'_{>v})`) separately.
  3. **Cut-count / sign-toggle counting** (a refinement of the dead per-cut
     charging idea, not a repeat of it): rather than charging each cut's
     *value* effect on the band (round-18's dead approach — sign is global,
     not local), count how many parity toggles of `u_{R'}` a single cut can
     cause on the *whole* domain (each cut can change `u_{R'}`'s value on at
     most one sub-interval, so with `≤n-3` cuts, `u_{R'}` has at most
     `2(n-3)+1` "runs"). Whether this coarse toggle-count bound is enough to
     force `I_1 - J_0` above the needed threshold is unverified — flagged
     as a candidate, not developed further (per instructions, not proving
     it here).

- Candidate technique(s): tighten the legal cut-budget bookkeeping (item 1)
  first — it is cheap (pure combinatorics of how many cuts building
  `{v1,v2}∪P` truly costs) and changes the numeric picture from "false in
  general" to "true in every trial tested." Then attack the coupled
  quantity `Δ(n,v)` (item 2) via the already-certified Vertex-Minimum
  Theorem / Odd-Run-Reduction Lemma restricted to the `n-3`-cut vertex
  family, rather than the context-free `A(S_{>v})` ceiling that round 18
  correctly identified as the wrong target.

- Cheap-kill candidates: the cut-count bookkeeping check (item 1) is itself
  a cheap structural pruning step — before any heavy new machinery, the
  outliner should re-verify (by hand, one paragraph) that Theorem 34's
  stated `≤n-2` cap for `R'` should really read `≤n-3`, and re-check whether
  this alone (with the *already*-certified IH(n-2) machinery, which already
  covers `≤n-3` as a special case) closes any additional slice of the band
  beyond `v1+v2≤p2` — e.g. try substituting the `n-3` cap directly into
  Theorem 34's own proof steps (its bound `J_0≤v2` and the IH floor
  `A(R')≥f(n)`) to see how much of the middle band it now covers before
  reaching for a new mechanism.

- Knowledge-base entries to use: none of `knowledge_base.md`'s generic
  entries are new here (per round-1 finding, the crux corpus and KB have no
  direct analog for this specific game); the load-bearing tools remain the
  problem's own certified lemmas: `vertex-minimum-theorem`,
  `odd-run-reduction-lemma`, `tail-self-similarity`, `upper-truncation-identity`,
  `two-threshold-truncated-alternating-sum-floor` (Theorem 32),
  `theorem-33-...` and `theorem-34-...` (already certified, cite don't
  re-derive per the dispatch instructions).

- Analogous past problems (cruxes): searched combinatorics subtopics
  `extremal-principle`, `size-bounding-and-descent`,
  `inequalities-SOS-and-convexity`, `induction-and-construction` for
  "threshold / truncation / order-statistic / budget / cut" keywords.
  Nothing is a genuine analog to a *coupled two-threshold* truncated
  alternating sum over a superincreasing sequence with a tight cut budget.
  The closest surface-level match, `aimo-0388` ("Bound a middle order
  statistic by noting the coins at or above it are numerous enough that
  their known total caps its size"), is the same flavor of crude
  mass-domination bound already tried and confirmed too weak here (it's
  essentially the `max-domination-lemma`/`A(R')≤max(R')`-style ceiling
  already in use for Theorem 33, and it fails exactly where the middle band
  needs a *joint* bound). No strong analog found — consistent with round 1's
  original finding; do not spend further round budget re-searching the
  corpus for this specific gap.

- Prior progress: Theorem 32 (unconditional, `v1≤s`), Theorem 33
  (unconditional, `v1∈(s,p2)`, `v2≥s`), Theorem 34 (conditional on
  `(★_{n-2})`, `v1∈(s,p2)`, `v2<s`, `v1+v2≤p2`) are all certified and cover
  everything except the middle band `v2∈(p2-v1,s)`, `v1∈(s,p2)`. Round 18
  confirmed per-cut charging and the LP-floor-constraint mechanisms are
  dead for this exact band.

- Dead ends (do not retry):
  - Per-cut value-charging on the middle band (round 18): sign of an
    individual cut's effect on `A(R'_{>v2})` depends on global parity of
    other fragments, not locally bounded — confirmed dead, re-confirmed by
    my own re-derivation of the algebra (Step in Theorem 34's discussion:
    the needed inequality is a genuine lower bound on the *joint*
    `I_1 - J_0`, not decomposable cut-by-cut).
  - Adding the inductive floor `A(R')≥f(m)` as an extra LP constraint
    (round 18): confirmed too weak, 60-80k trials, constrained max = plain
    unconstrained max.
  - **NEW finding this round**: the middle-band inequality is **actually
    FALSE** if `R'` is allowed an unrestricted or `n-2`-capped cut budget
    (exact counterexample found, `n=3`: `v1=39703/150000≈0.2647`,
    `v2≈0.1326`, `R'` using 1 cut on the tail, gives
    `A(F∪G')≈0.0061 < f(3)=1/15≈0.0667` — a genuine violation of the naive
    "any legal `R'`" version). This is NOT a counterexample to Claim B
    itself (the game only allows `R'` up to `n-3` cuts here, per the mass-
    conservation argument in item 1), but it does mean: **do not attempt to
    prove the middle-band inequality for an arbitrary/`n-2`-capped `R'` —
    it is false as stated; the honest hypothesis is `≤n-3` cuts.** Any
    future mechanism (per-cut charging, LP floor, or a new one) must build
    in this tighter cap from the start, or it will chase a false statement.

- Small-case / intuition notes (all conjecture, exact-Fraction not proof):
  - With the corrected `≤n-3` cap on `R'`, exact-`Fraction` random search
    (20,000+ trials per `n`, `n=3..8`, uniform sampling of `v1∈(s,p2)`,
    `v2` in the exact middle band `(p2-v1,s)`, `R'` a genuinely random legal
    refinement with a random cut budget in `[0,n-3]`) finds **zero
    violations** of `A(F∪G')≥f(n)` at every `n` tested — strong conjectural
    support that the middle band, correctly scoped, is true.
  - The worst-case margin (relative to `f(n)`) is small but not vanishing
    and does **not** sit at a fixed obvious boundary: for `n=3,4` the worst
    case found uses `budget=0` (i.e. `R'` completely untouched — the
    ladder tail as-is); for `n=5,6,7,8` the worst case shifts to an
    *interior* budget close to (but not always exactly) the maximum `n-3`.
    Margin generally *decreases* as `R'`'s cut budget increases (more
    cutting power for the adversary), roughly monotonically, with a slight
    non-monotone wobble near the top budget at `n=7,8` (likely sampling
    noise, not confirmed). This means a naive "worst case is always at the
    boundary `v2→s` or `v2→p2-v1`" limiting/continuity argument is **not**
    directly supported — the worst-case *budget* of `R'` (not just `v1,v2`)
    also varies with `n`, so a pure boundary/continuity argument in
    `(v1,v2)` alone, without also pinning down `R'`'s structure, looks
    insufficient on its own.
  - Recommendation for the outliner: prioritize item 1 (fix the cap to
    `n-3`) as a near-free correction, then attempt item 2 (treat the
    coupled quantity `Δ(n,v)` as a self-similar inductive target one level
    down, evaluated via the already-certified Vertex-Minimum/Odd-Run
    machinery restricted to the `n-3`-cut vertex family) as the next
    genuinely new mechanism — this is different in kind from all four
    previously-dead mechanisms (per-cut charging, LP floor, Danskin/
    concavity, weighted-combination) since it exploits the *cut-budget*
    structure directly rather than trying to bound `A(R'_{>v})` as an
    isolated quantity.
