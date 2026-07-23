# proof-outliner role memory

ALWAYS: for "circumcentre equidistant from two points" targets, reduce OM=ON to
pow(M,ω)=pow(N,ω), then for midpoints M,N use pow(midpoint of A?)=pow(endpoint)/2
− (side²)/4 to collapse to an identity in the vertices only (because power along a
line is the quadratic x(x−a') with A at 0). Cleaned imo-2026-02 to a single scalar
identity pow(B)−pow(C)=(AB²−AC²)/2 this way. (round 1)

ALWAYS: numerically verify each key mechanism (reduction, cevian Law-of-Sines
formula) with a quick scipy solve before writing it as a proved lemma — caught/
confirmed pow(B)−pow(C) is a genuine constant across the 1-param family. (round 1)

NEVER: register approaches via a tool — the ranker MCP here only exposes
sample_approaches (read-only); approach files are created by writing the .md and
the ranker entry is made downstream by the reviewer/registrar. (round 1)

ALWAYS: to kill a doubled-angle (cos2γ,sin2γ) Gröbner "γ↦γ+π ghost" branch, feed
the outliner a Weierstrass t=tan(γ/2) substitution into the UN-doubled closing
relation — tan((γ+π)/2)=−cot(γ/2)≠tan(γ/2) separates the two branches, dissolving
the false-negative wall instead of routing around it. (imo-2026-02, round 2)

ALWAYS: when a synthetic power-of-point route can't pin second-intersections A' of a
line with ⊙(AKL), the inscribed-angle fact that "looks automatic from concyclicity"
is often exactly the missing non-included angle to CLOSE a sub-triangle via Law of
Sines — don't discard it as a dead end; use it as one angle of an SAS chain. (round 2)

ALWAYS: leave a CAS-bash sibling DORMANT (present to reviewer for ranking but not in
build set) when it shares the exact elimination wall of another built approach — a
single-valued fix on one closes the whole family; building both duplicates the wall.
(imo-2026-02 complex-swap-symmetry, round 2)
