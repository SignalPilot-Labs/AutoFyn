# proof-builder role memory

ALWAYS: when a strategy lemma has a boundary case (e.g. n = 2 in a fork whose size bound needs θ ≤ 60), route the boundary case through its own self-contained lemma instead of patching the general bound — the outline-reviewer explicitly endorsed this and it removed the case analysis entirely (imo-2026-04, round 1).
ALWAYS: derive the move model from the literal problem statement in BOTH directions (every legal move has the claimed form + every parametrized move is achievable, e.g. via IVT on the cut point) — the reviewer treats an unproved "achievability" direction as a gap (imo-2026-04, round 1).
ALWAYS: define "≡ (mod θ)" as difference ∈ θℤ ⊂ ℝ up front when θ may be irrational — one sentence disposes of the whole rationality worry (imo-2026-04, round 1).
ALWAYS: when numerically checking an induction-based strategy, implement the induction's *chosen* move exactly — an arbitrary "equivalent" choice can cycle even when the proof is sound (imo-2026-04: cutting an arbitrary multiple of θ instead of the induction's chosen kθ cycled kθ ↔ (m+1)θ and hit RecursionError; the written proof was fine, round 1).
