# proof-outliner report — round 6 — imo-2026-06

## What round 6's explorers established (recap, load-bearing for everything below)

1. **Universal Singleton Hypothesis is FALSIFIED, unconditionally, as a blanket
   claim.** Singleton-lens explorer: `a_1 = 4807` (Q={11,19,23}) gives a rogue pair
   A'={3,5,19}, B'={2,11} with earliest witnesses n_A=6, n_B=7, and
   F' = P(a_7)\S₀ = {13,17}, size 2. `a_1 = 11305` similarly gives F'={11,103}, size
   2. Both computed with the literal global-minimum witness convention (not the
   round-3/4 bug). **No approach may rely on |F'| = 1 in general from now on.** The
   `covering-system-construction` Conditional Single-Pair/Simultaneous Resolution
   Theorems and the `greedy-exchange-cost-potential` Round Resolution Lemma, as
   literally stated (conditional on Universal Singleton Hypothesis), are therefore
   conditional on a hypothesis now known to be false in general — they must be
   rebuilt on a different, not-yet-falsified hypothesis (see below), not merely
   re-asserted.
2. **But a strictly weaker, not-yet-falsified replacement is visible in the same
   data.** In the `a_1=4807` counterexample, the Lemma-G-guaranteed prime (17, from
   gcd(a_{n_A},a_{n_B})) divides **100% (151/151)** of all occurrences of the rogue
   type B'={2,11}, while the *other* element of F' (13) divides only ≈7% (11/151).
   Lemma H (Critical Prime Dichotomy) explains why: 13 falls into branch (a)
   (stripping it drops below the previous term — checked directly: 4862/13=374 ≤
   a_6=4845) at its one witnessing index, i.e. it is "incidental," not
   reconciliation-relevant. This suggests the correct target is **not** "F' is a
   singleton" but **"the Lemma-G prime achieves full absorption"** — see Approach 2
   below, a precise, different, unfalsified statement.
3. **The "collateral rogue pairs" gap (new in round 5) has an unconditional partial
   closure available now, for free.** Collateral-lens explorer: a **Projection
   Lemma** (S₁-persistent types project to S₀-persistent parents; base type is
   invariant under projection since Q ⊆ S₀ always) combined with the *already
   certified* Monotonicity of Resolution Lemma gives, with no new hypothesis and no
   Singleton Hypothesis of any kind: **a base-type pair that is fully safe at S₀
   stays fully safe at every S₁ ⊇ S₀.** Computationally confirmed on 646 fully-safe
   pairs across 82 seeds, 0 collateral violations — and now there is a real
   *unconditional* argument for why, not just numerics. This is a genuine, cheap,
   closeable sub-result — see Approach 1 below.
4. **No bypass of the recruitment framework exists.** Fresh-framing explorer:
   checked the closest corpus analog (`aimo-0678`, coupled gcd/lcm recursion) and
   confirmed our problem is "exactly one gap harder" because our admissibility
   condition has unbounded memory (checks against *every* earlier term), whereas
   aimo-0678's map is memoryless by construction — the finite-automaton framing
   (`reversible-transition-map`) is provably equivalent to V=∅, not a bypass. The
   complement/"skipped integers" reframing is also just a restatement. **Do not
   re-propose either.** The one live new idea: attack the *number of recruitment
   rounds* directly (bound or mere finiteness) rather than V=∅ pointwise — flagged
   as promising but with **no charging object yet identified** (honest gap).

## Field of approaches for round 6

Two live approaches are revised (their Singleton-Hypothesis-dependent content is
explicitly retired, replaced with a precisely stated new target); one new approach is
opened on the charging/termination-bound framing. `witness-index-descent` and
`reversible-transition-map` are **not** revived — both correctly RETHINK'd last round,
no new idea for either this round (their one surviving certified byproduct, Same-Side
Ordering Lemma, stays in the shared lemma pool). `amortized-charging-budget`,
`density-sieve-contradiction`, `hypergraph-transversal`, `witness-depth-bound` remain
correctly retired/stale.

---

### Approach 1 (revise): `covering-system-construction` — Collateral-Safety Theorem
+ relocate the crux to base-type-pair-level termination

**Retire explicitly:** the Conditional Single-Pair / Simultaneous Resolution
Theorems' *appeal to* the Universal Singleton Hypothesis is dead (falsified,
finding 1 above). Do not re-cite them as conditional on that hypothesis without
qualification; either restate them conditional on the new Full-Absorption Hypothesis
(Approach 2's target — cross-reference, don't reprove) or mark them retired pending
that approach's progress.

**New Step 8 — certify the Projection Lemma (trivial, ≤1 page).**
*Statement.* For S₀ ⊆ S₁ (finite, Q ⊆ S₀), ρ(n):=P(a_n)∩S₀, ρ₁(n):=P(a_n)∩S₁: if
A'' is S₁-extended-persistent then A' := A''∩S₀ is S₀-extended-persistent, and
A''∩Q = A'∩Q (same base type).
*Proof sketch (already found by the collateral explorer, just needs writing up
rigorously):* every n with ρ₁(n)=A'' has ρ(n) = ρ₁(n)∩S₀ = A' (fixed), so A' occurs
at least as often as A'', hence infinitely often — same pigeonhole mechanism as
Persistent-Type Pigeonhole / Extended Persistent-Type Pigeonhole, no new machinery.
Base-type invariance: A''∩Q = (A''∩S₀)∩Q = A'∩Q since Q⊆S₀. **No gap expected here —
this is the round's one "should just work," assign a builder to write it up
rigorously and get it certified.**

**New Theorem (Collateral-Safety Theorem).** Combine the (to-be-certified)
Projection Lemma with the certified Monotonicity of Resolution Lemma
(`lemmas/monotonicity-of-resolution.md`): if base-type pair (A,B) is **fully safe**
at S₀ (every S₀-extended-persistent refinement pair A',B' with A'∩Q=A, B'∩Q=B
satisfies A'∩B'≠∅), then (A,B) is fully safe at every S₁ ⊇ S₀.
*Proof:* Let A'',B'' be any S₁-extended-persistent refinements of A,B. By the
Projection Lemma, A':=A''∩S₀, B':=B''∩S₀ are S₀-extended-persistent refinements of
A,B, so (fully-safe hypothesis) A'∩B'≠∅. By Monotonicity of Resolution (applied
literally as stated, with A''∩S₀=A', B''∩S₀=B'), A''∩B''≠∅. **No new hypothesis, no
Singleton Hypothesis needed — this closes half of round 5's "collateral rogue pairs"
gap unconditionally.**

**What this does NOT close (must be stated honestly, not smoothed over).** It says
nothing about base-type pairs that are **not** fully safe at S₀ (rogue pairs) —
whether recruiting a prime against one witnessed instance of a rogue pair makes the
*whole* base-type pair fully safe at S₁, or only the one witnessed instance, is
exactly the content of "full absorption," which depends on the (not yet proved)
Approach-2 hypothesis. Also does not address whether genuinely *new* base-type pairs
can appear — this sub-point is actually free (note the fresh explorer's own
observation, confirmed here): base types live at the Q-level, and Q = P(a_1) never
changes, so the set 𝒫 of persistent base types and the finite list of disjoint
base-type pairs is fixed once and for all from round 0 — refinement only changes
which EXTENDED refinements exist, never which base-type pairs are in play. State
this explicitly as a one-paragraph corollary (it is immediate from 𝒫's Q-level
definition, Step 1) so it need not be re-derived by future rounds.

**Reformulated crux, precisely.** Define open(k) := the set of base-type pairs not
yet fully safe at stage S₀^(k). By the Collateral-Safety Theorem, open(k) is
non-increasing (⊇ open(k+1)) — a base-type pair, once fully safe, never becomes
rogue again. |open(0)| ≤ C(|𝒫|,2), a fixed finite bound depending only on Q. **The
process terminates (in ≤ C(|𝒫|,2) further rounds) IF AND ONLY IF every round that
recruits against an open base-type pair strictly shrinks open(k) by at least one
pair** — i.e. iff resolving the one witnessed rogue instance in a round in fact
makes that WHOLE base-type pair fully safe (not just the one witnessed extended
refinement). **This "full absorption" property is exactly Approach 2's target below
— import it as a black box, do not reprove it here.** Given Approach 2's Full-
Absorption Hypothesis (for the specific Lemma-G prime), the process provably
terminates in ≤ C(|𝒫|,2) rounds, and Step 5's CRT+cyclic-pigeonhole finish applies
verbatim at the terminal S₀^(k*). Without it, the base-type-pair count is merely
non-increasing, which is not yet sufficient (a rogue base-type pair could in
principle spawn infinitely many new never-fully-resolved extended refinements one at
a time, each requiring its own round, without the base-type pair ever registering as
"fully safe").

**Gaps this approach leaves open, explicitly:**
(G1) Certify the Projection Lemma (expected easy, assign to this round's builder).
(G2) The Collateral-Safety Theorem itself (expected easy given G1 + certified
Monotonicity — mostly a write-up task).
(G3) Full absorption for rogue base-type pairs — **imported, not to be reproved
here**; owned by Approach 2.
(G4) Given G1–G3, write the final termination + CRT finish cleanly as one theorem
(mechanical once G3 lands).

---

### Approach 2 (revise): `greedy-exchange-cost-potential` — retire the Universal
Singleton Hypothesis, attack the Full-Absorption Hypothesis instead

**Retire explicitly, do not re-attempt as stated:** the Universal Singleton
Hypothesis (|F'| = 1). Falsified (finding 1). The Round Resolution Lemma's proof, as
literally written, used |F'|=1 to collapse the Generalized Bounded Witness Lemma's
disjunction to a single term (part (i) of its proof) — this specific proof no longer
applies in general and must not be cited as unconditionally usable; keep it in-file
labeled "conditional on the now-false Universal Singleton Hypothesis, superseded by
the Full-Absorption Hypothesis below" for the audit trail.

**New target — the Full-Absorption Hypothesis (FAH), precisely stated.** Fix a rogue
pair (A',B') of S₀-extended-persistent types (disjoint base types, A'∩B'=∅), with
n_A := min{n:ρ(n)=A'} < n_B := min{n:ρ(n)=B'} (WLOG, per Lemma G). By the certified
**Lemma G** (`lemmas/extended-earliest-witness-intersection.md`), some prime
q ∉ S₀ divides both a_{n_A} and a_{n_B}; fix such a q (if more than one such prime
exists, any one choice — the Hypothesis is stated per-choice, see Gap below).

**FAH:** q | a_n for **every** n > n_B with ρ(n) = A' (not merely infinitely many —
the Recruitment Corollary already gives infinitely many for free via pigeonhole;
the added content is "eventually all," i.e. no other S₀^(1)-refinement of A'
survives as persistent past n_B besides A'∪{q}).

**Why this is the right replacement target, not a repeat of the falsified claim.**
FAH does **not** assert |F'| = 1 — it is compatible with |F'| ≥ 2 (as in both
round-6 counterexamples), it only asserts that *one specific* prime (the Lemma-G
prime) is load-bearing for *every* later A'-occurrence, while other elements of F'
may be "incidental" (Lemma H branch-(a) only, as spot-checked for prime 13 in the
a_1=4807 example — 100% vs 7% recurrence is exactly the FAH-consistent pattern).
**FAH is not yet falsified by anything found this round; it is the same conclusion
the (retired) Round Resolution Lemma needed, restated without smuggling in the false
premise.**

**Proof strategy to attempt (sketched by the singleton-lens explorer, not yet
carried out — this is the round's real work item).**
1. Fix n > n_B with ρ(n) = A'. By Free Facts, gcd(a_n, a_{n_B}) > 1; let p be any
   shared prime. If p ∈ S₀, contradiction exactly as in Lemma G's own proof (p would
   lie in A' ∩ B' = ∅). So p ∈ F' := P(a_{n_B}) \ S₀.
2. **The gap:** show p = q necessarily (not merely p ∈ F'). This is where the
   argument must do genuinely new work: apply **Lemma H (Critical Prime Dichotomy)**
   to p at the term a_n — either (a) stripping p from a_n drops it ≤ a_{n-1}
   (p is "incidental" to THIS occurrence), or (b) some earlier a_i shares *exactly*
   {p} with a_n. The builder should attempt to show that every prime of F' other
   than q is **always forced into branch (a) at every A'-occurrence**, i.e. never
   load-bearing, by an argument along these lines: q is characterized as the prime
   that is *also* forced (by an analogous Lemma-H argument, or by Lemma G applied at
   n and n_B directly) to persist — attempt a **joint/simultaneous pigeonhole**
   across ALL infinitely many A'-occurrences at once (the exact new ingredient
   flagged as missing by round 5's greedy-exchange file and round 6's singleton
   explorer): since each of the infinitely many n>n_B with ρ(n)=A' contributes a
   nonempty subset of F' (the primes of F' actually dividing a_n) via Free Facts +
   Lemma G's mechanism, and F' is finite, some SPECIFIC nonempty subset T ⊆ F'
   recurs for infinitely many n (ordinary pigeonhole on 2^{F'}, finite); the builder
   should investigate whether T = {q} can be forced (rather than merely "T is some
   fixed subset"), e.g. by combining with the same argument applied from the B'-side
   (symmetric roles) or with the Same-Side Ordering Lemma (certified,
   `lemmas/same-side-ordering-lemma.md`) to pin down which occurrences are eligible.
3. If step 2 cannot be closed for a *specific* q, a fallback weaker target
   (**still sufficient for Approach 1's finish**) is: prove FAH for **some** prime
   of F' (existence of at least one universally-recurring prime), not necessarily
   the specific Lemma-G one — this is a strictly weaker existential claim that may
   be more tractable and is enough for the Collateral-Safety Theorem's "full
   absorption" input (Approach 1, G3) as long as that one prime is used consistently
   in the S₁ construction.

**Honest disclosure of risk.** FAH itself might also be false in general (only
spot-checked on one side of one instance: 100% for q=17 in the a_1=4807 example;
the symmetric B'-side check and the a_1=11305 example were NOT completed by the
explorer). **The builder's first task, before attempting a proof, should be to
complete this verification** (both sides, both counterexample seeds, plus a handful
of the round-5 seeds 187/209/247/385) — if FAH is falsified too, report that
immediately and do not force a proof attempt; report the falsifying data with the
same rigor as this round's Singleton Hypothesis falsification (fresh
reimplementation, exact witness indices and factorizations shown).

**Gaps this approach leaves open, explicitly:**
(G1) Complete the empirical verification of FAH (both sides, ≥6 seeds) before
attempting a proof.
(G2) Prove FAH in general (Step 2 above) — the actual open mathematical content, not
yet closed by any certified lemma.
(G3) If G2 stalls, attempt the weaker "some universally-recurring prime exists"
fallback (Step 3).

---

### Approach 3 (new): `recruitment-round-charging` — bound (or merely prove finite)
the number of recruitment rounds via an explicit charging/potential argument,
independent of Full Absorption

**Motivation (fresh-framing explorer, finding 4).** Approaches 1+2 together, if
successful, already give termination in ≤ C(|𝒫|,2) rounds (a byproduct of Full
Absorption, not a separate argument). This approach is a **hedge**, explored in
parallel, in case Full Absorption (Approach 2) turns out to be false or unreachable:
can the number of recruitment rounds be bounded (or merely shown finite) by some
OTHER explicit function of a_1, via a genuinely different mechanism — a charging or
potential argument that does not go through "each round fully resolves one
base-type pair"? This is a **different target** (finiteness/explicit-bound of the
process, attacked by resource-charging) from both Approach 1 (structural,
pair-level, via Collateral-Safety) and Approach 2 (per-prime persistence, via
Critical-Prime-Dichotomy) — genuinely different framing, not a repackaging.

**Distinguish two strengths of target, as CLAUDE.md's dispatch asks (do not
conflate them):**
- **(T-weak) Mere termination:** the recruitment process (as exactly defined in
  `covering-system-construction` Step 4c) halts after *some* finite number of
  rounds, with no explicit bound required. Sufficient for the CRT+pigeonhole finish
  (Step 5) exactly as-is — Step 5 only needs a fixed finite terminal S₀, not a bound
  on how many rounds it took to reach it.
- **(T-strong) Explicit bound:** the number of rounds is ≤ f(a_1) for some explicit,
  computable f. Strictly stronger than T-weak; not needed for the problem's finish,
  but would be a cleaner, fully constructive result and may be easier to attack via
  a charging argument than an abstract "must halt" argument (charging arguments
  naturally produce explicit bounds as a byproduct).
This approach targets **T-strong** directly (an explicit f(a_1)), since a
successful charging argument automatically gives T-weak as a corollary; if T-strong
stalls, the builder should report whether the partial argument at least yields
T-weak alone (a real, valuable, weaker fallback per the dispatch's explicit request
to keep these two strengths distinguished).

**What a builder should attempt (no working mechanism identified yet — this is a
genuinely open sub-problem, state honestly, do not force a fake resolution):**
- Candidate charging object 1: total number of distinct primes recruited across all
  rounds, charged against ω(a_1) or Ω(a_1) (number of prime factors of a_1). **Known
  obstruction (fresh explorer):** recruited primes need not divide a_1 at all (the
  a_1=175 chain recruits 13, not a factor of 175=5²·7) — no certified mechanism ties
  a recruited prime back to a_1's own factorization. A builder attempting this
  route must either find such a tie (not yet known to exist) or abandon this
  specific charging object and report why.
- Candidate charging object 2: |𝒫| (number of persistent base types, ≤ 2^{|Q|}-1) or
  C(|𝒫|,2) (number of base-type pairs) as an a-priori cap on rounds, PROVEDdirectly
  (independent of Full Absorption) by showing each round strictly reduces some
  quantity tied to 𝒫's structure without needing "full absorption" — e.g. attempt to
  show that a round's recruited prime, even without full absorption, strictly
  reduces the number of *simultaneously rogue* extended-type pairs (not base-type
  pairs) by tracking the actual empirical "one prime resolves ALL currently-rogue
  pairs at once" phenomenon reported in `current.md` ROUND 4 (a_1=175: one recruited
  prime 13 resolved 6 rogue pairs simultaneously) as a target to prove directly,
  rather than via Full Absorption. This is a **distinct, not-yet-attempted
  mechanism** (a "batch resolution" theorem) — if provable, it would give T-strong
  with f(a_1) = C(|𝒫|,2) ≤ 2^{2|Q|} directly, via a totally different route from
  Approach 2.
- Candidate charging object 3 (long shot, flagged by fresh explorer as unexplored):
  a growth-rate/counting argument bounding total (index,new-prime) recruitment
  events up to N by the Bounded Gap Lemma's a_n = O(n); the fresh explorer found no
  way to convert this into a bound on *distinct* recruited primes (a bounded-size
  factorization per term is compatible with unboundedly many distinct primes across
  different terms) — report this route as very likely a dead end unless a genuinely
  new idea surfaces; do not spend more than minimal effort re-confirming this unless
  a new angle appears.

**Gaps this approach leaves open, explicitly (all of it is open — this is an early-
stage approach, Status should be `unsolved` unless the builder makes real progress):**
(G1) No charging mechanism is yet known to work (candidate 1 has a known
obstruction; candidate 2 is the most promising, targeting a "batch resolution"
theorem as a direct alternative to Full Absorption; candidate 3 is likely dead).
(G2) Even T-weak (mere finiteness) has no proof strategy yet beyond "if Approach 2
succeeds" — the value of this approach is exploring whether T-weak is reachable by
a genuinely independent route, as a hedge.

---

## Summary table

| slug | target this round | status expected after build | genuinely new vs. retired |
|---|---|---|---|
| `covering-system-construction` | Collateral-Safety Theorem (G1,G2 easy); relocate crux to base-pair-level termination importing Approach 2's FAH | partial, real narrowing | retires appeal to Universal Singleton Hyp.; Collateral-Safety is new, easy, unconditional |
| `greedy-exchange-cost-potential` | Full-Absorption Hypothesis (replaces Universal Singleton Hyp.) | partial (verification + partial proof attempt) or honest new falsification | retires Universal Singleton Hyp. and its Round Resolution Lemma; FAH is a new, sharper, not-yet-falsified target |
| `recruitment-round-charging` (new) | bound/prove-finite the number of recruitment rounds via charging, independent of Full Absorption | likely `unsolved`, honest exploration | genuinely new framing (charging/potential vs. structural pair-safety vs. per-prime persistence); explicitly hedges against Approach 2 failing |

`witness-index-descent`, `reversible-transition-map`: not revived this round (no new
idea; correctly RETHINK'd last round). `amortized-charging-budget`,
`density-sieve-contradiction`, `hypergraph-transversal`, `witness-depth-bound`:
remain stale/retired, not nominated.

build set: covering-system-construction, greedy-exchange-cost-potential, recruitment-round-charging
