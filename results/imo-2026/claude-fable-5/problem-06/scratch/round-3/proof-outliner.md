# Proof-outliner — Round 3

## imo-2026-06

### Field summary

- `small-prime-core` — **REVISE, primary build target.** Threshold corrected (see below: it is z = a_1, not rad(a_1), not p_max, not P(a_1)); the SCPL crux now has a complete, hand-checked descent proof plan (streamlined from the alternative-routes explorer: single companion, no case split). Every step has a named mechanism. HIGH confidence.
- `wqo-domination` — **NEW, secondary build target.** Same SCPL crux proved independently, then a *different endgame*: minimal antichain E_∞ + Dickson's lemma on the finite universe 2^Q. Serves as an independent re-derivation of the crux (two builders writing the descent independently is deliberate error-catching redundancy) and gives a second complete write-up path if small-prime-core's endgame hits friction. MEDIUM-HIGH confidence.
- `greedy-clique-closure` — **HOLD (live, not built this round).** Its density/first-moment route to "E_∞ finite" is the only genuinely different framing in the field. Do NOT convert it to the SCPL route (that would collapse the field to one framing and one shared gap). If the SCPL descent survives review this round it becomes superseded; if the descent breaks, this is the fallback. Keep live, no builder.

**Shared-gap warning for the reviewer:** the two built approaches share the SCPL crux by design (the dispatch's call, and I agree the descent is strong enough to double down on). `greedy-clique-closure` is retained precisely as the out-of-framing insurance against that shared gap.

### Corrections this round (record; builders must respect these)

1. **Threshold correction (new, found by stress-testing the explorer's Claim 4).** The companion construction fails at threshold B = rad(a_1) for non-squarefree a_1. Counterexample: a_1 = 48, B = 6. Sequence: 48, 50, 52, 54, 56, … The term 56 = 2³·7 has large prime 7 > B and σ(56) = {2}, but NO integer with prime set exactly {2} lies in [48, 56) (32 < 48 ≤ 64). The explorer verified only squarefree a_1 ∈ {15, 35, 77, 30}, where B = a_1, masking this. Same failure mode kills threshold p_max. **The provable threshold is z = a_1** ("small prime" = prime ≤ a_1): then a term a with small prime p and large prime q > a_1 satisfies pq | a, so a ≥ pq > p·a_1, which is exactly the room the companion needs. Any finite threshold suffices downstream (only |Q| < ∞ matters), so the sharp computational threshold p_max is NOT needed and must not be claimed.
2. **Streamlined descent (no case split).** The explorer's two-case argument (x_j < a_i vs x_j ≥ a_i, constructing both x_j and x_i) reduces to a single companion x_i; see Step 4 skeleton below. Fewer moving parts, same contradiction.
3. Recorded dead ends re-confirmed: Q = P(a_1) is FALSE (a_1 = 15: terms 18, 20 share only 2 ∉ {3,5}); pure Dickson/WQO on P_fin(primes) is FALSE (infinite antichains exist); "primes of terms stabilize" is FALSE (bonus large primes appear forever).

---

### small-prime-core: revise
Target: There exist positive integers T, L with a_{n+T} = a_n + L for every n ≥ 1 (the full claim).
Technique: Fix the finite prime universe Q = {primes ≤ a_1} in advance; prove the Small Common Prime Lemma (SCPL) by minimal-counterexample descent (aimo-0030 Claim-4 adaptation: strip large primes, restore size with a small prime power, force the companion to be an earlier term); collapse all constraints mod M = ∏_{p∈Q} p; conclude by greedy enumeration of an exactly periodic set.

Notation (fix once): B = rad(a_1); "small" prime = prime ≤ a_1; σ(m) = primes(m) ∩ [2, a_1]; V_n = {m > a_n : gcd(m, a_i) > 1 for i = 1..n}; V_∞ = {m > 1 : gcd(m, a_i) > 1 for all i ≥ 1}; A = {a_1, a_2, …}.

Skeleton:
  1. **Clique** — gcd(a_m, a_n) > 1 for all m ≠ n — by definition of the rule (for m > n it is a defining constraint of a_m). SOLID.
  2. **Bounded gaps + well-formedness** — every multiple of rad(a_1) that is > a_n lies in V_n (it shares with each a_i the prime a_i shares with a_1), so a_{n+1} ≤ a_n + B. (Scaffolding; the final chain does not lean on the density corollary anymore.) SOLID.
  3. **Reduction Lemma** — a_{n+1} = min(V_∞ ∩ (a_n, ∞)) for all n ≥ 1, hence A = V_∞ ∩ [a_1, ∞) enumerated increasingly — because V_∞ ⊆ V_n gives min V_∞ ∩ (a_n,∞) ≥ a_{n+1}, while a_{n+1} ∈ V_∞ (its gcd conditions vs later terms are those terms' defining constraints) gives ≤. Certify as `lemmas/reduction.md`. SOLID.
  3'. **Structural fact (valid-below-are-terms)** — V_{n} ∩ [a_1, a_n] = {a_1, …, a_n} for every n — because a non-term m ∈ (a_t, a_{t+1}) ∩ [a_1, a_n] valid vs a_1..a_n is a fortiori valid vs a_1..a_t, contradicting minimality of a_{t+1}. Certify as `lemmas/valid-below-are-terms.md`. SOLID.
  3''. **Companion Lemma** — if a term a has a prime factor q > a_1, then there exists x with primes(x) = σ(a) and a_1 ≤ x < a — because σ(a) ≠ ∅ (a shares a prime with a_1, and all primes of a_1 are ≤ a_1); pick p ∈ σ(a), set m_0 = ∏_{r∈σ(a)} r, x = m_0·p^t with t ≥ 0 minimal s.t. x ≥ a_1; if t = 0 then x = m_0 divides a and m_0 ≤ a/q < a; if t ≥ 1 then minimality gives x < p·a_1 < p·q ≤ a (p, q distinct primes dividing a). SOLID (this is exactly where z = a_1 is forced; see Correction 1).
  4. **SCPL [GAP — the crux; full plan below]** — any two terms share a prime ≤ a_1.
     Proof plan (strong induction on the larger index j; descent on the smaller index i):
     a. Base: (a_1, a_j) always share a prime of a_1, all ≤ a_1. So any counterexample pair (i, j) has i ≥ 2.
     b. Induction hypothesis: every pair with larger index < j shares a small prime. Suppose some i < j has gcd(a_i, a_j) supported only on primes > a_1; take i MINIMAL. Fix a shared large prime q > a_1; note q | a_i and q | a_j.
     c. Disjointness bookkeeping: σ(a_j) ∩ primes(a_i) = ∅ and σ(a_i) ∩ primes(a_j) = ∅ — because a shared small prime would contradict the choice of (i, j).
     d. Build the SINGLE companion x_i of a_i (Companion Lemma, since q | a_i, q > a_1): primes(x_i) = σ(a_i), a_1 ≤ x_i < a_i.
     e. x_i ∈ V_{i-1} — because for each i' < i the pair (a_{i'}, a_i) shares a small prime r (induction hypothesis on larger index i < j), and r ∈ σ(a_i) = primes(x_i), r | a_{i'}.
     f. x_i is an earlier term: x_i ∈ V_{i-1} ∩ [a_1, a_i) ; the slice (a_{i-1}, a_i) is empty of V_{i-1}-elements by greedy minimality of a_i, and V_{i-1} ∩ [a_1, a_{i-1}] = {a_1,…,a_{i-1}} by Step 3'. So x_i = a_s, s ≤ i−1.
     g. Contradiction via minimality of i: the pair (s, j) with s < i shares a small prime r (i was minimal); r | a_s = x_i so r ∈ σ(a_i); r | a_j so r ∈ σ(a_i) ∩ primes(a_j) = ∅. Contradiction. QED.
  5. **Constraints collapse mod M** — with Q = {p ≤ a_1}, M = ∏_{p∈Q} p: A = {m ≥ a_1 : σ(m) ∩ σ(a) ≠ ∅ for every term a} — (⊆) is exactly SCPL; (⊇) σ(m) hitting σ(a_i) gives gcd(m, a_i) > 1 for all i, so m ∈ V_∞ ∩ [a_1, ∞) = A by Step 3. The condition quantifies over the family {σ(a) : a ∈ A} ⊆ 2^Q, which is finite with NO stabilization-in-time argument; and p | m for p ∈ Q depends only on m mod M. Hence A = {m ≥ a_1 : m mod M ∈ R}, R ⊆ Z/M, R ∋ a_1 mod M ≠ ∅. SOLID given Step 4.
  6. **Conclusion** — set L = M, T = |R|. Each half-open window [x, x + M) ⊆ [a_1, ∞) contains exactly T elements of A (one per residue class in R), and m ↦ m + M maps A order-isomorphically into A; since a_n ∈ A, the T-th successor of a_n in A is a_n + M, i.e. a_{n+T} = a_n + L for ALL n ≥ 1 (no transient — the enumeration starts at a_1 ∈ A). SOLID; write the counting argument out in full.
Key lemmas (claim + mechanism):
  - Reduction: A = V_∞ ∩ [a_1, ∞) — because V_∞ ⊆ V_n squeezes the greedy minimum from both sides.
  - Valid-below-are-terms: V_n ∩ [a_1, a_n] = {a_1..a_n} — because a valid non-term in a gap would beat the greedy choice that closed that gap.
  - Companion: term with prime > a_1 has a same-small-signature proxy in [a_1, a) — because stripping the large prime frees a factor > a_1 of room, and refilling with p-powers overshoots a_1 by a factor < p < q.
  - SCPL: all clique edges carry a prime ≤ a_1 — because the minimal bad pair forces the companion of a_i to be an earlier term whose small primes must simultaneously hit a_j (minimality of i) and miss a_j (disjointness). 
Open gaps: Step 4 (write the descent rigorously: exact induction statement, the two uses of minimality — IH on larger index for (e), minimal i for (g) — and the empty-slice justification in (f)). Steps 3', 3'', 5, 6 need full write-ups but mechanisms are complete.
Cases to cover: i = 1 impossibility (base of descent); t = 0 vs t ≥ 1 in the Companion Lemma; a_1 prime or prime power (SCPL is then trivial — every term shares a prime of a_1 — but the general proof covers it anyway; a remark suffices).
Confidence: HIGH
Watch out for:
  - Do NOT claim thresholds B = rad(a_1) or p_max: the Companion Lemma FAILS there (a_1 = 48, term 56 example). z = a_1 is the provable threshold; sharpness is irrelevant.
  - Do not conflate "no term has a large prime factor" (FALSE — large bonus primes appear forever) with the actual claim "no clique edge is carried only by large primes."
  - In (f), x_i ≠ a_i needs no argument (x_i < a_i strictly), but do state that x_i could not land in (a_{i-1}, a_i) and why.
  - In Step 5, R is defined via the realized σ-classes of the actual infinite A; finiteness of 2^Q is what makes this legal.
  - In Step 6, "exactly T per window" requires the window to sit inside [a_1, ∞); a_1 ∈ A anchors n = 1.

---

### wqo-domination: new
Target: There exist positive integers T, L with a_{n+T} = a_n + L for every n ≥ 1 (the full claim).
Technique: Same SCPL crux (proved INDEPENDENTLY by this builder — do not import the other builder's write-up; independent derivation is the point), then the antichain endgame: minimal constraint family E_∞ lives in 2^Q, Dickson's lemma (finite universe) gives |E_∞| < ∞, V_∞ is exactly L-periodic with L = ∏ of the finitely many primes in ∪E_∞, and greedy enumeration of a periodic set is arithmetic-periodic.
Skeleton:
  1. Clique, Reduction, Structural fact, Companion Lemma — as in small-prime-core Steps 1–3'' (import certified lemmas from `lemmas/` where available). SOLID.
  2. SCPL with Q = {primes ≤ a_1} — [GAP: same descent as small-prime-core Step 4; this builder writes it from scratch]. 
  3. **E_∞ ⊆ 2^Q and is finite** — let F = {primes(a_i) : i ≥ 1} and E_∞ its inclusion-minimal members; every member of F contains a minimal member (finite sets), so V_∞ = {m > 1 : primes(m) hits every F ∈ E_∞}. Claim: every F ∈ E_∞ has all primes ≤ a_1 — because if q > a_1, q ∈ F = primes(a_k), then by SCPL every term hits σ(a_k) = F ∩ [2, a_1], so ∏_{p ∈ σ(a_k)} p^N is in V_∞ for large N, hence (Reduction) a term with prime set σ(a_k) ⊊ F, contradicting minimality of F. Then E_∞ ⊆ 2^Q, finite outright (|2^Q| = 2^{π(a_1)}; Dickson/WQO is available but not even needed — a subset family of a finite set is finite). SOLID given Step 2.
  4. **Exact periodicity of V_∞** — P = ∪_{F∈E_∞} F ⊆ Q, L = ∏_{p∈P} p; membership "primes(m) hits every F" depends only on m mod L; so V_∞ ∩ (1, ∞) = {m > 1 : m mod L ∈ R}. SOLID.
  5. **Conclusion** — T = |R ∩ (residues realized in [a_1, ∞))|-per-window count as in small-prime-core Step 6: shift by L is an order-isomorphism, each window carries exactly T elements, a_{n+T} = a_n + L for all n ≥ 1. SOLID.
Key lemmas: same four as small-prime-core, plus: large-prime constraints are dominated — because SCPL makes the pure-small-power ∏_{p∈σ(a_k)} p^N a term, and its prime set strictly undercuts any F containing a large prime.
Open gaps: Step 2 (the descent, independently written); Step 3's "∏ p^N ≥ a_1 is a term" needs the one-line Reduction application spelled out.
Cases to cover: as in small-prime-core; additionally E_∞ could contain F = P(a_1) itself — fine, no special handling, but don't assume E_∞ elements are ≠ P(a_1).
Confidence: MEDIUM-HIGH (crux shared with small-prime-core; endgame independent and slightly longer).
Watch out for:
  - This approach DIES WITH small-prime-core if the descent is flawed — that is accepted this round; greedy-clique-closure is the hedge.
  - Do not cite "P_fin(primes) is WQO" (false, recorded dead end). Only 2^Q for FINITE Q is used.
  - "Primes of terms stabilize" is false; only E_∞ stabilizes. Keep the quantifiers straight in Step 3.

---

### greedy-clique-closure: advance (HOLD — keep live, do NOT build this round)
Target: full claim, via finiteness of E_∞ by density/first-moment bounds + greedy minimality (its existing Step 4 route).
Status rationale: the SCPL descent supersedes its crux IF the descent survives review; converting this slug to SCPL would collapse the field to one framing. It stays live, unbuilt, as the genuinely-different fallback (density route: Σ_{p∈F} 1/p ≥ 1/B for every F ∈ E_∞, joint transversal decay for subfamilies). If both SCPL builds fail this round, revise this next round with the explorer's B^N-is-a-term lemma (rad(a_1)^N is always a term — every term shares a prime of a_1) as new ammunition: it kills all F ⊋ P(a_1) and anchors the density argument.
Confidence: LOW-MEDIUM as currently written; retained for field diversity.

---

### Shared lemmas — certify once in `results/imo-2026-06/lemmas/`, import everywhere

1. `clique.md` — gcd(a_m, a_n) > 1 for all m ≠ n.
2. `reduction.md` — a_{n+1} = min(V_∞ ∩ (a_n, ∞)); A = V_∞ ∩ [a_1, ∞).
3. `valid-below-are-terms.md` — V_n ∩ [a_1, a_n] = {a_1, …, a_n}.
4. `companion.md` — term a with a prime > a_1 has x with primes(x) = σ(a), a_1 ≤ x < a (threshold z = a_1 is load-bearing; see Correction 1).
5. `scpl.md` — any two terms share a prime ≤ a_1 (once the descent is certified by the proof-reviewer, both live approaches import it).
6. `periodic-enumeration.md` — the increasing enumeration of {m ≥ a_1 : m mod M ∈ R} with a_1 in the set satisfies x_{n+|R|} = x_n + M for all n ≥ 1.

Builders: whoever proves a lemma first proposes it; the proof-reviewer certifies; the other imports rather than re-proving.

build set: small-prime-core, wqo-domination
