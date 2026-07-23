# Lemma: Euclidean-subtraction identity for exponents

**Statement.** For all integers $\alpha,\beta\ge0$, with the convention $\gcd(0,0)=0$ and
$\gcd(0,x)=x$:
$$\gcd\big(\min(\alpha,\beta),\,|\alpha-\beta|\big)=\gcd(\alpha,\beta).$$

**Proof.** Case $\alpha=\beta$: LHS $=\gcd(\alpha,0)=\alpha=\gcd(\alpha,\alpha)=$ RHS. Case
$\alpha<\beta$ (the case $\alpha>\beta$ is symmetric): LHS $=\gcd(\alpha,\beta-\alpha)$. If
$\alpha=0$ both sides equal $\beta$. If $\alpha>0$: for any $d\ge1$, $d\mid\alpha$ and
$d\mid\beta-\alpha$ iff $d\mid\alpha$ and $d\mid(\beta-\alpha)+\alpha=\beta$, so the sets of common
divisors of $\{\alpha,\beta-\alpha\}$ and $\{\alpha,\beta\}$ coincide, hence their maxima (the two
gcds) coincide. $\blacksquare$

**Source.** Certified from `results/imo-2026-01/approaches/prime-valuation-invariant.md` (Lemma 2)
and independently re-derived in `results/imo-2026-01/approaches/confluence-newman.md` (Lemma 1);
the two derivations agree. Certified by proof-reviewer, round 1: statement is correct, proof is
complete and case-exhaustive (trichotomy on $\alpha$ vs $\beta$, with the $\alpha=0$ boundary
handled explicitly), no gaps.

**Reuse.** This is the core arithmetic fact underlying the per-prime gcd invariant for the
Confucius gcd/lcm blackboard process (`imo-2026-01`): it shows that replacing $(\alpha,\beta)$ by
$(\min(\alpha,\beta),|\alpha-\beta|)$ — the effect of one board move on the $p$-adic valuations at
a fixed prime $p$ — preserves $\gcd(\alpha,\beta)$. Reusable in any problem whose update rule is
"replace a pair by $(\min,\,|{\rm diff}|)$" and needs a preserved gcd invariant.
