# Lemma: Bisect-top recursive identity (Theorem C′)

**Source:** `approaches/lp-duality-certificate.md`, round 9.

**Statement.** For any Liu Bang marking $p_1\ge\cdots\ge p_m>0$ ($m\ge2$),
$T=\sum p_i$: bisecting $p_1$ alone (1 cut) and then applying **any**
further legal strategy to the untouched tail $\{p_2,\dots,p_m\}$ using
$\le n-1=m-2$ further cuts, producing a refinement $M'$ with value
$\Phi'$, yields, exactly,
$$\Phi(\text{combined}) = \frac{p_1}{2}+\Phi'.$$
Consequently $\Phi_{\min}(p_1,\dots,p_m;n)\le p_1/2+\Phi_{\min}(p_2,\dots,p_m;n-1)$.

**Proof.** The final multiset is $\{p_1/2,p_1/2\}\cup M'$. By
`pair-cancellation-identity`, $A(\{p_1/2,p_1/2\}\cup M')=A(M')$. Writing
$T':=T-p_1=\mathrm{Total}(M')$, $A(M')=2\Phi'-T'$. Hence
$\Phi(\text{combined})=(T+2\Phi'-T')/2=(T-T')/2+\Phi'=p_1/2+\Phi'$, for
any legal tail strategy, in particular the optimal one. $\blacksquare$

**Status.** Proved in full, unconditional, general $m\ge2$/every marking —
an exact bookkeeping identity, not a numeric or ladder-specific fact.
Independently re-verified by the reviewer with 2000 random exact-`Fraction`
trials comparing both sides directly (sort-and-sum vs. the formula), zero
mismatches. Strictly generalizes the (previously certified-in-substance but
not yet standalone-filed) Theorem C "bisect-top-identity" special case
($\Phi'=\Phi_{\text{tail}}$ with zero further cuts).

**Certified by:** proof-reviewer, round 9.
