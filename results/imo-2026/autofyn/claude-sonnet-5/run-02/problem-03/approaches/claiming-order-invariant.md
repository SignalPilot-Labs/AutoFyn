## Status
unsolved

## Approaches tried
- **claiming-order invariant, adapted from crux `aimo-0117`'s "defer
  commitment" strategy** (round 4, this build). Attempted to build an
  invariant on the *order in which pieces are claimed* in the (already
  certified, solved) claiming-subgame, mirroring the "keep the current
  extremal element in the black box" invariant that wins `aimo-0117`.
  **Dead end, with a structural reason, not just a failed guess** — see
  "Why this framing cannot work" below. Numerically checked the outline's
  first candidate invariant against the on-file $n=3$ vertex example and it
  fails already at the first step (see §2), consistent with the structural
  diagnosis. No repair is proposed because the structural mismatch (§1) rules
  out *any* invariant of this shape, not just this particular guess.

## Current best
Empty. No correct partial progress was produced under this framing. The
diagnostic value of this round's work is entirely negative: it identifies
*why* the `aimo-0117` mechanism cannot transplant here, which should prevent
future rounds from re-attempting a "claiming order" or "defer commitment"
framing for this problem without addressing point §1 first.

## Full proof
(absent — Status is `unsolved`)

---

## 1. Why this framing cannot work: the structural mismatch with `aimo-0117`

`aimo-0117`'s winning mechanism (crux corpus, `domain=combinatorics`,
`subtopic=games-and-strategy`) is a genuinely **sequential, adaptive**
two-player process: Jesse and Tjeerd alternate one atomic move at a time —
Jesse writes one new value and places one stone, then Tjeerd (seeing the
current state) may move *one* stone, then Jesse acts again, etc., for $n$
full rounds. The winning invariant ("the current largest power of two sits
in the black box") is a **loop invariant maintained across many alternating
moves**: Jesse's strategy at each of his turns depends on what Tjeerd did
on the *immediately preceding* turn (defer the extremal commitment until
Tjeerd frees the target cell, otherwise play a safe smaller value). The
invariant only has content because there are many rounds of real-time,
alternating information exchange for it to be inductively re-established
across.

Our problem's marking stage has **no such structure**. Re-reading the
problem statement precisely: "Liu Bang marks at most $n$ points on the
stick, and then Xiang Yu marks at most $n$ points on the stick." This is a
**two-move Stackelberg game, not an alternating stone-game**:

- Liu Bang chooses his *entire* set of $\le n$ marks in one shot, with no
  intervening information from Xiang Yu (there is nothing to defer against
  yet — Xiang Yu hasn't moved).
- Xiang Yu then chooses his *entire* set of $\le n$ marks in one shot, with
  full information of Liu Bang's marks, but Liu Bang gets no further move to
  react to *that* choice.

So there is exactly **one** round of "move, then adaptive response," not $n$
alternating rounds. A "defer commitment until the opponent's next move
reveals information, then react" invariant needs $\ge 2$ real
back-and-forth exchanges to have any content (Jesse's whole strategy in
`aimo-0117` is *itself* the multi-round loop). Here there is only one
exchange total (Liu Bang's marks $\to$ Xiang Yu's marks), so there is no
"loop" to maintain an invariant across. Xiang Yu's problem, given Liu
Bang's fixed marks, is a **static continuum optimization** (minimize
$\Phi$ over his $\le n$ additional cut points) — exactly the object the
`vertex-minimum-theorem` / LP-vertex approaches already attack directly,
not a sequential game with room for a "defer" trick.

The **claiming stage** (after both mark sets are fixed and the stick is
cut) *is* literally sequential — Liu Bang and Xiang Yu alternate claiming
pieces one at a time. But this outline's own premise (correctly, per the
outline itself) already used the certified `claiming-subgame-reduction`
lemma: at the claiming stage, both players' *unique* best response at
every step is "claim the currently-largest unclaimed piece." This is not a
strategic choice that a cleverer "defer" strategy could improve on — the
lemma is a proved *equality* (the greedy claiming order is forced, and its
value is $\Phi(S)=\sum_{i\text{ odd}}L_i$ regardless of tie-breaking). So
the claiming order is a **mechanical, fully-determined sort**, not a
locus of remaining strategic freedom. Any "invariant on claiming order" is
therefore just bookkeeping on a pre-sorted list — arithmetic identity, not
new strategic content — and cannot say anything new about *which* final
multiset $S$ (i.e., which marks) is optimal, which is where the actual open
gap (general-$n$ vertex enumeration, Proposition 10's cross-term
inequality) lives.

In short: **`aimo-0117`'s mechanism needs a multi-round adaptive loop to
have content; our game has at most one round of adaptive response at the
marking stage, and zero remaining strategic freedom at the claiming
stage.** There is no honest way to relocate the "defer commitment" idea
into either stage of this problem.

## 2. Numeric check of the outline's Step-2 candidate invariant (confirms §1)

The outline's first candidate ("after Liu Bang's $k$-th claim, the largest
not-yet-claimed piece is smaller than $(\text{LB running total} - \text{XY
running total})$, scaled by a $k$-dependent factor") was checked, as the
outline requested, against the on-file $n=3$ tie-vertex example from
`rank-tie-vertex-reduction.md` §3: ladder $8,4,2,1$ (units of $1/15$),
composition (1 cut on $p_1$, 1 cut on $p_2$), vertex $a=p_2=4$, $b=p_4=1$,
final multiset $S=\{4,4,3,2,1,1\}$ (units $1/15$), claimed in that sorted
order alternately (Liu Bang first):

```
sorted S = [4, 4, 3, 2, 1, 1]  (units of 1/15)

after LB claim #1 (claims 4): LB_run=4, XY_run=0, largest remaining=4,
    LB_run - XY_run = 4        -> candidate strict inequality "largest
    remaining < LB_run - XY_run" FAILS already (4 < 4 is false; equality,
    not strict domination)
after LB claim #2 (claims 3): LB_run=7, XY_run=4, largest remaining=2,
    LB_run - XY_run = 3        -> holds here (2 < 3)
after LB claim #3 (claims 1): LB_run=8, XY_run=6, largest remaining=1,
    LB_run - XY_run = 2        -> holds here (1 < 2)
```

Python verification (exact `Fraction` arithmetic, not floats):
LB total = 8, XY total = 7, Phi = 8/15 — matches the certified c(3) value.

Two observations, both consistent with §1's diagnosis:
1. The invariant already fails (as a strict inequality) at the very first
   claim, exactly where it would need to hold to seed an induction — this
   is not a minor scaling-constant issue, it is a structural failure at the
   base of the induction.
2. Even where it happens to hold (claims #2, #3), it is a **trivial
   consequence of $S$ already being sorted** (largest remaining piece in
   any suffix of a sorted list is automatically bounded by simple partial-sum
   arithmetic on that same fixed list) — it does not encode any information
   about *why* this particular $S$ (arising from this particular Liu
   Bang/Xiang Yu mark choice) is extremal among all multisets Xiang Yu could
   have produced. That is, it cannot distinguish the ladder's optimal $S$
   from a non-optimal one, so even a corrected/repaired version of this
   invariant could not close Proposition 10's cross-term gap or the general
   vertex-enumeration gap — those questions are about comparing across
   different $S$ (different Xiang Yu responses), not about arithmetic within
   one fixed, already-sorted $S$.

No repair is proposed: the failure in observation 2 is independent of the
exact form of the invariant tested, since it stems from the mechanical-sort
nature of the claiming stage (§1), not from a bad choice of scaling
constant or threshold.

## 3. Recommendation for future rounds

Do not re-attempt a "claiming order" or "defer commitment" invariant for
this problem. If the crux corpus's alt-framing idea is to be pursued
further, the more promising target (per the round-4 alt-framing explorer's
own #1-ranked candidate, `rank-pigeonhole-budget`, not attempted here) is
to look for pigeonhole/budget-style invariants over the *marking* stage
itself (Liu Bang's one-shot choice vs. Xiang Yu's one-shot best response),
where the real single round of adaptive information transfer actually
lives — not over the claiming stage, which is already a fully solved,
non-strategic sort.
