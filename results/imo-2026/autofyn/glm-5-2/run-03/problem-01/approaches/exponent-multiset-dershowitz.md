# exponent-multiset-dershowitz

## Status
partial

## Target
Prove both (a) termination with exactly one M>1, and (b) M is choice-independent.

## Technique
A DIFFERENT termination engine from the (Ω,K) lex route: a **Dershowitz–Manna multiset-ordering descent on the prime-exponent vectors** directly exploits the per-prime Euclidean dynamics, with no separation into coprime/non-coprime cases. The (b) and "exactly-one" parts still use the d_p invariant (the only known clean source), but (a)-termination is supplied by the multiset order — a structurally different, more algebraic measure.

KB: "Invariants & monovariants" (line 117), "Divisor analysis / gcd structure" (line 86). The Dershowitz–Manna multiset-extension theorem of a well-founded order is the named tool. Crux analogue: aimo-0258 (positional-integer / multiset-order termination on configurations).

## Setup
Fix an enumeration of all primes p_1, …, p_r that divide at least one initial number (r finite). Encode each board number a_i as its exponent vector **e_i = (v_{p_1}(a_i), …, v_{p_r}(a_i)) ∈ ℕ^r**. Note 1 ↔ zero vector **0**. The whole board is the multiset E = {**e_1**, …, **e_{2026}**} of 2026 vectors in ℕ^r.

Order ℕ^r by the componentwise partial order: **u** ≤ **v** ⇔ u_j ≤ v_j ∀j. This is a well-quasi-order (Dickson's lemma), in particular well-founded as a strict order (no infinite strictly descending chain) when restricted to the divisors of the fixed N_0 = Π_i a_i (so all exponent vectors stay in a finite box [0,E_1]×…×[0,E_r]).

## Skeleton
1. **Per-prime move identity.** Choosing numbers with exponent vectors **u**, **v**, the move replaces them with **u'** = min-cw(**u**,**v**) (componentwise min = v_p(gcd)) and **v'** = |**u** − **v**| (componentwise |u_j − v_j| = v_p(lcm/gcd)). — by v_p(gcd)=min, v_p(lcm/gcd)=max−min=|diff|, componentwise. (Same identity as the direct route.)
2. **Both new vectors ≤ max-cw(u,v) componentwise.** min(**u**,**v**) ≤ **u** and ≤ **v** componentwise, so ≤ max-cw(**u**,**v**); and |**u**−**v**| has each coordinate |u_j−v_j| = max_j − min_j ≤ max_j, so ≤ max-cw(**u**,**v**). — by componentwise arithmetic.
3. **Multiset strictly decreases (when u ≠ v).** The two removed vectors {**u**,**v**}; their max-cw is **M** = max-cw(**u**,**v**) and it equals one of them iff **u** ≤ **v** or **v** ≤ **u**. The two added vectors {**u'**,**v'**} both satisfy ≤ **M** componentwise. When **u** ≠ **v**, at least one coordinate differs, so min-cw(**u**,**v**) is strictly < **M** in that coordinate, hence **u'** < **M** in the componentwise order. Therefore in the Dershowitz–Manna multiset order on (ℕ^r, ≤_cw): {**u**,**v**} >_mul {**u'**,**v'**} strictly (we removed a maximal element **M** and added an element strictly below it; the other added element is ≤ **M**). — by definition of multiset order.
4. **A legal move strictly decreases E (multiset order).** A move is legal iff both chosen numbers are >1 iff there is at least one prime p_j with both exponents >0 iff **u** ≠ **v** as vectors (since if **u**=**v** the two numbers are equal; equality is allowed and is a sub-case). Careful: **u** = **v** means the two numbers are equal; then the move sends (**u**,**u**) → (**u**, **0**) (min=**u**, |diff|=**0**); the multiset {**u**,**u**} >_mul {**u**,**0**} strictly (removed one **u**, added **0** < **u** provided **u** ≠ **0**, i.e. the number >1, which holds). Hence *every legal move* strictly decreases E in the multiset order. — by cases (u≠v / u=v) above, both giving strict decrease.
5. **Termination.** All exponent vectors remain ≤ **E_0** := (v_{p_1}(N_0), …, v_{p_r}(N_0)) (the prime exponents of the initial total product), since the new vectors are ≤ max-cw of two existing vectors, which are themselves ≤ **E_0** by induction. So E lives in the finite multiset space over the finite box [0,**E_0**]. The Dershowitz–Manna multiset extension of the well-founded componentwise order on this finite box is well-founded (finite ⇒ trivially well-founded; or apply the multiset-extension theorem). Hence no infinite descending chain ⇒ every play terminates. — by multiset-order well-foundedness.
6. **Stuck ⟺ ≤1 non-unit.** A move exists iff two entries have exponent vectors ≠ **0**; stuck iff at most one non-zero vector ⇒ at most one number >1. — by legality restated in vectors.
7. **Rule out "all zero" (all ones).** Use the d_p invariant (per-prime gcd of exponents; see perprime-gcd-lexmonovariant steps 2, 6): some initial a_i>1 ⇒ some p_j divides it ⇒ the initial gcd of p_j-exponents d_{p_j} ≥ 1 ⇒ at every reachable state (invariant) the multiset of p_j-exponents has gcd ≥ 1 ⇒ not all p_j-exponents are zero ⇒ some entry has nonzero vector ⇒ at the terminus exactly one non-zero vector remains. — by the d_p invariant (shared sub-lemma; can be imported).
8. **Determine M (gives (b)).** At the terminal state the multiset of p-exponents is {v_p(M), 0,…,0}; its gcd is v_p(M); by invariance equals d_p; so M = ∏_p p^{d_p}, choice-independent. — by the d_p invariant (shared sub-lemma).

## Key lemmas (claim + mechanism)
- The move is (**u**,**v**) → (min-cw(**u**,**v**), |**u**−**v**|) — because v_p(gcd)=min and v_p(lcm/gcd)=|diff|, applied componentwise across all primes simultaneously.
- Both new vectors ≤ max-cw(**u**,**v**) — because min ≤ max and |u_j−v_j| ≤ max(u_j,v_j) coordinatewise.
- {**u**,**v**} >_mul {min,**diff**} strictly for every legal move — because the removed max-cw element strictly dominates at least one added element (the min, in the differing coordinate when u≠v; the zero, when u=v>0).
- Well-foundedness of the multiset order over a finite box — finite set, or the Dershowitz–Manna multiset-extension theorem of a wqo (Dickson).

## Open gaps (builder fills)
- Rigorous write-up of the multiset-order decrease in both sub-cases (**u** ≠ **v** and **u** = **v** ≠ **0**). Verify the multiset-order definition is correctly invoked (the standard Dershowitz–Manna definition: A >_mul B iff A is obtained from B by replacing zero or more elements by finitely many strictly smaller elements, with multiset inclusion of the rest).
- Justify the bounding box [0, **E_0**] rigorously: by induction, every reachable exponent vector is componentwise ≤ **E_0**. (This is the key step that makes the multiset space finite without invoking full Dickson — the box is fixed and finite, so termination is elementary.)
- Import / prove the d_p invariant (steps 7, 8) — either re-derive (per-prime gcd identity) or import from perprime-gcd-lexmonovariant's certified lemma once available.
- Verify well-foundedness claim does not rely on the wqo antichain property (which is about no infinite antichain, not directly about descending chains); the finite bounding box makes it elementary, and this is the cleaner justification.

## Cases to cover
- Legal move sub-cases: **u** ≠ **v** (general) and **u** = **v** ≠ **0** (equal numbers). Both yield strict multiset decrease. The case **u** = **v** = **0** is not a legal move (both numbers 1).

## Watch out for
- Multiset order over ℕ^r componentwise is NOT well-founded on the whole ℕ^r if r ≥ 2 — there ARE infinite descending chains? Actually no: componentwise ≤ on ℕ^r is a wqo ⇒ its multiset extension is wqo ⇒ well-founded. But avoid relying on this heavy theorem; the **finite bounding box** makes termination elementary. Use the box, not Dickson, as the primary argument.
- The min-cw vector could equal max-cw in some coordinates; the strict-decrease proof must locate *at least one* coordinate where min-cw < max-cw (exists when u≠v) — pin that coordinate.
- This route does NOT separate coprime from non-coprime moves; that is its advantage (cleaner case structure) but also means the Ω-difference arithmetic of the direct route is not reused — confirm the multiset argument is self-contained for (a).
- (b) and "exactly one" still depend on d_p; this approach does NOT replace that. Its distinct contribution is the (a) termination engine.
