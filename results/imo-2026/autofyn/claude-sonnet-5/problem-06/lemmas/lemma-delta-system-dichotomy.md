# Δ-System (Sunflower) Dichotomy for Uniformly Bounded Finite-Set Families

**Source.** `results/imo-2026-06/approaches/sunflower-bundle-closure.md`
(round 8, §4a). Standard classical combinatorial fact (confirmed absent from
`knowledge_base.md` and the crux corpus by this round's outline search),
proved here from scratch. General-purpose, not specific to this problem.

## Statement

Let `𝓕` be an infinite family of pairwise distinct finite sets, each of size
`≤M` (`M≥0` fixed), drawn from an arbitrary (possibly infinite) universe.
Then `𝓕` has an infinite sub-family `𝓕'` that is either:

(a) **pairwise disjoint**, or

(b) a **sunflower**: there is a fixed nonempty set `Y` (the *core*) with
`Y⊊F` for every `F∈𝓕'`, and the *petals* `{F∖Y:F∈𝓕'}` are pairwise disjoint
and nonempty.

## Proof

By induction on `M`.

**Base case `M=0`.** Every `F∈𝓕` has `F=∅`; pairwise distinctness forces
`|𝓕|≤1`, contradicting infinitude — vacuous.

**Inductive step (`M≥1`, assuming the statement for bound `M-1`).** Let `𝓕`
be infinite, sets of size `≤M`. Build a sub-family greedily: pick
`F_1∈𝓕` arbitrarily; having picked pairwise disjoint `F_1,…,F_r`, if some
`F∈𝓕` is disjoint from `F_1∪⋯∪F_r`, pick `F_{r+1}:=F` and continue.

- If the process never terminates, `{F_1,F_2,…}` is an infinite
  pairwise-disjoint sub-family: case (a).
- If it terminates after finitely many steps `r`, every `F∈𝓕` intersects
  `U:=F_1∪⋯∪F_r` (else the process would continue); `U` is finite
  (`|U|≤rM`). Since `𝓕∖{F_1,…,F_r}` is still infinite and every member
  intersects the finite set `U`, pigeonhole gives a fixed `u∈U` in
  infinitely many members of `𝓕∖{F_1,…,F_r}` — call this infinite
  sub-family `𝓕_u`.

  `𝓕_u':={F∖{u}:F∈𝓕_u}` is an infinite family (the map `F↦F∖{u}` is
  injective on `𝓕_u` since all members contain `u` and are pairwise
  distinct) of pairwise distinct sets of size `≤M-1`. By the inductive
  hypothesis, `𝓕_u'` has an infinite sub-family that is pairwise disjoint or
  a sunflower with some core `Y'`.

  - If pairwise disjoint: `𝓕':={F∈𝓕_u:F∖{u}∈𝓕_u''}` (infinite) is a
    sunflower with core `{u}` (petals `F∖{u}` pairwise disjoint by
    hypothesis; discard the at-most-one member with `F∖{u}=∅`, still
    leaving an infinite sub-family).
  - If a sunflower with core `Y'`: `𝓕':={F∈𝓕_u:F∖{u}∈𝓕_u''}` (infinite) is
    a sunflower with core `Y:=Y'∪{u}` (petals `F∖Y=(F∖{u})∖Y'`, exactly the
    petals of `𝓕_u''`).

  Either sub-case gives case (b). `∎`

*(No finiteness of the ambient universe is used anywhere — only that each
set has bounded finite size, so every pigeonhole step involves a finite
index set regardless of how large the universe is.)*

## Certification

Fully proved from scratch, standard finite combinatorics, no gap.
Independently re-derived by the round-8 proof-reviewer (hand re-derivation
of both the base case and the inductive pigeonhole/recursion step; confirmed
correct, including the vacuity handling at `M=1`, which the reviewer
double-checked separately: for `M=1`, pairwise-distinct singletons are
automatically pairwise disjoint, so the "terminates" branch of the greedy
process is itself vacuous for `M=1`, consistent with the inductive
structure). General-purpose, reusable outside this problem's context.
Certified `solved`-quality.
