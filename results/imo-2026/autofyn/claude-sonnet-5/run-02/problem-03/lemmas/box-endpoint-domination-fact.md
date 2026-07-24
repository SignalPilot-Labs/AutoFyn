## Box-Endpoint Domination Fact

**Source:** `rank-pigeonhole-budget`, round 24, §7.9.3.

**Statement.** For any finite multiset T with max(T) = c < M, and
g(b) := A({b} ∪ T) on [0,M]: g is non-decreasing (in fact strictly
increasing, slope exactly +1) on [c,M]. Hence g(M) >= g(c) always — the
top box-endpoint breakpoint b=M is never a strictly smaller value of g
than the breakpoint at T's own maximum, so it never needs a separate
bound once g(c) is bounded.

**Proof.** On (c,M], T_{>b} = empty for every b in this range (nothing
in T exceeds b there, since b>c=max(T)), so by the Insert-Element
Identity, A({b}∪T) = 2A(empty) - A(T) + (-1)^0 b = b - A(T), which is
affine in b with slope +1. Continuity at b=c (matching the
pair-cancellation value from the tie case) gives g(c) <= g(b) for all
b in (c,M], in particular g(c) <= g(M). QED.

**Scope.** Fully general — no ladder structure, no dependence on n or
on the specific problem's tail values; a pure consequence of the
certified Insert-Element Identity's affine-slope structure. Proof-
reviewer independently re-derived this from scratch (one line of
algebra) and confirms it is correct and immediately reusable wherever
a "does the box-endpoint candidate need its own bound" question arises
in a Single-Insert-Point Vertex Lemma analysis.

**Certification.** CERTIFIED, unconditional, general-purpose.
