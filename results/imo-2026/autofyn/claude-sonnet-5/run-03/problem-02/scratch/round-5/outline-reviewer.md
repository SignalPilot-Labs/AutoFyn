## imo-2026-02 — outline review, round 5

Read: `/tmp/round-5/proof-outliner.md`, `results/imo-2026-02/current.md`,
`results/imo-2026-02/approaches/{coordinate-bash-resultant-boundary,
ptolemy-trig-identity,fixed-point-concyclic}.md`,
`/tmp/round-5/math-explorer-f3lens.md`, `/tmp/round-5/math-explorer-positivitylens.md`.

Independently reproduced (own `numpy`/`scipy` scripts, not the explorers'
code) the two key claims flagged for scrutiny. Both check out, and one is
even simplifiable.

### Independent verification 1 — cross-product-sign selection (f3lens's finding)

Rebuilt the exact rotation parametrization (`A=(0,0),B=(a,0),C=(b,cc)`,
`K=B+t1(-cosβ,sinβ)`, `L=C+s2·R(β)(A-C)`) from scratch using the *true*
transcendental hypothesis-2/3 angle equations (`∠LBK=∠LNC`, `∠LCK=∠BMK`,
via `arccos`/`arctan2`, not the population's derived polynomials) plus
`point_in_triangle` containment tests.

- Reproduced the explorer's exact counterexample triangle
  (`a,b,cc=1.763,1.534,0.297`, `β≈0.8306`): hyp-2 has 3 roots in `s2`, two
  (`0.0152`, `0.0330`) both pass plain containment `L∈△BNC` — confirms the
  "plain containment under-determines near an F3-crossing" claim exactly.
- **New finding beyond the explorer's report**: the condition "K inside
  angle LBA" is a function of `(β, s2)` **only** — it does *not* need `t1`
  at all, because ray `BK`'s direction is fixed by `β` alone (`t1` only
  scales along that fixed ray), so "ray BK lies between rays BA and BL" is
  a pure direction/cross-product test on `(β,s2)`. Symmetrically, "L inside
  angle ACK" depends on `(β,t1)` only. **This means the two extra
  hypotheses are NOT a "joint condition coupling K and L together" as the
  outline's Step 3/Key-lemma text describes — each one is a single-variable
  (plus β) selection criterion, fully decoupled, mirroring the existing
  homogeneity-decoupling lemma.** This is a genuine simplification of the
  outline's plan, not a flaw in it.
- Verified this simplified (decoupled) criterion at scale: ~4000 random
  triangles per side, 34 multi-root hyp-2 cases and 47 multi-root hyp-3
  cases found (i.e. genuinely non-rare, matching explorer's ~1/1300
  estimate), **100% uniquely resolved (81/81) by the single-hypothesis
  cross-product-sign test alone**, with sign-of-the-fixed-reference-cross
  (`cross(BA,BK)`, itself β-only) as the test rule. On the reproduced
  counterexample, the surviving root (`s2=0.0152`) matches the explorer's
  reported `G2a`-branch root exactly.
- **Verdict: the mechanism is real and well-supported**, and the builder
  should be told to attempt the simpler decoupled version first (test each
  extra hypothesis against its own single quadratic-branch pair,
  independently) before the outline's more complex "four joint
  combinations" framing — this should make Steps 3–4 meaningfully easier
  than the outline anticipates.

### Independent verification 2 — F>4 sharpened positivity target

Rebuilt `F(θ,A,B,C)` from the file's exact closed forms (`a1,b1,c1,D1,x`
and the `B↔C` swap for `a2,b2,c2,D2,y`) in a fresh script.

- 200,000-sample random sweep: `min F ≈ 4.014`, **zero samples with
  `F≤4`** — confirms `F>4` and the near-tightness.
- Targeted sweep `A→0` along `B=C, θ=B/2`: `F−4` shrinks linearly
  (`A=0.1→F−4≈0.91`; `A=1e-6→F−4≈8e-6`), i.e. **`F→4` exactly as `A→0`**
  along this direction — confirms the claimed extremal limit is real, not
  a sampling artifact.
- A second direction (`B=1.5` fixed, `A→0`, `θ=0.75·min(B,C)`) does *not*
  approach 4 (stays `≥5.14`), confirming the explorer's claim that `F→4`
  only along specific degenerating directions, not the whole `A→0`
  boundary — consistent, not contradictory.
- 500,000 more random samples found global min `≈4.005`, no violations.

**Verdict: F>4 is robustly supported and correctly reduced to exactly
`α+α'<A` (Step 1, already certified) — this is a sound, well-scoped
target for the blow-up/radical-clearing plan.**

### Per-approach verdicts

**coordinate-bash-resultant-boundary (advance) — APPROVE (with a
simplification note).** Technique is sound, both new steps are backed by
independent numeric confirmation at meaningfully larger scale than the
explorer's own test (81 resolved cases vs. explorer's smaller sample), and
I found the underlying mechanism is actually simpler (decoupled per
hypothesis) than the outline states — tell the builder to try the
single-hypothesis version first. Step 4's "sign-fixed-factor on the G2b
branch" is honestly flagged as a conjectured mechanism to formalize, not
asserted as done — correct labeling, no overclaiming risk. The magnitude
bound `t1<t1max(β)` watch-out is correctly retained as a separate possible
gap.

**ptolemy-trig-identity (advance) — APPROVE.** `F>4` independently
reconfirmed, tightly characterized (exact limit 4, approached only along
specific degenerating directions as `A→0`). The plan (compute `F−4`
directly, blow-up analysis in `A=εa`, fallback to radical-clearing + SOS)
is a standard, appropriate toolkit for this kind of boundary-tight
inequality — sound technique, no red flags. Correctly avoids repeating the
dead-end `sympy.simplify`/naive-interval-bound approaches.

**ptolemy-trig-identity-synthetic (copy) — APPROVE.** A genuine second
lever on the *same* precisely-isolated gap (`α+α'<A`), using auxiliary-
circle/inscribed-angle ideas instead of algebra — legitimate use of
`copy_approach` per its documented purpose (same proven prefix, two
viable ways to close the remaining gap). Correctly cites the round-1
8-point concyclicity search boundary (nine-point circle wasn't in that
search) so it isn't retreading refuted ground, and explicitly avoids the
already-dead spiral-similarity-at-A shortcut. Entirely speculative (no
mechanism found yet), honestly labeled as "a fresh search," registered
freshly at cold-start Elo — appropriate.

**fixed-point-concyclic (revise) — APPROVE.** Extending the previously-
diagnosed-precisely elimination (`T ≡ −(BC̄−B̄C)·S mod ⟨P1,P2,P3⟩`) with
two new constraints `P4,P5` built from the *same* newly-identified extra
hypotheses is a well-motivated, cheap, honestly-scoped test (either `S`
falls into the extended ideal, closing the gap, or it reports the new
remainder's structure — precedent of two prior honest negative reports
from this file gives confidence it will be reported accurately either
way). Correctly imports the population's certified isosceles lemma
instead of re-deriving it.

### Convergence note (not a RETHINK, but flag for tracking)

Two of the four approaches (`coordinate-bash-resultant-boundary` and
`fixed-point-concyclic`) both pivot, this round, on the *same* newly-
discovered insight (the two extra "K inside ∠LBA / L inside ∠ACK"
hypotheses are load-bearing for uniqueness) — but via genuinely different
algebraic devices (real cross-product signs in the rotation
parametrization vs. complex "ratio ∈ ℝ" polynomials in the cross-ratio
elimination), so this is legitimate technique diversity on a shared
insight, not a same-framing plateau. Watch next round: if *both* stall on
"does the extended constraint set actually kill the obstruction," that
would indicate the insight itself (not just one formalization of it) is
insufficient, and a third mechanism would be needed.

No approach is RETHINK. All four target the actual problem end-to-end
(via the already-proved reduction chain to the central identity /
`A,K,L,Q` concyclic), none is a sub-lemma split across siblings, and none
repeats a recorded dead end (acute-angle bound, spiral-similarity-at-A,
naive containment-interval bound, direct `sympy.simplify` on the raw
radical, literal IVT-transfer to `G2a` alone — all correctly avoided).

### Ranking

Registered `ptolemy-trig-identity-synthetic` (new copy) at cold-start Elo.
Ran `update_ranking` anchoring the new copy against its established
sibling and against the other two established approaches: post-round Elo
order is `coordinate-bash-resultant-boundary` (1594, top — most concrete,
independently-strengthened progress this round) ≈ `ptolemy-trig-identity`
(1544, close second — tight, well-scoped remaining gap) > `fixed-point-
concyclic` (1500 — plausible but fully untested extension) >
`ptolemy-trig-identity-synthetic` (1457 — freshest, purely speculative).
`coordinate-bash-resultant` (not sampled this round, last Elo 1535,
untouched) remains in the population unranked this round.

build set: coordinate-bash-resultant-boundary, ptolemy-trig-identity, ptolemy-trig-identity-synthetic, fixed-point-concyclic
