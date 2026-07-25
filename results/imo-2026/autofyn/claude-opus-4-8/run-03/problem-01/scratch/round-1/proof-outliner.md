## imo-2026-01

Field of 3 rival approaches. Diversity axis = the part-(b) mechanism (explicit invariant /
abstract confluence / induction). Numerically verified this round: formula M = ∏_p p^{g_p},
single-survivor, and full order-independence (400/400 formula+single-survivor, 300/300
order-independence over random move orders). KEY STRUCTURAL FINDING for the field: part (a)
is fully elementary and needs NO prime decomposition — non-collapse follows from
g·ℓ = lcm(m,n) > 1 (the two outputs can't both be 1), and "≤1 survivor" is just the move-
legality rule; only termination (a monovariant) is substantive. Primes are needed only to
value M in part (b). The dispatcher's "concentration onto one slot" is FORCED by the terminal
condition (only one slot >1), not a separate hard fact — I made sure no approach treats it as
an assumption or as a hard gap.

---

per-prime-gcd-invariant: new
Target: (a) exactly one survivor after finitely many moves; (b) M choice-independent, and
  M = ∏_p p^{g_p}, g_p = gcd of the initial p-adic valuations across all 2026 entries.
Technique: p-adic decoupling + exact conserved quantity (gcd of each prime's exponent
  multiset) + lex monovariant (Ω_total, K). KB: Invariants & monovariants; Divisor analysis.
Skeleton:
  1. Per prime, move acts as (a,b)↦(min, max-min) — by v_p(gcd)=min, v_p(lcm/gcd)=max-min.
  2. g_p = gcd of the whole p-exponent multiset is EXACT-invariant — Euclid identity
     gcd(min,max-min)=gcd(a,b) + multiset-gcd associativity (Lemma A).
  3. Termination — (Ω_total,K) lex strictly decreases every move, bounded below (Lemma B).
  4. ≤1 survivor — move legal iff ≥2 entries >1, so terminal ⟹ ≤1 (definitional).
  5. ≥1 survivor — g·ℓ = lcm > 1, outputs never both 1 (Lemma C, prime-free).
  6. (a) = 3+4+5.
  7. (b): terminal p-multiset = 2025 zeros + one e_p, gcd = e_p = g_p (invariant) ⇒
     M = ∏_p p^{g_p}, fixed by initial board.
Key lemmas: A (g_p invariant — Euclid + gcd(A∪B)=gcd(gcd A,gcd B)); B (Ω_total drops iff
  gcd>1, else K drops via the output 1); C (lcm>1 ⇒ ≥1 active).
Open gaps: full Lemma A with associativity + gcd(0,x)=x conventions; Lemma B Ω-count identity
  and m=n subcase; Step 7 gcd-of-(zeros+one) and same-slot (automatic).
Cases to cover: gcd=1 vs >1, m=n, primes with g_p=0 (contribute p^0=1).
Watch out for: M ≠ gcd(a_i) ({4,8}→2, not 4); concentration is forced not proved; 2026
  irrelevant (works ∀ n≥2). Most likely APPROVE — cleanest route.

---

confluence-normal-form: new
Target: (a) exactly one survivor; (b) M order-independent, proved WITHOUT any closed form —
  as uniqueness of the rewriting normal form. Furthest framing from the compute-M route.
Technique: prime-free monovariant (product P, active-count A) for (a); abstract rewriting +
  Newman's Lemma (terminating + locally confluent ⇒ unique normal form) for (b).
Skeleton:
  1. P = ∏ a_i non-increasing, halves when gcd>1 (g·ℓ=lcm=mn/gcd).
  2. A = #{>1}: drops by 1 on gcd=1 moves (outputs (1,mn)).
  3. Termination: ≤ log2(P0) non-coprime + ≤ 2026 coprime moves.
  4. Non-collapse (lcm>1) + legality ⇒ terminal A = 1. (a) done.
  5. Local confluence: disjoint moves commute; overlap (3 slots) reconverges (Gap 1).
  6. Newman: terminating + locally confluent ⇒ unique normal form.
  7. (b): unique terminal ⇒ M independent of choices.
Key lemmas: LC-disjoint (commuting, trivial); LC-overlap (Gap 1 — 3-entry sub-board has a
  unique terminal by its own (A,P) induction; self-contained, NOT via g_p).
Open gaps: Gap 1 local-confluence overlap case (the load-bearing hard step); Newman's Lemma
  statement + well-founded-induction proof off the Step-3 order.
Cases to cover: disjoint / share-one / identical move pairs; coprime vs non-coprime buckets.
Watch out for: don't smuggle g_p into Gap 1 (would collapse into approach 1); global
  confluence is the conclusion not a hypothesis; if Gap 1 is intractable to write, RETHINK to
  a direct swap/order-independence argument (valid proof exists — confirmed numerically).

---

strong-induction-descent: new
Target: both parts via one strong induction; (b) order-independence falls out of the IH.
Technique: well-founded descent on (Ω_total, K); strengthened induction statement carrying
  the value μ(B)=∏ p^{g_p}. Distinct in ARCHITECTURE (recursion) from the other two.
Skeleton:
  1. Φ=(Ω_total,K) lex strictly decreases per move.
  2. P(B): terminates at one survivor = μ(B), same for every play; base = no-move board.
  3. Step: any first move → B' with Φ(B')<Φ(B); IH ⇒ B' ends at μ(B'); μ(B')=μ(B) by
     per-prime gcd preservation; so every first move ends at μ(B) ⇒ order-independent.
  4. Specialize n=2026.
Key lemmas: monovariant (= Lemma B); μ preserved per move (= Lemma A engine); non-collapse
  (= Lemma C) for the base case.
Open gaps: Φ strict-decrease all cases; μ-preservation lemma (import from lemmas/ if
  certified); base case value = μ(B); induction over ALL n (B' may contain inert 1s).
Cases to cover: gcd=1/>1 first moves, m=n, terminal base boards, g_p=0 primes.
Watch out for: shares the g_p-preservation engine with approach 1 (robustness/architecture
  variant, not maximally independent) — its distinct payoff is (b) without any terminal-state
  argument; keep the value μ(B) inside the induction hypothesis or (b) is lost.

---

Recommended build set (all three are new; hand every one to the outline-reviewer):
per-prime-gcd-invariant, confluence-normal-form, strong-induction-descent.
Note on registration: I only hold the read-only ranker sampler; the three new approach files
are written and ready for the reviewer/registrar to register and rank.
