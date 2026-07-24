## Statement (Lemma 25)

Let $F=\{v_1,v_2\}\cup P$ with $v_1>v_2>0$ and $P$ an exactly-paired
multiset (every value in $P$ appears an even number of times), and let $G$
be **any** finite multiset of positive reals (no ladder structure, no
legality restriction needed — a fully general algebraic fact about $A$).
Write $F_1:=\{v_1\}\cup P$, $F_2:=\{v_2\}\cup P$ (each with $\ell(\cdot)=1$).
Then
$$A(F\cup G) = A(G) + A(F_1\cup G) - A(F_2\cup G),$$
where $A(S):=\sum_i(-1)^{i+1}L_i$ (alternating sum over $S$ sorted
descending).

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
new Lemma 25 (round 11). By the odd-run-reduction fact, the odd-parity
indicator of $F$ is $u_F(x)=\mathbb1[v_2\le x<v_1]$, so
$A(F)=v_1-v_2$. Applying the certified `cross-term-identity-threshold`
(Lemma 8) to the pairs $(F,G)$, $(F_1,G)$, $(F_2,G)$ separately and using
$\mathbb1[v_2\le x<v_1]=\mathbb1[x<v_1]-\mathbb1[x<v_2]$ pointwise, the
three cross-term integrals solve linearly for the stated identity (full
algebra in the approach file).

## Certification note

**CERTIFIED — proof-reviewer, round 11.** Independently re-derived and
re-verified with a fresh, from-scratch script (not the builder's own),
using the project's own definition $A(S)=\sum(-1)^{i+1}L_i$ (the reviewer's
first attempt used a different, incompatible convention — literal
game-value/odd-sorted-rank-sum — and spuriously found near-100% mismatches;
once corrected to the file's own $A$ convention, 5000/5000 random
exact-`Fraction` trials over arbitrary non-ladder multisets matched
exactly, zero mismatches). This is a genuinely general, ladder-independent
identity, reusable by any future approach reducing an $\ell(F)=2$
computation to two $\ell(F)=1$ computations.
