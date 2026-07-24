## Goal

Solve IMO 2026 P6 (benchmark id `imo-2026-06`, number_theory, difficulty_rating 9/hard).

Statement: Let a_1, a_2, a_3, ... be an infinite sequence of positive integers greater than 1.
Suppose that for all positive integers n, a_{n+1} is the smallest positive integer greater than
a_n such that gcd(a_{n+1}, a_i) > 1 for every i=1,...,n. Prove that there exist positive integers
T and L such that a_{n+T} = a_n + L for every positive integer n (eventual periodicity of the gap
sequence).

Metric: `results/imo-2026-06/current.md` `## Status` field (unsolved | partial | solved), gated by
proof-reviewer APPROVE for `solved`.
Eval: read `results/imo-2026-06/current.md` and `results/imo-2026-06/approaches/.ranking.json` each
round.
Baseline (round 1 start): unsolved, empty approach population.
Target: Status = solved, with proof-reviewer APPROVE and a complete rigorous proof in
`## Full proof` of current.md.
Constraint: one problem only (imo-2026-06) for the whole run; keep approaches diverse in framing
per CLAUDE.md (not just technique variants).

## Goal Updates

## Eval History (round 28 addition)

- Round 28: Status partial -> partial overall, but **8th APPROVE of the
  run**: `a1-11q-subfamily-theorem` solved and certified — literal T=1,L=11
  periodicity for the FULL a_1=11q subfamily (all primes q>11 outside
  Bad(11)={13,17,19,31,37,43}), instantiating the certified p-uniform
  machinery at p=11, exactly mirroring the a1-5q/a1-7q closure pattern (90
  cells, 76 below-threshold triples, 6 diagonal exceptions, 29 k>=1
  quadruples reduced to 5 non-moot witnesses). 3 math-explorers (a1-pq
  r-generalization lens, subfamily-extension candidate lens, H2 direct-
  attack lens) -> found: (1) new closed form gcd(N,a_n)=gcd(j,(k+1+
  c(p,j,r)) mod j) with c(p,j,r)=s_0(j,r)*p^{-1} mod j q-independent,
  proving r=1 is the UNIQUE residue giving unconditional k=0 closure
  (structural, not just empirical, explanation); (2) a1=9q already
  subsumed by certified a1-3aq(a=2); a1=11q found build-ready with fresh
  Bad(11) table; a1-3qk m=4 reconfirmed false/no cheaper strategy; (3)
  H2's "N(S_0)=0 direct attack" found to be STALE — round 19's Prop 3
  already proves no finite-data method can ever resolve it; large-scale
  resimulation (700k-750k terms, 3 seeds) found nothing new, mild caution
  flag on 11305 near-flattening. -> 1 proof-outliner (new a1-11q-
  subfamily-theorem; revised a1-pq-subfamily-theorem with the r-
  generalization result; parked H2/H1 generic search) -> 1 outline-
  reviewer (independently reproduced Bad(11) and the closed-form/
  uniqueness claims; build set = a1-11q-subfamily-theorem, a1-pq-
  subfamily-theorem) -> 2 proof-builders (parallel) -> 1 proof-reviewer
  (independently re-derived/re-simulated both from scratch, tens of
  thousands of instances checked). Verdicts: a1-11q-subfamily-theorem
  **APPROVE (solved)** — the run's 8th APPROVE. a1-pq-subfamily-theorem
  CHANGES REQUESTED (partial) — new certified Universal Look-Back Closed
  Form + Uniqueness-of-r=1 Theorem (proved for ALL r via a single
  universal witness band j=p-1, not spot-checked), a genuine bookkeeping
  narrowing but does not close any new (j,r,k) cell; r=1 k>=1 residual
  and general r!=1 closure both remain open. 1 new lemma certified
  (universal-look-back-closed-form-and-r1-uniqueness). Run now stands on
  **8 fully certified solved sub-family theorems** (2|a_1; a_1=p^k;
  a_1=3q; a_1=3q^2; a_1=3q^3; a1-3aq a=1-5; a1-5q; a1-7q; a1-11q), plus
  the gap-free Master Conditional Theorem reducing full generality to H1
  (FAH, 22nd consecutive plateau round, 6-28) + H2 (absorption-chain
  termination, now confirmed structurally unattackable via finite data
  per round-19 Prop 3).

## Eval History (round 27 addition)

- Round 27: Status partial -> partial overall, but **7th APPROVE of the
  run**: `a1-7q-subfamily-theorem` solved and certified — literal T=1,L=7
  periodicity for the FULL a_1=7q subfamily (all primes q outside
  Bad(7)={11,13}), instantiating the certified p-uniform machinery at
  p=7, exactly mirroring the a1-5q closure pattern. 3 math-explorers
  (a1-7q build-readiness lens, covering-system 11305/x_2=103 follow-up
  lens, H1 fresh-corridor lens) -> found: (1) a1-7q fully build-ready,
  Bad(7)={11,13} independently confirmed, zero new obstruction types; (2)
  applying the certified Finite-Window Literalization Lemma to seed
  a_1=11305's witness x_2=103 is a routine reapplication (order-swapped
  relabeling needed: n_B=4 < n_A=7, opposite of a_1=4807), closes
  residual class d=103 for that single seed; (3) 2nd consecutive
  dedicated H1/FAH fresh-corridor search (rounds 26-27) finds nothing new
  — corridor-hunting at current technique level likely exhausted; the one
  new crux check (aimo-0907 orbit-merging) dies for the same reason as
  the already-dead orbit-merging-additive-offset-dichotomy mechanism. ->
  1 proof-outliner (advance a1-7q to full build; light housekeeping
  advance to covering-system-construction for 11305; new r=1 sub-target
  for a1-pq-subfamily-theorem exploiting that j never equals 1 so no
  diagonal band exists in that residue class; kept a1-3qk m=4 low
  priority) -> 1 outline-reviewer (independently verified the p=7 table,
  Bad(7)={11,13} via full greedy resimulation, the r=1 diagonal-
  elimination algebra across p=5,7,11,13, and the 11305 reapplication;
  build set = a1-7q-subfamily-theorem, a1-pq-subfamily-theorem,
  covering-system-construction) -> 3 proof-builders (parallel) -> 1
  proof-reviewer (independently re-derived/re-simulated all 3 from
  scratch). Verdicts: a1-7q-subfamily-theorem **APPROVE (solved)** — the
  run's 7th APPROVE, zero gaps found. a1-pq-subfamily-theorem CHANGES
  REQUESTED (partial) — new certified Universal Look-Back Witness
  Identity (gcd(N,a_i)=gcd(p(n-i)+j, q+i-1), general for all r) proved,
  with its r=1 corollary showing k=0 is ALWAYS safe (unconditionally,
  no per-p computation) via the exact formula gcd(k+1,j); residual
  k>=1 with gcd(k+1,j)>1 honestly left open, requiring the pre-existing
  per-p sieve machinery. covering-system-construction CHANGES REQUESTED
  (partial) — a_1=11305's d=103 residual class now closed (literal Joint
  FAH), giving TWO standing hard seeds (4807, 11305) both fully resolved
  via this lemma; explicitly scoped as dual-seed, not general. 1 new
  lemma certified (universal-look-back-witness-identity). Run now stands
  on **7 fully certified solved sub-family theorems** (2|a_1; a_1=p^k;
  a_1=3q; a_1=3q^2; a_1=3q^3; a1-3aq (a=1-5); a1-5q; a1-7q = 7 total
  APPROVEs across families), plus the gap-free Master Conditional Theorem
  reducing full generality to H1 (FAH, 21st consecutive plateau round,
  6-27) + H2 (absorption-chain termination).

## Eval History (round 26 addition)

- Round 26: Status partial -> partial overall, but **6th APPROVE of the
  run**: `a1-5q-subfamily-theorem` solved and certified — literal T=1,L=5
  periodicity for the FULL a_1=5q subfamily (all primes q outside
  Bad(5)={7,13,19}), instantiating the certified p-uniform machinery
  (Generalized K_0-Boundedness, gcd-difference Witness Lemma, Legendre
  Sieve Gap Bound, Primorial Floor Bound) at p=5, exactly mirroring the
  a1-3q closure pattern. 3 math-explorers (Bad(p) pinning lens, a1-3qk
  m=4 lens, H1 fresh-corridor lens) -> found: (1) Bad(5)={7,13,19} and
  Bad(7)={11,13} confirmed, no new obstruction type vs p=3, ready to
  build; (2) a1-3qk m=4 hit a GENUINE counterexample (q=17,k=0: sequence
  provably fails to resettle to constant gap 3) plus an infeasible
  ~2x10^11 verification threshold — correctly held out of the build set,
  do not force m=4 as originally stated; (3) H1/FAH fresh-corridor sweep
  found nothing concrete — 20th consecutive plateau round on the main
  crux -> 1 proof-outliner (field of 4: a1-5q-subfamily-theorem revise,
  new a1-7q-subfamily-theorem, a1-pq-subfamily-theorem advance targeting
  a new Minimal-Window Necessity Conjecture, covering-system-construction
  advance on seed 4807's d=13 residual class) -> 1 outline-reviewer
  (independently verified Bad(5)/Bad(7) and the minimal-window
  corroboration on all 6 known exceptions; fixed 3 stale/missing approach
  files; build set = a1-5q-subfamily-theorem, a1-pq-subfamily-theorem,
  covering-system-construction; a1-7q held out as lower priority/untraced)
  -> 3 proof-builders (parallel) -> 1 proof-reviewer (independently
  re-derived/re-simulated all 3 from scratch). Verdicts: a1-5q-subfamily-
  theorem **APPROVE (solved)** — the run's 6th APPROVE. a1-pq-subfamily-
  theorem CHANGES REQUESTED (partial) — 2 new certified lemmas (Diagonal
  Characterization s_0(j,r)=1 iff j=r; First-Risk Theorem, verified on
  282k tuples) but the full Minimal-Window Necessity Conjecture remains
  open (a concrete isolated non-diagonal counterexample construction
  shows the naive argument doesn't close, though it's never the actual
  first deviation in practice — the "why" is still a gap).
  covering-system-construction CHANGES REQUESTED (partial) — new
  certified Finite-Window Literalization Lemma fully closes the d=13
  residual class for the single standing seed a_1=4807 (literal, not just
  cofinite, Joint FAH now proven for that one seed), but honestly scoped
  as single-seed, not a general theorem; flagged as immediately
  re-applicable to a_1=11305 next round. 3 new lemmas certified. Run now
  stands on **5 fully certified solved sub-family theorems** (2|a_1;
  a_1=p^k; a_1=3q; a_1=3q^2; a_1=3q^3) PLUS a1-3aq (a in 1..5) PLUS
  a1-5q = **6 total APPROVEs**, plus the gap-free Master Conditional
  Theorem reducing full generality to H1 (FAH, 20th consecutive plateau
  round, 6-26) + H2 (absorption-chain termination).

## Eval History (round 22 addition)

- Round 22: Status partial -> partial overall, but **THIRD APPROVE of the
  run**: `a1-3q-subfamily-theorem` solved and certified — literal T=1,L=3
  periodicity for the FULL a_1=3q subfamily (all primes q>=7, q!=5),
  unconditional, no FAH/H1/H2 machinery needed. The long-standing Case (b)
  n-even k>=1 gap was closed not via the anticipated Chebyshev/binomial
  chain but via a simpler direct sieve counting argument: new certified
  Legendre Sieve Gap Bound (g(M)<=2^ω(M)(ω(M)+1), inclusion-exclusion) +
  Primorial Floor Bound (ω(M)=r => M>=(r+1)!), reducing the residual band to
  k in {1,...,11} and then to exactly 3 boundary cases (2 hand-checked, 1
  free via q|K), all resolved. Reviewer independently re-derived every step
  from scratch (own sieve/primorial proofs, own 18-entry table, 3 fresh
  simulations) and found zero gaps — both lemmas promoted from
  certified-candidate to certified
  (lemmas/legendre-sieve-gap-bound.md, lemmas/primorial-floor-bound.md). 3
  math-explorers (Jacobsthal citable-literature lens, FAH-seed-deepening
  lens, fresh-framing lens) -> found: (1) no citable elementary sieve result
  exists in KB/crux corpus for the Jacobsthal-type bound, and no
  bounded-ω(M) structural shortcut works (refuted), but the "write out a
  real sieve argument from scratch" path was assessed finishable — this
  turned out correct; (2) the last inconclusive fah-counterexample-hunt seed
  (a_1=105945) is now RESOLVED clean (exact period T=109096,L=570570 found
  via a new Z-function-based O(N) exact-period detector, zero violations
  across ~5.6 periods) — record now 12/12 seeds with no FAH counterexample;
  its structural §1.3(a) invariant-proof pivot assessed not viable (no
  candidate invariant exists); (3) fresh-framing lens found ONE genuinely
  new H1 candidate surviving the ambient-statistic-obstruction pre-screen:
  "orbit-merging/additive-offset dichotomy" adapted from crux aimo-0907 —
  built and tested this round (see below), now confirmed dead too. ->
  1 proof-outliner (new orbit-merging-additive-offset-dichotomy targeting
  H1; revised a1-3q-subfamily-theorem with Option (a)/Option (b) paths;
  fah-counterexample-hunt held out of build set, no live next step) -> 1
  outline-reviewer (verified orbit-merging genuinely distinct from all 30+
  dead H1 mechanisms, required a disambiguation check as builder's first
  deliverable; flagged a1-3q's Option (a) Step 3 as an unverified sketch,
  told the builder to pivot to Option (b) if it stalled; build set = both)
  -> 2 proof-builders (parallel) -> 1 proof-reviewer. Verdicts:
  a1-3q-subfamily-theorem **APPROVE (solved)** — the run's 3rd APPROVE.
  orbit-merging-additive-offset-dichotomy RETHINK (unsolved) — the mandatory
  disambiguation check FAILED concretely: both candidate offset-object
  instantiations collapse, one into the already-dead existential-to-
  universal mechanism family (and mistargets H2 not H1), the other into an
  object whose well-definedness is itself EQUIVALENT to the full periodicity
  conclusion — a stronger circularity than the round-5 reversible-
  transition-map precedent (that was merely equivalent to gap †; this is
  equivalent to the theorem itself). Independently reconfirmed by the
  reviewer via a fresh a_1=385 simulation. 31st+ FAH mechanism now dead. Run
  now stands on **3 fully certified solved sub-family theorems** (2|a_1;
  a_1=p^k; a_1=3q) plus the gap-free Master Conditional Theorem reducing the
  fully general case to H1 (FAH, 17th consecutive plateau round now, 6-22)
  + H2 (absorption-chain termination).

## Eval History (round 21 addition)

- Round 21: Status partial -> partial. PLATEAU on main FAH crux (H1, 16th
  consecutive round, 6-21) but two genuinely productive negative/diagnostic
  results and a new reusable tool. 3 math-explorers (Jacobsthal-bound lens
  for the a1-3q gap, 6th fresh-whole-problem-framing sweep for H1,
  audit/4th-subfamily-scouting lens) -> found: (1) no off-the-shelf
  Jacobsthal tool in KB/crux corpus, but a crude elementary g(M)<=2^ω(M)
  bound plus a q-independent uniformity argument looked like a tractable
  path to close a1-3q's last gap; (2) 6th fresh-framing sweep found NOTHING
  new for H1 (Kolmogorov complexity, martingale/optional-stopping, renewal
  theory, return-words/Rauzy graphs, coding theory, combinatorial game
  theory all dead/inapplicable) but surfaced a useful meta-filter
  (ambient-statistic-obstruction kills ANY framing not reading realized
  occupancy data, regardless of vocabulary) and flagged one genuinely
  untried idea: a dedicated FAH-counterexample hunt (falsification-seeking,
  not proof-seeking); (3) audit confirmed Master Conditional Theorem chain
  still gap-free, found a_1=p^2*q reduces to the same open gap (not a new
  subfamily), recommended committing to the floor deliverable -> 1
  proof-outliner (revised a1-3q-subfamily-theorem with the Jacobsthal-bound
  outline; new fah-counterexample-hunt approach; light optional touch to
  n1-periodicity-reconciliation) -> 1 outline-reviewer (verified the
  uniformity fix IS q-independent and resolvable, but found the underlying
  g(M)<=2^ω(M) elementary proof itself is more fragile than portrayed —
  constructed a concrete counterexample to the naive "two-halves induction"
  sketch; confirmed fah-counterexample-hunt targets genuinely untried |Q|>=3/
  CRT-lopsided territory; build set = a1-3q-subfamily-theorem,
  fah-counterexample-hunt; n1-periodicity-reconciliation deferred) -> 2
  proof-builders (parallel) -> 1 proof-reviewer (independently re-derived/
  re-simulated everything from scratch with fresh scripts). Verdicts:
  a1-3q-subfamily-theorem CHANGES REQUESTED (partial) — uniformity fix
  (Step 4) confirmed valid and q-independent; but Step 1 (crude Jacobsthal
  bound) genuinely resists elementary proof — reviewer independently hit
  the same two walls (halving-induction collision; AP-peel reproducing only
  the insufficient radical bound); new adversarial CRT seed (q=40153,
  k=3335, K=10010) independently confirmed, minimal witness offset exactly
  10 (not a small universal constant) — the "witness always found early"
  observation is a confirmed search-depth artifact, not evidence of an easy
  bound. Gap now precisely: this needs real (non-elementary) Jacobsthal-
  function-level number theory, or a fundamentally different argument — not
  a routine finishing touch. fah-counterexample-hunt RETHINK (unsolved,
  clean honest negative, not a criticism) — tested 11 fresh seeds (|Q|=3,4,5,
  CRT-lopsided) at 150k-500k terms, zero FAH counterexamples found;
  discovered and reviewer-reverified (3rd independent script) a new "direct
  literal-period detection" technique, giving exact (T,L) for a_1=385 (new)
  and 2 of the 4 canonical hard seeds (187,221) plus an EXACT one-full-period
  FAH check at a_1=385 (zero violations) — a genuinely new reusable tool for
  future rounds, not previously documented. One seed (105945) inconclusive
  (T<25000 search found no period), reviewer recommends deepening that
  search or pivoting to the outline's structural non-intersection-invariant
  proof next round rather than more undifferentiated seed sweeps. No new
  lemma certified this round (both results negative/diagnostic per the
  Lemma F/I precedent — do not force-certify diagnostic non-results). Run
  still stands on 2 fully certified solved sub-family theorems (2|a_1;
  a_1=p^k) plus the gap-free Master Conditional Theorem; a1-3q remains the
  most concrete near-term 3rd-APPROVE target but now has a precisely
  diagnosed non-elementary obstruction rather than an open-ended gap.

## Eval History (round 20 addition)

- Round 20: Status partial -> partial. IMPROVED (5 new lemmas certified,
  including a genuinely NEW general-purpose negative screen; 15th
  consecutive plateau round on the main FAH crux itself, 6-20, but
  substantial narrowing on 3 fronts and one dead mechanism cleanly
  retired). 3 math-explorers (singleton-witness non-closed-form mechanism
  lens, 5th fresh-whole-problem-framing sweep, write-up/insurance audit
  lens) -> found: (1) new elementary "Constrained Singleton Coherence"
  mechanism sidestepping the round-19 sieve/density dead end; (2) 5th
  fresh-framing sweep found NOTHING new for H1 (priority-argument/
  computability, o-minimality, nonstandard-analysis/model-theory, spectral/
  operator all collapse into dead/inapplicable) but yielded a useful
  general screening rule (deterministic-recursion argument premised on
  "two legal continuations" is invalid without an explicit construction);
  (3) audit confirmed Master Conditional Theorem chain gap-free, and found
  a promising candidate 3rd subfamily a_1=3q (q prime !=5) with strong
  numeric support -> 1 proof-outliner (field of 4: revise
  triangle-consistency-pigeonhole with the Constrained Singleton Coherence
  reframing; copy triangle-critical-dichotomy-witness targeting the same
  narrowed gap via Critical Prime Dichotomy Lemma's "sole rescuer" branch;
  new a1-3q-subfamily-theorem; advance n1-periodicity-reconciliation to
  fix round 19's circularity + tighten floor write-up) -> 1 outline-reviewer
  (found the outliner hadn't actually written 2 of the 4 approach files —
  seeded them itself from the outline text; verified triangle-critical-
  dichotomy-witness is genuinely distinct from its sibling, not a
  single-gap-trap duplicate; falsified the a1-3q outline's proposed witness
  mechanisms (a_2 alone, {a_2,a_3} pair) but found the true minimal witness
  index stays small (<=5), handed to builder as a corrected lead; build set
  = all 4) -> 4 proof-builders (parallel) -> 1 proof-reviewer (independently
  re-derived and re-simulated everything from scratch). Verdicts:
  triangle-consistency-pigeonhole CHANGES REQUESTED (partial) — proved and
  certified Constrained Singleton Coherence Lemma + corollaries
  (unconditional), but found the "prime-power dominant class" pattern
  numerically observed is a CONFOUND — fully explained by pre-existing
  Cofinite-FAH witnesses at both known hard seeds (4807, 11305), not
  independent evidence; failed to construct a fresh non-confounded hard
  seed after ~70-seed heuristic scan; reduction argument shows the
  sharpened target doesn't evade round 19's obstruction after all — same
  missing ingredient restated. triangle-critical-dichotomy-witness RETHINK
  (unsolved) — proved and certified the new **Universal Branch-(a)
  Dominance Theorem** (a_n/p^e <= a_{n-1} unconditionally for any prime
  p|a_n), showing the Critical Prime Dichotomy Lemma's branch (b) "sole
  rescuer" NEVER fires, for any index/prime/core — kills this mechanism at
  the root, confirmed on thousands of instances; honest negative result,
  recommend retirement of this slug. a1-3q-subfamily-theorem CHANGES
  REQUESTED (partial, NOT solved) — closed odd-n case via a clean parity
  witness (gcd(a_n+2,a_n)=gcd(a_n+2,2)); closed-form analysis of the first
  Case-(b) occurrence pins exceptions to q=7,11 (both resolved by hand) and
  precisely explains why q=5 fails (witness window size exactly 1, that
  candidate provably fails); genuine open gap: Case (b) for even n, k>=1
  occurrences after the first — naive pigeonhole bound proven too weak via
  an adversarial CRT construction, likely needs a non-elementary
  Jacobsthal-type gap theorem. n1-periodicity-reconciliation CHANGES
  REQUESTED (partial) — round 19's circular Generalized Class-Blindness
  Obstruction WITHDRAWN (not just retracted) and replaced with a correctly,
  narrowly-scoped non-circular **Ambient-Statistic Obstruction** (unifies
  only the two already-certified predecessors, Escape-Cost Vacuity +
  Density-Argument Vacuity Corollary; explicitly does NOT rule out
  occupancy-referencing statistic families); floor-deliverable write-up
  tightened (Theorem A/B inline, Master Conditional Theorem, dead-mechanism
  summary by family not just count). 5 new lemmas certified:
  constrained-singleton-coherence-lemma, universal-branch-a-dominance-
  theorem, a1-3q-parity-and-k0-window-lemmas, ambient-statistic-obstruction,
  vacuous-fah-under-2-divides-a1-corollary. Main FAH crux (H1) and H2 both
  remain unresolved; run still stands on 2 fully certified solved
  sub-family theorems (2|a_1; a_1=p^k) plus the gap-free Master Conditional
  Theorem, now with a live near-complete 3rd candidate subfamily (a_1=3q)
  one gap away from a 3rd APPROVE.

## Eval History (round 18 addition)

- Round 18: Status partial -> partial overall, but **second APPROVE of the run**:
  `prime-power-seed-periodicity-theorem` solved and certified for the full
  a_1=p^k subfamily (any prime p, any exponent k>=1) via a self-contained
  strong induction generalizing the p=2 special case — T=1,L=p literal from
  n=1, no FAH/H1/H2 machinery needed. Reviewer independently re-derived and
  re-tested on 19 seeds outside the builder's set (p=29,31,37,41; k up to 10),
  exact match. Certified lemmas/prime-power-seed-literal-periodicity-theorem.md.
  3 math-explorers (NTBT/H2 numeric-resolution lens, fresh whole-problem-framing
  lens, audit/insurance lens) -> the NTBT lens resolved round 17's flagged
  candidate exception (a_1=255255, type {5,7,11,13,17} recurs at n=135914,
  triple-independently confirmed by 3 different scripts across explorer/
  outline-reviewer/proof-reviewer) — zero open numeric counterexamples to
  NTBT remain now; the fresh-framing lens found a genuinely new corridor for
  the main FAH crux via crux corpus aimo-0866/aimo-0421 (ISL 2021 N8)'s
  triangle-consistency/nested-pigeonhole technique on the complete graph of
  pairwise gcd>1 (Free Facts Lemma) -> 1 proof-outliner (new
  triangle-consistency-pigeonhole targeting FAH; revise self-absorbing-by-
  construction with the NTBT correction; new prime-power-seed-periodicity-
  theorem; advance n1-periodicity-reconciliation with 2 negative findings) ->
  1 outline-reviewer (CHANGES REQUESTED the triangle approach's cheap-kill
  scoping pre-build — required re-scoping to genuine hard rogue pairs, not
  easy base-Q-type pairs; APPROVE'd the other 3; build set = all 4) -> 4
  proof-builders (parallel) -> 1 proof-reviewer. Verdicts:
  prime-power-seed-periodicity-theorem APPROVE (solved, scoped); the other 3
  all CHANGES REQUESTED/partial. triangle-consistency-pigeonhole: original
  outline mechanism (Cross-Witness Common-Prime Lemma) proved DEAD (new
  certified negative result, Same-Type Triangle Vacuity — the shared type's
  own in-core primes fully explain any gcd>1 hit, carrying zero out-of-core
  information) but the builder discovered a genuinely new positive mechanism,
  the **Two-Sided Singleton Witness Theorem**: applying Singleton-Side FAH
  with ANY witness occurrence (not just the canonical/earliest) on both sides
  gives Cofinite FAH when matching singleton out-of-core signatures exist;
  fully explains BOTH known hard rogue-pair test seeds (a_1=4807, 11305) with
  zero exceptions, independently reconfirmed by reviewer. Residual open gap:
  existence of matching singleton witnesses in general — reviewer confirmed
  this is honestly distinct from (not a restatement of) the main FAH crux, a
  real narrowing. This is the 18th/19th FAH mechanism area but the FIRST in
  many rounds to leave behind a positive (not just negative) certified
  result plus a genuinely narrower open residual — the strongest FAH-crux
  progress since round 9-10. self-absorbing-by-construction: NTBT correction
  recorded, H2 counting/pigeonhole corridor confirmed fully exhausted (3
  sub-routes all dead). n1-periodicity-reconciliation: 2 new negative
  findings recorded (odd-prime p|a_1 does NOT trivialize FAH like 2|a_1 does
  — counterexample a_1=15,45, persistent period-4 base-type alternation,
  75%/25% not cofinite; |Q|=2 confirmed intractable as a general subfamily,
  36-seed sweep reproduces the same canonical hard seeds since round 6). Run
  now has 2 certified solved sub-family theorems (2|a_1; a_1=p^k) plus the
  gap-free Master Conditional Theorem reduction of the general case to H1
  (FAH)+H2 (absorption-chain termination), with H1's open residual now
  sharpened to "existence of matching singleton witnesses" rather than the
  full original crux.

## Eval History (round 19 addition)

- Round 19: Status partial -> partial. PLATEAU (14th consecutive round, 6-19,
  with no proof of the main FAH crux itself; all 4 built slugs CHANGES
  REQUESTED, no APPROVE), but real narrowing on 3 fronts plus one important
  circularity CAUGHT before certification. 3 math-explorers (singleton-witness-
  existence lens, fresh whole-problem framing, H2/subfamily lens) -> 1
  proof-outliner (revise n1-periodicity-reconciliation as consolidation/
  insurance + new meta-obstruction; revise triangle-consistency-pigeonhole to
  attack the Two-Sided Singleton Witness Theorem's existence hypothesis via an
  anatomy-of-integers/density style; revise core-growth-monotonicity to attack
  weaker H2 target "some self-absorbing S* exists"; advance
  self-absorbing-by-construction with 2 new adversarial NTBT seeds) -> 1
  outline-reviewer (APPROVE all 4, verified against explorer reports and
  approach files, no repackaged-dead mechanisms) -> 4 proof-builders (parallel)
  -> 1 proof-reviewer. Explorer findings: a_1=p*q DEFINITIVELY REFUTED as a
  tractable clean-periodicity subfamily (p=13,q=47 messy while q=43,53+ clean,
  no monotone threshold; q>=2p not sufficient either — do not re-propose this
  subfamily); singleton-witness existence hypothesis tested on 7 new seeds with
  0 counterexamples, but flagged as weak evidence (near-statistically-
  inevitable at easy under-recruited cores, not the 2 genuinely hard
  properly-recruited cores); fresh-framing sweep (p-adic/algebraic NT,
  generating functions, probabilistic/Borel-Cantelli, extremal graph theory,
  finite-Fourier/character-sums) found NO new corridor for FAH — 4th
  consecutive dead fresh-framing sweep (rounds 13,15,17,19). Builder/reviewer
  outcomes: n1-periodicity-reconciliation's new "Generalized Class-Blindness
  Obstruction" meta-lemma (meant to kill the ENTIRE statistical-method family
  for FAH in one argument) was NOT certified — reviewer found a genuine
  circularity (its "two scenarios agree" step asserts what needs an actual
  construction of two divergent legal continuations); the floor-deliverable
  audit (§8, citing the 2 certified subfamily theorems) is correct.
  triangle-consistency-pigeonhole: honest negative result — the anatomy-of-
  integers/density attack on the singleton-witness existence hypothesis FAILS
  even at the weakest "infinitely often" sub-target, with a precisely located
  NEW obstruction (no closed-form/CRT-independent local densities exist for
  the adaptively-defined persistent-type index set — classical sieve methods
  structurally inapplicable here); new elementary ω(a_n)=O(log n) bound
  certified (elementary-omega-bound.md). core-growth-monotonicity: new
  Monotone Chain Reformulation Lemma proved and certified (monotone-chain-
  reformulation-lemma.md) but its own attack on the weaker H2 target hits the
  SAME Proposition-3 non-constructivity wall a third time — confirmed dead
  end for this specific sub-target, though noted the weaker target is not
  actually new content (verbatim the standing sub-gap (a) of the
  Self-Absorbing Core Theorem). self-absorbing-by-construction: numeric
  hardening only, 2 new adversarial seeds (a_1=510510, 209370) independently
  reproduced by reviewer with a fresh SPF-sieve script (one minor type-
  mislabeling found and corrected, doesn't affect conclusion) — zero open
  NTBT counterexamples remains true. 5 new lemmas certified total this round
  (elementary-omega-bound, monotone-chain-reformulation-lemma, plus 3 pending
  round-18 lemmas finally certified after full independent re-verification:
  double-witness-nested-pigeonhole, same-type-triangle-vacuity, two-sided-
  singleton-witness-theorem). Main FAH crux (H1) and H2 both remain
  unresolved; run still stands on 2 certified solved sub-family theorems
  (2|a_1; a_1=p^k) plus the gap-free Master Conditional Theorem.

## Eval History

- Round 2: Status partial -> partial. PLATEAU (but real internal progress on gap (†)).
  3 math-explorers (minimality/monovariant, hypergraph fresh-framing, density fresh-framing) ->
  1 proof-outliner (revised covering-system-construction with a "Universal Glue Prime Lemma" +
  sparse/dense-Q split; opened new approach greedy-exchange-cost-potential from crux corpus
  aimo-0678 monotone-potential framing) -> 1 outline-reviewer (numerically FALSIFIED the Universal
  Glue Prime Lemma / sparse-regime conjecture via a_1=35 counterexample: true period needs TWO
  extra primes {2,3}, not one; sent both build-set slugs back CHANGES REQUESTED with explicit
  retraction instructions) -> 2 proof-builders (covering-system-construction, greedy-exchange-cost-
  potential; both genuinely retracted the falsified claim, both proved new unconditional lemmas:
  Generalized Bounded Witness Lemma (S0-level), Generalized Bounded Gap Lemma, Single-Witness-Prime
  Pigeonhole Refinement, Extended Persistent-Type Pigeonhole — all certified to
  results/imo-2026-06/lemmas/) -> 1 proof-reviewer (independently verified both retractions genuine
  and all 4 new lemmas correct/unconditional/non-circular; made 3 independent attempts of its own
  to close (†), all failed at the same wall, confirming (†) is a genuine crux not hand-waving; both
  slugs CHANGES REQUESTED, Status partial, current.md updated with (†) reformulated as an exact
  "recruitment-process halting question": start from Finite Core Theorem's S, check for (†)-
  violating pairs, recruit a forced new prime via the Generalized Bounded Witness Lemma if found,
  repeat — only termination of this concrete process is open. 10-seed computational check
  (including |Q|=4, a_1=1155) found zero violations using only the original S with zero further
  recruitment rounds, proposed as next round's concrete target.
  Elo: covering-system-construction ~1583 (leader), others largely unchanged/stale
  (amortized-charging-budget, density-sieve-contradiction, hypergraph-transversal left untouched
  this round per outliner recommendation to avoid wasting builder slots on the same shared gap).
- Round 1: Status unsolved -> partial. IMPROVED. 4 approaches opened (hypergraph-transversal,
  covering-system-construction, amortized-charging-budget, density-sieve-contradiction). Build set:
  amortized-charging-budget, covering-system-construction. Both CHANGES REQUESTED (partial).
  6 lemmas certified to results/imo-2026-06/lemmas/ (free-facts-gcd, bounded-gap-lemma,
  persistent-type-pigeonhole, bounded-witness-lemma, finite-core-theorem, forced-linking-prime
  [superseded]). Elo: covering-system-construction 1531, amortized-charging-budget 1530,
  density-sieve-contradiction 1486, hypergraph-transversal 1453.
  Sharpest open gap (†), from covering-system-construction: with S_0 = Q ∪ S (Q = P(a_1), S the
  finite core prime pool from the Finite Core Theorem) and extended type ρ(n) = P(a_n) ∩ S_0, do
  any two extended-persistent types A',B' with disjoint base Q-types necessarily satisfy
  A' ∩ B' ≠ ∅? Not yet proved by either approach. Given (†), both approaches independently derive
  the CRT + cyclic-pigeonhole finish (L = ∏ S_0, T = |good residues|) correctly.
  Secondary open gap (both approaches, unattempted): extending periodicity back to n=1 literally
  (empirically true on all tested seeds, not proved).

- Round 3: Status partial -> partial. IMPROVED (real narrowing, plus a genuine
  falsification correcting a prior conjecture). 3 math-explorers (monovariant,
  closure, fresh-framing lenses) -> 1 proof-outliner (field of 4: revise
  covering-system-construction + greedy-exchange-cost-potential importing 2 new
  lemmas; new witness-depth-bound; new minimal-counterexample-glue) -> 1
  outline-reviewer (APPROVE'd the two revisions, CHANGES-REQUESTED witness-depth-bound
  with a falsification-driven fix (index depends on prime magnitude not |Q| alone), cut
  minimal-counterexample-glue as a fake-diversity technique-variant of the same
  residual gap) -> build set: covering-system-construction, greedy-exchange-cost-
  potential, witness-depth-bound (3 proof-builders, parallel) -> 1 proof-reviewer.
  New certified lemmas: Canonical-Refinement Lemma
  (lemmas/canonical-refinement-lemma.md) and F_A ∩ F_B ≠ ∅
  (lemmas/canonical-witness-intersection.md) — both proved independently in two
  sibling approach files, verified identical, certified once crediting both. These
  localize gap (†) to a strictly smaller residual set V of "rogue pairs" (both sides
  non-canonical extended-type refinements) — a real narrowing of the crux. All 3
  built slugs: covering-system-construction CHANGES REQUESTED (minimal-counterexample
  attack on V documented as failing for 2 specific structural reasons), greedy-
  exchange-cost-potential CHANGES REQUESTED (exchange argument on V fails; new
  negative "Lemma F" proved — magnitude lemmas only build larger competing
  candidates, ruling out this whole proof-attempt family; not separately certified,
  toolkit-bound not portable), witness-depth-bound RETHINK (reviewer verified its own
  "scope observation": even fully proved, this target would NOT close (†) as framed —
  Finite Core Theorem already gives finite S with no depth bound needed; approach
  dead as scoped). IMPORTANT: reviewer's own independent simulation on a_1=175 (a
  seed neither builder tested) found a REAL violation of the "zero further
  recruitment rounds" computational conjecture from rounds 2-3 — extended-persistent
  types {2,7} and {3,5} are a genuine disjoint rogue pair, recruitment correctly
  forces prime 13, true period T=274, L=2730=2·3·5·7·13, matching the recruitment
  mechanism exactly. This FALSIFIES "zero rounds needed" (do not re-propose it) while
  CONFIRMING the recruitment-process mechanism itself still works correctly on this
  case. Elo: covering-system-construction ~1636 (leader), greedy-exchange-cost-
  potential ~1559, witness-depth-bound cold-start ~1506 then RETHINK this round.

- Round 4: Status partial -> partial. IMPROVED (major correction, sharper reopened target).
  3 math-explorers -> 1 proof-outliner -> 1 outline-reviewer (caught a restated-falsified-claim
  risk pre-build) -> 2 proof-builders (both CHANGES REQUESTED/partial; PUCL proved false in all
  forms; new conditional Round Resolution Lemma + unconditional Lemma G) -> 1 proof-reviewer,
  which found round 3's a_1=175 "falsification" of the zero-further-recruitment-rounds
  conjecture was a witness-selection bug (non-minimal witness), RETRACTED it, and reverified
  18/18 seeds show V=∅ with the theorem's literal minimal-witness convention — reopening a
  sharper, better-supported direct target for round 5. 1 new certified lemma
  (extended-earliest-witness-intersection). Elo: covering-system-construction ~1660 (leader),
  greedy-exchange-cost-potential ~1607.

- Round 5: Status partial -> partial. IMPROVED (major reversal, correctly caught, real
  narrowing). 3 math-explorers (extremal-witness, singleton-hypothesis, fresh-framing
  lenses) -> 1 proof-outliner (4 approaches: revise covering-system-construction toward
  "Simultaneous Resolution Lemma"; revise greedy-exchange-cost-potential toward proving
  Singleton Hypothesis in general; new witness-index-descent from crux aimo-0030; new
  reversible-transition-map from crux aimo-0514) -> 1 outline-reviewer (independently
  reimplemented from scratch and CONFIRMED a major reversal: round 4's "V=∅ always"
  claim is FALSE — genuine counterexamples a_1=187,209,247,385, each resolved by exactly
  one recruitment round with a Singleton F'; downgraded reversible-transition-map's
  injectivity step over gap-(†)-in-disguise risk; build set = all 4) -> 4 proof-builders
  (parallel) -> 1 proof-reviewer, which independently reimplemented the pipeline a THIRD
  time and reconfirmed the reversal, then found an additional unflagged gap ("collateral
  rogue pairs": does refining S₀→S₁ spawn brand-new rogue pairs among previously-safe
  base types? unproved either way, 0/3 seeds show it but not general).
  Per-approach verdicts: covering-system-construction CHANGES REQUESTED (new certified
  Monotonicity of Resolution Lemma; Conditional Single-Pair/Simultaneous Resolution
  Theorems correct but conditional on Universal Singleton Hypothesis); greedy-exchange-
  cost-potential CHANGES REQUESTED (new certified Lemma H "Critical Prime Dichotomy";
  Singleton Hypothesis honestly still open); witness-index-descent RETHINK (Same-Side
  Ordering Lemma certified but trivial; descent mechanism fails for 2 reasons — false
  single-stage target, non-monotone cross-stage measure, same wall as round 3's size
  measure); reversible-transition-map RETHINK (forward-well-definedness PROVED equivalent
  to gap (†) itself — confirms it's not a bypass; backward-injectivity genuinely
  different but conditional on (†) and faces a new obstruction re: secondary n=1 gap).
  3 new lemmas certified (monotonicity-of-resolution, same-side-ordering-lemma,
  critical-prime-dichotomy). Crux now precisely: prove the Universal Singleton
  Hypothesis (|F'|=1 always at a rogue-pair witness) AND rule out collateral rogue pairs
  under refinement.

## Eval History (round 16 addition)

- Round 16: Status partial -> partial overall, but **first APPROVE of the run**
  (15 rounds stuck): `even-a1-full-periodicity-theorem` solved and certified for
  the restricted 2|a_1 subfamily (T=1, L=2, literal from n=1, unconditional,
  requires none of the FAH machinery). 3 math-explorers (restricted-family FAH
  lens, termination-criterion N(S_k) boundedness lens, fresh whole-problem
  framing lens) -> 1 proof-outliner (new even-a1-full-periodicity-theorem;
  advanced n1-periodicity-reconciliation as consolidation/write-up; new
  core-growth-monotonicity attacking core-termination sub-gap) -> 1
  outline-reviewer (APPROVE all 3; verified 2|a_1 induction airtight and
  genuinely new via grep) -> 3 proof-builders -> 1 proof-reviewer (independently
  re-derived everything from scratch, re-simulated on seeds not in builders'
  lists). Verdicts: even-a1-full-periodicity-theorem APPROVE (solved, scoped);
  n1-periodicity-reconciliation CHANGES REQUESTED (partial — Master Conditional
  Theorem chain assembled gap-free from 6 certified lemmas, both open hypotheses
  H1=FAH, H2=core-termination precisely stated, H1 shown to trivialize when
  2|a_1, H2 shown NOT to trivialize); core-growth-monotonicity CHANGES REQUESTED
  (partial — 2 new lemmas certified: Binary Refinement Lemma, Threshold
  Recursion Bound Lemma; proved the next-level quantity M_B is provably
  non-constructive, a general toolkit-independent fact, explaining the round-16
  explorer's numeric stall; H2 boundedness still open). Main FAH crux itself
  (general/odd-a_1 case) remains untouched — 11th consecutive plateau round on
  it — but the run now has its first genuinely solved, certified special-case
  theorem as a concrete deliverable if FAH stays unsolved.

## Eval History (round 15 addition)

- Round 15: Status partial -> partial. PLATEAU on the main FAH crux (10th consecutive
  round, 6-15, with no proof — all 3 explorers again found no genuinely new corridor),
  but real secondary progress: sub-gap (b) of n1-periodicity-reconciliation fully
  closed, and a duplicate-content pseudo-mechanism caught pre-build. 3 math-explorers
  (bespoke |F''|=2 narrow-case deeper dig, fresh whole-problem framing across 5 new
  angles, crux-corpus mining outside number_theory) -> all three independently found
  NOTHING new: narrow-case explorer reconfirmed rounds 12-13's dead ends plus 2 new
  computational/structural clarifications (canonicality of (†) is strictly weaker than
  FAH; two-witness-only legality mechanism concretely, not just abstractly, dead);
  fresh-framing explorer tried transfer-matrix, ergodic/symbolic-dynamics,
  compactness/König's-lemma, additive-combinatorics, and a sidestep reformulation —
  all collapse into certified content or have no foothold; crux-mining explorer found
  the two closest corpus analogs (aimo-0016, aimo-0051) were ALREADY imported round 9
  and already died, and aimo-1019's double-counting mechanism requires a conserved
  global additive quantity this problem provably lacks (Escape-Cost
  Vacuity/Sandwich Genericity) -> 1 proof-outliner (opened new
  rogue-pair-termination-potential targeting a base-type-pair-count finiteness
  parameter; rejected H-prime-fiber packaging as (†)-equivalent pre-scoping; advanced
  n1-periodicity-reconciliation toward its 2 disclosed sub-gaps; kept
  covering-system-construction/greedy-exchange-cost-potential live) -> 1
  outline-reviewer (RETHINK'd rogue-pair-termination-potential — NOT a new mechanism
  at all, its steps 2-4 verbatim duplicate the already-certified Collateral-Safety
  Theorem's own Corollary/Theorem/Consequence paragraphs, with step 4's "genuinely
  new open key lemma" being literally FAH restated under the Collateral-Safety
  Theorem's own text; not registered in ranker per RETHINK policy; APPROVE'd
  n1-periodicity-reconciliation's continuation plan; build set =
  n1-periodicity-reconciliation only) -> 1 proof-builder -> 1 proof-reviewer
  (independently reconstructed and reverified everything from scratch, including a
  fresh Python reimplementation of the computational sanity check on a_1=175, exact
  match). Verdict: n1-periodicity-reconciliation CHANGES REQUESTED (partial) — proved
  Universal Early Intersection Lemma + Literal n=1 Periodicity Theorem (sub-gap (b),
  "can N(S*)=0", FULLY CLOSED: literal n=1 periodicity now holds under the SAME two
  hypotheses as the existing Self-Absorbing Core Theorem, no new hypothesis added,
  unconditional relative to FAH+self-absorption); proved Termination Criterion Lemma
  (sub-gap (a) iff-reduction: absorption terminates iff threshold sequence N(S_k) is
  bounded — genuine new content, both directions independently reverified, but
  boundedness itself NOT established, honestly left open); independently confirmed
  sub-gap (a) is a logically DISTINCT object from the main FAH crux (not a smuggled
  equivalence, checked not just trusted). 3 new lemmas certified
  (universal-early-intersection-lemma, literal-n1-periodicity-theorem,
  termination-criterion-lemma). n1-periodicity-reconciliation's residual dependency
  chain shrank from 3 open ingredients to 2 (FAH; existence/termination of S*). Main
  FAH/Symmetric FAH/Cofinite FAH/EEA crux itself remains completely untouched this
  round — 10 consecutive plateau rounds (6-15) on it now, and this round is the
  strongest evidence yet that the general-mechanism well for this exact crux (via
  gcd-pigeonhole-family and all adjacent techniques) may be structurally exhausted;
  no new domain/technique family remains unmined per this round's 3-lens sweep.

## Eval History (round 8 addition)

- Round 8: Status partial -> partial. IMPROVED (plateau-breaking round per CLAUDE.md: a
  fresh top-level framing was opened and honestly falsified with a precise diagnosis, and
  the FAH mechanism found a gap even more basic than previously flagged, narrowing what a
  future mechanism must avoid; 2 new unconditional lemmas certified). 3 math-explorers
  (density/asymptotic, fresh whole-problem framing, FAH direct-mechanism lenses) -> 1
  proof-outliner (revised covering-system-construction with "Fixed-Witness Divisor-Chain"
  scoped to Lemma-G rogue-pair witnesses; opened NEW seed-coupling-induction — induction on
  ω(a_1) via reduced seeds, the required genuinely-different framing after 3 rounds
  plateaued on FAH; also sketched a greedy-exchange-cost-potential occurrence-order
  induction) -> 1 outline-reviewer (verified the Fixed-Witness scoping is real via 3-seed
  numerical check; sanity-checked seed-coupling-induction on a_1=15; held out
  greedy-exchange-cost-potential's revision this round — shares the same unresolved
  canonicality sub-lemma as approach 1, plus its own pigeonhole has an anchoring gap;
  build set = covering-system-construction, seed-coupling-induction) -> 2 proof-builders
  (parallel) -> 1 proof-reviewer (independently reconfirmed both from scratch).
  Verdicts: covering-system-construction CHANGES REQUESTED (partial) — found the dispatched
  mechanism's core dichotomy branch ("pigeonholed prime r ∈ S₀ ⟹ contradicts rogueness") is
  FALSE (r ∈ S₀ only tautologically forces r ∈ A', no contradiction) — more basic than the
  canonicality gap flagged pre-build; proved unconditional byproduct **Singleton-Side FAH**
  (if F' is a singleton, cofinite divisibility is free from the Generalized Bounded Witness
  Lemma) which fully explains why this round's (and prior rounds') positive computational
  evidence never actually tested the genuinely open |F'|≥2 case (a_1=187,209 both have
  singleton F'; a_1=4807 with |F'|=2 independently reconfirmed to genuinely fail the
  analogous claim, ~6.2% divisibility not cofinite). seed-coupling-induction RETHINK
  (unsolved as a mechanism) — builder + reviewer both independently, from-scratch
  confirmed a real falsification: for any seed with 2∉Q, every single-prime-removal
  reduction leaves Q' without 2, and the type-correspondence claim fails with large
  non-vanishing mismatch (15-68%) at N=8000; no rescuing choice exists in this framing as
  scoped. 2 new lemmas certified (singleton-side-fah, divisor-chain-well-definedness).
  Elo: covering-system-construction leads (edges ahead of greedy-exchange-cost-potential
  this round per anchoring-correctness), seed-coupling-induction registered above all
  confirmed dead-ends/stale approaches but below the two live leaders.

## Eval History (round 9 addition)

- Round 9: Status partial -> partial. IMPROVED (plateau-breaking round per CLAUDE.md:
  a genuinely new top-level framing was opened, verified sound in its non-FAH parts,
  and its stall precisely diagnosed as the same underlying obstruction as 5+ prior
  mechanisms — a real narrowing of what ANY future FAH mechanism must overcome; a
  9th direct mechanism was also ruled out with a clean counterexample; 4 new
  unconditional lemmas certified). 3 math-explorers (FAH |F'|>=2 direct-mechanism,
  fresh whole-problem framing, crux-corpus mining lenses) -> 1 proof-outliner (revised
  covering-system-construction toward a "Recruitment-Budget / fixed Q-level witness
  pool W_{A,B} counting bound"; opened NEW cofinite-window-capacity-bound — the
  mandatory plateau-breaking framing, targeting cofinite (not literal zero-exception)
  FAH via an aimo-0051-style window-capacity counting bound, after proving cofinite
  suffices for the existing finish; revised greedy-exchange-cost-potential toward an
  aimo-0016-style downward-transport/predecessor-inheritance induction) -> 1
  outline-reviewer (independently reimplemented the pipeline from scratch, found
  round 8's "~6% divisibility, not cofinite" a_1=4807 evidence was measured at the
  WRONG core — S₀=Q, before recruitment — not a genuine counterexample; found a
  proper |F'|>=2 rogue pair at a correctly recruited core, a_1=11305, with 100%
  zero-exception divisibility, REVERSING that evidence to support FAH; verified
  "cofinite suffices" logically sound; build set = all 3) -> 3 proof-builders
  (parallel) -> 1 proof-reviewer (independently reconfirmed all three from scratch).
  Verdicts: covering-system-construction CHANGES REQUESTED (partial) — refuted its
  own dispatched Recruitment-Budget mechanism with a clean counterexample (a_1=209,
  forced prime q=7 recruited outside the fixed base-type witness pool W_{A,B} at
  round 2 of recruitment; independently reconfirmed plus a second escape at
  a_1=247); the "expand the pool" rescue is circular. 9th FAH-adjacent mechanism now
  dead. cofinite-window-capacity-bound CHANGES REQUESTED (partial) — proved 2 new
  certified lemmas (Cofinite Sufficiency Lemma: cofinite, not zero-exception, FAH
  suffices for the existing finish; Confined-GCD Lemma: strictly strengthens
  Divisor-Chain Well-Definedness), but the window-capacity counting bound itself
  genuinely stalls on the same existential-to-universal promotion gap (infinite
  pigeonhole only guarantees SOME divisor-class is infinite, not that only the
  q*-class is) — independently confirmed genuine, not an avoidable gap.
  greedy-exchange-cost-potential CHANGES REQUESTED (partial) — ~270+185 combined
  seed sweep at properly-recruited cores found ZERO FAH counterexamples anywhere
  (strong, not conclusive, positive evidence for literal FAH); proved new certified
  Successor-Transport Reduction Lemma (successor claim, if true, gives cofinite FAH)
  and Same-Type Free Facts Vacuity observation, but the successor step itself
  collapses into the same Lemma-I "branch fires uninformatively" dead pattern.
  4 new lemmas certified (cofinite-sufficiency-lemma, confined-gcd-lemma,
  successor-transport-reduction-lemma, same-type-free-facts-vacuity).
  Elo: covering-system-construction ~1832 (leader), greedy-exchange-cost-potential
  ~1762, cofinite-window-capacity-bound cold-start ~1540 (new).

## Eval History (round 10 addition)

- Round 10: Status partial -> partial. IMPROVED (plateau-breaking round per CLAUDE.md:
  explorer consensus surfaced crux aimo-0680's window-counting/AP-identity template as
  the best untried genuinely-different mechanism; 3 rival attempts built on it, all
  cleanly killed with rigorous impossibility proofs rather than just failed search,
  yielding 4 new certified lemmas and a sharper diagnosis of what's missing). 3
  math-explorers (analytic/counting, fresh whole-problem framing, crux-corpus mining
  lenses) -> 1 proof-outliner (revised covering-system-construction with Step 11
  "Growth-Forced Divisibility"/Escape-Cost Lemma; revised greedy-exchange-cost-potential
  with an Escape-Budget attack on the Successor Claim; new confined-competitor-construction
  mirroring dead Lemma K with the Confined-GCD Lemma's one controlled coordinate;
  explicitly investigated and REJECTED a standalone Return-Time Boundedness Lemma as
  circular — reduces to round-5's S-sufficiency <=> V=∅ equivalence, i.e. the crux
  itself) -> 1 outline-reviewer (independently verified all 3, did fresh numeric
  sanity checks, build set = all 3) -> 3 proof-builders (parallel) -> 1 proof-reviewer
  (independently reconfirmed all 3 from scratch). Verdicts: covering-system-construction
  CHANGES REQUESTED (partial) — proved Escape-Cost Lemma is vacuous via new certified
  Sandwich Genericity Theorem + Escape-Cost Vacuity Theorem (class-blind premises can't
  yield class-sensitive conclusions); 10th FAH mechanism retired. greedy-exchange-cost-
  potential CHANGES REQUESTED (partial) — new certified Window Resolution Lemma resolves
  windowing ambiguity (telescoped interval, not single step), then Escape-Budget mechanism
  dies via Growing-Constraint Obstruction (illegality witness pool unboundedly growing,
  not fixed-size); 11th mechanism retired. confined-competitor-construction RETHINK
  (unsolved) — new certified Minimality Tautology Lemma (any candidate c with
  a_{n-1}<c<a_{n_j} and gcd>1 vs all prior terms would already have been chosen as a_n,
  contradiction) kills this competitor-construction mechanism (12th), BUT reviewer caught
  an overclaim: it does NOT kill round-7's Lemma K, which uses a different proof shape
  (blocking-index extraction, not full-legality competitor construction) — corrected in
  the certified lemma file and current.md. 4 new lemmas certified (sandwich-genericity-
  theorem, escape-cost-vacuity, window-resolution-lemma, minimality-tautology-lemma).
  Elo: covering-system-construction leader, greedy-exchange-cost-potential close second,
  confined-competitor-construction low (dead-end recorded).

## Eval History (round 11 addition)

- Round 11: Status partial -> partial. PLATEAU (real narrowing again — 2 more FAH
  mechanisms killed, but 6th consecutive round on the same crux, reviewer explicitly
  flags shared-gap plateau per CLAUDE.md). 3 math-explorers (CRT/multiplicative-
  structure-of-a_1 lens, automaton/graph-walk-encoding lens, Lemma K + Confined-GCD +
  Window Resolution combination lens) all independently converged on the same wall
  and found NO genuinely new mechanism: CRT lens found q's identity is dynamically not
  algebraically determined, and the one real CRT-shaped regularity found is circular
  (equivalent to FAH itself, per reversible-transition-map); automaton lens found the
  graph-walk encoding is isomorphic to already-dead mechanisms (Successor Claim /
  reversible-transition-map equivalence); Lemma K lens found Confined-GCD's control
  lives on F'/F''-primes while Lemma K's generic blocking witness lives on S0-primes
  (dominated by a_1's own factors) — structurally disjoint, but identified a precise
  open sub-question (force blocking witness j outside S0) -> 1 proof-outliner (field
  of 3: revise greedy-exchange-cost-potential with a "Forced-Escape Blocking
  Construction" directly targeting that sub-question via CRT-glue; kept
  covering-system-construction live for ranking continuity; new
  sieve-density-exception-bound approach, an analytic/counting technique family) -> 1
  outline-reviewer (independently ran the CRT-glue construction numerically and found
  it magnitude-doomed — competitor lands ~8 orders of magnitude above a_n, Lemma K's
  dichotomy never reaches its informative branch; certified this as the 13th dead
  mechanism, "CRT Magnitude Obstruction"; also corrected an outline error where a
  logically-impossible sub-case was mislabeled "most promising to check first"; build
  set = greedy-exchange-cost-potential, sieve-density-exception-bound) -> 2
  proof-builders (parallel) -> 1 proof-reviewer (independently reconfirmed both from
  scratch). Verdicts: greedy-exchange-cost-potential CHANGES REQUESTED (partial) —
  found the "Minimal-Modulus Generalization": ANY partial-subset CRT modulus falls
  into one of two dead branches (informative-but-magnitude-doomed, or
  cheap-but-uninformative), closing the ENTIRE CRT-glue/competitor-construction
  family in full generality (14th dead mechanism); no new lemma certified
  (deliberately, precedent from Lemma F/Lemma I). sieve-density-exception-bound
  RETHINK (unsolved as scoped) — mandatory pre-build class-blindness screening
  killed both sub-routes: sub-route (a) is window-class-blind, killed by new
  certified Density-Argument Vacuity Corollary (extends Escape-Cost
  Vacuity/Sandwich Genericity Theorems to window/counting statements); sub-route
  (b) reduces to positing the open crux itself via Borel-Cantelli on an unproved
  decay rate. 1 new lemma certified (density-argument-vacuity-corollary).
  Elo: covering-system-construction leads (~1855), cofinite-window-capacity-bound and
  confined-competitor-construction mid-pack, greedy-exchange-cost-potential close
  behind covering-system-construction, sieve-density-exception-bound cold-start then
  dead-end this round. Reviewer's explicit recommendation for round 12: push for at
  least one approach that abandons the shared "persistent-type reconciliation via
  class-blind/window-aggregate technique" corridor entirely; if none found, consider
  a bespoke small-|Q|/small-seed-family ad hoc argument as a fallback to narrow the
  general claim rather than another general-mechanism attempt doomed to the same wall.

## Eval History (round 12 addition)

- Round 12: Status partial -> partial. IMPROVED (successful plateau-break per
  CLAUDE.md/round-11 mandate: a genuinely new corridor was opened, independently
  verified, and pushed to a sharper corrected diagnosis rather than dead-ending
  silently; 4 new lemmas certified). 3 math-explorers (multiplicative/valuation
  structure of a_1, bespoke |F'|=2 small-case, fresh whole-problem framing) ->
  fresh-framing lens found the plateau-break: a Morse-Hedlund/subword-complexity
  reformulation (gap sequence's factor complexity), never tried in 11 rounds; the
  other two lenses confirmed no new corridor (both re-land on the standing
  diagnosis) -> 1 proof-outliner (new subword-complexity-periodicity approach;
  revised seed-coupling-induction toward an aggregate/set-level claim; kept
  covering-system-construction live for a small bookkeeping task) -> 1
  outline-reviewer (APPROVE'd subword-complexity-periodicity as a genuine new
  corridor via own simulation; RETHINK'd seed-coupling-induction's revision —
  numerically falsified on 3/12 (a_1, removed-prime) pairs, same underlying
  failure mode as round 8's dead positional version, not real progress; build set
  = subword-complexity-periodicity, covering-system-construction) -> 2
  proof-builders (parallel) -> 1 proof-reviewer (independently re-verified both
  from scratch). Verdicts: subword-complexity-periodicity CHANGES REQUESTED
  (partial) — proved Lemma A (Gap-Periodicity Equivalence, certified,
  unconditional) and Lemma B (Right-Extension Determinism => periodicity, the
  actual Morse-Hedlund pigeonhole+induction mechanism, certified, general-purpose
  beyond this problem); found the outline's headline "finite-defect" weaker
  target is TRIVIALLY VACUOUS (automatic consequence of Bounded Gap Lemma, not
  real content) — confirmed genuine against the outline's own text, not a
  strawman; isolated the corrected necessary condition EEA (Eventual Escape from
  Ambiguity) and proved Theorem C (EEA => periodicity, certified with a wording
  fix to the "safe residue" definition); independently re-derived that EEA
  reduces to exactly the same FAH content via the Confined-GCD Lemma — same crux
  under new vocabulary, not a bypass. covering-system-construction CHANGES
  REQUESTED (partial) — certified the Reduced-Alphabet Corollary (closed-form
  |D_bad(q*)| = prod(e_p+1)-1 over F''\{q*}, unconditional, built only from
  already-certified lemmas, no circularity), independently reverified via a
  fresh from-scratch simulation of a_1=4807 (exact match, D_bad(17)={13}); in the
  standing |F''|=2 mult-1 test seeds this collapses the residual alphabet to a
  SINGLE divisor class — flagged as the most concrete fallback target for round
  13 if no further new corridor is found. Overall Status remains partial; EEA
  and FAH now known-equivalent-difficulty vocabularies, don't re-dispatch hoping
  EEA is a shortcut without a genuinely new ingredient.

## Eval History (round 13 addition)

- Round 13: Status partial -> partial. PLATEAU on the main FAH crux (no genuinely new
  corridor survived this round — a candidate Central Sets Theorem/idempotent-ultrafilter
  attempt was RETHINK'd pre-build), but real defensive/secondary progress: a new
  unconditional lemma certified and a genuine new gap precisely isolated in a fresh
  approach. 3 math-explorers (de Bruijn/special-factor deeper dig on the round-12
  Morse-Hedlund corridor, bespoke |F''|=2 mult-1 narrow-case attack, fresh whole-problem
  framing) -> both the de Bruijn-corridor dig and the bespoke narrow-case attack
  re-collapsed into the standing FAH wall (no new build); fresh-framing surfaced (a) an
  untried idempotent-ultrafilter/Hindman/Central Sets Theorem toolkit and (b) a new
  concrete "No-Restart Lemma" fact (restarting the greedy process at a later index as a
  fresh seed is structurally invalid, proved via a_1=15 example) -> 1 proof-outliner
  (field of 3: new central-sets-idempotent-recurrence; revised greedy-exchange-cost-
  potential to formalize the No-Restart Lemma; new n1-periodicity-reconciliation
  attacking the untouched-since-round-5 secondary n=1 gap, conditional on FAH) -> 1
  outline-reviewer (RETHINK'd central-sets-idempotent-recurrence pre-build — Central/
  idempotent-ultrafilter machinery only guarantees SOME cell of a finite partition is
  central, never the specific target cell, the same existential-not-target wall restated
  in Ramsey vocabulary, the 15th confirmed-dead-shaped mechanism; APPROVE'd the other two;
  build set = greedy-exchange-cost-potential, n1-periodicity-reconciliation) -> 2
  proof-builders (parallel) -> 1 proof-reviewer (independently reconfirmed both).
  Verdicts: greedy-exchange-cost-potential CHANGES REQUESTED (partial) — No-Restart Lemma
  proved in full generality, unconditional, non-circular, independently reverified by the
  reviewer via fresh simulation; CERTIFIED to lemmas/no-restart-lemma.md; purely
  defensive/explanatory, does not touch FAH. n1-periodicity-reconciliation CHANGES
  REQUESTED (partial, new approach) — correctly scoped as conditional on open FAH
  throughout; proved Non-Constructivity of N₀/N₁/N₁'/N₂ observation (the pigeonhole
  thresholds used workspace-wide are only existentially finite, not effectively
  computable from a_1); Self-Absorbing Core Theorem's conclusion independently confirmed
  correct by the reviewer but its WRITTEN proof has a real gap in the "Combining both
  parts" step (cites Step 5's construction for a claim about a broader eligible-residue
  set G* that Step 5's own narrower definition never actually establishes) — not
  certified this round, fix path specified. 6-seed fresh computational check (15, 35,
  105, 175, 187, 209) found literal n=1 periodicity (N₀=0) on all 6 — evidence, not
  proof. 1 new lemma certified (no-restart-lemma). Elo: central-sets-idempotent-
  recurrence not registered (RETHINK pre-build); n1-periodicity-reconciliation
  registered as new; greedy-exchange-cost-potential and covering-system-construction
  otherwise unchanged in ranking.

## Eval History (round 14 addition)

- Round 14: Status partial -> partial. IMPROVED (real secondary-gap closure plus a
  16th FAH mechanism cleanly killed with a generalizing diagnosis; main crux itself
  still open). 3 math-explorers (fresh whole-problem framing, crux-corpus identity-
  level-tool mining, p-adic valuation/monovariant lens) -> freshframing found nothing
  new (4 angles tried, all dead/unsound — notably falsified a rad(a_1)-induction idea
  via a_1=105 vs a_1=315 diverging from their first recruited term); valuation lens
  found a NEW negative result (exact valuation v_{q*}(a_n) is non-monotone along
  same-type occurrences on a_1=11305, ruling out exact-valuation-monovariant
  induction by direct counterexample); cruxmining found ONE genuinely new candidate,
  crux aimo-0134's integer running-average + difference-identity monovariant
  technique -> 1 proof-outliner (revised n1-periodicity-reconciliation with a fix
  plan for the round-13 "combining both parts" gap; opened new
  integer-monovariant-difference-identity adapting aimo-0134, pre-screening and
  rejecting 2 obvious candidate statistics; kept covering-system-construction /
  greedy-exchange-cost-potential live for ranking continuity) -> 1 outline-reviewer
  (verified the outliner's proposed fix mechanism for n1-periodicity-reconciliation
  was FICTITIOUS — grepped Step 5's actual proof and found no such trichotomy exists
  — and supplied the correct fix itself: split into Sufficiency + Landing, both
  already free from the certified Free Facts Lemma and the theorem's own FAH-at-S*
  hypothesis; APPROVE'd integer-monovariant-difference-identity for build after
  independently re-verifying the pre-screened candidates are genuinely dead, not
  smuggled; build set = both) -> 2 proof-builders (parallel) -> 1 proof-reviewer
  (independently reconfirmed both from scratch). Verdicts: n1-periodicity-
  reconciliation CHANGES REQUESTED (partial) — the round-13 "combining both parts"
  gap is now GENUINELY CLOSED (reviewer independently re-derived the Sufficiency/
  Landing split, found and fixed one additional non-fatal precision gap — the
  "every two elements of 𝒫'(S*) intersect" hypothesis needed an explicit derivation
  of its equivalence to standard FAH-at-S*, now added); **certified**
  `lemmas/self-absorbing-core-theorem.md`; the two disclosed sub-gaps (existence/
  termination of self-absorbing S*, whether N(S*) can be 0) remain honestly open —
  this approach is STILL conditional on FAH throughout, so does not touch the main
  crux. integer-monovariant-difference-identity RETHINK (unsolved, honest negative
  result, no overclaim) — 5 candidate integer statistics tried and killed (running
  average of gaps computationally refuted as non-monotone on both mandated seeds;
  running min and overall-gcd genuinely bounded/monotone but structurally
  uninformative; persistent-type count and recruited-core size restate already-
  certified content or are circular with (†)); general diagnosis proved: ANY purely
  numeric (count/min/gcd/average) statistic built from this problem's class-blind
  legality test is poisoned the same way, generalizing past the 5 specific tries.
  16th confirmed-dead FAH-adjacent mechanism. Reviewer independently reimplemented
  the greedy sequence from scratch and reproduced every reported number exactly on
  both a_1=4807 and a_1=11305. Elo: n1-periodicity-reconciliation advanced (genuine
  progress, new certified lemma); integer-monovariant-difference-identity registered
  then marked dead; covering-system-construction / greedy-exchange-cost-potential
  unchanged. Main FAH/Symmetric FAH/Cofinite FAH/EEA crux itself remains untouched
  this round — now 9 consecutive rounds (6-14) with no proof, though this round DID
  produce a fully new (17th-mechanism-adjacent... actually 16th direct) killed idea
  plus a genuine secondary-gap closure, so not a silent/unproductive plateau.

## Eval History (round 17 addition)

- Round 17: Status partial -> partial. PLATEAU on the main FAH crux (12th consecutive
  round, 6-17, with no new mechanism attempted — by design, given 3 consecutive
  fresh-framing sweeps (rounds 13, 15, 17) all found nothing new), but real progress
  on the secondary H2 (core-absorption-chain termination) hypothesis. 3 math-explorers
  (restricted-family-extension lens, H2-termination-quantity lens, fresh
  whole-problem-framing lens) -> restricted-family lens confirmed with fresh numeric
  evidence that no clean restricted-family theorem exists beyond the certified
  prime-power/2|a_1 cases (companion-prime behavior is genuinely seed-dependent for
  p>=3); H2-termination lens found round 16's "a1=11305 doesn't stabilize within
  15,000 terms" was a SAMPLING-WINDOW ARTIFACT (resolves cleanly at 20,000-30,000
  terms on 9/9 seeds |Q|<=4), and flagged a fresh untried angle (bound |𝒫'(S)|
  combinatorially instead of index-based N(S)/M_B); fresh-framing lens found nothing
  new for FAH itself (4 angles: ultraproduct/compactness, per-prime indicator
  decomposition, transfer-operator, LP-duality — all require FAH-equivalent input,
  not a bypass), 3rd consecutive exhaustive sweep with zero new corridors -> 1
  proof-outliner (new type-alphabet-counting-bound attacking H2 via |𝒫'(S)|; new
  self-absorbing-by-construction forcing self-absorption constructively; advanced
  n1-periodicity-reconciliation as consolidation/hedge-deliverable groundwork;
  bookkeeping touch to covering-system-construction) -> 1 outline-reviewer
  (RETHINK'd type-alphabet-counting-bound pre-build — independently verified its own
  mandated pre-check and found "finitely many absorption rounds" is trivially
  EQUIVALENT to "N(S_k) bounded," collapsing back into the dead M_B territory, not a
  new target; APPROVE'd self-absorbing-by-construction after independently
  reconfirming the 9/9-seed N(S_0)=0 numeric claim is NOT a repeat of the round-16
  window-artifact bug; build set = self-absorbing-by-construction only) -> 1
  proof-builder -> 1 proof-reviewer (independently re-simulated from scratch).
  Verdict: self-absorbing-by-construction CHANGES REQUESTED (partial) — proved and
  CERTIFIED the new **Vacuous/Weak Self-Absorption Lemma** (N(Q) <= 1 suffices for
  S_0=Q itself to be self-absorbing with zero absorption rounds — a genuine
  sharpening, unconditional, verified both cases N(Q)=0 and N(Q)=1 from scratch);
  extensive ~50-seed numeric sweep found 2/3 flagged "window artifacts" (a_1=30030,
  15015) reproduce exactly, but caught the builder's a_1=255255 claim as INCOMPLETE —
  an exhaustive re-enumeration (not just re-checking the builder's named list) found
  a second unflagged single-occurrence type {5,7,11,13,17} at n=27184 still
  unresolved through window 65,000, contradicting the builder's "sole remaining type
  is full-Q" claim; the "NTBT conjecture" (N(Q)<=1 for ALL a_1) honestly left open,
  no overclaim. 1 new lemma certified (vacuous-self-absorption-lemma). Main FAH crux
  itself remains completely untouched this round (by design) — now 12 consecutive
  plateau rounds (6-17) on it, and 3 consecutive independent fresh-framing sweeps
  (13, 15, 17) finding zero new corridors is now very strong evidence the direct-
  mechanism well is exhausted; H2 however continues to show real incremental
  progress each round it's touched (round 16, round 17).

## Rules (additions from round 22)

- **Third APPROVE of the run: `a1-3q-subfamily-theorem` is solved and
  certified** (literal T=1,L=3 periodicity, all primes q>=7, q!=5,
  unconditional) — ALWAYS treat this alongside the 2|a_1 and a_1=p^k
  theorems as a floor deliverable (round 22).
- **New reusable elementary sieve tools, general-purpose beyond this
  problem**: Legendre Sieve Gap Bound (`g(M) <= 2^ω(M)(ω(M)+1)` via
  inclusion-exclusion — the max gap from any integer to the next integer
  coprime to M) and Primorial Floor Bound (`ω(M)=r => M >= (r+1)!`). Both
  certified, elementary, no PNT/Chebyshev input needed. If a future
  problem/subfamily needs a coprimality-gap bound, use these directly
  instead of re-deriving (round 22).
- **NEVER re-attempt orbit-merging/additive-offset-dichotomy mechanisms for
  H1 (FAH)** — both natural offset-object instantiations (single-prime
  divisibility split; occurrence-index alignment offset) are now confirmed
  dead: the first mistargets H2 and repeats the existential-to-universal
  dead family; the second's well-definedness is provably EQUIVALENT to the
  full periodicity conclusion itself (stronger circularity than the
  round-5 reversible-transition-map precedent). 30+ FAH mechanisms now
  confirmed dead (round 22).
- **fah-counterexample-hunt's seed record is now 12/12 clean (zero FAH
  counterexamples)**, including the previously-inconclusive a_1=105945
  (exact period T=109096, L=570570 found via a new Z-function-based O(N)
  exact-period detector — reusable tool, faster than round 21's naive
  scan). Its structural §1.3(a) invariant-proof pivot was scouted and
  assessed NOT viable (no candidate invariant exists after 22 rounds). Do
  NOT dispatch another undifferentiated seed sweep on this approach without
  a genuinely new angle (round 22).
- **`aimo-0907` (IMO functional-equation crux) is now mined and exhausted**
  as a source for FAH mechanisms — its orbit-merging/well-definedness proof
  shape does not transfer (round 22).

## Rules (additions from round 21)

- **a1-3q's remaining gap needs non-elementary number theory, not a routine
  finish**: Case (b)/n-even/k>=1 requires a genuine Jacobsthal-function-level
  bound on g(M) (max gap to next integer coprime to M) — the crude bound
  g(M)<=2^ω(M) resists elementary proof; two independent attempts (outliner's
  builder, then the reviewer independently) both hit the same two walls
  (naive halving-induction has a real counterexample at M=6; an AP-based
  repair only reproduces the already-insufficient radical-scale bound). The
  q-independent uniformity fix (Step 4, `7k>=2^(ω(K)+2)`) IS valid and
  resolvable — that part is not the blocker. Do NOT re-attempt an elementary
  proof of g(M)<=2^ω(M) without a genuinely new idea; either import real
  sieve-theory (citable per KB/crux corpus rules) or find a problem-specific
  shortcut that avoids needing the general bound (round 21).
- **NEVER treat "witness always found early" as evidence of a small
  universal bound** — round 20's a_1 up to k~200 impression was a
  search-depth artifact; round 21 constructed q=40153,k=3335,K=10010 with
  minimal witness offset exactly 10 (matching g(10010) exactly, not a small
  constant), independently reconfirmed by the reviewer (round 21).
- **New reusable tool: direct literal-period detection.** Given a seed,
  directly search for the exact (T,L) pair by simulation rather than only
  checking asymptotic/statistical FAH-style claims — this round found exact
  periods for a_1=385 (new) and 2 of the 4 canonical hard seeds (187, 221),
  enabling an EXACT one-full-period FAH check (not just asymptotic
  evidence) at a_1=385, zero violations, independently reverified by the
  reviewer with a 3rd from-scratch script. Future rounds studying FAH at a
  concrete seed should use this technique first (round 21).
- **fah-counterexample-hunt found no FAH counterexample across 11 fresh
  |Q|=3,4,5 and CRT-lopsided seeds** (150k-500k terms each) — broadens the
  evidential base beyond the 4 canonical |Q|=2 seeds, still not proof. One
  seed (a_1=105945, CRT-lopsided |Q|=4) is inconclusive (no period found
  within T<25000) — worth deepening the search on this specific seed before
  concluding either way (round 21).
- Falsification-seeking (actively hunting a counterexample rather than
  attempting a proof) is a legitimate and genuinely diverse approach type
  per CLAUDE.md's framing-diversity mandate after a long plateau — consider
  this move again if another long plateau recurs and proof-attempts are
  exhausted (round 21).

## Rules (additions from round 18)

- **Second APPROVE of the run**: `prime-power-seed-periodicity-theorem` is
  `solved` and certified (`lemmas/prime-power-seed-literal-periodicity-theorem.md`)
  for the full subfamily `a_1 = p^k` (any prime p, any exponent k>=1),
  strictly generalizing round 16's `2|a_1` special case: T=1, L=p, literal
  from n=1, via a self-contained strong induction with no FAH/H1/H2 machinery.
  ALWAYS treat this alongside the 2|a_1 theorem as a floor deliverable (round 18).
- **NTBT conjecture now has zero open numeric counterexamples**: round 17's
  flagged candidate exception (a_1=255255, type {5,7,11,13,17}) is resolved —
  it recurs at n=135914, triple-independently confirmed by 3 different scripts.
  Treat NTBT (N(Q)<=1 for all a_1) as strongly evidenced but still NOT proved
  (round 18).
- **NEW positive FAH-crux progress via the Two-Sided Singleton Witness
  Theorem** (`approaches/triangle-consistency-pigeonhole.md` §3, reviewer-
  verified): applying Singleton-Side FAH with ANY witness occurrence (not
  just the canonical/earliest one) on both sides of a rogue pair gives
  Cofinite FAH when matching singleton out-of-core signatures exist on both
  sides. Fully explains BOTH known hard rogue-pair test seeds (a_1=4807,
  11305) with zero exceptions. The residual open hypothesis — existence of
  matching singleton witnesses in general — is confirmed genuinely narrower
  than (not a restatement of) the original FAH crux. ALWAYS treat this as
  round 19's primary FAH target (round 18).
- NEVER re-attempt the Cross-Witness Common-Prime Lemma mechanism (the
  ORIGINAL triangle-consistency-pigeonhole outline target) — proved dead via
  the new certified Same-Type Triangle Vacuity result: any gcd>1 hit between
  two witnesses of the same shared type is fully explained by the type's own
  in-core primes, carrying zero out-of-core identity information (round 18).
- NEVER re-attempt the H2 counting/pigeonhole corridor (bounding self-
  absorption rounds via |𝒫'(S)|, |S_∞|, or type-count stabilization) without a
  genuinely new idea — all 3 sub-routes tried and confirmed dead (round 18).
- NEVER claim odd-prime p|a_1 trivializes FAH the way 2|a_1 does — REFUTED by
  a_1=15,45 (persistent period-4 base-type alternation between {3},{5}, only
  75%/25% divisibility, not cofinite) (round 18).
- NEVER treat |Q|=2 as a tractable general FAH subfamily — a 36-seed sweep
  reproduces exactly the same canonical hard seeds (187,209,221,247) used
  since round 6, no simplification found (round 18).
- 4 new lemmas certified round 18: `prime-power-seed-literal-periodicity-
  theorem.md`, plus (within triangle-consistency-pigeonhole, not yet
  separately certified as portable — check next round) the Double-Witness
  Nested Pigeonhole Lemma, Same-Type Triangle Vacuity, and Two-Sided
  Singleton Witness Theorem.

## Rules (additions from round 20)

- **a1-3q-subfamily-theorem is one gap away from a 3rd APPROVE**: literal
  T=1,L=3 periodicity for a_1=3q (prime q>=7, q!=5) is proved for all cases
  EXCEPT Case (b) with n even, k>=1 (occurrences after the first). The
  naive K-consecutive-integers pigeonhole bound is proven too weak (an
  adversarial CRT construction, q=11, rad~1.16e13, still has a witness far
  below the naive bound) — likely needs a Jacobsthal-type prime-gap theorem,
  not more pigeonhole bookkeeping. ALWAYS pick this up first next round if
  no fresh FAH corridor is found (round 20).
- **NEW general-purpose negative screen, reusable beyond this problem**:
  any argument premised on "two legal continuations/scenarios consistent
  with the same finite data" is INVALID without an explicit construction
  of both continuations, whenever the underlying recursion is fully
  deterministic given its seed (as this problem's greedy rule is) — there
  is no free ensemble to draw two scenarios from. This diagnosed round 19's
  circularity exactly and also kills Borel-Cantelli/ultraproduct-style
  "consistent scenario" arguments in one shot. ALWAYS apply this as a
  pre-build screen to any future statistical/ensemble-style FAH argument
  (round 20).
- **Constrained Singleton Coherence Lemma is certified but its "prime-power
  dominant class" numeric pattern is a CONFOUND, not evidence**: both known
  hard seeds (4807, 11305) already have an independently-established
  Cofinite-FAH witness prime from the Two-Sided Singleton Witness Theorem,
  which fully explains the observed pattern without needing the general
  conjecture. Do NOT cite the "prime-power dominant class" numeric sweep as
  supporting evidence for the general existence hypothesis without a
  genuinely fresh, non-confounded hard seed — none has been found yet after
  a ~70-seed heuristic scan (round 20).
- **NEVER re-attempt triangle-critical-dichotomy-witness's "sole rescuer"
  mechanism (Critical Prime Dichotomy Lemma branch (b))** — proved dead via
  the new certified Universal Branch-(a) Dominance Theorem
  (`lemmas/universal-branch-a-dominance-theorem.md`): branch (b) NEVER
  fires, for any index/prime/core, unconditionally. This slug should be
  retired (round 20).
- 5 new lemmas certified round 20: `constrained-singleton-coherence-
  lemma.md`, `universal-branch-a-dominance-theorem.md`,
  `a1-3q-parity-and-k0-window-lemmas.md`, `ambient-statistic-
  obstruction.md`, `vacuous-fah-under-2-divides-a1-corollary.md`.
- 15 consecutive plateau rounds (6-20) on the main FAH/H1 crux itself; 5th
  consecutive dead fresh-framing sweep (rounds 13,15,17,19,20) — treat the
  general-mechanism well as very likely fully exhausted. Priority-argument/
  finite-injury, computability/decidability framings, o-minimality/tame
  geometry, nonstandard-analysis/model-theory, and spectral/operator beyond
  transfer-operator are now ALL confirmed dead/inapplicable in addition to
  the pre-existing dead list (round 20).

## Rules (additions from round 19)

- NEVER re-propose `a_1 = p*q` (p,q distinct primes) as a tractable clean-
  periodicity subfamily — DEFINITIVELY REFUTED (round 19): for p=13, q=47 is
  messy while both q=43 and q=53+ are clean, so no monotone threshold f(p)
  exists; q>=2p is also not sufficient (q=31,37,43 for p=11 are messy despite
  q>=2p). This subfamily is exactly as hard as general FAH — do not spend
  another round probing it.
- The Two-Sided Singleton Witness Theorem's residual existence hypothesis
  (round 18's primary FAH target) does NOT close via an anatomy-of-integers/
  density-style argument — confirmed dead even at the weakest "infinitely
  often" sub-target (round 19): the persistent-type index set and out-of-core
  cofactor are defined only adaptively via the entire greedy legality history,
  with no closed form or CRT-independent local densities, so classical sieve
  methods (Brun/Selberg or any explicit-sequence method) are structurally
  inapplicable. A future attempt on this target needs a mechanism that does
  NOT require an explicit/closed-form sequence.
- The existing computational evidence for singleton-witness existence (0
  counterexamples across 7+ new seeds, round 19) is WEAK — near-statistically-
  inevitable at easy/under-recruited cores where singleton occurrences are
  85-92% dominant, not the 5-37% minority regime seen at the only 2 known
  genuinely hard properly-recruited cores (a_1=4807, 11305). Do not cite the
  7-new-seed sweep as strong evidence for the general hypothesis without this
  caveat (round 19).
- CAUGHT PRE-CERTIFICATION: a proposed "Generalized Class-Blindness
  Obstruction" meta-lemma (meant to kill the entire statistical-method family
  for FAH at once) had a genuine circularity — its "two scenarios agree" step
  asserted what would require an actual construction of two divergent legal
  continuations referencing realized sequence data, which the lemma's own
  premises can't produce. NOT certified (round 19). If re-attempted, the fix
  must supply an explicit construction of two divergent legal continuations,
  not assert their existence "by definition of open."
- The weaker H2 target "some self-absorbing S* exists" (vs. full NTBT) is NOT
  actually new content — it is verbatim the standing open sub-gap (a) of the
  already-certified Self-Absorbing Core Theorem, and hits the SAME
  Proposition-3 (M_B non-constructive) wall a third time when attacked via the
  new Monotone Chain Reformulation Lemma (round 19). Do not re-propose this
  framing as if it were a genuinely distinct, easier target without a new
  idea for bypassing Proposition 3 specifically.
- 4th consecutive dead fresh-framing sweep for the main FAH crux (rounds
  13,15,17,19) — p-adic/algebraic NT, generating functions, probabilistic/
  Borel-Cantelli, extremal graph theory, and finite-Fourier/character-sums are
  now ALL confirmed dead in addition to the pre-existing dead list (round 19).
  Seriously consider dedicating a near-future round to the write-up/insurance
  deliverable (Master Conditional Theorem + 2 certified subfamilies) if a 5th
  sweep also finds nothing.
- 5 new lemmas certified round 19: `elementary-omega-bound.md`,
  `monotone-chain-reformulation-lemma.md`, plus 3 pending round-18 lemmas
  finally certified after full independent re-verification:
  `double-witness-nested-pigeonhole.md`, `same-type-triangle-vacuity.md`,
  `two-sided-singleton-witness-theorem.md`.

## Rules (additions from round 16)

- **First APPROVE of the run**: `even-a1-full-periodicity-theorem` is `solved`
  and certified (`lemmas/even-seed-literal-periodicity-theorem.md`) for the
  restricted subfamily `2 | a_1`: unconditionally `a_n = a_1 + 2(n-1)` for all
  n≥1 (T=1, L=2, literal from n=1). ALWAYS treat this as the run's floor
  deliverable — if the general FAH crux remains unsolved by the end of the run,
  this is a genuine, reviewer-verified partial theorem to report, not a
  fallback to invent later (round 16).
- **H1 (FAH) trivializes when 2|a_1, but H2 (core-termination) does NOT**:
  `n1-periodicity-reconciliation`'s §4.1/§4.2 (round 16, reviewer-verified)
  proved FAH becomes vacuously true at cores containing 2, but the absorption-
  chain termination question stays genuinely open even in that case — do not
  assume 2|a_1 trivializes the whole conditional chain, only H1 (round 16).
- **M_B (the natural next-level refinement of N(S) from a one-prime-at-a-time
  recursion) is provably non-constructive** — proven as a general,
  toolkit-independent fact in `lemmas/binary-refinement-and-threshold-recursion.md`
  (round 16), extending round 13's Non-Constructivity result. Explains why the
  round-16 termination-lens explorer's numeric probe never stabilized on hard
  seeds. Any future core-termination (H2/N(S_k) boundedness) attempt must find a
  DIFFERENT quantity than M_B to bound, not attempt to make M_B constructive
  (round 16).
- 3 new lemmas certified round 16: `even-seed-literal-periodicity-theorem.md`,
  `binary-refinement-and-threshold-recursion.md` (2 lemmas: Binary Refinement
  Lemma, Threshold Recursion Bound Lemma).

## Rules (additions from round 15)

- **17th-and-onward "new mechanism" false positive caught pre-build**:
  `rogue-pair-termination-potential` (round 15) LOOKED like a new base-type-pair-
  counting mechanism but its steps 2-4 were verbatim duplicates of the already-
  certified `lemmas/collateral-safety-theorem.md`'s own Corollary/Theorem/
  Consequence paragraphs — its "genuinely new open key lemma" was literally FAH
  restated in that theorem's own text. BEFORE approving any future "bound a finite
  pool and show recruitment makes progress" outline, diff it against
  Collateral-Safety Theorem's full text first — this is now a known trap shape,
  not just a coincidence (round 15).
- **Sub-gap (b) of n1-periodicity-reconciliation is CLOSED**: ALWAYS cite the new
  certified **Literal n=1 Periodicity Theorem**
  (`lemmas/literal-n1-periodicity-theorem.md`, built on
  `lemmas/universal-early-intersection-lemma.md`) instead of the older
  Self-Absorbing Core Theorem when literal n=1 periodicity (not just eventual, from
  N(S*)) is needed — same two hypotheses (S* self-absorbing + FAH at level S*), no
  new hypothesis, unconditional relative to those. n1-periodicity-reconciliation's
  ONLY remaining open ingredients are now: (1) FAH itself (shared with main crux),
  (2) existence/termination of a self-absorbing S* (round 15).
- ALWAYS reuse round 15's certified **Termination Criterion Lemma**
  (`lemmas/termination-criterion-lemma.md`) if attacking existence/termination of a
  self-absorbing core S* — proved iff-reduction: absorption terminates iff the
  threshold sequence N(S_k) along the absorption chain is bounded. Independently
  confirmed to be a logically DISTINCT question from the main FAH crux (checked, not
  assumed) — do not treat proving this as equivalent to proving FAH, but also don't
  expect it to be easier without a genuinely new boundedness argument (round 15).
- **10 consecutive rounds (6-15) with zero progress on the main FAH/Symmetric FAH/
  Cofinite FAH/EEA crux itself**, despite continued real secondary progress every
  round. Round 15's 3-explorer sweep (bespoke narrow-case deeper dig, 5-angle fresh
  whole-problem framing, cross-domain crux-corpus mining outside number_theory) found
  ZERO new corridors — the strongest evidence yet that general mechanisms in the
  gcd-pigeonhole family (and all adjacent families: magnitude/sandwich, CRT-glue,
  sieve/density, automaton, Ramsey, monovariant, double-counting, compactness,
  additive-combinatorics) are exhausted for this exact crux. If round 16 ALSO finds
  no new corridor, seriously consider: (a) writing up the current best PARTIAL
  result honestly as the final deliverable (FAH stated precisely as the sole open
  ingredient, with the full unconditional reduction chain proven, matching the
  workspace's own repeated recommendation that this is now evidentially
  near-certain but proof-theoretically stuck); or (b) a structurally different kind
  of attack not yet tried at all: e.g. an explicit infinite family of a_1 seeds for
  which FAH CAN be proven by brute structural argument (not just verified
  numerically) as a partial/restricted theorem, narrowing the open case rather than
  solving it in full generality (round 15).

## Rules (additions from round 14)

- ALWAYS reuse round 14's certified **Self-Absorbing Core Theorem**
  (`lemmas/self-absorbing-core-theorem.md`) instead of re-deriving the n=1-literal-
  periodicity argument — it is now a COMPLETE, gap-free proof CONDITIONAL on FAH
  holding at a self-absorbing core S*. It does NOT prove FAH itself and does NOT
  yet establish that a self-absorbing S* exists/that the absorption process
  terminates, nor that N(S*) can be taken to be 0 — both remain explicitly open;
  do not cite this lemma as closing the n=1 gap outright (round 14).
- **16th FAH-adjacent mechanism confirmed dead**: integer-monovariant-difference-
  identity (crux aimo-0134 transplant) — ALL purely numeric (count/min/gcd/average)
  integer statistics built from this problem's greedy process are poisoned by the
  same structural fact: the certified legality test is class-blind (existence-only,
  never identity), so no such statistic's difference identity can recover
  identity-level (which-prime) information. Do not re-propose a running-average,
  running-min, overall-gcd, persistent-type-count, or recruited-core-size
  monovariant for FAH — all 5 concretely tried and killed, plus the general
  diagnosis rules out the whole family, not just these 5 (round 14).
- **Exact p-adic valuation monovariant induction for the Successor Claim is
  confirmed dead** (round 14) — v_{q*}(a_n) is demonstrably NON-MONOTONE along
  consecutive same-extended-type occurrences on the on-record a_1=11305 rogue-pair
  instance (valuation 2 then 1; later 3 then 1), and the Confined-GCD divisor class
  g_n is not absorbing (jumps to a richer value then reverts). Do not re-propose
  tracking exact valuations/prime-powers as a monovariant for FAH's Successor Claim
  without a fundamentally different invariant, not just finer bookkeeping on the
  same gcd-pigeonhole family (round 14).
- **rad(a_1)-induction (induction on ω(a_1) via reduction to the squarefree
  radical) is FALSIFIED** — a_1=105 and a_1=315=3²·5·7 share rad=105 but diverge
  from their very first recruited term with very different transient lengths;
  exponents on a_1's primes are NOT free to vary within a fixed-radical induction
  step. This is a 3rd structurally distinct failure of seed-reduction/induction-on-
  prime-factorization ideas (after rounds 8 and 12's seed-coupling-induction
  attempts) — a future revival needs a fundamentally different reduction step, not
  another aggregation/aggregation-radical variant (round 14).
- 9 consecutive rounds (6-14) with no proof of the main FAH/Symmetric FAH/Cofinite
  FAH/EEA crux itself, despite continued real secondary progress each round
  (2 more mechanisms killed this round: 16th direct, plus valuation-monovariant as
  a distinct negative result; 1 new certified lemma; n=1 secondary gap now fully
  closed conditional on FAH). If round 15 also finds no new corridor for the MAIN
  crux, escalate per CLAUDE.md's plateau-breaking guidance harder than before:
  consider whether a bespoke ad hoc argument restricted to the single concrete
  |F''|=2, multiplicity-1 case (round 12's Reduced-Alphabet Corollary reduces this
  to ONE fixed-integer divisibility-persistence question) is now the most promising
  remaining path, since 16 general mechanisms have failed and the general/mechanism
  well may be structurally exhausted for gcd-pigeonhole-family techniques (round 14).

## Rules (additions from round 13)

- **15th FAH-adjacent mechanism confirmed dead pre-build**: Central Sets Theorem /
  idempotent-ultrafilter (Hindman-style) recurrence — the machinery only guarantees SOME
  cell of a finite partition is central/syndetic, never the SPECIFIC target cell
  (q-divisible, A'-type) that FAH needs; this is the same "existential, not the one you
  wanted" wall restated in Ramsey vocabulary. Do not re-propose Ramsey-theoretic/
  ultrafilter recurrence arguments for FAH without a mechanism that pins the SPECIFIC
  target cell, not just partition-regularity in general (round 13).
- ALWAYS reuse round 13's certified **No-Restart Lemma**
  (`lemmas/no-restart-lemma.md`) — unconditional: restarting the greedy process at a
  later index a_k as a fresh seed is structurally invalid in general (dropping earlier
  constraints can only admit MORE legal candidates, never fewer, so the fresh-restart
  sequence can diverge at the very next step). Retroactively explains why rounds 3/5/8's
  well-ordering/induction attempts on a "smaller tail instance" all failed — cite this
  lemma to immediately kill any future proposal assuming a tail of the sequence is itself
  a fresh instance of the problem (round 13).
- **The n=1 secondary gap (literal periodicity from n=1, not just eventual) now has a
  precisely isolated remaining defect**, not just an untouched TODO: round 13's
  Self-Absorbing Core Theorem's CONCLUSION is correct (independently reconstructed by
  the reviewer) but its written proof has a gap in the "combining both parts" step —
  it cites Step 5's construction (`G := {sig(r) ∈ 𝒫'}`, a narrow condition) for a claim
  about a differently-defined BROADER eligible-residue set G* that Step 5 never actually
  establishes. A future n1-periodicity-reconciliation build should fix this specific
  step (tighten G* to match what Step 5 proves, or reprove the broader G* claim
  directly) rather than restart the theorem from scratch (round 13).
- **Pigeonhole thresholds N₀, N₁, N₁', N₂ used throughout the workspace are only
  EXISTENTIALLY finite, not effectively computable from a_1** (round 13's certified
  Non-Constructivity observation) — do not assume or claim an explicit/computable bound
  on these thresholds in any future approach; treat "finite" and "computable" as
  genuinely different claims here.
- REMOVED: none this round (all round 1-12 rules re-verified still applicable — FAH/
  Cofinite FAH/EEA remains the sole main-crux blocker, now with 15 confirmed-dead
  mechanisms total).

## Rules (additions from round 12)

- **EEA (Eventual Escape from Ambiguity) is now proved equivalent-difficulty to
  FAH/Cofinite FAH**, not an easier route — round 12's subword-complexity-
  periodicity approach independently derived (builder + reviewer, from scratch)
  that establishing EEA for one ambiguous residue is literally an instance of
  full (non-cofinite) FAH via the certified Confined-GCD Lemma. Do NOT dispatch
  a future approach hoping the Morse-Hedlund/EEA vocabulary is a shortcut around
  FAH without first identifying a genuinely new ingredient beyond the certified
  stack (round 12).
- **The "finite-defect" / vacuous-target framing for subword-complexity-
  periodicity is dead** — proved a one-line automatic consequence of the
  already-certified Bounded Gap Lemma, not real content (at most L₀ residues mod
  L₀ can ever be ambiguous, with no argument beyond alphabet finiteness). Do not
  re-propose "finitely many ambiguous windows" as if it were a nontrivial weaker
  target (round 12).
- ALWAYS reuse round 12's 2 new general-purpose certified lemmas
  (`lemmas/gap-periodicity-equivalence.md` = Lemma A, unconditional restatement
  of the goal as gap-sequence periodicity; `lemmas/red-k-periodicity-lemma.md` =
  Lemma B, the actual Morse-Hedlund pigeonhole+induction mechanism for ANY
  finite-alphabet sequence, reusable beyond this problem) instead of re-deriving
  them (round 12).
- ALWAYS reuse round 12's certified `lemmas/eea-implies-periodicity.md`
  (Theorem C, EEA at some finite core => periodicity) as an alternative,
  independently-verified derivation of the existing CRT/cyclic-pigeonhole
  finish's true hypothesis, if a future approach wants a cleaner endpoint to
  target than the original finish (round 12).
- ALWAYS reuse round 12's certified `lemmas/reduced-alphabet-corollary.md`
  (closed-form `|D_bad(q*)| = prod_{p in F''\{q*}}(e_p+1) - 1`) when working
  with covering-system-construction's D_bad object under Singleton-Side FAH
  conditions — collapses to a SINGLE residual divisor class in the standing
  `|F''|=2`, multiplicity-1 test seeds (a_1=4807, 11305). This is the most
  concrete fallback target for a future round if no further new corridor is
  found: attack this single fixed-integer divisibility-persistence question
  directly rather than the general FAH claim (round 12).
- NEVER re-attempt seed-coupling-induction's aggregate/set-level Base-Type
  Correspondence claim (round 12 revision) — FALSIFIED numerically (3/12
  (a_1, removed-prime) pairs, 2 robustly reconfirmed at 15,000 terms), same
  underlying failure mode (a locally-dominant prime doing unrepeatable work) as
  round 8's dead positional/frequency version. The seed-reduction/induction-on-
  ω(a_1) idea has now failed in two structurally different forms; a third
  revival needs a fundamentally different reduction step, not another
  aggregation of the same correspondence claim (round 12).
- **Explorer calibration note**: a_1=105 and a_1=315=3^2*5*7 share the same
  Q={3,5,7} but a_1=315 recruits a much larger core S₀ and does not stabilize
  into its eventual period even within 15,000 sampled terms (vs ~1000 for 105,
  T=58, L=210) — useful stress-test seed; treat "N-seed sweep found 0
  counterexamples" claims cautiously when seeds aren't checked for transient
  length, not just Q (round 12).

## Rules (additions from round 11)

- **FOURTEEN mechanisms for FAH/Cofinite FAH now confirmed dead** (see round 10
  Rules for #1-12; round 11 adds: #13 CRT-glue "Forced-Escape Blocking
  Construction" (force blocking-index witness outside S0 by CRT-matching a_n's
  full S0-signature while forcing prime q*) — killed by the outline-reviewer's
  numerical **CRT Magnitude Obstruction**: the competitor lands ~8 orders of
  magnitude above a_n, so Lemma K's dichotomy never reaches its informative
  branch; #14 the ENTIRE CRT-glue/competitor-construction family in full
  generality (not just the full-signature version) — killed by the builder's
  **Minimal-Modulus Generalization**: any partial-subset CRT modulus is either
  magnitude-doomed (needs all of Q to guarantee legality) or informationally
  uninformative (blocking witness is >99% S0-junk, never the target prime)).
  Do NOT re-attempt any CRT-glue/competitor-construction variant, at any modulus
  size — proven structurally impossible in full generality, not just difficult
  (round 11).
- **Sieve/density/analytic-counting technique family for Cofinite FAH is
  confirmed dead** (`sieve-density-exception-bound`, round 11) — both sub-routes
  (Mertens-style density comparison; Borel-Cantelli on an assumed decay rate)
  killed: sub-route (a) is window-class-blind, ruled out by the newly certified
  **Density-Argument Vacuity Corollary** (`lemmas/density-argument-vacuity-
  corollary.md`, extends Escape-Cost Vacuity/Sandwich Genericity Theorems to
  window/counting statements — no aggregate-count argument can ever distinguish
  the FAH exception set being finite vs. infinite); sub-route (b) is circular
  (assumes the open crux). ALWAYS check any future density/counting-style FAH
  argument against this corollary before building it out (round 11).
- **Three explorer lenses in round 11 (CRT/multiplicative structure of a_1;
  automaton/graph-walk encoding; Lemma K + Confined-GCD + Window Resolution
  combination) all independently found NO new top-level mechanism** — all three
  reduce to or are isomorphic to already-dead framings. The CRT lens's one
  genuine finding (value-gaps between same-type occurrences are exact multiples
  of 2·q·rad(A')) is real but circular — equivalent to the problem's own
  periodicity conclusion via `reversible-transition-map`'s certified
  equivalence. The automaton lens confirmed the finite-state graph-walk
  encoding IS the Successor Claim / reversible-transition-map equivalence under
  a different name. Do NOT re-dispatch either lens without a genuinely new
  angle not already covered (round 11).
- **SIX consecutive rounds (6-11) now stuck on the same FAH/Cofinite FAH crux**
  — a confirmed shared-gap plateau per CLAUDE.md. Proof-reviewer's round-11
  explicit recommendation: round 12 should push for at least one approach that
  abandons the shared "persistent-type reconciliation via class-blind/window-
  aggregate technique" corridor entirely (all 14 dead mechanisms fall in this
  corridor in some form); if the outliner still cannot find a genuinely
  different corridor, fall back to a bespoke small-|Q| or small-seed-family
  ad hoc argument to at least narrow the general claim, rather than dispatching
  yet another general-mechanism attempt doomed to the same wall (round 11).

- **TWELVE mechanisms for FAH/Cofinite FAH now confirmed dead** (see round 9 Rules for
  the first 9; round 10 adds: #10 Growth-Forced Divisibility/Escape-Cost Lemma — killed
  by Sandwich Genericity Theorem showing the Bounded Gap Lemma's sandwich is identical
  across all types/divisor-classes, so no class-blind magnitude argument can ever
  distinguish classes; #11 Escape-Budget attack on the Successor Claim — killed by
  Growing-Constraint Obstruction, the illegality witness pool for a skipped candidate is
  unboundedly growing, not the fixed-size pool the Confined-GCD Lemma controls; #12
  confined-competitor-construction — killed by Minimality Tautology Lemma, ANY
  competitor-construction mechanism that builds a legal candidate c with a_{n-1}<c<a_{n_j}
  is a logical impossibility by definition of minimality, not a provable-with-more-tools
  gap). Do NOT re-attempt any magnitude/sandwich-based class-distinguishing argument, nor
  any "construct a smaller legal competitor c and contradict minimality" mechanism — both
  families are now proven structurally impossible, not just difficult (round 10).
- ALWAYS reuse round 10's certified **Minimality Tautology Lemma**
  (`lemmas/minimality-tautology-lemma.md`) to IMMEDIATELY kill any future proposed
  "constructive competitor c, prove legal, contradict minimality" outline before
  dispatching a builder on it — check this lemma first, it's a one-line disqualifier.
  NOTE the corrected scope: it does NOT invalidate round-7's Lemma K (blocking-index
  extraction is a different proof shape, not a full-legality construction) — Lemma K
  remains separately dead for its own documented reason (round 10).
- ALWAYS reuse round 10's certified **Window Resolution Lemma**
  (`lemmas/window-resolution-lemma.md`) if scoping any future "window between consecutive
  same-type occurrences" argument — it proves the correct reading is the fully telescoped
  interval to the next occurrence, not a single greedy step (round 10).
- The crux corpus has now been searched exhaustively across 3 different explorer lenses
  (analytic/counting, fresh-framing, crux-mining) with NO exact structural match found for
  this problem's shape; the best analogues (aimo-0477, aimo-0678, aimo-0680, aimo-0682) all
  rely on a closed-form algebraic recurrence/successor map that this problem's
  greedy/existential definition of a_{n+1} does not have — confirmed as a fatal disanalogy
  by 2 independent explorers via different routes (round 10). Future crux-corpus mining
  should not re-search for a direct transplant; if revisited, look for problems whose
  legality condition is itself a minimality/existential search over ALL prior terms (not
  just a recurrence), which is the actual structural signature to match.
- **Four consecutive rounds (7-10) have now killed a mechanism via a genuinely distinct
  technique each time** (Blocking-Data Bridging/Lemma K; Recruitment-Budget counting;
  Successor-Transport/window-capacity family; this round's sandwich/growing-constraint/
  minimality-tautology trio) and all still bottom out at the same core problem: no
  certified tool currently in the stack extracts information about an ARBITRARY
  intermediate term's factorization — every tool either says "some prime works" (Free
  Facts, Bounded Witness) or bounds MAGNITUDE (Bounded Gap Lemma), never IDENTITY of which
  prime divides a specific far-away term. A genuinely new mechanism must supply an
  identity-level (not just existence- or magnitude-level) constraint on intermediate
  terms — e.g. from the multiplicative/CRT structure of a_1, or a wholly different
  encoding of the greedy process not yet tried (round 10).

## Rules (additions from round 9)

- **CORRECTED round-8 finding**: the "a_1=4807 shows ~6% divisibility, not cofinite"
  evidence AGAINST FAH was measured at the WRONG core (S₀=Q, i.e. before the Finite
  Core Theorem's recruitment) — NOT a genuine test of FAH at a properly recruited
  core. Do not cite it as counter-evidence to FAH going forward. At a correctly
  recruited core, a genuine |F'|,|F''|>=2 rogue pair (a_1=11305, canonical prime
  q*=11) shows 100% (zero-exception) divisibility — real positive evidence FOR FAH
  (round 9).
- **All 3 large seed sweeps this round (270+185+~100 seeds combined, across 2
  independent builders + the outline-reviewer) found ZERO genuine FAH
  counterexamples** at properly-recruited cores. FAH is now very well-supported
  computationally but still unproven — the obstruction is purely proof-theoretic
  (existential-to-universal promotion), not evidential (round 9).
- NEVER re-attempt "Recruitment-Budget / fixed Q-level witness pool W_{A,B} counting
  bound" for closing (†) — FALSIFIED round 9 (2 independent reimplementations,
  matching numbers exactly): a_1=209 forces prime q=7 at round-2 recruitment, and
  q=7 divides neither base-type witness a_2=220 nor a_3=228, so q ∉ W_{A,B}. A
  second escape confirmed at a_1=247. The "expand the pool dynamically" rescue is
  CIRCULAR — its own finiteness would already require the very recruitment-process
  termination that (†) asks to prove. This is the 9th confirmed-dead FAH-adjacent
  mechanism (round 9).
- ALWAYS reuse round 9's certified **Cofinite Sufficiency Lemma**
  (`lemmas/cofinite-sufficiency-lemma.md`): the existing finish (covering-system-
  construction Step 8.5) only needs COFINITE (eventually-always) divisibility, NOT
  literal zero-exception FAH. Any future FAH mechanism should target this strictly
  weaker claim, not the zero-exception version (round 9).
- ALWAYS reuse round 9's certified **Confined-GCD Lemma**
  (`lemmas/confined-gcd-lemma.md`) — strictly strengthens Divisor-Chain
  Well-Definedness, reduces the exception set to a finite-alphabet pigeonhole target
  via g_n := gcd(a_n, a_{n_B}) (round 9).
- ALWAYS reuse round 9's certified **Successor-Transport Reduction Lemma**
  (`lemmas/successor-transport-reduction-lemma.md`): IF a downward-transport/
  predecessor-inheritance successor claim on consecutive same-type occurrences
  holds, THEN cofinite FAH follows. The successor claim itself is NOT yet proved —
  it collapses into the same Lemma-I "branch fires uninformatively" pattern as 5+
  prior dead mechanisms when attacked via Lemma H branch analysis. A future attempt
  needs a genuinely different way to prove the successor step, not a repair of the
  Lemma H route (round 9).
- **The crux is now maximally sharpened**: FIVE independent framings (pigeonhole/
  dichotomy round 6-8, inductive chaining, exchange/minimality, two-witness
  intersection uniqueness round 7, scalar-well-ordering/algebraic-recursion round 7,
  seed-coupling-induction round 8, recruitment-budget-counting round 9, successor-
  transport round 9 — 9 total now) all reduce to or collapse into the SAME
  underlying obstruction: promoting an existential ("some prime of a fixed finite
  set divides a_n, for each n") to a universal/cofinite claim ("one specific prime
  divides ALL sufficiently large a_n of the type") without a genuinely new tool
  beyond the already-certified stack (Free Facts, Generalized Bounded Witness Lemma,
  Gap Lemmas, Lemma H, Confined-GCD). A future approach MUST bring a mechanism
  outside this family — e.g. a genuinely new monovariant/potential not built from
  gcd-pigeonhole, or an analytic/counting tool not yet tried in this workspace
  (round 9).

## Rules (additions from round 8)

- **The FAH crux is now narrowed further**: it's confirmed that the Fixed-Witness
  Divisor-Chain / pigeonhole mechanism's natural dichotomy is genuinely broken at a more
  basic level than canonicality — "recovering a prime already in S₀" is NOT a
  contradiction, it's tautological. Any future divisor-chain/pigeonhole mechanism for
  FAH must find a DIFFERENT way to derive a contradiction from the pigeonholed prime,
  not assume landing in S₀ is already impossible (round 8).
- ALWAYS reuse the round-8 certified **Singleton-Side FAH** lemma
  (`lemmas/singleton-side-fah.md`) — unconditionally proves FAH/cofinite-divisibility for
  free whenever the far witness's outside-core factor set F' is a singleton (direct
  corollary of the Generalized Bounded Witness Lemma, no pigeonhole needed). This means
  **the genuinely open content of FAH is entirely confined to the |F'|≥2 case** — do not
  re-test or re-cite singleton-F' seeds (e.g. a_1=187, 209) as if they were general
  evidence for FAH; they are already unconditionally solved. Future numerical checks of
  FAH/Symmetric FAH MUST report |F'| and specifically target |F'|≥2 seeds (e.g. a_1=4807)
  to be informative (round 8).
- ALWAYS reuse the round-8 certified **Divisor-Chain Well-Definedness** lemma
  (`lemmas/divisor-chain-well-definedness.md`) if building on the divisor-chain object
  d_n := gcd(a_{n_A}, a_n) (round 8).
- NEVER re-attempt "Seed-Coupling Lemma via single-prime-removal induction on ω(a_1)"
  in its round-8 form — FALSIFIED (builder + reviewer, independent from-scratch
  reimplementations, matching numbers exactly): whenever seed a_1 has 2∉Q, every
  single-prime-removal choice of reduced seed leaves Q' without 2, and the claimed
  type-correspondence between the original and reduced greedy sequences fails with a
  large (15-68%), non-vanishing-at-N=8000 mismatch rate. If a seed-reduction /
  induction-on-ω(a_1) idea is revived, it needs a fundamentally different reduction
  step (not single-prime removal) or a different correspondence claim — not a repair
  of this one (round 8).
- NEVER hold `greedy-exchange-cost-potential`'s occurrence-order induction and
  `covering-system-construction`'s Fixed-Witness Divisor-Chain as independent build
  slots in the same round while they share the identical open canonicality sub-lemma —
  the outline-reviewer correctly deduplicated this round; import whichever resolves it
  first rather than re-deriving independently (round 8).

## Rules (additions from round 7)

- NEVER re-attempt "Two-Witness Intersection Uniqueness via joint Critical-Prime-Dichotomy"
  for FAH — confirmed dead round 7 (both abstractly, by re-deriving Lemma H's actual proof
  which never extracts S₀-type info about a branch-(b) witnessing index, and concretely on
  a_1=4807 where both candidate primes trivially land in Lemma H's uninformative branch).
  This is the 4th confirmed instance of the Lemma-I dead-recombination family (round 7).
- NEVER re-attempt a fixed-pair scalar well-ordering / algebraic-recursion-locking mechanism
  (imported from crux aimo-0678) for FAH or the whole problem — RETHINK'd round 7. Proven
  counterexample a_1=175: recruiting prime q=2 breaks continuity between witness a_3=182 and
  a_4=189 (odd), refuting the hypothesized recursion q_k | w_{k+1}. Certified as the Witness
  Discontinuity Obstruction (lemmas/witness-discontinuity-obstruction.md): the "witness of the
  currently relevant type" is globally re-selected at every recruitment stage, not locally
  continuous, so no fixed-pair scalar recursion can work. Both natural repairs (fixed-pair
  tracking, |open(k)| scalar) collapse back into open FAH — don't re-propose either (round 7).
  If a scalar-well-ordering idea is revived, it needs a genuinely different scalar, not a
  repair of this one.
- ALWAYS reuse round 7's 5 certified lemmas (divisor-restricted-pigeonhole,
  adjacent-multiple-blocking, exact-equality-reduction-lemma [n=1 gap reduction],
  non-automaticity-of-prefix-folding, witness-discontinuity-obstruction) instead of
  re-deriving them (round 7).
- ALWAYS target "Joint FAH" (single prime q*:=min(F'∩F'') witnessing full absorption on BOTH
  sides at once) rather than proving FAH and Symmetric FAH separately — covering-system-
  construction's Step 8.7 Canonicalization Lemma (correct, not portable enough to certify
  standalone but safe to reuse within that approach) shows this unified target suffices for
  the finish, and Step 8.8 shows Blocking-Data-style mechanisms are side-agnostic anyway
  (round 7).
- "Blocking-Data Bridging" (using illegality/negative data from skipped greedy candidates,
  via Lemma K Adjacent-Multiple-Blocking) is the newest live angle on FAH — first mechanism
  in the workspace built from negative rather than positive divisibility facts. Stalled round
  7 on: Lemma K's constructed competitor has no controlled factorization relationship to the
  actual witness, so the Free-Facts-guaranteed shared prime can't be pinned to q. A repair
  needs to fix that factorization-control gap specifically, not just re-run the same
  construction (round 7).
- The n=1 secondary gap now has real machinery, not just an untouched TODO: the certified
  Exact-Equality Reduction Lemma reduces it to exactly N₀−1 explicit equalities, but round 7
  proved (by explicit counterexample) that the naive period-rescaling fix is NOT automatic —
  a precise, documented obstruction remains in covering-system-construction.md Step 9.3
  (round 7).

## Rules (additions from round 6)

- NEVER trust "Universal Singleton Hypothesis" (|F'|=1 always at a rogue-pair witness) —
  FALSIFIED round 6, independently reverified FOUR times (2 explorers, outline-reviewer,
  proof-reviewer, all from-scratch reimplementations): genuine |F'|=2 counterexamples
  a_1=4807 (F'={13,17}) and a_1=11305 (F'={11,103}), plus 3 more found in a 122-seed scan.
  Do not re-propose it in any form (round 6).
- ALWAYS reuse the round-6 certified Projection Lemma (lemmas/projection-lemma.md) and
  Collateral-Safety Theorem (lemmas/collateral-safety-theorem.md) — these UNCONDITIONALLY
  close the round-5 "collateral rogue pairs" gap (a base-type pair fully safe at S₀ stays
  fully safe at any refinement S₁⊇S₀), with zero dependence on the falsified Singleton
  Hypothesis. This reduces gap (†) to termination of a monotone-shrinking sequence over a
  FIXED FINITE set of ≤ C(|𝒫|,2) base-type pairs — a real narrowing, don't re-derive it
  (round 6).
- ALWAYS treat the current sharpest crux as the **Full-Absorption Hypothesis (FAH)**: the
  specific Lemma-G-guaranteed prime q (not all of F', which can have size ≥2) eventually
  divides EVERY sufficiently large term of the rogue pair's A'-side type. Empirically
  confirmed 0 counterexamples across 7+ seeds by TWO independent builders plus the
  proof-reviewer's 4th independent check, including the "Symmetric FAH" (B'-side too).
  Three independent proof attempts (Lemma H branch analysis, inductive chaining, exchange/
  minimality) have all failed — see greedy-exchange-cost-potential.md for why. A future
  approach needs a genuinely NEW mechanism, not a recombination of the four already-
  certified tools (Free Facts, Generalized Bounded Witness Lemma, Gap Lemmas, Lemma H) —
  proof-reviewer's round-6 diagnostic "Lemma I" formalizes why recombination can't work
  (round 6).
- NEVER re-attempt "recruitment-round-charging"'s three charging candidates (charge
  against ω(a_1), growth-rate charging, batch-resolution-as-independent-route) — all
  confirmed dead-end or crux-equivalent round 6. The "batch resolution" phenomenon (many
  simultaneous rogue pairs sharing one recruited prime) is real and well-documented but
  reduces to the same open FAH question from a different angle, not an escape from it
  (round 6). RETHINK'd this round; needs a genuinely different framing if revived.
- ALWAYS reuse round 6's Hub-Singleton-Batch Lemma (lemmas/hub-singleton-batch-lemma.md,
  certified, narrow corollary of Lemma G) if relevant to a hub-type's own F' set (round 6).

## Rules

- ALWAYS use the LITERAL MINIMAL/EARLIEST-occurrence witness (m_B = smallest index n with
  τ(n)=B, taking N_0=1 whenever all subsets of Q are persistent) when computing S/S₀ for the
  Finite Core Theorem / Generalized Bounded Witness Lemma — round 4's proof-reviewer found BOTH
  round-4 builders (and round 3's original a_1=175 "falsification") used a non-minimal witness
  (e.g. a tail-window sample instead of the true earliest occurrence), producing mutually
  inconsistent wrong S₀ values for the identical seed. Because: with the correct minimal witness,
  the "falsification" of the zero-further-recruitment-rounds conjecture evaporates — 18/18
  seeds (including a_1=175 itself: correct S₀={2,3,5,7,13}, ρ(3) and ρ(5) now intersect via 13,
  matching the true period T=274, L=2730 exactly) show V=∅. ALWAYS recompute S₀ from scratch
  with the minimal-witness convention before trusting or reusing any numerical rogue-pair example
  from rounds 3-4 (round 4).
- The round-3 "zero further recruitment rounds" FALSIFICATION is RETRACTED (superseded in
  current.md) — it was a witness-selection computational bug, not a genuine counterexample. The
  conjecture is REOPENED and now better-supported than ever (18/18 correct-witness seeds show
  V=∅). Do not re-cite round 3's a_1=175/a_1=385 "rogue pair" findings as valid; recompute them
  correctly first if referencing (round 4).
- ALWAYS reuse the new certified lemma from round 4, Lemma G / Extended Earliest-Witness
  Intersection (`lemmas/extended-earliest-witness-intersection.md`) — unconditional, gives a
  symmetric witness-index pair rather than the asymmetric Generalized Bounded Witness Lemma
  version (round 4).
- NEVER re-attempt the round-2 "universal glue prime" / "cost≤1 in sparse-Q regime" claims —
  these remain genuinely falsified by a_1=35 independent of the witness-selection bug (that
  falsification did not depend on witness choice) (round 2, reconfirmed round 4).
- Next-round target (sharper than prior gap (†) framing): attempt a DIRECT proof that V=∅
  always holds when S₀ is built from the Finite Core Theorem's literal minimal-witness
  convention — i.e. try to prove the (now well-supported empirically, unconditionally on
  18/18 seeds) "zero further recruitment rounds ever needed" statement outright, rather than
  building recruitment-process termination machinery on top of a process that may not be
  needed at all (round 4).
- ALWAYS treat "Core Lemma" / gap (†) — finiteness+mutual-reconciliation of the load-bearing prime
  set across pairwise-disjoint persistent types — as the true crux of this problem; both round-1
  approaches independently bottomed out here despite different framings (because reviewer verified
  the shared supporting lemmas are correct and the wall is genuine, round 1).
- ALWAYS reuse the 6 certified lemmas in results/imo-2026-06/lemmas/ (free-facts-gcd,
  bounded-gap-lemma, persistent-type-pigeonhole, bounded-witness-lemma [supersedes
  forced-linking-prime], finite-core-theorem) instead of re-deriving them; they're independently
  verified and unconditional (round 1).
- NEVER treat "Core Lemma" style self-sufficiency-of-witness-set claims as proved just because a
  conditional finish built on top of them is logically valid — check the claim isn't secretly
  smuggling in what the finish needs (amortized-charging-budget's circularity, flagged round 1).
- ALWAYS keep the secondary "periodicity from n=1 literally, not just eventually" gap on the radar
  for whichever approach closes the main gap first — untouched by both round-1 approaches, though
  empirically true on every tested seed.
- NEVER trust a "single universal witness prime" / bounded-recruitment-cost conjecture for gap (†)
  without checking a case where Q is missing MULTIPLE small primes (round 2: a_1=35, Q={5,7},
  falsified "cost=1" claims that looked ~100% confirmed on other seeds — true reconciling core
  needed TWO extra primes {2,3}, not one). ALWAYS test conjectures like this across a_1 values that
  are missing 2+ small primes from Q, not just 1.
- ALWAYS treat gap (†) via its round-2 sharper reformulation: an iterative recruitment process
  (start from Finite Core Theorem's S; find a (†)-violating pair; recruit a forced new prime via
  the Generalized Bounded Witness Lemma; repeat) — only TERMINATION of this concrete process is
  open, not the abstract refinement-intersection statement. This is a more attackable target than
  round 1's abstract (†) (round 2).
- ALWAYS reuse the 4 new certified lemmas from round 2 (generalized-bounded-witness-lemma,
  generalized-bounded-gap-lemma, single-witness-prime-pigeonhole, extended-persistent-type-
  pigeonhole) alongside the 6 from round 1 — all verified unconditional (round 2).
- ALWAYS reuse the 2 new certified lemmas from round 3 (canonical-refinement-lemma,
  canonical-witness-intersection = F_A∩F_B≠∅) — they localize gap (†) to the residual set V
  of "rogue pairs" (both sides non-canonical extended-type refinements); do not re-derive
  them, and do not re-attempt the minimal-counterexample or exchange-argument routes on V
  that round 3's two builders already showed fail for specific structural reasons (round 3).
- NEVER trust the "zero further recruitment rounds beyond the Finite Core Theorem's S"
  conjecture — FALSIFIED round 3 by a_1=175 (rogue pair {2,7} vs {3,5} forces recruiting
  prime 13, T=274, L=2730). The recruitment-process mechanism itself still works correctly
  on this case; only the "zero rounds" strengthening is false, not the underlying framework
  (round 3).
- NEVER register/build an approach whose only difference from a live approach is proof
  *technique* on the identical residual sub-lemma (e.g. minimal-counterexample-glue vs
  covering-system-construction on set V) — that's the single-gap trap in disguise, not
  framing diversity; fold it into the existing approach file instead (round 3,
  outline-reviewer).
- ALWAYS numerically test a claimed bound/conjecture across seeds with DIFFERENT prime
  magnitudes at fixed |Q|, not just varying |Q| — witness-depth-bound's "index is a function
  of |Q| alone" was falsified this way (index ranged 35-488 across four |Q|=4 seeds) (round 3).

## Rules (additions from round 5)

- NEVER trust "V=∅ always with minimal witnesses" (round 4's claim) — RE-FALSIFIED round 5,
  triple-independently reconfirmed (explorer, outline-reviewer, proof-reviewer each
  reimplemented the pipeline from scratch): genuine counterexamples a_1=187,209,247,385, each
  resolved by exactly one recruitment round via a Singleton F'. This was NOT a repeat of the
  round-3/4 witness-selection bug — the minimal-witness convention was applied correctly and
  the claim is just false as a blanket statement. The crux reverts to round 2-3's original
  recruitment-process framing (round 5).
- ALWAYS treat the "Universal Singleton Hypothesis" (|F'|=1 at any rogue-pair witness) as the
  precise remaining crux for the one-round case — proving it in general is the sharpest
  concrete target; case-by-case numeric confirmation is not proof (round 5).
- NEW gap surfaced round 5, previously unflagged: "collateral rogue pairs" — does refining
  S₀ → S₁ (recruiting new primes to resolve existing rogue pairs) spawn brand-new rogue pairs
  among base types that were safe at S₀? Unproved either way; 0 counterexamples on 3 tested
  seeds but not general. Any Simultaneous/Single-Pair Resolution Theorem that treats S₁ as
  terminal must address this or it's incomplete (round 5).
- NEVER re-attempt the "reversible-transition-map" / finite-automaton-bypass framing as a way
  to sidestep gap (†) — round 5's proof-reviewer and builder both independently proved forward-
  well-definedness of such a map is LOGICALLY EQUIVALENT to gap (†) itself, not a bypass. The
  certified equivalence lemma should be cited to shut down future re-proposals of this idea in
  any guise (round 5). The backward-injectivity half (targeting the secondary n=1-periodicity
  gap) is genuinely different content but is conditional on (†) and hit a new obstruction this
  round (early/small-index terms face weaker legality constraints than eventual-regime terms).
- NEVER re-attempt a well-ordering/minimal-counterexample descent on a size- or index-based
  measure for closing (†) directly — THREE independent measures have now failed for related
  "refinement manufactures new/larger classes, not smaller" reasons: round 3's set-size measure,
  round 5's witness-index-pair measure (non-monotone under recruitment), and the same
  refinement-based obstruction underlies the round-5 "collateral rogue pairs" gap. If a future
  approach wants a descent, it needs a genuinely different monovariant, not a variant of size/
  index (round 5).
- ALWAYS reuse round 5's 3 new certified lemmas (monotonicity-of-resolution.md,
  same-side-ordering-lemma.md, critical-prime-dichotomy.md = Lemma H) alongside all prior
  certified lemmas (round 5).

## Eval History (round 6 addition)

- Round 6: Status partial -> partial. IMPROVED (major reversal on the round-5 crux, real
  unconditional progress, sharper reopened target). 3 math-explorers (singleton-hypothesis,
  collateral-rogue-pairs, fresh-framing lenses) -> 1 proof-outliner (revised
  covering-system-construction toward Collateral-Safety Theorem + imported FAH; revised
  greedy-exchange-cost-potential to target FAH directly, retiring the falsified Singleton
  Hypothesis; new recruitment-round-charging approach) -> 1 outline-reviewer (independently
  reimplemented and CONFIRMED the Universal Singleton Hypothesis falsification from scratch;
  approved all 3 slugs for build) -> 3 proof-builders (parallel) -> 1 proof-reviewer
  (independently reverified everything a 4th time). Verdicts: covering-system-construction
  CHANGES REQUESTED (certified Projection Lemma + Collateral-Safety Theorem, unconditional,
  closes round-5's collateral-rogue-pairs gap for good; reduces (†) to termination over a
  fixed finite set of ≤C(|𝒫|,2) base-type pairs, further reduced to imported FAH/Symmetric
  FAH); greedy-exchange-cost-potential CHANGES REQUESTED (FAH stated precisely, verified
  empirically with 0 counterexamples across 7+ seeds both sides, 3 honest failed proof
  attempts documented, new diagnostic Lemma I not certified as portable); recruitment-
  round-charging RETHINK (all 3 charging candidates dead-end or crux-equivalent). 3 new
  lemmas certified (projection-lemma, collateral-safety-theorem, hub-singleton-batch-lemma).
  Elo: covering-system-construction ~1726 (leader), greedy-exchange-cost-potential ~1702,
  recruitment-round-charging ~1529 then RETHINK.

## Eval History (round 7 addition)

- Round 7: Status partial -> partial. IMPROVED (2 dead mechanisms retired cleanly, 5 new
  unconditional lemmas certified, sibling approaches decoupled). 3 math-explorers
  (density/growth-rate, minimality/greedy-structure, fresh-framing lenses) -> 1 proof-outliner
  (revised greedy-exchange-cost-potential toward "Two-Witness Intersection Uniqueness" +
  "Blocking-Data Bridging"; revised covering-system-construction toward Symmetric FAH mirroring
  + reopened n=1 secondary gap; new scalar-well-ordering-lock-in importing crux aimo-0678's
  technique) -> 1 outline-reviewer (flagged Two-Witness Uniqueness as high-risk possible
  repackaging of dead Lemma H branch analysis; approved scalar-well-ordering-lock-in as genuine
  diversification; build set = all 3) -> 3 proof-builders (parallel) -> 1 proof-reviewer
  (independently reconfirmed everything from scratch). Verdicts: greedy-exchange-cost-potential
  CHANGES REQUESTED (retracted Two-Witness Intersection Uniqueness as genuinely dead — 4th
  confirmed instance of the Lemma-I dead family, do not re-attempt; new Lemma J
  Divisor-Restricted-Pigeonhole + Lemma K Adjacent-Multiple-Blocking certified, first tools built
  from negative/illegality data, but Blocking-Data Bridging stalls: no controlled factorization
  link between Lemma K's competitor and the witness); covering-system-construction CHANGES
  REQUESTED (Step 8.7 Canonicalization Lemma decouples this approach from the sibling's now-dead
  mechanism via q*:=min(F'∩F''), reduces to "Joint FAH" — honestly scoped as not easier, just
  independent; Step 8.8 confirms Blocking-Data mechanism is side-agnostic so one proof would give
  both FAH+Symmetric FAH; Step 9 first real treatment of n=1 secondary gap — Exact-Equality
  Reduction Lemma certified + a proven counterexample showing the naive rescaling fix is NOT
  automatic, precise obstruction documented); scalar-well-ordering-lock-in RETHINK (found and
  proved a clean counterexample a_1=175 refuting the imported aimo-0678 recursion — recruiting
  q=2 breaks witness continuity, a_3=182 hands off to unrelated odd a_4=189; generalized+certified
  as Witness Discontinuity Obstruction; both natural repairs collapse back into open FAH, no
  independent route survives). 5 new lemmas certified (divisor-restricted-pigeonhole,
  adjacent-multiple-blocking, exact-equality-reduction-lemma, non-automaticity-of-prefix-folding,
  witness-discontinuity-obstruction).

## State

### Done
- Round 8: 3 math-explorers (density/asymptotic, fresh whole-problem framing, FAH
  direct-mechanism lenses) -> 1 proof-outliner (revised covering-system-construction's
  Fixed-Witness Divisor-Chain; opened new seed-coupling-induction as the mandatory
  plateau-breaking framing) -> 1 outline-reviewer (numerically verified scoping,
  build set = covering-system-construction, seed-coupling-induction) -> 2
  proof-builders -> 1 proof-reviewer. covering-system-construction CHANGES REQUESTED
  (found dichotomy branch is tautological, not a contradiction; certified
  Singleton-Side FAH byproduct showing FAH's open content is entirely the |F'|≥2
  case). seed-coupling-induction RETHINK (single-prime-removal reduction falsified
  for any seed with 2∉Q). 2 new lemmas certified.
- Round 4: 3 math-explorers (monovariant/well-ordering, joint-family/simultaneous-constraint,
  fresh-framing lenses) -> 1 proof-outliner (revised covering-system-construction toward a
  "Persistent Uniform Core Lemma", revised greedy-exchange-cost-potential toward a scoped
  "Round Resolution Lemma" via time-ordered minimality; new uniform-core-direct-induction
  approach proposed) -> 1 outline-reviewer (caught PUCL's Step-3 non-sequitur as a restated-
  falsified-claim risk before build, rescoped Round Resolution target, RETHOUGHT the new
  approach as duplicative of PUCL not real diversity; build set = covering-system-construction,
  greedy-exchange-cost-potential) -> 2 proof-builders (covering-system-construction: proved
  PUCL false in all forms tried incl. a numeric a_1=175 "counterexample"; greedy-exchange-cost-
  potential: proved new Lemma G unconditionally, proved a rescoped Round Resolution Lemma
  CONDITIONAL on an unproved Singleton Hypothesis, honestly documented why a time-ordered
  minimality induction stalls) -> 1 proof-reviewer (MAJOR FINDING: independently recomputed
  S₀ for a_1=175 and found BOTH builders, plus round 3's original finding, used a non-minimal/
  incorrect witness choice, giving 3 mutually-inconsistent wrong S₀ values for the same seed;
  with the theorem's literal minimal-witness convention, S₀={2,3,5,7,13}, the claimed rogue
  pair actually intersects via 13, matching the true period T=274/L=2730 exactly; RETRACTED
  round 3's "zero further recruitment rounds" falsification, reverified 18/18 seeds show V=∅
  with correct witnesses; certified Lemma G to lemmas/extended-earliest-witness-intersection.md;
  both slugs CHANGES REQUESTED/partial; current.md updated with a prominent correction section
  and sharper next-round target).
- Round 1: workspace initialized (results/imo-2026-06/{approaches,lemmas}, current.md status=unsolved).
  numpy/scipy/sympy installed.
- Round 1: 3 math-explorers (graph/hypergraph, modular/CRT, density/pigeonhole lenses) -> 1
  proof-outliner (4 approaches) -> 1 outline-reviewer (ranked, build set = amortized-charging-budget
  + covering-system-construction) -> 2 proof-builders (both partial) -> 1 proof-reviewer (both
  CHANGES REQUESTED, 6 lemmas certified, current.md updated with merged best progress and gap (†)).

### Broken
(none — no failing builds/tests; this is a proof-only workspace)

### Done
- Round 12: 3 math-explorers (multiplicative structure, small-|F'| bespoke,
  fresh whole-problem framing) -> 1 proof-outliner (new subword-complexity-
  periodicity via Morse-Hedlund; revised seed-coupling-induction; bookkeeping-
  only touch to covering-system-construction) -> 1 outline-reviewer (APPROVE
  new approach, RETHINK the seed-coupling-induction revision, build set =
  subword-complexity-periodicity + covering-system-construction) -> 2
  proof-builders -> 1 proof-reviewer. Both CHANGES REQUESTED/partial. 4 new
  lemmas certified (gap-periodicity-equivalence, red-k-periodicity-lemma,
  eea-implies-periodicity, reduced-alphabet-corollary). Plateau-break achieved
  per round-11 mandate: EEA now proved equivalent-difficulty to FAH (not a
  shortcut), and the residual alphabet collapses to a single divisor class in
  the |F''|=2 mult-1 test seeds — concrete fallback target for round 13.

### Done
- Round 13: 3 math-explorers (de Bruijn/special-factor deeper dig, bespoke
  |F''|=2 mult-1 narrow-case, fresh whole-problem framing) -> 1 proof-outliner
  (new central-sets-idempotent-recurrence; revised greedy-exchange-cost-
  potential with No-Restart Lemma; new n1-periodicity-reconciliation) -> 1
  outline-reviewer (RETHINK central-sets-idempotent-recurrence pre-build as
  15th dead mechanism; build set = greedy-exchange-cost-potential,
  n1-periodicity-reconciliation) -> 2 proof-builders -> 1 proof-reviewer. Both
  CHANGES REQUESTED/partial. 1 new lemma certified (no-restart-lemma,
  unconditional). Self-Absorbing Core Theorem's conclusion confirmed correct
  but proof has a fixable gap in "combining both parts" step (see Rules).

### Done
- Round 14: 3 math-explorers (fresh whole-problem framing, crux-corpus identity-
  level-tool mining, p-adic valuation/monovariant lens) -> 1 proof-outliner
  (revised n1-periodicity-reconciliation with a fix plan; new
  integer-monovariant-difference-identity adapting crux aimo-0134) -> 1
  outline-reviewer (caught the outliner's proposed fix as fictitious, supplied
  the correct Sufficiency+Landing fix itself; build set = both) -> 2
  proof-builders -> 1 proof-reviewer. n1-periodicity-reconciliation CHANGES
  REQUESTED/partial — "combining both parts" gap genuinely closed, new lemma
  certified (self-absorbing-core-theorem), still conditional on FAH throughout.
  integer-monovariant-difference-identity RETHINK/unsolved — 16th FAH mechanism
  killed with a generalizing diagnosis (all numeric monovariants from this
  problem's class-blind legality test are structurally poisoned). Main crux
  untouched, 9th consecutive plateau round on it (6-14), though continued real
  secondary progress each round.

### Done (round 22)
- Round 22: 3 math-explorers (Jacobsthal citable-literature lens, FAH-seed-
  deepening lens, fresh-framing lens) -> 1 proof-outliner (new
  orbit-merging-additive-offset-dichotomy targeting H1; revised
  a1-3q-subfamily-theorem with Option (a)/(b); fah-counterexample-hunt held
  out) -> 1 outline-reviewer (build set = both new/revised) -> 2
  proof-builders (parallel) -> 1 proof-reviewer. a1-3q-subfamily-theorem
  **APPROVE (solved, 3rd APPROVE of the run)** — closed via new certified
  Legendre Sieve Gap Bound + Primorial Floor Bound. orbit-merging-additive-
  offset-dichotomy RETHINK (unsolved) — disambiguation check failed, both
  offset-object instantiations dead (one mistargets H2, one is equivalent
  to the theorem itself — circular). 2 new lemmas certified. Run now has 3
  certified solved sub-family theorems (2|a_1; a_1=p^k; a_1=3q) + gap-free
  Master Conditional Theorem; main FAH crux (H1) still open, 17th
  consecutive plateau round (6-22).

### Next
- Round 22: for round 23, the run now has 3 solved subfamilies as a floor
  deliverable and the main crux (H1/FAH) at its 17th consecutive plateau
  round with the general-mechanism well now very likely exhausted (7+
  fresh-framing sweeps all dead, 30+ direct mechanisms dead). Two options
  worth weighing for round 23: (a) if a math-explorer can find yet another
  genuinely new H1 corridor (unlikely per the exhaustive sweep record, but
  cheap to check with 1 explorer lens before giving up), pursue it; (b)
  seriously consider dedicating round 23 (or soon after) to a comprehensive
  write-up/insurance deliverable consolidating the Master Conditional
  Theorem + 3 certified subfamily theorems (2|a_1 T=1,L=2; a_1=p^k T=1,L=p;
  a_1=3q T=1,L=3) as the run's floor, explicitly stating H1(FAH)+H2
  (absorption-chain termination) as the sole remaining open ingredients,
  given diminishing returns from further generic exploration. Do NOT
  re-attempt: orbit-merging/additive-offset-dichotomy (dead, round 22, see
  Rules), any of the 30+ previously-dead H1 mechanisms (see Rules
  cumulative list), a_1=p*q as a subfamily (refuted round 19). If pursuing
  a 4th subfamily theorem, a1-3q's sieve-tool success (Legendre Sieve Gap
  Bound) suggests other subfamilies with a similarly bounded/simple
  residual-gap structure might now be reachable using the same new tools —
  worth an explorer lens scouting candidate subfamilies with this pattern.
  Continue math-explorer -> proof-outliner -> outline-reviewer -> builders
  -> reviewer flow per CLAUDE.md.
- Round 21: for round 22, two live concrete threads. (a) a1-3q-subfamily-
  theorem's Case (b)/n-even/k>=1 gap needs a genuine (non-elementary)
  Jacobsthal-function-level bound on g(M) — either find a citable sieve-
  theory result in the crux corpus/literature that can be proved or cited
  properly per KB rules, or find a problem-specific shortcut that avoids
  needing the general g(M)<=2^ω(M) bound entirely (e.g. exploit the specific
  structure of M=3q-derived moduli rather than a fully general bound). Do
  NOT re-attempt the elementary halving-induction or AP-peel repairs, both
  confirmed dead this round. (b) fah-counterexample-hunt's one inconclusive
  seed (a_1=105945, CRT-lopsided |Q|=4) should be deepened (search T<25000
  was insufficient) using the new literal-period-detection tool before
  drawing any conclusion; alternatively pivot fah-counterexample-hunt to the
  outline's structural non-intersection-invariant proof attempt (§1.3(a))
  per the reviewer's suggestion, now that undifferentiated seed sweeping has
  hit diminishing returns. Given 16 consecutive plateau rounds on H1 itself
  and 6 exhausted fresh-framing sweeps, do NOT dispatch a 7th generic
  fresh-framing explorer without first exhausting threads (a) and (b) above,
  which are concrete and unexhausted. Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per
  CLAUDE.md.
- Round 19: for round 20, the anatomy-of-integers/density route to the
  Two-Sided Singleton Witness Theorem's existence hypothesis is now dead
  (structurally inapplicable — no closed-form sequence). Two live threads:
  (a) if a math-explorer can find a mechanism for singleton-witness existence
  that does NOT require an explicit/closed-form sequence (e.g. a genuinely
  new pigeonhole/recursive argument using only the certified Generalized
  Bounded Witness Lemma's "divides infinitely many occurrences" foothold,
  bridging to "is the sole escaping prime"), pursue it; (b) given the 4th
  consecutive dead fresh-framing sweep (rounds 13,15,17,19) on the main FAH
  crux, seriously consider dedicating round 20 (or soon after) to the
  write-up/insurance deliverable — consolidate the Master Conditional Theorem
  + 2 certified subfamily theorems (2|a_1; a_1=p^k) + the now-certified
  Generalized Class-Blindness family of obstructions (once a correct,
  non-circular version exists — round 19's attempt was caught circular, do
  NOT re-certify without fixing that first) as the run's floor deliverable.
  Do NOT re-attempt: a_1=p*q as a tractable subfamily (definitively refuted,
  round 19); the weaker H2 "some self-absorbing S* exists" target via the
  Monotone Chain Reformulation Lemma (dead, same Proposition-3 wall, round
  19); any sieve/density-based closure of the singleton-witness hypothesis
  (round 19). Continue math-explorer -> proof-outliner -> outline-reviewer ->
  builders -> reviewer flow per CLAUDE.md.
- Round 18: for round 19, pursue the newly-narrowed FAH residual: prove (or
  find a counterexample to) "existence of matching singleton witnesses" (the
  Two-Sided Singleton Witness Theorem's hypothesis, results/imo-2026-06/
  approaches/triangle-consistency-pigeonhole.md §3-4) — this is a genuinely
  narrower, more concrete target than the original FAH crux, first real
  positive progress on the main crux since round 9-10. Test it computationally
  on more rogue-pair seeds beyond 4807/11305 first (both known hard test seeds
  are the same two used since round 8; find/construct new ones with |F'|,|F''|>=2
  if possible) before attempting a general proof. Do NOT re-attempt: the
  original Cross-Witness Common-Prime Lemma mechanism (dead, Same-Type Triangle
  Vacuity), the H2 counting/pigeonhole corridor (exhausted, 3 sub-routes dead),
  odd-prime-trivializes-FAH or |Q|=2-is-tractable (both refuted round 18).
  NTBT numeric support is now clean (zero open counterexamples across 50+
  seeds) — treat as strong evidence, still not proof. 2 solved sub-family
  theorems now certified (2|a_1 T=1,L=2; a_1=p^k T=1,L=p) — consider whether a
  future round should also check other small tractable subfamilies (e.g.
  a_1=p*q with q>>p, flagged as a live but unproven empirical lead by round
  18's audit-insurance explorer, counterexample a_1=341=11*31 exists so not
  universal — needs the exact threshold, if any). Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 17: 3 math-explorers (restricted-family-extension, H2-termination-
  quantity, fresh whole-problem framing) -> 1 proof-outliner -> 1
  outline-reviewer (RETHINK 1 pre-build, APPROVE 1) -> 1 proof-builder -> 1
  proof-reviewer. Result: new certified Vacuous/Weak Self-Absorption Lemma
  (N(Q)<=1 suffices for S_0=Q to be self-absorbing, zero rounds) — real H2
  progress; NTBT conjecture (N(Q)<=1 for ALL a_1) honestly open; a builder
  numeric overclaim on a_1=255255 caught and corrected by the reviewer. Main
  FAH crux (H1) untouched — 12th consecutive plateau round (6-17), and 3
  independent fresh-framing sweeps (rounds 13, 15, 17) now agree the direct-
  mechanism well is exhausted. No restricted-family theorem exists beyond
  prime-power/2|a_1 (round 17 confirmed with fresh numerics — don't re-probe
  this). For round 18: (a) if attempting H2 again, try proving or refuting the
  NTBT conjecture (N(Q)<=1 for all a_1) directly, or try the untried
  |𝒫'(S)|-combinatorial-bound angle flagged by round 17's H2-termination
  explorer (NOT the type-alphabet-counting-bound framing already RETHINK'd —
  find a genuinely different way to use |𝒫'(S)|, since that specific framing
  collapsed into the dead N(S_k)-bounded question); (b) given 3 consecutive
  dead fresh-framing sweeps for the MAIN FAH crux, seriously consider
  dedicating a round to polishing/writing up the final deliverable (Master
  Conditional Theorem + 2|a_1 special case + Vacuous Self-Absorption Lemma),
  stating FAH as the sole remaining open ingredient, as insurance if no new
  corridor appears; (c) if a math-explorer is dispatched again on fresh-
  framing for FAH, it should be told explicitly that ultraproduct/compactness,
  per-prime indicator decomposition, transfer-operator, and LP-duality
  relaxation are now ALL confirmed dead (round 17) in addition to the
  pre-existing 17-mechanism dead list. Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per
  CLAUDE.md.
- Round 14 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH / Cofinite FAH**
  (now 15 confirmed-dead mechanisms; Central Sets Theorem/idempotent-ultrafilter
  is the latest, killed pre-build round 13 — do not re-propose Ramsey-theoretic
  recurrence arguments without a mechanism pinning the SPECIFIC target cell).
  Two live threads: (a) if explorers find a genuinely new corridor for the main
  crux, pursue it — round 12's Morse-Hedlund corridor and round 13's bespoke
  |F''|=2 narrow case are both now exhausted, re-dispatching either without new
  content wastes builder slots; (b) continue n1-periodicity-reconciliation's
  Self-Absorbing Core Theorem — fix the specific "combining both parts" gap
  (Step 5's G construction doesn't establish the broader G* claim used) rather
  than restarting; this is conditional on FAH so won't alone solve the problem,
  but is real independent progress on the secondary gap. Consider whether
  round 13's reviewer/explorer findings justify another explicit escalation per
  CLAUDE.md's plateau-breaking guidance if round 14 also finds no new corridor
  for the MAIN crux (7 rounds stuck on FAH itself, rounds 6-13, even though
  secondary/defensive progress continues each round). Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 13 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH / Cofinite FAH**
  (now also expressible as EEA at some finite core, proved equivalent-difficulty
  round 12 — do not re-dispatch EEA hoping it's a shortcut without a genuinely
  new ingredient). Two live threads: (a) if another genuinely new corridor can
  be found by explorers, pursue it (round 12's Morse-Hedlund corridor is now
  itself absorbed into the standing crux, not exhausted as a toolset — de Bruijn
  graph / special-factor techniques beyond Lemma B/Theorem C weren't tried); (b)
  otherwise, attack the concrete fallback per round 12's Reduced-Alphabet
  Corollary: in the |F''|=2, multiplicity-1 case (a_1=4807, 11305), FAH reduces
  to a SINGLE fixed-integer divisibility-persistence question (does one specific
  prime divide gcd(a_n, a_{n_B}) for all sufficiently large n of the type) —
  try a bespoke direct attack on this single-integer case per CLAUDE.md's
  plateau-breaking escalation guidance, rather than another general-mechanism
  attempt. Continue math-explorer -> proof-outliner -> outline-reviewer ->
  builders -> reviewer flow per CLAUDE.md.
- Round 12 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH / Cofinite FAH**,
  now on its SIXTH consecutive round with no genuinely new corridor found (see
  round 11 Rules). FOURTEEN mechanisms confirmed dead, spanning 6 structurally
  distinct technique families (existential/pigeonhole, magnitude-sandwich,
  tautological-minimality, CRT-glue/competitor-construction, sieve/density,
  automaton/graph-walk — the last 3 all closed this round). Three independent
  explorer lenses this round (CRT-structure-of-a_1, automaton-encoding, Lemma-K-
  combination) found NOTHING new — all reduce to already-dead framings. This is
  a confirmed shared-gap plateau per CLAUDE.md's plateau-breaking guidance:
  round 12's outliner MUST put up at least one approach from a corridor outside
  "persistent-type reconciliation via class-blind/window-aggregate technique"
  entirely (per reviewer's explicit round-11 recommendation) — do not dispatch
  another variant within that corridor without first identifying a concrete
  new corridor. If no genuinely new corridor can be found after another
  explorer round, fall back to a bespoke small-|Q| or small-seed-family ad hoc
  argument (e.g. prove FAH unconditionally for |Q|<=2 or |F'|=2 specifically)
  to at least narrow the general claim rather than repeating a doomed general-
  mechanism attempt. Continue math-explorer -> proof-outliner ->
  outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 11 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH / Cofinite FAH**.
  TWELVE mechanisms now confirmed dead (see round-10 Rules for the full updated
  list). The diagnosis is now sharp: every certified tool in the stack gives either
  EXISTENCE ("some prime of a fixed set divides a_n") or MAGNITUDE ("a_n is between
  these bounds"), never IDENTITY-level information about an arbitrary intermediate
  term's factorization — that is precisely the missing ingredient. A future approach
  MUST bring a tool that pins down WHICH prime(s) divide a specific far-away term,
  not just how many or how big. Candidates worth exploring: (a) the multiplicative/
  CRT structure of a_1 itself (not yet directly exploited — every mechanism so far
  treats a_1's prime factorization only via Q, never via deeper structure like which
  residues mod small primes are forced); (b) a wholly different encoding of the
  greedy process — e.g. as a walk in a graph/automaton whose transitions ARE
  identity-preserving, rather than trying to retrofit identity information onto
  magnitude/existence tools; (c) revisit whether round-7's still-undead Lemma K
  (blocking-index extraction) can be pushed further now that Confined-GCD and
  Window Resolution are certified — it was not re-killed this round, only
  confined-competitor-construction's different construction was. The crux corpus
  has been exhaustively mined (3 lenses, round 10) with no direct transplant found;
  do not re-search for one unless a problem matching "legality = minimality/
  existential search over ALL prior terms" surfaces. Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 10 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH** (now known to only
  need the COFINITE, not zero-exception, version per the certified Cofinite
  Sufficiency Lemma). NINE mechanisms are now confirmed dead, all collapsing into
  the same existential-to-universal promotion obstruction (see round-9 Rules above
  for the full list). Computational evidence for FAH is now very strong (0
  counterexamples across 550+ combined seed-checks at properly-recruited cores) —
  this is a proof-theoretic gap, not an evidential one. Two live threads worth
  pursuing: (a) the Successor-Transport Reduction Lemma reduces the remaining work
  to ONE specific successor claim (consecutive same-type occurrences inherit
  divisibility) — needs a genuinely different proof route than Lemma H branch
  analysis; (b) the window-capacity counting-bound framing (cofinite-window-
  capacity-bound) reduces to ruling in the q*-divisor-class specifically among
  Confined-GCD's finite alphabet — needs a tool that distinguishes classes, not just
  bounds their count. Per CLAUDE.md and the round-9 Rule, the next new approach (if
  any) should bring a mechanism OUTSIDE the gcd-pigeonhole family entirely (e.g. an
  analytic/counting tool, or a structural argument using the multiplicative/CRT
  structure of a_1 not yet exploited). Continue math-explorer -> proof-outliner ->
  outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 9 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH**, now sharpened further:
  the Fixed-Witness Divisor-Chain/pigeonhole mechanism's natural dichotomy is broken at
  a more basic level than canonicality (recovering a prime already in S₀ is NOT a
  contradiction — tautological, not informative). A future mechanism must derive its
  contradiction differently, not assume S₀-membership is already impossible. Also:
  **Singleton-Side FAH is now certified and unconditional** — the ENTIRE open content of
  FAH is confined to the |F'|≥2 case (a_1=4807-style seeds); do not treat singleton-F'
  seeds (187, 209) as general FAH evidence going forward, they're already solved. The
  seed-coupling-induction framing (induction on ω(a_1) via single-prime removal) is
  RETHINK'd/dead in its round-8 form — do not repair it, needs a fundamentally different
  reduction step if revived. greedy-exchange-cost-potential's occurrence-order induction
  (sketched but not built this round) remains a live option — genuinely sidesteps the
  Witness Discontinuity Obstruction, but shares the same open canonicality sub-lemma as
  covering-system-construction AND has its own unresolved pigeonhole-anchoring gap; import
  covering-system-construction's canonicality progress rather than re-deriving. The n=1
  secondary gap is still blocked on Joint FAH being resolved first (per round 8 finding).
  Continue math-explorer -> proof-outliner -> outline-reviewer -> builders -> reviewer
  flow per CLAUDE.md; consider whether the |F'|≥2 confinement (round 8) is itself sharp
  enough to justify a dedicated new mechanism aimed SPECIFICALLY at |F'|≥2 rogue pairs.
- Round 8 (superseded, kept for audit): sole remaining crux is still **FAH + Symmetric FAH** (now unified: covering-
  system-construction's Step 8.7 shows a single "Joint FAH" proof — one prime q*:=min(F'∩F'')
  witnessing full absorption on BOTH sides at once — suffices, and Step 8.8 confirms any
  Blocking-Data-style mechanism would be side-agnostic, so target Joint FAH directly rather
  than two separate proofs). FOUR proof mechanisms are now confirmed dead (Lemma I family):
  Lemma H branch analysis, inductive chaining, exchange/minimality competitor construction,
  and (round 7) "Two-Witness Intersection Uniqueness via joint Critical-Prime-Dichotomy".
  A FIFTH framing (scalar-well-ordering-lock-in importing crux aimo-0678) also RETHINK'd
  round 7 — Witness Discontinuity Obstruction shows no fixed-pair scalar recursion can work
  because the "witness of the currently relevant type" is globally re-selected at every
  recruitment stage, not locally continuous. "Blocking-Data Bridging" (using illegality/
  negative data from skipped candidates, via new Lemma K) is the newest genuinely-different
  angle but stalled this round on: no controlled factorization link between Lemma K's
  constructed competitor and the actual witness. A future approach needs either (a) a
  repaired Blocking-Data mechanism that fixes this factorization-control gap, or (b) a truly
  new mechanism per Lemma I's diagnosis — converting an existential per-occurrence
  divisibility fact into a uniform/cofinite identity claim, still unexplored beyond the 5 now-
  dead families. Do NOT re-attempt: all round 1-6 dead items (see Rules), Two-Witness
  Intersection Uniqueness (round 7, confirmed dead against Lemma H's own proof + a_1=4807),
  scalar-well-ordering-lock-in's fixed-pair or |open(k)| repairs (round 7, both collapse into
  FAH). Separately, the n=1 secondary gap now has real machinery: Exact-Equality Reduction
  Lemma (certified) reduces it to N₀−1 explicit equalities, but the naive rescaling fix is
  PROVEN not automatic (round 7 counterexample) — a documented precise obstruction remains,
  worth a dedicated attempt if FAH stays stuck. Continue math-explorer -> proof-outliner ->
  outline-reviewer -> builders -> reviewer flow per CLAUDE.md.

## Eval History (round 25 addition)

- Round 25: Status remains `partial` overall (4 certified subfamily
  theorems stand as the run's floor: 2|a_1 T=1,L=2; a_1=p^k T=1,L=p; a_1=3q
  T=1,L=3; a_1=3^a*q T=1,L=3 for a=1..5). No APPROVE this round, but 2 new
  certified lemmas and genuine narrowing on 3 fronts. 3 math-explorers
  (a1-3qk m=3-closure lens, H2 seed-asymmetry lens, diversity-scout lens)
  -> found: (1) m=3 closure for a1-3qk is a routine finite-table close
  (26 total exceptions, all small q, same pattern as m=1/m=2, refuted
  current.md's "two-dimensional argument" speculation); (2) round 24's H2
  "11305 diverges ~sqrt(N)" claim was a measurement ARTIFACT of a
  global-power-law fit contaminated by early transient growth — corrected
  local-exponent analysis on a much larger sim (up to n=750k-1M) shows
  BOTH hard seeds (4807, 11305) decelerating, just at different
  rates/scales (11305's bigger S_0 core needs more runway); (3) the
  certified Legendre Sieve Gap Bound + Primorial Floor Bound toolkit is
  prime-agnostic — a_1=p*q for general odd prime p (not just p=3) gives
  finite stable exceptional sets numerically, a genuinely new broader
  subfamily target. -> 1 proof-outliner (advanced a1-3qk-subfamily-theorem
  toward m=3 closure; advanced a1-5q-subfamily-theorem; new
  a1-pq-subfamily-theorem targeting uniform-in-p reduction; advanced
  n1-periodicity-reconciliation with the corrected H2 diagnosis) -> 1
  outline-reviewer (seeded the missing a1-pq approach file per recurring
  outliner-doesn't-write-files issue; resolved single-gap-trap question
  for a1-pq vs a1-5q as legitimate scope-containment not duplication, held
  a1-5q out of build set to avoid duplicated casework; build set =
  a1-3qk-subfamily-theorem, a1-pq-subfamily-theorem,
  n1-periodicity-reconciliation) -> 3 proof-builders (parallel) -> 1
  proof-reviewer (independently re-derived/re-simulated everything from
  scratch with fresh scripts; found one minor non-load-bearing arithmetic
  typo in a1-3qk's write-up, doesn't affect the theorem). Verdicts: ALL 3
  CHANGES REQUESTED (partial) — no APPROVE this round, but real content:
  a1-3qk's m=3 case (a_1=3q^3) is now FULLY CLOSED and certified as a
  standalone theorem (5th distinct m/family theorem in the stack:
  m=1,2,3 all certified; general m>=4 remains open — growing threshold
  constants need fresh per-m derivation, no telescoping shortcut found);
  a1-pq-subfamily-theorem proved and certified a genuinely p-uniform
  symbolic reduction (Generalized K_0-Boundedness + gcd-difference witness
  lemmas, verified via independent p=5 brute-force cross-check, exact
  match) but honestly left Bad(p) (the finite exceptional set) unpinned
  for any specific p>=5 — same "requires hand-discovery" phenomenon that
  q=5 needed even at p=3; n1-periodicity-reconciliation's H2 diagnostic
  correction verified logically sound (though the reviewer's own
  large-N numeric re-verification was partial-confidence, disclosed
  explicitly — did not have time to independently recompute S_0 for
  11305). 2 new lemmas certified (a1-3q-cubed-periodicity-theorem,
  generalized-k0-boundedness-and-gcd-difference-witness). Main FAH crux
  (H1) untouched this round (by design, per outline-reviewer's
  recommendation to avoid a 4th consecutive subfamily-only round without
  it) — now 19th consecutive plateau round (6-25). H2 diagnosis clarified
  (de-threatened, not resolved) but still fully open.

## Eval History (round 24 addition)

- Round 24: Status partial overall, but **4th APPROVE of the run**:
  `a1-3aq-subfamily-theorem` solved and certified for a_1=3^a*q, a in
  {1,...,5} (all primes q>=7, q!=5) — a genuinely different generalization
  axis from the stuck a_1=3q^m family (exponentiate the SMALL prime,
  K_0=3^a+s_0 stays q-independent). Required a corrected witness-window
  identity (m=3^{a-1}q+(i-1), not the naive transplant m=q+i-1, which would
  have falsely "resolved" the genuine a=2,q=11 exception). 3 math-explorers
  (a1-3qk-closure lens, H2-absence lens, diversity-scout lens) -> found:
  (1) round 23's "m>=2 structurally insufficient" diagnosis for a1-3qk was
  a BOOKKEEPING ERROR (wrong sieve modulus omega(qK_0) vs omega(K_0) at
  k=0) — fixed, giving only 4 (m=2) / 12 (m=3) failures up to q<20000, a
  genuine finite residual table like the solved m=1 case; (2) H2-absence:
  400k-term simulation found seeds 4807 and 11305 behave differently —
  4807's new-type arrival decelerates (H2-supportive), 11305 stays flat
  ~sqrt(N) (H2-threatening), flagged as possibly a window artifact; (3)
  diversity-scout found the a_1=3^a*q axis as structurally the "right" next
  subfamily (K_0 bounded as q->infinity, unlike 3q^m). -> 1 proof-outliner
  (revised a1-3qk-subfamily-theorem with the bookkeeping fix; new
  a1-3aq-subfamily-theorem; new new-prime-recruitment-rate-bound targeting
  H2 via direct rate-counting instead of S_0-containment) -> 1
  outline-reviewer (independently reproduced the bookkeeping fix and the
  a1-3aq numerics; verified genuine axis distinctness; APPROVE all 3 for
  build) -> 3 proof-builders (parallel) -> 1 proof-reviewer. Verdicts:
  a1-3qk-subfamily-theorem CHANGES REQUESTED (partial) — m=2 FULLY CLOSED
  and certified (lemmas/a1-3q-squared-periodicity-theorem.md, explicit
  theorem a_n=3(q^2+n-1), 9 residual exceptions all hand-resolved); m>=3
  remains open (K_0 becomes quadratic in q, needs re-derivation not
  transplant). a1-3aq-subfamily-theorem **APPROVE (solved for a=1..5)** —
  4th APPROVE, certified lemmas/a1-3aq-generalized-corollary-and-
  mechanisms.md. new-prime-recruitment-rate-bound RETHINK (unsolved) — but
  produced a valuable new certified result along the way, the "Unbounded
  Total Prime Support Theorem" (union of P(a_j) is infinite for every a_1,
  via smooth-number-counting vs. Bounded Gap Lemma contradiction,
  certified lemmas/unbounded-total-prime-support-theorem.md); confirmed
  this does NOT refute H2 (self-absorption only needs a finite-prefix
  containment, not global finiteness) — H2 remains open, untouched by this
  attempt. Run now stands on **4 fully certified solved sub-family
  theorems** (2|a_1; a_1=p^k; a_1=3q; a_1=3^a*q for a=1..5) plus a
  partially-closed 5th (a_1=3q^2, m=2 of the 3q^m family) plus the gap-free
  Master Conditional Theorem reducing the fully general case to H1 (FAH,
  now 9th consecutive dead fresh-framing sweep) + H2 (absorption-chain
  termination, actively open, new seed-asymmetry finding at 4807 vs 11305).

## Eval History (round 23 addition)

- Round 23: Status remains `partial` overall (3 certified subfamily
  theorems stand as the run's floor: 2|a_1 T=1,L=2; a_1=p^k T=1,L=p; a_1=3q
  T=1,L=3). Both round-23 builds got CHANGES REQUESTED (real progress, no
  APPROVE this round). 3 math-explorers (H1 fresh-corridor check, subfamily
  candidates, H2 termination) -> 1 proof-outliner -> 1 outline-reviewer
  (build set = a1-3qk-subfamily-theorem, direct-s0-self-absorption) -> 2
  proof-builders -> 1 proof-reviewer. `a1-3qk-subfamily-theorem` (new,
  generalizes certified a1-3q to a_1=3q^m any m>=1): Parts I-III (base
  case, a_n+1 illegality, Case (a), odd-n Parity Witness, n_0/K_0
  bookkeeping) proven m-general and certified
  (lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md); builder's Part IV
  claim that the sieve toolkit is "structurally insufficient" for m>=2 was
  REFUTED by the reviewer's extended computation (q<20000 vs builder's
  q<200): failures stop past q~1000-2000, a finite residual band exactly
  like the solved m=1 case, not a regime change. `direct-s0-self-
  absorption` (new H2 framing, direct non-inductive N(S_0)=0 target):
  reduces to an existing certified lemma (Monotone Chain Reformulation at
  M=N_0, no new leverage) but produced a certified new insufficiency lemma
  (lemmas/bounded-witness-insufficiency-for-containment.md) AND a
  genuinely valuable citation correction — round 17's "N(S_0)=0 on 9/9
  seeds" claim (relied on by past rounds as H2 optimism) was traced and
  confirmed to actually be about S_0=Q, not the Finite Core Theorem's real
  S_0; fresh 20,500-term simulation on both hard seeds (4807, 11305) shows
  brand-new extended types still arriving at the 95th percentile —
  H2's existence hypothesis is now known to be actively open, not
  trivially-supported. H1 explorer confirmed the generic-mechanism well is
  exhausted (8th consecutive dead fresh-framing sweep) — do not dispatch
  another generic H1 attempt without a concrete new corridor.

## Rules (additions from round 28)

- **`a1-11q-subfamily-theorem` is now fully certified solved** (T=1,L=11
  from n=1, all primes q>11, q not in Bad(11)={13,17,19,31,37,43}), the
  run's 8th APPROVE, closed in ONE round exactly like a1-5q/a1-7q —
  further confirms the p-uniform machinery genuinely generalizes per-p
  with no new obstruction types (now verified at p=3,5,7,11) (round 28).
  a1=9q needs NO separate work: already subsumed by certified
  `a1-3aq-subfamily-theorem` at a=2 (round 28).
- **New Universal Look-Back Closed Form + Uniqueness-of-r=1 Theorem
  certified**: gcd(N,a_n)=gcd(j,(k+1+c(p,j,r)) mod j) with
  c(p,j,r)=s_0(j,r)*p^{-1} mod j q-independent; r=1 is PROVABLY the
  unique residue class (mod p) with c=0, via a single universal witness
  band j=p-1 that works for every r!=1 and every prime p simultaneously.
  This is a genuine structural explanation (not just empirical pattern)
  of why only r=1 gets an unconditional k=0 shortcut — but it is a
  bookkeeping simplification only: it does NOT close any new (j,r,k)
  cell, does not resolve r=1's k>=1 residual, and does not touch r!=1's
  general closure (round 28).
- **H2's "N(S_0)=0 direct attack" is now confirmed STALE, not a live
  lever** — round 19's Proposition 3 (Non-Constructivity of M_B) already
  proves NO finite-data/numeric method can ever resolve N(S_0)=0 or any
  bound on it; this forecloses the round-27 Next-priority (c) framing.
  Large-scale resimulation (700k-750k terms, seeds 4807/11305/105945)
  found nothing beyond consistency with this impossibility; do NOT
  dispatch another H2 numeric-attack round without a genuinely new
  non-finite-data structural argument (invariant/monotonicity/
  compactness) (round 28).
- **22nd consecutive plateau round on H1/FAH (round 28)** — untouched
  again this round per explorer/outliner agreement (3rd consecutive
  round with no dedicated H1 search after 2 dead searches in rounds
  26-27); the subfamily-theorem track remains the only source of new
  APPROVEs. Consider a1-13q as the next routine near-certain 9th-APPROVE
  candidate (Bad(13)={17,19,23,47}, 132-cell table, already scouted by
  round-28's subfamily-extension explorer but not yet outlined/built).

## Rules (additions from round 27)

- **`a1-7q-subfamily-theorem` is now fully certified solved** (T=1,L=7
  from n=1, all primes q outside Bad(7)={11,13}), the run's 7th APPROVE,
  closed in ONE round exactly like a1-5q — confirms the p-uniform
  machinery genuinely generalizes per-p with no new obstruction types at
  p=3,5,7 (round 27).
- **New Universal Look-Back Witness Identity certified**:
  gcd(N,a_i)=gcd(p(n-i)+j, q+i-1) for a_1=pq family, general for ALL r
  (not just r=1) — generalizes the prior gcd-difference Witness Lemma.
  Its r=1 corollary (q≡1 mod p) proves k=0 is UNCONDITIONALLY safe via
  the exact formula gcd(k+1,j), no per-p computation needed — but does
  NOT extend to look-back distance d=k or d=k+1 (checked and refuted:
  d=k+1 is provably never a witness; d=k reduces to a genuinely
  parameter-dependent gcd, doesn't telescope) — do not assume this
  identity closes k>=1 for free (round 27).
- **`covering-system-construction` now has TWO standing hard seeds fully
  resolved** (a_1=4807 d=13, round 26; a_1=11305 d=103, round 27) via the
  certified Finite-Window Literalization Lemma — both single-seed
  closures, not a general theorem. IMPORTANT bookkeeping trap: the two
  seeds have OPPOSITE canonical witness orderings (4807: n_A<n_B; 11305:
  n_B<n_A) — any future reapplication must explicitly verify/relabel
  which witness is "A" vs "B" rather than copying by type-letter analogy
  (round 27).
- **21st consecutive plateau round on H1/FAH (round 27)** — 2nd
  consecutive dedicated fresh-corridor search (rounds 26-27) found
  nothing new, including a crux-corpus check of aimo-0907 (orbit-merging)
  which dies for the same reason as the already-dead
  orbit-merging-additive-offset-dichotomy mechanism. Corridor-hunting at
  the current technique level is likely exhausted — do not dispatch a
  3rd consecutive generic fresh-corridor sweep without a concrete new
  lever in hand; consider whether H2's untried "N(S_0)=0 direct attack"
  or continuing the subfamily-theorem track exclusively is higher value.

## Rules (additions from round 26)

- **`a1-5q-subfamily-theorem` is now fully certified solved** (T=1,L=5
  from n=1, all primes q outside Bad(5)={7,13,19}), the run's 6th
  APPROVE, closed in ONE round by direct instantiation of the certified
  p-uniform machinery at p=5 — confirms the a1-pq machinery genuinely
  generalizes cleanly per-p; `a1-7q-subfamily-theorem` (targeting
  Bad(7)={11,13}, 30-cell table) is registered and outline-approved but
  UNBUILT — a low-risk near-term 7th-APPROVE target for a future round.
- **`a1-3qk-subfamily-theorem` m=4 (a_1=3q^4) is FALSE as originally
  stated for at least q=17** — direct greedy simulation confirms the
  sequence provably does NOT resettle to constant gap 3 (alternates
  3/6/2/4 through n=60). Any future m=4 attempt must scope the theorem to
  exclude q=17 (and search for other exceptions) as a finite exceptional
  set, analogous to Bad(p) — do NOT restate m=4 as "true for ALL q."
  Additionally the naive threshold generalization gives a
  computationally infeasible ~2x10^11 verification bound (vs m=3's
  tractable 737,282) — a fresh, cheaper closure strategy is needed before
  this is worth building, not just a bigger table (round 26).
- **Minimal-Window Necessity Conjecture (a1-pq family) is a real open
  sub-target, not yet proven**: genuine exceptions to a1-pq periodicity
  empirically occur only at s_0(j,r)=1 (diagonal, j=r) cells, and this is
  now backed by 2 certified lemmas (Diagonal Characterization:
  s_0(j,r)=1 iff j=r; First-Risk Theorem: n_0(j) increasing in s_0(j,r),
  verified on 282k tuples) — but a concrete isolated counterexample shows
  non-diagonal bands CAN have empty windows in isolation; only ordering
  (diagonal tested first) explains why this never becomes the actual
  first deviation, and "tested first" != "later bands safe" is still an
  open gap (round 26).
- **`covering-system-construction`'s new Finite-Window Literalization
  Lemma closes seed a_1=4807's d=13 residual class completely (literal,
  not cofinite, Joint FAH)** but is explicitly single-seed scoped, not a
  general theorem — immediately re-applicable to a_1=11305's untried
  recorded candidate witness x_2=103 as a cheap next-round follow-up
  (round 26).
- **20th consecutive plateau round on H1/FAH (round 26)** — fresh-corridor
  explorer found nothing concrete again; the "ambient-statistic
  exemption for occupancy-conditioned statistics" loophole (named since
  round 19-20) was traced this round and found NOT to be real progress
  (occupancy-conditioning just relabels the same adaptively-defined index
  set with no closed-form density control) — do not re-propose this
  specific loophole again without a genuinely new idea for supplying the
  missing local-density control.

## Rules (additions from round 25)

- **`a1-3qk-subfamily-theorem` now has m=1,2,3 ALL fully certified as
  standalone theorems** (a_1=3q^m for m=1,2,3, T=1,L=3 from n=1, all
  primes q>=7,q!=5 outside small finite exception lists). General m>=4
  remains open — do NOT assume a telescoping/inductive shortcut from m=3
  to m=4 exists; each m needs its own threshold-constant re-derivation
  (confirmed no telescoping found, round 25). Extending to m=4 is a
  routine-but-not-free finite-table close, same difficulty tier as m=3
  was.
- **The Legendre Sieve Gap Bound + Primorial Floor Bound toolkit is
  prime-agnostic** — it generalizes cleanly from base prime 3 to general
  odd prime p (a1-pq-subfamily-theorem, round 25, 2 lemmas certified:
  Generalized K_0-Boundedness + gcd-difference witness). The REMAINING
  gap for any specific p>=5 is pinning down the literal finite
  exceptional set Bad(p) — this structurally requires a per-p
  hand/computational discovery step (analogous to how q=5 was found only
  by direct check for p=3, never predicted by formula), not automatic
  from the uniform machinery. Do not expect a closed-form Bad(p) formula.
- **Round 24's H2 "seed a_1=11305 diverges ~sqrt(N)" finding is RETRACTED
  as a measurement artifact** (global power-law fit contaminated by early
  transient growth) — a corrected local-exponent analysis on a much
  larger simulation (up to n=750k-1M terms) shows BOTH canonical hard
  seeds (4807, 11305) decelerating, just at different rates because
  11305's Finite-Core-Theorem-enlarged S_0 core is bigger (|S_0|=12 vs 9)
  and needs more runway (round 25). This DE-THREATENS but does NOT PROVE
  H2 — do not cite this as evidence H2 is true, only that the prior
  round's evidence against it was flawed.
- **19th consecutive plateau round on H1/FAH (round 25)** — deliberately
  untouched this round per outline-reviewer's explicit recommendation to
  avoid a 4th consecutive subfamily-only round with zero H1 attention;
  next round should weigh dispatching a genuinely fresh H1 lens (only if
  a concrete new corridor is found, not another generic sweep) against
  continuing the subfamily-theorem track (a1-5q, a1-pq's Bad(p) for
  p=5/7, a1-3qk m=4 are all live, low-risk, near-term APPROVE-class
  targets).

## Rules (additions from round 24)

- **ALWAYS double-check sieve-modulus bookkeeping (r=omega(N) for which N
  exactly) before accepting a builder's "structural insufficiency" claim**
  — round 23's a1-3qk "m>=2 insufficient" verdict was itself wrong: it used
  omega(q*K_0) instead of omega(K_0) at k=0 (q-coprimality already free
  there). Always have the reviewer/next explorer re-derive the exact
  modulus from the lemma's own hypotheses before trusting a "regime
  change" diagnosis (round 24, corrects round 23's Rule).
- **`a1-3aq-subfamily-theorem` (a_1=3^a*q) is certified for a in {1,...,5}
  only** — the architecture is general but the explicit residual-table
  computation stops at a=5. A future round COULD extend to larger a (same
  method, larger table) for a stronger APPROVE, but this is optional/low
  priority given other open fronts (round 24).
- **`a1-3qk-subfamily-theorem` m=2 is now fully closed and certified**
  (a_n=3(q^2+n-1)); m=3 remains open because K_0 becomes quadratic in q
  requiring a fresh threshold re-derivation, not a mere transplant of m=2's
  argument (round 24).
- **New-prime-recruitment-rate framing for H2 is now closed as a dead
  end** — the "Unbounded Total Prime Support Theorem" (certified) proves
  the RAW recruitment target is unconditionally false for every seed, but
  this does NOT refute H2 itself (self-absorption only needs finite-prefix
  containment in some core S*, compatible with globally unbounded prime
  support). Do not re-attempt a literal global-rate H2 framing; any future
  H2 attempt must work with an S*-relative/restricted rate, not the raw
  count (round 24).
- **H2 seed-asymmetry (4807 decelerating vs 11305 flat ~sqrt(N) over 400k
  terms) is an open flag, not yet resolved** — could be a finite-window
  artifact or evidence of real seed-dependent H2 behavior. A future H2
  round should consider a much larger (millions of terms) simulation on
  11305 specifically before designing a new general mechanism (round 24).

## Rules (additions from round 23)

- **NEVER trust a builder's numeric "insufficiency" claim without
  independently extending the computation range** — round 23's
  a1-3qk-subfamily-theorem builder tested only q<200 and wrongly concluded
  a regime change; the reviewer's q<20000 sweep found a plain finite
  residual band instead, identical in shape to the already-solved m=1
  case. Always re-run numeric claims at 10-100x the builder's tested range
  before accepting a "no further progress possible" conclusion (round 23).
- **`a1-3qk-subfamily-theorem` (a_1=3q^m, m>=1) is very likely closeable
  next round** — Parts I-III already proven+certified m-generally; the
  ONLY remaining work is a residual-band closure for the Legendre Sieve
  Gap Bound at K_0(q,m)=3q^{m-1}+s_0, mirroring m=1's 3-round closure
  pattern (finite table, not new machinery). Do NOT let the next builder
  chase a Chebyshev/Jacobsthal-strength general bound — check crux
  corpus/KB for a Robin/Nicolas-Robin-style highly-composite-number bound
  on ω(qK_0(q,m)) first, or just directly hand-resolve the larger-but-
  finite residual table the same way m=1 did (round 23).
- **Round-17's "N(S_0)=0 on 9/9 seeds" citation is WRONG/misleading and
  now corrected** — it was actually about S_0=Q (a much smaller/different
  object), not the Finite Core Theorem's real enlarged S_0. At the correct
  S_0, both known hard seeds (4807, 11305) show new extended prime-factor
  types still arriving at the 95th percentile of a 20,500-term window.
  Treat H2's existence hypothesis as ACTIVELY OPEN going forward, not
  near-trivial — any future H2 approach needs a genuine mechanism for
  "absence of primes outside a fixed finite core," not just "presence of a
  shared prime" (the certified Bounded Witness Lemma only gives the
  latter, per new lemmas/bounded-witness-insufficiency-for-containment.md,
  round 23).
- **8th consecutive dead fresh-framing sweep on H1/FAH (round 23)** — the
  generic-mechanism well for H1 is now essentially certain to be
  exhausted. Do not dispatch another undifferentiated fresh-framing H1
  explorer without a concrete new corridor candidate in hand first.

## State (round 23 addition)

### Done (round 23)
- Round 23: 3 math-explorers (H1 fresh-corridor, subfamily candidates, H2
  termination) -> 1 proof-outliner (new a1-3qk-subfamily-theorem, new
  direct-s0-self-absorption, new a1-5q-subfamily-theorem registered but
  held out, covering-system-construction advance held out) -> 1
  outline-reviewer (build set = a1-3qk-subfamily-theorem,
  direct-s0-self-absorption) -> 2 proof-builders (parallel) -> 1
  proof-reviewer. Both CHANGES REQUESTED/partial — no APPROVE this round,
  but real progress on both: a1-3qk Parts I-III certified (m-general),
  Part IV's "insufficiency" claim refuted (finite residual band found
  instead, near-closeable); direct-s0-self-absorption produced a certified
  insufficiency lemma and corrected a load-bearing round-17 citation error
  that changes H2's status from "trivially optimistic" to "actively open."
  2 new lemmas certified.

### Done (round 24)
- Round 24: 3 math-explorers (a1-3qk-closure bookkeeping-fix lens,
  H2-absence/rate lens, diversity-scout lens) -> 1 proof-outliner (revised
  a1-3qk-subfamily-theorem, new a1-3aq-subfamily-theorem, new
  new-prime-recruitment-rate-bound) -> 1 outline-reviewer (build set = all
  3) -> 3 proof-builders (parallel) -> 1 proof-reviewer. **4th APPROVE**:
  a1-3aq-subfamily-theorem solved for a=1..5. a1-3qk-subfamily-theorem
  CHANGES REQUESTED (m=2 now fully closed and certified; m=3+ open).
  new-prime-recruitment-rate-bound RETHINK (own target false, but produced
  a certified new lemma, Unbounded Total Prime Support Theorem, that does
  NOT refute H2). 4 lemmas certified this round.

### Done (round 25)
- Round 25: 3 math-explorers (m=3-closure lens, H2-asymmetry lens,
  diversity-scout lens) -> 1 proof-outliner (advanced a1-3qk toward m=3
  closure, advanced a1-5q, new a1-pq-subfamily-theorem, advanced
  n1-periodicity-reconciliation) -> 1 outline-reviewer (seeded missing
  a1-pq file, held a1-5q out as scope-contained by a1-pq, build set = 3)
  -> 3 proof-builders (parallel) -> 1 proof-reviewer. All 3 CHANGES
  REQUESTED/partial — no APPROVE, but a1-3qk's m=3 case (a_1=3q^3) fully
  closed and certified (5th m/family theorem), a1-pq's uniform-in-p
  machinery certified (Bad(p) for p>=5 still needs per-p pinning), H2
  seed-asymmetry diagnosis corrected (de-threatened, not resolved). 2 new
  lemmas certified. H1/FAH untouched, 19th consecutive plateau round.

### Done (round 26)
- Round 26: 3 math-explorers (Bad(p) pinning lens, a1-3qk m=4 lens, H1
  fresh-corridor lens) -> 1 proof-outliner (revised a1-5q-subfamily-
  theorem, new a1-7q-subfamily-theorem held out, advanced a1-pq-subfamily-
  theorem and covering-system-construction) -> 1 outline-reviewer (build
  set = a1-5q-subfamily-theorem, a1-pq-subfamily-theorem, covering-
  system-construction) -> 3 proof-builders (parallel) -> 1 proof-reviewer.
  **6th APPROVE**: a1-5q-subfamily-theorem solved (Bad(5)={7,13,19}).
  a1-pq-subfamily-theorem and covering-system-construction both CHANGES
  REQUESTED/partial with real new certified lemmas each. 3 lemmas
  certified this round. H1/FAH untouched, 20th consecutive plateau round.

### Done (round 27)
- Round 27: 3 math-explorers (a1-7q build-readiness, covering-system
  11305 follow-up, H1 fresh-corridor) -> 1 proof-outliner (advance a1-7q
  to full build; light advance covering-system-construction for 11305;
  new r=1 sub-target for a1-pq-subfamily-theorem) -> 1 outline-reviewer
  (build set = all 3) -> 3 proof-builders (parallel) -> 1 proof-reviewer.
  **7th APPROVE**: a1-7q-subfamily-theorem solved (Bad(7)={11,13}).
  a1-pq-subfamily-theorem CHANGES REQUESTED (new certified Universal
  Look-Back Witness Identity; r=1's k=0 layer unconditionally closed;
  k>=1 residual open). covering-system-construction CHANGES REQUESTED
  (a_1=11305's d=103 closed, dual-seed now). 1 lemma certified. H1/FAH
  untouched by new mechanisms, 21st consecutive plateau round.

### Done (round 28)
- Round 28: 3 math-explorers (a1-pq r-generalization, subfamily-extension
  candidates, H2 direct-attack) -> 1 proof-outliner (new a1-11q-subfamily-
  theorem; revised a1-pq-subfamily-theorem with r-generalization result;
  parked H2/H1) -> 1 outline-reviewer (build set = a1-11q-subfamily-
  theorem, a1-pq-subfamily-theorem) -> 2 proof-builders (parallel) -> 1
  proof-reviewer. **8th APPROVE**: a1-11q-subfamily-theorem solved
  (Bad(11)={13,17,19,31,37,43}). a1-pq-subfamily-theorem CHANGES
  REQUESTED (new certified Universal Look-Back Closed Form + Uniqueness-
  of-r=1 Theorem, proved for all r via a single universal witness band —
  bookkeeping narrowing, no new cell closed). 1 lemma certified. H1/FAH
  untouched, 22nd consecutive plateau round. H2's "N(S_0)=0 direct
  attack" confirmed stale (round 19 Prop 3 already forecloses it).

### Next
- Round 29 priorities: (a) live near-term APPROVE-class target:
  `a1-13q-subfamily-theorem` (Bad(13)={17,19,23,47}, 132-cell table,
  already scouted numerically by round-28's subfamily-extension
  explorer but not yet outlined/built) — likely 9th APPROVE in one round,
  same pattern as a1-5q/a1-7q/a1-11q. (b) `a1-pq-subfamily-theorem`: the
  r=1 k>=1 residual and general r!=1 closure remain open; only pursue if
  a concrete new angle is found, not another bookkeeping-only pass. (c)
  H1/FAH: 22 consecutive plateau rounds, 3 consecutive rounds with no
  dedicated search after 2 dead searches (26-27) — do NOT dispatch
  another generic fresh-corridor sweep without a concrete new lever;
  consider whether consolidating the (soon 8-9)-subfamily-theorem floor
  deliverable is the practical ceiling for this run. (d) H2: "N(S_0)=0
  direct attack" now confirmed foreclosed by round-19 Prop 3 for ALL
  finite-data methods — do not revisit without a genuinely new
  non-finite-data structural argument. (e) `covering-system-construction`
  remains dual-seed capped, low priority. Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per
  CLAUDE.md.
- Round 28 priorities (superseded, kept for reference): (a) `a1-pq-subfamily-theorem`: extend the new
  Universal Look-Back Witness Identity's r=1 corollary approach to other
  small residues r (r=2, r=p-1, etc.) looking for more unconditional
  k=0 closures before falling back to per-p computation — concrete,
  well-scoped continuation of this round's real progress. (b) Consider
  a1-9q or a1-11q as further routine subfamily extensions (same p-uniform
  machinery, likely near-certain APPROVEs) if diversity/build-slot
  capacity allows, OR pivot capacity toward a1-3qk m=4 (needs a fresh,
  cheaper closure strategy per round-26 rule, not the naive ~2x10^11
  threshold). (c) H1/FAH: 21 consecutive plateau rounds, 2 consecutive
  dedicated-search rounds (26-27) found nothing — do NOT dispatch a 3rd
  generic fresh-corridor sweep without a concrete new lever; consider
  H2's untried direct "N(S_0)=0" attack instead, or weigh consolidating
  the 7-subfamily-theorem floor deliverable as the practical ceiling for
  this run. (d) `covering-system-construction` is now dual-seed capped —
  do not force a 3rd seed application without a specific reason (housekeeping
  only, low priority). Continue math-explorer -> proof-outliner ->
  outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 27 priorities (superseded, kept for reference): (a) live near-term APPROVE-class target:
  `a1-7q-subfamily-theorem` (Bad(7)={11,13}, 30-cell table, outline
  already approved, unbuilt) — likely 7th APPROVE in one round, same
  pattern as a1-5q. (b) `covering-system-construction`: apply the new
  Finite-Window Literalization Lemma to seed a_1=11305's untried
  candidate witness x_2=103 — cheap, concrete follow-up. (c)
  `a1-pq-subfamily-theorem`: the Minimal-Window Necessity Conjecture gap
  (why non-diagonal risky bands are always safe when tested after the
  diagonal) is a genuine open sub-target if a math-explorer finds a
  concrete angle. (d) Do NOT attempt a1-3qk m=4 as originally stated —
  it's false for q=17; only revisit with a rescoped finite-exception
  version and a cheaper closure strategy than the naive ~2x10^11
  threshold. (e) H1/FAH: 20 consecutive plateau rounds — do not dispatch
  another generic fresh-framing sweep without a concrete new corridor;
  the ambient-statistic/occupancy-conditioning loophole is now also
  confirmed not real progress. Continue math-explorer -> proof-outliner
  -> outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 26 priorities (superseded, kept for reference): (a) live near-term APPROVE-class targets: pin down
  Bad(p) for a1-pq at a specific small p (e.g. p=5 or p=7, reusing the
  already-certified uniform machinery — cheap, concrete); or close
  a1-3qk's m=4 case (same difficulty tier as m=3, no telescoping
  shortcut, needs fresh threshold derivation); either is a plausible 5th/
  6th APPROVE. (b) H1/FAH: 19 consecutive plateau rounds — do not dispatch
  another generic fresh-framing sweep without a concrete new corridor in
  hand; consider whether it's time to weigh a genuinely fresh H1 lens
  (only if concrete) against continuing the subfamily track exclusively.
  (c) H2: diagnosis now clarified (round 24's divergence claim was an
  artifact) but still fully open — no new concrete mechanism proposed
  yet; only pursue if a math-explorer finds something genuinely novel, not
  another S_0-related framing already dead. Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per
  CLAUDE.md.
- Round 22: for round 23, superseded, see round 25 entry above.
- Round 25 priorities (superseded, kept for reference): (a) LOW PRIORITY/optional: extend
  a1-3qk-subfamily-theorem to m=3 (K_0 quadratic in q, needs fresh
  threshold re-derivation) for a possible 5th APPROVE-class result, or
  extend a1-3aq to a>5 (same method, bigger table) — either is a routine
  finite-table close, not urgent. (b) H2 (absorption-chain termination)
  remains the real bottleneck alongside H1/FAH: consider a much larger
  (millions-of-terms) simulation on seed 11305 to resolve the seed-
  asymmetry flag before designing a new general mechanism; do NOT re-try a
  raw/global recruitment-rate framing (now confirmed dead). (c) H1/FAH:
  9th consecutive dead fresh-framing sweep — do not dispatch another
  generic sweep without a concrete new corridor in hand. Consider whether
  it's time to consolidate: with 4 certified subfamilies + a gap-free
  Master Conditional Theorem, evaluate whether writing up the strongest
  possible partial/floor deliverable (clearly scoped, per current.md) is
  higher value than continuing to hunt for full generality, OR keep
  pushing subfamilies (each is a concrete, low-risk APPROVE opportunity)
  while H1/H2 remain stuck. Continue math-explorer -> proof-outliner ->
  outline-reviewer -> builders -> reviewer flow per CLAUDE.md.
- Round 23 (superseded but kept for reference): TWO concrete, well-scoped continuation targets
  (both re-dispatch the SAME slug's builder per CLAUDE.md CHANGES REQUESTED
  routing, not new approaches): (a) `a1-3qk-subfamily-theorem` — close the
  residual-band table for K_0(q,m)=3q^{m-1}+s_0 mirroring m=1's successful
  closure pattern (check crux/KB for a Robin/Nicolas-Robin bound first;
  else hand-resolve the finite table directly); this is very likely a 4th
  APPROVE within 1-2 more rounds. (b) `direct-s0-self-absorption`/H2 — the
  "direct S_0" framing is now a confirmed dead end (no new leverage over
  existing lemmas); a genuinely new H2 mechanism is needed (absence-of-
  outside-primes argument, not presence-of-shared-prime), or a much larger
  numeric study (200k+ terms) to see if the new-type arrival rate at the
  now-corrected true S_0 actually tapers off. Lower priority than (a) given
  (a)'s near-closeable state. Do NOT dispatch another generic H1/FAH
  fresh-framing sweep (8th dead in a row, well essentially exhausted) or
  re-attempt a1-5q-subfamily-theorem before (a) is finished (registered but
  intentionally held out this round). Continue math-explorer ->
  proof-outliner -> outline-reviewer -> builders -> reviewer flow per
  CLAUDE.md.

## Eval History (round 29 addition)

- Round 29: Status partial overall, but **9th AND 10th APPROVEs of the
  run** (a double-APPROVE round): `a1-13q-subfamily-theorem` and
  `a1-17q-subfamily-theorem` both solved and certified — literal T=1,L=13
  and T=1,L=17 periodicity for the FULL a_1=13q and a_1=17q subfamilies
  (Bad(13)={17,19,23,47}; Bad(17)={19,23,29,31,37,43,61,67}),
  instantiating the certified p-uniform machinery at p=13,17, exactly
  mirroring the a1-5q/7q/11q closure pattern (now verified at 5 distinct
  primes p=3,5,7,11,13,17 with zero new obstruction types across all).
  a1-13q required one bookkeeping subtlety: q=19 produces a moot
  duplicate no-witness cell (12,6) alongside the genuine deviation cell
  (6,6) at n=3 — correctly not double-counted. 3 math-explorers (a1-13q
  build-readiness lens, H1 fresh-corridor lens, a1-pq-residual/diversity-
  scout lens) -> found: (1) a1-13q fully build-ready, Bad(13) confirmed
  via full table + resimulation; (2) ONE genuinely new H1 angle
  distinct from the 30+ dead graveyard — "bipartite-network invariant"
  attack on H1's open(k)->∅ target, adapted from crux aimo-1000 (ferry
  islands), reviving a round-3 idea never retried in 25 rounds; (3) no
  new bookkeeping-free angle on a1-pq's r=1 k>=1/r!=1 residuals, but
  found a1=17q as a viable secondary subfamily (Bad(17), 8 exceptions)
  and confirmed a1=6q/a1=15q are dead (3-prime-factor families
  qualitatively harder). -> 1 proof-outliner (new a1-13q-subfamily-
  theorem full outline; new bipartite-network-invariant-fah targeting
  H1 plateau-break; new secondary a1-17q-subfamily-theorem) -> 1
  outline-reviewer (independently verified Bad(13) over primes to
  20000 and Bad(17); CRITICALLY caught that the H1 approach's original
  disambiguation check was TRIVIALLY TRUE/vacuous — mirrors round-9
  Same-Type Free Facts Vacuity trap one level up — mandated a sharper
  "does the linking-prime pool stay bounded" question before build;
  build set = all 3) -> 3 proof-builders (parallel) -> 1 proof-reviewer
  (independently re-derived/re-simulated all 3 from scratch, tens of
  thousands of instances). Verdicts: a1-13q-subfamily-theorem **APPROVE
  (solved)** — 9th APPROVE. a1-17q-subfamily-theorem **APPROVE (solved)**
  — 10th APPROVE. bipartite-network-invariant-fah RETHINK (unsolved,
  clean genuine negative) — the corrected disambiguation question has
  exactly 2 possible readings, both collapse into already-known dead/
  open territory (fixed-core reading = certified-but-insufficient
  Generalized Bounded Witness Lemma; growing-core reading = definitionally
  the same object as the open H2 termination question); the aimo-1000
  "toggle rule" mechanism confirmed to have no arithmetic analog here.
  New certified lemma: bipartite-network-reduction-collapse (forecloses
  the whole graph/network-invariant transplant family for H1/FAH). Run
  now stands on **10 fully certified solved sub-family theorems** (2|a_1;
  a_1=p^k; a_1=3q; a_1=3q^2; a_1=3q^3; a1-3aq a=1-5; a1-5q; a1-7q;
  a1-11q; a1-13q; a1-17q — note this list is 11 items but a1-3q^2/3q^3
  count under the a1-3qk umbrella, so 10 distinct APPROVE events), plus
  the gap-free Master Conditional Theorem reducing full generality to H1
  (FAH, 23rd consecutive plateau round, 6-29, but with one new dead
  mechanism cleanly retired and certified as a reusable foreclosure
  lemma) + H2 (absorption-chain termination).

## Rules (additions from round 29)

- **`a1-13q-subfamily-theorem` and `a1-17q-subfamily-theorem` both now
  fully certified solved** (T=1,L=13 from Bad(13)={17,19,23,47}; T=1,L=17
  from Bad(17)={19,23,29,31,37,43,61,67}), the run's 9th and 10th
  APPROVEs, both closed in ONE round in parallel — the p-uniform
  subfamily machinery is now confirmed robust across 6 distinct primes
  (p=3,5,7,11,13,17) with zero new obstruction types; treat any future
  a1-pq-style subfamily (for a specific small prime p) as a routine,
  near-certain APPROVE candidate given explorer-confirmed build-
  readiness (round 29).
- **a1-13q has a moot-duplicate-cell pattern**: for q=19, TWO no-witness
  k=0 cells arise, (6,6) [genuine deviation at n=3] and (12,6) [vacuous,
  since H(3) never holds for q=19 so (12,6)'s premise is never
  satisfied] — do not double-count moot duplicate cells as extra genuine
  exceptions in future subfamily builds; check for this pattern whenever
  a below-threshold no-witness cell appears at an index reachable only
  after an earlier genuine deviation already occurred (round 29).
- **NEW dead H1/FAH mechanism, certified as reusable foreclosure lemma**:
  `bipartite-network-reduction-collapse` — any graph/network-invariant
  transplant attempt (modeling primes/linking as nodes/edges with a
  repair-on-failure rule, e.g. adapted from crux aimo-1000 ferry
  islands) collapses into exactly 2 readings of "does the linking
  resource pool stay bounded across repairs," and BOTH readings are
  already dead/open: fixed-core = certified-but-insufficient Generalized
  Bounded Witness Lemma (finite pigeonhole only gives "some class
  infinite," never "cofinite"); growing-core = definitionally identical
  to the open H2 termination question. The crux aimo-1000 mechanism
  itself (deterministic toggle rule) has NO arithmetic analog in this
  problem — the greedy-gcd recursion only supplies an EXISTENTIAL
  (never simultaneous/deterministic) shared-prime guarantee. Do NOT
  re-attempt any graph/network-invariant/repair-rule H1 framing without
  a genuinely new resource-boundedness argument that isn't just Bounded
  Witness or H2 in disguise (round 29).
- **Trivial/vacuous disambiguation-check trap recurs at one level up**:
  when a new approach's "cheap first check" premise is guaranteed true
  by an ALREADY-CERTIFIED free-facts-style lemma (e.g.
  lemmas/free-facts-gcd.md here), the check gives zero leverage even
  though it "passes" — this is the round-9 Same-Type Free Facts Vacuity
  trap recurring one abstraction level higher (first seen at the raw
  gcd level, now at the "does a repair prime exist" level). Outline-
  reviewers should always ask "is this check's YES answer already
  guaranteed by a certified lemma?" before accepting it as a
  disambiguation gate (round 29).
- **23rd consecutive plateau round on H1/FAH (round 29)** — a genuinely
  new mechanism (bipartite-network-invariant) WAS tried this round (1st
  dedicated attempt since round 22's orbit-merging, after rounds 26-28
  had none), found dead, and cleanly certified as foreclosed — this is
  real progress (narrowing the remaining search space) even though H1
  itself is untouched. The subfamily-theorem track remains the sole
  source of new APPROVEs (now 10 total). Consider a1-19q or a1-23q as
  the next routine near-certain APPROVE candidates if continuing this
  track, or seriously weigh a write-up/consolidation round given
  diminishing marginal distinctiveness of each new small-p subfamily.

## State (round 29 addition)

### Done (round 29)
- Round 29: 3 math-explorers (a1-13q build-readiness, H1 fresh-corridor,
  a1-pq-residual/diversity-scout) -> 1 proof-outliner (new a1-13q-
  subfamily-theorem; new bipartite-network-invariant-fah; new secondary
  a1-17q-subfamily-theorem) -> 1 outline-reviewer (caught vacuous
  disambiguation-check trap, mandated sharper H1 question; build set =
  all 3) -> 3 proof-builders (parallel) -> 1 proof-reviewer. **9th AND
  10th APPROVE** (double-APPROVE round): a1-13q-subfamily-theorem and
  a1-17q-subfamily-theorem both solved. bipartite-network-invariant-fah
  RETHINK (unsolved, clean negative, 1 new certified foreclosure lemma:
  bipartite-network-reduction-collapse). Run now has 10 certified solved
  subfamily-theorem APPROVEs + gap-free Master Conditional Theorem;
  H1/FAH 23rd consecutive plateau round (6-29).

### Next
- Round 30 priorities: (a) the subfamily-theorem track remains the
  reliable APPROVE source (10 for 10 success rate at this pattern across
  p=3,5,7,11,13,17) — a1-19q or a1-23q are the next routine candidates if
  continuing, but marginal value of yet another small-p instance is
  declining; consider whether round 30 should pivot to a genuine
  write-up/consolidation deliverable (Master Conditional Theorem + all
  10 certified subfamilies, explicitly scoped floor) given 23 plateau
  rounds on H1 and diminishing distinctiveness. (b) H1/FAH: one new
  dedicated mechanism was tried and killed this round
  (bipartite-network-invariant, now foreclosed) — if another dedicated
  search is attempted, it must be genuinely distinct from ALL now
  30+ dead mechanisms including this new one; do not force a search
  without a concrete lead. (c) a1-pq-subfamily-theorem's r=1 k>=1 and
  r!=1 general residuals remain open with no new bookkeeping-free
  angle found across rounds 27-29 — only pursue with a genuinely new
  idea. (d) H2: still fully open, no new mechanism since round 24;
  N(S_0)=0 direct attack remains foreclosed (round 19 Prop 3). Continue
  math-explorer -> proof-outliner -> outline-reviewer -> builders ->
  reviewer flow per CLAUDE.md.

## Rules (additions from round 30)

- **`a1-19q-subfamily-theorem` now fully certified solved** (T=1,L=19 from
  Bad(19)={23,29,31,37,43,53,73}), the run's **11th APPROVE**, the 7th
  instantiation of the p-uniform machinery (p=3,5,7,11,13,17,19), zero
  new obstruction type. New reusable general result this round: a single
  **Diagonal Window-Parity/Mod-5 Lemma** proves ALL diagonal exceptions
  at once via K_0's prime factorization (2 and 5), replacing the old
  per-prime ad hoc factorization-check pattern — apply this lemma
  template directly at future p instantiations (e.g. a1-23q) instead of
  re-deriving diagonal exceptions case-by-case (round 30).
- **NEVER trust a large-window near-miss/inconclusive simulation claim
  without independent resimulation** — round 30's fah-counterexample-hunt
  builder claimed a genuine "6 simultaneous singleton" near-miss for
  a_1=7402395 in a 500k-term window and reported it as honest-inconclusive,
  but the proof-reviewer's independent bitmask resimulation found 2 of
  the 6 claimed "singleton" types actually recur within the same window
  (a real numerical bug, not just an under-searched budget issue). Always
  independently re-simulate headline numeric near-miss claims before
  accepting "inconclusive" framing (round 30).
- **H1/FAH: 25th consecutive plateau round (round 30)** — no new H1/H2
  mechanism found this round beyond the fah-counterexample-hunt stress
  tests (which themselves need rework per the rule above). Two invariant
  candidates newly refuted (introduction-order permutation, residue-
  vector-mod-core-prime) — do not re-propose either.
- **a1-pq-subfamily-theorem generalization confirmed to have no
  low-hanging uniform-for-all-p shortcut** (round 30 consolidation
  explorer): the two residual gaps (general r!=1 closure; r=1 k>=1
  residual) are p-independent algebraic sub-questions; each new small-p
  instance (e.g. a1-19q, future a1-23q) still costs a full round of
  effort, no shortcut unlocked by accumulating more instances.

## State (round 30 addition)

### Done (round 30)
- Round 30: 3 math-explorers (a1-19q build-readiness — computed and
  verified Bad(19)={23,29,31,37,43,53,73}; H1 fresh-corridor — 6
  candidate framings all found dead; consolidation/write-up audit —
  Master Conditional Theorem re-verified gap-free, current.md staleness
  identified) -> 1 proof-outliner (new a1-19q-subfamily-theorem; revised
  fah-counterexample-hunt with 2 new sub-targets per CLAUDE.md plateau-
  break rule; a1-pq-subfamily-theorem restricted to housekeeping-only,
  folded into a1-19q builder rather than its own slot) -> 1
  outline-reviewer (independently re-derived Bad(19) and the diagonal
  parity/mod-5 mechanism; verified fah-counterexample-hunt's 2 sub-targets
  genuinely distinct from 30+ dead mechanisms; build set = a1-19q-
  subfamily-theorem, fah-counterexample-hunt) -> 2 proof-builders
  (parallel) -> 1 proof-reviewer (independently re-derived/re-simulated
  both from scratch). Verdicts: a1-19q-subfamily-theorem **APPROVE
  (solved)** — the run's **11th APPROVE**, plus a new general Diagonal
  Window-Parity/Mod-5 Lemma unifying all future diagonal-exception proofs.
  fah-counterexample-hunt CHANGES REQUESTED (partial) — invariant
  refutations confirmed correct, but the headline H2-stress-test near-miss
  claim found to be a genuine numerical error (2 of 6 claimed singleton
  types actually recur), needs rework next round. current.md housekeeping
  (## Approaches tried / ## Current best) refreshed through round 30. Run
  now stands on **11 fully certified solved subfamily theorems** (2|a_1;
  a_1=p^k; a_1=3q; a_1=3q^2; a_1=3q^3; a1-3aq a=1-5; a1-5q; a1-7q; a1-11q;
  a1-13q; a1-17q; a1-19q) plus the gap-free Master Conditional Theorem
  reducing full generality to H1 (FAH, 25th consecutive plateau round,
  6-30) + H2 (absorption-chain termination, still open).

### Next
- Round 31 priorities: (a) rework fah-counterexample-hunt's H2 stress
  test — the a_1=7402395 near-miss claim needs a corrected, independently
  cross-validated resimulation (2 of the 6 claimed singleton types
  actually recur per round 30's proof-reviewer) before it can be trusted
  either way; this "gapped primorial" seed shape may still be a genuinely
  interesting H2 stress case once the bug is fixed. (b) subfamily track:
  a1-19q now 11/11 success rate (p=3,5,7,11,13,17,19); a1-23q is the next
  routine candidate using the new Diagonal Window-Parity/Mod-5 Lemma
  template, but marginal value continues to decline — weigh against a
  genuine H1/H2 plateau-break attempt (25 rounds now) or a real
  consolidation/write-up round. (c) H1/FAH: no new mechanism found this
  round across 6 checked framings; any future dedicated search must be
  genuinely distinct from all 30+ dead mechanisms plus this round's 2
  newly-refuted invariant candidates. (d) H2: still fully open; the
  corrected a_1=7402395-style stress test is the most concrete near-term
  lever. Continue math-explorer -> proof-outliner -> outline-reviewer ->
  builders -> reviewer flow per CLAUDE.md.
