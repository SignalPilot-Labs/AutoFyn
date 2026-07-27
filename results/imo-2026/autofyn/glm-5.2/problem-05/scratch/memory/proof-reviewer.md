# proof-reviewer per-role rules

ALWAYS: verify claimed SOS/algebraic identities with sympy (expand and check zero residue) before accepting a lemma — round 2, the master squeeze lemma's two identities were confirmed exactly this way, settling a 3-way builder conflict.

ALWAYS: when a builder "rejects" a lemma as false with a counterexample, test whether the counterexample satisfies the ORIGINAL hypothesis — round 2, density's "a=1,b=3" counterexample was an f violating the chain (QM<AM), so not a counterexample to the implication chain=>squeeze.

ALWAYS: for Kronecker/equidistribution squeeze arguments, check whether the denominator is bounded BELOW (then arbitrary density suffices, no rate needed) or GROWS (then a Dirichlet/continued-fraction rate is required) — round 2, density's "denominator >= a+b" lower bound correctly defused the rate concern, but the master-squeeze denominator grows so a rate WOULD be needed there.

ALWAYS: in orbit-membership kills, check the sign/direction: forward orbit {b+m*step: m>=0} walks UPWARD from b, so a point a=b+k*step with k<=-1 is BELOW b and NOT in the forward orbit — round 2, density's Stage B k<=-1 sub-case had this exact sign error.

ALWAYS: scrutinize the target constant in Kronecker-approximation setups against the actual cross-distance formula — round 2, density set c0=a+alpha-b but the cross-distance b-a+m*beta-(n+1)*alpha requires target a-b (off by alpha), making the bound tend to alpha^2/(a+b)>0 instead of 0.

ALWAYS: in commensurate-coset / Bezout kill arguments, verify the orbit-point index vs image-point index are consistent: cross-distance x-f(y) uses x=b+m*beta (orbit index m) but f(y)=a+(n+1)*alpha (image index n+1); a Bezout equation (n+1)p-(m+1)q=k* uses image index m+1, giving D=-(a-b)-dk*-dq (drops -dq if conflated). Re-index to x=b+(m+1)*beta or use eq (n+1)p-mq=k* for |D|=rho exactly. Round 3, density Section 7 R2 off-by-one (pre-existing from round 2, missed).
