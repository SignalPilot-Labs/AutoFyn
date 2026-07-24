# Proof review — imo-2026-04 (Mulan's Triangle Game, IMO 2026 P4)

Both builders claim a complete proof (Status: solved) with answer **θ = 180°/n, integer n ≥ 2**
(equivalently θ ∣ 180). I re-derived every load-bearing step independently and stress-tested both
directions numerically. Both proofs are correct and complete.

## Verification performed
- **Necessity invariant (Lemma A / Lemma D):** re-derived the four-pairing exclusion by hand; brute
  force over 200000 random (good triangle, θ∤180, apex, cut) — **0 events** where both children are
  bad. The two bad-residue sets {0, 180−β} and {α, −β} are provably disjoint under goodness + θ∤180.
- **Sufficiency strategy:** simulated Mulan's explicit strategy (alignment → adversarial keep → peel)
  vs a Shan-Yu who always keeps the non-θ child, from 20000 random starts for each n = 2..12 —
  **0 failures**, always a win within ≤ n−1 moves. Edge stress (near-equilateral live n=3, near-right
  n=2, 50000 each) — all pass. The "no multiple in alignment interval" and "illegal x" guards never
  fired.
- Move algebra (★), the supplementary cut-point identity, and the interval sweeps (γ,180−β) /
  (α_min,180−α_min) checked against the angle formulas directly.

## Slug: residue-invariant → **APPROVE** (Status: solved)
- Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full solution.
- §0 move algebra correct; Facts P1/P2 (open/closed interval covering) correct. Lemma A (residue
  survival) correct — the four excluded coincidences (a≡0, b≡0, c≡0, θ∣180) are exactly the negated
  hypotheses. Good-start existence fine. Lemma B alignment handles both regimes; the α=θ⇒equilateral
  boundary (θ=60) and the θ=90 altitude case are correctly disposed. Lemma C peel: x=(m−1)θ legal,
  double fork at m=2, forced descent for m≥3 — all valid. No skipped case, no hand-waving.
- Builder's recorded Status (solved) is correct.

## Slug: geometric-forcing-extremal → **APPROVE** (Status: solved)
- Scores: Correctness 10/10, Completeness/rigor 10/10, Progress: full independent solution.
- Lemma D (fixed-sum covering) is the raw-degree twin of Lemma A, correct. The non-obtuse invariant
  for θ>90 is a valid self-contained second proof (at most one of the two supplementary cut-point
  angles exceeds 90, keep the other child). Lemma E (extremal alignment from the largest vertex):
  the union (α,180−β)∪(β,180−α)=(α_min,180−α_min) via β<90 is correct, and the multiple-in-interval
  case analysis (n even → 90; n odd, n≥5 → 90∓90/n; n=3 → α_min<60 at live positions) is complete
  and correct via IVT. Lemma F peel identical in substance to Lemma C, correct.
- Builder's recorded Status (solved) is correct. This proof is genuinely independent of the quotient
  group and corroborates the answer.

## Answer correctness
The characterization is correct and completely determined: necessity (θ∤180 ⇒ Shan-Yu survives, a
hard invariant guarantee) and sufficiency (θ=180/n ⇒ forced win in ≤ n−1 moves) are both proven, so
the set is exactly {180/n : n≥2}, all ≤ 90°. Both an upper "bound" (necessity) and an explicit
"construction" (Mulan's strategy) are present, satisfying the find-all bar.

## Actions
- `current.md` updated: Status solved + Full proof (residue-invariant as canonical, geometric route
  noted as independent confirmation).
- Certified promotable lemmas into `lemmas/`: residue-survival-invariant.md (Lemma A/D),
  alignment-and-peel.md (Lemmas B/C = E/F). All hold the sorry-free / correct-statement bar.
- Recorded both outcomes as verified-milestone.
