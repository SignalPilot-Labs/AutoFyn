# Build report — remainder-forcing — round 2 — imo-2026-04

## What I built

Full proof written into `results/imo-2026-04/approaches/remainder-forcing.md`. **Status: solved** (both directions, every gap G0–G6 closed, answer stated and verified).

- **G0 (Cut Lemma):** realizability of every t ∈ (0, a) via IVT on the continuous angle function f(s) = ∠BAP(s) (no monotonicity needed — f(0) = 0 < t < a = f(1) already forces an interior s*); piece-angle formula derived from angle-sum + collinearity (∠ABP = b since ray BP = ray BC; supplementary P-angles); angle additivity ∠BAP + ∠PAC = a proved by an explicit convex-sector argument (positive combination of linearly independent u, v lies strictly inside the sector). Relabeling remark (B ↔ C ⟺ t ↔ a − t) included per reviewer note 3, plus the converse ("every legal move is of this labeled form").
- **G1 (Descent Lemma):** strong induction on m, t = θ valid since m ≥ 2 ⟹ θ < mθ; kept-piece analysis for both of Shan-Yu's choices; the top-of-iteration check handled in both base and inductive step; bound m − 1 telescopes.
- **G2 (Forcing Lemma):** general mechanism t = θ − r_b (residues in (0, θ) by safety + R1), both P-side angles ≡ 0 mod θ and positive hence positive multiples; validity split n ≥ 3 (largest angle ≥ 60° ≥ θ) vs n = 2 (θ = 90°): obtuse and acute sub-cases fully written (acute uses a + b = 180° − c ≥ 120° > 90°), exhaustiveness of the sub-cases argued (safe at n = 2 ⟺ no right angle; at most one angle ≥ 90°). For n = 2 both pieces get exactly 90° = θ — one-cut win, consistent with n − 1 = 1.
- **G3 (Assembly A):** explicit disjoint exhaustive trichotomy (has θ / has multiple mθ with m ≥ 2 / safe); reviewer note 1 satisfied — index bound m′ ≤ n − 1 stated as Observation O1 and invoked explicitly BEFORE each use of Descent; total bound n − 1 in all cases.
- **G4 (safe start):** M finite (≤ ⌊180/θ⌋), isoceles family (α, α, 180° − 2α) dodges the finite exclusion set of size ≤ 2⌊180/θ⌋.
- **G5 (Safety Preservation):** reviewer note 2 satisfied — ≡ mod θ over ℝ ((x−y)/θ ∈ ℤ), compatibility with ±, and Remark R1 (positive + residue 0 ⟹ positive multiple) all defined in Step 0, before any case split. Four-case proof inline (Step 6): (i) a ≡ 0, (ii) b ≡ 0, (iii) c ≡ 0, (iv) 180 ≡ 0 — each contradictory; quantification over every vertex/companion/t justified via Cut Lemma (3).
- **G6 (Assembly B):** induction over iterations; safe ⟹ no angle θ ⟹ check never fires; game runs forever.
- **Answer:** θ ∈ {180°/n : n ∈ ℤ, n ≥ 2}, stated explicitly with the n ≥ 2 automaticity remark and θ > 90° folded into Direction B. Verification: θ = 90° concrete one-cut win on (80°, 60°, 40°); θ = 40° safe start (55°, 55°, 70°) with a sample cut showing a safe piece survives.

## Shared-lemma deliverable

`results/imo-2026-04/lemmas/safe-piece-exists.md` filed — self-contained (definitions of ≡ mod θ over ℝ, positive multiple, safe; derivation of the piece formula and relabeling remark in the setup; full quantification over every vertex choice and every t ∈ (0, a); four-case proof; importer remarks). Marked **proposed, awaiting proof-reviewer certification**.

## Numerical sanity checks (exact rational arithmetic, this build)

- Forcing cut: n ∈ {2, 3, 5, 7, 12}, ~400 random triangles each (safe ones kept): validity t ∈ (0, a) AND both pieces containing a positive multiple — **0 failures**.
- Safety preservation: θ ∈ {40, 70, 100, 123.4, 17/3}, 89 900 random (triangle, vertex, t) cuts on safe triangles — at least one safe piece in **all** cases, 0 failures.
- Confirmed (50°, 80°, 50°) is unsafe for θ = 40° (80 = 2·40) and (55°, 55°, 70°) is safe.

## What remains open

Nothing in the proof itself. Pending external action: proof-reviewer certification of `lemmas/safe-piece-exists.md` (proposed by me, condition set by the outline-reviewer).

## Spec concerns

- Minor outline erratum (not a route problem): the outline's Step 7 suggested verifying Direction B with θ = 40°, T = (50°, 80°, 50°) — that triangle is unsafe (80° = 2·40°). Replaced with (55°, 55°, 70°) and recorded under Approaches tried. No other outline issues found; the outline-reviewer's three notes were all implementable as stated.
