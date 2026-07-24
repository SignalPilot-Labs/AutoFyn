## Statement (CERTIFIED — round 32, proof-reviewer; conditional theorem,
certified exactly as scoped)

**Master Theorem.** Let $m\ge2$ and let $\sigma=(\sigma_1,\dots,\sigma_m)$
be a ratio-2 superincreasing tail ($\sigma_i=2\sigma_{i+1}$). Suppose
$\mathrm{MinFloor}(m-1)$ holds: $A(W)\ge\sigma_m$ for every legal
$\le(m-2)$-cut refinement $W$ of $\sigma':=(\sigma_2,\dots,\sigma_m)$. Then
$\mathrm{MaxCeil}(m)$ holds in full: for every legal $\le(m-2)$-cut
refinement $S$ of $\sigma$ (any distribution of cuts across all $m$
elements, including $\sigma_1$ possibly untouched),
$$A(S)\ \le\ \sigma_1-\sigma_m.$$

**Certified scope: this is a conditional implication.** It is
unconditionally applicable wherever $\mathrm{MinFloor}(m-1)=(\star_{m-2})$
is itself already certified — currently this holds for $m-2\in\{1,2,3\}$,
i.e. $m\in\{3,4,5\}$ (via `minfloor-4-full-closure` and earlier certified
$(\star_1),(\star_2)$ results) — giving an unconditional closure of
$\mathrm{MaxCeil}(5)$ this round. It does **not** by itself establish
$\mathrm{MaxCeil}(m)$ for $m\ge6$, which needs $(\star_4)$ or higher, not
yet certified.

## Proof

Let $c_1\ge0$ be the cuts spent on $\sigma_1$ (so $\sigma_1$ splits into
$c_1+1$ fragments, $c_1=0$ meaning untouched), $x$ the largest such
fragment, $W:=S$ restricted to $\sigma_2,\dots,\sigma_m$ (a legal
$\le(m-2)$-cut refinement of $\sigma'$, so $A(W)\ge\sigma_m$ by hypothesis).

- **Case $x\le\sigma_2$:** every element of $S$ is $\le\sigma_2$ (every
  other fragment of $\sigma_1$ is $\le x\le\sigma_2$; every element of $W$
  is a fragment of some $\sigma_i$, $i\ge2$, so $\le\sigma_i\le\sigma_2$).
  By Max Bound, $A(S)\le\sigma_2\le\sigma_1-\sigma_m$ (using
  $\sigma_1=2\sigma_2$ and $\sigma_2\ge\sigma_m$).
- **Case $x>\sigma_2$:** $x$ is the strict unique maximum of $S$ (the other
  fragments of $\sigma_1$ sum to $<\sigma_2$, hence each $<\sigma_2<x$;
  every element of $W$ is $\le\sigma_2<x$). By
  `sharp-dominant-removal-identity`, $A(S)=x-A(S\setminus\{x\})$. If
  $c_1=0$: $S\setminus\{x\}=W$, $x=\sigma_1$, direct substitution gives
  $A(S)\le\sigma_1-\sigma_m$. If $c_1\ge1$: $S\setminus\{x\}=W\cup\{y_1,
  \dots,y_{c_1}\}$ with $\sum y_i=\sigma_1-x$; applying the Insertion
  Sandwich lower bound $c_1$ times,
  $$A(S\setminus\{x\}) \ge A(W)-\sum y_i \ge \sigma_m-(\sigma_1-x),$$
  so $A(S)=x-A(S\setminus\{x\})\le x-\sigma_m+\sigma_1-x=\sigma_1-\sigma_m$.

Both cases give $A(S)\le\sigma_1-\sigma_m$. $\blacksquare$

## Verification

Independently re-derived by the proof-reviewer (round 32): re-checked both
case-split steps by hand; independently verified the $m=5$ instantiation
(using the already-certified `minfloor-4-full-closure`) via a fresh
300,000-trial exact-`Fraction` random + adversarial-boundary search at
$\sigma=(16,8,4,2,1)$ (units $1/31$): maximum $A(S)$ found was exactly
$15=\sigma_1-\sigma_5$ (attained, not exceeded, at a boundary configuration
with $\sigma_1$ untouched and $\sigma_2$ split into 4 fragments), zero
violations.

## Origin / usage

Proved in `results/imo-2026-03/approaches/rank-pigeonhole-budget.md`
§7.19.3, round 32. Instantiated unconditionally at $m=5$ (§7.19.4),
closing $\mathrm{MaxCeil}(5)$ in full and hence $(7.9.1)$ at $n=8$. Will
apply automatically once $(\star_4),(\star_5),\dots$ are certified in
future rounds.
