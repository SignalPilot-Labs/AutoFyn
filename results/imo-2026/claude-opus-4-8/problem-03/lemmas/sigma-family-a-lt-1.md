# Lemma F_a (σ-parametrized descent-closed parametric family, `a < 1` top cut of G-INC-2nt)

**Status:** CERTIFIED (round 11 proof-reviewer). Reviewer independently re-derived (ii)
`A(F_k)=A(G_{k-1})+(-1)^k a` and every case of the strong `k→k-2` induction step (h=0, h≥4, h=2 with
2a/2b-i/2b-ii; arithmetic `2+2b-σ`, `σ+2a_v`; used `A(Q_lo)=measure(S_{Q_lo})≤measure(S_{F_{k-2}})=A(F_{k-2})`
for 2a, IH `F_a(k-2)` for 2b). Descent-closedness confirmed structural: for `a<1` the parts `≥2^{k-2}`
are exactly `{2^{k-1},2^{k-2}}`, `h=2` at every level, so the R10 O1 parity break cannot fire (distinct
from the refuted abstract `{Claim_R,T_R}` class). Numerically verified 0-violation: family bound over the
`k=2,3,4` grid AND the top-level G-INC-2nt `a<1` closure over 124 configs (`n=3,4`, `a∈{1/3,2/3}`).

## Definitions
For a finite multiset `P` sorted `p₁ ≥ p₂ ≥ …`, `A(P) = Σ_i (−1)^{i+1} p_i = measure(S_P)` where
`S_P = {x ≥ 0 : #{parts > x} odd}` (certified `alt-sum-integral`). `G_{k−1} = {2^0,…,2^{k−1}}`
(`k` parts, `ΣG_{k−1} = 2^k − 1`). Fix `a ∈ (0,1)` and put

  `F_k := {a} ∪ G_{k−1} = {a, 1, 2, 4, …, 2^{k−1}}`   (`k+1` parts, `ΣF_k = 2^k − 1 + a`).

Depends on certified `gen-decomp-refined`, `parity-condition-inc`, `forcing-inc-reduction`,
`set-identity-selfsimilar` (`A(G_j) ≥ 1`), `alt-sum-integral`.

## Structural facts
- **(i) Descent (`k ≥ 3`).** The parts of `F_k` that are `≥ 2^{k−2}` are exactly `{2^{k−1}, 2^{k−2}}`
  (as `a < 1 ≤ 2^{k−3} < 2^{k−2}`), so `h_{F_k} = 2` (even), and Gen-Decomp's low part is
  `{parts < 2^{k−2}} = {a} ∪ G_{k−3} = F_{k−2}`. The family is closed under `k → k−2`.
- **(ii) `A(F_k) = A(G_{k−1}) + (−1)^k a`,** hence `A(F_j) ≥ 1+a` for all `j ≥ 2` (`j` even:
  `A(G_{j−1})+a ≥ 1+a`; `j` odd `≥ 3`: `A(G_{j−1})−a ≥ 3−a ≥ 1+a`). Proof: `S_{F_k}` differs from
  `S_{G_{k−1}}` only on `[0,1)`, where `N_{F_k} = k+1` on `[0,a)`, `= k` on `[a,1)`, vs
  `N_{G_{k−1}} = k` on `[0,1)`; comparing the two by parity of `k` gives the `±a`.

## Statement (Family Lemma F_a)
For every `k ≥ 1` and every finite multiset `Q` with `S_Q ⊆ S_{F_k}`, `|Q| ≤ k`, and
`σ := ΣQ − ΣF_k ∈ (0,2)`:
`A(F_k) − A(Q) ≥ min(σ, 2−σ)`.

## Proof (strong induction on `k`, descending `k → k−2`)
**Bases.** `k=1`: `S_{F_1} = [a,1)`; a valid `Q` (`|Q| ≤ 1`, `ΣQ ∈ (1+a,3+a)`) is a single part `> 1`
with `S_Q = [0,ΣQ) ⊄ [a,1)` — none exists, vacuously true. `k=2`: `S_{F_2} = [0,a) ∪ [1,2)`,
`A(F_2)=1+a`; the only valid `Q` are (α) `p₁=p₂` (`A(Q)=0`, gap `1+a ≥ 1 ≥ min`), (β) two parts in
`[1,2]` with `A(Q)=p₁−p₂`, giving `A(F_2)−A(Q) = 1+a−2p₁+ΣQ ≥ 2a+σ ≥ min(σ,2−σ)` (as `p₁ ≤ 2`,
`ΣQ = 3+a+σ`).

**Step `k ≥ 3`.** `h := #{Q-parts ≥ 2^{k−2}}` even (Gen-Decomp (i)). For `h=2` write `q₁ ≥ q₂ ≥ 2^{k−2}`;
Forcing gives `q₁ ≤ 2^{k−1}`; with `a_v := 2^{k−1}−q₁ ≥ 0`, `b := q₂−2^{k−2} ≥ 0`, and
`S_{F_k} ∩ I_{k−1} = I_{k−1}` (full band), one gets `deficit_top = 2^{k−2} − (q₁−q₂) = a_v + b` and
`σ_lo := ΣQ_lo − ΣF_{k−2} = σ + a_v − b` (using `ΣF_k − ΣF_{k−2} = 3·2^{k−2}`); `|Q_lo| ≤ k−2`,
`S_{Q_lo} ⊆ S_{F_{k−2}}`.

- `h ≥ 4` (only `k ≥ 4`): `ΣQ_lo ≤ σ+a−1`, `A(Q_lo) ≤ ΣQ_lo`, so
  `A(F_k)−A(Q) ≥ A(F_{k−2}) − (σ+a−1) ≥ (1+a) − σ − a + 1 = 2−σ ≥ min` (by (ii)).
- `h = 0`: `deficit_top = 2^{k−2} ≥ 2 > 1 ≥ min`.
- `h = 2`, `deficit_top = a_v+b`, `σ_lo = σ+a_v−b`:
  * 2a (`a_v+b ≥ min(σ,2−σ)`): `A(F_k)−A(Q) ≥ a_v+b ≥ min`.
  * 2b (`a_v+b < min ≤ 1`): then `a_v,b < 1` and `σ_lo ∈ (0,2)` (bounded as `σ ≤ 1 ⟹ σ_lo < 2σ ≤ 2`,
    `σ > 1 ⟹ σ_lo < σ+(2−σ)=2`; and `σ_lo > 0` both ways); IH `F_a(k−2)` gives
    `A(F_{k−2})−A(Q_lo) ≥ min(σ_lo,2−σ_lo)`.
    - 2b-i (`σ_lo ≥ 1`): `≥ (a_v+b)+(2−σ_lo) = 2+2b−σ ≥ min(σ,2−σ)`.
    - 2b-ii (`σ_lo < 1`): `≥ (a_v+b)+σ_lo = σ+2a_v ≥ min(σ,2−σ)`.
  (At `k=3`, `k−2=1` is the vacuous base, so case 2b is empty; `h=0` and 2a settle `k=3`.)

Every case gives `A(F_k)−A(Q) ≥ min(σ,2−σ)`; descent grounds on `k ∈ {1,2}`. ∎

## Application (closes G-INC-2nt for `a < 1`, all `n`)
For `R = G_{n−1}` with `2^{n−1} → {a, 2^{n−1}−a}`, `a < 1`, `ΣQ = 2^n`, `S_Q ⊆ S_R`, `|Q| ≤ n`: `h_R = 2`,
one Gen-Decomp step gives `R_lo = F_{n−2}`, `σ = ΣQ − ΣR = 1`, `σ_lo = 1 + a_v − b`. The cases `h=0`
(`deficit_top = 2^{n−2}−a ≥ 1` for `a ≤ 2^{n−2}−1`), `h≥4` (`A(F_{n−2}) ≥ 1`), and `h=2`
(2a/2b-i/2b-ii, invoking `F_a(n−2)` at `σ_lo`) each yield `A(R) − A(Q) ≥ 1`. Hence the INC branch of
Lemma LL holds for every `a < 1` top cut of `G_{n−1}`, all `n ≥ 3`.

## Scope
Closes ONLY the `a < 1` top-cut sub-branch of G-INC-2nt, plus (via the full top band) the lower-band cut
G-INC-2lb when the cut value `< 1`. The `a ≥ 1` cut is NOT covered: there the family loses descent
closure (the count `#{F_lo-parts ≥ 2^{k−4}}` can go odd once `a ≥ 2^{k−4}`, i.e. O1 fires for this
family), so a different (direct `A(R)`) argument is required. G-INC-2e⁺ and G-GAP are untouched.
