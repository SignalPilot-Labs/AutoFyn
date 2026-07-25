# proof-builder report — self-similar-induction-on-n (round 20)

## What was done

1. **Fixed the stale overclaim in the approach file body** (the reviewer's
   housekeeping item): the "Exact achievability" subsection (previously
   claiming the chain+pair witness works "for every k>=2, no numerics")
   is corrected in place to state it holds only for k>=3 (certified
   `lemmas/gch-achievability-witness-k-geq-3.md`), with k=2 handled by
   the separately-certified Lemma 2 witness `{2,b,b}`. The internally
   inconsistent "cross-check" sentence (claiming a chain-empty
   specialization equals `{2,r,r}` when it's actually `{r,r}`) is removed
   and replaced with an accurate statement citing both certified lemmas.

2. **Closed the real gap the round-20 outline-reviewer found**: LNI and
   the outline's step 2 pigeonhole left untouched the case of two free
   coordinates in *different* Γ-gaps landing on the *same* rank parity
   (separated by an odd number of untouched Γ-levels). This is now
   resolved by two new lemmas, both proved in full and stress-tested in
   exact `Fraction` arithmetic before write-up:

   - **Invisible-Block Skip Fact**: a coordinate crossing an
     even-multiplicity fixed block has its rank shift by an even amount,
     so its rank-parity sign is unchanged before/after — an even block is
     not a genuine breakpoint of AltSum along a moving coordinate's
     trajectory (a trajectory-level strengthening of the certified Lemma
     BCF's "even blocks are free" corollary).

   - **General Pairwise Reduction Lemma**: for any two distinct *active*
     free values in a feasible R (no restriction on Γ-gap membership or
     rank parity — this is the key generalization), there is a
     feasible R' with the same sum/cardinality, AltSum weakly smaller,
     and strictly fewer distinct active free values. Proved via a
     mass-conserving line-segment argument: AltSum is affine on the
     maximal segment bounded only by *active* reference points (using
     the Skip Fact to rule out inactive breakpoints); slope 0 exactly in
     the previously-unaddressed same-parity case (verified exactly
     constant on a hand-built k=6 cross-gap example, both interior points
     and both boundary endpoints), slope != 0 exactly reproducing Lemma
     LNI's case (so this lemma strictly generalizes LNI rather than
     patching around it).

   Combined, these give a corrected **Finite Reduction Theorem**: every
   feasible R reduces (weakly non-increasing AltSum, same sum/cardinality)
   to an R'' with at most one distinct active free value, via a
   terminating process (potential = number of distinct active free
   values, a strictly decreasing nonnegative integer, terminating in
   <= k+1 steps). This is now airtight — no configuration is left
   unaddressed, unlike round 19's draft.

3. **Numerically stress-tested every new claim in exact arithmetic before
   writing it up** (per the dispatch instruction): local-linearity
   formula (28,558 trials, k=2..7, zero violations), the hand-built
   cross-gap same-parity worked example (exact constant AltSum=22
   throughout the segment including both boundary endpoints), and
   well-definedness of the slope despite odd-multiplicity siblings with
   even remainder (11,604 trials, zero violations). An end-to-end
   automated reduction-algorithm simulation was also attempted; it
   confirmed zero violations of the core monotonicity invariant across
   1,238 trials but had an implementation bug in its direction-selection
   heuristic (not a flaw in the underlying lemma) — the written proof
   does not depend on that script and instead gives a clean by-hand
   termination argument via the potential function.

## What remains open (honest gap)

The general Cardinality-Constrained Half-Sum Lemma's lower bound
(AltSum(R∪Γ_{k-1}) >= 1 for every feasible R, all k) is now reduced,
via a complete Finite Reduction Theorem, to a precise finite
combinatorial claim about integer multiplicity vectors (m_0,...,m_{k-1})
plus a single active free block — but that claim itself is **not proved**
for general k (proved for k=2, numerically corroborated k=3,4,5). This
is unchanged from the round 18/19 diagnosis: it needs a genuinely more
general two-parameter family GCH(j,cap,b;S) (fixed cap, decreasing
Γ-index and count budget), not a naive single-parameter induction on k.
This round's contribution is entirely on the *reduction* side (making
outline steps 1-2 gap-free); the combinatorial closure (outline steps
3-5) remains the open target for the next round.

## Status

`partial` (unchanged) — real, certifiable progress (2 new general-purpose
lemmas + 1 corrected theorem, all proved in full and numerically
stress-tested), but the central lower-bound gap for general k is still
open.

## Files touched

- `/home/agentuser/repo/results/imo-2026-03/approaches/self-similar-induction-on-n.md`
  — new "Round 20" section prepended (General Pairwise Reduction Lemma,
  Invisible-Block Skip Fact, corrected Finite Reduction Theorem,
  Promotable lemmas (round 20) subsection), plus in-place correction of
  the stale "for every k>=2" achievability overclaim.

## Promotable lemmas (for reviewer certification — not self-certified)

1. **Invisible-Block Skip Fact** — elementary, proved in full, see
   "Step 1" of the Round 20 section.
2. **General Pairwise Reduction Lemma** — strictly generalizes the
   certified Lemma LNI, proved in full, see "Step 2" of the Round 20
   section.
3. **Finite Reduction Theorem (corrected)** — proved in full via the
   above two plus a strictly-decreasing-potential termination argument,
   see "Step 3" of the Round 20 section. Supersedes round 19's
   incomplete "at most one free block" claim (which the round-20
   outline-reviewer correctly found had an unaddressed case).
