# Build report — self-similar-recursion — round 6 — imo-2026-03

## Status: partial (honest; no overclaim)

Spine §0–§5 unchanged and sound (all certified: S-core `ker U=0`, M2/M3/M4, block formula). The
conditional integrality closure (§5) still gives `f(P*)≥1` GIVEN Gap A (forest) + Gap B (no μ=3
even-leaf). I advanced Gap A and left Gap B open. Answer pinned `c(n)=2^n/D_n`.

## What I PROVED this round (new, rigorous)

**Lemma CC (isolated-cycle exclusion).** The piece–component incidence multigraph `H` at the Φ-max
minimizer has NO isolated cycle — no connected component that is a bare 2-regular cycle through
distinct pieces `2^{a_1},…,2^{a_r}` and distinct components `Q_1,…,Q_r`, all edges multiplicity 1.
- Even `r`: alternating `±1` on the cycle components is a nonzero `ker U` vector (the components have
  degree 2, so `Ud=0` on every piece), contradicting Lemma S-core. `r=2` is directly inconsistent
  (`u_1+u_2=2^{a_1}=2^{a_2}`, impossible).
- Odd `r`: the cyclic system `u_{i-1}+u_i=2^{a_i}` is nonsingular (det = 2), unique solution
  `u_j=½Σ_t(-1)^t 2^{a_{j+1+t}}`. Choose the start so the largest budget `2^{a_max}` carries a minus
  sign (possible since offsets cover all residues mod r, r≥3); then `2u_j ≤ -2^{a_max}+Σ_{ℓ≠M}2^{a_ℓ}
  < 0` by the **superincreasing** bound `Σ_{a<a_max}2^a < 2^{a_max}`. So `u_j<0`, contradicting
  positivity.

This uses the numerical powers-of-two budgets essentially — exactly the geometric/distinct-powers
input the integrality explorer proved is NECESSARY (his 479-instance family refutes any pure
kernel/multiplicity closure; those examples are all NON-isolated, so Lemma CC is untouched by it).
Numerically verified: 0 feasible isolated odd cycles of 47376 (r=3,5,7, exponents ≤7); even cyclic
incidence matrices singular.

## What REMAINS open (sharpened residuals)

- **Gap A′ (non-isolated cycles).** Lemma CC narrows Gap A from "any cycle" to cycles with a chord,
  an off-cycle attachment (a cycle piece of degree ≥3 — the "private extra mass" of the 479 family),
  or a multiplicity-≥2 edge. There the cycle equations relax to inequalities `u_{i-1}+u_i ≤ 2^{a_i}`
  and the alternating telescoping no longer forces a sign contradiction (off-cycle surplus terms
  enter with uncontrolled signs). I attempted the outline's full-cycle telescoping and could not
  close it — this is where the geometric rank-contiguity must convert into an inequality; I did not
  achieve that. STILL OPEN.
- **Gap B (μ=3 even-block piece-leaf).** No local move excludes it (M3 is a V-kink on the even block,
  M2 needs 4 copies). I confirmed the two obvious global one-liners FAIL: (i) bisect-instead changes
  `f` (parity flip on `[0,v)` via layer-cake); (ii) symmetric-to-degenerate gives `f(P')≥m`, the
  wrong direction. The genuine route is a degenerate competitor `P'∈G` with `f(P')=m` exactly (then
  Claim(N−1) closes it, no Φ needed), i.e. the outline's Lemma BD — NOT constructed this round.
  STILL OPEN. NOTE: the outline's `{2,3,3}` numeric illustration is WRONG (`f({2,3,3})=2`, and it is
  a matched-pair refinement of one `2^3`, not a μ=3 even-leaf); I discarded it — no proof depends on
  it. The reviewer should not trust that illustration.

## Lemmas proposed for certification

- **isolated-cycle-exclusion** (Lemma CC above) — fully proven in §6, numerically verified. Reusable
  by the block-recursion route (its UPM-5 residual is the same non-isolated-cycle wall; Lemma CC
  disposes of the isolated/pure sub-case there too).

## Spec / correctness concerns for the reviewer

- Please check the odd-`r` indexing in Lemma CC (the wrap-around producing coefficient ±2 on a single
  `u_j`, and the claim that offsets `t≡M-(j+1) mod r` cover an odd residue for r≥3). I verified the
  identity `(ODD)` and the negativity numerically over all r∈{3,5,7} and exponents ≤7 (0 feasible of
  47376), but the general-`r` write-up is by re-indexing, not brute force — worth a close read.
- Lemma CC does NOT close Gap A; do not read it as a forest proof. It excludes only isolated cycles.
- No refuted object reintroduced (no Lemma W/S/T, no V-kink 3-shift, no pure-algebra Gap-A closure,
  no consecutive-ones/TU).

## Net
Genuine incremental advance on the shared wall using the mandated distinct-powers mechanism (Lemma
CC), honestly scoped. Gap A′ and Gap B remain the two open steps. Recommend: CHANGES REQUESTED
(partial, real progress), certify Lemma CC.
