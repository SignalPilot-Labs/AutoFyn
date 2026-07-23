# Proof-Outliner Role Memory

## Rules from prior rounds

ALWAYS: Check explorer reports for numerically verified formulas before outlining (because they contain tested constraints like BK = (AB/2) sin(gamma)/sin(alpha+gamma), round 1)

ALWAYS: Note the "factor of 2" structure when midpoints appear in angle conditions (because 2l-c and 2k-b encode reflections over N and M, round 1)

NEVER: Use unsigned angle encoding for directed angle conditions (because signed angles are essential per explorer verification, round 1)

NEVER: Try concyclicity of K,L,M,N or spiral S(K)=L (because explorer verified these fail numerically, round 1)

ALWAYS: When explorer reports decoupling (constraints factor into univariate equations in separate variables), use this structure directly — it reduces polynomial elimination from hard Groebner to simple univariate arithmetic (round 2)

ALWAYS: When an explicit polynomial certificate is provided (like F·T = P1·C1 + P2·C2), include it in the skeleton — this is the proof, not just evidence (round 2)
