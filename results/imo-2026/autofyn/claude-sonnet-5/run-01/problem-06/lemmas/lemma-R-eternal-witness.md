# Lemma R (eternal witness per index)

**Statement.** With `(a_n)` as in the problem, for every index `i\ge1`, there is a
prime `p\in P_i:=\mathrm{rad}(a_i)` such that `p\mid a_n` for infinitely many `n>i`.
(Call such a `p` an *eternal witness* for index `i`.)

**Proof.** Fix `i`. For every `n>i`, Lemma P′ (pairwise global intersection) gives
`\gcd(a_n,a_i)>1`, i.e. `P_n\cap P_i\ne\varnothing`. Define
`\varphi(n):=\min(P_n\cap P_i)` (a well-defined element of the finite set `P_i`) for
every `n>i`. This partitions the infinite index set `\{n:n>i\}` into at most
`|P_i|<\infty` classes `\varphi^{-1}(p)`, `p\in P_i`. By the infinite pigeonhole
principle (partitioning an infinite set into finitely many classes forces at least
one class to be infinite), some `p\in P_i` has `\varphi^{-1}(p)` infinite, i.e.
`p\mid a_n` for infinitely many `n>i`. $\blacksquare$

**Source.** Proved in full in `approaches/intersecting-family-covering-construction.md`
("Lemma R"), generalizing crux `aimo-0421`'s pigeonhole device from the single index
`i=1` to every index `i`. The proof as given there derives `\gcd(a_n,a_i)>1` for all
`n>i` inline, from the problem's definition directly; this is exactly Lemma P′
(certified separately in this folder), so the two certified lemmas are consistent
and Lemma R may cite Lemma P′ directly rather than re-deriving it.

**Certification.** Standard infinite-pigeonhole argument on a well-defined finite-valued
function of an infinite domain; no gaps. Certified `solved`-quality (sorry-free) by
the round-1 proof-reviewer. Note for reuse: the lemma gives an eternal witness
*existing for each fixed `i`*, but does **not** by itself give a single prime that is
an eternal witness for *every* `i` simultaneously, nor rule out the eternal witness
depending on `i`; strengthening this uniformity is exactly the open "backbone
finiteness" content that remains unresolved across all three round-1 approaches.
