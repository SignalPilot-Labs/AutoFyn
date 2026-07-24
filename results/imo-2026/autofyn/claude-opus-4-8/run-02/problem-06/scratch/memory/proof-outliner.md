# proof-outliner role memory

ALWAYS reformulate greedy "smallest x with property vs all prior terms" as the increasing enumeration of the static set A={x compatible with ALL terms}; the greedy min coincides with min over A when every term itself lies in A (pairwise compatibility). This converts a dynamic process into a static periodicity question and delivers exact-from-n=1 for free (imo-2026-06, round 1).

ALWAYS look for the "universal admissible" cheap kill: for gcd-covering problems, a multiple of rad(a_1) meets every prior term (each shares a prime with a_1), giving a one-line bounded-gap (a_{n+1}-a_n ≤ rad(a_1)) and linear growth a_n=Θ(n) — the arena for any density/counting argument (imo-2026-06, round 1).

NEVER settle an "a_{n+T}=a_n+L for EVERY n" claim at eventual periodicity: a nonzero pre-period would make the claim FALSE, so exactness-from-n=1 is mandatory. Verify it numerically first (found exact from n=1 with L possibly a multiple of the tail's minimal period, e.g. a_1=143 → L=858 not 22), and build the exactness mechanism into every approach (imo-2026-06, round 1).

ALWAYS run a quick python simulation to pin (T,L) and the essential prime set before committing skeletons — it distinguishes "L=∏(essential S)" from naive guesses like "S=supp(a_1)" (recruited primes 2,3 appeared that don't divide a_1) (imo-2026-06, round 1).

NOTE when rival approaches genuinely share one deep nucleus (here: finitely many essential primes), keep them diverse on FRAMING and on the secondary subtlety (exactness mechanism), and flag the shared gap to the reviewer rather than pretending independence — honest is better than forced diversity (imo-2026-06, round 1).

ALWAYS when a corpus crux uses a GAME/dynamic recursion but our object is a static greedy sequence, look for the one game-fact that needs a static bridge and prove it via the certified greedy-min lemma: here "bad number has a move to a good number" became the static (★) "n≥a1 is a term ⟺ it shares a prime with every smaller term", provable directly from a_{n+1}=min(A∩(a_n,∞)). This let aimo-0030 Claim 4+5 transfer verbatim and CLOSE the whole (HS) finiteness gap (S={primes≤a1}), numerically confirmed 0 violations (imo-2026-06, round 2).
