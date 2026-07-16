# Lemma LL (t = 1) — single cut of the largest geometric piece

**Status:** certified (proof-reviewer, round 3). Statement re-derived independently and verified
numerically (5000 random Q×R configs, n=2,3,4, with A(R) ≥ 1 enforced: 0 violations).

## Statement
Let n ≥ 1. Let Q = {q, 2^n − q} be a two-part partition of 2^n with q ≤ 2^{n−1}, and let R be any
finite multiset with **A(R) ≥ 1** and **max(R) ≤ 2^{n−1}**. Then

  A(Q ∪ R) ≥ 1,

where A(·) is the alternating sum of the sorted multiset and A(Q ∪ R) = A(Q) + A(R) − 2B is the merge
identity (B = measure{x : N_Q(x) odd and N_R(x) odd}).

(This is the settled t = 1 tail of the geometric lower bound: it is the reduction step used when Xiang Yu
makes exactly one cut inside the largest piece 2^n. The hypotheses A(R) ≥ 1 and max(R) ≤ 2^{n−1} are
supplied by the induction hypothesis on G_{n−1}.)

## Proof
Since q ≤ 2^n − q, we have N_Q(x) = 2 on [0, q), = 1 on [q, 2^n − q), = 0 on [2^n − q, ∞). Hence the
Q-odd region is the single interval S_Q = [q, 2^n − q), of measure A(Q) = 2^n − 2q ≥ 0.

The R-odd region S_R = {x : N_R(x) odd} satisfies S_R ⊆ [0, max(R)) ⊆ [0, 2^{n−1}) (for x ≥ max(R),
N_R(x) = 0). Therefore

  B = measure(S_Q ∩ S_R) ⊆ [q, max(R)),   so   B ≤ (max(R) − q)^+.

- If max(R) ≤ q: B = 0, and A(Q ∪ R) = A(Q) + A(R) ≥ 0 + A(R) ≥ 1.
- If max(R) > q: B ≤ max(R) − q, so
  A(Q ∪ R) = A(Q) + A(R) − 2B ≥ (2^n − 2q) + A(R) − 2(max(R) − q) = 2^n − 2·max(R) + A(R) ≥ A(R) ≥ 1,
  using max(R) ≤ 2^{n−1} ⟹ 2^n − 2·max(R) ≥ 0.

In both cases A(Q ∪ R) ≥ 1. ∎

## Scope note
This closes only the t = 1 tail. The sub-case t ≥ 2 with A(Q) > 0 (Q partitions 2^n into ≥ 3 parts) is
NOT covered by this lemma and remains the open shared gap. There S_Q is a union of two intervals and the
single-interval overlap bound above no longer applies.
