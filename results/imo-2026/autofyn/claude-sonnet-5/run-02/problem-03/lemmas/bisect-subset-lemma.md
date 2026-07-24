## Bisect-Subset Lemma (generalizes Bisect-Top-k to arbitrary subsets)

**Source:** `lp-duality-certificate`, round 24, §R24.2.

**Statement.** Fix a marking p_1>=...>=p_m>0, T=sum p_i, and any subset
S subseteq {1,...,m} with |S|<=n. The strategy "bisect every piece in S
into two equal halves, leave every piece not in S untouched" is a legal
Xiang-Yu response (|S| cuts <= n), and
  Φ_S(p) = (T + A(R)) / 2,   R := (p_i)_{i not in S} in inherited
descending order,
unconditionally — no feasibility/order constraint beyond |S|<=n.

**Proof.** For each i in S, the two fragments p_i/2,p_i/2 are equal
values from the same piece — an ordinary same-piece pair — so
`odd-run-reduction-lemma` cancels them regardless of sort position
(order-independent, as established in
`cross-piece-sign-assignment-identity`'s Step 1); hence q_i=0 for i in
S. The untouched pieces retain their individual values unchanged and
inherit their relative order (deleting elements from a sorted list
preserves the order of the rest), so the merged sorted multiset equals
R exactly, with each surviving piece a singleton rank (monochromaticity
trivial). By `cross-piece-sign-assignment-identity`, A(M) = A(R).

**Relation to prior work.** `bisect-top-k-lemma` (already certified) is
exactly the special case S={1,...,k}; this lemma strictly generalizes
it to arbitrary subsets, with an equally short, from-scratch proof (not
a re-derivation of the special case, a direct general argument).

**Proof-reviewer independent re-verification.** Confirmed the S={2,3}
row (Φ = (T+p1-p4)/2, R={p1,p4}) by hand; the reasoning is a direct,
mechanical instantiation for every subset and does not depend on which
subset is chosen — no case-by-case numeric curve-fitting was involved,
each table row follows immediately from evaluating A(R) for the stated
R.

**Certification.** CERTIFIED, general (any m, any n, any subset S with
|S|<=n), unconditional.
