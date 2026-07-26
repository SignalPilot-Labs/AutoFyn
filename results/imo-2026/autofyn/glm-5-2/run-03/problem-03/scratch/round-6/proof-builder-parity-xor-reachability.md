# Round-6 proof-builder report — parity-xor-reachability (NEW)

## Status: solved (lower bound G1 closed for all n, all sub-cases, uniformly)

## What was built

Created the new approach file `results/imo-2026-03/approaches/parity-xor-reachability.md` with a complete, rigorous proof of the G1 lower bound `D ≥ 1/D_n` for ALL `n ≥ 1` and ALL G1 sub-cases (i, ii, iii-a, iii-b) uniformly, via a single induction on `n`.

## The proof (engine: F_2 / XOR-measure, NOT measure inequality or alternating discrepancy)

**Setup (certified):** By the parity-XOR toggle lemma (`lemmas/parity-integral.md`), `D_final = |f_n ⊕ h|` where `f_n = [j_Liu_n odd]` and `h = XOR` of per-split toggles.

**Band structure:** `f_n = 1` on the largest band `B = (2^{n−1}, 2^n]` (where `j = 1`), and `f_n = (1 − f_{n−1})` on the lower half `L = [0, 2^{n−1}]` (since `j_Liu_n = j_Liu_{n−1} + 1` on `L`).

**Only `h_{2^n}` reaches `B`:** Toggles on `p ≤ 2^{n−1}` have support `⊆ [0, 2^{n−1}]`, so `h_rest = 0` on `B`.

**Induction on `n`:**
- Base `n = 0`: `|f_0| = 1`. ✓
- Step (`n ≥ 1`): decompose `h = h_{2^n} ⊕ h_rest`. Let `y = 2^{n−1} − v` (top shortfall).
  - **Case A (no toggle on `2^n`):** residual on `B` `= 2^{n−1} ≥ 1`. ✓
  - **Case B (EH, `y = 0`):** `D = 0 + |g| ≥ 1` by induction. ✓
  - **Case C1 (`y ≥ 1`):** `D ≥ y ≥ 1`. ✓
  - **Case C2 (`0 < y < 1`, the crux):** residual on `L` `= |g ⊕ 1_I|` where `g = f_{n−1} ⊕ h_rest`, `I = [2^{n−1}−y, 2^{n−1})` (length `y`). By the **XOR-measure reverse triangle inequality** `|g ⊕ 1_I| ≥ ||g| − |I|| = |g| − y ≥ 1 − y` (using `|g| ≥ 1 > y` by induction). So `D = y + |g ⊕ 1_I| ≥ y + (1 − y) = 1`. ✓

**Equality** at the equal-halving (EH) reply: `y = 0` at every level, bottoming at `|f_0| = 1`, giving `D = 1` exactly.

## How the crux was closed (the residual quantification)

The outline-reviewer flagged (step a): "the residual from a toggle's other interval is `L − 2|other interval ∩ (f=1 region)|`, NOT obviously `≥ L − (sum of smaller bands)` — the other interval could overlap `f=1` regions, REDUCING the residual."

**Resolution:** The F_2 induction does NOT recurse on "cover the largest uncovered band" (the superincreasing-prefix-forcing heuristic). Instead it recurses on the `(n−1)`-Liu-instance (via the complement-on-L identity `f_n = (1 − f_{n−1}) ⊕ 1_{[0, v)}` rewritten as `f_{n−1} ⊕ 1_I`). The reverse triangle inequality `|g ⊕ 1_I| ≥ ||g| − |I||` is a **universal** XOR-measure bound that needs NO overlap bookkeeping — it holds for ANY `g`, regardless of how `h_rest` overlaps `f=1` regions. The "other interval could overlap" worry is moot.

## Verified numerics (exact-rational, `fractions`, all scripts < 30s)

- f-band structure superincreasing n=1..6. ✓
- Tight case (EH on all pieces) D=1 for n=2,3,4,5. ✓
- Case C2 min D = 1 + 2y > 1 for n=3,4,5 (y=1/2→2, y=1/4→1.5, y=1/8→1.25, y=1/16→1.125). ✓
- (n−1)-induction: min |f_2 ⊕ h_rest| = 1 over ≤ 2 toggles. ✓

## Collapse-to-union-bound check: PASSED

The F_2 framing operates on the raw `f_n`, `h` toggle-algebra (decomposed by toggle: `h_{2^n}` vs `h_rest`), agnostic to the `R_0`/`F` piece-origin decomposition that Lemma 7 requires. It applies to ALL G1 sub-cases (i, ii, iii-a, iii-b) without re-derivation, while Lemma 7 is G1-i-HC-specific. The framing is genuinely different from dyadic-induction (Boolean/XOR-measure vs real-valued alternating-discrepancy inequality).

## Genuinely different from dyadic-induction

- dyadic-induction: `Alt_s = Σ(−1)^{i+1} G(f_i)` — real-valued alternating-discrepancy at F's breakpoints against `E_R_0`'s bands. G1-i-HC-specific. General `s ≥ 3` CONJECTURED, not proved.
- parity-xor-reachability: `|f_n ⊕ h| ≥ 1` — Boolean/XOR-measure on the raw toggle algebra. Uniform across all sub-cases. PROVED for all n.

## What this closes

- **G1 lower bound `D ≥ 1/D_n` for ALL n, ALL sub-cases (i, ii, iii-a, iii-b)** — including G1-iii-b (flat), which resisted every prior mechanism (peeling-pair unsound, continuity provenance-switch, discrepancy G1-i-HC-specific).
- The lower bound side of the answer `c(n) = 2^n/(2^{n+1}−1)` is PROVED for all n.
- For n ≤ 3, both bounds are PROVED (lower here, upper by `case-c-n3.md` / `pairing-charging` / `dyadic-induction` §5.1), so `c(1) = 2/3, c(2) = 4/7, c(3) = 8/15` are ESTABLISHED.

## What remains open

- **G2 upper bound for n ≥ 4** (Xiang's strategy for arbitrary Liu marks). Governed by pairing-charging's `f_n` recursive-functional conjecture (verified n=3,4; n≥5 open). This approach does NOT address G2 — it is a lower-bound framing.

## Promotable lemmas (proposed for certification)

1. **G1 (splits-inequality, F_2 form) — FULL, all n, all sub-cases.** Should replace the PARTIAL `lemmas/splits-inequality.md` with a complete proof.
2. **XOR-measure reverse triangle inequality** (`|g ⊕ q| ≥ ||g| − |q||`).
3. **Complement-on-L identity** (`f_n = (1 − f_{n−1})` on `[0, 2^{n−1}]`).

## Files touched

- `/home/agentuser/repo/results/imo-2026-03/approaches/parity-xor-reachability.md` (CREATED — full proof).
- `/tmp/round-6/proof-builder-parity-xor-reachability.md` (this report).
