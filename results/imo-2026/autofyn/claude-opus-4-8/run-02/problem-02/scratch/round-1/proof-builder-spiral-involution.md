# Proof-builder report — spiral-involution (imo-2026-02), round 1

## Bottom line
Status: **partial**. Spec concern: **RETHINK the engine** (GAP-1 refuted as false).

## What I PROVED (rigorous, in the approach file)
- **Reduction:** `OM=ON ⟺ O∈perp-bisector(MN) ⟺ pow_M(⊙AKL)=pow_N(⊙AKL)` (A∈⊙AKL).
- **L1 (σ-invariance), full proof.** `σ:(A↦A,B↔C,M↔N,K↔L)` fixes condition 1 and the
  region hypotheses, swaps conditions 2↔3, and fixes the conclusion. Correct, but only
  an organizing relabelling — NOT an isometry, proves nothing alone.
- **L2 (supplementary relation), full proof.** `∠LBA+∠NLC=π` and σ-image `∠KCA+∠MKB=π`.
  Derivation: ray BK between BA,BL ⇒ ∠LBA=∠KBA+∠LBK = ∠ACL+∠LNC (cond 1,2); ∠LCN=∠ACL
  (N on AC); angle-sum in △LNC ⇒ ∠LBA=π−∠NLC. Numerically = 180.0000° on 3 triangles ×
  3 θ. Both L1, L2 are **promotable**.

## GAP-1 — did it close? NO. It is FALSE.
The approach's engine required upgrading condition 3 to a spiral similarity `S_K`
(L↦B, C↦M), i.e. `△KLC ~ △KBM`. On the exact configuration (all 3 conditions satisfied
to 1e-10, OM−ON≈8e-11) the angle multisets are `{0.245,2.581,0.315}` vs
`{2.526,0.300,0.315}` — only the one GIVEN angle matches; side ratios KL/KB=2.30 vs
KC/KM=4.13. Not similar under any correspondence. `S_L` fails identically.
Decisive: an exhaustive search over ALL triangle pairs on {A,B,C,M,N,K,L}, forced across
two θ, yields ONLY the trivial midpoint similarities (△ABC~△AMN). There is no hidden
similarity for a spiral engine. L2 cannot supply the missing second angle because none
exists. **The spiral-similarity framing is a genuine dead end.**

## Remaining gap
The real target `pow_M=pow_N` (verified = −1.7312 via both secants AB, AC) has NO
synthetic mechanism in this approach once the spirals are gone.

## Spec concerns → RETHINK
Route this slug back to the outliner for a NEW engine. Keep L1, L2 (both proved, both
promotable — certify into results/imo-2026-02/lemmas/). Discard "conditions 2,3 are
base-angles of spirals at K,L." L2 is a *supplementary/cyclic-type* relation, so a
correct engine is more likely directed-angle concyclicity or isogonal/trig-Ceva feeding
`pow_M=pow_N`, combined with L1 to halve the work — a framing genuinely distinct from
the (dead) spiral route and from the other live slugs.

## Note for the field
The trig-metric-identity slug is unaffected (independent engine). L1+L2 may shorten
equal-power-secants and any future synthetic approach.
