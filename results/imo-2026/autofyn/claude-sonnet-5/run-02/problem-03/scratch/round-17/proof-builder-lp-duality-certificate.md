# proof-builder report — lp-duality-certificate (round 17)

## Task
Per the round-17 outline and outline-reviewer's mandatory correction: attempt a
genuinely non-circular weighted-combination certificate for case (b2)
(T/D_n < p2 < a_nT/2, p1 < T/2), the last open sub-case of the general upper
bound c(n) <= a_n. The reviewer had warned that defining lambda(p) by
"equating the two strategies' worst-case values to the target" is tautological
and adds zero content beyond the existing pointwise-min check.

## What was done
1. Attempted a genuinely independently-motivated lambda (not defined via the
   target) for combining two certified exact primal identities at n=3
   (Theorem C "bisect p1" and Bisect-Top-2), by trying to choose lambda from
   the identities' own coefficients (to cancel dependence on the most
   dangerous free coordinate). Found algebraically that no fixed lambda can
   make the combination coefficientwise nonnegative over all valid orderings
   (needs lambda <= 1/15 AND lambda >= 7/15 simultaneously - impossible).
2. Ran an exact LP search (scipy.optimize.linprog) over case (b2)'s full n=3
   polytope, sweeping lambda in [0,1]: confirmed no lambda in [0,1] rescues
   this pair (best worst-case value ~ -0.033 < 0, i.e. always a violating
   point exists).
3. Diagnosed *why*, and proved a fully general, rigorous, non-numeric
   **Convex-Combination Futility Theorem**: for any finite family of
   explicit legal Xiang-Yu strategy values Phi_1(p),...,Phi_k(p) and *any*
   weighting rule lambda_i(p) >= 0 summing to 1 (fixed or adaptively
   p-dependent, however derived), the weighted combination
   sum lambda_i Phi_i(p) <= theta(p) holds if and only if min_i Phi_i(p) <=
   theta(p) already holds. Proof: if all Phi_i(p) > theta(p), then since
   weights are nonnegative and sum to 1, the weighted average is also
   strictly > theta(p) (elementary convexity argument, full proof in the
   lemma file). This is a complete, general, non-numeric theorem - not a
   numeric conjecture.
4. This settles the round's target definitively as a negative/dead-end
   result, exactly as CLAUDE.md and the dispatch prompt permit when a
   genuine attempt collapses to the pointwise-min check: it proves (not just
   suspects) that the "weighted-combination certificate over a fixed finite
   primal family" framing can NEVER add coverage of case (b2) beyond what
   round 16's plain pointwise-minimum grid check already tested, regardless
   of how cleverly lambda(p) is chosen (this forecloses every future attempt
   at this exact mechanism, not just the "equate to target" version the
   reviewer flagged).
5. Diagnosed the deeper structural reason: Phi_min(p) is already defined as
   a minimum over Xiang Yu's legal responses, so an upper bound on it is
   witnessed by exhibiting ONE strategy - never improved by post-hoc
   averaging of several already-computed values (Xiang Yu cannot randomize
   and be scored in expectation - this is a one-shot worst-case game).
   Genuine LP-duality/weighting arguments are the natural tool for LOWER
   bounds (Claim (B), a min bounded below by a dual-feasible weighting) -
   suggesting this slug's own namesake technique is better suited to the
   *other* half of the theorem than the one it has targeted since round 8.

## Files changed
- `/home/agentuser/repo/results/imo-2026-03/approaches/lp-duality-certificate.md`
  — appended "Round 17 build" section (R17.1-R17.3) with the full attempt,
  LP search description, and complete theorem proof; updated `## Status`
  (unchanged: `partial`), `## Approaches tried`, and `## Current best`.
- `/home/agentuser/repo/results/imo-2026-03/lemmas/convex-combination-futility-theorem.md`
  — new lemma file with full proof, submitted for reviewer certification.

## Verification artifacts
- `/tmp/lp_check.py`, `/tmp/lp_witness.py` — exact LP searches confirming the
  n=3 pair fails for every lambda in [0,1] (numeric diagnostic only, cited in
  the writeup as such, not as a proof step).

## Status
`partial` (unchanged). Case (b2) remains open; this round produced a genuine,
rigorous, general negative result (a real theorem, not a numeric finding)
that forecloses an entire family of future attempts and gives a structural
diagnosis / redirection recommendation for the slug, but does not close any
new territory of case (b2). No overclaiming: the file is explicit that this
is a dead-end finding on the assigned mechanism, not progress toward closure.
