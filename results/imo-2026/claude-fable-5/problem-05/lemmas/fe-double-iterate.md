# Lemma: fe-double-iterate

**Status:** certified (round 1, proof-reviewer). Statement matches what is proved, `sorry`-free; substitution x = f(y) collapses QM and GM to f(y) (positive root justified); both inequality directions verified independently.

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy, for all x, y > 0,
```
√((x² + f(y)²)/2) ≥ (f(x) + y)/2 ≥ √(x·f(y)).
```
Then f(f(y)) = 2f(y) − y for all y > 0. (In particular 2f(y) − y = f(f(y)) > 0.)

**Proof.** Fix y > 0 and substitute x = f(y) (legitimate since f(y) > 0) into both inequalities.

Left inequality at x = f(y): √((f(y)² + f(y)²)/2) = √(f(y)²) = f(y) (the positive root, since f(y) > 0), so
```
f(y) ≥ (f(f(y)) + y)/2,   i.e.   f(f(y)) ≤ 2f(y) − y.
```
Right inequality at x = f(y): √(f(y)·f(y)) = f(y), so
```
(f(f(y)) + y)/2 ≥ f(y),   i.e.   f(f(y)) ≥ 2f(y) − y.
```
Combining the two, f(f(y)) = 2f(y) − y. Since f(f(y)) lies in the codomain ℝ_{>0}, also 2f(y) − y > 0. ∎

**Where proved:** `results/imo-2026-05/approaches/orbit-forbidden-zone.md`, Step 2.1.
