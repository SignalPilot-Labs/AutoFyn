# Build report — right-spreading-fixed-points (round 1, imo-2026-05)

## Outcome
Status set to **solved**. Both open gaps closed; full proof written to
`results/imo-2026-05/approaches/right-spreading-fixed-points.md`.

## What was done
- **Steps 2.1–2.3 proved in full inside the file** (no certified lemmas existed in `results/imo-2026-05/lemmas/` at build time, so nothing to import). FE by x = f(y) in both inequalities (the QM/GM collapse to f(y) is stated without squaring, using f(y) > 0); ORB by a clean double-payload induction (fⁿ(y) = y + n·h(y) AND h(fⁿ(y)) = h(y), both needed in the step); NONNEG by Archimedean orbit escape.
- **GAP 1 (Step 2.5' chase) closed** per the reviewer's note (b): explicit threshold on n — n = max(0, ⌈(x₀−y₀)/b⌉, ⌊(a²/(b−a)−y₀)/b⌋+1) guarantees both yₙ ≥ x₀ (so the chasing index m = ⌈(yₙ−x₀)/a⌉ is a well-defined integer ≥ 0 with s = xₘ − yₙ ∈ [0, a)) and yₙ > a²/(b−a) (the strict kill). The expansion (EXP) LHS−RHS = 4yₙ(a−b) + (s+a)² − 4sb is derived inline term by term; the lossy crude bound the file warned about is avoided (a note in the proof records why: crude only kills b > 2a).
- **GAP 2 (Step 2.6' spreading) closed** per the reviewer's note (a): the Sub-claim [y₀, S) ⊆ F is proved explicitly (every t < sup A lies below some s ∈ A; nested-union phrasing included), and the chosen y ∈ W = (S−r₀, S) is shown to satisfy y > y₀ (via S ≥ y₀ + 2r₀, so S − r₀ ≥ y₀ + r₀ > y₀), which makes √(a·y) > r₀ strict and pushes the union [y₀, S) ∪ [y, y+2√(ay)) past S to cover [y₀, S+r₀), including the endpoint S itself.
- **Case exhaustion made airtight** in Step 2.7': a subset of [0, ∞) with ≥ 2 elements either has two positive elements (2.5') or equals {0, a} (2.6'); hence range(h) is a singleton {c}, c ≥ 0.
- All four load-bearing identities re-verified with sympy before writing (verification SOS margins ×2, (EXP), the fixed-point zone (y−y₀)² − 4ay₀). Every squaring in the prose is flagged as between positive quantities.
- Knowledge-base citations aligned to the actual entry name ("Standard inequalities: AM-GM, QM-AM").

## Promotable lemmas (for the proof-reviewer to certify into lemmas/)
- **FE**: f∘f = 2f − id (Step 2.1).
- **ORB**: h(fⁿ(y)) = h(y), fⁿ(y) = y + n·h(y) ∈ ℝ_{>0} (Step 2.2).
- **NONNEG**: h ≥ 0 (Step 2.3).
- **ONEPOS**: h takes at most one positive value — right-inequality-only proof (Step 2.5').

I did not write lemma files myself to avoid colliding with the sibling builder (orbit-forbidden-zone proves identical 2.1–2.3); statements + proof locations are listed under `## Promotable lemmas` in my approach file for one-time certification.

## Spec concerns
None. The problem statement in `problems.jsonl` matches the dispatched statement; answer_type is a characterization and both directions (verification + uniqueness) are in the proof. No continuity/monotonicity was assumed anywhere; only the right inequality is used after Step 2.1 (Step 2.1 itself needs both sides, which is inherent to this route).

## Points a reviewer should probe (I believe they hold, flagging for attention)
- Step 2.6'(ii): the union-covering argument [y₀,S) ∪ [y, y+2√(ay)) ⊇ [y₀, S+r₀) — I wrote the overlap justification ([y, S) nonempty since y₀ ≤ y < S); check the endpoint S is indeed covered (it is: S > y and S < y+2√(ay)).
- Step 2.5' threshold arithmetic: (T2) is strict (n > threshold), handled by the ⌊·⌋+1 term in the max.
