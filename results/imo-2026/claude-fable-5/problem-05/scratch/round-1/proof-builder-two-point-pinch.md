# Build report — two-point-pinch (imo-2026-05), round 1

## What was closed
Wrote the complete rigorous proof in results/imo-2026-05/approaches/two-point-pinch.md. Status: **solved**.

All five reviewer-required rigor points from /tmp/round-1/outline-reviewer.md are addressed:
1. **Squaring legality** stated explicitly at every use (Part I both inequalities; Part II inequality (3): f(f(y')) + y > 0 since f(f(y')) > 0 as a value of f).
2. **Step-2 induction explicit** (Claims A/B/C): y_n > 0 for all n by induction on the codomain; recurrence y_{n+2} = 2y_{n+1} − y_n from the core identity at each orbit point; y_n = y + n·d(y) by two-step induction; d(y) < 0 refuted via Archimedean choice n > y/(−d(y)).
3. **Pinch identity derived by hand**: full expansion showing LHS − RHS = (y − y')² + 4f(y')(d(y') − d(y)) exactly (equation (5)); re-verified with sympy (0).
4. **Subdivision step**: min(t_i, t_{i+1}) = t_i ≥ a stated, bound (b−a)²/(4ak), conclusion via Archimedean property with explicit k > (b−a)²/(4aε).
5. **c < 0 exclusion** stated as a codomain fact (x + c ≤ 0 for x ≤ −c), independent of the inequality chain.

Sufficiency written with full algebra: both squared inequalities reduce to (x − y − c)² ≥ 0 (expansions shown; sympy re-check gives 0 for both differences).

Final answer stated and verified: exactly {f(x) = x + c : c ≥ 0}.

## Promotable lemmas (for reviewer certification)
- Core identity f(f(y)) = 2f(y) − y (Part II Step 1).
- f(y) ≥ y (Part II Step 2).
- Two-point pinch |d(a) − d(b)| ≤ (a − b)²/(4 min(a,b)) (Part II Step 3).

## Remaining gaps
None known. The argument is case-free; every step derives from the original inequalities (right inequality + the squeeze at x = f(y) only — the left inequality is used only in sufficiency and in the initial squeeze).

Spec concerns:
