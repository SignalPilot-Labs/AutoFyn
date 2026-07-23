p-position-small-prime-classification — APPROVE
- This is a complete end-to-end route. The P-position recursion identifies exactly the greedy sequence, the stripping/descent argument proves the load-bearing small-common-prime theorem, signature invariance follows, and periodicity of the ordered set yields the required indexed identity from n=1.
- Builder checks required: in Step 4 split explicitly into (i) no large prime, (ii) a large prime with least exponent 0, and (iii) positive least exponent, proving in the last case x<pA<=sA<sq<=b (with the appropriate strict/non-strict inequalities). In Step 5 state why x is bad from the legal move b'->x and why the new good pair (b*,b) has no common small prime and has larger member strictly below b'. In Step 8 define the half-open integer blocks precisely and prove the order-preserving translation shifts the enumeration by exactly T places.

cnf-minimal-transversals — RETHINK
- Step 4 is the entire finite-support theorem, but its proposed mechanism does not follow. A private-witness clause for a large prime q only says the other factors of one transversal miss that row; prime stripping that row does not produce a replacement prime that hits every other clause formerly hit by q, nor does the bounded-gap estimate imply divisibility domination of the modified transversal. Thus Step 5 has no foundation.
- Step 6 also acknowledges only tail stabilization and provides no mechanism to obtain the exact identity for every n. This cannot be handed to a builder until an actual essential-prime elimination identity/descent is supplied.

finite-window-forgetting — RETHINK
- Steps 2-3 merely conjecture bounded memory. Bounded gaps do not stop arbitrarily old selected terms with new large prime factors from remaining essential, and the claimed descent among A-prime signatures is not defined or proved. Consequently neither a fixed modulus nor a finite deterministic state exists yet.
- Even granting finite state, Step 5 gives eventual periodicity only; “determinism backward” is invalid for a non-injective transition map and does not remove a transient. Both missing claims are load-bearing, so this is not buildable.

translation-equivariant-greedy-set — CHANGES REQUESTED
- The direct greedy route can work, but Step 3 as written is too vague and its stated “blocker forced coprime to both representatives” is not the precise contradiction. Builder must formulate the minimal-counterexample argument explicitly: choose similar a (rejected) and b (accepted) minimizing max(a,b); obtain an accepted r<a coprime to a; strip r to r'<=r with the same small signature and only small prime factors; minimality applied to the similar pair (r',r) makes r' accepted; then accepted r' and b share a prime p, which is small, so p divides r and a by the two signature equalities, contradicting gcd(a,r)=1.
- All strict inequalities needed for minimality must be stated, including r<a<=max(a,b), and the r'=r case. Once repaired, Steps 4-5 give exact periodicity from A.
- This is not genuinely far from the first approach: both prove the same small-prime-signature classification by the same stripping/minimality core, differing mainly in game language. It is retained as a viable alternate exposition but should not consume a second build slot this round.

Ranking rationale: p-position-small-prime-classification beats translation-equivariant-greedy-set because its small-witness mechanism is fully specified and directly matches the valid descent, whereas the direct exchange theorem needs correction. The other two candidates were not registered because their central lemmas are conjectural rather than mechanisms.

build set: p-position-small-prime-classification