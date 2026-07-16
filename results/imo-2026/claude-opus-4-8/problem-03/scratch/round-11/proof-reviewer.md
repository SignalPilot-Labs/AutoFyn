# Proof-reviewer report — imo-2026-03, Round 11

Three approaches built, reviewed independently. All three are honest partials with real,
reviewer-verified progress (including two correctly-scoped negative results). No overclaim found; every
recorded Status matches reality. Problem remains **partial** overall.

Joint cut budget (`#Q-cuts + #R-cuts ≤ n`) enforced in every numeric check below.

---

## 1. geometric-selfsimilar (UPPER BOUND)
**Verdict: CHANGES REQUESTED. Status: partial (matches builder).**
Scores — Correctness 10/10, Completeness 6/10 (m≥5 hard case open), Progress 8/10.

**Lemma MK (`μ(X,|X|−1) ≤ min(X)`) — CERTIFIED.** Re-derived the induction from scratch: base k=1
(`A({p₁})=p₁=min`), base k=2 (midpoint-halve `p₁` → invisible equal pair → `A=p₂=min`), step (halve `p₁`
into an invisible pair, then MK on `{p₂,…,p_k}` with budget `k−2`; parity-invisibility keeps `A` at every
`x` since an equal pair adds an even count → `A(final)=A(play on tail)≤min(tail)=p_k`). Budget
`1+(k−2)=k−1` exact, cuts interior/distinct. Airtight. Corollary MK.1 (δ≤t, or some `d_j≤t`) re-checked:
both give `μ(X,m−1)≤t` at tight budget, uniform in m. Numeric: 0 violations / 4000.

**Reduction is complete.** Given `p₁≤Σ/2`, trichotomy `(δ≤t) ∨ (∃d_j≤t) ∨ (all d_j>t ∧ δ>t)` is
exhaustive; (a) `p₁>Σ/2` closed by Case A.A-at-threshold (re-derived: `A=2q₁−Σ<2·2^{m−1}t−(2^m−1)t=t`,
0 viol m=3,4,5), (b) closed by MK.1, (c) the pure hard case (closed m≤4 via T4, open m≥5). So the entire
remaining UB is exactly case (c) — genuinely all easy cases closed for all m.

**Negative result — CORRECT (not a builder error).** The threshold-invariant induction with invariant
`{(I'),(II'),(III')}` is refuted: after the universal `p₁@p₂` move the subproblem `Y'={d₁,p₃,…,p_m}` does
not inherit `(2')`. Witness `X={8,4,3,2,1}, t=18/31, Y'={4,3,2,1}` — I verified neither escape holds yet
`μ({4,3,2,1},3)=0` (`{4,3,2,1}→{2,2,2,2,1,1}`, `A=0`, 2 cuts ≤ 3). (II') inheritance is the false step;
(III') Σ′-size is fine. Correctly scoped: kills the naive route, not the UB.

**Gap (open):** case (c) for m≥5. The m=4 T4 structure is the template; needs a weaker-recursable
invariant or a direct hard-case strategy.

---

## 2. ll-inclusion-gap (LOWER BOUND)
**Verdict: CHANGES REQUESTED. Status: partial (matches builder).**
Scores — Correctness 10/10, Completeness 6/10 (a≥1 residual open), Progress 8/10.

**Family Lemma F_a — CERTIFIED.** Closes the `a<1` top-cut sub-branch of G-INC-2nt for ALL n. The
σ-reference fix is correct: parametrizing by `σ:=ΣQ−ΣX` (excess over the object's own sum) makes the top
cut and `F_k={a}∪G_{k−1}` obey the identical recursion. I independently re-derived:
- (ii) `A(F_k)=A(G_{k−1})+(−1)^k a` (S-sets differ only on `[0,a)`), hence `A(F_j)≥1+a`, j≥2.
- Every induction case (strong `k→k−2`): h=0 (`deficit_top=2^{k−2}≥2`), h≥4 (`ΣQ_lo≤σ+a−1`,
  `A(Q_lo)≤ΣQ_lo` → `≥2−σ`), h=2 with 2a (`deficit_top≥min` and `A(Q_lo)=measure(S_{Q_lo})≤A(F_{k−2})`
  from S-containment), 2b-i (`2+2b−σ≥2−σ`), 2b-ii (`σ+2a_v≥σ`). Arithmetic matches the certified
  `t-ell-mutual-induction`; bases k=1 (vacuous), k=2 (full casework) hold. No circularity (step uses only
  the certified Gen-Decomp identity + IH at k−2).
- **Descent-closedness confirmed structural (the load-bearing worry):** for `a<1` the parts `≥2^{k−2}` are
  exactly `{2^{k−1},2^{k−2}}`, so `h=2` at every level and `F_k→F_{k−2}` stays in the family — the R10 O1
  parity break provably cannot fire. This IS a specific descent-closed family, NOT the refuted abstract
  `{Claim_R,T_R}` class (the O1 witness `{1,2,2,2,8,16,32}` and Claim-false `{1,3,3}` are not in it).

Numeric: 0 violations on the family bound (k=2,3,4 grid) AND on the top-level G-INC-2nt `a<1` closure
(124 configs, n=3,4, budget + `S_Q⊆S_R` enforced).

**Gap (open, honestly flagged):** G-INC-2nt `a≥1` (family loses descent-closure once `a≥2^{k−4}` — count
goes odd; needs a direct `A(R)` evaluation), G-INC-2lb terminal cut `≥1`, G-INC-2e⁺ (m≥6), G-GAP.

---

## 3. ll-dyadic-symdiff (LOWER BOUND)
**Verdict: CHANGES REQUESTED. Status: partial (matches builder).**
Scores — Correctness 10/10, Completeness 5/10 (crux open), Progress 7/10 (correction + reduction).

**Negative correction — CORRECT, and the counterexample is within budget.** The outline's
"INC forces `max(Q)≤max(R)`" is FALSE. Checked `Q={15/2,15/2,1}, R={7,4,2,1,1}` (n=4): `ΣQ=16=2⁴`,
`ΣR=15=2⁴−1`, `S_Q=[0,1)⊆[0,2)∪[4,7)=S_R` (INC holds), yet `max(Q)=15/2>7=max(R)`. **Budget check:** R is
G₃`={1,2,4,8}` with the 8-piece cut `8→7+1`, so `c_R=1` refining cut; `c_Q=|Q|−1=2`; joint
`c_Q+c_R=3≤4=n` — legitimate, not a spurious over-budget config. The cause is even multiplicity of
`max(Q)`. Corrected lemma PROVED (point-parity: if `q=max(Q)>max(R)` with odd multiplicity `m`, then on
`(max(r,q⁻),q)`, `N_Q=m` odd, `N_R=0`, contradicting INC). So the `(r−q)`-slack identity collapses.

**Level-charge reduction — rigorous.** Re-derived: `A(Q∪R)=measure{g odd}` (`g=N_Q−N_R`, `∫g=1`); for
`max|g|≤2`, `A=A_++A_-`, `∫g=(A_+−A_-)+2(B_+−B_-)=1` ⟹ `A(Q∪R)=1+2(A_-+B_-−B_+)`, hence
`A≥1 ⟺ B_+≤A_-+B_-`. Verified on the counterexample: `A_-=1,B_-=1,B_+=1/2 ⟹ A=1+2(3/2)=4` ✓. D1-direct
(all-n `max|g|≤1` slice) unaffected and correct.

**Gap (open, honestly the crux):** `B_+≤A_-+B_-` (g=+2 excess dominated by g<0 mass) — not implied by
`∫g=1` alone; needs a wide-support argument from `ΣQ=2^n`; plus the `max|g|≥3` extension.

---

## Certifications this round
- `lemmas/MK.md` — CERTIFIED.
- `lemmas/sigma-family-a-lt-1.md` (Family Lemma F_a) — CERTIFIED.
- ll-dyadic's corrected INC top-order lemma and level-charge reduction: both verified rigorous (in the
  approach file, no separate lemma file); recorded in current.md.

## Overall
Status unchanged: **partial**. Answer `c(n)=2^n/(2^{n+1}−1)` still conjectured-and-verified-small-n.
UB = only the m≥5 hard case (c) of (T). LB = G-INC-2nt `a≥1` direct bound + the dyadic `B_+≤A_-+B_-`
crux. No false proof was built; all three verdicts are CHANGES REQUESTED.
