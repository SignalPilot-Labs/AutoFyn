
## imo-2026-04 (Mulan's Triangle Game)
ALWAYS: stress-test the CLAIMED answer with a concrete small computation before building the proof around it (because in round 2 the field's target θ=90/n was FALSE — θ=60° is a 2-move Mulan win; the true answer is θ=180/m, m∈ℤ≥2, i.e. 180/θ∈ℤ. The cevian's two P-angles are supplementary summing to 180, so the modulus is 180 not 90).
ALWAYS: the ⊇ (winnable) construction for θ=180/m is clean and complete: Lemma A peel (vertex kθ, split at x=θ, forces (k−1)θ) + Lemma B (split largest vertex, both children get multiple-of-θ vertices since 180−jθ=(m−j)θ). Fully rigorous, promote it.
NEVER: trust an explorer/outliner's numerically-"verified" answer when their check only enumerated the CLAIMED winnable set — they never tested that the OTHER values are unwinnable, so a too-small answer passes their check (round 2: 90/n "verified" but 60,36,180/7 also winnable).

## imo-2026-04 (round 2)
ALWAYS: recompute the claimed ANSWER before building — for imo-2026-04 the whole field's answer θ=90/n was WRONG; true answer is θ=180/k (k≥2 int). Odd k (θ=60,36) are winnable too. Verified by exact-Fraction full-branch game search from a generic start.
NEVER: trust an outline's closure set C(θ) built on halving v↦v/2 — the Shan-Yu-immune generators here are ADDITIVE (+θ), giving G={mθ}; halving is not a forced move. (because it produced the wrong {90/2^k}/{90/n} family, round 2)
## imo-2026-04 (round 2)
ALWAYS stress-test the TARGET ANSWER before building its proof: round-2 target {90/n} for imo-2026-04 was FALSE — θ=60 is a rigorous 2-move win (inject 180-θ=2θ via P-angle threat x=180-θ-B, then 2θ-device), and 90/60=3/2. Corrected conjecture: winnable iff θ≤90 and 90/θ is a dyadic rational (numerator of θ/90 in lowest terms is a power of 2).
NEVER trust "S1/S2 verified" as verifying the full characterization: those only gave {90/n}⊆win and θ>90 excluded; the ⊆ "nothing else is winnable" was never checked and was wrong (round 2).

ALWAYS: for imo-2026-04, the F-free (no angle = positive multiple of θ) boolean invariant fully closes the ⊆ survival direction via Sub-lemma B's 4-combo algebra; transcendence/genericity is unnecessary (because Sub-lemma B is universal in x, subsuming collapse x=mθ−B and halving, round 3).

## imo-2026-04 (round 3) — SOLVED
ALWAYS: when a survival/defender invariant stalls on an "adversarial collapse" x=c−B move, check whether the invariant is over-strengthened. Here dropping the transcendence conjunct and keeping the PURE BOOLEAN invariant "F-free" (no angle = any positive multiple of θ) closed the gap: Sub-lemma B is universally quantified over x∈(0,A), so x=c−B, x=180−mθ−B, and halving are all already covered by one finite 4-case algebra. The collapse only defeated the extra transcendence conjunct, never F-freeness. (round 3)
