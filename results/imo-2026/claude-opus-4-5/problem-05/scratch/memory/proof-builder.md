# proof-builder rules

ALWAYS: For functional equation problems with a "minimum at x = f(y)" structure, use finite-difference analysis (L and R constraints at x = f(y) + h) to extract regularity without assuming differentiability (because it's algebraic, round 2)

ALWAYS: When proving a function g is constant from quadratic regularity |g(u+h) - g(u)| <= C*h^2, use the partition argument: divide [u,v] into n intervals of size delta = (v-u)/n, get bound (n * C * delta^2) = C*(v-u)^2/n -> 0 as n -> infinity (because this avoids needing to invoke measure theory or differentiability, round 2)

ALWAYS: Use numerical examples to verify edge cases before finalizing the proof (because the a=0 case needed explicit verification, round 2)

NEVER: Assume that a general orbit-growth argument handles all cases - check degenerate cases (a=0, fixed points) separately with direct numerical evaluation (because they may need direct evaluation at specific points, round 2)
