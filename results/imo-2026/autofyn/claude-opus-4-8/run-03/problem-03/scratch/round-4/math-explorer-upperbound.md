## imo-2026-03 — upper-bound framing scout (far from match/bisect-DP and min-pairing)

**Target.** Prove: for every multiset A (sum 1, ≤ n+1 parts), XY has a ≤n-cut refinement B with
S(B) ≤ 1/D_n, D_n = 2^{n+1}−1. Equivalently (L2/L3/L4) max_A min_B S(B) = 1/D_n from above.
Both the induction-peel branch-inequality route (Open gap 2) and the min-pairing/amortized-
charging witness route (G2 in alternating-sum-potential) are EXHAUSTED per dispatch; this report
avoids both and looks for a structurally different certificate.

### Opening 1 — LP-duality / weighting certificate (checked: real obstruction found)

Idea: recast "∃ a ≤n-cut refinement with S(B) ≤ target" as a value of a concave/convex program in
A, so a minimax exchange (sup_A inf_B ↔ inf-over-dual sup_A) replaces the need to exhibit XY's
actual moves. This would be the most different framing from the other two dead approaches — a
*nonconstructive existence certificate* instead of a strategy.

**I checked the key structural premise this needs and it fails.** S(A) — the alternating sum of
the DESCENDING SORT of an *unsorted* input vector A — is neither convex nor concave as a function
on R^k_{>0}. Numerically (2000 random midpoint trials, k=3): 780/2000 violate convexity and
773/2000 violate concavity (both directions fail on ~39% of trials each) — see the trial in this
report's supporting computation. This kills the naive plan "S is convex in A, so inf_B S(B) over
the polytope of reachable refinements is a concave program in A, apply LP duality directly."
Any LP-duality approach must instead dualize a DIFFERENT, genuinely convex quantity — e.g. the
sum-of-top-j functionals top_j(A) := sum of the j largest entries, which ARE convex (each is a max
of linear functionals — pick which j indices). S can be written as an alternating combination
Σ_{j odd}(top_j − top_{j−1}) of these, but the alternating combination of convex functions is not
itself convex, so this doesn't repair the obstruction directly; a workable dual certificate would
need to bound top_j(B) for each rank j uniformly (a stronger, vector-valued statement, not a
scalar LP). **Promise: low as a direct plan; the raw S-functional is the wrong object to dualize.**
A salvageable variant: dualize per-rank ("Robin Hood") constraints top_j(B) ≤ target_j(A) for all
j simultaneously (a majorization-style certificate, see Opening 3) rather than one scalar S — but
that is a different (harder, vector) LP than a naive scalar weighting.

### Opening 2 — Direct interval/measure recursion on N(t) (the layer-cake function itself)

Instead of working with the discrete multiset recursion U_k(A) (which is what induction-peel does,
just in a different guise — REJECT as too close to the exhausted branch-inequality route), work
directly with the continuous step function N_A(t) = #{parts of A ≥ t} and ask: what is the minimal
achievable meas{t : N_B(t) odd} over all "≤n admissible edits" of the step function N_A, where an
edit = replacing one downward jump of height 1 at some x by two downward jumps (of heights
summing appropriately) inserted anywhere in [0,x]? This is genuinely the SAME game (L1 says cuts
↔ splits ↔ jump-splits), so on its own it is not a new attack — but it suggests a different
PROOF VEHICLE: bound meas{N odd} using total variation / crossing-number arguments on N directly,
e.g. "N_A has ≤ n+1 downward jumps, hence ≤ n+1 sign changes of (N mod 2) as an integer step
function, so meas{N odd} is a union of ≤ ⌈(n+1)/2⌉ intervals; bound the SUM OF LENGTHS of the
odd-parity intervals using the interlacing of jump locations rather than tracking which specific
part gets cut." This could give a genuinely different (though not obviously stronger) angle: it
converts "which part to split" into "where to place a NEW jump inside the step function to
minimize total odd-interval length," which is a 1-D combinatorial-geometry question (interval
covering / jump placement) rather than a multiset-recursion question. Likely obstruction: it is
information-equivalent to the original problem (same recursion in different notation) unless
paired with a genuinely new inequality on "how much total odd-length a single new jump can kill" —
that inequality is exactly what's been elusive (branch inequalities / cut-budget cap, reappearing
under a new name). Promise: moderate as a REFRAMING that might make an obstruction visible, but
by itself it does not sidestep the crux; flag this to the outliner as "repackaging, not new
content" unless someone can name the killed-length inequality explicitly and prove it directly on
N(t) (e.g. via a clean geometric/interval argument rather than case-splitting a_1 vs rest).

### Opening 3 — Explicit global construction keyed to a MAJORIZATION target (not greedy)

Distinct from a one-pass/local rule (KNOWN-FALSE per dispatch): construct XY's ENTIRE refinement
in one global step from A's sorted profile, defined not by "which move locally beats IH" but by a
CLOSED-FORM rank assignment: sort A descending a_1≥…≥a_k; define n "target cut thresholds"
τ_1 > τ_2 > … > τ_n from the DYADIC SCALE ITSELF (τ_i = 2^{n−i} · a_1/2^n or similar, i.e.
thresholds proportional to the extremal cascade's scale ladder, NOT recomputed from A's shape).
XY cuts wherever a part of A straddles a threshold τ_i (place the cut exactly at τ_i), producing
≤ n cuts (one per threshold, provided each threshold is straddled by a distinct part — needs a
pigeonhole/counting lemma that ≤ n thresholds can't all miss all parts of a ≤(n+1)-part A, or a
patch for the "misses" case). The FINAL multiset's odd-rank sum is then bounded by a majorization
argument: the resulting B is majorized (in the top-j sense, Opening 1's convex functionals) by the
dyadic cascade of the SAME total sum, and top-j-majorization is known to control alternating-sum
functionals monotonically only in the SAME parity direction one needs (this is the open technical
core — needs proof, not asserted). This differs structurally from MATCH/BISECT because thresholds
are fixed in advance (function of n only, not of A), so there is no recursive lookahead and no
per-step branch inequality — a genuinely different mechanism. Likely obstruction: producing
*exactly* n cuts (not more) when A has k ≫ n parts requires several original parts to fall between
the SAME pair of thresholds, and then no single cut can separate them — the majorization claim
must be re-derived for "clustered" A, which is exactly the near-superincreasing regime where F1
(no one-pass rule works) was demonstrated to break naive constructions. So this needs the
majorization inequality to already absorb clustering, which is unproven; flag as the real content
gap, distinct from (but possibly as hard as) Open gap 2.

### Opening 4 — Averaging / probabilistic XY strategy (most promising NEW angle found)

Rather than exhibiting ONE deterministic refinement achieving S(B) ≤ 1/D_n, define a RANDOMIZED
family of ≤n-cut refinements {B_ω} (a genuine probability distribution over legal XY strategies,
e.g. randomizing the MATCH-vs-BISECT choice at each step with a probability depending only on the
CURRENT top ratio r = a_1/ρ, or randomizing which of several structurally-equivalent global
constructions to use) and prove E_ω[S(B_ω)] ≤ sum(A)/D_n. Since min_ω S(B_ω) ≤ E_ω[S(B_ω)], this
suffices and turns the branch-inequality case analysis into a single expectation computation,
which is often more robust to "clustered" configurations that break deterministic one-pass rules
(precisely the KNOWN-FALSE failure mode flagged in dispatch — a randomized mixture over several
deterministic rules can smooth out exactly the adversarial configurations where each individual
rule fails). This is directly the pattern in the crux corpus at **aimo-0198**
(combinatorics/probabilistic-method): "Bound a greedy minimizer's outcome by the average of its
two available options, min(A,B) ≤ (A+B)/2, to get a clean recursive bound on the potential" — used
there to close a recursive potential bound exactly where a deterministic worst-case branch
argument was hard to pin down. This is a genuine structural match to our situation: instead of
proving "the BETTER of MATCH/BISECT beats target" (the exhausted branch-inequality route), prove
"the AVERAGE of MATCH and BISECT (with a well-chosen mixing weight p(r) depending on r = a_1/ρ)
beats target," which is a strictly weaker (hence more tractable) claim implying the same
conclusion via min ≤ average. Concretely: define
  Ū_{k}(A) := p·U_{k−1}(MATCH(A)) + (1−p)·U_{k−1}(BISECT(A))
for a weight p = p(r) to be chosen, and try to show Ū_k(A) ≤ sum(A)/D_k directly (a linear/convex
combination of two IH-bounded quantities, each ≤ sum·2^{k}/... times the appropriate weight) —
this could plausibly close using ONLY the two per-branch sum bounds (sum(A)/D_{k−1} for the loser
branch is too weak alone, per the existing writeup — but a WEIGHTED combination need not use the
full IH bound on both branches at once, so it has a chance to close where the "min of the two"
argument stalled). **This is a genuinely new mechanism** — not a repackaging of MATCH/BISECT
branch inequalities, since it never needs to identify WHICH branch wins case-by-case (the source
of the F1 failure/no-closed-form obstruction); it only needs an averaged inequality to hold
uniformly. Likely obstruction: finding the correct p(r) and proving the two-term convex
combination actually telescopes to 1/D_k requires knowing the EXACT (not just qualitative) shape
of U_{k−1} under both moves — which is available (Section 4 of induction-peel.md derives the exact
S-effect of MATCH and BISECT) — so this opening can directly reuse that certified computation
without redoing it, just recombining it under an averaging inequality instead of a min/case split.

### Recommendation ranking

1. **Opening 4 (averaging XY strategy, weight p(r))** — most promising: reuses the ALREADY
   CERTIFIED exact MATCH/BISECT S-effect formulas from induction-peel.md §4 (not off-limits — only
   the branch-inequality CASE-SPLIT reasoning is exhausted, not the formulas themselves), swaps the
   case-split ("whichever wins") for a convex-combination inequality, and has a genuine crux-corpus
   analog (aimo-0198) for the technique "min ≤ weighted average of options, closes a recursive
   bound cleanly." Concretely different top-level mechanism from both exhausted routes.
2. **Opening 3 (global majorization construction)** — plausible but its core majorization lemma is
   unproven and may be exactly as hard as Open gap 2 in disguise; worth a slot if Opening 4 stalls,
   but flag the clustering obstruction honestly.
3. **Opening 2 (interval recursion on N(t))** — mostly a reframing; only useful if paired with a
   genuinely new "killed-length" inequality nobody has stated yet.
4. **Opening 1 (LP-duality)** — checked and largely closed off: the natural scalar S is neither
   convex nor concave in unsorted A (verified numerically, ~39% violation rate each direction), so
   a naive dual-weighting certificate on S does not exist; a vector-valued (per-rank/majorization)
   LP might work but collapses into Opening 3's majorization question.

### Cheap-kill candidates
None obvious for the upper bound itself (it is a universal statement over all A, not reducible by
parity/pigeonhole alone). One useful STRUCTURAL pruning: by L1/(P1)/(P2), WLOG A has ≤ n+1 parts
and A ≠ single part trivial case (S=0, done in ≤1 bisect); also by homogeneity WLOG sum(A)=1.
These are already used by all approaches, not new.

### Knowledge-base entries to use
- **Piecewise-concavity smoothing** (Algebra section) — relevant vocabulary for Opening 3's
  majorization idea, though the KB entry is stated for sinusoid sums, not order statistics;
  adapt with care, do not cite as directly applicable.
- **Hall's marriage theorem / SDR** — was the tool underlying explicit-certificate.md's Lemma E/F
  (rank-injection); that approach is a stub (not built, "concentrate cuts" flagged KNOWN-FALSE by
  dispatch) — Hall-type injection is a candidate ONLY for a genuinely different construction than
  Lemma F's "concentrate on the largest part," which is refuted.
- **Extremal principle / pigeonhole** — generic, used implicitly in Opening 3's threshold-miss
  patch.
- No entry in knowledge_base.md directly addresses LP duality / minimax game value or
  probabilistic amplification for a two-player sequential optimization — the closest generic tool
  is the crux corpus (below), not the KB.

### Analogous past problems (cruxes)
- **aimo-0198** (combinatorics, probabilistic-method) — "Bound a greedy minimizer's outcome by the
  average of its two available options, min(A,B) ≤ (A+B)/2, to get a clean recursive bound on the
  potential." Genuinely analogous: our U_k(A) = min(S(A), min over splits U_{k−1}(A')) is exactly a
  "greedy minimizer over two options" (MATCH vs BISECT) recursive potential, the same shape as the
  aimo-0198 setup. This is the strongest analog found and underlies Opening 4.
- **aimo-0117** (games-and-strategy, dyadic/geometric superincreasing sequence, "assign played
  values as a two-sided geometric sequence so the largest strictly exceeds the sum of the others" +
  a defer-commit invariant) — thematically resonant (superincreasing dyadic structure is exactly
  our G_n), but the game mechanics (write-and-move-between-boxes) don't map onto our cut/claim
  game; useful only as intuition-reinforcement for why dyadic/superincreasing is the extremal
  shape, not as a technique transplant.
- **aimo-0461** (games-and-strategy, knight-placement upper bound via "partition the conflict graph
  into small identical components, respond inside the same component the mover just used") —
  checked and judged NOT genuinely analogous: it is a graph-component pairing bound for a
  placement game, structurally unrelated to a continuous refinement/cut game; do not force this
  match.
- No entry in the corpus directly implements LP-duality for a sequential min-max cut game; Opening
  1's obstruction (non-convexity of S) was found by direct computation, not by a corpus match.

### Prior progress
See current.md: L0–L8 certified; lower bound reduced to (A-res)/G1 (same statement, cut-budget cap
on layer-cake overlap W); upper bound reduced to Lemma B / Open gap 2 (MATCH/BISECT branch
inequalities, exhausted per dispatch) and G2 (amortized-charging witness pairing, exhausted per
dispatch — this is the "min-pairing witness/smoothing" route). Both exhausted routes are recorded
in current.md and should not be repeated; the four openings above are all structurally distinct
from both.

### Dead ends (do not retry)
- Match/bisect value-function DP with per-branch case-split inequalities (induction-peel §4, Open
  gap 2) — exhausted per dispatch; F1 shows no (a_1, sum)-only closed form exists, and no branch
  inequality proof has closed after 3 rounds.
- Min-pairing witness / amortized charging (alternating-sum-potential G2, "aimo-0012-style"
  charging) — exhausted per dispatch; explicitly flagged as requiring "whole-list lookahead the
  pure charging does not by itself supply."
- "XY concentrates cuts on the largest part" (explicit-certificate.md Lemma F(a)) — KNOWN-FALSE
  per dispatch; do not resurrect even inside a new framing (e.g. Opening 3's threshold construction
  must NOT reduce to concentrating on a_1 alone).
- Any one-pass/local greedy XY rule — KNOWN-FALSE per dispatch (documented 15–75% failure rates in
  induction-peel.md); Opening 4's averaging idea is NOT a one-pass rule in this sense (it mixes two
  already-analyzed global moves by a weight, it does not decide greedily move-by-move without
  lookahead) — but the outliner should double check this distinction carefully before building.
- Huffman / reverse-merge-exchange — KNOWN-FALSE per dispatch.

### Small-case / intuition notes (conjectural)
- Numerically (n=1..4, thousands of random trials in prior rounds per induction-peel.md/
  alternating-sum-potential.md) min_B S(B) ≤ 1/D_n always achievable, confirming the upper bound
  target is correct; no new numeric check needed here beyond the convexity test above.
- The S(A) non-convexity finding (this report) is new evidence, not previously recorded in any
  approach file — worth logging so future LP-style attempts don't retry the naive scalar dual.
