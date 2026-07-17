# Outline Review — imo-2026-03, Round 6

Field this round: **direct-constructive** (advance) + **upper-general-cascade** (copy-of direct-constructive).
Two new framings were pre-killed by the outliner at the gate (xor-covering-upper, extremal/compactness); I did not re-test — both are documented graveyard collapses (rename of the pair-creation wall / interior-valley) and correctly not put up.

---

## direct-constructive (advance) — APPROVE

The round-6 changes repair the exact defect the round-5 reviewer caught, and I verified the repair numerically and logically.

**LOWER bound — the dyadic Case-1/Case-2 split is sound and, crucially, robust to clustering.**
- Case 1 (max fragment w_1 ≤ 2^{n-2}): A ≥ v_1 − v_2 ≥ 2^{n-1} − 2^{n-2} = 2^{n-2} ≥ 1. The "first-gap" bound A ≥ v_1 − v_2 is valid (sorted-descending alternating sum; the tail (v_3−v_4)+(v_5−v_6)+… ≥ 0). Verified: 0 failures over 20k a=0 configs each for n=3,4,5; A ≥ 2^{n-2} held every time. **Both round-5 counterexamples land in Case 1** ({2,10/3,10/3,11/3,11/3} and {2,7/2,7/2,7/2,7/2}: max frag 3.67, 3.5 ≤ 4, giving A=5). This is the correct fix: the false universal receiver claim is *removed*, not patched.
- Case 2 (w_1 > 2^{n-2}): the max fragment has exactly one piece strictly above it (the intact 2^{n-1}), so G(w_1)=1 (receiver). Verified robust: 0 failures over the Case-2 configs (n=3,4,5) — `#{pieces > w_1} = 1` held at every clustered/tie-laden config. This is the key improvement over round 5: the receiver is now a *named specific* fragment whose parity is forced by piece-counting, not an existence claim that broke at ties.
- Descent trichotomy at a Case-2 minimiser: (a) positive donor b≠w_1 ⇒ A′=−2, contradiction; (b) no positive donor ⇒ smallest piece is intact 2^0=1 at odd rank 2n+1 ⇒ A = 1 + (nonneg alt-sum) ≥ 1; (c) only donor is w_1 (flat move). Branches (a),(b) are rigorous; (b)'s intact-1/odd-count mechanism is stated and checks out.

**Remaining gap (CHANGES-level, not fatal):** branch (c) flat-move **finite-termination** is still a loose end. The outliner correctly flags it and prescribes an explicit well-foundedness argument (each flat step strictly reduces #{tied pairs}; the cell complex is finite ⇒ a boundary face is reached, closing at g_i=0 or g_i=2^{n-1}). The builder MUST write this as a strict-decrease/well-foundedness proof, not "iterating reaches a boundary." Until it is written the lower bound is not `solved`.

**UPPER bound — IH(4) closure via two pure-conditional lemmas is certifiable.**
- IH(q)-reducible: state as a **pure conditional** ("one pair-cancel move drops to a valid IH(q−1) instance iff S − max(b_1,2b_2) < (2^{q−1}−1)/D"), with **no empirical percentage** in the statement. Round-5's rejection was solely the bundled ~94%; the trimmed conditional certifies. Confirm the builder strips it.
- IH4-flat: verified. The flat residual forces both S−b_1 ≥ 7/D and S−2b_2 ≥ 7/D (the `max` makes both bind), so b_2 < 4/D follows cleanly. The two sub-cases close by the gap condition: if b_2<b_3+b_4 then A=b_3+b_4−b_2 < b_4−1/D < 1/D (uses gap b_2>b_3+1/D and b_4<2/D); if b_2≥b_3+b_4 then b_3>b_4+1/D>2/D so b_3+b_4>3/D and b_2−b_3−b_4<1/D, pick δ small. Numerically: 0 failures over the flat-residual q=4 configs, worst A=0.59·(1/D) < 1/D. Sound.
- IH(4) = reducible (→IH(3), base proven) ∪ flat residual (IH4-flat) is a complete partition. Closure is honest.

**Verdict: APPROVE.** Build items for the builder: (1) write the branch-(c) flat-move well-foundedness argument explicitly; (2) re-propose IH(q)-reducible and IH4-flat as pure conditionals stripped of all empirical %; (3) state the split for n≥3 and cite §7 for n≤2 (the n=2 edge where 2^{n-2}=1 coincides with the smallest intact). Do NOT reinstate the universal "receiver always exists."

---

## upper-general-cascade (copy-of direct-constructive) — APPROVE (registered)

Sanctioned use of `copy_approach`: two viable ways to fill the same gap (general-n IH(q≥5) upper bound), both worth pursuing in parallel. It is a whole attempt (imports the lower bound + IH≤4 as closed, targets the actual problem claim), not a fragment-split. Its distinctive new content is genuine, not a rename:
- **IH+(m) strengthened dual-bound induction** — carries sum bound AND max<2^{m−1}/D together. The explorer showed the max-bound alone is FALSE (559/20000 fails) and the sum-bound alone stalls at the flat residual; carrying *both* is the new idea that shrinks two resources per level. This is a real strategic difference from direct-constructive's single-threshold IH(q) reduction, so it is legitimately a parallel branch on the shared wall rather than a graveyard rename.
- **B2 double-pair-cancel entry** — because the sum sits exactly on the IH(n+1) boundary, one cancellation cannot enter a strict IH instance; two pair-creations on the two largest pieces drop the sum strictly below IH(n−1). Mechanism stated.

**Open gaps (honest, the build target):** IH+(m) descent termination for all m (the depth/gap contradiction — verify intermediate singletons stay >1/D or get absorbed); B2 keeping all residual pieces >1/D within the ≤n cut budget. These are the genuine open core and are correctly labelled as gaps, not hidden behind "it follows."

**Verdict: APPROVE.** Constraints for the builder: NEVER drop the sum bound for the max bound alone (false); use adaptive fragment cascades, not a fixed Euclidean/4-cut residual (both fail ~50%); if the double-cancel entry stalls, report the exact sub-region rather than overclaim.

**Diversity note for the orchestrator:** the field is narrow — both live approaches attack the general upper bound with the *same move-set* (pair-creation cascades / Lemma H mechanism); they differ only in the inductive bookkeeping (single vs dual invariant). They share one wall. This is acceptable this round because direct-constructive's main new work is the LOWER bound + IH(4) while the copy owns the general upper — so they are not both stalled on the same step *this* round. But if the general IH(q≥5) upper bound has not moved by round 8, the two will have collapsed onto one wall and a genuinely different upper-bound framing (different move-set or target, outside the whole graveyard) must be commissioned. Flagging now.

---

## Cut / not registered
- caseB-matching (elo 1517, dead-end, Lemma M refuted) — stays dead, not a survivor.
- induction-recursion (elo 1368, dead-end engine) — stays dead.
- potential-duality (elo 1440, never built, vacuity risk) — parked, not built.
- amortized-parity, extremal-config — graveyard.

## Ranking (updated, stale cleared)
upper-general-cascade 1650.2 ≈ direct-constructive 1648.0 (twins, drawn) > caseB-matching 1517.2 > potential-duality 1439.9 > induction-recursion 1368.0.
Comparisons anchored: both live approaches beat all three non-live (dead-ends and parked vacuous); the twins drawn (copy inherits, unevaluated); caseB-matching > induction-recursion (salvaged certified lemmas); potential-duality > induction-recursion (refuted engine ranks lowest).

build set: direct-constructive, upper-general-cascade
