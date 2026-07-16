# Lemma: Circumcenter of {0, k, l} in complex coordinates

**Statement.** For three non-collinear points `0, k, l ∈ ℂ` (non-collinear ⟺ `kl̄ − k̄l ≠ 0`),
the circumcenter of the triangle they form is
```
O = (k|l|² − l|k|²)/(k l̄ − k̄ l) = kl(l̄ − k̄)/(k l̄ − k̄ l).
```

**Proof.** O is the unique point with `|O| = |O−k| = |O−l|`. Expanding `|O|² = |O−k|²`
gives `O k̄ + Ō k = |k|²`, and `|O|² = |O−l|²` gives `O l̄ + Ō l = |l|²`. This is a linear
system in `(O, Ō)` with determinant `k̄ l − k l̄ = −(k l̄ − k̄ l) ≠ 0`. Solving for `O`
by Cramer's rule yields `O = (k|l|² − l|k|²)/(k l̄ − k̄ l)`; using `|l|² = l l̄`,
`|k|² = k k̄` gives `k|l|² − l|k|² = kl(l̄ − k̄)`, the second form. ∎

**Certification (proof-reviewer, round 1).** Verified: the symbolic derivation is correct and
the formula gives a point equidistant from `0, k, l` (numerically checked on 5 random pairs).
Certified for reuse. Certified from approach `complex-reality-conditions` §1.
