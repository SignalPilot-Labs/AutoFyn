# Key Lemma (ω-bound)

**Statement.** Suppose there is a fixed constant `M` with `ω(a_n)≤M` for every
`n≥1` (a hypothesis, not proved). Let `q*(n)` denote a prime factor of `a_n`
achieving the Domination Lemma's maximum `D_{n-1}(q*(n)) = max_j D_{n-1}(q_j)
≥ (n-1)/ω(a_n)` (well-defined for `n≥2`). Then

`q*(n) ≤ M·(a_1+L)` for every `n≥2`, where `L := rad(a_1)` (Lemma 1's
constant).

Consequently `Q := {q*(n) : n≥2}` is a **finite** set of primes, contained in
the set of primes `≤ M(a_1+L)` — conditional only on the hypothesis
`ω(a_n)≤M`.

**Proof.** Fix `n≥2`, write `x = a_n`, `r := ω(x) ≤ M`, and let `q* = q*(n)`
be a prime factor of `x` achieving the Domination Lemma's maximum, so
`D_{n-1}(q*) ≥ (n-1)/r`. Since `a_1,…,a_{n-1}` are `n-1` distinct positive
integers each `≤ a_{n-1}`, the number of them divisible by `q*` is at most
the number of multiples of `q*` in `{1,…,a_{n-1}}`, i.e.
`D_{n-1}(q*) ≤ ⌊a_{n-1}/q*⌋ ≤ a_{n-1}/q*`. Combining,
`(n-1)/r ≤ D_{n-1}(q*) ≤ a_{n-1}/q*`, so `q* ≤ r·a_{n-1}/(n-1)`.

By Lemma 1, `a_{n-1} ≤ a_1+(n-2)L`, so `a_{n-1}/(n-1) ≤ a_1/(n-1) + L ≤ a_1+L`
(using `a_1/(n-1) ≤ a_1` for `n≥2`). Substituting `r ≤ M`:
`q* ≤ M·(a_1+L)`.

Since this bound is independent of `n`, `Q ⊆ {primes ≤ M(a_1+L)}`, a finite
set. `∎`

**Dependencies.** Domination Lemma (`lemmas/domination-lemma.md`), Lemma 1
(`lemmas/lemma-1-uniform-gap-bound.md`). No circularity: this is a three-line
algebraic consequence, correctly re-derived independently by the reviewer
(matches the outline-reviewer's own hand-check).

**Status.** Conditional lemma — the hypothesis `ω(a_n)=O(1)` is explicitly
NOT proved anywhere in the workspace as of round 3 (open). This lemma is
certified as a correct conditional implication, not as an unconditional
result. It resolves only the "necessity" half of backbone finiteness; see
Propositions ND1/ND2 for proof that it does **not** by itself yield a valid
FCBC covering set (sufficiency is a separate, still-open question).

**Source.** `results/imo-2026-06/approaches/persistent-backbone-monovariant.md`
(round 3), "Round 3: the ω-boundedness algebra" section.

**Certification.** Independently re-derived by the reviewer from scratch;
algebra checked line by line, matches. No gaps. Certified `solved`-quality
(sorry-free), conditional on its stated hypothesis.
