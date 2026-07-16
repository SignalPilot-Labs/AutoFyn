# Per-role rules — proof-outliner

ALWAYS: sympy-verify every load-bearing algebraic expansion before putting it in a skeleton (round 1: caught that the crude bound (x+y+a) <= 2y+2a in the right-inequality orbit chase only kills b > 2a, while the exact expansion kills all b > a — a trap a builder would have hit).
ALWAYS: for FE-inequality problems on R_{>0}, check whether chaining the two one-sided bounds at the collapse point (x = f(y)) yields a two-variable inequality in f alone — it gave near-Lipschitz increment bounds + telescoping, the cleanest route for imo-2026-05 (round 1, chain-lipschitz-squeeze).
NEVER: let an orbit-chase argument cover the step-0 (fixed-point) case implicitly — chasing needs the smaller AP step strictly positive; the mixed 0/positive case always needs its own mechanism (round 1).
