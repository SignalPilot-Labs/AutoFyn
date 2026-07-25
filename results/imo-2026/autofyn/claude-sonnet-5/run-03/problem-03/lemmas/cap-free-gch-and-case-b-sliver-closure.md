# Cap-Free General Cardinality-Constrained Half-Sum Lemma, AltSum Peeling Identity (tie-robust), and Case-B(m,k) Sliver Closure Theorem

**Source:** `self-similar-induction-on-n`, round 22 Track 2. Certified by proof-reviewer, round 22, after independent re-derivation and exact-`Fraction` stress testing (own scripts, not reused from the builder).

## 1. Cap-Free General Cardinality-Constrained Half-Sum Lemma (all $k\ge1$)

**Statement.** For every $k\ge1$ and every finite multiset $R$ of positive
reals with $|R|\le k+1$ and $\mathrm{sum}(R)=S\in[2^k,2^k+1)$ — **no bound
on $\max(R)$** — $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ (equivalently
$\mathrm{OddSum}(R\cup\Gamma_{k-1})\ge(S+2^k)/2$).

**Proof.** For $k\ge2$: a line-by-line audit of the certified proof of
GCH($k\ge2$) (`general-cardinality-constrained-half-sum-lemma.md`) and of
the Finite Reduction Theorem it rests on
(`invisible-block-skip-fact-and-general-pairwise-reduction.md`) shows the
value cap $\mathrm{cap}=2^{k-1}$ is used *only* to supply an early-stopping
condition in the General Pairwise Reduction Lemma's affine-interval
argument and as an extra (non-binding) boundary in Case (C2)'s topmost
interval; in both places the cap-free version of the argument still
terminates at a finite $t$ via the "hits $0$" boundary condition alone, and
Case (C2)'s minimum was already attained at the *interior* boundary
$r\to v_1^+$ (the cap only bounded the interval from above, where the
function's *maximum*, not minimum, sat). Steps A and B never reference the
cap at all. For $k=1$: proved directly by hand (two exhaustive cases on
$|R|\in\{1,2\}$, further split on $y\gtrless1$ when $|R|=2$).

**Independent verification:** re-audited every one of the certified proof's
steps (Finite Reduction Theorem, Step A, Step B, Cases C0/C1/C2) for cap
usage independently; 18,000-trial direct exact-`Fraction` stress test of
the final theorem, $k=1,\ldots,6$, $S\in[2^k,2^k+1)$ random, $|R|\in\{1,
\ldots,k+1\}$ random, **values of $R$ genuinely uncapped** (including
instances with one element far exceeding $2^{k-1}$): zero violations,
observed minimum $\mathrm{AltSum}=1$ exactly (tight). Also spot-checked
extreme cap-violating instances by hand (e.g. $k=3$, $R=\{7,1\}$,
$\max(R)=7\gg\mathrm{cap}=4$: $\mathrm{AltSum}(R\cup\Gamma_2)=5\ge1$).

## 2. AltSum Peeling identity, tie-robust (general, no uniqueness needed)

**Statement.** For any finite multiset $M$ of positive reals and $g$ a
chosen copy of $\max(M)$ (ties allowed, no uniqueness hypothesis):
$\mathrm{AltSum}(M)=g-\mathrm{AltSum}(M\setminus\{g\})$.

**Proof.** Elementary rank-shift: sort $M$ descending with $g$ in position
1; removing it shifts every remaining element's rank down by exactly 1,
flipping parity, giving the stated identity directly from the definition
of $\mathrm{AltSum}$.

**Independent verification:** confirmed the rank-shift argument requires
no uniqueness of the maximum (any tie-breaking of equal values leaves
$\mathrm{AltSum}$ unchanged, since swapping equal values doesn't change
any rank's value); this is what makes it usable for `Case-B(m,k)` below,
where $b_1$ may tie with another part of $B$.

## 3. Case-B(m,k) Sliver Closure Theorem

**Statement.** For every $m\ge2$ and every partition $B=(b_1\ge\cdots\ge
b_p)$ of $2^m$ into $p\le m+1$ positive parts with $b_1\in(2^{m-1}-1,
2^{m-1})$ (the previously-open sliver): $\mathrm{OddSum}(B\cup\Gamma_{m-2})
<2^m-1$ (in particular $\le2^m-1$).

**Proof.** $b_1=\max(B\cup\Gamma_{m-2})$ (checked: $b_1>2^{m-1}-1\ge
2^{m-2}=\max(\Gamma_{m-2})$ for every $m\ge2$). Peel it via the tie-robust
AltSum Peeling identity above: $\mathrm{AltSum}(B\cup\Gamma_{m-2})=b_1-
\mathrm{AltSum}(B'\cup\Gamma_{m-2})$, $B':=B\setminus\{b_1\}$. Since
$\mathrm{sum}(B')=2^m-b_1\in(2^{m-1},2^{m-1}+1)$ and $|B'|\le m=(m-1)+1$,
$B'$ is a feasible instance of the Cap-Free GCH with $k=m-1$ (no bound on
$\max(B')$ needed — this is exactly why the cap-free strengthening in
Part 1 is required here), giving $\mathrm{AltSum}(B'\cup\Gamma_{m-2})\ge1$,
hence $\mathrm{AltSum}(B\cup\Gamma_{m-2})\le b_1-1<2^{m-1}-1$. Converting
via $\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$ gives the stated
bound.

**Independent verification:** 13,617-trial exact-`Fraction` stress test,
$m=2,\ldots,6$, $b_1$ random in the sliver, $B'$ of random count/structure
(uncapped), zero violations of $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$.

**Combined with round-5's Theorem 2** (which already closed $b_1\le
2^{m-1}-1$), this gives: **`Case-B(m,k)` is now fully closed** —
$\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$ for every partition $B$ of
$2^m$ into $\le m+1$ parts with $b_1<2^{m-1}$.

## Scope note (important for downstream use)

This certifies that `Case-B(m,k)` (the $q=0/p=0$ excess-0 sliver arising
from Theorem 2's own peeling reduction) is fully closed. It does **not**
close sub-case (i)'s own separate $e=0$ residual (the window $a_1\in
(2^{k-1},2^{k-1}+1)$ when $m=k$), which the round-22 audit found reduces to
a sum range on the *opposite side* of the relevant threshold
($\mathrm{sum}(R)\in(2^{k-1}-1,2^{k-1})$, below $2^{k-1}$, vs. Case-B(m,k)'s
peel landing at $\mathrm{sum}(B')\in(2^{m-1},2^{m-1}+1)$, above $2^{m-1}$)
— these are two distinct open/closed objects, not interchangeable, contrary
to round 17's characterization. $\mathrm{GT}(m)$ as a whole remains open
because of this separate residual.
