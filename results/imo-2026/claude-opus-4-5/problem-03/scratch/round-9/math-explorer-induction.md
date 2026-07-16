## imo-2026-03 — Induction Lens

### The "halve P_{n+1} + IH on remainder" strategy

**Main finding: induction works EXACTLY when P_{n+1} ≥ c(n), but FAILS when P_{n+1} < c(n).**

**The working sub-case (P_{n+1} ≥ c(n)):**

XY strategy: (1) halve P_{n+1} with 1 mark; (2) apply the (n-1)-game IH strategy with n-1 remaining marks on {P_1,...,P_n}.

By Pairing Cancellation: LB ≤ P_{n+1}/2 + c(n-1)·(1 - P_{n+1}).

The bound f(x) = x/2 + c(n-1)·(1-x) is DECREASING in x (since c(n-1) > 1/2 for all n). So the maximum is at the smallest value of P_{n+1}.

Key algebraic identity (verified for n = 2,...,7, provable symbolically):
  c(n-1)·(1 - c(n)) = c(n)/2  [because: 2^{n-1}/(2^n-1) · (2^n-1)/(2^{n+1}-1) = 2^{n-1}/(2^{n+1}-1) = c(n)/2]

Therefore f(c(n)) = c(n)/2 + c(n-1)·(1-c(n)) = c(n)/2 + c(n)/2 = c(n) exactly.

Since f is decreasing and P_{n+1} ≥ c(n), we get LB ≤ f(c(n)) = c(n). QED for this sub-case.

The IH applies because {P_1,...,P_n} (scaled to unit length) is achievable with n-1 LB marks, so the (n-1)-game upper bound applies.

**The failing sub-case (P_{n+1} < c(n) and P_1 > L_0):**

When all n+1 pieces are in (L_0, c(n)), both "halve P_{n+1}" and "halve P_1" produce bounds that EXCEED c(n). Specifically:

- f(P_{n+1}) > f(c(n)) = c(n) when P_{n+1} < c(n).
- g(P_1) = P_1/2 + c(n-1)·(1-P_1), at P_1 = L_0: g(L_0) = (2^{n+1}+1)/(2(2^{n+1}-1)) > c(n).

**Concrete counterexample for pure induction:** The equal-piece config P_k = 1/(n+1) for all k satisfies P_{n+1} = 1/(n+1) < c(n) (verified for all n ≥ 1). For this config, "halve P_{n+1}" gives f(1/(n+1)) > c(n) by a gap of roughly c(n-1)/(n+1) - c(n)/2(n+1) > 0.

### What this means structurally

The n → n+1 induction breaks into two clean sub-cases:

**Sub-case 1 (P_{n+1} ≥ c(n)):** Clean inductive proof via halving. For n=5 specifically: if P_6 ≥ 32/63, XY halves P_6 (1 mark) and applies the proved n=4 strategy (4 marks) on {P_1,...,P_5}. LB ≤ c(5). This is RIGOROUS given the n=4 result.

**Sub-case 2 (L_0 < all pieces < c(n)):** Induction does NOT close this. The n=4 Case B proof (S4/S5/S6/BPP) handles a version of this sub-case directly via the Singleton-Pair Formula: XY creates n-1 pairs + 2 singletons with |s_2 - s_1| ≤ L_0. Whether this can be proved by induction (on the number of "bad" differences d_j = P_{j+1} - P_j) or requires a fresh construction is unclear.

### Barrier check

The "Case B Trivial" claim in current.md ("if P_{n+1} ≤ c(n), XY uses 0 marks and LB picks P_{n+1}") is WRONG for n ≥ 2: with 0 XY marks and n+1 pieces, LB picks ceil((n+1)/2) pieces and can exceed c(n) even when the largest piece is < c(n). Example: n=2, P={1/3,1/3,1/3}, LB gets 2/3 > 4/7 with 0 XY marks. This error is in current.md but does NOT affect the n=4 proof (which covers all Case B via S4/S5/S6/BPP without relying on this claim).

### Recommendation for outliner

A clean partial induction IS available: prove Case B for general n in two tiers:
- Tier 1 (P_{n+1} ≥ c(n)): The halve + IH argument above is rigorous.
- Tier 2 (all pieces small): Needs the Singleton-Pair approach independently of induction.

The Tier 1 argument alone closes a non-trivial portion of the Case B gap for all n ≥ 5 using only the proved n=4 result as base.
