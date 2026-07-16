## imo-2026-04

Central disagreement RESOLVED in favor of the two-explorer consensus: the answer is
**θ = 180°/N, N ≥ 2 integer** (180/θ ∈ ℤ). The analogy lens's "rational ≤ 90°" answer is
wrong on θ = 72°. Reason (algebra + computation, both checked this round): the ONLY way one
cut makes both children non-safe is the identity 180 = (n+m)θ, i.e. 180/θ ∈ ℤ. For θ = 72°
no cut from a safe triangle produces two non-safe children (grid-confirmed for 72,40,100,50),
and Mulan cannot force 144° = 2θ (a {72,144} child pair forces A=216, B=72, C=−72, or
sum=216 — all impossible). So 72° loses; Shan-Yu cycles on (36,36,108). The θ=180/N
construction x = A+C−nθ works exactly (the grid only missed it by resolution at the exact x).

Field: two rival routes to the correct answer (hedging the winning-side gap) plus one rival
carrying the disputed answer so the ranking tests 72° head-on and refutes it explicitly.

---

safe-set-invariant: new
Target: Characterize all θ for which Mulan forces a win — prove it is exactly θ = 180/N (N≥2),
  with Mulan's winning strategy for those θ and Shan-Yu's survival for all other θ.
Technique: Two-sided. Impossibility via closed "safe set" S = {no angle is a multiple of θ},
  4-case closure lemma driven by 180=(n+m)θ. Sufficiency via one-cut-both-multiples (Phase 1)
  + multiplicity descent kθ→(k−1)θ→…→2θ→θ (Phase 2).
Skeleton:
  1. Shan-Yu start (θ/2,θ/2,180−θ) ∈ S — by θ≠180/N ⟹ 180−θ not a multiple.
  2. Closure lemma: parent ∈ S, θ≠180/N ⟹ some child ∈ S — by 4-case split forcing a parent
     angle to be a multiple OR 180=(n+m)θ, both excluded.
  3. Induction ⇒ Shan-Yu survives ⇒ θ≠180/N loses.
  4. Phase 1 (θ=180/N): cut largest vertex, x=A+C−nθ ⟹ both children carry nθ and (N−n)θ.
  5. Phase 2: descend the multiplicity to k=2, where both children get θ ⇒ win in ≤N steps.
  6. N=2 (θ=90): supplementary (90,90) one-step win.
Key lemmas: closure lemma (both children non-safe ⟹ 180=(n+m)θ, from matching supplementary
  multiples); both-multiples cut (x=A+C−nθ, apexes nθ and 180−nθ=(N−n)θ); descent (x=θ off a
  kθ vertex leaves (k−1)θ and plants θ; k=2 wins).
Open gaps: G1 Phase-1 existence of n for EVERY start incl. triangles already holding a higher
  multiple (route to Phase 2), largest-angle>θ; G2 Phase-2 validity/positivity; G3 N=2
  realizability of x+B=90; G4 closure 4-case exhaustiveness across all vertices/third angles.
Cases to cover: impossibility all θ≠180/N (rational 72/40 AND irrational); sufficiency N=2 vs N≥3.
Watch out for: 72° is rational ≤90 but loses — closure lemma applies; do not equate rational
  with 180/N. Phase-1 endpoint A+C=nθ hides a parent-multiple.

force-2theta-bisect: new
Target: Same full characterization (θ=180/N), independent winning-side route.
Technique: Winning = force an angle exactly 2θ, then bisect it (cut 2θ vertex with x=θ ⟹ both
  children θ). Reach 2θ by descending the multiple chain. Impossibility = import/rederive safe set.
Skeleton:
  1. Impossibility: import closure lemma (or "supplementary multiples ⟹ 180/θ∈ℤ").
  2. Chain entry: force survivor onto {2θ,…,(N−1)θ} via a both-multiples cut.
  3. Descend kθ→(k−1)θ (cut θ off the kθ vertex) until 2θ.
  4. Bisect 2θ ⟹ both children θ ⇒ win.
Key lemmas: 2θ vertex is an immediate 1-move win (θ+θ=2θ); descent monovariant on marked
  multiplicity; chain entry needs 180=Nθ.
Open gaps: G1 chain entry for arbitrary start; G2 descent validity + Shan-Yu can't escape;
  G3 impossibility import; G4 N=2 special case (2θ=180 degenerate — use direct 90-90 win).
Cases to cover: N=2 (direct) vs N≥3 (chain+bisect); impossibility all θ≠180/N.
Watch out for: N=2 makes 2θ=180 vacuous; chain entry FAILS for θ≠180/N (e.g. 72°, no
  180=(n+m)·72) — do not claim it there.

rational-below-90: new (RIVAL ANSWER — deliberately tests 72°)
Target: The rival characterization θ ∈ ℚ·180 ∩ (0,90]; carries the analogy answer so the
  ranking must confront 72° directly.
Technique: θ>90 loses (2θ>180); irrational loses (rational-angle invariant); rational≤90
  claimed to win by forcing 2θ via periodic chain kθ mod 180.
Skeleton:
  1. θ>90 impossibility — 2θ>180 blocks the only double-θ cut.
  2. Irrational impossibility — rational-angle invariant, Shan-Yu keeps rational child.
  3. Rational≤90 sufficiency — CONTESTED: force 2θ then bisect.
Key lemmas: θ>90 and irrational impossibility (both SOLID, reusable under either answer);
  the disputed "rational≤90 ⟹ force 2θ" lemma.
Open gaps: G1 (decisive) prove-or-REFUTE force-2θ at θ=72°; outliner algebra says it is FALSE
  (a {72,144} child pair needs A=216/B=72/C=−72/sum=216, all impossible) ⇒ Part C fails ⇒
  correct answer is 180/N. G2 exhibit any actual win for a rational θ≤90 with 180/θ∉ℤ, else concede.
Cases to cover: θ>90; irrational; rational≤90 split 180/θ∈ℤ (wins) vs ∉ℤ (72,40 — predicted lose).
Watch out for: Parts A (θ>90) and B (irrational) are correct under BOTH answers — harvest them
  as shared lemmas even when Part C is refuted; then retire the rational-≤90 claim.

---

Proposed slugs to register (all Status=unsolved, new this round):
- safe-set-invariant — key gap G1: Phase-1 both-multiples cut exists from EVERY start (largest angle > θ, integer n in (C,A+C)).
- force-2theta-bisect — key gap G1: force the survivor onto the multiple chain from an arbitrary start (chain entry).
- rational-below-90 — key gap G1: prove/refute "rational θ≤90 forces 2θ" at θ=72° (outliner predicts REFUTE ⇒ 72° loses ⇒ answer is 180/N).

Recommended build set (spread + head-on 72° test): safe-set-invariant, force-2theta-bisect, rational-below-90
