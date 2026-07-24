## Lemma: Reduced-Alphabet Corollary (proposed for certification, round 12)

**Source.** `covering-system-construction`, round 12, Step 4g. Formalizes an
observation from this round's math-explorer (smallcase lens,
`/tmp/round-12/math-explorer-smallcase.md`): "D_bad often collapses to a single
residual divisor class once the Singleton-Side FAH Lemma is applied to strip off the
already-free direction."

**Depends on (certified).** `free-facts-gcd.md`, `confined-gcd-lemma.md`,
`singleton-side-fah.md`.

**Setup.** Fix a core `S₀ ⊇ Q` and a rogue pair — disjoint-base-type
`S₀`-extended-persistent types `(A', B')` — with witnesses `n_A < n_B` (`ρ(n_A)=A'`,
`ρ(n_B)=B'`). Let `F' := P(a_{n_A}) \ S₀`, `F'' := P(a_{n_B}) \ S₀`, and
`b := ∏_{p∈F''} p^{e_p}` with `e_p := v_p(a_{n_B})`, the `F''`-part of `a_{n_B}`
(exactly the `b` of the Confined-GCD Lemma).

**Hypothesis.** `F'` is a singleton, `F' = {q'}` (the symmetric statement, with `F'`
and `F''` exchanged, holds by the identical argument if instead `F''` is the
singleton).

**Corollary.**
(i) By the Singleton-Side FAH Lemma, `q' | a_n` for EVERY `n > n_A` with `ρ(n)=B'` —
the `B'`-side is fully resolved, zero exceptions.
(ii) For any `q* ∈ F''`, the `A'`-side FAH-for-`q*` exception set is
`E(q*) = {n>n_B : ρ(n)=A', g_n ∈ D_bad(q*)}` (`g_n := gcd(a_n,a_{n_B})`), where
`D_bad(q*) := {d ∈ Div(b) : d>1, q*∤d}`, and

  `|D_bad(q*)| = ∏_{p ∈ F''\{q*}} (e_p+1) − 1`,

a fixed, finite, explicit quantity computable from the single witness `a_{n_B}`
alone, independent of `n`. In particular, when `|F''|=2` with the non-`q*` prime
appearing to multiplicity `1` in `a_{n_B}` (the shape of every `|F''|=2` seed
concretely computed in this workspace to date — a_1=4807, 11305), `|D_bad(q*)|=1`.

**Proof.** (i) Direct application of Singleton-Side FAH's hypothesis `F'={q'}`.
(ii) By the Confined-GCD Lemma, `g_n | b`, `g_n>1`, and `q*|a_n ⟺ q*|g_n`, giving the
stated form of `E(q*)`. Every divisor `d` of `b=∏_{p∈F''}p^{e_p}` corresponds
bijectively (unique factorization) to a tuple of exponents `(f_p)_{p∈F''}`,
`0≤f_p≤e_p`; `q*∤d ⟺ f_{q*}=0`, so divisors with `q*∤d` correspond bijectively to
tuples `(f_p)_{p∈F''\{q*}}` with `0≤f_p≤e_p`, of which there are
`∏_{p∈F''\{q*}}(e_p+1)`. Exactly one of these (`f_p=0` for all `p`) is `d=1`, excluded
by the requirement `d>1` in the definition of `D_bad(q*)` (this requirement never
actually removes a genuine value of `g_n`, since `g_n>1` always by Free Facts /
Confined-GCD part (b)). Subtracting this one divisor gives the stated formula. ∎

**Scope.** Purely a bookkeeping/alphabet-size statement: it does not rule out any
element of `D_bad(q*)`, does not supply a new class-sensitive fact (the certified
Escape-Cost Vacuity Theorem, `lemmas/escape-cost-vacuity.md`, still forecloses every
magnitude-only route to eliminating even a single remaining class), and does not
generalize to a UNIFORM bound across all rogue pairs (larger `|F''|` or higher
multiplicities give a correspondingly larger, still-finite `|D_bad(q*)|`). Does NOT
resolve Cofinite FAH or literal FAH.

**Status.** Correct, complete, no gaps, fully unconditional (a one-line divisor-
counting corollary of two already-certified lemmas plus the Fundamental Theorem of
Arithmetic — no dependence on any open hypothesis). Verified against concrete data:
a_1=4807's rogue pair (`S₀={2,3,5,11,19,23}`, `F'={17}`, `F''={13,17}`,
`b=13·17=221`) gives `|D_bad(17)| = (1+1)−1 = 1`, matching direct enumeration
`Div(221)={1,13,17,221}`, `D_bad(17)={13}`. Proposed for certification as a
standalone, reusable, importable bookkeeping lemma (in particular for
`seed-coupling-induction`'s orphaned Lemma B).
