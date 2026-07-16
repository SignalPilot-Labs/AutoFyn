# proof-outliner role memory

ALWAYS: for FE-inequality "find all f" problems, symbolically verify the load-bearing derived
inequality with sympy before committing it to an approach file (imo-2026-05 round 1: the right-ineq
bound h(t+p)-h(t)<=p^2/(4f(t)) and the left-ineq bound f(t+p)^2>=(f(t)+p)^2-p^2/2 both checked; SOS
slacks both = (x-f(y))^2). Cheap and catches a fabricated "combined inequality" the explorers guessed.

ALWAYS: when the hard step reduces to a single crux lemma that turns out clean (a quadratic
modulus-of-continuity here), still open >=1 approach that reaches the claim WITHOUT that lemma
(imo-2026-05: two-sided-orbit uses the LEFT inequality + orbit interleaving), so the field is not
one-line-fragile even when the leader looks complete.

NEVER: trust an explorer's "combined inequality (I)-(II)" without deriving it — subtracting two
inequalities does not preserve direction (imo-2026-05: the claimed (x-f(y))^2>=|h(x)-h(y)|(f(x)+f(y))
could not be rederived; the correct crux is the one-sided (U) from the RIGHT inequality alone).
