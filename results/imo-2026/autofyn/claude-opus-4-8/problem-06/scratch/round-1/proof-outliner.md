# Proof-outliner field — imo-2026-06 (round 1)

## imo-2026-06

**Problem.** Sequence a_1,a_2,… of integers >1; a_{n+1}=smallest integer >a_n with gcd(a_{n+1},a_i)>1 for all i≤n. Prove ∃ T,L>0 with a_{n+T}=a_n+L for every n.

**Shared proved foundation (all three approaches build on these two elementary, verified facts):**
- **T1 (gaps ≤ a_1):** every positive multiple of a_1 is admissible — a_1 and a_i share a prime p (gcd>1), so a_1|m ⇒ p|gcd(m,a_i)>1; each length-a_1 window has one ⇒ a_{n+1}-a_n ≤ a_1. (Computationally confirmed maxgap ≤ a_1 across 25+ starts.)
- **T2 (pairwise gcd>1):** gcd(a_i,a_j)>1 for ALL i≠j (symmetry) ⇒ every term hits every clause S_j=supp(a_j).

**Shared clean FINISH (fully worked, no gap) once the eventual admissible set A is known periodic mod M:**
- Every term a_n (all n≥1) has a_n mod M ∈ A (by T2). And a_{n+1}=min(A∩(a_n,∞)) for ALL n≥1 (a_{n+1}∈A⊆A_n is the min of the larger set A_n, so equals the min of A above a_n). Hence the sequence IS the increasing enumeration of A from a_1 ⇒ a_{n+T}=a_n+L for every n with L=M, T=|A mod M|. Verified from n=1 for a_1∈{15,35,105,143,221}.

**The single genuine crux (explicit GAP in all three): the admissible constraint system stabilizes — only finitely many primes are "essential", so A_n = union of residue classes mod M is eventually constant.** Empirically every essential prime ≤ maxpf(a_1) and gaps ≤ a_1. Per dispatch this convergence is unavoidable; the three approaches DIVERGE in how they attack this crux and how they exploit the structure (chain-termination via number theory / fixed-point closure via monovariant / reversible finite-state machine). Advance all three so the field probes the crux three different ways; if one mechanism cracks it the others inherit a certifiable shared lemma.

---

clique-descent: new
Target: ∃ T,L>0 with a_{n+T}=a_n+L for every n≥1 (the whole claim).
Technique: descending-chain termination (monovariant on a finite subset lattice) + greedy-enumeration finish.
Skeleton:
  1. GAP (crux): every essential prime ≤ P₁=maxpf(a_1) ⇒ essential primes lie in fixed finite set {p≤P₁} — number-theoretic redundancy/domination of large primes.
  2. Finitely many possible minimal clauses ⇒ chain A_1⊇A_2⊇… stabilizes to A periodic mod M — by finiteness of the subset lattice.
  3. A is a GCD-clique — tail greedily lists all of A above a_N; a coprime pair (lifted by periodicity above a_N) forces a later term coprime to an earlier one, contradicting T2.
  4. Every term ∈ A (all n) — T2 on minimal clauses.
  5. Sequence = greedy enumeration of A from n=1 — a_{n+1}∈A is min of larger A_n.
  6. a_{n+T}=a_n+L, L=M, T=|A mod M|.
Key lemmas: gaps≤a_1 (T1); pairwise-gcd (T2); stabilized⇒clique (enumeration+T2); for-all-n via min-of-superset. Crux: essential primes ≤ maxpf(a_1) — large prime q in supp(a_k) always shares p≤P₁ with a_1 and supp(a_k) contains a strictly smaller clause, so q never sits in a MINIMAL clause.
Open gaps: step 1 only (essential-prime finiteness). Any finite bound suffices.
Cases to cover: prime-power a_1 (M=p,T=1); even a_1 (M=2,T=1) — subsumed by the general lemma.
Watch out for: A is the finer transversal set, not {some p∈S_1 divides m}; step-3 needs both coprime reps above a_N; state step 5 for ALL n.

sieve-closure: new
Target: the whole claim (∃ T,L, all n).
Technique: fixed-point / self-consistent-closure of the clause system + coprime-pair monovariant.
Skeleton:
  1. Vacuous-constraint lemma: once A_n is self-consistent (GCD-clique) the next term is in the clique, adds no constraint ⇒ A fixed forever.
  2. GAP (crux, different mechanism): A_n becomes self-consistent after finitely many effective steps — coprime-pair count Φ(A_n) strictly drops on each effective term, lives in a finite space (essential primes finite), ⇒ termination.
  3–5. Every term ∈ A (T2); sequence = greedy enumeration of A from n=1; conclude a_{n+T}=a_n+L, L=M.
Key lemmas: vacuous-constraint (self-consistent ⇒ fixed) is the fixed-point; Φ-monovariant termination is the distinct lever; same for-all-n finish.
Open gaps: step 2 — (a) essential primes finite (shareable with clique-descent), (b) Φ drops with no new coprime pairs created. Genuinely different if Φ can be bounded WITHOUT the prime bound.
Cases to cover: none separate.
Watch out for: verify Φ never increases (survivors are a subset); "self-consistent" ≠ single-modulus set.

finite-state-bijection: new
Target: the whole claim (∃ T,L, all n) — headlines the "for EVERY n" (pure periodicity from n=1).
Technique: finite-state machine + reversibility (aimo-0514 crux): cyclic-bijection successor ⇒ purely periodic orbit, no transient.
Skeleton:
  1. GAP (crux, imported): constraint system stabilizes ⇒ finite state set A mod M.
  2. Every term is a state from n=1 (T2) — no transient.
  3. Successor f:A→A well-defined (A a union of residue classes ⇒ "next admissible above x" is translation-invariant mod M); (a_{n+1} mod M)=f(a_n mod M) all n.
  4. f is a cyclic-order successor ⇒ bijection ⇒ functional graph = disjoint cycles.
  5. Purely periodic from n=1: a_{n+T}=a_n+L with T=|A|, L=M (via "each length-M window holds exactly |A| admissible values in order", sidestepping per-cycle bookkeeping).
Key lemmas: translation-invariant successor; bijection ⇒ no transient (reversibility crux); T=|A|,L=M safe accounting.
Open gaps: step 1 (shared stabilization) + step-4 per-cycle vs global-T care (use T=|A|).
Cases to cover: none separate.
Watch out for: reversibility only valid AFTER M finite; don't claim a minimal period — use T=|A|, L=M.

---

**Recommended build set (advance all three — round 1 breadth):** clique-descent, sieve-closure, finite-state-bijection.

**Guidance to reviewer/builders:** The proof is ~90% done and clean EXCEPT the stabilization crux (finitely many essential primes). Prioritize builder effort on that crux. clique-descent attacks it by a hard number-theoretic bound (essential prime ≤ maxpf(a_1)); sieve-closure by a coprime-pair monovariant that may bound termination independently of the prime bound; finite-state-bijection imports it and instead nails the "for every n" pure-periodicity. If any builder proves the stabilization lemma, CERTIFY it as a shared lemma in results/imo-2026-06/lemmas/ so the other two can import it and immediately complete. These three are far apart in mechanism (number theory / order-theoretic monovariant / dynamical reversibility); if the prime-bound route stalls, the monovariant route is the intended escape — flag next round for a genuinely different framing only if BOTH the prime-bound and the monovariant stall on the same wall.

build set: clique-descent, sieve-closure, finite-state-bijection
