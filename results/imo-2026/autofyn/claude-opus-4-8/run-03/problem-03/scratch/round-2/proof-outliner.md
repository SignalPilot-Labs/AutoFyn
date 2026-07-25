## imo-2026-03

Context carried in: answer c(n)=2^n/D_n (D_n=2^{n+1}−1), the L0/L1 reduction to the
multiset-refinement game, and the lower bound are all confirmed (numerics solid across the
field). The UPPER bound is the sole crux, and the whole field currently shares one
primitive: per-cut match-vs-bisect on the peeled top piece. Round-2 explorers established
two hard facts that reshape the field:
  (F1) NO one-pass local match/bisect rule works — every syntactic rule (even the correct
       clamp a = max(C/2, min(C,q)) applied greedily, or "match till last cut") fails on
       15–30% of random partitions. The upper bound needs genuine backward-induction / DP
       weighing the whole remaining list, OR a framing that sidesteps an explicit strategy.
  (F2) Two new tools that sidestep rank/parity bookkeeping: (a) the min-pairing identity
       S = min over adjacent pairings of Σ|diffs| + leftover (existential certificate), and
       (b) a smoothing/exchange argument on the LB-partition space (max side), proving
       dyadic maximizes XY's forced value without ever building an explicit XY strategy.

Field: revise the two S-sharing recursion approaches to obey (F1); repurpose the broken
explicit-certificate around the min-pairing certificate (F2a); open ONE genuinely different
framing, smoothing-extremal (F2b), that attacks the upper bound from the max side.

Recurring facts for every skeleton below (state once, all reuse):
  - L2 identity: LB total = (1+S)/2, S = Σ(−1)^{i+1}p_(i); upper bound ⇔ S ≤ 1/D_n.
  - Min-pairing identity (provable, checked exact): for y_1≥…≥y_m, S equals the MINIMUM
    over pairings-into-adjacent-pairs (+one leftover if m odd) of Σ_pairs|y_i−y_j| +
    y_leftover, attained by consecutive pairing. Mechanism: uncrossing/exchange — swapping
    a crossing pair to nested never increases cost. Consequence: ANY witness pairing with
    cost ≤ V proves S ≤ V (no need to know ranks).

---

induction-peel: revise
Target: c(n) = 2^n/(2^{n+1}−1) — both bounds, LB guarantee ≥ c(n) and XY response ≤ c(n).
Technique: strong induction on n via the self-similar peel; UPPER bound re-planned as a
  genuine backward-induction on the value function (NOT a syntactic per-step rule — F1).
Skeleton:
  1. Reduce to the multiset game — by L0 (greedy claim) + L1 (order irrelevance).
  2. Base n=1: c(1)=2/3, finite case analysis (unchanged, rigorous in explorer report).
  3. Lower bound: LB plays dyadic G_n; every XY refinement has odd-rank sum ≥ 2^n/D_n —
     by Lemma A (superincreasing forces small parts to even ranks; IH on scaled rest).
  4. Upper bound: define the value function V_n(A) = min over ≤n cuts of odd-rank sum of
     LB partition A; prove V_n(A) ≤ (sum A)·2^n/D_n for every A with ≤ n+1 parts — by
     Lemma B', a backward-induction where XY's first cut is chosen as the arg-min of the
     resulting (n−1)-subgame (EXISTENCE via IH, not a closed-form rule).
  5. Combine + verify n=1,2,3 (2/3, 4/7, 8/15).
Key lemmas (claim + mechanism):
  - Lemma A (unchanged): LB=G_n ⇒ S ≥ 1/D_n, because g* = (mass of rest)+(smallest part)
    (superincreasing), so each small part is forced to an even rank; IH on the
    ((2^n−1)/D_n)-scaled G_{n−1} handles the rest.
  - Lemma B' (REVISED — this is the whole point of the revise): V_n(A) ≤ (sumA)·2^n/D_n.
    Mechanism: strong induction on n. XY makes ONE cut on the largest part a_1, producing
    a partition A' with n+2 candidate parts and n−1 cuts left; V_n(A) = min over that one
    cut of V_{n−1}(A'). It SUFFICES to exhibit ONE good cut. The two candidate cuts to
    analyze are MATCH (a_1 → (a_2, a_1−a_2)) and BISECT (a_1 → (a_1/2, a_1/2)); take the
    minimizing one AND apply IH to the residual — the IH already encodes the multi-step
    lookahead (F1), so no syntactic one-pass rule is claimed. Prove the value bound via the
    invariant r = a_1 / (sum of the rest) (the ratio mirroring superincreasing, per F1):
    if r ≥ 1 (top dominates) BISECT drives value ≤ a_1/2 + IH-bound on rest ≤ target; if
    r < 1 MATCH cancels a_2 and the carry a_1−a_2 re-enters a strictly smaller subgame,
    IH closes it. Equalizing the two branches over LB's choice pins the geometric ratio 2
    and the value 2^n/D_n. Derive u(n)=(2^n−1)/D_n from u(n−1) as the scalar check.
Open gaps: Lemma B' — (i) prove V_n(A)=min over the one cut of V_{n−1}(A') (that XY need
  only consider cutting the current largest, and only MATCH/BISECT among cuts of it —
  interchange argument, this is where F1's "no naive rule" bites, must be an existence
  argument closed by IH not a fixed rule); (ii) the r≥1 vs r<1 branch inequalities;
  (iii) equalization pins dyadic as LB's maximizer (derive, don't assume). L0 exchange
  argument (shared). Lemma A rank-interleaving rigor.
Cases to cover: r ≥ 1 vs r < 1; partitions with < n+1 parts (pad zeros); tied largest
  parts (cheap-kill: zero-cost match cancels both); XY need NOT use all n cuts.
Watch out for: F1 — do NOT let the builder collapse Lemma B' back to a one-pass greedy
  rule; the argument must be "min over the cut, closed by IH." XY need not use all cuts
  (forcing full usage overshoots to 0.75 on a lone piece). Keep the +1 in superincreasing.

---

alternating-sum-potential: revise
Target: c(n) = 2^n/(2^{n+1}−1), both bounds (via max_LB min_XY S = 1/D_n).
Technique: global scalar monovariant on S; UPPER bound re-grounded so the per-cut
  contraction is an EXACT inequality on a genuinely monovariant reserve (not "S contracts"),
  and the terminal accounting is discharged by the min-pairing witness (F2a) rather than a
  cut-by-cut rank claim — this is the revise.
Skeleton:
  1. Reduce to multiset game + S-potential (L0, L1, L2).
  2. Lower: LB=G_n ⇒ S ≥ 1/D_n for every ≤n-cut refinement — Lemma C (reserve monovariant).
  3. Upper: for any LB partition, XY refines (≤n cuts) so S ≤ 1/D_n — Lemma D' (below).
  4. Conclude S-value = 1/D_n ⇒ c(n); verify n=1,2,3.
Key lemmas (claim + mechanism):
  - Lemma C (unchanged): reserve Φ = surplus 2^n − (2^{n−1}+…+1) = 1 (units 1/D_n) is a
    conserved lower bound for S under any refinement of the superincreasing dyadic.
  - Lemma D' (REVISED): XY has ≤n cuts producing final pieces that admit an explicit
    adjacent pairing of cost Σ|diffs| + leftover ≤ 1/D_n; then S ≤ that cost ≤ 1/D_n by
    the min-pairing identity. Mechanism: XY builds pieces so each large piece is matched
    to a near-equal twin (small |diff|) and the single leftover is the shrinking carry.
    The per-cut monovariant is now on the WITNESS cost, not on ranks: each cut either
    creates a matched pair (adds a small |diff| to the running cost) or halves the carry
    (leftover), and the total witness cost telescopes to ≤ 1/D_n after n cuts. Because the
    bound is via a witness (S = min ≤ witness), XY never needs to prove any piece's actual
    rank/parity (this discharges the round-1 "parity of m=k+#cuts" and "slivers" worries).
Open gaps: Lemma D' — construct, for arbitrary A, the ≤n cuts AND the pairing achieving
  witness cost ≤ 1/D_n, and prove the per-cut cost telescopes to 1/D_n (this still needs
  the match/bisect construction — F1 — but the ACCOUNTING is via pairing cost, strictly
  lighter than rank tracking). Lemma C reserve inequality made exact. L0 (shared).
Cases to cover: match vs bisect per cut; < n+1 parts; tied pieces; carry-only leftover
  when no original remains to match.
Watch out for: the witness pairing must actually be a valid pairing of the FINAL multiset
  (twin + original both survive as two pieces — the F1 bookkeeping trap: a matched twin
  does NOT delete the original). Don't force full cut usage.

---

explicit-certificate: revise
Target: c(n) = 2^n/(2^{n+1}−1), both bounds.
Technique: two explicit certificates — Hall/marriage injection (lower, Lemma E, kept) and
  a min-pairing existential certificate (upper, replacing the REFUTED "concentrate don't
  spread" Lemma F). This is the natural home for F2a: existential, no rank/parity, no
  Schur-convexity hand-wave.
Skeleton:
  1. Reduce to multiset game (L0, L1).
  2. Lower: LB=G_n; inject small parts g_0..g_{n−1} into distinct even ranks (Hall) ⇒
     LB ≥ g_n — Lemma E (unchanged, reviewer-sound).
  3. Upper (REPLACED): for any LB partition A, exhibit ≤n cuts and an adjacent pairing of
     the resulting pieces with Σ|diffs| + leftover ≤ 1/D_n ⇒ S ≤ 1/D_n ⇒ odd-rank sum
     ≤ c(n) — Lemma F' (min-pairing certificate).
  4. Conclude + verify n=1,2,3.
Key lemmas (claim + mechanism):
  - Lemma E (kept): Hall condition |{final pieces ≥ g_j}| ≤ (#odd ranks above g_j's slot)
    holds because XY's ≤n cuts create ≤n extra pieces and dyadic spacing 2^j leaves room
    for exactly one XY sub-piece between thresholds; injection ⇒ XY (even ranks) ≤ (2^n−1)/D_n.
  - Lemma F' (NEW, replaces refuted F): construct the cuts + witness pairing. Mechanism:
    process A's parts largest-first with a carry; MATCH the carry against the next part
    (creating a near-equal pair, |diff| small) when the next part ≥ carry/2, else BISECT
    the carry (its two halves form a zero-|diff| pair). Pair each created piece with its
    partner; the accumulated Σ|diffs| + final leftover ≤ 1/D_n. Since S = MIN over all
    pairings, this ONE witness pairing upper-bounds S — no need that this pairing be the
    optimal one, and NO rank/parity/"spreading" claim is made (this is exactly why the
    refuted "concentrate don't spread" is not needed: the witness is allowed to be any
    valid pairing, spreading or not).
Open gaps: Lemma F' — prove the constructed witness cost ≤ 1/D_n for EVERY A (this is the
  same F1 obligation as Lemma B'/D', but recast as a cost bound — the builder should share
  the core construction/accounting with alternating-sum-potential's Lemma D' if useful).
  Lemma E Hall inequality made rigorous vs slivers. L0 (shared).
Cases to cover: dominant top part (bisect branch); ties (cancel); < n+1 parts; balanced
  near-dyadic (match branch, the tight case).
Watch out for: do NOT resurrect "concentrate cuts on the largest, don't spread" — REFUTED
  ({0.428,0.410,0.162} at n=2 needs slivering). The witness pairing must range over the
  actual final multiset including surviving originals (F1 trap).

---

smoothing-extremal: new
Target: c(n) = 2^n/(2^{n+1}−1), both bounds — GENUINELY DIFFERENT framing of the upper
  bound (attacks the max side; never builds an explicit XY strategy for arbitrary A).
Technique: extremal principle + exchange/smoothing on the LB-partition space (F2b). Let
  F(A) = min over XY's ≤n cuts of odd-rank sum of LB partition A. Prove max_A F(A) is
  attained at dyadic G_n by showing any non-dyadic A can be perturbed toward dyadic without
  DECREASING F; then max_A F(A) = F(G_n) = 2^n/D_n gives the upper bound F(A) ≤ 2^n/D_n
  for all A at once. The explicit XY response is needed ONLY at (near-)dyadic profiles.
Skeleton:
  1. Reduce to the multiset game (L0, L1); define F(A), F homogeneous of degree 1.
  2. Existence of a maximizer: F is continuous on the compact simplex of partitions with
     ≤ n+1 parts summing to 1 (F = min of finitely many continuous cut-response values),
     so max_A F(A) is attained — by extreme value theorem.
  3. Smoothing lemma (KEY): at any non-dyadic maximizer candidate A there exist two
     consecutive-rank parts (a_i, a_{i+1}) with ratio ≠ 2; the sum-preserving perturbation
     moving them toward ratio 2 does not decrease F. Iterating (finite-improvement /
     limit) drives A to G_n — by exchange/smoothing (KEY GAP, Lemma G).
  4. Evaluate F(G_n) = 2^n/D_n (this is exactly the lower-bound computation, already solid).
  5. Therefore F(A) ≤ F(G_n) = 2^n/D_n for all A (upper bound); combine with LB (F(G_n) ≥
     2^n/D_n) ⇒ c(n) = 2^n/D_n. Verify n=1,2,3.
Key lemmas (claim + mechanism):
  - Lemma G (smoothing monovariant — THE hard gap): moving a consecutive-rank pair toward
    the 2:1 ratio (sum fixed) does not decrease XY's forced value F. Mechanism candidate:
    at ratio ≠ 2, XY's best response leaves LB with a slack that a small re-allocation of
    mass toward 2:1 converts into extra protection for LB's odd-rank pieces (equivalently,
    away from 2:1 XY gains an extra cancellation, so F strictly drops as you move AWAY from
    dyadic). Prove via the S-form: show ∂S*/∂(perturbation toward 2:1) ≥ 0 where S* is
    XY's minimized S, using that at the dyadic ratios the superincreasing margin is exactly
    the smallest part (the equalizer), and any deviation slackens one telescoped gap.
  - Uses the min-pairing identity (F2a) as the tool to evaluate S* under the perturbation
    without rank bookkeeping.
Open gaps: Lemma G — the entire content. This framing is UNVERIFIED numerically (explorer
  flagged it as distinct-but-untested), so before heavy investment the builder should
  first NUMERICALLY check the monotonicity claim (perturb random non-dyadic A toward 2:1
  ratios, confirm F does not decrease) on n=2,3; if it fails, this approach is refuted and
  routes back. Also: the perturbation must stay within ≤ n+1 parts and the maximizer's
  active-parts count must be handled (could be < n+1).
Cases to cover: maximizer with fewer than n+1 active parts; perturbations that would merge
  two parts or split into a new one; boundary of the simplex (some part → 0).
Watch out for: F is a max-min, so "perturb toward dyadic doesn't decrease F" is a claim
  about the WORST XY response tracking under perturbation — XY's optimal response can jump
  discontinuously in strategy (which cut) even though F is continuous; the smoothing must
  bound F, not assume a fixed XY response persists. This is the crux risk and why the
  numerical pre-check gates the approach.
