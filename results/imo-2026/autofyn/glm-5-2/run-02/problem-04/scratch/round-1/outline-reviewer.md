# outline-reviewer — imo-2026-04 (Mulan's triangle game), round 1

Conjectured answer (field consensus): **Mulan wins ⇔ θ = 180°/N for some integer N ≥ 2** (θ a unit fraction of 180°). Reviewed all 4 approach files + 3 explorer reports. Re-verified the two load-bearing facts numerically (create-move for N ∈ {2,…,99} including non-integer-degree 180/7, 180/11, 180/13, 180/17, 180/19, 180/23, 180/99; obstruction for θ ∈ {72,100,50,7,13,40,135,36.5,60.0001} — 0 escapes in 2000 trials each). The core proof is sound.

## Cross-cutting finding: the field has collapsed to ONE framing (single-gap trap)

Three of the four approaches (`mod-theta-descent`, `fixpoint-attractor`, `torsion-subgroup`) are **the same proof re-skinned** — the outliner says so explicitly in each "Watch out for" section. They share exactly two load-bearing facts:
- the **create-move** (IF: γ = θ − (Y mod θ) at the max-angle vertex makes both children carry a θ-multiple), and
- the **four-case mod-θ obstruction** (ONLY: no γ makes both children θ-multiple; the four residue combinations reduce to "an existing angle ≡ 0" or "r = 180 mod θ ≡ 0", both excluded).

If either fact has a hidden flaw, all three die together. That is the single-gap trap the orchestrator warns about. `geometric-anchor` is the only approach with a (partial) independent route, and only for the IF direction's dyadic core.

**The harder, higher-value ONLY direction (Shan-Yu's defense for non-unit-fraction θ) has NO independent framing in the field** — every approach routes through the same four-case residue chase. This is the field's main structural weakness. Flag for next round's outliner: put ≥1 approach on a genuinely different ONLY-direction framing (e.g. a direct geometric/measure-theoretic defense, or a game-tree/coinductive argument that does not reduce to the four-case residue chase).

## Per-approach verdicts

### mod-theta-descent — APPROVE
The workhorse. Both directions worked out end to end; the skeleton is essentially a complete proof. I re-derived the angle transform (child1 = (γ, Y, 180−Y−γ), child2 = (X−γ, Z, Y+γ); the two P-angles are supplementary — verified) and checked the create-move algebra (Y+γ ≡ 0 mod θ by construction; 180−Y−γ ≡ 0 because Nθ = 180) and the four-case obstruction (each case ends in X≡0, Y≡0, Z≡0, or r≡0, all excluded) — both valid. The k-descent (split kθ with γ = θ → child2 has (k−1)θ; k strictly decreases; ≤ N−2 steps) is correct.

Gaps for the builder (presentation rigor, NOT soundness):
1. **Unify the validity-inequality casework.** The θ ≤ 60 vs θ = 90 split is correct but scattered; write it as one lemma. (Numerically verified for all N ∈ {2,…,99}.)
2. **Initial-triangle existence for the ONLY direction.** The outline hedges with a "Kronecker density" caveat that is **unnecessary and misleading**: for fixed θ, the forbidden angle-values are {kθ : k = 1,…,⌊180/θ⌋}, a **finite** set (≈ 180/θ points) in (0,180). The forbidden locus in the 2-simplex is a finite union of line segments (codim-1); its complement is open and dense (indeed full-measure). Generic choice is trivial. Write it as the finite/countable-avoidance argument it actually is — do NOT invoke density of {kθ mod 180}.
3. **Four-case exhaustiveness:** already exhaustive (each child has 3 angles; Y in child1 and Z in child2 are non-zero by the invariant, leaving 2 slots × 2 = 4 combinations). State this count once.

No fatal flaw. Build it.

### fixpoint-attractor — APPROVE (sound), but DO NOT BUILD this round
A correct least/greatest-fixpoint re-skin of the AND-OR game operator. W = 𝒯 when r = 0 (create-move lifts θ-multiple-free triples into M ⊆ W via the k-induction); C = {no θ-multiple} is G-closed when r ≠ 0 (four-case obstruction). Sound. But it shares the EXACT same two load-bearing facts as `mod-theta-descent` — the outliner calls it "diversity insurance … shared wall." Building it in parallel with the workhorse duplicates effort on the same wall; if the wall breaks, both die together. Register; keep as insurance; do not spend a build slot this round. (The fixpoint framing's real value is as a verification lens IF a flaw surfaces in the workhorse's prose — pursue it then.)

### torsion-subgroup — APPROVE (sound), but DO NOT BUILD this round
A correct ℝ/θℤ circle-group framing: win ⇔ r̄ = 0̄ (180 torsion). The four-case obstruction restates cleanly in G (each case ends in "a coordinate forced to 0̄, contradiction"). Its one genuine merit over the workhorse: it makes **transparent** why the defense explorer's stronger "group ⊆ ℤ/p" invariant was wrong (that one tried to constrain γ̄ to a subgroup; the correct invariant constrains the COORDINATES, tolerating arbitrary γ̄). Same wall as `mod-theta-descent`; same single-gap trap. Register; do not build this round.

### geometric-anchor — CHANGES REQUESTED
The only approach with an independent route, and the only one worth building alongside the workhorse to keep the field diverse. The synthetic-geometry IF for dyadic θ = 180°/2^a is sound: altitude-foot-interior classification (acute: all 3; right: the legs; obtuse: from the obtuse vertex) gives θ = 90° in one move; bisecting 2θ gives θ in both children; induction on a (force 2θ = 180/2^{a−1} by IH, then bisect) gives ≤ a moves.

Issues (fixable, not fatal):
1. **Not a whole-attempt rival yet.** It defers the ENTIRE ONLY direction and all non-dyadic IF to `mod-theta-descent`. Per CLAUDE.md, a slug should target the claim end to end. The builder must either (a) be explicit and honest that ONLY + non-dyadic IF are imported lemmas (acceptable as a population member if the shared cache certifies them), or (b) ideally sketch an independent ONLY direction next round.
2. **IH-reuse subtlety (real gap).** The induction reuses "Mulan forces 2θ to appear" (the stopping condition for target 2θ) as an intermediate event for target θ. This is correct (appearance = "2θ is an angle of T" = the same event), but the outline flags it as a gap — the builder must write the one-line equivalence explicitly.
3. **Altitude-foot classification** is the only non-trivial geometric step; write it as a named lemma with the acute/right/obtuse cases.

Build it for the independent dyadic IF certification (insurance on the create-move for N = 2, 4, 8, …) and to keep the field from collapsing to one line. With the change-request that it must be honest about scope and ideally pivot toward an independent ONLY direction.

## Ranking
`update_ranking` run with 6 head-to-head comparisons. `mod-theta-descent` wins all three of its matchups (most complete, both directions, numerically verified) → Elo 1546, clear leader. The three insurance approaches cluster just below 1500 (draws among themselves — equal promise as re-skins, none separates). `geometric-anchor` edges slightly below the two re-skins because it defers the harder ONLY direction entirely, but stays close (its IF diversity keeps it competitive). All `stale` flags cleared.

## Copy request
None. The outliner did not request a copy, and I agree: the create-move + four-case is a single shared wall; branching an approach into two gap-fills would double the same wall (single-gap trap). Wait until the wall is reviewer-certified before duplicating.

## Build set (round 1)
Advance the workhorse AND build the most diverse framing — a mix, per CLAUDE.md (don't collapse to one line).

- `mod-theta-descent` — write the validity-inequality lemma cleanly, the k-descent rigorously, and the initial-triangle existence as the finite-avoidance argument it actually is. Both directions should reach reviewer-certifiable form.
- `geometric-anchor` — write the dyadic IF induction rigorously and independently (altitude-foot lemma + bisector lemma + IH-reuse statement); mark the ONLY + non-dyadic-IF deferrals honestly.

build set: mod-theta-descent, geometric-anchor
