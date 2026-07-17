## imo-2026-03

Answer c(n) = 2^n/D, D = 2^{n+1}−1. Reduction to A = μ{N odd} (Lemma X: A = μ(⊕[0,ℓ_i]) = alternating
sum of sorted piece lengths). Lower bound ⟺ A ≥ 1 on the geometric construction; upper bound ⟺ A ≤ 1/D
on every XY response. Lower bound: only L2 (stray cuts) open. Upper bound: IH(q≥5) flat residual + B2
(n≥3) open. Field below puts the L2 finish, a genuinely-different upper framing, and the corrected B2
advance on the table.

---

### direct-constructive: advance
Target: The whole problem — c(n) = 2^n/D, both bounds. This advance closes the SOLE remaining lower-bound
gap L2 (XY cuts placed outside the largest LB piece R_n), which would flip the LOWER bound fully closed.
Technique: Augmented Δ-vertex reduction (Opening B of the L2 explorer) — extend the certified
DyadicLower-confined argument from the confined subspace to the full augmented space (confined R_n
fragments PLUS stray sub-pieces of some R_j, j<n). Same PL-min-attained-at-a-vertex spine, three cases.
Skeleton:
  1. Spare-R_n case (no cut in R_n): A ≥ 2^n. — certified (Spare-R_n lemma), no new work.
  2. Confined case (all k cuts in R_n): A ≥ 1. — certified DyadicLower-confined, no new work.
  3. Stray case (k_n≥1 cuts in R_n, s≥1 stray cuts in R_j, j<n): minimise A over the AUGMENTED compact
     space; A piecewise-affine ⟹ min at an arrangement vertex (same as confined). — by PL-min-at-vertex
     (KB piecewise-concavity smoothing), the tool that certified DyadicLower.
  4. Vertex case a=1 (some R_n fragment > 2^{n-1}): top-fragment cascade. — CERTIFIED, no new work.
  5. Vertex Case 1 (max R_n fragment w_1 ≤ 2^{n-2}), R_{n-1} intact: A ≥ v_1−v_2 = 2^{n-1}−2^{n-2}
     = 2^{n-2} ≥ 1. — exactly the confined Case 1, unchanged.
  6. Vertex Case 1, R_{n-1} cut at a (a ≤ 2^{n-2}): if a = 2^{n-2} the pair {2^{n-2},2^{n-2}} XOR-cancels
     (Lemma H pair-cancellation) ⟹ reduce to DyadicLower on (n−1 effective intacts) + R_n fragments,
     A ≥ 1 by INDUCTION on the number of intacts; if a < 2^{n-2} the larger sub-piece 2^{n-1}−a > 2^{n-2}
     is the new v_1 and the instance is a smaller-n instance handled inductively. — CHEAPEST KILL here.
  7. Vertex Case 2 (w_1 ∈ (2^{n-2}, 2^{n-1})): let G = #{non-R_n pieces in (w_1, 2^{n-1}]}. If G odd, w_1
     is a named receiver (G(w_1) odd), no-donor from minimality ⟹ A ≥ 1 (confined Case 2 verbatim). If G
     even, minimality gives A′₊(e_{w_1}−e_b) = 1+(−1)^{Geq(b)} with donors present ⟹ flat moves exist;
     the strictly-decreasing flat-move weight m = #{positive fragments} (sub-case 2c of DyadicLower)
     terminates at a boundary/lower-m config already covered. — reuse the certified termination monovariant.
Key lemmas (claim + mechanism):
  - Count Lemma: at least one non-R_n piece sits at an ODD rank — because k_n+1 (R_n fragments) ≤ n−s+1
    < n+s (non-R_n pieces) for every s ≥ 1 (n−s+1 < n+s ⟺ 2s > 1), so R_n fragments cannot fill all odd
    ranks. This forbids the all-non-R_n-at-even-rank tie that would drop A below 1.
  - Midpoint-cancel induction (step 6): a midpoint stray cut of R_{n-1} produces an XOR-cancelling equal
    pair, so the augmented instance collapses to a DyadicLower instance with one fewer intact — valid
    because DyadicLower's proof never used the exact intact multiset, only #fragments ≤ n+1 and the sum.
  - Flat-move termination in the augmented space (step 7, G even): the weight m = #{positive fragments}
    strictly decreases along every A′₊ = 0 move and is bounded below — because A′₊ ≤ 0 forces a positive
    donor whose fragment vanishes, exactly the DyadicLower monovariant, unchanged by the stray pieces.
Open gaps: steps 6 (the a<2^{n-2} smaller-n inductive reduction — verify the induction hypothesis form)
and 7 (G-even branch — confirm the flat-move monovariant still terminates once stray pieces are present).
Cases to cover: a=1 (done); Case 1 with R_{n-1} intact/cut(midpoint)/cut(a<2^{n-2}); Case 2 with G
odd/even; boundary w_1 = 2^{n-1} by continuity.
Watch out for: the POINTWISE exchange "stray→confined weakly raises A" is FALSE (716/17980 violations, r7
explorer) — do NOT route L2 through a monotone exchange; must go through the augmented vertex reduction.
The Count Lemma gives A > 0 only, not A ≥ 1 — the dyadic per-case bounds (steps 5-7), not the count, carry
the ≥ 1. Test the G-even flat-move termination at CLUSTERED tie-laden augmented vertices, never random ones.

---

### upper-vertex-reduction: new (copy-of direct-constructive)
Target: The whole problem's UPPER bound A ≤ 1/D in the Case-B hard regime for ALL n (i.e. IH(q) for every
q, closing the IH(q≥5) flat residual that the entire q-induction framing has stalled on for 3+ rounds).
Lower bound + reductions imported from direct-constructive / certified lemmas.
Technique: UPPER Δ-vertex reduction — mirror the SAME PL-max-at-vertex spine that certified the lower
bound, now on the upper side. Genuinely different from the whole graveyard: NOT step-by-step q-induction
(evades the r6 fixed-point obstruction), NOT concavity-of-g (evades the r3 interior-valley refutation —
we need only "a PL function attains its max at an arrangement vertex," which is UNCONDITIONAL, not
concavity), NOT a potential/monovariant, NOT greedy-XOR, NOT the menu.
Skeleton:
  1. Fix q. K_q = closure {b_1 ≥ … ≥ b_q ≥ 1/D, all gaps ≥ 1/D, S ≤ (2^q−1)/D} — a bounded polytope in
     b-space. Define f(b) = min over XY's (q−1)-cut strategies of A. — hard-regime setup.
  2. f is piecewise-LINEAR and continuous on K_q. — because A is jointly PL in (b, cut-positions) over the
     sort-order arrangement, and partial-minimisation of a jointly-PL function over the (compact) cut
     polytope yields a PL function of b (KB: marginal of a PL function is PL when the min is attained).
  3. max_{K_q} f is attained at a VERTEX of the arrangement subdividing K_q by the sort-order/gap/sum
     hyperplanes. — because a PL function is linear on each cell and a linear function on a bounded cell
     attains its max at a 0-cell (vertex). This is the EXACT tool that closed the lower bound; concavity
     is NOT invoked, so the r3 refutation does not touch it.
  4. IH(q) ⟺ f(v) ≤ 1/D at every arrangement vertex v. Classify vertices by which constraints are active:
       (T) a TIE b_i = b_{i+1}: XY pair-cancels the equal pair for free ⟹ q−1 pieces, one fewer cut ⟹
           f(v) ≤ f on an IH(q−1) instance ≤ 1/D by INDUCTION on q. — pair-cancellation (Lemma X/H).
       (G) a gap = 1/D: CaseB-Reduction 2 (certified) gives A ≤ that gap = 1/D. — no new work.
       (S) only the sum constraint S = (2^q−1)/D active, no tie, all gaps > 1/D: the isolated
           geometric-family vertex b_k = 2^{q−k}/D. Bound f directly by an explicit leaf strategy.
  5. Combine: every vertex falls in (T) ∪ (G) ∪ (S); (T),(G) closed by import/induction; (S) is a finite,
     isolated set (the geometric vertex per q) — the only genuine new leaf to bound. IH(q) for all q ⟹
     Case-B B1-large upper bound for all n, and (via the same vertex classification on the boundary sum)
     B2's sum-boundary too.
Key lemmas (claim + mechanism):
  - PL-max-at-vertex for f: max of a piecewise-linear function over a bounded polytopal complex is attained
    at a vertex — because f is linear on each closed cell and a bounded linear program is optimised at an
    extreme point. This is the load-bearing reframing that dodges BOTH graveyard obstructions.
  - Tie vertices reduce q: at b_i = b_{i+1} the two equal pieces XOR-cancel (μ(⊕) drops the pair), leaving
    a q−1-piece instance strictly inside IH(q−1) — because removing an equal pair lowers the sum below the
    tie-config's, staying under the (2^{q−1}−1)/D boundary; induction on q closes it.
  - Geometric-vertex leaf (S): at the isolated non-tie sum-boundary vertex, f = 1/D EXACTLY (the geometric
    achieves A = 1/D with q−1 cuts and no strategy beats it) — because the geometric's every cut is forced
    by its dyadic dominance; this is the unique tight vertex, matching the answer's tightness.
Open gaps: (a) rigorously establish f PL + max-at-vertex on K_q (the marginal-of-PL step 2-3 — this is the
whole novelty, must be airtight); (b) the geometric-vertex leaf bound f(S-vertex) ≤ 1/D (step 4 case S);
(c) verify the vertex classification is EXHAUSTIVE (no vertex escapes T∪G∪S).
Cases to cover: vertex types T (tie), G (gap=1/D), S (pure sum-boundary geometric); plus base IH(q≤4)
(certified) as the induction base.
Watch out for: DO NOT slip into a concavity claim for f — max-at-vertex needs only PL-ness (r3 killed
concavity via an interior VALLEY; a valley is a local MIN and is harmless for an upper bound, but never
argue f is concave). The r6 fixed-point obstruction only kills SINGLE-STEP descent; the vertex reduction
is a global max characterisation, not a descent — keep it that way.
KILL-SWITCH (run BEFORE build): enumerate/densely-sample the arrangement vertices of K_5 (configs with a
tie, or a gap = 1/D, or the pure sum-boundary geometric) and evaluate f (best over a fine 4-cut search) at
each. PASS iff max over ALL sampled interior configs AND all vertices of f ≤ 1/D with the geometric the
unique attainer at exactly 1/D. If ANY interior arrangement vertex gives f > 1/D (an interior PEAK above
1/D), the framing is REFUTED — kill it at the gate, do not build. (Explorer's dense q=5 sampling already
found no config with A > 1/D and geometric worst at exactly 1/D — consistent, but re-run targeting vertices.)

---

### upper-general-cascade: advance
Target: The whole problem's UPPER bound in Case B — specifically closing sub-case B2 (a_1 ≤ c(n)) for
general n, the second open upper-bound gap. Lower bound + IH(q≤4) imported.
Technique: Corrected double-cancel entry + a B2-flat leaf. FIRST fix the arithmetic error (r7 B2 explorer):
the double-cancel entry threshold is 3·2^{n-2}/D, NOT 2^{n-1}/D. The true B2 residual (a_2+a_3 ≤ 3·2^{n-2}/D)
is EMPTY for n ≤ 2 but NONEMPTY for n ≥ 3 — so B2 for n ≥ 3 is genuinely open and the file's current claim
must be corrected before advancing.
Skeleton:
  1. Correct the entry: double-cancel (cut a_1 at a_2, then residual at a_3) removes 2(a_2+a_3); active
     sum 1−2(a_2+a_3) < (2^{n-1}−1)/D ⟺ a_2+a_3 > 3·2^{n-2}/D. Above this, IH(n−1) closes. — arithmetic fix.
  2. Geometric config sits EXACTLY at a_2+a_3 = 3·2^{n-2}/D (verified n=2..5) ⟹ the entry is tight at the
     geometric; the true residual a_2+a_3 ≤ 3·2^{n-2}/D is the honest open set for n ≥ 3.
  3. B2-flat leaf on the residual: in a_2+a_3 ≤ 3·2^{n-2}/D the pieces are tightly bounded — a_2 < 3·2^{n-2}/D,
     a_3 < 3·2^{n-3}/D, cascading a_k < 3·2^{n-k}/D — mirroring how IH4-flat exploited b_2 < 4/D. Build an
     explicit n-cut leaf strategy collapsing to a bounded number of controlled singletons and bound their
     alternating sum < 1/D using these dyadic caps. — by Lemma X + the geometric-cap chain.
Key lemmas (claim + mechanism):
  - Corrected entry threshold 3·2^{n-2}/D — because 1 − 2(a_2+a_3) < (2^{n-1}−1)/D rearranges to
    a_2+a_3 > (D − 2^{n-1}+1)/(2D) = 3·2^{n-1}/(2D) = 3·2^{n-2}/D (the file's 2^{n-1}/D is 50% too small).
  - Dyadic cap chain in the residual: a_j < 3·2^{n-j}/D — because a_2+a_3 ≤ 3·2^{n-2}/D with gaps > 1/D
    forces each a_j below the geometric ceiling, giving the IH4-flat-style small-piece control that makes
    an explicit leaf bound possible.
Open gaps: the B2-flat leaf strategy (step 3) — the explicit cut pattern and its < 1/D bound are not yet
written; this is the real work. Triple-cancel (cut a_1 at a_2,a_3,a_4) is a candidate opener when
a_2+a_3+a_4 > (3·2^{n-2}+2)/D — enumerate whether it plus B2-flat covers the whole residual.
Cases to cover: a_2+a_3 > 3·2^{n-2}/D (double-cancel, done via IH(n−1)); a_2+a_3 ≤ 3·2^{n-2}/D (B2-flat
leaf / triple-cancel — the open residual, nonempty for n ≥ 3).
Watch out for: the file currently states the WRONG threshold 2^{n-1}/D and "B2 settled for n ≤ 2 for the
right reason" — it's right only because that residual is vacuously empty for n ≤ 4; the correction exposes
a real n=3,4 residual. Concrete residual witnesses to test the leaf on: n=3 {47/90,31/135,43/270,4/45};
n=5 {32/63,2/15,73/630,31/315,17/210,4/63}. Do NOT re-propose IH+(m) dual-bound (refuted r6).

---

### Field summary for the outline-reviewer
- **direct-constructive** — ADVANCE (L2, augmented Δ-vertex): closes the sole lower-bound gap; could flip
  the LOWER bound fully closed this round. Highest expected value.
- **upper-vertex-reduction** — NEW (copy-of direct-constructive): the genuinely-different upper framing
  DUE by the shared-gap-plateau rule (q-induction wall unmoved 3+ rounds). Carries an explicit numerical
  kill-switch (interior-peak check on K_5) to apply AT THE GATE before any build. Evades both the r6
  fixed-point obstruction and the r3 concavity refutation by construction.
- **upper-general-cascade** — ADVANCE (B2, corrected threshold 3·2^{n-2}/D + B2-flat leaf): first fix the
  r7-flagged arithmetic error, then attack the now-exposed n≥3 residual.

build set (recommended): direct-constructive, upper-vertex-reduction, upper-general-cascade
(gate upper-vertex-reduction on its kill-switch; if it fails the interior-peak check, drop it and fall
back to FRAMING 2 — the IH5-flat 2-delta leaf — as the upper new-framing slot.)
