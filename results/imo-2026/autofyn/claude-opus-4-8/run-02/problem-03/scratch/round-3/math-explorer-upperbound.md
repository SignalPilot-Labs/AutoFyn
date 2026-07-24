## imo-2026-03 (lens: GAP-U MIDDLE REGIME)

### (a) Precise definition of the middle regime

Setup (all certified, imported from `alternating-sum-threshold-potential.md` /
`lemmas/cut-and-pair-reduction.md`): for a sorted multiset `P` (`a_1≥a_2≥…≥a_m`, sum `s`,
`m ≤ b+1`) and cut budget `b`, `g_b(P) := min` over Xiang Yu's `≤b` cuts of the final
alternating sum `f`. Target invariant (I): `g_b(P) ≤ s/D_b`, `D_b=2^{b+1}-1`. The one-step
recursion (★) `g_b(P) ≤ g_{b-1}(R)` (bisect-top: `R={a_2,…,a_m}`, `Σ(R)=s-a_1`; top-match:
`R={a_1-a_2,a_3,…}`, `Σ(R)=s-2a_2`) plus IH at `b-1` closes (I) **iff**
```
        max(a_1, 2a_2)  ≥  (2^b/D_b)·s.                      (H)
```
The **middle regime** is exactly the negation of (H) together with not-already-done:
```
   f(P) > s/D_b        AND       a_1 < (2^b/D_b)s   AND   2a_2 < (2^b/D_b)s.       (M)
```
Why (H)/geometric-step fails there: the single-shot inequality needs `Σ(R) ≤
(D_{b-1}/D_b)s`, i.e. the ONE cut must remove a `≥ (2^b/D_b)≈1/2`-fraction of the mass in
one shot; that requires `a_1` (or `2a_2`) to already be about half the total. When the top
pieces are near-balanced (comparable in size, no single piece near `s/2`), no *one* cut
achieves that fraction — but I confirmed numerically (below) the target is still met, just
not by one dominant cut.

### (b) Candidate amortised/phase arguments — what I tried and what I found

I ran full brute-force minimax search (recursive, fine grid, `b≤3`) on the exact
flagged example `[0.455,0.217,0.180,0.148]` (`b=3,m=4`, regime (M): `f≈0.270 > 1/15`,
`a_1≈0.455 < 8/15`). Results (numerics, i.e. **conjectural evidence, not proof**):

- **True `g_3` for this config is `≈0.032`, far below target `1/15≈0.0667`** — the
  invariant is comfortably true here, it's only the *lock-step single-geometric-step proof*
  that fails, not the claim.
- The **optimal 3-cut path found**: bisect-top (`a_1→a_1/2,a_1/2`, invisible pair) →
  bisect-top again on the **new effective top** (`a_2→a_2/2,a_2/2`, another invisible pair)
  → one more cut on the new top (`a_3`) that is close to (but not exactly) a top-match.
  I.e. the winning strategy is **iterated bisect-top on the successively-revealed
  "effective top"** (the largest piece not already cancelled by an invisible matched pair),
  continuing past where hypothesis (H) fails at the *outer* level, because (H) becomes
  true again one or two levels *deeper* once the dominant piece has been peeled away.
- On a second flagged config `[0.385,0.233,0.230,0.153]` (also regime (M) at `b=3`), true
  optimum is `≈0.002`; the winning 2-cut path is bisect-top then a near-top-match on the
  new top — again "keep peeling the effective top a couple more levels than the one-shot
  test requires."
- **I disproved a naive "just keep bisecting the (physical) max forever" strategy**: applied
  blindly for all 3 cuts on `[0.385,0.233,0.230,0.153]`, `f` goes `0.229→0.156→0.077→0.153`
  — it OVERSHOOTS on the 3rd cut (this reproduces the recorded dead end "peel top `n`
  times overshoots"). The fix is not "cut less" but "recompute the *effective* residual
  (after subtracting invisible matched pairs) and re-decide bisect-top vs top-match at
  *that* level," i.e. genuine strong recursion on the residual, not physical greedy on the
  raw list.
- **I also tried and DISPROVED (bug caught, then corrected) a "generalized top-match to any
  deeper piece `a_k`" move done as a single step** — a naive coding of it violated mass
  conservation (an easy trap: matching `a_1` to `a_k` for `k>2` while discarding the
  original `a_k` loses mass). The *conservative* single-step version (cut `a_1` into
  `(a_k, a_1-a_k)`, `k>2`) gives **no improvement** on the flagged near-balanced configs
  (`f` unchanged to 3 significant figures) — a single top-match-to-any-rank move is
  provably too weak alone in regime (M); it must be **combined across ≥2 cuts**.

**Candidate amortised argument (most promising direction, NOT yet proved):** strengthen the
induction to strong induction on `b` using the recursion (★) applied for a *variable* number
`k≥1` of consecutive steps before invoking IH, i.e. prove directly by strong induction (not
via the single fixed geometric-step lemma) that:
```
   g_b(P) ≤ g_{b-k}(R_k)   for the BEST k chosen adaptively,
```
where `R_k` is obtained by `k` iterated bisect-top/top-match moves on the successively
revealed "effective top," and show that **some** `k ≤ b` achieves the needed mass-removal
fraction `1 - D_{b-k}/D_b` — i.e. replace the ONE-STEP geometric test (H) with a
**telescoped/amortised** multi-step test: `Σ_{j=1}^k (removed mass at step j) ≥ (1 -
D_{b-k}/D_b)s` for some `k`. This is exactly a "phase" argument (a phase = however many
consecutive peels are needed until either (H) fires or the piece count/budget forces a base
case), and is the shape the outliner should adopt. The open technical piece: prove that such
a `k` **always exists** — i.e., that repeated bisect-top peeling of the effective top cannot
get "stuck" removing too little mass for arbitrarily many steps in the near-balanced regime.
This is plausible (peeling shrinks `m` by 1 each step, and with only `≤ b+1` pieces total,
after `m-1` peels only the base case remains, so the phase is automatically bounded by `m`,
not `b`), but the quantitative mass-removal-per-phase bound in the WORST near-balanced case
is not yet derived — **this is the honest remaining gap**, now narrowed from "an amortised
argument is needed" (round 2) to "prove a multi-step (telescoped) version of the geometric
test (H) always fires within `≤ m-1 ≤ b` peeling steps."

**A second, alternative angle worth flagging** (not verified, but structurally clean):
attack `f(P)` directly via the **matching form** (Lemma 2) using the whole sorted list at
once rather than a greedy peel: view Xiang Yu's task as choosing `≤ b` cuts to make the
adjacent-pair min-weight-matching cost small. Since `f = Σ_i (a_{2i-1}-a_{2i})` (the sum
over consecutive-pair gaps), a **global charging argument** — "close the single largest
gap-term with one cut, recompute, repeat" — was the FIRST thing I tried (a literal greedy on
gap size); it does NOT work directly as a valid single-piece cut (see the mass-conservation
bug above) and, once fixed to be a valid cut, does not clearly dominate the effective-top
peeling approach; I do not recommend pursuing it further without a cleaner formalization,
but note it for completeness since it's the most "textbook amortised" framing (each cut
kills the largest term, `f` should telescope down).

### (c) Dead ends (verified, do NOT retry)

- **Single one-shot geometric-step test (H) applied only once, then falling back on the
  IH's crude worst-case bound `Σ(R)/D_{b-1}`** — this fails whenever (M) holds, *not*
  because the invariant is false (numerically confirmed true, `g_3≈0.032≪1/15` and
  `g_3≈0.002≪1/15` on the two flagged configs) but because IH's bound is not tight enough
  in one step; a multi-step (telescoped) version is required. Already recorded in round 2;
  re-confirmed here with concrete numbers.
- **Naive fixed "bisect the physical current max, `b` times, no re-evaluation"** —
  overshoots (round-1/round-2 dead end), re-confirmed numerically here: on
  `[0.385,0.233,0.230,0.153]`, 3 blind bisections give `f: 0.229→0.156→0.077→0.153`
  (the *3rd* cut alone reverses 2 cuts' progress). The correct move requires recomputing
  which piece is the "effective top" (top rank not already in an invisible matched pair)
  and choosing bisect-top vs. top-match there — blind physical-max bisection ignores this.
- **Single-step "top-match to a deeper piece `a_k`, `k>2`"** — verified numerically to give
  no improvement alone on the flagged near-balanced configs (`f` essentially unchanged);
  ruled out as a *one-shot* fix. (A naive coding of "match to `a_k`" that also silently
  deletes the original `a_k` from the pool violates mass conservation — a bug to avoid if
  re-attempting this move; the mass-conserving version is weak alone.)
- **A literal "always close the single largest consecutive-pair gap term" as a raw cut** —
  my first implementation of this had a mass-conservation bug (deleted 2 pieces, added 2,
  net losing mass); once caught, this needs careful re-derivation before trusting any
  numeric result from it. Flag for whoever revisits it: validate `Σ(new pieces) =
  Σ(old pieces)` before trusting any simulation output.

### (d) Most promising technique + crux moves

**Most promising:** the **telescoped/phase-based strengthening of the cut-and-pair
recursion (★)** — prove that in regime (M), iterating bisect-top/top-match on the
successively-revealed effective top for `k` steps (some `k` depending on the configuration,
bounded by `m-1 ≤ b`) always achieves the needed cumulative mass-removal fraction
`1-D_{b-k}/D_b`, closing via IH at `b-k`. This directly extends the already-certified
`cut-and-pair-reduction` lemma (Lemma 4/H) rather than replacing it — a genuine "amortize
over a phase" continuation of the existing proof, not a new framework. The formal target to
prove: *for any `P` with `m≤b+1` pieces failing (H) at level `b`, there is `k∈{1,…,m-1}`
such that iterating the effective-top peel `k` times removes mass `≥ (1-D_{b-k}/D_b)s`.*

**Crux moves from the corpus (combinatorics, `games-and-strategy` /
`processes-and-algorithms` subtopics; queried `past_crux_moves_database.json` with the
correct `technique`/`how_used` fields per `crux_moves_documentation.md`):**

- **`aimo-0236`** (token/valuation game) — crux: *"maintain a two-phase invariant (stronger
  bound before the opponent moves, weaker bound after) that is self-restoring"* and a
  companion crux *"find a regime preserved by both players' moves in which one player's
  move fixes every relevant valuation while the other's forced move strictly decreases a
  nonnegative-integer potential each round."* This is the closest structural analogue found:
  the *shape* of a phase-based invariant (holds at the start of a phase, degrades in a
  controlled way, self-restores or terminates within a bounded number of steps) is exactly
  what GAP-U's middle regime needs — not the mechanics (that problem is 2-adic valuations on
  a token game, unrelated to stick-cutting), but the proof *architecture*.
- **`aimo-0146`** — crux: *"when a relaxed optimum exceeds the target by a fixed gap and is
  attained only at one profile, close the gap by re-imposing on that exact profile a
  structural constraint the relaxation discarded."* Weaker analogy, but relevant: our
  situation is similarly "the crude IH bound (the 'relaxation') overshoots the true minimum
  in regime (M); the fix is to re-impose the extra structure (piece-count/surplus-budget
  information) that the crude bound discarded." Worth reading if the phase argument stalls.
- No other combinatorics `games-and-strategy`/`processes-and-algorithms` crux with an
  amortised/charging structure was a closer structural match after scanning ~250 candidates
  filtered on those two subtopics with amortisation-related keywords; `aimo-0558`/`aimo-0620`
  (greedy + charging) are generic "greedy + charge deficit to a distinct witness" arguments,
  a weaker but potentially useful pattern if the telescoped-phase route needs a discharging
  step (charge each "wasted" cut to a specific piece it eventually cancels).

### Knowledge-base entries
`knowledge_base.md`'s general **Induction/strong induction** and **Invariants and
monovariants** sections remain the right generic pointers (as in round 2); no new
KB entry specific to phase/amortised potential arguments exists — the phase argument must
be built from scratch, using the already-certified `cut-and-pair-reduction.md` as its base
step.

### Prior progress (imported, not re-derived)
See `results/imo-2026-03/current.md` and `alternating-sum-threshold-potential.md`: reduction
`c(n)=(1+M*)/2 ⇔ M*=1/D_n` (certified), `n=1` fully solved, GAP-L Case 1 (`f≥2a_1-Σ`,
certified as `lemmas/alt-sum-two-max-minus-total.md`), the cut-and-pair recursion (★) and
dominant-regime dichotomy (both certified as `lemmas/cut-and-pair-reduction.md`), Invariant
(I) verified true and tight. GAP-U reduced to exactly the middle regime (M) above.

### Small-case / intuition notes (all labeled conjecture — numeric evidence only)
- Regime (M) genuinely exists for `b≥3` (confirmed by the two flagged configs); the
  invariant (I) is comfortably true there (`g_3` an order of magnitude below target in both
  cases checked), so there is real slack — the difficulty is purely in the *proof*
  architecture (crude one-step IH vs. needed multi-step telescoping), not in the truth of
  the claim.
- Conjecture: the number of peeling steps needed to "escape" regime (M) and trigger (H) is
  small relative to `m` (both examples needed only 2 extra steps beyond the failing first
  check), suggesting the telescoped bound, if provable, likely closes with a modest
  worst-case phase length (not requiring the full budget `b`).
