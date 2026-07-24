## Statement

Let $M$ be any finite multiset of positive reals and let $v>0$ be any
value (not required to already occur in $M$). Then
$$A(M\cup\{v,v\})\ =\ A(M),$$
where $A(\cdot)$ is the alternating-sum-of-sorted-descending-order
functional of `odd-run-reduction-lemma`.

**Corollary (iterated).** For any finite sequence of values
$v_1,\dots,v_k>0$ (each possibly repeated, possibly coinciding with each
other or with elements of $M$),
$$A\bigl(M\cup\{v_1,v_1\}\cup\{v_2,v_2\}\cup\dots\cup\{v_k,v_k\}\bigr)\ =\
A(M).$$

## Proof

By `odd-run-reduction-lemma`, $A$ of any multiset $S$ equals $A$ of its
odd-run reduction $S'$: for every distinct value $w$ occurring in $S$
with multiplicity $\mu_S(w)$, $S'$ keeps one copy of $w$ if $\mu_S(w)$ is
odd and zero copies if $\mu_S(w)$ is even.

Compare $S:=M\cup\{v,v\}$ with $M$. For every value $w\ne v$,
$\mu_S(w)=\mu_M(w)$ (appending two copies of $v$ leaves every other
value's count untouched), so $w$ survives the reduction of $S$ with the
same multiplicity ($0$ or $1$) as it survives the reduction of $M$. For
$w=v$, $\mu_S(v)=\mu_M(v)+2$, which has the same parity as $\mu_M(v)$
(adding $2$ never changes parity, regardless of whether $v$ already
occurred in $M$ zero, one, or more times), so $v$ survives the reduction
of $S$ (with exactly one copy) iff it survives the reduction of $M$.
Hence the odd-run reductions of $S=M\cup\{v,v\}$ and of $M$ are the
identical multiset, so $A(S)=A(M)$.

The iterated corollary follows by applying the one-step case $k$ times in
succession (each application only requires the previous multiset and one
new value $v_i$, matching the hypothesis exactly).

## Discussion

This isolates, as a standalone reusable fact, a pattern the project's
chamber-construction toolbox (`case-b2-n3-covering-closure`,
`double-sandwich-chambers`, the Bisect-family chambers throughout
`lp-duality-certificate.md`) has used repeatedly but never certified by
name: "bisecting a piece exactly (or pinning one fragment of a cut to
match another piece's value exactly) erases its contribution to the
alternating sum $A$, unconditionally, with no genericity/non-coincidence
assumption needed" — because the corollary's proof only tracks parity,
which is insensitive to any accidental coincidence between $v$ and other
values already present. This was the key mechanism enabling a clean,
casework-free derivation of the four Gap-Filler chambers (A, B, C, E) in
`results/imo-2026-03/approaches/lp-duality-certificate.md`, §R27.2.

## Verification

Independently checked by 2000 exact-`Fraction` random trials
(`/tmp/round-27/verify_formulas.py`, run by the round-27
`lp-duality-certificate` builder): for random $4$-tuples
$p_1\ge p_2\ge p_3\ge p_4>0$, the four chamber formulas derived via this
corollary (each requiring one or two applications) were verified to match
a direct sort-and-alternate-sum computation on the full, un-reduced
fragment multiset in every trial, zero mismatches.

## Certification note

CERTIFIED round 27. Elementary and correct: a two-line parity argument
from `odd-run-reduction-lemma` alone (independently re-derived by the
proof-reviewer). Independently re-verified by a fresh script computing
`A(M∪{v,v})` and `A(M)` directly via sort-and-alternate-sum for random
multisets and values $v$ (including $v$ coinciding with existing elements
of $M$): zero mismatches.
