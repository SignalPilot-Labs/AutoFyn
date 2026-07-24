## imo-2026-06 — reversible-transition-map, round 5

**Mandatory disambiguation completed (per dispatch).** Rigorously determined that the
approach's proposed "forward+backward determinism of a finite-state transition map"
splits into two parts with different answers:

1. **Forward well-definedness of the finite state map (Steps 1–2 of the outline) is
   logically EQUIVALENT to gap (†)** at the corresponding core level S: proved both
   directions. (⇐) is a restatement of the already-certified Step-5 CRT+cyclic-
   pigeonhole finish; (⇒) is new — shown that if two disjoint extended-persistent
   types fail to intersect within S, the true legality condition needs a prime outside
   S, so the S-signature state is not a sufficient statistic for legality. Conclusion:
   this part is **gap (†) restated in different language, not a bypass** — the
   dispatch's option (a). This directly contradicts the outline's claim that the
   approach "sidesteps the type-intersection question entirely," and I report this
   honestly rather than paper over it.

2. **Backward-determinism/injectivity (Step 3), aimed at the secondary "periodicity
   from n=1" gap, is genuinely different content** (option (b)) — it is not equivalent
   to (†) — but it is *conditional* on (†) already being resolved, and (new finding
   this round) it is **not by itself sufficient** to close the secondary gap even if
   proved: the early, small-index terms face a strictly weaker legality constraint
   (compatibility with fewer prior terms) than the eventual-regime rule, so an
   abstract bijection/cycle-structure argument on the eventual state space does not
   automatically show the early terms already lie on that cycle. This is stated
   precisely in the approach file as the "Obstruction" and correctly scopes what the
   secondary gap actually still requires.

**Net assessment:** this approach does not close either gap this round. Its main
deliverable — the equivalence proof "S-sufficiency ⟺ V=∅ at level S" — is a clean,
fully proved, reusable result that formally rules out the "reduce to a finite automaton"
framing as an alternate route to (†) for any future approach (proposed for
certification as a shared lemma). Status: `partial`. Given the equivalence found in
part 1, this specific approach should probably not be pursued further as an attempted
*primary*-gap bypass in future rounds (it just restates the recruitment-process
termination question); if kept alive, it should be re-scoped purely to the secondary
gap using the Step 3 obstruction as its new, narrower target.

File: `/home/agentuser/repo/results/imo-2026-06/approaches/reversible-transition-map.md`
