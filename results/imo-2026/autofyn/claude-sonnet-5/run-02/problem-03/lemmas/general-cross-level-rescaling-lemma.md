## General Cross-Level Rescaling Lemma

**Source:** `approaches/greedy-halving-adversary.md`, round 22.
**Status:** CERTIFIED (proof-reviewer, round 22). Fully general closed-form
algebra, no induction on the depth $k$, no legality assumption.

### Statement

Fix the $n$-ladder $p_1>\dots>p_{n+1}$ ($p_i=2^{n+1-i}f(n)$,
$f(n)=1/(2^{n+1}-1)$), and any integer $k$ with $0\le k\le n$. Write
$m:=n-k$ and $\lambda_k:=f(n)/f(m)$. Then the depth-$k$-truncated tail
$\{p_{k+1},\dots,p_{n+1}\}$ is **exactly** $\lambda_k$ times the unit
$m$-ladder: writing $q_i^{(m)}:=2^{m+1-i}f(m)$ ($i=1,\dots,m+1$) for the
$m$-ladder's own pieces,
$$p_{k+i}=\lambda_k\cdot q_i^{(m)}\qquad\text{for every }i=1,\dots,m+1.$$
In particular $\lambda_k\cdot f(m)=f(n)$ exactly.

Strictly generalizes the certified `tail-self-similarity` (its $k=1$
instance: $\lambda_1=f(n)/f(n-1)=r$) and subsumes the previously ad hoc
$k=3$ instance used in Theorem 35 ($\lambda=f(n)\cdot D_{n-3}$, since
$D_{n-3}=1/f(n-3)$).

### Proof

Directly from the ladder formula, $p_{k+i}=2^{n+1-k-i}f(n)$. On the other
side,
$$\lambda_k\cdot q_i^{(m)}=\frac{f(n)}{f(m)}\cdot2^{m+1-i}f(m)=f(n)\cdot2^{m+1-i}
=f(n)\cdot2^{(n-k)+1-i}=2^{n+1-k-i}f(n),$$
using $m=n-k$. These are identical term by term. The "in particular"
clause is immediate: $\lambda_k f(m)=(f(n)/f(m))\cdot f(m)=f(n)$.
$\blacksquare$

### Verification

Proof-reviewer independently re-derived the algebra from scratch and
re-verified it with a fresh exact-`Fraction` script
(`/tmp/round-22/verify_gha.py`, "Rescaling lemma" test): checked the
identity $p_{k+i}=\lambda_k q_i^{(m)}$ and $\lambda_k f(m)=f(n)$ for every
$n=2,\dots,9$ and every $k=0,\dots,n-1$ — zero discrepancies, matching the
builder's own independent check.

### Scope note

Pure ladder algebra (depends only on the closed-form ladder definition,
not on legality of any response or on the game). Safe to reuse by any
future depth-$k$ rescaling argument in this file or a sibling.
