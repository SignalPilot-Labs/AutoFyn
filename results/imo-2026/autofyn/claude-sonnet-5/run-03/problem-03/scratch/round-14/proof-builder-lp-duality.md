# proof-builder report — lp-duality-split-polytope (round 14)

## Task
Attempt the general nonzero-residual fragment-vs-fragment family at $e_0$:
numerically characterize (then try to prove) how a non-perfect-tie
residual trades off against the required split count $s$, using
exact-arithmetic active-set enumeration (kept distinct from
`global-lp-vertex-sufficiency`'s LP/hyperplane numeric search this round).

## What was found
A full, rigorously proved theorem, not just a numeric characterization —
the **Chain-Correction Floor Theorem**: at $e_0$, for every $n\ge6$, an
explicit hybrid construction (active set = all pieces except the smallest
2, i.e. $s=n-1$; pieces 1,2 each tie one fragment to a whole untouched
piece, pieces 3,5 each tie one fragment to a "chain" value derived from
pieces 1/2 respectively, piece 4 and all pieces $6,\dots,n-1$ simply
self-tie into two equal halves) achieves $\mathrm{OddSum}(M)=1/2$ exactly
— the universal absolute floor for any legal response at any partition
(via the elementary fact $\mathrm{AltSum}\ge0$ always).

The proof rests on:
1. An exact algebraic identity: two "chain" values (derived by
   subtracting from pieces 3 and 5 respectively) collapse to the same
   constant $a-2\delta$ for every $N$ — verified symbolically, not
   numerically.
2. A Positivity Lemma ($a>2\delta$, where $a=p_N(e_0)$, $\delta=\gamma(n)$)
   proved by induction for all $n\ge6$ (reduces to $(n+1)(n+4)<2^{n+2}-2$).
3. The already-used Even-Block-Neutrality mechanism, applied to $n-1$
   disjoint equal-valued pairs that partition the entire $2n-2$-element
   response multiset.

Independently re-verified in exact `Fraction` arithmetic for
$n=6,7,8,9,10,12,15,20$ (8 instances): $\mathrm{AltSum}=0$ and total mass
$=1$ exactly in every case (zero deviation), plus the positivity
condition checked exactly in each instance.

## Significance / honest scope
- This decisively answers the round's dispatch question: nonzero residual
  doesn't just modestly beat the Perfect-Tie value (as round 12's numeric
  spot check suggested) — at $s=n-1$ it reaches the theoretical floor.
- It surfaces a likely **correction** to the existing record: `current.md`
  and `global-lp-vertex-sufficiency.md` state "$V(e_0)=c(n)$ exactly"
  (established there only via the $k$-Anchor-Merge upper-bound
  construction). This round's construction is an equally legal response
  at the same $e_0$ achieving strictly less ($1/2<c(n)$), so the true
  minimax value is $V(e_0)=1/2$ for $n\ge6$, not $c(n)$. This is flagged
  explicitly for the reviewer/other approach to reconcile — I did not
  edit any file other than my own approach file, per the ownership rule.
  It is good news for the overall program (the actual target only needs
  $V(p)\le c(n)$ everywhere; $e_0$ turns out to be even less binding than
  previously recorded), not a threat to any established result.
- Genuinely open, not resolved this round: whether smaller $s$ (more than
  2 untouched pieces) can also reach the floor (an unreliable float-only
  local-optimizer scan hinted it might for $m=3,\dots,6$ at a few $n$, but
  this is explicitly NOT claimed as established — flagged as a lead only);
  the cases $n=2,3,4,5$ (too few active pieces for this specific
  construction, which needs $\ge5$ active pieces).

## Status
Set to `partial` (unchanged for the approach as a whole — the fully
general residual-vs-$s$ trade-off and smaller-$s$/small-$n$ cases remain
open), but with a new, complete, independently-checkable theorem proposed
for certification (not self-certified, per protocol).

## Files touched
- `/home/agentuser/repo/results/imo-2026-03/approaches/lp-duality-split-polytope.md`
  (new "Round 14 update" section at top, new "Approaches tried" round-14
  entry, new "Current best" round-14 paragraph, new "Promotable lemmas"
  entry for the Chain-Correction Floor Theorem).
- No other approach files or `current.md` were edited (per ownership
  rule) — the flagged correction to `global-lp-vertex-sufficiency.md`'s
  "$V(e_0)=c(n)$ exactly" claim is reported in my file only, for the
  reviewer to act on.
