# Conditional Markov density bound (and why it is insufficient alone)

**Statement.** Suppose, as a hypothesis, `ω(a_n) ≤ M_0` for every `n` (some
fixed constant `M_0`). Then for every `N≥1`,
`|{q prime : D_N(q) ≥ N/M_0}| ≤ M_0^2`.

**Proof.** `Σ_q D_N(q) = Σ_{i=1}^N ω(a_i) ≤ N·M_0` (double-counting: the sum
over primes `q` of the count of terms among the first `N` divisible by `q`
equals the sum over `i≤N` of the number of distinct prime factors of `a_i`).
If `t` primes each satisfy `D_N(q)≥N/M_0`, then `Σ_q D_N(q) ≥ t·N/M_0`, so
`t·N/M_0 ≤ N·M_0`, giving `t ≤ M_0^2`. `∎`

**Why this does not, by itself, prove any prime-set finiteness result (the
"cycling primes" obstruction — important negative finding, keep this
disclaimer attached whenever the bound is cited).** The bound is *pointwise
in `N`*: for each fixed `N` separately, at most `M_0^2` primes can meet the
threshold at time `N`. It does **not** bound `|⋃_{N≥1} Q_N|` where
`Q_N:={q:D_N(q)≥N/M_0}`, because the threshold `N/M_0` grows with `N` while
`D_N(q)` is only non-decreasing: a prime can be in `Q_{N_0}` and later drop
out of `Q_N` for `N>N_0` if it stops accumulating occurrences relative to
the rising threshold. So the set of dominant primes over all time can be
infinite even though at most `M_0^2` are dominant at any single instant —
the pointwise bound is fully consistent with `{q*(n):n≥1}` (the Domination
Lemma's per-step dominant primes) being infinite. Closing this requires a
*persistence* argument (some primes, once dominant, cannot be permanently
displaced from a bounded pool), not supplied by any currently certified
lemma.

**Source.** `results/imo-2026-06/approaches/forced-primes-well-ordering.md`
(round 3).

**Certification.** The inequality itself is correct (standard averaging
argument, verified line by line by the reviewer). Certified `solved`-quality
as a conditional lemma (conditional on the stated `ω(a_n)=O(1)` hypothesis,
itself still open). The accompanying obstruction analysis is correct and
must be retained as a permanent disclaimer: this bound alone does **not**
prove FCBC or any backbone-finiteness claim, and future rounds citing it
must not silently drop the "pointwise, not cumulative" caveat.
