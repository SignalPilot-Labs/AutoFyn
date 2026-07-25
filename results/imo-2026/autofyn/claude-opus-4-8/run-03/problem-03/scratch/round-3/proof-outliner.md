## imo-2026-03

Answer (confirmed): c(n) = 2^n/D_n, D_n := 2^{n+1}−1. Certified foundation L0–L5 in
`lemmas/`: L0 claim=odd-rank sum, L1 order-irrelevance, L2 S_odd=(1+S)/2, L3 layer-cake
S=meas{#parts>t odd}, L4 min-pairing S=sum−2β (witness principle). Both remaining gaps
live on the SAME extremal object — the MATCH/BISECT cascade — but the two live approaches
share one wall (control the layer-cake overlap W / beat the value-function IH). I hand up
FOUR approaches with **deliberately different mechanisms on the shared crux** so they do
not die together: two advances on differentiated routes, one new far-from-field lower-bound
induction, one new far-from-field upper-bound exchange argument. smoothing-extremal is
retired (Lemma G refuted, mechanism re-imports the crux — no nomination).

Two structural facts verified numerically this round (hand these to builders as free
inputs):
- **Peel-max identity (exact, 0/20000):** S(B) = b_(1) − S(B∖{b_(1)}) for ANY multiset,
  no strict-max needed (removing the top flips the sign of the rest's alternating sum).
- **Min-odd-sum floor (exact, 0/20000):** S_odd(P) ≥ sum(P)/2 for every multiset — so the
  value-function base case V_0(A)=S_odd(A) ≤ sum(A) holds for ANY part count (this fixes a
  latent bug in Lemma B — see induction-peel below).

---

### induction-peel: advance
Target: c(n) = 2^n/D_n — both bounds, via strong induction peeling the top dyadic scale
(value-function DP on the multiset-refinement game).
Technique: backward induction on the cut budget k for a value function V_k(A); layer-cake
L3 for the lower bound.
Skeleton (only the two open gaps remain; L0–L3, base n=1, lower-bound Case 1 are DONE):
  1. Lower-bound Case 2 (Sub-claim A2) — band-split the layer-cake at height 2^{n-1}.
  2. Upper-bound (Sub-claim B) — value-function induction with a part-count fix and an
     r = a_1/ρ two-branch step.
Key lemmas (claim + mechanism):
  - **Sub-claim A2, sharpened via band decomposition.** Write B = Q ⊔ C (Q = c-cut
    refinement of the top 2^n, c≥1; C = ≤(n−c)-cut dyadic refinement of R={2^0..2^{n-1}},
    S(C) ≥ 1 by IH). Every part of C is ≤ 2^{n-1}, so N_C(t)=0 (even) for t>2^{n-1}: the
    overlap W = meas{N_Q odd ∧ N_C odd} lives **entirely in the low band t ≤ 2^{n-1}**, and
    all of S(C) lives there too. Also **at most one part of Q exceeds 2^{n-1}** (two would
    sum > 2^n = sum Q), so on the high band N_Q ∈ {0,1} and it contributes exactly
    h := max(q_1 − 2^{n-1}, 0), uncancellable. Hence
      S(B) = h + [S_low(Q) + S(C) − 2W] ≥ h + |S_low(Q) − S(C)|.
    The residual obligation is h + |S_low(Q) − S(C)| ≥ 1 — because it is FALSE that W can
    reach min(S_low(Q),S(C)) freely: W is capped by the (n−c)-cut budget on C. Close it by
    **strong induction on the cut budget c** (peel one top cut at a time; the numerics show
    the superincreasing "+1" is spent exactly once, at the bottom scale — see
    math-explorer-lowerbound), not by the abstract |S(Q)−S(C)| bound (proven too weak).
  - **Sub-claim B, with the part-count fix.** Restate Lemma B for ALL A (drop "≤ k+1
    parts" — it is unnecessary and breaks the one-cut recursion, since a BISECT grows the
    part count past k). Base k=0: V_0(A)=S_odd(A) ≤ sum(A)=sum(A)·2^0/D_0 by the min-odd-sum
    floor above — valid at any part count. Step: exhibit ONE split A→A′ with
    V_{k−1}(A′) ≤ sum(A)·2^k/D_k. Plain IH gives sum(A)·2^{k−1}/D_{k−1} which is too large
    by the exact factor 2D_{k−1}/D_k<1, so the split must genuinely beat IH. Parametrize by
    r := a_1/ρ (ρ = sum of the rest): if r ≥ 1 (top dominates the superincreasing boundary)
    **BISECT** caps a_1 at a_1/2 and the rest is closed by IH; if r < 1 **MATCH** cuts
    a_1→(a_2, a_1−a_2), the twin a_2 cancels its equal at adjacent rank (mechanism: two equal
    values at consecutive ranks contribute +a_2−a_2=0 to S), the carry a_1−a_2 enters a
    strictly smaller subgame. Equalizing the two branch bounds over LB's choice pins the
    geometric ratio 2 and the value 2^k/D_k (dyadic is the maximizer).
Open gaps: (A2) the induction-on-c closing of h+|S_low(Q)−S(C)|≥1 using the budget cap on W;
(B) the two branch inequalities + the equalization that pins dyadic.
Cases to cover: A2 — sub-cases q_1 ≥ 2^{n-1} (h>0) vs q_1 < 2^{n-1} (h=0, all mass in low
band). B — r ≥ 1 (BISECT) and r < 1 (MATCH), plus ties among the top (MATCH costs 0).
Watch out for: the "twin AND original both survive" pitfall — MATCH does NOT delete the
matched original, both stay in the final multiset (memory rule, round 2). Do NOT reintroduce
the "≤ k+1 parts" hypothesis. Keep any numeric probe n≤3, incremental, <30s.

---

### alternating-sum-potential: advance
Target: c(n) = 2^n/D_n — both bounds, via the layer-cake potential S = meas{N(t) odd} and
the min-pairing witness principle L4 (S = sum − 2β). Deliberately DIFFERENT mechanism from
induction-peel: analytic band-accounting for the lower bound, explicit witness construction
(not a DP) for the upper bound.
Technique: layer-cake measure accounting (L3) + min-pairing witness (L4).
Skeleton (L0–L4, n=1, lower case (i), XOR decomposition (†) are DONE):
  1. G1 (binding lower bound) — bound the overlap W directly by band + budget accounting.
  2. G2 (general upper bound) — build a witness pairing for arbitrary A via a "match to the
     layer-cake staircase" construction, charged in the aimo-0012 amortized style.
Key lemmas (claim + mechanism):
  - **G1 via band-confined W.** Same band decomposition as A2 but pushed through L4/L3
    purely analytically (no value-function recursion): S(whole) = S(Q)+S(R′)−2W with W
    confined to t ≤ 2^{n-1}. The NEW content vs. what is already in the file: bound W not by
    the trivial min(S(Q),S(R′)) but by **∫_{low} 1[N_{R′} odd] where the (n−j)-cut budget on
    R′ limits how many level-crossings N_{R′} can make** — each cut adds at most one odd
    interval to R′'s odd-region, so W ≤ (measure of R′'s odd-region reachable with n−j cuts),
    and the superincreasing gap between Q's scale (~2^n) and R′'s top scale (2^{n-1}) forces
    the residual ≥ 1. This is the missing "budget cap on W" that the file flags as open.
  - **G2 witness for arbitrary A (charging style, borrowing crux aimo-0012).** Sort
    A=(a_1≥…≥a_k). Greedily process from the top: maintain a "carry"; at each step MATCH the
    current carry/top against the next part (creating an equal twin to cancel) or BISECT when
    the top exceeds the running rest — but instead of proving a one-pass rule correct
    (refuted, F1), **charge each of the ≤ n cuts against the mass it moves into a matched
    pair**, and show the total unmatched surplus telescopes to ≤ sum(A)/D_n. Target: exhibit
    a pairing of the final multiset with β ≥ sum(A)(2^n−1)/D_n (witness principle ⇒ S ≤ 1/D_n).
    On the dyadic profile the construction reduces to the cascade with β = 2^n−1 exactly
    (already verified in the file). The amortized accounting (credit 1/D_n per cut) is the
    aimo-0012 mechanism — genuinely different bookkeeping from induction-peel's DP.
Open gaps: (G1) the budget-cap bound on W finishing S(whole) ≥ 1; (G2) the charging
argument proving β ≥ sum(A)(2^n−1)/D_n for arbitrary A (the shared crux — a real risk this
route also needs lookahead; if the pure charging stalls, fall back to importing
induction-peel's DP as a black box for the branch choice).
Cases to cover: G1 — j (cuts on top) from 1 to n; G2 — the regime a_1 ≳ ρ (near
superincreasing boundary) is where every prior one-pass rule failed; the charging must
survive exactly there.
Watch out for: do NOT restate β-induction as if distinct from the S-DP — algebraically
identical (S=sum−2β), same wall (explorer-verified). The witness principle only lightens
accounting, not the construction. Keep numerics n≤3, <30s.

---

### global-max-peel: new
Target: c(n) = 2^n/D_n — the WHOLE claim, but the new leverage is a single unified lower-bound
induction merging Case 1 and Case 2 (currently proved by two separate arguments in both live
files). Far-from-field: induct on total piece count peeling the CURRENT global max, not the
fixed original top piece.
Technique: strong induction on |B| via the exact peel-max identity S(B) = b_(1) − S(B∖{b_(1)})
(verified this round), with a generalized superincreasing-margin invariant.
Skeleton:
  1. Prove the peel-max identity S(B) = b_(1) − S(B∖{b_(1)}) (one line: removing the top
     element flips the sign of the remaining alternating sum). [free — verified 0/20000]
  2. State the GENERALIZED lower-bound claim G(n): every ≤n-cut refinement B of the
     superincreasing set {2^0,…,2^n} has S(B) ≥ 1.
  3. Let m = b_(1) be the global max of B (a shard of some original 2^j, possibly = 2^n
     uncut). Peel it: S(B) = m − S(B∖{m}). Reduce S(B∖{m}) ≤ m − 1 to a smaller superincreasing
     instance.
  4. Assemble: uncut top (m = 2^n) recovers Case 1 for free (m − S(rest) ≥ 2^n − (2^n−1) = 1
     by the trivial S ≤ sum bound); cut top (m < 2^n) becomes the same reduction with a
     smaller effective margin — no separate Case 2 bookkeeping.
Key lemmas (claim + mechanism):
  - **Generalized IH G(n):** the induction is on the NUMBER of parts of B (or on n with an
    auxiliary), peeling the global max each step. The superincreasing margin transfers: after
    removing the max shard m from 2^j, the residual multiset is a refinement of a superincreasing
    set with the top mass reduced, and the "+1" surplus 2^0=1 at the very bottom survives every
    peel (mechanism: 2^n = 1 + Σ_{i<n}2^i, and every peel of a top shard leaves the bottom
    unit untouched until the final scale). The target inequality S(B∖{m}) ≤ m − 1 is the
    per-step obligation; because m is the global max, m ≥ (sum of B∖{m})/(#parts), giving the
    slack the superincreasing structure needs.
Open gaps: the precise generalized IH statement that closes the per-step reduction S(B∖{m})
≤ m − 1 uniformly (this is where the two Cases currently split; the bet is that peeling by
GLOBAL max, not fixed 2^n, removes the asymmetric Q/C bookkeeping both live files are stuck
on). Also the dual upper-bound direction is left to a later round — this approach's near-term
deliverable is a clean unified LOWER bound.
Cases to cover: m = 2^n (uncut top) vs m = a shard of 2^j (top or interior cut) — but the
whole point is a SINGLE argument covering both; enumerate only to check the base and the
smallest-scale peel (m from 2^0).
Watch out for: the generalized IH must be over refinements of ARBITRARY superincreasing
multisets (not just {2^0,…,2^n}), else the peeled residual falls outside the hypothesis. Do
NOT re-derive the two-case split — if the induction forces a case split on m's origin, it has
not bought anything over induction-peel and should say so honestly.

---

### huffman-merge-exchange: new
Target: c(n) = 2^n/D_n — specifically a from-scratch UPPER-bound witness for arbitrary A,
far from the value-function DP and the layer-cake overlap, via a merge-tree exchange argument.
Technique: reverse-merge (Huffman-style) construction of XY's final multiset + an exchange
(uncrossing) lemma, using L4's min-pairing cost as the objective.
Skeleton:
  1. **Translation step (the make-or-break obligation).** By L4, S(final) = Σ_{consecutive
     pairs}|diff| + leftover. Recast XY building B from A as a REVERSE merge: think of the
     final sorted list and repeatedly combine the two smallest surviving masses into a matched
     pair, charging |diff| to the cost. Establish the correspondence "≤ n cuts on A ⟺ a merge
     forest over A's parts with ≤ n internal combine operations," and that XY's achievable
     min cost = the min-cost such forest. THIS IS UNVERIFIED (explorer flagged the objective
     is Σ|diff|, not literal weighted-path-length) — the first build must either nail the
     correspondence precisely or abandon the approach.
  2. **Exchange lemma:** in a min-cost merge forest the two smallest masses are combined
     first, and adjacent combines can be swapped without increasing cost (standard Huffman
     uncrossing, but re-proved for the Σ|diff| objective).
  3. On A = G_n the forest is the caterpillar/chain tree (geometric-ratio-2 weights Huffman
     to a chain), reproducing the cascade with cost 1/D_n — the internal consistency check.
  4. For arbitrary A, the exchange lemma structurally justifies WHY match/bisect are the only
     optimal combines, converting Sub-claim B's ad-hoc case split into one exchange argument.
Key lemmas (claim + mechanism):
  - **Cut↔merge correspondence** — because each XY cut adds exactly one interior split point,
    and each merge combines exactly two masses; the bijection between ≤n cuts and an n-node
    forest is the content, IF the cost functionals match under L4. Mechanism: L4's consecutive-
    pairing cost is realized by combining sorted-adjacent masses, which is exactly a bottom-up
    merge order.
  - **Uncrossing exchange** — two crossing combines can be replaced by nested/adjacent ones
    without raising Σ|diff| (same four-value check as L4's non-crossing proof, already
    certified — reuse it).
Open gaps: the ENTIRE translation step 1 (correspondence + objective match) — this is the
speculative far bet; if it holds it gives a clean structural upper bound, if not the approach
is retired next round. Steps 2–4 are routine once 1 holds.
Cases to cover: none beyond the translation; the exchange lemma is uniform.
Watch out for: the Huffman objective (weighted path length) is NOT literally S — do not
assume the classical theorem transfers; the whole value is in proving the Σ|diff| version
from scratch. If step 1 cannot be made rigorous in one build, report that cleanly (a crisp
negative — "cut↔merge cost does not match" — is a valid outcome that prunes this branch).

---

Retired (no nomination): **smoothing-extremal** — Lemma G refuted (round 2); sum-preserving
consecutive-pair smoothing cannot connect generic A to G_n and decreases S* in ~35% of moves;
surviving weaker claim re-imports XY's optimal response (the crux). Durable contribution
(maximizer-existence, S* continuous on the simplex) already recorded; do not resurrect.

build hint for the reviewer: the two advances (induction-peel, alternating-sum-potential)
carry the concrete, near-term-closable gaps (lower bound looks tractable via band+budget cap
on W); global-max-peel is a concrete far bet on unifying the lower bound; huffman-merge-exchange
is the speculative far bet on the upper bound (gate it on the translation step).
