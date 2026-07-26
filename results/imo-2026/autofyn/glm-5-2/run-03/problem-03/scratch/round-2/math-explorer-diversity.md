# imo-2026-03 — diversity scout (upper-bound framings FAR from pairing)

Lens: find UPPER-BOUND framings structurally different from the pairing/D-monovariant line that 3 of 4 round-1 approaches converged on. Five candidate framings probed; the field narrowed to ONE genuinely different live opening and three confirmed dead-ends.

## Distinct openings surfaced

### (A) MIN OVER A FINITE FAMILY OF EXPLICIT XIANG STRATEGIES — the live genuinely-different framing

**Core idea.** The upper bound is `max_Liu min_Y D(Liu, Y) ≤ 1/D_n`. Instead of exhibiting ONE pairing construction (the round-1 wall: a domino partition for arbitrary marks is not known in closed form), exhibit a *finite family* `{S_k}` of simple explicit Xiang strategies and prove `max_Liu min_k D(S_k, Liu) = 1/D_n`. Pairing (= "equal-halve the n largest pieces", giving `D = p_{n+1}` in the regime `p_n ≥ 2 p_{n+1}`) is just ONE member of this family — `S_{n+1}`. The *genuinely different* members are the **barely-split strategies**: "barely-split piece `p_i`, equal-halve piece `p_j`, leave the rest," giving `D ≈ p_i − p_{i'}` (a difference of consecutive-ish pieces) rather than a lone small piece.

**Why this is far from pairing.** Pairing seeks near-equal pairs that cancel exactly. The barely-split branch deliberately creates a TINY fragment `ε` at the last rank and exploits that `ε` at the last odd rank cancels the `−ε` inside the barely-split piece at rank 1 — so the value is `p_i − p_{i'}`, a *difference of two Liu pieces*, not a residual small piece. Round-1 approaches never consider this as a co-equal strategy; they treat barely-split only as the n=1 special case.

**Concrete small-case evidence (n=2, probed).** For the dyadic config `{4/7, 2/7, 1/7}` (= the lower-bound witness / unique worst case), MULTIPLE family members tie at `D = 1/7`:
- `S_3` (equal-halve both 4/7, 2/7): `D = p_3 = 1/7`. ✓ (this is pairing)
- "equal-halve 4/7, barely-split 2/7": `D = p_2 − p_3 = 2/7 − 1/7 = 1/7`. ✓ (NOT pairing)
So the dyadic tie-point is realized by BOTH a pairing and a non-pairing strategy — exactly what a minimax-over-a-family proof needs.

**Family-membership / regime caveat (probed, not resolved).** A naive 3-member family `{equal-halve top 2, barely-split p_1 + equal-halve p_2, equal-halve p_1 + barely-split p_2}` is INSUFFICIENT: on 20k random n=2 configs, 1667 exceed 1/7 (worst 0.199 at Liu ≈ {0.403, 0.398, 0.199}). The true optimal for that witness is `D = 0.005`, achieved by *barely-split p_1 + equal-halve p_3* (the smallest piece, not the middle one) — a family member my naive 3-set omitted. So:
- the family must range over ALL choices of (which piece to barely-split) × (which piece to equal-halve), and the D-value of each member is **regime-dependent** (the sort order changes as `p_j/2` crosses `p_k`).
- the outliner must either (i) map the full family with a regime tree and prove the minimax, or (ii) find a cleaner parametric form.

**Tightness check.** For the dyadic n=2, n=3 configs, the true optimal Xiang D matches `1/D_n` exactly (probed: `0.142857`, `0.066667`). Worst random n=2 config found over 400 samples: `D = 0.139 < 1/7`. So the dyadic config is the unique worst case (Liu's lower-bound witness), confirming the minimax is attained there and the bound is tight.

**Candidate technique:** minimax over a finite explicit-strategy family + regime casework (KB: *Extremal principle* / *Casework*; analog: aimo-0198's "min(A,B) ≤ (A+B)/2" minimax-of-two-options recursion).

### (B) LP / minimax-duality within a fixed sort-order regime — secondary, less concrete

**Core idea.** Within a fixed total order of the final pieces (no rank ties), `D` is a LINEAR functional of Xiang's split positions; the minimization over splits (in that regime) is an LP, and the dual gives a *weighting/potential certificate* on the piece intervals proving `D ≤ 1/D_n`. The dual variable would be a weight function `w` on the pieces whose sum certifies the bound.

**Obstacle.** The optimal Xiang reply crosses sort-order boundaries (it deliberately creates equal pieces that TIE — the pairing mechanism). So the LP certificate only works regime-by-regime; the global bound needs a regime-transition argument. Not obviously viable as a clean single certificate, but could COMBINE with opening (A): the finite-strategy family is essentially a finite enumeration of the regimes, and the LP dual within each regime gives the matching weight certificate. This is a possible *rigor handle* for (A), not a standalone framing.

**Distance from pairing.** Moderate — the dual certificate IS a weighting (a generalization of "pairing"), but it is derived from LP duality rather than constructed combinatorially, and it handles barely-split regimes too.

## Confirmed dead-ends (do NOT pursue — same factor-of-2 wall as alternating-potential)

### (C) Measure / parity-integral control — DEAD (same wall)
The parity-integral `D = ∫[j(t) odd] dt` (already proved in dyadic-induction) does NOT yield a clean upper bound. Each Xiang cut inside a piece `p`, with smaller fragment `s ≤ p/2`, LIFTS `j(t)` by 1 on `(0, s]`, flipping parity there. To reduce `D`, parity on `(0,s]` must be odd. Total reduction ≤ Σ (smaller fragments) ≤ Σ p_i/2 = 1/2. With `D_Liu ≤ 1`, this gives `D ≥ 1/2`, far above `1/D_n ≈ 1/2^{n+1}`. This is exactly the alternating-potential factor-of-2 dead-end (round 1) restated in integral form. Confirmed numerically.

### (D) Probabilistic / Yao averaging with a single distribution — DEAD
Tested: Xiang picks n i.i.d. UNIFORM marks; `E[D]` over Xiang randomness. For n=1: `E[D]` ranges 0.25–0.56 across Liu configs (target 1/3 = 0.33); the worst Liu config (mark near endpoint) gives `E[D] ≈ 0.56 ≫ 1/3`. For n=2: `E[D]` ranges 0.22–0.42 (target 1/7 = 0.14). So NO single distribution works for all Liu (the value is Liu-dependent). A Liu-dependent distribution is just the primal restated. The minimax mixed strategy σ would need to be supported on the optimal-reply plateau of the dyadic config; no clean closed form found. Dead as a clean certificate.

### (E) Direct peeling-induction value recursion — DEAD (piece count does not close)
The recursion `1/c(n) = 1/c(n−1) + 2^{−n}` is arithmetically exact (proved, dyadic-induction Lemma 2). The natural proof: Xiang uses 1 mark to "peel" density `2^{−n}` and reduce to an `(n−1)`-game. But ONE Xiang mark SPLITS one piece into two, giving `n+2` pieces, not `n` — so the induction on "n" does NOT close on piece count. This is dyadic-induction's G2 wall (round 1), re-confirmed. The recursion identity is a SANITY CHECK, not a proof route, unless combined with a mechanism that merges pieces (none exists — Xiang can only cut).

### (F) Spectral / linear-algebraic — not concretely viable
`D = ⟨s, a⟩` with `s = (1,−1,1,…)`. Refinement is a piecewise-linear map with breakpoints at sort-ties. Formulable as a MILP, but the sort nonlinearity blocks a clean spectral certificate. No useful opening found.

## Cheap-kill candidates
- **The dyadic config is the UNIQUE worst case** (numerically: worst random n=2 config `D=0.139 < 1/7`; dyadic gives exactly `1/7`). Any upper-bound proof only needs to be TIGHT at dyadic and LOOSE elsewhere. This is a cheap structural fact: the outliner can exploit "slack everywhere except dyadic" to avoid tight casework on non-dyadic configs.
- **Per-strategy regime guard:** each barely-split strategy's D-formula holds in a stated regime (e.g. `p_j/2 ≥ p_k`); outside the regime the value only DECREASES (the sort change puts the barely-split piece at a *better* rank). If true, this collapses the regime tree — a one-line guard per strategy. CONJECTURE (probed on 20k n=2 configs: holds); needs proof.

## Knowledge-base entries to use
- *Extremal principle* / *Casework* (for the minimax-over-family + regime enumeration).
- *Invariants & monovariants* — NOT for a D-monovariant (that's the dead wall), but the *regime-invariant* form of each strategy's D-value.
- *Constructive vs existence* (the upper bound is "for every Liu, exhibit Xiang"; the family is the construction).
- *Pólya "solve a simpler case first"* — the n=1 two-strategy minimax (barely-split vs equal-split, crossover at `p_1=2/3`) is the template; generalizing the family is the route.

## Analogous past problems (cruxes)
- **aimo-0198 (IMO-SL 2012 C6, liar's game)** — crux: "bound a greedy minimizer's outcome by the average of its two available options, `min(A,B) ≤ (A+B)/2`, to get a clean recursive bound on the potential." The n=1 upper bound IS exactly this: `min(1−p_1, 2p_1−1) ≤ 1/3` maximized at the crossover. The general-n upper bound is the multi-option generalization: `min over family ≤ 1/D_n`. Analogous in the minimax-over-options structure, not in the domain. (The crux is a *hint to adapt* — re-prove from scratch.)
- **aimo-0117 (Dutch TST 2021, Jesse–Tjeerd stones)** — crux: "assign dyadic values so the single largest exceeds the sum of all others." This is the LOWER-bound mechanism (Liu's dyadic construction) already used. NOT an upper-bound analogue; listed only because it confirms the dyadic structure is the right witness for BOTH bounds.
- **aimo-0115 (domino pairing)** and **aimo-0461 (antipodal response)** — these are the PAIRING cruxes already cited by pairing-charging; NOT analogous to the genuinely-different framing (A). Do NOT cite for opening (A).
- No crux in the corpus is a clean analogue of the "min over a finite explicit-strategy family with regime-dependent values" framing. This is genuinely new territory; the outliner builds it from scratch.

## Prior progress
- Answer `c(n) = 2^n/(2^{n+1}−1)` conjectured + verified n=1..5 (round 1).
- Greedy-alternating lemma CERTIFIED (`lemmas/greedy-alternating.md`).
- D-reduction `S_odd ≤ 2^n/D_n ⟺ D ≤ 1/D_n` proved.
- n=1 both bounds fully proved (the two-strategy minimax is the template).
- Lower bound: dyadic construction + Case A (largest piece unsplit, all n) proved; G1-general (splits-inequality, n≥3) OPEN (shared wall).
- Upper bound G2-general (arbitrary Liu marks): WALL — pairing-charging built it only for n=1; this report identifies the barely-split strategies as a genuinely-different family to develop.

## Dead ends (do not retry)
- **Measure/parity-integral control for the upper bound** — factor-of-2 wall (each cut flips parity on interval ≤ p/2; total reduction ≤ 1/2 ≫ 1/D_n). Same as alternating-potential round-1 dead-end.
- **Uniform-random Yao averaging** — `E[D]` Liu-dependent and far above target for endpoint-ish configs.
- **Peeling-induction on n via the recursion identity** — piece count grows (`n+1 → n+2`), induction doesn't close.
- **Surrogate-adversary restricted strategies** — round-1 RETHINK; all non-pairing surrogates falsified n≥2.
- **Naive dyadic-decrement telescope** — caps `D ≤ 1/2^n`, factor-of-2 short.

## Small-case / intuition notes (labeled CONJECTURE)
- CONJECTURE: the dyadic config is the UNIQUE worst case for the upper bound (numerically, n=2: worst random D = 0.139 < 1/7 = dyadic). If true, the upper-bound proof need only be tight at dyadic; elsewhere slack is allowed.
- CONJECTURE: each barely-split strategy's D-formula, valid in a regime, gives a value that only DECREASES outside the regime (the rank reordering favors Xiang). Probed on 20k n=2 configs, holds. If true, the regime tree collapses to one formula per strategy.
- CONJECTURE: the family `{barely-split p_i + equal-halve p_j : i≠j} ∪ {equal-halve top n}` has minimax value exactly `1/D_n` over Liu. NOT yet verified for n≥3 (only n=2 probed, and even there the full family's coverage wasn't exhaustively checked — 3-member subset is insufficient; the full 6-member set for n=2 is the testable next step).

## Recommendation to the outliner
**Build ONE approach on framing (A): minimax over a finite explicit-strategy family (barely-split + equal-halve combinations), with pairing as one family member.** It is the only genuinely-different framing that survived probing. The concrete next steps for the builder:
1. For n=2, enumerate the full 6-member family (3 choices of barely-split piece × 2 choices of equal-halve piece, plus the all-equal-halve member) and verify `min ≤ 1/7` on a fine grid — this is the testable n=2 milestone.
2. Prove the per-strategy regime guard (formula holds in regime; value only decreases outside).
3. Generalize to n≥3: the family grows, but the dyadic tie-point (where multiple members coincide at `1/D_n`) is the structural anchor.
4. The LP-dual-within-regime (framing B) can supply the rigor certificate for each regime if the combinatorial formula stalls.

Failing (A), the field concedes the upper bound to pairing-charging (the round-1 leader) — but (A) is alive and worth one builder round.
