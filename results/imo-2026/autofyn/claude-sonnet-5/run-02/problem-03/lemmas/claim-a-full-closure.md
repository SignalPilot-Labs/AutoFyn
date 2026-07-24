# Claim (A) — Full Closure

**Certified:** round 8, from `rank-pigeonhole-budget.md` §6, combining §2
(achievability), §3 (`case-ii-closure-theorem.md`), and §5
(`case-i-closure-theorem.md`). Reviewer independently re-verified the
achievability construction $F^\ast$ exactly for $n=1,\dots,9$
(`/tmp/round-8/verify_achievability.py`) — including correcting an
off-by-one in the construction's cut count (it uses exactly $n$ cuts, i.e.
Xiang Yu's *entire* budget, not $n-1$ as an earlier round's prose stated;
the identity itself was never wrong, only the cut-count claim in its
prose).

**Statement.** For every $n\ge1$: writing $T=\{p_2,\dots,p_{n+1}\}$ (the
$n$-ladder's tail, untouched) and $a_n=1/(2^{n+1}-1)$,
$$\min_{F}\ A(F\cup T)\ =\ a_n,$$
where $F$ ranges over all partitions of $p_1$ into at most $n$ cuts (i.e.
$\le n+1$ parts), the minimum attained exactly by
$F^\ast=\{p_2,\dots,p_n,p_{n+1},p_{n+1}\}$ (using exactly $n$ cuts).

**Scope — read carefully.** This is the "Xiang Yu spends his *entire*
budget fragmenting $p_1$, leaving the rest of the tail completely
untouched" sub-case of the whole `imo-2026-03` lower bound. It does **not**
by itself establish the general lower bound $A(S)\ge a_n$ for an arbitrary
legal Xiang Yu response $S$ (cuts split between $p_1$ and the tail in any
way) — that additionally needs "Claim (B)" (`greedy-halving-adversary`'s
target, open in general as of round 8: proved only for fully-paired $F$
with leftover cut budget, `cross-term-vanishing-lemma`/Proposition 16), nor
does it address the general upper bound (`lp-duality-certificate`'s target,
open as of round 8).
