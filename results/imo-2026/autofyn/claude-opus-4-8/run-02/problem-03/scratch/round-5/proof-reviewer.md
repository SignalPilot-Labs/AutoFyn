# Proof-reviewer report — round 5, imo-2026-03 (IMO 2026 P3)

Two approaches built; both self-reported `partial`. I independently re-derived every new sub-lemma
and numerically re-verified the load-bearing steps. **Both are HONESTLY partial — no overclaim, no
re-introduction of the refuted round-4 Lemmas W/S/T.** One verdict per slug below.

Answer `c(n)=2^n/D_n`, `D_n=2^{n+1}−1`, remains pinned; upper bound certified and correctly imported
by both slugs (neither re-proves it — checked). The sole open gap of the whole problem (f≥1 at the
tied non-degenerate minimizer) remains open, but is now sharpened.

---

## Approach 1: self-similar-recursion — VERDICT: CHANGES REQUESTED (Status: partial)

### Scores
- Correctness: 9/10 — every claimed-proved step is sound; the two remaining gaps are honestly flagged.
- Completeness/rigor: 6/10 — Steps 0–4 complete and rigorous; Step 5 (integrality ⇒ f≥1) is valid
  but CONDITIONAL on the two open gaps A, B.
- Progress: high — discards the false Lemma W and rebuilds on 5 sound moves, sharpening the residual
  to two crisp, checkable graph facts.

### What I verified independently
- **Lemma S-core (`ker U=0`).** Re-derived. Feasible sum-preserving shift `w_j(δ)=w_j+δd_j` for
  `Ud=0`; affine `f` ⇒ minimality kills slope≠0, strict convexity of `Φ` kills slope=0. Sound.
- **Move M2 (`μ_{k,j}≤3`).** `{v,v,v,v}→{v+t,v+t,v−t,v−t}`: two matched pairs before and after, so
  P1-invisible ⇒ f exactly unchanged, `Φ` gains `4t²`. Verified 0/30000. Parity-independent — kills
  ALL μ≥4, so the round-4 "μ even ⇒ power of 2" error is genuinely bypassed. Sound.
- **Move M3 (odd-block, μ_{k,j}≤1).** `Δf = s(σ_{a_j}−σ_{a_j+μ_j−1})`; for odd μ_j the ranks differ
  by even μ_j−1 so signs coincide ⇒ Δf=0, `Φ` gains `2s²`. I re-derived the sign identity from
  scratch and verified 0 failures over valid samples (the many "failures" in my first sweep were
  the invalid μ=1 case, which is NOT the move's hypothesis — it requires a piece contributing ≥2
  copies). Sound; correctly identifies EVEN blocks as the V-kink residual.
- **Move M4 (no piece has two odd-block sub-pieces).** Within-piece transfer is affine for odd
  blocks (top=bottom sign); slope≠0 ⇒ descent, slope=0 ⇒ `dΦ/dδ=2(u−w)>0`. Verified affine
  (no kink) 0/50000. Sound; this is what drives the non-integer continuum `piece2={a,2−a}` to the
  degenerate boundary — consistent with the round-4 refutation, not in conflict.
- **Block formula BF** `f=Σ_{μ_j odd}σ_{a_j}w_j`. Verified 0/20000. Sound.

### The two open gaps — confirmed honestly open
- **Gap A (acyclicity of the incidence multigraph).** `ker U=0` does NOT force a forest for a
  multigraph — `[[1,2],[2,1]]` has trivial kernel yet is a double-edge 2-cycle. Genuinely open. It
  is the SAME wall as block-recursion's chorded-even-cycle UPM-5 (the builder's own "shared wall"
  observation is correct — the two integrality routes are NOT independent).
- **Gap B (μ=3 even-block piece-leaf).** `{v,v,v}`, `v=2^k/3`, `v` shared. No local move reaches it
  (M2 needs 4 copies; M3 gives only a stable V-kink on even blocks). Needs a global
  degenerate-domination lemma. Genuinely open.

Step 5's peeling argument (integrality GIVEN A+B ⇒ f≥1 via Theorem F) is valid but conditional; not
certified (rests on open gaps). No promotable lemma depends on A or B.

### Gap / what's missing
Close **Gap A** (multiplicity-aware cycle exclusion for the Φ-max multigraph) and **Gap B** (exclude
the μ=3 even-block piece-leaf, likely via a global degenerate-domination lever). Both are narrow and
checkable but neither is local. This is the sole residual of the problem.

---

## Approach 2: cut-budget-jacobsthal-recursion — VERDICT: CHANGES REQUESTED (Status: partial)

### Scores
- Correctness: 9/10 — all six proved lemmas are sound; the negative finding is correct.
- Completeness/rigor: 5/10 — proves top-uncut and all-bisection cases (both already covered by
  certified results) and refutes its own novel driver; the actual residual (LBL-B) is untouched.
- Progress: modest — genuine diversity value and a clean reusable identity, but no advance toward
  the residual; the headline mechanism died.

### What I verified independently
- **Lemma 2.1 (Jacobsthal).** `f(W_m)=(2^{m+1}+(−1)^m)/3` = 1,1,3,5,11,21,43. Correct.
- **Lemma 3.1 (two-band single-cut identity).** Re-derived `c'−c = 1[V_1>t]+1[V_2>t]−1[V>t]` = +1 on
  `[0,m)`, −1 on `[V−m,V)`; parity flips on those two bands only; `|Δf|≤2m`. Sound.
- **Lemma 4.1 (tightness cascade).** Top-bisection reduces visible `W_{n−k}→W_{n−k−1}`, reaching
  f(W_0)=1 in n cuts. Sound (gives min_XY f ≤ 1).
- **Lemma 5.1 (uncut survivor).** Pigeonhole `Σr_i ≤ 2n+1` over n+1 pieces. Sound.
- **Lemma 6.1 (top-uncut floor).** `2^n` unique max ⇒ f=2^n−f(R), f(R)≤2^{n−1} ⇒ f≥2^{n−1}. Sound
  (= certified round-1 Case A / top-band-decoupling).
- **Lemma 6.2 (all-bisection).** Sound (subsumed by certified integer-parity-alt-sum).
- **Refutation of the proposed driver — CONFIRMED CORRECT.** I verified the instance
  `Q'={16,4,3.567,2.115,2,1.885,1,0.433}`: sum=31 (reachable from W_4 in 3 cuts: groups
  8={3.567+2.115+1.885+0.433}, 16,4,2,1 intact), f(Q')=14.134; the best single further cut
  (bisect 16→8,8) gives f=1.866, a drop of 12.27, while the Jacobsthal decrement D_4=0. So
  "single-cut drop ≤ Jacobsthal decrement" is FALSE. The negative finding is legitimate and the
  reduction to (LBL-B) is sound.

### Gap / what's missing
The novel budget-induction DRIVER is dead (correctly refuted by the builder). The gap reduces
exactly to the classical **(LBL-B)** / Case B crux (top piece `2^n` is cut). To survive, the IH must
be strengthened to a profile/majorization monovariant on the count function `c(t)` (not scalar f),
or the top-cut case attacked structurally. Kept live as the non-integrality diversity hedge.

---

## Certified this round (6 new lemmas, total 16)
All unconditional (do NOT rest on any open gap):
- `phimax-trivial-kernel.md` (Lemma S-core) — self-similar
- `two-invisible-pairs-mult-bound.md` (M2) — self-similar
- `symmetric-odd-block-move.md` (M3, with the μ≥2 hypothesis made explicit) — self-similar
- `odd-block-formula.md` (BF) — self-similar
- `two-band-single-cut-identity.md` (Lemma 3.1) — cut-budget
- `uncut-survivor.md` (Lemma 5.1) — cut-budget

Move M4 is sound but was not proposed as promotable; not certified as a standalone lemma this round.
Lemmas 6.1/6.2 are subsumed by already-certified results; not re-certified.

## Goal Progress (for Eval History)
- Status: **partial** (unchanged flip-wise; residual sharpened, not closed). Still ONE gap from solved.
- self-similar-recursion: **advanced** (Elo→1638). False Lemma W discarded; 5 sound moves certified;
  residual crisply = Gap A (acyclicity) ∪ Gap B (μ=3 even-block leaf); Gap A ≡ block-recursion's
  UPM-5 — the two integrality routes share one wall (plateau signal).
- cut-budget-jacobsthal-recursion: **partial** (Elo→1519). Scaffold + two-band identity sound; novel
  driver refuted (verified); reduces to classical Case B; diversity value only.
- Both **CHANGES REQUESTED**. No APPROVE. Answer + both bounds still TRUE; upper bound certified.

## Orchestration note
The self-similar (Φ-max) and block-recursion (UPM) integrality routes are now PROVABLY the same wall
(Gap A ≡ UPM-5 chorded even cycles). Per CLAUDE.md's shared-gap-plateau rule, the tied-vertex residual
has cost multiple rounds and the two integrality framings have collapsed onto one wall — round 6
should seed ≥1 genuinely different framing (the builders suggest an SOS/quadratic-certificate route,
or the cut-budget count-function-profile monovariant) rather than another integrality variation.
