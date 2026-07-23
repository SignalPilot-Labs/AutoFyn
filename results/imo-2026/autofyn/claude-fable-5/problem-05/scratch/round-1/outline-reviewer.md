# Outline review — imo-2026-05, round 1

All three approaches are whole attempts (each targets the full characterization {f(x)=x+c : c>=0}, sufficiency + uniqueness). None repeats a recorded dead end. I independently re-verified every load-bearing identity symbolically (sympy) and numerically this round.

## Verification performed (Bash/sympy)

- **Core identity** x=f(y): both outer means collapse to f(y), forcing f(f(y)) = 2f(y) - y. Sound (QM(t,t)=GM(t,t)=t).
- **The claimed pinch identity (dispatch focus):** substituting x=f(y') into the squared right inequality (f(f(y'))+y)^2 >= 4 f(y') f(y) and using f(f(y')) = y'+2d(y') gives LHS - RHS = (y-y')^2 + 4 f(y') (d(y')-d(y)) — sympy confirms this simplifies to 0 exactly. Hence d(y)-d(y') <= (y-y')^2/(4 f(y')) <= (y-y')^2/(4y') (using f>=id, itself sound via orbit-AP positivity). Swapping roles yields |d(a)-d(b)| <= (a-b)^2/(4 min(a,b)). **The identity DOES follow from the original inequalities** — no circularity: it uses only the original right inequality plus the already-established core identity, both derived directly from the hypothesis.
- **Marching-orbits asymptotic slack (dispatch focus):** with x_m = y_n + S, sympy confirms (x_m+p+y_n)^2 - 4x_m(y_n+q) = 4y_n(p-q) + (S+p)^2 - 4Sq exactly. With S in [0,p) bounded and p<q, the slack tends to -infinity, contradicting the inequality. **Sound.**
- 4a exclusion: (a+s)^2 - 4a(s+c) = (s-a)^2 - 4ac — confirmed.
- 4b quadratic: roots of x^2 - 2(a+c)x + a^2 - c^2 - 2ac are a+c +/- sqrt(4ac+2c^2); lower root < a (since c < sqrt(4ac+2c^2)), so the whole interval [a, a+c+sqrt(4ac+2c^2)) is covered — confirmed.
- Tangency slopes: L_y'(f(y)) = U_y'(f(y)) = 1 — confirmed.
- Numeric: f(x)=x+c satisfies the chain on 10^4 random pairs; the pinch bound instantly kills a piecewise {0,c} d (0.7 vs 2.5e-7 at nearby points).

## two-point-pinch — APPROVE

Every step follows from the previous with a verified mechanism; the argument is case-free and needs no regularity. This is a candidate complete solution. Builder must:
- State squaring legality explicitly at each use (all quantities positive: (f(x)+y)/2 > 0, f(f(y'))+y > 0 since f(f(y')) > 0).
- Make step 3's induction explicit: y_n = f^n(y) is a positive real for every n >= 0, so the core identity applies at each orbit point, giving y_{n+1} = 2y_n - y_{n-1} and y_n = y + n d(y); d(y) < 0 forces y_n <= 0 for n > y/|d(y)|, contradiction.
- Derive the step-4 identity by hand (currently machine-verified) — it's a two-line expansion, include it.
- In step 5, note min(t_i, t_{i+1}) >= a so each summand is <= ((b-a)/k)^2/(4a); conclude d(a)=d(b) by Archimedean property.
- State why c < 0 is excluded: x + c <= 0 for x <= -c violates the codomain (domain fact, not the inequality).

## marching-orbits — APPROVE

Genuinely different framing (orbit asymptotics + fixed-point propagation vs two-point algebra) — good field diversity. All mechanisms check out. Fixable gaps the builder must close:
- Step 3: m = ceil((y_n - x)/p) must be shown to be a positive integer for n large (y_n -> infinity, so y_n > x eventually); bound the O(1) terms explicitly ((S+p)^2 < 4p^2, 4Sq < 4pq) rather than using limits, then pick n concretely large enough.
- Step 4 dichotomy justification: step 3 gives "at most one positive value", so range(d) is a subset of {0, c} for some c > 0 (or d == 0) — say it in exactly this form before using it.
- 4b: the strict inequality d(x) < c on the half-open interval, plus the d in {0,c} dichotomy, gives d(x)=0 — write out the bootstrap induction a_{k+1} in the extended fixed region and conclude fixed points are unbounded.
- 4c: make the AP-hits-open-interval argument explicit (b_0 = b below the interval since a' - 2 sqrt(a'c) > b, gap c < length 4 sqrt(a'c) once a' > c/16, orbit tends to +infinity; a floor argument lands some b_n inside).
- Watch-out confirmed valid: 4a genuinely requires f(a)=a exactly, which the dichotomy licenses — do not apply it before the dichotomy is established.

## tangent-envelope — CHANGES REQUESTED

The technique is legitimate (envelope tangency verified) but step 5 (density/syndeticity of range(f) anchors) is a real structural gap with no chosen mechanism — only three candidate ideas. Also, this route shares its core framing (quadratic pinch + telescoping) with two-point-pinch, which achieves the same pinch anchor-free; the outliner itself marks it a reserve. Registered in the population but NOT in this round's build set. Required changes before it earns a build slot: pick and prove one concrete mechanism for step 5, and replace all derivative/curvature language in step 4 with exact two-sided algebraic inequalities with explicit constants (f is not assumed continuous).

## Field diversity

Two of three approaches (two-point-pinch, tangent-envelope) share the quadratic-pinch framing; marching-orbits is a genuinely independent second framing. Acceptable for round 1 given two-point-pinch is a candidate complete solution — but if the pinch identity's write-up hits an unexpected wall, the field should NOT respond with more pinch variants; marching-orbits is the correct hedge and a third framing (e.g. two-variable simultaneous substitution or extremal/inf-based) would be the next diversification.

## Ranking (updated this round)

two-point-pinch 1531 > marching-orbits 1500 > tangent-envelope 1469. Rationale: two-point-pinch has no structural gap and every step verified; marching-orbits is complete-in-outline but with more delicate constants/inductions; tangent-envelope carries an open structural gap and framing overlap with the leader.

build set: two-point-pinch, marching-orbits
