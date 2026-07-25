# Certified (round 4): AltSum reformulation, Single-Insertion Lemma, Reduction B

Certified from `approaches/self-similar-induction-on-n.md` (round 4).
Proof-reviewer independently re-verified the Single-Insertion Lemma formula
(5,000 random-instance check, zero mismatches) and the Reduction B identity
`OddSum(B∪S) = μ + EvenSum(B∪S')` (897 random-instance check respecting the
`b1<μ` and cut-budget constraints, zero mismatches).

**Lemma AS (AltSum reformulation).** For any finite multiset $X$ of positive
reals, $\mathrm{OddSum}(X)=(\mathrm{sum}(X)+\mathrm{AltSum}(X))/2$ where
$\mathrm{AltSum}(X):=x_1-x_2+x_3-\cdots$ (sorted descending). Consequently,
for refinements of $\Gamma_m$ (fixed sum $2^{m+1}-1$), $T(m,k)$ is exactly
equivalent to "every $\le k$-cut refinement has $\mathrm{AltSum}\ge1$."
Elementary, proved in two lines from $\mathrm{Odd+Even=sum}$,
$\mathrm{Odd-Even=AltSum}$.

**Single-Insertion Lemma.** For a sorted sequence $Z=(z_1\ge\cdots\ge z_L)$
and $v>0$ inserted at sorted position $s$ (ties broken: inserted element
after equal originals): $\mathrm{AltSum}(Z\cup\{v\})-\mathrm{AltSum}(Z)
=(-1)^{s+1}(v-2\,\mathrm{AltSum}(z_s,\dots,z_L))$. Strictly generalizes the
certified Peeling Lemma (the $s=1$ special case). Verified independently.

**Reduction B.** If $B=\{b_1\ge\cdots\}$ (partition of $2^m$) has
$b_1<\mu:=\max(S)$ where $S$ is a refinement of $\Gamma_{m-1}$, and
$S'=S\setminus\{\mu\}$, then $\mathrm{OddSum}(B\cup S)=\mu+\mathrm{EvenSum}
(B\cup S')$, and consequently $\mathrm{OddSum}(B\cup S)\ge2^m\iff
\mathrm{OddSum}(B\cup S')\le2^m-1$. Proved from the certified Peeling
Lemma; verified independently. The target `Case-B(m,k):
OddSum(B∪S')≤2^m-1` itself remains **open** (numerically supported, not
proved) — do not cite this file as closing Case B, only as reducing it.

**Reusable by:** any approach needing to track AltSum under general
insertions (not just at the maximum), or needing the EvenSum-target-to-
OddSum-target conversion (Reduction B's mechanism).
