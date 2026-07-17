# Outline Review: IMO 2026 P6

## Problem Summary
Greedy sequence with gcd > 1 constraint. Prove eventual shift-periodicity: a_{n+T} = a_n + L.

---

## antichain-stabilization

**Verdict: CHANGES REQUESTED**

The conceptual framework is sound: track minimal prime-sets as an intersecting antichain H, argue H stabilizes to a self-blocking state, then the valid set is periodic.

**Issues:**
1. **Gap A (Prime support bounded):** The outline claims prime support eventually stabilizes but offers no mechanism. The candidate route ("first K terms have bounded values") is circular -- K depends on when primes stabilize, which depends on K. Need: every prime in any a_n must divide some a_i where i <= K_0 for explicit K_0, e.g., show that new primes can only enter via terms not divisible by any existing S-prime, which is impossible after backbone constraint kicks in.

2. **Gap B (Self-blocking achieved):** The mechanism is sketched but incomplete. The claim "greedy can produce a term with P(a_{n+1}) = S" for a non-contained transversal S is not justified -- the greedy picks the *smallest* valid integer, not one whose prime set is exactly S. The smallest valid integer might have prime set strictly containing S.

3. **Gap C:** Step 5 correctly identifies constraint domination but the formal statement needs tightening.

**Fixable if:** Gap A is closed by linking to the backbone constraint (every term divisible by some prime in B = primes(a_1)), and Gap B is closed by proving that when H is not self-blocking, the greedy eventually picks an element adding to |H| (finite process).

---

## backbone-periodicity

**Verdict: APPROVE**

This is the cleanest reduction. By forcing every term to share a prime with a_1, the backbone B = primes(a_1) is fixed from the start. The constraint structure lives entirely over B.

**Strengths:**
- Step 1 (every a_n divisible by some prime in B) is immediate from gcd(a_n, a_1) > 1.
- The "minimal transversal" framing (Step 3-4) is promising: startup types should be minimal transversals of each other, and any later type must contain one of them.
- Periodicity mod L = lcm(B) = product(B) follows cleanly from CRT.

**Issues (minor):**
- Gap 1: The claim "T_i are minimal transversals" needs more care. The greedy picks the smallest *integer*, not the smallest *backbone type*. But the key claim can be rephrased: T_1, ..., T_K form a self-blocking family in the sense that any transversal of {T_1,...,T_K} contains some T_i. This is weaker but sufficient.
- Gap 2: K bounded by 2^|B| is correct (each startup type is a distinct subset, no two comparable in the antichain).
- Gap 3: Extra primes outside B don't create new constraints -- correct, since gcd condition is satisfied by backbone primes.

**Ready to build.** The gaps are well-identified and have clear mechanisms.

---

## clique-valid-set

**Verdict: RETHINK**

**Fatal flaw:** Gap A is not closable with the stated mechanism.

The claim "coprime pairs resolve when the smaller element is visited" is true for any *specific* coprime pair (x, y) with x < y: once a_m = x, the element y is excluded. But the problem is:
- V_0 contains infinitely many elements.
- There are infinitely many coprime pairs in V_0 (e.g., among primes, any two distinct primes are coprime).
- The greedy visits elements in increasing order, so at step n, the smallest unvisited valid element is a_{n+1}.
- The argument needs to show that after some N, *all* remaining elements in V_N are pairwise non-coprime. But why would all coprime pairs have their smaller element visited by step N?

The mechanism conflates "each coprime pair eventually resolves" with "all coprime pairs resolve in finite time." The former is true but doesn't give the latter -- it only gives that for any fixed pair, eventually one is excluded. But there are infinitely many pairs, and we need a uniform bound.

**Why it can't work:** The clique stabilization argument needs a different mechanism -- perhaps via finite prime support (if V_N has finite prime support, then clique structure is automatic). But that's essentially the backbone-periodicity argument.

**Recommendation:** Abandon this approach or merge it into backbone-periodicity.

---

## two-of-k-structure

**Verdict: APPROVE**

This is the most explicit and computationally verified approach. The claim H = K_k^2 (all 2-element subsets of a finite prime set S) gives a completely explicit characterization of the valid set.

**Strengths:**
- Numerical evidence strongly supports the K_k^2 structure.
- The valid set formula (divisible by >= 2 primes from S) is explicit and periodic.
- The T count is computable by inclusion-exclusion.

**Issues:**
- Gap 1 (H is exactly K_k^2): This is the key claim and needs a proof. The heuristic "greedy produces all pairs" is plausible but not rigorous. Need to show: if {p,q} and {p,r} are in H, eventually {q,r} is forced into H by a term divisible by qr but not p. This requires showing such a term is eventually greedy-selected.
- Gap 2 (S finite): This follows from backbone constraint if S is defined as primes(a_1) union primes of early terms. More precisely, S should be the minimal set such that every valid element is divisible by >= 2 elements of S.
- Gap 3 (k=1 case): The degenerate case a_1 = p^j is trivial and handled correctly.

**Key risk:** The K_k^2 characterization might be too strong. The actual antichain H might be a proper subset of K_k^2 in some cases. However, numerical evidence across multiple starting values supports the full K_k^2.

**Ready to build.** This approach has the most concrete target and the clearest path to completion.

---

## Diversity Assessment

The four approaches share a common backbone:
1. Constraints eventually stabilize (finite prime support).
2. Valid set becomes L-periodic for L = lcm of some finite prime set.
3. Greedy on periodic set gives shift-periodicity.

However, they diverge on *which* finite structure captures the constraint stabilization:
- antichain-stabilization: self-blocking intersecting antichain
- backbone-periodicity: minimal transversals over primes(a_1)
- clique-valid-set: clique property of valid set (RETHINK)
- two-of-k-structure: explicit K_k^2 structure

**Assessment:** The top three (excluding clique-valid-set) are sufficiently distinct. backbone-periodicity focuses on the backbone primes, while two-of-k-structure makes a stronger structural claim (K_k^2). antichain-stabilization is more abstract but subsumes the others conceptually.

The field does not suffer from the "single-gap trap" -- the approaches attack different aspects of the problem.

---

## Rankings

| Rank | Slug | Elo | Rationale |
|------|------|-----|-----------|
| 1 | two-of-k-structure | 1546 | Most explicit, computationally verified |
| 2 | backbone-periodicity | 1516 | Cleanest reduction, well-identified gaps |
| 3 | antichain-stabilization | 1484 | Sound framework but gaps harder to close |
| 4 | clique-valid-set | 1454 | Fatal flaw in Gap A |

---

## Final Verdicts

- **antichain-stabilization:** CHANGES REQUESTED (close Gap A and B with explicit mechanisms)
- **backbone-periodicity:** APPROVE
- **clique-valid-set:** RETHINK (fatal flaw: cannot show all coprime pairs resolve in finite time)
- **two-of-k-structure:** APPROVE

---

## Build Set

Build the two strongest approaches in parallel:

**build set: two-of-k-structure, backbone-periodicity**

Rationale: These two have the clearest paths to completion and are sufficiently distinct (K_k^2 structure vs. minimal transversal structure). If both succeed, they may converge to the same proof. If one fails, the other provides a backup.
