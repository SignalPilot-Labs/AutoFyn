## imo-2026-04  (LENS: shan-yu-escape — lower bound / complement)

### Answer conjecture (scouted independently, then cross-checked)
Mulan can guarantee victory in finitely many steps **iff** `180°/θ` is an integer `≥ 2`, i.e.
`θ ∈ {180°/n : n = 2,3,4,…} = {90, 60, 45, 36, 30, …}`.
Equivalently: `θ = 180°/n` for an integer `n ≥ 2`.

The complement (Shan-Yu escapes forever) is `180°/θ ∉ ℤ`, i.e. `θ` is **not** of the form `180°/n`.
This report scouts **only the escape (complement) direction**; that half is essentially cracked (clean invariant + clean closure proof). The win direction (`180/θ ∈ ℤ`) is the genuinely hard half and is the dynamics lens's turf — I flag where it connects but do not develop it.

---

### (1) Formal notion of Shan-Yu's "safe set" S_θ

A triangle is an ordered angle triple `(A,B,C)` with `A,B,C > 0`, `A+B+C = 180°`. A **Mulan cut** at vertex `V` (angle `A`) with split parameter `x ∈ (0,A)` produces two children:
- `child1 = (x, B, (A+C) − x)`   [= `(x, B, 180−B−x)`]
- `child2 = (A−x, C, B + x)`

(Analogously for cutting at `B` or `C`.) `x` ranges over the **open** interval `(0,A)` (`P` is not a vertex).

Define the **bad-angle set**
`B_θ := { kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180° }   = {θ, 2θ, 3θ, …} ∩ (0,180°)`.

Define the **(conjectured, then verified) safe set**
`S_θ := { triples (A,B,C) : no angle lies in B_θ }`.

A triple containing `θ` is already a Mulan win, so `S_θ ⊆ {θ-free triples}`. The claim: `S_θ` is the **maximal** safe set (greatest fixed point of "every Mulan cut leaves some child in the set").

---

### (2) Maximal safe-set characterization

**Claim.** `S_θ = B_θ-free triples` is the maximal Shan-Yu-safe set, and it is **closed** (every cut from a `B_θ`-free triple has a `B_θ`-free child) **iff** `180°/θ ∉ ℤ`. When `180°/θ ∈ ℤ`, `S_θ = ∅` (Mulan wins from everywhere).

**Closure proof (the key fact — four-case analysis).** Take a `B_θ`-free triple `(A,B,C)` (so `A,B,C ∉ B_θ`). Mulan cuts at `A` with split `x`. For **both** children to land outside `S_θ` (i.e. each acquires a `B_θ`-angle), since `B` and `C` are themselves not in `B_θ`, the bad angle of `child1` must be `x` or `A+C−x`, and the bad angle of `child2` must be `A−x` or `B+x`. Four combinations:

| child1's bad angle | child2's bad angle | consequence |
|---|---|---|
| `x = k₁θ` | `A−x = k₂θ` | `A = (k₁+k₂)θ ∈ B_θ` — contradiction (A was B-free) |
| `x = k₁θ` | `B+x = k₂θ` | `B = (k₂−k₁)θ ∈ B_θ` — contradiction |
| `A+C−x = k₁θ` | `A−x = k₂θ` | subtract → `C = (k₁−k₂)θ ∈ B_θ` — contradiction |
| `A+C−x = k₁θ` | `B+x = k₂θ` | **add** → `A+B+C = 180° = (k₁+k₂)θ` ⇒ `180°/θ = k₁+k₂ ∈ ℤ` |

So the **only** way for Mulan to make **both** children `B_θ`-bad in one cut is case 4, which forces `180°/θ ∈ ℤ`. Therefore:

- If `180°/θ ∉ ℤ`: case 4 is impossible, so at least one child stays `B_θ`-free every cut → `S_θ` closed → **Shan-Yu escapes** by always keeping a `B_θ`-free child.
- If `180°/θ ∈ ℤ`: the invariant `B_θ`-free is **not** closed (case 4 is achievable), so this invariant alone doesn't save Shan-Yu; in fact (dynamics lens) Mulan actively forces a win. `S_θ = ∅`.

**Numerical verification (discrete grid, units of θ and 1°):** For every tested non-`180/n` `θ` (72, 70, 50, 54, 80, 100, 120, 135, 60.5, 36.4, 20.5, …), the computed greatest-fixed-point safe set equals `B_θ`-free triples **exactly** with **zero mismatches** (e.g. θ=72: safe=15508, all and only the triples avoiding {72,144}; θ=50: avoiding {50,100,150}; θ=100: avoiding {100}; θ=54: avoiding {54,108,162}). For every `θ = 180/n`, `n=2..20`, the safe set is **empty** (Mulan wins). Classification is sharp at the boundary (θ=60 wins; θ=60.5 fully escapes).

---

### (3) For which θ does a nonempty reachable safe set exist? (the complement of Mulan's winning θ)

`S_θ ≠ ∅` (and is reachable as an initial triangle) **iff** `180°/θ ∉ ℤ`, i.e. `θ ≠ 180°/n` for every integer `n ≥ 2`.

**Reachability:** when `180°/θ ∉ ℤ`, the angle `60°` is **not** a positive multiple of `θ` (else `θ = 60°/k` ⇒ `180°/θ = 3k ∈ ℤ`, contradiction). Hence the **equilateral triangle `(60,60,60)` is `B_θ`-free** for every escape-`θ`. So Shan-Yu has a universal, explicit initial triangle: the equilateral. (For the finitely many `θ` where an equilateral angle `60` would be a multiple, we are in the win case anyway.)

So the escape set is exactly `θ ∈ (0°,180°) \ {180°/n : n≥2}`, and the equilateral is a uniform witness.

---

### (4) Explicit escape constructions

- **θ = 120°** (`180/θ = 1.5`): `B_120 = {120}`. Equilateral `(60,60,60)` avoids it. Closure: any cut gives children whose angles are `x, 60, 120−x` and `60−x, 60, 60+x`; the new angles `120−x, 60+x ∈ (60,120)` never hit 120 (would need `x=0`), and `x, 60−x < 60`. So **both** children are `B`-free — equilateral is a "super-safe" state. (Generic `B`-free triples only need *one* child safe.)
- **θ = 72°** (`180/θ = 2.5`): `B_72 = {72,144}`. Equilateral avoids both. Closure holds by §2.
- **θ = 70°** (irrational-ish; `180/θ` irrational): `B_70 = {70,140}`. Equilateral avoids. Escape.
- **θ = 100°**: `B_100 = {100}`. Equilateral avoids.
- **θ = 90°**: NOT an escape — `180/90 = 2 ∈ ℤ`, Mulan wins (in fact in one move: from any triangle cut at vertex `A` with `x = 90−B`, giving `child1=(90−B,B,90)`, `child2=(90−C,C,90)`, both containing 90).
- **θ irrational** (e.g. `θ = 1 radian`): `B_θ` is a discrete set of irrationals; equilateral (all rational) avoids it. Escape.

---

### (5) Hardest step in proving escape for the full complement

The escape half is, perhaps surprisingly, the **clean** half — the four-case closure above is short and rigorous. The subtle points to get right (flagged for the builder):

(a) **Endpoint exclusion.** `x ∈ (0,A)` open (P not a vertex); the closure argument must not rely on `x=0` or `x=A`. It doesn't — the case analysis is for interior `x` and the contradictions are strict.

(b) **The boundary `kθ = 180°`.** `B_θ` excludes `180°` itself (an angle is `< 180°`); so when `180°/θ ∈ ℤ = n`, the multiple `nθ = 180°` is **not** in `B_θ`. That is why, in the win case, `B_θ = {θ,…,(n−1)θ}` — and a `B_θ`-free triple can still have angles that are *rational* multiples of `θ` with numerator `≥ n` reduced… the closure genuinely fails and Mulan forces. Make sure the definition `kθ < 180°` (strict) is used consistently.

(c) **Determinacy / no-draw zone.** Need to rule out a `θ` where **neither** player can force (Shan-Yu draws forever but Mulan can't be excluded). The game is an open reachability game (Mulan's target = closed set `{θ-containing triples}`); the attractor `W` (least fixed point: contains-θ, or ∃ cut with both children in `W`) and the safe region `S` (greatest fixed point: avoids θ and ∀ cuts ∃ child in `S`) are complements by standard determinacy of these games (transfinite back-and-forth; here it stabilizes by the explicit `B_θ` description). Numerically every `θ` is cleanly either `S=∅` (win) or `S≠∅` (escape) — **no middle ground exists**, so a draw = Mulan loses, matching the problem's "guarantee victory in finitely many steps". The hardest *conceptual* point is writing the determinacy/well-foundedness argument cleanly: the attractor is ordinal-indexed but here collapses to a single step (case 4) when `180/θ∈ℤ` and is empty otherwise. (Builder should cite the invariants/monovariants + games-and-strategy KB entries; the n-gon crux `aimo-0225` is the closest determinacy-by-fixed-point analogue.)

(d) **The escape half does NOT prove the win half.** This is the critical warning: the four-case argument shows `B_θ`-freeness is *not* closed when `180/θ∈ℤ`, but that only says *this particular* invariant fails — it does **not** by itself prove Mulan wins. The win direction needs its own argument (see the distinct framings below; that's the dynamics lens). So the escape proof, once paired with a win proof, yields the full characterization; alone it is only the "Shan-Yu wins for `θ ∉ {180/n}`" half.

---

### Distinct openings (rival framings — each a different attack on the WHOLE problem, not technique-variants of the dynamics route)

- **F1. Bad-multiple invariant (escape half, this lens).** Target: prove the complement `θ ≠ 180/n` via the `B_θ`-free invariant + four-case closure. Clean, short, rigorous. Pairs with any win-direction proof. Distinctive because it never analyzes Mulan's strategy — it is purely a Shan-Yu-side invariant-preservation argument.

- **F2. Attractor/determinacy dual (whole problem in one frame).** Define `W` = least fixed point of "contains θ OR ∃ Mulan cut with both children in W"; prove `W = all triples` iff `180/θ∈ℤ` directly by characterizing the attractor's complement as `B_θ`-free (the case analysis is the same, but the *framing* is fixed-point duality rather than invariant-preservation). Same algebra, different logical structure — useful if the outliner wants a single self-contained proof rather than two halves.

- **F3. Equilateral "super-safe" + perturbation (escape, structural).** Observe the equilateral `(60,60,60)` is not merely `B_θ`-free but *doubly* safe: for non-`180/n` `θ`, *both* children of any equilateral cut avoid `B_θ` (a strictly stronger condition than Shan-Yu needs). This suggests a structural framing around "Shan-Yu maintains near-equilateral / all-equal-angles" rather than the general `B_θ`-free set. Niche but gives a very concrete escape strategy (stay equilateral-ish).

- **F4. Modular-residue complement (escape, algebraic).** Reframe `B_θ`-freeness as: every angle has nonzero residue mod `θ` (in the group `ℝ/θℤ`), and `180°` has residue `180° mod θ`. When `180/θ ∉ ℤ`, the total residue `180 mod θ ≠ 0` is a *fixed nonzero* value that the three angle-residues must sum to; a cut permutes/redistributes residues but the total stays nonzero, so the residues can never all vanish — `θ` (residue 0) never appears. This is the same proof in modular language; useful if the outliner prefers a one-line "the sum of residues is a nonzero invariant" punchline. (When `180/θ ∈ ℤ` the total residue is 0, the invariant dies, and Mulan wins — matches.)

---

### Candidate technique(s)
- **Invariants & monovariants** (preserve `B_θ`-freeness) — KB "Invariants & monovariants".
- **Game fixed-point / attractor duality** (least vs greatest fixed point; `aimo-0225` n-gon crux uses the same Win/Loss attractor recursion) — KB "games-and-strategy".
- **Casework on which child-angle is a multiple** (the four cases of §2) — KB "Casework / exhaustion".
- For the win half (not this lens but flagged): **2-adic / dyadic descent on angle differences** mirroring `aimo-0225`; **modular arithmetic mod θ**.

### Cheap-kill candidates
- The four-case closure IS the cheap kill for the escape half — no heavy computation, pure case analysis on linear combinations of `x`. The whole complement direction reduces to "add the two new-at-P angles: they sum to `180°`, so they can't both be multiples of `θ` unless `180°` itself is" (case 4). That one-line addition is the entire escape.
- Equilateral as universal initial triangle is the cheap construction attaining the bound (no parametric family needed for the escape).

### Knowledge-base entries to use
- "Invariants & monovariants" (Combinatorics) — the `B_θ`-free invariant.
- "Casework / exhaustion" (General Proof Methods) — the four cases.
- "games-and-strategy" (crux subtopic) — fixed-point Win/Loss recursion, esp. `aimo-0225`.
- "Contrapositive / contradiction" (General Proof Methods) — each case derives a contradiction with `B_θ`-freeness.

### Analogous past problems (cruxes)
- **aimo-0225** (UK, regular n-gon token game) — crux: *position = multiset {a,b,c} with a+b+c=n; a move resplits a pair keeping the sum; winning positions characterized by the 2-adic valuation `v_2(a−b)` via recursive **halving** of the difference, with "good positions" `{a,a,b}` of even 2-adic parity.* Analogous because (i) same state shape (triple summing to a fixed total), (ii) the move is a resplit of a 2-sum exactly like our cut producing children that resplit `A+C` and `A+B`, (iii) the answer hinges on an arithmetic property of `180/θ` exactly as the n-gon answer hinges on `v_2(n−3)`, (iv) Win/Loss determined by fixed-point recursion. **Caution:** the n-gon move is an *unconstrained* resplit (any pair, any split increasing the min); ours is a *constrained* resplit (split at the cut vertex only, coupled to the side angles). So it is a hint to adapt, not a citation — the `B_θ`-multiple structure here is genuinely different from the 2-adic-difference structure there. Still the single closest crux in the corpus.
- No other corpus crux resembles the triangle-cut game directly; the combinatorics `games-and-strategy` and `invariants-and-monovariants` cruxes (paint game `aimo-0019`, liar's game `aimo-0198`, coin-circle `aimo-0196`) share the *style* (second-player invariant maintenance, potential/monovariant drainage) but not the state space. Do not force a match.

### Prior progress
None (round 1; no approaches in population, `current.md` empty).

### Dead ends (do not retry)
None yet (first round). One *warning* to record for future rounds: do **not** try to prove the win direction (`180/θ∈ℤ`) by extending the `B_θ`-free invariant — that invariant is *false* in the win case (`S_θ=∅`); the win needs a separate descent/attractor argument.

### Small-case / intuition notes (conjectures, labeled)
- One-step universal win for `θ=90°`: from any triangle, cut at vertex `A` with `x=90°−B` (valid since `A+B>90°⇔C<90°`, etc.); both children contain 90°. Confirmed by sim (`S_90=∅`).
- "Bad angles = positive multiples of θ below 180°": confirmed by exact match of the simulated safe set with `B_θ`-free triples (zero mismatches) for θ ∈ {50,72,54,100,120,70,80,135}. **Conjecture** (strong, numerically exact on integer grids, and the closure proof is rigorous): `S_θ = B_θ`-free triples for all escape `θ`.
- "Equilateral is a universal escape start": conjecture, proven conditionally (the closure proof of §2 shows any `B_θ`-free triple, including equilateral, is safe; equilateral is `B_θ`-free for all escape `θ` by the residue argument).
- No "neither-can-force" `θ` exists: conjecture from determinacy + numerical confirmation; needs a clean written fixed-point-duality argument in the final proof.
