## Goal

Prove IMO 2026 Problem 6 (`imo-2026-06` in problems.jsonl, domain number_theory,
difficulty_rating 9, difficulty_level hard, task proof_only):

> Let $a_1,a_2,a_3,\ldots$ be an infinite sequence of positive integers greater than $1$.
> Suppose that, for every positive integer $n$, the number $a_{n+1}$ is the smallest
> integer greater than $a_n$ such that $\gcd(a_{n+1},a_i)>1$ for $1\le i\le n$.
> Prove that there exist positive integers $T$ and $L$ such that $a_{n+T}=a_n+L$
> for every positive integer $n$ (eventual periodicity of the gap sequence).

Metric: `results/imo-2026-06/current.md` `## Status` field (unsolved | partial | solved)
+ the approach-ranker Elo distribution in `results/imo-2026-06/approaches/.ranking.json`.
Eval: read `current.md` Status and `.ranking.json` each round; a `solved` Status
confirmed by proof-reviewer APPROVE (no gaps, all cases settled, every lemma named)
is the win condition.
Baseline (round 1, pre-work): workspace just created, no approaches yet, Status
does not exist. 0 approaches registered, Elo distribution empty.
Target: Status = solved with a complete, gap-free, rigorous prose proof.
Constraint: never re-attempt with an approach already recorded dead-end for the
same reason; keep rival approaches diverse in framing (see Rules).

## Goal Updates

(none yet — task given directly in round-1 user message, matches imo-2026-06 verbatim)

## Eval History

- Round 1 (pre-work baseline): results/imo-2026-06/ workspace created
  (approaches/, lemmas/), no approaches yet, current.md not yet written.
  Status: N/A (fresh start).
- Round 1 (post-work): Status = partial. 3 approaches built (backbone-existence-crt
  Elo 1514, intersecting-family-covering-construction Elo 1517,
  bounded-gap-density-covering Elo 1469), all CHANGES REQUESTED (none RETHINK), all
  genuinely advanced the population. 4th opened approach
  (minimal-witness-index-descent) was cut pre-build by outline-reviewer as fatally
  flawed (Tight(n) degenerates to trivial singleton). 7 lemmas certified into
  results/imo-2026-06/lemmas/: lemma-P-permanent-hub, lemma-P-prime-pairwise-
  intersecting, lemma-Q-prime-power-base-case, lemma-1-uniform-gap-bound,
  domination-lemma, lemma-R-eternal-witness, lemma-S-prime-saturation-AP (reviewer-
  repaired). Reviewer found a cross-approach synergy: combining
  backbone-existence-crt's Domination Lemma with bounded-gap-density-covering's
  Lemma 1 unconditionally resolves the "growth control" half of the core
  backbone-finiteness gap (previously thought stuck). Remaining core gap (shared by
  all 3 approaches): "Case II" — no single prime saturates every term (witnessed by
  a_1=15, 247) — needs (a) concentration onto finitely many dominant primes
  (backbone finiteness), (b) explicit finite covering-set construction, (c)
  periodicity from n=1 not just eventually. Annotation: IMPROVED (strong first-round
  progress, dichotomy fully solves a nontrivial sub-case "Case I", real shared
  lemma cache built).
- Round 2 (post-work): Status = partial. Alt-framing explorer PROVED round 1's
  "backbone finiteness" formalization (backbone-existence-crt's H_n via
  pairwise-recruited primes) is FALSE/unbounded — numerically demonstrated even in
  the solved a_1=15 case (2948 incidental cross-pair primes). Outliner's first
  attempted fix (⋆: primes dividing infinitely many a_n finite) was ALSO proven
  false by outline-reviewer (any prime coprime to the eventual period L divides
  infinitely many terms by density 1/q — rigorous + numerically confirmed on
  a_1=15: 24->549 distinct primes across growing residue-class samples, no
  leveling). The correct reformulation, found by the new persistent-backbone-
  monovariant approach and validated by outline-reviewer: canonical minimal witness
  w(i,j)=min(rad(a_i) ∩ rad(a_j)); target is finiteness of W=⋃w(i,j). Field this
  round: backbone-existence-crt -> RETHINK (Step 3 only; verdict per-approach, not
  re-attempted this round). persistent-backbone-monovariant (new) and
  intersecting-family-covering-construction (revised) both CHANGES REQUESTED
  (partial, real progress, no RETHINK): persistent-backbone-monovariant certified
  Lemma C (Global Intersection Collapse, sound) and proved its own two natural
  W-finiteness conjectures FALSE with hand-verified counterexamples (NC1: a_1=221
  refutes reading backbone off Lemma C's collapse point; NC2: a_1=375 refutes
  bounding witnesses by rad(a_1)) — reformulated to weaker still-open "Finite
  Covering Backbone Conjecture." intersecting-family-covering-construction proved
  a genuinely new conditional bridge (Theorem 2.2 H-hitting characterization,
  Lemma 2.3 Σ-stabilization, Theorem 2.4: W/H finite => eventual periodicity),
  reviewer generalized it to require only "some common prime per pair" (weaker
  hypothesis than W itself). Elo: intersecting-family-covering-construction 1545,
  persistent-backbone-monovariant 1528, backbone-existence-crt 1498 (dropped),
  bounded-gap-density-covering 1428 (parked, unchanged). 6 new lemmas certified.
  Two gaps now precisely pinned down and shared by both live approaches: (1) does
  W (canonical-witness set) exist finite — core existence gap, still fully open;
  (2) periodicity-from-n=1 — intersecting-family-covering-construction tested a
  candidate mechanism, works for a_1=15 but FAILS numerically for a_1=35,65 under
  naive guessed H, confirming this is real remaining work not a formality.
  Annotation: BREAKTHROUGH (round 1's entire shared "core gap" was a chase after a
  false target; round 2 found and validated the correct reformulation via
  systematic refutation — this is a hazard-avoidance breakthrough, not a solve, but
  redirects all future effort onto a provably well-posed question instead of an
  unprovable one).

- Round 3 (post-work): Status = partial. **BREAKTHROUGH**: the entire problem
  now reduces to exactly ONE open gap (down from two at end of round 2).
  3 explorers scouted the FCBC gap (Finite Covering Backbone Conjecture: does
  a finite prime set H exist with H∩rad(a_i)∩rad(a_j)≠∅ for every pair i<j?)
  and the periodicity-from-n=1 gap in parallel; found (a) canonical witness
  set W is very likely UNBOUNDED (a_1=4199, 4087, no plateau to 20000 terms)
  — do not target W-finiteness, only the strictly weaker FCBC; (b) a concrete
  "forced primes" H candidate (primes that are the unique common radical
  factor of some pair) stabilizes by index <=12 and passed every stress test
  across 24 diverse a_1; (c) round 2's periodicity-from-n=1 negative finding
  (fails for a_1=35,65) was an ARTIFACT of testing against a wrongly-guessed
  H=rad(a_1); using the TRUE covering set, periodicity from n=1 held with
  zero exceptions across 7 examples. Outliner built a 4-approach field: 3
  rival techniques all attacking FCBC (persistent-backbone-monovariant via
  ω(a_n) boundedness; forced-primes-well-ordering via well-ordering/channel
  reduction; explicit-window-backbone-construction via explicit finite window
  H_K + pigeonhole) plus intersecting-family-covering-construction retargeted
  at periodicity-from-n=1. outline-reviewer: no RETHINK, all 4 CHANGES
  REQUESTED-worthy outlines advanced to build set. All 4 builders ran; proof-
  reviewer independently re-derived and re-simulated everything.
  **intersecting-family-covering-construction fully and rigorously closed
  periodicity-from-n=1**: Theorem 5.1 (Master Conditional Theorem) proves
  that IF FCBC holds (finite H exists) THEN a_{n+T}=a_n+L for EVERY n>=1
  exactly (not just eventually), with explicit T=|Good|<=L, L_per=L=lcm(H).
  Reviewer independently re-derived Lemma A/Corollary 3.1/Lemma B/Theorem 5.1
  and re-simulated all 8 examples including a_1=35,65 (the round-2 breakers)
  — zero discrepancies. The 3 FCBC-attacking approaches all made real
  progress but did NOT close FCBC: persistent-backbone-monovariant proved
  (Propositions ND1, ND2) two natural sufficiency mechanisms from the ω-bound
  do NOT work (a_1=221, 375 counterexamples); forced-primes-well-ordering
  reduced FCBC to <=3^ω(a_1) independent "channel" sub-questions, resolved
  all but doubly-infinite-class channels, found the natural closing mechanism
  false on a_1=247 and diagnosed a "cycling primes" obstruction; explicit-
  window-backbone-construction proved Lemma W1: the Key Lemma (some finite K
  makes H_K=∪_{i<=K}rad(a_i) a covering set) is LOGICALLY EQUIVALENT to FCBC
  — unifying all 3 approaches as literally the same proposition — and showed
  the natural finite-descent template can't transfer (monovariant candidates
  are non-decreasing in K, wrong direction). All 4 verdicts: CHANGES
  REQUESTED, none RETHINK. 8 new lemmas certified (21 total in lemmas/).
  Elo: intersecting-family-covering-construction 1595 (top), persistent-
  backbone-monovariant 1554, explicit-window-backbone-construction 1518,
  forced-primes-well-ordering 1510, backbone-existence-crt 1467 (parked),
  bounded-gap-density-covering 1384 (parked). Annotation: BREAKTHROUGH (two
  independent gaps collapsed to one; the one remaining gap, FCBC, is now
  precisely unified across 3 rival techniques as a single well-posed
  proposition, with several sufficiency mechanisms ruled out so future
  rounds don't repeat them).

## Rules

- SUPERSEDED (round 8): the round-7 "two live threads" framing (bundle-count
  bounding vs. escape-depth bounding, treated as possibly-independent) is
  now proven WRONG in a precise way — thread-unification explorer proved
  𝓥_S-finiteness ⟹ bounded escape-depth (one-directional), so depth-
  bounding is a COROLLARY of the master gap, not an independent target;
  simultaneously, permanent-bundle-count-alone (persistent-backbone-
  monovariant's literal round-7 target) is proven INSUFFICIENT for
  𝓥_S-finiteness (ignores transient members). NEVER treat escape-recursion-
  depth-boundedness as a separate/independent sub-problem going forward
  (round 8).
- THE SOLE REMAINING GAP as of round 8: `(UB_S)` — for every proper core
  `S⊊P_1`, `sup{|rad(a_i)∖S|:i∈I_S}<∞` (equivalently `sup_{n∉I_{P_1}}
  ω(a_n)<∞`, a restricted descendant of round 3's abandoned global bound).
  Proved unconditionally sufficient for the WHOLE problem (Theorem-UBS-
  sufficiency, results/imo-2026-06/lemmas/theorem-UBS-sufficiency.md,
  reviewer-independently-verified). Structurally different from every
  target attacked in rounds 6-8 (those all bound bundle COUNT; this needs
  bundle SIZE) — see Next (round 9) for what NOT to re-attempt (round 8).
- NEVER treat closing NIBC (persistent-backbone-monovariant's remaining
  gap after round 8's cross-approach synergy) as equivalent to solving the
  whole problem — proven (Transient-Bundles-Are-Invisible finding,
  builder+reviewer confirmed) to only bound the permanent/(SA)-satisfying
  share of Λ_S, not transient members; strictly weaker than (UB_S) (round
  8).
- NEVER re-attempt pure-intersection mechanisms (S^+, S^{++}, or any
  variant) to recover a prime that's absent from even one class member —
  forced-primes-well-ordering's Vacuity Proposition and Intersection-
  Fragility Proposition (results/imo-2026-06/lemmas/lemma-vacuity-and-
  intersection-fragility.md, reviewer-certified) prove this structurally
  impossible for the whole family of intersection-based mechanisms, not
  just the one S^{++} attempt tested (a_1=21528751, S={1061}, missing prime
  11) (round 8).

- ALWAYS confirm the user-given problem statement against problems.jsonl by exact
  text match before starting work — this run's statement matches `imo-2026-06`
  verbatim (round 1).
- ALWAYS keep rival approaches diverse in framing/route, not just technique
  (CLAUDE.md single-gap trap) — for this problem, plausible distinct framings
  include: (a) direct graph/interval-covering argument on prime supports building
  eventual periodicity of gaps directly, (b) "primes eventually settle into a
  periodic pattern of which prime handles each residue" via CRT / density argument,
  (c) an extremal/monovariant argument bounding gcd(a_{n+1},a_i) structure to force
  finitely many primes ever used as the smallest-available witness, (d) analytic
  density / natural-density argument on primes dividing some a_i forcing periodicity
  mod L. Push explorers to scout genuinely different ones, not variations of one.
- ALWAYS install numpy/scipy/sympy via pip (not present by default) in round 1
  setup (round 1).
- ALWAYS check whether the outliner actually persisted approaches/<slug>.md to
  disk before dispatching builders — round 1's outliner registered slugs in the
  ranker but did NOT write the approach files; builders had to be pointed at
  /tmp/round-1/proof-outliner.md for their outline content instead. Verify with
  `ls results/<id>/approaches/` before writing builder prompts (round 1).
- NEVER re-attempt minimal-witness-index-descent framing (Tight(n) descent on
  "tight unresolved earlier indices") — outline-reviewer proved it degenerates:
  the problem's own recursive definition already forces gcd(a_n,a_{n+1})>1, so
  Tight(n) collapses to the trivial singleton {n} and the Step3->Step4 inference
  doesn't follow. Cut before build in round 1.
- NEVER re-attempt bounded-gap-density-covering's original Step 3 strategy
  (upgrade the a_{n+1}-a_n<=rad(a_1) bound to a finite state "backbone-
  agnostically," without identifying which primes get recruited) — builder itself
  proved this collapses onto the same backbone-finiteness question the other
  approaches attack (concrete counterexample: a_1=65 traces {5},{13} force back to
  full radical). Lemma 1 (the gap bound itself) remains valid and reusable; only
  the Step-3 continuation strategy is dead (round 1).
- The core open gap for imo-2026-06 as of round 1: prove "backbone finiteness" —
  only finitely many distinct primes are ever "dominant" per the Domination Lemma
  (results/imo-2026-06/lemmas/domination-lemma.md) across all n, for the
  non-single-prime-saturating case ("Case II", witnessed by a_1=15, stress-tested
  by a_1=247). Growth control is now resolved (Domination Lemma + Lemma 1 combine
  unconditionally); concentration onto finitely many primes and periodicity-from-
  n=1 remain open. Next round's outliner should read lemmas/*.md and try to close
  this directly, or open a genuinely new framing if 2+ more rounds plateau here.
- SUPERSEDED (round 2): the "backbone finiteness" gap as stated above is a false
  formalization (see Eval History round 2) — do not target it. The correct,
  outline-reviewer-validated open target is: finiteness of W, the canonical
  minimal-witness set generated by w(i,j)=min(rad(a_i)∩rad(a_j)) over all pairs
  i<j (equivalently, per intersecting-family-covering-construction's Theorem 2.2,
  finiteness of any finite set H such that every pair i<j shares some H-prime —
  this hypothesis is weaker than W itself and already suffices, per the reviewer's
  generalization). Both live approaches (persistent-backbone-monovariant,
  intersecting-family-covering-construction) now share this exact target plus the
  separate periodicity-from-n=1 gap. NEVER retarget at H_n (pairwise-recruited
  primes, refuted a_1=15) or at (⋆) (primes dividing infinitely many terms,
  refuted a_1=15) — both are proven false, not just hard (round 2).
- ALWAYS sanity-check any new "backbone/covering set" definition against the
  already-solved a_1=15 case (T=8, L=30, tail primes {2,3,5}) with a few seconds of
  Python before spending builder effort on it — this cheap check caught two false
  formalizations in round 2 alone (round 2).
- SUPERSEDED (round 3): periodicity-from-n=1 is now FULLY CLOSED, conditional
  only on FCBC (see below) — Theorem 5.1 (Master Conditional Theorem,
  lemmas/theorem-5.1-master-conditional-theorem.md) proves a_{n+T}=a_n+L for
  EVERY n>=1 (exact, not eventual) whenever a finite covering set H exists,
  independently re-verified by the round-3 reviewer including re-derivation
  of every step. Round 2's negative finding (fails for a_1=35,65) was an
  ARTIFACT of testing against a wrongly-guessed H=rad(a_1), not a real
  obstruction — do not resurrect that finding as a reason to doubt this gap
  is closed. NEVER re-attempt proving periodicity-from-n=1 from scratch —
  it is done; only re-open if a future reviewer finds a flaw in Theorem 5.1.
- THE SOLE REMAINING GAP (round 3): the Finite Covering Backbone Conjecture
  (FCBC) — does a finite set of primes H exist with H∩rad(a_i)∩rad(a_j)≠∅
  for every pair i<j of the whole infinite sequence? Once FCBC is proven, the
  problem is SOLVED (Theorem 5.1 already bridges FCBC => the full headline
  conclusion). Per lemma-W1 (explicit-window-backbone-construction), FCBC is
  logically EQUIVALENT to "some finite K makes H_K=∪_{i<=K}rad(a_i) a
  covering set" — these are the same proposition, not two. Do NOT target
  W-finiteness (canonical witness set) — strong numerical evidence (a_1=4199,
  4087, no plateau to 20000 terms) it is unbounded; FCBC is strictly weaker
  and still open/plausible. Known-failed sufficiency mechanisms for FCBC, do
  NOT re-attempt: (a) literal per-step Domination-Lemma argmax set (refuted,
  Proposition ND1, a_1=221); (b) broadened averaged-threshold set from the
  same argmax idea (refuted, Proposition ND2, a_1=375); (c) "extended-imprint-
  overlap" closing mechanism on forced-primes channels (refuted numerically,
  a_1=247); (d) pointwise-in-N Markov/Cauchy-Schwarz bound on dominant-prime
  count (proven to give only a per-time-slice bound, not global finiteness —
  "cycling primes" obstruction: the bound doesn't control the union over all
  N); (e) finite-descent/well-ordering monovariant directly on |H_K| or
  2^|H_K|-1 (wrong direction — both are non-decreasing in K, round 3
  explicit-window builder). Promising unexplored angles per round 3: the
  "channel reduction" (forced-primes-well-ordering) narrowed FCBC to finitely
  many (<=3^ω(a_1)) independent sub-questions, all but "doubly-infinite-
  class" channels already resolved — attacking those specific channels
  directly is a concrete, narrower next target.
- SUPERSEDED/SHARPENED (round 4): the sole open gap is now more precisely
  pinned to Hypothesis (MRS) — 𝓜_n (the set of distinct radical values
  realized by Lemma W3's inclusion-minimal indices M_n, NOT |M_n| itself)
  is eventually constant. Certified Lemma MS
  (lemmas/lemma-MS-minimal-radical-stabilization-sufficiency.md) proves
  (MRS) ⟹ FCBC ⟹ the whole problem via Theorem 5.1, unconditionally. All 3
  live FCBC framings (ω-bound, channel-reduction, explicit-window) are
  proven the same proposition (Lemma W1) AND this round independently
  converged on producing the identical explicit set H as (MRS)'s target —
  so (MRS) is the sharpest known cut through that single object, not a 4th
  independent framing. Round 5+ should attack (MRS) directly. NEVER attempt
  a plain cardinality monovariant on |𝓜_n| (Lemma-C-style non-increasing-
  integer descent) — proven to fail: |𝓜_n| is non-monotone, with a
  documented collapse 17->3 in one step at n=54 for a_1=4087 (round 4,
  reviewer-reproduced exactly). A correct (MRS) proof needs an invariant on
  the VALUE SET 𝓜_n itself (or a different well-founded order), not on its
  cardinality.
- SUPERSEDED/SHARPENED (round 5): (MRS) is now proven EQUIVALENT to
  finiteness of 𝓥 := ⋃_n 𝓜_n (every value ever locally minimal, not just
  currently minimal) — Theorem V / Theorem V-MRS
  (lemmas/theorem-V-veto-finite-iff-MRS.md), proved twice independently
  (No-Resurrection+Interval-Lemma route and Lemma-PS/NR route), both
  verified correct. 𝓥 further splits, unconditionally, into <=2^k-1 pieces
  𝓥_S indexed by nonempty cores S⊆P_1 via Theorem CD
  (lemmas/theorem-CD-core-decomposition-and-lemma-TC.md) — the top core
  S=P_1 is already closed (𝓥_{P_1}={P_1} always, Lemma TC). THE SOLE
  REMAINING GAP as of round 5: finiteness of 𝓥_S for each remaining proper
  core S⊊P_1 (equivalently forced-primes-well-ordering's (MRS_S) for
  doubly-infinite imprint classes, per Channel Splitting Lemma,
  lemmas/channel-splitting-lemma.md). Round 6+ should attack 𝓥_S-finiteness
  directly using this decomposition rather than 𝓜_n/𝓥 in the raw. Case I
  (single global hub prime) is fully closed unconditionally with an exact
  closed form (Theorem CI, lemmas/theorem-CI-case-I-explicit-stabilization.md)
  — do not re-attempt Case I, only Case II's proper cores remain open.
- NEVER attempt the Dershowitz-Manna multiset-order argument ALONE as a
  complete proof of (MRS)/𝓥_S-finiteness — round 5 confirmed it correctly
  shows each individual collapse event is a well-founded decrease, but does
  NOT bound how many transient/DM-increasing values can accumulate between
  collapses, nor rule out nested/parallel simultaneously-active cores (see
  a_1=2747, 2-level nesting) growing forever. It remains a valid tool for
  part of a proof, just not sufficient by itself (round 5).
- NEVER attempt to bypass (MRS)/𝓥-finiteness via H=rad(L_per) or any other
  "read the covering set off the eventual period" characterization — round 5
  explorer proved this is a circular tautology of already-certified Theorem
  5.1 (L=lcm(H) for a covering set H trivially gives rad(L)=H), not a new
  route; computing L_per already presupposes the periodicity being proved
  (round 5).
- Round 5's fresh-framing explorer tried 6 genuinely different top-level
  attacks on the ORIGINAL problem statement (edge-clique-cover/Ramsey,
  Morse-Hedlund/subword-complexity, ultrafilter/compactness limit,
  generating-function encoding, bounded-clique transversal, elementary
  "derive-from-the-conclusion" consequences) and found NONE escape FCBC/
  (MRS) — treat this as evidence (not proof) that FCBC really is the
  problem's irreducible core, so continuing to sharpen (MRS)/𝓥_S rather
  than hunting for an orthogonal framing is likely still the right call,
  though CLAUDE.md's 3+-round-plateau guidance should be revisited if round
  6 also fails to close 𝓥_S (round 5).
- Round 6 confirmed (again) via a targeted crux-corpus + knowledge_base.md
  search that NO analytic-number-theory/probabilistic tool (sieve, Mertens,
  Borel-Cantelli, second-moment) applies — the sequence is fully
  deterministic, no randomness to average over; Mertens divergence argues
  AGAINST a sieve-exhaustion approach, not for one. Two closest crux
  analogues (aimo-0477 bounded-ascending-divisor-chain, aimo-0134
  monotone-monovariant+difference-identity) checked in detail and confirmed
  NOT transplantable (both need a fixed finite ambient bound proper-core
  fans don't have). NEVER re-dispatch a generic "search for an analytic
  tool" explorer lens on this problem again — it is now confirmed twice
  (round 3 partially, round 6 thoroughly) that none exists in the KB/corpus;
  any future analytic angle must be built from scratch, not retrieved
  (round 6).
- NEVER re-attempt strong induction on core size |S| as a termination
  measure for 𝓥_S-finiteness (the core-depth-induction approach's Step 3) —
  round 6 builder AND reviewer independently confirmed |S| does not track
  difficulty: a_1=21528751 has 3 singleton (|S|=1) cores with fresh-value
  counts 2363, 41, and 2 through n=6000 (1000-fold spread at identical core
  size), and the conjectured "depth-d event = nested depth-(d-1) shape" is
  fully refuted (0/13 fresh values of the depth-2 core S={197,103} match
  through n=6000, reviewer-reproduced exactly, stronger than the builder's
  own claimed 12/13). Lemma B1 (singleton-core value pinning via FOM)
  remains valid, certified, reusable content — only the induction-on-|S|
  architecture built on top of it is dead (round 6).
- NEVER re-attempt a single-witness "Freeze Criterion" for proper-core
  freezing (one witness index's companion-prime set blocking all
  extensions) — round 6 builder found and reviewer confirmed a concrete
  counterexample on a_1=247: witness a_3 (companion radical {2,7,19}) does
  NOT block candidate extensions {2,13} or {7,13} (they share a prime with
  it). The correct replacement is the Companion-Disjointness Coarsening
  Lemma (results/imo-2026-06/lemmas/lemma-companion-disjointness-
  coarsening.md, certified round 6): needs TWO witnesses with DISJOINT
  companion-prime sets to force a finite coarse-bucket decomposition; when
  no such disjoint pair exists (e.g. a_1=2747, S={41}, all witnesses share
  {2,3,7} through n=400), the core does not freeze and the bucket mechanism
  doesn't directly apply (round 6).
- THE SOLE REMAINING GAP as of round 6 is now most precisely stated as a
  LOCAL, RESTRICTED instance of FCBC itself: per persistent-backbone-
  monovariant's Multi-Companion Reduction Proposition AND forced-primes-
  well-ordering's cross-bucket-domination gap (independently derived,
  reviewer-confirmed to be the same underlying difficulty) — bounding how
  many primes can ever serve as a MULTI-prime companion bundle to a fixed
  proper core S reduces to a finite hitting-set condition on
  {rad(a_j): j∈J_S}, structurally the same shape as the original FCBC but
  restricted to indices in the S-avoiding set J_S. This is the 4th
  consecutive round (3,4,5,6) the population bottoms out on essentially the
  same self-similar difficulty, now confirmed self-similar in a precise,
  proved sense (not just "feels similar") — round 7 should weigh whether
  this genuine self-similarity (FCBC restricted to a sub-sequence is still
  FCBC-shaped) points toward a proof BY INDUCTION ON A DIFFERENT WELL-
  FOUNDED QUANTITY than |S| (round 6 killed |S|) — e.g. induction on
  |companion bundle size| itself (single-companion case IS fully closed,
  round 6's Single-Companion Finiteness Lemma — multi-companion is what's
  open), or accept CLAUDE.md's plateau guidance and open a genuinely
  orthogonal top-level approach not yet tried in any of rounds 1-6 (round 6
  explorers found no such escape, but did not exhaustively rule one out for
  the NARROWED multi-companion-bundle sub-question specifically, only for
  the whole problem and for 𝓥_S generally) (round 6).

## State

### Done (round 1)
- Verified environment: numpy/scipy/sympy installed via pip.
- Confirmed problem identity: user's IMO P6 statement == `imo-2026-06` in
  problems.jsonl (proof_only, number_theory, difficulty_rating 9).
- Created results/imo-2026-06/{approaches,lemmas}/ directories (were placeholder-only).
- Ran full pipeline: 3 math-explorers (graph-structure, finite-primes-crt,
  gap-monovariant) -> proof-outliner (4 approaches opened) -> outline-reviewer
  (cut 1, ranked 3, build set emitted) -> 3 proof-builders in parallel -> 1
  proof-reviewer (all 3 CHANGES REQUESTED, 7 lemmas certified, current.md written).
- results/imo-2026-06/current.md Status = partial.

### Done (round 2)
- Ran 3 math-explorers in parallel, each a genuinely different lens: backbone-
  finiteness/concentration, periodicity-from-n=1, and alt-framing (plateau-break
  insurance). Alt-framing explorer found and proved round 1's core gap
  formalization false (see Eval History / Rules).
- proof-outliner revised backbone-existence-crt (retargeted at (⋆), later also
  refuted) and intersecting-family-covering-construction (retargeted Case II,
  new strong-induction-from-n=1 architecture), opened new approach persistent-
  backbone-monovariant (aimo-0678-inspired well-ordering mechanism), parked
  bounded-gap-density-covering.
- outline-reviewer found (⋆) also false, validated persistent-backbone-
  monovariant's canonical-minimal-witness target W as the correct reformulation,
  gave backbone-existence-crt RETHINK (Step 3 only), APPROVEd persistent-backbone-
  monovariant's skeleton, CHANGES REQUESTED intersecting-family-covering-
  construction's Step 4. Build set: persistent-backbone-monovariant,
  intersecting-family-covering-construction.
- 2 proof-builders in parallel: persistent-backbone-monovariant certified Lemma C,
  refuted its own 2 natural W-finiteness conjectures with hand-verified
  counterexamples (a_1=221, a_1=375), reformulated to weaker still-open "Finite
  Covering Backbone Conjecture." intersecting-family-covering-construction proved
  a new conditional bridge W/H-finite => eventual periodicity (Thm 2.2, Lemma 2.3,
  Thm 2.4).
- proof-reviewer independently re-verified all claims (including re-simulating
  both counterexamples), CHANGES REQUESTED both (partial, no RETHINK), certified
  6 new lemmas, generalized Theorem 2.2's hypothesis (reviewer-owned improvement),
  updated current.md.
- results/imo-2026-06/current.md Status = partial (unchanged label, but the open
  gap is now correctly formalized instead of chasing a false target).

### Broken
(none)

### Next
- Round 3: the shared core gap is now precisely and correctly stated: does a
  finite set H exist such that every pair i<j of terms shares some H-prime
  (equivalently, finiteness of canonical-witness set W — the H-only version is
  weaker and already suffices per Theorem 2.2's reviewer-generalized hypothesis)?
  Dispatch explorer(s) that attack THIS exact question fresh — do not reuse the
  now-refuted H_n or (⋆) framings even as a starting point. Promising unexplored
  angles per round 2 reports: (a) persistent-backbone-monovariant's own
  well-ordering/minimal-counterexample mechanism (still open, not yet closed);
  (b) the second-moment/Cauchy-Schwarz plan on Σ_q D_n(q)^2 via Mertens (flagged
  by math-explorer-backbone-finiteness.md opening 2, not yet attempted since the
  target it was aimed at (⋆) is now refuted — check whether it can be retargeted
  at W/H instead); (c) fresh eyes on why NC1 (a_1=221) and NC2 (a_1=375) fail, to
  find what invariant DOES survive them.
- Separately/in parallel conceptually: periodicity-from-n=1 remains open even
  conditional on H-finiteness (intersecting-family-covering-construction's naive
  mechanism fails for a_1=35,65) — worth a dedicated explorer lens again if round 3
  closes the H-finiteness gap, since CLAUDE.md's per-approach routing means this
  could become the sole remaining blocker.
- Then proof-outliner: advance persistent-backbone-monovariant and intersecting-
  family-covering-construction (both real progress, no RETHINK); backbone-
  existence-crt got RETHINK on Step 3 only — Sections 1/2/4 remain valid/certified,
  so the outliner may either repair Step 3 with the new W/H target or let it stay
  parked; do NOT re-open minimal-witness-index-descent or bounded-gap-density-
  covering's original Step 3 strategy (see Rules).
- Then outline-reviewer -> build set -> proof-builder(s) -> proof-reviewer, same
  pipeline as rounds 1-2.

- Round 7 (post-work): Status = partial. 3 math-explorers ran in parallel, split
  mandate per the round-6 plateau flag: 2 continuing the narrowed multi-companion
  line, 1 dedicated to finding a genuinely new top-level mechanism. multicompanion-
  induction explorer PROVED (not just observed) bundle-size induction ALSO fails,
  via a new Permanent Pair Lemma (bundles with both companions outside D_S\P_1 are
  permanently undominated) — stronger than round 6's |S|-induction refutation
  since it shows some instances can NEVER reduce to the base case, not just that a
  proposed reduction is empirically false. cross-bucket-domination explorer proved
  a new Escape-Confinement Lemma (escape primes confined to blocking witness's
  companion set) and found a striking empirical pattern: a small set W(a_1) same
  across all SINGLETON cores of a fixed a_1. orthogonal-mechanism explorer found
  NO new top-level escape (2nd confirmation after round 5): checked crux aimo-0447
  (fails quantitatively, density argument needs a deficiency that never appears)
  and a Ramsey-extraction idea (proved definitionally identical to round-1's
  Lemma R). Outliner revised persistent-backbone-monovariant (Permanent Pair/
  Bundle Lemma + pivot to bounding count of D_S-disjoint bundles) and forced-
  primes-well-ordering (Escape-Confinement Lemma + escape-recursion-depth target),
  opened NEW global-recruiter-finiteness (global W(a_1) reformulation) but flagged
  its own Step 0: a likely counterexample already in this round's data. outline-
  reviewer independently reverified the tension from scratch and confirmed
  Hypothesis (GW) AS STATED IS FALSE (a_1=21528751, depth-2 core {103,197},
  permanent bundle {11,97} lies outside the singleton-only W={2,3,7}) — cheap
  honest kill, build set still 3 slugs. All 3 builders ran: persistent-backbone-
  monovariant found+closed a real gap in its own Permanent Pair Lemma (silent
  incompleteness for non-singleton cores), generalized to Permanent Bundle Lemma
  (arbitrary size k, validated on 44 fresh bundles/5 hard cases, zero exceptions),
  pushed antichain-freeze simulation to N=5,000,000 (deepest evidence yet for
  (MRS), still no general proof). forced-primes-well-ordering certified Escape-
  Confinement Lemma, attempted escape-recursion-depth bound: found max realized
  depth 2 across 13 instances BUT diagnosed the natural structural-induction
  formalization does not visibly terminate (depth 6 explored, leaves proliferate),
  and that the observed small depth is an artifact of the already-open cross-
  bucket-domination gap, not an independent route. global-recruiter-finiteness
  self-diagnosed a clean dead end: proved any global/depth/nested W(a_1) variant
  is logically EQUIVALENT (same mechanism as certified Theorem CD) to the
  per-core statement already under direct attack — no new leverage, Status
  unsolved. proof-reviewer independently re-derived everything from scratch
  (fresh generators, cross-validated against each other, freeze simulation
  re-run to 400k-1M on all 5 cases, exact match) and caught a REAL ERROR the
  builder missed: forced-primes-well-ordering's "max escape depth 2" claim is
  WRONG — reviewer found 2 confirmed depth-3 counterexamples by extending the
  builder's own search (a_1=2747 bucket {17,23,67} n=19617; a_1=21528751 bucket
  {19,41,197} n=30017). Verdicts: persistent-backbone-monovariant CHANGES
  REQUESTED (advanced), forced-primes-well-ordering CHANGES REQUESTED (partial,
  with the depth-3 correction flagged), global-recruiter-finiteness RETHINK
  (dead-end confirmed). No cross-approach synergy found. Elo: intersecting-
  family-covering-construction 1688.4 (top, done pending FCBC), forced-primes-
  well-ordering 1620.4, persistent-backbone-monovariant 1588.3, core-depth-
  induction 1487.5 (parked), explicit-window-backbone-construction 1487.4
  (parked), global-recruiter-finiteness 1476.8 (dead-end, new), imprint-
  automaton-periodicity 1445.9 (parked), backbone-existence-crt 1411.5 (parked),
  bounded-gap-density-covering 1322.0 (parked, dead-end). Annotation: IMPROVED
  (two genuinely new certified lemmas — Permanent Pair/Bundle Lemma and Escape-
  Confinement Lemma — plus a clean, well-argued elimination of a whole new
  reformulation family (GW) in one round rather than several; the reviewer's
  catch of a false "depth 2 max" claim is itself valuable: escape-recursion
  depth is NOT bounded by 2, so any future depth-bound attempt must account for
  depth>=3 instances). This is the 5th consecutive round (3-7) on the FCBC/
  (MRS)/𝓥_S family; round 7's dedicated orthogonal-mechanism explorer found
  nothing new for the 2nd time (after round 5) — see sharpened Rule below.

- Round 5 (post-work): Status = partial. All 3 approaches targeting Hypothesis
  (MRS) (persistent-backbone-monovariant, forced-primes-well-ordering,
  imprint-automaton-periodicity) made independently-verified progress and all
  converged on the exact same reduced open fact, now in its cleanest form:
  **finiteness of 𝓥_S (equivalently (MRS_S)) for each remaining proper core
  S⊊P_1** (Theorem CD's core decomposition; top core S=P_1 already closed
  unconditionally via Lemma TC). 3 math-explorers (MRS-direct, H-characterization,
  fresh-framing) ran first: MRS-direct found a genuinely new first-hitting-time
  "fan/threshold" mechanism + Dershowitz-Manna multiset-order idea (shown this
  round to be necessary-but-insufficient alone: proves individual collapses are
  well-founded decreases but doesn't bound growth-phase length or nested-core
  count); H-characterization proved H=rad(L_per) is a tautology of Theorem 5.1,
  a dead end for bypassing (MRS); fresh-framing tried 6 genuinely different
  top-level framings (graph/Ramsey, Morse-Hedlund, ultrafilter/compactness,
  generating-function, etc.), found NONE escape FCBC/(MRS) — strong confirmation
  FCBC really is the irreducible core, not an artifact of current framings.
  outline-reviewer caught a real gap in imprint-automaton-periodicity's first
  draft (Bounded-Core-Family sub-lemma only covered collapse-triggering cores,
  missed permanent survivors — counterexample a_1=91, 3 permanent survivors,
  zero collapses) before build; builder fixed it same round (Lemma PS/NR/
  Theorem V-MRS/Theorem CD/Lemma TC). persistent-backbone-monovariant proved
  Theorem V (𝓥 finite ⟺ (MRS)) independently via a different route (No-
  Resurrection Lemma + Interval Lemma) — reviewer confirmed both Theorem V
  proofs correct and merged into one lemma file — plus Theorem CI: Case I
  gives 𝓥 finite unconditionally with an EXACT closed-form stabilization
  index (reviewer re-derived a_1=11623 -> N_0=3285 exactly from scratch).
  forced-primes-well-ordering proved the Channel Assembly Theorem (global FCBC
  follows from independent per-channel stabilization, zero cross-channel
  leakage, citing Lemma FH) and the Channel Splitting Lemma (reduces
  <=3^ω(a1) two-sided channels to <=2^ω(a1)-1 one-sided (MRS_S) conjectures;
  reviewer reproduced exactly on a_1=247,2747 incl. exact stabilization
  position 154 for a_1=2747), plus an unconditional strengthening of Lemma
  FX2 (finite imprint classes need no conditional machinery). Reviewer found
  and flagged one numerics error (not a proof error): forced-primes-well-
  ordering's §E misattributed a_1=21528751's dramatic 1103->8 collapse data
  to the local class-restricted antichain when it was actually the global
  antichain; true local antichain collapses 1092->3 directly, no further
  changes -- corrected, does not affect any certified theorem. Reviewer
  explicitly checked for cross-approach synergy closing the remaining gap:
  none found; confirmed genuinely partial, not overclaimed as solved. All 3
  verdicts: CHANGES REQUESTED (advanced), none RETHINK. 7 new lemmas
  certified (31 total in lemmas/, including a merged Theorem V file citing
  both independent proofs). Elo: intersecting-family-covering-construction
  1665.1 (top, done pending FCBC), forced-primes-well-ordering 1579.3,
  persistent-backbone-monovariant 1569.2, explicit-window-backbone-
  construction 1525.6 (parked), imprint-automaton-periodicity 1440.9,
  backbone-existence-crt 1419.8 (parked), bounded-gap-density-covering 1328.5
  (parked, dead-end). Annotation: IMPROVED (steady, well-verified narrowing;
  the sole open gap is now sharper and better-organized than round 4's (MRS)
  but not smaller in a way that changes the difficulty — genuine open content
  (𝓥_S finiteness in Case II) remains fully unresolved; this is the 3rd
  consecutive round the same core proposition survives attack, so round 6
  should weigh CLAUDE.md's "3+ rounds plateau -> genuinely different framing"
  guidance, tempered by this round's fresh-framing explorer finding that no
  alternative framing has yet escaped FCBC).

### Done (round 3)
- Ran 3 math-explorers in parallel: FCBC direct attack (found new invariant
  H_ρ, retargeted Cauchy-Schwarz plan, found ω(a_n) bound stays single-digit
  numerically), monovariant-mechanism scout (found W likely unbounded,
  found "forced primes" H candidate that passed every stress test), and
  periodicity-from-n=1 scout (found round 2's negative result was an
  artifact, true-H periodicity-from-n=1 holds with zero exceptions).
- proof-outliner built 4-approach field: 3 rival FCBC techniques + 1
  periodicity-from-n=1 retarget, all persisted to disk.
- outline-reviewer: no RETHINK, build set = all 4 slugs, ranked field, copied
  forced-primes-well-ordering as new branch, registered explicit-window-
  backbone-construction fresh.
- 4 proof-builders in parallel. intersecting-family-covering-construction
  FULLY CLOSED periodicity-from-n=1 (Theorem 5.1, conditional on FCBC). The
  3 FCBC approaches made real progress, ruled out several sufficiency
  mechanisms, proved FCBC-equivalence across all 3 (Lemma W1), did not close
  FCBC itself.
- proof-reviewer independently re-derived/re-simulated all 4 builds, all
  CHANGES REQUESTED (none RETHINK, none APPROVE yet), certified 8 new lemmas
  (21 total), rewrote current.md to reflect single-gap state.
- results/imo-2026-06/current.md Status = partial (but now: exactly ONE gap,
  FCBC, remains for the entire problem).

### Done (round 4)
- Ran 3 math-explorers in parallel, each a genuinely different lens on the
  sole remaining gap FCBC: doubly-infinite-channels direct attack (found
  G_n, the P_1-imprint sequence, is numerically purely periodic from n=1,
  zero exceptions across 12 a_1 incl. hard cases to 400,000 terms), H_ρ
  density-excess invariant (fixed a flat-threshold bug, matches rad(L_per)
  exactly in 26 stress tests, closed 2 previously-open hard cases a_1=247,
  4199), and an adversarial "try to refute FCBC" lens (found a new hardest
  case a_1=21528751 with K=86, 17x harder than prior worst case; FCBC
  survived; proved via Patch-via-P′ Lemma that FCBC's "every pair" really
  is irreducible to "both indices arbitrarily large" — no easier equivalent
  target exists).
- proof-outliner built a 3-slug build set, deliberately diversified per
  CLAUDE.md's single-gap-trap warning since all 3 live FCBC approaches
  target the literally-identical proposition (Lemma W1): opened new
  imprint-automaton-periodicity (G_n periodicity lever), pivoted
  explicit-window-backbone-construction (compactness/König framing),
  pivoted forced-primes-well-ordering (H_ρ/channel bridge). Parked
  persistent-backbone-monovariant (no new idea this round, ND1/ND2 still
  block its old framing).
- outline-reviewer approved the field as genuinely diverse (verified, not
  rubber-stamped), specifically checked imprint-automaton-periodicity's
  Gap A is not a round-2-style trap (it proposes no untested mechanism,
  unlike the 5 already-refuted ones) and that the König's-lemma pivot isn't
  hand-waving. Build set: all 3 new/pivoted slugs.
- 3 proof-builders in parallel, all CHANGES REQUESTED (no RETHINK):
  imprint-automaton-periodicity found and proved new **Lemma MS**:
  Hypothesis (MRS) (𝓜_n, minimal-radical antichain of Lemma W3's indices,
  eventually constant) ⟹ FCBC ⟹ whole problem via Theorem 5.1 — single
  clean implication, no extra machinery. explicit-window-backbone-
  construction proved Lemma W4 (Pool Lemma): FCBC ⟺ some finite pool Π has
  all level sets 𝒢_N(Π) nonempty — a real equivalence via finite descent,
  honestly self-scoped as architecture not progress. forced-primes-well-
  ordering proved Lemma FH (uncovered-pair localization) and reduced its
  own gap to 2 independent conjectures (Lemma FF finiteness, Lemma FS
  forced-sufficiency).
- proof-reviewer independently re-derived and re-verified all 3 new lemmas
  from scratch (fresh Python, exact factorization, no reliance on builder
  scripts), certified MS/W4/FH into lemmas/ (24 total). **Key convergence
  finding**: all 3 independent constructions produce the IDENTICAL explicit
  finite set H for every tested a_1 (e.g. a_1=4199 → {2,3,13,17,19,83} from
  all three methods) — strong evidence of one canonical object.
  Recommended (MRS) as round 5's single sharpest target: it's one
  conjecture (not two like FF+FS), a strict equivalence-free sufficient
  condition (unlike Pool Lemma), and stabilizes very early empirically
  (n<=92 worst case vs periods in the hundreds of thousands) — suggesting
  combinatorial, not analytic-density, proof territory (Lemma FF provably
  needs Mertens/Borel-Cantelli tooling confirmed absent from KB and corpus).
- results/imo-2026-06/current.md Status = partial. Elo:
  intersecting-family-covering-construction 1656.8 (top, done pending FCBC),
  explicit-window-backbone-construction 1556.7, forced-primes-well-ordering
  1552.3, persistent-backbone-monovariant 1541.1, imprint-automaton-
  periodicity 1473.2, backbone-existence-crt 1419.8 (parked),
  bounded-gap-density-covering 1328.5 (parked).

### Done (round 5)
- Ran 3 math-explorers in parallel, each a genuinely different lens on
  (MRS): direct mechanism scout (found first-hitting-time fan/threshold
  mechanism + Dershowitz-Manna multiset-order idea, both new), H-
  characterization (proved H=rad(L_per) is a circular tautology, dead end),
  fresh-framing insurance (tried 6 orthogonal top-level framings, none
  escaped FCBC — confirms FCBC is the irreducible core).
- proof-outliner revised all 3 live approaches with genuinely different
  mechanisms all targeting (MRS): persistent-backbone-monovariant (No-
  Resurrection Lemma + Event-Counting Corollary), forced-primes-well-
  ordering (channel-localized divide-and-conquer), imprint-automaton-
  periodicity (DM-order + fan/threshold, corrected T_C formula).
- outline-reviewer caught a real pre-build gap in imprint-automaton-
  periodicity (Bounded-Core-Family sub-lemma missed permanent survivors,
  a_1=91 counterexample), approved the other two outright, build set = all
  3 (none RETHINK).
- 3 proof-builders in parallel. imprint-automaton-periodicity fixed the
  flagged gap (Lemma PS/NR/Theorem V-MRS/Theorem CD/Lemma TC).
  persistent-backbone-monovariant proved Theorem V (𝓥 finite ⟺ (MRS)) +
  Theorem CI (Case I closed unconditionally, exact closed form).
  forced-primes-well-ordering proved Channel Assembly Theorem + Channel
  Splitting Lemma (reduces to <=2^ω(a1)-1 one-sided (MRS_S) conjectures).
  All 3 converged independently on the identical remaining open fact.
- proof-reviewer independently re-derived/re-simulated everything from
  scratch, merged the two independent Theorem V proofs into one lemma file,
  caught and corrected one numerics misattribution (not a proof error,
  forced-primes-well-ordering §E), confirmed no cross-approach synergy
  closes the remaining gap, confirmed genuinely partial not overclaimed.
  All 3 verdicts CHANGES REQUESTED (advanced), none RETHINK. 7 new lemmas
  certified (31 total). Rewrote current.md with Round 5 update.
- results/imo-2026-06/current.md Status = partial. Elo:
  intersecting-family-covering-construction 1665.1 (top, done pending
  FCBC), forced-primes-well-ordering 1579.3, persistent-backbone-monovariant
  1569.2, explicit-window-backbone-construction 1525.6 (parked),
  imprint-automaton-periodicity 1440.9, backbone-existence-crt 1419.8
  (parked), bounded-gap-density-covering 1328.5 (parked, dead-end).

### Next (round 6)
- **Single sharpest target: 𝓥_S-finiteness** for each remaining proper
  core S⊊P_1 (equivalently (MRS_S) for doubly-infinite imprint classes,
  per Channel Splitting Lemma). This is now the cleanest possible
  restatement of the whole problem's sole remaining content — Case I and
  the top core S=P_1 are both fully closed unconditionally; only Case II's
  proper cores remain. Dispatch explorer(s) directly at this: does 𝓥_S
  admit a bound via the first-hitting-time/fan mechanism combined with
  Theorem CI's Case-I closed-form template (round 5's MRS-direct explorer
  flagged this combination as untested — Case I's mechanism needs "a
  single dominating prime," unavailable in Case II by Lemma C's
  ∩P_i=∅ conclusion, but the fan/threshold *shape* of argument might still
  transfer with a per-core adaptation)?
- This is round 3 running on the FCBC/(MRS)/𝓥_S family as the sole gap
  (rounds 3,4,5). Per CLAUDE.md's single-gap-trap guidance, round 6's
  outliner should weigh opening >=1 approach with a genuinely different
  top-level mechanism for 𝓥_S specifically (not just another cut of FCBC)
  — BUT round 5's fresh-framing explorer already tried 6 orthogonal
  framings of the whole original problem and found none escape FCBC, so a
  6th-round fresh-framing dispatch on the WHOLE problem is likely low
  -value; more promising is a fresh mechanism aimed narrowly AT 𝓥_S itself
  (e.g. probabilistic/second-moment argument now that the search space is
  much smaller — <=2^k-1 cores instead of the whole sequence — or a direct
  attempt at strengthening the DM-multiset-order idea with an explicit
  bound on growth-phase length between collapses, which round 5 identified
  as the precise missing piece).
- Do not re-run H-characterization or a 6-framing fresh-framing sweep
  again unless round 6 also plateaus — both were tried thoroughly this
  round with negative/dead-end results (see Rules).

- Round 6 (post-work): Status = partial. 3 math-explorers ran in parallel,
  each a genuinely different lens on 𝓥_S-finiteness: fan-structural (found
  and proved new Lemma FOM — First-Occurrence Minimality: a radical value's
  first-ever occurrence as some a_n's radical always equals the explicit
  minimum T_C; verified 6000+ radical first-occurrences, 70+ collapse
  events, zero exceptions), analytic-tools (confirmed AGAIN no analytic/
  probabilistic tool applies — see Rules), narrow-fresh-framing (confirmed
  the Case-I-template DOES transfer to proper cores but is recursive/
  nested — a_1=21528751's depth-2 core stabilizes at n=101957 via 2 nested
  depth-1-shaped absorptions — flagged as real but risking circularity).
  proof-outliner built a 4-slug field (later trimmed to 3 for build, one
  deferred as redundant): revised persistent-backbone-monovariant (Lemma
  FOM + open Growth-Budget Lemma), NEW core-depth-induction (strong
  induction on |S|, testing whether nesting depth gives a well-founded
  escape from the recursive-but-circular trap), revised
  forced-primes-well-ordering (Permanent-Freeze Dichotomy), revised
  imprint-automaton-periodicity (deferred by outline-reviewer as
  essentially the same bridge as persistent-backbone-monovariant's
  Growth-Budget Lemma — genuine redundancy caught pre-build, not a
  diversity failure). outline-reviewer independently re-derived Lemma FOM
  by hand + fresh-tested it on 9 new a_1 values (1442 checks, zero
  violations), reproduced both mandatory sanity-check examples
  (a_1=247 freeze, a_1=2747 non-freeze) from scratch, build set = 3 slugs
  (none RETHINK pre-build). All 3 builders ran in parallel: persistent-
  backbone-monovariant certified FOM + 4 new lemmas (ER, Λ_S-Reduction,
  Single-Companion Finiteness — exact numerical matches on 2 cases) and
  proved (not just asserted) the remaining gap reduces to a local
  FCBC-shaped hitting-set problem (Multi-Companion Reduction Proposition);
  core-depth-induction proved Lemma B1 (singleton-core pinning) but found
  and the reviewer independently CONFIRMED (even more strongly: 0/13 not
  12/13) that the induction-on-|S| architecture's Step 3 mechanism is
  refuted — |S| doesn't track difficulty (1000x spread at |S|=1 on
  a_1=21528751); forced-primes-well-ordering REFUTED its own outline's
  single-witness Freeze Criterion (real counterexample, a_1=247) but proved
  a working replacement, the Companion-Disjointness Coarsening Lemma,
  verified exactly on both mandatory examples. proof-reviewer independently
  re-derived/re-simulated all claims from scratch (fresh code, not
  builders' scripts), certified 6 new lemmas (37 total), explicitly checked
  cross-approach synergy (found genuine conceptual convergence — the
  Multi-Companion Reduction gap and the cross-bucket-domination gap are the
  same difficulty in two languages — but no combination closes it). All 3
  verdicts: CHANGES REQUESTED, none RETHINK (per this workspace's standing
  rule that real certified progress, e.g. Lemma B1, keeps a verdict at
  CHANGES REQUESTED even when a specific sub-mechanism is refuted). Elo:
  intersecting-family-covering-construction 1688.4 (top, done pending
  FCBC), forced-primes-well-ordering 1611.7, persistent-backbone-
  monovariant 1573.9, core-depth-induction 1487.5 (new), explicit-window-
  backbone-construction 1487.4 (parked), imprint-automaton-periodicity
  1445.9 (parked this round), backbone-existence-crt 1411.5 (parked),
  bounded-gap-density-covering 1322.0 (parked, dead-end). Annotation:
  IMPROVED (real narrowing — the remaining gap is now PROVED to be a
  self-similar local instance of FCBC restricted to the S-avoiding index
  set, not just observed to feel similar; single-companion case is now
  fully closed, isolating multi-companion bundling as the precise
  remaining unknown; one dead architecture (induction on |S|) cleanly
  eliminated so round 7 doesn't repeat it). This is the 4th consecutive
  round (3-6) on the FCBC/(MRS)/𝓥_S family — see sharpened Rule below on
  what round 7 should weigh.

## Eval History (round 8 addendum)

- Round 8 (post-work): Status = partial. **BREAKTHROUGH-adjacent narrowing**:
  the entire problem now reduces, unconditionally and reviewer-verified, to
  exactly ONE clean hypothesis, `(UB_S)` (sup{ω(a_n): n∉I_{P_1}}<∞,
  restricted per-core companion-bundle-size boundedness). 3 math-explorers
  ran in parallel per round 7's "Next" mandate: subset-avoidance (found new
  pairwise-disjoint-bundle pigeonhole corollary, ~636k-check verified, plus
  a sketched Δ-system extension), thread-unification (proved 𝓥_S-finiteness
  ⟹ bounded escape-depth one-directionally, and permanent-count-alone is
  insufficient — the real gap is transient-member count), cross-bucket-
  direct (found S^+ extended-imprint recruiter set, necessary but not
  sufficient, one counterexample S={1061}). Outliner built 3-slug field:
  revised persistent-backbone-monovariant (retargeted at transient count
  per thread-unification's finding), revised forced-primes-well-ordering
  (retired independent depth-hunting, pivoted to S^+/S^{++}), new
  sunflower-bundle-closure (classical Δ-system/sunflower dichotomy). No
  4th orthogonal-mechanism approach opened (outliner judged this round's
  findings pointed at concrete closable steps, not a flat plateau).
  outline-reviewer independently verified all 4 dispatch-flagged claims
  plus the shared core-avoiding-witness prerequisite, no RETHINK, build set
  = all 3. All 3 builders ran: sunflower-bundle-closure proved the headline
  Theorem-UBS-sufficiency ((UB_S) ⟹ whole problem, unconditional beyond
  (UB_S), via new Lemma ERD/Lemma SR/Δ-system dichotomy) and honestly
  diagnosed why its own machinery can't close (UB_S) itself (bounds bundle
  COUNT not SIZE). persistent-backbone-monovariant certified RBD Lemma
  (duplicate of sunflower's ERD, merged) + Finite-Reachability Theorem
  conditional on new open hypothesis NIBC. forced-primes-well-ordering
  certified Freeze-Confinement Domination Lemma + S^+ Necessity/Finiteness
  Lemma, self-corrected its own outline's depth-bound formula (doesn't
  follow), proved S^{++} sufficiency fix FAILS via 2 new negative results
  (Vacuity Proposition, Intersection-Fragility Proposition). proof-reviewer
  independently re-derived/re-simulated everything from scratch (fresh
  generator, not builders' scripts — 3 max-ω(a_n) values, full 19-index S^+
  table, escape-chain worked example, zero discrepancies), found a real
  cross-approach synergy neither builder noticed (RBD + Lemma SR dissolves
  persistent-backbone-monovariant's witness-existence gap, leaving NIBC as
  its sole remaining gap), certified 7 new lemma files (46 total). All 3
  verdicts: CHANGES REQUESTED, none RETHINK. Elo and current.md updated.
  Annotation: BREAKTHROUGH-adjacent (not a solve, but the sole remaining
  gap across the whole 6-round FCBC/(MRS)/𝓥_S family is now, for the first
  time, reduced to ONE unconditionally-sufficient hypothesis with a
  precise structural diagnosis of why prior techniques can't reach it —
  round 9 has a genuinely sharper, narrower target than any prior round).

## State

### Done (round 6)
- Ran 3 math-explorers in parallel (fan-structural, analytic-tools,
  narrow-fresh-framing) — see Eval History for findings (Lemma FOM found,
  analytic tools confirmed absent, Case-I-template transfer found but
  recursive).
- proof-outliner revised persistent-backbone-monovariant, forced-primes-
  well-ordering, imprint-automaton-periodicity, opened new core-depth-
  induction; all persisted to disk (verified).
- outline-reviewer independently re-verified Lemma FOM and both mandatory
  numerical sanity checks from scratch, deferred imprint-automaton-
  periodicity as a redundant bridge (caught before wasting a build slot),
  build set = persistent-backbone-monovariant, core-depth-induction,
  forced-primes-well-ordering.
- 3 proof-builders in parallel — see Eval History for what each closed/
  refuted.
- proof-reviewer independently re-derived and re-simulated every claim
  from scratch (own code, not builders'), certified 6 new lemmas (37
  total), checked cross-approach synergy (found convergence, not a
  solve), all 3 verdicts CHANGES REQUESTED (none RETHINK), updated
  current.md with Round 6 section.
- results/imo-2026-06/current.md Status = partial.

### Broken
(none)

### Next (round 7)
- **The remaining gap is now precisely: bounding multi-prime companion
  bundles for a proper core S** — proved (not just observed) to reduce to
  a LOCAL, RESTRICTED instance of FCBC on the S-avoiding index set J_S
  (persistent-backbone-monovariant's Multi-Companion Reduction Proposition
  + forced-primes-well-ordering's cross-bucket-domination gap, confirmed
  by the reviewer to be the same difficulty). The SINGLE-companion case is
  now fully closed (Single-Companion Finiteness Lemma) — this is genuine
  progress, not a restatement, since it isolates exactly what's open.
- Concrete ideas to try per round 6's own Rules entry: (a) induction on
  companion-bundle SIZE (not core size |S|, which is refuted) — does
  single-companion-closed give a base case for size-2, size-3, ... bundles
  with a genuine reduction this time? (b) if round 7 also plateaus on this
  narrowed sub-question, treat CLAUDE.md's plateau guidance as triggered
  for real (this is round 4 of 4 on the FCBC family) and open >=1 approach
  with a top-level mechanism never tried on ANY narrowing of this problem
  in rounds 1-6.
- NEVER re-attempt: induction on |S| (refuted round 6, see Rules), single-
  witness Freeze Criterion (refuted round 6, see Rules), generic "search
  KB/corpus for an analytic tool" (confirmed absent twice, see Rules), nor
  any of the round 1-5 refuted mechanisms already listed in Rules above.
- imprint-automaton-periodicity was deferred (not built) this round as
  redundant with persistent-backbone-monovariant's bridge — do not treat
  this as a dead-end verdict, it's simply parked; if persistent-backbone-
  monovariant's Growth-Budget Lemma line of attack is abandoned, this slug
  may be worth reviving with a genuinely different bridge mechanism.
- NEVER re-attempt bundle-size induction (inducting on companion-bundle size
  |Q|, the natural follow-up to round 6's Single-Companion Finiteness Lemma)
  as a route to multi-companion-bundle finiteness — round 7 PROVED (Permanent
  Pair Lemma, results/imo-2026-06/lemmas/lemma-permanent-bundle.md, reviewer-
  verified) that some size-2+ bundles are PERMANENTLY unreducible to the
  single-companion base case, not merely hard to reduce. Combined with round
  6's |S|-induction refutation, this is now 2/2 "induct on a syntactic size
  parameter" strategies proven dead — a correct mechanism must NOT be a raw
  size induction of any kind (round 7).
- NEVER re-attempt a "global recruiter set W(a_1)" reformulation (one finite
  set of primes covering every proper core's companions, replacing the
  ≤2^k-2 separate per-core statements) — round 7's global-recruiter-
  finiteness approach proved this is logically EQUIVALENT (same mechanism as
  the already-certified Theorem CD core-decomposition argument: finite union
  of finite per-core sets) to the per-core statement already under direct
  attack, giving zero new leverage; also numerically refuted in its naive
  singleton-only form (a_1=21528751, depth-2 core {103,197}'s permanent
  bundle {11,97} ⊄ {2,3,7}). Do not resurrect any depth/nested variant of
  this idea without first refuting the equivalence proof in
  results/imo-2026-06/approaches/global-recruiter-finiteness.md §3 (round 7).
- NEVER cite "max escape-recursion depth is 2" — this specific empirical
  claim (forced-primes-well-ordering, round 7 builder) was CHECKED and
  FOUND WRONG by the round-7 proof-reviewer: 2 confirmed depth-3
  counterexamples exist (a_1=2747 bucket {17,23,67} at n=19617; a_1=21528751
  bucket {19,41,197} at n=30017). Escape-recursion depth is NOT known to be
  bounded by any constant found so far; treat depth-boundedness itself as
  still fully open, not "probably 2" (round 7).
- ALWAYS have the proof-reviewer independently re-run/extend a builder's own
  numerical search (not just re-verify the reported instances) before
  accepting a "found zero counterexamples up to depth/size K" claim as
  reliable — round 7 caught a false negative-claim exactly this way (see
  escape-depth rule above); spot-checking only the claimed instances would
  have missed it (round 7).
- Round 7's orthogonal-mechanism explorer found NO new top-level escape for
  the 2nd time (after round 5) — two independent thorough searches (round 5:
  6 framings on the whole problem; round 7: crux aimo-0447 + Ramsey-
  extraction on the narrowed multi-companion question) both came up empty.
  Treat a 3rd "hunt for a totally new top-level mechanism" dispatch as low
  expected value unless a future round's narrower findings suggest a
  specific new angle — prefer deepening the two live threads (companion-
  COUNT bounding on persistent-backbone-monovariant; escape-recursion-depth
  bounding, now knowing depth>=3 occurs, on forced-primes-well-ordering)
  (round 7).

### Done (round 7)
- Ran 3 math-explorers in parallel with a split mandate (continue narrowing
  + hunt fresh mechanism): multicompanion-induction (proved bundle-size
  induction dead via Permanent Pair Lemma), cross-bucket-domination (proved
  Escape-Confinement Lemma, found singleton-only W(a_1) pattern), orthogonal-
  mechanism (found no new top-level escape, 2nd confirmation after round 5).
- proof-outliner revised persistent-backbone-monovariant and forced-primes-
  well-ordering, opened new global-recruiter-finiteness (flagging its own
  likely counterexample as mandatory Step 0), left core-depth-induction
  parked with a cross-reference note; all persisted to disk (verified).
- outline-reviewer independently reverified the Step 0 tension from scratch,
  confirmed Hypothesis (GW) as stated is FALSE, cheap-killed it pre-build
  (still gave it a build slot per its own file's honest pivot), build set =
  all 3 slugs.
- 3 proof-builders in parallel: persistent-backbone-monovariant found+closed
  a real self-gap, generalized to Permanent Bundle Lemma (44 fresh instances,
  zero exceptions), pushed freeze simulation to N=5,000,000. forced-primes-
  well-ordering certified Escape-Confinement Lemma, found max-depth-2 claim
  (later shown false by reviewer) and diagnosed the depth mechanism isn't
  independent of the open cross-bucket gap. global-recruiter-finiteness
  proved its own hypothesis family logically equivalent to the already-
  attacked per-core statement — clean dead end, Status unsolved.
- proof-reviewer independently re-derived everything, caught a real error
  (builder's "max depth 2" claim false — 2 confirmed depth-3 instances),
  certified 2 new lemmas (lemma-permanent-bundle, lemma-escape-confinement;
  39 total in lemmas/), verdicts: persistent-backbone-monovariant CHANGES
  REQUESTED, forced-primes-well-ordering CHANGES REQUESTED, global-recruiter-
  finiteness RETHINK. Updated current.md with Round 7 section.
- results/imo-2026-06/current.md Status = partial.

### Broken
(none)

### Next (round 8) [COMPLETED — see round 8 section below]

### Next (round 9)
- **The entire problem now reduces, unconditionally and rigorously, to ONE
  hypothesis: `(UB_S)` for every proper core `S⊊P_1`** — equivalently
  `sup_{n∉I_{P_1}}ω(a_n)<∞` (a restricted, weaker-but-not-easier descendant
  of round 3's abandoned global `ω(a_n)=O(1)`). Proved this round
  (sunflower-bundle-closure's Theorem-UBS-sufficiency,
  lemmas/theorem-UBS-sufficiency.md, reviewer-independently-verified
  line-by-line): `(UB_S)` for every proper core ⟹ the whole problem, via
  already-certified Theorem 5.1/Lemma MS/Theorem V/Theorem CD chain. This
  is the sharpest, most unified single target the population has produced
  across 6 rounds (3-8) — attack `(UB_S)` DIRECTLY as round 9's sole target.
- Known structural fact (sunflower-bundle-closure's own honest §5
  diagnosis, reviewer-confirmed, do not re-derive): all pigeonhole/Δ-system/
  reachability machinery built in rounds 6-8 bounds the COUNT of
  bounded-size companion bundles, never the SIZE of an individual bundle —
  which is exactly what `(UB_S)` needs. A correct mechanism needs a
  genuinely different tool aimed at bundle SIZE, not count. This is a new,
  precise diagnosis of why 3 rounds of count-bounding techniques (Escape-
  Confinement, RBD, S^+, Δ-system) all stall at the same wall — round 9
  should NOT extend any of those count-bounding techniques further hoping
  they eventually bound size; they structurally cannot.
- persistent-backbone-monovariant's narrower NIBC target (its sole
  remaining open gap after this round's cross-approach synergy dissolved
  its witness-existence gap) is PROVEN INSUFFICIENT for the whole problem
  even if closed (only bounds the permanent/(SA)-satisfying share of Λ_S,
  not transient members) — do not treat closing NIBC as equivalent to
  solving the problem; it is a strictly weaker sub-result.
- Numerically, max ω(a_n) off the top core stays single-digit in every
  tested hard case (247→6, 2747→6, 21528751→7, reviewer-reproduced exactly)
  — strong supporting evidence for (UB_S), not a proof.
- This is the 6th consecutive round (3-8) on the FCBC/(MRS)/𝓥_S family. If
  round 9 also fails to move (UB_S) itself with a genuinely new size-
  bounding tool, seriously weigh CLAUDE.md's plateau guidance (a top-level
  approach never tried before) — but note 2 prior dedicated fresh-mechanism
  searches (rounds 5, 7) already found nothing on the WHOLE problem; round
  9's fresh-mechanism search, if triggered in round 10, should be scoped
  specifically to "what bounds the size of an object in a greedy recursive
  construction," not a repeat of the whole-problem sweep.

## Eval History (round 9 addendum)

- Round 9 (post-work): Status = partial. **MAJOR REDIRECT**: `(UB_S)` (round
  8's "sole remaining hypothesis") is now RIGOROUSLY REFUTED in Case II
  (sunflower-bundle-closure's Theorem-UBS-false-Case-II,
  lemmas/theorem-UBS-false-case-II.md, reviewer-independently-verified: fresh
  Turán/Landau second-moment derivation checked exactly at X=2000 by brute
  force, Chebyshev-type bound re-verified numerically to X=2*10^6, non-
  circularity of the Imprint Periodicity Lemma specifically checked). This
  retires the entire (MRS)/𝓥_S/(UB_S)-via-bundle-SIZE program (rounds 4-8)
  as a proven dead end — but does NOT refute FCBC or the whole problem, since
  (UB_S) was only ever proven SUFFICIENT (never necessary) for FCBC. 3
  math-explorers first found the refutation evidence (2 independent fresh
  simulations to n~400,000-1,300,000, ~100-400x past round 8's tested range,
  found omega(a_n) off the top core hits new records (8, not the previously-
  reported 6-7) via a reproducible "primorial-skip-sibling-prime" mechanism,
  zero blocking witness found in 1.3M terms; 3rd explorer exhaustively
  searched knowledge_base.md + full 2434-entry crux corpus, found NO
  transferable size-bounding technique exists — every corpus technique needs
  a fixed external anchor this problem's proper-core bundles provably lack).
  proof-outliner made a key reframing judgment call (verified sound by
  outline-reviewer): re-read the "alarming" numerics as evidence FOR a small
  explicit FCBC covering set, since unbounded bundle size and a small fixed
  covering set H are logically compatible (H only needs to intersect every
  pair, nothing stops extra primes). Built 4-approach field targeting FCBC
  directly via 4 distinct mechanisms; outline-reviewer independently verified
  the reframing, found via its OWN fresh Python a genuine counterexample to
  the literal small-H candidate on the hardest case (a_1=21528751, bridged by
  prime 97) not caught by any explorer, and caught a "wrong quantifier
  direction" bug in sunflower-bundle-closure's Step 3 (o(N) claimed but
  false; weaker (1-c)N form is true and sufficient) BEFORE build. Build set:
  sunflower-bundle-closure, explicit-window-backbone-construction,
  intersecting-family-covering-construction (forced-primes-well-ordering
  deferred as redundant with explicit-window this round, not cut). All 3
  builders ran: sunflower-bundle-closure completed the (UB_S) refutation
  (Case II) end-to-end using the outline-reviewer's corrected Step 3.
  explicit-window-backbone-construction found a strong universal candidate
  H_100:=P_1∪{primes≤100} with zero violations across 11 tested a_1 (incl. 2
  hard cases) but did not close pairwise-sharing (Step 4). intersecting-
  family-covering-construction (top-Elo, holder of gap-free Theorem 5.1)
  proved Theorem SW (Stabilization Sufficiency): FCBC reduces unconditionally
  to the Stabilization Conjecture needed ONLY for "doubly-infinite" disjoint
  core-pairs (every other case disposed of automatically) — tested on 7
  channels across 5 a_1 (incl. adversarial 4199, 4087), zero exceptions in
  ~370M+ checks, but the Stabilization Conjecture itself remains open.
  proof-reviewer independently re-derived/re-simulated all 3 builds from
  scratch (own generators, not builders' scripts), certified 2 new lemmas
  (theorem-UBS-false-case-II, theorem-SW-stabilization-sufficiency; 48 total
  in lemmas/), corrected current.md's round-8 numeric claim (247/2747: 6→8).
  All 3 verdicts: CHANGES REQUESTED (none RETHINK). Elo: intersecting-family-
  covering-construction 1720.5 (top), forced-primes-well-ordering 1616.9,
  persistent-backbone-monovariant 1586.8, explicit-window-backbone-
  construction 1542.9, sunflower-bundle-closure 1499.3 (verified-milestone
  outcome — killed a target, not a partial-progress build), core-depth-
  induction 1457.4 (parked), imprint-automaton-periodicity 1445.9 (parked),
  global-recruiter-finiteness 1436.5 (dead-end), backbone-existence-crt
  1411.5 (parked), bounded-gap-density-covering 1310.7 (parked, dead-end).
  Annotation: BREAKTHROUGH (a 5-round-old target family, chased since round
  4, is now definitively and rigorously killed rather than left to plateau
  indefinitely — exactly the kind of principled redirect CLAUDE.md's
  plateau-break guidance calls for; simultaneously FCBC itself, the actually-
  needed target, is now narrower than ever: Theorem SW reduces it to ONLY
  doubly-infinite core-pairs, and a strong universal-candidate-set empirical
  finding (H_100) gives round 10 a concrete, falsifiable object to attack).

## Rules (round 9 additions)

- THE SOLE REMAINING GAP as of round 9: FCBC itself, attacked directly (not
  via 𝓥_S/(MRS)/(UB_S), now a dead family — see below), narrowed by Theorem
  SW (lemmas/theorem-SW-stabilization-sufficiency.md, reviewer-verified) to
  the **Stabilization Conjecture for doubly-infinite disjoint core-pairs
  only** — every other pair type (same-core, one-finite, top-core-involving)
  is unconditionally disposed of. Round 10 should attack this narrower
  conjecture directly. A complementary concrete empirical lead: the
  universal candidate H_100:=P_1∪{primes≤100} (explicit-window-backbone-
  construction, round 9) has zero violations across 11 tested a_1 (incl.
  a_1=21528751, 9674419) — worth testing as a candidate witness-pool
  generator for Theorem SW's doubly-infinite pairs specifically (round 9).
- NEVER re-attempt to prove (MRS)/𝓥_S-finiteness/(UB_S) (equivalently
  sup{ω(a_n):n∉I_{P_1}}<∞) as a route to FCBC — DEFINITIVELY REFUTED in Case
  II (lemmas/theorem-UBS-false-case-II.md, reviewer-independently-verified:
  fresh Turán/Landau derivation, numeric checks to X=2*10^6, non-circularity
  specifically checked). This retires the ENTIRE target family pursued rounds
  4-8 under 3 successive names ((MRS)→𝓥_S-finiteness→(UB_S)). It does NOT
  refute FCBC or the whole problem — (UB_S) was only ever sufficient, never
  necessary, for FCBC (round 9).
- ALWAYS test "stays single-digit / looks bounded" numeric claims on this
  workspace to n~10^5-10^6 before trusting them, NOT n~3000 — round 9 found
  round 8's "ω(a_n) stays single-digit (max 6-7)" claim was an N-too-small
  artifact; true values are 8, found only past n~400,000, via a reproducible
  "primorial-skip-sibling-prime" growth mechanism. This exact failure mode
  (shallow numeric check → false plateau belief) has now recurred at least 3
  times in this workspace (rounds 2, 5/7 partially, 9 decisively) — treat ANY
  future "checked up to N and it's bounded" claim on this problem as
  unverified until independently pushed at least 100x past the original N
  (round 9).
- NEVER assume a hypothesis being false threatens the approach built on top
  of it without first checking whether that hypothesis was proven necessary
  or merely sufficient — round 9's outliner correctly identified that (UB_S)
  false does not threaten FCBC (sufficient-only relationship), turning an
  apparent crisis into a productive redirect. Always check the exact
  direction of a certified implication (⟹ vs ⟺) before concluding a refuted
  hypothesis kills downstream work (round 9).
- Confirmed again (round 9, 3rd time after rounds 3, 6): exhaustive KB +
  full 2434-entry crux corpus search found NO transferable technique for
  bounding an individual object's SIZE (as opposed to counting objects) in
  this problem's structure — every corpus size-bounding technique requires a
  fixed external anchor (a known input, bounded interval, polynomial
  coefficients) that this problem's proper-core companion bundles provably
  lack. Do not re-dispatch a generic KB/corpus search for size-bounding tools
  again; any future size-bounding argument must be built from scratch, like
  sunflower-bundle-closure's from-scratch Turán/Landau lemma (round 9).
- forced-primes-well-ordering was deferred (not built) round 9 as redundant
  with explicit-window-backbone-construction (same small-prime candidate set,
  same open sub-question) — not a dead-end verdict, just parked; worth
  reviving next round specifically to test whether S^+_S∪{bridge primes}
  (e.g. the round-9-found prime 97) closes its own documented S={1061} gap,
  informed by round 9's bridge-prime-patch findings (round 9).

## State (round 9 addendum)

### Done (round 9)
- Ran 3 math-explorers in parallel (minimality lens, KB/corpus size-tools
  lens, computational-invariant lens) per round 8's "Next" mandate to attack
  (UB_S) with a genuinely new SIZE-bounding tool. All 3 converged: (UB_S) is
  very likely false (2 independent fresh simulations to n~400k-1.3M found
  omega(a_n) hitting new record 8 via "primorial-skip-sibling-prime"
  mechanism, zero blocking witness in 1.3M terms); KB/corpus search found no
  transferable size-bounding tool exists.
- proof-outliner reframed the finding (verified sound by outline-reviewer):
  (UB_S) false doesn't threaten FCBC since (UB_S) was only sufficient, never
  necessary. Built 4-approach field, all attacking FCBC directly: revised
  explicit-window-backbone-construction (small H + bridge primes), revised
  sunflower-bundle-closure (pivot to refuting (UB_S) itself), redirected
  intersecting-family-covering-construction (per-core-pair witness pools),
  revised forced-primes-well-ordering (S^+-seeded patch).
- outline-reviewer independently verified the reframing is sound, found (via
  own fresh Python) a real counterexample to the literal small-H candidate
  on a_1=21528751 (bridged by prime 97) and a wrong-quantifier bug in
  sunflower-bundle-closure's Step 3 before build. Build set: 3 of the 4
  slugs (forced-primes-well-ordering deferred as redundant).
- 3 proof-builders ran in parallel: sunflower-bundle-closure completed a
  rigorous (UB_S) refutation (Case II); explicit-window-backbone-
  construction found universal candidate H_100 empirically (11/11 a_1, no
  proof); intersecting-family-covering-construction proved Theorem SW
  (FCBC reduces to doubly-infinite core-pairs only).
- proof-reviewer independently re-derived/re-simulated all 3 builds from
  scratch, certified 2 new lemmas (48 total), corrected current.md's round-8
  numeric claim, all 3 verdicts CHANGES REQUESTED (none RETHINK).
- results/imo-2026-06/current.md Status = partial.

### Broken
(none)

### Next (round 10) [COMPLETED — see round 10 section below]

## Eval History (round 10 addendum)

- Round 10 (post-work): Status = partial. All 3 math-explorers converged
  with strong POSITIVE evidence for the round-9 target (Theorem SW's
  Stabilization Conjecture): H100-stabilization explorer found ZERO
  coverage violations for H_100:=P_1∪{primes≤100} on doubly-infinite
  channels pushed to unprecedented depth (up to 160M terms), plus a
  striking "shadow saturation" finding (realized-signature count under a
  small fixed watch set {2,3,5,7} freezes exactly, decoupled from the
  (dead) unbounded full-bundle-size question). bridge-primes explorer found
  and verified a new "Smooth-Multiple Recurrence" mechanism explaining why
  bridge primes (e.g. 97 for a_1=21528751) stay bounded rather than
  growing, proposed the "Frozen-Antichain-Union Window Conjecture".
  orthogonal-stabilization explorer confirmed no genuinely different
  top-level mechanism transfers (Landau/Turán tooling from the (UB_S)
  refutation is the wrong shape for an existence-of-covering-set claim) but
  independently corroborated the same positive picture on 2 more adversarial
  cases (a_1=4087, 4199) at 15-25x round-3's depth. proof-outliner built a
  4-slug field, each a structurally distinct mechanism for the SAME target
  (density/pigeonhole magnitude bound; finite-alphabet bitmask family
  argument; well-ordering seeded by Smooth-Multiple Recurrence; retargeted
  Δ-system/sunflower cross-family covering) — correctly judged this is round
  1 of a new target, not yet a plateau requiring forced diversity.
  outline-reviewer independently verified the (MRS)/𝓥_S-refutation Rule does
  NOT block any of the 4 skeletons (none invoke it), independently
  reproduced key numerics, found a NEW pre-build gap in sunflower-
  bundle-closure (Δ-system Dichotomy Lemma's bounded-size hypothesis
  violated by theorem-UBS-false-case-II — flagged as mandatory Step 0,
  build slot kept), deferred explicit-window-backbone-construction as
  offering no new content. Build set: intersecting-family-covering-
  construction, forced-primes-well-ordering, sunflower-bundle-closure. All 3
  builders ran: intersecting-family-covering-construction proved new
  unconditional Lemma RD (Restricted Domination, generalizes Domination
  Lemma to arbitrary index subsets) + Magnitude Bound Corollary, reduced
  further progress to density hypothesis (PD_{S,S'}) (honestly diagnosed as
  hard, with a valid squares/non-squares counterexample to the naive
  inference and a correct circularity catch on reusing the (UB_S)-refutation
  density toolkit). forced-primes-well-ordering (revived from deferred)
  proved Greedy Augmentation + Termination-Sufficiency Lemmas, reduced to a
  First-K-Prefix Recruitment Conjecture. sunflower-bundle-closure fully
  resolved its mandatory Step-0 gap (new Lemma XC/NIDF/FT, proved WITHOUT
  any bounded-size hypothesis — genuinely routes around the flagged
  obstruction), reduced to Conjecture (JW) (does U_S∪U_S' jointly cover?),
  verified on ~74.4M cross pairs (a_1=247) and ~597K (a_1=21528751), zero
  violations. proof-reviewer independently re-derived/re-simulated
  everything from scratch (own generators, not builders' scripts; caught
  one minor arithmetic-labeling slip in sunflower's report, no correctness
  impact), certified 3 new lemmas (51 total), explicitly checked cross-
  approach synergy: **all 3 converge on structurally similar finite
  witness-pool objects but do NOT combine** — confirmed a genuine shared
  mathematical obstruction (same wall, 3 vocabularies: (PD_{S,S'}),
  First-K-Prefix Recruitment, Conjecture (JW)), not coincidental overlap.
  All 3 verdicts: CHANGES REQUESTED (advanced), none RETHINK, none APPROVE.
  Elo: intersecting-family-covering-construction 1746.4 (top),
  forced-primes-well-ordering 1628.8, persistent-backbone-monovariant 1586.8
  (parked), explicit-window-backbone-construction 1504.9 (deferred),
  sunflower-bundle-closure 1499.5, core-depth-induction 1457.4 (parked),
  imprint-automaton-periodicity 1445.9 (parked), global-recruiter-finiteness
  1436.5 (dead-end), backbone-existence-crt 1411.5 (parked),
  bounded-gap-density-covering 1310.7 (parked, dead-end). Annotation:
  IMPROVED (3 genuine new unconditional lemmas, the Stabilization Conjecture
  is now sharpened into 3 precisely-stated sub-questions instead of 1 vague
  one, AND reviewer proved they don't trivially combine — saves round 11
  from chasing a false synergy).

## Rules (round 10 additions)

- THE SOLE REMAINING GAP as of round 10: the Stabilization Conjecture
  (Theorem SW), now attacked from 3 independent non-combining angles, each
  reduced to one sharp open sub-question: `(PD_{S,S'})` (positive density of
  one doubly-infinite class along the other — a genuinely NEW freestanding
  density question, distinct from the retired (UB_S)/Landau-Turán density
  toolkit, which reviewer confirmed cannot be reused here without
  circularity); the First-K-Prefix Recruitment Conjecture
  (forced-primes-well-ordering, bounded provenance of the recruited prime
  set); Conjecture (JW) (sunflower-bundle-closure — does U_S∪U_S' jointly
  cover cross-pairs, verified on ~75M pairs, zero violations, no proof).
  Reviewer recommends round 11 attack Conjecture (JW) directly (sharpest-
  stated, most concrete, strongest numerical support) and/or open a
  dedicated explorer lens on `(PD_{S,S'})` (round 10).
- NEVER assume this round's 3 converging approaches (density magnitude
  bound, well-ordering recruitment, Δ-system cross-covering) can be
  combined to close the Stabilization Conjecture — reviewer explicitly
  checked all 3 pairwise combinations and found each fails for a distinct
  structural reason (index-dependent vs fixed-set mismatch; different
  senses of "intersection"; JW-circularity) — this is the SAME wall in 3
  vocabularies, not 3 complementary partial results (round 10).
- sunflower-bundle-closure's new Lemma XC/NIDF/FT are proved WITHOUT any
  bounded companion-set-size hypothesis (verified by reviewer tracing the
  proof line-by-line) — safe to build on/cite even though companion-bundle
  size is proven unbounded ((UB_S) false, round 9); do not assume these
  lemmas are threatened by that unboundedness (round 10).
- explicit-window-backbone-construction was deferred (not RETHINK) round 10
  as offering no new attack content — its remaining option either
  self-admittedly fails per its own H_100-saturation data or duplicates the
  other 3 approaches' open content verbatim; revive only if a genuinely new
  angle for it is found (round 10).

## Eval History (round 11 addendum)

- Round 11 (post-work): Status = partial. All 3 math-explorers dove into the
  3 non-combining sub-questions from round 10 (Conjecture (JW), (PD_{S,S'}),
  First-K-Prefix Recruitment) and returned with positive numerical evidence
  and sharper reformulations, no counterexamples: (JW) reformulated as
  "trace-clash-freedom" for an explicit small Π (e.g. {2,3,83} for a
  previously-scary a_1=4199 pair); (PD_{S,S'}) confirmed unreachable via the
  retired Landau-Turán toolkit (re-confirmed circular), flat/no-decay
  densities to N=10^6, noted a curiosity of exact-dyadic-looking densities
  for a_1=4087; First-K-Prefix explorer flagged that the blanket "(MRS)/
  V_S-finiteness" ban may be over-applied to a narrower per-core object
  (MRS_S). Outliner independently re-scrutinized this last claim and found a
  correction: (MRS_S) for a SINGLE core is legitimately untouched by the
  round-9 (UB_S) refutation, but (MRS_S)-for-EVERY-core would re-derive the
  whole problem and is therefore equi-hard to the already-abandoned round
  4-8 (MRS)/V-finiteness program (round 6's Multi-Companion Reduction
  Proposition) — outline-reviewer independently re-verified this correction
  from scratch (own Python, found the containment M_n^S ⊇ M_n restricted-to-S
  is strict on 3/6 tested cores) and scoped forced-primes-well-ordering's
  revised outline to ONLY the cores of one doubly-infinite pair, not the
  general claim. Built a 5-approach field (sunflower-bundle-closure revised,
  new copy sunflower-inadmissibility-toolkit, intersecting-family-covering-
  construction revised, forced-primes-well-ordering revised (correctly
  scoped), explicit-window-backbone-construction revised); outline-reviewer
  APPROVEd all 5 outlines, deferred explicit-window as redundant, build set
  = other 4. All 4 builders ran in parallel: sunflower-bundle-closure proved
  new Lemma CB (Core Blocking, cores are automatically non-realized in the
  doubly-infinite setting) and sharpened Π to a single witness-pair per side,
  but Conjecture (JW) still stalls on the same u=w rigidity wall.
  sunflower-inadmissibility-toolkit proved Lemma UCR + Corollary UCR-JW
  (WRP), a genuinely simpler one-shot sufficient criterion for (JW),
  fully closing it on a_1=247's mandatory instance but failing on 875/2929
  indices of the hard a_1=21528751 instance (honestly relocating, not
  closing, the gap). intersecting-family-covering-construction proved Lemma
  CB (Complement Bound, an exact density identity) and Proposition CB-2/
  Corollary CB-3, rigorously showing the "seesaw"/complement-bound mechanism
  gives NO independent leverage on (PD_{S,S'}) — a real negative result, not
  a stall. forced-primes-well-ordering proved the Local No-Resurrection/
  Interval/Equivalence Theorem + Subset Lemma (V_S ⊆ V_S^loc) and a
  No-Shortcut Corollary showing the in-scope core S={103,197} (a_1=21528751)
  is equi-hard to the already-known-hard Multi-Companion hitting-set target
  — confirmed the concrete realized instance {103,197,11,97} at index 862.
  proof-reviewer independently re-derived/re-simulated all 4 builds from
  scratch (own generators), caught and corrected one internal overclaim in
  sunflower-inadmissibility-toolkit's own §3 (already self-retracted in its
  §5, Status stayed honestly partial), certified 4 new lemmas (55 total),
  explicitly checked cross-approach synergy across all 4 — found NONE (each
  pairing confirmed to hit the same wall from a different angle, or a
  different quantifier shape that doesn't transfer). All 4 verdicts:
  CHANGES REQUESTED, none RETHINK, none APPROVE. Elo: intersecting-family-
  covering-construction 1758.9 (top), forced-primes-well-ordering 1630.7,
  persistent-backbone-monovariant 1564.1 (parked), sunflower-bundle-closure
  1539.4, sunflower-inadmissibility-toolkit 1527.5 (new), explicit-window-
  backbone-construction 1497.3 (deferred), core-depth-induction 1443.3
  (parked), imprint-automaton-periodicity 1432.4 (parked), global-recruiter-
  finiteness 1424.0 (dead-end), backbone-existence-crt 1407.7 (parked),
  bounded-gap-density-covering 1302.8 (parked, dead-end). Annotation:
  IMPROVED (4 genuine new certified lemmas, one real negative result closing
  off a mechanism, one honest overclaim caught and corrected before it could
  mislead a future round, and — importantly — a careful independent
  re-scrutiny that avoided both over-banning a legitimately-different local
  claim AND accidentally resurrecting the dead global (MRS)/V-finiteness
  program under a new name).

## Rules (round 11 additions)

- THE SOLE REMAINING GAP as of round 11: still the Stabilization Conjecture
  (Theorem SW), via the same 3 non-combining sub-questions as round 10
  (Conjecture (JW), (PD_{S,S'}), (MRS_S)) — proof-reviewer confirmed round 11
  found NO synergy between any of the 4 built approaches (checked all
  pairings explicitly). Conjecture (JW) is now the recommended sharpest
  target: 2 independent mechanisms this round (fixed-Π trace-clash-freedom;
  Lemma UCR/WRP one-shot criterion) both stall on the identical "u=w
  rigidity wall" (do the shared-prime witnesses from Lemma P′ that arise
  from three overlapping intersection facts get forced equal, or can they
  differ?) — round 12 should seek a THIRD, genuinely different mechanism for
  (JW) specifically, or a dedicated explorer lens on the greedy sequence's
  actual arithmetic behind this rigidity question (round 11).
- NEVER treat (MRS_S) (single fixed core's local minimal-radical antichain
  freeze) as either (a) already banned by the round-9 (UB_S) refutation — it
  is a genuinely different, weaker-in-isolation object (round 11,
  independently confirmed twice: outliner then outline-reviewer, both via
  fresh Python showing M_n^S ⊋ M_n|_S on 3/6 tested cores) — OR (b) an easy
  route to the whole problem — proven this round (No-Shortcut Corollary,
  forced-primes-well-ordering) that (MRS_S)-for-every-core is equi-hard to
  the already-abandoned round 4-8 Multi-Companion/V-finiteness target for
  any core with a known permanent multi-companion bundle (concrete instance
  {103,197,11,97} at index 862, a_1=21528751). Only attack (MRS_S) SCOPED TO
  a single doubly-infinite pair's cores, never generalized to all cores
  (round 11).
- NEVER re-attempt the "seesaw"/Complement-Bound-alone mechanism on
  (PD_{S,S'}) — intersecting-family-covering-construction's Proposition
  CB-2/Corollary CB-3 (lemmas/lemma-complement-bound-and-density-
  equivalence.md, reviewer-verified) proves it only converts the two-sided
  density question to an equivalent one-sided one, giving zero new leverage
  — confirmed by direct computation, not just suspected (round 11).
- This is now the 5th consecutive round (7,8,9 partially via different
  names, 10, 11) that independently-designed mechanisms converge on the
  same "count vs. magnitude, no leverage from current toolkit" pattern
  (round 11's proof-reviewer explicitly flagged this as a 3rd/4th
  observation in yet more vocabularies). Per CLAUDE.md's plateau guidance,
  if round 12 also fails to move any of the 3 sub-questions with a
  genuinely new mechanism, round 13 should seriously consider a dedicated
  fresh top-level explorer search — but scoped specifically to "what forces
  two independently-derived witnesses of the same divisibility fact to
  coincide" (the (JW) rigidity wall's actual shape), not a repeat of the
  whole-problem or whole-(UB_S)-family sweeps already done 3 times (rounds
  5, 7, 9) (round 11).

## State (round 11 addendum)

### Done (round 11)
- Ran 3 math-explorers in parallel, one per round-10-identified sub-question
  (Conjecture (JW), (PD_{S,S'}), First-K-Prefix Recruitment). All returned
  positive/no-counterexample evidence and sharper reformulations.
- proof-outliner caught and corrected a subtle error in the fk-explorer's
  finding before it propagated (see Rules) and built a 5-approach field, all
  persisted to disk.
- outline-reviewer independently re-verified the correction from scratch,
  APPROVEd all 5 outlines, deferred 1 as redundant, build set = 4 slugs.
- 4 proof-builders ran in parallel; all produced genuine new certified-
  quality content (Lemma CB x2 in different approaches, Lemma UCR/Corollary
  UCR-JW, Local Equivalence Theorem + No-Shortcut Corollary) but none closed
  their gap.
- proof-reviewer independently re-derived/re-simulated all 4, caught and
  corrected one overclaim, certified 4 new lemmas (55 total), checked and
  ruled out all cross-approach synergies, updated current.md.
- results/imo-2026-06/current.md Status = partial.

### Broken
(none)

### Next (round 12)
- Attack Conjecture (JW) with a THIRD, genuinely different mechanism (not a
  third cut of the u=w rigidity wall already hit twice this round) — see
  Rules above for the precise open question. A dedicated explorer lens on
  the greedy sequence's arithmetic behind why shared-prime witnesses from
  overlapping intersection facts might/might not coincide is the most
  concrete unexplored angle.
- Do not re-attempt (MRS_S)-for-every-core or the seesaw/Complement-Bound
  mechanism on (PD_{S,S'}) (both proven dead ends this round, see Rules).
- If round 12 also fails to move any of the 3 sub-questions, weigh a
  scoped fresh-mechanism search per the round-11 Rule (not a repeat of the
  3 already-done whole-problem sweeps).

## Eval History (round 12 addendum)

- Round 12 (post-work): Status = partial. 3 math-explorers ran in parallel per
  round 11's mandate to attack Conjecture (JW) with a genuinely third mechanism:
  jw-rigidity explorer refuted round 11's sharpened Π narrowing (explicit
  counterexample a_1=247, i=51/j=739, shared prime 3 ∉ Π) but found a NEW
  "single-side backbone" mechanism (running intersection of one side's
  chronological companion sets) that freezes almost immediately in 5/7 tested
  doubly-infinite core pairs ("Case A"), combining with certified Lemma UCR to
  close (JW) for those pairs in principle; only 2/7 pairs ("Case B": 247:(13,19),
  4199:(13,17)) lack any backbone. pd-density explorer found G_n (coarse P_1-
  projection sequence) is EXACTLY periodic from n=1 in every tractable case
  (KMP-verified, not density-estimated; 247→1806, 2747→2062, 4087→64,
  4199→105250), a genuinely new opening for (PD_{S,S'}) independent of both
  known dead ends; resolved round 11's "dyadic density" curiosity as an artifact
  of a1=4087's small period. mrs-s-scoped explorer pushed core {103,197}
  (a_1=21528751) freeze verification to n=10,000,000 (100x mandate), zero
  further changes, but traced the found "complementary-core pool identity"
  pattern to the ALREADY-KNOWN global antichain freeze equivalence — honestly
  reported as no new leverage, not oversold. Outliner revised all 4 live
  approaches around these findings (sunflower-inadmissibility-toolkit ->
  Backbone Permanence for Case A; sunflower-bundle-closure -> Case B via NIDF-
  pigeonhole; forced-primes-well-ordering -> second Case-A-style mechanism;
  intersecting-family-covering-construction -> G_n-periodicity route to
  (PD_{S,S'})). outline-reviewer independently verified all 4 central claims
  with fresh computation, caught and flagged a real pre-build gap (forced-
  primes-well-ordering's Case B outline was vacuous for 247:(13,19), since Case
  B is defined as "no backbone exists" — redirected to ONLY 4199:(13,17)),
  build set = all 4. All 4 builders ran: sunflower-inadmissibility-toolkit
  claimed Backbone Permanence proven + (JW) closed for Case A (5 instances,
  incl. a_1=2747, 4087 which would fully solve those instances since |P_1|=2
  leaves only one core pair). sunflower-bundle-closure proved Row-Restriction
  Obstruction (why NIDF-pigeonhole can't close Case B in general) + refuted a
  natural "matched-witness" refinement with 2 hand-verified counterexamples
  (247: gcd 5 at a_2/a_5; 4199: gcd 83 at a_9/a_5). forced-primes-well-ordering
  proved a general Sandwich Uniqueness Lemma, used it to unconditionally KILL
  the Realized-Backbone/UCR mechanism for 4199:(13,17) on both possible anchors
  — clean negative result. intersecting-family-covering-construction proved
  Theorem PD-Conditional: G_n eventual periodicity ⟹ (PD_{S,S'}) with explicit
  constants (Lemma BRL-from-Periodicity + Lemma PD-from-BRL), honestly left
  unconditional periodicity itself open (one attempted closure via Lemma W3
  failed, reported not hidden). **proof-reviewer caught a real overclaim**:
  sunflower-inadmissibility-toolkit's "Backbone Permanence proven" claim was
  false — Lemma BS only proves a non-increasing sequence eventually stabilizes
  at SOME point, not that a finitely-checked prefix (2-4 matching terms) has
  already reached it; the pre-build outline-reviewer had already correctly
  flagged this as open and the build regressed past that correct assessment.
  This means a_1=2747 and a_1=4087 (which the false claim would have fully
  solved, per Theorem SW's exhaustive case split with |P_1|=2) remain open, NOT
  solved. Reviewer certified corrected Lemma BS/Theorem CAC (scope-corrected)
  and the Sandwich Uniqueness Lemma (58 lemmas total). All 4 verdicts: CHANGES
  REQUESTED, none RETHINK, none APPROVE. Elo: intersecting-family-covering-
  construction 1751.0 (top), forced-primes-well-ordering 1596.2,
  sunflower-inadmissibility-toolkit 1589.8, sunflower-bundle-closure 1554.0,
  persistent-backbone-monovariant 1548.9 (parked), explicit-window-backbone-
  construction 1497.3 (parked), core-depth-induction 1443.3 (parked),
  imprint-automaton-periodicity 1432.4 (parked), global-recruiter-finiteness
  1413.3 (dead-end), backbone-existence-crt 1399.0 (parked),
  bounded-gap-density-covering 1302.8 (parked, dead-end). Annotation: IMPROVED
  (2 genuinely new mechanisms opened — single-side backbone for (JW), G_n exact
  periodicity for (PD_{S,S'}) — with real certified content on both, PLUS a
  caught overclaim that prevented a false "solved" status from propagating;
  this is the 6th consecutive round on the Stabilization Conjecture family but
  round 12 broke real new ground rather than just re-cutting the same wall).

## Rules (round 12 additions)

- THE SOLE REMAINING GAP as of round 12: still the Stabilization Conjecture
  (Theorem SW), now via 4 live threads: (a) Backbone Permanence for Conjecture
  (JW) Case A — Lemma BS PROVES eventual stabilization exists but NOT that any
  specific tested prefix has reached it; closing (JW) for the 5 claimed Case A
  instances (incl. a_1=2747, 4087, which are otherwise fully solvable via
  |P_1|=2) needs an explicit stabilization-INDEX bound, not just existence; (b)
  Case B of (JW) (247:(13,19), 4199:(13,17)) — Row-Restriction Obstruction shows
  why the natural pigeonhole technique can't work; Sandwich Uniqueness killed
  the Realized-Backbone/UCR route unconditionally for 4199:(13,17); both pairs
  need a genuinely different mechanism; (c) (PD_{S,S'}) — reduces cleanly
  (Theorem PD-Conditional) to unconditional G_n eventual-periodicity, itself
  still open (one closure attempt via Lemma W3 failed: |M_n| provably
  unbounded); (d) a_1=21528751 (hardest case) showed no detectable G_n period
  within N=400,000 — periodicity itself unconfirmed there, a concrete numerical
  target (round 12).
- NEVER cite "Backbone Permanence is proven" or treat a_1=2747/4087 as solved
  based on sunflower-inadmissibility-toolkit's round-12 build — Lemma BS only
  proves a non-increasing subset sequence eventually stabilizes at SOME finite
  point, which is a much weaker existence fact than "the 2-4 matching terms
  already checked constitute the stabilization point." The proof-reviewer
  caught this exact overclaim and scope-corrected the certified lemma
  (lemmas/lemma-BS-backbone-stabilization-and-theorem-CAC.md) — read the
  corrected scope, not the original builder claim, before reusing (round 12).
- ALWAYS distinguish "a monovariant/sequence eventually stabilizes" (existence,
  usually easy) from "a specific finite prefix has already reached the
  stabilization point" (needs an explicit bound or a separate argument) when a
  builder proposes to certify permanence/freezing from finite numerical
  matching — this exact conflation caused a false "solved" claim to almost
  propagate in round 12; the pre-build outline-reviewer had flagged it
  correctly but the build regressed past that flag, so ALSO always re-check
  whether a builder's final claim matches or exceeds what its own outline-
  reviewer already scoped as open (round 12).
- NEVER re-attempt the Realized-Backbone/UCR mechanism for a_1=4199's pair
  (13,17) on either the {13}-side or {17}-side anchor — Sandwich Uniqueness
  Lemma (lemmas/lemma-sandwich-uniqueness.md, reviewer-certified) proves both
  anchors unconditionally fail (B_full({17})=∅ directly; B_full({13}) dichotomy
  resolved false via already-certified Lemma ERD-C). A different mechanism is
  needed for this specific pair (round 12).
- NEVER re-attempt the "matched one-sided covering set" refinement for (JW)
  Case B (guessing {2,3}={2,3} as a shared covering set from Lemma CB +
  Escape-Confinement with smarter witness selection) — sunflower-bundle-
  closure's round-12 build found and refuted this with 2 independently-
  verified hand counterexamples (247: a_2=260 vs a_5=285, gcd 5 not in the
  guessed set; 4199: a_9=4316 vs a_5=4233, gcd 83 not in the guessed set)
  (round 12).
- NEVER re-attempt closing G_n eventual-periodicity unconditionally via Lemma
  W3's minimal-radical-antichain compression — intersecting-family-covering-
  construction's round-12 build tried this and found it fails for a documented
  reason: |M_n| (the antichain size) is provably unbounded, so it cannot serve
  as a finite-state compression witnessing periodicity (round 12).

## State (round 12 addendum)

### Done (round 12)
- Ran 3 math-explorers in parallel (jw-rigidity, pd-density, mrs-s-scoped) per
  round 11's mandate — see Eval History for findings (backbone mechanism found,
  G_n exact periodicity found, mrs-s-scoped honest negative).
- proof-outliner revised all 4 live approaches around the 2 new findings; all
  persisted to disk (verified).
- outline-reviewer independently verified all 4 central claims with fresh
  computation, caught and fixed a real pre-build vacuity gap in forced-primes-
  well-ordering's Case B scoping, build set = all 4 slugs.
- 4 proof-builders ran in parallel — see Eval History for what each produced.
- proof-reviewer independently re-derived/re-simulated all 4 builds from
  scratch, caught and corrected a real overclaim (sunflower-inadmissibility-
  toolkit's "Backbone Permanence proven" was false), certified 2 new lemmas
  (58 total: lemma-BS-backbone-stabilization-and-theorem-CAC (scope-corrected),
  lemma-sandwich-uniqueness), all 4 verdicts CHANGES REQUESTED (none RETHINK,
  none APPROVE), updated current.md.
- results/imo-2026-06/current.md Status = partial.

### Broken
(none)

### Next (round 13)
- **4 live threads, attack whichever has the most concrete next step:**
  (a) Find an EXPLICIT stabilization-index bound for Backbone Permanence
  (Case A of (JW)) — Lemma BS only proves eventual stabilization exists;
  closing this for a_1=2747/4087 (which would fully solve those instances,
  |P_1|=2) needs either an explicit bound or a different argument that the
  already-checked prefix suffices. This is the highest-value target: it's the
  closest thing to an actual solved instance this workspace has produced.
  (b) Case B of (JW) (247:(13,19), 4199:(13,17)) needs a genuinely different
  mechanism — Row-Restriction Obstruction explains why pigeonhole-on-escape-
  primes can't work; Sandwich Uniqueness killed Realized-Backbone/UCR for
  4199:(13,17). Neither dead end should be re-attempted (see Rules).
  (c) G_n eventual-periodicity itself (needed for Theorem PD-Conditional to
  unconditionally give (PD_{S,S'})) — Lemma W3 compression is proven not to
  work (|M_n| unbounded); a genuinely different periodicity-proving technique
  is needed. Concrete numerical target: push a_1=21528751 past N=400,000 to
  find/confirm its G_n period (or find it's NOT periodic, which would be a
  major finding).
  (d) mrs-s-scoped line is now confirmed to offer no further leverage — do not
  revive without a new idea distinct from the already-known global antichain
  equivalence.
- Given 6 consecutive rounds (7-12) on the Stabilization Conjecture family,
  weigh CLAUDE.md's plateau guidance if round 13 also fails to close any
  thread outright — but round 12 opened 2 genuinely new mechanisms (backbone,
  G_n-periodicity) with real certified content, so this is not a flat plateau;
  prefer deepening (a) (the explicit-bound gap) as the single sharpest,
  most concrete target before considering a fresh top-level search.
- ALWAYS re-verify a builder's final claim against what its own outline-
  reviewer already scoped as open before accepting it (see new Rule) — this
  applies especially to any future "permanence/stabilization from finite
  numerical matching" claim.

## Eval History (round 13 addendum)

- Round 13 (post-work): Status = partial, but **MILESTONE: a_1=247 is now a
  fully, unconditionally SOLVED concrete instance of the whole IMO problem**
  (first solved instance in 13 rounds) — forced-primes-well-ordering's
  Theorem FW2 (W={2,3,5,7} covers Case-B pair 247:(13,19) via the new
  low-index-witness-chaining mechanism) combined with already-certified
  Theorem SW + Theorem 5.1 gives explicit H={2,3,5,7,13,19}, L=51870,
  reviewer-independently-verified after maximal adversarial scrutiny
  (re-derived Lemma WF from Lemma P'+XC from scratch, re-verified all 10
  witness factorizations via sympy, re-simulated to N=400,000, zero
  violations). This is NOT a solve of the general problem (which needs every
  a_1) — current.md Status correctly stays partial with this caveat stated
  explicitly. 3 math-explorers ran in parallel on round 12's 3 open threads:
  explicit-bound (pushed a_1=2747/4087 backbone tracking to N=10-20M, zero
  shrink events, found "Early/Bounded Stabilization" sub-conjecture
  candidate), case-b (found the new low-index-witness-chaining mechanism,
  singleton witness a_12=4352 for 4199:(13,17)), gn-periodicity (pushed
  a_1=21528751 to N=25M, found implied period ~10^10-10^11 infeasible to
  verify numerically; also surfaced a global-antichain finding later
  rejected — see below). proof-outliner built 5-slug field incl. new
  core-antichain-content-freeze (global 𝓥_S-finiteness, flagged by outliner
  itself as "needs verification"). outline-reviewer independently traced the
  full lemma chain and CHEAP-KILLED core-antichain-content-freeze pre-build
  (RETHINK, not registered) — proved it's equi-hard to FCBC, not weaker, via
  already-certified Multi-Companion Reduction Proposition + No-Shortcut
  Corollary (a fact already recorded as a standing rule in a sibling
  approach's own file that the outliner missed). Build set: 4 existing
  approaches. All 4 builders ran: sunflower-inadmissibility-toolkit
  rigorously REFUTED its own outline's EBS conjecture (3 counterexamples,
  incl. a 108-consecutive-member plateau that later breaks) — clean honest
  negative result, reviewer-reproduced exactly. forced-primes-well-ordering
  proved Theorem FW1 (4199:(13,17) covered by {2,3,83}) and Theorem FW2 (the
  247 milestone above). sunflower-bundle-closure proved general Chaining
  Sufficiency Theorem + Single-Witness-Per-Side Insufficiency Proposition,
  honestly corrected the outline's "WCE possibly easier" framing (proved
  WCE⟹JW, not easier). intersecting-family-covering-construction proved
  Lemma WO (window occupancy, CRT count) + Proposition BI (backbone
  permanence doesn't force class revisitation, rules out that route to BRL).
  proof-reviewer independently re-derived/re-simulated everything from
  scratch, certified 4 new lemmas (61 total), all 4 verdicts CHANGES
  REQUESTED (none RETHINK, none APPROVE beyond the 247 sub-instance). Elo:
  intersecting-family-covering-construction 1750.5 (top), forced-primes-
  well-ordering 1631.1, sunflower-inadmissibility-toolkit 1590.0,
  sunflower-bundle-closure 1560.9, persistent-backbone-monovariant 1518.6
  (parked), explicit-window-backbone-construction 1497.3 (parked),
  core-depth-induction 1443.3 (parked), imprint-automaton-periodicity 1432.4
  (parked), global-recruiter-finiteness 1402.0 (dead-end), backbone-
  existence-crt 1399.0 (parked), bounded-gap-density-covering 1302.8
  (parked, dead-end). Annotation: BREAKTHROUGH (first solved concrete
  instance of the problem in 13 rounds, PLUS a clean pre-build kill of a
  risky resurrection attempt that could have wasted a build cycle, PLUS a
  clean refutation closing off the EBS sub-conjecture so round 14 doesn't
  chase it further).

## Rules (round 13 additions)

- THE SOLE REMAINING GAP as of round 13: general FCBC / Conjecture (JW) for
  arbitrary a_1, now via the low-index-witness-chaining mechanism (Lemma
  WF/Theorem FW1/FW2, certified round 13) as the most concrete tool —
  closed the concrete pairs 4199:(13,17) and 247:(13,19); 4199 still has
  other open channels (its own core pairs beyond (13,17)) so a_1=4199 is
  NOT yet solved even though a_1=247 is. Round 14 should extend the
  witness-chaining mechanism to more Case-B-style pairs and/or attack the
  general Conjecture (WCE) that sunflower-bundle-closure formalized
  (WCE⟹JW proved, but WCE itself open) as the sharpest remaining target
  (round 13).
- NEVER cite a_1=247 as evidence the GENERAL problem is solved — only one
  concrete instance is closed (Theorem FW2 + Theorem SW + Theorem 5.1
  chain, |P_1|=2 case with a single disjoint core pair). The general
  problem (every a_1) remains open; current.md Status is correctly partial
  (round 13).
- NEVER re-attempt the "two-in-a-row locks it" / Early-Bounded-Stabilization
  mechanism for Backbone Permanence (Case A of (JW)) — round 13's
  sunflower-inadmissibility-toolkit rigorously refuted it with 3
  counterexamples (a_1=375; a_1=4199 core {13,19}, 24-member plateau then
  breaks; a_1=4199 core {17,19}, 108-member plateau then breaks), reviewer-
  reproduced exactly. No finite computational check can certify permanence
  via this route — a_1=2747/4087's backbone status remains genuinely open,
  not just unverified (round 13).
- NEVER re-attempt "global 𝓥_S-finiteness (Hypothesis (MRS)) is a provably
  WEAKER target than the local 𝓥_S^loc apparatus" — outline-reviewer proved
  (round 13, via already-certified Multi-Companion Reduction Proposition +
  No-Shortcut Corollary) this is EQUI-HARD to FCBC for any core with a
  realized multi-companion bundle (concrete instance: a_1=21528751,
  S={103,197}, Q={11,97}), not a bypass. This was independently flagged by
  a math-explorer, built into a full outline by the proof-outliner, and
  only caught by the outline-reviewer BEFORE build — a reminder that
  "provably weaker via a certified Subset Lemma" claims still need a full
  corpus grep (all lemmas/ + all sibling approaches/ files) for the exact
  target's name before being trusted, not just a check against the most
  famous prior refutation ((UB_S), round 9) (round 13).
- ALWAYS grep the full lemmas/ + approaches/ corpus for a target's exact
  name (not just the outline's own cited blockers) before approving a
  "provably weaker/easier target" claim — round 13's outline-reviewer added
  this as a standing check after catching core-antichain-content-freeze's
  missed cross-reference to a rule already recorded in a sibling approach's
  own file (round 13).
- Do NOT re-attempt Lemma W3 antichain-compression, the rejected global-
  antichain shortcut, or further N-pushing on a_1=21528751's G_n period
  (implied ~10^10-10^11, infeasible) as routes to G_n eventual-periodicity
  — all 3 confirmed unproductive as of round 13; intersecting-family-
  covering-construction's new Lemma WO/Proposition BI redirect toward a
  minimality-sensitive argument instead of feasibility/pigeonhole tools
  (round 13).

## State (round 13 addendum)

### Done (round 13)
- Ran 3 math-explorers in parallel (explicit-bound, case-b, gn-periodicity)
  per round 12's 3-thread mandate — see Eval History for findings.
- proof-outliner built 5-slug field (4 revised/advanced + 1 new, the new one
  self-flagged as needing verification); all persisted to disk.
- outline-reviewer independently traced the full lemma chain, cheap-killed
  the new approach pre-build (RETHINK, equi-hard not weaker), APPROVEd the
  other 4, build set = 4 existing approaches.
- 4 proof-builders ran in parallel — see Eval History for what each
  produced (1 clean refutation, 1 milestone solved-instance result, 1
  general-conjecture formalization + honest non-closure, 1 new lemma pair).
- proof-reviewer independently re-derived/re-simulated all 4 builds from
  scratch, gave the milestone claim maximal adversarial scrutiny before
  confirming it, certified 4 new lemmas (61 total), all 4 verdicts CHANGES
  REQUESTED (none RETHINK, none APPROVE beyond the 247 sub-instance).
- results/imo-2026-06/current.md Status = partial (with a_1=247 flagged as
  a solved concrete instance — first in the workspace's history).

### Broken
(none)

### Next (round 14)
- Extend the low-index-witness-chaining mechanism (Lemma WF, certified
  round 13) to more concrete Case-B-style pairs, and/or attack the general
  Conjecture (WCE) (sunflower-bundle-closure, round 13: WCE⟹JW proved, WCE
  itself open) as the sharpest remaining target — this is the most concrete
  unexplored angle with a working proof template already in hand (Theorem
  FW1/FW2's case-split method).
- a_1=4199 has other open core-pair channels beyond (13,17) — closing those
  too would give a second solved concrete instance; worth a dedicated
  explorer lens if round 14 wants a second milestone.
- Do NOT re-attempt: Early/Bounded Stabilization for Backbone Permanence
  (refuted, see Rules), global 𝓥_S-finiteness as a "weaker target" (refuted
  equi-hard, see Rules), Lemma W3 compression or further N-pushing on
  a_1=21528751 for G_n-periodicity (see Rules).
- This is round 7 of the Stabilization Conjecture family (7-13), but round
  13 produced the first solved concrete instance — treat this as continued
  real progress, not a plateau; no fresh top-level search needed yet.

## Eval History (round 14 addendum)

- Round 14 (post-work): Status = partial, but **BREAKTHROUGH: workspace now
  has 5 fully solved concrete instances** (15, 247, 4199, 2747, 4087) plus a
  new general Corollary (MSF) that closed an extra channel of the workspace's
  hardest recurring test case (a_1=21528751, core pair {103}/{197}). 3
  math-explorers ran in parallel per round 13's mandate (WCE-general,
  4199-remaining-channels, Case-A-alternative) and ALL THREE independently
  converged on the same generalization of certified Lemma WF (Witness
  Forcing): wce-general found "Multi-Singleton Forcing" closes 10/10 fresh
  Case-B pairs tested incl. a_1=2747/4087; 4199-channels explorer derived
  closures for all 5 remaining open core-pair channels of a_1=4199;
  case-a-alt explorer found Lemma WF is NOT gated by the Case-A/Case-B
  classification and used "Singleton-Chain Closure" to close a_1=2747/4087
  directly, bypassing the still-open Backbone Permanence route entirely.
  proof-outliner built a 4-slug field: forced-primes-well-ordering (a_1=4199
  full 6-channel closure), sunflower-inadmissibility-toolkit (a_1=2747/4087
  closures via new Lemma SCF), new witness-chaining-universal-existence
  (general Corollary MSF + honest attempt at a Small-Companion Existence
  Lemma, left open), intersecting-family-covering-construction (kept as
  structurally independent density/minimality route for diversity).
  outline-reviewer found the SAME process gap as round 1 (outline not
  persisted to disk) and fixed it by pointing builders at
  /tmp/round-14/proof-outliner.md; independently re-verified all 4 outline
  claims including the a_1=4199 witness-scoping fix; build set = all 4.
  All 4 builders ran: forced-primes-well-ordering proved a_1=4199 second
  solved instance (H={2,3,13,17,19,83}, L=2,091,102; builder itself found a
  genuine simplification — a_82 is redundant, only 6 witnesses needed not
  7). sunflower-inadmissibility-toolkit proved Lemma SCF (Singleton-Chain
  Forcing) and closed a_1=2747 (H={2,3,7,41,67}, L=115374) and a_1=4087
  (H={2,61,67}, L=8174) as 3rd/4th solved instances. witness-chaining-
  universal-existence proved Corollary MSF as a GENERAL theorem (valid for
  arbitrary a_1/core pair, corollary of certified Chaining Sufficiency
  Theorem), used it to close a NEW channel of a_1=21528751's {103}/{197}
  pair (this workspace's longest-standing hardest test case, flagged rounds
  6-11), and honestly left the harder "Small-Companion Existence Lemma"
  general conjecture open (found negative numerical evidence, proposed
  replacement "Bounded Forced-Set Existence" conjecture). intersecting-
  family-covering-construction proved Theorem MO (Minimality Obstruction):
  bounded-modulus/CRT minimality selection cannot resolve BRL(S')/
  G-periodicity — reviewer confirmed the individual lemmas but scope-
  corrected an overclaim ("entire technique family" -> only 2 extreme
  cases proven, not fully general). proof-reviewer independently re-derived
  and re-verified ALL 4 builds from scratch (fresh generators, sympy
  factorizations, hand-traced case splits) under maximal scrutiny per the
  round-12 overclaim-history rule; confirmed all claims sound (with the one
  intersecting-family-covering-construction scope correction); certified 4
  new lemmas (65 total); all 4 verdicts CHANGES REQUESTED, none RETHINK,
  general theorem correctly NOT claimed solved. Explicitly checked and
  rejected the temptation to conflate 5 solved instances with the general
  problem being close. Annotation: BREAKTHROUGH (3 independent explorers
  converging on the same powerful generalization in one round, then 4
  builders successfully harvesting it into 4 new solved instances/channels
  plus one new general corollary, all independently re-verified with zero
  errors found beyond one scope correction — the single most productive
  round in this workspace's 14-round history by instance count).

## Rules (round 14 additions)

- THE SOLE REMAINING GAP as of round 14: the GENERAL Stabilization
  Conjecture / Conjecture (JW) / (WCE) for ARBITRARY a_1 — now via the
  certified Corollary MSF (Multi-Singleton Forcing,
  lemmas/corollary-MSF-multi-singleton-forcing.md) as the sharpest general
  tool, but its applicability to EVERY disjoint core pair (the "Small-
  Companion Existence" / "Bounded Forced-Set Existence" question — does
  every core pair admit enough low-index small-companion witnesses?) is
  NOT proven and has genuine negative numerical evidence at a_1=21528751,
  class S={197} (509+ members tested, zero small-companion witnesses,
  no downward trend). Round 15 should attack this existence question
  directly — it is now the single sharpest remaining open fact standing
  between the workspace's 5 solved instances and a general proof (round 14).
- ALWAYS re-verify a builder's numerical "witness redundancy" or
  "simplification" self-claim (e.g. "witness a_82 turned out unnecessary")
  independently before trusting it in a certified lemma — round 14's
  reviewer confirmed forced-primes-well-ordering's self-caught
  simplification was correct, but this is exactly the kind of self-report
  the round-12 overclaim taught this workspace not to trust blindly (round
  14).
- NEVER let a large batch of solved-instance results (this round: 5 total)
  create pressure to approve a general theorem claim without full
  independent re-proof — round 14's reviewer explicitly flagged and
  rejected this temptation; the general problem's status is determined
  solely by whether Corollary MSF (or a successor) is proven to apply to
  EVERY a_1/core pair, not by how many instances have been individually
  closed (round 14).
- NEVER treat "Corollary MSF closes many/most tested instances" as
  evidence the Small-Companion/Bounded-Forced-Set existence question is
  true in general — round 14 found a specific counter-signal (a_1=21528751,
  S={197}) that should be taken seriously, not explained away, when round
  15 attacks this gap (round 14).
- NEVER re-attempt closing BRL(S')/G-periodicity via bounded-modulus/CRT
  minimality selection (single-modulus OR companion-enriched-modulus
  variants) — Theorem MO + Proposition MO-2
  (lemmas/theorem-MO-minimality-obstruction.md, reviewer-scope-corrected)
  prove this impossible for the two extreme cases tested (raw CRT window,
  and enrichment that collapses to either the full Stabilization
  Conjecture or already-certified Lemma WF machinery); do not cite this as
  ruling out "an entire technique family" (reviewer-corrected overclaim) —
  only these two specific mechanisms are ruled out (round 14).

## State (round 14 addendum)

### Done (round 14)
- Ran 3 math-explorers in parallel (wce-general, 4199-channels, case-a-alt)
  per round 13's 3-thread mandate — all 3 independently converged on the
  same generalization of certified Lemma WF (see Eval History).
- proof-outliner built a 4-slug field (3 advanced/revised, 1 new); did NOT
  persist outline content to results/imo-2026-06/approaches/ (same gap as
  round 1 — see standing Rule above about always checking this).
- outline-reviewer caught the persistence gap, independently re-verified
  all 4 outline claims from scratch, pointed builders at
  /tmp/round-14/proof-outliner.md, build set = all 4 slugs.
- 4 proof-builders ran in parallel, each pointed explicitly at the
  outliner's tmp report — all 4 produced genuine new certified-quality
  content (see Eval History): 2 new solved instances + 1 new solved channel
  of the hardest case + 1 general corollary + 1 scope-corrected
  impossibility theorem.
- proof-reviewer independently re-derived/re-simulated all 4 builds from
  scratch under maximal scrutiny, certified 4 new lemmas (65 total),
  scope-corrected one overclaim, all 4 verdicts CHANGES REQUESTED (none
  RETHINK, none APPROVE for the general theorem), rewrote current.md.
- results/imo-2026-06/current.md Status = partial (5 solved instances:
  15, 247, 4199, 2747, 4087; general problem remains open).

### Broken
(none)

### Next (round 15)
- **Single sharpest target**: prove or refute whether Corollary MSF
  (or a successor mechanism) applies to EVERY disjoint core pair for
  EVERY a_1 — i.e. resolve the "Small-Companion Existence" / "Bounded
  Forced-Set Existence" open conjecture (see Rules). This is now THE gap
  standing between 5 solved instances and a general proof.
- Take the a_1=21528751/S={197} negative numerical evidence seriously —
  round 15's explorer(s) should investigate WHY this class resists (is
  there a structural reason some cores never get small-companion
  witnesses, requiring a genuinely different mechanism for those, or is it
  just a slow-converging case that eventually gets one)?
- Do NOT re-attempt: bounded-modulus/CRT minimality selection for
  BRL(S')/G-periodicity (Theorem MO, see Rules); Early/Bounded
  Stabilization for Backbone Permanence (refuted round 13, now also
  superseded — Case A pairs 2747/4087 are solved via Singleton-Chain
  Closure instead, so Backbone Permanence itself is no longer even needed
  for those instances).
- Consider whether a dedicated approach should now attempt: "does every
  a_1 eventually produce a solved instance via the MSF/SCF toolkit" as a
  literal general-existence proof target, formalizing what's currently
  spread across 3 approaches (forced-primes-well-ordering,
  sunflower-inadmissibility-toolkit, witness-chaining-universal-existence)
  into one unified general theorem attempt.

## Eval History (round 15 — TERMINAL)

- Round 15 (post-work): **Status = SOLVED. The general problem (imo-2026-06,
  IMO 2026 P6) is fully proved for every a_1>1.** 3 math-explorers ran in
  parallel per round 14's mandate (structural-obstruction, alternative-
  mechanism, general-unification), and ALL THREE independently converged on
  a decisive crux-corpus discovery: `aimo-0030` (IMO Shortlist 2013 N5, "Ana
  and Banana") has a recursive rule VERBATIM IDENTICAL to imo-2026-06's own
  rule, and its official solution's similarity-dichotomy (same small-prime
  signature mod P=prod_{p<=a_1}p => same term/non-term status) plus a mod-P
  CRT-periodicity corollary gives an explicit (T,L) for the ENTIRE general
  conclusion, bypassing all 14 rounds of FCBC/(JW)/(WCE)/Corollary-MSF
  apparatus. proof-outliner opened new approach
  `similarity-dichotomy-crux-adaptation` (primary target) plus kept 2 other
  approaches live for diversity/insurance (forced-primes-well-ordering:
  Common-Recruiter Reuse; intersecting-family-covering-construction:
  intermediate-mechanism negative result). outline-reviewer independently
  re-verified the crux match from the raw JSON, traced Claim 1's proof,
  found and closed a silently-missing bridge lemma ("IN/OUT recursive
  characterization"), numerically spot-checked on 3 fresh a_1 (65,77,91),
  caught a wording bug in the outline's own sanity check (T=8008,L=30030 for
  a_1=15, a valid 1001x multiple of certified minimal L=30, not literally
  T=8,L=30), build set = all 3. proof-builder for
  similarity-dichotomy-crux-adaptation produced a complete proof: Lemma REC
  (bridge), Claim 1 (via certified Corollary P''), Claims 2/3 (re-derived
  from scratch, not game framing), Main Dichotomy Theorem (both
  minimal-counterexample cases p<=k/p>k), and an exact periodicity corollary
  (T = #good residues mod P, L=P, a_{n+T}=a_n+L for EVERY n>=1). Other 2
  builders: forced-primes-well-ordering formalized Corollary CRR, closed 4
  more channels of a_1=21528751 (5/6 total, 6th genuinely isolated as open);
  intersecting-family-covering-construction proved Theorem EI, a clean
  negative result ruling out the last untested intermediate mechanism in the
  bounded-modulus/CRT family. **proof-reviewer applied maximum adversarial
  scrutiny** (per this workspace's 14-round history of catching overclaims):
  independently re-derived every step from scratch with fresh Python (not
  the builder's scripts), cross-checked aimo-0030 against
  past_problems_database.json directly, ran an exhaustive (not sampled)
  small-prime-signature-vs-term-status scan on all 5 of this workspace's
  hardest historical test cases including a_1=21528751 (169,436 consecutive
  integers, zero violations), tested 8 NEW a_1 values not used by the
  builder (incl. edge cases a_1=2,3), found exactly ONE gap — a cosmetic
  one-line domain-hypothesis omission, true and trivially derivable from
  facts already on the page — patched it into the certified writeup rather
  than downgrading. Verdict: similarity-dichotomy-crux-adaptation APPROVE
  (Status: solved); other 2 builds CHANGES REQUESTED (correct, honestly
  scoped, now superseded in importance). current.md rewritten with the full
  self-contained proof; 3 new lemmas certified (68 total: lemma-REC,
  theorem-similarity-dichotomy, theorem-periodicity-from-dichotomy).
  Annotation: **BREAKTHROUGH — TERMINAL.** The 14-round FCBC apparatus
  remains valid, certified, independently interesting content about finer
  structure (minimal T,L, minimal covering set H) that the problem's literal
  statement does not require — it was simply not the shortest path to the
  problem as stated. This closes the run's Goal.

## Rules (round 15 additions)

- TERMINAL: imo-2026-06 (IMO 2026 P6) is SOLVED as of round 15. Do not
  re-attempt or re-open this problem in future rounds of this run. If this
  run continues (e.g. user requests refinement), the only legitimate further
  work is: (a) sharpening the proof for minimality of T,L, (b) fully
  formalizing/cleaning the write-up, or (c) a NEW problem if the user
  redirects the Goal. The general problem itself needs no further proof
  work (round 15).
- The winning technique was a crux-corpus adaptation (aimo-0030, IMO-SL 2013
  N5), found only after 14 rounds of deep independent work on a much harder
  reduction (FCBC/(MRS)/Corollary-MSF) — that apparatus was real, correct,
  and richer than what the problem needed, not wasted effort, but it was not
  the shortest path. Lesson for future runs: keep at least one explorer
  lens per round dedicated to a fresh crux-corpus sweep of the ORIGINAL
  problem statement even after many rounds of deep progress on a derived
  sub-question — round 15's 3 explorers all independently found the same
  crux only when explicitly re-scouting broadly, not by continuing to
  narrow the existing gap (round 15).

## State (round 15 addendum)

### Done (round 15)
- Ran 3 math-explorers in parallel (structural-obstruction,
  alternative-mechanism, general-unification) per round 14's mandate; all 3
  independently surfaced crux aimo-0030 as a likely complete-proof route.
- proof-outliner opened similarity-dichotomy-crux-adaptation (primary) and
  advanced 3 other approaches for diversity; all persisted to disk.
- outline-reviewer independently verified the crux match, patched a missing
  bridge lemma, caught a wording bug, build set = 3 slugs.
- 3 proof-builders ran in parallel: similarity-dichotomy-crux-adaptation
  produced a complete general proof; forced-primes-well-ordering closed 4
  more channels of a_1=21528751; intersecting-family-covering-construction
  proved a clean negative result (Theorem EI).
- proof-reviewer applied maximum adversarial scrutiny, independently
  re-derived and re-verified everything from scratch, found and patched one
  cosmetic gap, APPROVED similarity-dichotomy-crux-adaptation (Status:
  solved), certified 3 new lemmas (68 total), CHANGES REQUESTED for the
  other 2 builds (correct but superseded).
- results/imo-2026-06/current.md Status = SOLVED. Goal achieved.

### Broken
(none)

### Next
- Run complete. imo-2026-06 is solved. If continued: only minimality/
  write-up polish work remains, or a new problem if redirected.
