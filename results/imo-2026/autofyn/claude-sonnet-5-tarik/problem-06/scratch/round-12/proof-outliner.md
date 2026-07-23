## imo-2026-06

This round splits the sole remaining gap (Stabilization Conjecture, via
Theorem SW → Theorem 5.1, restricted to doubly-infinite disjoint core
pairs) using two genuinely new mechanisms found by this round's explorers:
jw-rigidity's "backbone + Lemma UCR" route for Conjecture (JW), and
pd-density's "exact G_n-periodicity / bounded-run-length" route for
`(PD_{S,S'})`. mrs-s-scoped's finding (companion-pool identity between
complementary cores) was confirmed to give no new leverage — no approach
was built around it, per dispatch; its only use here is to help retarget
`forced-primes-well-ordering` away from the now-recorded-dead direct
`(MRS_S)`-for-`{103,197}` pursuit.

All 4 revisions below are persisted to
`results/imo-2026-06/approaches/<slug>.md` as a new "## Round 12 Outline"
section immediately after "## Status" (verified with `grep`).

---

sunflower-inadmissibility-toolkit: revise
Target: the whole problem (`a_{n+T}=a_n+L` for every `n\ge1`), via the
already-certified Theorem SW → Theorem 5.1 chain, restricted this round to
closing Conjecture (JW) for "Case A" doubly-infinite pairs (5/7 tested:
`2747:(41,67)`, `21528751:(103,197)`, `4199:(13,19)`, `4199:(17,19)`,
`4087:(61,67)`).
Technique: well-ordering/minimal-counterexample on the running
companion-set intersection of one class (the "backbone" `B_k`), adapting
the single-family Escape-Confinement/Permanent-Inadmissibility mechanism
to a single-class-scoped claim, then combining with the already-certified
Lemma UCR (this file's own §1, unconditional) for the cross-class step.
Skeleton:
  1. Prefix backbone `B_k:=\bigcap_{t\le k}\mathrm{comp}(a_{j_t})`
     stabilizes at finite `k_0` — trivial finite descent (monotone
     non-increasing subsets of the finite set `B_1`).
  2. Backbone Permanence Lemma (the crux, open): `B_{k_0}` equals the
     intersection over the WHOLE infinite class `I_{S'}`, not just the
     tested prefix — attempted via minimal-counterexample + adaptation of
     Escape-Confinement/Permanent-Inadmissibility to a single class.
  3. Realized-Backbone ⟹ (JW): combine Backbone Permanence with Lemma
     UCR (already certified) in a 3-line set-chase — Lemma UCR gives the
     other side's coverage, Backbone Permanence gives this side's.
  4. Honest reporting if hypothesis (ii) [exact realization of the
     frozen backbone] doesn't follow automatically from Steps 1–2.
Key lemmas:
  - Step 1 — trivial finite descent, because `B_k` is monotone
    non-increasing on a fixed finite ground set.
  - Backbone Permanence (Step 2) — because it freezes almost immediately
    (0–2 realized members) and holds with zero exceptions across
    hundreds-to-thousands of later members in every Case-A instance
    tested this round; conjectured, not yet proved — needs a
    single-class adaptation of already-certified single-family tools.
  - Realized-Backbone ⟹ (JW) (Step 3) — Lemma UCR (already certified,
    proved from Lemma P′ + elementary set manipulation) supplies the
    cross-class half for free.
Open gaps: Backbone Permanence (Step 2, the crux); whether hypothesis
(ii) needs a separate proof (Step 3 caveat).
Cases to cover: Case A only — 5/7 tested doubly-infinite pairs. Case B
explicitly ceded to sunflower-bundle-closure / forced-primes-well-ordering
this round.
Watch out for: do not conflate Backbone Permanence with `(MRS_S)` (a
logically different, strictly weaker object per both this round's
explorers); round 11's WRP mechanism is superseded for Case A, do not
patch its 30%-failure gap on the hard instance further.

sunflower-bundle-closure: revise
Target: the whole problem, via Theorem SW → Theorem 5.1, restricted this
round to closing Conjecture (JW) for "Case B" pairs (the 2/7 tested pairs
lacking any single-side backbone: `247:(13,19)`, `4199:(13,17)`).
Technique: continue the Trace-Clash-Freedom Reformulation (Round 11
skeleton, Steps 1–3,5 retained unchanged and still valid) with Step 4
(Cross-Permanent-Inadmissibility) reframed via pigeonhole on the
escape-prime set (applying the already-certified, size-agnostic Lemma
NIDF injection argument directly to escape primes) rather than continuing
to hunt for exact `u=w` rigidity — motivated by this round's finding that
joint coverage empirically comes from small-prime redundancy/density
(prime 2 alone realizes ~70-100% of joint intersections across ~270M
pairs checked), not a forced algebraic coincidence.
Skeleton: Steps 1 (Trace-Clash-Freedom Reformulation), 2 (finite trace-
type space), 3 (everywhere-nonempty trace), 5 (finite repair +
termination) unchanged from Round 11. Step 4′ (new): show the set of
possible escape primes for a clashing trace-type pair is finite via Lemma
NIDF's injection technique applied to the escape-prime set itself.
Key lemmas:
  - REFUTED this round: round 11's specific `Π:=comp(a_{j_3})∪comp(a_{j_3'})`
    construction (§8.3) — explicit counterexample `a_1=247, i=51, j=739`,
    shared prime 3 not in Π (998 total failures). Retired, not
    re-attempted. Lemma CB (Core Blocking), which built Π, remains
    valid/certified/reusable — only the Π construction on top of it died.
  - Escape-prime finiteness via NIDF pigeonhole (Step 4′, new framing) —
    because Lemma NIDF's injection argument needs no size bound on either
    family, and the same technique (map each escape prime to a fixed
    finite anchor companion set) is a plausible, untried adaptation.
Open gaps: Step 3, Step 4′ (crux), Step 5 assembly.
Cases to cover: Case B only this round — the harder residual, explicitly
distinct from sibling sunflower-inadmissibility-toolkit's Case A scope.
Watch out for: never re-attempt the refuted §8.3 Π construction in any
form (explicit counterexample on record).

forced-primes-well-ordering: revise
Target: the whole problem, via Theorem SW → Theorem 5.1. Pivots away from
direct `(MRS_S)`-for-`{103,197}` pursuit (this round's mrs-s-scoped
explorer pushed the local antichain-freeze simulation to n=10,000,000,
~100x past the already-known freeze index, found zero further leverage
beyond the already-certified No-Shortcut Corollary showing this equi-hard
to the abandoned Multi-Companion target) toward Backbone Permanence for
Case B pairs — a SECOND, independent mechanism alongside
sunflower-bundle-closure's, since Backbone Permanence is proven (by both
this round's explorers) to be a strictly weaker, single-class object,
NOT touched by the No-Shortcut Corollary's equi-hardness proof (which is
specifically about the full local antichain 𝓥_S^loc).
Technique: adapt the already-certified Local No-Resurrection Lemma
(§J Step 1, competitor pool restricted to I_S, no cross-family reasoning)
from the full local antichain to the coarser running-intersection object
B_k (same definition as sunflower-inadmissibility-toolkit's Step 1,
shared, cited not redefined).
Skeleton:
  1. Restate Backbone Permanence Lemma (shared statement, cite sibling
     file, do not re-derive).
  2. Attempt the Backbone-to-Antichain Bridge: does B(S')'s stabilization
     value coincide with an actual locally-minimal antichain element at
     the same index, so the Local No-Resurrection Lemma's extremal
     argument transfers? Cheap sanity check first: does B_k's
     stabilization index empirically track this approach's own local
     antichain freeze indices?
  3. If the bridge exists, apply the Local Interval Lemma / Local
     Equivalence Theorem (§J Steps 3-4, cite) to conclude permanence.
  4. Combine with sibling's Lemma UCR (cite) to close (JW) for the pair.
Key lemmas:
  - Local No-Resurrection Lemma (already certified) — restated as the
    source technique to transplant.
  - Backbone-to-Antichain Bridge (Step 2, new, open, the crux) —
    conjectured on a not-yet-checked empirical coincidence of
    stabilization indices; report as a clean negative finding if the
    extremal argument fundamentally cannot transfer.
Open gaps: the Bridge (Step 2) is the crux; Steps 3-4 conditional on it.
Cases to cover: Case B pairs (same scope as sunflower-bundle-closure,
deliberately a second rival mechanism for the same hard residual).
Watch out for: do not silently re-attempt `(MRS_S)`-for-`{103,197}` under
a new name — the No-Shortcut Corollary stands, re-confirmed this round;
Backbone Permanence must stay explicitly distinct from `(MRS_S)` in the
write-up.

intersecting-family-covering-construction: revise
Target: the whole problem, via Theorem SW → Proposition 9.4 → Theorem 5.1,
retargeting Step 2 (eventual near-periodicity of class membership, the
sole open ingredient of `(PD_{S,S'})`) away from the retired "dyadic
near-fraction" hint (this round resolved `a_1=4087`'s clean-looking
densities as an artifact of its small exact period, not a universal
2-adic mechanism) toward a bounded-run-length/pigeonhole argument on the
FIXED, bounded `P_1`-core alphabet, motivated by this round's much
stronger finding: G_n (the coarse P_1-core-membership sequence) is
EXACTLY periodic from n=1 in 4/5 tractable tested instances, rigorously
verified via KMP/Border-Lemma exact-period computation (not density
estimation), stable over 1600+ repeated periods in the best case.
Technique: an inequality (run-length bound), not a prediction claim —
explicitly sidesteps round 4's proven-dead bounded-window Markov
prediction mechanism (circular: window size needed equals the true
period) and the dead seesaw/Complement-Bound mechanism (no leverage on
bounding any single class away from 0); uses the already-certified Growth
Lemma's O(n) bound on a_n as an external anchor legitimate for this
BOUNDED-alphabet target (unlike (UB_S)/(MRS_S), which provably lack one).
Skeleton (Step 1, 3-4 of round 11 unchanged; Step 2 replaced):
  1. Complement Bound Lemma (already certified, unchanged, cite).
  2′. Bounded-Run-Length Lemma (new crux, open): no R+1 consecutive
     indices can all avoid core S', for some finite R=R(a_1); attempted
     via "reusing a P_1-prime is cheaper than an ever-larger companion
     bundle," anchored by the Growth Lemma.
  3′. (PD_{S,S'}) from Bounded-Run-Length — immediate pigeonhole once R
     exists, constant c=1/(R+1).
  4′. Exact periodicity from n=1 — optional stretch goal matching this
     round's KMP numerics, not required for Theorem SW.
Key lemmas:
  - Bounded-Run-Length Lemma (Step 2′, crux, open) — conjectured because
    G_n is exactly periodic (stronger than density-stable) in every
    tractable instance, and the fixed finite P_1 alphabet gives a genuine
    external anchor (Growth Lemma) this target has that (UB_S)/(MRS_S)
    provably lack.
  - (PD_{S,S'}) from Bounded-Run-Length (Step 3′) — elementary pigeonhole.
Open gaps: Bounded-Run-Length Lemma (Step 2′, the crux); the general
|T_infty|>=3 case (unchanged from round 11, lower priority);
a_1=21528751 remains numerically inconclusive for G_n-periodicity at
N=400,000 (concrete numerical follow-up, not required before a general
proof attempt).
Cases to cover: |T_infty|=2 vs >=3 (unchanged); report precisely if
Bounded-Run-Length is refuted on any instance.
Watch out for: do not re-attempt bounded-window Markov PREDICTION of
G_{n+1} (round 4, dead, circular) — Bounded-Run-Length is an inequality
claim, keep the distinction explicit. Do not resurrect the dyadic hint as
a proof strategy — confirmed this round to be a coincidental artifact of
a_1=4087's small period.

---

Not touched this round (left live, un-revised, no new content to add):
`persistent-backbone-monovariant` (Elo 1564.1, last touched round 8, its
sole remaining gap NIBC is already proven insufficient for the whole
problem even if closed — no new idea surfaced this round to justify a
revision); `explicit-window-backbone-construction`, `core-depth-
induction`, `imprint-automaton-periodicity`, `backbone-existence-crt`,
`global-recruiter-finiteness` (dead-end), `bounded-gap-density-covering`
(dead-end) — all parked, none touched.

Slugs built/revised this round: sunflower-inadmissibility-toolkit,
sunflower-bundle-closure, forced-primes-well-ordering,
intersecting-family-covering-construction.
