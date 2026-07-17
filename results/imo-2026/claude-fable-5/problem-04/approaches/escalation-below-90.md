# Approach: escalation-below-90

## Status
unsolved

## Approaches tried
- 2θ-double-threat escalation targeting the answer "Mulan wins iff 0° < θ ≤ 90°" (round 1) — opened as the falsification rival to the residue-divisibility field; blocked at Step 0 unless a hole is found in the mod-θ invariant.

## Current best
Nothing correct established beyond the shared lemmas (θ = 90 one-move win; θ > 90 Shan-Yu "all angles < θ" invariant). This approach's target answer (all θ ≤ 90) CONTRADICTS the residue invariant of `residue-divisibility-characterization` for every θ ≤ 90 with 180/θ ∉ ℤ (e.g. θ = 55°). Exact-fraction adversarial search (depth 8, structured cut candidates) found no Mulan win at θ = 55° or 40°, supporting the rival. This approach lives only if Step 0 below succeeds.

---

## Proof body (with gaps)

**Target answer.** Mulan wins iff 0° < θ ≤ 90°.

**Step 0 (mandatory gate — attack the residue invariant).** The rival's Step 3b claims: if no angle of (P,Q,R) is in θℤ and 180 ∉ θℤ, then for every attacked vertex and every t, some child has no angle in θℤ. To keep this approach alive, exhibit a concrete hole: either
- (a) a Mulan strategy at some θ ∤ 180 (say θ = 55°, exact arithmetic) winning against all Shan-Yu replies — this would require the invariant algebra to be wrong (recheck the child formulas C1 = (P, t, Q+R−t), C2 = (Q, R−t, P+t) and the four-case intersection), or
- (b) an error in the claim that a winning terminal state must contain an angle in θℤ (it contains θ itself, class 0 — hard to dispute), or
- (c) a legal move outside the modeled move set (e.g. a reading of the problem where the cut point choice gives Mulan more than the (vertex, t) parameters — recheck the statement).
*If Step 0 fails, this approach is dead and should be recorded as a dead end for the whole "θ ≤ 90" answer.*

**Step 1 (θ > 90: Shan-Yu wins).** Shared with the field: start equilateral; maintain "all angles < θ". Breaking it in one move needs r1 ≥ θ − P and r2 ≥ θ − Q with r1 + r2 = R, feasible iff 2θ ≤ 180. For θ > 90 the invariant is unbreakable.

**Step 2 (θ = 90: one-move win).** At most one angle ≥ 90; attack it (or any vertex if acute) with r2 = 90 − Q: children (P, r1, 90) and (Q, 90−Q, 90) both contain 90.

**Step 3 (θ < 90: escalation — conditional on Step 0).** Force an angle exactly 2θ (split it θ + θ: both children contain θ), via the fork r1 = 2θ − P which plants 2θ in C2 while C1 = (P, 2θ−P, 180−2θ) has fixed third angle 180 − 2θ; escalate by peeling θ off the leftover (forced transfers), driving the leftover down 180 − kθ until a multiple-of-θ coincidence is forced.
*GAP (fatal as far as round-1 analysis shows):* the peeling dynamics preserve residues mod θ (proved by the retrieval explorer), and the fork analysis shows no residue can ever be fixed when 180 ∉ θℤ — exactly the rival's invariant. No mechanism found that escapes it.

## Open gaps
- Step 0 (the gate): find a genuine hole in the residue invariant, or record this answer as refuted.
- Step 3: the entire forcing construction for θ ∤ 180, θ < 90 — currently believed impossible.

## Watch out for
- Do not cite the round-1 grid simulations as evidence for wins at θ = 55°, 33°, 70°: nearest-grid-point lookup fabricates exact hits; the exact-fraction search contradicts them.
- If Step 0(c) is explored: the statement says P is on the perimeter, different from the three vertices, cut to the OPPOSITE vertex — the (vertex, t) model does appear complete.
