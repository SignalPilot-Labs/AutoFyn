## imo-2026-06 — Stabilization Mechanics for the Constraint Antichain

- **Distinct openings:**

  **Opening A — The frozen-antichain route (most direct).** Show H becomes self-blocking (H = Tr(H)) in finite steps. Once frozen, all future terms have prime sets dominated by H so H never changes. Use the monovariant f(H) = Σ_{Q ∈ H} 2^{-|Q|}: this is non-decreasing (proved below) and bounded above by 1 (for self-blocking antichains). If discrete step-size can be bounded away from 0, finiteness follows.

  **Opening B — The backward-extension-first route.** Prove ALL terms lie in V (the stable valid set) without first proving H stabilizes. This is immediate from the gcd conditions (see key structural facts below). Then reduce the whole problem to: "the greedy on a periodic valid set is shift-periodic." This splits the problem cleanly: prove V is eventually periodic separately.

  **Opening C — The support-shrinks route.** Track support(H) (the union of all primes in H-elements) rather than H itself. Computational evidence shows support(H) is NOT monotone: it can grow (when a new prime enters) and SHRINK (when a term with smaller prime set replaces a larger element of H). The final stable support is a strict subset of all primes ever seen. Exploit the shrinking phases: each "shrink step" increases f(H) by more than each "grow step," driving H toward termination.

  **Opening D — The "greedy visits every minimal transversal" route.** Show that the greedy sequence must eventually visit a term with prime set equal to each element of Tr(H) \ H (the missing minimal transversals). Each visit adds one such element to H, reducing |Tr(H) \ H|. Need to show |Tr(H) \ H| eventually hits 0 (H = Tr(H)) and the process doesn't oscillate. This is a combinatorial game on a finite state space for a fixed prime set.

- **Candidate technique(s):** Intersecting antichain theory; blocking/transversal duality for hypergraphs; the monovariant f(H) = Σ 2^{-|Q|}; Chinese Remainder Theorem for the periodic valid set; Dirichlet / density arguments for eventual smoothness of greedy terms.

- **Cheap-kill candidates:**
  - **Case 1 (prime power enters):** Trivial. If a_n = p^e, then every a_m is divisible by p (past and future), so T=1, L=p immediately. This case is already fully proved.
  - **Backward extension:** NOT a hard step — it's immediate from gcd conditions (see below). The round-1 claim that it "needs rigor" is correct, but the rigor is one short paragraph.
  - **K_k^2 claim:** Do NOT attempt. Computationally false for a1=35 and a1=105.

- **Knowledge-base entries to use:**
  - **Modular arithmetic, CRT:** The valid set V = {m : P(m) transverses H} is periodic with period L = product(support(H)). V is a union of residue classes mod L. Covered under "Modular arithmetic, CRT."
  - **Divisor analysis / gcd structure:** The intersecting property of H elements follows from gcd > 1 pairwise. The backward extension follows from this. Covered under "Divisor analysis."
  - **Dirichlet's theorem:** If needed to argue that certain prime-smooth residue classes contain elements of the sequence.

- **Analogous past problems (cruxes):** None found from the crux corpus that directly match. The self-blocking antichain structure is specific to this problem.

- **Prior progress:**
  - Status: partial.
  - Best approach: two-of-k-structure (CHANGES REQUESTED). Core structure (antichain stabilization → periodic valid set → shift-periodicity) is sound. The false K_k^2 claim is not needed.
  - Dead approach: backbone-periodicity (RETHINK) — used backbone primes only, wrong period.

- **Dead ends (do not retry):**
  - K_k^2 claim (H = all 2-element subsets): FALSE. Counterexample a1=35 gives H = {{5,7},{2,5},{2,3,7},{3,5}} with the 3-element set {2,3,7}. Counterexample a1=105 gives H = {{3,5,7},{2,3},{2,7},{2,5}} with the 3-element set {3,5,7}.
  - backbone-periodicity (L = product of primes in P(a_1) only): FALSE period. For a1=15, L=15 is wrong; correct L=30 because prime 2 enters.

- **Small-case / intuition notes (all computational conjectures, not proofs):**

  **Structural fact 1 (PROVED — the backward extension):** Every a_n lies in V (the valid set for the stable antichain H). Proof: H consists of minimal elements of {P(a_j) : j ≤ N}. For any a_n and any Q ∈ H, Q = P(a_j) for some j, and gcd(a_n, a_j) > 1 so P(a_n) ∩ Q ≠ ∅. Hence P(a_n) transverses H. So a_n ∈ V. This is rigorous and avoids any K_k^2 assumption.

  **Structural fact 2 (PROVED — the frozen-antichain property):** Let H* be a self-blocking antichain (H* = Tr(H*)). Then for any transversal P of H*, there exists Q ∈ H* with Q ⊆ P. Proof: every element of H* is a minimal transversal of H* (since H* = Tr(H*)). If P transverses H* but contains no Q ∈ H*, then every proper subset T of P that transverses H* witnesses that P ∉ Tr(H*). But P must contain some minimal transversal = some Q ∈ H*. Contradiction. Therefore P contains Q ∈ H*. CONSEQUENCE: once H = H* (self-blocking), any future term a_{n+1} has P(a_{n+1}) ⊇ Q for some Q ∈ H*. So P(a_{n+1}) is dominated — it does NOT add a new element to H. H stays frozen forever.

  **Structural fact 3 (PROVED — P(r) ⊆ P(r+kL)):** For L = product(support(H*)) and any r ≥ 1, every prime p dividing r also divides r + kL (since p | r and p | L implies p | r+kL). Thus P(r) ⊆ P(r+kL). CONSEQUENCE: once in the periodic regime (a_n = r + kL), the prime set only GROWS beyond P(r), never introduces new "fresh" primes from H's perspective. H stays frozen.

  **Structural fact 4 (CONJECTURE — H is always eventually self-blocking):** Verified computationally for a1 ∈ {6,10,14,15,21,30,35,42,70,77,91,105,143,210,1001}. The function f(H) = Σ_{Q∈H} 2^{-|Q|} is NON-DECREASING: when an element Q is replaced by P ⊊ Q (Case 2), Δf = 2^{-|P|} - 2^{-|Q|} ≥ 0. When a new incomparable P is added (Case 3), Δf = 2^{-|P|} > 0. So f only increases. And f is bounded: for every verified stable self-blocking H, f ≤ 1. The MAIN GAP is proving that f(H) reaches its limit in FINITE steps (i.e., the number of H-changing steps is finite).

  **Key observation on support(H):** support(H) is NOT monotone — it can shrink. For a1=105: support grew from {3,5,7} to {2,3,5,7,11,13} (via intermediate terms 110=2·5·11 and 130=2·5·13), then SHRANK back to {2,3,5,7} at step 16 when a_{16}=160=2^5·5 entered with P={2,5}, replacing {2,5,11} and {2,5,13} in H. The stable period L = product({2,3,5,7}) = 210, not product of all primes ever seen.

  **Critical gap for the proof — H stabilization:** The most promising argument: the monovariant f(H) is non-decreasing, bounded, and increases by a discrete amount at each H-changing step. The bound comes from: for a self-blocking intersecting antichain H on prime set S, f(H) ≤ 1 (empirically verified; likely provable via Bollobás-type inequality for self-blocking families). The discrete increase lower bound: each H-changing step where H gains a new incomparable element increases f by at least 2^{-k} where k = max element size of H. If k is bounded (which holds once H contains a 2-element set, which the sequence always generates eventually since the greedy picks 2-prime-factor numbers), then the number of steps is at most 1/(2^{-k}) = 2^k, which is finite.

  **Specific route for H stabilization:** Once any 2-element set {p,q} enters H, any valid m must be divisible by p or q. The min-size elements of H are 2-element sets, and they make future constraints tight. The 2-element sets enter H whenever the greedy picks a product of exactly 2 primes (like 2p for any prime p). These appear with positive density in any arithmetic progression (by Dirichlet). So within O(L) steps, the greedy visits a term with a 2-element prime set, adding it to H. Eventually enough 2-element sets accumulate that H = Tr(H).

  **The overall proof outline (once H stabilization is established):**
  1. If a prime power enters: T=1, L=p. (Proved, trivial.)
  2. Otherwise: H_n stabilizes to self-blocking H* at step N.
  3. V = {m : P(m) transverses H*} is L-periodic with L = product(support(H*)), T = |valid residues mod L|.
  4. All a_n ∈ V for all n (Structural fact 1 above — trivial from gcd conditions).
  5. Greedy on L-periodic set V cycles through valid residues: a_{n+T} = a_n + L for all n.
  
  Steps 3, 4, 5 are clean once N exists. Step 2 is the main gap.
