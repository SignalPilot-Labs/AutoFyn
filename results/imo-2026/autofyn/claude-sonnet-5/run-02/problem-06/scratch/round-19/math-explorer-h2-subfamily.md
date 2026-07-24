## imo-2026-06

### Prong 1: H2/NTBT (self-absorption at S_0=Q, zero recruitment rounds)

- **Distinct openings tried:** (a) hunt for a genuinely new *proof* angle for
  NTBT beyond the two already-recorded dead routes (density/class-blindness;
  FAH-reduction) — none found; (b) actively search for a *counterexample*
  on adversarially-chosen new seeds (large |Q|=7, and skewed seeds mixing a
  huge prime with small ones) — none found, two more "apparent
  counterexample" candidates resolved (see below); (c) re-examine the
  logical *necessity* of NTBT for H2 — confirmed NTBT is only *sufficient*,
  not necessary, for the cleanest possible H2 resolution (`S*=Q`); the
  weaker target "some self-absorbing S* exists at all, however large" is the
  actually-needed statement, and NTBT is a strictly stronger, more
  convenient special case of it. This weaker target has NOT been separately
  probed by any round so far (all H2 numeric work has tested `N(Q)` at the
  minimal core, not the more general question of whether *some* enlarged
  core eventually self-absorbs even if `Q` itself does not) — flagging this
  as the one genuinely under-explored angle, though I did not find a
  mechanism for it either.
- **Candidate technique(s):** none new found. The standing diagnosis
  (`core-growth-monotonicity.md` Proposition 3: `M_B` non-constructive from
  any bounded prefix; `self-absorbing-by-construction.md` §3 routes 1–2)
  still fully accounts for why no direct argument closes NTBT.
- **Cheap-kill candidates:** none obvious beyond what's already used
  (window-artifact re-checking at 3-4x scale, per rule 24). No new
  parity/pigeonhole/injection angle surfaced.
- **Knowledge-base entries to use:** none beyond what's already cited in
  `self-absorbing-by-construction.md`/`core-growth-monotonicity.md`
  (Persistent-Type Pigeonhole, Extended Persistent-Type Pigeonhole, the
  Termination Criterion Lemma). No new KB entry looks applicable to NTBT.
- **Analogous past problems (cruxes):** none found specific to this prong
  beyond what's already been mined (rounds 9–15 exhausted the "infinitely
  often → universal" corpus candidates aimo-0016/aimo-0051/aimo-1019 for the
  sibling FAH crux; none of these transplant any better to NTBT's
  "occurs-once implies occurs-again" shape — it is a recurrence/renewal
  claim, not a promotion-from-cofinite claim, so the aimo-0016 downward-
  transport template doesn't obviously apply either). Did not find a better
  match this round.
- **Prior progress:** NTBT (`N(Q) ≤ 1` for all `a_1`) has zero open
  counterexamples across the ~50+ seeds tested through round 18. This round
  adds computational evidence but no proof route.
- **Dead ends (do not retry, confirmed again this round):** the
  counting/pigeonhole corridor (3 sub-routes, round 18) remains exhausted —
  I did not re-attempt it, per your instruction, and nothing in this
  round's work reopens it. The density/class-blindness route and the
  FAH-non-equivalence finding (§3 of `self-absorbing-by-construction.md`)
  both still stand on inspection — I re-derived the class-blindness
  argument informally and it still holds (the only certified magnitude
  facts, Sandwich Genericity / Bounded Gap, are identical formulas
  regardless of which specific subset of `Q` a term's type is, so they
  cannot distinguish "this type recurs" from "it doesn't").
- **Small-case / intuition notes (conjecture only):** Ran two new
  adversarial-seed tests with a fast bitmask simulator (per rule 30's
  spirit; verified small-n against the naive generator first):
  - `a_1 = 510510 = 2·3·5·7·11·13·17` (`|Q|=7`, the largest tested to date):
    at window 60,000, three single-occurrence types were found: the trivial
    `τ(1)=Q` and two genuine candidates, `{2,3,5,11,13,17}` (first at
    `n=36466`) and `{2,3,7,11,13,17}` (first at `n=51052`). Extending the
    window to 200,000 found **both recur** (no longer singles) — another
    resolved window artifact, exactly the round-17/18 pattern, now on a
    `|Q|=7` seed (larger than any previously tested). Zero surviving
    exceptions at window 200,000.
  - `a_1 = 209370 = 2·3·5·7·997` (skewed: one huge prime, four small ones):
    at window 60,000 a genuine candidate single `{2,3,5,7,997}` appeared at
    `n=34896` (besides the trivial `n=1`); extended to window 300,000, it
    **also recurs** and — notably — even the trivial `τ(1)=Q` type itself
    recurs by this window, leaving zero singles at all. This is evidence
    (not proof) that skewing the seed toward one very large prime does not
    obviously produce a genuine NTBT counterexample either.
  - No genuine (non-resolving) counterexample found in any new seed tried.
    This strengthens, but does not change the proof status of, the round-18
    record. **Conjecture, not proof.**

### Prong 2: a_1 = p·q subfamily (the "q >> p" lead)

- **Headline finding: REFUTED as a clean threshold family.** A systematic
  sweep (fast trial-division simulator, cross-checked against a naive
  brute-force `gcd` generator on small n before trusting it) for `p ∈
  {3,5,7,11,13}` against dozens of primes `q > p` shows the "clean" case
  (`T=1, L=p`, i.e. `a_n = pq + p(n-1)` literally, the exact analog of the
  `p^k` theorem) holds for MOST `q`, but fails ("messy": some other,
  seed-dependent, much longer eventual period) at a **sparse, non-monotone**
  set of `q` values that does **not** stabilize once `q` exceeds any fixed
  multiple of `p`. Concretely:
  - `p=11`: messy at `q ∈ {13,17,19,31,37,43}` (all `≤43 ≈ 3.9p`), clean at
    every one of 95 further primes `q ∈ (43, 700)` tested (window 1800-2200
    terms each). `q=13,17,19` (`a_1=143,187,209` — 187/209 are two of the
    workspace's 4 canonical hard `|Q|=2` seeds) break almost immediately
    (by index 2-4); `q=31,37,43` (`a_1=341,407,473`) also break early (by
    index 3-4 of the sequence) despite `q` being noticeably larger than `p`
    — this directly falsifies the "q >> p suffices" intuition, since 31–43
    is already "much bigger than 11" by any reasonable reading, yet still
    messy, while slightly larger primes (47, 53, ...) are clean.
  - `p=13`: messy at `q ∈ {17,19,23,47}` (`221=13·17`, `247=13·19` are the
    other 2 of the 4 canonical hard seeds), clean at every other tested `q`
    up to 400 (including all of 29,31,...,43,53,...,139 and 44 further
    primes up to 400). **`q=47` is messy while both smaller (43) and larger
    (53+) neighboring primes are clean** — this is the sharpest single data
    point ruling out ANY monotone-in-`q` or interval-based threshold
    `f(p)`: there is no `f(11)` or `f(13)` such that `q>f(p)` implies clean,
    since messiness recurs at a `q` value strictly interior to a run of
    clean values.
- **Mechanism identified for the first possible break (useful partial
  fact, not a full theorem).** For `a_1=pq` (`p<q`), `a_2 = a_1+p` is always
  forced exactly as in the `p^k` proof (candidates `a_1+1,...,a_1+(p-1)`
  are automatically illegal against `a_1` alone, since neither `p` nor `q`
  divides them). The FIRST possible deviation, from `a_2` to `a_3`, can only
  occur if `q < 2p` (so that `j^* := q-p ∈ [1,p-1]` is a valid candidate
  offset with `a_2+j^* ≡ 0 (mod q)`), **and** the resulting candidate must
  also pass `\gcd(\cdot, a_2)>1`, which reduces to the elementary check
  `gcd(q-p,\, p(q+1)) > 1`. Verified this exactly predicts the `q<2p` break
  cases (`q=13,17,19` for `p=11`; presumably similarly for `p=13`'s `q=17,
  19,23`). For `q ≥ 2p` (`q=31,37,43` for `p=11`; `q=47` for `p=13`), the
  break necessarily happens at a *later* step `k`, governed by whether
  `(k-1)p mod q` lands in `[1,p-1]` (guaranteed to happen periodically in
  `k` by pigeonhole, roughly every `q/(p-1)` steps) **and** the resulting
  candidate additionally survives `\gcd(\cdot, a_i)>1` against every single
  earlier term `a_2,...,a_{k-1}` (not just `a_1`) — this second condition is
  the genuinely hard part and is exactly as intricate/case-dependent as the
  general FAH question; I found no closed form for it and do not believe
  one exists that is meaningfully simpler than the general problem.
- **Verdict on the prong-2 mandate:** there is **no clean threshold
  `f(p)`** under which `a_1=p·q` is unconditionally clean for `q>f(p)` —
  refuted by concrete counterexamples interior to runs of clean values
  (`q=47` for `p=13` is the sharpest). The `q<2p` sub-case DOES have a
  clean, elementary, fully checkable necessary-and-sufficient condition for
  the *first-step* break (`gcd(q-p, p(q+1))>1`), which could in principle
  be assembled into a genuine (but narrow — only rules out breaking at the
  very first inductive step, says nothing about later steps) partial lemma
  if a future round wants a small, low-risk addition; but it does **not**
  extend to a general clean/messy criterion, and does not touch `q≥2p`,
  which is the bulk of the family and provably not simpler than general FAH.
  **Recommend NOT pursuing `a_1=p·q` as a tractable subfamily target next
  round** — the data conclusively shows it inherits the full difficulty of
  the general problem, matching (and now sharpening beyond) round 18's
  single counterexample (`341=11·31`) finding.
- **Cheap-kill candidate found:** if a future round is tempted to try `q<2p`
  as a "half-clean" restricted family (i.e., prove `q≥2p ⟹ clean`), it is
  ALREADY REFUTED by this round's data (`q=31,37,43` for `p=11`, all
  `≥2p=22`, are messy) — do not re-propose this exact restriction without
  new information.
- **Knowledge-base / lemma reuse:** the existing
  `prime-power-seed-literal-periodicity-theorem.md`'s proof technique
  (ruling out `a_n+1,...,a_n+(p-1)` via `\gcd` with `a_1` alone) transfers
  cleanly to justify `a_2=a_1+p` in the `pq` case (first step only) — this
  is the extent of the reusable overlap; nothing further generalizes.

### Overall recommendation for the outliner

- Prong 1 (H2/NTBT): no new proof mechanism found; treat as still stuck,
  same status as round 18. If dispatched again, the one unexplored angle
  worth a dedicated try is the *weaker* target (existence of *some*,
  possibly larger, self-absorbing `S*` — not necessarily `S*=Q`) rather
  than NTBT itself, since NTBT is sufficient but not necessary for H2.
- Prong 2 (`a_1=pq`): definitively refuted as a clean tractable subfamily —
  do not dispatch a builder to attempt a general `p·q` theorem; the
  `q<2p` first-step necessary condition (`gcd(q-p,p(q+1))>1`) is the only
  salvageable fragment, and it is very narrow (does not resolve cleanliness
  even within `q<2p`, only predicts the first-step outcome).
