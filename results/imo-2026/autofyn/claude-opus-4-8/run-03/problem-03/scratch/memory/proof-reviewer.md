# proof-reviewer role memory

ALWAYS: for imo-2026-03, the certified foundation is L0(claiming=odd-rank sum, greedy opt),
L1(reduction c(n)=max_A min_B odd-rank), L2(Σ_odd=(1+S)/2 ⇒ target ⟺ max min S=1/D_n),
L3(layer-cake S=meas{#parts>t odd}, XOR decomp S(Q⊔C)=S(Q)+S(C)−2W≥|S(Q)−S(C)|),
L4(min-pairing S=1−2β, witness principle). All in results/imo-2026-03/lemmas/. Do not
re-review these; build on them. (round 2)
ALWAYS: the two live crux gaps are the general UPPER bound (witness pairing β≥(2^n−1)/D_n for
arbitrary A / value-function induction) and the BINDING lower case (XY cuts top piece, control
overlap W). Both live approaches share them — watch for a shared-gap plateau. (round 2)
NEVER: certify L4 from the writeup's uncrossing proof alone (it is sketched); the airtight
proof is via L3 parity c(t)≡N(t) mod 2. (round 2)
ALWAYS: S*(A) estimated as min-over-random-cuts is UPWARD-biased (min under-explored), so a
random A appearing to beat 1/D_n is estimator noise, not a counterexample. (round 2)
ALWAYS: round-3 certified L5(peel-max S(X)=m−S(X\m)), L6(A0 ≤1 shard>2^{n-1} + truncation S(B)=e+S(B_low)), L7(unconditional Lemma H: h≥1⟹S≥1), L8(generalized Case-1 φ-telescoping, ratio-≥2 sets). All re-derived + numerically clean. Build on these. (round 3)
ALWAYS: all 3 lower-bound gaps (A-res/G1/GAP-LB) are ONE statement — a cut-budget cap on the low-band overlap W in the small-top-shard sub-case (e<1/h<1). 3 rounds same wall; upper bound second wall. Flagged plateau → push a different framing. (round 3)

ALWAYS: round-4 certified L9(self-pairing W=0), L10(β=even-rank sum=∫⌊N/2⌋ + β-split), L11(R1 parity-vs-mean reformulation S(B_low)=∫[D odd], ∫D=sum diff, + R2 pointwise D≤1⟹PM). The general (PM) ∫[D odd]≥∫D interior-D≥2 compensation stays OPEN — L11 certifies only the reformulation+R2. (round 4)
NEVER re-attempt top-part-restricted upper bound (BISECT_top/MATCH_top averaging): REFUTED exactly, U_2({2,2,1})=0 via non-top small-part bisect while both top moves give U_1=1>5/7; every convex avg ≥ min of branches. Winning UB move is often a NON-top split. (round 4)
ALWAYS: (Tβ) β(B)≤2^n−1 is EXACTLY equivalent to layer-cake residual S(B)≥1 — the β-reforge is a reframing not a closure; don't let a builder claim it advances past the wall. (round 4)

ALWAYS: round-5 certified L12 (level-set form of (PM): ∫[D odd]−∫D=2(ΣB_{2m−1}−ΣA_{2m}); induction-peel R4 = interlacing IB-1, SAME identity — verify the pointwise f(d)=2(Σ1[d≤−(2m−1)]−Σ1[d≥2m]) termwise), L13 (meas{N_X≥k}=x_(k)), L14 (two-part-top-cut S({a,b}⊔R)≥S(R), closes c_n=1 slice; key: e=H−b exact, W≤H−b). L12 is a RECASTING not a closure — the general ΣB_{2m−1}≥ΣA_{2m} is still the open crux. (round 5)
NEVER let the level-set/IB-1 recasting be scored as closing the LB — it is exactly equivalent to (PM); (CB) for k_C=0 is numerically-confirmed-only (not proven), k_C≥1 aggregate + UB branch inequalities all still open. (round 5)

ALWAYS (round 6): when a proof claims a signed-sum/graph LB via "bipartition sign identity", check the edge-length identity is applied ONLY to a full connected component (not an arbitrary vertex subset) — that restriction is exactly what makes every incident edge have both endpoints inside; segment-subset-pigeonhole got this right and it is the load-bearing subtlety.
ALWAYS (round 6): a seeded-from-official proof can still be a genuine solve if EACH step is re-derived in-file (not cited) — re-derive the two new lemmas from scratch + run exact-Fraction numerics (0-violation over n=1..5, random inputs) on both bound-lemmas before APPROVE. segment-subset-pigeonhole passed all; solved imo-2026-03 after 5 rounds partial.
