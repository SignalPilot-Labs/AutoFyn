# Lemma: orbit-invariance

**Status:** certified (round 1, proof-reviewer). Full double-payload induction checked (base, step, positivity of iterates); hypothesis is only the functional equation, so the lemma is correctly no stronger than proved.

**Statement.** Let f : ℝ_{>0} → ℝ_{>0} satisfy f(f(y)) = 2f(y) − y for all y > 0 (e.g. any solution of the problem's double inequality, by lemma `fe-double-iterate`). Define h(y) := f(y) − y and the iterates f⁰(y) := y, fⁿ⁺¹(y) := f(fⁿ(y)). Then for every y > 0 and every integer n ≥ 0:
```
(a) fⁿ(y) = y + n·h(y),   (b) h(fⁿ(y)) = h(y).
```
In particular h(f(y)) = h(y), and the forward orbit of y is the arithmetic progression {y + n·h(y) : n ≥ 0}.

**Proof.** First, the iterates are defined and positive: f⁰(y) = y > 0, and if fⁿ(y) > 0 then fⁿ⁺¹(y) = f(fⁿ(y)) > 0 since f maps ℝ_{>0} into ℝ_{>0}; induction on n.

The functional equation rewrites as f(f(y)) − f(y) = f(y) − y, i.e.
```
h(f(y)) = h(y) for all y > 0.   (★)
```

Now induct on n. Base n = 0: (a) reads f⁰(y) = y, true; (b) reads h(y) = h(y), true.

Inductive step: assume (a), (b) for n. Then
```
fⁿ⁺¹(y) = f(fⁿ(y)) = fⁿ(y) + h(fⁿ(y))     [definition of h at the point fⁿ(y)]
        = (y + n·h(y)) + h(y)               [hypotheses (a) and (b)]
        = y + (n+1)·h(y),
```
giving (a) for n + 1; and
```
h(fⁿ⁺¹(y)) = h(f(fⁿ(y))) = h(fⁿ(y)) = h(y)   [(★) at the point fⁿ(y) > 0, then (b)],
```
giving (b) for n + 1. ∎

**Where proved:** `results/imo-2026-05/approaches/orbit-forbidden-zone.md`, Step 2.2.
