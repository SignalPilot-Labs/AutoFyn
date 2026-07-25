# Outline review — imo-2026-03, round 4

Field: 4 nominated approaches (3 LB advance/revise + 1 new UB). Refuted mechanism check first:
the round-3 "cut-count on C caps W" is REFUTED (explorer confirms the true n=3 extremal spends
ZERO cuts on C with W large). I checked each skeleton — **none relies on it**; all four explicitly
drop or route around it. Good.

Numeric sanity (this round): confirmed the β-reformulation is exact and tight — at the n=3 extremal
cascade B_min={4,4,2,2,1,1,1}, sum=15, S=1, β=(15−1)/2=7=2^n−1 attained. So both LB
reformulations (S(B_low)≥1−e ⟺ β(B_low)≤2^n−1) are algebraically sound and sharp.

---

## induction-peel — APPROVE (leader; strongest LB advance)
- Skeleton is valid end-to-end: L6 truncation → residual S(B_low)≥1−e for e<1 → S(Q_low)+S(C)−2W≥1−e
  via L3 XOR. Each step follows from a named certified lemma.
- **L9 self-pairing mini-lemma is rigorous and free** — N_Q(t) even ∀t<H ⟹ the W-integrand
  {N_Q odd ∧ N_C odd} is empty ⟹ W=0 ⟹ S(B_low)=S(Q_low)+S(C)≥S(C)≥1 by IH. Tautologically valid
  (W only counts t where N_Q is odd). Bank it as L9; it cleanly disposes of the h=0 boundary slice.
- The load-bearing gap — the **pointwise profile IH P\*(n)** replacing the scalar S(C)≥1 — is
  correctly identified as the honest missing content, with a stated mechanism (only the *shape*
  m_C(t) of C's odd-region controls alignment overlap; it inducts because R is a scaled P_{n−1}).
  This is a real gap, not hand-waving, and it is flagged as the builder's work. Approve to build.
- Issue to hold the builder to: step 4's "extremal +1 accounting" must be derived, not asserted —
  the surviving +1 = S(Q_low)−S(C) claim needs the exact identity written out, not "it follows."

## alternating-sum-potential — APPROVE (distinct mechanism: β-matching, verified tight)
- The reformulation is exact and I verified it numerically: S(B_low)=sum−2β (L4), sum=D_n−e, so
  S(B_low)≥1−e ⟺ β(B_low)≤2^n−1, e cancels cleanly. Sound.
- Genuinely different language from the W-overlap route (combinatorial matching on shard ranks vs
  measure overlap) — good diversity; does not die with induction-peel.
- Gap = the β≤2^n−1 combinatorial cap (step 3) — honest, flagged. The watch-out is correctly
  stated: β is a MAX over pairings, so the cap must hold for EVERY pairing (Hall-deficit / scale-
  bucket argument), not a single good one. Builder must not silently prove it for one pairing.

## averaging-upper-bound — APPROVE, registered (the plateau-breaking NEW UB framing)
- This is the ONLY approach attacking the never-closed upper-bound crux this round, on a framing
  far from both exhausted routes (branch-inequality DP, min-pairing/charging witness). Registered
  at 1500.
- The core lever min(X,Y)≤pX+(1−p)Y is trivially valid, and it genuinely sidesteps the F1
  "which branch wins / no closed form in (a_1,sum)" obstruction — it never decides the branch.
  Has a real crux-corpus analog (aimo-0198). Not a one-pass greedy rule (it mixes two analyzed
  global moves by an r-only weight), so it escapes the KNOWN-FALSE one-pass ban — I confirm this
  distinction holds.
- **Honest risk to flag (not a gate-out): the averaged bound is strictly weaker than the min.** The
  builder MUST use the exact MATCH/BISECT S-effect formulas (certified, induction-peel §4) plus a
  profile-sensitive IH — the scalar sum-IH s/D_{k−1} on both branches is provably too weak
  (average of two things ≤ s/D_{k−1} is still > s/D_k). The make-or-break is whether an r-ONLY
  weight p(r) exists that makes the two-term average telescope to s/D_k; if p must depend on more
  than r=a_1/ρ the approach stalls. This is the crux and it is honestly labelled as such. Because
  the min≤average step is valid and the framing is the designated plateau-breaker, it is APPROVED
  to build — but the builder should first (≤30s numeric probe, incremental print) check whether a
  fixed p(r) can hold the average ≤ target on the exact formulas at n=2,3 before investing, to
  fail fast if no r-only weight exists.

## global-max-peel — CHANGES REQUESTED (live, not in build set this round)
- The amortized frontier-potential sweep (aimo-0019 style) is a legitimately different LB framing
  and correctly avoids re-importing the static W-overlap wall. But it is the least-specified of the
  four: the credit function λ(t)/floor(t) and the per-crossing charge bound (step 3) are entirely
  open, and there is real danger the sweep silently reduces to the same superincreasing-gap
  inequality (the wall) one step later. Its own residual is the shared crux and its new mechanism
  is as speculative as averaging but attacks the already-well-covered LB gap rather than the
  untouched UB gap. Keep it live (it fails independently), but it is out of this round's build set —
  build capacity is better spent on the two developed LB mechanisms + the new UB attack.
- If built later: the builder must read aimo-0019 in full and write λ(t) explicitly before charging.

## explicit-certificate — no change (dormant; not nominated)
- Never built; its "concentrate cuts on a_1" core is KNOWN-FALSE. Sank in the ranking. Leave dormant.

---

## Diversity / plateau note for the orchestrator
The three LB mechanisms are genuinely distinct (profile-IH alignment bound / β-matching Hall-deficit
/ frontier sweep) — the single-gap trap is avoided on the LB side. The UB wall is now attacked for
the first time in 3 rounds by averaging-upper-bound. Explorer finding worth carrying: the LB extremal
witness = the UB dyadic cascade B_min exactly (verified), so a proof characterizing "S(B)≥1 with
equality iff B is cascade-type" could close BOTH walls at once — flag for a future round if the two
walls persist. No copy/branch requested this round.

## Ranking (Elo after this round)
induction-peel 1657 · alternating-sum-potential 1568 · averaging-upper-bound 1505 (new) ·
global-max-peel 1473 · explicit-certificate 1394. Stale flags cleared.

build set: induction-peel, alternating-sum-potential, averaging-upper-bound
