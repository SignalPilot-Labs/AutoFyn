## imo-2026-06

Round-1 status: the whole problem is certified-reduced (lemmas/bounded-gaps-and-clique.md, §§0–4) to
ONE crux: **finitely many minimal clauses** (equiv. **the essential-prime set Π is finite**). Round-1's
Lemma S ("all minimal clauses ⊆ {primes ≤ P₁}") is **FALSE** (a₁=385: clauses {3,7,19},{2,11,19} share
only 19 > P₁=11). Do NOT re-derive the reduction or finish; import them. All three approaches below are
COMPLETE end-to-end attempts whose SOLE open gap is the corrected finiteness crux, attacked from three
GENUINELY DIFFERENT walls so they do not fail together.

**New certified-clean fact I established this round (verified a₁∈{4,6,15,35,77,143,210,221,385,255,1001,2310}, 0 violations):**
the correct threshold is **a₁, not P₁**. Define Lemma S′: *any two clauses share a common prime ≤ a₁*
(finite ground set G := {primes ≤ a₁}). Then the round-1 Proposition-1 mechanism goes through UNCHANGED
with G in place of Π, giving a fully clean reduction (Prop 1′ below). This turns the crux into exactly the
IMO-2024-P5 / aimo-0030 conclusion. This is the spine of approach **descent-shared-prime**.

---

descent-shared-prime: new
Target: the whole claim — ∃ T,L>0 with a_{n+T}=a_n+L ∀n≥1.
Technique: minimal-counterexample / infinite descent (knowledge_base "Contradiction / minimal counterexample / infinite descent"), q-cofactor divisor analysis, adapted from aimo-0030 (IMO-2024-P5 — the SAME good-number sequence).
Skeleton:
  1. Import certified reduction + finish (lemmas/bounded-gaps-and-clique.md): Tools 1–2, Sub-lemma E, Cor E.1, "finitely many minimal clauses ⟹ A periodic ⟹ a_{n+T}=a_n+L ∀n". — CERTIFIED.
  2. **Prop 1′ (NEW, clean — this is the corrected Prop 1, PROVED from Lemma S′).** Let G={primes ≤ a₁} (finite). If Lemma S′ holds, every minimal clause ⊆ G. — by Cor E.1: given minimal clause C, put C′=C∩G; C′≠∅ (Cor 1.1 gives a prime ≤P₁≤a₁ in C). For any clause D, S′ gives a shared prime ≤a₁ lying in C∩D∩G ⊆ C′, so C′ hits D; C′ hits every clause ⟹ C′ is a clause (Cor E.1); C′⊆C + minimality ⟹ C′=C ⊆ G.
  3. Finitely many subsets of the finite G ⟹ finitely many minimal clauses ⟹ crux ⟹ conclusion (step 1). So the ENTIRE problem reduces to Lemma S′.
  4. **Lemma S′ via descent (the gap).** Suppose S′ fails; take the lex-minimal violating pair (S_j,S_k), j<k, whose shared primes are all > a₁. Fix q∈S_j∩S_k (q>a₁). Set e = a_k / q^{v_q(a_k)}, supp(e)=S_k\{q}.
     - e ∈ A_{j-1}: for l<j the pair (l,k) is non-violating (minimality), so S_l∩S_k has a prime ≤a₁ ≠ q, which lies in S_k\{q}=supp(e); so e hits every S_l, l≤j-1.
     - e misses S_j: S_j∩supp(e)=(S_j∩S_k)\{q}; all of S_j∩S_k is >a₁, and by choosing the descent on the FULL disjoint-small-shadow version (σ(S_j)∩σ(S_k)=∅, σ=·∩G) this is ∅, so gcd(a_j,e)=1.
     - Contradiction hunt: if e>a_{j-1} then a_j≤e (minimality of a_j in A_{j-1}); with gcd(a_j,e)=1 and Tool 2 (every term pairwise-non-coprime), e is NOT a term. Drive the descent: show either (a) some multiple of e exceeding a₁ lies in A and is a term coprime to a_j (Tool-2 contradiction), or (b) supp(e) dominates an earlier clause, producing a violating pair with smaller k (descent), contradicting minimality.
Key lemmas (claim + mechanism):
  - Prop 1′ — minimal clause C = C∩{primes≤a₁}, because its small-shadow already hits every clause (Lemma S′) so is itself a clause (Cor E.1) and can't be proper by minimality. THIS makes the finite ground set a₁ (not P₁) and is the clean fix to the round-1 bug.
  - Lemma S′ (gap) — any two clauses share a prime ≤ a₁, because a large-only shared prime q lets the q-cofactor e slip below a_j while staying admissible yet coprime to a_j, which Tool 2 forbids for terms; descent on (j,k) closes it.
Open gaps: Lemma S′ step 4 — the closing contradiction ("e or its multiple must appear as a term / dominate an earlier clause"). This is the genuine hard core; everything else (steps 1–3) is clean and complete.
Cases to cover: b:=e vs a₁ split (b>a₁ already handled in round-1 clique-descent §5 "first-appearance non-minimal"; b≤a₁ is the new open branch — the descent must cover it, since computationally b≤a₁ in nearly all cases).
Watch out for: aimo-0030 manufactures "good numbers" via game moves we lack — replace that step by Cor E.1 (support-is-a-clause) + Sub-lemma E, never by assuming a value with prescribed support is a term without checking it hits every clause. Do the descent on disjoint SHADOWS σ(·)∩G, not on a single prime, so S_j∩supp(e)=∅ is guaranteed.

---

clique-descent: revise
Target: the whole claim (unchanged).
Technique: descending-chain stabilization, but finiteness via an EXTREMAL COUNT bounding the number of distinct large essential primes (knowledge_base "Pigeonhole / extremal principle", "Sunflower/Δ-system"). Distinct wall from descent: no minimal-counterexample, a direct finitary bound.
Skeleton:
  1. Import reduction + finish (as above). Retarget the crux from FALSE Lemma S to "finitely many minimal clauses"; retract Prop 1 (P₁ version).
  2. **Split the minimal-clause family** M = M_small ⊔ M_large, where M_small ⊆ 2^Π (Π={primes≤P₁}) and M_large = minimal clauses containing ≥1 prime > P₁. |M_small| ≤ 2^{π(P₁)} (finite, trivially).
  3. **Sunflower/per-prime bound (from sunflower explorer).** For a fixed large prime q, the minimal clauses containing q form a sunflower with core {q}: their small-shadows σ=·∩Π are pairwise DISJOINT (if {q,S_i},{q,S_j} shared a small prime they'd share ≤P₁ and each would need the other as a minimality witness — removing q from one misses the other, forcing S_i∩S_j=∅). Pairwise-disjoint nonempty subsets of Π number ≤ π(P₁). So ≤ π(P₁) minimal clauses per large prime.
  4. **Bound the number of DISTINCT large essential primes (the gap).** Key structural theorem (density explorer Opening 1, PROVABLE from Tool 2): two minimal clauses with disjoint small-shadows must share a common LARGE prime (else their supports are disjoint, contradicting pairwise intersection). Map each large essential prime q to the "intersection gap" it fills — an unordered pair {σ(C),σ(D)} of disjoint small-shadows that only q reconciles. Show this assignment lands in the finite set of disjoint shadow-pairs (≤ 3^{π(P₁)}) and bound its fibers, giving finitely many large essential primes.
  5. Finitely many large essential primes × (≤π(P₁) clauses each) + finite M_small ⟹ finitely many minimal clauses ⟹ crux ⟹ conclusion.
Key lemmas (claim + mechanism):
  - Disjoint-shadow ⟹ shared-large-prime — because all minimal clauses pairwise intersect (Tool 2, Cor E.1), so disjoint small parts force the intersection into the large primes.
  - Per-large-prime sunflower bound ≤ π(P₁) — pairwise-disjoint small petals live in Π, |Π|=π(P₁).
Open gaps: step 4 — that the map {large essential prime} → {disjoint small-shadow pair it reconciles} has finitely many primes total (finite domain). Concretely: bound the number of distinct large primes that can each be the UNIQUE reconciler of some disjoint shadow-pair. Fibers may be non-trivial; needs the witness/greedy-minimality constraint to force injectivity or a per-pair cap.
Cases to cover: a₁ prime power / single prime factor (M_large=∅ trivially, cheap kill); the mutual-witness case (≥2 large clauses sharing q) is the hard one — first-appearance-only was round-1 partial progress and does NOT cover it.
Watch out for: do NOT reuse P₁ as the finiteness ground — large essential primes exist (19 for a₁=385). The count must bound DISTINCT large primes; per-prime finiteness (step 3) alone is not the crux.

---

sieve-closure: revise
Target: the whole claim (unchanged).
Technique: closure / fixed-point (self-consistent GCD-clique), finiteness of Π via a WITNESS-CASCADE absorption argument (density explorer Opening 2) — a third distinct wall (each large prime's minimality-witness must absorb the other large primes into one finite support).
Skeleton:
  1. Import reduction + finish; keep Lemma 1 (vacuous-constraint/fixed-point) and Lemma 2 (Π finite ⟹ stabilization mod ∏Π). Retarget crux to "Π finite" (already this approach's correct framing — sieve-closure was NOT chasing the false P₁ statement, only its monovariant was insufficient).
  2. **Witness structure.** Each minimal clause H_i={q_i}∪C_i (q_i large, C_i its small/other part) has a minimality witness T_i — a term with supp(T_i)∩C_i=∅ (else C_i alone is a hitting set and H_i not minimal). T_i must hit H_i ⟹ q_i∈T_i.
  3. **Cascade / absorption (the gap).** T_i is a term ⟹ (Tool 2) hits every other H_j. If C_i⊇C_j then supp(T_i)∩C_j=∅, so T_i hits H_j only via q_j ⟹ q_j | T_i. When the small-shadows C_i form a chain/nest (or a common refinement forces the ⊇ relations), one witness T_i absorbs ALL other large primes q_j into its finite support ⟹ #{large essential primes} ≤ Ω(T_i) < ∞.
  4. Establish the nesting/refinement hypothesis needed in step 3 from the self-consistent-closure structure (Lemma 1) — the closure forces the small-shadow family toward a finite refinement, capping the disjoint-shadow "gaps".
  5. Finitely many large essential primes + finite small-shadow lattice ⟹ Π finite ⟹ Lemma 2 ⟹ conclusion.
Key lemmas (claim + mechanism):
  - Witness contains its own large prime — T_i avoids C_i but must hit H_i={q_i}∪C_i, so q_i|T_i.
  - Absorption bound — when C_i⊇C_j, T_i can hit H_j only through q_j, so a single finite term's prime factorization caps the number of large essential primes (Ω(T_i)<∞).
Open gaps: step 3–4 — that the shadow-nesting condition (C_i⊇C_j) holds often enough (or that some single witness absorbs all large primes) to yield a finite bound. The nesting is not automatic; deriving it from the closure/fixed-point structure is the wall for this framing.
Cases to cover: "all large clauses share a common small prime p" branch — then {p} is a hitting set ⟹ A={multiples of p}, p|a₁, drastically simplifying (near cheap-kill); the residual hard case is genuinely disjoint small-shadows.
Watch out for: keep this framing's wall (witness absorption) distinct from clique-descent's (gap-counting) — do not silently import the shadow-pair count; if both collapse to the same sub-claim, flag it for round-3 reframing.

---

Field summary for the reviewer:
- Three complete attempts, ONE shared crux (finitely many minimal clauses / Π finite), THREE distinct walls:
  descent-shared-prime = minimal-counterexample descent proving Lemma S′ (cleanest: step 4 is the only gap, and Prop 1′ reduction is airtight);
  clique-descent = extremal count of distinct large essential primes via disjoint-shadow gaps;
  sieve-closure = witness-cascade absorption of large primes into one finite support.
- Recommended build priority: descent-shared-prime (new, cleanest reduction Prop 1′, closest corpus analogue aimo-0030), then clique-descent (revise), then sieve-closure (revise).
- finite-state-bijection: leave as-is (not nominated) — it only repackages the certified finish and imports the crux, adding nothing to closing it; keep for breadth only.
- SHARED-GAP WATCH for the orchestrator: all three ultimately hinge on "bound the large essential primes." descent-shared-prime SIDESTEPS the count (proves S′ directly) — if it also stalls at step 4 AND the two counting/cascade routes stall on the distinct-large-prime bound, round 3 must open a genuinely 4th framing (e.g. a growth/size argument: a large prime q>a₁ in a minimal clause forces a term below the pure-small-prime admissible minimum, impossible once the small-prime structure matures).
