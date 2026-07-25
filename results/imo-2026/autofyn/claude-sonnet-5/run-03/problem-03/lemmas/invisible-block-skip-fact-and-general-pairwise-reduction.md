## Source
`approaches/self-similar-induction-on-n.md`, round 20, "Round 20: closing
the multi-gap same-parity gap flagged by the round-20 outline-reviewer,"
Steps 1–3. Certified by the round-20 proof-reviewer after full independent
re-derivation and stress-testing (own exact-`Fraction` scripts, not
reusing the builder's), specifically targeting the exact cross-Γ-gap
same-parity configuration the round-20 outline-reviewer flagged as
unaddressed.

## Setting

$\mathrm{GCH}(k)$: $R$ a finite multiset with $\max(R)\le\mathrm{cap}:=
2^{k-1}$, $|R|\le k+1$, $\mathrm{sum}(R)=S\in[2^k,2^k+1)$; $\Gamma_{k-1}=
\{2^{k-1},\dots,2,1\}$. $\mathrm{AltSum}(M)$ is the alternating sum of $M$
sorted in weakly decreasing order (rank 1 gets $+$). A value $v$ occurring
in $R$ is *free* if $v\notin\Gamma_{k-1}$; free and *active* if in
addition its $R$-multiplicity is odd.

## Fact 1 (Invisible-Block Skip Fact)

If a value $z$ occurs with even multiplicity $m$ in a multiset $M$, a
coordinate $x\notin M$ moving continuously across $z$'s entire block (all
else fixed) has its rank in $M\cup\{x\}$ shift by exactly $m$ (even), so
its rank parity — hence its $\mathrm{AltSum}$ sign, and the slope of
$\mathrm{AltSum}$ under any mass-conserving two-coordinate perturbation
involving $x$ — is unchanged across the crossing. Elementary (immediate
from the definition of rank); a trajectory-level strengthening of the
already-certified Corollary of Lemma BCF
(`tied-pair-cancellation-and-block-contribution-formula.md`).

## Theorem (General Pairwise Reduction Lemma)

For $R$ feasible in $\mathrm{GCH}(k)$ with two distinct **active** free
values $w_i\ne w_j$ — no restriction on which $\Gamma$-gaps they occupy,
adjacency, or rank parity — there is a feasible $R'$ with $\mathrm{sum}
(R')=\mathrm{sum}(R)$, $|R'|=|R|$, $\mathrm{AltSum}(R'\cup\Gamma_{k-1})
\le\mathrm{AltSum}(R\cup\Gamma_{k-1})$, and strictly fewer distinct active
free values than $R$.

*Proof.* Move one representative of each of $w_i,w_j$ along the
mass-conserving line $w_i\mapsto w_i+t,\ w_j\mapsto w_j-t$. By Fact 1, the
only points that can break affineness of $\mathrm{AltSum}(R(t)\cup
\Gamma_{k-1})$ in $t$ are members of the active boundary set $B:=
\{0,\mathrm{cap}\}\cup\{$Γ-levels with even $R$-multiplicity among the
untouched coordinates$\}\cup\{$other active free values of $R\}$, or the
meeting point $w_i+t=w_j-t$. On the maximal interval $[t_{\min},t_{\max}]$
avoiding these, $\mathrm{AltSum}$ is affine with slope $\sigma\in\{-2,0,
2\}$ (the rank-parity sign difference at $t=0$). If $\sigma\ne0$, move to
the sign-decreasing endpoint (strict decrease); if $\sigma=0$ (the
previously-unaddressed same-parity case, including cross-gap), the value
is exactly constant on the whole interval (equality, still weakly
non-increasing). At the endpoint reached, one of four things happens
(hits an even-multiplicity $\Gamma$-level; hits $0$ or $\mathrm{cap}$;
merges with another active free value, making it inactive; or the two
moving coordinates meet, combining to even multiplicity) — in every case
the active free value count strictly decreases. $\blacksquare$

## Theorem (Finite Reduction Theorem)

Every feasible $R$ of $\mathrm{GCH}(k)$ admits a feasible $R''$ with
$\mathrm{sum}(R'')=\mathrm{sum}(R)$, $|R''|\le|R|$, $\mathrm{AltSum}
(R''\cup\Gamma_{k-1})\le\mathrm{AltSum}(R\cup\Gamma_{k-1})$, and at most
one distinct active free value. Proved by iterating the General Pairwise
Reduction Lemma; the number of distinct active free values is a strictly
decreasing nonnegative integer, so the process terminates in $\le k+1$
steps.

**Consequence.** It suffices to prove $\mathrm{AltSum}(R''\cup
\Gamma_{k-1})\ge1$ for every feasible $R''$ with at most one active free
value — a finite, per-$k$ combinatorial statement about integer
multiplicity vectors plus a single free block. This statement itself
remains **open** for general $k$ (proved for $k=2$, numerically
corroborated for $k=3,4,5$) — not part of this certification.

## Independent verification (round-20 proof-reviewer)

Own exact-`Fraction` scripts (not reusing the builder's), built directly
from the theorem statements, not the file's worked examples:

- **General Pairwise Reduction Lemma**, general stress test: 59,952
  random trials, $k=2,\dots,6$, arbitrary R, exact computation of the
  maximal affine interval via exact breakpoint algebra (not a coarse
  numerical grid — an earlier grid-based attempt produced spurious
  "violations" traced to grid-resolution artifacts near the domain
  boundary, corrected before the final run) — zero violations of
  $\mathrm{AltSum}$-non-increase, active-count strict decrease,
  feasibility, or sum-preservation, in every one of four categorized
  configurations (same-gap/diff-gap $\times$ same-parity/diff-parity).
  **22,632 of these trials are specifically the flagged
  different-Γ-gap-same-parity configuration** (the exact gap the
  round-20 outline-reviewer raised) — zero violations there.
- Reproduced the file's own hand-built $k=6$ worked example
  ($x_0=20,y_0=3$) exactly: confirmed $\mathrm{AltSum}=22$ constant on
  the **true** maximal affine interval $t\in(-1,1)$ (endpoints at $y=4$
  and $y=2$, both $\Gamma$-levels) — and confirmed $\mathrm{AltSum}$
  genuinely changes (jumps to $23$) at $t=-3/2$, which lies **outside**
  this true interval, showing the file's own Step 0 write-up tested one
  point ($t=-3/2$) beyond the interval it was describing as
  "$22$ throughout" (a phrasing looseness, not a mathematical error —
  the file's boundary claim, $t=\pm1$, is exactly correct).
- **Finite Reduction Theorem**, full-reduction termination test: 4,000
  random feasible $R$, $k=2,\dots,6$, iterating the certified lemma to
  termination — zero non-monotonicity, zero infeasibility, zero
  sum-mismatches, zero non-termination; observed max steps $6\le k+1=7$.

## One correction made during certification (non-load-bearing)

The source file's "why this closes the flagged gap" paragraph asserts
"same gap, same parity — vacuous, since two distinct values in one gap
are automatically adjacent hence opposite parity." **This is false in
general**: when $R$ has $\ge3$ distinct active free values inside one
$\Gamma$-gap, two *non-adjacent* same-gap values can have the same rank
parity (confirmed by the reviewer's own stress test: 3,301 of the 59,952
trials above fall in exactly this "same-gap, same-parity" category, with
zero violations of the Lemma there too). This does **not** threaten the
Lemma or its proof — the proof of the General Pairwise Reduction Lemma
never invokes this vacuity claim; it handles the $\sigma=0$ case
uniformly regardless of gap structure. The claim is an incidental,
non-load-bearing mis-classification in the exposition, not a gap in the
mathematics; it should be corrected (deleted or fixed) in the source file
text but does not affect certification of the theorems above.

## Status
**Certified** — Invisible-Block Skip Fact, General Pairwise Reduction
Lemma, and Finite Reduction Theorem all proved in full and independently
re-verified, specifically covering the round-20-flagged
different-gap-same-parity configuration. The combinatorial closure this
reduces to (general $k$) remains open and is explicitly **not** certified
here.
