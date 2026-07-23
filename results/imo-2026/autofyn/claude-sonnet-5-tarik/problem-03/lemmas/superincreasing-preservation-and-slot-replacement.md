# Superincreasing Preservation Lemma and Slot-Replacement Corollary

**Certified by:** proof-reviewer, round 9, from approach `concavity-minimax-duality` (round-9
builder, §15.2). Independently re-derived by the reviewer (the induction and its key sub-claim
re-traced from scratch) and re-verified computationally with fresh code, independent of the
builder's own harness:
- Superincreasing Preservation: BFS over D/M-reachable states from 60 freshly-generated random
  strictly-superincreasing bases (sizes 1–6, non-power-of-2 gaps), depth up to 4 operations,
  8527 total states examined, 0 violations.
- Slot-Replacement Corollary: 3000 random `(superincreasing sequence, a, b)` trials, exact integer
  arithmetic, comparing the predicted in-place sorted list against a from-scratch re-sort — 0
  mismatches.
- Both independently reproduce the builder's own reported figures without reusing the builder's
  code.

**Depends on:** the definition `e(M) := Σ_i (-1)^{i+1} m_i` for a sorted descending multiset `M`;
the D/M-operation reformulation (`lemmas/dm-operation-reformulation.md`); Step 3 of the
already-certified `lemmas/superincreasing-no-early-zero.md` (simultaneously-active values in a
legal D/M sequence starting from a strictly superincreasing base are pairwise distinct, hence any
`M(x,y)` operation has a well-defined strict sorted-order pair `x=v_a>y=v_b`, `a<b`).

## Statement

**Superincreasing Preservation Lemma.** Let `a_1>a_2>\dots>a_k>0` be any strictly superincreasing
sequence (`a_i>a_{i+1}+\dots+a_k` for every `i<k`). Then every state reachable from
`\{a_1,\dots,a_k\}` by any legal sequence of `D`/`M` operations (of any length, not merely `<k`)
is again strictly superincreasing when sorted descending. (General base — not tied to `D_m` or
powers of `2`.)

**Slot-Replacement Corollary.** Under the same hypotheses, if a legal `M`-operation `M(x,y)`
(`x\ge y>0`) acts on the active state `v_1>\dots>v_r$ with `x=v_a`, `y=v_b`, `a<b`, and inserts
`w:=x-y`, then the new sorted list is *exactly*
```
v_1,\dots,v_{a-1},\ w,\ v_{a+1},\dots,v_{b-1},\ v_{b+1},\dots,v_r
```
— `w` takes over `v_a`'s exact sorted slot, `v_b`'s slot is simply deleted, and no other
re-sorting occurs. (This corollary's proof needs only the Key Sub-claim below, not
superincreasing-ness of the *whole* state beyond what is used to establish that sub-claim.)

## Proof

Induction on the number of operations.

**Base case.** The original sequence is superincreasing by hypothesis.

**`D`-step** (delete one active element `v_j`, sorted position `j`): for `i<j`, the new tail sum
(`\sum_{\ell>i,\ell\ne j}v_\ell`) is the old tail sum minus `v_j\le` the old tail sum, so
`v_i>` old tail `\ge` new tail still holds; for `i>j`, the tail is untouched, holds by IH.

**`M`-step** (the substantive case). Let the active state before the operation be `v_1>\dots>v_r`
(IH: superincreasing), operation `M(x,y)`, `x\ge y>0`, `x=v_a`, `y=v_b`, `a<b` (WLOG, since
`x\ge y` and the sequence is sorted descending; `x\ne y` by the already-certified distinctness
fact cited above). Let `w:=x-y=v_a-v_b`.

*Key Sub-claim.* `w > v_c` for every surviving index `c\ne a,b` with `c>a`. *Proof:* by the
superincreasing hypothesis at index `a`, `v_a>v_{a+1}+\dots+v_r`, a sum including `v_b` (since
`b>a`) and every other surviving `v_c$ (`c>a,c\ne b`) as distinct, disjoint, positive terms; hence
`v_a>v_c+v_b+(\text{other nonnegative terms})\ge v_c+v_b`, i.e. `w=v_a-v_b>v_c`, simultaneously
for every such `c`.

*Consequence (Slot-Replacement).* The new sorted list is exactly
`v_1,\dots,v_{a-1},w,v_{a+1},\dots,v_{b-1},v_{b+1},\dots,v_r`: `w` is bigger than everything from
`v_{a+1}` on (excluding `v_b`, by the sub-claim) and smaller than `v_a` itself (`w=v_a-v_b<v_a`
since `v_b>0`), hence smaller than `v_1,\dots,v_{a-1}`.

*Verifying superincreasing at each new position, using this exact slot structure:*
- Positions `1,\dots,a-1` (before `w`): new tail from position `i<a` is
  `(\text{old tail})-v_a-v_b+w=(\text{old tail})-2v_b\le\text{old tail}`; since `v_i>` old tail
  (IH), `v_i>` new tail too.
- Position of `w` (slot `a`): new tail after `w` is `(v_{a+1}+\dots+v_r)-v_b`. Need
  `w>(v_{a+1}+\dots+v_r)-v_b`, i.e. `v_a>v_{a+1}+\dots+v_r` — exactly the IH at position `a`.
- Positions `a+1,\dots,b-1` (between): new tail after `v_c` is
  `(\text{old tail from }c)-v_b<\text{old tail from }c<v_c` (IH), only subtracting a positive
  quantity from an already-dominated sum.
- Positions `b+1,\dots,r` (after `v_b`'s old slot): tail entirely unaffected, IH applies verbatim.

All surviving positions fall in exactly one of these four classes, completing the inductive
step. `\blacksquare`

## Verification

Independently re-verified by the proof-reviewer, round 9 (fresh code, not reusing the builder's
harness):
- Superincreasing Preservation: 60 randomly-generated strictly superincreasing bases (sizes 1–6,
  arbitrary integer gaps, not restricted to powers of 2), full BFS of D/M-reachable states up to
  4 operations deep, 8527 states examined in total, 0 violations of the superincreasing property.
- Slot-Replacement: 3000 random `(sequence, a, b)` trials (superincreasing sequences of size
  2–7), predicted in-place sorted list compared against an independent full re-sort of the actual
  resulting multiset — 0 mismatches.

## Reusable by

Any approach reasoning about the sorted structure of `D`/`M`-reachable states from a
superincreasing base — in particular, the D_m-specific Value-Order = Dominant-Index-Order Lemma
(`lemmas/value-order-dominant-index-order.md`) and the (still open) Local Claim reduction of the
Distinct-Bucket Lemma both build on the Slot-Replacement Corollary directly.
