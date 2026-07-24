ALWAYS: when an outline's necessity/sufficiency "gap" mechanism is vague or admittedly
undiscovered (e.g. "cell partition, needs care"), re-derive from first principles by
solving the underlying algebra directly (set up the exact equations for when a move
can force both children, solve for which parameter choices coincide) rather than trying
to force-fit the outline's guessed machinery — the real invariant is often much simpler
than the outline's speculative one. (imo-2026-04 round 1: outline guessed a cell-partition
invariant for necessity; direct algebra showed the real invariant is just "no angle is an
exact integer multiple of θ," provable in a two-case argument with zero geometric
machinery, and it subsumed the separately-proved θ>90° acute-triangle special case for
free.)

ALWAYS: for "explicit initial construction" existence lemmas, try the most symmetric
object first (equilateral triangle, all-equal tuple, etc.) and check the one-line
non-membership argument before reaching for "generic ε" or genericity appeals — it is
often literally the answer and gives a much cleaner, more explicit proof satisfying the
no-hand-waving/no-existence-appeal rule. (imo-2026-04: equilateral (60,60,60) works as
the universal safe start for every non-resonant θ, via one line: 60=kθ ⇒ 180/θ=3k∈ℤ.)

ALWAYS: use Bash/python3 to stress-test (thousands of random trials) any "for all X,
some Y holds" algebraic claim in a combinatorial game proof before committing to the
written proof — cheap, fast, and catches errors the reviewer would otherwise flag; but
remember the written proof must still stand alone (the numeric check is not a
substitute for the algebraic derivation, only a sanity check on it).

NEVER: assume a per-approach "distinct mechanism" the outliner assigned is actually
distinct once you dig in — game-tree/potential/lattice framings on the same base
formulas often reduce to the identical underlying algebra; if you find your lemma is a
special case or restatement of another approach's mechanism, say so explicitly in the
write-up (helps the reviewer avoid duplicate certification) rather than presenting it as
independent.
