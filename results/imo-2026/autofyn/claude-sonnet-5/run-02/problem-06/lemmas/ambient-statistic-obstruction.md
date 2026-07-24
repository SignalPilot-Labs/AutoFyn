## Lemma: Ambient-Statistic Obstruction (CERTIFIED, round 20 — replaces the
WITHDRAWN round-19 Generalized Class-Blindness Obstruction)

**Source.** `n1-periodicity-reconciliation`, round 20, §7. Independently
re-derived by the round-20 proof-reviewer, checking specifically for the
exact circularity flagged in round 19 (memory rule 7).

**IMPORTANT — do not confuse with the withdrawn predecessor.** Round 19's
"Generalized Class-Blindness Obstruction" is permanently withdrawn (found
circular: it asserted two divergent continuations of the sequence are "a
priori consistent... by definition of open," without constructing them).
This lemma is a different, strictly narrower, non-circular statement — cite
only this file, never round 19's version.

**Depends on (certified).** `escape-cost-vacuity.md`,
`density-argument-vacuity-corollary.md` (both subsumed as special cases);
`free-facts-gcd.md`, `bounded-gap-lemma.md`, `generalized-bounded-gap-lemma.md`,
`confined-gcd-lemma.md` (cited as examples of "ambient" certified facts).

**Definition (ambient statistic).** Fix `a_1` (hence `Q, S_0`), a rogue pair
`(A',B')` with fixed finite witness data (`n_A, n_B, q*, F'', D_bad`). For a
window bound `X`, `Φ(X)` is an *ambient statistic* if it is computed by a
single fixed explicit formula whose only inputs are `X` and the fixed finite
data, and whose formula never queries, for any `n > n_B`: (i) which integers
are actual sequence terms, (ii) the actual value `a_n`, or (iii) the actual
base type `ρ(n)`. Equivalently: computable by ordinary number theory
(Mertens products, sieve/congruence counts over ALL integers in a range,
etc.) without running the greedy recursion past index `n_B`.

**Theorem.** No finite deductive argument `𝒟`, all of whose premises are (a)
finitely many values of ambient statistics (possibly with a limiting step
`X_j → ∞`) and (b) other already-certified ambient facts (in the same
formula-never-references-the-tail sense), can establish that
`E := {n > n_B : ρ(n)=A', q* ∤ a_n}` is finite (nor infinite, nor any
conclusion quantifying over realized `a_n, ρ(n)` for `n` beyond the cited
window bounds).

**Proof.** Compose `𝒟`'s finitely many steps into one explicit function
`Ψ(X_1,…,X_k)`; since every input `Φ_j` is by definition computable without
referencing the tail (`n > n_B`), so is the composed `Ψ` — a purely
syntactic fact about `Ψ`'s formula, no existence claim required. To refute
soundness of "𝒟 proves E finite," exhibit a *purely formal* (not asserted
realizable) assignment `σ`: agrees with the true sequence through
`max(X_1,…,X_k,n_B)`, but sets `ρ(n):=A'`, `q*∤a_n` for infinitely many
`n` beyond that point (making `E` infinite under `σ`). Every premise `𝒟`
is entitled to cite is, by the ambient definition, satisfied identically
under `σ` (its formula never reads the redefined tail), yet the conclusion
"E finite" fails under `σ`. Hence `𝒟`'s premises do not entail the
conclusion. (Symmetric argument for "E infinite," and for every finite
truncation of a limiting step.) ∎

**Why this is non-circular (the exact fix to round 19's gap).** `σ` is
never asserted to be an actual, legally-realizable alternate continuation of
the true, unique deterministic sequence — only that it satisfies, by direct
formula inspection, the finitely many premises `𝒟` is actually entitled to
cite. This is the standard semantic-entailment-failure check (a model of the
premises falsifying the conclusion), requiring no construction of a genuine
second legal completion.

**MANDATORY scope note (do not cite without this).** This lemma covers ONLY
arguments built entirely from ambient statistics in the strict sense above —
e.g. pairwise class-blind facts (`escape-cost-vacuity.md`) and pure
Mertens/sieve window density over ALL integers, not conditioned on occupancy
(`density-argument-vacuity-corollary.md`). It does **NOT** cover, and does
**NOT** rule out, the practically useful, occupancy-referencing forms of:
density ratios conditioned on realized `A'`-occurrences; second moment over
pairs of realized occurrences; Borel–Cantelli over the realized indicator
`1[ρ(n)=A']`; or finite-Fourier/character-sum/LP-relaxation built from the
realized occupation-count vector. Those remain formally un-ruled-out by any
certified lemma in this workspace. Any future citation of this lemma as
"killing the whole statistical-method family" is an overclaim and should be
rejected, exactly as round 19's version was.

**Status.** Correct, complete, non-circular, given the mandatory scope
note above. Reusable as a pre-certification screening check: before treating
a proposed ambient-only argument as potential FAH progress, verify it
actually stays within the strict ambient definition above.
