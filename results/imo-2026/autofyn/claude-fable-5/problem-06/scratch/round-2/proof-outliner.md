# Round 2 — proof-outliner — imo-2026-06

Shared certified-ready scaffolding (all approaches import these; builder should file as lemmas):
- **Clique**: gcd(a_i,a_j)>1 for all i≠j.
- **Bounded gaps**: every multiple of B := rad(a_1) is always valid, so a_{n+1}−a_n ≤ B; A is B-syndetic.
- **Reduction/Squeeze (the global-periodicity bridge)**: with V_∞ = {m>1 : gcd(m,a_i)>1 ∀i}, every term is in V_∞ and a_{n+1} = min(V_∞ ∩ (a_n,∞)) for ALL n ≥ 1 (squeeze: V_∞ ⊆ V_n gives ≤, membership gives ≥). So **A = V_∞ ∩ [a_1,∞)**: the sequence is exactly the increasing enumeration of V_∞ from a_1, no transient. Once V_∞ ∩ [a_1,∞) is shown exactly L-periodic with T residues per window, a_{n+T} = a_n + L for all n ≥ 1 falls out. **The whole problem reduces to: V_∞ ∩ [a_1,∞) is exactly periodic.**

---

greedy-clique-closure: advance
Target: full claim (∃T,L: a_{n+T}=a_n+L ∀n≥1).
Technique: minimal-antichain E_∞ finiteness via density/first-moment + greedy minimality; then constraints collapse mod L = ∏(primes in ∪E_∞); then squeeze.
Skeleton: as in `results/imo-2026-06/approaches/greedy-clique-closure.md` (Steps 1,2,3,5,6 complete-modulo-writing). Remaining crux = Step 4: E_∞ = {inclusion-minimal P(a_i)} is finite.
Key lemmas: every F ∈ E_∞ satisfies Σ_{p∈F} 1/p ≥ 1/B — because A ⊆ ∪_{p∈F} pℤ and A is B-syndetic. Joint transversal bound for subfamilies forces concentration on a small kernel.
Open gaps: Step 4 only (plus writing out Step 6 rigorously).
New ammunition this round: (a) **Domination lemma** (from stabilization explorer): if P(a_i) ⊆ P(a_j), i<j, then a_j adds no new minimal constraint — so E-changes come only from terms whose prime set contains NO earlier prime set. (b) **Self-reference from Reduction**: A = V_∞ ∩ [a_1,∞), so the constraint family is the prime sets of ALL valid numbers ≥ a_1; in particular V_∞ contains every multiple of rad(v) for every v ∈ V_∞ ∩ [a_1,∞). Use this to show implied constraints collapse (e.g. if all constraints contain 2, all evens ≥ a_1 are terms, so a power of 2 is a term and {2} dominates everything).
Watch out for: it may suffice (and be easier) to prove "finitely many F ∈ E_∞ already cut V_∞ ∩ [a_1,∞) exactly" rather than literal finiteness of E_∞ — but the collapse must hold from a_1 on, not just eventually; eventual-only periodicity does NOT imply the global statement.
Confidence: MEDIUM-HIGH.

wqo-domination: new
Target: full claim.
Technique: stabilization of E_n via the domination lemma + a bad-sequence/descent argument, then periodic V* and the squeeze.
Skeleton:
  1. Clique, bounded gaps, Reduction/Squeeze — shared lemmas.
  2. Domination lemma: P(a_i) ⊆ P(a_j) (i<j) ⇒ a_j is dominated (E unchanged at step j) — because E_{j−1} already has some F ⊆ P(a_i).
  3. Non-dominated terms have prime sets forming a bad sequence (no i<j with P(a_{n_i}) ⊆ P(a_{n_j})).
  4. **[GAP — the crux]** Only finitely many non-dominated terms.
  5. Hence E_n = E* for n ≥ N; V* is L-periodic (L = ∏ primes in ∪E*, since p|m ⇔ p|(m+L)); every a_n ∈ V* (every F ∈ E* is some P(a_k); clique); squeeze ⇒ a_n = min(V* ∩ (a_{n−1},∞)) for all n ≥ 1; greedy on an L-periodic set with T residues gives a_{n+T} = a_n + L globally.
Key lemmas: step 5 is solid (periodicity explorer verified each sub-step). Step 4 is NOT closed by Dickson/Higman as claimed: **(P_fin(primes), ⊆) is NOT a WQO** — {p_n, p_{n+1}}_{n≥1} is an infinite antichain — so "bad sequence ⇒ finite" is false without extra input. Repair route: each non-dominated P(a_n) meets the fixed finite set P(a_1) (clique) — pigeonhole an infinite subfamily sharing p ∈ P(a_1); deleting a shared prime preserves badness; iterate descent, and use greedy self-reference (approach 1, ammunition (b)) to show an infinite descending chain of shared-prime kernels forces a dominating term to actually appear in the sequence, contradiction.
Open gaps: step 4 (repaired WQO/descent).
Cases to cover: none beyond the descent dichotomy.
Watch out for: do not cite "finite subsets of ℕ are WQO" — it is false; the greedy dynamics must enter the finiteness proof, pure order theory cannot.
Confidence: MEDIUM (endgame solid; finiteness needs the repair).

small-prime-core: advance
Target: full claim.
Technique: pin a finite prime universe Q first — show every clique edge is carried by a prime in Q — then constraints collapse mod M = ∏Q with no stabilization-in-time analysis.
Skeleton: as in `results/imo-2026-06/approaches/small-prime-core.md`; Steps 1,2,4,5 complete-modulo-writing; crux = Step 3 (Small Common Prime Lemma: ∃ finite Q such that any two terms share a prime of Q; "all but finitely many pairs" suffices).
Key lemmas: terms divisible by a fixed large prime q have density ≤ 1/q < 1/B ≤ density of A — so most terms miss q and must hit each earlier term through small primes; upgrade "most" to "all large" via the rad-multiple cones from the Reduction self-reference.
Open gaps: Step 3.
Watch out for: large primes DO keep appearing in terms forever; the claim is only that no *edge* rides exclusively on large primes.
Confidence: MEDIUM (genuinely different framing from the antichain routes; keeps the field diverse if both antichain approaches hit the same wall).

---

Field note: all three share the certified-ready endgame (Reduction/Squeeze ⇒ global, not just eventual, periodicity — the "for all n ≥ 1" worry is fully handled). They differ on the single real crux — why the effective constraint family is finite — attacked by density (slug 1), order-theoretic descent + greedy self-reference (slug 2), and finite prime universe for edges (slug 3). Builder for slug 1 or 2 should first certify Clique, Bounded-gaps, Reduction as `lemmas/` entries — all three approaches import them.

build set: greedy-clique-closure, wqo-domination
