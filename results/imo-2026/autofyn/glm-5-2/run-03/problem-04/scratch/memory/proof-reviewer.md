# proof-reviewer — per-role memory

ALWAYS: re-derive the load-bearing step (e.g. the angle-transformation formula, the lattice-point-in-interval claim, the pairing lemma) from scratch with numpy over many random triangles AND hand-check the boundary n=2/θ=90 case separately — three IMO-2026-P4 proofs all passed because the boundary sub-case and the random numerical check both confirmed the entry lemma (round 1).

ALWAYS: when multiple builders submit rival complete proofs of the same characterization, verify the necessity closure is genuinely exhaustive (the 2×2 disjunction expansion gives exactly four cases — list them and settle each) and that each sufficiency route's "entry cut" produces positive angles in both children (the m_u≤n−1 refinement in the deficit-pairing route is exactly what prevents a degenerate zero angle — flag any entry cut that doesn't explicitly bound the multiplier) (round 1).

NEVER: accept "by symmetry" or "clearly" in a necessity closure — demand the four cases be written out; the case (iv) that yields 180∈θZ is the load-bearing one and must be there (round 1).
