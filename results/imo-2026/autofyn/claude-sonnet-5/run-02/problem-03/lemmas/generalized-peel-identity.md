# Lemma: Generalized one-step-peel identity (Theorem B$_k$)

**Source:** `approaches/lp-duality-certificate.md`, round 9.

**Statement.** For any marking $p_1\ge\cdots\ge p_m>0$ ($m\ge2$) and any
index $k\in\{2,\dots,m\}$, let $w_k:=p_1-p_k\ge0$ and
$S'_k:=\{w_k\}\cup\{p_i:2\le i\le m,\,i\ne k\}$ ($m-1$ elements, total
$T-2p_k$). For any further legal strategy on $S'_k$ using $\le m-2$ cuts,
producing refinement $M'$ with value $\Phi'$, the combined strategy (cut
$p_1$ into $(p_k,w_k)$, then the $S'_k$-strategy) yields exactly
$$\Phi(\text{combined})=p_k+\Phi'.$$

**Proof.** The final multiset is $\{p_k,p_k\}\cup M'$ (the untouched
original $p_k$ and the fragment of size $p_k$ cut from $p_1$). By
`pair-cancellation-identity`, $A(\{p_k,p_k\}\cup M')=A(M')$; the same
total-bookkeeping as the $k=2$ case gives $\Phi(\text{combined})=p_k+\Phi'$.
$\blacksquare$

**Status.** Proved in full, unconditional, general $m\ge2$, any
$k\in\{2,\dots,m\}$ — strictly generalizes the certified
`one-step-peel-identity` ($k=2$ case) to peeling $p_1$ against any tail
element. Independently re-verified by the reviewer with 2000 random exact-
`Fraction` trials (random $m$, random $k$), zero mismatches.

**Certified by:** proof-reviewer, round 9.
