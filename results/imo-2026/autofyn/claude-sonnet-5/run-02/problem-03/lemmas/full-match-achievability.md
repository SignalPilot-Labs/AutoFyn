# Lemma: Full-match achievability (Theorem A)

**Source:** `approaches/lp-duality-certificate.md`, round 8 (backfilled
round 9 since round-9 work directly builds on it).

**Statement.** For any marking $p_1\ge\cdots\ge p_m>0$ with total $T$: if
$p_1\ge T/2$ (equivalently $p_1\ge p_2+\cdots+p_m$), Xiang Yu can use
exactly $m-1$ cuts, all inside $p_1$, to split it into fragments of sizes
exactly $p_2,\dots,p_m$ plus a leftover $v:=p_1-(p_2+\cdots+p_m)=2p_1-T\ge0$
(leaving $p_2,\dots,p_m$ untouched). This achieves $\Phi=p_1$ exactly.

**Proof.** The resulting multiset is $\{p_2,p_2,\dots,p_m,p_m\}\cup\{v\}$
(degenerate, no $v$, if $v=0$): exactly `leftover-formula`'s hypothesis
with $m-1$ pairs and unpaired element $v$. So $A=v$ and
$\Phi=(T+v)/2=(T+2p_1-T)/2=p_1$. Uses exactly $m-1$ cuts, legal within
budget $n=m-1$. $\blacksquare$

**Status.** Proved in full, unconditional, general $m\ge1$. Independently
re-verified by the reviewer with 2000 random exact-`Fraction` trials, zero
mismatches. Used as a base case throughout the round-9 `p_1\ge T/2`
closure (§3-4 of the approach file).

**Certified by:** proof-reviewer, round 9.
