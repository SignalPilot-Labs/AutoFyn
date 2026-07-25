# Odd-Excess (e≥3) Endpoint Closure Theorem

**Source:** `self-similar-induction-on-n`, round 22 Track 1. Certified by proof-reviewer, round 22, after independent re-derivation and exact-`Fraction` stress testing (own scripts, not reused from the builder).

## Statement

Fix $k\ge1$ and $m\ge k+3$ with $e:=m-k$ **odd**, $e\ge3$. Let $a_1\in(2^{k-1},2^k]$
and let $R$ be **any** finite multiset of positive reals (no cardinality
cap, no value cap) with $\mathrm{sum}(R)=2^m-a_1$. Set $D:=\{a_1\}\cup R$
(so $\mathrm{sum}(D)=2^m$). Then
$$\mathrm{OddSum}(D\cup\Gamma_{m-1})\ \ge\ 2^m,$$
where $\Gamma_j:=\{2^0,2^1,\ldots,2^j\}$.

Equivalently (via the certified even-target companion peeling / corrected
$q=0$-chain identity), $\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge T_{\mathrm{odd}}
:=2^m-2^k-\frac{2^{m+1}-2^{k+2}}3$ for every $a_1$ in the stated range.

## Proof sketch (verified)

Let $\mathrm{margin}(a_1):=\mathrm{LB}_{\mathrm{odd}}(a_1)-T_{\mathrm{odd}}
=\frac{2^k}6+\frac{2^m}6-\frac{a_1}2-\frac12$, where $\mathrm{LB}_{\mathrm
{odd}}(a_1)=\frac{(2^m-a_1)+2^k-1}2$ is the certified cap-free Half-Sum
Corollary bound ($\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$ applied to
$R\cup\Gamma_{k-1}$). This is affine, strictly decreasing in $a_1$
(slope $-1/2$), so on the right-closed interval $(2^{k-1},2^k]$ its
minimum is attained at $a_1=2^k$:
$$\mathrm{margin}(2^k)=\frac{2^k(2^e-2)}6-\frac12.$$
For odd $e\ge3$, $2^e-2\ge6$, so $\mathrm{margin}(2^k)\ge2^k-\frac12\ge
\frac32>0$ for every $k\ge1$ (tight at $k=1,e=3$). Hence
$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge\mathrm{LB}_{\mathrm{odd}}(a_1)\ge
T_{\mathrm{odd}}+\mathrm{margin}(2^k)\ge T_{\mathrm{odd}}$ for every
$a_1$ in range. No cardinality cap on $R$ is used anywhere.

**Sharp scope note (important, do not misuse):** at $e=1$ the same
formula gives $\mathrm{margin}(2^k)=-\frac12<0$ — this theorem's hypothesis
$e\ge3$ odd is load-bearing; $e=1$ genuinely needs the separate,
cardinality-capped General Cardinality-Constrained Half-Sum Lemma
(round 21) instead, consistent with round 17's exact counterexample at
$(k,e)=(2,1)$.

## Independent verification

- Re-derived the margin formula symbolically from scratch (`sympy`),
  confirmed identical to the file's closed form.
- 547-trial and 10,000-trial exact-`Fraction` stress tests, $k=1,\ldots,6$,
  $e\in\{3,5,7\}$, $a_1$ spanning the whole interval including the exact
  endpoint $a_1=2^k$, $R$ of random count (deliberately uncapped, up to
  15 elements) with $\max(R)\le2^{k-1}$: zero violations, minimum
  observed margin (in $\mathrm{OddSum}(R\cup\Gamma_{k-1})-T_{\mathrm{odd}}$)
  consistent with the theoretical floor $3/2$ at $(k,e,a_1)=(1,3,2)$.
- Confirmed by direct computation that $(k,e)=(1,3)$, $a_1=2$, $R=$ 14
  copies of $1$ gives $\mathrm{OddSum}(D\cup\Gamma_{m-1})=18>16=2^m$,
  consistent with (not tight against) the theorem.

## Scope

Closes odd excess $e\ge3$ (sub-case (i) of $\mathrm{GT}(m)$) unconditionally,
over the full range $a_1\in(2^{k-1},2^k]$, for every $k\ge1$. Does **not**
address $e=1$ (separate lemma) or $e=0$ (still open — see
`Case-B(m,k) Sliver Closure Theorem` below and the still-open sub-case (i)
$e=0$ residual, which is a *distinct* object from `Case-B(m,k)`).
