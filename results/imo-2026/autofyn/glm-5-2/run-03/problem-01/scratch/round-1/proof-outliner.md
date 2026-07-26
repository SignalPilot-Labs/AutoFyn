## imo-2026-01

perprime-gcd-lexmonovariant: new
Target: Prove (a) the process terminates with exactly one integer M>1 remaining, and (b) M is independent of Confucius's move choices.
Technique: Per-prime p-adic exponent tracking. (b) via the invariant d_p = gcd of the multiset of p-exponents (preserved by the Euclidean step gcd(min,|a−b|)=gcd(a,b)); (a)-termination via the lexicographic monovariant (Ω, K) — Ω = total prime-factor multiplicity, K = count of entries >1 — which strictly lex-decreases every move and is bounded below; "exactly one" rules out the all-ones terminus via the same d_p invariant. KB lines 86, 117, 191, 184.
Skeleton:
  1. Per-prime move identity (α,β)→(min(α,β),|α−β|) — by v_p(gcd)=min, v_p(lcm/gcd)=max−min=|diff|, since gcd·lcm=mn.
  2. d_p = gcd of the multiset of p-exponents is invariant — because gcd(min,|α−β|)=gcd(α,β) (Euclidean step) and the other 2024 exponents are untouched.
  3. Monovariant (Ω, K) strictly lex-decreases each move — case analysis (coprime: Ω fixed, K drops; non-coprime m≠n: Ω drops by Ω(gcd)≥1, K fixed; m=n>1: both drop), using Ω additivity Ω(xy)=Ω(x)+Ω(y).
  4. Termination — Ω ∈ ℕ bounded below, K ∈ [0,2026]; lex order on ℕ×[0,2026] well-founded (Ω drops finitely often; between drops, K drops finitely often).
  5. Stuck ⟺ K ≤ 1 — a move requires two entries >1.
  6. Rule out K=0 — terminus K=0 ⟹ all p-exponents 0 ⟹ d_p=0 ∀p (invariant) ⟹ initial all-ones, contradicting a_i>1. Equivalently d_p≥1 for some p ⟹ M>1 at terminus.
  7. Combine: termination at K=1 ⇒ exactly one M>1 remains. ✓(a)
  8. At terminus the multiset of p-exponents is {v_p(M),0,…,0}; its gcd is v_p(M); by invariance = d_p; hence M = ∏_p p^{d_p}, fixed by initial board ⇒ choice-independent. ✓(b)
Key lemmas (claim + mechanism):
  - gcd(min(α,β),|α−β|)=gcd(α,β) — because the Euclidean step gcd(a,b)=gcd(a,b−a) is gcd-preserving and min/|diff| is exactly that step.
  - Ω(m)+Ω(n)−[Ω(gcd)+Ω(lcm/gcd)]=2Ω(gcd)≥0, equality iff gcd=1 — because Ω is completely additive and the move's exponent accounting double-counts the gcd's min-exponent.
  - Non-coprime m≠n ⟹ lcm/gcd>1 — write m=ga,n=gb, gcd(a,b)=1, m≠n forces ab≥2.
  - All-ones terminus unreachable — because d_p invariant: terminus K=0 ⟹ initial all-ones contradiction; positive direction d_p≥1 for some p ⟹ M>1.
Open gaps: full rigorous case write-up of step 3 (the Ω-difference identity derived term-by-term on exponents); explicit well-foundedness statement of lex order; stuck⟺K≤1 lemma; step 8 convention gcd(e,0,…,0)=e and finiteness of the prime set; verify M=∏p^{d_p} by substitution on a worked example ({12,18,30,7,100,9,25}→210) for the reviewer's check.
Cases to cover: move cases (i) g=1, (ii) g>1 & m≠n, (iii) g>1 & m=n — exhaustive (g=1 with m=n impossible).
Watch out for: do NOT confuse d_p (gcd of exponents) with v_p(gcd of numbers)=min of exponents (not preserved); do NOT prove (a) by running per-prime Euclidean algorithms to completion (moves couple primes); Ω≥1 at reachable states comes from d_p, not from P's size (P can drop to 1).

exponent-multiset-dershowitz: new
Target: Prove (a) and (b), with (a)-termination supplied by a DIFFERENT engine: a Dershowitz–Manna multiset-ordering descent on the prime-exponent vectors, directly exploiting the per-prime Euclidean dynamics with no coprime/non-coprime case split. (b) and "exactly-one" still use the d_p invariant.
Technique: Encode each board number as its exponent vector **e** ∈ ℕ^r (r = primes dividing some initial number). Show every legal move strictly decreases the multiset of vectors in the Dershowitz–Manna order induced by the componentwise partial order; since all vectors stay in the finite box [0,**E_0**] (E_0 = exponents of initial total product), the multiset space is finite ⇒ well-founded ⇒ termination. KB lines 86, 117. Crux analogue aimo-0258 (multiset/positional-order termination).
Skeleton:
  1. Per-prime move identity: (**u**,**v**)→(min-cw(**u**,**v**), |**u**−**v**|) — by v_p identities, componentwise across all primes.
  2. Both new vectors ≤ max-cw(**u**,**v**) componentwise — because min ≤ max and |u_j−v_j| ≤ max(u_j,v_j) per coordinate.
  3. Strict multiset decrease: removed {**u**,**v**}, added {min,**diff**}; when **u**≠**v** at least one coordinate differs so min-cw < max-cw in that coordinate ⇒ min strictly below the removed maximal element; when **u**=**v**≠**0** the added **0** < **u**. Hence {**u**,**v**} >_mul {min,**diff**} strictly in both sub-cases.
  4. Every legal move strictly decreases E (multiset order) — a move is legal iff both chosen numbers >1 iff **u**,**v** ≠ **0** (and at least one ≠ the other, or the equal sub-case); both sub-cases give strict decrease by step 3.
  5. Termination — by induction every reachable vector ≤ **E_0** componentwise; the multiset space over the finite box [0,**E_0**] is finite; the Dershowitz–Manna multiset extension of a finite partial order is well-founded ⇒ no infinite descending chain.
  6. Stuck ⟺ ≤1 non-zero vector — restated legality.
  7. Rule out all-zero via d_p invariant (shared sub-lemma; some initial a_i>1 ⇒ d_{p_j}≥1 for some p_j ⇒ at terminus some entry nonzero) ⇒ exactly one M>1.
  8. M = ∏_p p^{d_p} at the terminus ⇒ (b) (shared sub-lemma).
Key lemmas (claim + mechanism):
  - The move is (**u**,**v**)→(min-cw, |**u**−**v**|) — because v_p(gcd)=min and v_p(lcm/gcd)=|diff|, applied componentwise across all primes simultaneously.
  - Both new vectors ≤ max-cw(**u**,**v**) — componentwise arithmetic.
  - {**u**,**v**} >_mul {min,**diff**} strictly for every legal move — the removed maximal element strictly dominates the added min (in a differing coordinate) or the added zero.
  - Well-foundedness over the finite box — finiteness of the bounding box [0,**E_0**] (every reachable vector ≤ **E_0** by induction), not the heavy Dickson wqo theorem.
Open gaps: rigorous write-up of the multiset-order decrease in both sub-cases (**u**≠**v** and **u**=**v**≠**0**); correct invocation of the Dershowitz–Manna multiset-order definition; proof that every reachable vector ≤ **E_0** by induction (the elementary well-foundedness source); import/derive the d_p invariant for steps 7–8.
Cases to cover: legal-move sub-cases **u**≠**v** and **u**=**v**≠**0** (both strict decrease); **u**=**v**=**0** is not legal.
Watch out for: do NOT rely on Dickson's wqo for well-foundedness on all of ℕ^r (use the finite bounding box); pin the differing coordinate where min-cw < max-cw when **u**≠**v**; this route does not separate coprime/non-coprime (its advantage) and does not replace the d_p invariant (its limitation — distinct contribution is only the (a) engine).

confluence-newman: new
Target: Prove (a) and (b), with (b) established by abstract-rewriting theory (Newman's lemma: terminating + locally confluent ⇒ confluent ⇒ unique normal form) rather than by computing M explicitly. The genuinely different framing of (b).
Technique: Treat the process as an abstract rewriting system on multisets of 2026 integers. Termination from the (Ω,K) lex monovariant (imported). Local confluence by checking all critical pairs (disjoint redexes commute; overlapping redexes sharing one entry are joinable by direct gcd/lcm algebra — the hard gap). Newman's lemma ⇒ confluence ⇒ unique normal form ⇒ (b). Exactly-one-M via the d_p invariant. Newman's lemma must be stated as a named theorem (not in KB).
Skeleton:
  1. Per-prime move identity (as in the direct route) — used in step 3.
  2. Termination (a)-finiteness — (Ω,K) lex monovariant (imported sub-lemma); supplies "terminating" half of Newman's lemma.
  3. Local confluence (the new hard step): any two moves from a state S join. Critical pairs:
     (A) Disjoint redexes (four distinct entries) — the moves commute; joinable in one step each.
     (B) Overlapping redexes (three entries {a,b,c}; moves on (a,b) and (a,c)) — apply the missing move on each branch and complete; joinable by gcd/lcm algebra (empirically verified on 20+ random triples; the algebraic proof is the open gap).
     (No third shape: same-pair redexes coincide.)
  4. Newman's lemma: terminating + locally confluent ⇒ confluent.
  5. Confluent + terminating ⇒ unique normal form ⇒ (b) WITHOUT exhibiting M's formula.
  6. Exactly one M>1 — unique normal form has ≤1 entry >1 (stuck); d_p invariant forces ≥1 (some initial a_i>1 ⟹ d_p≥1 for some p ⟹ terminus has that p-exponent ≥1) ⇒ exactly one. ✓(a)
  7. (Optional) Recover M = ∏p^{d_p} as a consistency check (not required for (b)).
Key lemmas (claim + mechanism):
  - Termination — (Ω,K) lex monovariant (imported).
  - Local confluence for overlapping critical pairs — because the per-prime Euclidean step commutes across the three-element configuration; the two-step reducts along the two branches coincide after a third move. (Empirical verification confirms; algebraic proof is the gap.)
  - Newman's lemma (terminating + locally confluent ⇒ confluent) — standard diamond lemma for terminating ARSs.
  - Unique normal form for confluent terminating ARSs.
  - d_p invariant for the all-ones ruling (imported).
Open gaps: the critical-pair joinability proof for case B (step 3) — exhibit the explicit common reduct of the two branches {g_ab,h_ab,c} and {g_ac,h_ac,b} by named moves and verify equality via gcd/lcm algebra; verification that no other critical-pair shape exists; the (Ω,K) monovariant sketched or imported so step 2 is not bare.
Cases to cover: critical-pair shapes (A) disjoint (commute), (B) overlapping one-shared-entry (hard); same-pair redexes coincide. (Ω,K) move cases if re-derived.
Watch out for: Newman's lemma is NOT in knowledge_base.md — must be stated precisely as a named theorem of abstract rewriting theory or the reviewer rejects it; the critical-pair joinability is the genuine risk (if the algebra fails this approach dies on step 3, but on a DIFFERENT gap than the direct route — that is the point of the diversity bet); need only local confluence, not full confluence; pin "normal form = stuck state = ≤1 entry >1" so confluence yields "all reachable stuck states are the same multiset"; this route reuses (Ω,K) and d_p — its distinct contribution is the (b)-via-confluence argument, a methodological diversity bet and the long shot.

(Note: the ideal/divisibility-lattice framing suggested in the dispatch was considered and CUT — its lattice-rank descent collapses to the Ω measure of the direct route, since Ω(N_0) is the rank of the divisor lattice of the fixed total product and the move's rank-drop equals the Ω-drop already used in perprime-gcd-lexmonovariant. Keeping it would be a technique-clone, not a different framing.)

build set: perprime-gcd-lexmonovariant, exponent-multiset-dershowitz, confluence-newman
