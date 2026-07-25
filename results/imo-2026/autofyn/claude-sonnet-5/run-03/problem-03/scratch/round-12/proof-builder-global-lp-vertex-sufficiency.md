# Round 12 summary — global-lp-vertex-sufficiency

## Task
Primary target: Region-Boundary Monotonicity (Opening 2) — show V(p) has a
boundary-pointing direction along which it is weakly non-decreasing, for
every interior p, which would close the Existence Theorem outright without
classifying Σ(n,k). Secondary: fragment-vs-fragment tying (not attempted
this round — time went entirely to the primary target).

## What was done
1. **Reformulated the target precisely**: the outline's literal
   "monotone along the whole path" claim is stronger than what's actually
   needed; the sufficient condition is just the endpoint inequality
   V(p) ≤ V(q) for some boundary q reachable by a straight segment from p.
   Both forms were tested.
2. **Built a numerical V(p) estimator** from the Global Vertex Lemma's own
   structure (exhaustive enumeration of all cut-allocations m with
   Σm_i ≤ n, multi-restart Nelder–Mead per shape, softmax-parametrized
   fragment proportions), cross-validated against the certified exact
   V(e_0) values from Section 4.3.
3. **Tested "move toward e_0" (and e_1) at n=2**: clean, robust
   monotonicity in every one of 20 trials — genuine positive signal, but
   only at this one, structurally exceptional value of n.
4. **Tested the identical mechanism at n=3**: found genuine (non-noise,
   confirmed at 3x restart count) non-monotonicity — refutes the "always
   aim at a single fixed vertex" mechanism as an n-uniform tool. Caught
   and fixed a real parametrization bug (varying one slack coordinate
   while holding the others numerically fixed silently leaves the
   sum-to-1 constraint hyperplane) before drawing this conclusion.
5. **Independently tested a second idea**: transplanting the exact
   consecutive-pairing k-Anchor-Merge construction that closes e_0
   (Theorem 10, closed form) unchanged to every point of the region.
   Refuted in **exact Fraction arithmetic** for n=2..8 (100% failure rate
   for n≥5, after fixing a region-membership filter bug).

## Key finding
Both proposed bypass mechanisms for closing the Existence Theorem without
classifying Σ(n,k) are now ruled out (numerically for monotonicity, exactly
for the transplanted construction). Neither test found any violation of
V(p) ≤ c(n) itself — all sampled values stayed comfortably below c(n) — so
this is evidence against these specific *proof mechanisms*, not against the
Existence Theorem. The weaker endpoint-inequality reformulation remains
open and unrefuted; it's the concrete next lead (Section 4.6.5 lists it
explicitly, along with a suggestion to try an exchange-argument-on-the-
optimal-response approach instead of a geometric-path argument).

## Status
Remains `partial`. No lemma proposed for certification this round (both
results are negative/scoping findings, analogous to how round 11's Section
5 numerical finding and the Mass-Constraint refutation were handled — the
exact-Fraction transplanted-construction result is a genuine proof of
failure at specific rational points, not a general theorem, so it stays in
the approach file rather than being promoted).

## Files
- Updated: `/home/agentuser/repo/results/imo-2026-03/approaches/global-lp-vertex-sufficiency.md`
  (new Section 4.6, new "Round 12 target" marker at top, new "Approaches
  tried / Round 12" entry).
- Scripts used (scratch, not part of the proof): `/tmp/round-12/vp_n2.py`,
  `/tmp/round-12/vp_general.py`, `/tmp/round-12/cons_pair.py`.
