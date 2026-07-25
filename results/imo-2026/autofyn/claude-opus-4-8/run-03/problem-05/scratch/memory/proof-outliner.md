# proof-outliner role memory

ALWAYS: verify the load-bearing algebraic identity in sympy BEFORE writing it into an
approach as the "key lemma" (imo-2026-05 round 1: the R-test defect (p-q)^2+4(a-b)(p+a)
and L-test defect were confirmed symbolically, which turned a vague squeeze into a
near-complete orbit-crossing argument). A confirmed identity is a real key; an unverified
one is a placeholder.

NEVER: chase a large-n orbit-telescoping contradiction on this problem — the (x-y)^2 term
contributes +a^2 n^2 and dominates every linear term, so L'/R' hold automatically for large
iterates (imo-2026-05 round 1). The real constraint lives at COMPARABLE x,y; the working
move is to keep TWO orbits within a BOUNDED gap (AP-approximation) while marching to
infinity so the linear RHS beats the bounded (x-y)^2.
