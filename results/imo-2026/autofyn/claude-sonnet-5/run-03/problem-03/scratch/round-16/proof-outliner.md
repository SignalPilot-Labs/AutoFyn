## imo-2026-03

self-similar-induction-on-n: revise
Target: The problem's actual claim — for every n, Liu Bang can guarantee
exactly c(n)=2^n/(2^{n+1}-1), i.e. both directions of
V(p)<=c(n)<=(LB's construction value), via the certified minimax
reduction c(n)=max_p min_response OddSum(...). This approach attacks the
lower-bound direction (LB's geometric construction achieves >=c(n)),
specifically closing General Theorem GT(m) for all m (currently proved
m<=3 in full, m>=4 reduced — by round 15 — to the width-1 window
a_1 in (2^{k-1}, 2^{k-1}+1) in sub-case (i), plus the separate
Case-B(m,k) sliver).
Technique: self-similar peeling induction on the "reserve top piece,
recurse on residual" structure (Global-max/Companion Peeling), with the
AltSum/OddSum machinery (Lemma AS) as the algebraic backbone.
Skeleton:
  1. Re-derive Step 3 of the Sub-case (i) window reduction WITHOUT
     invoking Monotonicity Reduction to shrink to the abstract small
     boundary sum(D)=2^k — instead track the actual value sum(R) forced
     by the genuine embedding, i.e. sum(R) = 2^m - a_1 (large, of order
     2^m), where m is the TOP-level parameter and k=m-e is the level at
     which the width-1 window is hit after e successive q=0 (level-drop)
     steps — by the mechanism from math-explorer-window.md: sum(D) is
     invariant under a q=0 chain, so R = D\{a_1} really does carry the
     top-level mass, not a fresh small mass.
  2. Prove the genuinely-needed inequality
     OddSum(R ∪ Γ_{k-2}) >= sum(R) = 2^m - a_1
     directly for R with |R| = k+e (e = m-k, the real excess), max(R) <=
     2^{k-1}, and sum(R) = 2^m - a_1 large — via the certified
     AltSum Small-Sum Lemma / Growth Lemma applied at the ACTUAL sum
     value, not the small-boundary value; use the extra headroom
     (sum(R) large relative to the 2^k-scale target) as slack, since the
     abstract e=0 case is exactly tight but the embedded e>=1 case has
     sum(R) roughly (2^m-2^k) larger than the abstract counterexample's
     sum, which is exactly where all numerically-tested embedded
     instances show comfortable positive margin.
  3. Combine with the already-closed a_1 >= 2^{k-1}+1 range (round 15) to
     get GT(m) unconditionally for every m, for sub-case (i).
  4. Leave Case-B(m,k)'s own sliver (2^{m-1}-1,2^{m-1}) as a separate,
     still-open target — flag (per math-explorer-window.md) that any
     future "reduce via Monotonicity to a small boundary sum" argument
     for it must be checked against the SAME over-generalization trap
     before being trusted, since it has the identical shape.
  5. Secondary task (absorbing discharging-neighbor-transfer's output,
     see below): once the corrected Single-Cut Rank-Shift Identity is
     certified as a lemma (AltSum-labeled, with the OddSum=Δ/2
     corollary via Lemma AS), check explicitly whether its region-A/B/C
     decomposition gives a cleaner restatement of GT(m) sub-case (i)'s
     Step 1/2 — a possible simplification of this file's own proof, not
     a new external result (per discharging-neighbor-transfer's Opening
     3, flagged but unexplored).
Key lemmas (claim + mechanism):
  - Corrected embedding identity: for a q=0-chain of length e from level
    m down to level k=m-e, the residual R=D\{a_1} obtained after peeling
    has sum(R) = 2^m - a_1, NOT any value freely reducible to 2^k - a_1
    — because a q=0 step at each level only peels Γ's own next element
    into the running OddSum total and does not touch D's own mass at
    all (this is the mechanism explicitly verified by
    math-explorer-window.md, distinguishing the false abstract
    counterexample from the true, unreachable-by-recursion scenario).
  - Large-sum slack lemma (to be proved): OddSum(R ∪ Γ_{k-2}) >= sum(R)
    whenever sum(R) is forced to the large value 2^m-a_1 (not the small
    abstract value) — because the AltSum/Growth Lemma machinery's known
    tight case occurs exactly at |R|=k (the abstract e=0 boundary); once
    sum(R) genuinely exceeds that boundary's scale by an amount growing
    with m-k, the same machinery's slack term (currently unexploited in
    the small-sum reduction) dominates the deficit that broke the
    abstract e>=1 counterexample.
Open gaps: Step 2's large-sum slack lemma is not yet proved — this round
found only the correct target (track sum(R)=2^m-a_1) and strong numeric
support (comfortable positive margins, growing with m, at every tested
e=1,2,3 instance); no proof yet. Case-B(m,k)'s sliver remains fully
untouched by this round's fix.
Cases to cover: e=1,2,3,... (excess, i.e. depth of the q=0 chain) —
the abstract statement is false at every e>=1 but the embedded, actual
one must be re-verified case-by-case in e via the large-sum mechanism,
or (preferably) proved uniformly in e using the feasibility bound
e=O(log m) noted by the explorer.
Watch out for: do NOT re-attempt proving the excess-relaxed GT(k,e>=1)
statement in its fully general (arbitrary sum(R)) form — confirmed FALSE
by exact counterexample this round (k=3 witness in
math-explorer-window.md). Any proof must use the actual forced large
sum(R), never the abstract small boundary.

discharging-neighbor-transfer: revise (final build, then retire)
Target: same problem-level claim as above (this approach was opened as a
plateau-break attempt at the lower-bound gap via discharging/charge
transfer); this round's job is narrow and terminal — certify its one
genuine reusable result, then step aside.
Technique: single-cut rank-shift discharging identity (relabeled AltSum),
consumed by self-similar-induction-on-n's machinery via Lemma AS.
Skeleton:
  1. Rewrite the Single-Cut Rank-Shift Identity's statement and both
     worked examples under the CORRECT label: the quantity computed is
     AltSum (Σ (-1)^{i+1} m_i over sorted-descending rank i), not OddSum.
  2. State and prove the OddSum corollary: since a single cut conserves
     total mass (v1+v2=m_j exactly, Δsum=0), the certified identity
     OddSum=(sum+AltSum)/2 (Lemma AS) gives ΔOddSum_true = ΔAltSum/2
     exactly, unconditionally, for any single split — already
     numerically confirmed to 60,000+ trials (two worked examples +
     30k/10k/20k generic and tie-heavy random trials) by this round's
     explorer.
  3. Submit both (the corrected AltSum identity and the OddSum corollary)
     for certification as one reusable lemma file — it strictly
     generalizes the already-certified insertion-only identities
     (arbitrary split of an EXISTING element, not just inserting new
     mass).
  4. Formally recommend retirement of this approach as an independent
     top-level line: its connecting step is confirmed (this round, not
     just diagnosed) to reduce to the identical stuck GT(m) recursion
     under the corrected labeling too (the OddSum/AltSum relation is a
     global affine rescaling that does not change any term's
     boundedness or which sub-case is hard) — no independent leverage on
     either open gap. Any future work on "bound the suffix/Region-C
     term" should be filed directly under self-similar-induction-on-n's
     GT(m), not this approach.
Key lemmas (claim + mechanism):
  - ΔOddSum_true = ΔAltSum_formula / 2 for every single split — because
    mass conservation (Δsum=0 per split) plus the certified
    OddSum=(sum+AltSum)/2 identity forces the two deltas to be
    proportional by exactly 1/2, with no residual/approximation term.
Open gaps: none mathematically — this is a closing, certifying round for
this approach, not a gap-narrowing one.
Cases to cover: none beyond the certification write-up (two structurally
different worked examples already validated; general proof is the mass-
conservation argument, not case-based).
Watch out for: do not let a future round reopen this as a "genuinely new"
route without first checking self-similar-induction-on-n's own progress —
the affine-rescaling argument shows relabeling cannot unlock new
leverage; only a structurally different discharging RULE (not a relabel)
could, and none has been found in 2 rounds.

reciprocal-potential-induction-on-n: new
Target: same problem-level claim, attacking the upper-bound direction
(V(p)<=c(n) for every legal p, the Existence Theorem's remaining
Σ-shape/branch-comparison-boundary residual) via a genuinely different
top-level framing — induction on n at the level of the value function
itself, bypassing per-n vertex/tie-topology classification entirely.
Technique: reciprocal/potential-function (renewal-equation-style)
induction on n, using the exact algebraic fact
1/c(n) = 1/c(n-1) + 2^{-n}, c(0)=1 (verified exactly, Fraction
arithmetic, n=0..7, by this round's explorer) — a self-consistency
equation of resistor-network/continued-fraction type, structurally
disjoint from every live approach's vertex-enumeration/tie-topology
machinery.
Skeleton:
  1. MANDATORY FIRST STEP, before any proof investment (per repo rule —
     numerically stress-test any proposed inequality mechanism before
     building on it): test the pointwise inequality
     1/V(p) >= 1/V(p') + 2^{-n}
     against the catalogued hard n=3,4 balanced-region points already
     logged in global-lp-vertex-sufficiency.md Sections 4.6-4.7 (excess
     ≈0.0098, 0.0013, 0.0098 against every named construction), under at
     least two candidate canonical reduction maps p -> p' (e.g. (a)
     bisect the top piece into two equal halves, treat one half plus the
     rest as a rescaled (n-1)-piece instance; (b) peel the top piece
     entirely and rescale the tail to sum 1). Use the existing V(p)
     solvers already built by sibling approaches (exhaustive
     cut-allocation enumeration, per global-lp-vertex-sufficiency's own
     Sections 4.6-4.7 methodology) rather than writing a new one from
     scratch, to avoid introducing an independent numerical-bug risk.
  2. IF (and only if) step 1 holds at the hard points under some
     reduction map with no violations on a broader random sweep (not
     just the 3 catalogued points): formalize the reduction p->p' as an
     explicit legal (n-1)-piece partition construction, and attempt to
     prove the pointwise inequality directly (likely via a peel-the-top-
     piece argument analogous to Global-max Peeling, but tracking the
     RECIPROCAL of OddSum rather than OddSum itself — the technique is
     new to this project, no KB entry matches it directly).
  3. IF step 1 fails broadly: record the specific reduction map(s) tried
     and their failure mode as a documented dead end (do not silently
     drop the framing — check at least the two reduction maps above
     before concluding the whole Opening is dead, since a wrong reduction
     map choice is a distinct failure mode from the inequality itself
     being false, per Rule 94/round-16 window finding on GT(m)).
  4. If the pointwise inequality is confirmed true and provable, downward
     induction on n from the certified base case c(0)=1 (already proved,
     round 1) closes the Existence Theorem's ENTIRE Σ-shape residual at
     once, without ever touching Σ(n,k) classification or tie-topology
     construction — the strongest possible outcome for this approach.
Key lemmas (claim + mechanism):
  - Closed-form reciprocal recursion 1/c(n)=1/c(n-1)+2^{-n} — algebraic
    identity from c(n)=2^n/(2^{n+1}-1), already exactly verified
    (Fraction arithmetic n=0..7); this is proved fact about the
    SUPREMUM only, not yet about V(p) pointwise — must not be conflated
    with the (unverified) pointwise claim in the outline write-up.
Open gaps: everything past step 1 — the pointwise inequality has NOT
been numerically tested yet against real V(p) computations (only the
closed-form supremum recursion is verified); this is explicitly a
cheap-kill-first approach, no proof attempt before the test.
Cases to cover: at least two distinct reduction maps p->p' must be
tested before ruling the framing out (see step 3); a single failed map
is not evidence the whole Opening is dead.
Watch out for: do not let a builder skip straight to a proof attempt on
an unvalidated reduction map — this is exactly the failure mode the
repo's cheap-kill discipline exists to prevent (Rule: "ALWAYS numerically
stress-test any proposed adversary/algorithmic strategy... before writing
it up as a lemma"). If the cheap test is inconclusive (holds at 2/3
points, fails at 1/3, say), report it precisely rather than rounding to
"works" or "fails."

global-lp-vertex-sufficiency: advance
Target: same problem-level claim, upper-bound direction — close the
Existence Theorem's remaining Σ-shape residual: branch-comparison-
boundary candidates (f_σ(q)=f_τ(q) for distinct valid shapes σ≠τ) and
within-branch-tie candidates (two coordinates of the same y_σ(q)
coincide), per Section 6.3 of the approach file (round 15's honest
diagnosis: no uniform-convexity/concavity LP-duality certificate can work
cell-independently, confirmed by an exact 4-piece counterexample with
slopes 0,+1,-1,0).
Technique: finite-cell affine-vertex reduction (already certified),
extended with a genuinely case-split-tolerant (not uniform-curvature)
argument for the two remaining Σ-shape candidate families.
Skeleton:
  1. Since a uniform convexity/concavity certificate is now confirmed
     dead (Section 6.3), attempt the two honestly-scoped remaining
     routes named in the file's own diagnosis: (a) a genuinely
     case-split argument that stays TRACTABLE despite re-approaching
     Σ(n,k)-classification — e.g. by using the Zero-Removal Invariance
     Lemma's style of argument (reduce a candidate to a strictly smaller
     legal instance) applied to branch-comparison-boundary points
     specifically, checking whether f_σ(q)=f_τ(q) forces some structural
     degeneracy usable the same way zero-fragments were; (b) a
     genuinely different non-constructive mechanism (explicitly flagged
     as not yet identified in the file — this round should attempt to
     name one, not just repeat the search).
  2. As a concrete narrower target: restrict attention to n=3,4 (the
     catalogued hard points already logged in Sections 4.6-4.7) and
     attempt to EXACTLY classify which of the two remaining candidate
     families is actually realized as the maximizer at each hard point —
     if in every catalogued hard case the maximizer sits at a
     within-branch-tie candidate (not branch-comparison-boundary), that
     narrows the target to one family, a genuine simplification.
Key lemmas (claim + mechanism): none yet proposed this round — this is a
diagnostic/search step, not a lemma-producing one; any genuine new lemma
found must pass the same cheap-kill discipline as the four already-killed
tie-topology families before being trusted.
Open gaps: both remaining Σ-shape candidate families (branch-comparison-
boundary, within-branch-tie) are fully open; no new mechanism was found
by this round's explorers (out of scope for their assigned lenses).
Cases to cover: n=3,4 catalogued hard-point classification (step 2) as a
diagnostic before attempting general n.
Watch out for: do NOT re-attempt any of the 4 already-refuted bounded
tie-topology families (cyclic, linear-chain, descending-chain, star/
tree) or a uniform convexity/concavity certificate — all confirmed dead
in exact arithmetic across rounds 9, 13-15.

lp-duality-split-polytope: advance
Target: same problem-level claim, upper-bound direction — this
approach's own object (the split-fragment polytope at region vertices,
especially e_0) is now fully characterized for the Perfect-Tie and
Twin-Anchor families (V(e_0)=1/2 for all n>=3, certified); no new lead
was found this round (out of scope for the three dispatched explorer
lenses), so this round's task is a light, well-scoped extension rather
than a fresh direction.
Technique: exact vertex/fragment-family construction and characterization
at region vertices, continuing the Perfect-Tie / Twin-Anchor line.
Skeleton:
  1. Cross-check whether the certified Twin-Anchor Construction (V(e_0)=
     1/2 exactly, all n>=3) or the Perfect-Tie-Family Characterization
     (only s=n-1 active pieces ever attain c(n)) can be adapted to
     directly exhibit — or rule out — a within-branch-tie candidate at
     e_0 matching global-lp-vertex-sufficiency's Section 6.3 open family,
     since both approaches share the same underlying object (fragment
     ties at region vertices) — a direct cross-approach data point, not
     a new theorem attempt.
  2. If step 1 finds a genuine correspondence, hand the identified
     within-branch-tie instance to global-lp-vertex-sufficiency as a
     concrete worked example (per Rule: cross-substitute one approach's
     result against a sibling's open target before assuming independence).
Key lemmas (claim + mechanism): none proposed this round; step 1 is a
cross-check, not a new proof.
Open gaps: the general upper-bound Existence Theorem itself remains with
global-lp-vertex-sufficiency, not this approach — this file's own
Necessity+Sufficiency picture for the triangular family and V(e_0)=1/2
for all n>=3 are already complete and certified.
Cases to cover: none beyond the n=3,4 cross-check.
Watch out for: do not duplicate global-lp-vertex-sufficiency's own
Section 6 work — this is a light cross-check contribution only; if no
correspondence is found quickly, do not force one.
