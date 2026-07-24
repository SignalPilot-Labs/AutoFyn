# Permanent-Inadmissibility Lemma

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 6, §F preamble, elementary Step 1).

**Statement.** If some index `j` has `rad(a_j)∩C=∅` for a candidate radical
`C`, then no term with radical exactly `C` can appear at any index `>j`.

**Proof.** Admissibility of a candidate `x` at step `n` requires
`gcd(x,a_i)>1` for **all** `i≤n`, in particular `i=j` (once `n≥j`). If
`rad(x)=C` and `C∩rad(a_j)=∅`, then `gcd(x,a_j)=1`, so `x` is inadmissible
at every step `n≥j`. The greedy rule's admissibility requirement only ever
gains constraints as `n` grows (it never relaxes), so this failure persists
for all `n≥j`, i.e. for all candidate steps producing `a_{n+1}` with `n≥j`,
i.e. all indices `>j`. ∎

**Discussion.** Elementary but foundational — the basis for the
Companion-Disjointness Coarsening Lemma's Bucket-Exclusion Corollary
(`lemmas/lemma-companion-disjointness-coarsening.md`) and logically the
negative counterpart of the already-certified Lemma ER
(`lemmas/lemma-ER-eventual-realization-dichotomy.md`): together, every
candidate integer is either eventually realized or permanently blocked by
some fixed earlier witness, with no third possibility.

**Independent verification (proof-reviewer, round 6).** Re-derived from the
definition of the greedy rule directly; one-line, no gap. Also directly
confirmed on the concrete instance `a_1=247`: `a_3` (`rad={2,7,19}`)
permanently blocks any radical disjoint from `{2,7,19}` — e.g. `{3,13}` — an
explicit case-check, not just the abstract statement.

## Certification

Trivial but correct and reusable; distinct from and more primitive than the
Coarsening Lemma. Certified `solved`-quality.
