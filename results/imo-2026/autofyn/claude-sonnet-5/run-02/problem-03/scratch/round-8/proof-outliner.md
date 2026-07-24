## imo-2026-03

### Context read: the gap and why round-8's two explorers converge

Sub-case (†) (rank-pigeonhole-budget.md §4.8-4.9, Branch B of peel-the-
global-minimum, N=m+k even) is diagnosed by BOTH round-8 explorers as an
**exact identity, not a reducible sub-claim**: peeling μ=min(F) from an
even-sized S shifts nothing else (μ sits at the last, even rank), so
"E(F'∪τ)≤R(τ)-μ" is algebraically the SAME statement as the target
D(S)≥0, not a smaller instance. Peeling two elements at once reproduces
the identical wall one level down (alt-induction explorer, verified by
direct computation). Any Δ-invariant of the form h=min(S)·[N even] is
refuted at the base case. LP-duality's bounded/context-free certificate
vocabulary is shown (dagger-attack + alt-induction explorers,
independently) to be **structurally incapable** of covering the tight
c_1=2 witness (n=3, F={4,2,2}/15, exact equality) — any certificate that
closes it must smuggle in A(G')'s exact recursive value, i.e. is the
induction in disguise. **Conclusion for this round: do not field another
same-mechanism variant of peel-induction on raw N, and do not ask
lp-duality-certificate to patch its atom basis for Case I** — both are now
confirmed, not just suspected, dead ends for this specific sub-target.
Two genuinely different mechanisms are on offer instead: (1) exchange-
smoothing/vertex-maximization of E(F∪τ) directly (bypasses peel-induction
entirely; crux aimo-0146 transplant), and (2) induction on the
odd-run-reduced size |S'| instead of raw N (untested, flagged as possibly
hitting a symmetric wall but structurally distinct). I field one approach
per mechanism, plus advance the two live approaches whose real work this
round is orthogonal to (†) (Claim B, and the still-open general upper
bound for n≥3) rather than starving them by piling everyone onto the same
wall a fifth time.

---

rank-pigeonhole-budget: revise
Target: c(n) = 2^n/(2^{n+1}-1) — specifically this round's contribution is
closing Claim (A)'s Case I in full (equivalently E(F∪τ)≤R(τ) for every
ratio-2 superincreasing tail τ and every partition F of s∈(0,2τ_1] into
≤m+1 parts with max(F)≤τ_1), which subsumes (†) as one sub-case rather
than treating (†) in isolation.
Technique: Exchange-smoothing maximization of E(F∪τ) directly over the
simplex of legal F, bypassing the peel-the-minimum induction entirely —
adapted from the crux aimo-0146 (extremal-principle/double-counting)
exchange-smoothing-to-plateau-profiles mechanism.
Skeleton:
  1. Restate the target as (4.3) in the file: E(F∪τ)≤R(τ). Fix m,k,s,τ.
  2. Observe: within any fixed combinatorial "sorted-order type" (which
     positions the m tail values and k free F-values interleave into),
     E(F∪τ)=Σ_i w_i·F_i is a LINEAR functional of F's free coordinates
     (w_i∈{0,1} = indicator that F_i's fixed order-position is an even
     sorted rank) — order type only depends on which inequalities hold
     among the values, not their magnitudes, so within one order-type
     region E is literally linear.
  3. The feasible region for F (sum = s, 0≤F_i≤τ_1, ≤m+1 parts) is a
     compact polytope (bounded box ∩ a hyperplane). A linear functional on
     a compact polytope attains its MAXIMUM at a vertex — cite the same
     standard convex-polytope fact `vertex-minimum-theorem` already
     proved for the minimum; state explicitly that the identical argument
     (affine objective, compact polytope) gives the maximum too, so this
     is a genuine reuse, not a re-derivation from scratch — by tool/
     theorem: standard LP vertex-extremum fact (cite `vertex-minimum-
     theorem`'s proof verbatim with min→max).
  4. Characterize the vertices using the exchange-smoothing lemma (adapt,
     not cite, from aimo-0146): if two free coordinates F_i>F_j lie in an
     interior configuration where F_i's weight w_i ≤ w_j (i.e. moving mass
     from the higher-weight to lower-weight coordinate is available and
     would only help if reversed), the move (F_i,F_j)→(F_i-ε,F_j+ε) or its
     reverse strictly changes E monotonically in the direction of
     increasing weighted mass — repeat until no such move exists. Terminal
     configurations are exactly: two F-values tied to each other, one
     F-value forced to 0 (degenerates k→k-1), or one F-value forced to τ_1
     (boundary, connects to Branch-A/Case-II structure already closed).
  5. Enumerate the finitely many resulting vertex TYPES (bounded by k,m)
     and evaluate E at each via the certified `odd-run-reduction-lemma`
     closed form; compare each to R(τ).
  6. Cross-check: the certified achievability construction F* (§2 of the
     file, "pairs cancel, one leftover triple") is exactly a plateau
     profile of the shape step 4 predicts — verify it recovers as the
     extremal (equality) vertex, not merely a feasible point, confirming
     the enumeration is complete and correctly identifies the true
     maximum, not just a critical point.
Key lemmas (claim + mechanism):
  - Linearity-in-order-type: E(F∪τ) restricted to one sorted-order region
    is linear in F's free coordinates — because a value's contribution to
    E depends only on its rank position, which is locally constant as
    long as the relative order among all values doesn't change.
  - Exchange-smoothing terminal-plateau lemma (aimo-0146 transplant):
    repeated weight-favoring exchanges on a fixed-sum sequence terminate
    in finitely many steps at a configuration with no further strictly
    improving exchange — because each exchange strictly increases (or
    leaves unchanged, at which point the search stops) a bounded objective
    over a compact discrete-vertex set.
  - Max-attained-at-vertex (reuse): same proof as `vertex-minimum-theorem`
    with min replaced by max — a linear functional on a compact polytope
    attains its extrema (both directions) only at vertices of the
    polytope's facet structure.
Open gaps: whether the exchange-smoothing terminal set coincides exactly
with the polytope's LP-vertices (should be true by standard theory but the
builder must state this precisely, not wave at it); full enumeration and
evaluation of every vertex type for general m (not just the specific (†)
branch); confirming F* is the unique maximizer (or one of finitely many
tied maximizers) rather than merely a local plateau.
Cases to cover: vertex types split by (a) how many F-values tie to each
other, (b) whether an F-value degenerates to 0, (c) whether an F-value
saturates to τ_1 — must show these are jointly exhaustive.
Watch out for: this is a MAXIMIZATION of E (upper-bound target), the
opposite polarity from `vertex-minimum-theorem`'s original min-of-Φ use —
double check the theorem's proof genuinely doesn't use a min-specific
step (it shouldn't, it's a generic LP-vertex fact, but verify explicitly
rather than assuming). Also verify the m+1-part budget constraint is
correctly encoded as a polytope facet (not silently dropped), since
round 6 already found the unrestricted-part-count version is FALSE.

---

rank-tie-vertex-reduction: revise
Target: c(n) = 2^n/(2^{n+1}-1) — this round's contribution is the general
c_1≥2 case (Xiang Yu spends ≥2 cuts fragmenting p_1 itself), which is the
same underlying wall as (†) in different notation (confirmed identical by
round-7's Case-II-Exact-Peel-Identity diagnosis and round-8's explorers).
Technique: strong induction on ℓ(S):=|S'|, the size of the ODD-RUN-REDUCED
multiset (via the certified `odd-run-reduction-lemma`, which collapses
even-multiplicity value-runs since matched pairs contribute 0 to A) —
instead of inducting on raw element count N. This is a genuinely
different induction variable never tried by any approach on file: N's
parity is an artifact of raw count, while ℓ's parity tracks the "surviving
structure" after cancellation, and peeling one element can change ℓ by 0
or 2 (not always 1), potentially decoupling ℓ's parity from the exact
rank-shift trap that stalls peel-the-min on N.
Skeleton:
  1. Recall `odd-run-reduction-lemma`: A(S)=A(S') where S' is S with every
     maximal run of an even-multiplicity value removed entirely (pairs
     cancel exactly).
  2. Define ℓ(S):=|S'| as the induction variable for the target
     A(F∪τ)≥s-R(τ) (equivalently the c_1≥2 domination statement).
  3. Base cases ℓ=0 (S'=∅, i.e. S is entirely pairable): A(S)=0 directly;
     verify the target's RHS is ≤0 in every configuration that can reach
     this base case (needs an explicit check, not assumed).
  4. Base case ℓ=1 (S' is a single value v): A(S)=v exactly by definition
     of A on a singleton; verify target directly.
  5. Inductive step: given S=F∪τ with ℓ(S)=ℓ≥2, exhibit an explicit
     operation removing exactly 2 elements from S' — the two lowest
     surviving reduced values (candidates: (a) the two smallest elements
     of S' if both come from F, i.e. a genuine within-F cancellation
     candidate; (b) the smallest element of F' paired against the
     smallest surviving tail value if they happen to coincide) — track
     precisely how this changes the target's RHS s-R(τ) and set up the
     matching sharper hypothesis needed (this is new content, not yet
     derived by anyone — the builder's first job).
  6. Combine with the certified achievability (§2) and Case II closure
     (Theorem GC(m), already proved for all n) to close the full lower
     bound once step 5 succeeds.
Key lemmas (claim + mechanism):
  - Reduced-instance reformulation: A(F∪τ)=A((F∪τ)') where the RHS uses
    the odd-run-reduced multiset — because cancelling matched pairs is an
    exact, mechanism-neutral operation (already certified), so all of the
    "hard" combinatorial content of A lives in S' alone, and the
    superincreasing tail τ, being generically all-distinct, only
    participates in a reduction-pair when it exactly ties an F-value —
    an event the builder must characterize (does this only happen at
    genuine Branch-A-type ties, or can it happen deep inside Case I too?).
  - (To be constructed by the builder, NOT assumed true yet) A
    ℓ-indexed slack invariant g(ℓ) with E(F∪τ)≤R(τ)-g(ℓ), chosen so a
    2-element reduced-peel decreases g by an amount that exactly absorbs
    the removed mass — this is the actual open content of the approach;
    the skeleton above only sets up the induction scaffold.
Open gaps: the entire inductive step (5) is unconstructed — this is
explicitly flagged by the explorer as untested and possibly hitting a
symmetric obstruction; the builder's job is to attempt it honestly on
small cases (n=3,4,5 by hand/exact-Fraction) FIRST, and report a clean
negative result (with the specific reason it fails) if it reproduces the
same exact-identity trap, rather than forcing an unconvincing partial
proof.
Cases to cover: whether S''s reduced pair always comes from within F, from
F tying τ, or can involve 3+ way ties (needs the general `odd-run-
reduction-lemma`, not just the pairwise case).
Watch out for: the alt-induction explorer explicitly warns this may hit an
analogous symmetric wall one level down — if the builder finds this, it
must be recorded as a genuine (third) confirmation of the same
obstruction under yet another name, not silently abandoned or reframed
as success.

---

greedy-halving-adversary: advance
Target: c(n) = 2^n/(2^{n+1}-1) — this round's contribution is closing the
weaker, correctly-restated Claim (B): refining Xiang Yu's tail cuts (on
top of however he splits p_1) can never push A below Claim (A)'s value
a_n — needed because Claim (A) alone only covers "all n cuts spent on p_1,
tail untouched"; combining with whichever sibling closes Case I this round
gives the full general lower bound. (Claim B as originally, unrestricted,
stated is already REFUTED — round 5, do not re-attempt that form.)
Technique: chain the certified `single-cut-perturbation-identity` (Lemma
14) over a sequence of tail cuts, using the ladder's ratio-2 spacing to
show each additional split, when F is at or near Claim (A)'s optimum,
lands its perturbation window in a provably safe (compensating) band.
Skeleton:
  1. Recall Lemma 14: splitting one element M into f_1≥f_2 changes A by
     an explicit difference of two odd-parity-indicator integrals over
     two windows of total length 2f_2 in the rest of the multiset.
  2. Structural lemma (new, to construct): for F at or within a bounded
     neighborhood of Claim (A)'s optimal configuration (F* or GC(m)'s
     tight case), and any tail piece p_i (i≥2) being split, show the two
     Lemma-14 windows land entirely within a single "safe" region relative
     to the ladder's p_i=2p_{i+1} spacing — by tool: direct case analysis
     using the ratio-2 identity (every p_i exceeds the sum of everything
     below it, so a split of p_i can only interact with pieces strictly
     smaller than p_i, bounding where the windows can fall).
  3. Strong induction on the number of tail cuts made so far: base case 0
     tail cuts is exactly Claim (A) (owned by the sibling); inductive step
     applies step 2's structural lemma to show one more tail cut cannot
     push A below a_n, regardless of cut order — by tool: Lemma 14 +
     step 2, summing nonnegative/bounded per-cut perturbations.
  4. Combine with Claim A (Case I + Case II, once closed) via the
     project's decomposition (F ∪ tail-refinement, arbitrary split of
     Xiang Yu's n cuts between the two) to state the full general lower
     bound.
Key lemmas (claim + mechanism):
  - Safe-window structural lemma (new): because the ladder is
    superincreasing with ratio exactly 2, p_i > Σ_{j>i} p_j always, so any
    split of p_i creates fragments whose perturbation windows (length
    ≤p_i) cannot reach past p_{i-1}'s boundary — this pins the affected
    parity band to a controllable local region, unlike an arbitrary
    (non-ladder) multiset where Lemma 14's window could span anything.
  - Ordering-independence of chained perturbations (to construct): the net
    effect of applying several single-cut perturbations does not depend
    on the order they're applied in, for the ladder's specific structure
    — needed to reduce "many cuts" to "one cut at a time" cleanly; not
    yet proved, must be checked (commutativity is NOT automatic for
    Lemma 14's window-integral formula in general).
Open gaps: step 2's structural lemma is new and unconstructed; step 3's
ordering-independence is unverified and may fail (if it does, an explicit
worst-case cut ORDER must be identified and shown to still respect the
bound, a weaker but sufficient substitute).
Cases to cover: F exactly at F* vs. F in a "near-optimal" neighborhood
(the restriction's precise scope needs pinning down — too narrow and it
doesn't combine with Case I/II's F values; too broad and it re-risks the
refuted unrestricted claim).
Watch out for: do NOT restate Claim (B) in its original unrestricted form
(refuted round 5, exact counterexample n=2, F={p_1}, splitting p_3,
12/35 < 3/7) — every step here must explicitly track the restriction to
F near Claim (A)'s optimum.

---

lp-duality-certificate: revise (reframed target — genuinely different
top-level claim, not a same-mechanism variant of the lower-bound wall)
Target: c(n) = 2^n/(2^{n+1}-1) — this round's contribution is the general
UPPER bound (c(n) ≤ a_n for an ARBITRARY Liu Bang marking with ≤n points,
not just the ladder), which is currently only proved for n≤2 and is a
structurally separate half of the theorem from the (†)/Case-I lower-bound
wall this approach was previously converging onto. Per round-8 explorers'
structural no-go (any bounded, context-free certificate for the lower
bound's tight c_1=2 witness must smuggle in the exact recursive value of
A(G'), i.e. is the induction in disguise) — this approach should NOT
continue patching its Type III/IV atom basis for that target; redirect its
LP-dual-certificate machinery to the upper bound instead, where it has
already produced a complete, non-numeric proof at n=2 (the certified
six-template argument, `n2-upper-bound-lp-argument`).
Technique: LP duality / explicit strategy certificate, generalizing the
n=2 six-template contradiction argument into an inductive family indexed
by n, built on the already-certified resource-deficit fact (Liu Bang's
n+1 pieces vs. Xiang Yu's n cuts, "one short of full bisection" —
`greedy-halving-adversary`'s Lemma 3/5).
Skeleton:
  1. Fix an arbitrary Liu Bang marking p_1≥…≥p_{n+1} (sum 1, ≤n points;
     `must-use-all-n-points` already shows WLOG exactly n points/n+1
     pieces). Goal: exhibit a Xiang Yu strategy (≤n cuts) achieving
     Φ≤a_n for every such marking, not just the ladder.
  2. Recall the n=2 base case in full (six explicit templates, LP-style
     contradiction — cite `n2-upper-bound-lp-argument`, do not re-derive).
  3. Propose a general-n strategy family generalizing the resource-deficit
     "greedy pair-and-bisect-the-residual" idea (already sketched
     numerically in `greedy-halving-adversary`'s Open gaps §1): repeatedly
     match the two closest-valued remaining pieces (or sub-fragments) into
     an equal pair via one cut, leaving a single residual v to bisect last
     — by tool: an explicit greedy/matching construction (constructive,
     not existential).
  4. Prove Φ(strategy) ≤ a_n by an INDUCTIVE dual certificate: build the
     n-certificate from the (n-1)-certificate by a fixed local
     modification (one new cut, one new matched pair) rather than
     re-deriving from scratch per n — by tool: LP duality / weak-duality
     bound, mirroring the n=2 template's contradiction structure one
     level up.
  5. Verify at n=3 against the known trisection witness (round 4's ad hoc
     seventh strategy for the configuration (3/8,1/4,1/4,1/8), which
     defeated all six n=2-style templates) — the general strategy from
     step 3 must reduce to (or dominate) this witness as a sanity check.
Key lemmas (claim + mechanism):
  - Resource-deficit greedy-matching strategy (reuse + extend): with n+1
    pieces and n cuts (one short of full bisection), pairing pieces by
    nearest value and bisecting only the leftover residual minimizes the
    final residual v — because any unmatched mass beyond the single
    unavoidable leftover only inflates Φ=(1+v)/2, so the strategy's
    optimality reduces to a matching/subset-sum minimization already
    partially explored numerically by the sibling.
Open gaps: this is a substantial, largely unattempted sub-problem for
general n (only n≤2 fully closed, one ad hoc n=3 witness on file) — the
builder should treat this as exploratory; an honest partial result (e.g.
closing n=3 non-numerically, or proving the strategy family achieves
Φ≤a_n only under an extra structural assumption on the marking) is
acceptable progress, not a failure, given how little of this half of the
theorem has been touched since round 4.
Cases to cover: none pre-specified — the builder should first attempt to
reproduce n=3's known answer (1/2 via trisection) non-numerically as the
new base case before attempting general n.
Watch out for: do not conflate this with the (†)/Case-I lower-bound gap —
this approach's role this round is exclusively the upper bound, a
genuinely different top-level target; explicitly note in the build that
the structural no-go from round 8's explorers applies only to bounded
lower-bound certificates for Case I and does NOT rule out this direction.
