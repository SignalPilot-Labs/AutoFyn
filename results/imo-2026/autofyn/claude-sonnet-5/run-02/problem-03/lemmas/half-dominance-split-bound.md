## Theorem 29 (Half-Dominance Split Bound)

**Statement.** Let $M>0$ and let $R$ be any finite multiset of nonnegative
reals with $\max(R)\le M/2$. Then for every finite split $F_2$ of $M$ (any
$k\ge1$ positive parts summing to $M$),
$$A(F_2\cup R)\ \le\ M - A(R).$$

This is completely general — no ladder structure is assumed anywhere in the
statement or proof; the hypothesis $\max(R)\le M/2$ is the only input.

## Proof

Let $s:=\mathrm{Total}(R)$ and $u_{F_2},v_R$ the respective odd-parity
indicators. By the certified `cross-term-identity-threshold` (with $F=F_2$,
$G=R$, threshold $s$):
$$A(F_2\cup R) = A(F_2)+A(R) - 2\int_0^s u_{F_2}(x)v_R(x)\,dx. \tag{1}$$
Since every element of $R$ is $\le\max(R)\le M/2$, $v_R(x)=0$ for
$x\ge\max(R)$; combined with $\max(R)\le s$, $\max(R)\le\min(s,M/2)$, so the
integrand in (1) vanishes outside $[0,\max(R)]\subseteq[0,M/2]$, hence
$$\int_0^s u_{F_2}v_R\,dx = \int_0^{M/2} u_{F_2}(x)v_R(x)\,dx. \tag{2}$$
Pointwise, since $u_{F_2}(x)\in\{0,1\}$ and $0\le v_R\le1$:
$u_{F_2}(x)v_R(x)\ge v_R(x)-(1-u_{F_2}(x))$ (check both values of $u_{F_2}$
directly). Integrating over $[0,M/2]$ and using that $v_R$ vanishes outside
$[0,M/2]$ (so $\int_0^{M/2}v_R=A(R)$):
$$\int_0^{M/2}u_{F_2}v_R\,dx \ \ge\ A(R)-\frac M2+\int_0^{M/2}u_{F_2}\,dx.$$
Substituting into (2) then (1):
$$A(F_2\cup R)\ \le\ A(F_2)-A(R)+M-2\int_0^{M/2}u_{F_2}(x)\,dx.$$
By the certified `symmetry-lemma-29a`, $A(F_2)\le2\int_0^{M/2}u_{F_2}$, so
$A(F_2)-2\int_0^{M/2}u_{F_2}\le0$. Hence $A(F_2\cup R)\le M-A(R)$.
$\blacksquare$

## Ladder-specific corollary (p2-Pinned-Dominance)

For every $n\ge3$, every legal split $F_2$ of $p_2$ and every legal
refinement $R$ of $\{p_3,\dots,p_{n+1}\}$ (ladder $p_i=2^{n+1-i}/(2^{n+1}-1)$),
$$A(F_2\cup R)\ \le\ p_2-A(R).$$
Proof: apply the theorem with $M:=p_2$; by `safe-window-lemma` applied one
level down, every element of a legal refinement of $\{p_3,\dots,p_{n+1}\}$ is
$\le p_3$; and by the certified `general-ladder-dominance` (Lemma 23),
$p_3=p_2/2$. So $\max(R)\le p_2/2$, the exact hypothesis needed.

## Certification note (proof-reviewer, round 14)

Independently re-derived the proof (via a fresh reading, not by re-running
the builder's own script) and re-verified with a fresh 20,000-trial
exact-`Fraction` script: (i) `symmetry-lemma-29a`'s inequality; (ii) the
general theorem with random $M$, random splits $F_2$, and random $R$
satisfying $\max(R)\le M/2$ — zero violations in both checks. Cross-checked
the scope claim against the non-ladder counterexample $\tau=\{49,2/5\}$,
$m=203/4$: $\max(\tau)=49>m/2=203/8$, so the hypothesis genuinely fails
there — consistent with (not contradicting) the theorem, confirming the
theorem is honestly scoped to the hypothesis $\max(R)\le M/2$ and does not
overreach into the false generic statement. No gap found. Genuinely
supersedes round 13's Proposition 28 (dominant-fragment-only): this version
requires no case split on $F_2$'s shape. Certified correct as written, both
the general theorem and the ladder-specific corollary.

**Origin:** `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 14, Theorem 29 and its Corollary.
