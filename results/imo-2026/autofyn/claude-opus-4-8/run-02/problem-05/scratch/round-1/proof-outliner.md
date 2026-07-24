## imo-2026-05

Answer (all three approaches): **f(x) = x + c for a constant c >= 0**, and this is the whole solution
set. Construction half (mandatory for a find-all): for f=x+c both (A) and (B) have residual
(x - y - c)^2 >= 0, so the whole chain holds for every real c; codomain f:R_>0->R_>0 forces x+c>0 for
all x>0, i.e. c>=0. This construction is written into every approach file.

Shared reductions (all approaches import): substitute x=f(y) to squeeze the chain to equality ⇒ the
FE f(f(y))=2f(y)-y; orbits are APs f^n(y)=y+n·g(y) with g:=f-id; codomain positivity ⇒ g>=0
(f(y)>=y); FE ⇒ f injective. The CRUX shared by every route: promote "g invariant per orbit" to
"g a single global constant c." I put up three FAR-APART framings for that crux.

---

orbit-distance: new  — **PRIMARY; appears to close the whole problem.**
Target: characterize all f (answer f(x)=x+c, c>=0), construction + uniqueness end to end.
Technique: derived FE + arithmetic-progression orbits + a bounded-distance two-orbit comparison
(discrete/dynamical, NOT algebraic and NOT per-orbit).
Skeleton: FE (x=f(y) squeeze) → orbits are APs, g orbit-invariant → g>=0 → CRUX: for any two positive
gaps α=g(a), β=g(b), pick iterates x_k=a+kα->∞ and y_k=b+m_kβ with |x_k-y_k|<=β bounded; plug (x_k,y_k)
into (B): residual = 4x_k(α-β)+O(1), so (B) for large k forces α>=β; swap ⇒ β>=α ⇒ α=β. Then case
split: no fixed point ⇒ f=x+β; a fixed point a exists ⇒ (A) at (b,a) gives (b-a)^2 > β^2 for every
positive-gap b, so fixed points are β-thick and cover (0,∞) ⇒ f=id (c=0).
Key lemmas (claim + mechanism):
  - FE f(f(y))=2f(y)-y — because x=f(y) makes (A)'s LHS and (B)'s RHS both collapse to f(y), squeezing.
  - all positive gaps equal — because at bounded orbit-distance with x->∞ the (B)-residual's leading
    term is 4x(α-β), so α≠β violates (B) (numerically confirmed: margin ~4x(α−β) -> −∞).
  - fixed point ⇒ f=id — because (A) at (b, fixed a) gives (b-a)^2 >= 2(a+b)β+β^2 > β^2, forcing every
    point within β of a to be fixed; overlapping β/2-steps cover (0,∞).
Open gaps: make the O(1) remainder in the (B)-residual explicit and uniform in k; verify m_k choice
gives |x_k-y_k|<=β with m_k>=0 for large k; write the β-cover of (0,∞) carefully.
Cases to cover: construction for all c>=0; uniqueness Case A (no fixed point) and Case B (a fixed
point exists) — exhaustive.
Watch out for: (i) do NOT combine (A)&(B) at the SAME (x,y) — collapses to trivial ((x-y)-g(y))^2>=0
(recorded dead end); (ii) do NOT use UNbounded |x-y| cross-orbit comparison — the (x-y)^2 term then
dominates and the argument dies (I checked: it gives no contradiction); (iii) steps 5-6 must use the
ORIGINAL (A)/(B), not the FE alone (the FE admits jump pseudo-solutions).

---

bound-pinch: new  — alternative framing, no orbits (real-analysis pinch).
Target: same full characterization.
Technique: turn (A),(B) into a two-sided pointwise bound on f(x) with free knob y, then pinch.
Skeleton: (B) ⇒ f(x) >= 2 sqrt(x f(y)) - y; (A) ⇒ f(x) <= sqrt(2x^2+2f(y)^2) - y, for every y →
optimize over y; both extrema are attained at the preimage y (f(y)=x), giving x+c; define
c=inf(f-id)>=0 and squeeze via a minimizing sequence.
Key lemmas: optimizing y is the preimage of x (extremum condition) — the optimum of 2 sqrt(x f(y))-y
sits where f(y)=x; f(y)>=y bootstrapped from (A) as y->∞ (independent of the FE).
Open gaps: attainment needs SURJECTIVITY (a preimage of x) — the main gap; replace by minimizing
SEQUENCES f(y_k)->x and a limit passage; make the o(1) uniform to reach ALL x.
Cases to cover: construction all c>=0; pinch must cover every x, not just the minimizing sequence.
Watch out for: without continuity the inf may not be attained — the whole route rests on the
sequence version being clean; if not, defer to orbit-distance.

---

monotone-gap: new  — third framing (order-theoretic), maximizes field diversity.
Target: same full characterization.
Technique: FE + prove f non-decreasing from (A)/(B) → order-preservation of iterates → g
non-decreasing → g constant.
Skeleton: shared FE/AP/g>=0; step 5 f non-decreasing (from (B) monotone in x with adaptive y);
step 6 x1<x2 ⇒ f^n(x1)<f^n(x2) ⇒ x1+n g(x1) < x2+n g(x2), let n->∞ ⇒ g(x1)<=g(x2) (g non-decreasing);
step 7 exclude strict increase via (A) at large separation.
Key lemmas: g non-decreasing — because order-preserving iterates give x1+n g(x1) < x2+n g(x2) for all
n, divide by n.
Open gaps: step 5 (monotonicity of f) is unproven and is this route's crux — may need (B) with
adaptive y; step 7 (non-decreasing ⇒ constant) is again the global gap — borrow orbit-distance's
bounded-distance closure if it resists.
Cases to cover: construction all c>=0; strictly-increasing vs constant g in step 7.
Watch out for: iterate order-preservation gives g NON-decreasing only (never non-increasing) — do not
claim constancy from step 6 alone; if step 5 fails, RETHINK and defer to orbit-distance.

---

Build recommendation: build **orbit-distance** first (it looks complete — highest priority to fill and
verify), and **bound-pinch** in parallel as an independent-mechanism hedge on the crux. monotone-gap is
the diversity/insurance third; advance it if a reviewer finds a hole in orbit-distance's step 5-6.
