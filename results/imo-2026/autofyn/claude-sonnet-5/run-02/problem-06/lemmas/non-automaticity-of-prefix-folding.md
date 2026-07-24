## Non-Automaticity of Prefix Folding (CERTIFIED, round 7)

**Source.** `covering-system-construction`, round 7, Step 9.2.

**Depends on.** Nothing beyond elementary arithmetic; applies to any strictly
increasing sequence of positive integers, not specific to this problem's greedy
recursion. Companion to `exact-equality-reduction-lemma.md`.

**Statement.** There exists a strictly increasing sequence of positive integers
(a_n)_{n≥1} that is eventually periodic in the gap sense — i.e. a_{n+T} = a_n + L holds
for all n ≥ N₀ for some positive integers T, L and some index N₀ — but for which **no**
pair of positive integers (T'', L'') satisfies a_{n+T''} = a_n + L'' for **every**
n ≥ 1. In particular, "eventual periodicity from some N₀" does not, in general, imply
"literal periodicity from n=1" even after rescaling to a multiple of the eventual
period.

**Explicit example.** Define a_1 := 1, a_2 := 5, and a_n := 997 + n for n ≥ 3. This is
strictly increasing (1 < 5 < 1000 < 1001 < ...), and eventually periodic with T = 1,
L = 1 from N₀ = 3: for n ≥ 3, a_{n+1} = 997+(n+1) = (997+n)+1 = a_n + 1.

**Proof that no (T'',L'') works for all n ≥ 1.** Suppose such a pair existed.
Restricting the hypothesis to n ≥ 3 (where n+T'' ≥ 3 too, since T''≥1): a_{n+T''} =
997+n+T'' must equal a_n + L'' = 997+n+L'', forcing T'' = L''. Now apply the hypothesis
at n = 1, using T''=L'': a_{1+T''} = a_1 + T'' = 1+T''.
- If T'' = 1: this requires a_2 = 2, but a_2 = 5 ≠ 2 — contradiction.
- If T'' ≥ 2: then 1+T'' ≥ 3, so a_{1+T''} = 997+(1+T'') = 998+T'' by the formula for
  n≥3; the required equality 998+T'' = 1+T'' gives 998 = 1 — contradiction.

Both cases are impossible, so no valid (T'',L'') exists for any positive integer T''.
∎

**Scope.** A fully general negative result about strictly increasing integer
sequences with an eventually-periodic gap structure: it refutes, in general, any
"period-rescaling" mechanism (taking T'' to be a multiple of the eventual period T, or
any other single fixed multiple) as an automatic way to extend periodicity back to
n=1. Consequently, for any specific sequence (such as the greedy sequence of this
problem) for which literal periodicity from n=1 is sought, genuine use of the
sequence's own defining structure is required — the reduction of
`exact-equality-reduction-lemma.md` to finitely many equalities is not, by itself, a
formality.

**Status.** Correct, complete, no gaps, unconditional. Certified by the round-7
proof-reviewer: independently re-verified the counterexample by hand (a_2=5,
a_3=1000,...) and re-checked the case split (T''=1 vs T''≥2) — both derivations
correct, no gap.
