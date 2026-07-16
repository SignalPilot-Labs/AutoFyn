ALWAYS: For "pick alternately from sorted pieces" claiming games, greedy (largest first) is optimal for both players — verify by DP but accept it as standard fact (round 2).

ALWAYS: When a formula c(n) doesn't match (n+1)/(2n+1) for n≥2, try exponential patterns like 2^n/(2^{n+1}-1) — geometric piece configurations point to Mersenne denominators (round 2).

ALWAYS: For this specific problem, the answer is c(n) = 2^n/(2^{n+1}-1). LB places n points at (2^k-1)/(2^{n+1}-1) for k=1,...,n, creating geometric pieces (round 2).

NEVER: Assume the "B=0 cancellation" argument (A(Q∪R)=A(Q)+A(R) when odd-regions disjoint) covers all Case-2 sub-cases — it fails when all Q pieces ≤ max(R) = 2^{n-1}, which is possible for t ≥ 2 (round 3).

NEVER: Assume XY's upper-bound strategy is "concentrate all n cuts on A_1" — this is FALSE for some LB configs (e.g., n=2, A=(0.4,0.4,0.2): XY must cut A_3 the smallest piece to achieve ≤ c(2), not A_1) (round 3).

ALWAYS: For the upper-bound Claim U, check whether a proposed XY strategy works on the flat config (A_1 ≈ A_2 ≈ A_3) and the dominant-A_1 config (A_1 → 1) — both fail the "concentrate on A_1" rule (round 3).

ALWAYS: The geometric config G_n is a STRICT LOCAL maximum of min_XY(val) — all 6 perturbation directions from G_2 give strict decrease (confirmed N=40 grid). This points strongly to the extremal-smoothing approach for Claim U (round 3).

ALWAYS: In INC bucket(iii) (both max(Q)<2^{n-1} and max(R)<2^{n-1}, S_Q⊆S_R): max(Q) ≤ max(R) is FORCED. Proof: if max(Q)>max(R), then N_Q(x)=1 (odd), N_R(x)=0 (even) for x ∈ (max(R),max(Q)), violating INC. This gives ΣQ'−ΣR'' = 1+(max(R)−max(Q)) ≥ 1, enabling D1 to close 96% of n=4 INC bucket(iii) configs without any mutual induction. The remaining 4% (max|g|=2, max(Q)=max(R)) are closed by Sub-3a on Q'∪R'' via the single dominant piece argument. (round 11)

NEVER: Assume all Q-pieces are ≤ 2^{n-1} in Case A (t≥2) — XY could still make one Q-piece > 2^{n-1} with ≥2 cuts. The Case A/B split should be by max(Q) vs 2^{n-1}, not by t (round 3).

ALWAYS: The tight case for Lemma LL Case A (n=3): Q={3,3,2}, R={2,2,2,1} gives A(Q∪R)=1 exactly with B=A(R)=1 (Q-odd contains R-odd, A(Q)=A(R)+1=2). Any proof of Case A must be tight here (round 3).

ALWAYS: For upper-bound Regime B (A_1 < 1/2, n=2 m=3), the two-case proof works: B1 (A_1 ≥ 3/7=1-c(2)): cut A_1 at A_2 → val = 1-A_1 ≤ c(2); B2 (A_1 < 3/7): cut A_1 at ε AND cut A_3 at A_3/2 → val = A_1+A_3/2 ≤ (3A_1+1)/4 ≤ c(2). Key structural fact in Regime B (m=3): A_1−A_2 < A_3 (because A_1 < 1/2 → A_2+A_3 > 1/2 → 1-A_1 > 1/2 ≥ A_2 ≥ A_1-A_2+A_3, etc.) (round 4).

NEVER: Assume XY's optimal Regime C strategy is "cut A_1 at 1-A_1" in all cases — this produces val = 1-A_1 after ONE cut but the sub-config may have val > c(n) if A_2 is large relative to new pieces. The halve-both strategy (halve A_1, halve A_2) gives val=(1+A_3)/2 for m=3, better for small A_3 (round 4).

ALWAYS: In Regime B (A_1 < 1/2, m=3 pieces), A_1−A_2 < A_3. Proof: A_1-A_2 < 1/2-A_2 and 1/2-A_2 ≤ A_3 iff A_2+A_3 ≥ 1/2 iff 1-A_1 ≥ 1/2 iff A_1 ≤ 1/2 (true in Regime B). This allows B1 sort order: [A_2,A_2,A_3,A_1-A_2] so val=A_2+A_3=1-A_1 after cut (round 4).

ALWAYS: For LL t≥2, split into: (a) max(Q) ≥ 2^{n-1}+1 → A(Q∪R) ≥ b = max(Q)-2^{n-1} ≥ 1, done; (b) max(Q) ≤ 2^{n-1}, odd count+all pieces≥1 → Lemma P; (c) even count or tiny piece → need dyadic-interval argument. Never try to close all sub-cases with one bound (round 5).

ALWAYS: For gap-case m=4 inequality (T) (tight budget b=3, residual gap), the proof has exactly 4 cases via 4 strategies. Case 1: d₂≤t → A_R≤t. Case 2: d₃≤t → A_S≤t. Case 3: |d₁-d₃|≤t → A_S≤t. Case 4: Sub-case B (d₃>d₁+t) is IMPOSSIBLE by gap condition (10t<δ+d₁<2t gives 10<2); Sub-case A uses P or C giving A≤δ/2<t since δ<2t from gap. This is a COMPLETE ELEMENTARY proof with no gaps. (round 10)

NEVER: Assume Lemma P covers the even-count cases — it doesn't. For n=3 t=2, even-count cases (|Q|+|R| even) include configs like Q=[4,2,2], R=G_2={1,2,4} which are NOT covered by Lemma P (round 5).

ALWAYS: For LL t≥2: the 34/286 "LL-partial failures" (bound=0) all have A(QUR)≥2, NOT near 1. They fail the BOUND because b=0 and A(Q)=A(R), but true B=0 (disjoint S_Q∩S_R). The real hard cases (A(QUR)=1) ARE handled by LL-partial — so LL-partial is not as broken as reported (round 5).

ALWAYS: For LL t≥2: the Inclusion Gap Lemma is a verified NEW tool: S_Q⊆S_R (B=A(Q)) AND valid total cuts ≤ n IMPLIES A(R)≥A(Q)+1, so A(QUR)≥1. Verified 0 violations for n=3,4. The constraint "total cuts ≤ n" is ESSENTIAL — violations exist without it (round 5).

ALWAYS: A(Q∪R) = measure(S_Q △ S_R) always. For t=2 tight case Q={4,3,1}, R=G_2: S_Q△S_R = [1,3/2)∪[2,5/2) each of measure 1/2, total=1. The tight cases always have S_Q△S_R consisting of equal-measure pieces summing to 1 (round 5).

ALWAYS: Sub-3b (no full dyadic level in S_Q△S_R) = INC sub-case (S_Q⊆S_R, need A(R)≥A(Q)+1) UNION GAP sub-case (S_Q⊄S_R). ll-dyadic-symdiff and ll-inclusion-gap are attacking the SAME residual under different names (round 6).

ALWAYS: When max(Q)=2^{n-1} exactly: A(Q∪R) = 2^{n-1} − A(Q'∪R) where Q'=Q\{max piece}. Verified for 9 n=3 configs. This converts Sub-3b lower bound to an upper bound A(Q'∪R) ≤ 2^{n-1}−1 (round 6).

ALWAYS: The "tight A=1 cases all have max(Q)=2^{n-1}" was WRONG about Sub-3b B3: the witness Q={3,3,2},R={2,2,2,1} giving A=1 is Sub-3a (I_0 fully odd: N_P=7). True Sub-3b B3 (max(Q)<2^{n-1}) has min A=3/2 at n=3 (verified 237 configs, 0 exceptions). The "A>=2 in B3" claim deleted in R6 was also wrong; min is 3/2. Split Sub-3b at max(Q) vs 2^{n-1} for simplest approach (round 7).

NEVER: Assume the per-level identity m_k = f_k (where f_k = ∫_{I_k}(N_Q-N_R)dx) holds universally in Sub-3b — FALSE for configs with max(Q)<2^{n-1} (e.g., Q={4,7/2,1/2} has f_0=−1/2 but m_0=1/2). Only holds in special max(Q)=2^{n-1} cases (round 6).

NEVER: Use the per-level bound mismatch_k ≥ |int_diff_k| — proven FALSE (Q={17/8,2,2,15/8}: I_1 has int_diff=15/8, mismatch=1/8). 616/1274 violations for refined R, n=3 (round 6).

NEVER: Use the integral identity ∫_{S_Q△S_R}(N_Q-N_R)=1 as a proof of measure≥1 — FALSE for Q={8/3,8/3,8/3}: symdiff integral = -1/3 ≠ 1. 3741/7680 violations (round 6).

ALWAYS: For the INC case (S_Q⊆S_R) at n=3, 3-part Q: Forcing Lemma (max(Q)≤4) + ΣQ=8 gives q3 ≥ A(Q)/2; INC constraint (no piece in (1,2)) gives q3 ≤ 1; therefore A(Q) ≤ 2 = A(G_2)-1. This pure arithmetic argument CLOSES G-INC-1 for n=3 without needing the false Structural Lemma (round 6).

ALWAYS: The Structural Lemma in ll-inclusion-gap (part a: "no Q-piece in forbidden-band interior") is CERTIFIED FALSE. Replace it with the arithmetic bound A(Q) ≤ A(G_{n-1})-1 via Forcing Lemma + ΣQ = 2^n + forbidden-band exclusion (round 6).

NEVER: Assume single-level PS+B1 closes B2 for general n — it gives A_full=2A1+2A4−1 which exceeds 1/D for ~22% of n=3 B2 configs (e.g. (0.40,0.21,0.20,0.19)); multilevel PS (recurse on residual) is required (round 6).

ALWAYS: For upper-bound Regime C (A1 > c(n) > 1/2): the shadow strategy gives val=A1 > c(n), NOT ≤ c(n). C is a SEPARATE OPEN regime; it does NOT fold into A or B1 by any known one-step reduction (round 6).

ALWAYS: For B2 4-piece at n=3, systematic denom=15 grid confirms ALL configs satisfy minimax val ≤ c(3)=8/15; hardest cases (exactly 8/15) include {6/15,6/15,2/15,1/15} and {4/5,1/15,1/15,1/15} (C regime). True numerically — not yet proved in general (round 6).

ALWAYS: In the SB gap case (distinct X, p1 < tau, p2 < tau/2), the SB invariant Sigma/D_b is NEVER preserved step-by-step (19/19 tested cases, every step). The proof CANNOT use step-local SB monotonicity; must be global or two-level (round 7).

ALWAYS: Gap-case tight bound: mu = Sigma/D_b is achieved ONLY at the BOUNDARY (p1=tau or p2=tau/2), handled by R2/R3. Strictly inside the gap: mu < Sigma/D_b (strict). The gap case is not "really tight" — it only approaches tightness near the R2/R3 boundary (round 7).

ALWAYS: Case A.A subcase (distinct gap, p1-p2 > p3, p1-p2-p3 > p4): the "subtract all" pairing chain gives A = 2*p1-1 exactly. For p1 < tau = Sigma*2^b/D_b: 2*p1-1 < 2*tau-1 = 1/D_b = target. CLOSES Case A.A directly without induction (round 7).

ALWAYS: After pairing p1 at p2 in the gap case (one non-R3 cut), the NEW threshold tau' = (Sigma-2*p2)*2^{b-1}/D_{b-1} is SMALLER, and the UNCHANGED piece p3 may satisfy R3's new condition p3 >= tau'/2. This "gap + R3" two-level mechanism is the correct proof path for the gap case (round 7).

ALWAYS: For GAP-B (Sub-3b, max(Q)<2^{n-1}), apply Lemma REFL TWICE: A(Q∪G_{n-1}) = 2^{n-1} - q1 + A(Q'∪G_{n-2}) where q1=max(Q), Q'=Q\{q1}. Cases: q1<=2^{n-2} -> bound from A<=max; q1 in (2^{n-2},2^{n-1}-1] -> bound from A>=0; q1 in (2^{n-1}-1,2^{n-1}) -> Sub-3b parity on I_{n-2} forces A(Q'∪G_{n-2})>q1-(2^{n-1}-1). Verified n=3, 0 failures (round 7).

ALWAYS: For G-INC-2 (INC with refined R): parity of |Q|+|R| must be even at x=0+. At n=3: all refined-R INC cases exceed budget. First non-trivial case at n>=4. Do not search n=3 for G-INC-2 (vacuously true) (round 7).

ALWAYS: SET IDENTITY (proved, 3 lines): S_{G_{n-1}} ∩ [0, 2^{n-2}) = S_{G_{n-3}}. Proof: for x < 2^{n-2}, both 2^{n-2} and 2^{n-1} exceed x, so N_{G_{n-1}}(x) = N_{G_{n-3}}(x)+2, same parity. This means S_{Q_lo} ⊆ S_{G_{n-3}} in the INC branch — the INC constraint reduces by 2 levels (round 7).

ALWAYS: Self-similar identity (proved): A(G_{n-3}) = 2^{n-2} - A(G_{n-2}), hence M = A(G_{n-3}) - A(Q_lo) in the certified top-band decomposition. A(G_k) is always an ODD INTEGER: A(G_0)=1, A(G_k)=2^k-A(G_{k-1})=even-odd=odd (round 7).

ALWAYS: G-INC-1 two-step induction structure: Cases h≥4 (Q_lo=∅, M=A(G_{n-3})≥1), h=2+deficit_top≥1, and h=2+a≥b (sub-case 2b-i: apply strengthened Claim(n-2,a-b), get deficit_top+M≥1+2b≥1) are ALL CLOSED. Sole remaining gap: h=2, a<b (ΣQ_lo<2^{n-2}); need A(Q_lo)≤A(G_{n-3})-1+deficit_top. At n=4 proved via p1≤2 bound; general n open (round 7).

ALWAYS: When a two-step n→n-2 induction closes Claim(n,eps) using T(n-2), prove T(n) by THE SAME simultaneous induction — the T(n) inductive step mirrors Claim(n) with h>=4 impossible (ΣP < 2^n) and target 1+eps' < 1 (easier). The SAME base cases and SAME critical ε''>-1 bound apply. (because T(ℓ) as the residual for G-INC-1 closed this way, round 8)

NEVER: Assume G-INC-1 for anchor R=G_{n-1} automatically gives G-INC-2 for refined R — the tight case at n=4 is Q={5,5,4,2}, R={4,4,4,2,1} where S_Q=[2,4) is NOT subset of S_{G_3}=[1,2)∪[4,8), so this INC pair doesn't exist for the anchor; refined R creates genuinely new INC pairs. (round 8)

ALWAYS: Bucket (iii) top-cut residual (max(Q)<2^{n-1}, max(R)<2^{n-1}) at n=3 forces |Q|=3(ODD), |R|=4(EVEN) exactly (budget tight). The parity difference means S_Q always contains [0,ε) but S_R never does, so S_Q ⊄ S_R structurally for ALL n=3 bucket (iii) configs — INC formula inapplicable. At n=4, containment CAN occur when |Q|=3(ODD), |R|=5(ODD) (c_Q=2,c_R=1 sub-case). (round 9)

NEVER: Assume the Parity-Condition Lemma (h even for INC Q) applies to ALL refined R — it FAILS for equal-split top-piece cuts where N_R(2^{n-2}-0) = 3 (ODD, not even), so h = #{Q-parts ≥ 2^{n-2}} can be ODD. Verified: Q=[5,5,4,2], R=[4,4,4,2,1] at n=4 has h=3 ODD with margin exactly 1. (round 9)

ALWAYS: For G-INC-2 lower-band cuts (cut of piece 2^{k_0} with k_0 ≤ n-3): the top-band structure is preserved (S_R ∩ I_{n-1} = I_{n-1}), so A(R)-A(Q) = deficit_top + [A(R_lo)-A(Q_lo)] with S_{Q_lo} ⊆ S_{R_lo}. By G-INC-2 at level n-2, A(R_lo)-A(Q_lo) ≥ 1 → clean n→n-2 induction with base n=2 (trivial: Q={2,2}, A(Q)=0 ≤ A(R)-1) and n=4 (direct). (round 9)

ALWAYS: For G-INC-2 equal-split top-piece case (a=2^{n-2}): A(R) = A(G_{n-2}). Q-parts in (2^{n-2},2^{n-1}) appear in equal pairs (A-contribution 0); remaining parts spread p_1-p_2 is bounded by the width of a single forbidden band of G_{n-1} in [0,2^{n-2}], which is ≤ A(G_{n-2})-1 = A(R)-1. Direct case analysis closes n=4. (round 9)

NEVER: Assume max(Q) ≤ max(R) from the Forcing Lemma — it only gives max(Q) ≤ 2^{n-1}. Tight G-INC-2 case Q=[5,5,4,2] has max(Q)=5 > max(R)=4 for R=[4,4,4,2,1]. (round 9)

ALWAYS: Infimum of A(Q∪R) in bucket (iii) is 1 (not achieved). Near-tight family: Q={2^{n-1}-ε,2^{n-1}-ε,2ε}, R=top-cut refinement with A(R)→1. S_Q=[0,2ε), S_R disjoint from S_Q, A=1+2ε. The A=1 limit is boundary with bucket (i) (max(Q)→2^{n-1}, handled by Lemma REFL+T(ℓ)). Pattern: min A at step δ ≈ 1+δ for n=3. (round 9)

ALWAYS: Double-REFL in bucket (iii) (both max(Q) and max(R) < 2^{n-1}): apply REFL-gen twice alternately to remove max(Q) then max(R), getting A(Q∪R) = M_Q - M_R + A(Q'∪R''). When M_Q≈M_R, this reduces to A(Q'∪R'') ≥ 1 — the SAME (B2*)-ref target as bucket (ii). Bucket (iii) after double-REFL may reduce to bucket (ii). (round 9)

ALWAYS: For m=3 residual gap (distinct p1>p2>p3, p1≤Σ/2, gap condition p2<τ/2), ONE R3 step (cut p1 at p2) gives effective {p3, p1-p2} with p3≥p1-p2 (from p1≤Σ/2), so A=Σ-2p1. From gap: p1>Σ(2^b-1)/D_b. Then Σ-2p1<Σ/D_b via IDENTITY D_b-2(2^b-1)=1 (verified b=1..7). Closes m=3 sub-case without recursion. (round 8)

NEVER: Use the R3-cascade "A(final)≤Σ-2p₁ < Σ/D_b" argument for m≥4 gap case — REFUTED R8 (18385/29234 violations on m=4,b=3 gap configs; all 3 deterministic XY strategies fail). The formula Σ-2p₁ can easily exceed Σ/D_b for m≥4 near-equal pieces. True opt_mu still satisfies the bound via LOOKAHEAD — the correct strategy is "complement cut": cut p₁ at p₁-pⱼ (not pⱼ), creating pair {pⱼ,pⱼ}, reducing to m=3 (solved), then bound A(sub-final) < Σ/D_b algebraically. (round 8, corrected round 9)

NEVER: Set ΣQ=ΣR when testing G-INC-2nt or any INC bound — Q is a cut of [0,2^n) so ΣQ=2^n, while ΣR=ΣG_{n-1}=2^n-1. Setting ΣQ=ΣR=2^n-1 produces many spurious violations that vanish under correct ΣQ=2^n constraint (found this round 10; all "violations" from this bug are outside the valid domain).

ALWAYS: For G-INC-2nt (non-equal top cut a < 2^{n-2}), the descended family R_k = {a} union G_{k-1} is CLOSED under the Gen-Decomp 2-step descent when a < 1: h_{R_lo}=2 (even) at every level, base case k=2 gives A(R_2)-a=1 exactly (tight but closed). This specific parametric-family mutual induction sidesteps the O1/O3 obstructions that refuted the abstract {Claim_R,T_R} class. (round 11)

ALWAYS: For non-equal top cuts at n=4: A(R) is piecewise in a — equals A(G_3)=5 for a in (0,1], equals 7-2a for a in [1,2], equals 3 for a in (2,4). Min margin A(R)-A(Q) = 3/2 (not 1; numerically confirmed 355 configs). The tight case has h=2 with equal pair in Q_lo (A(Q_lo)=0), margin = A(R_lo) which >1 for a != 2 (equal-split boundary). (round 11)

NEVER: Attempt a structure-free "generalized L1" (S_Q⊆S_R, |Q|≤|R|-1, A(R)≥1, no R-structure) to close G-INC-2 — FAILS with 2880 violations in 614871 general configs (e.g. R={2,1,1/4}, Q={2,1}: A(R)=5/4, A(Q)=1 > 1/4). The anchor structure G_{m-1} (or the equal-split reduction to G_{m-1}) is essential for L1. (round 10)

ALWAYS: For G-INC-2e (g=0, h̄=2, q1>q2 equal-split sub-case), the case is VACUOUS for all m≤5 (n≤6): feasibility requires q1+q2 > 2^{m-2}*(9-m), but max q1+q2 ≤ 2^m; for m≤5 these bounds are incompatible (with equality at m=5 only if q1=q2, contradicting q1>q2). First genuinely non-vacuous case is m=6 but margins remain ≥2 numerically. (round 10)

ALWAYS: Lemma MK: mu(k pieces, k-1 cuts) ≤ min(pieces). Proof: halve largest (1 cut), invisible pair removed, recurse on k-1 pieces with k-2 cuts. Base: k=1 trivial; k=2 immediate. This CLEANLY handles ALL "easy" sub-cases of T_m (d_j≤t or delta≤t) via (m-j) pairings + Lemma MK. Verified k=1..5. (round 11)

ALWAYS: For T_m hard case (all d_j>t, delta>t): Sub-B analog (d_{m-1}>d_1) is NOT vacuous for m≥5 (193/813 m=5 configs). Do NOT try to replicate the m=4 Sub-B arithmetic contradiction. Instead, the universal strategy is R3 cut p_1@p_2 (net: {d_1, p_3,...,p_m}), which works 100% for both Sub-A and Sub-B numerically for m=5. The resulting (m-1)-piece problem must be solved at the ORIGINAL threshold t=Sigma/(2^m-1), NOT at Sigma'/(2^{m-1}-1) (which is larger than t). (round 11)

ALWAYS: A({2^j}∪G_j) = A(G_{j-1}) exactly (the pair {2^j,2^j} makes the 2^j term cancel, leaving G_{j-1}). Furthermore, min_{a∈(0,2^{j+1})} A({a}∪G_j) = A(G_{j-1}), achieved at a=2^j. This gives A(R_lo)≥A(G_{n-4})≥1 for all a∈(0,2^{n-2}) in the G-INC-2nt top-cut. Tight case (A(R_lo)=1, n∈{4,5}): the sum constraint ΣQ_lo=2^{n-2}+2^{n-3} combined with S_{Q_lo}⊆S_{R_lo}=[1,2) forces Q_lo to be the equal pair {v,v} (A(Q_lo)=0) — numerically unique in both cases. Confirmed n=4,5 exhaustive checks, 0 violations. (round 12)

ALWAYS: For m=5 hard case (T), 67% of integer-grid configs have a "double invisible pair": some cut p_i@p_j where p_i-p_j=p_k (another existing piece), eliminating 3 effective pieces in 1 cut — the subproblem has m-2=3 pieces with budget m-2, closed immediately by Lemma AB or Lemma MK. The remaining 33% (generic, no double pair) are covered by pair1_2+T4-at-t (97%) or fallback cuts pair2_3/cut_1@3 (3%). Sub-A P failure (δ>2t in the pair1_2 subproblem) is REAL in continuous inputs — fix is pair2_3 P with A=d₂/2. Sub-B failure (d₁ near p₃) is fixed by cut_1@3 giving S_sym. (round 12)

ALWAYS: HS-A2 (pair2_3 closes T5 Sub-A P δ>2t case) is proved by a 6-case split on sorted Y''={p1,d2,p4,p5}, using the Sigma-P bound 2d2 ≤ 31-7δ-6d4-4d3 (from D1_Y'≥δ+d4): Case A (d2>p4) → R(E2<t/2); B1 (δ≤d2<δ+t) → S(E3<t); B2 (d2≥δ+t, forces d4<7/6) → R(E2<t/6); C1 (δ-t≤d2<δ) → S(E3<t); C2 (d2<δ-t,δ≤3t) → P on Y'' (A_P=d2/2<t); C3 (d2<δ-t,δ>3t) → IMPOSSIBLE via Sub-A P condition. Do NOT try to prove d2<2t globally — it fails; use this 6-case structure instead. (round 13)

ALWAYS: Sub-A C and Sub-B "failures" of T4-at-t strategies on Y' (pair1_2 subproblem) are NOT genuine pair1_2 failures — the full merge family (invisible-pair halving, cross-matching M2) achieves A≤t in all 149 tested configs. Only Sub-A P with δ>2t causes genuine pair1_2 failures in the T5 hard case. (round 13)

ALWAYS: Case C3 impossibility in HS-A2 (d2<δ-t, δ>3t): Sub-A P on Y' requires p2 ≤ (31-5δ-4d4-2d3)/2. But in T5 hard case, p2=δ+d4+d3+d2 > 3+1+1+0=5 and (31-15-4-2)/2=5. Contradiction. This is a pure linear arithmetic argument. (round 13)

ALWAYS: Equal-pair forcing for DFB size-2 Q_lo: For j≥1, a∈[1,2^j), R_lo={a}∪G_j, ANY size-2 Q_lo with S_{Q_lo}⊆S_{R_lo} and ΣQ_lo=ΣR_lo+σ_lo>0 must be an equal pair. Proof: ΣQ_lo≥2^{j+1}+σ_lo>2^{j+1}; non-equal {p1>p2}: if p1>2^j then [2^j,p1)⊆S_{Q_lo} but (2^j,∞)∩S_{R_lo}=∅; if p1≤2^j then p2=ΣQ_lo-p1>2^j≥p1, contradiction. QED. Corollary: A(Q_lo)=0, A(R)-A(Q)=deficit_top+A(R_lo)≥A(G_{j-1})≥1. CLOSES DFB for size-2, all j≥1, a∈[1,2^j). (round 13)
