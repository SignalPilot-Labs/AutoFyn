# Certified (round 3, CONDITIONAL): Theorem 5, top-dominant regime reduces to T(n-1)

Certified from `approaches/universal-halving-adversary.md` (round 3).
**This lemma is conditional** — it is a genuine proved implication, not a
standalone unconditional closure, and should only be cited as such.

## Statement

Fix $n\ge1$ and assume $T(n-1)$ holds in full (for every sorted
$q_1\ge\cdots\ge q_n>0$ summing to $1$, XY has a $\le(n-1)$-cut response
achieving $\mathrm{OddSum}\le c(n-1)$). Then for every sorted
$p_1\ge\cdots\ge p_{n+1}>0$ summing to $1$ with $p_1\ge c(n)$, XY has a
$\le n$-cut response achieving $\mathrm{OddSum}\le c(n)$.

## Proof sketch (full proof in the approach file)

XY bisects $p_1$ (1 cut) and applies $T(n-1)$'s response, scaled by
$S=1-p_1$, to $R=(p_2,\dots,p_{n+1})$ ($\le n-1$ cuts). By the certified
Subadditivity Lemma (`perfect-pairing-subadditivity-and-general-insertion.md`),
$\mathrm{OddSum}\le \varphi(p_1):=p_1/2+(1-p_1)c(n-1)$, affine and strictly
decreasing in $p_1$ (since $c(n-1)>1/2$). The key identity
$\varphi(c(n))=c(n)$ holds exactly (verified below), so for $p_1\ge c(n)$,
$\varphi(p_1)\le\varphi(c(n))=c(n)$.

## Verification (proof-reviewer, round 3)
- $\varphi(c(n))=c(n)$ checked exactly by rational arithmetic for
  $n=1,\dots,7$: exact equality every time (using
  $c(n)=2^n/(2^{n+1}-1)$).
- $c(n)>1/2$ for all $n\ge0$ checked exactly (needed for $\varphi$'s slope
  to be strictly negative).
- Cross-check: at $p_1=1/2<c(1)$ (outside the theorem's hypothesis),
  $\varphi(1/2)=3/4$, matching the previously-documented dead end
  (bisecting $p_1=1/2$ alone gives $0.75>c(1)=2/3$) — confirms the formula
  correctly reproduces known failure outside its valid domain.

## Status and reuse

This reduces "$T(n)$ restricted to $p_1\ge c(n)$" to "$T(n-1)$ in full" —
exactly as strong a hypothesis as what is being proved one level down. It
does **not** independently establish $T(n)$ for any $n$; it is only useful
once $T(n-1)$ is closed in full by some other means. Recorded here so a
future round that closes $T(n-1)$'s remaining gap (the balanced/near-uniform
regime, see `approaches/universal-halving-adversary.md`) can immediately
invoke this lemma to also close the $p_1\ge c(n)$ regime at level $n$
without re-deriving the reduction.
