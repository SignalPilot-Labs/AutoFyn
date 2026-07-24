## imo-2026-03

rank-pigeonhole-budget: advance
Target: the actual problem's claim c(n) = 2^n/(2^{n+1}-1), via this
approach's own sub-target (star_3)=MinFloor(4), which by the certified
Index-Chain Identity is definitionally equivalent to the project's central
open (star_k), k>=3 obstruction at k=3.
Technique: direct finite-shape/vertex enumeration (Vertex-Minimum Theorem
confines the minimizer of A(U) to a tie/degenerate-cut vertex over a
budget-<=3, 4-piece object), the exact method that already closed
MaxCeil(3)/MaxCeil(4) — not a self-similar rescaling (that route is doubly
confirmed dead).
Skeleton:
  1. Enumerate the 20 legal cut-distribution shapes (k1,k2,k3,k4),
     sum<=3, over the unit 4-ladder (8,4,2,1)/15 — by direct
     stars-and-bars combinatorics.
  2. Cheap-dispatch every shape via sharp-dominant-removal-identity +
     Fact 1/Fact 2 (A>=0, A<=Total), already certified.
  3. For the 2 shapes numerically identified as exactly tight,
     (3,0,0,0) [reuses Claim-(A)'s optimal witness] and (2,0,1,0) [a
     genuinely new tie configuration], do the full breakpoint/
     piecewise-linear sweep (Insert-Element-Identity + odd-run-reduction-
     lemma) to get an exact equality derivation, not just an inequality.
  4. Confirm all remaining shapes close by the step-2 cheap dispatch
     alone; name every shape explicitly per the project's write-up
     convention (no silent batching).
  5. Conclude (star_3), hence MinFloor(4), fully closed both branches.
Key lemmas (claim + mechanism):
  - Shape enumeration is exhaustive and finite (20 shapes) — because the
    Vertex-Minimum Theorem confines the minimizer to a tie/zero-fragment
    vertex, collapsing a continuum optimization to a finite discrete
    case split.
  - Shapes (3,0,0,0) and (2,0,1,0) are exactly tight at value 1/15 — the
    first reuses the already-certified Claim-(A) optimum; the second is
    new content, a tie configuration touching pi_1 and pi_3, not yet
    derived anywhere on file.
Open gaps: the exact derivation for shape (2,0,1,0) is new work.
Cases to cover: all 20 shapes, individually.
Watch out for: do not attempt any rescaling reduction of (star_3) to a
smaller (star_k) instance (confirmed dead twice, round 23); do not
conflate with the already-closed dual quantity MaxCeil(4).

greedy-halving-adversary: revise
Target: the actual problem's claim c(n) = 2^n/(2^{n+1}-1), via this
approach's own sub-target Claim (B) — specifically closing h(m), the
"T'-cuts-p4" branch of Case (b)'s "v>=a" branch, for general m (not just
m<=2).
Technique: adapt the already-certified Theorem 40/41 rank-split mechanism
(insert-element-identity applied at the tie point, then bound the two
resulting halves H,L separately by trivial per-piece bounds) — proved
once, general n, on the structurally analogous "T'-untouched" branch's own
deep-tie residual — to h(m)'s deep-tie residual. This is a genuinely
different target than re-running the per-shape exhaustive technique at
m=3 (confirmed by the explorer's direct shape-count blow-up: 4 shapes at
m=2, 15 at m=3, 56 at m=4, each with more free continuous parameters per
branch — per-m grinding does not scale and is exactly the trap the
shared-gap-plateau rule warns against).
Skeleton:
  1. Restate the target: at any deep-tie vertex c=t* in S (t* neither the
     boundary 0/q1 nor the top-tie max(S)), show A({c}∪S)>=f(m) — by
     Vertex-Minimum Theorem + odd-run-reduction-lemma.
  2. Rank-split S\{t*} into H (elements > t*) and L (elements < t*) via
     insert-element-identity (general, multiset-agnostic — not
     ladder-specific to m=2).
  3. Bound H and L separately by trivial per-piece bounds (Fact 1, Fact
     2), exactly the mechanism (not lump-bounding the whole residual
     tail) that let Theorem 41 avoid an unproven upper bound on a
     same-size self-similar instance.
  4. Combine into one m-uniform inequality chain, using the ladder's own
     doubling q_i=2q_{i+1} to make the domination hypothesis automatic
     (mirrors Theorem 40/41's use of p4=2p5).
  5. Combine with Theorem 38's already-closed base vertices to conclude
     h(m)>=f(m) for every m>=1.
Key lemmas (claim + mechanism):
  - Deep-tie vertices reduce to a rank-split exactly as in Theorem
    40/41 — because insert-element-identity is general, not tied to any
    specific m's arithmetic.
  - Domination is automatic from ladder doubling q_i=2q_{i+1}
    (general-ladder-dominance, already certified).
Open gaps: whether the per-piece bounds on H,L actually close the
inequality for h(m)'s object is genuinely new — h(m)'s object (a free
coordinate inserted into an (m-1)-cut-budget tail) differs structurally
from Theorem 40/41's fixed-anchor object, so this check cannot be assumed
free.
Cases to cover: the deep-tie vertex family (main target); confirm
Theorem 38's base vertices still cover c in {0,q1} and c=max(S).
Watch out for: do not make per-m exhaustive shape enumeration the primary
target (confirmed to not scale past m~3); if the general mechanism
stalls, a fallback h(3)-only closure is acceptable but must be flagged as
"one more level," not conflated with general-m progress. Do not assert
"worst c is always top-tie" (confirmed false, ~3.7% of trials). Do not
re-attempt "h(m) as a disguised (star_{m-2}) corollary" (Proposition 39,
confirmed dead) or "single global rescaling of the whole T'-cuts-p4
sub-case" (round 23, confirmed dead twice) — the rank-split-at-a-vertex
idea is a different, local mechanism, not barred by either dead end.

lp-duality-certificate: revise
Target: the actual problem's claim c(n) = 2^n/(2^{n+1}-1), via this
approach's own sub-target, the general upper bound c(n)<=a_n for arbitrary
markings — specifically closing the p1>=T/2 regime of n=4 (c(4)<=16/31)
"for free" by re-running the certified Theorem C'/Theorem A argument one
index up, now that round 27 closed P(4) (the complete n=3 upper bound,
both regimes) — the exact missing prerequisite. Chosen over pivoting to
the n=3 lower bound because that front is the identical central
obstruction (star_k)/Claim (B) the two sibling approaches already own —
opening it here would collapse this file's diversity onto the shared
wall; the n=4 upper-bound bootstrap stays on this file's own distinct
front and is genuinely near-mechanical.
Technique: substitution/re-indexing of already-general-n theorems
(Theorem A Full-Match, Theorem C' bisect-and-recurse), not new machinery.
Skeleton:
  1. T/2<=p1<a4*T: close via Theorem A (general-n, pure re-instantiation
     at n=4).
  2. p1>=a4*T: close via Theorem C', whose sufficient condition is
     "P(n-1) fully closed" — instantiate at n=4, consuming round 27's
     now-complete P(4) as the induction hypothesis.
  3. Combine via the already-certified telescoping-threshold-identity
     (a_{n-1}=a_n/(2(1-a_n))), confirming the two sub-case domains meet
     with no gap and no overlap.
  4. State precisely what remains open: p1<T/2 at n=4 (the hard,
     must-redo chamber census; not attempted this round).
Key lemmas (claim + mechanism):
  - Theorem A and Theorem C' transplant to n=4 verbatim — both are
    already stated/proved for arbitrary n, no n=3-specific arithmetic
    baked in; only the P(n-1) hypothesis they consume was previously
    unavailable at this level.
  - Telescoping threshold identity places the two sub-case domains
    exactly end-to-end — already certified, reused not re-derived.
Open gaps: verify (do not assume) Theorem C''s proof never secretly used
n=3-specific constants (D3=15, a3=8/15) rather than "P(n-1)'s threshold"
abstractly — a concrete re-indexing risk to check explicitly.
Cases to cover: T/2<=p1<a4T (Theorem A), p1>=a4T (Theorem C').
Watch out for: do not claim this closes c(4)<=a4 in general — p1<T/2 is
untouched and, per the density-growth signal (28%->64% between n=3,4
chamber censuses), expected to need substantially more work than a repeat
of n=3's chamber count. Re-verify Theorem C''s "P(n-1) fully closed"
hypothesis genuinely means the complete n=3 theorem (both regimes), not
just case (a) or (b1) — a real coupling per round 9's finding, not a
formality.
