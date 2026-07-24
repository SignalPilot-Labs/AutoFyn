## imo-2026-06

covering-system-construction: revise
Target: there exist positive integers T, L with a_{n+T} = a_n + L for every positive
integer n.
Technique: (unchanged spine) explicit constructive recruitment of a finite "core"
prime pool via a single-witness pigeonhole argument (Bounded Witness Lemma / Finite
Core Theorem, both already certified), now COMBINED with a new round-2 mechanism to
close the crux gap (†): a minimality/exchange argument targeting a concrete "Universal
Glue Prime," split by whether Q = P(a_1) is "sparse" (misses small primes) or "dense"
(already contains them).
Skeleton:
  1. Free Facts (gcd(a_i,a_j)>1 for all i≠j) — direct from the hypothesis (certified,
     `lemmas/free-facts-gcd.md`).
  2. Persistent-Type Pigeonhole: finitely many "base types" τ(n) = P(a_n)∩Q, some
     persistent, eventually exhaustive — infinite pigeonhole (certified,
     `lemmas/persistent-type-pigeonhole.md`).
  3. Bounded Witness Lemma + Finite Core Theorem: an explicit finite prime pool S
     (built from ≤ 2^{|Q|}-1 fixed witnesses) such that every large term of a
     persistent type shares an S-prime with any disjoint persistent type's witness —
     certified, `lemmas/bounded-witness-lemma.md`, `lemmas/finite-core-theorem.md`.
  4. NEW (round 2): let p* = smallest prime not in Q. Prove the Universal Glue Prime
     Lemma — for n large with τ(n) ⊊ Q (proper base type), p* | a_n — via a
     minimality/exchange argument: exhibit an explicit p*-divisible legal candidate
     ≤ a_n + a_1·p* (by the Generalized Bounded Gap fact: a multiple of a_1·p* is
     always legal, same proof as the certified Bounded Gap Lemma with a_1 replaced by
     a_1·p*), then argue the greedy process, choosing the SMALLEST legal successor,
     could not have preferred a non-p*-divisible candidate needing a strictly "more
     expensive" (less dense) alternative prime scheme.
  5. If 4 holds (sparse-Q case): (†) follows for free — both types in any disjoint
     pair are proper subsets of Q (Q∩A=∅, A⊆Q, A≠∅ forces A⊊Q), so both eventually
     carry p*, so all extended-type refinements share p* ∈ S_0. No refinement case
     analysis needed at all.
  6. Dense-Q case (Q already contains several small primes, e.g. a_1=30,210): no
     single universal prime dominates (numerically confirmed this round). Fall back
     to a finite, explicit case-enumeration of the (small, since |𝒫|≤2^{|Q|}-1) family
     𝒫' of extended types for any FIXED a_1 — open in full generality, flagged as the
     harder residual sub-case.
  7. Finish (already fully proved, conditional on 4/6): CRT reduction mod L = ∏S_0,
     finite cyclic pigeonhole on good residues G, giving T=|G|, and a_{n+T}=a_n+L for
     n large (`knowledge_base.md` "Modular arithmetic, CRT"; "Pigeonhole / extremal
     principle").
  8. Secondary gap: extend periodicity back to n=1 (empirically true on every tested
     seed, not proved in general).
Key lemmas (claim + mechanism):
  - Bounded Witness Lemma / Finite Core Theorem — certified, mechanism: single-witness
    pigeonhole on the finite prime factorization of one fixed integer.
  - Universal Glue Prime Lemma (NEW, open) — mechanism: greedy minimality forces the
    cheapest (densest) reconciling condition, namely divisibility by the smallest
    prime outside Q, rather than a scarcer alternative — needs an EXPLICIT
    smallest-candidate size comparison, not a density heuristic.
Open gaps: the Universal Glue Prime Lemma (sparse-Q case, primary target — concrete,
narrower than the old (†)); the dense-Q fallback case (harder, largely untouched); the
n=1 boundary extension (secondary, downstream of the above).
Cases to cover: |Q|=1 (trivial, already resolved with no gap); |Q|≥2 sparse (primary
target of the round-2 mechanism); |Q|≥2 dense (Q ⊇ {2,3,...}, separate harder case).
Watch out for: do not conflate the trivial containment fact (a_n shares SOME S-prime
with each disjoint witness — already certified) with the stronger claim that ALL of
a_n's relevant extra factorization is confined to a SINGLE shared prime across every
disjoint partner simultaneously — the latter is what's actually open. Do not let the
minimality argument degrade into an unjustified "cheaper is smaller" hand-wave; it must
produce an explicit candidate and an explicit inequality.

greedy-exchange-cost-potential: new
Target: same as above (full eventual periodicity).
Technique: a genuinely different top-level framing — an explicit integer-valued cost
potential (number of "extra" primes outside Q dividing a_n) plus a minimality/exchange
argument, in the spirit of the aimo-0678 crux ("min-of-a-set" monovariant, adapted:
here it is a per-term recruitment cost, not the raw sequence value, since a_n itself
grows unboundedly unlike aimo-0678's bounded sequence). This is the round's answer to
the "shared-gap plateau — attack from a genuinely different framing" mandate: instead
of asking "do two disjoint families of sets intersect" (the persistent-type/covering
machinery all three round-1 approaches converge on), it asks "how expensive (in extra
primes) can a legal term ever be, and why."
Skeleton:
  1. Free Facts, Bounded Gap Lemma — imported unchanged (certified).
  2. NEW: Generalized Bounded Gap fact — a_{n+1} ≤ a_n + a_1·p for ANY prime p (proved
     unconditionally: the smallest multiple of a_1·p exceeding a_n is always legal,
     by the identical proof as the certified Bounded Gap Lemma).
  3. Define cost(n) := |P(a_n) \ Q|. Attempt to bound cost(n) via the Finite Core
     Theorem. IMPORTANT (self-corrected during outlining): a naive reading gives only
     the TRIVIAL bound |P(a_n) ∩ S| ≤ |S| (S finite, already certified) — it does NOT
     give a nontrivial bound on cost(n) itself, since the Finite Core Theorem only
     guarantees at least one shared S-prime per disjoint type, not exclusivity or a
     bound on total distinct extra primes.
  4. Reduce the finish to a finite enumeration: since S is finite and explicit for any
     fixed a_1, the question "does a single small subset of S serve every disjoint
     persistent type's requirement simultaneously" is a finite, checkable question —
     open in general, but concretely enumerable case-by-case for any specific a_1
     (recommended fallback route for the dense-Q case shared with
     covering-system-construction).
  5. Finish (same CRT + cyclic pigeonhole mechanism as the sibling approaches),
     conditional on resolving step 4.
Key lemmas (claim + mechanism):
  - Generalized Bounded Gap fact — mechanism: multiples of a_1·p are legal against
    every earlier term via the shared-Q-prime argument, exactly as the certified
    Bounded Gap Lemma, generalized to an extra factor p.
  - Trivial S-bound |P(a_n)∩S| ≤ |S| — mechanism: S is finite by the certified Finite
    Core Theorem; does not resolve the sharp question.
Open gaps: the sharp cost/consistency question of step 3-4 — on inspection this is
equivalent in substance to (†), reached from a per-term counting angle instead of a
family-intersection angle; disclosed honestly as NOT a full escape from the shared
crux, but a different (possibly more tractable, finite-enumeration-based) angle of
attack, plus a small independently-valuable new lemma (Generalized Bounded Gap fact).
Cases to cover: |Q|=1 (trivial); |Q|=2 sparse (recommended first target: the finite
enumeration has ≤ 2 disjoint pairs to check); dense Q (harder, shared with
covering-system-construction's fallback).
Watch out for: an earlier draft of this approach overclaimed a false unconditional
"cost(n) ≤ |𝒫|-1" bound; that error is flagged and corrected in the approach file
itself (`results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`) — builders
must not resurrect it without a real proof. Do not present the finite-enumeration
reframing as a proof of (†) — it is a scoping device, not a resolution.

amortized-charging-budget: advance (low priority / stale this round)
Target: same as above.
Technique: unchanged — amortized charging/potential-budget argument bounding total
recruitment events, now understood to bottom out on essentially the same gap as
covering-system-construction's (†) (its own "Core Lemma," Section 5).
Skeleton: unchanged from round 1 (Free Facts, Bounded Gap Lemma, Recurrent-Pattern
Pigeonhole, Forced-Linking-Prime Lemma, all certified; conditional CRT+pigeonhole
finish in Section 6, fully proved conditional on the Core Lemma).
Key lemmas: unchanged; Core Lemma remains the open gap, now understood to be
essentially equivalent to (†).
Open gaps: same Core Lemma as before. NOT revised this round — recommend the
outline-reviewer deprioritize a fresh builder pass here in favor of
covering-system-construction (more precise statement of the identical gap, and
already has the round-2 Universal Glue Prime mechanism attached); once/if that
mechanism succeeds, amortized-charging-budget's Core Lemma can import it directly
without independent re-derivation.
Cases to cover: none new.
Watch out for: do not spend a builder slot duplicating the same gap-closing attempt
here and in covering-system-construction in the same round — CLAUDE.md's
single-gap-trap warning applies to simultaneously patching two near-identical stuck
approaches with the same fix, not just to splitting one approach across slugs.

density-sieve-contradiction: advance (low priority / stale this round)
Target: same as above.
Technique: unchanged — proof by contradiction via density/sieve estimates on gap size,
noting its own step 4 ("each new recruited prime pays for itself") was this round's
seed for the Universal Glue Prime mechanism now developed in
covering-system-construction and greedy-exchange-cost-potential.
Skeleton: unchanged from round 1.
Open gaps: same as round 1 (gap-boundedness by contradiction, non-circular version) —
its author's own step 3 (raw Mertens/sieve estimate) is flagged by this round's
explorers as likely intractable (the "working prime set" is not a priori fixed, so
density estimates risk circularity); step 4 is the live seed, now absorbed into the
other two approaches above. Recommend NOT re-attempting the sieve route (step 3)
without first seeing whether the minimality mechanism (already being developed
elsewhere) succeeds; if it does, this approach's per-step-4 content becomes
redundant, so it should stay stale rather than consume a builder slot this round.
Cases to cover: none new.
Watch out for: do not silently assume a fixed working prime set when estimating
densities — the total prime support of {a_1,...,a_n} is UNBOUNDED (verified
numerically this round, see `/tmp/round-2/math-explorer-hypergraph.md` point 4); any
argument implicitly bounding "all primes ever used" (rather than the certified,
carefully-selected finite core S) is attacking a false sub-claim and should be
rejected on sight.

hypergraph-transversal: advance (low priority / stale this round)
Target: same as above.
Technique: unchanged — minimal-antichain / transversal encoding of the covering
condition, with an (unproved) monovariant-potential argument for finiteness of the
eventual prime support.
Skeleton: unchanged from round 1.
Open gaps: same as round 1 (finiteness of S via the Φ_n = Σ 2^{-min(B)} potential) —
flagged by this round's explorer as under-specified and likely to re-derive, not
surpass, the already-certified Finite Core Theorem by a different (less successful)
route. Recommend NOT re-attempting this exact potential function without a
substantively new idea; if the field wants a monovariant-flavored attempt this round,
greedy-exchange-cost-potential is the better-developed vehicle for that idea.
Cases to cover: none new.
Watch out for: do not conflate "the antichain M_n has bounded elements" (a set-size
claim) with "M_n has bounded underlying prime support" (a different finiteness claim);
only the latter matters and neither round-1 draft nor this round's explorers found a
route to it via the antichain/potential vocabulary that the certified Finite Core
Theorem doesn't already give more directly.

---

### Outliner's recommendation for the build set

Primary: **covering-system-construction** — highest Elo, most precise prior gap
statement, and now carries the round's best-developed concrete attack (Universal Glue
Prime Lemma + sparse/dense split) on the shared crux (†). This is the strongest
candidate to make real progress this round.

Secondary (for population diversity, per CLAUDE.md's plateau-break rule): **new
approach greedy-exchange-cost-potential** — a genuinely different top-level framing
(cost potential + minimality, not family-intersection), explicitly requested by this
round's dispatch instructions as the furthest-from-the-field framing available. Its
honest self-correction (retracting an initial overclaim) shows real rigor; its
concrete deliverable this round is the Generalized Bounded Gap fact (small, genuinely
new, unconditional) plus a useful reframing of the remaining gap as a finite
enumeration, which may be a more tractable target for a builder than the fully
abstract (†).

Do NOT build this round: amortized-charging-budget, density-sieve-contradiction,
hypergraph-transversal — all three are live but stale, and none offers a genuinely
new mechanism beyond what covering-system-construction and greedy-exchange-cost-
potential now carry; building them in parallel this round would duplicate effort on
the identical crux rather than diversify it (the single-gap-trap CLAUDE.md warns
against, applied across approaches rather than within one). If the outline-reviewer
has spare builder capacity, the best use of a third slot would be
covering-system-construction's dense-Q sub-case (Step 4b Case (ii)) as an
independent sub-target within the SAME approach file, not a separate slug.

Slugs touched/opened this round:
- covering-system-construction — REVISED (Step 4b added: Universal Glue Prime Lemma,
  sparse/dense split; Open gaps and Approaches-tried sections updated).
- greedy-exchange-cost-potential — NEW (opened, including an in-file self-correction
  of an initial overclaim).
- amortized-charging-budget, density-sieve-contradiction, hypergraph-transversal —
  left untouched, explicitly recommended stale/low-priority this round (not revised,
  not nominated to build).
