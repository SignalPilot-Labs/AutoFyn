## imo-2026-03

greedy-halving-adversary: revise
Target: c(n) = 2^n/(2^{n+1}-1) — this approach's piece is Claim (B): for
every legal split F of p1 (any number of cuts ℓ(F)), and every legal tail
refinement G', A(F∪G') ≥ f(n). Current live sub-target: the ℓ(F)=2
mixed-regime sub-case (c) (v1≥p2>v2), reduced (Lemma 25 + Proposition 20,
both certified) to the exact identity A(F∪G')=v1−A(F2∪G'), F2={v2}∪P, so
the remaining content is the single inequality
  (‡)  A({v2}∪G') ≤ (p1−v2) − f(n),  ∀ v2∈(0,p2), legal G' with ≤ n−1 cuts.
Round-12 explorer confirmed the naive "flat bump" of (†) (same fixed RHS
p2−f(n) at budget n−1) is FALSE by a comfortable margin — do not re-attempt
that literal step. The correctly v2-substituted (‡) is numerically tight
(margin → 0) exactly as v2→p2⁻, and has real slack away from that corner.
Technique: two-pronged — first a cheap reduction, then whichever of two
genuinely different mechanisms the reduction leaves standing.
Skeleton:
  1. Cheap reduction (do first, before either heavy mechanism): show it
     suffices to prove (‡) only at P=∅ (i.e. c=1, the single minimal-cut
     unequal split v1+v2=p1, no other paired fragments of p1) — because any
     ℓ(F)=2 configuration with nonempty P uses c≥2 cuts on p1, hence strictly
     less tail budget (≤n−2, already inside the closed (†)-regime via the
     same monotonicity-in-budget argument (†) itself uses). This is a short,
     mechanical lemma (a corollary of the certified cut-count bookkeeping in
     Lemma 19/Proposition 21) and should be written up and certified as its
     own reusable fact before either heavy step below, since it halves the
     case analysis.
  2. Boundary/continuity route (try first — cheaper): parametrize by
     t := p2−v2 ∈ (0,p2] (distance from the closed boundary case v2=p2,
     which is exactly Proposition 22's already-certified statement — the
     t=0 endpoint of (‡) is literally the closed (†) case, since v1=p1−v2=
     p1−p2 there matches the boundary of sub-case (c) with sub-case (a)).
     Write A({v2}∪G') as a function of t and show its derivative/finite
     difference against the RHS (p1−v2)−f(n) = (p1−p2+t)−f(n) is controlled:
     both sides are linear-ish in t (RHS exactly linear; LHS's dependence on
     t enters only through the single moved element v2=p2−t and the tail
     budget, which does NOT change as t varies — budget stays n−1 throughout
     since P=∅ is fixed by step 1). Reduce to bounding
     d/dt[A({p2−t}∪G')] ≤ 1 pointwise or in an integrated/telescoped sense,
     using the same single-cut-perturbation identity (Lemma 14, certified)
     that this approach already has on file for exactly this kind of
     "move one element" derivative computation — this is a genuinely
     different application of an already-certified tool (Lemma 14 was
     derived for splitting one element into two; here reuse its
     "how does A change as one coordinate moves continuously" content,
     which the identity's proof establishes as a byproduct — check this
     applies before assuming it).
  3. Exchange-smoothing import route (fallback if step 2 stalls, or run in
     parallel as a genuinely distinct mechanism — the round-12 explorer's
     structural observation is why this is worth trying as its own line,
     not just a backup): observe that F2∪G' = {v2}∪G', where G' (after the
     certified tail-self-similarity rescaling to the (n−1)-ladder) ranges
     over the ENTIRE unrestricted legal-response space at level n−1 (full
     budget n−1, no restriction) — structurally "one floating extra element
     plus a fully free full-budget response," which is exactly the shape
     Claim (A)'s exchange-smoothing vertex-maximization argument
     (`exchange-smoothing-vertex-maximization`, certified, dualized to a max
     in `case-i-closure-theorem`) was built to handle for its own achievability
     side. Adapt it here: treat v2 as Liu Bang's "extra" fixed point and ask
     whether the certified machinery's reduction (arbitrary legal composition
     of a distinguished set collapses to a small pinned+tied vertex family,
     evaluated via `odd-run-reduction-lemma`) transfers when the ambient
     multiset already contains one extra fixed foreign element v2 rather than
     being built entirely from the marking's own points. State explicitly,
     before using it, which of the machinery's hypotheses (fixed marking size,
     ladder self-similar tail, etc.) do or do not require v2 to be one of the
     marking's own ladder values — v2 is NOT a ladder value in general (it is
     an arbitrary point in (0,p2)), so this adaptation is not a free reuse and
     must be checked at the hypothesis level, not just asserted (cf. per-role
     rule: a theorem for one polarity/setting is not automatically transferable
     — verify explicitly).
  4. Whichever of steps 2/3 succeeds, combine with the already-certified
     Lemma 25 identity to conclude A(F∪G')≥f(n) for all of ℓ(F)=2 sub-case
     (c), closing the last open branch of ℓ(F)=2 and hence (modulo the
     already-honestly-flagged ℓ(F)≥3 case) advancing Theorem P(n) one
     concrete step.
Key lemmas (claim + mechanism):
  - Reduction to P=∅ — because nonempty P forces c≥2, hence budget ≤n−2,
    already inside the certified (†) regime by the same monotonicity fact
    (†)'s own derivation used (more cuts on p1 ⟹ strictly less tail budget,
    and (†)'s bound was proved at the tighter n−2 already).
  - (‡) at the boundary t=0 (v2=p2) is exactly the already-certified
    Proposition 22 statement — because sub-case (c)'s v2=p2 boundary
    coincides algebraically with sub-case (a)'s v1=v2=p2 degenerate limit,
    both reducing to the same closed (†) inequality.
  - The exchange-smoothing import (step 3) is only valid if its proof's use
    of "ladder self-similarity" does not require v2 itself to be a ladder
    value — this must be checked, not assumed, before certifying anything
    built on it.
Open gaps: (‡) itself, via either route; whichever route is attempted first
and stalls should report precisely which hypothesis broke (per NEVER-assume
rule in memory) rather than silently trying the other route without
recording the failure.
Cases to cover: P=∅ (the only case that matters after step 1's reduction,
covering c=1); the reduction argument for nonempty P (short, should be
written explicitly even though "the interesting case" is P=∅).
Watch out for: do not silently extend the case-1 (P=∅) proof to nonempty P
without re-checking the budget bookkeeping; do not assume the exchange-
smoothing machinery transfers just because the ambient shape "looks similar"
— check every certified lemma's actual hypotheses (marking membership,
ladder ratios) before invoking it on an object (v2) that isn't literally a
marking value.

lp-duality-certificate: revise
Target: c(n) = 2^n/(2^{n+1}-1) — this approach's piece is the general upper
bound, c(n) ≤ a_n for arbitrary Liu Bang markings. Round-12 explorer fully
resolved the equal-pieces stress point (both parities, exact and general,
zero numerics — a genuine small closed result) and sharpened the open
remainder of the Iterated-Greedy-Peel route to one precisely-scoped branch:
"Iterated Greedy-Peel uses its entire cut budget n with zero exact ties
occurring at any step" — ~66% of random trials land in this branch, so it
is the real content, not a corner case. This is a genuine narrowing (from
"~48-62% of trials fail" to one exactly-characterized sub-case) — advance
by formalizing the two already-proved cheap pieces, then attacking the
narrowed residual with a new selection-rule construction.
Technique: constructive/existence proof via a smarter deterministic
strategy, replacing "always match the current top two" with a rule that
provably forces either (i) an exact tie to occur before budget exhaustion
(handled by the certified pair-cancellation reduction), or (ii) an explicit
closed-form bound on the fully-generic (all-distinct, no-tie) outcome.
Skeleton:
  1. Formalize and certify, as clean standalone lemmas (both are already
     fully rigorous one-liners per the explorer, just not yet written up as
     approach-file theorems): (a) **Equal-Pieces Closure** — for m equal
     pieces value T/m, Xiang Yu achieves Φ=T/2 exactly using 0 cuts (m even,
     the m/2 exact pairs already cancel via `pair-cancellation-identity`) or
     1 cut (m odd, bisect any single piece to create one more exact pair);
     in both cases Φ=T/2<a_nT since a_n>1/2 for every n (cite the certified
     telescoping fact a_n>1/2 already proved in this approach's §2). (b)
     **Spare-Cut Bisection Corollary** — whenever Iterated Greedy-Peel
     (`iterated-greedy-peel-identity`, certified) finishes with a nonzero
     leftover value v_final and at least 1 unused cut, bisecting v_final
     achieves Φ=T/2<a_nT immediately, by the same pair-cancellation +
     a_n>1/2 argument. Together these prove: Φ_min≤a_nT holds automatically
     whenever the greedy-peel process either (i) ever produces an exact tie
     mid-process (equivalently ends with leftover of odd multiplicity ≥2
     canceling for free) or (ii) has budget to spare at the end.
  2. State the residual precisely: the only configurations not covered by
     step 1 are those where Iterated Greedy-Peel's deterministic "match
     current top two" process uses all n cuts and never once produces an
     exact intermediate tie (all m original values pairwise distinct with
     no coincidental fragment collisions throughout the process) — this is
     the explorer's exactly-characterized ~66%-of-trials branch.
  3. Attack the residual with a modified selection rule (new construction,
     not the naive greedy): instead of always matching the two current
     largest fragments, at each step choose which pair of fragments to
     equalize (or pre-emptively split one fragment) so as to *guarantee* a
     tie is created strictly before the budget is exhausted. Concretely:
     maintain the invariant that after each cut, the multiset of fragment
     values, viewed as a sequence of "gaps" between consecutive distinct
     sorted values, has strictly decreasing total variation — i.e. treat
     the n available cuts as a budget for closing n-1 "gaps" among the
     m ≥ n original sorted values (pigeonhole: m=n+1 distinct values means
     n gaps to close with n cuts — one cut per gap suffices to force ALL
     adjacent values equal, which telescopes to full pairing/cancellation).
     Make this pigeonhole argument precise and check it is legal (each cut
     must act within a single piece, not merge two separate pieces) before
     claiming it closes the residual — this is the key new idea to verify,
     not yet proved.
  4. If step 3's "close all gaps" pigeonhole argument does not go through
     legally (a real risk — cuts split one piece, they cannot merge two
     into a common value without first bisecting the larger down to the
     smaller, which may need more than one cut per gap for badly-spaced
     values), fall back to a weaker aim: show only that SOME legal
     selection rule forces a tie (or reaches T/2 exactly) using ≤n cuts for
     every marking with m=n+1 distinct pairwise-incommensurate values —
     i.e. relax "guarantee before exhaustion" to "guarantee using the full
     budget, ending exactly at a tie" — still sufficient since ending at an
     exact tie (leftover 0) or with spare budget both give Φ≤T/2<a_nT by
     step 1.
Key lemmas (claim + mechanism):
  - Equal-Pieces Closure — because m equal values pairwise-cancel
    (`pair-cancellation-identity`) or cancel after one bisection creates an
    even count, and T/2 is always strictly below the target a_nT (telescoping
    identity a_n>1/2, already certified).
  - Spare-Cut Bisection Corollary — same mechanism (create one more exact
    pair with a free cut), applied to the leftover of any process, not just
    the equal-pieces marking; this is what turns "T/2 is always safe" into a
    general reduction rather than a single stress-point fix.
  - The residual's pigeonhole reframing (step 3) — because m=n+1 distinct
    sorted values have exactly n gaps between consecutive values, matching
    exactly the n available cuts; whether "closing one gap = 1 cut" is
    always achievable legally (a cut only bisects a single piece; equalizing
    two DIFFERENT pieces to a common value requires cutting the larger one
    at exactly the smaller one's value, which is a single legal cut,
    contributing one new exact pair with the untouched smaller piece) is the
    crux to verify — this is the genuinely new content, not yet proved.
Open gaps: whether the gap-closing selection rule (step 3) is always legal
and always completes within budget n for arbitrary distinct markings; if
not, the weaker fallback (step 4) and its own proof.
Cases to cover: m even / m odd (equal-pieces, already closed); the residual
zero-tie/full-budget branch, further split (if needed) by whether all m
values are pairwise distinct (the hard case) vs. merely "no tie occurred
under naive greedy but some non-adjacent coincidence exists" (should reduce
to the distinct case via the certified pair-cancellation reduction first).
Watch out for: a cut can only act within one piece (splitting it into two
pieces) — it can never merge two pieces or directly force two DIFFERENT
original pieces to share a value without one of them being cut down to
match the other exactly; verify the "one cut per gap" accounting in step 3
respects this (cutting the larger of two pieces at the smaller piece's
value is legal and uses exactly 1 cut per gap, but only if pieces are
processed in a specific order — check the order does not conflict with
budget already spent on earlier gaps). Do not conflate "zero ties occur"
(the greedy algorithm's own runtime property) with "no two values are
close" — near-ties among incommensurate values may still admit a
"nudge to exact tie" argument different from what the pigeonhole framing
assumes; state explicitly which real markings are covered.
