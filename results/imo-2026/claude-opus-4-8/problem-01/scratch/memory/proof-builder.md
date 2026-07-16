# proof-builder role memory

ALWAYS: recompute Omega-sum drops per-prime, not from the dispatch prose (for imo-2026-01 the move m,n->gcd,lcm/gcd drops sum-Omega by exactly Omega(gcd), NOT 2*Omega(gcd) as the dispatch text claimed; per-prime min+|diff|=max gives Omega(g)+Omega(h)=Omega(lcm), so drop=Omega(m)+Omega(n)-Omega(lcm)=Omega(gcd)). Trust the approach-file/reviewer version and verify numerically. (round 1)
ALWAYS: numerically simulate a claimed monovariant + invariant over thousands of random legal play-outs before writing; catches sign/factor errors and confirms the closed form (M=prod p^{d_p}). (round 1)
