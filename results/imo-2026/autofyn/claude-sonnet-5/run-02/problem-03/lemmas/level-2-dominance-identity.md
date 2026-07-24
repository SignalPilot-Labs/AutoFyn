# Lemma: Level-2 dominance identity (Lemma 24)

**Source:** `approaches/greedy-halving-adversary.md`, round 10.

**Statement.** For the $n$-ladder ($n\ge2$), with
$s:=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})$ (so $s=r-p_2$, $r=1-p_1$),
$$p_2 - s = f(n).$$

**Proof.** $s=r-p_2$, so $p_2-s=2p_2-r=2p_2-(1-p_1)=2p_2+p_1-1$. Using
$p_1=2p_2$ (`general-ladder-dominance`, Lemma 23), this is $4p_2-1$. With
$p_2=2^{n-1}f(n)$ and $f(n)=1/(2^{n+1}-1)$:
$4p_2-1=\dfrac{2^{n+1}}{2^{n+1}-1}-1=\dfrac{2^{n+1}-(2^{n+1}-1)}{2^{n+1}-1}
=\dfrac1{2^{n+1}-1}=f(n)$. $\blacksquare$

**Status.** Proved in full, unconditionally, for every $n\ge2$.

**Scope.** Exactly analogous, one level down, to the identity
$r\cdot f(n-1)=f(n)$ already inside `tail-self-similarity`; used directly by
Proposition 24 (`v-in-s-p2-closure`) and Proposition 25
(`p2-cut-complement-branch-closure`).

**Certified by:** proof-reviewer, round 10 - independently re-verified (fresh exact-Fraction scripts, corrected for legal-refinement piece-boundary/cut-budget coupling): CERTIFIED.
