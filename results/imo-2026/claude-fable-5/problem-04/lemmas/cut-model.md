# Lemma L0 (cut model) — CERTIFIED (round 1)

**Statement.** Let 𝒯 be a triangle with angles P, Q, R at its three vertices. Mulan's legal moves (perimeter point distinct from the vertices, cut to the opposite vertex) are exactly the pairs (attacked vertex with angle R, split parameter t ∈ (0, R)), producing the two nondegenerate children with angle triples
C₁ = (P, t, Q + R − t) and C₂ = (Q, R − t, P + t).
Both directions hold: every legal move has this form, and every such pair is realizable (via the Crossbar Theorem, or IVT on the angle swept from the attacked vertex).

**Proof.** Lemma 0 of `approaches/circle-group-quotient.md` (Crossbar version); Lemma 1 of `approaches/residue-divisibility-characterization.md` (IVT version). Independently verified by the proof-reviewer with exact coordinate geometry on 200 random triangles/cut points.

**Consequence.** The game depends only on the (unordered) angle triple; both the stop condition and both players' option sets are functions of the triple alone.
