## Lemma: Legendre Sieve Gap Bound (CERTIFIED, round 22)

**Source.** `a1-3q-subfamily-theorem`, round 22, closing Case (b) `n` even
`k≥1`. Self-contained; not previously present in `knowledge_base.md` or the
crux corpus (checked by the round-22 math-explorer,
`/tmp/round-22/math-explorer-jacobsthal.md`). Independently re-verified in
full by the round-22 proof-reviewer (every step re-derived from scratch, plus
an independent computational sanity check distinct from the builder's) —
promoted from certified-candidate to **certified**.

**Statement.** Let `M ≥ 2` be an integer with `r := ω(M)` distinct prime
factors. Then any window of `L` consecutive integers with `L ≥ 2^r(r+1)`
contains an integer coprime to `M`. Equivalently, the Jacobsthal-type gap
function satisfies `g(M) ≤ 2^{ω(M)}(ω(M)+1)`.

**Proof.**

*Step 1 (sub-lemma: `p_i ≥ i+1`).* Let `p_1 < p_2 < ⋯ < p_r` be the distinct
prime factors of `M` in increasing order. A strictly increasing sequence of
integers with first term `p_1 ≥ 2` has `i`-th term `p_i ≥ p_1+(i-1) ≥ i+1`.

*Step 2 (telescoping bound on the density factor).* Since `1-1/x` is
increasing in `x>0` and `p_i ≥ i+1`, `1-1/p_i ≥ 1-1/(i+1) = i/(i+1)` for each
`i`. All factors are positive, so
`∏_{i=1}^r (1-1/p_i) ≥ ∏_{i=1}^r i/(i+1) = 1/(r+1)`
(telescoping product).

*Step 3 (Legendre/inclusion-exclusion sieve identity).* Let `I` be a window
of `L` consecutive integers, and `S := #{n ∈ I : gcd(n,M)=1}`. Since
`gcd(n,M)=1 ⟺ gcd(n, rad(M))=1` (`rad(M)=p_1⋯p_r`), Möbius inversion gives
`S = Σ_{d | rad(M)} μ(d)·N_d`, where `N_d := #{n∈I : d|n}`. Writing
`I=\{a+1,…,a+L\}`, `N_d = ⌊(a+L)/d⌋-⌊a/d⌋ = L/d + e_d` with `|e_d|<1` (a
standard floor-difference estimate). So
`S = L·Σ_{d|rad(M)} μ(d)/d + Σ_{d|rad(M)} μ(d)e_d = L·∏_{i=1}^r(1-1/p_i) + E`,
where `|E| ≤ Σ_{d|rad(M)} |e_d| < 2^r` (`rad(M)` squarefree has exactly `2^r`
divisors).

*Step 4 (assemble).* Combining Steps 2–3: `S > L/(r+1) - 2^r`. If
`L ≥ 2^r(r+1)`, then `L/(r+1) ≥ 2^r`, so `S > 0`; since `S` is a nonnegative
integer, `S ≥ 1`, i.e. the window contains an integer coprime to `M`. ∎

**Status.** Correct, complete, unconditional, fully elementary (Legendre's
sieve / inclusion-exclusion + a one-line telescoping estimate; no analytic
number theory, no Chebyshev/PNT-level input). Independently sanity-checked
by direct computation against known/computed Jacobsthal-function values
(`M=6,10,30,210,2310,30030,…`, `ω` up to 6): the bound holds with wide margin
in every case (e.g. `g(30030)=22 ≤ 448`), confirming it is a valid, if not
tight, upper bound — tightness was never required for the application.
**Caveat:** the bound is intentionally crude (loses a factor of roughly
`(r+1)` versus known sharper Jacobsthal-function estimates); it is designed
to be easy to prove outright, not to be optimal. Reusable whenever a future
approach needs *some* explicit, fully elementary upper bound on the maximal
gap between integers coprime to a modulus `M`, expressed purely in terms of
`ω(M)`.
