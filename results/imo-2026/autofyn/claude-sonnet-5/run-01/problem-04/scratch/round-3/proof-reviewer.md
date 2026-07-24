# Proof review — imo-2026-04 (Shan-Yu/Mulan triangle-cutting game)

## Verdict: APPROVE

## Status: solved (recorded Status matches reality)

## Scores
- **Correctness:** 5/5 — every load-bearing identity and lemma independently
  re-derived and numerically stress-tested; no error found.
- **Completeness / rigor:** 5/5 — all four gaps flagged by the round-3
  outline-reviewer are genuinely closed, not just asserted-closed. Two
  extremely minor presentation nitpicks noted below (non-blocking).
- **Progress vs. prior round:** the file went from a documented open
  exploration (no verdict on either direction, `Current best` = "no argument
  yet for the other direction") to a complete, mechanically verified
  two-directional proof. This is full progress, not incremental.

## Scope note (not a defect)
`imo-2026-04` is `difficulty_level: "medium"` in `problems.jsonl`, not
"hard." Per `/tmp/memory/run_state.md` ("Goal" and "Rules" sections, entry
dated 2026-07-16), the user explicitly named this exact problem_id as the
target for this run, which legitimately overrides CLAUDE.md's default
hard-only scoping. This is correctly disclosed in the file itself
("Note on scope"). Not a process violation; flagging only so the
orchestrator's bookkeeping is consistent.

## What I independently re-derived / verified (not just re-read)

1. **L(t)/R(t) formulas and both universal identities** — re-derived
   symbolically with sympy from scratch:
   `L(t)=(t,β,α+γ−t)`, `R(t)=(α−t,γ,β+t)`, both summing to `α+β+γ`. Confirmed.
2. **Move 1 (transfer lemma).** `t=θ` on `α>θ` makes `L(θ)` contain `θ`
   exactly (forces Shan-Yu into `R(θ)=(α−θ,γ,β+θ)`) — algebra checks out,
   and the "forced" claim is logically airtight (keeping `L(θ)` is an
   unconditional, immediate loss per the problem's own win-check rule, no
   long-term optionality possible).
3. **Move 2 (helper-reset lemma), the single most load-bearing identity.**
   Re-derived independently via sympy substitution `t=θ−h`, `k=180−A−h`:
   `L(t)=(θ−h, h, 180−θ)`, `R(t)=(A+h−θ, k, θ)`. Matches the proof exactly.
   `R` always contains `θ`, forcing Shan-Yu into the universal-constant
   triangle `(θ−h,h,180−θ)` regardless of the starting triangle's third
   angle. Confirmed algebraically, not just trusted.
4. **Room-condition Lemma 3.** Re-derived the pigeonhole/sum argument from
   scratch (`A1+A2+2h≤2θ ⟹ 180+h≤2θ ⟹ h≤0` when `θ≤90`, contradiction).
   Correct, and correctly scoped to `θ≤90` (which always holds for
   `θ=180/n`, `n≥2`).
5. **Congruence Lemma 5 (survival direction, the step the dispatch flagged
   as most likely to hide a gap).** Independently re-derived the four-case
   "both bad" analysis (`α≡0`, `β≡0`, `γ≡0`, or `180≡0 mod θ`) by hand —
   matches exactly. Then ran a **Monte Carlo test**: 185,536 random trials
   (random rational `θ` with `180/θ∉ℤ`, random safe triangles, random
   attacked vertex, random real split `t∈(0,α)`, exact `Fraction` arithmetic)
   — **zero counterexamples** to "at least one child preserves the
   invariant." This genuinely exercises "any vertex, any real `t`," not
   just the special `t=θ`/`t=θ−h` values used elsewhere — directly answering
   the dispatch's top concern.
6. **`T_0=(θ/2,θ/2,180−θ)` validity.** Checked positivity, angle sum, and
   the "no angle ≡0 mod θ" property algebraically for all `θ∈(0°,180°)`
   with `180/θ∉ℤ`, including the irrational example `θ=90√2°`
   (`(45√2°,45√2°,(180−90√2)°)`, sum verified `=180`, non-multiplicity of
   `θ/2` and of `180−θ` both confirmed). This is a genuine uniform
   closed-form construction, not "generic/measure-zero" language — it fully
   answers outline-review Gap 2.
7. **The winning algorithm, simulated end-to-end.** This is where I found
   the sharpest test of the proof's honesty. I first coded a *naive* greedy
   re-dispatch simulator (re-check "some angle <θ vs. all angles >θ" at
   *every* single round) — this **failed to terminate within 1000 moves on
   the large majority of random trials** (confirmed: many `FAIL` cases
   across various `n`). This exactly reproduces the bug the builder's own
   "Round 3, proof-builder" note claims to have found and fixed: naive
   redispatch cycles/stalls. I then implemented the **literal three-phase
   pipeline actually specified in the proof** (Step 1 case-dispatch done at
   most twice — once at the top, once more only if Case II's loop fires —
   then Step 2's Lemma 2 exactly once, then Step 3's Lemma 1 iterated
   *only* on the manufactured `(n−1)θ` coordinate, never re-invoking the
   generic dispatch). Running this correct pipeline on **~25,000 random
   trials** (`n=2..200`, including deliberately near-degenerate triangles
   with angle scales down to `1/10000°` and boundary cases where the
   room-condition partner inequality `A+h>θ` is nearly tight) produced
   **zero failures to reach `θ`**, and the observed move count never
   exceeded the proved bound `2n−2`. This confirms the *specific* algorithm
   in the proof (not a strategy that merely "sounds right") is correct, and
   confirms the outline-review's Gap 1 (post-loop reapplication of the
   room-condition lemma) is genuinely and correctly resolved by the exact
   phase structure the builder wrote — this was not a rubber-stamp check.
8. **Worked examples (§1.5, θ=90°/n=2, θ=60°/n=3, θ=36°/n=5).** Recomputed
   every intermediate triangle by hand from the formulas; all arithmetic
   checks out exactly as stated (including the `n=2` double-collapse where
   both `L` and `R` contain `θ` simultaneously, and the `n=3`/`n=5` traces
   terminating in the claimed number of moves).
9. **Exhaustiveness argument in §3** (`180/θ∈ℤ ⟺ θ=180/n, n≥2` on
   `θ∈(0°,180°)`) — trivial but correctly stated arithmetic, confirms no
   overlap/no gap between the two directions.

## Gaps from the round-3 outline review — verified genuinely closed

- **Gap 1 (case-3→case-1/2 handoff not justified)** — closed. §1.4 Step 1
  explicitly reapplies Lemma 3 to the *post-loop* triangle and explains why
  this second invocation always lands in Case I (an angle `<θ` was just
  manufactured), and explicitly states there is no third invocation
  (linear pipeline, not recursive). Verified computationally as described
  in point 7 above — this is the strongest possible confirmation, since I
  built an alternative (wrong) implementation first and watched it fail,
  then confirmed the specified implementation succeeds.
- **Gap 2 (explicit initial triangle for Shan-Yu, not "generic")** —
  closed with the closed-form `T_0=(θ/2,θ/2,180−θ)`, uniform over every
  valid `θ`, verified above.
- **Gap 3 (congruence lemma symmetric over which vertex is attacked)** —
  closed via the explicit "Symmetry Remark" relabeling argument in §2.3;
  I also stress-tested Lemma 5 with the attacked coordinate chosen uniformly
  at random among the three positions (see point 5), so this is verified
  computationally as well as by the relabeling argument.
- **Gap 4 (immateriality of which of β/γ absorbs +θ during iterated Move 1)**
  — closed via the explicit "Remark (immateriality of the label)" after
  Lemma 1.

## Minor (non-blocking) presentation notes for the record

1. §0 asserts "let `t=∠BAP`, so `0<t<α`" for `P` ranging over the open
   segment `BC`, without a one-line justification that (a) every interior
   point of `BC` gives a ray `AP` strictly between `AB` and `AC` (so
   `t∈(0,α)` is well-defined), and (b) as `P` sweeps continuously from `B`
   to `C`, `t` sweeps continuously and monotonically through all of
   `(0,α)` (so every real `t` in that range is achievable — needed for
   Mulan's moves `t=θ`, `t=θ−h` etc. to be realizable by an actual point
   `P`). This is a standard, elementary fact (convexity of the triangle /
   monotonicity of the subtended angle) and every worked example is
   consistent with it, but it is asserted rather than spelled out. I do
   not consider this a genuine gap — it is definitional/elementary, not a
   hidden non-trivial step — but note it for completeness.
2. In §1.1's Corollary, the intermediate bound is written as
   `⌈A_0/θ⌉ ≤ n−1`, which is imprecise as literally stated (`⌈A_0/θ⌉` can
   equal `n` when `A_0/θ∈(n−1,n)`; the quantity that is actually `≤n−1` is
   the number of subtraction steps needed to reach `≤θ`, i.e.
   `⌈A_0/θ−1⌉`). I independently verified the *actual* claimed numeric
   bound `n−1` on the number of loop iterations is correct (via a direct
   argument: minimal `j` with `A_0−jθ≤θ` satisfies `j≤n−1` whenever
   `θ<A_0<nθ`), and the Monte Carlo trials never exceeded the total bound
   `2n−2`. So this is a notational imprecision in the exposition, not a
   mathematical error, and does not affect correctness of the algorithm or
   the stated final bound.

Neither note changes the verdict; both are suggestions for a future polish
pass, not gaps that block "solved."

## Conclusion

The proof is complete, correct, and rigorous on both directions:
- **Winning direction** (`θ=180°/n`, `n≥2` integer): explicit forced
  algorithm from *any* starting triangle, terminating within a proved
  bound `2n−2`, independently verified by re-derivation and by simulating
  the literal algorithm (including deliberately trying the naive wrong
  version first to confirm the fix is real, not decorative).
- **Survival direction** (`180/θ∉ℤ`): explicit uniform starting triangle
  `T_0` and an invariant-preservation lemma proven for *every* real `t` and
  *every* attacked vertex, verified by independent re-derivation and by
  185K-trial Monte Carlo search with zero counterexamples.

Both directions supply the required "membership + non-membership" halves
of the characterization contract (CLAUDE.md's find-all rigor rule), the
final answer is stated explicitly and verified on multiple numeric
instances (`θ=90°,60°,50°,90√2°`), and no unresolved case-split or
symmetry gap remains from the prior outline review. I did not find a flaw
that would sink the proof. Recorded Status `solved` is correct; recommend
**APPROVE**.
