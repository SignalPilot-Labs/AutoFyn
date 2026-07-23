# Problem 2 — computer-algebra scripts

These are the computer-algebra scripts Claude Sonnet 5 produced while solving IMO 2026 Problem 2 in its Claude Code session. The written solution (`../problem-02.md`) reduces `OM = ON` to a single trigonometric identity, equation (5), in the angle unknowns `x = ∠BAK` and `y = ∠CAL`, and states that (5) is an algebraic consequence of the two angle-condition equations `E_K`, `E_L` together with `sin² + cos² = 1`. These scripts are the symbolic derivation and the Gröbner-basis reduction behind that step.

## Files

- `groebner1.py` — builds `E_K`, `E_L`, and the cleared form of target equation (5), and pickles them to `target_cleared.pkl`.
- `groebner3.py` — loads the pickle, computes a Gröbner basis of `⟨ E_K, E_L, sx²+cx²−1, sy²+cy²−1 ⟩` over `ℚ(sin θ, cos θ, sin α, cos α, b, c)`, reduces the cleared target modulo it, and prints the simplified remainder.
- `verify_eqs.py` — numerical cross-check (numpy/scipy): solves the configuration for a concrete scalene triangle and evaluates `E_K`, `E_L`, and the cleared target at that point.
- `sym1.py … sym7.py`, `explore.py … explore8.py` — the symbolic derivation and exploration scripts leading to `E_K`, `E_L`, and equation (5).

`groebner1.py` must be run first (it writes `target_cleared.pkl`, which `groebner3.py` and `verify_eqs.py` load).
