ALWAYS: For inequality-based functional equations, the FIRST substitution to try is x = f(y) (or the substitution that makes LHS = RHS, squeezing the middle), because it gives a NECESSARY condition on f(f(y)) for free. (because this worked immediately for imo-2026-05, round 1)

ALWAYS: Check whether the problem's middle term equals AM of the other two arguments -- if f(x)+y = x+f(y), the whole chain reduces to QM >= AM >= GM trivially, and the answer is f(x)-x = constant. (because this was the key insight for imo-2026-05, round 1)

ALWAYS: After finding a candidate answer family (e.g., f(x)=x+c), compute the EXACT algebraic slack (LHS-MID and MID-RHS) and check if it's a perfect square. This reveals the equality locus and the SOS proof structure. (because both slacks = (x-f(y))^2 for imo-2026-05, round 1)

NEVER: Trust that a necessary condition (like f(f(y))=2f(y)-y) is also sufficient without numerically testing OTHER functions satisfying that necessary condition. (because the functional equation g(y+g(y))=g(y) has many formal solutions that all fail the original inequality, round 1)

ALWAYS: For a chain QM >= MID >= GM, subtract and add the L and R inequalities separately to get (I) = LHS-RHS of L and (II) = LHS-RHS of R; then (I)+(II) = 2*(x-f(y))^2 (automatic) and (I)-(II) = 2*(h(y)-h(x))*(f(x)+f(y)), so the combined constraint is (x-f(y))^2 >= |h(x)-h(y)|*(f(x)+f(y)). (because this was the key algebraic identity for imo-2026-05 round 1)

ALWAYS: When f(x)=x+c is the answer family, the ANSWER is f(x)=x+c for c >= 0 (all non-negative shifts), not just c=0. Verify this before assuming f(x)=x is the only solution. (because imo-2026-05 round 1 initial guess was f=id but the correct answer is the whole shift family)
