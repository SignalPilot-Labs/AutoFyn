## imo-2026-06

Context recap (verified against current.md, all 8 rounds, and the round-9 explorer
reports): the entire certified chain — Free Facts, Bounded Gap, Persistent-Type
Pigeonhole, Finite Core Theorem, Generalized Bounded Witness Lemma, Projection Lemma +
Collateral-Safety Theorem (round 6) — unconditionally reduces the whole problem to one
open gap: does the recruitment process on the FIXED finite index set of disjoint
base-type pairs terminate, i.e. is open(k) = ∅ for some finite k? Six direct-mechanism
attacks on literal zero-exception Full-Absorption Hypothesis (FAH)/Symmetric FAH have
failed (Two-Witness Uniqueness, Blocking-Data Bridging, algebraic-recursion transplant,
seed-coupling induction, Fixed-Witness Divisor-Chain same-side dichotomy, all three
charging variants) — Lemma I's diagnosis: nothing in the certified toolkit promotes
"some prime of a ≥2-menu works" into "one specific prime always works." |F'|=1 is
already unconditionally solved (Singleton-Side FAH, certified) — do not re-target it.
Per CLAUDE.md's plateau-breaking rule, this round puts the "count exceptions, don't
eliminate them" / "recruitment-round-counting" framing on the table as new/revised
approaches, genuinely different from the six dead per-occurrence-absorption mechanisms.

**Verified framing fact (re-derived here, not just asserted by the crux-mining
explorer):** `covering-system-construction` Step 8.5's actual use of Symmetric FAH only
needs, for the Lemma-G prime q_i and rogue pair (A'_i,B'_i), that q_i divide ALL BUT
FINITELY MANY A'_i-type occurrences (not literally every one). Re-reading Step 8.5's
proof: it needs infinitely many n with ρ₁(n)=A'' (S₁-extended-persistent, so infinite by
definition) to satisfy ρ(n)=A'_i and q_i|a_n, so q_i∈ρ₁(n)=A''. If q_i divides only
cofinitely many A'_i-occurrences, the finitely many exceptions are simply absorbed into
the "eventually" clause of the already-certified Persistent-Type Pigeonhole /
Extended Persistent-Type Pigeonhole (an S₁-extended-persistent type is by definition one
occurring infinitely often; a finite exceptional subset without q_i is not itself
persistent, so it never registers as a competing type at S₁ — it just delays the
threshold beyond which the induction argument fires). **So cofinite FAH is provably
sufficient for the existing finish; literal zero-exception FAH is strictly more than the
problem needs.** This licenses treating "cofinite FAH" as a legitimate, weaker,
not-yet-attempted target.

---

covering-system-construction: revise
Target: the problem's actual claim — ∃T,L with a_{n+T}=a_n+L for all n — via the
existing constructive-induction / covering-system route (Free Facts → Finite Core →
Collateral-Safety open(k) reduction → CRT finish), now re-planning the FAH gap as a
**global recruitment-budget counting bound** instead of a per-occurrence absorption
claim.
Technique: pigeonhole/counting on a FIXED finite prime pool (elementary, not existential
per-occurrence pigeonhole) — the "Opening 1" framing from this round's fresh-framing
explorer, anchored to the already-certified Collateral-Safety monotone open(k)
reduction, so it imports Step 8's machinery wholesale rather than re-deriving it.
Skeleton:
  1. (Already certified, import verbatim.) Collateral-Safety Theorem: open(k) is a
     non-increasing sequence of subsets of a FIXED finite index set (≤ C(|𝒫|,2) disjoint
     base-type pairs, fixed once and for all since Q never changes) — by
     `lemmas/collateral-safety-theorem.md`.
  2. (Already certified, import verbatim.) Whenever open(k) ≠ ∅, the Generalized Bounded
     Witness Lemma's Corollary forces a genuinely NEW prime q ∉ S₀^(k) into S₀^(k+1) —
     by `lemmas/generalized-bounded-witness-lemma.md`.
  3. **New target — Recruitment-Budget Lemma.** Define, for each disjoint base-type
     pair (A,B) ∈ open(0), the FIXED Q-level witness set W_{A,B} :=
     P(a_{m_A}) ∪ P(a_{m_B}) (m_A, m_B the earliest occurrences of base types A, B —
     Q-level objects, provably S₀-independent by the Same-Side Ordering Lemma). Claim:
     every prime EVER recruited by the Generalized Bounded Witness Lemma's Corollary
     against pair (A,B), at ANY stage k, lies in W_{A,B}. If true, since W_{A,B} is
     finite and computable from a finite sequence prefix, S₀^(k) ∩ (⋃_{(A,B)} W_{A,B})
     grows by ≥1 element each round open(k)≠∅ but is capped by the finite union
     ⋃ W_{A,B} — forcing open(k)=∅ within ≤ Σ|W_{A,B}| rounds by pure pigeonhole, with
     ZERO absorption/cofinite-divisibility content needed.
  4. **Cheap kill FIRST (mandatory before investing in Step 3's proof):** run a
     computational check on every available multi-round-eligible seed (a_1=175, 187,
     209, 4807, plus any seed needing a genuine 2nd recruitment round if one can be
     found) — does the recruited prime at EVERY round lie in W_{A,B} for the pair's
     fixed base-level witnesses m_A, m_B specifically (not the extended-type witnesses
     n_A, n_B, which the Witness Discontinuity Obstruction shows CAN drift)? This is a
     one-script check, not yet run by any approach — do it before writing a proof.
  5. If Step 4 confirms the claim: prove the Recruitment-Budget Lemma directly. Likely
     mechanism: induct on rounds, using the Generalized Bounded Witness Lemma's own
     proof (which constructs the recruited prime as a factor of a specific witness term
     divisible by a_{m_B}-side data) to show the recruited prime's origin is always
     traceable back to P(a_{m_A}) ∪ P(a_{m_B}) via a chain of gcds bounded in length by
     |S₀^(k)|.
  6. If Step 4 REFUTES the claim (a recruited prime lies outside W_{A,B}): this
     approach's mechanism dies as scoped, but the failure itself is informative — report
     exactly which extended-witness discontinuity produced the escaping prime, and
     whether a LARGER but still finite and Q-level-computable pool (e.g. closed under
     one further gcd-chain step) could be substituted; do not silently expand the pool
     ad infinitely without proving IT is still finite and independent of k.
  7. Given the Recruitment-Budget Lemma (Step 3), conclude open(k)=∅ for k ≤ the
     explicit bound, hence (†) holds; combine with the unconditional Step 5/CRT finish
     (already proved in this file) for the full theorem, modulo the still-open secondary
     n=1 gap (Exact-Equality Reduction Lemma, unchanged, orthogonal to this gap).
Key lemmas (claim + mechanism):
  - Recruitment-Budget Lemma (Step 3) — because every prime the Generalized Bounded
    Witness Lemma's Corollary can ever produce is extracted as a factor of a gcd
    involving the FIXED base-level witness terms a_{m_A}, a_{m_B} (this is the actual
    mechanism inside that lemma's own proof — needs to be re-examined line-by-line to
    confirm the extracted prime's provenance, not assumed).
Open gaps: the Recruitment-Budget Lemma itself (Step 3/5) — genuinely new, not yet
attempted by anyone; Step 4's computational check is a prerequisite, not yet run.
Cases to cover: Step 4's check must include at least one seed with a documented 2-round
recruitment history if any exists in the workspace's computational record (search for
one; if none exists, note this as a gap in evidence, not proof).
Watch out for: the Witness Discontinuity Obstruction (certified) shows EXTENDED-type
witnesses can drift when the core grows — the whole viability of this approach rests on
BASE-type witnesses m_A, m_B being immune to this (they are Q-level, defined before any
recruitment, and Same-Side Ordering Lemma gives a partial handle) — this must be
verified, not assumed, exactly as the fresh-framing explorer flagged.

---

cofinite-window-capacity-bound: new
Target: the problem's actual claim, end to end — reduce it (as in the shared certified
chain up through Collateral-Safety) to base-type-pair termination, then close that gap
by proving **cofinite FAH** (finitely many exceptions, not the literal zero-exception
form) via a window-capacity counting bound, exploiting the verified sufficiency fact
above (cofinite FAH already suffices for Step 8.5's finish — no further weakening of
the target is needed once this is proved).
Technique: window-capacity counting / pigeonhole-on-bounded-exception-count, adapted
from crux `aimo-0051` ("a fixed-width window can miss at most O(1) values from a single
chain, given an a priori finite structural bound ⟹ globally finitely many misses").
This is a genuinely different KIND of argument from every dead mechanism (which all
tried to force a single logical contradiction from one witness) — it instead bounds a
COUNT via double-counting against an already-certified finite structural ceiling.
Skeleton:
  1. Import the shared reduction (Free Facts → Persistent-Type Pigeonhole → Finite Core
     Theorem → Generalized Bounded Witness Lemma → Projection Lemma + Collateral-Safety
     Theorem) verbatim from `covering-system-construction` — no changes, all certified.
  2. State the target precisely: for a rogue pair (A',B') with canonical Lemma-G prime
     q* and Q-level witnesses n_A<n_B, the exception set
     E := {n > n_B : ρ(n)=A', q* ∤ a_n} is FINITE (not necessarily empty).
  3. **Window-capacity bound.** For a window [n_B, N], lower-bound the number of
     A'-type occurrences in the window via the Generalized Bounded Gap Lemma
     (a_{n+1} ≤ a_n + c gives a linear lower bound on how many A'-type terms occur in
     any sufficiently long index range, since A' is persistent — reuse
     Persistent-Type Pigeonhole's "occurs infinitely often" with an explicit rate,
     which may itself need a first sub-lemma: an explicit positive lower density for
     any persistent type, not currently in the certified stack — check whether this is
     already implicit in the existing proofs or needs proving fresh). Separately,
     upper-bound |E ∩ [n_B,N]| using the certified Divisor-Chain Well-Definedness Lemma:
     each exceptional n contributes a witness to some d_n ∈ Div(a_{n_A}) \ {q*}-related
     value (or, more directly, each exceptional n corresponds to a distinct "escape"
     event constrained by the finite menu F'' \ {q*}); the aim is to show the escape
     events cannot recur within a bounded number of consecutive A'-occurrences without
     forcing a SMALLER witness contradicting Q-level Free Facts (an actual counting
     argument to be constructed, not yet attempted by any prior approach — this is the
     approach's genuine open content).
  4. If Step 3's window-capacity bound is established: E finite follows immediately
     (grow N →∞, escape count per window stays O(1), so cumulative count over disjoint
     windows... — actually needs the bound to be UNIFORM/summable, not just O(1) per
     window, i.e. E's growth must be sublinear/bounded absolute — flag explicitly as
     the sharp point to get right: an O(1)-per-window bound alone gives density control,
     not finiteness; the proof must show the O(1) constant can be taken to be 0 beyond
     some explicit window, or that escapes are confined to an explicitly bounded initial
     range).
  5. Combine with the re-derived sufficiency fact above (cofinite FAH ⟹ Step 8.5's
     argument goes through) to finish exactly as `covering-system-construction`'s Step 5
     CRT/cyclic-pigeonhole (import verbatim, no changes needed beyond the "eventually"
     threshold already built into the existing proof).
Key lemmas (claim + mechanism):
  - Cofinite sufficiency (verified above in this outline's preamble) — because an
    S₁-extended-persistent type is by definition one occurring infinitely often; a
    finite exceptional subset lacking q_i is automatically non-persistent and gets
    absorbed into the "eventually" threshold already present in Extended
    Persistent-Type Pigeonhole.
  - Window-capacity exception bound (Step 3, the genuinely new content) — because each
    escape event (n with q*∤a_n) is forced, by Free Facts + the finite menu F''\{q*},
    to be witnessed by a DIFFERENT element of a bounded-size structure (Div(a_{n_A}) or
    similar), so escapes cannot repeat densely without contradicting an already-finite
    count — mechanism to be made precise by the builder; this is the hard step.
Open gaps: Step 3 (the actual counting bound) is unattempted by any prior approach —
genuinely new content; Step 4's upgrade from "O(1) per window" to "finitely many total"
needs care (flagged explicitly, a place this could silently fail to close the gap even
if Step 3 succeeds).
Cases to cover: none beyond the standard rogue-pair case (already reduced to this by
Collateral-Safety).
Watch out for: do NOT let the builder quietly re-derive literal zero-exception FAH and
call it "cofinite" — the point of this approach is that a genuinely weaker, counting-
based target may be tractable where the existential-to-universal promotion (Lemma I's
diagnosis) is not; if the builder's argument secretly forces zero exceptions, that is
fine (stronger than needed) but should not be assumed as the easy case.

---

greedy-exchange-cost-potential: revise
Target: the problem's actual claim, via the cost/witness-prime pigeonhole vocabulary
already established in this approach's earlier steps (Free Facts, Generalized Bounded
Gap Lemma, Divisor-Restricted Pigeonhole, Adjacent Multiple Blocking), now re-planning
the FAH gap using a **downward-transport / predecessor-inheritance induction** — a
mechanism genuinely different from both siblings' counting/window approaches above.
Technique: adapted from crux `aimo-0016`'s "upgrade an infinitely-often relation to
a for-all relation via one-step predecessor inheritance on an auxiliary sequence."
Skeleton:
  1. Import (already certified): Generalized Bounded Witness Lemma gives D :=
     {n > n_B : ρ(n)=A', q*|a_n} is infinite (the free "existential" half already
     proved). Let n_1 < n_2 < ... enumerate the FULL A'-occurrence index set (all of it,
     not just D) past n_B.
  2. **Cheap kill first (mandatory before the proof attempt):** on a_1=4807's rogue pair
     (q=17 at the properly recruited core, per round 6's 0/151 record — re-run with a
     much larger sample, N in the thousands, per the fah-mechanism explorer's flagged
     concern that round 8's "6%" figure was measured at the wrong granularity), check
     whether the FAILURES (n ∉ D, i.e. q*∤a_{n_j}) are scattered/isolated among
     consecutive A'-occurrences, or come in runs. If failures are scattered (isolated,
     no two consecutive), a one-step "q* divides occurrence j ⟹ q* divides occurrence
     j+1" transport lemma is FALSE on its face and this approach should pivot
     immediately to a "distance between consecutive failures is bounded" claim instead
     (a cofinite-style target, converging with the sibling `cofinite-window-capacity-
     bound` approach — acceptable, report the convergence honestly rather than forcing
     a false transport claim).
  3. **New target — Auxiliary Transport Lemma.** Define an auxiliary quantity
     e_j := gcd(a_{n_j}, a_{n_{j+1}}) restricted to F''-primes (via the certified
     Divisor-Chain Well-Definedness Lemma, this is well-defined and finite-valued).
     Attempt: q* | a_{n_j} AND (some explicit side condition on e_j, TBD by the
     builder from Step 2's data) ⟹ q* | a_{n_{j+1}}. This must be built on the
     A'-occurrence-to-occurrence sequence itself (NOT on core-refinement stages) —
     explicitly distinct from what the certified Witness Discontinuity Obstruction
     refutes (that lemma is about a witness's own type drifting when S₀ grows; this is
     about consecutive occurrences of the SAME already-fixed extended type A').
  4. If Step 3 succeeds and D is shown to be "closed under successor from some point,"
     combined with D's infinitude (Step 1) this forces D to contain a whole tail, i.e.
     literal FAH (stronger than cofinite) — reuse `covering-system-construction`'s
     Step 8.5 finish unchanged.
  5. If Step 3 fails (as Step 2's cheap kill may already indicate), do not force it —
     report the precise failure mode and hand off to `cofinite-window-capacity-bound`'s
     counting framing as the more promising route for the SAME data.
Key lemmas (claim + mechanism):
  - Auxiliary Transport Lemma (Step 3) — candidate mechanism: the Generalized Bounded
    Gap Lemma constrains how much a_{n_{j+1}} can exceed a_{n_j} (bounded drift), which
    may force any prime dividing a_{n_j} that is "cheap" (small, already recruited) to
    remain available as a divisor of a_{n_{j+1}} — genuinely untested, flagged as
    speculative by the source crux-mining explorer, must be checked computationally
    (Step 2) before trusting the mechanism.
Open gaps: Step 3 is the entire open content, contingent on Step 2's cheap kill; genuine
risk of early pivot to the sibling framing if failures are scattered.
Cases to cover: none beyond the standard rogue-pair case.
Watch out for: do NOT silently re-derive the already-refuted Witness Discontinuity-style
recursion (core-refinement-stage persistence) — this must be occurrence-to-occurrence
within a FIXED type, a different object, as flagged explicitly in Step 3.

---

seed-coupling-induction: no action (dead, RETHINK, do not revive in this form).
Per the certified falsification (round 8, independently reconfirmed by builder and
reviewer): single-prime-removal seed reduction fails reproducibly whenever 2∉Q'.
Not included in this round's build set; left out of the field entirely rather than
revised, since no viable different reduction step has been proposed by any explorer
this round.

Build-set recommendation for outline-reviewer: covering-system-construction (revised),
cofinite-window-capacity-bound (new), greedy-exchange-cost-potential (revised) — three
genuinely distinct mechanisms (global counting-budget on recruited primes; window-
capacity counting on exceptions; downward-transport induction on consecutive
occurrences), all targeting the same reduced gap but via structurally different routes,
satisfying CLAUDE.md's plateau-breaking requirement with more than one new framing.
