## imo-2026-03

greedy-halving-adversary: revise
Target: c(n) = 2^n/(2^{n+1}-1) — Claim B (full lower bound: refining Xiang
Yu's tail never drops Liu Bang's total below f(n)), as part of the overall
c(n) equality. This round's precise sub-target: close ℓ(F)=2 sub-case (b)'s
remaining range v1 ∈ (s,p2) (Theorem 32(ii)), which is now confirmed
(4 independent angles across rounds 15-17, re-confirmed this round's
explorer) to be THE single bottleneck for the whole lower-bound front.
Technique: exact-substitution reduction (Lemma 25 + Proposition 30, already
certified) to a single COUPLED inequality, then close that inequality via a
charging/pairing argument on individual Xiang-Yu tail cuts (crux
`aimo-0146`-style exchange/charge technique, genuinely new vocabulary for
this front — every prior attempt used integral/alternating-sum identities
directly, not a per-cut charge).

**Corrected diagnosis (from this round's explorer, must be used verbatim,
not re-derived): the missing ingredient is NOT a context-free bound on
A(R'_{>v}) alone.** The crude context-free ceiling is provably exactly
q_1 (top piece of the (n-2)-ladder tail) — too weak, already known. What
Theorem 32(ii) actually needs is a bound on the COUPLED quantity
D(v1,v2,R') := A(F2∪G') where F2={v2}∪P is tied to v1 and R' by a single
shared mass-conservation constraint (v1+v2+Total(P)=p1, and G'/R' is the
SAME tail refinement instance for both F1={v1}∪P and F2={v2}∪P). Equivalently
(Lemma 25 + Prop 30 algebra, already worked out in the round-17 outline)
this is a LOWER bound on the band quantity
I1 := A(R'_{>v2}) − A(R'_{>v1}) = ∫_{v2}^{v1} u_{R'}.
The round-17 "Two-Threshold Truncated Alternating Sum Floor" lemma
(I1 ≥ −(v1−v2)/2) is exactly this bound, already proved and already what
closed v1≤s — but it is too weak once v1 gets close to p2 (the band
(v2,v1] can then be almost the whole tail-scale range, and −(v1−v2)/2
is not tight enough against f(n)). The task this round is to find a
SHARPER band-lower-bound for the specific regime v1 ∈ (s,p2), not to
re-derive a new "A(R'_{>v}) ceiling" from scratch.

Skeleton:
  1. Cite Lemma 25 (certified, exact, general): A(F∪G')=A(G')+A(F1∪G')−A(F2∪G').
  2. Cite Proposition 30 (certified, exact, all v∈(0,p2)):
     A({v}∪P∪G') = p2−v+A(R')−2A(R'_{>v})+2v·ε(v).
  3. Cite the already-proved algebraic simplification (round 17, step 3):
     A(F∪G') = A(G') + (v2−v1) + 2 I1 + 2(v1ε(v1)−v2ε(v2)), where
     I1 = A(R'_{>v2})−A(R'_{>v1}).
  4. **New key step**: prove a sharper, v1-dependent lower bound on I1 for
     v1 ∈ (s,p2), via a charge/pairing argument on the tail's OWN cut
     sequence rather than a single flat constant. Concretely: process
     R'/tail construction cut-by-cut (in the order Xiang Yu legally makes
     them, or equivalently by descending piece rank); each cut either (a)
     splits a fragment straddling the band (v2,v1], contributing a
     specific signed charge to I1 that can be bounded below by the piece's
     own contribution to the band's total mass, or (b) lies entirely
     inside or outside the band, contributing 0 or a boundable amount.
     Sum the charges: since the band (v2,v1] has width bounded below by
     (v1 − s) when v1>s (using v2<s automatically since sub-case (b) has
     v2<v1), derive I1 ≥ g(v1,s,p2) for an explicit function g sharper
     than the flat −(v1−v2)/2 near v1=p2.
  5. Substitute the sharpened bound into step 3's identity, combine with
     the certified lower bound on A(G')+... (already available from the
     Truncated Alternating Sum Floor applied at v2, since v2≤v1<p2 also
     lies in the already-covered sub-range whenever v2≤s), and verify the
     resulting inequality meets A(F∪G')≥f(n) for the FULL range v1∈(s,p2),
     not just an improved-but-still-partial sub-range.
  6. If step 4's charge bound is not tight enough for the whole range,
     narrow explicitly: report exactly which residual sub-range of
     v1∈(s,p2) remains open (do not claim full closure unless step 5's
     algebra genuinely closes for every v1 in the range) — a partial
     closure of (s,p2) that strictly extends beyond v1≤s is still real,
     reportable progress even if not complete.

Key lemmas (claim + mechanism):
  - Lemma 25, Proposition 30 (already certified) — cited, not re-derived.
  - **NEW: Sharpened Band Floor via Cut-Charging.** I1 = A(R'_{>v2})−A(R'_{>v1})
    ≥ g(v1,s,p2) (explicit, v1-dependent, strictly sharper than the flat
    −(v1−v2)/2 near v1=p2) — because each individual Xiang-Yu cut on the
    tail can be charged to its net effect on the band's alternating sum,
    and the total charge is bounded using the tail's own total mass budget
    s and the specific position of v1 relative to s (not just the raw
    band width v1−v2), giving more information than the width-only floor.

Open gaps: whether the charging argument in step 4 actually produces a
bound sharp enough to close the FULL range v1∈(s,p2) (this is genuinely
open — the explorer's numeric probe did not find the exact extremal
witness for this range; the builder should compute it, exact-Fraction,
small n, before committing to a specific closed-form g).

Cases to cover: v1 ∈ (s,p2) only (v1≤s already closed by Theorem 32(i)).
ℓ(F)≥3 remains explicitly out of scope.

Watch out for:
  - Do NOT revive "peel p2 first" (proven structurally dead by mass-count,
    round 17) or the plain unconstrained/floor-constrained vertex-max of
    A(R'_{>v}) alone as a standalone target — BOTH confirmed too weak this
    round (context-free ceiling = q1; floor-constrained LP does not move
    the ceiling, 60k-80k-trial numeric confirmation). The target is the
    COUPLED quantity I1/D(v1,v2,R'), tied via p1's mass conservation, not
    an isolated A(R'_{>v}) bound.
  - Do NOT apply Half-Dominance Split Bound (Theorem 29) directly to
    F∪G' expecting it to close this gap — it gives an unconditional but
    WRONG-DIRECTION (upper) bound A(F∪G')≤p2+A(R'), useless for this
    lower-bound target; record it only as a documented consistency fact if
    the builder needs a sharpness check, not as a route to closure.
  - Verify the shared-R'-instance hypothesis (Prop 30 applied at v1 and
    v2 must use the literal same tail refinement) explicitly before
    trusting step 3's cancellation, per round-17's own warning.

lp-duality-certificate: revise
Target: c(n) = 2^n/(2^{n+1}-1) — the general upper bound c(n) ≤ a_nT for
arbitrary Liu Bang markings, every n. This round's precise sub-target:
case (b2) = {p1<T/2} ∩ {T/D_n < p2 < a_nT/2}, the sole remaining open
region after Theorem A / case (b1) / case (a); the ENTIRE peel/bisect/
recurse family and the entire weighted-combination family are now proven
(not suspected) incapable of reaching it.
Technique: a genuinely new mechanism — a smoothing/exchange-majorization
argument over LIU BANG's own tail-marking freedom (not Xiang Yu's response
space, which every existing lemma in this front already smooths over).
Adapted from crux `aimo-0560`'s "replace the adversary with a coarser but
dominant surrogate" move, reproven from scratch for this game's continuous
move structure (the crux's discrete-grid mechanism does not transplant
mechanically).

Skeleton:
  1. Fix p1,p2 inside case (b2)'s box and Xiang Yu's cut budget n. View
     Φ_min(p1,p2,tail-shape) as a function of Liu Bang's remaining free
     choice — the tail marking (p3,...,p_{n+1}), an (n-2)-dimensional
     simplex with fixed total s=T−p1−p2 — where Φ_min itself is already a
     min over Xiang Yu's legal cut compositions for that fixed marking
     (standard minimax value, well-defined since the response set is a
     compact polytope, per the already-certified vertex-minimum-theorem
     machinery run in reverse).
  2. **New key lemma — Tail Exchange Lemma**: for any two of Liu Bang's
     tail marks p_i, p_j (i≠j), the perturbation p_i → p_i+ε, p_j → p_j−ε
     (holding all other marks and the total s fixed) is a LEGAL alternative
     marking (both remain positive lengths summing to s — Liu Bang's
     marking freedom is unconstrained ordering/positivity, unlike Xiang
     Yu's "legal refinement," which must literally cut existing pieces).
     By Danskin's/the envelope theorem for a min over a compact polytope,
     the one-sided directional derivative of Φ_min(ε) at ε=0 is bounded by
     the min, over Xiang-Yu-optimal responses achieving the min at ε=0, of
     the corresponding partial derivative of the underlying (fixed-response)
     value — i.e. the derivative is controlled by which piece(s) the
     currently-optimal Xiang Yu response actually cuts through.
  3. Use step 2 to show: at any marking maximizing Φ_min over tail shapes
     (the actual object Liu Bang wants, since he wants the WORST case for
     Xiang Yu forced-minimum to be as large as possible), EITHER (a) two
     tail marks can be perturbed with non-negative one-sided derivative in
     a mass-increasing direction without violating positivity, contradicting
     maximality unless a first-order stationarity/tie condition holds
     between them, OR (b) the maximizing tail configuration is at a
     boundary of the simplex (some p_i → 0), which reduces the tail's
     dimension by one — an induction on the number of nonzero tail marks.
  4. Characterize the interior stationarity condition from 3(a) explicitly
     (this is the crux new content): what relation between p_i,p_j must
     hold at a stationary point, in terms of how Xiang Yu's optimal
     response currently treats those two pieces (tied fragments? one
     untouched?). This should collapse the (n-2)-dimensional continuum to
     a low-dimensional (ideally O(1)-parameter, or fully finite) family via
     repeated application across pairs — the dimensional collapse case
     (b2) needs.
  5. Enumerate/bound Φ_min over the resulting collapsed family directly
     (reuse Bisect-Top-k / Cross-Piece-Sign-Assignment / existing explicit
     strategies as candidate Xiang Yu responses at each point of the
     collapsed family) and check it never exceeds a_nT.

Key lemmas (claim + mechanism):
  - Tail Exchange Lemma (new) — because Liu Bang's tail-marking freedom is
    a genuinely unconstrained simplex (unlike Xiang Yu's cut-refinement
    freedom), a mass-transfer perturbation between two tail marks is
    always legal, letting Danskin's theorem bound Φ_min's derivative by
    the derivative at the currently-active optimal response(s).
  - Interior Stationarity Characterization (new, the hard step) — because
    at a maximum the one-sided derivative in every legal direction must be
    ≤0, forcing a tie/complementary-slackness-style condition between
    whichever tail marks are perturbed and the currently-optimal response's
    treatment of them.

Open gaps: step 4's exact stationarity condition is not yet derived (this
round's explorer only has noisy numeric evidence — worst tail ratio ≈1.8,
not exactly the ladder ratio 2, DE not fully converged, single point only)
— treat any small-case numeric ratio as a hint for what the stationarity
condition should look like, not as the condition itself; verify it
symbolically (exact-Fraction / Sympy) at n=3 (only one free tail parameter,
the simplest genuine test) before attempting general n. Whether the
resulting collapsed family (step 4-5) is small enough to check directly is
also open — a cheap-kill check (from the explorer's own report): confirm
first whether even n=3's single-parameter tail admits a clean closed-form
stationary point; if not, the general-n characterization is likely out of
reach this round and the approach should report the Exchange Lemma itself
(step 2, unconditional, general) as this round's certified partial result
rather than force a full closure.

Cases to cover: n=3 as the minimal genuine test (only one free tail
degree of freedom) before attempting general n. Boundary case 3(b)
(some p_i→0, dimension-reducing induction) must be handled explicitly,
not silently assumed absorbed into 3(a).

Watch out for:
  - Do NOT retry any peel/bisect/recurse variant, "adaptive/position-
    dependent peel target" (proven a special case of the already-dead
    recursive-image-escape mechanism — any construction whose only lever
    is "steer the recursed image into an already-solved case" is capped
    at the same zero-slack ceiling a_{n-1}T', regardless of how the target
    is chosen), or any weighted/convex combination of primal strategy
    values (Convex-Combination Futility Theorem, proven dead for ANY
    weighting rule, fixed or p-dependent) — all three families are
    CONFIRMED DEAD for case (b2), not just unpromising.
  - Do NOT pursue a pure boundary-continuity/compactness argument on p2
    alone ("Φ_min is small at both walls of the p2-interval, hence small
    throughout") — this round's explorer found Φ_min as a function of
    TAIL SHAPE (not just p2) is not monotone/concave (numeric bump at an
    interior ratio ≈1.8 above both neighbors), so a naive one-variable
    boundary-pins-interior argument is not credible without exactly the
    two-variable joint exchange argument this outline already proposes —
    don't waste a round rediscovering that these coincide.
  - This is a genuinely ambitious new mechanism for one round; if step 2
    (Tail Exchange Lemma) is the only piece fully closed, that is still
    real, novel, certifiable progress (a new general tool nothing on file
    currently has) — report it honestly rather than forcing an incomplete
    step 4 characterization to look closed.

rank-pigeonhole-budget: advance
Target: (already fully closed — Claim (A), all n, both directions,
APPROVE round 8). No further action needed this round; kept live in the
population as the certified-milestone anchor other fronts cite (Theorem
GC(m), Case I Closure Theorem, exchange-smoothing-vertex-maximization) —
nominate for re-ranking only, no new build needed unless a sibling's
progress this round creates a new sub-target that naturally belongs here
(e.g. if front 2's Tail Exchange Lemma needs the vertex-minimum-theorem
machinery reused/dualized once more).
