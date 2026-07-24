## Lemma: Sandwich Genericity Theorem (CERTIFIED, round 10)

**Source.** `covering-system-construction`, round 10, Step 11.6.

**Depends on (certified).** `bounded-gap-lemma.md`, plus strict monotonicity of the
sequence (immediate from the problem's greedy "smallest legal integer `> a_n`"
definition).

**Statement.** For all indices `1 ≤ m < n` of the sequence (no restriction to any
type, extended type, or divisor class), `n - m ≤ a_n - a_m ≤ (n-m)·a_1`, with both
bounds depending only on `m`, `n`, and the fixed constant `a_1` — in particular
independent of `τ(m), τ(n), ρ(m), ρ(n)`, or any divisor-class datum such as
`gcd(a_m, a_n)`.

**Proof.**
*Lower bound.* The sequence is strictly increasing (`a_{i+1}` is by definition the
smallest integer strictly greater than `a_i` satisfying the pairwise-gcd condition,
so `a_{i+1} > a_i`; since all terms are integers, `a_{i+1} ≥ a_i + 1`). Telescoping
`a_{i+1} ≥ a_i + 1` for `i = m, ..., n-1` gives `a_n ≥ a_m + (n-m)`.
*Upper bound.* By the certified Bounded Gap Lemma, `a_{i+1} ≤ a_i + a_1` for every `i`.
Telescoping for `i = m, ..., n-1` gives `a_n ≤ a_m + (n-m)·a_1`. ∎

**Scope.** A short, fully unconditional corollary of already-certified facts. Its
value is purely as a screening tool (see the companion Escape-Cost Vacuity Theorem):
it shows that any magnitude-only argument built from the (Generalized) Bounded Gap
Lemma carries zero divisor-class-discriminating information, since both its bounds
and constants are literally the same formula for every pair of indices regardless of
type or class.

**Status.** Correct, complete, no gaps, fully unconditional (uses only the certified
Bounded Gap Lemma and the sequence's defining strict-monotonicity property).
**Independently re-verified by the round-10 proof-reviewer** — a direct two-line
telescoping argument, re-derived from scratch and confirmed identical. Certified.
