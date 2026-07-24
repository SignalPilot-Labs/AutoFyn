# Outline review — imo-2026-05 (IMO 2026 P5), round 1

Answer family f(x)=x+c, c>=0 confirmed. I verified symbolically (sympy) that for f=x+c both
inequality residuals equal (x-y-c)^2>=0 exactly, and c>=0 is forced by the positive codomain.
Construction half is airtight in all three files.

## orbit-distance — APPROVE (near-complete; build primary)

I re-derived the load-bearing crux independently and it holds exactly, not merely to O(1):

- FE derivation (x=f(y) squeeze) is correct: (A)'s LHS and (B)'s RHS both collapse to f(y), giving
  f(f(y))=2f(y)-y. Steps 2-4 (orbits are APs f^n(y)=y+n g(y); g>=0 from positivity; injectivity) are
  standard and correct.
- Step 5 (all positive gaps equal) — the claimed "bounded-distance two-orbit comparison." Feeding
  (x_k, y_k=x_k-d_k, |d_k|<=beta) into (B) with f(x_k)=x_k+alpha, f(y_k)=y_k+beta gives, verified
  symbolically:
      (B)-residual = 4 x_k (alpha - beta) + (alpha - d_k)^2.
  The remainder (alpha-d_k)^2 is a NONNEGATIVE PERFECT SQUARE, bounded by (alpha+beta)^2. So if
  alpha<beta the residual -> -infinity and (B) is violated for large k; hence alpha>=beta, and swapping
  the two orbits gives beta>=alpha, so alpha=beta. This is genuinely rigorous — the outliner's "O(1)
  remainder" is actually an explicit perfect square, removing the one place I expected hand-waving.
  The mechanism is global (cross-orbit), not per-orbit, so it correctly closes the global-constant gap
  that all three framings share. The m_k=round((x_k-b)/beta) choice gives |d_k|<=beta/2 and m_k>=0 for
  large k — trivial to finish.
- Step 6 Case B (fixed point => f=id): (A) at (b, fixed a) gives, verified symbolically,
  (b-a)^2 >= 2 beta(a+b)+beta^2 > beta^2 for every positive-gap b, so every point within beta of a
  fixed point is fixed; overlapping beta/2-steps cover (0,infinity) => f=id. Correct and exhaustive with
  Case A (no fixed point => f=x+beta).

Verdict: this is effectively a complete, correct solution. Remaining work is write-up only:
(i) state the remainder bound (alpha-d_k)^2 explicitly (already an equality — easy);
(ii) verify m_k>=0 and |d_k|<=beta/2 for large k, dispatch the finitely many small-k terms;
(iii) write the beta/2-covering of (0,infinity) carefully, including stepping downward toward 0.
No circular reasoning: steps 5-6 use the ORIGINAL (A)/(B), not the FE alone (correctly guarding against
the FE's jump pseudo-solutions). Builder should produce the full rigorous proof and expect APPROVE.

## bound-pinch — CHANGES REQUESTED (viable independent hedge; build)

Technique (two-sided pointwise bound on f(x) with free knob y, then pinch to x+c) is sound and, crucially,
uses a DIFFERENT mechanism (analytic envelope/inf-sup) from orbit-distance, so it is a real hedge on the
shared crux rather than a re-skin. Gaps the builder must close:
- The optima of both envelopes are attained at a PREIMAGE (f(y)=x); existence of a preimage is a
  surjectivity claim NOT established. Do NOT assume attainment — use minimizing SEQUENCES f(y_k)->x with
  a clean limit passage (the file's option (ii)), and justify that f(y_k)->x is achievable (via the
  growth brackets of step 4 / an IVT-type argument).
- Propagating f(x)=x+c from the minimizing sequence to ALL x (uniform o(1)) is the real work — must be
  made rigorous, not asserted.
- f(y)>=y should be proved independently (step 4) OR imported as a certified lemma; either is fine.
This route is genuinely independent, so it survives even if a subtle hole appears in orbit-distance.

## monotone-gap — CHANGES REQUESTED (weakest; do NOT build this round)

Order-theoretic framing. Two unproven load-bearing steps, and it is only partially independent:
- Step 5 (f non-decreasing) is unproven and the file itself flags it may be false to prove from a single
  (x,y) pair. This is the crux of the framing and has no established mechanism yet.
- Step 7 (non-decreasing g => constant g) explicitly says to "import orbit-distance's closure" — so on
  the shared global-constant gap this route is NOT independent; it collapses to the same wall as
  orbit-distance rather than hedging it. Its only novel content is steps 5-6.
Keep it registered for diversity, but it is not worth a builder this round: its independent part (step 5)
is unproven and its finishing part is borrowed. Promote it only if orbit-distance's step 5-6 develops a
hole and step 5 monotonicity can be secured.

## Field diversity note (for the orchestrator)

orbit-distance and bound-pinch are genuinely far apart (discrete/dynamical vs analytic inf-sup) and do
NOT share a wall — a good hedge pairing. monotone-gap borrows orbit-distance's closure on the shared
crux, so it is a weaker diversity member than it looks. Since orbit-distance appears complete, no
plateau risk this round; if the builder unexpectedly finds a hole in the cross-orbit step, bound-pinch
is the independent fallback.

Ranking (Elo): orbit-distance 1531 > bound-pinch 1500 > monotone-gap 1469.

build set: orbit-distance, bound-pinch
