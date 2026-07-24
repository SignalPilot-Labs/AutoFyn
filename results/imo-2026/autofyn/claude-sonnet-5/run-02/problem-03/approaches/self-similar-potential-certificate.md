## Status
partial

## Approaches tried

- **Round 2 (this round).** Diagnosed and fixed the arithmetic bug the
  outline-reviewer flagged in the naive recursion
  $\Psi_n(S) := M-\Psi_{n-1}(S')$ (which reproduces
  $(2^n-1)/(2^{n+1}-1)$, not the target $1/(2^{n+1}-1)$). Traced the bug to
  a *conflation of two different quantities* — the outline's "$M-\Psi_{n-1}$"
  guess silently reused the **unscaled** $(n-1)$-target
  $1/(2^n-1)$ instead of accounting for the fact that the tail must be
  rescaled by $r=1-p_1$ before comparing to the $(n-1)$-ladder (alternating
  sums are homogeneous of degree 1 under positive scaling, so the correct
  self-similar identity is $A(\text{tail, unscaled}) = r\cdot A(\text{tail}/r)$,
  not a bare subtraction). Having fixed the identity itself
  ($f(n):=1/(2^{n+1}-1)$ satisfies $f(n)=r(n)\,f(n-1)$ **exactly**, proved
  below in full and numerically cross-checked), I then tried to build the
  full cut-monotone certificate for arbitrary Xiang-Yu cut-budget splits
  $c=0,\dots,n$ between the top piece $p_1$ and the tail. This succeeds
  **completely and rigorously for $c=0$** (recovering, and in fact
  strengthening, the certified `untouched-top-piece-lower-bound` lemma) and
  produces a new, fully proved, promotable formula for the "above-threshold"
  contribution $A_1$ for *every* $c$ (Lemma B below, a genuine generalization
  of Lemma 6's mechanism to arbitrary top-piece splitting). For $1\le c\le n$
  the argument runs into a genuine, identified obstruction — the low
  fragments of $p_1$ (those $\le r$) *interleave* with the tail's own pieces
  in the sorted order below threshold $r$, so $A(S)$ is **not** simply
  $A_1+A(\text{tail alone})$; I checked by hand (small numeric examples,
  see Lemma D below) that this interleaving can make the naive "insertion
  changes $A$ by at most the mass of what's inserted" bound too weak to
  recover the target — the loss from interleaving needs to be controlled
  more precisely than a mass bound, exactly the same fine case-by-case
  control that `smoothing-compactness-certificate` needed for $n=2$. I
  report this honestly as the approach's core open gap rather than paper
  over it with a numerically-checked but unproved claim.

## Current best

Throughout, write $p_i=p_i(n)=\dfrac{2^{n+1-i}}{2^{n+1}-1}$ ($i=1,\dots,n+1$)
for Liu Bang's ladder at budget $n$, $r=r(n):=1-p_1=\sum_{i\ge2}p_i=
\dfrac{2^n-1}{2^{n+1}-1}$, and $f(n):=\dfrac{1}{2^{n+1}-1}$ (the target value
of $A$). Import the certified lemmas
`claiming-subgame-reduction`, `integral-alternating-sum-formula`,
`leftover-formula`, `must-use-all-n-points`, `untouched-top-piece-lower-bound`
from `results/imo-2026-03/lemmas/`. By `claiming-subgame-reduction` and
`integral-alternating-sum-formula`,
$$\Phi(S)=\frac{1+A(S)}{2},\qquad A(S)=\int_0^\infty \mathbb 1[N(x)\text{ odd}]\,dx,\quad N(x)=\#\{i:L_i>x\},$$
so proving $c(n)=2^n/(2^{n+1}-1)$ reduces to proving
$$\min_{\text{Xiang Yu}} A(S) \ge f(n) \text{ (lower bound, Liu Bang plays the ladder)}, \qquad
\min_{\text{Xiang Yu}} A(S) \le f(n)\text{ for every Liu Bang config (upper bound)}.$$
This approach attacks the **lower bound only**; the upper bound (Step 4 of
the outline) is not attempted this round — the interleaving obstruction
below is the more urgent open item.

### Lemma A (corrected self-similar identity, fully proved)

$f(n) = p_1(n)-r(n)$ **and** $f(n)=r(n)\cdot f(n-1)$ for every $n\ge1$.

*Proof.* First identity: $p_1(n)-r(n) = \dfrac{2^n}{2^{n+1}-1}-\dfrac{2^n-1}{2^{n+1}-1}=\dfrac1{2^{n+1}-1}=f(n)$, a direct subtraction.

Second identity: $r(n)\cdot f(n-1) = \dfrac{2^n-1}{2^{n+1}-1}\cdot\dfrac1{2^n-1} = \dfrac1{2^{n+1}-1}=f(n)$ (valid for $n\ge1$; for $n=1$, $r(1)=1/3$, $f(0)=1/(2^1-1)=1$, product $=1/3=f(1)$, consistent using the convention that the "$0$-game" is the trivial single-piece game with value $A=$ whole mass). $\blacksquare$

This replaces the outline's broken formula "$\Psi_n(S):=M-\Psi_{n-1}(S')$"
(which implicitly used the *unscaled* value $f(n-1)$ in place of the
*rescaled* tail's alternating sum, producing $p_1-f(n-1)=(2^n-1)/(2^{n+1}-1)$,
exactly the wrong answer the reviewer computed) with the correct
scaling-aware statement: alternating sums are positively homogeneous of
degree 1 (immediate from the definition $A(S)=\sum(-1)^{i+1}L_i$: scaling
every $L_i$ by $\lambda>0$ preserves sorted order and scales every term by
$\lambda$), so if $G$ is the tail multiset with $\mathrm{Total}(G)=r$, then
$A(G) = r\cdot A(G/r)$ where $G/r$ is $G$ rescaled to total mass $1$. Lemma A
confirms this rescaling lands exactly on $f(n)$ when $G/r$ is itself the
$(n-1)$-ladder, i.e. the self-similar recursion for the *target constant*
is $f(n)=r(n)f(n-1)$, not the outline's additive guess.

### Lemma B (generalized above-threshold contribution, fully proved)

Fix $n\ge1$ and let Xiang Yu split his $\le n$ marks as $c$ marks cutting
$p_1$ into fragments $f_1\ge\dots\ge f_{c+1}>0$ (summing to $p_1$,
$0\le c\le n$) and the remaining $\le n-c$ marks refining the tail
$\{p_2,\dots,p_{n+1}\}$ into some multiset $G'$ (summing to $r$). Then, on
the interval $[r,p_1)$, every tail piece is $\le r\le x$
(since $G'$ has total mass $r$, no single piece of $G'$ can exceed $r$), so
$N(x)$ restricted to $[r,p_1)$ counts only fragments of $p_1$:
$$A_1:=\int_r^{p_1}\mathbb 1[N(x)\text{ odd}]\,dx = \max(f_1-r,\,0).$$

*Proof.* First, **at most one fragment exceeds $r$**: since
$f_1+\dots+f_{c+1}=p_1$ and (for the ladder) $p_1<2r$ whenever $n\ge2$, with
equality $p_1=2r$ at $n=1$ (check: $p_1-2r=p_1-2(1-p_1)=3p_1-2$, and
$p_1=2^n/(2^{n+1}-1)$ gives $3p_1-2 = (3\cdot2^n-2(2^{n+1}-1))/(2^{n+1}-1)
=(2-2^n)/(2^{n+1}-1)\le0$ for $n\ge1$, with equality iff $n=1$) — if two
fragments $f_i,f_j$ ($i\ne j$) both exceeded $r$, then $f_i+f_j>2r\ge p_1$,
contradicting $f_i+f_j\le p_1$. So at most one fragment exceeds $r$; since
the fragments are sorted descending, if any exceeds $r$ it must be $f_1$.

Case $f_1\le r$: then no fragment exceeds $r$, so for every $x\in[r,p_1)$,
$N(x)=0$ (even), giving $A_1=0=\max(f_1-r,0)$.

Case $f_1>r$: then $f_2,\dots,f_{c+1}\le r$ (as just shown, at most one
fragment exceeds $r$). For $x\in[r,f_1)$: $f_1>x$ and every other fragment
is $\le r\le x$, so $N(x)=1$ (odd). For $x\in[f_1,p_1)$: no fragment exceeds
$x$ (since $f_1\le x$ and all others $\le r\le f_1\le x$), so $N(x)=0$
(even). Hence the odd-parity region within $[r,p_1)$ is exactly $[r,f_1)$,
of measure $f_1-r=\max(f_1-r,0)$. $\blacksquare$

(When $c=0$, $f_1=p_1$, giving $A_1=p_1-r=f(n)$ by Lemma A — recovering
exactly the untouched-top-piece computation.)

### Lemma C (budget monotonicity, fully proved)

For any fixed multiset of $m$ pieces with total mass $T$, and any
$0\le k\le n$, the minimum over Xiang-Yu responses using **at most $k$**
marks of $A(\text{response})$ is $\ge$ the minimum over responses using
**at most $n$** marks.

*Proof.* Every strategy using at most $k\le n$ marks is, in particular, a
strategy using at most $n$ marks (the problem's rule is "at most $n$
points," a threshold, not an exact count — a player is never forced to use
all his marks). Hence the feasible set for budget $k$ is a subset of the
feasible set for budget $n$, so the minimum of $A$ over the smaller feasible
set is $\ge$ the minimum over the larger one. $\blacksquare$

### Full closure of the $c=0$ sub-case (fully proved, imported/strengthened)

If $c=0$ (Xiang Yu leaves $p_1$ entirely uncut), then $F=\{p_1\}$ is a
single piece with $p_1>r$ (true for the ladder since $p_1=2^n/(2^{n+1}-1)>
1/2\ge r$... more precisely $p_1>r\iff p_1>1-p_1\iff p_1>1/2$, and
$2^n/(2^{n+1}-1)>1/2\iff 2^{n+1}>2^{n+1}-1$, always true). Since $p_1$
exceeds every piece of $G'$ (each $\le r<p_1$), $p_1$ occupies rank $1$
in the full sorted multiset $S=\{p_1\}\cup G'$ and every $G'$-piece's rank
in $S$ is exactly one more than its rank within $G'$ alone. Hence
$$A(S) = p_1 - A(G')_{\text{as if listed after rank 1}} \;=\; (p_1-r) + \big(r-A(G')\big)+A(G')... $$
— more directly, by Lemma B with $c=0$, $A_1=p_1-r=f(n)$ exactly (no
approximation), and since $[0,r)$ then only sees $G'$ (as $F=\{p_1\}$
contributes nothing below $r$), $A_2=A(G')$ exactly, so
$$A(S) = f(n) + A(G').$$
By `untouched-top-piece-lower-bound` (certified), $A(S)\ge f(n)$ (equivalent
to $\Phi\ge p_1$), which combined with $A(S)=f(n)+A(G')$ and $A(G')\ge0$
(alternating sums of a multiset are always $\ge0$: this is part of the
certified `integral-alternating-sum-formula` lemma, $0\le A(S)\le
\mathrm{Total}(S)$) reproves the same conclusion; in fact it shows the
stronger $A(S)=f(n)+A(G')\ge f(n)+f(n)=2f(n)$ whenever $A(G')\ge f(n)$
also holds (true, since $G'$'s refinement uses $\le n$ marks and $A(G')\ge
f(n)$ is exactly what `untouched-top-piece-lower-bound` already
establishes for the tail alone). Either way, $A(S)\ge f(n)$: the $c=0$
case is fully closed, matching the certified lemma exactly, with an
explicit (non-numeric) computation of $A_1$ via Lemma B rather than the
original ad hoc integral-splitting argument.

### The open gap: $1\le c\le n$

For $1\le c\le n$ (Xiang Yu cuts $p_1$ at least once), Lemma B still gives
the exact value $A_1=\max(f_1-r,0)$. But now, **when $f_1\le r$ (so
$A_1=0$) or more generally whenever $c\ge1$, the low fragments
$f_2,\dots,f_{c+1}$ (and $f_1$ itself if $f_1\le r$) all lie in $[0,r)$ and
interleave in sorted order with the pieces of $G'$**, which also lie in
$[0,r)$ (total mass $r$). The remaining contribution
$$A_2 = \int_0^r \mathbb1[N(x)\text{ odd}]\,dx,\qquad N(x)=\#\{\text{low fragments}>x\}+\#\{G'\text{-pieces}>x\},$$
is **not** in general equal to $A(G')$ alone, nor to $A(F_{\mathrm{low}})+
A(G')$, because inserting the low fragments into $G'$'s sorted order shifts
the parity of ranks of $G'$-pieces above the insertion point. I derived
(by the standard "insert one element into a sorted list" identity: if $v$
is inserted into sorted $g_1\ge\dots\ge g_m$ at position $j$, then
$A(\text{new}) - A(\text{old}) = (-1)^{j+1}\big(v-2\tau_j\big)$ where
$\tau_j:=\sum_{i\ge j}(-1)^{i-j}g_i\in[0,g_j]$ is a partial alternating
sum) that a single insertion of mass $v$ changes $A$ by an amount whose
magnitude can approach $v$ (checked exactly: $G=\{1,\varepsilon\}$,
insert $v=1-\varepsilon'$ just below $1$ gives $A(\text{new})-A(\text{old})
\to -v$ as $\varepsilon,\varepsilon'\to0$). Summing this bound over the
(at most $c+1$) low-fragment insertions gives only
$$A(S) \ge A(G') - (p_1 - A_1) \ge f(n) - p_1,$$
using Lemma C to still get $A(G')\ge f(n)$ (tail budget $n-c\le n$, so
Lemma C applies with the *same* target as the untouched-top-piece lemma,
which is itself computed at full budget $n$ — this composition is valid
and is a genuine correct sub-result). But $f(n)-p_1$ is **negative** for
every $n\ge1$ (since $p_1>1/2>f(n)$), so this bound is strictly weaker than
the trivial $A(S)\ge0$ and useless for proving $A(S)\ge f(n)$. **The
mass-based insertion bound is provably too weak**; recovering the target
requires controlling the *exact* interleaving pattern (which low fragment
lands at which rank relative to $G'$'s pieces), which is precisely the
fine case-by-case sorted-order analysis that `smoothing-compactness-certificate`
carries out for $n=2$ by hand. I was not able, in the time available this
round, to find a single closed-form argument that handles all interleaving
patterns for general $n$ and general $c$ at once — this is the honest,
identified open gap of this approach, and I do not believe (based on the
above negative result for the naive bound) that a purely mass-based /
insertion-counting certificate can close it; a certificate would need to
track *rank*, not just mass, which likely means falling back to an
explicit strategy or template-enumeration argument — i.e. this approach,
after the fix, converges onto the *same* combinatorial core difficulty
identified by `greedy-halving-adversary` and `smoothing-compactness-certificate`,
rather than avoiding it via a slicker closed-form certificate. This is
reported as a genuine (negative) finding, not swept under a numeric check.

## Full proof
(absent — Status is `partial`; see "Current best" for what is fully
established and the precisely located open gap.)

## Promotable lemmas

- **Lemma A (corrected self-similar identity)**: $f(n):=1/(2^{n+1}-1)$
  satisfies $f(n)=p_1(n)-r(n)$ and $f(n)=r(n)\cdot f(n-1)$ for all $n\ge1$,
  where $p_1(n)=2^n/(2^{n+1}-1)$, $r(n)=1-p_1(n)$ — proved in full above by
  direct algebra, corrects the broken recursion flagged by the outline
  reviewer. Reusable by any approach needing the ladder's exact
  self-similarity constant.
- **Lemma B (generalized above-threshold formula)**: for Xiang Yu splitting
  his cuts as $c$ on $p_1$ (fragments $f_1\ge\dots\ge f_{c+1}$) and the rest
  on the tail, the contribution of $A(S)$ from $x\in[r,p_1)$ is exactly
  $\max(f_1-r,0)$ — proved in full above (generalizes the certified
  `untouched-top-piece-lower-bound`'s $c=0$ computation to every $c$).
  Reusable by `greedy-halving-adversary`, whose "repaired Lemma 6" skeleton
  needs exactly this fact for its $A_1$ term.
- **Lemma C (budget monotonicity)**: restricting a player to at most
  $k\le n$ marks can only increase (weakly) the game value that the
  *opponent's* minimization achieves against him, since a $k$-mark strategy
  is a special case of an $n$-mark strategy — a one-line but load-bearing
  fact, proved in full above, resolving the "monotonicity-in-budget" gap
  flagged in the outline for `greedy-halving-adversary`'s repaired Lemma 6
  without needing a separate induction.
- **Negative result (not a lemma to certify, but worth recording in
  Approaches tried for future rounds)**: the naive mass-based insertion
  bound $A(F_{\text{low}}\cup G')\ge A(G')-\mathrm{Total}(F_{\text{low}})$
  is real (provable) but is *provably insufficient* to close the general
  lower bound, since it degrades to the vacuous $A(S)\ge f(n)-p_1<0$. Any
  future certificate-style approach to this problem should not retry a
  purely mass-based interleaving bound; it needs to track rank/position,
  not just mass.

## Outline update (round 3, proof-outliner)

New, relevant finding from the round-3 integer-lattice explorer
(`/tmp/round-3/math-explorer-integer-lattice.md`): the *other* extreme of
this approach's own territory — $c=n$ (Xiang Yu spends **all** $n$ cuts
fragmenting $p_1$ into a rescaled copy of the $n$-ladder, tail untouched) —
also has an exact, elementary closed form matching the target,
$A=1/(2^{n+1}-1)$, proved (not just checked numerically) via a rigid strict
alternation of merge order and this approach's own scaling machinery (Lemma
A/`ladder-self-similarity-constant`). This approach's write-up closes $c=0$
via self-similarity but explicitly does not notice or attempt $c=n$. Rather
than revise this file's own interleaving argument (the negative result
above — mass-based insertion bounds are provably too weak — still stands
and should not be re-attempted), the two exact endpoints ($c=0$ here, $c=n$
new) are now the seed of a new sibling approach, `self-similar-bracketing`,
opened this round: it brackets the interior $c\in\{1,\dots,n-1\}$ between
these two tied-exact values and attacks monotonicity-in-$c$ / an induction on
Xiang Yu's cut count, rather than the interleaving bound this approach
already showed insufficient. If that approach's induction succeeds, it would
close this approach's open gap using this file's own Lemma A/B as
foundational pieces (both are reusable and remain sound). No change is made
to this file's own (correct) negative result or its proved lemmas.
