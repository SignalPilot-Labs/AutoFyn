# Build report — geometric-forcing-extremal (imo-2026-04), round 1

**Status: solved.** Full rigorous proof written to
results/imo-2026-04/approaches/geometric-forcing-extremal.md.

## What I closed
- **Necessity (all θ∤180) — Lemma D.** Closed gap G1 (the exhaustive case enumeration). The
  bad-x sets are S₁={0,180−β}, S₂={α,−β} mod θ; both-children-bad needs S₁∩S₂≠∅, which is
  exactly 4 pairings, each forcing an angle≡0 or 180≡0 (θ|180). All excluded ⇒ disjoint ⇒ a
  good child always survives. This one lemma covers **every** θ∤180, θ>90 and θ≤90 alike, so
  G2 ("glue the split at 90") dissolves: no gluing needed. I kept the non-obtuse survival
  invariant (start 60-60-60, keep max-angle≤90 child; the two P-angles sum to 180 ⇒ ≤1 exceeds
  90) as an independent, residue-free second proof for θ>90 — the approach's distinctive
  contribution — clearly flagged as optional since Lemma D already suffices.
- **Sufficiency range-existence (shared gap G1/G3) — Lemma E, closed cleanly.** The extremal
  move: cut from the **largest** vertex. Its two orientation P-angle ranges (α,180−β) and
  (β,180−α) overlap because the middle angle β<90 always, and their union is exactly
  (α_min,180−α_min). This open interval always contains a multiple of θ=180/n (n even ⇒ 90=（n/2)θ
  inside; n odd ⇒ nearest multiple 90±90/n inside since α_min≤60<90(n−1)/n, the only tight point
  n=3 being the already-won equilateral). The supplement of that multiple is also a multiple, so
  one cut puts a multiple of θ into both children. This is a genuinely closed pigeonhole, not a
  hand-wave — it replaces the "3 windows summing to 180" sketch with a two-interval union off the
  single largest vertex.
- **Peel — Lemma F.** Angle mθ, cut x=(m−1)θ: T₂ gets θ (Shan-Yu forced to discard), T₁ keeps
  (m−1)θ; iterate to m=2 double fork (both children carry θ). Finite (≤n−2 moves).
- **Answer + verification.** θ=180/n, n≥2. Verified θ=90 (altitude, 1 move), θ=60 ({32,51,97}
  align→120, peel, ≤2 moves), θ=45 (align→90, peel, ≤2 moves).

## Numerical validation (sanity only; proof is self-contained)
- Lemma D both-bad events over 300k good-triangle cuts, θ∈{100,120,50,80,17,73,25,44,110,140}: **0**.
- Lemma E multiple-in-interval over 20k triangles × n=2..39: **0** failures.

## Remaining / Spec concerns
- None material. The characterization is `answer_type: characterization`; answer stated and
  verified as required.
- Note the problem is tagged difficulty_rating 7 / "medium" in problems.jsonl (not "hard"), but I
  proceeded per dispatch. No effect on the proof.
- Lemma D and Lemma F coincide in substance with residue-invariant's Lemmas A and C; Lemma E's
  "largest-vertex two-interval union" is a cleaner range-existence than the outline's 3-window
  pigeonhole and could be promoted/shared to close the same G1 in the residue-invariant build.
