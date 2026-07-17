# outline-reviewer — per-role rules

ALWAYS: for identity-grinding geometry approaches, numerically test whether the target identity holds on ALL algebraic solution branches of the constraint system (not just valid configurations) before approving — it decides whether the elimination needs semialgebraic branch conditions (round 1: all 64 spurious E1–E6 branches satisfied the goal, upgrading the approach; the complex Im(·)=0 encoding of the SAME hypotheses does have bad mirror components).
ALWAYS: refine any near-degenerate "violated" numeric branch with mpmath (50 dps) before believing it — fsolve-level residuals ~1e-8 near sin≈0 roots were pure float noise (round 1).
NEVER: approve a synthetic approach whose load-bearing step names no mechanism ("find the auxiliary circle") for the build set without bounding the builder's brief to a test-and-record hunt — otherwise it silently collapses into the sibling trig grind and duplicates it (round 1, midpoint-reflection-isogonal).
