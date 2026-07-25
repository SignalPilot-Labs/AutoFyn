# proof-builder report: renormalization-induction-on-seed (round 6)

Status: partial (unchanged verdict category, but with new genuine content
and a real narrowing of the odd-seed gap).

## What was done this round

Read the outline (round-6 revision already appended to this approach's own
file by the outliner: general a_2=a1+p sketch + "two covering agents"
mechanism), current.md, and the relevant certified lemmas
(prime-factors-a1-cover-forever.md, pairwise-non-coprimality.md,
bounded-gap-via-rad-a1.md, minimum-gap-lemma.md,
even-seed-universal-lock-theorem.md).

1. **Certified the general a_2 = a_1 + p Lemma in full** (§8.1): for
   *every* a_1>1 (no hypothesis on omega(a_1)), writing p=min R(a_1),
   a_2 = a_1+p. Short, fully rigorous, elementary proof from the
   definitions; strictly subsumes the earlier special-case computations
   (base case §3, Third-Term Dichotomy setup §4.1) into one lemma.

2. **New corollary** (§8.2): for odd a_1, a_2 is divisible by 2p (both p
   and 2 simultaneously) — proved in three lines from (1) plus parity.

3. **Refuted the round-6 outline's central proposed mechanism ("two
   covering agents") in full**, rather than merely leaving it open. Proved
   the **Odd-Anchor Lemma** (§8.3): since a_1 odd implies 2 is not a prime
   factor of a_1, parity of a candidate m is logically irrelevant to
   whether gcd(m,a_1)>1 — only an actual shared *odd* prime factor of a_1
   can ever satisfy the index-1 constraint. This turns the outline's own
   informally-flagged risk ("the pair (1,.) still needs p, not 2") into a
   complete, general impossibility proof: no argument based on parity can
   ever discharge the index-1 constraint for an odd seed, at any step, for
   any candidate. This kills the specific mechanism the round-6 outline
   proposed to halve the "unaccounted in-between candidates" count.

4. **New counterexample refuting the natural fallback** (§8.4): even
   restricted to indices >=2 (dropping the index-1 hope entirely), "once
   even, stays even forever" is also false in general. Found and
   hand-verified (via exact gcd computation from the sequence's own
   definition, not just simulation) that for a_1=45, a_2..a_8 are all
   even (seven consecutive even terms) but a_9=75 is odd — computed and
   checked directly: 73, 74 both fail the index-1 constraint against
   a_1=45, and 75 passes all eight prefix constraints, giving a_9=75 by
   minimality.

5. Updated Status/Approaches tried/Current best sections and added the two
   new lemmas plus the two refutations to Promotable lemmas.

## Honest assessment

The odd-seed extension of the Even-Seed Universal Lock Theorem (Step 2 for
p >= 3) remains **open**. This round's genuine contribution is negative
but rigorous and useful: it fully closes off (with proof, not just
suspicion) an entire class of "parity-based" attempts at Step 2 for odd
seeds, and produces two new small positive lemmas (general a_2 formula,
2p | a_2 corollary) that are true unconditionally and may be useful
scaffolding for a future, genuinely different mechanism. No overclaiming:
Status remains `partial`.

## Files touched
- results/imo-2026-06/approaches/renormalization-induction-on-seed.md
  (updated: new §8, updated Status/Approaches tried/Current best/Promotable
  lemmas sections)
