## Insert-Element Identity

**Source:** `approaches/greedy-halving-adversary.md`, round 22.
**Status:** CERTIFIED (proof-reviewer, round 22). Fully general, no ladder
structure or legality assumption needed.

### Statement

Let $T'=\{t_1\ge\dots\ge t_k\ge0\}$ be any finite multiset sorted
descending and $b\ge0$ any value. Let $j:=|T'_{>b}|$. Then
$$A(\{b\}\cup T')\ =\ 2A(T'_{>b})-A(T')+(-1)^j\,b,$$
where $A(\cdot)$ is the standard alternating sum (sorted descending, $+$
at odd rank, $-$ at even rank).

### Proof

Insert $b$ into $T'$'s sorted order at position $j+1$ (it lands strictly
after the $j$ elements exceeding it and no later, by definition of $j$).
The elements of $T'_{>b}$ keep their original local ranks $1,\dots,j$ and
hence their original alternating signs, contributing $A(T'_{>b})$. The
element $b$ itself sits at global position $j+1$, contributing
$(-1)^{(j+1)-1}b=(-1)^jb$. Every element of $T'_{\le b}$ (size $k-j$) is
shifted from local rank $i$ (within $T'_{\le b}$ alone) to global position
$j+1+i$; its sign flips relative to its local-rank sign iff $j$ is odd, so
the contribution of $T'_{\le b}$ to $A(\{b\}\cup T')$ is
$-(-1)^jA(T'_{\le b})$. Summing:
$$A(\{b\}\cup T')=A(T'_{>b})+(-1)^jb-(-1)^jA(T'_{\le b}).$$
Separately, splitting $T'$ itself at rank $j$ gives $A(T')=A(T'_{>b})+
(-1)^jA(T'_{\le b})$, i.e. $(-1)^jA(T'_{\le b})=A(T')-A(T'_{>b})$.
Substituting,
$$A(\{b\}\cup T')=A(T'_{>b})+(-1)^jb-\big(A(T')-A(T'_{>b})\big)
=2A(T'_{>b})-A(T')+(-1)^jb.\qquad\blacksquare$$

### Verification

Proof-reviewer independently re-implemented and re-verified this identity
from scratch (`/tmp/round-22/verify_gha.py`, "Insert-Element Identity"
test): $20{,}000$ random trials, multiset sizes $0$–$6$, random rational
entries and $b$ — **zero mismatches**. This is a genuine, generally-true
combinatorial identity, not merely a numerically-corroborated conjecture;
the hand proof above was independently re-derived (matches the builder's
own proof) before the numeric check was run.

### Application on file

Used in `greedy-halving-adversary.md` to give a structural (not
case-by-case) proof of why Case (b)'s remaining sub-range ("$v\ge a$",
needing $A(B)\ge f(n)$ for $B=\{b\}\cup T'$) cannot be closed by any
one-sided *lower* bound on $A(T')$ alone — since $A(T')$ enters the target
with a minus sign, a lower bound moves the required inequality in the
wrong direction. This diagnostic use is correct and does not itself close
any open gap.

### Scope note

Purely combinatorial (sorted-multiset rank-shift bookkeeping); no
dependency on the ladder or on legality of any cut. Safe to reuse whenever
a single non-dominant element is inserted into a sorted multiset and its
exact effect on the alternating sum must be tracked.
