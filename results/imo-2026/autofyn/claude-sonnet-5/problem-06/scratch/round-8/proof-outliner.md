## imo-2026-06

This is round 6 of 6 consecutive rounds (3–8) on the FCBC/(MRS)/𝓥_S family.
Round 8's three explorers produced real new leverage — one genuinely new
unconditional lemma, one proof that a whole round-7 sub-thread (depth-
bounding) is not independent, and one partial explicit-recruiter-set
mechanism — so this round deepens the two live threads with corrected
targets and adds one genuinely new mechanism, rather than opening a 3rd
"hunt for an orthogonal top-level framing" (two dedicated searches, rounds 5
and 7, already came up empty; nothing this round suggests a 3rd would
differ, whereas all three findings below point at concrete, closable-looking
next steps within the FCBC family). `intersecting-family-covering-
construction` is untouched this round (still fully correct and complete
conditional on FCBC/(MRS); no new work for it until the sole gap closes).

persistent-backbone-monovariant: revise
Target: there exist positive integers T, L with a_{n+T}=a_n+L for every n≥1
(the problem's full statement) — reached via the already-certified chain
Theorem 5.1 (FCBC ⟹ whole problem) + Lemma MS (MRS ⟹ FCBC) + Theorem CD/
Theorem V (Λ_S finite for every proper core S ⟺ (MRS)). This approach's own
target is exactly: Λ_S finite for each proper core S.
Technique: elementary counting/well-ordering (No-Resurrection, Interval
Lemma, Generation-Chain Lemma, Lemma FOM/Fan-Size Corollary — all already
certified in this approach's lineage) plus a newly-certified pigeonhole
corollary of the Escape-Confinement Lemma, applied to bound the TOTAL
(permanent + transient) member count, not just permanent bundles.
Skeleton:
  1. Certify the Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary
     — for a proper core S with a core-avoiding witness j_3, every realized
     bundle Q_i intersects the fixed finite comp(a_{j_3}); pairwise-disjoint
     realized-bundle families are hence bounded by |comp(a_{j_3})| — by
     Escape-Confinement Lemma (certified) + pigeonhole.
  2. Retarget the Growth-Budget/Generation-Chain-count attempt at TOTAL
     𝓥_S/Λ_S (permanent + transient), using Step 1's corollary applied at
     every level of the certified iterated Escape-Confinement recursion (not
     just the top level) as a fresh lever on the round 3–6 "pointwise vs.
     cumulative" obstruction.
  3. Report honestly whether (2) converts to a cumulative bound or hits the
     same wall one level down; do not fall back to assuming ω(a_n)=O(1)
     silently — that hypothesis is the separate sunflower-bundle-closure
     approach's explicit content.
Key lemmas (claim + mechanism):
  - Pairwise-Disjoint-Bundle-Count Corollary — because Escape-Confinement
    forces every bundle to hit one fixed finite witness set, so disjoint
    bundles pigeonhole into it.
  - (Open) Generation-Chain cumulative bound — candidate mechanism: iterate
    the pigeonhole bound down the certified Escape-Confinement recursion
    rather than applying it once at the top.
Open gaps: (a) existence of a core-avoiding witness j_3 for every proper
core S (shared sub-lemma, prove once, see Watch out); (b) the cumulative
Generation-Chain bound itself — genuinely open, this round's real target.
Cases to cover: none beyond the standing Case I/Case II split (Case I
already closed elsewhere).
Watch out: round 8's thread-unification explorer PROVED (not conjectured)
that this approach's literal round-7 target (permanent bundle COUNT alone)
is a proper subset of Λ_S-finiteness and does not by itself close anything
— the retarget above is mandatory, not optional; do not silently revert to
reporting progress on the old, insufficient target. The core-avoiding-
witness existence lemma is shared verbatim with forced-primes-well-
ordering's Step 1 this round — prove once, cite from both files.

forced-primes-well-ordering: revise
Target: same as above (the problem's full statement via the certified
reduction chain); this file's own target is Λ_S finite for each proper core
S, approached via an explicit finite recruiter-set construction.
Technique: extended-imprint intersection (Generalized Lemma C applied to
I_S, the core's OWN matching class, rather than J_S, the avoiding class) —
a genuinely different, constructive mechanism from persistent-backbone-
monovariant's counting approach and sunflower-bundle-closure's extremal
approach.
Skeleton:
  1. Certify the Freeze-Confinement Corollary: (MRS_S) [antichain 𝓜_n^S
     freezes at finite n*] ⟹ escape-recursion depth bounded by
     max_{C'∈𝓜_{n*}^S}|C'\S| — by an elementary 3-way antichain-maintenance
     case split (a newly-realized radical is either a new minimal element,
     causes a removal, or is a dominated superset; past the freeze only the
     third case can occur). This formally retires independent depth-
     bounding as this round's dedicated explorer proved it is a one-
     directional corollary of the master gap, not an independent route (all
     7 of round 7's "deep" escape events were reverifed this round to be
     reuses of already-permanent bundles or later-dominated transients, not
     evidence of an independent depth mechanism).
  2. Define S^+ := ⋂_{i∈I_S} rad(a_i) (extended imprint over the core's own
     class), certify its finiteness (whenever I_S infinite) via the already-
     certified Generalized Lemma C applied to I_S instead of J_S, and the
     one-line Necessity Lemma: every exactly-realized bare value C=rad(a_i),
     i∈I_S, satisfies C ⊇ S^+.
  3. Attack the sufficiency gap found this round (S^+ matches exactly in
     7/8 tested instances but is incomplete for the sparse core S={1061},
     which needs one extra prime beyond S^+): define S^{++}_κ := the
     extended imprint restricted to the sub-class of I_S whose radical also
     contains bucket κ, and attempt to show S ∪ S^{++}_κ is SUFFICIENT (not
     just necessary) to pin down the dominator, at least for the one known
     failing instance.
Key lemmas (claim + mechanism):
  - Freeze-Confinement Corollary — because a frozen antichain admits no
    further minimal elements, so every later radical is comparable
    (superset) to a fixed frozen one.
  - S^+ Necessity Lemma — because S^+ is literally contained in every
    radical of class S by definition of intersection over I_S.
  - (Open) S^{++} sufficiency — candidate mechanism: restricting the
    intersection to bucket-matching indices only should tighten the
    intersection enough to capture the "extra" recruited primes; not yet
    tested.
Open gaps: (a) core-avoiding witness existence (shared, see above); (b) I_S
infinite in general (standing hypothesis, unproved, same status as J_S
infinite); (c) S^{++} sufficiency itself — genuinely open, unattempted by
this round's explorer, the concrete next step for the builder.
Cases to cover: none beyond the standing Case I/Case II split.
Watch out: do NOT resurrect the Recruiter-Alignment/W(a_1) pattern or the
naive full-branching escape-tree induction (both independently refuted,
round 7 and round 8) as depth-bound mechanisms — the Freeze-Confinement
Corollary supersedes both, cheaply and correctly. Do not claim S^+/S^{++}
closes Λ_S-finiteness even if sufficiency holds on every tested instance —
an arbitrary-core proof is required, not case-by-case verification.

sunflower-bundle-closure: new
Target: same as above (the problem's full statement via the certified
reduction chain); this file's own target is Λ_S finite for each proper core
S, approached via a pure extremal/counting argument requiring no explicit
construction.
Technique: classical infinite Δ-system (sunflower) dichotomy for families
of uniformly-bounded-size finite sets (confirmed absent from knowledge_base.
md and the crux corpus — prove from scratch, standard finite combinatorics),
combined with the certified Escape-Confinement Lemma and Lemma ER (Eventual
Realization Dichotomy), reducing the ENTIRE remaining gap to one precise,
already-on-record hypothesis: round 3's ω(a_n)=O(1) (restricted per-core as
Hypothesis (UB_S)).
Skeleton:
  1. Cite the certified reduction chain (Λ_S-Reduction Lemma → Theorem CD →
     Lemma MS → Theorem 5.1) — no new work, just assembly, to keep this
     file's target honestly the same whole-problem claim as every sibling
     approach.
  2. State Hypothesis (UB_S): companion-bundle size for realized class-S
     indices is uniformly bounded. Flag explicitly that |Q|=ω(a_i)-|S| for
     i∈I_S, so (UB_S) is the restriction of round 3's still-open ω(a_n)=O(1)
     to one subsequence — not a strictly easier target, an honestly-scoped
     instance of the same open difficulty.
  3. Certify the same Escape-Confinement Pairwise-Disjoint-Bundle-Count
     Corollary as persistent-backbone-monovariant's Step 1 (share the proof,
     do not duplicate) — unconditional, no (UB_S) needed for this step.
  4. Prove (UB_S) ⟹ Λ_S finite: assume the realized-bundle family for S is
     infinite; by (UB_S) it has uniformly bounded size, so the Δ-system
     dichotomy gives an infinite pairwise-disjoint sub-family (ruled out by
     Step 3) or an infinite sunflower with common core Y (ruled out by
     applying Lemma ER to S∪Y: either eventually realized, so only finitely
     many petals precede its realization index, or permanently blocked, so
     Escape-Confinement forces the petal remainders — already pairwise
     disjoint by the sunflower's own definition — to pigeonhole into a
     second fixed finite witness set, contradicting infinitude directly).
     Both branches contradict infinitude; conclude Λ_S = a finite union of
     bounded-size sets, hence finite.
  5. Attack (UB_S)/ω(a_n)=O(1) itself using Step 3's corollary as a fresh
     lever not available to round 3's original attempt (constrain how many
     distinct "bundle shapes," i.e. subsets of comp(a_{j_3}) hit, can
     coexist, combined with Lemma 1's linear gap bound) — report exactly
     where this stalls if it does not close.
Key lemmas (claim + mechanism):
  - Escape-Confinement Pairwise-Disjoint-Bundle-Count Corollary (shared with
    persistent-backbone-monovariant, prove once) — pigeonhole via a fixed
    witness companion set.
  - Classical Δ-system dichotomy — because a maximal pairwise-disjoint
    sub-family either is itself infinite, or, if finite, infinitely many
    remaining sets must hit it, forcing (by further pigeonhole/induction on
    set size) a common nonempty core with disjoint remainders.
  - Lemma ER (Eventual Realization Dichotomy, certified) — splits the
    sunflower-core case into two branches, both independently finite.
Open gaps: (a) core-avoiding witness existence (shared, prove once across
all three approaches this round); (b) I_S infinite where needed in Step 4's
case (i); (c) Hypothesis (UB_S)/ω(a_n)=O(1) itself — the sole remaining open
hypothesis after Steps 3–4, and this approach's genuine content.
Cases to cover: the Δ-system dichotomy's two branches (pairwise-disjoint /
sunflower), both handled in Step 4; Case I is out of scope (already closed
elsewhere).
Watch out: do not claim (UB_S) is easier than ω(a_n)=O(1) — it is the same
open hypothesis, honestly scoped to a subsequence. Do not resurrect ND1/ND2
(refuted covering-set mechanisms) as a route to (UB_S) — different failure
shape but same refuted family. Verify the classical Δ-system dichotomy's
proof explicitly allows an infinite universe of primes as the ground set
(only set *size* needs to be bounded) rather than silently assuming a
finite alphabet.

## Cross-cutting notes for the outline-reviewer

- All three approaches now share one open sub-lemma: existence, for every
  proper core S⊊P_1, of an index j_3 with rad(a_{j_3})∩S=∅ (a
  "core-avoiding witness"). This was flagged as an unproved "likely easy
  pigeonhole" in round 6 and never explicitly closed since. Recommend the
  reviewer treat this as a single shared prerequisite lemma (prove once,
  cite from all three files) rather than three independent proof
  obligations, and flag it prominently to whichever builder tackles it
  first.
- The "kill" from this round's subset-avoidance explorer — do NOT treat
  "does Subset Avoidance (SA) hold only finitely often per core" as a
  strictly easier reformulation of Λ_S-finiteness, since it is essentially
  the identical statement in different words (per the Class-Decomposition
  Fact's exhaustive dominator case split) — is folded into all three files
  above by construction (none of them pursue that framing); flag it
  explicitly here so round 9 doesn't rediscover it as if new.
- global-recruiter-finiteness remains RETHINK (confirmed dead, do not
  revive without refuting its equivalence proof); core-depth-induction and
  explicit-window-backbone-construction remain parked (no new idea
  surfaced this round for either); backbone-existence-crt and bounded-gap-
  density-covering remain parked/dead-end, unchanged.
- If round 9 finds all three of this round's threads stall on the shared
  witness-existence sub-lemma or on ω(a_n)=O(1)/(UB_S) itself, that would
  be a strong, sharply-localized signal (not a vague plateau) about exactly
  which single fact is blocking the whole population — worth treating as
  the round-9 target directly rather than a fresh reformulation.
