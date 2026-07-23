## Status
partial

## Approaches tried
- finite-state-bijection (this file): treat the tail of the sequence as the orbit of a deterministic map on a FINITE state space (residues mod M in the admissible set), show the successor map is a cyclic bijection (reversible ⇒ pure cycle, no transient), and upgrade to "for all n" via reversibility rather than via re-deriving the greedy identity. **Open gap:** finiteness of the state space M (stabilization) and that the successor depends only on the residue mod M.

## Current best
A dynamical-systems packaging of the finish that makes the "for EVERY n" requirement (pure periodicity from n=1) the structural headline, via reversibility of the successor map — the crux most emphasized by the gap-bounded explorer.

---

### Framing (distinct: finite-state machine + reversibility)
Analogy: aimo-0514 (a reversible deterministic process has a state graph that is a union of cycles ⇒ orbits are PURELY periodic, never merely eventually periodic). We cast the problem so the "for all n" clause is exactly this reversibility phenomenon.

Notation: S_i=supp(a_i); admissible set A_n={m : supp(m) hits S_i ∀i≤n}, periodic mod M_n; a_{n+1}=min(A_n∩(a_n,∞)).

### Proved tools (imported)
- **T1 gaps ≤ a_1:** every multiple of a_1 is admissible ⇒ a_{n+1}-a_n ≤ a_1, so a_n ≤ 1+(n-1)a_1.
- **T2 pairwise gcd>1:** gcd(a_i,a_j)>1 for all i≠j ⇒ every term hits every clause.

### Skeleton
1. **(GAP — stabilization / finite state):** the constraint system stabilizes: there is M (product of finitely many "essential" primes) and a fixed residue set A = (A_∞ mod M) with A_n = {m : m mod M ∈ A} for all n ≥ some N. — Finiteness of essential primes (bounded gaps ≤ a_1 keep the greedy inside a bounded local structure; essential primes ≤ maxpf(a_1), verified empirically). This is the SAME crux as the other approaches; here it is imported as the "finite state space" hypothesis.
2. **Every term is a state:** by T2, a_n mod M ∈ A for ALL n ≥ 1 (a_n hits every minimal clause of A). So the sequence lives in the finite state set A from n=1 — there is no transient.
3. **Successor is a well-defined map on states:** define f: A → A by f(r) = the residue mod M of min(A∩(x,∞)) for any x ≡ r. Because A is a union of residue classes mod M, min(A∩(x,∞)) depends only on r (translation-invariance mod M): if x ≡ x' (mod M) then min(A∩(x,∞)) ≡ min(A∩(x',∞)) (mod M). So f is well-defined, and by the greedy identity (a_{n+1}=min(A∩(a_n,∞)) for all n, since a_{n+1}∈A⊆A_n is the min of the larger set A_n) we have (a_{n+1} mod M) = f(a_n mod M) for all n ≥ 1.
4. **f is a bijection (cyclic successor ⇒ reversible):** f sends each residue in A to the next residue of A in cyclic order mod M; the "previous residue of A" map g is a two-sided inverse. Hence f is a permutation of the finite set A, and its functional graph is a disjoint union of cycles. The residue r_1 = a_1 mod M lies on one cycle of length T = (size of that cycle); one full traversal advances the actual value by exactly M (each length-M window contains |A| residues, and one cycle of f covers a residue-block advancing by M per lap). Standard: T | |A| and L=M works; taking T=|A|, L=M covers all cycles simultaneously.
5. **Pure periodicity from n=1:** since a_n mod M is on a cycle of f from the very first term (step 2), the state sequence is purely periodic: (a_{n+T} mod M) = (a_n mod M) for all n ≥ 1, and the value advances by exactly L=M per T steps because gaps sum to M over one residue-cycle. Hence a_{n+T} = a_n + L for every n ≥ 1. ∎

### Key lemmas (claim + mechanism)
- **State map well-defined & = residue successor** — A being a union of residue classes mod M makes "next admissible above x" translation-invariant mod M; the greedy identity a_{n+1}=min(A∩(a_n,∞)) (all n) transports the sequence onto f-orbits.
- **f is a bijection ⇒ pure periodicity (no transient)** — a cyclic-order successor on a finite set is a permutation; permutations have no transient, so periodicity holds from n=1. THIS is the reversibility crux (aimo-0514) that directly yields "for every n."
- **Constant total advance L=M per T steps** — the T residues of one cycle, taken in increasing real order, span exactly one period M; summing gaps gives L=M.

### Open gaps
- Step 1 (stabilization / finite M) — shared crux; import from clique-descent's essential-prime bound or sieve-closure's monovariant once certified.
- Step 4's accounting "one f-cycle advances value by exactly M": needs care because A may split into several cycles of f; the safe fix is to take T = |A| (all residues), L = M, and prove a_{n+|A|} = a_n + M directly from "each length-M window holds exactly |A| admissible values in increasing order" (step 5), sidestepping per-cycle bookkeeping.

### Cases to cover
None separately; prime-power / even a_1 give |A| small (T=1) and are subsumed.

### Watch out for
- The reversibility/bijection argument is only rigorous AFTER M is known finite (step 1); do not claim pure periodicity before stabilization is in hand.
- Distinguish "period of the state sequence mod M" (may be a proper divisor of |A| on one cycle) from the global T; using T=|A|, L=M avoids over-claiming a minimal period.
- Translation-invariance of "next admissible" REQUIRES A to be an exact union of residue classes mod M (needs step 1); it is false for the pre-stabilization A_n if M_n is still growing.
