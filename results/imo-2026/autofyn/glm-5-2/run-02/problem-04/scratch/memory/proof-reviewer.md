# proof-reviewer memory

ALWAYS: independently re-derive the load-bearing step from scratch and verify numerically (python3) before APPROVE — the mod-θ four-case obstruction looked airtight on paper but I confirmed zero escapes across 13 θ values incl. irrational 180/π and 50√2, which caught nothing broken but cemented confidence (round 1).

ALWAYS: when a "both children satisfy X" claim is reduced to 2×2=4 cases, check it is exhaustive via the distributive law (disjunction of conjunctions); disjointness of cases is NOT required — ruling out each conjunction rules out the disjunction (round 1).

NEVER: flag a "gap" for θ strictly between 60° and 90° in the IF direction when N is constrained to be an integer ≥2 — N integer ⇒ θ ∈ {90°}∪{≤60°}, so no such θ exists in the IF regime (round 1).

NEVER: conflate "angle-value is a multiple of θ" (finite forbidden set {kθ < 180°}, no Kronecker issue) with "residue coset mod 180°" (which IS a Kronecker-density issue) — the mod-θ obstruction uses the former; do not demand a density argument (round 1).

ALWAYS: for characterization problems, confirm BOTH directions are proved (the set AND its complement) and that the initial/existence construction is non-vacuous — a finite-union-of-lines-in-open-set complement argument suffices (round 1).
