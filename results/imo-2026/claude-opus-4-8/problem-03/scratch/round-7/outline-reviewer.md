# Outline Review — imo-2026-03 (Round 7)

Three approaches proposed, all **advances** (already registered — no new slug, no copy). The outliner opened
no new approach; I confirm that is correct: the shared lower-bound crux G-INC-1 = GAP-A **moved materially
this round** (SET IDENTITY two-step induction closes Cases 1/2a/2b-i; double-REFL closes Cases A/B1), so it is
NOT a 3+-round-unchanged plateau and the anti-plateau bypass rule does not fire. Concentrating builder effort
on converting the fresh machinery to rigor is the right call.

Pre-build numeric verification (tiny, bounded, joint cut budget respected where relevant):
- **A(G_m) odd ≥ 1**: 1,1,3,5,11,21,43 for m=0..6 — confirmed (explorer convention G_m={2^0..2^m}).
- **SET IDENTITY** S_{G_{n-1}} ∩ [0,2^{n-2}) = S_{G_{n-3}}: N_{G_{n-1}}−N_{G_{n-3}} ≡ 2 on the band, 0
  parity mismatches, n=3..7. CONFIRMED. (My first run mismatched only from an index-convention slip; corrected.)
- **Double-REFL formula** A(Q∪G_{n-1}) = 2^{n-1} − q₁ + A(Q'∪G_{n-2}) for q₁∈(2^{n-2},2^{n-1}): 0 mismatches / 3031 tests.
- **Case A** (q₁≤2^{n-2} ⇒ A(Q∪G_{n-2})≤2^{n-2}): 0 violations / 584.
- **Case A.A identity** 2τ−1 = 1/D_b for Σ=1: exact, b=1..5. So A=2p₁−1 < 1/D_b strictly for p₁<τ.

---

## ll-inclusion-gap — APPROVE (advance)

Verdict: **APPROVE.** The two-step strong induction n→n−2 is sound. Vetting of the flagged points:
- SET IDENTITY (step 2) verified — the mechanism (N-difference exactly 2 ⇒ parity preserved) is exactly right.
- Strengthened IH **Claim(n,ε) cycles cleanly**: sub-case 2b-i feeds ε' = a−b, and a−b ≥ 0 (a≥b) and
  a−b ≤ a < 1 (deficit_top = a+b < 1 in Case 2b), so ε'∈[0,1) — never negative. The ε<0 case is FALSE and the
  induction correctly never touches it. Budget matches exactly (|Q_lo| ≤ n−1 = (n−2)+1), and S_{Q_lo} ⊆ S_{G_{n-3}}
  is delivered by the SET IDENTITY, so Claim(n−2,ε') is legitimately applicable.
- Residual **sub-case 2b-ii (a<b)** is correctly isolated. It is a genuine open gap, but with a stated
  mechanism (recurse top-band decomposition on Q_lo, telescoping onto A(G_base)≥1).

Issues the builder must respect (CHANGES-REQUESTED-grade caveats, not blockers):
1. **2b-ii general n is NOT closed** — only n=4 (2-part Q_lo, via sup(S_{G_1})=2 ⇒ p₁≤2). Do not present the
   telescoping recursion as done; formalize the part-bound argument sup(S_{G_{n-3}})=2^{n-3} for multi-level Q_lo.
2. **G-INC-2 (refined R, general n) is a separate open residual** — the INC branch is proven only for R=G_{n-1}.
   Vacuous at n=3 (budget+parity kills all instances); first nontrivial at n=4 (|Q|=3, c_R=1). Do not overclaim.
3. Bound A(Q) by **arithmetic on part values only** — do NOT reinstate the decertified Structural Lemma; the
   INC-parity shortcut (A(Q)≤(q₁−q₂)+q₃<3) is the n=3 special case only, not a general proof. Even-multiplicity
   interior pairs {s,s} are admissible (Parity-Condition) and must be handled.

## ll-dyadic-symdiff — APPROVE (advance)

Verdict: **APPROVE.** Double-REFL telescoping is a correct double application of certified Lemma REFL (formula
verified, 0 mismatches). Case A (A(P)≤max P) and Case B1 (A≥0 ⇒ A ≥ 2^{n-1}−q₁ ≥ 1) are rigorous and complete.

Issues / caveats for the builder:
1. **B2 (q₁∈(2^{n-1}−1,2^{n-1})) is the only open piece for general n**, correctly isolated. But its stated
   mechanism — "Q'∪G_{n-2} is itself a valid B-type problem one level down, so A(Q'∪G_{n-2})≥1 by the same REFL
   chain" — is the **hand-waviest step in the field**. It is proven analytically only at n=3 (3-piece; 4-piece
   numeric). Caution: after REFL, max(Q'∪G_{n-2}) = max(q₂, 2^{n-2}), and q₂ can EXCEED 2^{n-2}, so the residual
   is not cleanly a level-down B-type instance in general — the naive "recurse" does not obviously terminate.
   The builder must either make the descent rigorous (handle q₂>2^{n-2}) or bound A(Q'∪G_{n-2}) > q₁−(2^{n-1}−1)
   ∈(0,1) directly; ≥1 is stronger than needed but is not yet established for n≥4.
2. Do NOT revive "max(Q)<2^{n-1} ⇒ A≥2" (FALSE; Sub-3b B3 min is 3/2). The tight A=1 witness Q={3,3,2},R={2,2,2,1}
   is **Sub-3a** (I_0 fully odd), not GAP-B — do not chase a phantom tight-at-1 case in Sub-3b.
3. GAP-A general n is the shared crux with ll-inclusion-gap — import whichever route closes it; do not re-prove
   it as a fresh sub-lemma inside this slug (keep the slug a whole attempt).

## geometric-selfsimilar — APPROVE (advance, leader)

Verdict: **APPROVE.** Owns the full upper bound, reduced to one residual gap case. Case A.A is a clean cheap kill
(identity A=2p₁−1, and 2τ−1=1/D_b exact ⇒ A<1/D_b STRICT for p₁<τ) — verified; **build this first**.

Issues / caveats:
1. **The gap-step-then-R3 two-level argument (p₁≤p₂+p₃) is the last and hardest residual.** Its mechanism
   ("gap-step shrinks Σ so the unchanged p₃ crosses the new R3 threshold τ'/2") is supported by only 25/28 cases
   (3 need two gap-steps). The R3-firing condition p₃ ≥ τ'/2 must be proved algebraically, and the adaptive choice
   of pairing j must be specified (fixed pair-at-p₂ fails 44/222, pair-at-smallest 95/222). Termination is claimed
   by descent in b — make that explicit.
2. Do NOT attempt to preserve the SB invariant step-by-step — PROVED FALSE (Σ'/D_{b−1}≤Σ/D_b fails 18/123/315/678).
   The descent is in b, not in SB; partial-shadow must not be reused here.

---

## Ranking (updated, all stale flags cleared)

All three built slugs advanced materially this round; the two unbuilt slugs are dead-ended/stuck and rank below.
Head-to-head anchored to evidence (SET IDENTITY + double-REFL + Case A.A all advancing; alternating-sum-value's
greedy route is a recorded dead-end; extremal-smoothing S1 stuck 4+ rounds with no mechanism).

Post-update Elo:
1. geometric-selfsimilar 1667.2 (leader — whole upper bound to one gap case, Case A.A cheap kill)
2. ll-inclusion-gap 1567.5 (cleanest LB progress — two-step induction closes 3 of 4 sub-cases with clean IH cycling)
3. ll-dyadic-symdiff 1511.3 (Cases A/B1 rigorous; B2 general-n descent hand-wavier)
4. alternating-sum-value 1426.8 (greedy dead-end; shares LL crux that is moving elsewhere)
5. extremal-smoothing 1327.2 (S1 stuck 4+ rounds, no mechanism)

No registration or copy needed: all three build slugs already exist; the outliner requested no branch (import,
not copy, for the shared GAP-A). Confirmed.

build set: ll-inclusion-gap, ll-dyadic-symdiff, geometric-selfsimilar
