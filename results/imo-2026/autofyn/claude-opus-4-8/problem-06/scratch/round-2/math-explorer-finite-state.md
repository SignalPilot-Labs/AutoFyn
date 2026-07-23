## imo-2026-06 — Lens: Finite-State / Gap-Sequence / Direct-Characterization

### Executive summary

The gap-pigeonhole ("finite-alphabet") route is NOT independent of the crux. The small-prime-shadow intersection route provides the cleanest reformulation of Lemma S and connects directly to the aimo-0030 crux, which is the closest corpus analogue. A partially-worked descent argument emerges from that analogue, with one genuine gap remaining — see "Distinct openings" item 3.

---

- **Distinct openings:**

  **(A) Gap-pigeonhole / finite-automaton** — DEAD END as an independent route. The gap sequence g_n = a_{n+1}−a_n ∈ {1,...,a_1} lives in a finite alphabet, but the "state" that determines the next gap is A_n (the current admissible set), not a bounded window of past gaps. Two positions n₁, n₂ with identical gap-windows (g_{n₁},...,g_{n₁+W−1}) = (g_{n₂},...) need not satisfy A_{n₁} = A_{n₂}, so they need not extend identically. Proving eventual periodicity of the gap sequence IS equivalent to proving A_n stabilizes — this route collapses to the crux rather than bypassing it. Do not pursue as an independent attack.

  **(B) Direct characterization A = {m : m hits every small-prime-only clause}** — also reduces to the crux. Writing A = {m : m hits every minimal clause} is valid, but "every minimal clause ⊆ Π" IS the crux (Prop 1 of clique-descent). No shortcut here.

  **(C) Small-prime-shadow pairwise-intersection + aimo-0030 descent** — the most promising new route. Restate Lemma S cleanly: define the *shadow* σ(C) = C ∩ Π (nonempty by Cor 1.1) for each clause C. Lemma S ⟺ {σ(C) : C clause} is a pairwise-intersecting family in 2^Π \ {∅}. Now run the aimo-0030 crux adapted to our setting:

    - Assume the pair (C = S_j, D = S_k), j < k, is lexicographically minimal with σ(C) ∩ σ(D) = ∅ (equivalently S_j ∩ S_k ⊆ large primes). Say q is a large prime in S_j ∩ S_k.
    - **Key computation:** Let e = a_k / q^{v_q(a_k)} (q-cofactor of a_k). supp(e) = D' = S_k \ {q} (the small part plus other large parts of D, minus q).
    - **D' hits all S_l for l < j:** By minimality of j (j is the minimal first index for this k), every pair (l, k) with l < j has S_l ∩ S_k ⊉ {q}, meaning S_l ∩ S_k contains a prime ≠ q. That prime lies in D' = S_k \ {q}. So D' hits S_l for l < j. Hence e ∈ A_{j-1}.
    - **D' does not hit S_j:** S_j ∩ D' = S_j ∩ (S_k \ {q}) = (S_j ∩ S_k) \ {q} = ∅. So e ∉ A_j.
    - **σ(S_j) and σ(e) = D' ∩ Π = σ(D) are disjoint** (since σ(C) ∩ σ(D) = ∅).
    - **e < a_k** and if e > a_{j-1}: e ∈ A_{j-1} ∩ (a_{j-1}, ∞), so a_j ≤ e (minimality of a_j). Then gcd(a_j, e) = supp(S_j) ∩ supp(D') ∩ ... = S_j ∩ D' = ∅. So **gcd(a_j, e) = 1**.
    - **The tension:** a_j and e are both in A_{j-1} with gcd = 1. This is a very tight constraint. If e = a_m for some m > j, then gcd(a_j, a_m) = 1, violating Tool 2. So e is NOT a future term. But e < a_k, and the sequence must eventually pick a_k. What forces a_k to appear rather than some term between a_{j-th} and a_k that might break the "only large prime shared" property?
    - **THE MISSING STEP:** We know e is not a term (by the coprimality + Tool 2). But we need to derive a contradiction from this. The proposed continuation: since e ∈ A_{j-1} and gcd(a_j, e) = 1, the element e will be permanently excluded from A_j (fails to hit S_j). So the q-cofactor of a_k is not in A_j. This means a_k cannot be "decomposed" as q-part × small-admissible-element. However, this does not immediately force a contradiction — a_k itself is still in A_{k-1} (hits S_j via q).
    - **What aimo-0030 does differently:** In aimo-0030, the stripped number x (Claim 4) is shown to be "good" by minimality of the counterexample. In our setting, showing e is related to a "term" or "clause" before k requires a different mechanism — possibly showing e or a multiple of e must appear as a term before k, which would contradict gcd(a_j, e) = 1 via Tool 2. This is the remaining gap.

  **(D) Monovariant on the σ-family** — partially promising. Since {σ(C) : C clause} is a family in 2^Π, which has 2^|Π| elements, and the family is built cumulatively (each new clause adds a shadow σ(S_n)), one could track the "intersection graph" of the shadow family. If at any step two shadows become disjoint, we have a Lemma S violation. Equivalently: track whether the MINIMUM pairwise intersection size across all shadow pairs ever hits 0. This is a finite monitor on a finite set Π, but it doesn't directly prove Lemma S — it just rephrases the induction.

- **Candidate technique(s):**
  - **Minimal counterexample descent** (General Proof Methods: contradiction/infinite descent, knowledge_base.md). The aimo-0030 crux provides the clearest template: take the minimal pair violating Lemma S, construct a "q-cofactor" e for the later clause, show e contradicts Tool 2 (if it's a term) or is not a term, then trace the contradiction through the minimality.
  - **Pigeonhole on shadows:** the shadow family {σ(C)} lives in the finite set 2^Π; some structural property of the greedy selection might force the shadows to be pairwise non-disjoint (Combinatorics: Pigeonhole / finiteness in knowledge_base.md).

- **Cheap-kill candidates:**
  - **a_1 is a "universal bridge":** Every clause C shares a small prime with supp(a_1) ⊆ Π (Tool 2 + a_1 ∈ A). But two clauses C, D can share different small primes of supp(a_1) while being disjoint from each other. So this doesn't immediately kill Lemma S violations — it only shows σ(C) ∩ supp(a_1) ≠ ∅ for all C.
  - **Prime-power a_1:** If a_1 = p^k (prime power), then supp(a_1) = {p} and every clause must contain p (every term shares p with a_1). So σ(C) ∋ p for all C, and all shadows pairwise share p. Lemma S holds trivially. This is a cheap kill for the prime-power case.
  - **b ≤ a_1 computation:** For a_1 = 143, the q-cofactor b = a_i/q^{v_q(a_i)} ≤ a_1 in ALL tested cases (never b > a_1 for the first-appearance clause of any large prime). The "partial progress" in clique-descent (b > a_1 → b is a term → S_i non-minimal) handles ZERO of the tested cases directly. This partial progress needs a complement for the b ≤ a_1 case. Evidence (a_1=143, 18 large primes tested): every such b has supp(b) appearing as a clause BEFORE the large prime appears. This is the empirical mechanism: supp(b) is already a clause, hence S_i is non-minimal (supp(b) ⊊ S_i). The proof task is showing supp(b) (or some subset) always appears as a clause before i.

- **Knowledge-base entries to use:**
  - "General Proof Methods: Contradiction / minimal counterexample / infinite descent" — core technique for Lemma S via aimo-0030 descent.
  - "Combinatorics: Pigeonhole / finiteness" — the shadow family lives on finite set 2^Π.
  - "Divisor analysis" (Number Theory) — the q-cofactor construction: a_i / q^{v_q(a_i)} has the same support minus q.
  - "Invariants & monovariants" — if the descent terminates (eventually the q-cofactor argument loops back to a smaller pair), the monovariant is the index k.

- **Analogous past problems (cruxes):**
  1. **aimo-0030** (number_theory, divisibility-and-gcd) — DIRECTLY ANALOGOUS. Crux: "Strengthen 'two good numbers share a forbidden-class (large) prime' to 'they share an allowed-class (small) prime' by minimal-counterexample descent: take the minimal violating pair (b, b'), strip large primes from one via Claim 4 to get x with same small primes but x ≤ b, x is good (by minimality of counterexample), x and b' share a prime (good numbers pairwise do), that prime is small (x has only small primes), but small prime lies in b (same shadow as x), contradicting b, b' sharing only large primes." The template maps exactly onto Lemma S. Gap in transfer: our "Claim 4" (stripping large primes from a clause produces a smaller clause) requires showing the stripped number's support is a clause, which in turn needs the sequence to have generated a term with that support. The descent works cleanly in aimo-0030 because the game produces good numbers at every step; in our sequence, the greedy does not guarantee terms with arbitrary small-prime signatures.

  2. **aimo-0421** (number_theory, divisibility-and-gcd) — partially analogous. Crux: "Since gcd of a fixed element with a varying one is always a divisor of that fixed element, it takes only finitely many values, so over an infinite family of partners, infinitely many must give the same gcd value." Applied to our setting: for any fixed clause C, the set {C ∩ D : D clause} consists of nonempty subsets of C, hence is finite. By pigeonhole over infinitely many clauses, infinitely many have the same intersection with C. This might allow structural compression of the clause family but does not directly prove Lemma S.

- **Prior progress:**
  - Certified (rounds 0–1): Tool 1 (gaps bounded), Tool 2 (pairwise gcd, every term in A), Sub-lemma E (greedy takes all admissibles, Cor E.1), minimal-clause reduction, for-every-n finish. All in lemmas/bounded-gaps-and-clique.md.
  - Partial (round 1): first-appearance clauses of large prime q are non-minimal IF b = a_i/q^{v_q(a_i)} > a_1 (mild size condition). This covers NO cases computationally for a_1 = 30 or 143 (b is always ≤ a_1 in these examples).
  - Open: Lemma S in full generality. The descent-from-aimo-0030 direction is the best live lead.

- **Dead ends (do not retry):**
  - **Gap-window pigeonhole as standalone proof** — reduces to A_n stabilizing, i.e., exactly the crux. Not a bypass.
  - **Direct density argument (Lemma 3 from sieve-closure)** — strict density drops don't bound the number of effective steps since drops shrink to 0. Confirmed dead by round-1 reviewer.
  - **"b > a_1 → b is a term" partial progress** — handles 0 out of ≈20 tested cases for a_1 ∈ {30,143,...}. Needs a companion argument for b ≤ a_1.

- **Small-case / intuition notes (labeled as conjectures):**
  - *Conjecture (empirically verified, not proved):* For a_1 = 30 = 2·3·5: A stabilizes immediately to {even numbers} after a_2 = 32 = 2^5 introduces the single minimal clause {2}. Large primes 17, 19, 23, ... appear as factors of 2q-form terms (b=2, supp(b)={2} ⊆ clause {2} already present). Every large prime appears in a non-minimal clause. Lemma S holds with zero violations.
  - *Conjecture:* For a_1 = 143 = 11·13: four minimal clauses {2,11},{3,11},{11,13},{2,3,13} stabilize by index 12. All large primes appear in terms of form 2·11·q (b=22=2·11, and {2,11} is already a clause at index 4 < 18 = first large prime index). supp(b) is always a pre-existing clause BEFORE the large prime's first appearance. This is the empirical mechanism for Lemma S: the q-cofactor's support is always dominated by an earlier clause.
  - *Conjecture from aimo-0030 analogy:* The correct proof of Lemma S is a descent on the index k of the later clause, using the q-cofactor argument to show either: (a) e = a_k/q^{v_q(a_k)} must appear as a term before k (contradicting gcd(a_j, e)=1 and Tool 2), OR (b) supp(e) is dominated by an earlier clause (giving a pair with smaller k). Which branch fires depends on whether e > a_1 or e ≤ a_1.
  - *Conjecture:* The b ≤ a_1 case of first-appearance large primes resolves as: since b ≤ a_1 and b has supp(b) = S_i ∩ Π (only small primes), and b ∈ A_{i-1}, some multiple b · p^m (for p ∈ supp(b)) is > a_1 and in A_{i-1}, hence (if in A) is a term by Cor E.1. The question is whether this multiple is in A (hits future clauses). For this, one needs the small primes of supp(b) to hit every future clause — which holds once we establish Lemma S (circular). Breaking this circularity is the true hard core.
