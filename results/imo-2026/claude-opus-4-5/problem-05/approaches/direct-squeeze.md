## Approach: direct-squeeze

## Status
partial

## Key idea
Work directly with the double inequality QM(x, f(y)) >= (f(x) + y)/2 >= GM(x, f(y)). For f(x) = x + c, the middle term (f(x) + y)/2 = (x + c + y)/2 = AM(x, y + c), and the inequality becomes QM(x, y + c) >= AM(x, y + c) >= GM(x, y + c), which is the standard mean chain. The approach is to show that any function satisfying the inequality must make the middle term equal to AM(x, f(y)) for all x, y, which forces f(x) - x = f(y) - y = constant. This is a "means characterization" route that avoids orbit arguments.

## Outline

1. **Reduce to the standard means structure**: Observe that for any u, v > 0, QM(u, v) >= AM(u, v) >= GM(u, v) with equality iff u = v. The given inequality places (f(x) + y)/2 between QM(x, f(y)) and GM(x, f(y)).
   - **Gap:** None.

2. **Compute the gap between QM and GM**: QM(u, v) - GM(u, v) = sqrt((u^2 + v^2)/2) - sqrt(uv). This gap is 0 iff u = v, and positive otherwise.
   - **Gap:** None.

3. **Analyze when the middle term achieves AM**: If (f(x) + y)/2 = AM(x, f(y)) = (x + f(y))/2 for all x, y, then f(x) + y = x + f(y), so f(x) - x = f(y) - y for all x, y. This forces f(x) = x + c for some constant c.
   - **Gap:** None (the implication is clear).

4. **Show the middle term must equal AM(x, f(y))**: Use the structural identity L + R = 2(x - f(y))^2 and L - R = 2(g(y) - g(x))*(sum of positive terms). If g is non-constant, then L != R at some (x, y), meaning the middle term is NOT equidistant from QM and GM. More specifically, from L = R + 2(g(y) - g(x))*(positive), if g(y) > g(x) then L > R, placing the middle term closer to QM than to GM (relative to the squared formulation). The constraint that both L >= 0 and R >= 0 while L + R = 2(x - f(y))^2 forces them to balance. The claim is: if g is non-constant, for some (x, y) either L < 0 or R < 0.
   - **Gap:** This step requires proving that non-constant g leads to a violation. This is the crux.

5. **Verify solutions satisfy the inequality**: For f(x) = x + c, both inequalities become (x - y - c)^2 >= 0, which is always true.
   - **Gap:** None.

## Hard steps
- **Step 4** is the crux. The direct route to proving L - R = 0 for all (x, y) (equivalently g(x) = g(y) always) from the constraints L >= 0, R >= 0, L + R = 2(x - f(y))^2 is not immediate. One must show that the signed term L - R cannot be nonzero everywhere while maintaining both non-negativities. This likely reduces back to the orbit or differentiation argument.

## Cases to cover
None.

## Watch out for
- This approach has a risk of being incomplete at Step 4 unless we can directly prove L = R everywhere. The orbit-growth argument from the orbit-invariance approach may be needed to fill this gap, making this approach less distinct than intended.
- The "means characterization" framing is clean but the actual proof mechanism may collapse to the same argument as orbit-invariance.
