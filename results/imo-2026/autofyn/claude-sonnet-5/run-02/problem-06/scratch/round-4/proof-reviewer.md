# Round 4 proof-reviewer report — imo-2026-06

## Headline finding (read this first)

Independent recomputation (python/sympy, code and results below) shows that
**the round-3 "falsification of the zero-further-recruitment-rounds conjecture"
via a_1=175 is itself WRONG — it was a computational bug (a non-minimal /
incorrect choice of "canonical witness"), not a genuine counterexample.** Both
files built this round layer new content on top of this same buggy numerical
example, and the bug is visible even within the files themselves (an internally
self-contradictory sentence in `covering-system-construction`, and a THIRD,
mutually inconsistent S₀ value in `greedy-exchange-cost-potential` for the
identical seed). This does not sink either file's abstract lemmas (which are
correctly proved as general statements, independent of the buggy example), but
it does sink the specific numerical "evidence"/"counterexample" both files build
on this round, and it reopens a much more promising conjecture than either file
realized. Full detail below.

## Independent re-derivation of the load-bearing claim

I reimplemented the sequence generator and the Finite Core Theorem's canonical-
witness construction from scratch (trial-division factorization via sympy,
literal greedy rule). For a_1 = 175 the sequence is:

```
1 175 [5,7]   2 180 [2,3,5]   3 182 [2,7,13]   4 189 [3,7]
5 195 [3,5,13]  6 210 [2,3,5,7]  7 231 [3,7,11]  ...
```

matching both files' hand-checked values exactly (a_1..a_6 verified). Q={5,7}.

**The Finite Core Theorem's own statement** (Step 3 of `covering-system-
construction`, unchanged since round 1): "for each persistent base type B, fix
one witness index m_B := the smallest index n > N_0 with τ(n)=B." Since Q has
only 2 primes, ALL 3 nonempty subsets of Q ({5},{7},{5,7}) are persistent, so
N_0 can (and should) be taken as small as possible (N_0=1), making m_B literally
the EARLIEST occurrence of type B over the whole sequence. Also note: the
**Bounded Witness Lemma itself** (Step 2) states witnesses can be ANY index m
with τ(m)=B — no restriction to n>N_0 is even needed for correctness. So using
the true earliest occurrence is both the literal, minimal, and unambiguously
correct choice.

Computing this correctly: witness for {5} is a_2=180 (extra primes {2,3});
witness for {7} is a_3=182 (extra primes {2,13}); witness for {5,7} is a_6=210
(extra primes {2,3}). **S = {2,3,13}, S₀ = {2,3,5,7,13}.**

Both files instead use **S₀ = {2,3,5,7,11}** (`covering-system-construction`
Step 6c/6d) — internally self-contradictory (the same sentence also says
"S = {2,3}", but Q∪{2,3} ≠ {2,3,5,7,11}) — or **S₀ = {2,3,5,7,11,29,41,67}**
(`greedy-exchange-cost-potential` round 4 setup) — a THIRD, mutually
inconsistent value for the SAME seed and the SAME theorem. Neither matches the
correct minimal construction; both appear to come from sampling a witness deep
in a simulated tail window rather than the true earliest occurrence (e.g.
`covering-system-construction`'s numbers are consistent with having used a_31 =
2·3·7·11 = 462 as the "witness" for type {7} instead of the true earliest
occurrence a_3 = 182 = 2·7·13).

**Consequence.** Under the CORRECT S₀ = {2,3,5,7,13}: ρ(3) = P(182)∩S₀ =
{2,7,13}, ρ(5) = P(195)∩S₀ = {3,5,13}. These are **NOT disjoint** — they share
13. This directly refutes `covering-system-construction` Step 6c's central claim
("the actual extended types realized by a_3 and a_5 are disjoint... 13 ∉ S₀") —
false once S₀ is computed correctly with 13 included, exactly where it belongs
(from the CORRECT earliest witness a_3, the very same integer already used
earlier in the same file's Step 6a!).

I verified the true period independently by direct simulation:
**T = 274, L = 2730 = 2·3·5·7·13** — exactly ∏(correct S₀), confirming 13 was
part of the true reconciling core from the start, with ZERO extra "recruitment
round" needed once the witness is chosen correctly.

I re-ran the corrected construction (minimal earliest-occurrence witnesses) on
18 seeds total: the original round-2/3 list (35, 21, 33, 45, 77, 143, 55, 65,
91, 175), the |Q|=4/5 seeds from round-3 (210, 105, 165, 231, 1155), and three
fresh untested seeds (3927, 715, 494). **Result: V = ∅ (zero rogue pairs, zero
recruitment rounds needed) in all 18/18 seeds**, including a_1=175 itself. Full
script output is reproducible; key snippet:

```
a1=175 S={2,3,13} S0={2,3,5,7,13} violations=0
a1=35  S={2,3}    S0={2,3,5,7}    violations=0
a1=1155 S={193,2,83,29,53,17,13} S0={193,2,3,5,7,11,13,17,83,53,29} violations=0
a1=3927 (fresh) S={2,131,5,13,47} violations=0
```

This **revives** the "zero further recruitment rounds" conjecture that round 3
reported as falsified — the falsification itself is retracted (see current.md
edit).

**What is NOT affected by this bug, independently reverified as correct:**
- `covering-system-construction` Step 6a (PUCL's literal first-occurrence
  construction is false: a_3=182 gives naive core {2,13}; a_4=189=3³·7 is
  divisible by neither) — uses only Q-level data, unaffected. Correct.
- `covering-system-construction` Step 6b (generous S-level PUCL is a trivial
  corollary of the Finite Core Theorem) — correct, adds no content, as claimed.
- `greedy-exchange-cost-potential`'s finding that 13 divides only ≈14% of
  base-type-{7} (352/2453 = 0.143) and base-type-{5} (264/1839 = 0.144)
  occurrences — a direct divisibility fact independent of S₀/witness choice.
  Independently reconfirmed to the reported precision. This falsification of
  the "whole base-type resolution" claim stands.
- Lemma G's and the Round Resolution Lemma's *proofs* (abstract statements) —
  see below, both verified correct as general claims, independent of the buggy
  numerical example built to motivate/test them.

## covering-system-construction — verdict: CHANGES REQUESTED

Status claimed: partial. True status: **partial**, but with a specific,
documented error in this round's main new content (Step 6c/6d) that must be
corrected, not merely "gap remains."

- Step 6a: correct, independently reverified (hand check + script match).
- Step 6b: correct (trivial corollary of Finite Core Theorem).
- Step 6c/6d: **incorrect** — the "exact minimal witness pair" is not actually
  a counterexample once S₀ is computed via the theorem's own literal (minimal)
  witness convention; the claimed disjointness ρ(3)∩ρ(5)=∅ is false under the
  correct S₀ (they share 13). The broader conceptual point ("disjunctive
  per-type coverage never pins down which shared element two specific
  occurrences realize") may still be true in principle, but this file's
  attempt to demonstrate it with a concrete, hand-checkable witness pair fails,
  and no valid replacement example is given.
- The file's overall conclusion ("PUCL alone is insufficient... conclusive
  reason... the still-missing ingredient is the global/simultaneous argument")
  is **not established** by this round's work — its supporting evidence is
  flawed. Gap (†) remains open, but the round's "negative result" is not the
  rigorous finding it is presented as.
- Required fix for next round: recompute S/S₀ with the literal minimal-witness
  convention across all examples in this file, and either exhibit a genuine
  (correctly computed) rogue pair or accept that none has been found in 18/18
  tested seeds with correct witnesses, and pivot the target accordingly (see
  current.md next-round guidance).

## greedy-exchange-cost-potential — verdict: CHANGES REQUESTED

Status claimed: partial. True status: **partial**, with real new certified
content, but the round's empirical support is compromised by the same class of
bug.

- **Lemma G (Extended Earliest-Witness Intersection)**: re-derived from scratch
  independently. Correct, complete, unconditional — a straightforward but
  genuine one-step application of the certified Free Facts lemma (pairwise
  gcd), giving a *symmetric* pair of witness indices rather than the
  certified Generalized Bounded Witness Lemma's asymmetric one. **CERTIFIED**
  to `results/imo-2026-06/lemmas/extended-earliest-witness-intersection.md`.
- **Rescoped Round Resolution Lemma**: correctly rescoped to the pair-local
  target per the outline-reviewer's mandatory correction (verified: the
  ≈14% base-type-divisibility figure is independently reconfirmed, so the
  rescoping was the right call). The Lemma's own proof, CONDITIONAL on the
  explicitly-stated "Singleton Hypothesis" (|F'|=1), is correct and the
  conditionality is honestly disclosed throughout — stated in the Lemma's own
  Statement, not smuggled in, and repeatedly flagged in the surrounding prose.
  This satisfies the rigor bar for a *conditional* result. Its attempted
  removal (first-bad-round minimality induction, modeled on aimo-0514/
  aimo-0077) genuinely stalls for the documented structural reason (the
  hypothesis is a static factorization fact about one integer, not tied to the
  recruitment process's own recursive structure) — this negative finding is
  itself correct and useful.
- **However**: the motivating a_1=175 setup and the "verified computationally
  in every rogue-pair instance... ~20 seeds" claim reuse the buggy S₀
  ({2,3,5,7,11,29,41,67}, itself inconsistent with the sibling file's number
  for the same seed). Since my corrected recomputation finds V=∅ for a_1=175
  with the correct S₀ (no rogue pair exists at all for this seed), it is now
  unverified whether any of the "~20 rogue-pair instances" used to support the
  Singleton Hypothesis are genuine rogue pairs under a correctly computed S₀,
  or artifacts of the same bug. This significantly weakens (does not
  necessarily falsify) the empirical support claimed for the Singleton
  Hypothesis, and must be redone before being relied upon.
- The honest "even granting the Singleton Hypothesis, this doesn't bound total
  rounds" scope analysis (final subsection) is sound reasoning and stands
  regardless of the S₀ bug — it is a valid conditional/structural observation,
  not a numerical claim.

## Lemma certification decisions
- **Certified**: Lemma G → `lemmas/extended-earliest-witness-intersection.md`
  (unconditional, correct, no gaps; includes a caution note about the
  witness-selection bug found this round).
- **Not certified**: the Round Resolution Lemma — correctly self-disclosed as
  conditional on the unproved Singleton Hypothesis; per the file contract,
  conditional results are not certified as portable unconditional lemmas.
  Recorded in current.md as valid conditional content, not yet promotable.

## current.md updates made
- Added a prominent "ROUND 4 CRITICAL CORRECTION" section retracting the
  round-3 "falsification of zero further rounds" finding, with the corrected
  S₀ computation, the 18-seed re-verification (0 violations), and the
  independent T=274/L=2730 confirmation.
- Marked the round-3 finding paragraph as SUPERSEDED (kept for audit trail).
- Added explicit next-round guidance: recompute all rogue-pair claims with the
  minimal-witness convention; attempt a direct proof that V=∅ always holds for
  the minimally-witnessed Finite Core Theorem's S₀ (a sharper, now
  better-supported target); do not re-attempt the (still genuinely falsified,
  unaffected by this bug) "universal glue prime"/"cost≤1" claims from round 2
  (a_1=35 counterexample, which does not depend on witness-selection and
  stands).
- Added two new "Approaches tried" entries for this round's builds with the
  CHANGES REQUESTED verdicts and the specific findings.
- Status field remains `partial` (no approach reached solved).

## Verdicts (per CLAUDE.md's per-approach routing)
- **covering-system-construction**: CHANGES REQUESTED. Status: partial.
  Gap: Step 6c/6d's central demonstration is computationally wrong (S₀
  mis-computed); must be recomputed with minimal witnesses or replaced with a
  valid example before the "PUCL cannot be rescued" conclusion can be trusted.
- **greedy-exchange-cost-potential**: CHANGES REQUESTED. Status: partial.
  Gap: Lemma G is solid (certified); the Round Resolution Lemma's proof is
  valid but its empirical/motivating support (a_1=175, "~20 seeds") needs to be
  redone with the correct minimal-witness S₀ before the Singleton Hypothesis's
  apparent prevalence can be trusted as evidence either way.

## Files touched
- `/home/agentuser/repo/results/imo-2026-06/current.md` (Status field kept
  `partial`; added ROUND 4 CRITICAL CORRECTION, superseded-round-3 note,
  next-round guidance, two new Approaches-tried entries).
- `/home/agentuser/repo/results/imo-2026-06/lemmas/extended-earliest-witness-intersection.md`
  (new, certified).
- Ranker: `record_outcome` called for both `covering-system-construction` and
  `greedy-exchange-cost-potential` (round 4, outcome `partial`).
