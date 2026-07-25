## imo-2026-03 — UPPER BOUND lens (Xiang-Yu's guarantee c(n)=2^n/D_n, D_n=2^{n+1}-1)

**Scope.** Only the fully-open crux: Lemma B, `U_k(A) ≤ sum(A)/D_k` for every multiset A and
every k, where `U_k(A) := min over ≤k-cut refinements B of S(B)` and `S` is the alternating-sum
potential (L2). Four routes are exhausted/refuted (match/bisect-DP branch inequalities,
min-pairing witness, huffman/reverse-merge-exchange, convex-combination/top-part averaging) — I
did not re-attempt any of them. What follows is new terrain-mapping plus fresh numeric evidence.

### Distinct openings surveyed (with verdicts)

1. **Full randomized/whole-process strategy (probabilistic method).** Idea: since
   `U_k(A) = min over deterministic strategies`, ANY distribution over valid ≤k-cut strategies
   gives `U_k(A) ≤ E[S(B)]`, with no restriction to a fixed 2-branch choice — this is structurally
   different from the refuted averaging (which fixed exactly two top-part moves and mixed them
   with weight p(r); Obstruction 1 there was "average ≥ min of the fixed two branches", and
   Obstruction 2 was that the *winning* move is often non-top, e.g. bisecting the smallest part
   on A={2,2,1}). A genuine probabilistic strategy would randomize **which part** gets cut, not
   just mix two named branches, so it structurally sidesteps Obstruction 2. **Status: live but
   unconstructed** — I did not find (nor had time to hand-derive) a concrete randomization law
   whose expectation telescopes with `D_k=2D_{k-1}+1`; designing it is plausibly as hard as the
   branch inequalities themselves (linearity of expectation still requires knowing, at every step,
   the conditional expected effect of the random cut on the whole profile). Crux-corpus check:
   `aimo-0198` (already cited/used, refuted at the top-part level) and `aimo-0956`
   ("set a single probability so two weakest branches become equal") are the only
   `combinatorics/probabilistic-method` analogs and both are 2-branch-equalizing tricks, i.e. the
   *same* mechanism already refuted, just possibly on a different pair of branches — **not a new
   mechanism**, only a hint that a "MATCH-the-smallest-unmatched-part vs BISECT-the-top" pairing
   might be a better 2-branch choice than the refuted top/top pairing. Worth a cheap follow-up
   probe before committing an approach to it.

2. **"S(B) ≥ 1 with equality iff B is cascade-type" (the reviewer-flagged unifier).** I ran an
   exact witness-extraction numeric check (`exact_U_witness`, small A, k≤3, Fraction arithmetic):
   for LB's own optimal profile A = P_n = {1,2,4,...,2^n}, the minimizer IS the cascade
   {2^{n-1},2^{n-1},...,1,1,1} exactly, confirming the LB/UB witnesses coincide there (already
   known). But for **generic** A away from P_n, the actual S-minimizing B is *not* cascade-shaped
   at all — e.g. A=(2,1),k=2 → witness {1,1,1/2,1/2} (one bisection, S=0); A=(6,4,2),k=3 →
   witness {4,4,2,2} (S=0, only one MATCH used, one cut unused); A=(2,2,1),k=2 → witness
   {2,2,1/2,1/2} (bisect the small part, S=0). **Verdict: the cascade characterization is a
   tightness tool for LB's extremal choice, not a general-A construction recipe.** Away from the
   extremal profile XY has large slack and a trivial pairing already beats the target by a wide
   margin; the *only* hard instances are ones structurally close to (but not exactly) dyadic,
   where genuine casework is unavoidable. This downgrades the reviewer's "closes both walls"
   flag for the UB side specifically — it is a real LB tool but not obviously a UB shortcut.

3. **LP / majorization duality certificate.** Structurally mismatched to the UB's existence
   direction: LP duality naturally proves *upper caps* (β(B) ≤ M for all B in a family), which is
   what the LB side needs; the UB side needs an *existence* statement (some B with β(B) ≥ target),
   for which the natural tool is a direct construction + witness, not a dual certificate. Moreover
   the LB-side obstruction O1 (certified, alternating-sum-potential.md §5) proves that **any**
   price/cover argument independent of the cut budget is doomed (unlimited bisection pushes
   β past the target), and by the β(Q⊔C)=β(Q)+β(C)+W duality this obstruction is essentially
   self-dual — a majorization/LP argument on the UB side would face the identical "ignores the
   cut-count" failure mode. **Verdict: low promise, do not invest a full approach here** without
   first exhibiting a concrete price function that provably depends on the cut budget (none found).

4. **Global potential/monovariant XY decreases regardless of partition.** This is, on inspection,
   exactly a restatement of Lemma B itself (`Ψ(A,k) := D_k·U_k(A) − sum(A) ≤ 0`, monovariant =
   "some split makes Ψ non-increasing"): not independent leverage, same content as the branch
   inequalities. Confirmed again this round by two fresh negative numeric probes (below).

### Cheap-kill / reconfirmation numerics (fresh this round, exact Fraction arithmetic, <30s each)

- **One-step lookahead greedy (pick the single split literally minimizing S(B) after one move,
  repeat) FAILS**: 12/60 random instances (n≤4 parts, k≤3) mismatch the exact DP value, with
  gaps up to `U_greedy − U_exact = 3` against exact values of 0 (e.g. A=(6,5,4,2), k=2: exact
  U=0, greedy=3). Confirms F1 (already known) with new concrete witnesses — do not propose "true
  greedy improvement each step" as a shortcut; it needs real multi-step lookahead.
- **Max-adjacent-gap-first MATCH strategy** (repeatedly MATCH the consecutive sorted pair
  y_(2j+1),y_(2j+2) with the largest gap) also **FAILS badly**: 43/80 random instances mismatch,
  worst gap `U_strategy − U_exact = 4`. This rules out the natural "attack the biggest S-term
  first" greedy as well — record as a fresh do-not-retry (it is a different rule from the
  averaging-upper-bound's top-part MATCH/BISECT, and from the reviewer's max-gap intuition, so
  worth banking explicitly).
- Re-confirmed (per L4/exact DP) that XY's optimal first move is genuinely profile-dependent:
  on A=(2,2,1) the winning move bisects the *smallest* part; on A=(4,2,1) (=scaled P_2) it
  bisects the *top*; on A=(6,4,2) a single MATCH already suffices with one cut unused. No
  (a_1, sum)-only or single-statistic rule threads all three.

### Terrain summary for the outliner

- **Live, worth a real approach slot:** (1) a genuinely whole-profile randomized strategy —
  but it must randomize the *target part* (not just mix two fixed top-part branches), and its
  first job should be a fast feasibility probe (does ANY natural weighting, e.g. probability
  proportional to `a_i`'s contribution to `S`, achieve `E[S(B)] ≤ sum/D_k` on the known hard
  counterexample A={2,2,1},k=2 and on P_2,P_3?) before committing to a full write-up.
- **Illusory / do not open as their own approach:** LP/majorization duality (wrong direction,
  O1 obstruction transfers), the cascade-equality characterization as a *general-A* UB recipe
  (numerically it only fires at/near the LB extremal, not generically), global monovariant
  (restates Lemma B, no new content), aimo-0012 merge/unmerge (isomorphic to the already-refuted
  huffman/reverse-merge-exchange route — same "cost doesn't decompose over merge order" failure
  mode is expected; do not re-import).
- **Honest assessment:** I could not identify a mechanism that clearly escapes the branch-
  inequality wall. The field's own diagnosis (F1: the value function genuinely depends on the
  whole profile, not `(a_1,sum)`) looks correct and load-bearing — any successful UB proof
  probably has to bite the bullet and do real casework/lookahead keyed to the ratio structure of
  the *whole* sorted profile (not just the top part), which is what induction-peel's Open gap 2
  already states as the target shape. The best concrete new lever surfaced this round is
  **randomizing the choice of which part to cut** (not just averaging two named top-part moves),
  which is a different mechanism from all four refuted ones even though its feasibility is
  unproven.

### Candidate technique(s)
Whole-profile randomized/probabilistic strategy (untested, feasibility open); otherwise the field
must fall back to induction-peel's branch-inequality DP (Open gap 2) — no shortcut found.

### Cheap-kill candidates
- Do NOT retry: one-step S-minimizing greedy (12/60 mismatches, this round).
- Do NOT retry: max-adjacent-gap-first MATCH greedy (43/80 mismatches, this round).
- Do NOT retry: "concentrate cuts on the largest part" (explicit-certificate.md Lemma F(a) — already
  flagged KNOWN-FALSE in memory; reconfirmed consistent with this round's A={2,2,1} witness).
- Do NOT retry: aimo-0012-style merge/unmerge induction on part-count — isomorphic to the refuted
  huffman/reverse-merge-exchange route (round 3).

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics) — only as scaffolding for stating Lemma B, not a
  bypass (per round-4 explorer's opening 3/4, reconfirmed).
- No KB entry directly supplies a UB-specific theorem; the reduction machinery (L0–L4, certified)
  remains the only imported infrastructure.

### Analogous past problems (cruxes)
- `aimo-0198` (min ≤ average of two options) — already tried and refuted at the top-part level
  (averaging-upper-bound.md); the underlying mechanism could in principle be retried on a
  *different* pair of branches (e.g. "MATCH smallest-unmatched-part" vs "BISECT top"), but that
  is a variant of the SAME technique, not a new one — flag, do not present as fresh.
- `aimo-0956` (equalize two probability-weighted worst cases) — same 2-branch-equalizing family
  as aimo-0198; no new mechanism.
- `aimo-0012` (Poland ISL bin-packing, "smallest k" merge/unmerge induction) — checked in full;
  its upper-bound technique (pigeonhole-merge an adjacent pair, induct, unmerge) is exactly
  isomorphic to the round-3 refuted huffman/reverse-merge-exchange approach for this problem
  (cost does not decompose over merge order here). **Not a viable new opening** — recorded so it
  is not re-proposed under a different name.
- Searched all `games-and-strategy` subtopic entries in `combinatorics` and `number_theory`
  again (round-4 explorer already enumerated ~20 problem_ids); none model a continuous-interval
  Stackelberg cut-then-claim game — reconfirm: **no close analog exists in the corpus** for the
  UB's actual structure.

### Prior progress
Unchanged from `current.md`/`induction-peel.md`/`alternating-sum-potential.md`: the recursion (R),
the part-count fix, the base case (`U_0(A)=S(A)≤sum(A)`, via P1/P2), and the exact S-effect
formulas for MATCH_top/BISECT_top are all rigorous. Only the two branch inequalities
(`U_{k-1}(c(A)) ≤ sum(A)/D_k` for whichever move c wins) remain open, and the dyadic-cascade
witness at A=P_n is exact (S=1/D_n, verified n=1,2,3).

### Dead ends (do not retry — consolidated)
match/bisect-DP branch inequalities as stated (need genuine profile-dependent lookahead, not a
closed form); min-pairing witness (round 3); huffman/reverse-merge-exchange AND its isomorphic
twin aimo-0012 merge/unmerge (cost doesn't decompose over merge order); convex-combination/
top-part averaging (min ≥ target already, non-top moves needed); one-step S-greedy (fresh, this
round); max-adjacent-gap-first MATCH greedy (fresh, this round); "concentrate cuts on the largest
part" (explicit-certificate Lemma F(a)); LP/majorization duality on the UB side (wrong direction,
O1 obstruction transfers — argued, not numerically tested, flagged low-promise rather than fully
refuted).

### Small-case / intuition notes (conjecture only)
- The optimal XY first move is **profile-dependent in a genuinely non-local way**: bisect top
  (dyadic profiles), bisect smallest (A={2,2,1}), or a single MATCH with a cut to spare
  (A={6,4,2}) — no single statistic of A predicts which. This is now confirmed by three
  independent numeric probes across rounds (this round's two greedy-failure sweeps plus the
  round-4 averaging counterexample), strengthening confidence that F1 is a real structural fact
  of the problem, not an artifact of a particular framing.
- Conjecture (unverified): the correct UB proof likely needs to condition on the *ratio of the
  top part to the rest* (`r = a_1/ρ`, already isolated in induction-peel §4) AND a secondary
  statistic distinguishing "several comparable large parts" (A={6,4,2}-like) from "one dominant
  part with small clutter" (A={2,2,1}-like) — i.e. genuinely two-parameter casework, which is
  consistent with why no one-parameter rule has worked in three independent attempts.
