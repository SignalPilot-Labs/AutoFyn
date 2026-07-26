# proof-reviewer — Round 2 re-review

**Approach:** `gm-lipschitz-partition`  **Problem:** `imo-2026-05` (IMO 2026 P5)

## Verdict: APPROVE  —  Status: solved

The round-1 gap (Part B cover iteration was rightward-only, leaving `(0, x_0 − 2√(c x_0))` uncovered when `x_0 > 4c`) is **closed**. The builder replaced the cover iteration with the maximal-connected-component boundary-push argument. I independently re-derived the load-bearing step.

### Part B verification (the fixed gap)
- `(†)` global bound `g(y) ≤ (y−x_0)²/(4x_0)` from `(★)` at `x = x_0`: correct (verified symbolically).
- `(†_s)` at any fixed point `s`; zero-region `|y−s| < 2√(c s)` ⇒ `g(y) < c` ⇒ `g(y) = 0` (since `g : {0, c}`): correct.
- `S = {g=0}` is **open**: each `s ∈ S` centres an open interval inside `S`: correct.
- Component `I = (α, β)` containing `x_0`. `β ≥ x_0 + 2√(c x_0) > 0` so `β > 0`.
- **β = ∞**: if `β < ∞`, pick `s ∈ I` near `β⁻`. The interval around `s` is connected, contains `s ∈ I`, so lies in `I`; its right endpoint `s + 2√(cs) → β + 2√(cβ) > β` (strict, since `β > 0, c > 0`), placing points of `I` right of `β` — contradiction. Rigorous; continuity of `s ↦ s + 2√(cs)` explicitly invoked; strict inequality justified.
- **α = 0**: symmetric; `α > 0` would give `s − 2√(cs) → α − 2√(cα) < α`, contradicting `α = inf I`. Only remaining option is `α = 0` (since `S ⊆ ℝ₊`).
- Hence `I = (0, ∞)`, `g ≡ 0`, contradicting `c > 0`. **No uncovered interval; no hand-waving at the limits.**

### Part A (Fact 5) — still correct & self-contained
- Fact 5 `|g(z)−g(y)| ≤ (√f(z)−√f(y))²`: derived from RHS inequality at `x = f(z)` plus the iterate identity (1) and AM-GM identity `2(AM−GM) = (√a−√b)²`; symmetric swap gives the other side. Verified.
- Close-encounter application: with `ε = c_a/2`, hypothesis `ε ≥ δ_0` holds because `d = gcd(c_a, c_b) ≤ c_a` (since `d | c_a`), so `δ_0 ≤ d/2 ≤ c_a/2`. Collision sub-case = immediate contradiction.
- Fact 5 at the close encounter gives `δ = c_b − c_a ≤ (√f(z)−√f(y))² ≤ (ε+δ)²/(4 min(f(y),f(z))) ≤ (ε+δ)²/(4 t_k) → 0`. Contradiction. Bound `min(f(y),f(z)) ≥ min(y,z) = t_k` valid since `c_a, c_b > 0`.

### Other steps
- Step 0 (existence via AM-GM + QM-AM on `(x, f(y))`): sound.
- Steps 1–2 (iterate `f(f(y)) = 2f(y) − y`, orbit-AP, `g ≥ 0`, injectivity): sound; both LHS and RHS of (P) used at `x = f(y)` to pin equality.
- Step 6 synthesis: mixed `{0,c}` case excluded (fixed point ⇒ Part B ⇒ `g ≡ 0`, contradiction); `g ≡ 0` ⇒ `c = 0`; `g ≡ c > 0` ⇒ `f = x + c`. Both directions proven; final answer `f(x) = x + c, c ≥ 0` stated and verified.

### Theorems named & cited
AM-GM, QM-AM, Kronecker/Weyl equidistribution, Bézout, SOS/completing the square, functional-equations substitution, invariants/monovariants — all cited to `knowledge_base.md`. No skipped cases.

### Note on Status header
The builder's `## Status` still reads `partial`, but the proof is now complete and rigorous — this is an **underclaim**, not an overclaim. I record the true Status as **solved**.

## Lemma certification
The three promotable lemmas (Fact 5, iterate-orbit, close-encounter) were already certified into `results/imo-2026-05/lemmas/` in round 1; no new certification needed. Fact 5 (`fact-5-g-bound.md`) is `sorry`-free, statement no stronger than proved — passes the bar.
