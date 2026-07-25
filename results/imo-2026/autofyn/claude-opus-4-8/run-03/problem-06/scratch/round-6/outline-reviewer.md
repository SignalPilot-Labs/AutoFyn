# Outline Review — imo-2026-06, Round 6

Field handed over: (1) `redundant-constraint-antichain` (LEADER, advance/consolidate only),
(2) `joint-recruitment-budget` (NEW far-framing pole — the last unexhausted joint-accounting thread,
opening 5 from the joint-potential explorer). The critical call this round is vetting the new pole.

---

## 1. redundant-constraint-antichain — VERDICT: CHANGES REQUESTED (consolidate only)

The certified spine. Every arrow except E5″ is proved and reviewer-certified; §13.1 re-verified the
whole reduction chain last round (no-transient ⇒ E1/E2/E3 ⇒ Crux ⟺ E4 ⟺ E5″; ∏G<a₁ subclass closed
by Prop 12.A). Elo 1690, live leader.

- No new E5″ lever appeared this round (correctly; the outliner did not fabricate one — good, per the
  plateau rule that a fake breaker is worse than none). So this slug is **advance-for-consolidation
  only**: keep §13 tidy and cross-link the new pole's cheap-kill outcome (below) as a certified
  negative guardrail, exactly as JSC/Collapse were recorded.
- Do NOT re-derive any ∏G / p_max / |t−t′| / density / sub-support lever (all proven-forked).
- No new cases; no circularity; the skeleton is sound. Nothing to change beyond housekeeping.

Earns its build slot automatically (consolidation leader).

---

## 2. joint-recruitment-budget — VERDICT: RETHINK as a positive route to E5″; CHANGES-REQUESTED-REDIRECTED to certify the negative guardrail

I vetted this HARD against the four fork traps (Φ_N/density, ∏G, |t−t′| spread, sub-support). **It
provably forks.** I can state the fork as a clean theorem — the *Rejection-Budget Dichotomy* — which
is itself the valuable deliverable. Details:

### The setup is sound but the budget is Φ_N (confirmed)
Steps 1–2 are correct and rest on certified facts. I verified numerically (a₁∈{375,385,867,105}, N=400)
that the rejection stream up to N is **exactly** Φ_N = a_N − a₁ − (N−1) = Σ(gap−1), each gap ≤ M=rad(a₁),
so Φ_N ≤ (M−1)(N−1) = **O(N)**. This is precisely the density quantity the certified obstruction family
{p*,q_k} freezes (density→1/p*>0 with infinitely many recruits). The outliner's preliminary cheap-kill
(raw budget = Φ_N) is confirmed. So the pole stands or falls on step 3's disjoint-attribution refinement.

### The Rejection-Budget Dichotomy (why step 3 cannot escape)
The rejection stream up to N is a set of exactly Φ_N = O(N) events. Step 3 wants **disjoint** cost sets
C_{q_k} drawn from this stream, one per recruit, with |C_{q_k}| ≥ c_{q_k} → ∞ (step 4), then a
contradiction (step 5) from "infinitely many recruits vs O(N) budget." But because the C_{q_k} are
disjoint subsets of a size-(M−1)N set, they **automatically** satisfy

  Σ_k |C_{q_k}| ≤ Φ_N = O(N).   (★)

(★) is a tautology, not a contradiction — you cannot have disjoint subsets of an S-element set with
total size > S. So step 5's contradiction is *impossible to reach* unless the lower bound c_{q_k}→∞
is forced by something other than "these are actual disjoint rejections." Two horns, both dead:

- **Horn A (local cost).** If C_{q_k} is drawn from a bounded-length window around the recruit's
  realizer ∏G_{q_k} (e.g. "the length-≤M window topping out at ∏G_{q_k}", as the outline literally
  proposes), then |C_{q_k}| ≤ M−1 — **bounded, cannot →∞**. Step 4 fails outright.

- **Horn B (global cost).** To get |C_{q_k}|→∞ the cost must span Ω(q_k) of the number line (reach
  across [t′_k, t_k], length ≥ q_k by TAS). Then two sub-cases: (i) disjointness makes (★) a tautology —
  large per-recruit cost just means recruits are sparse (fewer per unit length), fully **consistent**
  with Π infinite, no contradiction; (ii) to force a contradiction you must claim recruit q "needs" a
  window of length ≥ f(q) yet the window is capped at a₁-only length — i.e. bound t_k − t′_k by f(a₁).
  That is **exactly the JSC spread bound** (t_k−t′_k = q_k(A_k−B_k), A_k≠B_k ⇒ spread bound = magnitude
  bound), certified dead in R5.

- **Third variant (shared vocabulary).** The explorer's "recruitment consumes a globally finite
  vocabulary" phrasing: each recruit q pairs with a small-prime part B with ∏B<a₁ (E5″), B ranges over a
  finite set K(a₁); Π infinite ⇒ pigeonhole gives an infinite family with common core B ⇒ this is the
  anchor-partition common core, and forcing a B-term is the **R4 Collapse theorem** (dead).

Every route to c_q→∞ with disjoint costs from the O(N) rejection budget forks into Φ_N/density (Horn A
degenerate), JSC-spread (Horn B), or Collapse (vocabulary). **No escape.** I looked for a support-attributed
(rather than position-attributed) count; it changes nothing, because (★) holds for *any* disjoint
attribution regardless of how events are assigned — the counting obstruction is structural.

### Disposition
This is the honest, run-advancing outcome the dispatch explicitly authorized: certify the fork as a
**permanent negative guardrail**, closing opening 5 — the last unexhausted joint-accounting thread — the
way JSC/Collapse closed the spread and sub-support levers. I registered the pole (Elo 1530) and admit it
to the build set with a **redirected deliverable**: the builder does NOT attempt to close E5″; it writes
up the Rejection-Budget Dichotomy as a certified guardrail lemma (`lemmas/`), with the §2 numerics as the
concrete anchor, and cross-links it into the leader's §13. Do NOT let it drift into an actual Φ_N/spread
bound — the deliverable is the negative theorem itself.

---

## 3. Diversity / plateau note for the orchestrator

Field is now at a **6-round structural plateau** and the joint-potential lens is, after this round,
**fully mapped**: all five openings are certified forked (1/2/4 = density/JSC/Φ_N, 3 = anchor-partition,
5 = Rejection-Budget Dichotomy). Combined with R6's other two explorers (direct-periodicity and
alt-reduction both proven to re-derive the Reduction-Lemma equivalence, and the converse gap proven
non-existent), **all three top-level route families the R6 mandate named (i/ii/iii) are now exhausted.**
The negative guardrails are piling into a near-complete impossibility map around E5″. For R7 the honest
options are: (a) accept that E5″ must be attacked with genuinely new *arithmetic* input not yet on the
table (the explorers' one surviving intuition: an argument using E1-realizability + growth L2 to force an
arithmetic collision the non-realizable star family evades — but concretely, not as any bounded quantity),
or (b) a corpus/literature search for the specific finite-alphabet statement as a known result. The field
has collapsed to one live framing (the antichain spine); every rival is a certified dead-end guardrail.
This should be surfaced to the orchestrator as a hard plateau, not routed around with another disguised
single-quantity lever.

---

## Ranking (folded)
redundant-constraint-antichain 1690.6 (live leader) > realizer-index-joint-double-count 1551.3 (dead,
strong TAS salvage) > joint-recruitment-budget 1530.0 (new, forks; guardrail deliverable) >
residual-anchor-peeling 1511.4 (dead) > value-stream-double-freeze 1449.3 (dead) >
monovariant-witness-descent 1428.2 (retired) > anomaly-count-terminates 1339.2 (dead).

build set: redundant-constraint-antichain, joint-recruitment-budget
