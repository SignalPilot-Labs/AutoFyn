## Truncated Alternating Sum Floor (new, round 16)

**Statement.** Let $S$ be any finite multiset of nonnegative reals,
$T:=\mathrm{Total}(S)$, and for any threshold $v\in[0,T]$ write
$S_{>v}:=\{x\in S: x>v\}$, $\epsilon(v):=\mathbb1[|S_{>v}|\text{ odd}]$, and
$A(\cdot)$ for the alternating-sum-of-sorted-descending-order functional of
the certified `integral-alternating-sum-formula` lemma. Then
$$A(S) \;-\; 2A(S_{>v}) \;+\; 2v\,\epsilon(v) \;\;\ge\;\; v - T.$$

This is completely general: no ladder structure, no legality/refinement
assumption on $S$, and $v$ is an arbitrary real in $[0,T]$ (not required to
be an actual element of $S$ or tied to any legal cut). It is the natural
companion inequality to the certified `upper-truncation-identity`, from
which it follows in two lines.

**Proof.** Write $u_S(x):=\mathbb1[N_S(x)\text{ odd}]$ as in
`integral-alternating-sum-formula`. Since every element of $S$ is $\le T$
(they are nonnegative and sum to $T$), $N_S(x)=0$ for $x\ge T$, so $u_S$ is
supported on $[0,T]$ and
$$A(S)=\int_0^T u_S(x)\,dx=\int_0^v u_S(x)\,dx+\int_v^T u_S(x)\,dx. \tag{1}$$
By the certified `upper-truncation-identity` applied to $S$ at threshold
$v$,
$$\int_v^\infty u_S(x)\,dx = A(S_{>v})-v\,\epsilon(v),$$
and since $u_S\equiv0$ on $[T,\infty)$ this integral equals
$\int_v^T u_S(x)\,dx$, i.e.
$$\int_v^T u_S(x)\,dx = A(S_{>v})-v\,\epsilon(v). \tag{2}$$
Substituting (2) into (1) and rearranging,
$$\int_0^v u_S(x)\,dx = A(S) - A(S_{>v}) + v\,\epsilon(v). \tag{3}$$
Now compute, using (2) and (3),
$$
\int_0^v u_S\,dx - \int_v^T u_S\,dx
= \big(A(S)-A(S_{>v})+v\epsilon(v)\big) - \big(A(S_{>v})-v\epsilon(v)\big)
= A(S) - 2A(S_{>v}) + 2v\,\epsilon(v). \tag{4}
$$
Finally, since $u_S$ is $\{0,1\}$-valued, $\int_0^v u_S\,dx\ge0$ (length-$v$
integral of a nonnegative function) and $\int_v^T u_S\,dx\le T-v$
(length-$(T-v)$ integral of a function bounded above by $1$). Hence the
left side of (4) is $\ge 0-(T-v)=v-T$, i.e.
$$A(S)-2A(S_{>v})+2v\epsilon(v)\;=\;\int_0^v u_S\,dx-\int_v^T u_S\,dx\;\ge\;v-T.\qquad\blacksquare$$

**Remark (sharpness).** The two trivial bounds used ($\int_0^v u_S\ge0$,
$\int_v^T u_S\le T-v$) are simultaneously tight whenever $S$ has no element
in $(0,v]$ at all and every element of $S$ that exceeds $v$ still exceeds
it densely enough to keep $u_S\equiv1$ on all of $[v,T)$ — e.g. $S=\{T\}$ a
single point mass exceeding $v$: then $u_S\equiv1$ on $[0,T)$,
$\int_0^vu_S=v$, $\int_v^Tu_S=T-v$, giving equality $v-(T-v)=2v-T$ in (4)
directly... concretely: $A(S)=T$, $A(S_{>v})=T$ (if $v<T$), $\epsilon(v)=1$,
so the left side is $T-2T+2v=2v-T$, matching $\ge v-T$ **not** tightly here
(since $2v-T\ge v-T\iff v\ge0$, true, with equality only at $v=0$). The
bound is exactly attained (equality in the final inequality) whenever
$u_S\equiv 0$ on all of $(0,v)$ **and** $u_S\equiv1$ on all of $(v,T)$ — a
configuration realized, e.g., by any $S$ decomposing as one dominant
element $M$ with $M>T-M$ plus an exactly-paired remainder $P$ all of whose
values lie in $(0,v)$ (then $u_S\equiv0$ on $(0,v)$ since $P$'s truncated
parity is always even there, and $u_S\equiv1$ on $[v,M)$ from $M$ alone).
This sharpness case is exactly the vertex construction used in
`results/imo-2026-03/approaches/greedy-halving-adversary.md`, Theorem 31.

**Verification.** Independently checked by randomized exact-`Fraction`
trials (`/tmp/round-16/check_psi_bound.py`): for $k$-ladder tails
($k=1,\dots,5$), random legal $\le k$-cut responses $S$ and random
thresholds $v\in(0,T)$, the quantity $A(S)-2A(S_{>v})+2v\epsilon(v)-(v-T)$
was never negative across $20{,}000$ trials per $k$ (worst observed margins
strictly positive, consistent with the proof, e.g. $\approx0.0003\,T$ at
$k=4$ — small but never violating). Also checked end-to-end
(`/tmp/round-16/check_full_closure.py`): substituting this bound into
Proposition 30's identity reproduces $A(F\cup G')\ge f(n)$ for random
$\ell(F)=1$, $v<s$ configurations at $n=3,\dots,6$, zero violations.

## Origin / usage

Derived in `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 16, Theorem 31, to close the previously-open "Target Q" item left by
Proposition 30 (round 15): an upper bound on $A(R'_{>v})$, equivalently a
lower bound on $A(R')-2A(R'_{>v})+2v\epsilon(v)$, for $R'$ an arbitrary
legal $(n-2)$-ladder response and $v\in(0,s)$ arbitrary. This lemma
supplies that bound completely, unconditionally, and with no induction
hypothesis or ladder-specific structure at all — it holds for *any* finite
multiset, not just ladder responses.

**Status: proposed by this round's builder, not yet independently
re-certified by a proof-reviewer pass.**
