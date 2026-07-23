ALWAYS: For functional inequalities f: R_{>0} -> R_{>0}, try substituting x = f(y) first — this often creates equality in both the upper and lower bound simultaneously, forcing an exact identity like f(f(y)) = 2f(y) - y (because <symmetric substitution makes QM(a,a) = a exact>, round 1)

ALWAYS: After deriving f(f(y)) = 2f(y) - y from a double inequality, immediately set g = f - id and note g(f(y)) = g(y) — the orbit-invariance condition is the key constraint on g (because this cleanly encodes "g is constant on orbits of f", round 1)

ALWAYS: To show f(x) >= x from f(f(y)) = 2f(y) - y, use descent: if g(y₀) < 0 then f^n(y₀) = y₀ + n*g(y₀) -> -inf, leaving R_{>0}. No regularity needed (because this is purely algebraic from the orbit formula, round 1)

NEVER: Assume the answer to a double-inequality functional equation is just f = id; always check the full family f(x) = x + c (c >= 0) first — the QM-AM-GM chain for (x, y+c) shows all work when AM(f(x),y) = AM(x,f(y)) (because for f(x) = x+c the twisted AM equals the standard AM, round 1)

ALWAYS: For a QM-AM-GM double inequality with twisted AM, compute L+R and L-R explicitly (where L, R are the two inequalities in g=f-id form): L+R = 2*(x-f(y))^2 and L-R = 2*(g(y)-g(x))*(f(x)+x+f(y)+y). Then min(L,R) >= 0 gives the combined bound (x-f(y))^2 >= |g(x)-g(y)|*(f(x)+x+f(y)+y), which is the key to proving g constant (round 2)

ALWAYS: To prove g=f-id is constant from the key inequality (x-f(y))^2 >= |g(x)-g(y)|*(f(x)+x+f(y)+y): if g(x0)=a and g(y0)=b with a<b, use orbit points n_t=round(bt), m_t=round(at) so LHS stays bounded (O(1)) but RHS grows as ~4abt -> infinity — clean contradiction without continuity (round 2)

ALWAYS: For double-inequality problems, check the structural identity L+R = 2(x-f(y))^2 where L and R are the left and right surpluses — this shows both surpluses are complementary and governed by the same expression, and for f(x)=x+c both equal (x-y-c)^2 (round 2)

ALWAYS: When L(x,y) >= 0 achieves equality at x=f(y), and if f is C^1, differentiate L with respect to x at x=f(y) to get f'(f(y))=1 for all y — this forces f'≡1 on the range of f, giving f(x)=x+c (the cleanest route for C^1 proofs) (round 2)
