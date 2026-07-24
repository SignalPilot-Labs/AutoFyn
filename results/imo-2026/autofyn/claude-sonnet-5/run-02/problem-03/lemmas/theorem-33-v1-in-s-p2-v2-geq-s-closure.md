# Lemma: Theorem 33 — sub-case (b), $v_1\in(s,p_2)$, $v_2\ge s$ closure

**Source:** `approaches/greedy-halving-adversary.md`, round 18.

**Statement.** Fix $n\ge3$. Let $F=\{v_1,v_2\}\cup P$ with $\ell(F)=2$,
$P$ pairing up exactly, $s\le v_2<v_1<p_2$ (so both thresholds sit at or
above the tail's own total mass $s:=\mathrm{Total}(\{p_3,\dots,p_{n+1}\})$),
and $G'=\{p_2\}\cup R'$ where $R'$ is *any* legal refinement of
$\{p_3,\dots,p_{n+1}\}$ (no cap on the number of cuts). Then
$$A(F\cup G')\ >\ f(n),$$
**unconditionally**: no induction hypothesis, no cut-budget cap on $R'$.

**Proof.** By the Step-1 substitution identity (Lemma 25 + Proposition
30's exact formula, combined and confirmed independently by the
reviewer),
$$A(F\cup G')=p_2-A(R')-(v_1-v_2)+2\int_{v_2}^{v_1}u_{R'}(x)\,dx.$$
Since $\mathrm{Total}(R')=s$, $u_{R'}\equiv0$ on $[s,\infty)$; as
$v_2\ge s$, the interval $[v_2,v_1)\subseteq[s,\infty)$, so the integral
vanishes and $A(F\cup G')=p_2-A(R')-(v_1-v_2)$. It suffices to show
$A(R')+(v_1-v_2)<s$:
- $v_1-v_2<p_2-s=f(n)$ (Lemma 24), strict since $v_1<p_2$ strictly.
- Every fragment of $R'$ is at most the piece it was cut from, and the
  ladder is strictly decreasing ($p_3>p_4>\dots$, `general-ladder-
  dominance`), so $\max(R')\le p_3$; by `max-domination-lemma`,
  $A(R')\le\max(R')\le p_3$.
- $s-p_3=f(n)(2^{n-2}-1)\ge f(n)$ for $n\ge3$ (equality only at $n=3$).

Combining: $A(R')+(v_1-v_2)\le p_3+(v_1-v_2)<p_3+f(n)\le p_3+(s-p_3)=s$
(strict throughout, since step (a) is strict even at $n=3$). Hence
$A(F\cup G')=p_2-A(R')-(v_1-v_2)>p_2-s=f(n)$. $\blacksquare$

**Status.** Proved in full, unconditional for every $n\ge3$.

**Independent verification (reviewer, round 18).** Two independent checks:
(i) the Step-1 identity itself, re-derived and re-verified against a
fresh 20,000-trial exact-`Fraction` script (confirmed the identity
requires $p_2>\mathrm{Total}(R')$/dominance, an unstated but always-
satisfied hypothesis in this problem's ladder); (ii) Theorem 33's
conclusion directly, on the actual ladder, a fresh 12,000-trial
exact-`Fraction` script ($n=3,\dots,6$, 3000 trials per $n$), zero
violations, margins matching the builder's own reported figures.

**Scope.** Closes a slice of the range Theorem 32 (round 17) left open
($v_1\in(s,p_2)$), specifically $v_2\in[s,v_1)$. The complementary range
$v_2<s$ is handled (partially) by Theorem 34; the residual middle band
$v_2\in(p_2-v_1,s)$ remains open (reduces to the round-15/16 crux, a
sharp upper bound on the truncated alternating sum $A(R'_{>v_2})$).

**Certified by:** proof-reviewer, round 18 — independently re-derived the
proof by hand and re-verified numerically with fresh scripts: CERTIFIED.
