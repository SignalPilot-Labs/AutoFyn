# outline-reviewer per-role rules

ALWAYS: sanity-check load-bearing lemmas with a quick python3 numerical pass before approving (round 1: four-coset closure for non-winning theta, lattice-point-in-open-interval for winning theta across n in {2,3,4,5,7,11,60} — both confirmed; a wrong outline claim about n=2 equilateral (A>=90) was caught this way).

ALWAYS: read the dispatch context's "expected dead-end" hints — they flag the outliner's own high-risk probes. Cross-check against the explorer reports before cutting; a route the outliner concedes is dead (gcd obstruction for theta not dividing 90) should be RETHINK'd, not registered.

NEVER: register a RETHINK approach — junk stays out of the pool (round 1: residue-transfer-reframe had fatal gaps on BOTH directions and the only rescue collapsed it into a duplicate of lattice-coset-descent).

NEVER: trust "A >= X" pigeonhole claims for the max angle without checking the equilateral case — for n=2 (theta=90) the equilateral has A=60<90, so "A>=90" is false; the actual lattice-point-in-interval claim may still hold via a different justification.

ALWAYS: for "characterize the winning theta" games, push back when an approach only diversifies in proof-organization (attractor wrapper importing entry cuts from sibling approaches) — it shares the same wall and dies with them; register but rank below independent routes, defer build.
