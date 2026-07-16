# Approach: orbit-forbidden-zone

## Status
solved

## Approaches tried
- (round 1, outliner) Skeleton laid: functional equation f(f(y)) = 2f(y) − y from x = f(y); h := f − id ≥ 0 constant on arithmetic-progression orbits; LEFT inequality kills two distinct positive values of h (orbit chase) and kills coexistence of fixed points with non-fixed points (forbidden interval + supremum argument). No verdict yet — gaps open.
- (round 1, builder) Full writeup completed — worked. GAP 1 (two-positive-value kill, Step 2.5) closed with an explicit minimal-index choice by well-ordering and an explicit Archimedean threshold on m. GAP 2 (fixed-point kill, Step 2.6) closed: AP-hits-interval argument written with both sub-cases, (T, ∞) ⊆ P justified from F ∪ P = ℝ_{>0} and T = sup F, finiteness of T from P ≠ ∅, existence of y₀ > T − ε from the definition of supremum; the ε-squeeze replaced by the single clean choice ε = a/4 (no limit needed). Reviewer notes from the outline review (both explicit-existence points in 2.6(iii)) incorporated. All algebraic identities re-verified in sympy. No continuity or monotonicity is assumed anywhere.

## Current best
Complete proof below. Answer: the solutions are exactly f(x) = x + c for constants c ≥ 0. No open gaps.

## Full proof

**Answer.** The functions satisfying the condition are exactly

> **f(x) = x + c for all x > 0, where c ≥ 0 is a constant.**

Throughout, the hypothesis is that for all x, y > 0,

- **(LEFT)**  √((x² + f(y)²)/2) ≥ (f(x) + y)/2, and
- **(RIGHT)**  (f(x) + y)/2 ≥ √(x·f(y)).

### Part 1: Verification that f(x) = x + c (c ≥ 0) is a solution

Fix c ≥ 0 and let f(x) = x + c. Since x > 0 and c ≥ 0, f(x) = x + c > 0, so f indeed maps ℝ_{>0} to ℝ_{>0}.

Let x, y > 0. Both sides of both inequalities are positive (each is a positive multiple or root of positive quantities: x, y, f(x) = x + c, f(y) = y + c are all > 0), so each inequality is equivalent to the inequality between the squares.

*LEFT.* We must show (x² + (y + c)²)/2 ≥ ((x + c) + y)²/4. The difference of the two sides is
```
(x² + (y + c)²)/2 − (x + y + c)²/4
  = [2x² + 2(y + c)² − (x + (y + c))²]/4
  = [x² − 2x(y + c) + (y + c)²]/4
  = (x − y − c)²/4 ≥ 0.
```
(This is the QM–AM inequality for the pair (x, y + c); see **Standard inequalities** in `knowledge_base.md`, with the equality-case square exhibited explicitly.)

*RIGHT.* We must show ((x + c) + y)²/4 ≥ x(y + c). The difference is
```
(x + y + c)²/4 − x(y + c) = [x² − 2x(y + c) + (y + c)²]/4 = (x − y − c)²/4 ≥ 0.
```
(This is the AM–GM inequality for the pair (x, y + c); same knowledge-base entry.)

Both identities were verified symbolically as well. Hence every f(x) = x + c with c ≥ 0 is a solution. (For c < 0 the formula does not even define a map into ℝ_{>0}: at x = −c/2 > 0 we would get f(x) = c/2 < 0. So no c < 0 belongs to the family, consistent with the statement of the answer.)

### Part 2: Uniqueness

Let f : ℝ_{>0} → ℝ_{>0} be any solution. We never assume continuity, monotonicity, or any regularity of f.

#### Step 2.1 — The functional equation f(f(y)) = 2f(y) − y

Fix y > 0 and substitute x = f(y) (legitimate: f(y) > 0) into both inequalities.

In (LEFT): √((f(y)² + f(y)²)/2) = √(f(y)²) = f(y) (the positive root, since f(y) > 0), so
```
f(y) ≥ (f(f(y)) + y)/2,  i.e.  f(f(y)) ≤ 2f(y) − y.
```
In (RIGHT): √(f(y)·f(y)) = f(y), so
```
(f(f(y)) + y)/2 ≥ f(y),  i.e.  f(f(y)) ≥ 2f(y) − y.
```
Combining:

> **(FE) f(f(y)) = 2f(y) − y for all y > 0.**

(As a by-product, 2f(y) − y = f(f(y)) > 0, though we will not need this.)

#### Step 2.2 — h := f − id is constant on orbits; orbits are arithmetic progressions

Define h : ℝ_{>0} → ℝ by h(y) := f(y) − y (a priori h may take any real values). Rewriting (FE):
```
f(f(y)) − f(y) = f(y) − y,   i.e.   h(f(y)) = h(y)  for all y > 0.   (★)
```

Define the iterates f⁰(y) := y and fⁿ⁺¹(y) := f(fⁿ(y)) for n ≥ 0. First note fⁿ(y) ∈ ℝ_{>0} for all n, by induction: f⁰(y) = y > 0, and if fⁿ(y) > 0 then fⁿ⁺¹(y) = f(fⁿ(y)) > 0 since f maps ℝ_{>0} into ℝ_{>0}. So the iterates are always defined.

**Claim.** For every y > 0 and every integer n ≥ 0:
```
(a) fⁿ(y) = y + n·h(y),   and   (b) h(fⁿ(y)) = h(y).
```

*Proof by induction on n.* For n = 0: (a) reads f⁰(y) = y + 0 = y, true; (b) reads h(y) = h(y), true.

Inductive step: assume (a) and (b) hold for some n ≥ 0. Then
```
fⁿ⁺¹(y) = f(fⁿ(y)) = fⁿ(y) + h(fⁿ(y))        [definition of h at the point fⁿ(y)]
        = (y + n·h(y)) + h(y)                  [induction hypotheses (a) and (b)]
        = y + (n+1)·h(y),
```
which is (a) for n + 1; and
```
h(fⁿ⁺¹(y)) = h(f(fⁿ(y))) = h(fⁿ(y))           [(★) applied at the point fⁿ(y) > 0]
           = h(y)                              [induction hypothesis (b)],
```
which is (b) for n + 1. ∎ (Claim)

So the forward orbit of any y is the arithmetic progression {y + n·h(y) : n ≥ 0}, and h is constant (equal to h(y)) on it.

#### Step 2.3 — h ≥ 0 everywhere

Suppose h(y₀) < 0 for some y₀ > 0. By the Archimedean property of ℝ there is an integer n with n > y₀/(−h(y₀)); for that n,
```
fⁿ(y₀) = y₀ + n·h(y₀) = y₀ − n·(−h(y₀)) < y₀ − y₀ = 0,
```
contradicting fⁿ(y₀) ∈ ℝ_{>0} (Step 2.2). Hence

> **h(y) ≥ 0 for all y > 0.**

Consequently every orbit is a non-decreasing arithmetic progression, and if h(y) > 0 the orbit {y + n·h(y) : n ≥ 0} is strictly increasing and unbounded above.

#### Step 2.4 — The LEFT inequality in h-coordinates

Fix x, y > 0. Both sides of (LEFT) are positive (the left side is the square root of a positive quantity; the right side is (f(x) + y)/2 > 0), so (LEFT) is equivalent to the squared inequality
```
(x² + f(y)²)/2 ≥ (f(x) + y)²/4,   i.e.   2x² + 2f(y)² ≥ (f(x) + y)².
```
Write f(x) = x + h(x) and y = f(y) − h(y), and set c := h(x) − h(y) (a real number, possibly of any sign). Then
```
f(x) + y = (x + h(x)) + (f(y) − h(y)) = (x + f(y)) + c,
```
so the squared inequality reads 2x² + 2f(y)² ≥ (x + f(y))² + 2c(x + f(y)) + c². Since
```
2x² + 2f(y)² − (x + f(y))² = x² − 2x·f(y) + f(y)² = (x − f(y))²
```
(direct expansion, verified symbolically), (LEFT) is equivalent to

> **(L) (x − f(y))² ≥ 2c·(x + f(y)) + c²,  where c = h(x) − h(y),  for all x, y > 0.**

We will only invoke (L) at pairs (x, y) where c > 0; there its right side grows linearly in x + f(y), which is the mechanism of both kill arguments below.

#### Step 2.5 — h takes at most one positive value

Suppose, toward a contradiction, that h takes two distinct positive values. Name them so that h(x₀) = b and h(y₀) = a with 0 < a < b (this is merely choosing notation: of the two distinct positive values, call the larger one b and pick x₀ attaining it, the smaller one a and pick y₀ attaining it — no generality is lost).

By Step 2.2:
- xₘ := fᵐ(x₀) = x₀ + m·b, with h(xₘ) = b, for all m ≥ 0;
- yₙ := fⁿ(y₀) = y₀ + n·a, with h(yₙ) = a, and hence f(yₙ) = yₙ + h(yₙ) = y₀ + (n+1)·a, for all n ≥ 0.

So the set of values {f(yₙ) : n ≥ 0} = {y₀ + (n+1)a : n ≥ 0} is a strictly increasing arithmetic progression with common difference a > 0, unbounded above.

**Sub-claim (within-one-step hit).** For every real x with x ≥ y₀ + a there exists n ≥ 0 with
```
0 ≤ f(yₙ) − x < a.
```
*Proof.* The set N := {n ∈ ℤ_{≥0} : y₀ + (n+1)a ≥ x} is nonempty: by the Archimedean property there is an integer n ≥ (x − y₀ − a)/a, and any such n (taken ≥ 0) lies in N. By well-ordering, N has a least element n. Then f(yₙ) = y₀ + (n+1)a ≥ x, giving the left inequality. For the right inequality:
- If n ≥ 1, minimality gives n − 1 ∉ N, i.e. y₀ + n·a < x, so f(yₙ) − x = y₀ + (n+1)a − x < a.
- If n = 0, then f(y₀) − x = y₀ + a − x ≤ 0 by the hypothesis x ≥ y₀ + a; combined with f(y₀) ≥ x this forces f(y₀) = x, so f(y₀) − x = 0 < a. ∎ (Sub-claim)

Now choose, by the Archimedean property, an integer m ≥ 0 with
```
m > max{ (y₀ + a − x₀)/b ,  (a²/(4(b − a)) − x₀)/b },
```
and set x := xₘ = x₀ + m·b. Then:
1. x > y₀ + a (from the first bound), so the sub-claim provides n ≥ 0 with 0 ≤ f(yₙ) − x < a; in particular (x − f(yₙ))² < a² and f(yₙ) ≥ x.
2. x > a²/(4(b − a)) (from the second bound).

Apply (L) at the pair (x, yₙ): here c = h(x) − h(yₙ) = b − a > 0, so
```
a² > (x − f(yₙ))² ≥ 2(b − a)(x + f(yₙ)) + (b − a)² > 2(b − a)(x + x) = 4(b − a)x,
```
using f(yₙ) ≥ x and (b − a)² > 0. Hence x < a²/(4(b − a)), contradicting point 2.

Therefore **h takes at most one positive value.**

#### Step 2.6 — h cannot take both the value 0 and a positive value

By Steps 2.3 and 2.5, the range of h is either {0}, or {a}, or {0, a}, for some real a > 0. Suppose toward a contradiction that the range is {0, a} with a > 0. Define
```
F := {y > 0 : h(y) = 0}   (the fixed points of f, since h(y) = 0 ⟺ f(y) = y),
P := {y > 0 : h(y) = a}.
```
Then F and P are both nonempty, disjoint, and F ∪ P = ℝ_{>0}.

**(i) Forbidden interval around each fixed point.** Fix y₀ ∈ F; then f(y₀) = y₀. For any u ∈ P, apply (L) at (x, y) = (u, y₀): c = h(u) − h(y₀) = a − 0 = a > 0 and f(y₀) = y₀, so
```
(u − y₀)² ≥ 2a(u + y₀) + a².        (†)
```
Consider the quadratic in u:
```
q(u) := (u − y₀)² − 2a(u + y₀) − a² = u² − 2(y₀ + a)u + (y₀² − 2a·y₀ − a²).
```
Completing the square / the quadratic formula: the roots are
```
u = (y₀ + a) ± √((y₀ + a)² − (y₀² − 2a·y₀ − a²)) = (y₀ + a) ± √(4a·y₀ + 2a²),
```
since (y₀ + a)² − (y₀² − 2a·y₀ − a²) = 4a·y₀ + 2a² (direct expansion; verified symbolically). Set
```
w := √(4a·y₀ + 2a²) > 0,   α := y₀ + a − w,   β := y₀ + a + w.
```
Since q is an upward parabola with real roots α < β, we have q(u) < 0 exactly for u ∈ I(y₀) := (α, β). By (†), q(u) ≥ 0 for every u ∈ P, hence

> **P ∩ I(y₀) = ∅ for every y₀ ∈ F.**

Moreover the length of I(y₀) exceeds a:
```
|I(y₀)|² = (2w)² = 4(4a·y₀ + 2a²) = 16a·y₀ + 8a² > a²   (as a, y₀ > 0),
```
so **β − α = |I(y₀)| > a**.

**(ii) Every element of P lies at or above β = sup I(y₀).** Fix u ∈ P and y₀ ∈ F, with α, β, w as in (i). By Step 2.2, uₘ := fᵐ(u) = u + m·a and h(uₘ) = h(u) = a, i.e. **uₘ ∈ P for every m ≥ 0**: the orbit of u is a strictly increasing, unbounded arithmetic progression with step a, contained in P.

Suppose, toward a contradiction, that u < β. Two exhaustive cases:

- *Case u > α.* Then u ∈ (α, β) = I(y₀) and u ∈ P, contradicting (i).
- *Case u ≤ α.* (Note that in this case α ≥ u > 0 automatically; if α ≤ 0 this case is vacuous and the previous case applies, so the two cases are exhaustive for every sign of α.) The set M := {m ∈ ℤ_{≥0} : u + m·a > α} is nonempty (Archimedean: any integer m > (α − u)/a ≥ 0 works). By well-ordering let m be its least element. Since u ≤ α, we have 0 ∉ M, so m ≥ 1, and minimality gives u + (m − 1)a ≤ α. Hence
  ```
  α < uₘ = u + m·a = (u + (m−1)a) + a ≤ α + a < α + (β − α) = β,
  ```
  using β − α > a from (i). So uₘ ∈ (α, β) = I(y₀) while uₘ ∈ P — contradicting (i).

Both cases are impossible, so **u ≥ β = y₀ + a + w > y₀ + a** for every u ∈ P and every y₀ ∈ F.

**(iii) Supremum squeeze.** By (ii), for all u ∈ P and y₀ ∈ F we have y₀ < u − a. Fix any u₁ ∈ P (P is nonempty); then u₁ − a is an upper bound for F. Since F is nonempty and bounded above, by the completeness of ℝ (least-upper-bound property) **T := sup F exists and is finite**; also T > 0 since F ⊆ ℝ_{>0} is nonempty.

*Claim: (T, ∞) ⊆ P.* Let z > T. Then z > 0, and z ∉ F because every element of F is ≤ T (T is an upper bound of F). Since F ∪ P = ℝ_{>0} and z ∈ ℝ_{>0} \ F, we get z ∈ P. ∎

Now take ε := a/4 > 0.
- Since T = sup F of a **nonempty** set, T − ε is not an upper bound of F, so there exists y₀ ∈ F with **y₀ > T − ε**.
- Since T + ε > T, the claim gives **u := T + ε ∈ P**.

Apply (ii) to this pair: u > y₀ + a, i.e.
```
T + a/4 = T + ε > y₀ + a > (T − ε) + a = T − a/4 + a = T + 3a/4,
```
so a/4 > 3a/4, i.e. a < 0 — contradicting a > 0.

Therefore h cannot take both the value 0 and a positive value.

#### Step 2.7 — Conclusion of uniqueness

By Step 2.3 the range of h lies in [0, ∞); by Step 2.5 it contains at most one positive value; by Step 2.6 it cannot contain both 0 and a positive value. Hence the range of h is a single point: **h ≡ c for some constant c ≥ 0**, i.e. f(x) = x + c for all x > 0.

Combining with Part 1: the solutions are exactly

> **f(x) = x + c, x > 0, for an arbitrary constant c ≥ 0.**  ∎

## Promotable lemmas
Proved in full this round (statements and proofs verbatim in Steps 2.1–2.3 above; proposal files written under `results/imo-2026-05/lemmas/`, pending reviewer certification):

- **fe-double-iterate** — For any solution f of the problem's double inequality, f(f(y)) = 2f(y) − y for all y > 0. Proved in Step 2.1 (substitution x = f(y) in both inequalities).
- **orbit-invariance** — For any solution f, with h := f − id: h(f(y)) = h(y), and for all n ≥ 0, fⁿ(y) = y + n·h(y) and h(fⁿ(y)) = h(y). Proved in Step 2.2 (full induction written out).
- **h-nonnegative** — For any solution f, h(y) = f(y) − y ≥ 0 for all y > 0. Proved in Step 2.3 (orbit-escape/Archimedean argument).
