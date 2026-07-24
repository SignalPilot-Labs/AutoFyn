# Lemma A: General Anchored-Tie Bound (both parities)

**Certified: round 28 (proof-reviewer), from `greedy-halving-adversary.md`
new §"Round 28" section.**

## Statement

Let $w>0$ and let $X$ be a finite multiset of positive reals with
$\max(X)<w$. Let $g:=w-\mathrm{Total}(X)$. Let $t^\ast>0$ occur in $X$
with multiplicity $\mu\ge1$ (any parity). Then
$$A(\{t^\ast\}\cup\{w\}\cup X)\ \ge\ g+t^\ast,$$
where $A(S):=\sum_{i\text{ odd rank, descending sort}}L_i-\sum_{i\text{
even rank}}L_i$ is the standard alternating-sum functional used
throughout this problem's population.

Both parities of $\mu$ are covered: for $\mu$ odd this is exactly the
already-certified `anchored-single-tie-deletion-bound`; for $\mu$ even
it is a from-scratch reproof, in general (non-ladder-specific) notation,
of the mechanism certified in ladder-specific notation as
`even-multiplicity-non-maximal-tie-closure`. The proof uses only
$w>\max(X)$, $g=w-\mathrm{Total}(X)$, and $t^\ast\in X$ — no ladder
structure (no doubling ratio, no specific scale) anywhere.

## Proof sketch (full proof in the approach file)

- $\mu$ odd: `sharp-dominant-removal-identity` peels $w$ off cleanly
  ($w>\max(X)\ge\max(X\setminus\{t^\ast\})$ and $w>\max(X\cup\{t^\ast\})$),
  `odd-run-reduction-lemma` cancels one occurrence of $t^\ast$, and the
  trivial bound $A(S)\le\mathrm{Total}(S)$ finishes it.
- $\mu$ even, $\mu\ge2$: split $X$ (sorted descending) at $t^\ast$'s rank
  into $H:=X_{>t^\ast}$ and $L:=X_{<t^\ast}$. The Rank-Split Formula
  ($A(S)=A(P)+(-1)^kA(Q)$ for a split at position $k$) plus
  `odd-run-reduction-lemma` (the $\mu$ even copies of $t^\ast$ cancel
  against $L$) gives $A(X)=A(H)+(-1)^kA(L)$. Applying
  `insert-element-identity` (inserting $t^\ast$ into $\{w\}\cup X$) and
  `sharp-dominant-removal-identity` twice (peeling $w$ off both
  $\{w\}\cup H$ and $\{w\}\cup X$) yields an exact identity for $A(B)$,
  $B:=\{t^\ast\}\cup\{w\}\cup X$, in terms of $g$, $\mathrm{Total}(H)-A(H)$,
  $\mathrm{Total}(L)\pm A(L)$, and $\mu t^\ast$. The trivial bound
  $\mathrm{Total}\ge A$ and `alternating-sum-nonnegativity` ($A\ge0$)
  close both parities of $k=|H|$, giving $A(B)\ge g+(\mu-1)t^\ast\ge
  g+t^\ast$ since $\mu\ge2$.

## Verification

Reviewer independently re-verified via a fresh exact-`Fraction` script
(50,000 random trials, general abstract instantiation, not the ladder
special case): zero violations, minimum slack exactly $0$ (tight, matching
the odd-$\mu=1$ boundary case).

## Scope

Fully general — no ladder assumption. Immediately reusable anywhere a
Theorem-40/41-style anchored-tie bound is needed against a new
anchor/tail pair $(w,X)$, without re-deriving the mechanism or hunting
for a ladder-specific citation.
