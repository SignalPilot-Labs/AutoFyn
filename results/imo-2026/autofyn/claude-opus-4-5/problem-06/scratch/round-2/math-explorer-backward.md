## imo-2026-06 (Lens: Backward Extension of Periodicity)

- **Distinct openings:**

  1. **"No backward extension needed" reformulation.** The entire startup/backward-extension problem dissolves if we reformulate the conclusion as: "the sequence equals the greedy sequence on V* (the stable valid set) from n=1." Then T and L work uniformly for all n. The two key lemmas that make this work are independent of "stabilization time N" — they hold structurally for all n simultaneously (see details below).

  2. **Pairwise non-coprimality as the universal key.** Every two sequence terms a_j, a_k share a prime (gcd > 1, forced by construction in both directions: if k > j, then a_k was chosen to share a prime with a_j; if k < j, then a_j was chosen to share with a_k). This pairwise property, combined with the fact that H* consists of actual prime sets of terms, gives: P(a_j) ∩ Q ≠ ∅ for every Q ∈ H* and every j ≥ 1. So a_j ∈ V* for all j — this directly resolves the reviewer's concern without any induction or case split on n vs N.

  3. **Antichain refinement gives V* ⊆ V_{H_n}.** For any n, every element Q of H_n satisfies: Q = P(a_j) for some j ≤ n (H_n picks minimal prime sets from the first n terms). In the full collection {P(a_k) : k ≥ 1}, this same P(a_j) either stays minimal (so Q ∈ H*) or is superseded by some later P(a_k) ⊂ Q (so some Q* ∈ H* with Q* ⊊ Q exists). Either way, there exists Q* ∈ H* with Q* ⊆ Q. Therefore any transversal of H* also hits Q, meaning V* ⊆ V_{H_n} for ALL n — not just for n ≥ N.

  4. **The "greedy on V*" equivalence (combinatorial squeeze).** For each n: a_{n+1} = min V_{H_n} ∩ (a_n, ∞) (by definition). Since V* ⊆ V_{H_n}, we get min V_{H_n} ∩ (a_n, ∞) ≤ min V* ∩ (a_n, ∞), i.e., a_{n+1} ≤ min V* ∩ (a_n, ∞). But a_{n+1} ∈ V* (from opening 2), so a_{n+1} ≥ min V* ∩ (a_n, ∞). Together: a_{n+1} = min V* ∩ (a_n, ∞). The sequence is exactly the greedy traversal of V* from n=1. No startup phase, no extension needed.

  5. **Startup terms fit the period automatically.** Verified computationally for a1 ∈ {6,10,14,15,21,30,35,42,70,77,91,105,143,210}: (a) every a_j ∈ V*, (b) the greedy on V* reproduces the sequence exactly from n=1, (c) a_{n+T} = a_n + L holds for ALL n ≥ 1 including the startup terms. The H* antichain for a1=35 is {{5,7},{2,5},{3,5},{2,3,7}}, not K_k^2, and the period is T=34, L=210 — this holds from n=1.

- **Candidate technique(s):**
  - Greedy-sequence-on-periodic-set argument: once V* is identified as L-periodic with T valid residues per period, and the sequence equals the greedy on V*, shift-periodicity a_{n+T} = a_n + L for all n follows immediately.
  - The "pairwise non-coprimality" structural fact: every two terms share a prime (by construction symmetry: a_k is chosen with gcd > 1 with ALL earlier terms, so each earlier term also shares a prime with a_k). This is a "free" theorem that the proof should state explicitly as a standalone lemma.

- **Cheap-kill candidates:**
  - The key cheap structural observation: the antichain H* consists of actual prime sets of terms (not abstract sets), so pairwise gcd > 1 immediately gives P(a_j) ∩ Q ≠ ∅ for all Q ∈ H*. This is a one-line argument, not a deep lemma.
  - The inclusion V* ⊆ V_{H_n} follows from the antichain definition alone (no case analysis needed).

- **Knowledge-base entries to use:**
  - "Modular arithmetic, CRT": V* is a union of residue classes mod L, so periodic mod L.
  - "Invariants & monovariants": the antichain H_n is a monovariant (in the sense that eventually H_n = H* and stays stable); the argument needs this stabilization.
  - "Pigeonhole / extremal principle": the antichain is finite (bounded by the finite prime support), so must stabilize — this is still Gap A from the antichain-stabilization approach.

- **Analogous past problems (cruxes):** None directly identified in this scouting; the crux of this problem (greedy on a periodic set is shift-periodic) is specific to this construction.

- **Prior progress:**
  - two-of-k-structure: mostly correct, K_k^2 claim is false and not needed, backward extension argued hand-wavily. Status: partial.
  - backbone-periodicity: fatally flawed (backbone primes only). Status: dead-end.
  - antichain-stabilization: correct outline but Gap A (prime support bounded) and Gap B (self-blocking) unresolved. Status: unsolved.
  - clique-valid-set: identifies V eventually as a clique but has gaps. Status: unsolved.

- **Dead ends (do not retry):**
  - backbone-periodicity: restricts to backbone primes B = P(a_1), misses primes entering later (e.g., 2 for a1=15 gives wrong L=15 vs correct L=30).
  - K_k^2 claim: computationally false for a1=35 (H* = {{5,7},{2,5},{3,5},{2,3,7}}, has a 3-element set).

- **Small-case / intuition notes (all labeled as empirical):**
  - (Conjecture from computation) The greedy on V* exactly reproduces the sequence from n=1, for all tested starting values. This strongly suggests the proof strategy in Opening 4 is correct.
  - (Conjecture from computation) H* stabilizes after finitely many steps for all tested a1. For a1=35, H* stabilizes at step 4 and has 4 elements. The antichain does NOT always become K_k^2 (a1=35 is a counterexample), but L-periodicity and T-shift still hold.
  - (Proved) Every a_j is in V* for all j ≥ 1 (the pairwise non-coprimality argument is rigorous and unconditional).
  - (Proved) V* ⊆ V_{H_n} for all n (the antichain refinement argument is rigorous).
  - (Key gap remaining) Proving H* stabilizes in finite time (Gap A of antichain-stabilization) — the prime support must stop growing. This is the main unresolved gap; the backward extension issue is NOT a gap once the "greedy on V*" reformulation is adopted.
