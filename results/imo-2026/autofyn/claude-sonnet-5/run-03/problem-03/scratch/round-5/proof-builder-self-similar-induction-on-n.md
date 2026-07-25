# proof-builder report: self-similar-induction-on-n, round 5

## Target
`Case-B(m,k): OddSum(B∪Γ_{m-2}) ≤ 2^m-1` for the tail-untouched (TOP-ONLY)
scenario, via exchange/smoothing on the near-extremal family, per this
round's outline.

## Outcome: partial (Status stays `partial`), but a genuine, large narrowing

1. **Found the exact extremal boundary configuration in closed form**:
   `B* = {2^{m-1}} ∪ (Γ_{m-2} with its "1" replaced by "2")` satisfies
   `sum(B*)=2^m` and `OddSum(B*∪Γ_{m-2}) = 2^m-1` **exactly** (proved by a
   direct rank-counting argument using the certified Tie-neutrality block
   lemma, cross-checked by exact arithmetic at m=2,4,6). This explains why
   the target constant is tight and identifies precisely where any correct
   proof must become tight.

2. **Proved Theorem 2 (sliver reduction)**: `Case-B(m,k)` is now closed,
   unconditionally, for every `B` with `max(B) ≤ 2^{m-1}-1` — i.e. for the
   entire hypothesis range `max(B) ∈ [0, 2^{m-1})` **except** a width-1
   window `(2^{m-1}-1, 2^{m-1})`, uniformly in `m`. Two clean sub-cases,
   both closed by a single peel (certified Peeling Lemma) plus the
   certified First-mover-half Lemma (Lemma B, `OddSum ≥ sum/2`) — no
   induction on `m` needed, no new open dependency introduced. This is a
   major improvement over round 4's status, where the *entire* Case-B
   target was open (numerically confirmed only, no proof).

3. **Proved a new general-purpose Two-Level Half-Bound Lemma**
   (`OddSum(N) ≥ (sum(N)+y1-y2)/2` using the top two order statistics,
   derived from the certified Peeling + Companion Peeling + Lemma B), and
   used it to attempt closing the remaining sliver. Found, by explicit
   computed counterexamples at m=4..8, that this refinement is still
   insufficient (undershoots the target by up to ≈0.5 in the worst found
   case, even though the true value clears the target with real margin) —
   an honest negative result about this specific mechanism, not evidence
   the sliver claim is false (numerics strongly support the sliver bound
   still holds, just not via this tool).

4. Considered and abandoned a Monotonicity-Lemma-based induction route
   (reducing sub-case to TOP-ONLY at level m-1) after determining it would
   require the *full* Case A (not just the certified Dominant-Chain
   sub-regime) at level m-1, which is not yet established — would have
   imported an open dependency rather than closing anything. The Lemma-B
   route above avoids this entirely and closes unconditionally.

## What remains open
The width-1 sliver `2^{m-1}-1 < b1 < 2^{m-1}` in the tail-untouched
Case-B(m,k). No mechanism tried this round (Lemma B, Two-Level Half-Bound)
closes it; the exact extremal shape `B*` sits right at this sliver's
boundary, so any closing argument must be tight there.

## Certified-eligible new lemmas (see "Promotable lemmas" in the approach file)
- Two-Level Half-Bound Lemma (general, proved in full)
- Theorem 2 (Case-B(m,k) sliver reduction, proved in full)
- Extremal boundary identity for B* (proved in full)

File updated: `results/imo-2026-03/approaches/self-similar-induction-on-n.md`
(Status: partial — real, substantial narrowing of the target this round,
not a full closure; every claim above is proved in full in the file, no
hand-waving, with the one remaining gap named precisely).
