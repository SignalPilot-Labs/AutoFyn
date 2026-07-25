# Build report: lp-duality-split-polytope, round 11

## Dispatch
Test whether the Multi-Piece Sufficiency construction's Even-Block-
Neutrality mechanism generalizes past AP-structured (triangular-family)
landmarks to feed `global-lp-vertex-sufficiency`'s Σ-shape work (its
Opening 3), given round 10's negative Nelder-Mead numeric check against
LB's own geometric partition. Told to investigate honestly and report a
clean negative if it doesn't generalize.

## What was done
1. Built the direct, literal transplant of round 10's Multi-Piece
   Sufficiency construction to LB's geometric landmarks
   {2^0,...,2^n} (top-pair epsilon trick + middle-landmark even-halving +
   bottom unsplit) and evaluated it **exactly** (Python `Fraction`,
   n=2..8, not Nelder-Mead). Result: fails in every instance, with a
   shortfall (achieved OddSum minus c(n)) that **grows** monotonically
   towards a positive constant (~0.123 by n=8), not shrinking to 0. This
   upgrades round 10's imprecise numeric check to an exact result and
   pins down a structural reason: geometric landmarks have exponential
   (not constant-unit) gaps, and the top landmark alone is a Θ(1) (>1/2)
   fraction of the total mass — neither property the mechanism needs
   (dense unit-spaced landmarks, polynomially-larger total mass than any
   one piece) holds there.
2. Made explicit a definitional point: since c(n) is conjectured to equal
   max_p V(p) with LB attaining it, no construction can EVER beat c(n) at
   p=LB specifically (would contradict LB's own conjectured optimality) —
   so this was always a "fails or ties" search, never a "beats" search;
   this reframes why the round-10 finding was expected.
3. Pivoted to check "attains exactly" instead of "beats": found a
   different, narrower construction (split only the single top landmark
   p_1 into fragments duplicating every other landmark, using the full
   n-cut budget on that one piece) that hits OddSum = c(n) **exactly**,
   for every n>=0 in one uniform formula. Proved this in full (isolated
   tied-pair neutrality applied to n-1 pairs, plus a direct rank-parity
   computation of the bottom 3-element tied block of value 1, then the
   scaling identity) and independently re-verified by exact `Fraction`
   arithmetic for n=0..14 (15/15 exact fraction equalities, re-run twice
   independently in this session).

## Result
- Finding 1: clean, now exact (not just numeric), negative confirmation
  that the multi-landmark Even-Block-Neutrality transplant does not
  generalize past AP-structured landmarks — as the outliner predicted.
- Finding 2: a genuine new byproduct, the **Top-Duplication Witness
  Theorem** — V(p_LB) <= c(n) exactly, for every n>=0, via an explicit,
  fully proved, uniform construction. This is new content (distinct from,
  not overlapping, `T(2)`/Dominant-Chain's work on the reverse
  inequality V(p_LB) >= c(n)), proposed for certification.
- Honest scope maintained throughout: neither finding proves the general
  upper-bound Existence Theorem or the lower-bound direction; both are
  single-point / mechanism-scope results, stated as such.

## File updated
`/home/agentuser/repo/results/imo-2026-03/approaches/lp-duality-split-polytope.md`
— added "Round 11 update" summary at top, full "Round 11" proof section
(11.1 negative transplant + structural diagnosis, 11.2 Top-Duplication
Witness Theorem with full proof), a round-11 "Approaches tried" entry,
and a "New, round 11" Promotable lemmas entry (Top-Duplication Witness
Theorem) for the reviewer to certify.

Status: `partial` (unchanged for the approach as a whole — this round's
work is tool-supplier/secondary-target work, not a step towards closing
the approach's own primary target, which remains the triangular family's
already-complete Necessity+Sufficiency picture).
