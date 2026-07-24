## Lemma/Theorem: Unbounded Total Prime Support Theorem (CERTIFIED, round 24)

**Source.** `new-prime-recruitment-rate-bound`, round 24. Independently
re-verified in full by the round-24 proof-reviewer (every step re-derived
from scratch, including an independent check of the "Binomial Dominance"
sub-lemma and the final contradiction assembly).

**Depends on (certified).** `lemmas/bounded-gap-lemma.md` (`a_n ≤ n·a_1`).

**Statement.** For every valid sequence `(a_n)_{n≥1}` satisfying the
problem's hypotheses, the set `P_∞ := ⋃_{n≥1} P(a_n)` of all primes ever
dividing a term of the sequence is infinite.

**Proof (sketch, full derivation in `approaches/new-prime-recruitment-rate-bound.md`).**
Suppose `P_∞ = {p_1,...,p_k}` finite. Every `a_n` is then `P_∞`-smooth, so
the count `N(X)` of `P_∞`-smooth integers `≤ X` satisfies `N(X) ≤
(log_2 X+1)^k` (each of the `k` exponents is `≤ log_2 X`). Since
`a_1<...<a_n` are `n` distinct `P_∞`-smooth integers `≤ a_n`, `n ≤ N(a_n) ≤
(log_2 a_n+1)^k`; combined with the certified Bounded Gap Lemma
(`a_n≤n·a_1`), this gives, for every `n≥1`, `n ≤ (log_2 n + C)^k` where
`C:=log_2 a_1+1`. An elementary "exponential beats any fixed power of log"
argument (Binomial Dominance Lemma: for `K≥1,m≥2K`, `2^m≥(m/(2K))^K`, proved
directly from the Binomial Theorem) shows this inequality fails for `n=2^s`
once `s` exceeds an explicit, finite threshold `s_0(k)` depending only on
`k`, a contradiction. Hence `P_∞` is infinite. ∎

**Independent verification (this review).** Re-derived Steps A–D and Lemma A
from scratch; confirmed the algebra of the final division step
(`s/(2K)^K ≤ (1+C/s)^k ≤ 2^k` for `s≥C`, giving `s≤s_0(k):=2^k(2K)^K`) and
the resulting contradiction at an explicit `s^*>s_0(k)` with
`s^*≥max(2K,C)`. No gap found; this is a fully elementary, self-contained,
unconditional proof (no analytic number theory, no PNT/Chebyshev input) of
the standard "smooth numbers are sparse ⟹ total prime support of a
polynomially-growing distinct sequence is infinite" fact, specialized to
this problem's own certified linear growth bound.

**Relationship to H2 (important scope note, do not misapply).** This
theorem does **not** refute, and is fully compatible with, H2 (existence of
a finite self-absorbing core `S*`, per `lemmas/self-absorbing-core-theorem.md`):
self-absorption requires `P(a_j) ⊆ S*` only for the finitely many indices
`j = 1,...,N(S*)`; for every `j > N(S*)`, the certified machinery works
purely with `ρ_{S*}(j) := P(a_j) ∩ S*` and is silent about (and unaffected
by) any primes of `a_j` outside `S*`. So the divergence of `P_∞` can be
entirely realized by "vagabond" primes appearing past the finite
self-absorption threshold, never re-entering the core. **Do not cite this
theorem as evidence against H2's existence claim** — it settles a different,
unrestricted question.

**Status.** Correct, complete, unconditional. Reusable whenever a future
approach needs to know the sequence's total (unrestricted) prime support is
infinite, and — importantly — as a permanent closure of the "total/raw
prime support stays bounded" mechanism as a possible H2 attack route (it
cannot work, in its literal unrestricted form).
