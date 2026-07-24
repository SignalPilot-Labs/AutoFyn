## Status
partial

## Approaches tried
- **witness-depth-bound** (round 3, new). Corrected the outline's claim per the
  outline-reviewer's falsification (first-occurrence index of a persistent type is NOT
  a function of |Q| alone — index ranged 35–489 across four a_1 with |Q|=4 in the
  reviewer's simulation, confirmed independently below) to the weaker, still a priori
  claim: first-occurrence index is a function of a_1 itself (equivalently of Q together
  with its element sizes), not of the sequence's later behavior. Attempted to prove this
  corrected claim by an explicit pigeonhole/CRT construction. **Result: genuinely
  stalls** — identified and documented below a structural obstruction (the
  "simultaneous-reconciliation" effect) that blocks any closed-form a priori bound
  derivable from the currently certified lemmas, and confirmed by an independent,
  larger numerical run that no simple candidate formula (linear in p_max, linear in
  ΣQ, linear in a_1, or in the product ∏Q) fits the data. Additionally identified and
  recorded a **scope problem**: even a full proof of the corrected claim would NOT by
  itself close gap (†) as currently framed in `current.md`, because the Finite Core
  Theorem already gives an unconditionally finite core S with no depth bound needed —
  the actually open question is whether the S₀-recruitment process beyond S terminates,
  which an explicit-depth-for-S argument does not address. This is reported honestly
  rather than papered over, per the "no fake solved" rule.

## Current best
The following is fully proved this round (elementary, but load-bearing for framing the
obstruction precisely) and can be imported by any approach:

**Proposition (Base-Type Occurrence at n = 1).** Q itself is realized as a type at
n = 1: τ(1) = P(a_1) ∩ Q = Q ∩ Q = Q, since Q := P(a_1) by definition. Hence the
"full" type Q ∈ 𝒫 automatically has first-occurrence index 1, needing no argument.
(Trivial, but isolates that the hard case of the corrected claim is entirely about
proper subsets B ⊊ Q.)

**Restatement of the corrected claim (per outline-reviewer's fix).** For each type
B ⊆ Q that is EVER realized (∃ n with τ(n) = B), there is an explicit function
f(a_1) — computable directly from the factorization of a_1, with no reference to the
realized sequence — such that the first index n with τ(n) = B satisfies n ≤ f(a_1).

### Attempted proof and where it stalls

The natural strategy is a pigeonhole/pumping argument: since there are only
2^{|Q|} − 1 possible nonempty types, and the Generalized Bounded Gap Lemma
(`generalized-bounded-gap-lemma.md`) bounds how fast a_n can grow, one might hope to
show that if B has not occurred within some window of explicit length W(a_1), some
other already-realized type must recur so densely that B is permanently excluded —
forcing B to occur (if it ever does) within W(a_1). This was flagged by the outliner
as the mechanism to attempt; we attempted it and it fails at the following precise
step.

**Step attempted.** Fix n > N_0 (Persistent-Type Pigeonhole threshold) with
τ(n) ∈ 𝒫 already known to occur infinitely often for finitely many types. Suppose type
B ∈ 𝒫 has not yet occurred by index n. We tried to bound how much longer B can be
avoided by using the Bounded Witness Lemma and Free Facts to constrain a_{n+1}'s legal
candidates.

**Where it breaks.** The Free Facts lemma requires gcd(a_{n+1}, a_i) > 1
simultaneously for EVERY i = 1, ..., n — not merely for the most recent term or for a
bounded window. As more distinct types get realized among a_1, ..., a_n, the smallest
legal a_{n+1} must reconcile with ALL of them at once, which (as the certified
`generalized-bounded-witness-lemma.md`'s recruitment corollary already shows in the
S₀-level setting) can force a_{n+1} to recruit a completely new prime outside Q ∪ S
rather than merely re-realizing an old type. There is no certified bound — nor did we
find one — on how many DISTINCT such reconciliation-forced primes can appear before
type B specifically is finally realized, because the identity of which prime gets
recruited at each step depends on the actual values a_1, ..., a_n already produced,
not on Q alone. In particular, an attempted "windowed pigeonhole" argument (β: if B is
avoided for W = 2^{|Q|}·K consecutive terms, some other type must repeat K+1 times,
and repeated realization of that OTHER type should force reconciliation... hence
force B) does not go through: repeated realization of a type A ≠ B, even many times,
only produces (via the Bounded Witness Lemma) new witness PRIMES for reconciling A
against other already-seen types — it never forces the SPECIFIC type B to become
legal, because B's non-occurrence might simply mean the greedy rule never needs to
"choose" B's exact Q-signature; the sequence can satisfy all gcd-constraints using a
different available type + a recruited outside prime instead. This is exactly the
mechanism that makes gap (†) hard in the first place (recruitment can substitute for
reconciliation with a *specific* type), so the obstruction here is the same
underlying difficulty as (†), not an independent one — see "Scope observation" below.

**Conclusion of the attempt.** We were unable to produce an explicit closed-form
f(a_1). This is recorded as an honest gap, not asserted false: we did not find a
counterexample showing NO such f(a_1) exists (unlike round 2's "universal glue prime,"
which was actively falsified by an explicit computation); we simply could not
construct one from the currently certified lemma set, and identified the precise
obstruction (simultaneous multi-term reconciliation is history-dependent, not
Q-alone-dependent) that any future attempt must overcome.

### Numerical check (per the outline-reviewer's instruction to re-run a magnitude-scaling
check before investing further)

We independently reproduced the outline-reviewer's four data points with a direct
trial-division greedy simulator (`sympy.gcd`/`sympy.factorint`, no shortcuts), and
extended the simulation window to N = 1500 terms to make sure the reported maxima were
not truncation artifacts:

| a_1 | Q | max first-occurrence index | distinct types seen (of 2^{|Q|}−1 = 15) |
|---|---|---|---|
| 210 = 2·3·5·7 | {2,3,5,7} | 36 | 8 |
| 1155 = 3·5·7·11 | {3,5,7,11} | 114 | 15 |
| 5005 = 5·7·11·13 | {5,7,11,13} | 214 | 15 |
| 96577 = 13·17·19·23 | {13,17,19,23} | 489 | 15 |

(Indices differ from the outline-reviewer's by ±1 due to a 0- vs 1-indexing
convention in the simulator; the scaling pattern is identical, confirming the
falsification independently.) We then tested whether any of four simple closed-form
candidates fit: max-index / p_max (Q's largest prime) gives 5.14, 10.36, 16.46, 21.26
across the four cases — not constant, and not even monotonically clean in p_max
alone (a1 = 5005 has p_max = 13 but ratio 16.46, exceeding a1 = 96577's ratio-per-unit
p_max of 21.26/23 ≈ 0.92 vs 16.46/13 ≈ 1.27); max-index / (sum of Q) similarly fails to
stabilize (2.12, 4.38, 5.94, 6.79). **No simple monomial-in-(p_max or ΣQ) fit works**,
which is consistent with — though does not prove — the structural obstruction
identified above: the index depends on the specific interaction pattern among Q's
primes during the greedy process, not on a single summary statistic of Q.

Notably, a_1 = 210 realizes only 8 of the 15 possible nonempty subsets of Q within
1500 terms (the other 7 subsets may be non-persistent types that never recur, or may
occur only past index 1500 — we did not extend further, since resolving this is not
needed for the argument below and would not change the qualitative conclusion).

### Scope observation (the more important, fully rigorous finding this round)

Independent of whether the corrected claim is eventually provable, we record a
logical point about what it would and would not achieve, since it changes how much
value is at stake in resolving it:

**Claim.** A full proof of the corrected witness-depth-bound claim (an explicit
f(a_1) bounding first-occurrence indices) would NOT by itself close gap (†) as stated
in `current.md`.

**Justification.** The Finite Core Theorem (`finite-core-theorem.md`) already proves,
unconditionally and with no depth bound of any kind, that the core set
S = ⋃_{B ∈ 𝒫} (P(a_{m_B}) \ Q) is finite — this follows purely from 𝒫 being a finite
set (Persistent-Type Pigeonhole) and each P(a_{m_B}) being the prime-factor set of a
single fixed integer (hence finite), with no need to know m_B's numeric value at all.
An explicit numeric bound on m_B (which is what a proof of the corrected claim would
supply, since m_B is itself a first/witness-occurrence index) would make S's primes
explicitly computable in principle, which is a nice strengthening in kind but is
strictly weaker than what (†) requires. Gap (†), per `current.md`'s Step 4c
reformulation, is about whether the *recruitment process* — which starts from
S₀^(0) = Q ∪ S and iteratively adjoins NEW primes q ∉ S₀^(k) whenever the
Generalized Bounded Witness Lemma's Corollary (`generalized-bounded-witness-lemma.md`)
fires on a violating extended-type pair — terminates after finitely many rounds.
Bounding the ORIGINAL witnesses m_B (which only pins down S = S₀^(0) more explicitly)
says nothing about whether further rounds of recruitment beyond S are needed, since
those rounds are triggered by violations of the extended-persistent-type intersection
property, not by any depth bound on m_B. Hence even in the best case (corrected claim
fully proved with an explicit f(a_1)), this approach would produce a stronger, fully
explicit version of the already-certified Finite Core Theorem, but would leave gap (†)
exactly as open as it is now.

This is recorded honestly rather than silently discovered later: the value of
completing this approach is real but strictly smaller than initially hoped by the
outline (which framed it as "potentially bypassing gap (†) entirely"). Any future
round pursuing this slug should either (a) accept this narrower scope and pursue the
explicit-S₀ result as a standalone strengthening (useful for the record, not for
closing (†)), or (b) find a genuinely different depth-bound target that DOES speak to
the recruitment process (e.g. bounding the index depth at which *all* recruitment
rounds must have already fired, not just the index depth of original-S witnesses) —
which is a strictly harder claim than the one attempted here and was not attempted
this round due to time constraints.

## Full proof
Not present — Status is `partial`. The corrected witness-depth-bound claim (index
bounded by an explicit function of a_1) remains open, with the precise obstruction
(history-dependent simultaneous reconciliation, not a function of Q's static data
alone) identified and documented above rather than hand-waved past. Independently, even
a full proof of the claim would not close gap (†) — a scope limitation established
rigorously above and not previously recorded in `current.md`.

## Promotable lemmas
None proved to the point of reusability this round. The "Base-Type Occurrence at
n = 1" observation (τ(1) = Q) is correct but trivial (one line) and not worth
certifying as a standalone lemma file; any approach needing it can restate it inline.
