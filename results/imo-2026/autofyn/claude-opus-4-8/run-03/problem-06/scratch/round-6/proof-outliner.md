## imo-2026-06

Context for the reviewer. 5-round STRUCTURAL plateau on the single open crux **E5″ / Π-finite**.
All three R6 explorers independently reported that routes (ii) direct-periodicity and (iii)
alt-reduction are **exhausted/proven-collapse** (both re-derive the certified Reduction-Lemma =
Π-finite equivalence, and the direct-periodicity explorer freshly closed the last loophole by proving
the "converse gap" — A periodic mod K while Π infinite — does NOT exist, via certified E3/TAS). Route
(i) joint-potential is likewise mostly forbidden-in-disguise (openings 1/2/4 = density-of-A, JSC-spread,
Φ_N respectively; opening 3 = anchor-partition restated). The joint-potential explorer flagged **exactly
one** genuinely-unexhausted thread — opening 5, "joint multi-fiber recruitment-rate accounting" — as
"worth one more probe, cut fast if the first concrete inequality is a disguised ∏G/|t−t′| bound."

Per the dispatch mandate I put up (a) the leader to ADVANCE (consolidation only), and (b) ONE new
far-framing pole instantiating that last thread as a concrete **greedy-rejection-budget** accounting,
with the cheap-kill check hoisted to a front-and-center gap. I have done a **preliminary cheap-kill
myself** (recorded below) — it does NOT clear cleanly; I am seeding it anyway per dispatch because the
reviewer's vote either (i) finds the realizability escape (breakthrough) or (ii) certifies the fork as a
negative theorem (closing this last thread permanently, the way TAS/JSC closed the spread lever). Both
outcomes advance the run. I explicitly DECLINE to pad the field with poles I have already shown fork
(listed at the end) — per role-rule R5#16, a fake plateau-breaker is worse than none.

---

redundant-constraint-antichain: advance
Target: a_{n+T}=a_n+L for all n≥1 (whole theorem) via the Finite-Alphabet crux (𝓐_∞ finite).
Technique: order-theoretic antichain / transversal reduction (no-transient) + realizer-value pincer;
  this is the certified spine, everything but E5″ is proved.
Skeleton (all steps ● certified except the last):
  1. ● no-transient: a_{n+1}=s(a_n) for all n≥1, fixed successor on fixed set A.
  2. ● admissible ⟺ meets every ⊆-minimal support (E1/E2); private-witness q≤|t−t′| (E3).
  3. ● Crux ⟺ E4 (sup|G|<∞) ⟺ E5″ (∏(G∖{p_max})<a₁ on the ∏G≥a₁ subclass); ∏G<a₁ subclass
     fully closed (Prop 12.A).
  4. ○ E5″ — the sole open arrow.
Key lemmas: all certified (free-lemmas, no-transient, enumeration-and-transversal, size-bound-reduction,
  realizer-value-pincer, anchor-partition, two-anchor-scaffold).
Open gaps: E5″ only. NOMINATE-TO-ADVANCE for CONSOLIDATION ONLY — no new E5″ lever appeared this round,
  so do NOT re-plan it (per dispatch). The builder should keep §13 tidy and cross-link the new pole's
  cheap-kill outcome (whichever way it goes) as a certified guardrail, exactly as JSC/Collapse were.
Cases to cover: none new.
Watch out for: do NOT re-derive any ∏G/p_max/|t−t′|/density/sub-support lever (all proven-forked).

---

joint-recruitment-budget: new  ← FAR-FRAMING POLE; reviewer MUST vet HARD (see cheap-kill gap)
Target: a_{n+T}=a_n+L for all n≥1 (whole theorem), by proving 𝓐_∞ finite through a GLOBAL accounting
  that reads the greedy REJECTION stream (the choices), never bounding any single-support/pair quantity.
Technique: resource/monovariant accounting on the per-step bounded rejection budget, with
  per-recruit DISJOINT attribution — the one joint-system lens (opening 5) not yet proven forbidden.
  Distinct from every prior pole: it is NOT an A_n-statistic (it counts blocking EVENTS with
  support-attribution, reading which c were rejected and by whom), NOT a ∏G bound, NOT a |t−t′| spread,
  NOT an automaton, NOT a sub-support realization.
Skeleton:
  1. Rejection stream. For each step let R_n={c : a_n<c<a_{n+1}}. Each c∈R_n is inadmissible, so by
     no-transient + E1/E2 there is a minimal support F(c)∈𝓐_n with gcd(c,∏F(c))=1 (c misses F(c)).
     — by certified no-transient-fixed-successor + admissibility characterization.
  2. Budget is bounded-rate. Σ_{n<N}|R_n| = a_N−a₁−(N−1) ≤ (M−1)(N−1), M=rad(a₁) fixed.
     — by certified Gap-bound L2 (each gap ≤ M). [⚠ this equals Φ_N, the cumulative gap-deficit.]
  3. Recruitment attribution. When a NEW largest prime q is first recruited (first appears in a minimal
     support G_q; its realizer ∏G_q is a term by R1), attach to q a cost set C_q ⊆ (rejected candidates)
     of blocks that are FORCED by the newness of G_q / by supports containing q, defined so distinct
     recruits get DISJOINT cost sets. — by a to-be-constructed attribution rule (LOAD-BEARING, open).
  4. Per-recruit cost →∞. Show |C_q| ≥ c_q with c_q→∞ as q→∞. — LOAD-BEARING, open, THE cheap-kill target.
  5. Conclusion. If Π infinite there are recruits q_1<q_2<… with Σ|C_{q_k}| ≤ Σ_{n<N}|R_n| = O(N) yet the
     LHS →∞ faster than N (disjoint costs, each ≥c_{q_k}→∞) — contradiction ⇒ Π finite ⇒ theorem (certified
     Reduction Lemma + no-transient give T,L from n=1).
Key lemmas (claim + mechanism):
  - Budget bound Σ|R_n| ≤ (M−1)N — because each greedy gap ≤ M (certified L2). SOUND but see cheap-kill.
  - Disjoint-attribution + cost→∞ (OPEN, load-bearing) — the ONLY viable mechanism must exploit
    REALIZABILITY/self-blocking (TAS: a real recruit's E3 private witness is forced onto a SECOND fixed
    anchor p**≠p*), because the non-realizable obstruction family {p*,q_k} is the standing counterexample
    to every non-realizability-based count (see cheap-kill). The cost of recruit q_k must be the
    rejections generated in the length-≤M window topping out at ∏G_{q_k} together with the second-anchor
    realizer t′_k that TAS forces — phrased so the count is an aggregate rejection tally, NOT the spread
    |t_k−t′_k| and NOT a ∏G bound.
Open gaps:
  - G-cost: the disjoint per-recruit attribution with cost c_q→∞ (steps 3–4).
  - ★ CHEAP-KILL CHECK (RUN FIRST, before any build investment; explorer-mandated). Write the first
    concrete inequality step 4 needs and test whether it reduces to any of: (a) "budget/N → density(A)"
    i.e. Φ_N; (b) "∏G_q ≤ f(a₁)"; (c) "|t_k−t′_k| ≤ f(a₁)"; (d) "a proper sub-support of G_q is realized."
    Any of these ⇒ FORBIDDEN lever in disguise ⇒ RETHINK, and record the fork as a certified negative
    guardrail (like JSC/Collapse).
    **My preliminary cheap-kill (reviewer: verify and decide):** the RAW budget of step 2 IS Φ_N =
    a_N−a₁−(N−1), the density quantity (explorer opening 4), and the certified obstruction family
    {p*,q_k} has Φ_N/N bounded (density→1/p*>0) WITH infinitely many recruits — so any NON-attributed
    budget count provably fails. The pole is viable ONLY IF step 3's attribution+realizability refinement
    produces a per-recruit disjoint cost c_q→∞ that the (non-realizable) obstruction family evades, WITHOUT
    that cost secretly being |t_k−t′_k| (JSC-dead) or ∏G_q (dead). I could not land such a cost in the
    outline; that is precisely the load-bearing gap the builder must fill or the reviewer must certify-kill.
Cases to cover:
  - |P|=1 (a₁ a prime power): dispose separately exactly as in TAS (certified two-anchor-scaffold, |P|=1 case).
  - |P|≥2 main case: the multi-fiber accounting above.
Watch out for:
  - The obstruction family {p*,q_k} is the acid test: any candidate cost that does NOT →∞ on it (it is
    non-realizable, so it MAY legitimately be excluded — but only via a realizability lemma, not by fiat).
  - Do NOT let the cost degenerate into the JSC spread |t_k−t′_k| (proven equivalent to the magnitude
    bound) or into ∏G_q (dead) or into Φ_N/density (dead) — those are the four fork traps above.
  - Do NOT invoke "a dominating common sub-support is realized" (R4 Collapse theorem forbids it).

---

Declined new poles (weighed and NOT seeded — recorded so R7 does not rediscover them):
  - growth-rate clash on ω(a_n)=O(log n/log log n) (route iii idea 6): FROZEN by the obstruction family,
    which keeps |G_k|=|{p*,q_k}|=2 (ω bounded) with Π infinite — same vacuity as density. Not seeded.
  - intersecting-family / EKR / sunflower extremal (route i opening 3): rediscovers the certified
    anchor-partition pole verbatim (needs |G|≤k = E5 as hypothesis; infinite star = the anchor fiber).
    Not seeded.
  - sieve-weight Ψ_n=Σ1/∏G, aggregate witness-pair double-count, cumulative Φ_N (openings 1/2/4):
    density-of-A / JSC-spread / Φ_N in disguise. Not seeded.
  - "A periodic mod finite K" weaker target (route ii): the direct-periodicity explorer PROVED this round
    the converse gap does not exist (A periodic mod K ⟺ Π finite via E3/TAS). Closed. Not seeded.

build set candidates handed to the reviewer: redundant-constraint-antichain (advance/consolidate),
joint-recruitment-budget (new far-framing pole — VET HARD against the four fork traps; my preliminary
cheap-kill flags the raw budget = Φ_N, so the pole stands or falls on step 3's realizability-based
disjoint-cost refinement, which the reviewer should adjudicate before committing a full build).
