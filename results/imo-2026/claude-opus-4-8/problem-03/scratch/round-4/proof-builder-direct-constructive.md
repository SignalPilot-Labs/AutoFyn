# Proof-builder report — round 4 — imo-2026-03 — slug: direct-constructive

Status: **partial** (unchanged flip; substantial structural progress, no full solve).

## What I did this round

Priority 1 (lower bound L1+L2) and priority 2 (U1 Case B), per the build set.

### Lower bound — reduced to ONE inequality, closed two sub-cases
1. **§4.1 generalised to all placements.** "XY spares R_n ⟹ O ≥ 2^n" now holds for EVERY cut
   placement (not just confined): R_n = 2^n is the unique max ⟹ r_1 = 2^n ⟹ O ≥ r_1. The whole
   lower bound splits on the single dichotomy "does XY cut R_n?". Fully rigorous. Promotable.
2. **§4.2.6 Route A as a minimisation (REDUCTION PROVED).** Padding to n+1 fragments, A = μ{N odd}
   is continuous and piecewise-affine on the compact simplex Δ = {Σ g_i = 2^n, g_i ≥ 0}; its min is
   attained at a **vertex** of the cell complex. So the confined lower bound A ≥ 1 is EQUIVALENT to
   the vertex inequality **(★) A(vertex) ≥ 1**. Closed within (★): the interleaving cell (A ≡ 1,
   constant) and ALL case-a=1 vertices (via the certified top-fragment cascade). Residual: a=0
   *clustered* vertices only. The ≤ n+1 count is built into Δ and is load-bearing (I machine-checked
   min A drops to ≈0.01/0.10/0.28 at n=2/3/4 with n+3 fragments; = 1 exactly with n+1).
3. **§4.4 L2 collapses into (★).** Unreachable-interleaving (fragment-count bound + Lemma S) shows a
   stray cut outside R_n cannot even tie A = 1; the full A ≥ 1 for stray-cut configs is the same
   vertex inequality (★). **L1 and L2 are now a single gap**, a genuine simplification over round 3.

Net: the lower bound is now "prove (★) at a=0 clustered vertices," with everything else closed.
I did NOT close (★) — the global-vs-local minimum for clustered a=0 vertices remains open. Honest.

### Upper bound Case B (B1-large) — base cases proven
4. **§6.2 IH(1), IH(2), IH(3) proved rigorously.** B1-large reduces (halve a_1, pair cancels) to
   IH(q): q pieces > 1/D, sum < (2^q−1)/D ⟹ XY forces A ≤ 1/D with ≤ q−1 cuts. Proved q=1,2,3 with
   exhaustive disjoint gap-casework; the "doubly-hard" leaf uses the sum bound to get residual
   singleton < 1/D. Verified IH(2) numerically (0 violations). General IH(q≥4) step honestly OPEN.

## Gaps remaining (honestly flagged, Status stays partial)
- **(★)** — A ≥ 1 at a=0 clustered vertices of Δ. Sole remaining lower-bound inequality (subsumes
  old L1+L2). Numerically min_Δ A = 1 (n≤5) but no config-independent certificate yet.
- **U1 = Case B** — general-n IH(q≥4) pair-creation step (B1-large), and B2 entirely.

## Promotable lemmas (for reviewer to certify)
- **Spare-R_n lemma** (§4.1): any placement sparing R_n ⟹ O ≥ c(n). Fully proved.
- **Δ-reduction** (§4.2.6): lower bound ⟺ vertex inequality (★); interleaving cell + a=1 vertices
  closed; count is load-bearing. Fully proved as a reduction.
- **IH pair-creation leaves q≤3** (§6.2): fully proved base of B1-large induction.

## Spec concerns
None. Answer c(n) = 2^n/(2^{n+1}−1) stands; small-n verification intact.

## Assessment for orchestrator
Real progress: L1/L2 merged into one crisp vertex inequality with two sub-cases closed, and Case B
base cases rigorous. But the field-wide walls persist: (★) a=0 clustered vertices (lower) and the
general IH induction (Case B upper). Both are "global minimum / general induction" difficulties that
resisted a clean one-shot this round. Recommend: next round put a builder specifically on proving
(★) at clustered a=0 vertices (it is now a finite, concrete inequality — a per-cell LP lower bound
or a vertex enumeration by the fragment-count bound may crack it), and keep caseB-matching pushing
the induction-free Case B route.
