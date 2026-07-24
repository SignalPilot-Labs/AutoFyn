## Lemma: Confined-GCD Lemma (certified)

**Source.** `cofinite-window-capacity-bound`, round 9. Independently re-verified by
the proof-reviewer (round 9).

**Depends on (certified).** `free-facts-gcd.md`. Setup uses the definition of
extended type `ρ(n) := P(a_n) ∩ S₀` and the rogue-pair hypothesis `A' ∩ B' = ∅`.

**Setup.** Fix a rogue pair `(A',B')` (disjoint `S₀`-extended-persistent types) with
witnesses `n_A < n_B`, `F'' := P(a_{n_B}) \ S₀`. Let `b := ∏_{p ∈ F''} p^{v_p(a_{n_B})}`
(the `F''`-part of the fixed integer `a_{n_B}`).

**Lemma.** For every `n > n_B` with `ρ(n) = A'`, writing `g_n := gcd(a_n, a_{n_B})`:
(a) `g_n | b` (in particular `g_n` ranges over the FIXED finite set `Div(b)`,
independent of `n`); (b) `g_n > 1`; (c) for any prime `q* ∈ F''`, `q* | a_n ⟺ q* | g_n`.

**Proof.**
(a) Let `r` be a prime factor of `g_n`. If `r ∈ S₀`, then `r ∈ P(a_n) ∩ S₀ = ρ(n) = A'`
and `r ∈ P(a_{n_B}) ∩ S₀ = ρ(n_B) = B'`, so `r ∈ A' ∩ B' = ∅` — contradiction. Hence
every prime factor of `g_n` lies in `P(a_{n_B}) \ S₀ = F''` (using `g_n | a_{n_B}`),
each to a power at most its power in `a_{n_B}` (since `g_n | a_{n_B}`). This is
exactly the definition of a divisor of `b`. So `g_n | b`.
(b) Immediate from Free Facts applied to `n ≠ n_B`.
(c) (⇐): `g_n | a_n`, so `q*|g_n ⟹ q*|a_n`. (⇒): if `q*|a_n`, and `q* ∈ F'' ⊆
P(a_{n_B})` so `q*|a_{n_B}`, then `q*` divides both `a_n` and `a_{n_B}`, hence
`q* | gcd(a_n,a_{n_B}) = g_n`. ∎

**Scope.** Gives a clean finite-alphabet ("divisor-class") recast of the FAH
exception set `E = {n > n_B : ρ(n)=A', q* ∤ a_n} = ⋃_{d ∈ D_bad} {n : g_n = d}`, where
`D_bad := {d ∈ Div(b) : d>1, q* ∤ d}` — a fixed finite index set. Strictly stronger
than, and independent of, the certified Divisor-Chain Well-Definedness Lemma (which
only bounds `gcd(a_{n_A},a_n)` by divisors of `a_{n_A}` without pinning prime factors
to `F''` specifically): this Lemma additionally uses rogueness (`A'∩B'=∅`) to rule
out every `S₀`-prime from `g_n`, confining it to `F''`-primes alone.

**Status.** Correct, complete, no gaps, fully unconditional (no dependence on any
open hypothesis — proved from Free Facts and the definitions alone). Independently
re-derived by the reviewer. Does NOT by itself resolve Cofinite FAH or literal FAH
(see `cofinite-window-capacity-bound` Section 4 for the precisely-located stall: the
only certified counting tool, infinite pigeonhole, yields some infinite divisor-class
but not exclusivity of the `q*`-class, and no certified tool links `g_n` across
different `n`). Certified as a standalone reusable building-block lemma.
