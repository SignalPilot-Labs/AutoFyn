# Proof review — imo-2026-05 (IMO 2026 P5), round 1

Problem: find all f: R_>0→R_>0 with √((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x·f(y)) for all x,y>0.
Claimed answer: f(x)=x+c, c≥0.

## Approach 1 — orbit-distance  →  VERDICT: APPROVE (Status: solved)

Scores: Correctness 10/10 · Completeness/rigor 10/10 · Progress: complete solution.

I attacked every load-bearing step independently and re-derived the algebra from scratch with sympy.
All checks passed:

- **Squaring to (A),(B):** both halves of the chain are nonnegative, so squaring is reversible. Correct.
- **Construction (Part I):** 2(x²+f(y)²)−(f(x)+y)² = (f(x)+y)²−4xf(y) = (x−y−c)² — sympy `factor`
  returns `(-c+x-y)²` for both. Codomain forces c≥0 (choose 0<x<−c if c<0). Verified correct.
- **FE (Part II):** substituting x=f(y)>0 collapses both outer members to f(y); the middle is genuinely
  squeezed to equality because the outer terms are literally equal. f(f(y))=2f(y)−y is rigorous, no
  hand-waving. Correct.
- **Orbits / g≥0 (Part III):** the recurrence x_{n+2}=2x_{n+1}−x_n forces constant differences, so
  f^n(y)=y+n·g(y); g<0 would drive x_n→−∞ out of R_>0. g(y)≥y is PROVEN, not assumed. Correct.
- **THE CRUX (Part IV):** I re-derived the residual independently. (B) applied to (x_k,y_k) with
  f(x_k)=x_k+α, f(y_k)=y_k+β, y_k=x_k−d_k gives residual = 4x_k(α−β)+(α−d_k)². sympy confirms this
  identity is exact (difference 0) — it is a genuine perfect-square remainder, NOT an asymptotic O(1).
  The orbits are well-defined (each iterate positive), x_k→+∞, and y_k is chosen by nearest-integer
  rounding in b's AP so |d_k|≤β/2 (bounded). If α<β, 4x_k(α−β)→−∞ dominates the bounded square,
  violating (B)≥0 — contradiction; the symmetric swap gives β≥α. So α=β. Airtight. The α=0/c=0 case is
  not needed here (this claim concerns positive gaps only) and is handled in Part V.
- **No mixing (Part V):** exhaustive dichotomy on fixed-point existence. Case A (no fixed point) ⇒ all
  gaps positive ⇒ all equal c>0. Case B: (A) at (b,a) gives 2(b²+a²)−(b+c+a)² = (b−a)²−(2c(a+b)+c²)
  (sympy diff 0), so any positive-gap b has |b−a|>c; contrapositive makes every point within c of a
  fixed point fixed, and the segment-covering with step ≤c propagates fixedness to all of (0,∞),
  contradicting any positive gap ⇒ f=id. Complete, disjoint, exhaustive.
- **No smuggled regularity:** the argument is purely algebraic/combinatorial on orbits — NO continuity,
  monotonicity, or surjectivity is assumed anywhere. Covers ALL functions f.
- **Answer stated and verified** by substitution (Part VI). Both the characterization and the
  construction are present, as required for a find-all problem.

No gap found. The builder's recorded Status `solved` is correct. Recorded outcome: verified-milestone.
current.md updated (Status=solved, Full proof written). Promotable lemmas certified:
`lemmas/fe-collapse.md`, `lemmas/ap-orbit.md`, `lemmas/master-reformulation.md` — all sympy-verified,
statements no stronger than proved.

## Approach 2 — bound-pinch  →  VERDICT: CHANGES REQUESTED (Status: partial)

Scores: Correctness 10/10 (of what is claimed) · Completeness 6/10 · Progress: real, honestly bounded.

Builder's recorded Status `partial` is accurate — no overclaim. Verified correct components:
- Construction half complete (same (x−y−c)² identities, sympy-confirmed).
- f≥id via the shared FE bootstrap — correct.
- Master reformulations (A′),(B′): sympy confirms both are exact equivalents of (A),(B) (diff 0).
- Propagation lemmas (LEFT)/(RIGHT): 4x(g(x±s)−g(x)) ≤ (g(x)∓s)² — sympy confirms each equals −(B′),
  hence a correct consequence of (B′)≥0.
- UENV g(x) ≤ √(2x²+2f(y)²)−x−y: correct positive-root bound of (A′) as a quadratic in g(x).

**Gap (as the builder honestly states):** the uniqueness crux `g(x) ≤ c := inf g everywhere` is not
closed. Two obstructions remain — (1) attainment of the inf without continuity, and (2) filling g=c
strictly between AP minimizers. The envelope/minimizing-sequence machinery provably reduces to the same
bounded-distance cross-orbit comparison that orbit-distance performs, and does not surmount it here.
This is a legitimate partial (proven lemmas + a reduction), not a broken approach — hence CHANGES
REQUESTED, not RETHINK. Note: the problem is already solved by orbit-distance; this approach's value is
its certified reusable lemmas. Recorded outcome: partial.

## Summary
- orbit-distance: APPROVE — solved. Problem imo-2026-05 is SOLVED.
- bound-pinch: CHANGES REQUESTED — partial, honest gap at the constancy crux.
