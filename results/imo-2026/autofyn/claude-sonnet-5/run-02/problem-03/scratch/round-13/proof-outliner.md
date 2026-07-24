## imo-2026-03

greedy-halving-adversary: revise
Target: c(n) = 2^n/(2^{n+1}-1) — this approach's piece is Claim (B), the
lower bound's restricted "tail refinement never pushes A below f(n)"
statement, currently unified as Theorem P(n). This round's revision attacks
the two named open items: (†)'s p2-cut complement, and ℓ(F)=2's P≠∅
sub-case (the round-11/12 "needs an upper bound at budget one notch too
deep" diagnosis).
Technique: transplant the already-certified `exchange-smoothing-vertex-
maximization` + `per-piece-vertex-decomposition-theorem` reduction (proved
for Claim (A)'s Case-I-Closure-Theorem) onto both open items, using the
min/max symmetry `vertex-minimum-theorem` already states explicitly ("the
minimum, and by symmetry the maximum, ... is attained at a vertex"). Per
the round-13 explorer, the REDUCTION half of this transplant is essentially
free; the EVALUATION half (closed-form bound on the resulting finite vertex
family) is genuinely open and must be attempted from scratch — do NOT
assume Ratio-2-Spacing-Lemma/Last-Element-Bound transfer verbatim, since
they were derived for Case (A)'s specific reference-set shape.
Skeleton:
  1. Cheapest sub-target first (per explorer's numeric lead): prove the
     **p2-Pinned-Dominance Lemma** — among the finite vertex family
     produced by applying exchange-smoothing to (†)'s maximization
     (max_{G'} A(G'), G' a legal ≤(n-2)-cut refinement of τ={p2,...,p_{n+1}}),
     every vertex where p2 itself is cut is weakly dominated by some vertex
     where p2 is left untouched (pinned). Mechanism: a local exchange move
     — if p2 is split into fragments q_1≥q_2≥..., replace this split by
     leaving p2 whole and redistributing the same cut budget among
     p3,...,p_{n+1} in the way that increases A the most; show this
     redistribution is always legal (budget-preserving) and show A does
     not decrease, via the same "affine functional, local perturbation
     toward a vertex" argument that powers exchange-smoothing itself
     (a literal instance of the exchange step, not a new mechanism) — cite
     `exchange-smoothing-vertex-maximization`'s proof template directly,
     applied to the single coordinate p2's own fragment vector via
     `per-piece-vertex-decomposition-theorem`.
  2. If step 1 succeeds: (†) reduces to maximizing A over G' that leave p2
     untouched — this is EXACTLY the branch Prop 22 already closes
     (conditional on (⋆_{n-2}), unconditional n≤4) — so (†) closes at the
     SAME conditional status as Prop 22, with zero new evaluation work,
     for every n (not just n≤4 if we additionally push Prop 22 itself to
     general n, which remains its own separate open item — note this
     explicitly, do not overclaim unconditional closure).
  3. In parallel, attempt the general transplant for ℓ(F)=2, P≠∅: apply
     `per-piece-vertex-decomposition-theorem` to max_{G'} A(F_2∪G') where
     F_2={t*}∪P is now a FIXED extra reference element appended to every
     piece's own reference set (not part of the moving mass) — this
     reduction step should transplant essentially verbatim, per the
     explorer's diagnosis. Attempt an analogous p2-pinned-dominance lemma
     here too (step 1's exchange argument, now against the shifted
     reference set including t*) — flag explicitly if the shifted t*
     breaks the pinning argument's proof (the explorer's own honest
     caveat: t* breaks pure ratio-2 spacing).
  4. Fallback (if steps 1/3 evaluation resists a clean closed form): use
     the crude `half-bound-lemma`/`last-element-bound` bounds directly on
     the reduced finite vertex family — a weaker, non-tight bound may
     still suffice, since Prop 26's own closure already showed some slack
     exists in nearby regimes.
Key lemmas (claim + mechanism):
  - p2-Pinned-Dominance Lemma (NEW, to prove): the (†)-maximizer always
    leaves p2 uncut — because a local exchange move (undo any cut on p2,
    redistribute the freed budget onto the tail below p2) is legal and
    weakly A-increasing, by the same first-order perturbation argument
    `exchange-smoothing-vertex-maximization` already certifies for
    Claim (A)'s dual direction.
  - Min/max symmetry transplant: `vertex-minimum-theorem`'s own statement
    already covers minimizing E (⟺ maximizing A) via the polytope-vertex
    fact being polarity-agnostic — cite directly, no new proof needed for
    this half.
Open gaps: the p2-Pinned-Dominance Lemma itself (step 1) is the new,
unproved key lemma — the whole revision hinges on it; the ℓ(F)=2 P≠∅
shifted-reference version (step 3) is a second, harder instance that may
need its own separate argument if t* breaks the pinning proof.
Cases to cover: (†)'s p2-cut complement (target of steps 1-2); ℓ(F)=2
P≠∅ (target of step 3); explicitly do not claim general-n unconditional
closure even if step 1 succeeds, since it still bottoms out at Prop 22's
own (⋆_{n-2}) conditioning.
Watch out for: do not assume the exchange move in step 1 preserves cut
LEGALITY automatically — redistributing a freed cut from p2 onto
p3,...,p_{n+1} must respect each piece's own budget/positivity
constraints; verify this explicitly, not by analogy. Also do not conflate
"p2 pinned dominates" (a comparison between FAMILIES of vertices) with
"the p2-untouched branch is already fully closed" (it is only
conditionally closed) — closing step 1 narrows the gap to Prop 22's own
open item, it does not itself close Claim B.

lp-duality-certificate: revise
Target: the general upper bound c(n) ≤ 2^n/(2^{n+1}-1) for arbitrary Liu
Bang markings and every n — this approach's assigned half of the theorem.
Technique: per the round-13 explorer's finding that a literal per-cell LP
dual certificate adds no new leverage (it's a relabeling of the
already-certified exchange-smoothing/vertex machinery, and the real
obstruction — the objective's sign pattern depending on sorted order,
i.e. exponentially many LP cells — is exactly the file's own Open Gap 1),
REDIRECT this approach away from an LP-duality framing entirely and onto
directly attacking Open Gap 1 via a strengthened SIMULTANEOUS induction
(both regimes closed together at each level, as round 9's own diagnosis
requires) plus a new pigeonhole/multi-target peel argument, anchored at
the boundary cases already unconditionally closed (Equal-Pieces Closure,
Spare-Cut Bisection Corollary) — a continuity/perturbation strategy in
the spirit of round 12's successful `ALWAYS` rule 11 technique on the
sibling front, not a new LP mechanism.
Skeleton:
  1. Restate the target as ONE statement P(m) (both regimes together, per
     the round-9 circularity diagnosis): for every m-piece marking,
     Φ_min ≤ a_{m-1}T. Strong induction on m, using the FULL P(m-1) (not
     just its own p1≥T/2 half) as IH — this matches what Theorem C′ and
     Theorem D′/B_k already need, made explicit as the induction's actual
     hypothesis rather than an implicit dependency.
  2. Case split on p1 vs T/2 exactly as before (Theorem C′ closes
     p1≥T/2 unconditionally given full P(m-1)) — already done, reuse.
  3. For p1<T/2 (the genuinely open regime): prove a new **Peel-Target
     Existence Lemma** — either (a) some index k∈{2,...,m} satisfies the
     already-certified Theorem B_k ceiling condition p_k ≥ a_nT/2 (in
     which case Theorem B_k with that k closes P(m) via the IH, exactly
     as the p2-specific Corollary already does for k=2, generalized to
     any k — same proof, cite it verbatim with p_2 relabeled p_k), or
     (b) no such k exists, meaning EVERY piece (including p1) satisfies
     p_i < a_nT/2 for all i≥2 and p1<T/2 — show this forces the marking
     to be close to "spread out" (many small pieces), and handle this
     narrow residual band directly via the already-certified
     `equal-pieces-closure` and `spare-cut-bisection-corollary` as
     boundary anchors, extended by an explicit perturbation/continuity
     argument (bound the derivative of Φ_min's upper-bound construction
     as the marking moves away from equal-pieces, analogous to the
     already-successful round-12 "boundary + continuity" technique used
     by the sibling approach for Prop 26) rather than a fresh closed
     form.
  4. Combine (a)/(b) to close P(m) for p1<T/2, hence P(m) in general, by
     strong induction — state explicitly which sub-case each on-file hard
     witness falls into as a sanity check (both known hard witnesses
     should land in case (a), since Theorem B_k with k=4 already solved
     one of them per round 9).
Key lemmas (claim + mechanism):
  - Peel-Target Existence Lemma (NEW, to prove/refute): if p1<T/2, then
    either some p_k (k≥2) clears the Theorem-B_k ceiling threshold
    a_nT/2, or the marking lies in a narrow, characterizable band near
    equal-pieces — because if every p_i<a_nT/2 for i=1,...,m then
    T=Σp_i<m·a_nT/2, forcing a numeric bound on m·a_n (an elementary
    pigeonhole count on the sum, not yet checked to actually be vacuous
    or nontrivial — this is the cheap first computation to run before
    committing to the harder case (b) machinery).
  - Generalized Theorem B_k Corollary: the p2-specific sufficient
    condition "p_2≥a_nT/2 ⟹ closes" generalizes verbatim to any k, since
    the original Corollary's proof (already certified) never used k=2
    specifically — only that Theorem B_k matches SOME tail element
    exactly, cite `bisect-top-recursive-identity`/`generalized-peel-
    identity`'s existing algebra, re-index only.
Open gaps: the Peel-Target Existence Lemma's pigeonhole count (does
"every p_i<a_nT/2" actually happen for real markings, or is it vacuous by
elementary arithmetic?) is the FIRST thing to check numerically/
algebraically before investing in case (b)'s continuity argument — if
vacuous, this closes the whole upper bound in one clean step; if not
vacuous, case (b)'s boundary+continuity mechanism is the real remaining
work, itself unproved.
Cases to cover: p1≥T/2 (closed, reuse); p1<T/2 with a qualifying peel
target (closes via generalized Theorem B_k); p1<T/2 with no qualifying
peel target (open, attempt via boundary+continuity from Equal-Pieces
Closure/Spare-Cut Bisection Corollary).
Watch out for: do not repeat round-10's refuted "always match top two"
naive greedy claim, and do not assume Theorem B_k's ceiling threshold
a_nT/2 is met by SOME k just because it's plausible — check the
elementary pigeonhole arithmetic explicitly first (step/lemma above)
since this is the cheap kill that could make the whole redirect trivial
or could immediately reveal it's non-vacuous and genuinely hard; either
outcome is real progress, report honestly rather than assuming success.

build set: greedy-halving-adversary, lp-duality-certificate
