# Build report — ll-dyadic-symdiff (imo-2026-03), Round 13

Status: **partial** (advance). Target: HS-D1 residual `A(Q∪R) ≥ 1` via the NEW R-cut pairing.

## Proved (rigorous, new this round)
- **Lemma BR (bottom-restriction), general, `max|g|`-agnostic BYPASS.** For any `Q,R` and `τ>0`,
  `A(Q∪R) ≥ measure{x∈[0,τ): g odd}`, `g=N_Q−N_R`. With `τ=min(Q)`, since `N_Q≡|Q|` there,
  `A(Q∪R) ≥ B := measure{x∈[0,min(Q)): N_R(x) ≢ |Q| mod 2}`. One-line proof (measure monotonicity).
  Routes through NEITHER the alternating-tail crux NOR Sub-3a NOR any `max|g|≤2` hypothesis — a genuine
  bypass as required. Proposed as promotable.
- **Q-top reduction eliminates `Q` from the crux.** For *Q-top* configs (`min(Q) ≥ 2^{n−2}`, i.e. all
  `Q`-parts in the top level): proved `|Q|∈{3,4}`, and via the within-bottom parity identity
  `𝟙[N_R≢|Q|]=𝟙[N_R odd]/𝟙[N_R even]`, got `B = A_R^{bot}` (|Q|=4) or `2^{n−2}−A_R^{bot}` (|Q|=3), where
  `A_R^{bot}=measure{x∈[0,2^{n−2}):N_R odd}`. Hence for Q-top, `A(Q∪R) ≥ 1` reduces to the **R-only**
  inequality (★R): `|Q|=4 ⟹ A_R^{bot}≥1`; `|Q|=3 ⟹ A_R^{bot}≤2^{n−2}−1`. This is the FAITHFUL
  generalization of the explorer's n=3 identity `A = b+(1−b)+(q2−q1)+(4−q3)`: the `b+(1−b)=1` is exactly
  `A_R^{bot}=1` on `[0,2)`, and the Q-terms are the top-window odd-`g` mass that BR discards.

## Verified (exact Fractions, off-grid, 0 violations)
- (★R) both branches at n=3,4,5: `|Q|=4 ⟹ minA_R^{bot}=1`; `|Q|=3 ⟹ maxA_R^{bot}=2^{n−2}−1` (=1,3,7).
  Both tight, attained by unrefined/near-unrefined R.
- Q-top general R (top piece possibly UNCUT), `B≥1` with 0 violations INCLUDING inside the Sub-3a-failing
  residual; min B = 1 at n=3,4,5.

## Honest corrections / caveats (reviewer-relevant)
- The explorer's n=3 template `R={b,2−b,1,4}` has `max(R)=4=2^{n−1}` (top piece UNCUT). It is in the
  residual (Sub-3a fails) but NOT in the narrow "bucket (iii) max(R)<2^{n−1}" set. The single-R-cut
  sub-case (max(R)<2^{n−1}, one cut) always has a FULL odd bottom level ⇒ is SUBSUMED by certified Sub-3a,
  so it is NOT new progress; the genuine residual has top-uncut / multi-fragment R with only partial odd
  levels, handled by the bottom-restriction (partial-level accumulation into `B`).
- n=3 was already closed in R9; the value here is the BR reduction + the Q-free reformulation (★R), not
  the n=3 sub-case.

## Open gaps (honest)
1. Prove (★R) — clean Q-free parity inequalities on a refinement `R` of `G_{n−1}` under `c_R ≤ n−|Q|+1`.
   Verified, tight, but not proved. Handle: cut-adjustment calculus (cut of `2^k` at `f≤2^{k−1}` flips
   `N_R`-parity on `[0,f)` and `[2^k−f,2^k)`) accumulated against the budget.
2. Non-Q-top residual (`min(Q)<2^{n−2}`): the bottom window is shorter than 1 level, so BR alone need not
   reach measure 1 — NOT covered. Needs a longer window or combination with the discarded top-window mass.

## Did NOT revive (per instructions)
Circular `B₊≤A₋+B₋`; budget-parity "R has odd-mult piece"; INC⟹max(Q)≤max(R); mutual induction. Kept
`N_R(x)=#{r>x}` (values). Max|g|-agnostic throughout.

## Spec concerns
None. This closes ONE LB residual slice only (the Q-top part of the bucket-(iii)/LL t≥2 crux); the full LB
also needs the refined-R and non-containment (non-Q-top) pieces — NOT claimed solved.
