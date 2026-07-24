## imo-2026-03

greedy-halving-adversary: revise
Target: The whole problem's lower bound c(n) >= 2^n/(2^{n+1}-1) (Liu Bang's
guarantee), specifically closing the remaining Claim-B sub-cases needed for
the general-n induction P(n).
Technique: exact algebraic substitution (Lemma 25 + Proposition 30) reducing
ℓ(F)=2 sub-case (b) to a band-truncation-difference inequality, closed via a
new Two-Threshold Truncated Alternating Sum Floor lemma (2-line generalization
of the certified single-threshold floor).
Skeleton:
  1. Cite Lemma 25 (certified): A(F∪G')=A(G')+A(F1∪G')-A(F2∪G') for ℓ(F)=2.
  2. Cite Proposition 30 (certified): exact closed form for A({v}∪P∪G') for
     every v in (0,p2).
  3. Substitute v=v1, v=v2 into Prop 30 and plug into Lemma 25; simplify —
     shared terms cancel, leaving a band-truncation-difference
     A(R'_{>v2})-A(R'_{>v1}) plus explicit v1,v2 terms.
  4. Recognize R'_{>v1} ⊆ R'_{>v2} (since v1>v2): the difference is the
     truncated alternating sum of the band (v2,v1].
  5. Prove NEW Two-Threshold Truncated Alternating Sum Floor lemma bounding
     this band-difference, via the same upper-truncation-identity mechanism
     that proved the certified single-threshold floor.
  6. Combine to close A(F∪G')>=f(n); if the constant from step 5 is too
     weak, fall back to route (ii): extract an explicit UPPER bound on
     A(F2∪G') from Prop 30 directly and combine additively with a lower
     bound on A(F1∪G').
Key lemmas (claim + mechanism):
  - Lemma 25 — exact identity from a direct 2-term split of F, already
    certified.
  - Proposition 30 — exact closed form via upper-truncation-identity,
    already certified.
  - NEW Two-Threshold Truncated Alternating Sum Floor — because the
    single-threshold floor's proof (apply upper-truncation-identity at one
    cut) applies identically to a sub-instance restricted to a band
    (v2,v1], treated as its own truncated residual.
Open gaps: whether the two-threshold floor's constant is tight enough
(route i) or whether route (ii)'s explicit upper bound on A(F2∪G') is
needed instead — builder must state which route actually closes the
target.
Cases to cover: ℓ(F)=2 sub-case (b) only (v1,v2<p2, no dominance) this
round. Item 4 (ℓ(F)>=3) and proposition-29b-partial-closure's flagged
proof-gap are explicitly out of scope.
Watch out for: (1) do NOT revive "peel p2 first" — round-17 explorer gave a
structural mass-count proof (Total(peeled residual) < f(n) always) that any
one-shot peel-then-floor mechanism for Target B is impossible, not just
under-optimized; this is now a certified-strength negative finding, not a
hunch. (2) the minus sign in Lemma 25 means two separate LOWER bounds on
A(F1∪G') and A(F2∪G') do NOT combine into a lower bound on their
difference — an upper bound on A(F2∪G') is specifically needed if route
(ii) is used (round-15 reviewer's standing warning, repeated here since
it's the likeliest silent-overclaim spot). (3) verify Prop 30's reference
set R' is literally the same object for both v1 and v2 substitutions before
claiming term cancellation.

lp-duality-certificate: revise
Target: The whole problem's upper bound c(n) <= 2^n/(2^{n+1}-1) (some
Xiang Yu response achieves Phi <= a_n*T for every Liu Bang marking),
specifically closing case (b2) (T/D_n < p2 < a_n*T/2, p1 < T/2), the sole
remaining open region.
Technique: an actual LP-DUAL-style certificate — a convex/weighted
combination of two already-certified primal constructions (Bisect-Top-k,
Cross-Piece-Sign-Assignment), used purely as an algebraic bounding device
(min <= any convex combination), with an explicit closed-form weight
lambda(p) as a function of the marking — genuinely untried in this
polarity despite the slug's name (every prior attempt was a single primal
strategy, never a combination).
Skeleton:
  1. Cheap-kill first (~10 min numeric check, not a proof step): does a
     fixed simple rational weighting (e.g. 50/50 Bisect-Top-1 vs
     Cross-Piece j=1) already cover the R16.3 uncovered grid points? If
     yes, the target collapses to proving a much simpler fixed-weight bound.
  2. Cite bisect-top-k-lemma (certified): Phi_BTk = (T+A(tail))/2 <=
     (T+p_{k+1})/2.
  3. Cite Cross-Piece Sign-Assignment Identity (certified): Phi_CP =
     (T+sum eps_i p_i)/2 exactly, for a legal sign-respecting split.
  4. New step: prove min(Phi_BTk,Phi_CP) <= lambda*Phi_BTk +
     (1-lambda)*Phi_CP <= a_n*T for every marking in case (b2)'s box, for
     an explicit lambda(p1,...,pm,T) in [0,1] — NOT a claim Xiang Yu
     randomizes; a pure inequality-chaining device.
  5. Solve for lambda(p) explicitly as a linear function of the marking by
     equating the two strategies' worst-case values (linear algebra, not
     search); derive for n=3,4 first, then attempt general n.
  6. Verify against both round-14 hard witnesses and the round-17
     explorer's 15-point scan; confirm no regression vs. the
     already-unconditional coverage.
Key lemmas (claim + mechanism):
  - bisect-top-k-lemma, Cross-Piece Sign-Assignment Identity — both
    already certified, cited not re-derived.
  - NEW Weighted-Combination Bound — because min(A,B) <= any convex
    combination of A,B is a trivial but load-bearing fact; the real
    content is finding an explicit lambda(p) that makes the RHS <= a_n*T
    everywhere in case (b2)'s box.
Open gaps: whether an explicit closed-form lambda(p) exists covering the
whole box; whether 2 strategies suffice or a 3rd (Iterated Greedy-Peel) is
needed.
Cases to cover: case (b2)'s box only; do not re-attempt case (a)/(b1)
(closed) or re-derive round 16's sign-convention fix.
Watch out for: (1) the aimo-0560 "strengthen-the-adversary" transplant is
now CONFIRMED not applicable (one-shot Stackelberg vs. the crux's
multi-round replay/pigeonhole mechanism) — do not pursue it, it is a
closed dead end this round, not merely deprioritized. (2) the weighted
combination is an algebraic device only, not a randomized-strategy claim —
keep the writeup from drifting into expected-value language, since the
true game is one-shot worst-case. (3) if the right pair of strategies to
combine turns out to vary discontinuously across case (b2)'s box, the
outline may need an internal case-split — report this honestly rather than
forcing one fixed pair to work everywhere. (4) don't treat the explorer's
15-point n=3 numeric scan (no second tight point found) as proof of
general-n coverage — it is a sanity check only, the algebraic lambda(p)
construction is the actual proof obligation.
