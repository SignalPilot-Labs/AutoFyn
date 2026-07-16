## imo-2026-03 (lens: lower-bound general-n residual lemma T(ℓ))

---

### Primary finding: T(ℓ) is closed by the SAME mutual strong induction that closes Claim(n,ε)

**This is the key insight.** The existing two-step strong induction that proved G-INC-1 = Claim(n,0) for n ∈ {1,2,3,4} (Step 12 of ll-inclusion-gap) is a **simultaneous induction on two claims**:

- **Claim(n,ε)**: INC P with |P| ≤ n+1, ΣP = 2^n + ε (ε ∈ [0,1)) ⟹ O_P ≤ O_{G_{n−1}} + ε.
- **T(n)**: INC P with |P| ≤ n+1, ΣP ∈ (2^n − 1, 2^n) ⟹ O_P ≤ O_{G_{n−1}}.

Both Claim(n) and T(n) are needed by the other's inductive step: Claim(n) uses T(n−2) (in sub-case 2b-ii), and T(n) uses Claim(n−2) (in sub-case 2b'-i). The bases Claim(1,·), Claim(2,·), T(1), T(2) are all already proved (Step 11). The inductive step for T(n) **mirrors Claim(n) exactly**, with two structural simplifications:

1. **h ≥ 4 is IMPOSSIBLE in T(n)**: ΣP < 2^n, so h high parts each ≥ 2^{n−2} would give ΣP_hi ≥ 4·2^{n−2} = 2^n > ΣP. Contradiction. So h ∈ {0, 2} only.
2. **The target is 1 + ε' (with ε' ∈ (−1, 0) < 0), which is strictly less than 1** — easier than Claim's target 1 − ε ≥ 0.

Inductive step for T(n), n ≥ 3 (write ε' ∈ (−1, 0) for ΣP = 2^n + ε'):

- **h = 0**: All parts < 2^{n−2}. Then S_P ∩ I_{n−1} = ∅, so δ_top = 0 and deficit_top = 2^{n−2} ≥ 1 > 1 + ε'. Done.
- **h ≥ 4**: Impossible (shown above).
- **h = 2**: Let q1 ≥ q2 be the two high parts. a = 2^{n−1} − q1 ≥ 0, b = q2 − 2^{n−2} ≥ 0, deficit_top = a + b. ε'' := ε' + a − b, ΣP_lo = 2^{n−2} + ε''.
  - **Sub-case 2a'** (a + b ≥ 1 + ε'): deficit_top + M ≥ a + b ≥ 1 + ε'. ✓
  - **Sub-case 2b'** (a + b < 1 + ε', strictly): Then b < 1 + ε' (since a ≥ 0), so ε'' = ε' + a − b > ε' − (1 + ε') = −1. Thus ε'' ∈ (−1, 0) or ε'' ≥ 0.
    - If ε'' ≥ 0: Apply Claim(n−2, ε'') (IH). M ≥ 1 − ε''. deficit_top + M ≥ (a+b) + (1−ε'') = 1 + ε' + 2b ≥ 1 + ε'. ✓
    - If ε'' < 0 (i.e., ε'' ∈ (−1, 0)): Apply T(n−2) (IH). M ≥ 1 + ε''. deficit_top + M ≥ (a+b) + (1+ε'') = 1 + ε' + 2a ≥ 1 + ε'. ✓

**The critical bound** (ε'' > −1 when ε'' < 0): same as in Claim's 2b-ii. In sub-case 2b' with ε'' < 0, we have b < 1 + ε' (strict from 2b' hypothesis and a ≥ 0), so ε'' = ε' + a − b > ε' + 0 − (1 + ε') = −1. This puts ΣP_lo = 2^{n−2} + ε'' ∈ (2^{n−2}−1, 2^{n−2}) strictly inside T(n−2)'s domain.

**Verified**: T(3) (172 INC configs on 1/4 grid, 0 violations, max O_P = 5 = O_{G_2} achieved); T(4) (33 INC configs on 1/2 grid, 0 violations, max O_P = 10 = O_{G_3} achieved). Tight case for T(3): P = {4, 11/4, 1} (sum = 31/4, O_P = 5). It falls in sub-case 2a' (deficit_top = 3/4 = 1 + ε' exactly), so no sub-case 2b' is invoked at the tight boundary.

**Conclusion**: The simultaneous strong induction on n closes both Claim(n, ε) and T(n) for ALL n ≥ 1. G-INC-1 = Claim(n,0) is now proved for all n. The residual T(ℓ) is NOT a separate obstacle — it falls inside the same mutual induction.

---

### Distinct openings

1. **Simultaneous mutual induction (PRIMARY — closes T(ℓ) and G-INC-1 for all n)**: Extend the existing Step 12 proof by adding a "T(n) inductive step" alongside Claim(n), invoking the same pair (Claim(n−2), T(n−2)) as IH. The Claim(n) proof doesn't change at all; T(n) is a parallel proof with the same structure, simpler in h (only 0 or 2 occur) and easier target (1 + ε' < 1 vs 1 − ε). This is clean, rigorous, and verifiably tight. **This is the builder's task for ll-inclusion-gap.**

2. **h=0 write-up for G-INC-1 Step 12 (TRIVIAL, missing write-up)**: The reviewer flagged that h=0 is reachable for n ≥ 5 (e.g., n=5: Q={13/2, 13/2, 6, 6, 4, 3}). The write-up is one line: "h=0 ⟹ all parts < 2^{n−2} ⟹ no S_Q mass in I_{n−1} ⟹ δ_top = 0 ⟹ deficit_top = 2^{n−2} ≥ 1 ≥ 1 − ε. Done." This unblocks the Step 12 gap.

3. **G-INC-2 (refined R, first nontrivial at n=4)**: Numerically 0 violations on integer 1/2-grid for all 5 tested R-refinements at n=4. The proof challenge is that S_R lacks dyadic band structure, so the top-band decomposition must be re-derived from S_R's own level sets. One possible opening: a "refined top-band decomposition" that characterizes S_R's forbidden bands by its own interval structure (analogously to the dyadic case) and then runs the same parity argument. Not attempted yet; the existing approach file records this as open.

4. **Majorization approach for T(ℓ) (alternative, skip if mutual induction works)**: T(ℓ) says O_P ≤ O_{G_{ℓ−1}} for INC P with ΣP ∈ (2^ℓ−1, 2^ℓ). Since A(P) = 2O_P − ΣP, this is equivalent to A(P) ≤ A(G_{ℓ−1}) − 1 − ε' (where ε' = ΣP − 2^ℓ ∈ (−1, 0)). Could be approached via majorization: if the sorted parts of P are dominated by G_{ℓ−1} in a weak majorization sense, the alternating sum inequality follows. However, the mutual induction is cleaner and avoids needing to define a majorization preorder.

5. **Bypass T(ℓ) entirely by a direct Claim(n) proof (only if mutual induction has unfixable gap)**: If sub-case 2b-ii of Claim(n) could be handled without invoking T(n−2), this would eliminate the need for T(ℓ) altogether. One idea: show ΣP_lo ≥ 2^{n−2} always (ruling out ε'' < 0). But this is FALSE: the tight case shows ΣP_lo = 2^{n−2} − 1/4 (ε'' < 0 IS reached). So the bypass doesn't exist; T(ℓ) IS needed.

---

### Candidate technique(s)
- **Mutual two-step strong induction n → n−2** on the pair (Claim(n,ε), T(n)). Same engine as Step 12, same base cases, same case split (h ∈ {0,2} for T vs h ∈ {0,2,≥4} for Claim), same bounds (ε'' > −1 from sub-case 2b' condition).

---

### Cheap-kill candidates
- **h=0 write-up** for Step 12 (G-INC-1): one-line argument, not a gap but a missing sentence. Kill it immediately.
- **T(n)'s h≥4 impossibility**: purely arithmetic (ΣP < 2^n). One line.
- **T(n)'s h=0 trivial case**: deficit_top = 2^{n−2} ≥ 1 > 1 + ε'. One line.

---

### Knowledge-base entries to use
- Two-step strong induction (the existing Step 10–13 machinery from ll-inclusion-gap)
- Certified lemmas: `set-identity-selfsimilar` (SET IDENTITY + self-similar identity, the induction engine), `top-band-decomposition`, `parity-condition-inc`, `forcing-inc-reduction`
- Base cases: Step 11 proofs of Claim(1,·), Claim(2,·), T(1), T(2) — already done, just need to cite them in the T(n) inductive step
- No new KB entries needed; this is pure exploitation of the existing certified machinery

---

### Analogous past problems (cruxes)
- none that map closely — the mutual simultaneous induction on a pair of companion claims is a non-standard olympiad move

---

### Prior progress
- G-INC-1 proved for n ∈ {1,2,3,4} (Steps 10–13); T(1), T(2) proved (Step 11). General n reduces to T(ℓ) ≥ 3. The mutual induction closes T(ℓ) for all ℓ.
- h=0 sub-case of Step 12 (G-INC-1): flagged by reviewer as reachable for n≥5 and unwritten. Trivial.
- G-INC-2: vacuous n=3, numerically verified n=4, proof open.
- G-GAP (alignment branch): open.
- Upper-bound gap (p₁ ≤ Σ/2): open, SB-monotone certified-dead.

---

### Dead ends (do not retry)
- **Direct application of Claim to negative ε**: FALSE (reviewer certified counterexample). T(ℓ) is needed as a separate statement, not a specialization of Claim.
- **ε-free bound O_P ≤ O_{G_{ℓ−1}} without the sum constraint**: FALSE (example P = {7/2,7/2,7/2,2} at ℓ=3 has O_P = 7 > 5 = O_{G_2} but ΣP = 12.5 ∉ (7,8)). The sum constraint in T(ℓ) is essential.
- **"All tight A=1 cases have max(Q) = 2^{n−1}"**: FALSE (deleted in R6; the true tight case Q={3,3,2}, R={2,2,2,1} is Sub-3a, not Sub-3b).
- **Majorization argument without the SET IDENTITY engine**: stalled multiple rounds before the SET IDENTITY was found (R7); don't retry without the certified identities.
- **SB-monotone / partial-shadow chain for upper-bound gap**: CERTIFIED DEAD (sb-obstruction theorem, R7). Do not retry.

---

### Small-case / intuition notes (conjectures unless marked proven)
- **T(3): 0 violations, 172 INC configs, max O_P = 5 = O_{G_2} achieved** at P = {4, 11/4, 1}. [VERIFIED, conjectured tight]
- **T(4): 0 violations, 33 INC configs, max O_P = 10 = O_{G_3} achieved** at P = {8, 9/2, 2, 1}. [VERIFIED]
- **Tight case structure** (conjecture): T(ℓ) is tight (O_P = O_{G_{ℓ−1}}) precisely when P = {2^{ℓ−1}, q, 2^{ℓ−4}?, ...} with the sub-case 2a' at its boundary (a + b = 1 + ε' exactly). The induction hits the tight T(n−2) base at these cases but stays within the ≥ bound.
- **G-INC-2 at n=4**: 0 violations over all 7 integer refinements of G_3, 60−72 INC configs each. [VERIFIED, not proved]
- **Mutual induction dependency chain** (proven): T(3) uses T(1) [proved] + Claim(1) [proved]; T(4) uses T(2) [proved] + Claim(2) [proved]; T(5) uses T(3) [proved by above] + Claim(3) [proved by Step 12]; etc. All T(ℓ) follow by simple strong induction from T(1), T(2).

