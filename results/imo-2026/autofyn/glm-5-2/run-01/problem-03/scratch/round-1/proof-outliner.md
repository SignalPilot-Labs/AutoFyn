## imo-2026-03
Spec review: required
Technique: Minimax for an alternating-pick cake game. Reduction to an alternating-sum D = a1−a2+a3−… of sorted pieces (greedy-pick lemma); lower bound by explicit geometric construction 1:2:4:…:2^n + inductive bound on D; upper bound by an inductive adaptive "halve or match" XY strategy (or, alternatively, a majorisation/Hall pairing argument showing the geometric config is the worst case).

Skeleton:
  1. Reduce the claim phase: greedy alternating pick is optimal for both, so LB gets odd-position pieces = (1+D)/2, D = alternating sum of sorted-descending pieces. — by the standard "greedy is optimal in alternating item-picking" lemma (exchange/backward-induction).
  2. Reformulate: D = 1 − 2·(XY's even-position take); minimising D = maximising XY's take. In units of 1/S_n, D≥1 ⟺ XY ≤ 2^n−1 ⟺ LB ≥ 2^n. Also D = ∫_0^{a1} 1_{#{pieces≥t} odd} dt. — by algebra / the parity-integral identity.
  3. Lower bound: LB plays geometric config G_n=(1,2,…,2^n) (units 1/S_n). — construction.
  4. Let k = # cuts XY puts on the piece 2^n.
  5. Case A (k=0): b1=2^n is LB's; D = b1 − D_tail ≥ 2^n − 2^{n-1} = 2^{n-1} ≥ 1. — by D=b1−D_tail and D_tail ≤ largest tail piece ≤ 2^{n-1}. (Forces XY to cut 2^n.)
  6. Case B (k≥1): induct on n; the "+1 gap" (2^k = sum(smaller)+1) is preserved, and interleaving a fragment of 2^n into an even rank costs a cut and reduces the rest to the sub-instance G_{n-1}, to which L(n−1) applies. Equality at "full halving". — key lemma LB-B.
  7. Conclude D ≥ 1 = 1/S_n, so LB ≥ 2^n/S_n.
  8. Upper bound: for every ≤(n+1)-piece partition, XY adds ≤n cuts to force D ≤ 1/S_n. Base n=0,1 hand-proved (n=1: halve if L≥2/3 else shave sliver). Inductive step: first cut = halve L if L≥T_n=2^n/S_n, else match L to the second-largest; recurse with n−1 cuts. — key lemma UB-1.
  9. Conclude c(n) = 2^n/(2^{n+1}−1).

Key lemmas (claim + the one-line mechanism that makes it true):
  - LB-A: k=0 ⟹ D≥2^{n-1} — because D=b1−D_tail and D_tail ≤ b2 ≤ 2^{n-1}.
  - LB-B (crux of lower bound): k≥1 cuts on 2^n still give D≥1 — because the "+1 gap" 2^k=(1+…+2^{k-1})+1 is an invariant under refinement: cutting the dominant piece sends both fragments to LB's odd positions unless XY interleaves a fragment into an even rank, which spends a cut and leaves the n−k remaining cuts facing exactly G_{n-1}, where induction forces D≥1; equality at full halving (all consecutive pairs cancel, leaving one unit).
  - UB-1 (crux of upper bound): the halve/match recursion leaves a final unpaired leftover ≤ 1/S_n — because each XY cut creates one canceling equal-consecutive pair (contributing 0 to D), so after n cuts ≤1 active piece remains and that piece IS D; the halve-vs-match choice keeps it ≤ 1/S_n. The rigorous invariant for ARBITRARY configs is the open sub-claim.
  - UB-2 (obstacle, must be resolved): the alternating sum is GLOBAL, so the "rest" after cutting the largest is not an independent sub-stick and n does not cleanly decrement — needs a strengthened scale-invariant hypothesis, or a majorisation/Hall pairing argument instead.

Cases to cover: LB makes k pieces for every k=1..n+1 (k<n+1 is easier: XY can drive D to 0, numerics confirm); equal-piece configs (halve one piece → D=0); the tight pair LB=geometric, XY=full halving, D=1/S_n.

Watch out for:
  - Greedy-pick reduction is load-bearing; prove it, don't assume it.
  - LB-B is NOT raw dominance: XY can break dominance (n=1, halving 2→1+1 makes largest = 1 < sum of rest); the proof MUST use the cut budget ≤n + the "+1 gap". With >n cuts the lower bound fails (n=1, 2 cuts ⇒ D=0), so the budget is essential.
  - Upper bound is the real risk: myopic greedy XY FAILS (verified on 36/400 configs n=2, 67/400 n=3); a complete proof needs the full inductive/majorisation argument.
  - Re-verify n=4,5 numerically (using the "fragment-matches-existing-size" candidate cut set, which provably covers all piecewise-linear breakpoints of D) before fully trusting the general conjecture.
  - Conjecture is strongly confirmed: exhaustive/grid + full-lookahead optimal XY for n=1,2,3 show geometric is the unique LB optimum and D*=1/S_n.
