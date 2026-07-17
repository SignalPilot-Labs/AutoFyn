# proof-outliner memory — imo-2026-04 run

ALWAYS: re-derive and stress-test any residue/invariant seed an explorer flags as a "dead end for one strategy" — it may extend to ALL moves and overturn the conjectured answer (mod-θ invariant killed the θ≤90 conjecture; true answer is 180/θ ∈ ℤ, round 1).
NEVER: trust grid-discretized value-iteration evidence for games whose win condition is an EXACT real hit — nearest-grid-point lookup fabricates exact coincidences; use exact Fraction arithmetic with structured candidate moves instead (grid said θ=55 wins, exact search + invariant proof say it does not, round 1).
ALWAYS: for imo-2026-04, the cut model is: attacking angle R with parameter t gives children C1=(P,t,Q+R−t), C2=(Q,R−t,P+t); residue sum mod θ is invariant ≡ 180 for both children (verified round 1; exact-check script pattern in /tmp/exact_check.py, regenerate if needed).
