# Lemma L4 — Min-pairing / balanced-mass identity

**Status:** CERTIFIED (proof-reviewer, round 2). Numerically verified: 0/400 mismatches.
(The writeup in `alternating-sum-potential.md` proved it via an uncrossing argument, which is
standard but sketched; the airtight proof below via L3-parity is what is certified.)

**Statement.** For sorted y_1 ≥ … ≥ y_m ≥ 0, over all partitions of the indices into pairs and
singletons, define cost = Σ_{pairs {i,j}} |y_i − y_j| + Σ_{singletons {i}} y_i. Then
S(y) := Σ_i (−1)^{i+1} y_i = min cost, attained by the consecutive pairing
(y_1,y_2),(y_3,y_4),…. Equivalently, if Σ y_i = 1 then S = 1 − 2β, where
β := max over pairings of Σ_{pairs} min(y_i, y_j).

**Proof.**
(≤) The consecutive pairing has cost (y_1−y_2)+(y_3−y_4)+… (+ y_m if m odd) = S, so min ≤ S.

(≥) Fix any pairing. By layer-cake, |y_i − y_j| = ∫_0^∞ 1[exactly one of y_i,y_j ≥ t] dt and
y_i = ∫ 1[y_i ≥ t] dt, so cost = ∫_0^∞ c(t) dt where
c(t) = #{pairs with exactly one endpoint ≥ t} + #{singletons ≥ t}.
Compare with N(t) = #{elements ≥ t}: a pair contributes (both≥t: 0 to c, 2 to N), (one≥t: 1,1),
(none: 0,0) — always equal parity contributions; a singleton contributes (1,1). Hence
c(t) ≡ N(t) (mod 2) for every t. When N(t) is odd, c(t) is odd, so c(t) ≥ 1. Therefore
cost = ∫ c(t) dt ≥ ∫ 1[N(t) odd] dt = S (by L3). So every pairing has cost ≥ S, giving
min = S.

Finally, writing each pair as (u ≥ v) and singleton as ℓ, cost = Σ(u−v) + Σℓ = (Σ all) − 2Σv.
With Σ all = 1, cost = 1 − 2Σv; minimizing cost maximizes Σv = Σ min(y_i,y_j), so S = 1 − 2β. ∎

**Witness principle.** For any refinement P XY produces and any pairing of P, S(P) ≤ cost of that
pairing = 1 − 2·(mass of the smaller elements of the pairs). So the upper bound S ≤ 1/D_n follows
from exhibiting ≤ n cuts and one pairing with β ≥ (2^n − 1)/D_n.

Depends on: L3.
