## imo-2026-02 — lens: gap7-primary

- **This is a concrete, essentially-complete lead, not just a scouted direction — write it up carefully, but note it is still a "found in exploration, unverified by a builder/reviewer" claim.**

### Exact objects (from the file, not guessed)
From `results/imo-2026-02/approaches/coordinate-bash-resultant-boundary-pointwise-tangent.md` Step 3 and its cited lemma `lemmas/claim-I-closed-and-claim-II-caseA-closed.md` ("Setup" + Theorem A):

- WLOG `∠B ≤ ∠C`, so `γ := ∠B ≤ π/2` (from `2B ≤ B+C = π-A < π`).
- `f(β) := K_c + P sinβ + Q cosβ`, with
  `P = ½sin(A−B) + (3/2)sin(A+B)`, `Q = −sinA sinB`, `K_c = 2 sinA sin(A+B)`.
- `β₀(A) := (π−A)/3`. Case (a) is `β₁ ∈ (0, β₀(A)]` (the sub-range with no proof yet).
- **Theorem A's own proof already establishes `f'(β) = sin(A+β)cosB + sin(A+B−β) > 0` for the WHOLE open interval `(0,γ)`** (not just `(β₀,γ)`) — this is stated and proved in the "Setup"/Theorem A block itself (elementary sign facts: `cosB>0`, `sin(A+β)>0` since `A+β∈(0,A+B)⊂(0,π)`, `sin(A+B−β)>0` since `A+B−β∈(A,A+B)⊂(0,π)`), so this piece needs **no new work** — it is already certified in `claim-I-closed-and-claim-II-caseA-closed.md`, just not yet *used* on `(0,β₀]`.
- Theorem B of the same lemma proves `f(β₀)>0` (a self-contained trig argument, certified) — this is the endpoint fact Case (a)'s text alludes to but doesn't correctly chain to `(0,β₀]`.

### The lead: f(0) ≥ 0 (in fact f(0) > 0 strictly) — found and essentially closed this round

`f(0) = K_c + Q = 2sinA·sin(A+B) − sinA·sinB = sinA·(2sinC − sinB)` (verified exactly by fresh sympy: `f0 = (-sin(B) + 2*sin(A+B))*sin(A)`, and substituting `sin(A+B)=sin(π−C)=sinC` gives `(2sinC − sinB)·sinA` exactly, zero residual).

**Claim: `sinB ≤ sinC` whenever `B ≤ C`, `A+B+C=π`, `A>0`** (this is the fact that actually needs proving; `2sinC≥sinB` then follows trivially from `sinC≤2sinC` since `sinC>0`, giving `f(0) ≥ sinA·sinC > 0`, in fact strict).

Proof sketch found (elementary, two cases on whether `C ≤ π/2` or `C > π/2`):
- **Case `C ≤ π/2`:** then `B ≤ C ≤ π/2`, and sin is increasing on `[0,π/2]`, so `sinB ≤ sinC` directly.
- **Case `C > π/2`:** then `π−C < π/2`. Since `A>0`, `A+B+C=π ⟹ B < π−C`. So `B` and `π−C` are both in `(0,π/2)` with `B < π−C`; sin increasing on `[0,π/2]` gives `sinB < sin(π−C) = sinC`.

Both cases give `sinB ≤ sinC` (strict in case 2), hence `2sinC − sinB ≥ sinC > 0` and `f(0) = sinA(2sinC−sinB) ≥ sinA·sinC > 0` strictly (since `A,C ∈ (0,π)` genuine triangle angles). **Independently verified numerically**: 2M-sample and 3M-sample fresh sweeps (own `random`/`numpy` scripts, not reusing any file's code) found (i) `sinC − sinB ≥ 0` with **zero violations**, minimum `≈1.5e-7 → 0` only in the fully degenerate limit `A→0, B→C→π/2` (consistent with equality only at a measure-zero boundary, matching the proof's structure exactly: equality needs `B=C` in case 1 at `C=π/2`, or the case boundary), and (ii) the two-case partition itself (`C≤π/2 ⟹ B≤C≤π/2`; `C>π/2 ⟹ B<π−C<π/2`) holds with **zero violations** in 2M samples. `2sinC−sinB` itself was independently swept (my first script): minimum `≈0.0013` trending to `0` only as `A→π` (fully degenerate, both `B,C→0`), consistent with strict positivity on the open (non-degenerate) domain.

### How this closes Gap 7
Combine:
1. `f` is continuous (in fact analytic — a finite trig-linear combination) on the closed interval `[0,γ)`, including at `β=0`.
2. `f'(β) > 0` throughout the open interval `(0,γ)` — **already proved**, Theorem A's own proof (see above), no new derivative work.
3. Standard real-analysis fact (MVT corollary): continuous on `[0,γ)`, strictly positive derivative on `(0,γ)` ⟹ `f` strictly increasing on the closed-below interval `[0,γ)`, i.e. `f(β) > f(0)` for every `β ∈ (0,γ)`.
4. `f(0) ≥ 0` (in fact `> 0`), proved above from scratch, elementary, no numerics needed in the final form.

⟹ For every `β₁ ∈ (0, β₀(A)] ⊂ (0,γ)`: `f(β₁) > f(0) ≥ 0`, i.e. `f(β₁) > 0`. **This is exactly the missing Case (a) fact (Gap 7), for the FULL sub-range `(0,β₀(A)]`, not just asymptotically.**

This does not need Theorem A's `(β₀,γ)`-restricted conclusion at all — it uses only Theorem A's *proof* of `f'>0` on `(0,γ)` (already established) plus the new `f(0)≥0` fact. So the fix is: extend Theorem A's stated conclusion (or add a Theorem A′) to say `f` is strictly increasing on all of `[0,γ)` with `f(0)≥0`, hence `f>0` on all of `(0,γ)` — which then also trivially re-derives Theorem A's original `(β₀,γ)` statement (a special case) and Theorem B (`f(β₀)>0`) becomes a corollary too, though Theorem B's existing proof can stay as an independent cross-check.

### What still needs writing up (not yet a certified lemma)
- The `sinB ≤ sinC` two-case argument itself, cleanly, as a lemma (elementary — should be quick for a builder).
- The MVT/continuity extension step from "positive derivative on open interval" to "strictly increasing on the half-open closed-at-0 interval" — standard but must be stated with the right hypotheses (continuity at 0, which holds trivially since `f` is a finite sum of `sin`/`cos` compositions).
- Confirming `(0,β₀(A)] ⊆ (0,γ)` in all cases where Case (a) is invoked (should already be guaranteed by the file's own Case (a)/(b) split, `β₀(A)<γ` is exactly the "domain nonempty" condition used throughout).

### Cheap-kill / sanity check performed
- Checked whether `f(0)≥0` might fail somewhere in the *actual* Case-(a) sub-domain (not just the full angle simplex) — no, the proof above uses only `B≤C, A>0`, which is required WLOG throughout the whole file, so it's unconditional on the whole domain `D`, a strict superset-safe fact.
- Checked whether `2sinC≥sinB` was tight/needed exactly — no, `sinC≥sinB` alone already gives `2sinC-sinB≥sinC>0`, so the "2×" is not even load-bearing; slight slack in the fact, good margin for the builder.

### Knowledge-base entries
Nothing beyond elementary trig monotonicity (`sin` increasing on `[0,π/2]`) and the Mean Value Theorem / continuity-derivative-sign-to-monotonicity corollary — both standard real-analysis facts, likely already implicitly used elsewhere in this file's MVT/Lipschitz machinery (`lemmas/mvt-lipschitz-reduction-case-b.md` uses MVT already, so the technique is already "in-house" for this population).

### Dead ends / things NOT to retry
- Do not try to prove `G(β₁)≥0` in Case (a) — round 18 confirmed (2M samples) this is FALSE ~70% of the time; `G` is provably the wrong target for Case (a). The file's own "Setup" aside already flags this; my numeric spot-check (independent, smaller scale) is consistent with round 18's finding — no need to re-verify further, it's already solidly established.
- Do not re-derive Theorem A's `f'>0` proof — it is already fully general on `(0,γ)`, not restricted to `(β₀,γ)`; the restriction in the file's stated Theorem A conclusion is an artifact of how it was originally invoked (for the `(β₀,γ)` sub-case only), not a limitation of the proof itself.

### Small-case / intuition notes (labeled conjecture where not yet in lemma form)
- Conjecture (now essentially proved above, pending write-up/certification): `sinB ≤ sinC` for all triangle angles with `B≤C` — true with equality only at degenerate/boundary configurations (`B=C` and `C=π/2` simultaneously forces `A=0`, i.e. only in the fully degenerate limit within case 1; case 2 is always strict). This is a clean, general, reusable fact about triangle angle sines, likely useful elsewhere in the population too (e.g. anywhere `sinB` vs `sinC` sign comparisons come up).
- `f(0) = sinA(2sinC-sinB)` numerically bottoms out near `0` only as `A→0` or `A→π` (degenerate triangle), consistent with strict positivity `f(0)>0` for every genuine (non-degenerate) triangle, matching the proof.
