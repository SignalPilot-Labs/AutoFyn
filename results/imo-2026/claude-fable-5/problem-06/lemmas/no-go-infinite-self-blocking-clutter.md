# Lemma (no-go): infinite identically self-blocking clutters exist

Certification: **CERTIFIED** (round 1, proof-reviewer). Proved in full in `approaches/self-blocking-clutter-induction.md` (Theorem + Lemmas 1–6, the "ladder clutter"); every lemma checked line by line and Lemma 3 independently re-verified by the reviewer with fresh code (585 cut-transversals on truncations, 0 failures; all enumerated minimal cuts contain r₀ as forced by the path {r₀}).

## Statement

There is an **infinite** antichain M of finite nonempty subsets of a countable ground set Ω such that:
- M is pairwise intersecting;
- every finite transversal of M contains a member (self-covering; equivalently b(M) = M, identically self-blocking);
- the witness lemma holds (for Y ∈ M, y ∈ Y there is W ∈ M with W ∩ Y = {y});
- there is a 2-element set E₀ ⊆ Ω meeting every member such that for every finite B ⊆ Ω ∖ E₀ some member avoids B.

Construction: Ω = {1,2} ∪ E(ladder); M = {{1,2}} ∪ {{1}∪P : P a simple s–t path} ∪ {{2}∪C : C a minimal finite s–t cut} on the one-way infinite ladder with s = u₀, t = v₀.

## Use

**Hypothesis filter.** The minimal-type clutter M of the greedy-sequence problem satisfies all the properties above; therefore "M is finite" is NOT provable from these clutter-level properties alone. Any proof of finiteness must use the number-theoretic realization (integer sizes, windows, densities) essentially. The certified proof of finiteness (`essential-prime-bound.md`) does exactly this: the Exclusion Principle's witness satisfies the SIZE bound rad(t) ≤ t < m, which has no clutter-level analog — consistent with, and explained by, this no-go lemma.
