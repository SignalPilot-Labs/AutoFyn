# Lemma: increment-bounds

**Status:** certified (round 1, proof-reviewer; proposed by proof-builder for `chain-lipschitz-squeeze`). All squaring/division steps between positive quantities checked; derivation re-verified independently.

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy the chain inequality (*) of lemma `chain-inequality` (in particular, any solution of the problem's double inequality). Then f is strictly increasing, and for all z, t > 0:
```
t − t²/(4f(z)) ≤ f(z + t) − f(z) ≤ t + t²/(4f(z)).
```

**Proof.** Write q = √(f(z)) > 0 and p = √(f(z + t)) > 0.

*Upper bound.* (*) with y₁ = z + t, y₂ = z gives 2pq ≤ 2q² + t; dividing by 2q > 0, p ≤ q + t/(2q). Both sides are positive, so squaring preserves the inequality:
```
f(z + t) = p² ≤ q² + t + t²/(4q²) = f(z) + t + t²/(4f(z)).
```

*Lower bound and monotonicity.* (*) with y₁ = z, y₂ = z + t gives 2pq ≤ 2p² − t, i.e. t ≤ 2p(p − q); dividing by 2p > 0, p − q ≥ t/(2p) > 0. Hence p > q and f(z + t) > f(z): f is strictly increasing. Moreover
```
f(z + t) − f(z) = (p − q)(p + q) ≥ (t/(2p))(p + q) = t − t·(p − q)/(2p),
```
and using p − q ≤ t/(2q) (from the upper-bound step) together with pq > q² = f(z):
```
t·(p − q)/(2p) ≤ t²/(4pq) < t²/(4f(z)).
```
So f(z + t) − f(z) ≥ t − t²/(4f(z)). ∎

**Where proved:** `results/imo-2026-05/approaches/chain-lipschitz-squeeze.md`, Step 2.2.
