# math-explorer per-role rules

ALWAYS: Numerically stress-test the "obvious" guessed answer against nearby
variants (constant shifts, scalings) before reporting it as the likely answer
— on imo-2026-05, the task framing assumed f(x)=x was forced, but f(x)=x+c
for any c>=0 also satisfies the sandwich identically (QM-AM-GM applied to
(x, f(y)) when f(x)+y = x+f(y)); a 20000-trial random python3 check caught
this in seconds and would have sent the outliner down a dead end otherwise
(round 1).

ALWAYS: When a functional inequality is a two-sided sandwich of the form
LOWER(x,g) <= middle <= UPPER(x,g) where LOWER/UPPER are a known mean
inequality chain (QM/AM/GM) applied to a pair (x, g), try substituting the
argument that makes the pair equal (e.g. x = g, or x = f(y) when g = f(y))
first — mean inequalities collapse to equality at equal arguments, which
forces the whole sandwich into an exact identity for free with one line of
algebra. This was the single highest-value move on imo-2026-05 (round 1).

NEVER: assume a crux-corpus problem is analogous just because it shares
surface vocabulary (e.g. "f(x)+y = f(y)+x", "g(x)=x-f(x)" substitution) —
aimo-0761 looked promising by keyword search but is a materially different
problem (implication-based hypothesis over all of R, no positivity
constraint, needs a much heavier order-theoretic argument); report such
matches explicitly as "weak/loose inspiration only," not as a template
(round 1).
