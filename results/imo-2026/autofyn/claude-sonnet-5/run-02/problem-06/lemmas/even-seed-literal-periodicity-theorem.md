# Even-Seed Literal Periodicity Theorem (certified round 16)

**Source.** `approaches/even-a1-full-periodicity-theorem.md`, round 16 build.
Independently re-verified (full re-derivation of both induction branches,
plus an independent Python simulation on seeds
6, 30, 210, 1994, 14, 22, 26, 4, 8, 34, 194, 2310) by the round-16
proof-reviewer. No gap found.

**Statement.** Let `a_1, a_2, ...` be the sequence defined by the problem
(`a_1 > 1`; for `n ≥ 1`, `a_{n+1}` is the smallest integer `> a_n` with
`gcd(a_{n+1}, a_i) > 1` for every `i = 1,...,n`). If `2 | a_1`, then
`a_n = a_1 + 2(n-1)` for every `n ≥ 1`; in particular `a_{n+1} = a_n + 2` for
every `n ≥ 1`, so `T = 1, L = 2` witness the problem's conclusion literally
from `n = 1` (not merely eventually).

**Proof.** Strong induction on `n`. Base case `n=1` trivial. Inductive step:
assume `a_i = a_1+2(i-1)` for `i ≤ n` (so every `a_i`, `i≤n`, is even, since
`a_1` is even and `2(i-1)` is even). Then:
- `a_n+1` is illegal for `a_{n+1}`: `gcd(a_n+1, a_n) = 1` since consecutive
  integers are coprime (independent of parity).
- `a_n+2` is legal: it is even (sum of two even numbers), so
  `gcd(a_n+2, a_i) ≥ 2 > 1` for every `i ≤ n` (each `a_i` even by hypothesis).
- Since no integer lies strictly between `a_n+1` and `a_n+2`, and the former
  is illegal while the latter is legal, minimality of the problem's own
  definition of `a_{n+1}` (as the minimum of the legal-candidate set) forces
  `a_{n+1} = a_n + 2` exactly.
This gives `a_{n+1} = a_1+2(n-1)+2 = a_1+2n`, closing the induction (and
`a_{n+1}` is again even, so the hypothesis propagates). ∎

**Scope note (not overclaimed by the source).** This theorem does NOT
generalize to odd `a_1`, or to seeds whose smallest prime factor `p ≥ 3`
(the "two-candidate dichotomy" argument needs `p=2` specifically: for
`p ≥ 3` there are `p-2 ≥ 1` intermediate candidates between the
always-illegal `a_n+1` and the first multiple of `p` above `a_n`, and bare
coprimality with `a_n` alone does not settle their legality against the
full history). It is a strictly easier, self-contained mechanism (no
persistent-type / FAH machinery), not a special case obtainable by
specializing the general FAH-based machinery elsewhere in this workspace.

**Reusable content.** Strictly generalizes the previously certified `|Q|=1`
special case (prime-power even seeds only) to ALL even seeds, including
seeds with several distinct odd prime factors (e.g. `30 = 2·3·5`,
`210 = 2·3·5·7`). Fully resolves the problem's target for the infinite
subfamily `2 | a_1`. Usable as a free base case in any future case-split by
parity of `a_1` or by `min Q`.

**Uniform Evenness Lemma (byproduct, implicit in the induction above, used
elsewhere in the workspace — e.g. `n1-periodicity-reconciliation` §4.1).**
If `2 | a_1`, then `2 | a_n` for every `n ≥ 1`. (Immediate from the proof
above: each inductive step both uses and re-establishes evenness of every
term up to and including the new one.)
