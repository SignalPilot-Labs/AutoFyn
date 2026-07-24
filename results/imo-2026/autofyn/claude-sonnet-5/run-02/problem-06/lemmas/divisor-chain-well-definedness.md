## Lemma: Divisor-Chain Well-Definedness (certified)

**Source.** `covering-system-construction`, round 8, Step 8.9. Independently
re-verified by the proof-reviewer (round 8).

**Depends on (certified).** `free-facts-gcd.md`.

**Setup.** Fix any index n_A and let A' be an extended-persistent type with
ρ(n_A) = A'. For every n > n_A with ρ(n) = A', define d_n := gcd(a_{n_A}, a_n).

**Lemma.** For every such n, d_n is a divisor of the FIXED positive integer a_{n_A}
satisfying d_n > 1. In particular, as n ranges over the (infinite, since A' is
extended-persistent) set of A'-type indices beyond n_A, d_n ranges over a subset of
the FINITE set Div(a_{n_A}) \ {1}.

**Proof.** d_n = gcd(a_{n_A}, a_n) divides a_{n_A} by the definition of gcd, for
every n. Div(a_{n_A}) is finite since a_{n_A} is one fixed positive integer
(standard divisor-count finiteness, `knowledge_base.md` "Divisor analysis"). By the
certified Free Facts Lemma, gcd(a_i, a_j) > 1 for all i ≠ j; applying this with
i = n_A ≠ n gives d_n > 1. ∎

**Scope.** A purely bookkeeping fact — no dependence on any open hypothesis. Its
value is as a clean building block for any future pigeonhole-over-divisors attack
on FAH/Symmetric FAH (any such attack immediately gets, for free, that the sequence
of gcds with a fixed witness takes only finitely many values, hence some value
recurs infinitely often by pigeonhole).

**Status.** Correct, complete, elementary, unconditional. Certified as a standalone
reusable building-block lemma.
