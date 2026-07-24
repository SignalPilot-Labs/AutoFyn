## Statement

Fix $n\ge3$ and the $n$-ladder. For $3\le j\le n+1$, let $x:=p_1-p_j$
(so $x\in(p_2,p_1)$ strictly, for every finite $j\ge3$), and let
$S_j:=\{x,p_j\}\cup T$ where $T=\{p_2,\dots,p_{n+1}\}$ is entirely untouched
(so $p_j$ occurs with multiplicity 2 in $S_j$: once as $p_1-x$, once as the
untouched tail element). Writing $C(j):=\sum_{i=2}^j(-1)^ip_i$ and
$D(j):=\sum_{i=j+1}^{n+1}(-1)^ip_i$ (so $A(T)=C(j)+D(j)$),
$$A(S_j) = x + 2C(j) - (-1)^jp_j - A(T).$$

This closed form is **fully general** (proved for every $n\ge3$ and every
$3\le j\le n+1$, not merely checked numerically).

**Not part of this certification:** the corollary "$A(S_j)\ge f(n)$, strict
for $n\ge3$" is verified only for $n\le7$ (exact `Fraction` computation) —
a general-$n$ symbolic proof of this final inequality was not completed and
is NOT certified here.

## Proof

Position lemma: $x/p_2=2-2^{2-j}\in[1,2)$ for $j\ge3$ (direct algebra from
the ladder's ratio-2 structure), so $p_2<x<p_1$ strictly. By
`odd-run-reduction-lemma`, $p_j$ (multiplicity 2) cancels, leaving
$S_j'=\{x\}\cup(T\setminus\{p_j\})$, sorted $x,p_2,\dots,p_{j-1},
p_{j+1},\dots,p_{n+1}$ (using the position lemma to place $x$ above $p_2$).
Elements $p_2,\dots,p_{j-1}$ keep their original signs (contributing
$C(j)-(-1)^jp_j$); elements $p_{j+1},\dots,p_{n+1}$ each shift down one rank
(net shift $0$ from $x$ replacing $p_1$ at the top, $-1$ from $p_j$'s
removal), flipping their sign, contributing $-D(j)$. Substituting
$D(j)=A(T)-C(j)$ gives the stated formula.

## Verification (proof-reviewer, round 5)

Independently re-verified the closed form's *consequence* — $A(S_j)$'s
numeric values — by direct exact-`Fraction` sort-and-alternate-sum
computation, for $n=1,\dots,7$ and every $j=3,\dots,n+1$: reproduces exactly
the pattern claimed (equality with $f(n)$ only at $n\le2$, strict excess for
$n\ge3$), zero violations of $A(S_j)\ge f(n)$ found. The sign-bookkeeping
derivation itself is elementary and was independently re-derived by hand;
no gap found.

## Origin / usage

Derived in `results/imo-2026-03/approaches/rank-tie-vertex-reduction.md`
§5.3 (round 5), settling a second infinite family of tie-vertices (interior
cross-ties against an untouched tail) distinct from
`cascading-halving-family-characterization`.

## Certification note (proof-reviewer, round 5)
**CERTIFIED (closed-form identity only).** The formula for $A(S_j)$ is fully
general and gap-free, promoted to `lemmas/`. The corollary
$A(S_j)\ge f(n)$ for all $n$ is NOT certified — it is checked only for
$n\le7$ and remains open for general $n$; future builders must not treat it
as proved.
