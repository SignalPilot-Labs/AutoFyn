## imo-2026-03 (lens: upper-bound mechanism — the shared crux)

### Distinct openings
1. **Peel-and-match/bisect recursion (induction-peel's Lemma B / potential's Lemma D).**
   Process LB's original pieces in decreasing order a_1 ≥ a_2 ≥ …; maintain a "carry"
   C initialized to a_1. At each of the n cuts, XY either (i) **MATCH**: cut C into
   (a_i, C−a_i) so the new twin a_i cancels the *original* piece a_i at adjacent ranks
   (both a_i's now present, one at odd one at even rank, net contribution exactly a_i −
   a_i = 0 to the alternating sum), carry becomes C − a_i; or (ii) **BISECT**: cut C into
   (C/2, C/2), which usually ends the "chain" (the two halves tie each other). I confirmed
   by exact symbolic check that on the dyadic fixed point {2^n,…,1}/D_n this recursion
   (match every step) reproduces c(n) EXACTLY to machine precision for n=1,2,3 (2/3, 4/7,
   8/15) — a genuine fixed-point sanity check, not just approximate numerics.
2. **Global monovariant / potential contraction (alternating-sum-potential's Lemma D).**
   Same match/bisect primitive, but tracked via the scalar reserve Φ = S restricted to
   the not-yet-cancelled top chain, contracting by "≤ 1/2 plus next piece" per cut. This
   is mathematically the *same* mechanism as (1), just phrased as an amortized inequality
   instead of an explicit recursion — the two live approaches are not as independent on
   the upper bound as their framings suggest; they will very likely hit the identical
   wall (see below), so if both stall, a genuinely different top-level target is needed
   (see opening 4).
3. **Order-statistics/majorization (explicit-certificate's Lemma F)** — already flagged
   by round-1 reviewer as broken ("concentrate don't spread" refuted). I did not re-test
   this since the reviewer's counterexample stands (see Dead ends).
4. **A genuinely different fourth opening worth flagging for the outliner if (1)/(2)
   stall further:** cast the upper bound as an LP/exchange-argument over the FIXED
   dyadic target directly — i.e. instead of designing an explicit XY strategy, show
   by a pure exchange/smoothing argument that any LB partition not equal to dyadic can be
   "improved toward dyadic" without decreasing XY's guaranteed odd-rank-sum-suppression,
   using a local perturbation lemma (move mass from a non-geometric-ratio pair of
   consecutive-rank pieces toward the 2:1 ratio, showing XY's forced value only rises).
   This avoids constructing an explicit strategy altogether and instead argues LB gains
   nothing by deviating — a smoothing/exchange proof, structurally unlike (1)-(3). Not
   attempted numerically here due to time; flag as untested but distinct.

### The key finding: local one-step match-vs-bisect heuristics are NOT sufficient
I built and stress-tested several increasingly careful greedy XY strategies (Python,
n=2,3,4, thousands of random LB partitions each), all based on peel + local match/bisect
decisions:
- **Naive "match while q ≥ C/2 else bisect-and-stop":** fails badly and often wastes
  cuts (e.g. lone piece [1.0] with 2 cuts: naive rule repeatedly halves the residual,
  giving LB 0.75, when the true optimum is ≈0.5 — obtained by bisecting ONCE and putting
  the second cut to no further use on the same chain).
- **"Always match except decide match-vs-bisect only on the very last cut" (greedy5):**
  passed 3000/3000 random trials for n=2,3,4 with **zero failures** in my first pass —
  but this passing run had a bookkeeping bug (the lookahead comparison silently dropped
  already-"consumed" original pieces from the candidate final multiset, an easy trap
  because the twin AND the original both survive as two separate final pieces). Once I
  fixed the bookkeeping (greedy6, verified exactly reproduces c(n) on the dyadic fixed
  points to full precision — a real sanity pass), the SAME rule now **fails on 15–30% of
  random trials** across n=2,3,4 (worst gaps up to +0.26 above target, e.g.
  pieces=[0.7416,0.2554,0.0029] at n=2: naive-greedy gives 0.7416, but a local
  brute-force search finds a response reaching ≈0.502 — bisecting the carry ONCE right
  after the first match, rather than matching again against the tiny 0.0029, is far
  better). **Conclusion: "always match until the last cut" is provably wrong as a clean
  rule; the match/bisect decision needs genuine multi-step lookahead** (effectively:
  XY must sometimes bisect a residual carry even when a small original piece remains
  unconsumed, if consuming that piece would waste a cut for negligible benefit while
  leaving a large residual to eventually re-enter at odd rank). This is a **real
  mathematical obligation**, not just a bookkeeping issue: Lemma B/D as currently stated
  ("XY chooses the tactic minimizing LB's total... at each peel") is correct in spirit
  but its proof cannot rely on a syntactically simple one-pass rule — it needs either (a)
  a genuine backward-induction / DP argument over the whole remaining piece list (i.e.
  literally solve the recursion, which is what "induction on n" already proposes, so this
  is consistent with, not a refutation of, induction-peel's plan) or (b) a smarter
  invariant that doesn't require greedily committing cut-by-cut in piece order.
- **However**, a genuine brute-force local search (trying all cut-count assignments to
  each original piece, then randomly/locally optimizing the split points within each) DID
  find, for every one of several thousand random LB partitions at n=2,3, a response
  reaching ≤ c(n) (often well below, e.g. ≈0.5) — so **the upper bound itself is not in
  doubt**; only the *explicit clean one-pass strategy* that would make a slick proof is
  elusive. This matches the outline-reviewer's framing: the bound holds, but a
  from-scratch explicit-strategy proof needs real casework/induction, not a one-line rule.

### What the {0.9,0.1} warning and the "concentrate don't spread" refutation together imply
- {0.9,0.1} (match-only, no bisect fallback) shows XY MUST sometimes bisect instead of
  matching (bisect dominates when the next piece is small relative to the carry).
- The reviewer's {0.428,0.410,0.162} counterexample to "concentrate cuts on the largest
  part only" shows XY must sometimes **spread** cuts onto a SECOND-largest part (sliver
  off the top + bisect the middle piece) rather than putting every cut on a_1.
- My new counterexample [0.7416,0.2554,0.0029] shows a third failure mode: XY must
  sometimes **decline to match against a small piece at all** (even though matching is
  "free" in the sense of exactly cancelling it), because doing so wastes a cut that would
  be better spent bisecting the (still-large) residual carry.
- Together these three refutations say the correct XY tactic is **not** any single local
  rule expressible by comparing only the current carry to the next piece — it requires
  weighing the *entire remaining piece list* (a genuine minimax/DP, matching what
  induction-peel's Lemma B already proposes as "strong induction on n," and what
  alternating-sum-potential's Lemma D calls an "amortized" argument). Any outline that
  tries to shortcut this with a syntactic one-line greedy rule for Lemma B/D should be
  treated as an unproven obligation, and probably wrong as stated — the builder should
  expect to need real casework (e.g., on the ratio of the largest piece to the sum of the
  rest, similar to the "superincreasing" split used in the LOWER bound) rather than a
  simple per-step comparison.

### Cheap-kill candidates
- Any LB partition with two exactly tied largest pieces: instant cheap kill (XY
  duplicates one via a zero-cost match, canceling both) — reconfirmed, already known.
- A lone big piece (LB uses < n+1 marks, esp. LB uses 0 marks, i.e. one piece = 1): XY
  reaches ≈1/2 (well under c(n)) by a single bisect + wasting remaining cuts — a genuine
  degenerate case the builder must still handle in the case list but it is easy (far
  below the bound, not tight).
- None found that outright proves the general upper bound cheaply — the tight cases
  cluster near partitions close to (but not exactly) dyadic, where the match/bisect
  choice is genuinely delicate (see [0.334,0.666]-type and [0.7416,0.2554,0.0029]-type
  cases above).

### Knowledge-base entries to use
No entry in `knowledge_base.md` names this exact game; the closest generic tools remain
strong/structural induction and extremal-principle framing (as round 1 found). No new
KB entry surfaced this round specific to the match/bisect DP.

### Analogous past problems (cruxes)
Consistent with round 1: **aimo-0117** (dyadic/geometric top-heavy construction, defer
committing the extreme value) remains the best analog for the LOWER bound / extremal
shape, but I found no crux in the corpus that resembles the specific "greedy peel with
match-vs-bisect minimax" upper-bound mechanism — this appears to be genuinely
problem-specific; no forced match recommended.

### Prior progress
current.md is still `unsolved` / empty (stale — the approach files have the real
content). The two live approaches (induction-peel, alternating-sum-potential) both stand
at: L0/L1 numerically solid, lower bound numerically solid, upper bound is the open gap.
My finding sharpens that gap: it is real (not closable by a naive rule) but does not
falsify the target value.

### Dead ends (do not retry)
- "Always match while cuts remain, decide match-vs-bisect only on the final cut" —
  refuted (15–30% failure rate over thousands of random trials at n=2,3,4, worst gap
  +0.26 over target). Any proof sketch resting on this exact rule is wrong as stated.
- "Concentrate cuts on the largest part only, never spread" — already refuted by round-1
  reviewer; I did not need to re-test, the counterexample is solid (checked their numbers
  are self-consistent).
- Naive "bisect the carry repeatedly whenever no original piece is left to match" (spend
  ALL remaining cuts re-halving the residual) — refuted: for a lone piece [1.0] with 2
  cuts, bisecting only once (0.5,0.5) and not touching the residual again gives 0.5,
  strictly better than bisecting twice (0.75).
- Beware: any quick greedy-strategy code for this problem is prone to a subtle
  bookkeeping bug — when XY "matches" carry against original piece a_i, BOTH the newly
  cut twin AND the original a_i survive as separate pieces in the final multiset (they
  cancel each other in rank, they don't literally merge/disappear). Forgetting to keep
  the original in any lookahead simulation silently produces false-passing test results
  (this bit me once this round; flagging so the builder doesn't repeat it when writing
  or verifying the Lemma B/D argument by hand or by code).

### Small-case / intuition notes (label: conjecture unless noted)
- CONFIRMED (exact, not just numeric-to-a-few-digits): the match-every-step recursion on
  the dyadic partition itself reproduces c(n) to floating-point precision for n=1,2,3 —
  a genuine fixed-point check supporting the recursion's internal consistency at the
  optimum, even though the same rule fails off the optimum.
- CONJECTURE (strong, thousands of random trials, n=2,3): for every tested LB partition,
  SOME response using ≤ n cuts achieves odd-rank sum ≤ c(n) (often much less, near 0.5);
  no counterexample to the upper bound itself was found. The obstruction is finding the
  explicit/clean description of that response, not its existence.
- CONJECTURE: the hard cases for the upper bound are partitions close to but not exactly
  dyadic (small perturbations), where the match/bisect decision must weigh the whole
  remaining list, not just the immediate next piece — suggesting the eventual proof
  needs an inductive invariant stated in terms of the RATIO of the current largest piece
  to the sum of everything not yet processed (mirroring the superincreasing condition
  used for the lower bound), rather than a pairwise local comparison.
