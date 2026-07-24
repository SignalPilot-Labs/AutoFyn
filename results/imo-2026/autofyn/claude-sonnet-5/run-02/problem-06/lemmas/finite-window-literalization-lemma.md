## Lemma: Finite-Window Literalization Lemma (CERTIFIED, round 26)

**Source.** `covering-system-construction`, round 26, Step 4h Step 2.
Independently re-verified in full by the round-26 proof-reviewer.

**Depends on (certified).** `lemmas/singleton-side-fah.md`,
`lemmas/two-sided-singleton-witness-theorem.md` (for the surrounding
existence-hypothesis context, not logically required by this lemma's own
proof).

**Statement.** Let `(A',B')` be a rogue pair at core `S₀` with canonical
witnesses `n_A < n_B`. Suppose there is an index `x_1` with `ρ(x_1)=B'`
and `P(a_{x_1})\S₀={q}` a singleton. If, in addition, there is **no**
index `n` with `n_B<n≤x_1` and `ρ(n)=A'`, then `q|a_n` for **literally
every** `n>n_B` with `ρ(n)=A'` — zero exceptions, upgrading Singleton-Side
FAH's conclusion from cofinite to literal.

**Proof.** For `n>n_B` with `ρ(n)=A'`: either `n>x_1` (then Singleton-Side
FAH applied with far-side witness `x_1` gives `q|a_n` directly) or
`n_B<n≤x_1` (vacuous by the second hypothesis). These two cases are
exhaustive and mutually exclusive, so `q|a_n` in every case. ∎ (Two-line
case split; full statement in `approaches/covering-system-construction.md`
Step 4h Step 2.)

**Independent verification (this review).** (1) Confirmed the proof's
logic is a valid, non-circular composition of the certified Singleton-Side
FAH Lemma (whose Setup explicitly allows "any valid witness," not just
canonical/earliest) with a finite, directly-checkable side condition — no
gap. (2) Applied to `a_1=4807` (`S₀={2,3,5,11,19,23}`, `A'={3,5,19}`,
`B'={2,11}`, `n_A=6`, `n_B=7`, `x_1=72`, `q=17`): independently
re-simulated the full sequence `a_1,…,a_80` from scratch (own greedy
generator) — **exact match, term by term and factorization by
factorization**, with the source file's displayed table, confirming
`x_1=72` (`a_{72}=5984=2^5·11·17`, singleton `{17}`) and confirming **no**
`A'`-occurrence in `(7,72]`. (3) Independently extended the simulation to
45,000 terms (fast sieve-based factorization up to `2×10^6`): found exactly
70 `A'`-occurrences with `n>7`, all with `gcd(a_n,a_7)∈{17,221}` and
**none** equal to `13` — exact match with the source file's independent
cross-check, confirming the residual class `d=13` never occurs for this
seed.

**Status.** Correct, complete, unconditional given its two explicit
hypotheses (the singleton-witness existence hypothesis and the finite
window-vacancy check, both individually verified for `a_1=4807` in the
source file). Reusable by any approach that has secured a Two-Sided-
Singleton-Witness-style existence hypothesis and wants literal rather than
cofinite FAH — general existence of such a witness for arbitrary `a_1` is
NOT established (an honestly-flagged open scope limitation of the source
approach, not of this lemma itself).
