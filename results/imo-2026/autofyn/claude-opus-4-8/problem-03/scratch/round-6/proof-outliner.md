## imo-2026-03

Field this round: **advance direct-constructive** folding in BOTH explorer routes (the whole
lower bound closes; the upper bound closes through q=4), plus **one focused copy** to run the sole
remaining wall — the general-n upper bound (IH(q≥5) + B2) — in parallel. I tested the two candidate
NEW framings and both die at the gate (evidence below), so no new framing is put up: the disciplined
move is to advance/parallelize the leader, exactly as the dispatch directs.

Verified numerically this round (my own checks, not just explorer claims):
- Lower-bound two-case split: 0 failures over 20k a=0 configs each n=3,4,5. Both round-5
  reviewer counterexamples ({2,10/3,10/3,11/3,11/3}, {2,7/2,7/2,7/2,7/2}) sit in Case 1
  (max frag 3.67, 3.5 ≤ 2^{n-2}=4), where A=5 ≥ 4 directly — the false "receiver always exists"
  claim is REMOVED, not patched.
- IH4-flat strategy: 0 failures, max A well under 1/D (n=3: 0.044<0.067; n=4: 0.025<0.032;
  n=5: 0.011<0.016).
- KILL-SWITCH on candidate new framing "xor-covering-upper" (greedy μ(XOR)-minimizing n toggles):
  FAILS, worst μ/(1/D) = 2.34 (n=3), 2.52 (n=4), 3.37 (n=5). A greedy covering bound is false; the
  correct choice must be globally adaptive = pair-creation again ⇒ same wall (rename). Rejected.
- Extremal/compactness upper-bound framing rejected without build: the relevant functional has
  interior valleys (graveyard: concavity-of-g / extremal-config, r3), so "geometric config is the
  unique maximizer" is false — a perturbation/compactness route dies at the same kill-switch.

---

direct-constructive: advance
Target: c(n) = 2^n/(2^{n+1}−1). LB can guarantee ≥ c(n) AND XY can hold LB to ≤ c(n), for all n.
Technique: explicit optimal strategies both sides + Lemma-R reduction to μ{N odd}; this round fold
in (LOWER) the dyadic two-case split that removes the false receiver-existence claim and closes the
lower bound completely, and (UPPER) the IH4-flat pure-conditional lemma that closes IH(4).
Skeleton (only the steps changed/added this round; the rest is already reviewer-verified):
  1. LOWER — replace the round-5 "receiver always exists (all configs)" step in §4.2.7 by the
     dyadic dichotomy on the largest fragment w_1 vs threshold 2^{n-2} (= second-largest intact):
     - Case 1 (w_1 ≤ 2^{n-2}): direct — in the a=0 region the top piece is the intact 2^{n-1}
       (unique max), and the second-largest piece v_2 ≤ 2^{n-2} (every non-top intact ≤ 2^{n-2}
       and every fragment ≤ 2^{n-2}); so A ≥ v_1 − v_2 ≥ 2^{n-1} − 2^{n-2} = 2^{n-2} ≥ 1. — by the
       first-gap lower bound A ≥ v_1 − v_2 (all alt-sum terms ≥ 0, sorted list).
     - Case 2 (w_1 > 2^{n-2}): the max fragment w_1 is a receiver — G(w_1)=1 (only 2^{n-1} lies
       above it: all other intacts ≤ 2^{n-2} < w_1, no fragment above the max fragment), which is
       odd. — by piece-counting above w_1.
  2. LOWER — in Case 2 run the Descent Lemma minimiser trichotomy (already written) with the now-
     unconditional receiver w_1: at a minimiser either (a) a positive donor b≠w_1 exists ⇒
     A′₊(e_{w_1}−e_b) = −2 < 0, contradiction; or (b) no positive donor ⇒ smallest piece is the
     intact 2^0=1 at the bottom odd rank 2n+1 (count 2n+1 pieces is odd) contributing +1, delete it,
     remaining alt-sum ≥ 0 ⇒ A ≥ 1; or (c) the only receiver is a positive donor (flat move) ⇒
     A flat along e_{w_1}−e_c to a boundary face. — by the mass-transfer directional derivative
     A′₊(e_a−e_b)=(−1)^{G(g_a)}+(−1)^{Geq(g_b)} (§4.2.7).
  3. LOWER — boundaries: g_i=2^{n-1} ⇒ a=1 cascade (§4.2.4), A≥1; g_i=0 ⇒ fewer fragments,
     fewer-fragment induction (base n≤2, §7). Assemble: min_R A ≥ 1, with a=1 already closed ⇒
     A ≥ 1 on all of Δ ⇒ **lower bound c(n) ≥ 2^n/D closed for all n** (L1+L2 both, via (★)).
  4. UPPER — add IH4-flat as a pure conditional lemma (below) ⇒ IH(4) COMPLETE (reducible region
     ∪ flat residual). Re-propose the round-5 IH(q)-reducible reduction and IH4-flat as clean
     certifiable lemmas with NO empirical percentage in the statement.
  5. UPPER — restate status honestly: upper bound complete for the hard regime through q=4;
     general IH(q≥5) flat residual + B2 remain (handed to the copy build below).
Key lemmas (claim + mechanism):
  - Dyadic two-case split (LOWER, NEW, certifiable) — because in the a=0 region v_1=2^{n-1} is the
    unique max and the threshold 2^{n-2} is exactly the second-largest intact: below it A ≥ v_1−v_2
    ≥ 2^{n-2}; above it the max fragment has exactly one piece (2^{n-1}) over it, so G=1 (receiver).
    This REMOVES the round-5 false universal receiver claim: both reviewer counterexamples are in
    Case 1 where A ≥ 2^{n-2} trivially.
  - Descent no-donor branch (LOWER, already written, now the load-bearing interior closer) — because
    no positive donor ⇒ smallest piece is intact 1 at odd rank 2n+1 ⇒ A = 1 + (nonneg alt-sum) ≥ 1.
  - IH4-flat (UPPER, NEW, certifiable) — because the flat-residual condition S−2b_2 ≥ 7/D with
    S<15/D forces **b_2 < 4/D**; then XY halves b_1 (pair, 0), cuts b_2 at b_3 (pair {b_3,b_3}, 0),
    cuts b_4 at a tiny δ, leaving singletons {b_2−b_3, b_4−δ, δ}. If b_2<b_3+b_4: A=b_3+b_4−b_2 <
    b_4 − 1/D < 1/D (b_4<2/D). If b_2≥b_3+b_4: A=b_2−b_3−b_4+2δ, and b_2−b_3−b_4 < 4/D−3/D = 1/D,
    pick δ < (1/D−(b_2−b_3−b_4))/2 ⇒ A<1/D. Either way A<1/D. (Verified 0 fails; A≤0.044<0.067.)
  - IH(q)-reducible (UPPER, re-propose pure form for certification) — one pair-cancel move (halve b_1
    OR cut b_1 at b_2) drops to a valid IH(q−1) instance iff S − max(b_1,2b_2) < (2^{q−1}−1)/D. State
    WITHOUT the "~94%" empirical number so it certifies (round-5 rule).
Open gaps: general IH(q≥5) flat residual and sub-case B2 (both go to the copy build). Formal loose
end in LOWER: finite-termination of the flat-move face (c) — write the well-foundedness argument
(each flat step strictly reduces the "degenerate dimension" #{tied pairs}; the cell complex is
finite, so a boundary face is reached, closing at g_i=0 or g_i=2^{n-1}).
Cases to cover: LOWER interior Case 1 / Case 2; boundaries g_i=0 and g_i=2^{n-1}; a=1 region.
UPPER: IH(4) reducible ∪ flat-residual (both now covered).
Watch out for: (i) do NOT reinstate the universal "receiver always exists" — it is FALSE at
clustered configs (round-5 rule); the split is the fix. (ii) The n=2 edge where 2^{n-2}=1 coincides
with the smallest intact — base case n≤2 is already done in §7, so state the split for n≥3 and cite
§7 for n≤2. (iii) IH4-flat's b_2<4/D bound is TIGHT (equality at the geometric limit) — keep the two
sub-cases (b_2<b_3+b_4 vs ≥) both. (iv) The flat-move termination must be an explicit
well-foundedness argument, not "iterating reaches a boundary."

---

upper-general-cascade: copy-of direct-constructive
Target: c(n) = 2^n/(2^{n+1}−1) — the same whole problem; this twin focuses its new work on the ONE
remaining wall, the general-n Case-B upper bound (IH(q≥5) flat residual + sub-case B2), leaving the
lower bound and IH(q≤4) as imported/closed.
Technique: pair-creation cascade (Lemma H mechanism, fragment cuts allowed) with a **multi-level
flat-residual descent** — the only mechanism that survives a kill-switch (XOR-covering greedy and
extremal/compactness both refuted this round).
Skeleton:
  1. Establish the flat-level bound: in the flat residual (S − max(b_1,2b_2) ≥ (2^{q−1}−1)/D,
     S<(2^q−1)/D) one has **b_2 < 2^{q−2}/D** — by subtracting the two sum inequalities
     (2b_2 ≤ S − (2^{q−1}−1)/D < 2^{q−1}/D). This is the q-general form of IH4-flat's Step 1.
  2. Descend one level keeping BOTH invariants: after halving b_1 (pair cancels), recurse on
     {b_2,…,b_q} tracking (sum bound) AND (max bound b_2 < 2^{q−2}/D). The pure max-bound
     IH*(m): "m pieces, max < 2^{m−1}/D" is FALSE alone (explorer dead-end, 559/20000 fails) — the
     recursion MUST carry the sum bound too. State the strengthened hypothesis
     **IH+(m): m pieces > 1/D, all gaps > 1/D, sum < (2^m−1)/D AND max < 2^{m−1}/D ⇒ A ≤ 1/D with
     ≤ m−1 cuts.**
  3. Termination: each flat level halves the max-bound exponent (2^{q−2} → 2^{q−3} → …); the gap
     condition b_k > 1/D forces the descent to bottom out at max < 2/D with the last gap giving
     b_{last} < 1/D, contradicting > 1/D — bounding the depth. Base = IH4-flat (proved).
  4. B2 (a_1 ≤ 1/2, sum = 1 = (2^{n+1}−1)/D exactly, all pieces in (1/D,1/2]): the sum is AT the
     IH(n+1) boundary so a single pair-cancel cannot enter a strict IH instance (halving a_1≤1/2
     leaves sum 1−a_1 > (2^n−1)/D since a_1 < c(n)). Use TWO pair-cancels first: pair-create on the
     two largest pieces (cut a_1 at a_2 ⇒ {a_2,a_2}, cut the residual at a_3 or halve), dropping the
     sum by ≥ 2a_2 + 2a_3-worth of cancelled mass into a STRICT IH(n−1) instance sum <
     (2^{n−1}−1)/D, then apply IH+. — by Lemma H pair-cancellation (paired equal pieces contribute 0
     to A) + Lemma X (each cut toggles [c, ℓ−c] in the XOR).
Key lemmas (claim + mechanism):
  - IH+(m) strengthened induction — because the flat residual delivers max < 2^{m−1}/D FOR FREE, and
    carrying it alongside the sum bound is what makes the halve-b_1 descent close (the sum bound
    alone stalls at the flat residual; the max bound alone is false). The two together shrink both
    resources each level.
  - B2 double-cancel entry — because sum sits exactly on the IH(n+1) boundary, one cancellation is
    not enough; two pair-creations on the two largest pieces cut the sum strictly below the
    IH(n−1) boundary, after which IH+ applies.
Open gaps: whether IH+(m)'s descent terminates cleanly for all m (the depth/gap contradiction in
step 3 is the crux — verify the intermediate singletons stay > 1/D or get absorbed); B2's
double-cancel must be shown to keep all residual pieces > 1/D and within the ≤ n budget. Both are
the honest open core of the whole problem after this round.
Cases to cover: IH+(m) reducible vs flat at each level; B2 with a_1 near 1/2 vs near-equal pieces.
Watch out for: (i) NEVER drop the sum bound for the max bound alone (false, explorer dead-end).
(ii) NEVER use the plain Euclidean cascade or a fixed 4-cut cross-pair for q≥5 flat residual — both
fail ~50% (explorer dead-ends); the descent must be adaptive. (iii) Fragment cascades (cutting a
residual again) are REQUIRED — the finite matching menu is refuted (caseB-matching, r4). (iv) B2 is
the genuine difficulty; if the double-cancel entry stalls, the builder should report the exact
sub-region rather than overclaim (round-5 overclaim rule).

---

Not put up (rejected at kill-switch this round — recorded so future rounds don't retry):
- xor-covering-upper (greedy μ(XOR) covering): FAILS, worst 2.3–3.4× target — collapses to the
  pair-creation wall (rename). Same as dyadic-carry-upper's fate (r5).
- extremal/compactness upper bound ("geometric config is unique maximizer"): dies at the interior-
  valley kill-switch (graveyard: concavity-of-g / extremal-config, r3).
