# math-explorer per-role rules

ALWAYS: read past_problems_database.json / past_crux_moves_database.json with jq as a top-level array `.[]` (the file is one JSON array, not newline-delimited; `select(.domain==...)` on the array root errors with "Cannot index array with string"). (round 1)
ALWAYS: for inequality-FE problems, substitute the classical-inequality equality point first (e.g. x=f(y) where AM-GM and QM-AM share equality) — it collapses the sandwich window and yields a clean iterate relation in one move. (round 1, imo-2026-05)
NEVER: waste an approach on the y=x / diagonal substitution for symmetric-inequality FEs — it degenerates to the trivial classical inequality and yields zero information. (round 1, imo-2026-05)

ALWAYS: For an FE candidate family f(x)=x+c (constant shift), the right reduction target is "g=f-id is CONSTANT", not "g is additive Cauchy". A constant is additive only when it is 0, so the Cauchy-additive framing (aimo-0190 style) recovers only the c=0 case and silently misses c>0 solutions. (round 1, imo-2026-05)

ALWAYS: combine the iterate identity g(f(y))=g(y) with codomain positivity to get a sign kill before analysis: the forward orbit y_n=y+n*g(y) is arithmetic, and if g(y)<0 it exits R_{>0}, contradicting f>0. Yields g>=0 (f>=id) for free. (round 1, imo-2026-05)

NEVER: assume "right AM-GM-style inequality implies f(x)/x constant" without checking it rules out valid constant-shift solutions f(x)=x+c (c>0). For imo-2026-05 the implication is false — f(x)/x is not constant for the valid family — so that reduction is a dead end. (round 1, imo-2026-05)
