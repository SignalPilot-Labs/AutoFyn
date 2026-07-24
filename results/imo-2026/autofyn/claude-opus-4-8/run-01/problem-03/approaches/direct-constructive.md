## Status
partial

## Approach: direct-constructive

**Framing.** Solve the whole problem by exhibiting explicit optimal strategies for both
players and proving each bound directly. Answer:

  c(n) = 2^n / (2^{n+1} − 1) = 1 / (2 − 2^{-n}).   Write D = 2^{n+1} − 1.

Verification of the closed form on small values (see §7):
- n=1: 2^1/(2^2−1) = 2/3.  n=2: 4/7.  n=3: 8/15.

Spine: (Phase 1) the claiming game is greedy, so LB's take equals the odd-ranked sum
(Lemma G1); (Phase 2) LB's geometric marking forces odd-sum ≥ 2^n/D, and XY's response
forces odd-sum ≤ 2^n/D against every LB marking.

Once all cuts are fixed, sort the pieces weakly decreasing r_1 ≥ … ≥ r_m and set
- **odd-sum** O = r_1 + r_3 + …, **even-sum** E = r_2 + r_4 + …, **alt-sum** A = O − E.
Since the list is sorted, A = Σ_j(r_{2j−1} − r_{2j}) ≥ 0, and O + E = 1, so **O = (1+A)/2**.

Two lemmas are already reviewer-**certified** and imported here without re-proof:
- **G1** (`lemmas/G1-greedy-odd-ranked.md`): in the alternating claim-to-maximise game the
  first mover collects exactly the odd-ranked pieces; greedy is optimal for both. Hence
  **c(n) = max_LB min_XY O**, the odd-sum marking game.
- **R** (`lemmas/R-oddsum-rewritings.md`): with N(t) = #{pieces of length > t} and total 1,
  O = ∫_0^∞ ⌈N(t)/2⌉ dt and **O = 1/2 + (1/2)·μ{t : N(t) odd}** (μ = Lebesgue measure). So
  A = μ{N odd}, and O ≥ 2^n/D ⟺ μ{N odd} ≥ 1/D, O ≤ 2^n/D ⟺ μ{N odd} ≤ 1/D.

---

## 3. LB's construction and the dominance identity — PROVED

**Construction.** LB marks x_k = (2^k − 1)/D, k = 1,…,n. Left to right the pieces are
[0,x_1]=1/D, [x_{k−1},x_k]=2^{k−1}/D (k≤n), [x_n,1]=2^n/D. Indeed [x_{k−1},x_k] has length
(2^k − 2^{k−1})/D = 2^{k−1}/D and the last piece (D−(2^n−1))/D = 2^n/D. Write P_j = 2^j/D
(j=0,…,n); Σ_{j=0}^n P_j = (2^{n+1}−1)/D = 1. Let R_j be the interval of length P_j; R_n is
the largest.

**Dominance identity.** P_j − Σ_{i<j} P_i = (2^j − (2^j − 1))/D = 1/D > 0: every LB piece
strictly exceeds the sum of all strictly smaller LB pieces, by exactly 1/D. ∎

**Units.** Throughout §4 we scale lengths by D, so the intact LB pieces become the integers
I = {2^0, 2^1, …, 2^{n−1}} (the "intacts"; ΣI = 2^n − 1), R_n has length 2^n, the whole
stick has length D = 2^{n+1} − 1, and the target O ≥ 2^n/D becomes **O ≥ 2^n**, equivalently
**E ≤ ΣI = 2^n − 1**, equivalently (Lemma R) **μ{N odd} ≥ 1**.

---

## 4. Lower bound: LB guarantees ≥ 2^n/D

We show: against LB's construction, any placement of ≤ n XY cuts leaves O ≥ 2^n. The whole
lower bound splits cleanly on a single dichotomy — **does XY cut R_n?**

- **XY spares R_n** (no cut inside R_n): §4.1 gives O ≥ 2^n **for every placement of the other
  cuts** (they may be spread arbitrarily among the R_j, j<n). This is now a complete, general
  case — no confinement needed.
- **XY cuts R_n**: §4.2–§4.4. Here R_n is fragmented; §4.4 (L2) argues the minimiser confines
  all cuts to R_n, and §4.2 (L1) treats that confined problem.

### 4.1 XY spares R_n ⟹ O ≥ 2^n — PROVED (general placement)
Suppose XY places no cut inside R_n (its ≤ n cuts may lie anywhere among R_0,…,R_{n−1}). Then
R_n survives intact as a piece of length 2^n. Every other final piece is either an uncut R_j
(j ≤ n−1, length 2^j ≤ 2^{n−1}) or a sub-piece of some R_j (j ≤ n−1) of length < 2^j ≤ 2^{n−1}.
In all cases its length is ≤ 2^{n−1} < 2^n. Hence R_n is the **unique** largest piece: it sits
at rank 1, so r_1 = 2^n. Since every term of the odd-sum is nonnegative,
    O = r_1 + r_3 + r_5 + … ≥ r_1 = 2^n.
Therefore O ≥ 2^n whenever XY spares R_n, whatever it does elsewhere. ∎

This single case already disposes of every XY strategy that does not touch R_n; the remaining
content of the lower bound is entirely about strategies that fragment R_n.

### 4.2 Confined case: all k ≤ n XY cuts lie in R_n

Then the final pieces are the n **intacts** I = {2^0,…,2^{n−1}} together with the
**fragments** F = {f_1 ≥ … ≥ f_{k+1}} of R_n, Σ_i f_i = 2^n, with |F| = k+1 ≤ n+1. We must
prove O(I ∪ F) ≥ 2^n. Reducing all cases to this confined one is L2 (§4.4).

The old integral reduction ∫⌊(N_F − N_I)/2⌋ dt ≤ 0 is **dropped**: the lower-bound explorer
proved it is algebraically identical to O ≥ 2^n (since N_F − N_I is odd ⟺ N is odd,
∫⌊(N_F−N_I)/2⌋ dt = 2^n − O), hence a rename, not a reduction.

#### 4.2.1 Fragment-count bounds — PROVED
For every integer j ≥ 0, **N_F(2^{n−j}) := #{fragments > 2^{n−j}} ≤ 2^j − 1.** Indeed if m
fragments each exceed 2^{n−j}, then m·2^{n−j} < Σ_i f_i = 2^n, so m < 2^j, i.e. m ≤ 2^j − 1.
In particular at most one fragment exceeds 2^{n−1} (j=1), at most three exceed 2^{n−2}, etc.

Also the intacts satisfy, for t ∈ [2^m, 2^{m+1}) (m = 0,…,n−2), N_I(t) = #{intacts > t} =
n−1−m, and N_I = n on [0,1), N_I = 0 on [2^{n−1},∞). ∎

#### 4.2.2 The interleaving configuration attains O = 2^n exactly — PROVED
Choose fragments g_1 > … > g_{n+1} with 2^{n−j} < g_j < 2^{n−j+1} for j=1,…,n and
0 < g_{n+1} < 1, and Σ g_j = 2^n. These exist: set g_j = 2^{n−j} + δ_j (δ_j>0 tiny,
Σ_{j≤n} δ_j < 1); then Σ_{j=1}^n g_j = (2^n − 1) + Σδ_j, so g_{n+1} = 2^n − Σ_{j≤n} g_j =
1 − Σδ_j ∈ (0,1). The merged sorted order is
    g_1 > 2^{n−1} > g_2 > 2^{n−2} > … > g_n > 2^0 > g_{n+1},
because g_j ∈ (2^{n−j}, 2^{n−j+1}) forces 2^{n−j+1} > g_j > 2^{n−j}. Thus g_j sits at rank
2j−1 (odd) and the intact 2^{n−j} at rank 2j (even), and g_{n+1} at rank 2n+1 (odd). So the
odd ranks are exactly the fragments: O = Σ g_j = 2^n, and E = ΣI = 2^n − 1. This uses all
n cuts (n+1 fragments). Hence in the confined case **min O ≤ 2^n**; §4.2.3–4.2.5 prove the
matching lower bound O ≥ 2^n in the cases we can close. ∎

#### 4.2.3 The rank-swap lemma — PROVED
**Lemma S.** Let two pieces occupy consecutive ranks r, r+1 with values x > y, and suppose x
is decreased continuously past y (all other pieces fixed), so at x = y they swap ranks.
Just after the swap (x < y, x now at rank r+1, y at rank r) versus just before,
    ΔO = (−1)^{r+1}·(y − x).
*Proof.* Only ranks r, r+1 are affected. Before: value x at rank r, y at rank r+1. After:
y at rank r, x at rank r+1. O sums the odd ranks. If r is odd: before, x ∈ O; after, y ∈ O;
ΔO = y − x. If r is even: before, y (rank r+1, odd) ∈ O; after, x (rank r+1) ∈ O;
ΔO = x − y. Combining, ΔO = (−1)^{r+1}(y − x). ∎

**Consequence (boundary crossing).** When a fragment f (value x) at an ODD rank r crosses
BELOW an intact I (value y = I) at rank r+1 (so x decreases past I), r is odd and
ΔO = (I − f) > 0 at the crossing: O strictly increases. This is the mechanism by which
leaving the interleaving pattern (fragments odd, intacts even) raises O. It gives a rigorous
proof that the interleaving pattern is a **local** minimum; promoting this to a **global**
minimum for all fragmentations is the remaining content (see GAP L1).

#### 4.2.4 Top-fragment cascade — PROVED (closes the case "a fragment dominates")
Work with the **generalised** statement, which is what the recursion needs:

  **G-L1(n): for intacts I_n = {2^0,…,2^{n−1}} and any finite multiset F with |F| ≤ n+1 and
  ΣF ≤ 2^n, one has E(I_n ∪ F) ≤ ΣI_n = 2^n − 1.**

(The confined case of §4.2 is G-L1(n) with ΣF = 2^n exactly. G-L1 was checked with 8·10^5
random configs for n ≤ 4: no violation.) Because E(I_n ∪ F) is a continuous function of the
multiset of pieces, it suffices to prove G-L1 on the dense set of configurations with all
piece-values distinct; the general case follows by taking limits. So assume distinct values.

Let a = #{fragments > 2^{n−1}}. By §4.2.1, a ≤ 1.

**Case a = 1 (the top piece is a fragment).** One fragment f_1 > 2^{n−1} is the unique
largest piece (rank 1, odd); every other piece is < 2^{n−1}, so the intact 2^{n−1} is the
second largest (rank 2, even). Delete both r_1 = f_1 and r_2 = 2^{n−1}: every remaining piece
drops in rank by exactly 2, so **parities are preserved**, and
    E(I_n ∪ F) = 2^{n−1} + E(I_{n−1} ∪ F′),   F′ = F ∖ {f_1}.
Now |F′| ≤ n and ΣF′ = ΣF − f_1 ≤ 2^n − f_1 < 2^n − 2^{n−1} = 2^{n−1}. Thus (I_{n−1}, F′)
satisfies the hypotheses of G-L1(n−1) (count ≤ n = (n−1)+1, sum ≤ 2^{n−1}), so
E(I_{n−1} ∪ F′) ≤ ΣI_{n−1} = 2^{n−1} − 1. Hence E(I_n ∪ F) ≤ 2^{n−1} + 2^{n−1} − 1 = 2^n − 1
= ΣI_n. ∎ (Case a = 1.)

So **whenever the largest piece at every level of the recursion is a fragment, G-L1 closes.**
The base is n = 0 (I_0 = ∅, F with |F| ≤ 1, ΣF ≤ 1, so E = 0 ≤ 0). The only obstruction is
the first level at which a = 0 (no fragment exceeds the top intact); that residual case is
GAP L1 below.

#### 4.2.5 Base cases n = 1, 2 of the confined lower bound — PROVED
See §7: n=1 is proved in full (both bounds); n=2 confined case is proved by the finite case
analysis there. These are the base of the induction and are unconditional.

#### 4.2.6 Route A: the confined lower bound as a minimisation — REDUCTION PROVED, one residual

We recast the confined bound as an optimisation and reduce it to a single crisp inequality on
the extreme configurations. Throughout, A = O − E is the alternating sum of the merged sorted
list, and (units of §3) the target O ≥ 2^n is **A ≥ 1** (since O + E = D = 2^{n+1}−1 and
A = 2O − D, so O ≥ 2^n ⟺ A ≥ 2·2^n − D = 1). By Lemma R, A = μ{t : N(t) odd}.

**Padding to a fixed shape.** In the confined case there are k+1 = m ≤ n+1 fragments summing to
2^n. Add n+1 − m dummy fragments of length 0; this appends pieces of value 0 at the bottom of
the sorted list, changing neither the odd-sum O nor A (a value-0 piece contributes 0 and, sitting
below every positive piece, shifts no positive piece's rank). So it suffices to prove A ≥ 1 over

  **Δ := { (g_1,…,g_{n+1}) : g_i ≥ 0, Σ g_i = 2^n }**   (intacts I = {2^0,…,2^{n−1}} fixed),

the compact simplex of exactly n+1 nonnegative fragments summing to 2^n. The count bound
"≤ n+1 fragments" is *built into Δ* (dimension n+1); it is load-bearing — allowing n+3 fragments,
A can drop to ≈ 0 (machine-checked: min A ≈ 0.01 for n=2, 0.10 for n=3, 0.28 for n=4 with
m ≤ n+3), so any argument must use that Δ has exactly n+1 slots.

**A is continuous and piecewise-linear on Δ.** Write A = Σ_pieces v·(−1)^{#pieces strictly above v}.
On each cell of Δ — a maximal region on which the sorted order of the 2n+1 pieces is fixed — the
count "#pieces above" is constant for every piece, so A is an *affine* function of (g_1,…,g_{n+1})
there; across cell walls (two pieces swapping) A is continuous (Lemma S: the jump is ±(y−x) and
vanishes at the wall x = y). Hence A is continuous and piecewise-affine on the compact Δ, and

    min_Δ A is attained, and (A affine on each cell) is attained at a **vertex** of the cell
    complex — a point where n of the constraints {g_i = g_j}, {g_i = 2^s}, {g_i = 0} are tight.

**min_Δ A ≤ 1 (interleaving).** The interleaving config of §4.2.2 lies in Δ and has A = 1.

**Reduction of L1 to the vertex inequality.** Therefore

  **the confined lower bound A ≥ 1 is equivalent to: A(vertex) ≥ 1 at every vertex of the
  Δ-cell-complex.** (★)

**What is proved of (★).**
- *Interleaving cell.* On the whole interleaving cell A ≡ 1 (constant): there each g_j is the
  unique odd-rank piece 2j−1 and each intact 2^{n−j} the even rank 2j, so
  A = Σ_j g_j − Σ_j 2^{n−j} = 2^n − (2^n−1) = 1 regardless of the exact g_j. Its vertices satisfy
  (★) with equality.
- *Case a = 1 vertices* (a fragment exceeds 2^{n−1}). Handled by the **top-fragment cascade**
  (§4.2.4): peeling the pair (top fragment, 2^{n−1}) preserves parities and drops to G-L1(n−1),
  giving A ≥ 1. So every vertex with a fragment > 2^{n−1} satisfies (★).
- *Lemma S* certifies that the interleaving is a strict **local** minimum: any single wall-crossing
  away from it raises A by 2(I − f) > 0.

#### 4.2.7 The a = 0 case: dyadic two-case split + no-donor closer — PROVED (confined case)

We prove **A ≥ 1 on all of Δ**, closing the confined lower bound. Recall a ≤ 1 (fragment-count
bound §4.2.1), so Δ = {a=1} ∪ R with R := {g ∈ Δ : g_i ≤ 2^{n−1} ∀i}. On the a=1 part A ≥ 1
(top-fragment cascade §4.2.4). It remains to prove **A ≥ 1 on R.** We state the split for n ≥ 3
and cite §7 for n ≤ 2 (there 2^{n−2} = 1 coincides with the smallest intact and the base cases are
proved directly). Write m = #{positive fragments} (2 ≤ m ≤ n+1); the positive pieces are the n
intacts and the m positive fragments, N_tot := n + m in total (value-0 padding fragments sit below
everything and change neither ranks of positive pieces nor A, by Lemma X, so we ignore them).

This section **removes** the round-5 "a receiver always exists" claim, which the round-5 reviewer
refuted at clustered configs ({2,10/3,10/3,11/3,11/3}, {2,7/2,7/2,7/2,7/2} for n=4, which have no
receiver). Those two configs have max fragment 11/3, 7/2 ≤ 4 = 2^{n−2}, so they land in **Case 1
below**, where A ≥ 2^{n−2} = 4 directly — no receiver needed.

**Directional derivative of A under a mass transfer (recalled).** For a value v write
G(v) = #{pieces > v}, Geq(v) = #{pieces ≥ v}. Since A is piecewise-affine (§4.2.6), the transfer
e_a − e_b (fragment a up, fragment b down) has one-sided derivative
    A′₊(e_a − e_b) = (−1)^{G(g_a)} + (−1)^{Geq(g_b)}.
(After an up-move a lands at rank G(g_a)+1, sign (−1)^{G(g_a)}; after a down-move b lands at rank
Geq(g_b), sign −(−1)^{Geq(g_b)+1} = (−1)^{Geq(g_b)}.) Call a **receiver** a fragment with G odd, a
**donor** a positive fragment with Geq odd; a valid (receiver, distinct positive donor) pair gives
A′₊ = −2 < 0.

A is continuous on the compact R, so **min_R A is attained** at some v. We show A(v) ≥ 1 by a
dichotomy on the largest fragment w_1 of v. In R the intacts other than 2^{n−1} are all ≤ 2^{n−2},
every fragment is ≤ 2^{n−1}, so the top piece is the intact v_1 = 2^{n−1}.

**Case 1 (w_1 ≤ 2^{n−2}) — direct.** Then the second-largest piece is v_2 = max(2^{n−2}, w_1)
= 2^{n−2} (every non-top intact ≤ 2^{n−2} and every fragment = w_1 ≤ 2^{n−2}). Since the sorted
alternating sum A = (v_1 − v_2) + (v_3 − v_4) + ⋯ has every bracket ≥ 0 and any leftover last term
≥ 0,
    A(v) ≥ v_1 − v_2 = 2^{n−1} − 2^{n−2} = 2^{n−2} ≥ 1   (n ≥ 3 gives ≥ 2). ✓

**Boundary (w_1 = 2^{n−1}) — a=1 closure.** If the max fragment equals 2^{n−1}, then since
Σ fragments = 2^n > 2^{n−1} there is a second positive fragment; borrowing ε from it and adding to
the 2^{n−1}-fragment gives configs in Δ with a fragment > 2^{n−1} (the a=1 region, where A ≥ 1 by
the cascade §4.2.4), converging to v. By continuity of A, A(v) ≥ 1. ✓

**Case 2 (2^{n−2} < w_1 < 2^{n−1}) — the max fragment is a named receiver.** The pieces strictly
above w_1 are: intacts (only 2^{n−1}, as all other intacts ≤ 2^{n−2} < w_1) and fragments (none,
w_1 is the max fragment). So **G(w_1) = 1 (odd): w_1 is a receiver**, unconditionally — a specific
named fragment whose parity is forced by counting, not an existence claim. (This is the fix: at the
round-5 counterexamples w_1 ≤ 2^{n−2}, i.e. Case 1, so no receiver is ever asserted there.)

*Minimality forces no donor.* For every positive fragment b that is a distinct piece from w_1, the
direction e_{w_1} − e_b is feasible in R (w_1 < 2^{n−1} can increase; b > 0 can decrease). As v
minimises, A′₊(e_{w_1} − e_b) = (−1)^{G(w_1)} + (−1)^{Geq(b)} = −1 + (−1)^{Geq(b)} ≥ 0, forcing
**Geq(b) even**. If w_1 has multiplicity ≥ 2, taking b a second copy of w_1 gives Geq(w_1) even as
well; if w_1 has multiplicity 1 then Geq(w_1) = G(w_1)+1 = 2 is even anyway. Hence **no positive
fragment is a donor** (all have Geq even).

*Closing Case 2 from "no donor".* Let f_min be the smallest positive fragment value; N_tot = n + m.
  - **(2a) N_tot odd.** If f_min were the global minimum piece then Geq(f_min) = N_tot is odd, a
    donor — excluded. So the global minimum piece is an intact, necessarily the smallest intact 2^0
    = 1, and **all fragments exceed 1**. Thus 1 is the unique global minimum, at rank N_tot (odd),
    contributing +1 to A; the remaining N_tot − 1 (even count) sorted pieces have alternating sum
    A′ = Σ_j (r_{2j−1} − r_{2j}) ≥ 0. Hence A(v) = A′ + 1 ≥ 1. ✓
  - **(2b) N_tot even and f_min > 1.** Then all fragments exceed 1. Consider the transfer
    e_{w_1} − e_{f_min}: A′₊ = −1 + (−1)^{Geq(f_min)} = 0 (no donor), so A is flat initially. As
    f_min decreases it first meets the largest intact I* < f_min (which exists, since 1 < f_min);
    just past that wall Geq(f_min) has increased by 1 (I* now counted), turning A′₊ into −1 + (−1)^{odd}
    = −2. If w_1 has not yet reached 2^{n−1}, this point (feasible: w_1 < 2^{n−1} up, f_min = I* > 0
    down) has A < A(v), contradicting minimality; so this sub-case cannot occur unless w_1 reaches
    2^{n−1} first, in which case A(v) = A(that point) ≥ 1 by a=1 closure. Either way (2b) yields
    A(v) ≥ 1 (or is impossible). ✓
  - **(2c) N_tot even and f_min ≤ 1.** Then f_min is the global minimum piece and Geq(f_min) = N_tot
    is even (consistent with no-donor). The transfer e_{w_1} − e_{f_min} has A′₊ = −1 + (−1)^{N_tot}
    = 0: **a flat direction**, and — crucially — as f_min decreases toward 0 it crosses **no**
    positive piece (nothing lies in (0, f_min) except padding-zeros), so Geq(f_min) stays even and A
    stays exactly A(v) along the whole ray, until the first exit event:
      · w_1 reaches 2^{n−1} first ⟹ a=1 closure, A(v) = A(exit) ≥ 1; or
      · f_min reaches 0 first ⟹ a point v′ ∈ R with A(v′) = A(v) = min_R A and **one fewer positive
        fragment** (m − 1). So v′ is also a global minimiser, and N_tot(v′) = n + (m−1) is **odd**.

**Well-foundedness / termination of the flat move (2c).** Assign each global minimiser the integer
weight m = #{positive fragments} ∈ {2, …, n+1}. The flat move of (2c) sends a minimiser v to a
minimiser v′ with strictly smaller weight (m ↦ m−1). This is a strictly decreasing sequence of
non-negative integers, hence terminates after finitely many (≤ n) steps. At the terminal minimiser
one of Case 1, the a=1 boundary, or Case 2 with N_tot odd (sub-case 2a) applies — indeed the very
first flat step already flips N_tot from even to odd, so at v′ either Case 1 / a=1 hold (A ≥ 1) or
Case 2 applies with N_tot odd, closed by (2a). In every terminal state A = A(v) ≥ 1. (No infinite
regress: m ≥ 2 is a floor, and at m = 2 two fragments ≤ 2^{n−1} summing to 2^n force both = 2^{n−1},
the a=1 boundary, A ≥ 1.) ✓

Therefore A(v) ≥ 1 in Case 1, Case 2 (all sub-cases), and on the w_1 = 2^{n−1} boundary — an
exhaustive dichotomy on w_1 ∈ (0, 2^{n−1}]. Hence **min_R A ≥ 1**, and with the a=1 cascade,
**A ≥ 1 on all of Δ**: the confined lower bound O ≥ 2^n holds for all n ≥ 3 (n ≤ 2 by §7). ∎

**What is closed vs. open (lower bound).** The **confined** lower bound (all of XY's cuts inside
R_n) is now fully closed: the two-case split removes the false universal-receiver claim, and the
flat-move (2c) is closed by an explicit strictly-decreasing well-foundedness weight — the round-5
"degenerate flat-move face" loose end is gone. The remaining lower-bound item is **L2** (§4.4): XY
spending one or more cuts *outside* R_n (fragmenting an intact R_j, j < n). §4.4 reduces this to the
same vertex inequality on an augmented simplex but the exchange step (a stray cut cannot beat the
confined optimum) is not fully written; this is the sole remaining lower-bound residual.

### 4.4 L2 — XY spends cuts outside R_n (stray cuts). PARTIAL: reduced to the augmented a=0 closer.

By the dichotomy of §4, the only remaining lower-bound regime is: XY cuts R_n (k_n ≥ 1 cuts inside
R_n) **and** places s ≥ 1 stray cuts outside R_n (spare-R_n, k_n = 0, is closed in §4.1; the confined
case s = 0 is certified in §4.2.7 / `DyadicLower-confined`). This section (round 7) reduces the stray
regime, by a clean induction, to a **single residual** — the augmented a = 0 closer — and closes every
other branch rigorously. It does NOT fully close L2; the residual is flagged honestly at the end.

**Round-7 numerical status (support only, not a proof).** Over 4·10^5+ stray configs each for
n = 2,3,4,5, including CLUSTERED / tie-laden splits, min A ≥ 1 with 0 violations; the infimum equals 1
and is approached only as a stray sub-piece → 0 (recovering the confined interleaving), never attained
strictly inside the stray region. So the bound A ≥ 1 is **true and tight** on the stray region; the
work is a rigorous proof.

#### 4.4.1 Setup and the reformulated target — PROVED

Fix any stray placement (k_n ≥ 1 cuts in R_n, s ≥ 1 stray cuts among the intacts). Group the pieces:

- **F** = the k_n + 1 fragments of R_n, ΣF = 2^n. (Budget: k_n + s ≤ n, so k_n + 1 ≤ n − s + 1 ≤ n.)
- **G** = the non-R_n pieces. Each intact R_j = 2^j (j ≤ n−1) that receives c_j ≥ 0 stray cuts is
  replaced by a partition of 2^j into c_j + 1 nonnegative sub-pieces; Σ_j c_j = s. Thus
  |G| = n + s and **ΣG = Σ_{j<n} 2^j = 2^n − 1** (unchanged from the intacts). Each G-piece is
  ≤ 2^{n−1}, with value exactly 2^{n−1} only when R_{n−1} is uncut.

Sort all T = (k_n+1) + (n+s) pieces weakly decreasing. With total mass ΣF + ΣG = 2^n + (2^n − 1) = D,
the identity A = O − E and O + E = D give **A = D − 2E**, so

  **A ≥ 1  ⟺  E ≤ (D − 1)/2 = 2^n − 1 = ΣG.**   (†)

That is, the stray lower bound is exactly: *the even-rank sum is at most the total non-R_n mass.* This
is the clean unifying target; the confined case (`DyadicLower-confined`) is the same statement with G =
the intacts. **Warning (verified numerically, round 7):** (†) FAILS if G is an arbitrary multiset of
n+s pieces summing to 2^n − 1 (min A drops to ≈ 0.08 for n=3), and it FAILS if F is allowed
unboundedly many pieces (max(E − ΣG) ≈ 0.43 for n=3 with the budget removed). So the proof must use
**both** the dyadic structure of G **and** the cut budget k_n + s ≤ n; neither alone suffices.

#### 4.4.2 The augmented minimisation and vertex reduction — PROVED

Fix the combinatorial data (which intacts are cut, into how many pieces; k_n). The configuration space
is the product of simplices  P = Δ_F × ∏_j Δ_{G,j},  Δ_F = {ΣF = 2^n, ≥ 0},
Δ_{G,j} = {sub-pieces of R_j sum to 2^j, ≥ 0}, a compact polytope. As in §4.2.6, A = μ{N odd} is
continuous and piecewise-affine on P: on each cell of the sorted-order hyperplane arrangement the
rank of every piece is fixed, so A is affine there, and across a wall (two pieces swapping) A is
continuous by Lemma S (the jump ±(y−x) vanishes at x=y). A bounded affine function on a bounded cell
attains its minimum at a 0-cell, so **min_P A is attained at a vertex of the arrangement** (KB:
*piecewise-affine minimisation attains its optimum at a vertex of the cell complex*). There are
finitely many combinatorial data, so the stray minimum is a minimum over finitely many such P's.

#### 4.4.3 The unifying statement GDL(n) and its induction skeleton — REDUCTION PROVED

**GDL(n).** Let the intacts {2^0,…,2^{n−1}} be partitioned by a total of s ≥ 0 stray cuts into a
multiset G (|G| = n + s, ΣG = 2^n − 1, each piece ≤ 2^{n−1}), and let F be any multiset with
ΣF ≤ 2^n and k_n + s ≤ n where |F| = k_n + 1. Then **E(F ∪ G) ≤ ΣG**, equivalently A ≥ ΣF − ΣG
(≥ 1 when ΣF = 2^n).

The confined case s = 0 (G = the intacts) is exactly `DyadicLower-confined`, hence GDL(n) holds when
s = 0. We prove GDL(n) for s ≥ 1 by strong induction on n (base n ≤ 2 is a finite check; verified
numerically min A = 1). Take a minimiser v of A over the augmented space (§4.4.2). Let f_1 = max
R_n-fragment; by the fragment-count bound §4.2.1, at most one R_n-fragment exceeds 2^{n−1} (write
a ∈ {0,1} for their count). Sort v_1 ≥ v_2 ≥ ….

**Branch a = 1, R_{n−1} uncut — CLOSED.** The unique fragment f_1 > 2^{n−1} is the strict maximum
(every other R_n-fragment < 2^{n−1} since two would sum past 2^n; every G-piece ≤ 2^{n−1}, with = only
at the uncut 2^{n−1}). Since R_{n−1} is uncut, 2^{n−1} is present and is the unique second piece (all
others < 2^{n−1}). Peel the pair (f_1 at rank 1, 2^{n−1} at rank 2): every remaining piece drops in
rank by 2, so parities are preserved and E(F ∪ G) = 2^{n−1} + E(rest). Here rest = (F ∖ f_1) ∪
(intacts {2^0,…,2^{n−2}} with their stray cuts): ΣF' = 2^n − f_1 < 2^{n−1}, |F'| = k_n; the remaining
intacts are the dyadic set for n−1, cut a total of s times with (k_n − 1) + s ≤ n − 1 cuts. So rest is
a valid GDL(n−1) instance, and by induction E(rest) ≤ 2^{n−1} − 1. Hence
E(F ∪ G) ≤ 2^{n−1} + (2^{n−1} − 1) = 2^n − 1 = ΣG. ✓

**Branch v_1 = 2^{n−1} (R_{n−1} uncut) and v_2 ≤ 2^{n−2} — CLOSED.** Every bracket of the sorted
alternating sum is ≥ 0, so A ≥ v_1 − v_2 ≥ 2^{n−1} − 2^{n−2} = 2^{n−2} ≥ 1 (n ≥ 3). ✓ (This is the
augmented "Case 1"; it needs only the top gap, no minimality.)

**Count Lemma (structural, holds at every stray config) — PROVED.** Not all n + s non-R_n pieces can
sit at even ranks. Indeed if they did, every odd-rank piece would be an R_n-fragment, so the number of
odd ranks ⌈T/2⌉ ≤ k_n + 1; but ⌈T/2⌉ ≥ T/2 = ((k_n+1) + (n+s))/2, giving n + s ≤ k_n + 1 ≤ n − s + 1,
i.e. 2s ≤ 1, contradicting s ≥ 1. Hence **at least one non-R_n piece occupies an odd rank.** This
forbids the exact interleaving pattern (all intacts at even ranks, which is the unique A = 1 confined
optimum, §4.2.2) once any cut is spent outside R_n — the tie is structurally unreachable in the
stray region. (This yields A > 0 / "no strict tie", NOT A ≥ 1; the ≥ 1 must come from the dyadic
per-branch bounds above and the residual closer below. Do not overclaim from the count.)

#### 4.4.4 The residual — the augmented a = 0 closer (HONESTLY OPEN)

The branches of §4.4.3 close every top-structure EXCEPT the **augmented a = 0 case**: no R_n-fragment
exceeds 2^{n−1}, i.e. all pieces ≤ 2^{n−1}, and we are not in "v_1 = 2^{n−1} with v_2 ≤ 2^{n−2}". Two
sub-shapes remain:

- **(R2) R_{n−1} uncut, v_2 = w_1 (max R_n-fragment) ∈ (2^{n−2}, 2^{n−1}).** Then only the intact
  2^{n−1} lies above w_1, so G(w_1) = 1 (odd): w_1 is a **named receiver** (as in confined Case 2).
  Minimality over the R_n-fragment group forces no R_n-fragment donor (Geq even). In the CONFINED
  proof the closer then split on the parity of N_tot and used that the global-minimum piece is the
  intact 1 (contributing +1 at the bottom odd rank). **The obstruction in the augmented setting:** if
  R_0 = 1 (or another small intact) is stray-cut, the bottom piece is a *tiny sub-piece* ε, so "+1 at
  the bottom odd rank" becomes "+ε", and the confined (2a) closer breaks. The flat-move monovariant
  (2c) must also be re-established with donors restricted to a piece's own cut-group (moves cannot
  transfer mass between R_n and an intact, since each group's sum is fixed) — this group restriction
  is not present in the confined proof and is not yet discharged.

- **(R1') R_{n−1} cut, so v_1 < 2^{n−1}.** The top piece is a cut-R_{n−1} sub-piece or an R_n-fragment
  in (2^{n−2}, 2^{n−1}); the clean "v_1 = 2^{n−1}" structure used in both closed branches is gone, and
  the top-gap bound A ≥ v_1 − v_2 can be < 1. Handled at a minimiser it should again reduce by the
  augmented Case-2 machinery, but that machinery is exactly the unresolved (R2) closer.

**Precise statement of the gap.** L2 is now reduced to: *prove GDL(n) at the augmented a = 0
minimiser* (branches (R2)+(R1')), i.e. the DyadicLower Case-2 closer generalised to (i) donors
restricted to within a fixed-sum cut-group and (ii) the possibility that the global-minimum piece is a
tiny stray sub-piece rather than the intact 1. Every other branch (a = 1 with R_{n−1} uncut; the
top-gap Case 1; the confined base s = 0 via `DyadicLower-confined`; base n ≤ 2) is closed and feeds a
clean induction on n. Round-7 progress: the reformulation (†), the augmented vertex reduction, the
GDL(n) induction skeleton, and the Count Lemma are new and rigorous; the a = 0 closer is the sole
remaining lower-bound obstruction.

**Dead ends confirmed (do not retry).** (i) The pointwise exchange "removing/adding a stray cut
weakly raises A for fixed R_n cuts" is FALSE (716/17980 violations, round-7 explorer): L2 cannot be
routed through a monotone stray↔confined swap. (ii) The relaxed target (†) with G an arbitrary
multiset, or with F unbounded in count, FAILS — the dyadic structure of G and the budget are both
load-bearing.

#### 4.4.5 Round-8 progress on the augmented a=0 closer — T-parity framing (PARTIAL)

This round attacks the closer with the T-parity / interleaving framing (genuinely different from the
DyadicLower receiver/donor route: no cross-group transfer, and the reduction below is a majorisation /
layer-cake argument). It contributes **new, rigorous, reusable reductions** and closes a genuine slice,
but does **not** fully close the residual; the honest residual is stated precisely at the end.

Throughout, all pieces are positive, all ≤ 2^{n−1} (the a=0 hypothesis), F = R_n-fragments
(|F| = k_n+1, ΣF = 2^n), G = non-R_n pieces (|G| = n+s, ΣG = 2^n − 1, dyadic refinement of the
intacts), T = |F|+|G|. Sort the T pieces weakly decreasing. For a threshold x ≥ 0 write
N_F(x)=#{F-pieces > x}, N_G(x)=#{G-pieces > x}, N(x)=N_F(x)+N_G(x).

**(A) A sharper reformulation: A ≥ 1 ⟺ E_F ≤ O_G — PROVED.**
Split the odd- and even-rank sums by group: O = O_F + O_G, E = E_F + E_G (subscript = group of the
piece at that rank; well-defined once a tie-break is fixed). Then E = E_F + E_G and ΣG = O_G + E_G, so
E − ΣG = E_F − O_G, and this difference is **independent of the tie-break** (E and ΣG are). Since
A = D − 2E (§4.4.1), 
  **A ≥ 1  ⟺  E ≤ ΣG  ⟺  E_F ≤ O_G**  (even-rank fragment mass ≤ odd-rank G mass).   (‡)
This is (†) re-expressed intrinsically as a competition between *the fragments landing at even ranks*
and *the G-pieces landing at odd ranks* — exactly the quantities the interleaving construction trades.

**(B) All-F-odd sufficiency — PROVED (immediate).** If every F-piece is at an odd rank then E_F = 0,
so by (‡) A ≥ 1 (in fact A = 1 + 2 O_G, recovering the explorer identity). More generally any config
with E_F = 0 has A ≥ 1 unconditionally.

**(C) Injection / majorisation lemma (Case I) — PROVED.** *If N_F(x) ≤ N_G(x) + 1 for all x ≥ 0, then
A ≥ 1.* 
*Proof.* By Lemma R (certified), E = ∫_0^∞ ⌊N(x)/2⌋ dx and ΣG = ∫_0^∞ N_G(x) dx. The hypothesis gives
N(x) = N_F(x)+N_G(x) ≤ 2N_G(x)+1, so ⌊N(x)/2⌋ ≤ ⌊(2N_G(x)+1)/2⌋ = N_G(x) for every x. Integrating,
E ≤ ΣG, hence A = D − 2E ≥ D − 2ΣG = (2^{n+1}−1) − 2(2^n−1) = 1. ∎
(Interpretation: N_F ≤ N_G+1 is the Hall/majorisation condition under which each even-rank piece can be
matched to a distinct ≥-large G-piece. It holds whenever F is not "clustered above" G — e.g. whenever no
threshold is exceeded by ≥ 2 more fragments than G-pieces. It is genuinely different from the
receiver/donor machinery.)

**(D) Minimiser analysis — the receiver move (PARTIAL).** Take a global minimiser v of A over the
compact a=0 region. Using the tie-valid one-sided directional derivative certified in
`DyadicLower-confined`, for F-pieces a (with g_a < 2^{n−1}, hence increasable) and b (with g_b > 0),
minimality forces A′₊(e_a − e_b) = (−1)^{G(g_a)} + (−1)^{Geq(g_b)} ≥ 0. Consequently: **if the smallest
fragment b_0 has Geq(g_{b_0}) odd, then every fragment a has G(g_a) even, i.e. every fragment is at an
odd rank, so E_F = 0 and A(v) ≥ 1 by (B).** Now Geq(g_{b_0}) = T − β where β = #{G-pieces < g_{b_0}}
(all pieces below the smallest fragment are G-pieces). Hence this branch closes **whenever T − β is odd**
— in particular the pure T-odd case with no G-piece below the smallest fragment (β = 0), which is the
explorer's certified n=3 anchor.

**(E) HONEST RESIDUAL — the tight clustered minimiser.** The numerics (round-8, n=3,4,5, exact search)
show the true minimiser has **E_F > 0** (a fragment sits at an *even* rank) with **E_F ≈ O_G** (‡ nearly
tight): e.g. n=3, s=1 gives fragment ranks {2,3,5}, E_F ≈ 4 ≈ O_G. So the clean routes (B),(C) do NOT
describe the minimiser, and in (D) the minimiser falls in the complementary parity T − β even, where the
receiver move is blocked because the increasable fragment is tied to the G-piece directly above it (a
vertex of the arrangement). This is **exactly** the confined-case (2b)/(2c) flat-move obstruction,
now with the extra features that (i) the compensating donor must lie in the same fixed-sum group and
(ii) the bottom piece may be a tiny stray sub-piece. **The within-group flat-move termination for this
tight residual is not discharged this round.** It is the sole remaining lower-bound gap. Refuted this
round as insufficient on their own: (B) all-F-odd and (C) N_F ≤ N_G+1 — both FAIL at the true minimiser
(E_F > 0, and F is clustered so N_F can exceed N_G+1). The correct next step is the within-group
flat-move monovariant on the *tight* face E_F = O_G, not a majorisation bypass.

---

## 5. The interleaving lemma — PROVED

**Lemma I.** Suppose the current pieces are b > a_2 ≥ … ≥ a_p with b > a_2 + … + a_p. Then a
player with p−1 spare marks can cut b so that the p fragments of b occupy exactly the odd
ranks 1,3,…,2p−1 and a_2,…,a_p occupy the even ranks; hence O = b.

*Proof.* Let Δ = b − Σ_{i≥2} a_i > 0. Fix ε with 0 < ε < min(Δ/(p−1), min_{a_i>a_{i+1}}
(a_i − a_{i+1})) and small enough that s_p (below) satisfies s_p ≤ a_p. Cut b into
s_i = a_{i+1} + ε (i=1,…,p−1) and s_p = b − Σ_{i<p} s_i = Δ − (p−1)ε > 0 (p−1 cuts,
Σ s_i = b). Then s_1 = a_2 + ε > a_2; for 2 ≤ i ≤ p−1, a_i ≥ a_{i+1}+ε = s_i > a_{i+1}; and
s_p = Δ − (p−1)ε ≤ a_p (the condition on ε). Sorted:
s_1 > a_2 > s_2 > a_3 > … > a_p ≥ s_p. Odd ranks are s_1,…,s_p; by Lemma G1, O = Σ s_i = b. ∎

Lemma I needs both b > Σ_{i≥2} a_i and the residual fit s_p ≤ a_p (a large b is first reduced
by halving). When p−1 ≤ n and both hold, XY forces O = b = a_1.

---

## 6. Upper bound: XY holds LB to ≤ 2^n/D

LB's pieces are a_1 ≥ … ≥ a_p (p ≤ n+1), Σ = 1; XY has ≤ n marks. Target O ≤ 2^n/D.

### 6.1 Lemma H (halve the p−1 largest) — PROVED, closes Case A

**Lemma H.** XY cuts each of the p−1 largest LB pieces a_1,…,a_{p−1} at its midpoint (this is
p−1 ≤ n cuts, within budget) and leaves the smallest piece a_p intact. Then
    **O = 1/2 + a_p/2.**

*Proof.* The 2p−1 resulting pieces are the p−1 equal pairs {a_i/2, a_i/2} (i=1,…,p−1) and the
singleton a_p. It suffices to prove the formula on the dense set where all values are distinct
except for the intended pairs (a_i ≠ a_j and a_i/2 ≠ a_p for all i≠j); the general case
follows by continuity of O in the pieces.

Under distinctness each pair {a_i/2, a_i/2} consists of two equal values, and since no other
piece lies strictly between them (all other values differ from a_i/2), the two copies occupy
two CONSECUTIVE ranks r, r+1. Consecutive ranks carry opposite signs in the alternating sum
A = Σ_ρ (−1)^{ρ+1} r_ρ, so each pair contributes (−1)^{r+1}a_i/2 + (−1)^{r+2}a_i/2 = 0 to A.

Now locate the singleton a_p. Exactly k := #{i : a_i/2 > a_p} pairs lie entirely above a_p,
i.e. 2k pieces precede a_p, so a_p occupies rank 2k+1, which is **odd**. It contributes
(−1)^{2k+2}a_p = +a_p to A. All pairs (whether above or below a_p) contribute 0. Hence
A = a_p, and O = (1 + A)/2 = 1/2 + a_p/2. ∎ (Machine-verified n=1,2,3,4.)

**Corollary (Case A).** If **a_p ≤ 1/D** then
    O = 1/2 + a_p/2 ≤ 1/2 + 1/(2D) = (D+1)/(2D) = 2^{n+1}/(2D) = 2^n/D = c(n).
So Case A (smallest LB piece ≤ 1/D) is fully closed for all n, and equality holds at the
geometric config (a_p = 1/D). ∎

### 6.2 Case B (all pieces > 1/D) — the remaining hard core (GAP U1)

Here a_p > 1/D, so ALL p pieces exceed 1/D and Σ = 1 forces p ≤ D and a_1 ≤ 1 − (p−1)/D.

**B0 (n=1) — PROVED vacuous.** If n=1 and Case B holds, then p=2 and a_2 > 1/3, so
a_1 = 1 − a_2 < 2/3 = c(1). With two pieces O = a_1 < c(1); XY passes (0 cuts). ✓ (This is
why the two cases meet cleanly at n=1; see §7.)

**B1 (a_1 > 1/2, dominant piece).** If a_1 > 1/2 ≥ Σ_{i≥2} a_i, Lemma I applies:
  • if a_1 ≤ c(n), XY spends p−1 ≤ n cuts to force O = a_1 ≤ c(n) — **fully closed by Lemma I.**
  • if a_1 > c(n), XY first halves a_1 (1 cut), then plays the pair-creation sub-game below.

**B1-large (a_1 > c(n)) via pair-creation — base cases PROVED, general step OPEN.** Halving a_1
(1 cut) creates the pair {a_1/2, a_1/2}, which by the pair-cancellation of Lemma H contributes 0
to the alternating sum A. The remaining pieces are the singletons {a_2,…,a_p} with
S := Σ_{i≥2} a_i = 1 − a_1 < 1 − c(n) = 1 − 2^n/D = (2^n − 1)/D, all > 1/D (Case B), and XY has
p−1 ≤ n−1 cuts left. So B1-large reduces to:

  **IH(q): for q pieces b_1 ≥ … ≥ b_q, all > 1/D, with S = Σ b_i < (2^q − 1)/D, XY can force
  A ≤ 1/D using ≤ q−1 cuts** (whence O = 1/2 + A/2 ≤ 1/2 + 1/(2D) = c(n)).

Here q = p−1 ≤ n. We prove IH(q) for q = 1, 2, 3 rigorously; the general inductive step is the
open core (GAP U1).

*IH(1).* One piece b_1 with b_1 = S < 1/D and 0 cuts. Then it is a lone singleton at rank 1, so
A = b_1 < 1/D. ✓

*IH(2).* Two pieces b_1 ≥ b_2 > 1/D, S = b_1 + b_2 < 3/D, 1 cut. XY cuts b_1 at b_2, creating the
pair {b_2, b_2} (contributes 0 to A) and the singleton b_1 − b_2. Since b_1 = S − b_2 < 3/D − b_2
and b_2 > 1/D, we get b_1 − b_2 < 3/D − 2b_2 < 3/D − 2/D = 1/D. By Lemma H's pair-cancellation
(one singleton b_1 − b_2 ≥ 0 lands at an odd rank, the pair cancels), A = b_1 − b_2 < 1/D. ✓
1 cut used. ✓

*IH(3).* Three pieces b_1 ≥ b_2 ≥ b_3 > 1/D, S < 7/D, 2 cuts. Case split on the two consecutive
gaps:
  • *b_2 − b_3 ≤ 1/D:* halve b_1 (pair, 0), cut b_2 at b_3 (pair {b_3,b_3}, 0), singleton b_2 − b_3
    ≤ 1/D. A = b_2 − b_3 ≤ 1/D. ✓ (2 cuts.)
  • *b_1 − b_2 ≤ 1/D:* cut b_1 at b_2 (pair, 0), halve b_3 (pair, 0), singleton b_1 − b_2 ≤ 1/D.
    A = b_1 − b_2 ≤ 1/D. ✓ (2 cuts.)
  • *both gaps > 1/D* ("doubly-hard"): then b_2 > b_3 + 1/D > 2/D and b_1 > b_2 + 1/D > 3/D, so
    b_1 + b_2 + b_3 > 3/D + 2/D + 1/D = 6/D, whence b_1 = S − b_2 − b_3 < 7/D − 3/D = 4/D. XY cuts
    b_1 at b_2 (pair {b_2,b_2}, singleton b_1 − b_2 > 0) and then cuts that singleton at b_3
    (pair {b_3, b_3} if b_1 − b_2 ≥ b_3, else {b_1−b_2, b_1−b_2}), leaving a lone singleton of
    value |(b_1 − b_2) − b_3| = |b_1 − b_2 − b_3|. Bound it:
      – if b_1 ≥ b_2 + b_3: b_1 − b_2 − b_3 = b_1 − (b_2 + b_3) < 4/D − 3/D = 1/D;
      – if b_1 < b_2 + b_3: b_2 + b_3 − b_1 = S − 2b_1 < 7/D − 2·(3/D) = 1/D (using b_1 > 3/D).
    Either way |b_1 − b_2 − b_3| < 1/D. Every other piece is in a cancelling pair, so by Lemma H's
    pair-cancellation A = |b_1 − b_2 − b_3| < 1/D. ✓ (2 cuts.)
  These three cases are exhaustive and disjointly exhaust the gap conditions, so IH(3) holds.

**Two pure-conditional lemmas that TOGETHER close IH(4).** We state the two reduction steps as
clean conditional lemmas with NO empirical percentage bundled in (round-5 rule: bundled percentages
are not certifiable). Both use Lemma X (certified): a pair of equal pieces {x, x} contributes
[0,x] ⊕ [0,x] = ∅ to the XOR, hence 0 to A, regardless of the other pieces; so A depends only on
the XOR of the *unpaired* pieces.

**Lemma IH-reducible (pure conditional).** Let q ≥ 2, pieces b_1 ≥ … ≥ b_q all > 1/D with all
consecutive gaps b_k − b_{k+1} > 1/D (hard regime) and S = Σ b_i < (2^q − 1)/D. If
    **S − max(b_1, 2b_2) < (2^{q−1} − 1)/D**,
then XY spends one pair-cancelling cut to reduce to a valid IH(q−1) instance:
  • if S − b_1 < (2^{q−1} − 1)/D: **halve b_1** → pair {b_1/2, b_1/2} (XOR-cancels) and the active
    multiset {b_2,…,b_q}, all > 1/D, of sum S − b_1 < (2^{q−1} − 1)/D;
  • else (so S − 2b_2 < (2^{q−1} − 1)/D): **cut b_1 at b_2** → pair {b_2, b_2} (XOR-cancels) and the
    active multiset {b_1 − b_2, b_3, …, b_q}, all > 1/D (b_1 − b_2 > 1/D in the hard regime), of sum
    S − 2b_2 < (2^{q−1} − 1)/D.
Since S − max(b_1,2b_2) = min(S − b_1, S − 2b_2), the hypothesis guarantees at least one move is
admissible. By Lemma X, A of the whole config equals A of the active IH(q−1) instance; so if
IH(q−1) holds (XY forces A ≤ 1/D on it with q−2 cuts), then IH(q) holds here with q−1 cuts. ∎
(No gap condition is needed on the reduced instance — IH(q−1) is the plain statement.)

**Lemma IH4-flat (pure conditional).** Let q = 4, b_1 ≥ b_2 ≥ b_3 ≥ b_4 > 1/D with all gaps > 1/D,
S < 15/D, and **S − max(b_1, 2b_2) ≥ 7/D** (the complement of IH-reducible's hypothesis at q=4).
Then XY forces A < 1/D with 3 cuts.
*Proof.* Since 2b_2 ≤ max(b_1,2b_2), the hypothesis gives S − 2b_2 ≥ 7/D, whence
    2b_2 = S − (S − 2b_2) ≤ S − 7/D < 15/D − 7/D = 8/D,  so **b_2 < 4/D.**
The hard-regime gaps give b_3 > b_4 + 1/D > 2/D, b_3 < b_2 − 1/D < 3/D, b_4 < b_3 − 1/D < 2/D, and
b_3 + b_4 > 2/D + 1/D = 3/D. XY makes 3 cuts: (1) **halve b_1** → pair {b_1/2, b_1/2} (XOR ∅);
(2) **cut b_2 at b_3** → the new piece of length b_3 pairs with the intact b_3 (XOR ∅), leaving the
singleton b_2 − b_3; (3) **cut b_4 at δ** (δ > 0 small, chosen below) → singletons b_4 − δ and δ.
By Lemma X the two equal pairs contribute ∅, so A = alternating sum of the three singletons
{b_2 − b_3, b_4 − δ, δ}. Two exhaustive sub-cases (the b_2 < 4/D bound is tight, so both are kept):
  • **b_2 < b_3 + b_4:** then b_2 − b_3 < b_4, so for small δ the sort is b_4 − δ > b_2 − b_3 > δ,
    giving A = (b_4 − δ) − (b_2 − b_3) + δ = b_3 + b_4 − b_2 < b_4 − 1/D (since b_2 > b_3 + 1/D)
    < 2/D − 1/D = 1/D (since b_4 < 2/D). **A < 1/D**, independent of δ. ✓
  • **b_2 ≥ b_3 + b_4:** then b_2 − b_3 ≥ b_4 > b_4 − δ, so the sort is b_2 − b_3 > b_4 − δ > δ,
    giving A = (b_2 − b_3) − (b_4 − δ) + δ = (b_2 − b_3 − b_4) + 2δ. Now b_2 − b_3 − b_4 < 4/D − 3/D
    = 1/D (b_2 < 4/D, b_3 + b_4 > 3/D), so 1/D − (b_2 − b_3 − b_4) > 0; choosing
    0 < δ < min(b_4/2, (1/D − (b_2 − b_3 − b_4))/2) yields **A < 1/D**. ✓
In both sub-cases A < 1/D with 3 cuts. ∎

**IH(4) — COMPLETE.** For any q=4 hard-regime instance (b_i > 1/D, all gaps > 1/D, S < 15/D),
either S − max(b_1,2b_2) < 7/D — then IH-reducible drops to IH(3), proved in full above — or
S − max(b_1,2b_2) ≥ 7/D — then IH4-flat gives A < 1/D directly. These two conditions are
complementary and exhaustive, so **IH(4) holds unconditionally.** Combined with the earlier B1-large
setup, this closes the hard-regime upper bound **through q = 4**, i.e. for n ≤ 4 (B1-large branch).

**What is left open (upper bound).** The general step IH(q ≥ 5) in the flat residual (its complement
is IH-reducible ↦ IH(q−1)) and sub-case **B2** (a_1 ≤ 1/2, all pieces in (1/D, 1/2], sum exactly
(2^{n+1}−1)/D, no dominant piece) are NOT closed here; they are the honest open core, handed to the
sibling approach **upper-general-cascade** (IH+(m) dual-bound induction + B2 double-cancel entry).
This approach closes IH(q ≤ 4) and does not duplicate the general-q work.

**B2 (a_1 ≤ 1/2, no dominant piece) — OPEN (the genuine difficulty).** All pieces lie in
(1/D, 1/2]. Lemma I is unavailable (no piece exceeds the sum of the rest). Numerics (n=3,
config {0.375,0.357,0.219,0.049}) show XY wins by *distributing* cuts — halving several large
pieces separately, O ≈ 0.508 < c(3) — but no single lemma yet certifies an explicit strategy
achieving O ≤ c(n) for every B2 config, with a rigorous ≤ n mark budget. The candidate is a
MIXED strategy: halve a chosen subset of pieces and place one asymmetric cut creating a tiny
"singleton" fragment of length ≤ 1/D, so the surviving odd layer has measure ≤ 1/D
(Lemma R target μ{N odd} ≤ 1/D). Making the subset choice and the ≤ n budget rigorous is
GAP U1.

**GAP U1 (open) = CASE B general n (B1-large IH(q≥5) flat residual, and B2).** Explicit XY strategy
with O ≤ c(n) for every LB config with all pieces > 1/D and > q=4 pieces. Case A (§6.1) is closed;
Case-B hard regime is now closed **through q = 4** (IH(1)–IH(4) all proved). Handed to sibling
approach upper-general-cascade.

---

## 7. Base cases — PROVED

**n = 1, c(1) = 2/3, D = 3.**
*Lower.* LB marks 1/3; pieces {1/3, 2/3}. If XY spares the 2/3 piece, O ≥ 2/3 (§4.1). If XY
cuts it into (u, 2/3−u): pieces {1/3, u, 2/3−u}; since u + (2/3−u) = 2/3, at least one of
u, 2/3−u is ≤ 1/3, so the median of the three values is ≤ 1/3, and O = r_1 + r_3 = 1 − median
≥ 2/3. So LB guarantees ≥ 2/3.
*Upper.* Let L = max(LB's two pieces) ≥ 1/2 (L = 1 if LB uses 0 marks). If L ≤ 2/3: XY
passes, O = L ≤ 2/3. If L > 2/3: XY halves L; the other piece 1 − L < 1/3 < L/2, so pieces
sorted are L/2, L/2, 1−L, giving O = L/2 + (1−L) = 1 − L/2 < 1 − 1/3 = 2/3. Hence
c(1) = 2/3. ∎

**n = 2, c(2) = 4/7, D = 7.** LB pieces {1,2,4} in 1/7-units, R_2 = 4.
*Lower (confined case, full finite analysis).* Intacts {1,2}, fragments of 4 with ≤ 2 cuts.
- 0 cuts: R_2 = 4 intact, r_1 = 4, O ≥ 4 (§4.1).
- 1 cut: F = {c, 4−c}, 2 ≤ c < 4. Pieces {c, 4−c, 2, 1}. If c ≥ 3: 4−c ≤ 1, sorted
  (c,2,1,4−c), O = c + 1 ≥ 4. If 2 ≤ c < 3: 4−c ∈ (1,2], sorted (c,2,4−c,1), O = c + (4−c)
  = 4. Either way O ≥ 4.
- 2 cuts: F = {x,y,z}, x≥y≥z>0, x+y+z = 4, so x ≥ 4/3. If x ≥ 2: sorted begins x,2,… with
  y,z,1 (y+z = 4−x ≤ 8/3) below; checking the finitely many orderings of {x,y,z,2,1} gives
  O ≥ 4, with equality at the interleaving x,2,y,1,z (y∈(1,2), z<1: O = x+y+z = 4). If
  x < 2: the intact 2 is r_1 (odd); the two intacts {2,1} and three fragments summing to 4
  give, in every ordering, even-sum E ≤ 3 (the even ranks can capture at most the two intacts
  and at most one fragment, and the fragment values are capped by x<2; the supremum of E over
  the finitely many order-types is 3), so O = 7 − E ≥ 4. In all cases O ≥ 4. ✓
This is the base case of G-L1(2).
*Upper.* Against the geometric marking XY interleaves (cut the 4-piece into 2+ε,1+ε,1−2ε,
sorting 2+ε,2,1+ε,1,1−2ε) forcing O = 4/7; against any other marking §6.1 (Case A) or §6.2
applies. c(2) = 4/7 modulo GAP U1.

---

## 8. Assembly and final answer

Lemma G1 reduces the problem to the odd-sum marking game. The construction (§3), the easy case
(§4.1), the top-fragment cascade (§4.2.4, a=1), and now the **dyadic two-case split + no-donor
closer (§4.2.7)** establish the **confined** lower bound c(n) ≥ 2^n/D for all n (obstruction now
only GAP L2: XY cuts outside R_n). The interleaving lemma (§5), Lemma H (§6.1, closing Case A),
IH(1)–IH(4) (§6.2, closing the Case-B hard regime through q=4) and the n=1 analysis establish the
upper bound c(n) ≤ 2^n/D where proved (obstruction: GAP U1 = Case B general n, q ≥ 5, and B2).
The matching values give

    **c(n) = 2^n / (2^{n+1} − 1).**

Verified: n=1 → 2/3 (fully proved), n=2 → 4/7 (fully proved), n=3 → 8/15, consistent with
c(n) = 2c(n−1)/(2c(n−1)+1) (2·(2/3)/(4/3+1) = 4/7 ✓).

Open gaps blocking `solved`: **(lower)** the confined lower bound A ≥ 1 on all of Δ is fully
proved (§4.2.7); **L2** (XY cuts outside R_n) is now **reduced (round 7, §4.4) by a rigorous
induction to a single residual — the augmented a = 0 closer** (the DyadicLower Case-2 closer
generalised to within-group donors and tiny bottom stray sub-pieces). Every other stray branch is
closed. **(upper)** Case A closed (Lemma H); Case B B0/B1-clean closed; **B1-large hard regime
closed through q = 4** (IH(1)–IH(4) all proved, IH(4) via IH-reducible + IH4-flat); general
IH(q ≥ 5) flat residual and **B2** are open (sibling upper-general-cascade). — **L2 augmented-a=0
closer** (lower) and **GAP U1 = Case B general-n** (upper) block `solved`.

---

## Approaches tried
- Round 8 (direct-constructive): (LOWER, L2 augmented a=0 closer) attacked via the **T-parity /
  interleaving** framing (§4.4.5), genuinely different from DyadicLower's receiver/donor route. NEW
  rigorous content: (A) the sharper reformulation **A ≥ 1 ⟺ E_F ≤ O_G** (even-rank fragment mass ≤
  odd-rank G mass; tie-robust); (B) **all-F-odd sufficiency** (E_F = 0 ⟹ A ≥ 1, recovering the explorer
  identity A = 1 + 2O_G); (C) **injection/majorisation lemma** — if N_F(x) ≤ N_G(x)+1 ∀x then A ≥ 1 (a
  clean layer-cake bound via E = ∫⌊N/2⌋, ΣG = ∫N_G; the Hall condition matching even-rank pieces to
  larger distinct G-pieces); (D) minimiser receiver-move: if the smallest fragment b_0 has Geq odd
  (⟺ T − β odd, β = #G below b_0) then all fragments are at odd ranks so A ≥ 1 — closes the pure T-odd
  no-G-below anchor. **Did NOT close** the residual. KEY REFUTATION (round-8 exact search): the true
  minimiser has **E_F > 0** with **E_F ≈ O_G** (‡ tight) — fragment sits at an even rank (ranks {2,3,5}
  for n=3,s=1) — so (B) and (C) both FAIL at the minimiser, and (D)'s receiver move is blocked by a
  vertex tie. The residual is exactly the confined (2b)/(2c) within-group flat-move on the tight face
  E_F = O_G; not discharged. — **partial**; residual: within-group flat-move termination at the tight
  clustered minimiser (lower) + U1 (upper).
- Round 7 (direct-constructive): (LOWER, L2) attacked the sole remaining lower-bound gap (XY cuts
  outside R_n) via the **augmented DyadicLower** opening. NEW rigorous content: (i) the **reformulation
  (†)** A ≥ 1 ⟺ E ≤ ΣG = 2^n − 1 (even-rank sum ≤ total non-R_n mass), unifying confined and stray;
  (ii) the **augmented vertex reduction** (A piecewise-affine on the product-of-simplices P, min at an
  arrangement vertex); (iii) the unifying statement **GDL(n)** and its **induction skeleton on n**;
  (iv) the **Count Lemma** (≥1 non-R_n piece at an odd rank, so the A=1 interleaving is unreachable
  once s ≥ 1 — gives A > 0, not A ≥ 1). CLOSED branches feeding the induction: **a = 1 with R_{n−1}
  uncut** (cascade peel of (f_1, 2^{n−1}) → GDL(n−1)); **v_1 = 2^{n−1}, v_2 ≤ 2^{n−2}**
  (A ≥ 2^{n−2} ≥ 1); confined base s = 0 (import `DyadicLower-confined`); n ≤ 2. REDUCED L2 to a
  **single residual: the augmented a = 0 closer** — the DyadicLower Case-2 no-donor/parity closer
  generalised to (i) donors restricted to a piece's own fixed-sum cut-group and (ii) a tiny stray
  sub-piece (from cutting R_0) at the bottom odd rank instead of the intact 1. Verified numerically:
  stray min A ≥ 1 (0 violations, incl. clustered/tie-laden, n = 2,3,4,5), infimum 1 attained only as a
  stray sub-piece → 0. Confirmed dead: the pointwise stray↔confined monotone exchange (716/17980
  violations), and the relaxed (†) with G arbitrary or F unbounded (both fail — dyadic G + budget both
  load-bearing). — **partial**; residual: L2 augmented a = 0 closer (lower) + U1 (upper).
- Round 6 (direct-constructive): (LOWER) **fully closed the confined lower bound** A ≥ 1 on Δ,
  replacing the round-5 refuted "receiver always exists" by the **dyadic two-case split** on the
  max fragment w_1 vs 2^{n−2}: Case 1 (w_1 ≤ 2^{n−2}) ⇒ A ≥ v_1−v_2 ≥ 2^{n−2} ≥ 1 directly (both
  round-5 counterexamples land here); Case 2 (2^{n−2} < w_1 < 2^{n−1}) ⇒ w_1 is a NAMED receiver
  (G(w_1)=1 by counting, not an existence claim). At the compact minimiser, minimality forces
  **no donor**; then N_tot = n+m odd ⇒ all fragments > 1 ⇒ intact 1 at bottom odd rank ⇒ A ≥ 1;
  N_tot even ⇒ either f_min > 1 (ruled out by a flat-then-descent contradiction, or a=1 boundary)
  or f_min ≤ 1 (a **flat move** e_{w_1}−e_{f_min} drives m ↦ m−1, flipping N_tot to odd). The
  flat-move **termination** is closed by an explicit strictly-decreasing well-foundedness weight
  m = #{positive fragments} — the round-5 "degenerate flat-move face" loose end is GONE. This
  eliminates BOTH round-5 lower-bound gaps (false receiver + flat-move). (UPPER) restated
  **IH-reducible** and **IH4-flat** as PURE CONDITIONAL lemmas (no empirical %), and **closed
  IH(4)** completely: reducible (S−max(b_1,2b_2) < 7/D ⇒ drop to IH(3)) ∪ flat (≥ 7/D ⇒ b_2 < 4/D,
  3-cut strategy, A < 1/D) partition all q=4 hard-regime configs. Hard-regime upper bound now closed
  through q=4. Verified: 0 fails over 2·10^5+ a=0 configs each n=3..6 (A ≥ 1); IH4-flat 0 fails,
  maxA < 0.99·(1/D). — partial; residuals: **L2** (lower, XY cuts outside R_n) + general IH(q≥5)
  flat residual and **B2** (upper, sibling upper-general-cascade).
- Round 5 (direct-constructive): (LOWER) proved the **Descent Lemma** closing the a=0 case of the
  confined lower bound: min_R A attained at a cell-complex vertex, directional derivative of a
  mass-transfer e_a−e_b equals (−1)^{G(g_a)}+(−1)^{Geq(g_b)}, so a (receiver = G-odd fragment,
  positive donor = Geq-odd fragment) pair gives A′=−2 and forbids an interior min. Proved
  **receiver always exists** (i′-range/parity argument, generic + density). Three exhaustive
  minimiser cases — boundary g_i=2^{n−1} (continuity from a=1 cascade, A≥1), boundary g_i=0
  (fewer-fragment induction), interior (no valid pair ⟹ either no-donor ⟹ all fragments>1 ⟹
  intact 1 at bottom odd rank ⟹ A=A′+1≥1, OR the degenerate sole-receiver=donor flat-move face).
  This closes the lower bound **A ≥ 1 on all of Δ** modulo the finite-termination of one degenerate
  flat-move face (branches (i)+boundaries+receiver-existence fully rigorous). Numerically verified
  receiver present in 0/failures over ~1.5·10^5 a=0 configs n=3,4,5, and no-donor ⟹ min frag>1
  (0 exceptions). (UPPER) wrote the **corrected relative-threshold IH(q) reduction**: a valid
  one-step drop to IH(q−1) exists iff S−max(b_1,2b_2)<(2^{q−1}−1)/D (halve b_1 OR cut b_1 at b_2),
  closing ~94% of the hard regime; refuted the absolute threshold b_1>2^{q−2}/D and the plain
  Euclidean cascade; the ~6% flat residual (two-cut cascade) and B2 remain GAP U1. — partial;
  residuals: degenerate flat-move termination (lower, minor) + U1 flat two-cut + B2 (upper).
- Round 4 (direct-constructive): (i) generalised §4.1 to a clean **spare-R_n ⟹ O ≥ 2^n for
  EVERY placement** (unique-max argument), splitting the whole lower bound on the single
  dichotomy "does XY cut R_n?"; (ii) recast the confined lower bound as minimising the
  piecewise-affine A = μ{N odd} over the compact simplex Δ of ≤ n+1 fragments, proving min is
  attained at a vertex and reducing L1 to the **single vertex inequality (★) A(vertex) ≥ 1**,
  with the interleaving cell (A ≡ 1) and all case-a=1 vertices (cascade) closed and only a=0
  clustered vertices residual; (iii) showed L2 collapses into the same (★) via the
  unreachable-interleaving (fragment-count + Lemma S) argument — L1 and L2 are now ONE gap;
  (iv) proved IH(1),IH(2),IH(3) of the B1-large pair-creation sub-game rigorously (residual
  singleton < 1/D from the sum bound), leaving the general IH(q≥4) step as the honest core.
  Confirmed numerically min_Δ A = 1 (n≤5) and that the ≤ n+1 fragment count is load-bearing
  (min A ↓ ≈0 with n+3 fragments). — partial; residual (★) (lower) and U1 (Case B general n).
- Round 3 (direct-constructive): Proved **Lemma H** in full (halve the p−1 largest LB pieces
  ⟹ O = 1/2 + a_p/2, via the pair-cancellation of the alternating sum and the singleton
  landing at an odd rank), CLOSING Case A of the upper bound for all n. Proved the
  fragment-count bounds N_F(2^{n−j}) ≤ 2^j − 1, the exact interleaving value O = 2^n
  (min ≤ 2^n in the confined case), the **rank-swap Lemma S** (boundary crossing changes O by
  (−1)^{r+1}(y−x); interleaving is a local minimum), and the **top-fragment cascade** reducing
  the confined lower bound to case a=0 (generalised statement G-L1). Base cases n=1 (both
  bounds) and n=2 (confined lower + construction) completed. Dropped the circular integral.
  — partial; L1 (case a=0), L2, U1 (Case B) remain.
- Round 2 (direct-constructive): Proved G1, R1/R2, geometric construction + dominance,
  easy lower case, Lemma I; reduced hard lower bound to the (now-dropped) identity ‡. — partial.
- induction-recursion (round 2): DEAD-END (RETHINK) — n→(n−1) separation refuted (budget never
  decrements; odd-sum is a global functional). Do not retry.

## Current best
Fully rigorous and reviewer-verifiable: (i) reduction to the odd-sum game (G1, certified);
(ii) odd-sum rewritings (R, certified); (iii) LB construction + dominance identity; (iv) easy
lower-bound case (XY spares R_n); (v) interleaving Lemma I; (vi) **Lemma H**, closing Case A of
the upper bound (O = 1/2 + a_p/2, so O ≤ c(n) ⟺ a_p ≤ 1/D) for all n; (vii) fragment-count
bounds, interleaving value = 2^n, rank-swap Lemma S (interleaving = local min), top-fragment
cascade; (viii) base cases n=1 (both) and n=2 (lower confined + construction); (ix) NEW round 4:
spare-R_n general lower bound (all placements), the min-over-Δ reduction of the lower bound to
the single vertex inequality (★) with interleaving-cell + all a=1 vertices closed, the merge of
L1/L2 into (★), and rigorous IH(1/2/3) for B1-large pair-creation. Answer c(n) = 2^n/(2^{n+1}−1),
verified on small n. NEW round 6: the **confined lower bound is fully closed** (§4.2.7) by the
dyadic two-case split (max fragment vs 2^{n−2}) + the no-donor closer + an explicit flat-move
well-foundedness weight; **A ≥ 1 on all of Δ**. NEW round 7 (L2, XY cuts outside R_n): the stray
lower bound is reformulated as **(†) A ≥ 1 ⟺ E ≤ ΣG = 2^n − 1**; A is piecewise-affine on the
augmented product-of-simplices, min at an arrangement vertex; the unifying statement **GDL(n)** with
an induction on n closes every branch except one — the a = 1 (R_{n−1} uncut) cascade peel, the
top-gap Case 1 (A ≥ 2^{n−2}), the confined base (import DyadicLower), and the Count Lemma (≥1 non-R_n
piece at an odd rank) are all rigorous. **L2 is reduced to a single residual: the augmented a = 0
closer** (DyadicLower Case-2 generalised to within-group donors + tiny bottom stray sub-piece).
Numerics confirm stray min A ≥ 1 (tight, infimum 1). Upper: **IH-reducible** + **IH4-flat** close the
Case-B hard regime **through q = 4**. NEW round 8: the closer is sharpened to **A ≥ 1 ⟺ E_F ≤ O_G**
(§4.4.5(A)); the **injection lemma** N_F ≤ N_G+1 ⟹ A ≥ 1 (C) and the **all-F-odd sufficiency** (B) and
the **minimiser receiver-move** closing T − β odd (D) are proven, but the true minimiser is the tight
clustered face E_F = O_G with E_F > 0 (a fragment at an even rank), where (B),(C) fail and the receiver
move is tie-blocked — so the residual is now precisely a **within-group flat-move termination on the
tight face E_F = O_G**. Open: that within-group flat-move (lower); general IH(q ≥ 5) flat residual +
**B2** (upper, sibling upper-general-cascade).

## Full proof
Not present — Status is partial (gaps L1 case a=0, L2, U1 Case B open).

## Promotable lemmas
- **Sharper reformulation (‡): A ≥ 1 ⟺ E_F ≤ O_G — NEW, CERTIFIABLE.** With the group split O = O_F+O_G,
  E = E_F+E_G, one has E − ΣG = E_F − O_G (tie-break independent), so A = D − 2E gives A ≥ 1 ⟺ E_F ≤ O_G:
  the even-rank fragment mass is at most the odd-rank G mass. Sharper intrinsic form of (†). Proved
  §4.4.5(A). Corollary (all-F-odd): E_F = 0 ⟹ A ≥ 1 (= 1 + 2O_G). Reusable for any lower-bound approach.
- **Injection / majorisation lemma — NEW, CERTIFIABLE.** For the stray a=0 setup, if N_F(x) ≤ N_G(x)+1
  for all x ≥ 0 then A ≥ 1. Proof: E = ∫⌊N/2⌋ ≤ ∫N_G = ΣG via ⌊(N_F+N_G)/2⌋ ≤ N_G under the hypothesis
  (Lemma R for E = ∫⌊N/2⌋, ΣG = ∫N_G). Proved §4.4.5(C). Clean layer-cake bound covering the
  non-clustered regime; genuinely different from receiver/donor. Reusable.
- **Reformulation (†) of the stray lower bound — NEW, CERTIFIABLE.** With F = R_n-fragments
  (ΣF = 2^n) and G = non-R_n pieces (ΣG = 2^n − 1), total mass D, one has A = D − 2E, so
  **A ≥ 1 ⟺ E(F ∪ G) ≤ ΣG** (even-rank sum ≤ total non-R_n mass). Unifies confined and stray;
  `DyadicLower-confined` is the s = 0 case. Proved §4.4.1. (Warning built in: (†) is FALSE for
  G arbitrary or F unbounded — dyadic G and the budget k_n + s ≤ n are both load-bearing.)
- **Augmented vertex reduction — NEW, CERTIFIABLE.** For a fixed stray combinatorial type, A = μ{N odd}
  is continuous and piecewise-affine on the product of simplices P = Δ_F × ∏_j Δ_{G,j}, so min_P A is
  attained at an arrangement vertex; the stray minimum is a min over finitely many such P. Proved
  §4.4.2 (KB: piecewise-affine minimisation attains its optimum at a cell-complex vertex).
- **Count Lemma (stray) — NEW, CERTIFIABLE.** If XY places s ≥ 1 cuts outside R_n (budget k_n + s ≤ n),
  then in the sorted piece list at least one non-R_n piece occupies an ODD rank; equivalently the exact
  interleaving optimum A = 1 (all intacts at even ranks) is unreachable once any cut is spent outside
  R_n. Proof: else ⌈T/2⌉ ≤ k_n+1 forces n+s ≤ k_n+1 ≤ n−s+1, i.e. 2s ≤ 1. Proved §4.4.3. (Gives A > 0,
  not A ≥ 1.)
- **GDL(n) induction skeleton (L2 reduction) — NEW, partial (residual flagged).** GDL(n): for dyadically
  cut intacts G (ΣG = 2^n − 1) and F with ΣF ≤ 2^n, k_n + s ≤ n, one has E(F ∪ G) ≤ ΣG. Closed
  branches: a = 1 with R_{n−1} uncut (cascade peel → GDL(n−1)); v_1 = 2^{n−1}, v_2 ≤ 2^{n−2}
  (A ≥ 2^{n−2}); base s = 0 (DyadicLower) and n ≤ 2. Residual: the augmented a = 0 closer. Proved
  §4.4.3–4.4.4. Certifiable as a REDUCTION lemma (not yet a full closure).
- **Dyadic two-case split + no-donor closer (confined a=0 lower bound) — NEW, CERTIFIABLE.** For n
  intacts {2^0,…,2^{n−1}} and m ≤ n+1 fragments (values in [0,2^{n−1}], sum 2^n), at the compact
  minimiser v of A: (Case 1) if max fragment w_1 ≤ 2^{n−2}, then A ≥ v_1−v_2 = 2^{n−1}−2^{n−2}
  = 2^{n−2} ≥ 1; (boundary) if w_1 = 2^{n−1}, a=1 closure gives A ≥ 1; (Case 2) if 2^{n−2}<w_1<2^{n−1}
  then G(w_1)=1 so w_1 is a receiver, minimality forces no positive donor (all Geq even), and then
  N_tot=n+m odd ⇒ intact 1 at bottom odd rank ⇒ A ≥ 1, while N_tot even is closed by the flat move
  e_{w_1}−e_{f_min} (well-founded: strictly decreases #{positive fragments}). Hence **A ≥ 1 on all
  of Δ**. This REPLACES and corrects the round-5 (refuted) Descent Lemma / receiver-existence claim.
  Proved §4.2.7. Reusable engine for the lower bound.
- **IH-reducible (pure conditional, upper bound) — CERTIFIABLE.** For q ≥ 2 pieces > 1/D, all gaps
  > 1/D, S < (2^q−1)/D: if S − max(b_1, 2b_2) < (2^{q−1}−1)/D, one pair-cancelling cut (halve b_1 if
  S−b_1 < (2^{q−1}−1)/D, else cut b_1 at b_2) reduces to a valid IH(q−1) instance (all active pieces
  > 1/D, active sum < (2^{q−1}−1)/D), preserving A by Lemma X. No empirical % in the statement.
  Proved §6.2. Reusable engine for Case B.
- **IH4-flat (pure conditional, upper bound) — NEW, CERTIFIABLE.** For q=4, b_1≥b_2≥b_3≥b_4 > 1/D,
  all gaps > 1/D, S < 15/D, and S − max(b_1,2b_2) ≥ 7/D: then b_2 < 4/D, and XY forces A < 1/D with
  3 cuts (halve b_1; cut b_2 at b_3; cut b_4 at δ) — two sub-cases b_2 ≶ b_3+b_4 both give A < 1/D.
  Together with IH-reducible this closes **IH(4) unconditionally**. Proved §6.2. Reusable base for
  the general IH(q) induction.
- **Spare-R_n lemma (general lower bound).** For LB's geometric config, if XY places no cut
  inside R_n (its ≤ n cuts arbitrary elsewhere), then R_n = 2^n/D is the unique largest piece,
  so r_1 = 2^n/D and O ≥ r_1 = 2^n/D = c(n). Proved in full in §4.1. Reusable (imported by
  caseB-matching for the lower bound).
- **Δ-reduction of the lower bound.** After padding to n+1 fragments, A = μ{N odd} is continuous
  and piecewise-affine on the compact simplex Δ = {Σ g_i = 2^n, g_i ≥ 0}; its minimum is attained
  at a vertex of the cell complex, so the confined lower bound A ≥ 1 is EQUIVALENT to the vertex
  inequality (★) A(vertex) ≥ 1. The interleaving cell (A ≡ 1) and all a=1 vertices (cascade) are
  closed; the ≤ n+1 count is load-bearing. Proved in §4.2.6. Reusable framing for any lower-bound
  approach.
- **IH pair-creation leaves (q ≤ 3).** For q pieces all > 1/D with Σ < (2^q − 1)/D, XY forces
  A ≤ 1/D with ≤ q−1 cuts, for q = 1,2,3 (residual singleton < 1/D from the sum bound). Proved in
  §6.2. Reusable base of the B1-large induction.
- **Lemma H (halve-the-p−1-largest formula).** For LB pieces a_1 ≥ … ≥ a_p, halving the p−1
  largest (p−1 ≤ n cuts) and sparing a_p yields O = 1/2 + a_p/2; hence O ≤ c(n) ⟺ a_p ≤ 1/D,
  closing Case A of the XY upper bound. Proved in full in §6.1. Reusable across approaches.
- **Lemma S (rank-swap).** When two consecutive-rank pieces with values x>y swap (x decreased
  past y), ΔO = (−1)^{r+1}(y−x); a fragment at an odd rank crossing below an adjacent intact
  strictly raises O. Proved in §4.2.3. Reusable (local-monotonicity of the odd-sum).
- **Fragment-count bound.** For fragments of total 2^n, #{fragments > 2^{n−j}} ≤ 2^j − 1.
  Proved in §4.2.1. Reusable.
- **Interleaving value.** With intacts {2^0,…,2^{n−1}} and n+1 fragments summing to 2^n placed
  one per dyadic gap, O = 2^n exactly. Proved in §4.2.2. Reusable.
