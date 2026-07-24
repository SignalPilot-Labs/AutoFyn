## Exact-Equality Reduction Lemma (CERTIFIED, round 7)

**Source.** `covering-system-construction`, round 7, Step 9.1.

**Depends on.** Nothing beyond elementary case analysis; applies to any sequence of
integers, not specific to this problem's greedy recursion.

**Statement.** Let (a_n)_{n≥1} be any sequence of integers, and suppose T, L are
positive integers and N₀ ≥ 1 an index such that a_{n+T} = a_n + L holds for every
n ≥ N₀. Then:

a_{n+T} = a_n + L holds for **every** positive integer n

if and only if

a_{i+T} = a_i + L holds for each of the (N₀ − 1) indices i = 1, 2, ..., N₀ − 1.

**Proof.** (⟹) Immediate: if the identity holds for all n ≥ 1 it holds in particular
for each i ∈ {1,...,N₀−1}.

(⟸) Every positive integer n satisfies exactly one of "n < N₀" (i.e. n ∈
{1,...,N₀−1}) or "n ≥ N₀". In the first case the identity holds by hypothesis
(the assumed finitely many equalities); in the second case it holds by the given
eventual-periodicity hypothesis. Since these two cases exhaust all positive integers,
the identity holds for every positive integer n. ∎

**Scope.** A fully general, elementary fact about any eventually-periodic-gap integer
sequence: it exactly localizes "literal periodicity from n=1" to a **finite, explicit**
list of equalities (N₀ − 1 of them), ruling out any additional hidden global
consistency condition. It is a pure bookkeeping/case-split fact — it does NOT by
itself establish that the finitely many equalities hold (see the companion lemma
`non-automaticity-of-prefix-folding.md`, which proves this is a genuine additional
requirement, not automatic).

**Status.** Correct, complete, no gaps, unconditional. Certified by the round-7
proof-reviewer: independently re-derived (trivial case split, no hidden step);
correct as stated.
