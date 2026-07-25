# proof-builder role memory

ALWAYS: run the mandated numeric pre-check BEFORE writing a smoothing/monovariant proof; validate the estimator at the known extremal point first (e.g. S*(G_n)=1/D_n), then it is trustworthy near that point (imo-2026-03, round 2).
NEVER: trust a "single consecutive-pair, sum-preserving, toward-ratio-2" smoothing lemma without checking it can even CONNECT a generic point to the target — sum-preserving pair moves fix pair-sums and often cannot reach the extremal profile at all (imo-2026-03 Lemma G refuted this way, round 2).
ALWAYS: when a max-min value function's extremal claim survives numerically only as "some improving 2-part transfer exists," recognize its proof needs the directional derivative = envelope over the inner optimizer's OPTIMAL responses; that re-imports the crux and does NOT sidestep it (imo-2026-03 round 2).
ALWAYS: deliver the shared reduction lemmas (claim-game=odd-rank sum via order-statistic monotonicity + induction; order-irrelevance; O=(1+S)/2) as fully-proven promotable lemmas even when the crux gap stays open — they are the durable value (imo-2026-03 round 2).
## imo-2026-03 (IMO 2026 P3, alternating-sum-potential), round 2
ALWAYS: use the layer-cake identity S = meas{t>0 : N(t) odd}, N(t)=#pieces≥t, for this
  problem — it is cleaner than min-pairing and gives the EXACT split S(whole)=S(Q)+S(R')-2W
  ≥ |S(Q)-S(R')| when partitioning pieces into two groups (verified 0/400).
ALWAYS: the upper bound reframes as β = matched-smaller-mass ≥ (2^n-1)/D_n (S=1-2β).
NEVER: expect a per-cut match/bisect rule to prove the upper bound — F1 (explorers) shows
  15-30% random failure; needs whole-list lookahead / backward induction. Real crux, still open.
FACT: lower bound "hard case" is when XY CUTS the top dyadic piece (case ii). Case i (top
  uncut) is easy from superincreasing (2^n = 1 + sum-of-rest) but is the non-binding case.
  Random search confirms min-S over ≤n cuts on dyadic = 1 unit for n=1,2,3.
## imo-2026-03 (IMO 2026 P3, Chu-Han war)
ALWAYS: use the integral formula S(B)=measure{t: #parts>t is odd} (round 2) — cleaner than
  rank/parity bookkeeping AND than the min-pairing identity; a single split of v into (a,b)
  a>=b flips k_B parity exactly on (0,b) and [a,v) (each measure b), 0 elsewhere.
ALWAYS: reduce first via L0 (greedy claim optimal, value=odd-rank sum, proven by
  V(P)=T-min_i V(P\{p_i}) induction) + L1 (order irrelevance) + L2 (S_odd=(1+S)/2). Target
  becomes max_A min_B S(B)=1/D_n, D_n=2^{n+1}-1. All solid.
FACT: lower-bound Case 1 (top part 2^n left uncut) is trivial: S(B)=2^n-S(C)>=2^n-sum(C)=1.
  No IH needed. The HARD gap is Case 2 (top part cut): S(B)=S(Q)+S(C)-2M via integral XOR,
  and S>=|S(Q)-S(C)| is TOO WEAK — must use dyadic structure of C + superincreasing +1.
FACT: upper bound is the real crux (F1: no one-pass match/bisect rule; explorer confirmed
  15-30% failure). IH bound 2^{k-1}/D_{k-1} > 2^k/D_k so applying IH to any split is
  insufficient — chosen split must strictly beat generic IH. This is the shared field wall.

ALWAYS: for imo-2026-03 lower bound, use the truncation identity S(B)=e+S(B_low) at H=2^{n-1} (Lemma A1) instead of the Q/C band split — it is rigorous, cleaner, and reduces the whole LB to S(B_low)>=1-e; e>=1 (incl Case 1) is then free (round 3).
NEVER: try to close imo-2026-03 LB Case 2 with an interval bound — both |S(Q)-S(C)| and h+|S_low(Q)-S(C)| are numerically verified too weak (drop to 0 for n>=2 while S(B)=1); the residual genuinely needs the cut-budget cap on the overlap W (round 3).
NEVER: assume the upper-bound value function U_k(A) has a closed form in (a_1,sum) — single part {s} gives U_k=0 but same-sum dyadic gives s/D_k>0, so it depends on the whole profile (round 3).
## imo-2026-03 round 3 (alternating-sum-potential)
ALWAYS: the lower bound recasts cleanly as P(n): every <=n-cut refinement of a RATIO->=2
  superincreasing set {a_0<...<a_n} (a_j>=2a_{j-1}) has S>=a_0 (dyadic a_0=1). Verified
  numerically. Case 1 (top uncut) is COMPLETE for all such sets via phi_k=a_k-sum_{i<k}a_i,
  phi monotone increasing, S=a_n-S(rest)>=a_n-sum(rest)=phi_n>=a_0. No IH/budget needed.
NEVER: hope "S>=a_0" holds for GENERAL superincreasing (ratio in (1,2)) sets: {2,3} cut
  3->(2,1) gives {2,2,1} S=1<a_0=2. Ratio>=2 is essential. {1,4} min S=1=a_0 (ratio 4 ok).
FACT: G1 (binding lower Case 2, c>=1 cuts on top) reduces to S(Q)+S(C)-2W>=a_0 with
  S(C)>=a_0 by IH P(n-1); the STILL-OPEN piece is W<=(S_lo(Q)+S(C)-a_0)/2 (budget cap on
  overlap). Trivial W<=min(S(Q),S(C)) is TIGHT at the cascade so cannot close it. Real gap.
FACT: G2 upper crux genuinely needs lookahead; A={1} (single piece) is EASY (bisect once,
  S=0) NOT a hard case - the hard A are near-dyadic. Charging setup written but unproven.

## imo-2026-03 (round 3)
ALWAYS: for the lower bound S(B)>=1, the peel-max identity S(X)=m-S(X\{m}) is ONLY cosmetic — it unwinds via L2 back to Sigma_odd>=2^n = the same claim. Real content is the block/XOR + band decomposition. (because global-max-peel was pitched as unifying via peeling but peeling doesn't make residual superincreasing, round 3)
ALWAYS: the genuine unifier is the UNCONDITIONAL Lemma H: with h=max(q1-2^{n-1},0), h>=1 ==> S(B)>=1, no induction. It subsumes the whole "top uncut" Case 1 (c_n=0 gives h=2^{n-1}>=1) plus big-shard Case 2. Residual gap is only c_n>=1 AND h<1: a budget-cap bound on overlap W < min(S_low(B_n),S(Rest)). Shared crux across ALL live approaches. (round 3)

## imo-2026-03 round 4 (averaging-upper-bound, NEW UB slug)
NEVER: attempt the UB via averaging/min of the two TOP-PART moves (MATCH/BISECT) — REFUTED. Even the MIN of the two top-part branches overshoots s/D_k for k>=2 (A={2,2,1},k=2: both top-first-moves -> {2,1,1,1}, U_1=1 > target 5/7; true U_2=0 by bisecting the SMALL part). Convex avg >= min, so no weight p(anything) helps. (round 4)
FACT: the true UB strategy MUST split NON-top parts (bisect small unmatched parts to cancel them, beta=Sigma_even view L4). Which part to split is profile-dependent (dyadic->top, {4,4,2,1}->rank3, {2,2,1}->smallest) = the F1 case-split. Full any-part canonical move set DOES reach U_k*D_k<=1 (k<=3 verified). So Lemma B true; top-part-only insufficient. (round 4)

ALWAYS: for imo-2026-03 LB residual, use D:=N_Qlow-N_C — then S(B_low)=∫[D odd] and ∫D=1-e is a
  free sum identity, so residual ⟺ (PM) ∫[D odd]≥∫D; f(d)=[d odd]-d≥0 for d≤1 closes D≤1 slice
  (round 4). NEVER retry arbitrary-X profile invariant P* (S(XuC)≥sumX-sumC) — numerically false
  (slack -1.4); the single-block cut budget on Q is what's needed (round 4).

## imo-2026-03 round 4 (alternating-sum-potential, beta-matching reforge)
ALWAYS: whole LB (no truncation) = β(B)≤2^n-1 for ≤n-cut refinements of P_n, since ΣB=D_n and
  S=D_n-2β (L4). β=even-rank sum Σy_(2i)=∫⌊N/2⌋dt (consecutive pairing). Case1 (top uncut): 2^n is
  strict max, β(B)=odd-rank-sum(B∖{2^n})≤2^n-1 — ONE LINE. e≥1 via L6. (round 4)
NEVER: try to prove β≤2^n-1 pointwise (⌊N/2⌋≤N_R and y_(2i)≤2^{n-i} BOTH FALSE, ctrex
  {4,2,2,2,2,2,1}), by pure mass/LP-cover/majorization (unbounded cuts give β=2^n-1/2>2^n-1;
  six 2.5's majorized by P_3 has β=7.5), or by top-group recursion (β(Q⊔C)=β(Q)+β(C)+W
  re-imports the SAME overlap W). A valid proof MUST use cut-budget AND origin-group-sums, globally.

ALWAYS: for the imo-2026-03 (PM) residual, the clean layer-cake reformulation is
  ∫[D odd]−∫D = 2(Σ_{i≥0}meas{D≤−(2i+1)} − Σ_{i≥1}meas{D≥2i}); so (PM) ⟺ odd-down-time ≥
  even-up-time ⟺ ∫⌈D^-/2⌉≥∫⌊D^+/2⌋ (Lemma IB-1, proved+verified 0/60k). Makes R2 one line
  ({D≥2}=∅). (round 5)
NEVER: try to prove (PM) from ∫D≤1 alone — FALSE even for D≤2 (free/unstructured Q violates
  (PM) 67/20000 at n=3; genuine block-refinement+count budget 0/60000). The part budget
  |Q_low|+|C|≤2n+1 is provably essential to the injection totality. (round 5)

## imo-2026-03 round 5 (induction-peel, LB residual (PM))
ALWAYS: meas{N_X(t)>=k} = x_(k) (k-th largest part) EXACTLY — this turns the single-block part
  budget into Σ_k s_k = sum(Q_low) <= 2^n in measure form, and gives closed forms for level sets of
  D. This is the concrete lever P* lacked (round 5).
FACT: (PM) ⟺ Σ_m meas{D<=-(2m-1)} >= Σ_m meas{D>=2m} (level-set form, R4). The POINTWISE
  A_{2m}<=B_{2m-1} is FALSE for k_C>=1 (n=3 Q_low={4,4},C={2,16/9,4/3,1,8/9}: A_2=2>B_1=4/3,
  rescued by deeper B_3) — compensation is cross-scale, so per-level charging cannot work (round 5).
FACT: pointwise A_{2m}<=B_{2m-1} DOES hold for k_C=0 (Case B, C=P_{n-1} dyadic), reducing that whole
  regime to a finite shard inequality (CB); still needs Σ s_k<=2^n to prove. k_C>=1 needs full
  aggregate charging (round 5).

## imo-2026-03 round 5 (alternating-sum-potential)
ALWAYS: the c_n=1 LB case (top group cut into TWO parts {a,b}) closes cleanly: e=a-H=H-b EXACTLY
  (since a=2^n-b, H=2^{n-1}), so L6 S(B)=e+S(B_low) + L3-split S(B_low)=(H-b)+S(R)-2W with
  W<=H-b gives S(B)=2(H-b)+S(R)-2W >= S(R) >= 1 (IH). Generalizes L9's equal-bisection. Residual
  now c_n>=2 & e<1 (round 5).
NEVER: hope top-only cuts (all budget in top group, lower groups uncut) auto-satisfy beta<=2^n-1
  without the part budget — top group in n+2 parts already gives beta>2^n-1 (n=3: 5 top parts,
  beta=7.4>7). Budget essential per-group, not just global (O1', round 5).
FACT: the residual reduces to coupled overlap ineq (Wβ) 2W <= e+S(Q_low)+(S(R)-1); pointwise
  W<=S(Q_low) is TIGHT at cascade (n=3: 2*2=4 = 0+2+2) so proof MUST consume lower-block surplus
  S(R)-1 (global, matches O3). The "mass(G)>=mass(rest) => odd-rank-sum>=mass(G)" shortcut is FALSE
  (thirty 0.5's: G=16 halves mass 8, odd-sum=7.5<8) — needs the part budget too (round 5).

## imo-2026-03 round 6 (induction-peel, falsify-first)
NEVER: trust the s_1=H "boundary invariance" (slack constant over rest-splits) for imo-2026-03
  Case B — FALSIFIED round 6 (n=3 slack ranges [0,2], witness rest={3.9,0.1} slack 9/5). The
  matched-pair cancellation S(B_low)=S(Q_low' u P_{n-2}) at s_1=H IS rigorous (L4) but fires only
  on the measure-zero boundary s_1=H and recurses to a level-(n-1) copy ONLY if every residual
  shard <= H'=2^{n-2}; a shard in (H',H] breaks the cap and IS the non-constant slack. Shard-count
  induction axis is DEAD for (CB).
FACT: UB branch-inequality line (top-two-greedy MATCH/BISECT) RETIRED/DEAD — official IMO-2026
  n=5 all-32-branches counterexample. UB delegated to segment-subset-pigeonhole. Do not re-scope
  it inside induction-peel (round 6).
ALWAYS: run the gate's falsify-first numeric check FIRST and RESPECT the cut budget (<=n cuts =>
  <=n+1 shards) — an over-cut config gives spuriously negative slack and looks like a violation
  when it is just budget-illegal (round 6).

ALWAYS: for imo-2026-03 UB, split on part-count m: m≤n ⟹ bisect ALL parts ⟹ S(B)=0 (m cuts);
m=n+1 ⟹ pigeonhole 2^{n+1} subset sums vs D_n bins. Pigeonhole needs 2^m>D_n so ONLY m=n+1
works — the skeleton implicitly assumed n+1 parts and missed the m≤n case (round 6).
NEVER: assume the merge-align overhang is a single physical piece — compute S on the OUTPUT
multiset via L4 general min-pairing (equal pairs cost 0, overhang paired among itself cost ≤ its
mass). Cleanly dissolves the round-2 MATCH bookkeeping trap (round 6).
ALWAYS: for tree-extraction LB, exclude the isolated-dummy tree by a parity argument (N odd ⟹
dummy deg 1; N even ⟹ E≤n ⟹ ≥2 trees); self-loops are 1-cycles, auto-excluded from trees (round 6).
