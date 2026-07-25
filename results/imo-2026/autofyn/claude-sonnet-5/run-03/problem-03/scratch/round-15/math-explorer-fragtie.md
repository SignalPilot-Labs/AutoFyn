## imo-2026-03 (lens: fragment-vs-fragment tying / descending-chain gap)

- **Distinct openings surfaced:**
  1. **Closed-form 1-D optimization via the Singleton-Interleaving Lemma
     (new, verified this round).** The descending fragment chain's fragment
     multiset decomposes exactly as `B ⊔ L` in the sense of the certified
     **Singleton-Interleaving Lemma** (`lemmas/singleton-interleaving-and-
     k-anchor-merge.md`, Theorem 9): the `s-1` "tied" values each occur with
     multiplicity 2 (even block), and only `L = {x, S_{s-1}(x)} ∪
     untouched` (the free parameter `x=L_0`, the untied trailing fragment
     `S_{s-1}`, and the untouched pieces) is a genuine singleton set. Since
     the recursion `L_{a+1}=S_a`, `S_a=p_{i_a}-L_a` makes `S_{s-1}` an
     **explicit affine function of `x`** (coefficient `±1`), Theorem 9 gives
     `OddSum(M(x)) = (1/2)(TotalSplitMass - x - S_{s-1}(x)) + OddSum(L(x))`,
     a genuinely closed-form, piecewise-affine function of the single free
     parameter `x`, for any FIXED subset+linear order. I implemented and
     verified this in exact `Fraction` arithmetic (200 random trials,
     zero mismatch against direct construct-and-sort) — see "Small-case /
     intuition notes" below for the numeric confirmation. This replaces
     round 14's "fine grid over x" (which is only an approximation) with an
     **exact** minimization over `O(s + #untouched)` breakpoints (crossings
     of `x` or `S_{s-1}(x)` with each other or with any untouched piece) —
     the true 1-D minimum is attained at one of these finitely many points,
     not merely approximated by a grid. This is a genuine tractability
     improvement on the free-parameter part of the search (not the
     subset/order part, which remains combinatorial).
  2. **Existence-only compactness route (the framing the parent approach
     is supposed to prefer, per the dispatch).** The Global Vertex Lemma
     (already certified in `global-lp-vertex-sufficiency.md` Section 1)
     already guarantees the TRUE optimal adversary shape `σ*(p)` lies in a
     finite, `p`-independent shape set `Σ(n,k)` — so "does `σ*(p)` always
     have descending-chain shape" is really asking whether the descending-
     chain shapes form a subset of `Σ(n,k)` that is always the argmin. This
     doesn't need a closed-form selection *rule* at all if one instead
     proves an **existence statement** — e.g. "for every cell of the
     `L`-arrangement, *some* member of `Σ(n,k)` attains `V(p)` and is
     provably ≤ c(n) via a case-independent bound," bypassing enumeration
     of which specific descending-chain member wins. This is the
     $\Sigma$-shape classification route already flagged as the sole
     remaining obstruction — my numeric work below suggests it is NOT
     solvable by fixating on the descending-chain family alone (see finding
     3), so this route likely needs a genuinely different shape family or a
     non-constructive argument, not a sharper search within this one family.
  3. **New negative finding (this round, exact arithmetic): the descending
     fragment chain family fails EVEN under exact (not grid-approximated)
     optimization, already at n=3, and badly at n=4.** See item 3 below —
     this closes off "fixate on descending-chain, just search harder" as a
     viable direction.

- **Candidate technique(s):** the Singleton-Interleaving Lemma /
  even-block decomposition (Theorem 9 in
  `lemmas/singleton-interleaving-and-k-anchor-merge.md`) is the right tool
  for ANY construction built from chains of ties (cyclic or linear) — it
  converts `OddSum` of a chain-tie construction into a closed-form affine
  expression in the free parameters plus a small residual `OddSum(L)` over
  only the untied/singleton values. This should also be re-applied to the
  (already-refuted) cyclic chain family as a sanity check/simplification
  vehicle for future rounds, and to any NEW chain-like family a future
  round proposes. The existence-only compactness/LP-vertex framing
  (already the parent approach's own machinery, Sections 1, 4) remains the
  more promising top-level target per the dispatch — the fragment-tying
  searches are best used as *evidence* about which shapes in `Σ(n,k)` are
  ever optimal, not as a standalone proof mechanism.

- **Cheap-kill candidates:** the Singleton-Interleaving-based exact
  breakpoint minimization IS the cheap kill for the "closed-form x" part
  of question 1 — it is O(s+#untouched) exact evaluations instead of a
  grid, and I used it below as a strengthened, definitive cheap-kill on
  the whole descending-chain family (exhaustive over subset+order, exact
  optimum over x) rather than the round-14 grid-based version.

- **Knowledge-base entries to use:** none beyond what the parent approach
  already cites (Extreme Value Theorem / vertex-of-polytope argument,
  already used in Section 4's Finite-Cell theorem). No new KB entry
  matches "descending fragment chain" specifically.

- **Analogous past problems (cruxes):** none newly found this round beyond
  the two already cited in the approach file itself (`aimo-0146`,
  `aimo-0287`, both about exchange-smoothing directions, for the
  Region-Boundary-Monotonicity bypass, not this gap). I did not find a
  crux specifically about "closed-form selection over a discrete tie
  structure" — the corpus's combinatorics subtopics do not appear to have
  an entry matching a chained-tie optimization of this shape; recommend
  not forcing a match here.

- **Prior progress:** round 14's mixed/inconclusive finding (natural
  orderings fail broadly 5/8–8/8; exhaustive subset/order/grid-x search
  matches or beats V(p) at all 3 catalogued n=3 hard points, but is
  acknowledged as combinatorially expensive and not closed-form). The
  Chain-Correction Floor Theorem (`lemmas/chain-correction-floor-theorem.md`)
  is a DIFFERENT construction (a floor-attaining $e_0$-specific hybrid, not
  a general-`p` descending chain) — its closed-form technique (identify
  even-valued pairs via Even-Block-Neutrality, an instance of the same
  underlying mechanism as Theorem 9) is the same idea I re-applied here,
  confirming it generalizes.

- **Dead ends (do not retry):** cyclic pairwise-tie chain (refuted broadly,
  round 14); bounded-size construction families / fixed-$s_0$ tie-to-
  untouched-piece (Mass-Constraint Theorem, round 11); region-geometry and
  response-side exchange mechanisms (rounds 12–13); "natural orderings"
  (index-ascending/descending full-chain) for the descending-chain family
  (round 14, still fails broadly, reconfirmed implicitly by my finding 3
  below — natural full-`k`-piece chains are a strict subfamily of what I
  tested and my exhaustive search already subsumes and re-refutes them).
  **New this round — also now a dead end:** exhaustive/exact descending-
  chain search as a general-`n` proof mechanism (see finding 3) — do not
  invest further proof effort trying to extend the n=3 exhaustive-search
  success to a general theorem; the family itself breaks down by n=4.

- **Small-case / intuition notes (all exact `Fraction` arithmetic, all
  labeled conjecture/numeric evidence, not proof):**
  1. **Verified the closed-form (Singleton-Interleaving) reproduction of
     the descending-chain OddSum is correct**: 200 random trials
     (n=3..6-ish random simplices), exact match between (a) literally
     constructing the fragment multiset and sorting, and (b) the closed
     form `(1/2)(TotalSplitMass-x-S_{s-1}(x)) + OddSum({x,S_{s-1}(x)}∪
     untouched)`. Zero mismatches.
  2. **Reproduced round 14's own reported exhaustive-search numbers
     exactly** at all 3 catalogued n=3 hard points using the exact
     breakpoint method instead of a grid: point 1 → 0.5114 (exact match to
     V(p)), point 2 → 0.5150 (exact match to V(p)), point 3 → 0.5258
     (matches round 14's own table value, still short of the true
     V(p)≈0.5166). This cross-validates both my implementation and round
     14's grid-search finding — the family's true (not grid-approximated)
     best member is exactly what round 14 already found; there was no
     hidden extra slack in the grid discretization.
  3. **New finding — genuine failure of the exact/exhaustive family,
     n=3 and n=4 (this is new information beyond round 14, which only
     tested the 3 already-catalogued n=3 points, not fresh random ones).**
     Testing the FULL exhaustive family (every subset size `s=2..n`, every
     linear order/permutation, exact breakpoint-optimal `x`) against fresh
     random balanced-region points (exact rational, rejection-sampled to
     satisfy `p_1<1/2` and every gap `>γ(n)`): **n=3, 2/20 fail** (exceed
     `c(3)=8/15`); **n=4, 4/12 fail** (exceed `c(4)`). An explicit n=3
     failing example: `p≈(0.4508,0.2550,0.1852,0.1090)`, best
     descending-chain value `76261/136224≈0.5598 > c(3)≈0.5333` (subset
     `(0,1)`, exact optimum, not grid-approximate). This is a strictly
     stronger negative result than round 14's "natural orderings fail" —
     it shows the *entire existential family*, optimized exactly, is not
     a universal proof mechanism, even restricted to n=3, contradicting
     the impression (from only 3 cherry-picked points) that the family
     might "survive" at n=3. **Conjecture, well-supported**: `σ*(p)` does
     **not** always have descending-chain shape — question 2 from round
     14 is answered "no" as a general matter (though the exact-match
     coincidence at 2 of 3 catalogued points remains real and unexplained
     — plausibly those two points happen to have a genuinely
     descending-chain-shaped optimal response, while the third and the
     newly-found failures do not).
  4. Practical implication for next round: do not chase a closed-form
     selection rule for this specific family (round 14's open question 1)
     — the family itself is now shown insufficient in general, so a
     selection rule, even if found, would not close the Existence Theorem.
     The productive next target is either (a) a genuinely different
     fragment-vs-fragment tying topology (not linear-chain, not cyclic —
     e.g. a tree/star topology tying multiple fragments to one hub
     fragment) re-using the Singleton-Interleaving Lemma as the evaluation
     tool, cheap-killed the same way before any proof investment; or (b)
     abandon named constructions entirely and push the existence-only
     $\Sigma(n,k)$-classification / compactness route directly, treating
     all of rounds 11–15's fragment-tying numerics as evidence that no
     single bounded-description construction family suffices — consistent
     with, and now extended by, the file's own converging conclusion.
