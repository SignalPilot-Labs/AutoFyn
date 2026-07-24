## imo-2026-03

greedy-halving-adversary: revise
Target: Claim (B) — for every legal Xiang Yu response (any split of p1 into F,
any legal tail refinement G' of tau), A(F ∪ G') >= f(n) — the still-open half
of the general lower bound, whose closure (combined with the already-fully-
closed Claim (A)) would finish the lower-bound direction of c(n)=2^n/(2^{n+1}-1).
Technique: same overall route as rounds 4-9 (peel/exact-identity + rescaling
induction on the ladder's specific p_i=2p_{i+1} structure), now split into two
concrete, independently-attackable sub-targets instead of one more variant of
the same wall.

Skeleton (two parallel sub-targets, both feed the same top-level Claim B):

  Sub-target 1 — v<p2 case (currently has zero mechanism on file):
  1. Restate F = {v} ∪ P with P exactly-paired, v<p2 (odd residual of Xiang
     Yu's split of p1). By the certified Lemma 19 (`single-residual-
     indicator`), u_F(x) ≡ 1[x<v] pointwise for *every* v, not just v>=p2 —
     this part needs no new proof, it already holds unconditionally.
  2. NEW Threshold-v Decomposition Lemma (to prove, not yet proved): apply
     the already-certified, fully general `cross-term-identity-threshold`
     (proved for *any* threshold, round 2) at threshold r=v instead of at
     p2 — plug Lemma 19's pointwise indicator directly into that general
     identity's cross-term. This is a legitimate mechanical step (the
     identity's generality was never restricted to r=p2; Proposition 20 only
     used r=p2 for convenience because `safe-window-lemma` gives an easy
     kill there). Concretely derive what A(F ∪ G') equals as a function of
     v, A(G'), and one residual cross-term integral over [0,v) — do not
     assume in advance that it collapses to "v - A(G')" the way Prop 20 did;
     it may not (that clean form used p2's special role as the tail's own
     top piece, which v<p2 does not have).
  3. NEW dominance sub-lemma to bound the residual cross-term: use the
     scale-invariant fact (verified exactly this round by the explorer)
     that p2 > Total({p3,...,p_{n+1}}) — i.e. p2 dominates tau's *own*
     residual tail (not the whole multiset; that stronger claim is false,
     p2<1/2 always) — this is exactly the dominance fact already used one
     level up inside `tail-self-similarity`/Proposition 22, being reused
     one level lower here. Case-split on whether G' leaves p2 untouched:
       - if G' leaves p2 untouched: p2 is then the literal dominant element
         of {p2}∪(tail refinement of {p3,...}), so `dominant-element-
         removal-identity`/`sharp-dominant-removal-identity` (both already
         certified) apply directly to isolate A(G') = p2 - A(G'') for G''
         a refinement of the (n-2)-ladder — a genuine, non-circular
         reduction (not a reformulation) because it reduces the DEGREE of
         the problem (tail size shrinks by one level) while v stays fixed,
         unlike the §2 p2-cut recursion below which does not shrink degree.
       - if G' cuts p2: this sub-branch is honestly the same open p2-cut
         obstruction already on file (see Sub-target 2) — do not
         re-derive it here, defer to Sub-target 2's output.
  4. Combine 2+3's untouched-p2 branch into a closed sub-case of v<p2;
     leave the p2-cut branch explicitly open (shared with Sub-target 2).

  Sub-target 2 — p2-cut complement of (†) (the explorer's §2 recursive
  opening), scoped honestly as partial, NOT a closure:
  1. Rescale to the (n-1)-ladder Q = {q1,...,q_{m+1}}, m=n-1, via the
     already-certified `tail-self-similarity`.
  2. When G' cuts q1 (p2 in the original scale) and the induced split of q1
     itself lands in the "ℓ=1, w>=q2" family (w = that split's own odd
     residual), apply Propositions 20-21 recursively at level m — this is
     legitimate reuse of already-proved machinery one level down, and DOES
     genuinely close that one specific branch (not the whole p2-cut
     complement).
  3. State explicitly in the writeup (do not let this get lost as an
     overclaim): the remaining branches at level m — q1 split with ℓ=0
     (already covered elsewhere via `cross-term-vanishing-lemma`), ℓ=1 with
     w<q2 (recurses into Sub-target 1's v<p2 problem one level down, not
     resolved by this step), and ℓ>=2 (still fully open, see below) — are
     NOT closed by this step. Per the explorer's own diagnosis (confirmed
     here), a full closure requires a *simultaneous* strong induction over
     all branches at every level at once; this step supplies exactly one
     input branch to that eventual induction, not the induction itself.

  Sub-target 3 — ℓ(F)>=2 (numerically resolved as no-violation, still no
  proof mechanism): do NOT write up the 60,000+ trial / coordinate-descent
  numeric finding as a proof — it is not one. Instead attempt the following
  NEW reduction lemma suggested by the numeric pattern (both search methods
  found minimizers with ℓ(F)>=2 converging toward the already-fully-
  characterized c=n cascading/rescaled-ladder boundary family, not toward a
  genuinely new interior tie-vertex family):
  1. Conjecture (to attempt, not assume): an "ℓ(F)-Collapse Lemma" — for any
     legal Xiang Yu response with ℓ(F)>=2, there exists another legal
     response using no more cuts, with ℓ(F)<=1, achieving Phi no larger.
     Try to prove this via an exchange/merging argument on F's own fragments
     (fixing everything else, show merging two of F's tied/near-tied odd
     residuals into one weakly helps Xiang Yu) — this would be a genuine
     WLOG reduction eliminating Sub-target 3 entirely, not a case to close
     directly.
  2. If the Collapse Lemma resists proof in this round, fall back to
     reporting the numeric finding honestly as unresolved-but-supportive,
     exactly as the explorer did — do not promote it to "proved."

Key lemmas (claim + mechanism):
  - Threshold-v Decomposition Lemma — because `cross-term-identity-
    threshold` is already proved for an arbitrary threshold (round 2), and
    Lemma 19's pointwise indicator holds for arbitrary v, so plugging r=v
    is a legal instantiation of an already-general tool, not a new axiom.
  - p2-vs-own-tail dominance (p2 > Total({p3,...,p_{n+1}})) — because this
    is exactly the ladder's superincreasing identity p_i > sum_{j>i} p_j
    one level up from where `tail-self-similarity` already uses it.
  - ℓ(F)-Collapse Lemma (conjectural, to attempt) — because an exchange
    argument merging two odd residuals of F into one is the natural
    discrete analogue of `exchange-smoothing-vertex-maximization`'s
    tie-merging mechanism, already certified as valid for the analogous
    max-vertex problem on the whole multiset; whether it specializes to F
    alone (a sub-multiset) is the open question, not assumed here.

Open gaps: Threshold-v Decomposition Lemma's exact closed form (step 2 of
Sub-target 1) is not yet derived — do not assume it equals "v - A(G')"
before checking; the p2-cut branch of v<p2 (shared with Sub-target 2's
deferred branches); Sub-target 2's ℓ=0/w<q2/ℓ>=2 branches at level m
(explicitly NOT closed by the recursive step); the ℓ(F)-Collapse Lemma
(conjectural, unproved either way).
Cases to cover: v>=p2 (already closed, Proposition 20/21/22 partial), v<p2
untouched-p2 (Sub-target 1 target), v<p2 p2-cut (deferred, shared),
ℓ(F)=0 (already closed via `cross-term-vanishing-lemma`), ℓ(F)>=2
(Sub-target 3).
Watch out for: do NOT let the p2-cut recursion (Sub-target 2) be reported as
closing (†) in full — it closes exactly one of its three branches; do NOT
promote the ℓ(F)>=2 numeric search to a proof under any framing; the
Threshold-v Decomposition Lemma must be *derived*, not assumed to mirror
Proposition 20's clean form, since v<p2 lacks the safe-window mechanism that
made Prop 20's form clean.

lp-duality-certificate: revise
Target: the general upper bound c(n) <= a_n for an arbitrary Liu Bang
marking (any n, any legal <=n points) — currently closed only for n<=3 in
the p1>=T/2 regime (via Theorem C′ + telescoping-threshold-identity, both
certified) and entirely open for p1<T/2 beyond ad hoc per-witness patches
(Theorems D′/E/B_k).
Technique: two parallel routes on the same target, both newly enabled by
this round's finding that the lower-bound population's REDUCTION lemmas
(`vertex-minimum-theorem`, `exchange-smoothing-vertex-maximization`,
`pair-cancellation-identity`, `leftover-formula`, `odd-run-reduction-lemma`)
are marking-agnostic and transfer verbatim, while its EVALUATION lemmas
(`half-window-vanishing-lemma`, `ratio-2-spacing-lemma`, `last-element-
bound`) are ladder-specific and do NOT transfer — do not attempt to import
the evaluation lemmas verbatim, only the reduction machinery.

Skeleton:

  Route A — direct vertex characterization for "cut p1 only, tail
  untouched" strategies, arbitrary marking, p1<T/2:
  1. Fix an arbitrary Liu Bang marking with p1<T/2 and restrict Xiang Yu to
     strategies that only fragment p1 (mass s=p1, part-budget k<=n, tail
     tau = {p2,...,pm} untouched) — the family Theorems A-E were hand-
     building templates for piecemeal.
  2. Apply the already-certified `exchange-smoothing-vertex-maximization`
     directly (no re-derivation needed: its proof explicitly does not use
     ratio-2/ladder structure) to conclude the maximizer of E(F∪tau)
     (equivalently the minimizer of Phi over this restricted family) is
     attained at a vertex of the exact shape: some fragments pinned to
     existing tau-values tau_l, the rest sharing one common tied value —
     this is a literal, unconditional match to Theorem A (all-pinned),
     Theorem C/C′ (k=2, one shared tie, p=0), Theorem B/B_k (one pinned
     fragment) — i.e. this ALREADY proves those are the *only* candidate
     vertex shapes, for any marking, replacing "invent more templates" with
     "the family is finite and characterized."
  3. NEW step (not yet done): evaluate Phi at every vertex in this
     characterized family in closed form for an arbitrary (non-ladder)
     marking — this needs a genuinely new, marking-agnostic evaluation
     argument (NOT reuse of `half-window-vanishing-lemma` etc., confirmed
     ladder-specific by the explorer) and is the actual remaining content
     of Route A. Attempt this directly using only `leftover-formula` +
     `pair-cancellation-identity` (both marking-agnostic) to evaluate each
     vertex shape's Phi as an explicit sum, then take the min over the
     finite vertex family symbolically.
  4. Compare the resulting min against a_n * T; if it holds for every
     marking with p1<T/2, this closes Route A. If it doesn't (i.e. some
     "cut p1 only" vertex beats a_n*T), this only shows Xiang Yu needs a
     strategy touching more than p1 — consistent with, not contradicting,
     the still-open general upper bound; report honestly either way.

  Route B — bounded-leftover matching/pairing reformulation (construction,
  not induction):
  1. By the certified `leftover-formula` + `pair-cancellation-identity`
     (both marking-agnostic, zero new proof needed for this step): Phi =
     (T+v)/2 whenever the final multiset decomposes into exact-value pairs
     plus one leftover v. So c(n)<=a_n for a fixed marking is EQUIVALENT
     to: Xiang Yu has a legal response with <=n cuts producing n exact
     pairs plus one leftover v <= T/D_n (D_n=2^{n+1}-1) — a matching
     existence claim, not an inequality-induction claim. State this
     equivalence precisely and prove it (mechanical, from the two cited
     lemmas) before using it.
  2. NEW cheap necessary-condition filter (derive, do not skip): total
     final fragment count is m + (cuts used); for the "n pairs + 1
     leftover" target the total count must be odd. Use this parity filter
     to restrict which cut-counts can even reach v=0 exactly, before
     attempting a general construction — a cheap pruning step, not a proof
     by itself.
  3. Attempt a direct greedy/Steinitz-style pairing construction: process
     Liu Bang's marking points and repeatedly cut off matched pairs (a
     tail element with an appropriately placed fragment of a larger
     element, or two elements bisected against each other), tracking the
     running leftover, aiming to show the leftover can always be forced
     <= T/D_n within budget n. This is a genuinely different proof
     obligation (an algorithm + invariant, not a recursive template chase)
     and should be attempted fresh rather than as a repackaging of
     Theorems A-E.
  4. Sanity-check the construction against both on-file hard witnesses
     ((3/8,1/4,1/4,1/8) and (2/5,3/10,1/5,1/10), both already known to be
     solved *exactly* by v=0 perfect pairings using fewer than n cuts —
     use these as the first two test cases the construction must
     reproduce, not as proof of the general claim) and against a fresh
     n=4 random marking before claiming any general result.

Key lemmas (claim + mechanism):
  - Direct reuse of `exchange-smoothing-vertex-maximization` for Route A
    step 2 — because its certified proof text explicitly states it needs
    no ratio-2/ladder assumption on the reference set tau, so it applies
    verbatim to an arbitrary marking's tail.
  - Matching-existence equivalence (Route B step 1) — because
    `leftover-formula` + `pair-cancellation-identity` already reduce Phi to
    a pure function of the leftover v whenever the final multiset is
    exact-pairs-plus-one-leftover, with no marking-specific content, so the
    reformulation is a direct corollary, not a new conjecture.
  - Parity necessary condition (Route B step 2) — because total fragment
    count parity is forced by m and the number of cuts (each cut adds
    exactly one fragment), a purely combinatorial counting fact.

Open gaps: Route A step 3 (marking-agnostic vertex evaluation) is entirely
unproved — this is the real remaining content, not a formality; Route B
step 3 (the actual construction/invariant) is entirely unproved — only the
reformulation (step 1) and the cheap filter (step 2) are mechanical. Neither
route is close to a finished general-n proof; both are genuinely new lines
of attack this round, not incremental patches on Theorems A-E.
Cases to cover: p1>=T/2 (already closed for n<=3, cite `bisect-top-
recursive-identity` + `telescoping-threshold-identity`, do not re-derive);
p1<T/2 (both routes target this, the real open regime).
Watch out for: do NOT reuse `half-window-vanishing-lemma`, `ratio-2-
spacing-lemma`, or `last-element-bound` verbatim for Route A step 3 — all
three are one-line consequences of the ladder identity p1=2p2, which an
arbitrary marking does not have; a genuinely new evaluation argument is
required. Do NOT present Route B's numeric pattern (both known witnesses
solved by v=0 perfect pairings) as evidence the construction exists in
general — it is exactly two-and-a-half data points (explorer's own framing:
"conjecture, not verified beyond these 2-3 points"), not a proof or even
strong statistical evidence at this scale.

build set: greedy-halving-adversary, lp-duality-certificate
