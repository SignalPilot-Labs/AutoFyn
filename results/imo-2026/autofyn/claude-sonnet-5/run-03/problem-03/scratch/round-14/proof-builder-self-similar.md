# proof-builder report — self-similar-induction-on-n (round 14)

Status: partial (unchanged — genuine new progress, no closure).

## What was done

1. **Corrected the round's motivating numeric claim first**, per the
   outline-reviewer's mandatory flag: re-verified from scratch (own
   exact-`Fraction` and random-composition scripts, independent of the
   explorer's and the reviewer's own scripts) that the "full-count
   instance has genuine slack" claim does not reproduce — margins found
   are ≈0 (tight) at m=3,4, consistent with the reviewer's finding. No
   claim in this round's write-up depends on any slack assumption.

2. **Proved in full, and independently verified numerically** (own
   scripts, thousands of exact-`Fraction` trials, zero violations):
   - The **AltSum corollary**: `0 ≤ AltSum(N) ≤ max(N)` for any finite
     multiset N of positive reals — a one-paragraph induction from the
     certified Peeling identity, exactly the elementary tool the outline
     asked for.
   - The **Growth Lemma**: the increasing-direction complement of the
     already-certified Monotonicity Reduction Lemma. For D with ≥2
     pieces, cap 2^(m-1), sum(D) ≤ 2^m, D can be grown coordinatewise
     (never exceeding the cap) up to sum 2^m exactly, and OddSum(D∪T)
     ≤ OddSum(D''∪T) for the grown D''.

3. **New Small-Sum Reduction Theorem** (proved, modulo one flagged tie
   detail): using the Growth Lemma, the *entire* small-sum-mirror
   sub-case (ii) named in the dispatch — both the not-full-count
   instance (via the outline's own filler-insertion) and the full-count
   instance (newly reduced here) — is shown **equivalent** to
   `Case-B(m,k)` at the single boundary value sum(D)=2^m. Combined with
   the already-certified Monotonicity Reduction Lemma (which shows the
   large-sum/gap-(a) regime needs the identical boundary object), this
   **unifies the entire p=0 branch of GT(m), at every sum, into one
   single already-long-open object**: `Case-B(m,k)` (open since round 4,
   "the middle regime," closed only for the smallest instance at m=3,4
   in round 11). This is a genuine simplification of the remaining
   target for GT(m), not a new closure — sub-case (ii) needs no new
   machinery beyond what the file has already been attacking for seven
   rounds.

4. **Sub-case (i) (q=1, e≥1): honest negative finding + precise
   diagnosis, not closed.** Found an explicit counterexample (k=0, e=1,
   D={0.4,0.4}) disproving the natural "piece-cap-relaxed" fix — ruling
   out the most direct route. Traced exactly when a genuine q=1,e≥1
   instance is *forced* to occur in the real recursion (once a pure q=0
   chain becomes count-infeasible, matching and generalizing round 12's
   own m≥4 feasibility threshold) — a useful structural explanation for
   why m≥4 is exactly the threshold where this sub-case first becomes
   unavoidable — but no closing argument was found this round.

## Net effect

GT(m) for m≥4 (hence gap (a) of the shared Branch-I.A window for ℓ≥5)
**remains open**. What remains is now precisely two named objects
(`Case-B(m,k)`, already under attack since round 4; and sub-case (i),
newly diagnosed but unsolved) rather than an open-ended search across
multiple unreduced sub-cases. Two new general-purpose lemmas (AltSum
corollary, Growth Lemma) are proposed for certification.

## File updated

`/home/agentuser/repo/results/imo-2026-03/approaches/self-similar-induction-on-n.md`
— Status kept `partial`; new "Round 14 target" note, "Approaches tried"
entry, "Current best" headline, full "Round 14: the AltSum corollary,
the Growth Lemma, and the exact reduction ..." section, and "Promotable
lemmas (round 14)" section all added. No other files touched;
`lemmas/` not self-certified (left for the reviewer).
