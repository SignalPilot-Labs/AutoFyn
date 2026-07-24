# Round 5 — greedy-exchange-cost-potential builder summary

Status: partial (unchanged).

## What was done
Per the outline-reviewer's dispatch, attempted to prove the Singleton Hypothesis
(|F'| = 1 for the recruited/rogue-pair witness) in GENERAL, via minimality of the
earliest-occurrence index of the witnessed extended-persistent type (not more
numerical size-bound checking).

Carried out the mechanism rigorously and produced a new, fully proved, unconditional
lemma:

**Lemma H (Critical Prime Dichotomy).** For any index n ≥ 2, fixed finite S₀ ⊇ Q, and
prime q' ∉ S₀ with q' | a_n: writing e = v_{q'}(a_n), c = a_n/q'^e, either (a) c ≤
a_{n-1}, or (b) some earlier index i < n has P(a_i) ∩ P(a_n) = {q'} exactly (q' is the
sole common prime). Proved directly from the problem's own greedy defining rule plus
the certified Free Facts lemma — no dependence on any open gap.

Applying this to the Singleton Hypothesis (each q' in F' independently falls into
branch (a) or (b)) shows the mechanism gives a genuine necessary condition on each
element of F' but does NOT rule out two or more distinct primes of F' each
independently landing in branch (b) via different earlier witnessing indices — nothing
certified connects the critical-prime witnesses of distinct primes to force a
contradiction. Attempted and documented the failure of the natural repair (forcing the
two witnessing indices to coincide). Honest conclusion: the Singleton Hypothesis
remains open in general; this round sharply relocates the exact remaining obstruction
rather than closing it.

Also reran the computational search from scratch (independent implementation,
minimal-witness convention scanning the full index range from n=1, not a tail-window
sample) on the 4 confirmed seeds (187, 209, 247, 385) plus 16 fresh seeds including
several with |Q|=3,4 (143, 221, 299, 323, 391, 493, 527, 551, 703, 899, 1073, 1147,
1001, 1155, 1365, 935, 715): every rogue-pair instance across all 20 seeds has |F'|=1,
zero counterexamples found — reported honestly as supporting evidence only, not a
proof step.

## Outcome
Status left `partial`. Lemma H is a genuine new, unconditional, promotable lemma.
The Singleton Hypothesis is not resolved; the exact obstruction is now precisely
located (no certified mechanism forces distinct "critical primes" of F' to coincide or
to be ruled out simultaneously).

File updated: `/home/agentuser/repo/results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`
