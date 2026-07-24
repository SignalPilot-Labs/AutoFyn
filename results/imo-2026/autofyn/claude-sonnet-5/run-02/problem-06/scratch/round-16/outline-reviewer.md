# Outline review — round 16 (imo-2026-06)

## 1. even-a1-full-periodicity-theorem (new) — APPROVE

**Novelty check (grepped workspace).** Confirmed genuinely new: the existing
"|Q|=1 special case" (`greedy-exchange-cost-potential`, referenced in
`current.md` and `seed-coupling-induction.md`) only covers a_1 = q^e, a single
prime power. This proposal covers ALL a_1 with 2 | a_1 — a strictly larger
family (e.g. a_1 = 30, 210, 2·p for any odd prime p, none of which are prime
powers and none of which were previously covered by any certified lemma or
approach). Grepped `lemmas/*.md` and `approaches/*.md` for "a_n+1", "a_n + 1",
"consecutive", "Successor Determinism" — the only near-hits
(`covering-system-construction.md` lines ~401/853/1779,
`non-automaticity-of-prefix-folding.md`) are unrelated content (a different
consecutive-occurrence bound, and an eventual-periodicity counterexample about
prefix-folding). No prior file states or uses this exact even-a_1 induction.

**Soundness check.** The induction skeleton is airtight and elementary:
- Only ONE integer lies strictly between a_n and a_n+2, namely a_n+1, so
  checking exactly those two candidates is exhaustive by definition of
  "smallest legal integer greater than a_n" — no missing candidates.
- a_n+1 illegal: gcd(a_n+1, a_n) = 1 always (consecutive integers), true
  independent of parity — correct, unconditional fact.
- a_n+2 legal: if a_1,...,a_n all even (IH), then a_n+2 is even, so
  gcd(a_n+2, a_i) ≥ 2 for every i ≤ n — correct, direct.
- Hence a_{n+1} = a_n+2 exactly, and it's even, closing the strong induction.
This is a complete, gap-free, unconditional proof of its own scoped target
(literal n=1 periodicity, T=1, L=2, for the 2|a_1 subfamily).

**Numerical sanity check (independent, this review).** Verified via a
from-scratch simulation (trial-division gcd greedy generator, no sympy) on 8
seeds including non-prime-power composites (30, 210, 1994) and seeds with
several distinct odd prime factors (2·7, 2·3·5·7, 2·11, 2·13): every seed
produces a_{n+1} - a_n = 2 for ALL n from n=1, exactly matching the claim.

**Scope discipline.** The outline explicitly and correctly refuses to
overclaim: it states the workspace-level Status stays `partial` (general
problem for odd a_1 is still open, conditional on FAH), and explicitly
disclaims any attempt to generalize the mechanism to smallest-prime-factor
p ≥ 3 (correctly notes p-2 intermediate candidates aren't automatically
resolved by bare coprimality). No case-coverage gaps — the induction is
uniform over all n, one case, no casework needed.

Verdict: **APPROVE**, build as scoped.

## 2. n1-periodicity-reconciliation (advance) — APPROVE

Pure consolidation/write-up round per round-15's own recommendation; no new
mechanism attempt claimed, correctly declining to smuggle in an 18th FAH
mechanism under the "consolidation" label. The two open hypotheses (H1 = FAH,
H2 = core-chain termination) are stated with their exact precise mathematical
content, matching what's actually still open per `termination-criterion-
lemma.md` and the standing FAH crux — verified this matches current.md's own
record, no drift. The cross-reference to this round's even-a1 result (step 2:
both H1 and H2 are vacuous when 2|a_1, since {2} is forced into every
persistent type by Free Facts) is correct and cheap — worth writing up. The
stretch goal (step 3, "does 2 ∈ Q trivialize absorption?") is explicitly
gated as optional/honest-report-only, no overclaim risk.

One thing to watch: the outline states the step-3 lemma mechanism as "a
shared prime 2 in every type's support rules out disjointness by definition"
— this is correct IF 2 ∈ Q (2 divides a_1, hence 2 ∈ every base type by Free
Facts / Q ⊆ every base type, an already-certified fact), so no verification
issue. Build only if step 3 is cheap; do not force it.

Verdict: **APPROVE**.

## 3. core-growth-monotonicity (new) — APPROVE (exploratory, honest-report gate)

**Novelty/duplicate check.** Grepped for "Binary Refinement", "N(S ∪ {p})",
"N(S')", "one-prime-at-a-time" across lemmas/ and approaches/ — no hits. This
is NOT a restatement of the certified Termination Criterion Lemma (which only
gives the iff-reduction "terminates iff N(S_k) bounded", proving nothing about
HOW to bound it); this approach is a genuinely new, more granular attempt at
the bound itself via single-prime refinement, distinct from the 17+
FAH-adjacent mechanisms (round-15 rule #27's trap pattern — verbatim-diff a
"new bound a finite pool" claim against Collateral-Safety Theorem — does not
apply here; this targets H2 exclusively, not FAH/rogue-pair reconciliation).

**Logical check of the skeleton.** Step 2's Binary Refinement Lemma is
correct and trivial: ρ_{S'}(n) = ρ_S(n) ∪ (P(a_n) ∩ {p}) is definitionally a
binary append, so each S-type splits into at most 2 S'-sub-types — sound, no
issue. Step 3's plan is explicitly exploratory ("Attempt to..."), and step 4
mandates an honest report of failure if it stalls — this is correctly
structured to avoid an overclaim risk (the round-15/round-16 house rule of
"honestly report a stall as a stall, not silently reframe it as progress").

**Risk flagged by the outline itself, correctly disclosed**: the termination-
lens explorer already found N(S_0) is not observably bounded within 15,000
sampled terms on the two standard hard seeds — so a negative/stalled outcome
is the a priori likely result, and the outline says so plainly rather than
oversell. This is the right way to propose an exploratory attempt.

Verdict: **APPROVE**, contingent on the builder genuinely trying step 3 before
concluding, and reporting honestly if it stalls (do not let "attempted but
inconclusive" get written up as "resolved").

## Diversity assessment

The three approaches are genuinely non-overlapping in framing:
- even-a1-full-periodicity-theorem: a self-contained elementary induction on a
  restricted subfamily, no persistent-type/FAH machinery at all.
- n1-periodicity-reconciliation: consolidation of the general conditional
  chain, no new mechanism.
- core-growth-monotonicity: a dedicated attack on the OTHER open sub-gap (H2,
  termination), logically distinct from FAH per the certified Termination
  Criterion Lemma.
No shared-gap collapse this round; each targets a different piece of the
problem (a genuine subfamily-complete result, a write-up, and an H2-specific
attempt). The still-untouched main crux is FAH itself (11th consecutive round,
6-16, with no new corridor found overall this round either, though this is not
a silent plateau — real content was produced on both flanks).

## Ranking

Registered `even-a1-full-periodicity-theorem` and `core-growth-monotonicity`
(both new slugs). `n1-periodicity-reconciliation` keeps its existing slug (an
advance, already registered). Ran `update_ranking` anchoring the two
newcomers against the established field: `covering-system-construction` and
`greedy-exchange-cost-potential` (both more developed on the general problem)
beat both newcomers; `n1-periodicity-reconciliation` beats `core-growth-
monotonicity` (established conditional chain vs. speculative, unproven-yet
attempt); `even-a1-full-periodicity-theorem` beats `core-growth-monotonicity`
(a genuinely complete, gap-free result vs. an unproven exploratory attempt)
and draws with `n1-periodicity-reconciliation` (both deliver real, different-
scope progress this round). This clears staleness on `n1-periodicity-
reconciliation` and anchors both newcomers to real opponents rather than only
to each other.

build set: even-a1-full-periodicity-theorem, n1-periodicity-reconciliation, core-growth-monotonicity
