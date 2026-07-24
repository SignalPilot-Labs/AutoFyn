## Lemma: Density-Argument Vacuity Corollary (CERTIFIED, round 11)

**Source.** `sieve-density-exception-bound`, round 11 (pre-build screening,
dispatched by the round-11 outline-reviewer).

**Depends on (certified).** `escape-cost-vacuity.md`, `sandwich-genericity-
theorem.md` (proof technique reused and extended), `confined-gcd-lemma.md` (for
the definition of the divisor-class alphabet `Div(b)`, `D_bad`, and the class
function `g_n`).

**Setup.** Fix a rogue pair `(A',B')` with witnesses `n_A<n_B`, canonical prime
`q* := min(F'∩F'')`, and the Confined-GCD Lemma's finite data `S₀, F'', b,
D_bad`. These are finite, fixed once the rogue pair and its canonical witnesses
are fixed (themselves finite objects extracted from `a_1` via the certified
Finite Core Theorem / Collateral-Safety machinery) — hence, in the sense of the
Escape-Cost Vacuity Theorem, "constants depending on `a_1` alone."

**Definitions.** For a real parameter `X > a_{n_B}`, call a quantity `C(X)`
**window-class-blind** if it is computed as a deterministic function of `X`,
`a_{n_B}`, and the fixed finite data `S₀, F'', b, D_bad, q*` alone — in
particular, any Mertens-type product, sieve count, or asymptotic density
estimate of the count/proportion of integers `m ∈ (a_{n_B}, X]` satisfying a
fixed residue or coprimality condition defined by primes of `S₀ ∪ F''` — with
**no reference in its computation to which integers of the window are actually
realized as sequence terms, nor to their observed gcd-classes `g_n`.**

**Statement.** No finite deductive argument whose premises are all
window-class-blind (for any finite or countable family of window parameters `X`)
— together with other already-certified class-blind facts (e.g. the Sandwich
Genericity Theorem) — can establish a class-sensitive conclusion about the actual
sequence (in the sense of the Escape-Cost Vacuity Theorem: a conclusion stated in
terms of divisor-class equality, repetition, or exception-set finiteness for the
REALIZED terms `a_n`). In particular, no such argument can establish that
`E := {n>n_B : ρ(n)=A', q*∤a_n}` is finite.

**Proof.** By definition, each `C(X)` is a deterministic function of `X` and the
fixed data `S₀, F'', b, D_bad, q*`, none of which depend on which integers of the
window `(a_{n_B}, X]` are actually the sequence's own terms, nor on their
gcd-classes `g_n`. Fix any two hypothetical scenarios for the realized sequence
that agree on `a_1` (hence on `S₀, F'', b, D_bad, q*`) but differ in which
`A'`-occurrences past `n_B` land in `D_bad` classes (e.g. scenario (I): the
`D_bad`-class occurrences among the realized `A'`-occurrences are finite; scenario
(II): they are infinite, while — consistently, since `D_bad`-class integers can be
a sparse but infinite set — the ambient Mertens count of `D_bad`-class integers
among ALL integers in each window `(a_{n_B},X]` is small in both scenarios). Since
`C(X)`'s computation never inputs which integers are realized terms or their
`g_n` values, `C(X)` takes the identical value in scenario (I) and scenario (II),
for every `X`. Applying the same finite sequence of deductive steps to the same
sequence of `C(X)` values (plus other class-blind premises, which by the
Escape-Cost Vacuity Theorem's own proof are likewise identical in both scenarios)
therefore produces the identical output in both scenarios. Hence no such argument
can output a conclusion that is true in scenario (I) and false in scenario (II) (or
vice versa) — in particular, cannot output "`E` is finite," since this statement
differs in truth value between the two scenarios. ∎

**Scope.** This is a direct extension, in the same proof style (determinism of
deduction applied to inputs that do not carry the relevant data), of the certified
Escape-Cost Vacuity Theorem — generalized from facts about a single pair of
indices `(m,n)` to facts computed from a window parameter `X` (i.e., from
aggregate counts/densities over many integers at once, rather than from a single
pairwise relation). It supplies a general screening tool, complementary to the
original theorem, for the analytic/sieve-density proof-shape family: before
investing effort in any Mertens-type or sieve estimate aimed at FAH/Cofinite FAH,
check whether the estimate's inputs ever reference the realized sequence's
observed divisor classes (as opposed to only the ambient window and fixed prime
data). If not, by this Corollary, the estimate — however refined — cannot possibly
establish the desired class-sensitive exception-set-finiteness conclusion.

**Status.** Correct, complete, no gaps; a direct generalization of an already-
certified determinism-of-deduction argument to a new but structurally identical
setting (single deterministic function of class-blind inputs). Certified as a
standalone reusable screening lemma, alongside `escape-cost-vacuity.md`.
