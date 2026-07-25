# Lemma L5 — Peel-current-max identity

**Status:** CERTIFIED (proof-reviewer, round 3). Numerically verified: 0/20000 mismatches.
Sources: global-max-peel Lemma P, alternating-sum-potential (P2).

**Statement.** For any finite multiset X of reals with maximum m = x_(1),
S(X) = m − S(X ∖ {m}),
where one copy of a maximal element is removed. Consequences: 0 ≤ S(X) ≤ x_(1) ≤ Σ X.

**Proof.** Sort X as x_(1) ≥ x_(2) ≥ …. Then X ∖ {m} sorted is x_(2) ≥ x_(3) ≥ …, and
S(X ∖ {m}) = Σ_{i≥2} (−1)^{(i−1)+1} x_(i) = Σ_{i≥2} (−1)^{i} x_(i). Hence
m − S(X ∖ {m}) = x_(1) − Σ_{i≥2}(−1)^{i} x_(i) = x_(1) + Σ_{i≥2}(−1)^{i+1} x_(i) = S(X).
No strict-max hypothesis is needed: removing one copy of a maximal element and reindexing the
remaining sorted list shifts every rank by one, flipping the alternating sign. The bounds
0 ≤ S(X) ≤ x_(1) follow by pairing the descending sort as (x_(1)−x_(2))+(x_(3)−x_(4))+… ≥ 0
and x_(1) − ((x_(2)−x_(3))+…) ≤ x_(1). ∎

Reusable everywhere.
