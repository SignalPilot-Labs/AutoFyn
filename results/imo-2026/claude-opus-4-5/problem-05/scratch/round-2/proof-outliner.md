## imo-2026-05

orbit-invariance: new
Target: Determine all f: R+ -> R+ satisfying sqrt((x^2 + f(y)^2)/2) >= (f(x) + y)/2 >= sqrt(x*f(y)) for all x, y > 0.
Technique: Functional equation from equality substitution + orbit-invariance of g = f - id + growth contradiction
Skeleton:
  1. Substitute x = f(y): both inequalities become equalities, forcing f(f(y)) = 2f(y) - y.
  2. Define g = f - id; derive g(f(y)) = g(y) (orbit-invariant).
  3. Prove g >= 0 by descent (negative g sends orbits to -infinity).
  4. Derive L + R = 2(x - f(y))^2 and L - R = 2(g(y) - g(x))*(positive factor).
  5. If g takes two values a < b, use orbit growth: n ~ bt, m ~ at gives |x - f(y)| bounded but RHS -> infinity. Contradiction.
  6. Conclude g = c constant, f(x) = x + c. Verify both inequalities hold.
Key lemmas (claim + mechanism):
  - f(f(y)) = 2f(y) - y -- because x = f(y) makes both QM and GM equal to f(y), squeezing AM to equality
  - g >= 0 -- because orbit f^n(y) = y + n*g(y) must stay positive; negative g sends orbit to -infinity
  - g constant -- because two distinct orbit values a < b make RHS of constraint grow as O(t) while LHS stays O(1)
Open gaps: Step 5 orbit-growth argument (rigorous bound on |na - mb| and handling of a = 0 case)
Cases to cover: none (continuous family c >= 0)
Watch out for: Orbit indices must be valid positive integers; fixed points (g = 0) handled separately

differentiability-squeeze: new
Target: Same (characterize all solutions)
Technique: Critical-point analysis of L(x, y) as a function of x; minimum at x = f(y) forces f' = 1
Skeleton:
  1. Establish f(f(y)) = 2f(y) - y from x = f(y) substitution.
  2. Prove f(x) >= x by descent.
  3. Observe L(x, y) >= 0 with L = 0 at x = f(y) (unique minimum in x for fixed y).
  4. If f is C^1, differentiate L at x = f(y): dL/dx = 4f(y)(1 - f'(f(y))) = 0 => f'(f(y)) = 1 for all y.
  5. Range of f is (c, infinity); f' = 1 on range extends to f' = 1 everywhere via functional equation.
  6. Conclude f(x) = x + c with c >= 0.
Key lemmas (claim + mechanism):
  - f'(f(y)) = 1 -- because L attains minimum at x = f(y), derivative vanishes, and f(y) > 0
  - f' = 1 everywhere -- because range(f) includes all large reals and functional equation propagates derivative
Open gaps: Justifying the differentiability assumption (or finite-difference version)
Cases to cover: none
Watch out for: Differentiability is assumed; may need to prove f is locally Lipschitz from the inequality

direct-squeeze: new
Target: Same
Technique: Characterize the middle term as AM(x, f(y)) directly from the double inequality
Skeleton:
  1. Note QM >= AM >= GM is the standard chain; our inequality places (f(x) + y)/2 between QM(x, f(y)) and GM(x, f(y)).
  2. If (f(x) + y)/2 = (x + f(y))/2 for all x, y, then f(x) - x is constant.
  3. Use L + R = 2(x - f(y))^2 and L - R = 2(g(y) - g(x))*(positive) to show L = R requires g constant.
  4. Conclude f(x) = x + c and verify.
Key lemmas (claim + mechanism):
  - (f(x) + y)/2 = AM(x, f(y)) -- because L = R forces g constant, making middle term exactly AM
Open gaps: Step 3 crux (proving non-constant g violates L >= 0 or R >= 0) likely reduces to orbit argument
Cases to cover: none
Watch out for: This approach may collapse into orbit-invariance if Step 3 requires the same orbit-growth contradiction

---

**Build set recommendation:** orbit-invariance, differentiability-squeeze

- `orbit-invariance` is the most elementary route (no regularity assumptions), directly using the functional equation and orbit structure. Priority: advance this first.
- `differentiability-squeeze` offers a cleaner proof if regularity can be justified; worth pursuing in parallel as it gives a shorter argument once differentiability is established.
- `direct-squeeze` is weaker -- its crux step likely reduces to the same orbit argument as `orbit-invariance`, so deprioritize unless the builder finds a shortcut.
