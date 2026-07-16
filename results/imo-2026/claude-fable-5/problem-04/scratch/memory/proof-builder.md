# proof-builder — per-role rules

ALWAYS: for imo-2026-04, use the strong-induction Descent Lemma ("angle kθ ⟹ win within k−1 cuts", cut s = θ, companion-independent), never a "largest multiple decreases" monovariant (refuted: θ = 15°, T = (75°, 60°, 45°) maps to itself under that cut, round 2).
ALWAYS: prove cut-validity with the uniform bound z ≥ 90° − x/2 (from y ≤ z), giving z − (θ − x) ≥ (90° − θ) + x/2 > 0 for all θ ≤ 90° — this collapses the n = 2 vs n ≥ 3 ignition sub-cases into one line (worked, round 2).
ALWAYS: sanity-check a finished strategy with an adversarial exact-Fraction simulation (Shan-Yu keeps EITHER piece, assert every cut parameter in the open interval) before claiming solved — it catches validity edge cases the prose can miss (round 2).
NEVER: import a lemma from results/<id>/lemmas/ that the proof-reviewer has not yet certified — write the proof inline instead (reviewer condition, round 2).
