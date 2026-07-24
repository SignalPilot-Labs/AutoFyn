## Status
unsolved

## Approaches tried
- **bijective-mersenne-pairing** (round 6, this file): **DEAD END —
  abandoned at the go/no-go gate, as instructed by the outline.** The
  outline's core mechanism — a direct injection between the "even-parity"
  and "odd-parity" regions of $[0,\infty)$ (in the
  `integral-alternating-sum-formula` sense $A(S)=\int_0^\infty\mathbb
  1[N_S(x)\text{ odd}]\,dx$) respecting a fixed $2{:}1$ length ratio,
  mirroring the ladder's own doubling constant — was tested on $n=2$
  exactly as the outline demanded, **including the outline's own explicit
  warning to test on a *generic* (non-extremal) response, not just the
  cascading-halving family where a $2{:}1$ ratio is true by construction.**
  It fails on the very first generic test case. See "Current best" below
  for the full computation. Reason it fails: the $2{:}1$ ratio in
  `ladder-self-similarity-constant` is a property of the specific
  geometric ladder $p_i=2p_{i+1}$ and of the specific cascading-*halving*
  family of Xiang Yu responses (`cascading-halving-family-characterization`)
  — both built by repeatedly dividing by exactly $2$. It is not a property
  of the alternating-sum functional $A$ itself, nor of a generic legal
  Xiang Yu response, which may cut the ladder pieces at *any* real point,
  producing even/odd regions of arbitrary, unrelated lengths. Since the
  approach's entire mechanism (pair region of length $\ell$ with region of
  length $2\ell$) presupposes exactly this ratio, it has no purchase once
  cuts are generic. No amount of relabeling by "rank/position" rescues
  this: the lengths themselves, not just their order, must stand in a
  $2{:}1$ relationship, and generically they simply don't.

## Current best
Empty — no correct partial result was established; this is a documented
dead end, not a partial proof. The falsifying computation (exact
`Fraction` arithmetic, reproducible) is recorded here for future rounds so
nobody re-attempts this exact mechanism.

**Setup.** $n=2$ ladder (Liu Bang's marks), raw units of $1/7$:
$(p_1,p_2,p_3) = (4,2,1)$. Target: $A(S) \ge 1$ (raw units; $=1/7$ after
rescaling) for every legal Xiang Yu response $S$, with equality exactly at
the known extremal responses (`vertex-minimum-theorem`,
`cascading-halving-family-characterization`).

**Step 1a (sanity check on the known extremal case — composition $(1,1,0)$
at its infimum $a=2,\,b=1$, i.e. exactly $R_2$ from
`cascading-halving-family-characterization`).** $S=\{2,2,1,1,1\}$.
Breakpoint/region decomposition of $N_S(x)$:
- $x\in(0,1)$: $N=5$ (odd), length $1$.
- $x\in(1,2)$: $N=2$ (even), length $1$.

Here the odd region (length $1$) and even region (length $1$) trivially
match the target with no interesting pairing needed ($A(S)=1$ exactly, the
even region contributes nothing to $A$). This case is degenerate and does
not test the mechanism.

**Step 1b (the outline's own required test — a *generic*, non-extremal
composition $(1,1,0)$: $a=1.5$, $b=0.5$, i.e. $p_1=4\to\{2.5,1.5\}$,
$p_2=2\to\{1.5,0.5\}$, $p_3=1$ untouched).**
$S=\{5/2,\,3/2,\,3/2,\,1,\,1/2\}$. Exact computation (verified in Python
with `fractions.Fraction`, zero floating point):

| interval | length | $N(x)$ | parity |
|---|---|---|---|
| $(0,1/2)$ | $1/2$ | $5$ | odd |
| $(1/2,1)$ | $1/2$ | $4$ | even |
| $(1,3/2)$ | $1/2$ | $3$ | odd |
| $(3/2,5/2)$ | $1$ | $1$ | odd |

$A(S)=1/2+1/2+1=2$ (matches direct alternating sum $5/2-3/2+3/2-1+1/2=2$).
The even region has length $1/2$; nothing among the odd regions
($1/2$, $1/2$, $1$) is exactly $2\times1/2=1$ *by necessity* — the value
$1$ does appear, but only coincidentally (it is $p_3$, untouched, not
produced by any doubling relation to the even region). No structural rule
forces this.

**Step 1c (the decisive falsifying case — composition $(2,0,0)$, Xiang Yu
spends both points on $p_1$ with arbitrary, non-special cuts: $p_1=4\to
\{3,\,7/10,\,3/10\}$, $p_2=2,p_3=1$ untouched).**
$S=\{3,\,2,\,1,\,7/10,\,3/10\}$. Exact region decomposition:

| interval | length | $N(x)$ | parity |
|---|---|---|---|
| $(0,3/10)$ | $3/10$ | $5$ | odd |
| $(3/10,7/10)$ | $2/5$ | $4$ | even |
| $(7/10,1)$ | $3/10$ | $3$ | odd |
| $(1,2)$ | $1$ | $2$ | even |
| $(2,3)$ | $1$ | $1$ | odd |

$A(S) = 3/10+3/10+1 = 8/5$ (matches direct sum
$3-2+1-7/10+3/10=8/5$), still $\ge1$ as required, so the *lower bound
itself* is fine here — but look at the region lengths: even regions have
lengths $\{2/5,\,1\}$, odd regions have lengths $\{3/10,\,3/10,\,1\}$.
There is **no pairing** of even regions to odd regions in which every
paired odd length is exactly twice (or half) its partner's length:
$2\times(2/5)=4/5$ is not among $\{3/10,3/10,1\}$; $2\times1=2$ is not
among them either; nor does $1/2$ of either even length appear among the
odd lengths. The $2{:}1$ structure that held (trivially) in the
cascading-halving family is simply **absent** for this generic, equally
legal Xiang Yu response.

**Conclusion of the go/no-go test.** Step 1 fails at the very case the
outline itself flagged as the real test (a generic, non-extremal
response). The mechanism only "works" on the cascading-halving family
because that family is *defined* by repeated exact halving, which
manufactures the $2{:}1$ ratio by hand; it is not a consequence of the
functional $A$, the ladder's target value, or of the game's legality
constraints. Per the outline's explicit stop condition ("If no such
pairing is found within a half-round's effort... downgrade/abandon
immediately"), this approach is abandoned without proceeding to steps
2–4 (generalizing to $n=3$ / general $n$). No further build effort should
be spent on a direct fixed-ratio region-pairing mechanism; any future
revival of the "bijective/pairing" idea should pair *pieces* by some
invariant other than a literal length ratio (e.g. by count/rank alone, as
`odd-run-reduction-lemma` already does), not by insisting paired regions'
lengths differ by exactly a factor of $2$.

## Full proof
(absent — Status is `unsolved`; this file documents a dead end)
