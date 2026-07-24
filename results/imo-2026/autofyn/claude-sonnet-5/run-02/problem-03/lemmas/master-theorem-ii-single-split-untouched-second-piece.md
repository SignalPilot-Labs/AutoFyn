# Master Theorem II: Single-Split-Plus-Untouched-Second-Piece Bound

**Certified: round 28 (proof-reviewer), from `rank-pigeonhole-budget.md`
§7.16.**

## Statement

For the unit ratio-2 ladder $\pi=(\pi_1,\pi_2,\pi_3,\pi_4)=(8,4,2,1)$
(units of $1/15$), any single split of $\pi_1\to\{a,8-a\}$ ($a\in[0,4]$,
one cut, so $a$ ranges over the smaller fragment), $\pi_2=4$ left
untouched, and *any* legal refinement $V$ of $(\pi_3,\pi_4)$ using any
number of cuts distributed in any way — only $\mathrm{Total}(V)=\pi_3+
\pi_4=3$ is used, not the cut count or its distribution —
$$A(\{a,8-a,4\}\cup V)\ \ge\ 1.$$

## Proof sketch (full proof in the approach file, §7.16 "Master Theorem
II")

Three cases on $a$ (writing $b=8-a\ge4$):
- $a<4$: $b$ is the strict unique max of $\{a,b,4\}\cup V$ (every element
  of $V$ is $\le\pi_3=2<4<b$); peel $b$ via `sharp-dominant-removal-
  identity`. Then $4$ is the strict unique max of the remainder; peel
  again. This reduces the target to $A(\{a\}\cup V)\ge a-3$, closed by
  `alternating-sum-nonnegativity` ($A\ge0$) when $a\le3$, and by one more
  peel (of $a$ itself, now dominant over $V$) plus the trivial bound
  $A(V)\le\mathrm{Total}(V)=3$ when $a\in(3,4)$.
- $a=4$ (so $b=4$ too): $U=\{4,4,4\}\cup V$, multiplicity $3$ (odd);
  `odd-run-reduction-lemma` reduces the three $4$'s to one, then peel and
  apply the trivial bound on $V$.

## Verification

Reviewer independently re-verified with a fresh exact-`Fraction` script
(2000 random trials per shape, all 3 shapes $(1,0,0,2),(1,0,1,1),
(1,0,2,0)$ realizing this template): zero violations of $A(U)\ge1$.

## Scope

Directly reusable for any future closure needing "one cut on the top
piece, second piece untouched, arbitrary refinement below" — the proof
never used a cap on $V$'s cut count, only its total mass, so this
generalizes beyond the specific ladder instance it was derived for
whenever the same three qualitative facts hold (top piece split once,
second piece untouched and dominates the rest, tail total mass fixed).
Does **not** cover shapes where the second piece is also cut, or where
the top piece receives more than one cut — those remain open (see the
approach file's §7.16 "Net status").
