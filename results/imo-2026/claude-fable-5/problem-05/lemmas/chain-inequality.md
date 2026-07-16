# Lemma: chain-inequality

**Status:** certified (round 1, proof-reviewer; proposed by proof-builder for `chain-lipschitz-squeeze`). Derivation re-checked independently; note it subsumes `fe-double-iterate` (take y₁ = y₂).

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy, for all x, y > 0,
```
√((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y)).
```
Then
```
(*)  2·√(f(y₁)·f(y₂)) ≤ 2f(y₂) + y₁ − y₂  for all y₁, y₂ > 0.
```

**Proof.** Fix y₁, y₂ > 0 and substitute x = f(y₂) (legitimate: f(y₂) > 0).

Left inequality at (x, y) = (f(y₂), y₂): the left side is √((f(y₂)² + f(y₂)²)/2) = √(f(y₂)²) = f(y₂) (positive root, since f(y₂) > 0), so
```
f(y₂) ≥ (f(f(y₂)) + y₂)/2,   i.e.   f(f(y₂)) ≤ 2f(y₂) − y₂.
```
Right inequality at (x, y) = (f(y₂), y₁):
```
(f(f(y₂)) + y₁)/2 ≥ √(f(y₂)·f(y₁)),   i.e.   f(f(y₂)) ≥ 2·√(f(y₁)·f(y₂)) − y₁.
```
Chaining the two bounds on f(f(y₂)) gives 2·√(f(y₁)·f(y₂)) − y₁ ≤ 2f(y₂) − y₂, which is (*). ∎

**Remark.** At y₁ = y₂ = y, (*) plus the reverse direction from the left inequality yields f(f(y)) = 2f(y) − y (lemma `fe-double-iterate`).

**Where proved:** `results/imo-2026-05/approaches/chain-lipschitz-squeeze.md`, Step 2.1.
