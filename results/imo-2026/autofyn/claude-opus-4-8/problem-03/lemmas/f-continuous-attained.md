# Lemma f-continuous-attained — achievability of the strategy value (certified round 7)

**Setup.** Case-B hard regime, K_q as in `VertexFace.md`. For b ∈ K_q and an XY *strategy*
(a combinatorial cut pattern P assigning ≤ q−1 cuts among the current pieces, plus cut positions),
A(b, strategy) = μ(⊕ prefix intervals of the final multiset) (Lemma X). Define
    f(b) = min over all XY strategies with ≤ q−1 cuts of A(b, strategy).

**Statement.** f is continuous on the compact polytope K_q, and for each b the minimum is
**attained** by an actual XY strategy. Consequently f attains a maximum on K_q, and any bound
"f(b) ≤ 1/D" exhibits a concrete achieving XY strategy (not a bare existence claim).

**Proof.** There are finitely many combinatorial cut patterns P (each a composition of ≤ q−1 cuts
among ≤ 2q−2 pieces). Fix P. The admissible cut positions form a domain Π_P(b): a nested region in
which each cut position ranges over an interval whose endpoints are affine functions of b and of the
earlier positions in P (a cut on a piece created by an earlier cut has bounds depending on that
earlier position). Π_P(b) is a nonempty compact set, and as a correspondence of b it is continuous
(both upper- and lower-hemicontinuous) and compact-valued, since all defining bounds are continuous
(indeed affine). The map (b, positions) ↦ A is jointly continuous: final lengths are piecewise-affine
(hence continuous) in (b, positions), sorting is continuous, and the sorted alternating sum is a
continuous function of the sorted list. By the **Berge Maximum Theorem** (knowledge_base.md,
parametric optimisation / Maximum Theorem), g_P(b) = min_{positions ∈ Π_P(b)} A is continuous on
K_q and the min is attained (Weierstrass, Π_P(b) compact). Then f = min_P g_P is a minimum of
finitely many continuous functions, hence continuous, and is attained by the minimising P and its
positions. K_q compact + f continuous ⟹ f attains a maximum on K_q. ∎

**Certification.** Reviewer-verified round 7. Standard compactness/Berge argument; the domain Π_P(b)
is a nested position region (not a literal fixed product), but is compact and continuously varying,
so Berge + Weierstrass apply. No numerics on the load-bearing steps. Admitted to shared cache.
Reusable groundwork for any compactness-based upper-bound argument: it converts an "f ≤ bound"
statement into an explicit achieving XY strategy and supplies existence of max_{K_q} f.
