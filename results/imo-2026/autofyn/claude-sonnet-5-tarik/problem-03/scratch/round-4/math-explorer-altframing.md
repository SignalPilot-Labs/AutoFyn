## imo-2026-03

- Distinct openings (genuinely different top-level targets, not variants of Lemma
  G/P case-split induction on `a_1` vs `2a_2`):

  **(A) Global amortized potential / monovariant over the whole cutting DAG (top
  pick).** Instead of induction on recursion depth `m` with a Case (i)/(ii) split
  at every level (the mechanism all four current approaches share), define a
  single scalar potential `Φ` on an active multiset (e.g. a weighted variant of
  the certified gap-decomposition identity `e(M)=Σ_{i odd}(a_i-a_{i+1})`, or `Φ:=
  e(M) + λ·f(\text{multiset shape})` for some correction `f`) and prove directly
  that **no single D or M operation** (Lemma D/M, already certified) can move `Φ`
  below a hard floor, *regardless of which operation Xiang Yu (XY) picks* — i.e. a
  monovariant/amortized argument, not a "find the right policy" search. This
  targets the **universal-over-all-XY-strategies** direction (the lower bound:
  `D_m` resists every response) rather than the **existential** direction (the
  upper bound: some policy achieves the target) — these are logically different
  claims and the *lower*-bound one is exactly what a monovariant is naturally
  suited to (you never have to name XY's best move, only bound what any move can
  achieve). This would supersede `dyadic-cascade-induction`'s §5 Branch A/Branch
  B/"open multi-cut" three-way case split with **one** uniform argument. Crux
  provenance: `aimo-0196` (combinatorics/games-and-strategy) — B (the adversary)
  maintains a local "arc" potential (`N(alpha) ≤ 2ℓ-3`) that strictly decreases
  under ANY response from A, using a "just-used, so frozen this turn" trick to
  pin one boundary resource; the crux move ("define a size-weighted sub-window as
  a potential and show the adversary can always strictly lower it after any
  response," "run an integer monovariant that drops by a fixed amount regardless
  of the opponent's reply") is the transferable proof *shape*, not the subject
  matter (coins on a circle vs. stick pieces are unrelated). This is the strongest
  candidate to open as a new slug this round: it is honestly a different
  mechanism (no recursion-depth induction, no naming a policy), it targets a
  named still-open gap (`dyadic-cascade-induction §5.2`, "≥2 cuts inside the
  dominant piece"), and it does not require inventing new machinery beyond what's
  already certified (Lemma P / Lemma D/M supply the raw operation semantics; only
  the potential `Φ` itself is new). **Caveat, honestly stated:** no candidate `Φ`
  was derived or checked this round — this is a proof *shape* to try, not a
  result; the previous round's "merging monotonicity never increases `e`" general
  fix was tested and found FALSE (documented dead end, see below), so any `Φ`
  proposed must be checked against that exact counterexample family before being
  trusted.

  **(B) LP/majorization relaxation of XY's action space.** Relax XY's `≤m`
  discrete cuts to a continuous "resource-removal" adversary that can subtract
  any nonnegative real amount from any subset of pieces subject to a global
  budget, dominating (i.e. provably at least as powerful as) the true physical
  adversary. If domination holds, bounding the *relaxed* adversary's damage
  against `D_m` upper-bounds the true adversary's damage — turning the
  currently-open "≥2 cuts inside the dominant piece" casework into a Lagrangian/
  KKT-style continuous optimization solved in closed form, no case-split on where
  cuts land. This is dispatch candidate (a). No direct crux match was found in
  the corpus (`linear-algebra-method` and `extremal-principle` subtopics were
  searched; nothing subject-matter-analogous surfaced — the corpus's LP-flavored
  cruxes are all about *dimension-counting* or *F₂ linear systems*, not
  continuous majorization/relaxation of an adversary). Flagging this as
  plausible but **unverified and higher-risk than (A)**: making "the relaxed
  adversary dominates the real one" rigorous is itself nontrivial (a cut must
  produce two valid non-negative sub-pieces summing to the original — the
  relaxation would need to preserve that the *sum* of what's removed from a
  piece cannot exceed that piece's own value, which is exactly the same
  constraint structure the D/M framework already encodes combinatorially; it's
  not obvious the continuous relaxation is strictly easier to analyze than the
  combinatorial one that `potential-weighting-upper-bound` already built and
  found hard).

  **(C) Merge-tree / subtractive-Euclidean-algorithm framing.** Lemma D/M's two
  operations — `D(x)`: delete `x` (bisect-and-cancel), `M(x,y)`: replace `x,y`
  with `x-y` — are *literally* the subtractive Euclidean algorithm's step
  (`M`) plus a "kill a value against itself" step (`D`). This suggests recasting
  "minimize the final leftover using ≤n operations, starting from a
  superincreasing dyadic sequence" as a known extremal question about how many
  subtractive-Euclidean/continuant steps are needed to reduce a specific
  numerical sequence — connecting to continued fractions or Zeckendorf-style
  binary-representation bounds (the corpus has `aimo-0764`,
  "a fixed sum of powers of two needs at least as many terms as its binary
  weight," combinatorics/size-bounding-and-descent — only a loose structural
  echo, not a strong match; flagged as speculative). This is the most novel
  reframing (a different *domain of discourse* — number-theoretic reduction
  complexity rather than order-statistic game value) but also the least
  developed; no crux in the corpus directly matches "bound the min leftover of a
  bounded-length subtractive-Euclidean process on a superincreasing sequence." I
  would not open this as a build-set slug yet — it needs at least one round of
  scouting to see if the connection produces an actual usable inequality — but
  it is worth noting as a long shot distinct from (A)/(B).

  **(D) Restricted concavity, `a_1≥1/2` (the dispatch's item (d)) — checked, mild
  positive signal, but NOT a genuinely different framing; deprioritized.**
  Re-examined `concavity-minimax-duality`'s counterexample: the violating triple
  is `M_t=(1/2,t,1/2-t)` flanked by `p_1` (`a_1=12/25<1/2`) and `p_2`
  (`a_1=13/25>1/2`) — i.e. the violation straddles `a_1=1/2` and needs a point on
  *each* side, so restricting to `a_1≥1/2` removes `p_1` and this specific
  counterexample no longer applies within the restricted domain. I ran a fresh,
  independent numeric check (not reusing the disproved-file's numbers): an exact-
  `Fraction` computation of `g` via the vertex-lemma candidate move set (bisect /
  match, iterated 2 cuts deep — this proxy matches all 5 previously-certified
  exact values of `g` exactly, including the `M_t`/`p_1`/`p_2` counterexample
  values, so it's a trustworthy stand-in), tested against random pairs both with
  `a_1≥1/2` (denominators up to 30, thousands of pairs, midpoints also
  constrained to the sorted simplex and `a_1≥1/2`): **0/4329 violations found**.
  This is mild positive evidence the restricted-domain salvage is *plausible*,
  worth recording so no future round re-derives it from scratch — **but it is
  not a genuinely different framing from the field's shared wall**: it reuses
  the exact same machinery (the `F`-proxy piecewise-affine region table, edge-
  normal kink checks, Case (i)/(ii) region splitting) that
  `concavity-minimax-duality` already built and that already required the same
  kind of exhaustive casework the other three approaches use. Per CLAUDE.md's
  explicit guidance ("a bypass in the same framing hits the same wall one step
  later"), I recommend NOT prioritizing this as this round's "genuinely
  different" opening — it can be pursued in parallel by advancing
  `concavity-minimax-duality` itself (a revision, not a new slug) if the
  outliner wants a cheap, low-risk, narrow-scope task, but it should not be
  billed as the diversifying move CLAUDE.md is asking for this round.

- Candidate technique(s): amortized potential/monovariant argument (KB:
  "Invariants & monovariants," Combinatorics section) is the primary
  recommendation; LP/majorization relaxation is a secondary, higher-risk
  candidate; the Euclidean-algorithm/continuant reframing is a speculative third
  option not yet ready to build.

- Cheap-kill candidates: before investing in (A), check whether the natural
  first-guess potential `Φ(M) := e(M)` itself (no weighting) already satisfies
  "no single D/M op decreases it below the target" — this is essentially what
  the "merging never increases `e`" monotonicity lemma tested and refuted in
  round 3 (see Dead ends below), so the unweighted guess is already known dead;
  any real potential for (A) must be a genuinely weighted/corrected version, not
  raw `e`. For (B), a one-line sanity kill: check whether the continuous
  relaxation's unconstrained optimum ever requires removing more than a piece's
  own value from it (if so, domination fails trivially and the relaxation needs
  an extra constraint before it's even well-posed) — worth 5 minutes before
  committing a full round to it.

- Knowledge-base entries to use: "Invariants & monovariants" (Combinatorics
  section, `knowledge_base.md` line 117) for candidate (A); "Meta-Strategy" /
  "Problem-Solving Heuristics" generic reformulation advice ("translate to
  another domain") for candidate (C); no KB entry directly covers LP/majorization
  relaxation of an adversary — candidate (B) would need to be built from
  scratch, citing only elementary Lagrangian/optimization facts if attempted.

- Analogous past problems (cruxes):
  - `aimo-0196` (combinatorics/games-and-strategy) — **the strongest, most
    genuinely-analogous match found this round.** Crux moves: "For the
    lower-bound half, define a size-weighted sub-interval as a potential and
    show the adversary can always strictly lower it after any response" and
    "Run an integer monovariant equal to a deficient window's coin total: drain
    it by a fixed amount while the opponent's reply can push back strictly less."
    Structurally analogous in *proof shape* (adversarial two-player process,
    lower-bound direction proved via a local potential that any opposing move
    cannot fully restore, using a "frozen/just-used resource" trick to prevent
    the opponent's best possible counter) though the underlying combinatorial
    objects (coins on a circle vs. stick pieces under D/M operations) are
    unrelated — a hint to *adapt*, not a citation, per CLAUDE.md.
  - `aimo-0117` (combinatorics/games-and-strategy) — already used in round 1 for
    the dyadic-superincreasing *construction* idea (do not re-cite as new; noted
    here only to confirm it's not a fresh lead for this round's "whole new
    framing" ask — its crux move (assign values as a two-sided geometric
    sequence so the top value beats the sum of the rest) is about *building* the
    construction, not about a genuinely different proof mechanism for the
    *resistance* (lower-bound) direction, which is what's actually still open).
  - `aimo-0560` (combinatorics, min-max board game, "surrogate adversary
    dominates the true one") — checked in detail; the crux move ("replace the
    adversary with a strictly stronger surrogate whose reply is pointwise at
    least as damaging") is the right *shape* for candidate (B) but the problem
    itself (gardener/lumberjack tree-growing on a grid) has essentially no
    structural overlap with the stick-cutting game beyond "alternating adversary,
    determine the max the mover can guarantee" — a shape-only hint, not a strong
    match; do not expect to transplant technique details.
  - `aimo-0764` (size-bounding-and-descent) is a loose, speculative echo for
    candidate (C) only (binary-weight/popcount lower bound) — flagged as "worth
    a look if (C) is pursued," not a confirmed analogy.

- Prior progress: see `results/imo-2026-03/current.md` — n=1 fully solved;
  n=2 upper bound fully solved (both cases); n=3 Case (i) upper bound proved;
  lower-bound Branch A (XY never touches `a_1`) and Branch B (single cut on
  `a_1`) fully proved for every `m`; Lemma G, Lemma P, Lemma D/M, "dominant
  extraction" Facts 1&2, and non-concavity-of-`g`-at-n2 all certified. None of
  this round's three new framings (A/B/C) build directly on top of these
  results beyond re-using the certified Lemma P / Lemma D/M machinery as raw
  operation semantics — they propose a different top-level *mechanism* for the
  still-open gaps, not a continuation of the existing induction.

- Dead ends (do not retry): (1) global concavity of `g` at n=2 — proven FALSE,
  exact counterexample `g(1/2,t,1/2-t)=0` vs `g=1/25` nearby (certified,
  `lemmas/non-concavity-of-g-at-n2.md`); (2) both natural single-step greedy
  D/M policies (Rule 1 "top-two ratio test," Rule 2 "match smallest gap") are
  falsified with exact counterexamples (`potential-weighting-upper-bound.md`)
  — this is why candidate (A) explicitly avoids trying to name a policy at all;
  (3) a "merging never increases `e`" general monotonicity lemma, the natural
  first guess for closing the multi-cut lower-bound gap, was tested and found
  FALSE by random search (`dyadic-cascade-induction §5.2`) — so candidate (A)'s
  potential `Φ` cannot simply be raw `e`; it needs a genuine correction term,
  and any proposed `Φ` should be checked against whatever specific
  configuration refuted the monotonicity lemma before being trusted; (4)
  strategy-stealing from the upper-bound proof to the lower-bound direction is
  a non-sequitur (confirmed round 3); (5) extending Case (i)'s "for every m"
  claim past `m=3` without first closing Case (ii) at every lower level is
  circular (round 3 overclaim, corrected by the reviewer).

- Small-case / intuition notes: (conjecture, from a fresh independent numeric
  check this round, not reused from prior rounds) the restricted-domain
  concavity salvage `g` concave on `\{a_1\ge1/2\}` at n=2 shows **0 violations
  in 4329 random exact-fraction test pairs** using a vertex-lemma-based proxy
  for `g` that independently reproduces all 5 previously-certified exact values
  of `g` — mild positive evidence only, not a proof, and not prioritized as
  this round's genuinely-different opening (see item (D) above for why). No
  small-case computation was done for candidates (A)/(B)/(C) this round — they
  are proof-shape proposals, not yet reduced to a testable closed-form
  inequality; the outliner/next builder should derive a concrete candidate `Φ`
  (for A) or a concrete relaxed-adversary formulation (for B) before any
  numeric verification is possible.
