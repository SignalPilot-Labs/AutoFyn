# Case-B reductions 1 & 2 + Spare-R_n lemma (certified round 4)

Notation: LB's final pieces a_1 ≥ … ≥ a_p (p ≤ n+1, Σ = 1); D = 2^{n+1}−1; c(n) = 2^n/D;
by Lemma R the XY-goal O ≤ c(n) ⟺ A := μ{t : N(t) odd} ≤ 1/D. Case B = all pieces a_i > 1/D.
A is evaluated by Lemma X (XOR of prefix intervals).

## Reduction 1 (halve-all): Case B ⟹ p = n+1 — PROVED
If a Case-B config has p ≤ n pieces, XY halves all p of them (p ≤ n cuts). Each halved piece
gives [0, a_i/2] ⊕ [0, a_i/2] = ∅, so the total XOR is empty and (Lemma X) A = 0 ≤ 1/D, i.e.
O = 1/2 ≤ c(n). Hence the Case-B upper bound is nontrivial only when LB uses all n marks,
producing exactly p = n+1 pieces. ∎

## Reduction 2 (close-pair) — PROVED
Suppose p = n+1 and the minimum consecutive gap d* := min_{1≤k≤p−1}(a_k − a_{k+1}) ≤ 1/D (since
the pieces are sorted, the smallest pairwise difference is a consecutive gap). XY pairs the
consecutive pieces attaining d* — cut the larger a_k at a_{k+1} (1 cut), producing a copy of
a_{k+1} that cancels the intact a_{k+1} in the XOR and leaves residual [0, a_k − a_{k+1}] = [0,d*] —
and halves the other p−2 pieces (p−2 cuts, each → ∅). Total (p−2)+1 = p−1 = n cuts (within budget).
By Lemma X the surviving XOR is [0, d*], so A = d* ≤ 1/D, i.e. O ≤ c(n). ∎

## Spare-R_n lemma (lower bound) — PROVED
For LB's geometric construction (pieces P_j = 2^j/D, R_n the length-2^n/D piece), if XY places no
cut inside R_n (its ≤ n cuts arbitrary elsewhere), then every other final piece is an uncut R_j
(j ≤ n−1, length 2^j/D ≤ 2^{n−1}/D) or a strict sub-piece of some R_j (length < 2^j/D ≤ 2^{n−1}/D),
all < 2^n/D. Hence R_n is the unique largest piece, sits at rank 1, r_1 = 2^n/D, and since every
odd-sum term is nonnegative, O = r_1 + r_3 + … ≥ r_1 = 2^n/D = c(n). ∎

**Consequence (Case-B upper bound residual).** With Case A (Lemma H, a_p ≤ 1/D) and Reductions 1–2,
the Case-B upper bound is open ONLY in the **hard regime**: p = n+1, all pieces > 1/D, AND all
consecutive gaps > 1/D. This regime is nonempty for every n ≥ 2 (e.g. n=3,
a = (5144,2787,1386,683)/10000). The matching-menu strategy is provably insufficient there
(reviewer-verified: menu-optimum A = 683/10000 > 1/15 while a fragment cascade gives 288/10000);
fragment (cascade) cuts are required.

**Machine check (reviewer, round 4).** Reduction 1 (A = 0), Reduction 2 (A = d* exactly), and the
menu-vs-cascade counterexample all verified in exact rational arithmetic.

**Certification.** Reviewer-verified round 4. Statements correct, proofs sorry-free, derived from
certified Lemmas R, X, H. Admitted to shared cache. (Note: these are REDUCTIONS, not a closed
Case-B bound — the hard regime remains open, the field-wide U1 wall.)
