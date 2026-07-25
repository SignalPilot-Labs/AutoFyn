## imo-2026-03 — lens: the residual LOWER-BOUND gap (A-res / G1 / GAP-LB)

### 1. Cleanest restatement of the residual inequality

Work in units of 1/D_n with P_n = {2^0,…,2^n}. Fix n ≥ 1, H = 2^{n-1}. Let B be a ≤n-cut
refinement of P_n with c ≥ 1 cuts spent inside the top part 2^n, producing Q (sum 2^n, c+1
parts) and C = the refinement of R = {2^0,…,2^{n-1}} = "P_{n-1}" using the remaining ≤ n−c
cuts (sum 2^n − 1). Write h = (max(Q) − H)^+; the open sub-case is **h < 1** (all three live
approaches agree this is exactly the residual — Lemma H / L7 disposes of h ≥ 1 unconditionally).
By the XOR identity (L3),
  S(B) = S(Q) + S(C) − 2W,  W := meas{t < H : N_Q(t) odd ∧ N_C(t) odd} (confined to t<H since
  every part of C is ≤ H — L6/L7 band confinement).
IH gives S(C) ≥ 1 (from G(n−1)). The obligation is
  **S(Q) + S(C) − 2W ≥ 1,  equivalently  W ≤ (S(Q) + S(C) − 1)/2.**
This is A-res / G1 / GAP-LB verbatim — identical statement across all three approach files.

### 2. Why the naive bounds fail — AND a sharper diagnosis than "cut-budget on C"

I numerically hunted the true minimizer of S(B) inside the h<1 sub-case (n = 2,3,4, both
random search and Nelder–Mead optimization over Q's shape at fixed cut allocation). Two
findings that should change the outliner's framing:

**(a) The field's working hypothesis — "W is capped because cuts are spent on C" — is
numerically FALSE as the driving mechanism.** At n = 3, the *global* minimizer of S(B) among
h<1 configurations occurs at **r = 0 cuts spent on C** (C = R = {4,2,1} left completely
uncut, all n cuts spent on the top block) — verified by direct optimization: min S(B) = 1.000000
exactly, attained at Q → {4, 2, 1, 1} (i.e. Q converges to an exact **copy of C plus one extra
unit at the bottom scale**). At that point W ≈ 2.18 — *large*, not small — while S(Q) ≈ 2.37,
S(C) = 3. The trivial bound (†) W ≤ min(S(Q),S(C)) gives slack of only ≈0.08; the "cut count on
C" (r=0!) gives no information at all, since C is not cut. So a proof strategy that tries to
literally charge W against the number of cuts spent inside C cannot work — C can be *fully
uncut* and W still be forced large, and the truth only emerges from S(Q) and S(C) being
correspondingly large and *precisely aligned* with W.

**(b) The exact binding extremal witness is the SAME dyadic cascade as the round-3
upper-bound witness.** B_min = {4,4,2,2,1,1,1} for n=3 (two copies of {4,2,1} + one extra 1) is
*exactly* the cascade construction in alternating-sum-potential §4 (XY's cut sequence: bisect
top, then bisect one resulting half, …, down to the bottom scale). This is strong evidence that
the lower-bound residual and the upper-bound crux (G2 / Lemma D / Open gap 2) are not
independent — they are both governed by the same extremal object. A framing that proves
"S(B) ≥ 1 with equality iff B is (up to relabeling) this cascade family" would likely close
*both* gaps at once, or at least illuminate why 1/D_n is exactly the fixed point.

**(c) A second, cleanly disjoint extremal mechanism exists and is fully closable NOW.** When
c = 1 and Q is split *exactly in half* (Q = {2^{n-1}, 2^{n-1}}, the pure BISECT), N_Q(t) is even
for every t (2 parts, always tied) — this forces **W = 0 automatically, independent of C**, so
S(B) = S(Q) + S(C) = 0 + S(C) ≥ 1 straight from the IH, with **zero further argument**. This is
the boundary case h = 0 of the residual and is a genuine one-line sub-lemma any approach can
bank for free: *"if Q's sorted sequence pairs up into equal consecutive values (b_(2i-1)=b_(2i)
for all i), then W = 0 and S(B) = S(C) ≥ 1 by IH alone."* It does not cover the interior of the
h<1 regime (Q only near-bisected, or more than 2 shards), but it is a real, provable partial
win and a template for how "self-cancelling Q" configurations bypass the overlap problem
entirely.

### 3. Distinct openings to inject the missing content

1. **Matching/β-reformulation instead of layer-cake overlap (promising, genuinely different
   framing).** By L4, S(B) = sum(B) − 2β(B), β = max-weight matching (adjacent-pair sum). The
   residual becomes: show **β(B) ≤ (D_n − 1)/2** directly, i.e. bound the BEST matching's total
   weight combinatorially using the superincreasing scale gaps (each pair in an optimal matching
   pairs two shards from *adjacent* sorted ranks; use that no shard of C exceeds H and at most
   one shard of Q exceeds H to bound how many "high-value" pairs a matching can form). This
   sidesteps the W/overlap measure-theoretic picture (which the numerics show is unexpectedly
   subtle — large W is not itself the enemy) and works with combinatorial matchings, where a
   counting/pigeonhole argument on shard *ranks* rather than shard *measure* may be more
   tractable. Not yet attempted by any live approach — worth opening as approach content, not
   just noted as a lemma.

2. **Strengthen the induction hypothesis from S(C) ≥ 1 (an integral) to a pointwise / profile
   statement about N_C(t).** Finding (a) shows the scalar S(C) ≥ 1 alone is provably too weak to
   combine with any scalar bound on W — the *shape* of C's odd-region (not just its total
   measure) is what interacts with Q's shape at the extremal point (Q literally becomes a copy
   of C). A stronger IH — e.g. "for every t < H, meas{s < t : N_C(s) odd} obeys some bound
   depending on t and the scale 2^{n-1}" or "N_C's jump points lie only at the dyadic sub-scale
   boundaries up to the cut budget" — would let the induction control the *interaction* directly
   rather than post-hoc via a scalar W bound. This is more work to set up but directly targets
   what finding (a)/(b) show is missing. Likely the most honest fix, but heavier to formalize.

3. **Unify lower + upper bound via a single sharp characterization of the extremal cascade
   (ambitious, but backed by finding (b)).** Prove directly "S(B) ≥ 1 for all valid B, with
   equality *iff* B is a cascade-type configuration" via an exchange/smoothing argument on B
   itself (not on A, which is what smoothing-extremal tried and got refuted). CAUTION: this is
   close in spirit to the refuted smoothing-extremal approach (Lemma G, round 2) — that refutation
   was specifically about sum-preserving pair moves on the *choice set A* toward dyadic, not
   about smoothing a *fixed refinement B of the fixed dyadic P_n* toward the cascade witness.
   These are different questions (A is LB's free choice; B is XY's response to the already-fixed
   dyadic A). It is plausible this reopens a real path, but it must be checked from scratch —
   don't assume the refutation transfers.

4. **Amortized frontier potential (process framing, not static block decomposition — genuinely
   different from all 3 live approaches' static Q/C split).** Sweep t from 0 upward (or process B's
   parts from smallest to largest) maintaining an invariant like "the running deficit of
   odd-measure accumulated so far is bounded by a linear function of the scale reached," proved
   by induction on t crossing each part-boundary and charging each crossing against the part's
   own contribution — in the style of aimo-0019's frontier-potential game proof (see §4 below).
   This trades the "decompose into Q and C, bound W" static picture for a dynamic accounting that
   might naturally explain why the deficit caps at exactly 1 (the superincreasing "+1"). Promising
   as a genuinely different top-level framing per the plateau rule.

Likely dead-end / already-refuted, do not retry: the plain interval bounds |S(Q)−S(C)| and
h+|S_low(Q)−S(C)| (both proven too weak, round 3, and confirmed here numerically — at the r=0
n=3 extremal, |S(Q)-S(C)| ≈ 0.63, nowhere near the true bound of 1); "cut-count on C directly
caps W" as a literal mechanism (refuted by finding (a) above — flag this explicitly to whichever
approach still writes it that way, since induction-peel/global-max-peel/alternating-sum's prose
all currently *describe* the missing ingredient as "the cut budget on C caps W," which this
exploration shows is not the right mental model at the true extremal point).

### 4. Candidate technique(s)
- **L4 min-pairing / β reformulation** (already certified) — underused for a LOWER bound; so far
  only used as an upper-bound witness tool. Opening 1 above uses it in the other direction.
- **Induction hypothesis strengthening** (standard IMO technique: prove a stronger, more
  structural statement by induction than the one actually needed) — Opening 2.
- **Amortized/frontier charging** (cf. aimo-0019 crux below) — Opening 4.
- Layer-cake / XOR (L3) remains the natural language for stating the gap, but per finding (a) it
  may not be the natural language for *proving* it.

### 5. Knowledge-base entries to use
Read `knowledge_base.md` for generic entries; the load-bearing project-specific facts are
already the certified lemmas L0–L8 in `results/imo-2026-03/lemmas/`, all directly reusable:
L3 (layer-cake + XOR), L4 (min-pairing/β), L6 (at-most-one-large-shard / A0), L7 (Lemma H,
unconditional h≥1 case — NOT reusable for the residual itself, but frames exactly which sub-case
remains), L8 (φ-telescoping Case-1 generalization — same structural family, shows the "+1" is
spent exactly once at the extremal cascade).

### 6. Analogous past problems (crux corpus)
Filtered `combinatorics` domain by keyword sweep (budget/matching/pairing/layer/extremal/
amortized/superincreasing/cascade) over `past_crux_moves_database.json`. Best matches:
- **aimo-0019** (games-and-strategy / invariants-and-monovariants) — paint-budget game on [0,1]
  with dyadic ink amounts. Crux: "Maintain a linear potential bounding cumulative resource by a
  constant times progress, proved by amortized induction that charges each frontier advance
  against the pieces it absorbs" — this is precisely the *shape* of argument Opening 4 proposes:
  an amortized/frontier potential over a dyadic-scale process, proving a resource cap (3 < 4
  units of ink) via charging each step against what it absorbs, exactly analogous to needing to
  cap W by charging it against the "progress" made in the induction. Genuinely analogous
  technique, not just same-subtopic; worth reading in full if Opening 4 is picked up.
- **aimo-0156** (induction-and-construction / telescoping-and-summation) — dyadic frog-hop
  problem on {1,…,2^n−1}, self-similar recursive split into two isomorphic sub-lattices "linked
  by one connecting move," with an Abel-summation bound built from suffix sums capped by
  self-avoiding-walk lengths within residue classes mod 2^m. Structurally resonant with our
  problem's self-similarity (R is literally a copy of P_{n-1}) and the extremal cascade using
  "one extra unit" at the bottom — the "+1" / "one connecting move" pattern recurs. Less directly
  a budget-cap argument, more a reminder that dyadic self-similar problems often close via an
  Abel/telescoping identity across scales rather than a single scalar inequality.
- **aimo-0121** (processes-and-algorithms / invariants-and-monovariants) — token-shuffling with
  a move budget; crux move explicitly "split moves into two disjoint charges... add the two
  disjoint charges" to get a lower bound on move count past an assumed budget. Same shape as
  wanting to split the "+1" deficit into two disjoint charged pieces (e.g. one charge from the
  high band h, one from the low-band interaction) but for a genuinely different problem (process
  moves, not a static measure decomposition) — worth skimming if Opening 4 is developed, but
  the analogy is looser than aimo-0019's.
None of these directly hand over the overlap-cap inequality itself — no exact match found; they
are technique analogies (amortized charging, disjoint-charge splitting, self-similar recursive
linking), each a hint to adapt, not a citation.

### 7. Prior progress
Fully summarized in Section 1 above; nothing beyond what's in current.md / the three approach
files. All three approaches (induction-peel A-res, alternating-sum G1, global-max-peel GAP-LB)
independently derive the identical residual inequality via the identical XOR/band-confinement
mechanism (L3+L6/L7) — they are the same gap in different notation, confirmed by re-reading, not
merely asserted.

### 8. Dead ends (do not retry)
- Plain interval bounds |S(Q)−S(C)| and h+|S_low(Q)−S(C)| (round 3, reconfirmed numerically here).
- "Cut count spent inside C caps W" as a literal proof mechanism — refuted by finding (a): the
  true n=3 extremal minimizer spends **zero** cuts on C and still has large W. Any future
  approach that frames the residual as "bound W using the number of cuts in C" should be
  redirected — the content is in the *alignment* between Q's and C's shapes, not a raw cut count.
- smoothing-extremal's original mechanism (Lemma G, sum-preserving pair moves on A) — still dead;
  Opening 3 above is a different question (smoothing B, not A) and should not be conflated with it.

### 9. Small-case / intuition notes (all labeled conjecture/numeric evidence, not proof)
- Confirmed numerically (Nelder–Mead optimization + 400k-trial random search, n=2,3,4): the
  global minimum of S(B) over the entire h<1 sub-case is exactly 1, attained (up to symmetry) at
  the dyadic cascade B = two copies of {2^{n-1},…,2^0} plus one extra unit — matching the
  round-3 upper-bound witness exactly. This is strong (numeric) evidence that lower and upper
  bound cruxes share one extremal object, worth the outliner's attention as a genuine structural
  lead, not yet a proof.
- The "Q exactly bisected ⟹ W=0 ⟹ S(B)=S(C)≥1 by IH alone" sub-case (h=0 boundary) is fully
  rigorous right now and could be written up as a certifiable mini-lemma (zero new machinery,
  pure consequence of L3+L4) covering a slice of the residual for free.
