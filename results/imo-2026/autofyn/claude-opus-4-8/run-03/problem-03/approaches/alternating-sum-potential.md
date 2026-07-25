## Status
partial

## Approaches tried
- (fresh approach, round 1) — laid out the alternating-sum potential route.
- (round 2) alternating-sum potential via the **layer-cake identity** S = meas{t : N(t) odd}.
  Fully proved: L0–L4, the layer-cake identity, the min-pairing identity, the balanced-mass
  reframe of the upper bound, the whole problem for n=1 (both bounds, c(1)=2/3), and the lower
  bound in the case "XY does not cut the top dyadic piece". Gaps: G1 (binding lower bound) and
  G2 (general upper bound / Lemma D).
- (round 3) Recast the lower bound as the units-free claim P(n); **completed and generalized
  Case 1** (top piece uncut) via φ-telescoping (certified L8). Reduced the binding case to the
  overlap bound G1. Confirmed the dyadic cascade witness for the upper bound. Solid partial.
- (round 5) **Closed the entire c_n = 1 case** (top group cut into exactly two parts, with an
  arbitrary legal refinement of the lower groups): a clean 4-line proof via L6 (truncation) + L3
  (XOR split) + IH giving **S(B) ≥ S(R) ≥ 1** through the exact identity e = 2^{n-1} − b. This
  generalizes the certified L9 exact-bisection boundary (b = 2^{n-1}) to every unequal two-part top
  cut. Combined with Case 1 (c_n = 0) and the e ≥ 1 case (L6), the **residual gap Gβ now shrinks to
  c_n ≥ 2 and e < 1** (top group cut into ≥ 3 parts, none exceeding H by ≥ 1). Also **sharpened the
  obstruction map**: the part budget is essential *even in the top-only regime* (all cuts inside the
  top group) — a top-only refinement with n+2 parts already gives β > 2^n−1 (numeric: n=3, top group
  in 5 parts, β = 7.4 > 7), so the extremal sits at the part-budget frontier of *every* group, not
  just globally. Reduced Gβ to the clean coupled **overlap inequality** e + S(Q_low) + S(R) − 2W ≥ 1
  (W = meas{N_{Q_low} odd ∧ N_R odd}); the pointwise slack W ≤ S(Q_low) is tight for c_n=1 but loses
  at the cascade (c_n ≥ 2), which is exactly why the residual needs the actual value of S(R) (global
  coupling), matching O3.
- (round 4) **Reforged the ENTIRE lower bound as a single clean matching cap via L4, with NO
  truncation.** Established (all rigorous): (a) the reforge S(B) ≥ 1 ⟺ **β(B) ≤ 2^n − 1** for
  every ≤n-cut refinement B of P_n, where β = max matched weight (L4); (b) the clean identity
  **β(B) = even-rank sum = ∫ ⌊N_B(t)/2⌋ dt**, attained by consecutive pairing; (c) **Case 1
  (top uncut) in one line** via the peel identity — β(B) = odd-rank-sum(B∖{2^n}) ≤ 2^n−1; (d) the
  e ≥ 1 case reduces to L6 directly. **Three decisive obstruction results** that sharpen the gap:
  (O1) the cut budget is ESSENTIAL — with > n cuts β can reach 2^n − 1/2 > 2^n − 1 (bisect-all),
  so no bound ignoring cut count (pure mass / LP mass-cover / majorization-only) can work;
  (O2) pointwise-in-height (⌊N/2⌋ ≤ N_R) and pointwise-in-rank (y_(2i) ≤ 2^{n−i}) both **FALSE**
  (explicit counterexample B={4,2,2,2,2,2,1}); (O3) the recursive top-group split reproduces the
  overlap exactly: **β(Q⊔C) = β(Q) + β(C) + W**, so peeling does NOT dodge the wall — only a
  GLOBAL matching bound using cut budget + origin-group sums can. Also (O4) majorization+part-count
  is insufficient (six copies of 2.5 majorized by P_3, ≤7 parts, β=7.5). The residual crux —
  β(B) ≤ 2^n−1 in the e<1 / top-group-cut case — remains an **explicit gap (Gβ)**, now known to
  require a global argument consuming both the cut budget and the origin-group-sum constraints.

## Current best
**Answer c(n) = 2^n/(2^{n+1}−1)** (write D_n := 2^{n+1}−1). Rigorously established:

1. **Reduction to the multiset game** (L0, L1, certified) and **potential identity** (L2): LB's
   value = (1+S)/2, so c(n) = 2^n/D_n ⟺ max_A min_B S(B) = 1/D_n.
2. **Layer-cake** (L3) and **min-pairing** (L4) certified: S(P) = meas{N(t) odd} = sum(P) − 2β(P),
   β(P) = max over pairings of Σ_{pairs} min = **even-rank sum** = ∫ ⌊N(t)/2⌋ dt.
3. **Full n = 1** (both bounds): c(1) = 2/3.
4. **NEW (round 4) — the whole lower bound as one matching cap.** For LB's dyadic play A = P_n,
   in units of 1/D_n the parts are {2^0,…,2^n} (sum D_n). Cuts preserve sum, so for every
   ≤n-cut refinement B, S(B) = D_n − 2β(B), hence
     **S(B) ≥ 1  ⟺  β(B) ≤ (D_n − 1)/2 = 2^n − 1.**
   No truncation is needed; this single statement is the entire lower bound and subsumes L8.
5. **Case 1 (top uncut, c_n=0) via peel**, **e ≥ 1 via L6**, and **NEW (round 5) c_n = 1 (top cut
   into two parts) via the L6+L3-split chain giving S(B) ≥ S(R) ≥ 1** — all rigorous (§4). After
   these the **residual gap Gβ** is exactly β(B) ≤ 2^n−1 in the case **c_n ≥ 2 and e < 1** (top group
   cut into ≥ 3 parts, largest < 2^{n-1}+1), reduced to the coupled overlap inequality (Wβ) which
   provably must consume the lower block's surplus S(R) − 1 (global; §4 residual, §5).
6. **NEW (round 4) — obstruction map** O1–O4 (§5): the cut budget and the origin-group-sum
   constraints are BOTH provably necessary; pointwise, majorization-only, and recursive-split
   routes are all provably insufficient. This is the sharpest available characterization of what a
   valid proof of Gβ must use.

**Open gaps.** (Gβ) β(B) ≤ 2^n−1 for ≤n-cut refinements of P_n in the case **c_n ≥ 2 and e < 1**
(the case c_n ≤ 1 is now closed, round 5) — a *global* matching/rank-counting statement, reduced to
the coupled overlap inequality (Wβ) (§4 residual, §5 pins down which levers it must use). (G2) the general
upper bound (Lemma D): a witness pairing with β ≥ (2^n−1)/D_n for arbitrary A; the dyadic cascade
witness is exact but the general amortized charging is unproven.

---

# Full write-up (partial)

Throughout, the stick is [0,1]; Liu Bang marks ≤ n points, then Xiang Yu marks ≤ n further points;
the stick is cut at all marks; players alternately claim whole pieces, LB first. We determine the
largest guaranteed LB total c(n).

**Answer.** c(n) = 2^n/(2^{n+1}−1). Write D_n := 2^{n+1}−1.

## 1. Reduction to the multiset game (certified lemmas L0–L8 — imported)

Proved in full and **certified** in `results/imo-2026-03/lemmas/`; imported verbatim.

- **L0 (Claiming lemma).** Two players alternately remove one element (P1 first), each maximising
  his total; P1's optimum = Σ_{i odd} x_(i) (descending sort).
- **L1 (Order irrelevance).** The game reduces to: LB picks a partition A (≤ n+1 parts, sum 1); XY
  refines it with ≤ n binary splits into a multiset B; LB's value = odd-rank sum of B.
- **L2 (Potential identity).** For Σ p_(i) = 1, put S(P) := Σ_i (−1)^{i+1} p_(i). Then
  odd-rank sum = (1+S)/2. Hence c(n) = 2^n/D_n ⟺ max_A min_B S(B) = 1/D_n.
- **L3 (Layer-cake).** S(P) = meas{t>0 : N(t) odd}, N(t) := #{pieces ≥ t}; and for P = Q⊔C,
  **S(Q⊔C) = S(Q)+S(C)−2W, W := meas{N_Q odd ∧ N_C odd} ≥ 0.**
- **L4 (Min-pairing).** For sorted y_1 ≥ … ≥ y_m with Σ = 1, S = 1 − 2β where
  **β := max over pairings of Σ_{pairs} min(y_i,y_j)**, attained by the consecutive pairing
  (y_1,y_2),(y_3,y_4),…. (Unnormalised: S = sum − 2β.)
- **L5 (Peel-max).** S(P) = b_(1) − S(P∖{b_(1)}); 0 ≤ S ≤ b_(1) ≤ ΣP.
- **L6 (Truncation).** With H := 2^{n-1}: at most one part of B exceeds H; writing e := (max−H)^+,
  S(B) = e + S(B_low) where B_low replaces that part by H. Consequence: **e ≥ 1 ⟹ S(B) ≥ 1.**
- **L7 (High-band).** Unconditional: if the largest part ≥ 1 with the appropriate band condition,
  S(B) ≥ 1 (subsumed below by the cleaner β route for the uncut case).
- **L8 (φ-telescoping Case-1).** Top-uncut refinement of a ratio-≥2 set has S ≥ φ_n ≥ a_0.

## 2. The matching reforge of the lower bound (round-4 core, rigorous)

LB plays the **dyadic partition** A = P_n with parts 2^i/D_n, i = 0,…,n. **We work in units of
1/D_n**, so the parts are the integers P_n = {2^0, 2^1, …, 2^n}, with total D_n = 2^{n+1}−1. By (∗)
:= [c(n)=2^n/D_n ⟺ max_A min_B S = 1/D_n], it suffices to prove that **every ≤ n-cut refinement B
of P_n has S(B) ≥ 1** (one unit = 1/D_n).

Each cut splits one piece into two positive pieces of the same total length, so **every refinement
B of P_n has Σ B = D_n**. By L4 (unnormalised form, valid after scaling since S and β are both
1-homogeneous),
  **S(B) = D_n − 2β(B),  β(B) = max over pairings of Σ_{pairs} min.**            (β-reforge)
Therefore
  **S(B) ≥ 1  ⟺  β(B) ≤ (D_n − 1)/2 = (2^{n+1} − 2)/2 = 2^n − 1.**               (Tβ)

So the **entire lower bound** is the single combinatorial cap
  **(Tβ)  β(B) ≤ 2^n − 1  for every ≤ n-cut refinement B of P_n.**
No band-truncation and no case-split on e are needed to *state* it (they reappear only as tools).
[Numerically verified tight: over 2·10^5 random ≤n-cut refinements for n=1,2,3 the maximum β found
is exactly 2^n−1 (1, 3, 7); the cascade attains it.]

### 2a. The matching identity used throughout (promotable).
For any finite multiset with descending sort y_1 ≥ … ≥ y_m, the consecutive pairing gives
min(y_{2i−1}, y_{2i}) = y_{2i}, so by L4
  **β = Σ_{i≥1} y_{2i}  = even-rank sum,**
and by layer-cake (each even rank y_{2i} = ∫ 1[y_{2i} ≥ t] dt, and #{even ranks ≥ t} =
#{i : 2i ≤ N(t)} = ⌊N(t)/2⌋),
  **β = ∫_0^∞ ⌊N(t)/2⌋ dt.**                                                     (β-layercake)
Thus (Tβ) reads: *the sum of the even-ranked parts of any ≤n-cut refinement of P_n is ≤ 2^n−1*, and
equivalently *∫ ⌊N_B(t)/2⌋ dt ≤ 2^n − 1*. [Both identities numerically verified: β = even-rank sum
over 20000 random multisets; β = brute-force max matched weight over 3000 random small multisets;
0 mismatches.] These identities are elementary consequences of the certified L3, L4.

## 3. Complete solution for n = 1 (c(1) = 2/3)

Unchanged from the certified round-2 write-up: by (∗) show max_A min_B S = 1/3. LB plays {2/3,1/3};
in every one-cut response S = 1/3 or S ≥ 1/3 (three-piece case analysis). Conversely XY holds any
LB choice to S ≤ 1/3 (bisect / cut cases). Hence c(1) = 2/3 = 2^1/(2^2−1). ∎ (n = 1)

## 4. Cases of (Tβ) settled rigorously

Fix n ≥ 2 and a ≤ n-cut refinement B of P_n. Group the parts of B by **origin**: the parts of B
cut from the original 2^j form a sub-multiset with sum 2^j; let c_j = #cuts spent inside origin 2^j
(so it has 1 + c_j parts) and Σ_j c_j ≤ n. Let Q := parts from origin 2^n (sum 2^n, c_n + 1 parts).

### Case 1: c_n = 0 (top part uncut) — COMPLETE, one line.
Then 2^n is itself a part of B. Since 2^n > 2^n − 1 = Σ_{j<n} 2^j ≥ (sum of all other parts of B,
which refine {2^0,…,2^{n-1}} and total 2^n − 1), the value 2^n is the **strict maximum** y_1 of B.
Let B' := B ∖ {2^n} (sum 2^n − 1). In the descending sort of B, position 2i (i ≥ 1) holds the
element in position 2i − 1 of B' (removing the top element shifts every lower rank up by one).
Hence by (2a),
  β(B) = Σ_{i≥1} y_{2i}(B) = Σ_{i≥1} (2i−1)-th element of B' = **odd-rank sum of B' ≤ Σ B' = 2^n − 1.**
So β(B) ≤ 2^n − 1, i.e. S(B) ≥ 1. ∎ (Case 1)
*(This is the round-3 generalized Case 1 (L8) re-derived in one line in matching language; the
inequality "odd-rank sum ≤ total" is immediate as the odd ranks are a subset of the parts.)*

### Case 2a: a part exceeds 2^{n-1} by ≥ 1 (e ≥ 1) — COMPLETE via L6.
If the (by L6-A0 unique) part exceeding H = 2^{n-1} is ≥ H + 1, then e := (max − H)^+ ≥ 1, and L6
gives S(B) = e + S(B_low) ≥ e ≥ 1 (using S(B_low) ≥ 0 from L5). By (Tβ) this is β(B) ≤ 2^n − 1. ∎

### Case 2b: c_n = 1 (top group cut into exactly two parts) — COMPLETE (NEW, round 5).
Let the two top-group parts be a ≥ b with a + b = 2^n, so a ≥ 2^n − a, i.e. **a ≥ 2^{n-1} = H and
b ≤ H.** Let R := B ∖ {a,b} be the union of the lower origin groups; R is a refinement of
P_{n-1} = {2^0,…,2^{n-1}} using ≤ n − c_n = n − 1 cuts, so by the induction hypothesis P(n−1) (the
lower-bound statement one level down, base P(1) proved in §3) we have **S(R) ≥ 1.**

If a = H then b = H, the top group is bisected into two equal halves {H,H}; then N_{\{H,H\}}(t) ∈
{0,2} is even for all t, so by L9 (self-pairing) W = 0 and S(B) = S({H,H}) + S(R) = 0 + S(R) ≥ 1. ∎

Otherwise a > H, so a is the unique part exceeding H (by L6-A0, since b ≤ H and every lower part is
≤ 2^{n-1} = H). Set e := a − H > 0. Because a = 2^n − b,
  **e = a − H = (2^n − b) − 2^{n-1} = 2^{n-1} − b = H − b.**            (identity ⋆, verified exactly)
L6 (truncation) gives S(B) = e + S(B_low), where B_low = {H, b} ⊔ R (the part a replaced by H).
Apply the L3 XOR split to B_low with the two groups Q_low := {H, b} and R:
  S(B_low) = S({H,b}) + S(R) − 2W,  W := meas{ t : N_{\{H,b\}}(t) odd ∧ N_R(t) odd } ≥ 0.
Here S({H,b}) = H − b (as H ≥ b), and N_{\{H,b\}}(t) is odd exactly on t ∈ [b, H) (there
N_{\{H,b\}} = 1; it is 2 on [0,b) and 0 on [H,∞)), so
  **W ≤ meas{ t : N_{\{H,b\}}(t) odd } = meas[b, H) = H − b.**            (†)
Combining with (⋆), e = H − b, hence
  S(B) = e + S(B_low) = (H − b) + (H − b) + S(R) − 2W = 2(H − b) + S(R) − 2W
       ≥ 2(H − b) + S(R) − 2(H − b) = S(R) ≥ 1,
using (†) in the inequality and S(R) ≥ 1 in the last step. Thus **S(B) ≥ 1**, i.e. β(B) ≤ 2^n − 1. ∎
*(The whole c_n = 1 case reduces to the trivial pointwise bound W ≤ H − b because the L6 excess e
exactly equals S(Q_low) = H − b here — identity (⋆). This is the clean reason the two-part top cut
is easy; for c_n ≥ 2 the identity fails and W ≤ S(Q_low) becomes too lossy — see §5.)*

### Residual case (GAP Gβ): c_n ≥ 2 and e < 1.
After Cases 1, 2a, 2b the only remaining configurations are: the top group is cut into **≥ 3 parts**
(c_n ≥ 2) and **no part exceeds H by ≥ 1** (e < 1). Here β can approach 2^n − 1 from below and the
bound is sharp (the cascade, which lives in exactly this residual, attains it), so no pointwise slack
survives. **This is the honest remaining gap.** §5 pins down exactly what a proof must use.

**Sharpest reduction of the residual (round 5).** Grouping B = Q ⊔ R with Q the (capped) top group
Q_low and R the lower refinement, the same L6 + L3-split chain as Case 2b gives, with no case
hypothesis,
  **S(B) = e + S(Q_low) + S(R) − 2W,  W = meas{N_{Q_low} odd ∧ N_R odd}.**    (residual identity)
Since S(R) ≥ 1 (IH), the entire residual is the single coupled inequality
  **(Wβ)   e + S(Q_low) − 2W ≥ 1 − S(R),   equivalently   2W ≤ e + S(Q_low) + (S(R) − 1).**
The pointwise cap W ≤ S(Q_low) (used freely above) closes c_n = 1 because there e = S(Q_low) and
S(R) = 1 suffices; but at the cascade (n=3: e = 0, S(Q_low) = 2, W = 2, S(R) = 3) it gives only
2·2 = 4 ≤ 0 + 2 + 2 = 4 — **tight, and it genuinely needs the surplus S(R) − 1 = 2 of the lower
block.** So (Wβ) cannot be proved by bounding W against the top group alone (O3): it must consume
the lower block's surplus, i.e. be **global**. This is the exact shape of Gβ.

## 5. Obstruction map for Gβ (round-4, rigorous) — what a valid proof MUST use

These four results are proved rigorously and **sharply constrain** any proof of (Tβ)/Gβ; they are
the round's main structural contribution and rule out several tempting shortcuts.

**(O1′) The part budget is essential even in the TOP-ONLY regime (round-5 sharpening).** One might
hope that spreading cuts across origin groups is what breaks a naive bound and that confining all
cuts to the top group keeps β ≤ 2^n − 1 automatically. FALSE. Take R = P_{n-1} uncut and cut the top
group 2^n into m equal parts of 2^n/m (all cuts inside the top group). For n = 3, R = {4,2,1}:
- m = 3 or 4 top parts (≤ n = 3 cuts, legal): max β = 7 = 2^n − 1 (attained; the cascade top group
  {4,2,1,1} is the m = 4 optimum).
- m = 5 top parts (4 cuts, one over budget): β = 7.4 > 7 = 2^n − 1.
[Exact-Fraction search over top-group compositions, incremental, < 30 s.] So the cap fails already at
one over-budget cut *inside a single group*. Consequence: the extremal is pinned at the **part-budget
frontier of every group simultaneously** (each group j uses its full share c_j of the global budget
Σc_j ≤ n), not merely at a global part-count ≤ 2n+1. Any proof must consume the *per-configuration*
budget, and O1 (global) is the special case of O1′ that already suffices to kill pure-mass covers.

**(O1) The cut budget is essential; no cut-count-free bound can work.** With unlimited cuts, XY can
bisect every part repeatedly; after k rounds of global bisection all D_n·2^k parts are equal, so
β = even-rank sum = (#parts/2)·(part size) = ΣB/2 = D_n/2 = 2^n − 1/2 **> 2^n − 1**. (For n=3,
six equal 2.5's already give β = 7.5 > 7.) Therefore (Tβ) is FALSE without the ≤ n cuts hypothesis,
and **any bound on β that does not consume the cut budget (equivalently the part-count ≤ 2n+1)
cannot prove (Tβ).** In particular a pure mass argument, or any LP price cover φ_i + φ_j ≥
min(y_i,y_j) with prices depending only on values, is doomed: e.g. the dyadic-floor cover
φ_y := 2^m (2^m < y ≤ 2^{m+1}) satisfies φ_i + φ_j ≥ 2min(φ_i,φ_j) ≥ min(y_i,y_j) (as φ_y ≥ y/2 and
φ is monotone), giving β ≤ Σ φ_y, but Σφ_y can approach ΣB = D_n (parts just above a dyadic have
φ ≈ value), far above 2^n − 1. Proven.

**(O2) Pointwise bounds fail — the argument must be global.** Both natural pointwise strengthenings
are FALSE, witnessed by B = {4,2,2,2,2,2,1} (n=3: cut 2^3 into four 2's with 3 cuts, originals
{4,2,1} uncut; Σ = 15, a valid ≤3-cut refinement, β = even-rank sum = 2+2+2 = 6 ≤ 7 ✓):
  - *pointwise-in-height* ⌊N_B(t)/2⌋ ≤ N_R(t) (with R = {2^0,…,2^{n-1}}) FAILS: on t ∈ (1,2],
    N_B = 6 so ⌊N/2⌋ = 3 > N_R = 2. It is rescued only after integrating (the band (2,4] carries 0
    against N_R = 1, so ∫⌊N/2⌋ = 3+3+0 = 6 ≤ 7). The excess at one height is compensated by a
    deficit at another **through mass conservation** — a global, not pointwise, phenomenon.
  - *pointwise-in-rank* y_(2i) ≤ 2^{n−i} FAILS: y_(6) = 2 > 2^{3−3} = 1.
So (Tβ) genuinely requires a global integral/mass argument, not a heightwise or rankwise domination.

**(O3) The recursive top-group split reproduces the overlap W — peeling does NOT dodge the wall.**
For any split of the parts into Q (top group) and C (the rest), the elementary floor identity
⌊(a+b)/2⌋ − ⌊a/2⌋ − ⌊b/2⌋ = 1[a odd ∧ b odd] integrated against (β-layercake) gives, rigorously,
  **β(Q⊔C) = β(Q) + β(C) + W,  W := meas{N_Q odd ∧ N_C odd} ≥ 0**                (β-split)
[numerically verified, 20000 random Q,C, 0 mismatches]. This is exactly the dual of S(Q⊔C) =
S(Q)+S(C)−2W. Hence an induction that peels the top group and bounds β(C) by the IH re-introduces
**the identical overlap W** that blocks the layer-cake route — the β-language gives no free lunch
via recursion. The only escape is a **global** bound on β(B) (equivalently on ∫⌊N_B/2⌋) that never
splits into Q and C, i.e. one that treats all origin groups simultaneously.

**(O4) Majorization + part-count is insufficient; the origin-group sums are needed.** B is
majorized by P_n (each cut is a mass-spreading Robin-Hood transfer) and has ≤ 2n+1 parts, but these
two facts do NOT imply (Tβ): the multiset of six equal parts 2.5 (n=3) is majorized by P_3
(top-r sums 2.5,5,7.5,10,12.5,15 ≤ 8,12,14,15,15,15) and has 6 ≤ 7 parts, yet β = 7.5 > 7. It fails
(Tβ) precisely because it is **not** a refinement of P_3: no partition of the origin masses
{8,4,2,1} into 2.5-chunks exists (1 cannot be a 2.5). Therefore a valid proof must use the
**origin-group-sum constraints** (each group's parts sum to a fixed power of two), not merely
majorization and the count.

**Consequence — the exact shape of the missing argument.** By O1–O4, a proof of Gβ must be a global
bound on β(B) = ∫ ⌊N_B(t)/2⌋ dt = Σ_i y_(2i) that (i) consumes the cut budget / part-count ≤ 2n+1,
(ii) uses the origin-group-sum constraints Σ(group j) = 2^j, and (iii) does not reduce to a
heightwise, rankwise, or single-top-split comparison. The target value 2^n − 1 = Σ_{j=0}^{n-1} 2^j
is exactly the **total mass of all origin groups below the top**, so (Tβ) is equivalently
  **odd-rank sum of B ≥ 2^n  (= the top group's mass),**
a clean target for such a global argument. I do not have this argument; **Gβ is an honest gap.**

## 6. Upper bound for general n (GAP G2 — Lemma D)

Unchanged: for LB's dyadic profile A = P_n, XY's cascade of n cuts (bisect 2^n, then a resulting
2^{n-1}, …, down to a 2^1) produces two copies of each of 2^{n-1},…,1 plus one extra 1; pairing
equal copies leaves a lone singleton 1, so β = 2^{n-1}+…+1 = 2^n − 1 exactly, i.e. S = 1/D_n. This
confirms 1/D_n is achievable at the dyadic profile (matches the LB extremal, per the explorer).
**For arbitrary A the witness construction remains unproven (G2).** The clean target β(B) ≥
(2^n−1)/D_n via L4 is the right formulation but the amortized-charging construction is untouched.

## 7. Verification of the answer at small n
- n = 1: c(1) = 2/3 = 2/(2²−1), proved in full (§3).
- n = 2: c(2) = 4/7; (Tβ) says β ≤ 3, cascade {2,2,1,1,1} gives β = 2+1 = 3, S = 1/7.
- n = 3: c(3) = 8/15; (Tβ) says β ≤ 7, cascade {4,4,2,2,1,1,1} gives β = 4+2+1 = 7, S = 1/15.

## Summary of status
Rigorously complete: the reduction (L0–L4, certified), the full n = 1 solution, the **matching
reforge of the whole lower bound (Tβ): β(B) ≤ 2^n − 1** with the clean identity β = even-rank sum =
∫⌊N/2⌋, **Case 1 (c_n=0, top uncut)**, the **e ≥ 1 case** (via L6), and **NEW (round 5) the full
c_n = 1 case** (top group cut into two parts) via S(B) ≥ S(R) ≥ 1, the exact dyadic cascade witness,
and a rigorous **obstruction map (O1′,O1–O4)** delimiting the residual. The two gaps are Gβ (the
global matching cap in the **c_n ≥ 2, e < 1** case, reduced to the coupled overlap inequality (Wβ))
and G2 (the general upper-bound construction). Because a "determine c(n)" answer requires both global
bounds, Status = **partial**.

## Build report
- **Status:** partial.
- **Closed this round:** the entire **c_n = 1** case of the lower-bound residual Gβ (top origin group
  cut into exactly two parts, with an arbitrary legal refinement of the lower groups) — a fully
  rigorous 4-line proof (§4 Case 2b) via L6 (truncation) + L3 (XOR split) + the induction hypothesis,
  keyed on the exact identity e = 2^{n-1} − b, yielding S(B) ≥ S(R) ≥ 1. This strictly generalizes
  the certified L9 boundary (equal bisection b = 2^{n-1}) to every unequal two-part top cut. The LB
  residual therefore shrinks from "c_n ≥ 1, e < 1" to "**c_n ≥ 2, e < 1**".
- **Also delivered:** (i) sharpened obstruction **O1′** — the part budget is essential even inside a
  single group (top-only refinement with one over-budget cut gives β = 7.4 > 7 at n=3), pinning the
  extremal at every group's part-budget frontier; (ii) the residual reduced to the clean coupled
  overlap inequality **(Wβ) 2W ≤ e + S(Q_low) + (S(R) − 1)**, with a proof-obstruction showing it
  must consume the lower block's surplus S(R) − 1 (tight at the cascade), i.e. it is genuinely global
  (matches O3). Numeric confirmations (exact Fraction, < 30 s each, incremental): β-cap holds with
  max exactly 2^n − 1 for legal refinements n = 2,3,4; c_n = 1 identity chain and S(B) ≥ S(R) hold
  n = 2,3,4 with 0 violations; O1′ witness reproduced.
- **Remaining GAPs:** (Gβ) β(B) ≤ 2^n − 1 for c_n ≥ 2 and e < 1, i.e. the coupled overlap inequality
  (Wβ) — the make-or-break, needs a global argument coupling the top group's shredding to the lower
  block's surplus (the scale-bucket Hall deficit remains the proposed mechanism but its explicit
  injective matching is still unwritten). (G2) the general-A upper bound.
- **Spec concerns:** none. Note (Tβ)/Gβ is *exactly equivalent* to the layer-cake residual S(B) ≥ 1;
  the round-5 value is the newly-closed c_n = 1 slice and the sharpened residual (Wβ)/O1′, not a
  closure of the whole gap.

## Spec concerns
None on the problem statement. Note that (Tβ) is *exactly* equivalent to the layer-cake residual
S(B) ≥ 1 (both equal, via L4), so the β-reforge does not by itself close the gap; its value this
round is the clean single-statement framing plus the obstruction map O1–O4, which rule out the
pointwise / majorization / recursive-split shortcuts and identify the two genuine levers (cut budget
+ origin-group sums) any successful proof must combine.

## Promotable lemmas
- **Matching identity (β = even-rank sum = ∫⌊N/2⌋).** For any finite multiset with descending sort
  y_(1) ≥ … ≥ y_(m), the max matched weight β := max over pairings of Σ_{pairs} min(y_i,y_j) (from
  L4) equals the even-rank sum Σ_{i≥1} y_(2i) and equals ∫_0^∞ ⌊N(t)/2⌋ dt, where N(t) = #{parts ≥
  t}. *Proved in §2a from certified L3, L4; verified numerically (0 mismatches).*
- **β-reforge of the lower bound (Tβ).** For LB's dyadic play A = P_n (units 1/D_n), every ≤n-cut
  refinement B has Σ B = D_n and S(B) = D_n − 2β(B); hence the entire lower bound S(B) ≥ 1 is
  equivalent to **β(B) ≤ 2^n − 1**, equivalently the odd-rank sum of B ≥ 2^n. *Proved §2 from L4.*
- **β-split identity.** For any partition of the parts into Q and C, β(Q⊔C) = β(Q) + β(C) + W with
  W = meas{N_Q odd ∧ N_C odd}; the dual of the certified L3 XOR identity. *Proved §5 (O3); verified
  numerically.*
- **Case-1 (top uncut) via peel.** If the strict maximum of B equals its own value ≥ ΣB − (that
  value) [e.g. 2^n uncut in a refinement of P_n], then β(B) = odd-rank-sum(B∖{max}) ≤ ΣB − max.
  *Proved §4, Case 1.*
- **Two-part-top-cut closure (c_n = 1), NEW round 5.** Let B refine P_n by ≤ n cuts with the top
  origin group cut into exactly two parts {a, b}, a + b = 2^n, a ≥ b, and let R := B ∖ {a,b} (a
  refinement of P_{n-1} by ≤ n−1 cuts). Then S(B) ≥ S(R). *Proof (§4 Case 2b): with H = 2^{n-1},
  either a = b = H and L9 gives S(B) = S(R); or a > H, e := a − H = H − b, L6 gives S(B) =
  e + S(B_low) with B_low = {H,b}⊔R, the L3 XOR split gives S(B_low) = (H−b) + S(R) − 2W with
  W ≤ H − b, so S(B) = 2(H−b) + S(R) − 2W ≥ S(R).* Consequently, if additionally S(R) ≥ 1 (the LB
  statement one level down), then S(B) ≥ 1, i.e. β(B) ≤ 2^n − 1. Verified n = 2,3,4, 0 violations.
