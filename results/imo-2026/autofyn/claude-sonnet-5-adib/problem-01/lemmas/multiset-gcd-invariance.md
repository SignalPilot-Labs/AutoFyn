# Lemma: per-prime multiset-gcd invariance under the gcd/lcm board move

**Statement.** Let $S=(a_1,\dots,a_k)$ ($k\ge2$) be a state of positive integers, and for a prime
$p$ let $x_p(S)=(v_p(a_1),\dots,v_p(a_k))$. Define $g_p(S):=\gcd(x_p(S))$ (the gcd of this
multiset of $k$ nonnegative integers, with $\gcd$ of the multiset extended by $\gcd(0,x)=x$, so
$\gcd$ of an all-zero multiset is $0$). If $S'$ is obtained from $S$ by one legal move (replacing
two entries $m,n>1$ at distinct positions by $\gcd(m,n)$ and $\mathrm{lcm}(m,n)/\gcd(m,n)$), then
$g_p(S')=g_p(S)$ for every prime $p$.

**Proof.** By the standard valuation identities $v_p(\gcd(m,n))=\min(v_p(m),v_p(n))$,
$v_p(\mathrm{lcm}(m,n)/\gcd(m,n))=|v_p(m)-v_p(n)|$ (immediate from unique factorization), the move
sends the pair of touched coordinates $(\alpha,\beta)=(v_p(m),v_p(n))$ of $x_p(S)$ to
$(\min(\alpha,\beta),|\alpha-\beta|)$, leaving all other coordinates fixed. Writing $H$ for the
gcd of the untouched coordinates (well defined since $k\ge2$ leaves a well-defined, possibly-empty
sub-multiset of size $k-2\ge0$, with the convention $\gcd$ of the empty multiset is $0$, acting as
an identity), associativity/commutativity of gcd on $\mathbb Z_{\ge0}$ gives
$g_p(S)=\gcd(H,\gcd(\alpha,\beta))$ and $g_p(S')=\gcd(H,\gcd(\min(\alpha,\beta),|\alpha-\beta|))$.
By the Euclidean-subtraction identity (`euclidean-subtraction-identity.md`),
$\gcd(\alpha,\beta)=\gcd(\min(\alpha,\beta),|\alpha-\beta|)$, so $g_p(S)=g_p(S')$. $\blacksquare$

**Source.** Certified from `results/imo-2026-01/approaches/prime-valuation-invariant.md` (Lemma 3,
stated for $k=2026$) and `results/imo-2026-01/approaches/confluence-newman.md` (Lemma 2, stated for
general $k\ge2$, which is the form recorded here). Both derivations are correct and agree;
certified by proof-reviewer, round 1, after independent re-derivation and computational
cross-check (random and exhaustive simulation of the board process against the closed form
$M=\prod_p p^{\gcd_i v_p(x_i)}$ this lemma implies).

**Reuse.** Directly gives, by induction along any move sequence, that $g_p$ is a global invariant
of the whole process, hence (combined with a termination argument showing exactly one entry $>1$
survives) that the surviving value's $p$-adic valuation is pinned to $g_p(\text{initial state})$
for every $p$ — this is the mechanism proving both existence/uniqueness of the survivor and its
closed form for the `imo-2026-01` blackboard problem, and is reusable for any similar
gcd/lcm-splitting merge process on multisets of positive integers.
