## imo-2026-03 — lens: lower-bound multi-cut gap (≥2 XY cuts landing inside dominant piece a_1)

### Context re-verified
Confirmed by re-reading `dyadic-cascade-induction.md` §5/§5.1/§5.2/§5.2'/§5.2'' and
`lemmas/insertion-and-cascade-facts.md`: Branch A (0 cuts on a_1) and §5.1 (exactly 1 cut on
a_1, both bisect and every match-to-a_i) are genuinely fully closed for every `m` — the proofs
never depend on the open case, so they are safe to build on. The open case (§5.2/§5.2'') is
exactly: XY spends ≥2 of its cuts on fragments descended from `a_1`. Round 4's Fact 5
(chain-cancellation) is a real theorem, correctly rules out "residual stays below ceiling."
Fact 2 alone and Fact 4 (insertion bound) are confirmed too lossy on the `m=4,i=3` witness
(I re-derived the table in §5.2'' Part C by hand-checking the arithmetic; it is correct).

### New numerical work this round (exact `Fraction`, full D/M-language game-tree search)

I built an exact minimax search over the **D/M operation language** itself (not restricted to
physical-location casework): state = sorted multiset of Fractions, at each ply either bisect
any active value or match any active value down to any other active value, budget `b` total
ops, minimize final `e`. This is exactly `h(D_m,m)` from the (already partially certified)
`g=h` completeness lemma (`lemmas/dm-completeness-partial.md`), so it is legitimate evidence
about the *true physical* minimum modulo only the "all-cycles" edge case that lemma leaves open
(never observed to occur — my search gives further indirect evidence of that, since every
optimal-final-state trace I recovered decomposes into physically realizable non-cyclic D/M
sequences).

**Result: exhaustive confirmation `h(D_m,m) = e_m` exactly for every `m = 0,1,2,3,4,5`** (full
game tree, no sampling — `m=5` took ~5s, memo size 53422; `m=6` is computationally out of
reach with this brute force, state space too large — did not get a result there). This is
strictly stronger evidence than the previous rounds' random/grid searches (it is the true
minimum over **all** D/M sequences, not a sampled subset), and it now covers one more value
(`m=5`) than previously verified.

**Tracing the optimal (tying) strategies** (all length-`m` D/M sequences achieving exactly
`e_m`, enumerated for `m=3,4,5`):
- `m=3`: **5** distinct optimal final multisets/sequences.
- `m=4`: **12** distinct optimal final multisets/sequences.
- `m=5`: **46+** distinct optimal sequences (search truncated for the printout, not for
  correctness — `h` itself was computed exactly).

**Key finding — no small canonical form.** This is important negative information for the
"exchange argument reduces to a canonical finite set of cut points" opening: the optimal
(tying) strategies are **not** all instances of one clean recipe (e.g. "always match a_1 to
a_2 then cascade"). Concrete example at `m=4` (state `D_4=(16,8,4,2,1)/31`): one optimal
sequence is `M(a_2,a_3)=M(8,4)`, `M(a_1,a_4)=M(16,2)`, `M(14,4)`, `D(10)` — i.e. XY first
matches *a_2 down to a_3* (touching neither a_1 nor even the top of the multiset first!),
*then* matches a_1 against a_4, producing leftover `14/31`, which it *further splits twice
more* (M then D) — this is a genuine, non-toy instance of the open "leftover gets further
split" sub-case (§5.2'' Part C's exact target), and it still only *ties* `e_4=1/31`, never
beats it. Another optimal sequence for the same `m=4`: `M(4,2)`,`M(2,2)`? no — see raw data;
in general the first move is very often **not** on `a_1` at all (delay), and a_1 is always cut
*eventually* in every tying trace (consistent with Branch A's proof that never-touching-a_1
gives `e ≥ 2^{m-1}/(2^{m+1}-1)`, far above `e_m` for `m≥2` — my search independently confirms
Branch A never appears among the ties, as it must not).

**Conclusion for the "reduce to canonical form" opening (Section below, opening 1):** a clean
uniqueness-based exchange argument (à la "WLOG all cuts inside a_1 land at exactly these
dyadic points") looks unlikely to work directly — there is a whole *zoo* of inequivalent tying
strategies, not a small finite set. What IS uniform across all of them is that they all
achieve the *ceiling* exactly (Fact 5's content) via chains of Lemma-P/Fact-3 block
cancellations — so the right invariant to hunt for is not "which point is optimal" but "why no
sequence, however constructed, can undercut the ceiling," i.e. a genuine impossibility/
monovariant argument over the whole game tree, not a reduction to finitely many candidates.

### Distinct openings surfaced

1. **Canonical-form exchange argument** — tested numerically this round and found to be a
   weaker opening than hoped: no small canonical set of optimal cut points exists (46+ distinct
   tying sequences already at `m=5`). Not abandoned entirely (there may still be a coarser
   invariant — e.g. "every tying sequence eventually cuts a_1, and every prefix before that is
   itself an optimal sub-strategy on `R`" — but a literal finite-canonical-point reduction looks
   unlikely to close the gap by itself.

2. **Self-similar induction on `i` via the "dominant-tail class" 𝒟_j** (already proposed in
   §5.2' Step 3/Step 4, NOT re-derived here, just re-verified the diagnosis) — the needed
   inequality `ℓ = a_1-a_i ≥ 2·max(R\{a_i})` fails whenever `i≥3` (since `max(R\{a_i})=a_2=a_1/2`
   forces `a_i≤0`), so the naive class 𝒟_j does not contain the leftover after a match. Two
   unexplored refinements worth flagging for the outliner (not proved, not attempted by me):
   (a) weaken the dominance ratio from `≥2` to something matching what `ℓ` actually satisfies
   (`ℓ ≥ a_2` always, ratio exactly 1, not 2) and recompute what guarantee a ratio-1 "top-heavy"
   class gives — my search data shows this is worth checking against the concrete tying traces
   above (e.g. the `m=4` trace's leftover chain `14/31 → 10/31` after `M(14,4)`; is
   `10/31 ≥ max(rest)` at each step? `rest` there is `{4,4,4,2}/31`, so `10/31≥4/31` — ratio
   >2 actually, so a *weaker* general class might still recover enough); (b) a genuine
   minimal-counterexample argument restricted to the "further split of ℓ" sub-question, as
   already suggested — still untried by any builder.

3. **Direct strong induction over ARBITRARY states in D/M language, not location-based** —
   using the (round-4-certified, conditional) `lemmas/dm-completeness-partial.md` (`g=h` modulo
   the never-observed "all-cycles" case). This is a genuinely different top-level framing from
   both `dyadic-cascade-induction`'s physical-cut casework (which deliberately *dropped* D/M
   language in round 4 to avoid an overclaim) and from §5.2's location-based Branch A/B split:
   induct on total remaining budget `b` over the *current active multiset* `M` directly (not
   fixed to `D_j` shape), splitting only on whether the **first** operation touches the current
   maximum or not — Fact 2/3 handle "doesn't touch the max" for free (peel and recurse on
   `rest`), and "touches the max" is where the real content is. This is essentially the same
   underlying difficulty as opening 2 (finding the right class of states closed under the
   recursion) but is worth flagging explicitly as *available now* (it wasn't legitimately
   available before `dm-completeness-partial.md` was certified) and as a genuinely different
   framing from the physical-location split that has been stuck for 2 rounds (§5.2 → §5.2' →
   §5.2''), per the "challenge a shared-gap plateau" instruction. **Caveat, found by checking
   `concavity-minimax-duality`**: the single most natural scalar candidate for this
   (`Φ(M,r)=S(M)/(2^{r+1}-1)`) was already tried and refuted (fails P2 under M-moves, two exact
   counterexamples) — so this framing needs a genuinely richer invariant than one scalar
   potential per `(M,r)`, not just "try harder with the same shape."

4. **Two-sided / dual pairing bound (NEW, from crux `aimo-0388`, not previously tried in this
   population).** See "Analogous past problems" below. The current lower-bound machinery
   (Facts 1–5) is entirely a **top-down** peel: `e(M) = x_1 - e(rest)`, applied repeatedly from
   the current maximum downward. The `aimo-0388` crux move ("split a sorted sequence into two
   stacks by pairing consecutive elements so each pair's contribution to the difference is a
   non-positive gap, leaving only isolated boundary terms") is structurally a **different**
   pairing of the *same* sorted sequence than the fixed odd/even-rank one — and the proof there
   gets its bound by using **two different offset pairings** and combining. Applied here: `e(M)`
   itself is fixed by Lemma G (it must be the odd/even-rank alternating sum — this is forced,
   not a free choice, unlike the coins problem where the stack-split IS the free choice). So
   this crux does not transfer literally. But the *proof technique* — bound a target quantity
   using two different "shifted" alternating groupings of the same sequence and combine — may
   still be adaptable: e.g., bound `e(F)` both by peeling from the top (Fact 2/3, already done)
   **and** by a second, independent grouping that isolates the effect of "how many elements the
   i cuts inside a_1 contribute below rank 2" — untested, flagged as worth a careful look, not
   verified to work. This is the most genuinely novel mechanism I found this round; it has not
   been tried by any approach in the population.

### Cheap-kill candidates
- **Budget-usage check (done numerically):** every optimal (tying) D/M sequence found at
  `m=3,4,5` uses the **full** budget `m` — no strategy with `<m` operations ties or beats
  `e_m` (consistent with Fact 5 needing the "natural" `K-1` budget to reach the ceiling exactly,
  and with intuition that "wasting" cuts can only make `e` worse for the minimizer). This rules
  out any argument hoping to bound `i≥2` strategies by "they must use fewer effective cuts
  elsewhere" — they don't; the budget is always fully spent in the extremal cases.
- **Parity/dominance persistence check:** in every traced optimal sequence, `a_1` (or its
  current descendant) remains the *unique* rank-1 element until it is finally touched — no
  optimal sequence ever creates a tie at rank 1 before cutting the top piece. This is consistent
  with (does not contradict) Branch A's already-proven strict inequality.
- No new parity/pigeonhole/injection cheap-kill found for the general-`m` Step 4 gap itself;
  the obstruction is genuinely about magnitudes (budget-tradeoff), not combinatorial structure
  admitting an easy size argument.

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics section) — the existing Facts 1–5 are exactly
  this; the open gap needs either a richer invariant (a vector/pair, not a scalar, given
  `Φ`'s refutation) or a genuinely different proof method below.
- **Extremal principle / pigeonhole** — already exploited (dominance of `a_1`); no new
  application found this round.
- **Induction loading / generalize the hypothesis** (Pólya heuristics, "Problem-Solving
  Heuristics") — this is exactly what §5.2' Step 3 (𝒟_j class) already attempts; still the
  most concretely promising skeleton, just stuck at Step 4 as re-confirmed above.
- No SOS/convexity, generating-function, or algebraic-identity KB entry looks like a natural
  fit for this specific combinatorial-game gap.

### Analogous past problems (cruxes)
- **`aimo-0388`** (combinatorics, subtopics `extremal-principle` and `telescoping-and-summation`)
  — "100 coins, total 50, split into two 50-coin stacks minimizing `|difference|`." Genuinely
  analogous in *flavor*: an alternating-sum/order-statistic bound on a partition of a sorted
  sequence into two classes, using **two different pairings** of the same sorted list to get a
  two-sided bound (crux move: "split a sorted sequence into two stacks by pairing consecutive
  elements so each pair's contribution to the difference is a non-positive gap, leaving only
  isolated boundary terms"). This is the source of Opening 4 above. Not a literal transplant
  (our `L-X` split is *forced* by Lemma G, not free), but the *dual-pairing* proof mechanism is
  worth adapting.
- **`aimo-0019`** (combinatorics, `games-and-strategy` / `invariants-and-monovariants`) —
  "paintful game," dyadic-length interval covering with an ink budget. Superficially close
  (dyadic lengths, interval game, amortized-charge monovariant), but on closer reading the
  crux move is a *charging/amortized-induction* argument bounding cumulative resource by a
  linear function of progress — mechanically different from our alternating-sum structure and
  our two-player minimax-of-a-fixed-final-multiset setup (their game has no "final scoring by
  sorted order" structure at all). Judged **not** a strong match beyond the surface "dyadic
  lengths" coincidence — flagging it as considered-and-rejected so a future round doesn't
  re-chase it.
- **`aimo-0340`** (combinatorics, `processes-and-algorithms`/`invariants-and-monovariants`) —
  pearl-string cutting-in-half process. Also superficially close (repeated halving process,
  tracks longest/shortest string by induction), but it's a *deterministic* process (not an
  adversarial minimax), and the induction there tracks simple `⌈·/2⌉,⌊·/2⌋` bounds, not an
  alternating-sum payoff. Not a strong match; noted and set aside.
- No crux found that solves a genuinely equivalent "adversarial minimax over an alternating-sum
  payoff of a cut multiset" problem — this appears to be a fairly distinctive combination not
  well-represented in the pre-2026 corpus (checked `games-and-strategy` broadly across
  combinatorics and number_theory domains; the interval-based hits were `aimo-0019`/`aimo-0060`,
  both charging/monovariant games without the alternating-claiming payoff structure).

### Prior progress
Branch A (every `m`) and §5.1 exactly-one-cut-on-`a_1` (every `m`, both bisect and every match)
are fully closed and safe to build on (re-verified the algebra by hand for Case B1/B2's exact
computations — correct as stated). Facts 1–5 (dominant extraction, block extraction,
insertion bound, chain-cancellation/ceiling-achievability) are all correct, general, reusable —
re-derived Fact 5's induction argument independently and it holds. `m=4,i=3` concrete instance
(`3/31` vs target `1/31`) re-checked and correct. New this round: exact confirmation
`h(D_m,m)=e_m` for `m=0..5` via full D/M game-tree search (previously only verified through
grid/random search at `m≤4`; `m=5` is new, exact, and exhaustive, not sampled).

### Dead ends (do not retry)
- Fact 2 alone / Fact 4 insertion bound to close Step 4 generally — confirmed too lossy
  (concrete witnesses, `-5/31` vs true `+3/31` at `m=4,i=3`; re-verified the arithmetic).
- "Merging two smallest parts of a partition never increases `e`" — confirmed false by prior
  rounds' random search; not re-tested this round but the diagnosis (it's the wrong shape of
  claim, since ties in the tree data above show non-monotone effects of finer splitting) is
  consistent with it being false.
- A single scalar potential `Φ(M,r)` depending only on `(sum, budget)` — refuted by
  `concavity-minimax-duality`'s two exact counterexamples; any new candidate must depend on
  more of `M`'s structure than just its sum, or be a pair/vector invariant, not a scalar.
- Naive canonical-cut-point reduction (Opening 1) — new finding this round: the tying-strategy
  set is large and structurally diverse (12 at `m=4`, 46+ at `m=5`), so a literal "WLOG only
  finitely many candidate points" argument looks unlikely to be the right shape without a much
  coarser invariant than "list all optima."

### Small-case / intuition notes (all labeled conjecture except the exact `m≤5` computation)
- **Proved-by-exhaustive-search (not a hand proof, but exact, not sampled):** `h(D_m,m)=e_m`
  for `m=0,1,2,3,4,5`. This is strong confidence-building evidence the target `e_m` is correct
  and tight at every level checked so far; no counterexample at any `m≤5`.
- **Conjecture, pattern observed:** every optimal (tying) strategy, however it distributes its
  cuts, decomposes via a chain of Lemma-P/Fact-3 duplicate-block cancellations into something
  that telescopes exactly to `e_m` — i.e. the "generic" behavior of a cut is to cancel against
  something already present, and the residual few uncancelled terms are exactly what force the
  value up to (never below) `e_m`. This suggests the right proof mechanism is a **counting
  argument on cancellations**: every one of XY's `m` cuts either (i) creates a duplicate that
  cancels (net effect on `e`: zero, "wasted" from XY's perspective) or (ii) does not, and
  contributes some signed amount; bounding the number of "type (ii)" cuts and their signed sum
  might be the real joint budget-tradeoff invariant — this is speculative, not verified, but is
  a concrete new angle: **track cancelling vs. non-cancelling cuts as the two-part budget,
  instead of "cuts inside a_1 vs. cuts on R."** Worth the outliner's consideration as a fifth
  opening, orthogonal to location-based (physical) and value-class-based (𝒟_j) framings.
