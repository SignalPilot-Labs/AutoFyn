## imo-2026-03

greedy-halving-adversary: advance
Target: c(n) = 2^n/(2^{n+1}-1) — the full lower bound, this approach's piece
being restricted Claim (B) (arbitrary Xiang-Yu split F of p1 combined with any
legal tail refinement G', A(F∪G') >= f(n) = a_n·T), assembled via the unified
Theorem P(n). This round's target: close the `p2-Pinned-Dominance Lemma`'s
open "no-dominant-fragment" branch by proving a strictly stronger,
case-split-free claim, plus continue the ℓ(F)=2, P≠∅ sub-case.
Technique: exchange-smoothing vertex-maximization (dualized, box-free simplex
form) + odd-run-reduction-lemma evaluation, applied to the STRONGER
unconditional target the explorer found rather than Prop 28's dominant/
no-dominant split.

Skeleton:
  1. **Prerequisite fix (do first, it blocks everything else this round):**
     restate `simplex-exchange-smoothing-vertex-maximization` with pin set
     {0, τ_1,...,τ_r} (not {τ_1,...,τ_r}) — this is exactly the fix round 10
     diagnosed and round 11 already executed successfully for the *box*
     variant (`zero-pin-harmlessness-lemma` + corrected
     `exchange-smoothing-vertex-maximization`). Re-derive the box-free
     analogue the same way: the proof's exchange argument already treats
     "f_j hits 0" as a stopping condition, so re-deriving with the reference
     set R := {0, τ_1,...,τ_r} costs no new mechanism, only careful
     restatement — by direct analogy to lemmas/zero-pin-harmlessness-lemma.md
     and the round-11 corrected exchange-smoothing-vertex-maximization.md.
  2. **Main target (headline, explorer opening 1):** prove, unconditionally,
     for every legal split F_2 of p_2 into k >= 1 fragments and every legal
     refinement R of the ratio-2 tail {p_3,...,p_{n+1}}:
       A(F_2 ∪ R) <= p_2 - A(R).
     This is strictly stronger than Prop 28 (no dominant/no-dominant case
     split needed) and, if proved, closes p2-Pinned-Dominance in one shot —
     both branches of (†)'s p2-cut complement.
     Mechanism: apply the fixed Lemma (step 1) with reference set R and
     moving mass p_2, to get that the maximizer of A(F_2∪R) over all legal
     F_2 (fixed total p_2) is attained at a vertex: some coordinates pinned
     to {0}∪R's values, at most one free "tied" group. Evaluate each vertex
     type via `odd-run-reduction-lemma`. The explorer's numeric evidence
     (20,000+ trials, max always at the trivial vertex F_2={p_2}, i.e. k=0)
     strongly suggests the vertex enumeration COLLAPSES: show directly that
     every non-trivial vertex (k>=1, at least one real cut) gives a value
     strictly less than the k=0 baseline p_2 - A(R). Candidate mechanism for
     that collapse: use `general-ladder-dominance` (Total(tail) < p_2) to
     show any cut of p_2 removes mass from the "always-present" region of the
     odd-parity indicator without adding compensating odd-parity mass
     elsewhere, i.e. a monotonicity-in-fragmentation argument specific to the
     dominant-reference regime (this is NOT the previously-refuted single-step
     merge-monotonicity — that was refuted for the LOCAL single-merge step;
     here we only need to compare vertex values, which is a small finite set
     once the pin structure is fixed, not an arbitrary path of merges).
  3. **Load-bearing structural caveat, must appear explicitly in the write-up:**
     this inequality is FALSE for generic (non-ladder) reference multisets
     (explorer's counterexample τ={49,2/5}, m=203/4). The proof MUST invoke
     the ratio-2/ladder structure of the tail somewhere — most likely inside
     step 2's vertex-value comparison (e.g. via `general-ladder-dominance`'s
     exact spacing p_i = 2p_{i+1}), not as a generic multiset fact. Do not
     attempt a mechanism that would also "prove" the false generic version.
  4. **ℓ(F)=2, P≠∅ sub-case, large-Total(P) branch:** apply the same fixed
     vertex-maximization machinery (once available from step 1) to
     ψ(t*) = A({t*}∪G') with t* = p_2 - Total(P) as the moving mass and G' as
     reference, for the regime t* < Total(G') where `dominant-element-removal-
     identity` does not apply. Note the small-Total(P) regime (t* >= Total(G'))
     is ALREADY closed this round per the explorer's opening 4 — reduces
     cleanly to A(G') >= f(n) - Total(P), strictly weaker than the standard
     L(n-1) bound already used elsewhere in Theorem P(n); write this up as a
     clean corollary requiring no new machinery, then attack the genuinely
     open large-Total(P) branch with the step-2 machinery once ready.

Key lemmas (claim + mechanism):
  - Box-free Simplex Exchange-Smoothing Vertex-Maximization (pin set including
    0) — because the exchange argument's own stopping condition already uses
    f_j = 0 as a boundary case; the omission was a statement-only bug, not a
    mechanism gap (round 10/11 precedent for the box-restricted sibling).
  - A(F_2∪R) <= p_2 - A(R) unconditionally — because Total(tail) < p_2 always
    (general-ladder-dominance) makes p_2 the dominant reference automatically,
    and the vertex maximizer, once the pin-set-with-0 fix is available,
    numerically collapses to the trivial (uncut) vertex; the ladder's exact
    ratio-2 spacing is the structural ingredient that must enter the
    vertex-value comparison to rule out non-trivial vertices.
  - Small-Total(P) closure of the ℓ(F)=2 shifted-reference sub-case — because
    dominant-element-removal-identity applies whenever t*>=Total(G'), reducing
    to a strictly weaker instance of the standard recursive bound.

Open gaps: the large-Total(P) branch of ℓ(F)=2 P≠∅; whether the vertex
collapse in step 2 can be proved cleanly (only numerically supported so far).
Cases to cover: F_2's split of p_2 (dominant vs non-dominant — target is to
UNIFY these, not case-split); t* vs Total(G') for the ℓ(F)=2 sub-case.
Watch out for: (a) legal-refinement cut-budget bookkeeping — two rounds now
(10, 14) have found spurious numeric "violations" from ignoring per-piece or
total cut-budget coupling; always re-verify any check respects this. (b) Do
NOT attempt to prove the stronger claim (step 2) as a generic multiset fact —
it is false without ladder structure (explorer's counterexample is load-
bearing, must be cited in the write-up as the reason a fully general proof is
impossible). (c) the single-step merge-monotonicity mechanism is REFUTED
(3844/16000 violations) — do not use it as the collapse argument in step 2;
use vertex-value comparison over the (now finite, once pinned) vertex family
instead.

lp-duality-certificate: advance
Target: c(n) = 2^n/(2^{n+1}-1) — this approach's piece being Open Gap 1, the
general upper bound c(n) <= a_n for arbitrary Liu Bang markings, now narrowed
by the trichotomy (case a / b1 / b2) to case (b2): p_1<T/2, T/D_n < p_2 <
a_nT/2. Round 13-14 proved peel-and-recurse mechanisms structurally cannot
reach (b2) (exact-threshold proof, not just refuted witnesses) — this round's
outline explicitly forbids retrying that family.
Technique: (a) certify the new Bisect-Top-k Lemma as reusable general-n
machinery; (b) pivot from continuum optimization to the marking-agnostic
vertex-restricted machinery (per-piece-vertex-decomposition-theorem +
vertex-minimum-theorem, both already proven transferable) to search for and
characterize a genuinely tight case-(b2) worst-case witness, looking for a
structural constraint (e.g. on p_3 relative to p_2) that a new closed-form
sufficient condition could exploit.

Skeleton:
  1. **Write up and certify the Bisect-Top-k Lemma** (generalizes
     unconditional-p2-threshold-closure from k=1 to any k<=n): for any
     0<=k<=min(n,m-1), bisecting the top k pieces (k cuts, pair-cancellation-
     identity applied k times) and leaving the tail untouched gives
     Phi <= (T+p_{k+1})/2 by max-domination-lemma, hence Phi <= a_nT
     unconditionally whenever p_{k+1} <= T/D_n — no induction needed, for any
     k. State explicitly that this covers only 5-13% of case-(b2) witnesses
     numerically (explorer's honest scoping) — a genuine but partial
     sufficient region, orthogonal to Theorems A-D and Equal-Pieces/Spare-Cut
     closures.
  2. **Record the two new structural dead-end proofs** (peel-p1-vs-p2 + full
     IH has exact threshold p_2 >= a_nT/2 = case (a)'s own boundary exactly,
     zero slack into (b2); bisect-p1-alone + full IH has exact threshold
     p_1 >= a_nT, strictly inside Theorem A's p_1>=T/2 region) as certified
     negative lemmas — these rule out, algebraically not just numerically,
     any "strengthen the peel/bisect recursion" variant ever reaching (b2).
     Do not attempt to build on these mechanisms further for (b2).
  3. **Vertex-restricted worst-case search for (b2)** (the genuinely new
     mechanism): apply `per-piece-vertex-decomposition-theorem` (already
     proven marking-agnostic, extends to arbitrary compositions over all
     pieces) restricted to case-(b2) markings, to reduce the continuum
     adversarial search (which timed out this round as a raw
     differential_evolution run) to a finite vertex family. Search this
     finite family computationally for the tightest (smallest-margin)
     case-(b2) witness at n=3,4,5 — this is a much cheaper search than the
     raw continuum optimizer since the vertex family is finite and explicit.
  4. **Diagnose structure at the tight witness(es) found in step 3**: check
     specifically whether p_3 (or more generally p_{k} for small k) satisfies
     a clean relation to p_2 at the tightest witnesses — the explorer's
     finding that optimal cut allocations vary witness-to-witness (no fixed
     template) suggests the right target is an EXISTENCE claim ("a legal
     <=n-cut refinement exists achieving near-perfect pairing, small
     unpaired leftover") in the spirit of round 10's leftover-formula/
     matching reformulation, rather than another closed-form template. If
     step 3-4 locate a genuine near-tight family, state the existence claim
     precisely as this round's new open sub-target for the next round;
     if margins stay comfortable (>=0.01) at n=3,4,5 as they did this round's
     unfinished continuum search, report that honestly as evidence (b2) may
     have real slack, not a proof.

Key lemmas (claim + mechanism):
  - Bisect-Top-k Lemma: Phi <= (T+p_{k+1})/2 <= a_nT whenever p_{k+1}<=T/D_n
    — because bisecting the top k pieces cancels k exact pairs via
    pair-cancellation-identity, leaving A of the final multiset bounded by
    the untouched tail's own max (max-domination-lemma).
  - Peel-p1-p2+full-IH exact threshold = a_nT/2 (dead end, certify as
    negative lemma) — because substituting the FULL P(n-1) hypothesis (not a
    crude bound) into Theorem B's corollary and solving exactly recovers
    precisely case (a)'s own boundary, via the same telescoping-threshold-
    identity algebra already certified.
  - Bisect-p1+full-IH exact threshold = a_nT (dead end, certify as negative
    lemma) — symmetric derivation via Theorem C'/telescoping-threshold-
    identity, landing strictly inside Theorem A's region.

Open gaps: case (b2) itself remains open; the vertex-restricted search
(step 3) has not yet been run — this round's deliverable is setting it up
and getting first results, not a closure.
Cases to cover: within (b2), whether a witness family exists with vanishing
margin as n->infinity (unresolved — the round-13/14 continuum search found
comfortable margins at n=3,4 but did not finish an adversarial search).
Watch out for: (a) do not re-attempt any peel-p1-p2 or bisect-p1 variant
strengthened by a "better" IH substitution — both are now algebraically,
not just numerically, proven incapable of reaching (b2) (steps 1-2 above);
any new mechanism must be genuinely different in kind (existence/pairing,
not recursive-peel). (b) the continuum adversarial search is expensive
(timed out at n=4 this round) — use the vertex-restricted reduction (step 3)
rather than re-running raw differential_evolution, which wastes round budget
without closing anything.
