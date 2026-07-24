# Build report — self-similar-recursion, round 5

## Status: partial (honest). NOT solved. Two explicit residual gaps remain.

## What I did
Rebuilt the tied-non-degenerate integrality closure on SOUND moves, discarding the refuted Lemma W.
Every step below is numerically verified and avoids ALL round-4 refutations (Lemma W, the V-kink
3-shift, global integrality).

### Proved unconditionally this round (new, sound)
1. **Lemma S-core (`ker U=0`)** — salvaged sound half of old Lemma S. Feasible sum-preserving
   component shift ⇒ minimality (non-flat) or Φ-max (flat, strict convexity) contradiction. FULL.
2. **Move M2 (two invisible pairs)** — reviewer fix #1 executed. `{v,v,v,v}→{v+t,v+t,v-t,v-t}`,
   each pair P1-invisible so f unchanged (STAYS in G), Φ+4t². Excludes ALL μ_{k,j}≥4 (even OR odd —
   so the "μ even ⇒ power of 2" error is moot; M2 kills every μ≥4). ⇒ μ_{k,j}∈{1,2,3}. FULL, 0/30000.
3. **Move M3 (symmetric odd-block move)** — the correct REPLACEMENT for the refuted V-kink 3-shift.
   Move one same-piece copy +s, another −s, keep the third. For ODD-size tie-block, Δf =
   s(σ_a − σ_{a+μ−1}) = 0 EXACTLY (signs equal), f flat, STAYS in G, Φ+2s². ⇒ every odd block has
   μ_{k,j}≤1. FULL, 0/29962 (small-s). The key sign identity is what the old V-kink got wrong.
4. **Move M4** — no piece has two sub-pieces both in odd blocks (within-piece transfer is affine
   with slope σ_{a(u)}−σ_{a(w)}; nonzero⇒descent, zero⇒Φ-convex contradiction since dΦ/dδ=2(u−w)≠0).
   FULL. This is the mechanism driving the non-integer continuum `piece2={a,2−a}` to the degenerate
   boundary — consistent with round-4 refutation.
5. **Block formula** f = Σ_{μ_j odd} σ_{a_j} w_j (even blocks f-invisible). FULL, 0/20000.

### Conditional finish (Step 5 of proof)
GIVEN Gap A (forest) + Gap B (no μ=3 even-block leaf): generalized piece-leaf peeling ⇒ every w_j∈ℤ
⇒ (Theorem F, Σ=D_n odd) f(P*) odd ≥1. Peeling is valid: every tree of a forest has a piece-leaf
(degree count + full column rank), and μ∈{1,2} leaves give integer 2^k or 2^{k-1}. FULL given A,B.

## The two OPEN gaps (only open steps in the whole problem)
- **Gap A (acyclicity of the Φ-max incidence multigraph).** ker U=0 does NOT force a forest for a
  multigraph (`[[1,2],[2,1]]` has trivial kernel, is a double-edge 2-cycle). Cycles touching only
  cycle-pieces are killed by Lemma S-core; externally-touched / multiplicity-≠1 cycles are not.
  SAME wall as block-recursion's chorded-even-cycle UPM-5. Did not close.
- **Gap B (μ=3 even-block piece-leaf = core of "Φ-EVEN").** `piece 2^k={v,v,v}`, v=2^k/3, v shared.
  No LOCAL move excludes it (domain is a PRODUCT of per-piece simplices — no cross-piece moves; M3
  gives only a stable V-kink on the even block; M2 needs 4 copies). Exclusion needs a GLOBAL
  degenerate-domination lemma. Numerics strongly support it (3-equal-splits give f≈2.3–6.3 >> 1;
  {2,3,3} Φ=35 dominated by degenerate {5,4,2,2,1,1} Φ=51 same f=1). Did not close.

## Reviewer's mandated fixes — status
1. "μ even ⇒ power of 2" error: RESOLVED cleanly — M2 excludes ALL μ≥4 (parity-independent), so
   the flawed inference is never used. Surviving μ∈{1,2,3}.
2. Lemma Φ-EVEN's V-kink mechanism: REPLACED for the ODD-block half (M3, symmetric shift, provably
   stays in G). But the EVEN-block μ=3-leaf half (Gap B) is NOT closed by any local move — it
   genuinely needs the degenerate-domination lever, which I could not prove in general. Honestly
   flagged as Gap B.
3. Cycle⇒kernel through multiplicity edges (Lemma S′): confirmed the 0/1 cycle argument does NOT
   transfer, and ker U=0 alone does not give a forest for multigraphs. Flagged as Gap A.

## Spec concerns for the orchestrator
- The two integrality routes (self-similar Φ-max, block-recursion UPM) are now provably the SAME
  wall: Gap A ≡ block-recursion's chorded-even-cycle residual. The reviewer's "Φ-max forest ⊋ UPM"
  subsumption claim is OPTIMISTIC — Φ-max gives ker U=0, NOT acyclicity, for multigraphs. So the
  field's two integrality routes share ONE wall (Gap A) after all. This is a genuine plateau signal.
- The residual is now crisply TWO graph facts (A: forest; B: no μ=3 even-block leaf). If the next
  round wants integrality, Gap B likely needs a global degenerate-domination lemma (equal-splits
  raise f / lower Φ vs a bisection competitor); Gap A needs a multiplicity-aware cycle exclusion.
  Both are narrow and checkable, but neither is local. Consider seeding the SOS/quadratic-certificate
  framing (reviewer's opening D) as a genuinely different route, since both integrality routes now
  share Gap A.

## Files
- Proof: /home/agentuser/repo/results/imo-2026-03/approaches/self-similar-recursion.md
- 4 promotable sound lemmas proposed (S-core, M2, M3, block-formula) in that file's Promotable section.
