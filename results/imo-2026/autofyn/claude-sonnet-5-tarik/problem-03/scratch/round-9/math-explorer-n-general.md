## imo-2026-03 (plateau-break / general-n framing check)

### Headline finding (read this first)
**"General n≥4" is not a separate open frontier that needs a new top-level framing — it is
already automatically delivered by whatever closes Case (ii)'s aggregated Small-Gap
Crossing-Domination Lemma at general m.** I traced the exact induction structure in
`dyadic-cascade-induction.md` §2d (lines 711–800) and confirmed the round-3 reviewer's overclaim
finding still governs it: Case (i)'s "closed for every m" proof invokes the **strong IH's form
(A) at level m-1 on the residual `{a_2,...,a_k}`**, and that residual is an *arbitrary* multiset,
not one guaranteed to itself satisfy Case (i)'s hypothesis `a_2≥2a_3`. So Case (i)'s own closure
at level m is *conditional on the full theorem (both cases) already holding at level m-1* — it
is not an independently-generalizable building block, it is welded to Case (ii) inside one joint
strong induction. Consequently:
- There is no "Case (i) for all n" fact sitting separately from "Case (ii) for all n"; they rise
  and fall together, one level of `m` at a time, inside a single strong induction on `m` (=n at
  the tight case `k=m+1`, by Slack Collapse).
- The moment `potential-weighting-upper-bound`'s **aggregated Small-Gap Crossing-Domination
  Lemma** (`OPT(Y,p-1)=NC(Y,p-1)` for *arbitrary* `Y,p` — a purely combinatorial claim with no
  reference to which "level" of the outer game induction it's used at) is proved as a
  self-contained fact for all `p` at once, the outer strong induction on `m` closes **for every
  m simultaneously**, hence **for every n at once** — no separate "n≥4" argument is or will be
  needed beyond that one lemma.
- `current.md`'s own "what remains open" item 6 ("`n≥4`, both directions, remains essentially
  untouched") is now **stale/imprecise** and should be corrected by the outliner: (a) the
  **lower bound is already fully general** — the round-8 milestone (`superincreasing-no-early-zero.md`
  + `all-cycles-resolution.md`) proves `g(D_m,m)≥e_m·S(D_m)` for *every* `m` via an invariant
  argument with **no induction on n at all**, so there is no lower-bound "n≥4" task left; (b) the
  upper bound's generality-in-n is not a separate task from Case (ii)'s general-m closure, it's
  the *same* task viewed from a different index name.
- **Recommendation to the outliner: do NOT open a 5th slug for "general n" as a distinct
  framing.** Doing so would just relabel `potential-weighting-upper-bound`'s existing gap —
  exactly the single-gap-trap CLAUDE.md warns against. The one high-leverage target remains the
  aggregated Small-Gap Crossing-Domination Lemma.

### Job 1: the recursion c(n) = 2c(n-1)/(2c(n-1)+1) — re-examined post round-8 milestone
Re-derived and hand-checked the recursion (it's already on file, §0/§2d of
`dyadic-cascade-induction.md`, verified algebraically: `e_{n-1}/(2+e_{n-1})` with
`e_{n-1}=1/(2^n-1)` gives exactly `1/(2^{n+1}-1)=e_n`). Re-examined whether this now offers a
shortcut, given the round-8 lower-bound milestone:
- **Upper-bound side of the recursion is literally Case (i)'s own mechanism** (bisect `a_1`,
  apply IH to the residual) — see the headline finding above: it is not a new framing, it's the
  existing Case-(i) machinery restated, and it inherits the exact same circularity (needs
  Case (ii) at level m-1, i.e., needs the very thing it would be trying to bypass). **Attempting
  to "prove c(n) from c(n-1) directly" for the upper bound would just be re-deriving Case (i)
  again; it does not touch Case (ii)'s genuine difficulty** (in Case (ii), `a_1` is not dominant,
  so "bisect the top piece and treat the rest as an independent (n-1)-budget subgame" is not
  XY's best response — the whole multiset interacts, which is exactly why Case (ii) needs the
  aggregated OPT=NC combinatorial argument instead of a clean peel-and-recurse step).
- **Lower-bound side of the recursion is now strictly *superseded*, not helped, by the round-8
  milestone.** An inductive recursion argument (level n from level n-1) would be *weaker* than
  what's already proved: the Superincreasing No-Early-Zero Lemma + All-Cycles Resolution give
  `g(D_m,m)≥e_m·S(D_m)` for every `m` **directly, via a signed-subset-sum invariant, with no
  induction on n needed at all**. Re-deriving this via the n-recursion would be a strictly
  inferior, redundant route to a fact that's already unconditionally proved.
- **Net verdict: round 5's decline of this recursion as a 5th slug stands, and is now better
  justified** (previously "not genuinely cheaper"; now provably *no leverage at all* in either
  direction — upper-bound side is identical to Case (i)'s existing entangled mechanism,
  lower-bound side is strictly subsumed by an already-certified, non-inductive result). Do not
  revive it as a distinct approach.

### Job 2: bounded exact computation, TRUE game value (not just against D_m)
Implemented the certified D/M-operation game exactly (`fractions.Fraction`, full recursive
minimax over `D(x)`/`M(x,y)`/stop at every step — this computes `h(A,m)`, which by Lemma D/M is
always `≥ g(A,m)`, i.e. an upper bound on the true value; equality holds unconditionally for
`A` superincreasing per the round-8 milestone, and is the standing not-yet-contradicted
conjecture in general per `dm-completeness-partial.md`). All computation bounded to n≤4, no
unbounded search.

1. **Sanity check against `D_m` (should reproduce the already-certified lower bound exactly):**
   for `m=1..5`, `h(D_m,m)` computed exactly equals `1/(2^{m+1}-1)` in every case (bit-for-bit
   Fraction match) — reconfirms the certified lemma from an independent from-scratch
   implementation.
2. **Outer maximization over LB's opening `A` (the actual `c(n)=max_A g(A,n)` quantity, not
   just the value against the fixed dyadic opening):** ran randomized local search (15 random
   restarts + a dyadic-seeded run, coordinate perturbation + simulated-annealing-style step
   shrinkage) maximizing `h(A,n)` over the simplex of openings, for `n=1,2,3`:
   - `n=1`: best found `e=1/3` at `A≈(0.667,0.333)` — matches `D_1=(2,1)/3` and target `e_1=1/3`
     exactly.
   - `n=2`: best found `e=1/7` at `A≈(0.5714,0.2857,0.1429)` — this is `D_2=(4,2,1)/7` to 4
     decimal places, matching target `e_2=1/7` exactly.
   - `n=3`: best found `e=1/15` at `A≈(0.5333,0.2667,0.1333,0.0667)` — this is
     `D_3=(8,4,2,1)/15` to 4 decimal places, matching target `e_3=1/15` exactly.
   - `n=4`: dyadic-seeded local search converges to exactly `1/31` (matching `D_4`'s target);
     unseeded random restarts (60 iterations, a coarser budget) reached only `~0.007–0.021` <
     target `1/31≈0.0323`, i.e. did not fully converge in the time given — **inconclusive at
     n=4 only because of a shallow iteration budget, not a counterexample**; the dyadic-seeded
     run alone is not independent confirmation (it starts at the known optimum), so n=4's outer
     maximization is **not** independently re-verified here to the same standard as n=1..3.
   - **All findings here are numeric/local-search evidence, not proof**: local search can get
     stuck, and the outer objective is a continuous, non-smooth (piecewise-linear-in-cut-position)
     function so a handful of random restarts is not an exhaustive certificate. Still, for
     n=1,2,3 multiple independent restarts (not just the dyadic seed) converged to the exact
     dyadic optimum, which is a meaningfully stronger confirmation than "D_n itself achieves the
     target" (already proved) — it's evidence that **no other opening beats D_n**, i.e. genuine
     support for the conjectured closed form as the *true* answer, not just a lower bound.
3. **Recursion identity check**: substituting the closed form into `e_n=e_{n-1}/(2+e_{n-1})`
   confirms it algebraically for all n (exact fraction algebra, not numeric) — this was already
   on file in `dyadic-cascade-induction.md` §0; re-verified independently here, no discrepancy.

### Crux corpus (per dispatch, `crux_moves_documentation.md` field names used: `technique`,
`how_used`, `domain`, `subtopic`; filtered `combinatorics`/`games-and-strategy`,
`sequences-and-recurrences`, `extremal-principle`, `induction-and-construction`, plus free-text
keyword search across the whole corpus)
- **`aimo-0117`** (Jesse/Tjeerd stone-box game, NL olympiad) — genuinely close in *spirit* to
  our lower-bound dyadic construction: the winning player writes values as consecutive powers of
  two (`2^{-i},...,2^{j}`) specifically because the top power exceeds the sum of everything
  smaller, and defends a "largest power sits in the target box" invariant against the opponent's
  one-move-per-turn relocation power — this is essentially the same superincreasing-dominance
  idea our certified `superincreasing-no-early-zero`/`all-cycles-resolution` lemmas already
  formalize and have now fully closed. **Not new leverage** (our lower bound is already stronger
  and more general than this crux's ad hoc invariant-maintenance argument), but it is a genuine
  independent confirmation that "superincreasing dyadic sequence + top-exceeds-rest-of-sum" is
  the *standard* extremal recipe for this flavor of alternating-claim/box game — corroborates
  that `D_n` really is the right extremal shape, not a red herring.
- **`aimo-0558`** (ISL-style `±1`-sequence, gap-≤2 subsequence, answer `C=506`) — the *matching
  upper bound* crux move ("build the worst-case sequence as alternating same-sign blocks;
  any admissible selection touching `k` majority-blocks is forced to draw ≥1 element from each
  of the `k-1` intervening minority-blocks between them, capping the excess by `k -(k-1)`
  per-block bookkeeping") and its *achievability* companion ("greedy: always take the majority
  sign, skip a minority element only when forced by the gap budget, charge every forced-kept
  minority element to a distinct skipped one") are a genuinely different technique flavor
  (forced-inclusion-charged-to-a-distinct-skip) from anything currently tried on
  `potential-weighting-upper-bound`'s aggregated Small-Gap Crossing-Domination Lemma. **This is
  not a "general n" lead** (it doesn't touch the induction-on-m structure), but it is a concrete,
  not-yet-tried proof *shape* for the Case (ii) gap itself — worth flagging to whichever
  explorer/outliner owns the m-general upper-bound gap, not spun off as a new slug here (would
  duplicate `potential-weighting-upper-bound`'s existing target).
- No other crux in the corpus (searched by subtopic filter across `games-and-strategy`,
  `sequences-and-recurrences`, `extremal-principle`, `induction-and-construction` in
  `combinatorics`, ~564 cruxes, plus free-text keyword sweep of all 2434) resembles a
  genuinely different **whole-problem** framing for stick-cutting/alternating-claim games beyond
  these two; this echoes rounds 6 and 8's same conclusion (three/two other candidate framings
  each collapse into already-open or already-dead items) — I did not find a fourth new candidate
  framing to add to that list.

### Distinct openings surfaced
1. (Not new, confirms existing understanding) The Case (i)/Case (ii) coupling means "general n"
   is not a distinct task — see headline finding. This reframes how the outliner should describe
   remaining work: not "close Case ii at m, THEN separately handle n≥4" but "close the aggregated
   lemma once, get all n for free."
2. (Cheap, low-risk) Re-verify (already essentially done by this report) that the true game
   value — not just the value against D_n — matches the conjectured closed form for n=1,2,3 via
   independent from-scratch exact game-tree code; useful as a fresh sanity check artifact if the
   outliner wants one, but not proof content.
3. (Possible technique import, not a framing) `aimo-0558`'s forced-inclusion/charge-to-skipped-element
   argument as an alternative proof shape for the Small-Gap Crossing-Domination Lemma — flagged,
   not pursued (out of scope for this lens; belongs to the m-general upper-bound gap).

### Candidate technique(s)
No new whole-problem technique found. The two load-bearing techniques remain: (a) the
D/M-operation formalism + strong induction on m (needs the aggregated OPT=NC lemma to close);
(b) the (now complete) superincreasing-invariant argument for the lower bound. The recursion
c(n)=2c(n-1)/(2c(n-1)+1) is confirmed to be *identical in content* to (a)'s Case-(i) step, not a
separate technique.

### Cheap-kill candidates
None obvious beyond what's already been tried (the population has already ruled out concavity,
strategy-stealing, generating-function/entropy reframings, Schur-convexity, and local-exchange
matching techniques in prior rounds). No new parity/pigeonhole/injection shortcut found for
either the Case (ii) gap or a "general n" shortcut.

### Knowledge-base entries to use
No new KB entries beyond what's already cited by the population (Lemma G/P, D/M reformulation,
superincreasing-dominance results). This dispatch found no KB entry not already in use.

### Analogous past problems (cruxes)
- `aimo-0117` — dyadic/superincreasing-dominance invariant-maintenance defense; corroborates
  (does not extend) the already-certified lower-bound machinery.
- `aimo-0558` — forced-inclusion-charged-to-a-distinct-skip argument for a bounded-gap max-excess
  selection; a genuinely untried proof shape for the Case (ii) aggregated lemma (not this lens's
  target, flagged for the upper-bound-focused explorer/outliner).
- No crux found that offers a genuinely different top-level framing for the whole theorem
  (general n or otherwise) beyond what rounds 6 and 8 already ruled isomorphic.

### Prior progress
See `current.md`: lower bound against `D_m` fully unconditional for every m (round 8 milestone,
and per this report's headline finding, this already covers every n — no separate n≥4 lower-bound
task exists). Upper bound: Case (i) and Case (ii) are coupled via one joint strong induction
(not independently generalizable, per this report's re-derivation of the round-3 finding); the
single remaining lemma is the aggregated Small-Gap Crossing-Domination Lemma
(`OPT(Y,p-1)=NC(Y,p-1)`, general Y,p), 2060+ trials support it, unproved.

### Dead ends (do not retry)
- The n-indexed recursion `c(n)=2c(n-1)/(2c(n-1)+1)` as an independent 5th approach/framing —
  confirmed (this round) to have zero leverage beyond what Case (i)'s existing mechanism already
  provides for the upper bound, and to be strictly subsumed by the already-certified
  non-inductive lower-bound result. (Originally declined round 5 for a weaker reason; now
  re-confirmed dead for a stronger, more precise reason.)
- All previously-logged dead ends (global concavity, strategy-stealing, generating-function/entropy
  reframings, Schur-convexity/self-similar-recursion/leave-alone-or-subdivide-matching framings,
  local pairwise uncrossing-exchange, bounded-lookahead induction-loading, sorted-adjacency and
  general non-crossing-matching+deletion conjectures, single-operation monovariance of g*) still
  apply — not retried, not re-examined in depth this round (out of this lens's scope).

### Small-case / intuition notes (conjecture only, not proof)
- Independent from-scratch exact game-tree computation (not reused code) confirms, for n=1,2,3,
  that the TRUE optimal Liu Bang opening (found by unconstrained local search over the whole
  simplex of openings, not just checked against D_n) converges to D_n itself and achieves exactly
  the conjectured `c(n)=2^n/(2^{n+1}-1)`. This is stronger circumstantial evidence than "D_n
  achieves the target" alone (already proved) — it's evidence no other opening beats D_n, i.e.
  supports the *upper* bound direction numerically, though only as local-search evidence at
  n=1,2,3 (n=4's unseeded search did not fully converge within the bounded iteration budget used
  here, so is inconclusive, not contradictory).
- The apparent tension between round-3's "Case i closed for every m" wording (in the approach
  file's own "Conclusion" prose, §2d) and the reviewer's contemporaneous overclaim correction is
  now precisely explained (see headline finding): the proof is correct as an inductive *step*
  but requires the full joint IH (both cases) at m-1, so by itself it doesn't establish
  "Case i for every m" as an independent fact — it only becomes unconditionally true once
  Case ii closes at every level too. This is not a new gap, just a clarified restatement of the
  existing one; flagging it so the outliner doesn't accidentally re-cite dyadic-cascade-induction's
  §2d "Conclusion" sentence as if it were unconditional.
