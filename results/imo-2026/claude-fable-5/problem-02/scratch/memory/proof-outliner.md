# Per-role rules — proof-outliner

ALWAYS: For geometry problems, spend outline time deriving the explicit parametrization and testing candidate lemmas numerically (scipy brentq + complex coords) before fixing the field — round 1 turned "hard IMO geometry" into a nearly-complete proof by discovering the constraint decoupling and fixed point T numerically first. (round 1)
ALWAYS: Test whether the target identity holds at SPURIOUS roots of constraint equations — if yes, the theorem is a polynomial ideal-membership identity and a CAS certificate route is guaranteed to exist. (imo-2026-02: OM=ON held at all 4 root pairs, round 1)
ALWAYS: When the conclusion is "centre lies on line V" for a circle through a known point A, reformulate as "circle passes through reflection of A in V" — it turned OM=ON into a clean concyclicity with a natural point W. (round 1)
NEVER: Trust sympy trig `simplify` remainders blindly — it introduced float noise (~1e-18 coefficients) during polynomial division; use exact e^{iθ} Laurent-polynomial pipelines for certificates. (round 1)
NEVER: Assume a sine-quotient identity splits termwise (e.g. λ=γ, μ=β in power-point-trig) — check numerically first; the split claim was false while the combined identity was true. (round 1)
ALWAYS: In this repo, approach files must carry the ## Status / ## Approaches tried / ## Current best sections per CLAUDE.md contract, in addition to skeleton content. (round 1)
