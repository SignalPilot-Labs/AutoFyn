## imo-2026-03

Answer (fixed, certified consistent n=1,2,3): **c(n) = 2^n/D_n, D_n := 2^{n+1}−1.**
Every slug below is a WHOLE attempt at both bounds of this claim; LB machinery
(L0–L11) is shared/imported, the slugs differ in how they close the two open walls.

Field summary: two live approaches ADVANCE with sharpened, genuinely-different LB
mechanisms (charging-dichotomy vs. scale-bucket Hall); one NEW LB framing
(interlacing-bijection, discrete/combinatorial, far from both); one NEW UB probe
(randomized-xy-cut) opened GATED with an honest a-priori obstruction and a mandated
≤30s feasibility gate, whose fallback is the branch-inequality two-parameter casework.

---

### induction-peel: advance
Target: c(n) = 2^n/D_n for all n (both bounds), via peeling the top dyadic scale.
Technique: strong induction on n + the certified truncation identity S(B)=e+S(B_low);
LB residual = (PM) ∫[D odd] ≥ ∫D; UB = value-function recursion U_k(A) ≤ sum/D_k.

Skeleton (only the two open gaps change; everything else certified):
  1. LB residual (PM), {D≥2} interior — close via a **two-source charging dichotomy on k_C**
     (lower-bound explorer opening 1). Split on the number of cuts C spends inside P_{n-1}:
       (a) k_C = 0 (C keeps an uncut top block 2^{n-1}): every {D≥2} deficit pocket sits below
           H, and the surviving uncut H-part of C forces a persistent D=−1 "top band" of length
           Θ(H) right under the ceiling — surplus ≥ deficit by a direct interval-length compare.
       (b) k_C ≥ 1 (C is cut): D(0+) = (c+1)−(n+k_C) ≤ 1−2k_C < 0 (certified §3.3), so C stacks
           extra small parts near 0, a strongly-negative "bottom band" whose surplus ≥ deficit.
     The budget c+k_C ≤ n caps how much of BOTH bands can be simultaneously starved — this is the
     load-bearing use of the single-block part budget |Q_low|+|C| ≤ 2n+1.
  2. Give the charging map its rigorous spine via **summation-by-parts on the sorted merge**
     (lower-bound explorer opening 2): in the generic distinct-breakpoints case the parity of D
     strictly alternates breakpoint-to-breakpoint, so ∫[D odd] is a *positional* (interleaving)
     quantity and ∫D is the *path-dependent* signed-area of a ±1 walk with (c+1) down-steps and
     (n+k_C) up-steps; Abel summation against the fixed alternating indicator gives (PM).
  3. Tie / non-generic case (two shards equal ⟹ alternation skips a parity step): dispatch by
     **L9-style self-pairing cancellation** — equal adjacent parts cancel, reducing part count;
     recurse. Confirm this covers ALL tie configs (cheap-kill: check before the generic case).
  4. UB branch inequalities (Open gap 2): prove U_{k−1}(c(A)) ≤ sum/D_k for the minimizing
     c ∈ {MATCH,BISECT} via **two-parameter casework** (upper-bound explorer conjecture): primary
     r = a_1/ρ (BISECT when r≥1, MATCH when r<1) + a secondary statistic separating "several
     comparable large parts" (A={6,4,2}) from "one dominant part with small clutter" (A={2,2,1});
     equalize branch bounds to pin the geometric ratio 2 and value 2^k/D_k.

Key lemmas (claim + mechanism):
  - Two-source dichotomy — because with k_C=0 the uncut 2^{n-1} of C creates a full D=−1 band of
    length up to H right under the ceiling, and with k_C≥1 the origin D(0+)≤1−2k_C forces a deep
    negative band near 0; c+k_C≤n stops both from being starved at once.
  - Positional-vs-path Abel step — because D's parity alternates with EVERY generic breakpoint
    (L2/L3 alternating-sum on B_low=Q_low⊔C), so [D odd] is fixed by the interleaving order while
    ∫D depends on the ± sequence; summation-by-parts compares them.
  - Tie reduction — because two equal shards cancel at adjacent rank (L9), removing a matched pair
    without changing S, so the generic (distinct) case suffices after recursion.

Open gaps: (1) the explicit charging map / Abel inequality closing (PM) on {D≥2}; (2) the two
branch inequalities + the two-parameter secondary statistic. UB is the harder wall.
Cases to cover: LB — k_C=0 vs k_C≥1; generic-breakpoints vs tie. UB — r≥1 vs r<1 × secondary.
Watch out for: (i) the charging map must consume the part budget, NOT a cut-count-on-C cap
(refuted round 4 — extremal spends 0 cuts on C); (ii) the tie case must cover ALL ties, not just
pure-BISECT; (iii) don't let the UB casework collapse to a one-parameter rule — F1 says that fails.

---

### alternating-sum-potential: advance
Target: c(n) = 2^n/D_n for all n (both bounds), via the layer-cake/β matching cap.
Technique: reforge LB as β(B) ≤ 2^n−1 (β = even-rank sum = ∫⌊N/2⌋); UB as an ADDITIVE
matched-weight construction β(B) ≥ (2^n−1)/D_n. Distinct LANGUAGE from induction-peel (β/matching,
not D/parity) — keep apart.

Skeleton:
  1. LB Gβ (β(B) ≤ 2^n−1 in the e<1 case) — close via a **scale-bucket Hall-deficit argument over
     every pairing**. Bucket parts by dyadic scale j (2^{j−1} < y ≤ 2^j). β = Σ even-ranked parts
     = a matched weight; bound it by a Hall-type deficit count: in any consecutive pairing, the
     matched (even-rank) mass at scale ≥ 2^j is capped by the ORIGIN-GROUP mass available at that
     scale, Σ_{i<n}2^i = 2^n−1 = total mass below the top group. Use O1–O4's two mandated levers
     simultaneously: (cut budget / part-count ≤ 2n+1) AND (origin-group sums = 2^j).
  2. Equivalent clean target (§5): odd-rank sum of B ≥ 2^n = the top group's mass. Prove the
     top group's mass "cannot all be paired down" — every unit of top-group mass that becomes
     even-ranked must be matched against DISTINCT lower-group mass, and there are only 2^n−1 units
     of lower-group mass; the part budget caps how finely the top block can be shredded to steal
     matches. This is the Hall deficit made concrete.
  3. UB G2 (arbitrary A) — **additive β-accumulation construction**: XY grows β toward
     (2^n−1)/D_n·sum by n MATCH/BISECT moves, each adding its cut value to the even-rank sum with
     a carry; a telescoping lower bound Φ_k ≥ target. NOTE this must still choose MATCH vs BISECT
     per profile (F1), so it is NOT a single-rule construction — it inherits the branch choice but
     in additive-β bookkeeping (distinct from induction-peel's multiplicative value-function).

Key lemmas (claim + mechanism):
  - Scale-bucket Hall cap — because the even-ranked (matched) mass at each scale is bounded by the
    lower-origin-group mass it can be matched against (a matched pair needs one lower partner per
    top shard), and Σ_{j<n}2^j = 2^n−1 is the total such partner mass; the part budget ≤2n+1 caps
    the shredding that would create extra partners (kills the O1 bisect-all counterexample).
  - β-split reproduces W (O3, certified) — because β(Q⊔C)=β(Q)+β(C)+W, so the argument must be
    GLOBAL over all buckets at once, not a single top-split; the bucket accounting is that global
    view.
  - Additive β accumulation — because each MATCH of value v pairs a new v against an existing v,
    adding v to the even-rank sum, and the carry (a_1−v) re-enters a strictly smaller subgame.

Open gaps: (1) Gβ — the scale-bucket Hall deficit inequality (the global β cap); (2) G2 — the
telescoping lower bound on accumulated β for arbitrary A (still needs the profile-dependent branch
choice, F1).
Cases to cover: LB — bucket occupancy patterns; the O2 counterexample B={4,2,2,2,2,2,1} must
satisfy the bound (β=6≤7) so the bucket accounting must be integral/global, not heightwise.
Watch out for: O1 (bisect-all gives β=2^n−1/2 > target with UNLIMITED cuts) means the bound is
FALSE without the part budget — the bucket argument MUST consume it. O2/O3/O4 forbid pointwise,
recursive-split, and majorization-only routes: the deficit count must be global + origin-group-aware.

---

### interlacing-bijection: new
Target: c(n) = 2^n/D_n for all n (both bounds); LB via a discrete rank-crossing injection.
Technique: recast the LB {D≥2} compensation as a **combinatorial injection on interlacing
rank-patterns** (new-framing explorer, opening 1) — genuinely different from both charging
(measure) and β-matching. UB imported (branch inequalities / deferred).

Why a new framing (dispatch's breadth mandate): the field's three live LB mechanisms
(profile-IH/W-overlap, β-Hall-deficit, charging-dichotomy) are all *analytic* (integrate a
real-valued function). New-framing's numerics show S(B)=1 is governed by a DISCRETE
interlacing/rank pattern, not exact values (the equality set at P_n is a positive-measure union of
interlacing cells, ~4.7% of splits at n=3). So the natural object for the {D≥2} gap is rank
crossings, not a measure — a framing no live approach uses.

Skeleton:
  1. Import (PM) reduction and R2/L9 (certified). Represent B_low = Q_low ⊔ C by the interleaving
     word: the sorted merge of Q_low's (c+1) shard-values and C's (n+k_C) part-values, marked by
     origin (Q or C). D(t) changes by −1 at each Q-breakpoint, +1 at each C-breakpoint.
  2. An "excess crossing" is a maximal interval where D≥2; a "deficit crossing" where D≤0. (PM)
     ⟺ Σ excess (D−[D odd])·len ≤ Σ deficit ([D odd]−D)·len.
  3. Build an **injection** from excess-interval mass to deficit-interval mass, using the
     origin-group-sum budget: each excess crossing (D≥2 means ≥2 more Q-shards than C-parts have
     passed) is created by Q-breakpoints that, because Q's shards sum to exactly 2^n − e and C's to
     2^n − 1, must be "paid back" by a matching under-crossing lower down (mass conservation:
     ∫D = 1−e ≤ 1). The part budget |Q_low|+|C| ≤ 2n+1 bounds how many crossings exist, forcing
     each excess to inject into a distinct deficit.
  4. UB: import induction-peel's branch inequalities (this slug's contribution is the LB framing).

Key lemmas (claim + mechanism):
  - Rank-pattern locality — because S = meas{N odd} (L3) is locally constant in the continuous
    shard values and jumps only when a shard crosses an existing part; so the gap depends only on
    the interleaving WORD, reducing (PM) to a finite combinatorial statement per word.
  - Excess→deficit injection — because ∫D = 1−e ≤ 1 (mass conservation) forces every D≥2 excursion
    up to be preceded/followed by a compensating D≤0 excursion, and the part budget bounds the
    excursion count so the pairing is injective.

Open gaps: the injection itself (step 3) — the make-or-break; UB deferred to branch inequalities.
Cases to cover: generic word (distinct breakpoints) vs ties (L9); the injection must handle D
reaching 3+ (excess of size D−[D odd]).
Watch out for: this is a REFRAME, not yet a proof — new-framing explorer found the target object
(rank patterns) but not the injection. If the injection resists, it still de-risks the field by
testing whether the discrete view is more tractable than the analytic charging. Keep it far from
induction-peel: no measure-charging language, pure word/crossing combinatorics.

---

### randomized-xy-cut: new (GATED — cheap feasibility probe MANDATORY before any write-up)
Target: c(n) = 2^n/D_n; UB via a whole-profile randomized XY cut law with E[S(B)] ≤ sum/D_k.
Technique: designated plateau-breaker for the UB — randomize WHICH part is cut (not just mix two
fixed top-part branches, which is the refuted averaging).

HONEST a-priori obstruction (outliner's verdict — read before building):
The UB bound is TIGHT at the dyadic profile (min over ≤n-cut refinements of S = sum/D_n exactly).
For ANY distribution over ≤n-cut strategies, E[S] ≥ min = sum/D_n, with equality ONLY if the law
is supported entirely on S-minimizers at P_n. So randomization buys ZERO slack at the binding
instance. Combined with F1 (P_n needs BISECT-top, {2,2,1} needs BISECT-small, {6,4,2} needs one
MATCH — no fixed rule is optimal at dyadic AND elsewhere), a randomized law is either
profile-DEPENDENT (= the branch inequalities, no new leverage) or profile-INDEPENDENT (fails F1 /
overshoots at dyadic). This is the SAME failure family as averaging (E ≥ min, min already tight).

Skeleton (probe-first):
  1. **GATE (≤30s, exact Fraction, MUST run and print before anything else).** Pick ONE concrete
     profile-only randomization law (e.g. cut the part chosen with prob ∝ its current contribution
     to S, bisect-vs-match by a fixed coin). Compute E[S(B)] exactly at A=P_2 (target 1/7), A=P_3
     (target 1/15), and the F1 witnesses {2,2,1}, {6,4,2}. PASS iff E[S] ≤ target on ALL four.
  2. If GATE PASSES (unexpected): design the telescoping E[S] ≤ sum/D_k recursion matching
     D_k = 2D_{k−1}+1; write up as a genuine new UB.
  3. If GATE FAILS (expected, per the obstruction above): record the definitive UB do-not-retry
     "no profile-only randomized cut law beats the tight dyadic instance" — this CLOSES the
     randomization family for good. The same builder then falls back to the **least-bad UB
     framing**: advance induction-peel's branch inequalities with the two-parameter (r, secondary
     spread) casework (see induction-peel step 4), which is the field's honest UB crux.

Key lemmas (claim + mechanism):
  - Zero-slack-at-extremal — because S(cascade of P_n) = 1/D_n is the exact min, so E[S] ≥ 1/D_n
    forces minimizer-support and no averaging gain (dual of the refuted averaging obstruction).

Open gaps: the entire UB; the GATE decides whether this framing lives or is banked as dead.
Cases to cover: the four probe profiles (n=2,3 + two F1 witnesses).
Watch out for: do NOT write a full approach before the GATE passes (budget rule: ≤30s, incremental
print). If it fails, the value delivered is the recorded do-not-retry + the fallback dispatch —
do not iterate on new laws (the obstruction is structural, not law-specific).

---

Build-set recommendation to the outline-reviewer: advance induction-peel and
alternating-sum-potential (both have concrete new LB mechanisms and are in distinct languages);
build interlacing-bijection (new, genuinely different LB framing — field breadth); and run the
randomized-xy-cut GATE probe (cheap, and either breaks the UB plateau or definitively banks the
randomization family and redirects to the branch-inequality casework). The UB remains the field's
hard wall; no describable-strategy shortcut survives the zero-slack + F1 obstruction, so the honest
UB progress this round is the two-parameter branch-inequality casework inside induction-peel.
