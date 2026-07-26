# proof-reviewer — IMO 2026 P5 (round 1)

Adversarial review of both built proofs. Every load-bearing step was re-derived independently (sympy + numerical tests). Verdicts below.

---

## `orbit-close-encounter` — APPROVE (Status: solved)

**Headline.** The proof is complete and rigorous. The maximal-component argument for Part (B) is the correct repair of the outline-reviewer's flagged `3+2√2` flaw, and it closes Part (B) cleanly in both directions. All load-bearing steps verified.

### Step-by-step verification

**Step 0 (existence).** `f(x)=x+c` makes the middle term `AM(x, f(y))`, the RHS `GM(x, f(y))`, the LHS `QM(x, f(y))`; the chain is QM-AM + AM-GM (knowledge_base.md, *Standard inequalities*). Verified by sympy: both gaps are perfect squares and vanish at `x = f(y)`.
- *Minor cosmetic error (non-fatal):* the stated gap `QM² − AM² = (f(y)−x)²/2` is wrong by a factor of 2; the correct identity is `QM² − AM² = (f(y)−x)²/4` (verified: `QM²−AM² = (x²+f(y)²)/2 − (x+f(y))²/4 = (x−f(y))²/4`). The inequality `QM ≥ AM` still holds; existence is unaffected.

**Step 1 (equality-forcing preamble).** Setting `x = f(y)`: LHS collapses to `√((f(y)²+f(y)²)/2) = f(y)`, RHS collapses to `√(f(y)·f(y)) = f(y)`. The middle `(f(f(y))+y)/2` is sandwiched: `f(y) ≥ middle ≥ f(y)`, forcing `middle = f(y)`, i.e. `f(f(y)) = 2f(y) − y`. **Sandwich logic verified** — both outer bounds equal `f(y)`, so both inner inequalities are simultaneously tight. Rigorous.
- `g∘f = g`, orbits are APs `fⁿ(y) = y + n·g(y)`: verified by induction.
- `g ≥ 0`: if `g(y) < 0` then `fⁿ(y) = y + n·g(y) → −∞`, so `fⁿ(y) ≤ 0` for large `n`, contradicting `f: ℝ₊ → ℝ₊`. The forward orbit cannot "terminate" — `f` is defined on all of `ℝ₊` and maps to `ℝ₊`, so `fⁿ(y) > 0` for all `n`. **Verified.**
- Injectivity: `f(a)=f(b) ⇒ f(f(a))=f(f(b)) ⇒ 2f(a)−a = 2f(b)−b ⇒ a = b`. **Verified.**

**Step 2 (two-point constraints).** `(f(x)+y)² − 4x·f(y) = (x−y)² + 2(x+y)g(x) + g(x)² − 4x·g(y)` — **verified by sympy** (exact match). Within a level set `g(x)=g(y)=c`: reduces to `(x−y−c)² ≥ 0` (tautology). **Verified.**
- *Minor inaccuracy (non-fatal, unused):* the parenthetical "(star star) gives `4y·c_a ≤ … + 4y·c_b`, trivially true since `c_a < c_b`" has a glib justification. The claim itself is TRUE: minimizing (star star) − LHS over `x` gives minimum `4y(c_b − c_a) ≥ 0` (verified by sympy). But (star star) is not used in the proof, so this is cosmetic.

**Step 3 (Part A — at most one positive value).** This is the load-bearing step. Verified each sub-case:
- *Close-encounter lemma.* Irrational `p/q`: Kronecker/Weyl equidistribution (knowledge_base.md) gives `|A_n − B_m| ≤ ε` at arbitrarily large `A_n, B_m`. **Verified numerically** (`p=1, q=√2`: encounters within `0.0001` at `A_n ≈ 3643`). Rational `p/q = P/Q` (coprime, `d = p/P = q/Q`): same residue class mod `d` ⇒ Bézout gives collision; distinct residues ⇒ `δ₀ = min_k |a−b+kd| ≤ d/2 ≤ p/2` achieved periodically at unbounded `A_n, B_m`. **Verified numerically** (`p=4, q=6, d=2`: `δ₀ = 0.8 ≤ d/2 = 1 ≤ p/2 = 2`; same-residue case: collision at `n=2, m=1`). The `d ≤ c_a` step (since `d = gcd(c_a, c_b) | c_a`) is correct.
- *Collision sub-case.* Common point on both orbits ⇒ `g` takes both `c_a` and `c_b` there ⇒ contradiction. Genuine contradiction (not "same orbit"): even if `O_a = O_b`, `g` would take two values on it. **Verified.**
- *Close-encounter → (star) contradiction.* Plugging `x = x_k ∈ L_{c_a}`, `y = y_k ∈ L_{c_b}` into (star): `4x_k·c_b ≤ (x_k−y_k)² + 2(x_k+y_k)c_a + c_a²`. With `|x_k−y_k| ≤ c_a/2` and `y_k ≤ x_k + c_a/2`: RHS ≤ `c_a²/4 + 4x_k·c_a + c_a² + c_a² = 4x_k·c_a + (9/4)c_a²`. So `4x_k(c_b−c_a) ≤ (9/4)c_a²`, giving `x_k ≤ 9c_a²/(16(c_b−c_a))`. **Verified by sympy** (the `9/4` coefficient is exact). This uniform bound contradicts `x_k → ∞`. Orientation correct: smaller `c_a` in `g(x)` slot, larger `c_b` in `g(y)` slot. **Verified.**

**Step 4 (Part B — fixed point forces `g ≡ 0`).** The maximal-component argument — this is the key repair.
- *(dagger)*: `(star)` at `x = x_0` (with `g(x_0)=0`): `4x_0·g(y) ≤ (x_0−y)²`, i.e. `g(y) ≤ (y−x_0)²/(4x_0)`. **Verified** (correct specialization).
- *Zero-region radius `2√(cs)`:* if `|y−s| < 2√(cs)` then `(y−s)²/(4s) < c`, so `g(y) < c`, so `g(y) = 0` (by Part A). **Verified.** So `S = {g=0}` is open.
- *Maximal-component argument.* Let `I = (α, β)` be the connected component of `S` containing `x_0`. **This is the crux.** The argument shows `α = 0` and `β = ∞`:
  - `β = ∞`: if `β < ∞`, pick `s ∈ I` near `β`. The interval `(s−2√(cs), s+2√(cs)) ∩ ℝ₊ ⊆ S` is connected, contains `s ∈ I`, hence ⊆ `I`. But `s+2√(cs) → β+2√(cβ) > β` (since `β ≥ x_0+2√(cx_0) > 0`), so points of `I` lie right of `β` — contradiction. **Verified.**
  - `α = 0`: symmetric. If `α > 0`, pick `s ∈ I` near `α`. The interval extends to `s−2√(cs) → α−2√(cα) < α` (since `α > 0, c > 0`), placing points of `I` left of `α` — contradiction. **Verified.**
  - So `I = (0, ∞)`, hence `S = ℝ₊`, hence `g ≡ 0`. **Verified numerically** (simulation with `c=1, x_0=10 > 4c`: boundary-push drives `α → 0` and `β → ∞` in ~5 steps).
- **No hidden continuity/connectedness assumption.** The zero-SET `S` is open (proved), so its connected components are open intervals. The argument works on the single component `I` containing `x_0` and shows `I = (0, ∞)`. Once `I = (0, ∞)`, there is no room for other components (`S ⊆ ℝ₊ = I`), so `S = ℝ₊`. The argument does NOT need to show every component is unbounded — only that the component containing `x_0` is all of `ℝ₊`. **No gap.**

**Step 5 (synthesis).** Two cases: `g` takes no positive value ⇒ `g ≡ 0` (by `g ≥ 0`); `g` takes one positive value `c > 0` ⇒ if a fixed point existed, Step 4 forces `g ≡ 0` (contradiction), so no fixed point exists, so `g(x) = c` for all `x`. Both give `f(x) = x+c`, `c ≥ 0`. The mixed `{0, c}` case is excluded by Step 4. The `g ≡ c > 0` (no fixed point) case is handled. **No missing case.**

### Scores
- **Correctness:** 9/10 (two minor cosmetic errors in Steps 0, 2; neither load-bearing).
- **Completeness/rigor:** 10/10 (every case settled, every theorem named, no hand-waving in load-bearing steps).
- **Progress:** solved (complete proof from scratch).

### Verdict: **APPROVE** (Status: solved).

---

## `gm-lipschitz-partition` — CHANGES REQUESTED (Status: partial)

**Headline.** Fact 5 is a genuine, correctly-proven instrument. Part (A) via Fact 5 + close-encounter is correct and is a real alternative to the direct (star) route. But **Part (B) has a real gap**: the cover iteration only goes rightward and incorrectly replaces the zero-region `Z(x_k) = (x_k − 2√(c·x_k), x_k + 2√(c·x_k)) ∩ ℝ₊` with `(0, x_k + 2√(c·x_k))`, which is wrong when `x_k > 4c`. The conclusion `g ≡ 0` does not follow from the argument as written.

### Step-by-step verification

**Steps 0–2 (existence, iterate, orbit, `g ≥ 0`, injectivity).** Identical to `orbit-close-encounter` and correct. **Verified.**

**Step 3 (Fact 5).** `|g(z) − g(y)| ≤ (√f(z) − √f(y))²`. Proven by substituting `x = f(z)` into the RHS of (P), using `f(f(z)) = f(z) + g(z)` and `y = f(y) − g(y)`, reducing to `AM(f(z),f(y)) + (g(z)−g(y))/2 ≥ GM(f(z),f(y))`, then `(g(z)−g(y))/2 ≥ −(AM−GM) = −(√f(z)−√f(y))²/2`. Swapping `y ↔ z` gives the other side. **Verified by sympy** (AM−GM identity exact). Fact 5 is correct and promotable.

**Step 4 (Part A via Fact 5 + close-encounter).** Correct.
- Close-encounter lemma: same as orbit builder's, with the `d ≤ c_a` step. **Verified.**
- At a close encounter: `c_b − c_a = |g(z)−g(y)| ≤ (√f(z)−√f(y))²`. Bound: `|f(z)−f(y)| ≤ |z−y| + (c_b−c_a) ≤ ε + δ`; `(√f(z)−√f(y))² ≤ (ε+δ)²/(4·min(f(y),f(z))) ≤ (ε+δ)²/(4·t_k) → 0`. But `δ = c_b−c_a > 0` is fixed. **Contradiction. Verified** (the `min(f(y),f(z)) ≥ min(y,z) = t_k → ∞` step is correct since `c_a, c_b ≥ 0`).

**Step 5 (Part B — cover iteration). REAL GAP.**
- *(dagger)* and zero-region `Z(x_0) = (x_0 − 2√(cx_0), x_0 + 2√(cx_0)) ∩ ℝ₊`: **correct** (same as orbit builder).
- *Cover iteration:* `x_{k+1} = x_k + √(c·x_k)`, each `x_k` a fixed point, `x_k → ∞`. **Correct.**
- *The error (line: "the zero-region `(0, x_k + 2√(c·x_k))` (left endpoint clamped at `0` from the first step onward)").* The zero-region around `x_k` is `Z(x_k) = (x_k − 2√(c·x_k), x_k + 2√(c·x_k)) ∩ ℝ₊`, NOT `(0, x_k + 2√(c·x_k))`. These coincide only when `x_k − 2√(c·x_k) ≤ 0`, i.e. `x_k ≤ 4c`. When `x_0 > 4c` (which is a priori possible — no constraint forces `x_0 ≤ 4c`), `Z(x_0) = (x_0 − 2√(cx_0), x_0 + 2√(cx_0))` with positive left endpoint, and the rightward-only iteration leaves `(0, x_0 − 2√(cx_0))` UNCOVERED.
- *The false claim (line: "For every `Y > 0` choose `k` with `x_k + 2√(c·x_k) > Y`; then `Y ∈ Z(x_k)`").* `Y < x_k + 2√(c·x_k)` does NOT imply `Y ∈ Z(x_k)` — one also needs `Y > x_k − 2√(c·x_k)`. For `x_0 > 4c` and `Y < x_0 − 2√(cx_0)`, since `x ↦ x − 2√(cx)` is increasing for `x > c`, all `x_k ≥ x_0` satisfy `x_k − 2√(cx_k) ≥ x_0 − 2√(cx_0) > Y`, so `Y ∉ Z(x_k)` for every `k`. **Verified numerically** (`c=1, x_0=10 > 4c=4`: after 30 rightward steps, cumulative left endpoint stuck at `3.675`; interval `(0, 3.675)` uncovered).
- *Conclusion:* the proof that `g ≡ 0` on all of `ℝ₊` is INCOMPLETE. The rightward cover only gives `g = 0` on `(x_0 − 2√(cx_0), ∞)` when `x_0 > 4c`.

**The gap is fixable** (not a dead end): either (i) also iterate leftward (`x_{-(k+1)} = x_{-k} − √(c·x_{-k})`, reaching a fixed point `≤ 4c` in finitely many steps, whose zero-region extends to `0`), or (ii) replace the cover iteration with the orbit builder's maximal-component argument (which pushes both `α → 0` and `β → ∞` and works for all `x_0`). But the proof AS WRITTEN is incomplete.

**Step 6 (synthesis).** Correct assuming Parts (A) and (B). The mixed `{0, c}` case is excluded by Part (B) (once Part (B) is fixed).

### Scores
- **Correctness:** 7/10 (Parts A, Fact 5, existence all correct; Part B has a logical error in the cover claim).
- **Completeness/rigor:** 6/10 (Part B gap — the conclusion `g ≡ 0` is not established for `x_0 > 4c`).
- **Progress:** substantial (Fact 5 is a new instrument; Part A via Fact 5 is a genuine alternative).

### Verdict: **CHANGES REQUESTED** (Status: partial).
**Gap to close:** Part (B), Step 5 — the cover iteration must also cover the leftward direction `(0, x_0 − 2√(cx_0))` when `x_0 > 4c`. Either add a leftward iteration (`x_{-(k+1)} = x_{-k} − √(c·x_{-k})` until reaching a fixed point `≤ 4c`) or replace with the maximal-component argument from `orbit-close-encounter`.

---

## Lemma certification

**Promoted (from `orbit-close-encounter`):**
1. `iterate-and-orbit`: `f(f(y)) = 2f(y)−y`; `g∘f = g`; `fⁿ(y) = y + n·g(y)`; `g ≥ 0`; `f` injective. **Certified** (Step 1, sorry-free, statement correct).
2. `two-point-g-constraint`: (star) `4x·g(y) ≤ (x−y)² + 2(x+y)g(x) + g(x)²`; (star star) the swap; level-set tautology `(x−y−c)² ≥ 0`. **Certified** (Step 2).
3. `fixed-point-zero-region`: (dagger) `g(y) ≤ (y−x_0)²/(4x_0)`; zero-region radius `2√(cs)`; maximal-component argument forces `g ≡ 0`. **Certified** (Step 4 — the maximal-component argument is the correct, complete version).

**Promoted (from `gm-lipschitz-partition`):**
4. `fact-5-g-bound`: `|g(z)−g(y)| ≤ (√f(z)−√f(y))²`. **Certified** (Step 3, sorry-free, statement correct and no stronger than proved).
5. `close-encounter-lemma`: two unbounded forward APs have arbitrarily large `ε`-close encounters (Kronecker for irrational ratio, Bézout for rational). **Certified** (Step 4).

**Rejected:** none.

---

## Recorded outcomes

- `orbit-close-encounter`: **verified-milestone** (solved — complete rigorous proof, all steps verified).
- `gm-lipschitz-partition`: **partial** (Fact 5 + Part A correct; Part B cover-iteration gap when `x_0 > 4c`).
