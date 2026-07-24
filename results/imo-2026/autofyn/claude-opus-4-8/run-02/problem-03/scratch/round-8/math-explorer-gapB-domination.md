## imo-2026-03 — Gap B / Lemma BD (degenerate-Φ-domination)

### Precise statement of Gap B
At the `Φ=Σx_i²`-maximal minimizer `P*` (§5 of `self-similar-recursion.md`), after Moves M2
(`μ_{k,j}≤3`) and M3 (odd-size tie-blocks carry only `μ_{k,j}≤1`), the incidence-multigraph
peeling (Gap A) needs every **piece-leaf** (degree-1 piece node) to force an integer value. A
piece-leaf with edge-multiplicity `μ∈{1,2}` gives `w_j=2^k` or `2^{k-1}` (integer) automatically.
The **μ=3 even-block piece-leaf** is the one case that resists: piece `2^k` has all three of its
sub-pieces equal to a single value `v=2^k/3`, and that value `v` is *shared* with (at least) one
other piece — so its tie-block `C_j` has **even** total size `μ_j` (the *unshared* μ=3 case is a
size-3 **odd** block and is already killed by M3). Because `v` is shared, `(★)` does *not* force
`v` to be a nice fraction of `2^k` alone — the block-formula (BF) makes this leaf's own
contribution to `f` **vanish exactly** (even blocks are BF-invisible), so nothing internal to `f`
constrains `v`, and `v=2^k/3` need not be rational-nice or forced integer.

**Gap B (statement, as it must be proved):** *No `Φ`-maximal minimizer `P*` of a `≤n`-cut
refinement of `W_n` contains a μ=3 even-block piece-leaf.* Equivalently (round-7 sharpening):
any config containing such a leaf either (a) uses `>n` cuts (over budget — infeasible for `W_n`
directly), or (b) is not `Φ`-maximal / not a global minimizer of `f` (i.e. is Φ-dominated or
f-dominated by a competitor achieving `f≥1` in the true feasible class), so it cannot be `P*`.

**Lemma BD, as it must be proved:** *Every `≤n`-cut refinement of `W_n` that contains a μ=3
even-block piece-leaf has `f≥1`.* (This is exactly what is needed — it does not require
comparing to a *different* minimizer; it directly asserts the residual case satisfies the
target inequality, closing Gap B by absorbing it into (LBL) rather than by excluding it from
`G`.) The name "degenerate-Φ-domination" in the outline anticipated proving this via producing a
degenerate competitor `P'` with `f(P')=f(P*)` and invoking Claim(N−1); my numerical work below
shows a **cleaner, more promising route bypassing Φ/degeneracy entirely** — see "Most promising
opening."

### Distinct openings for a global, budget-based Lemma BD

1. **Direct cut-cost accounting + Claim(N−3) induction (MOST PROMISING — see numerics below).**
   Building a μ=3 even-block leaf costs *exactly* 3 cuts minimum: 2 to trisect the leaf piece
   `2^k` into `{v,v,v}`, plus **at least 1 more** cut on some *other* piece `2^m` to make `v`
   appear there too (since `v=2^k/3` is never itself a power of two, so it can never equal an
   *uncut* piece — the donor piece must be split). Given total budget `N≤n`, at most `n−3` cuts
   remain for the rest of `W_n`'s `n−1` other pieces (all pieces except the leaf-piece and the
   donor-piece, whose own remaining mass beyond `v` also counts as a new "piece" in the residual
   system). The natural move: show the **complement structure** (everything except the
   BF-invisible leaf block) is *itself* a legitimate `≤(n−3)`-cut-type refinement problem of
   smaller total budget, to which Claim(N−3) (the strong induction hypothesis, already proved for
   fewer cuts) applies, forcing its alternating sum `≥1` (or `≥0` with parity/positivity kicking
   in) hence `f(P)=0+f(\text{complement})≥1`. This is a genuine budget/induction argument, not a
   local move, exactly matching what CLAUDE.md and round 7 flagged as necessary.

2. **Direct verification that "spare" pieces around the leaf always contribute enough positive
   mass.** My numeric experiments (below) show that whenever the μ=3-even-leaf-with-donor
   construction is embedded at budget-`n`, any piece **above** the leaf in the descending order
   that remains uncut contributes at the *dominant* (`+`) sign and swamps the leaf's zero net
   contribution; only when the leaf sits at the very *top* (no larger piece above it) does the
   construction come close to `f<1`, and even then, once embedded at `n≥3` (so that budget allows
   the construction), the untouched *lower* pieces still contribute enough net positive mass to
   push `f≥1`. This suggests a case split on the leaf's *position relative to the top piece*.

3. **Recursive/self-similar framing: treat the (leaf + donor) pair as "spending" a piece 2^k of
   the original W_n, and recurse Claim on the reduced stick.** Since the leaf-plus-donor exactly
   consumes value `2^k + 2^m` of the original dyadic budget for 3 cuts, and the leftover donor
   mass `2^m − v` behaves like a "new small piece," one can try an exact accounting identity
   analogous to the certified `two-band-single-cut-identity` (Lemma 3.1, cut-budget route) but
   generalized to a 2-cut compound move (trisection + split), giving an exact formula
   `f(P) = f(\text{leaf+donor local piece}) + f(\text{rest})` and separately bounding each term.

4. **Dual-route translation:** in the Cramer/`(D′)` picture, the μ=3-even-leaf case is precisely
   where `det(U)` picks up a factor of 3 from the leaf's row (piece row = `3·e_j` up to
   permutation) — this is the *same* obstruction Lemma 1 of `concentration-exclusion-rigidity`
   already isolates (`m·e_k ⇒ m∣det U`, here `m=3`). The Concentration Exclusion Theorem
   currently proves only `m=2` concentrations survive (the μ=3 case was excluded there via "M3 on
   the odd block", but note: the *even* μ=3 case, i.e. exactly Gap B, is explicitly flagged in
   that approach file as needing its own separate treatment — check whether
   `concentration-exclusion-rigidity`'s machinery (Reduction Lemma peeling invisible columns) can
   peel the visible reduced μ=3-leaf column directly via a Cramer divisibility argument instead of
   a geometric domination argument. This may be a cleaner algebraic route to the SAME fact as (1).

### Relation to the dual route's Budget Lemma
Both are genuinely **budget-based accounting facts about `W_n` under `≤n` cuts**, but they are
NOT the same statement:
- Dual Budget Lemma: *no all-even refinement of `W_n` is reachable in `≤n` cuts* (needed for
  Positivity, `f≠0`). This is about *every* value having even multiplicity globally.
- Gap B / Lemma BD: a *local* structural fact — one specific piece-leaf shape (μ=3, shared,
  hence part of an even block) cannot survive within budget while keeping `f<1`. It does **not**
  require the *whole* configuration to be all-even — only this one leaf's block is even; other
  blocks can be odd (indeed must be, for Positivity to hold elsewhere).
- **Shared accounting principle:** both ultimately rest on the same "powers-of-2 are
  superincreasing, so redistributing budget away from a large piece to manufacture ties is
  expensive in cuts" idea, and both would benefit from a single general **cut-cost lemma**:
  *"realizing any tie of `t` equal sub-pieces sharing across `≥2` original dyadic pieces costs at
  least `t` cuts"* (here `t=4`: 2 to trisect + at least 2 more if you need TWO donor pieces, but
  in the μ=3 leaf case only 1 donor suffices since `μ_j=4` is achievable with one 3-piece leaf +
  one single donor copy). If proved as a *standalone* combinatorial fact (independent of both
  routes), it could feed directly into **both** the Budget Lemma (dual) and Lemma BD (primal) as
  a shared cut-counting engine — a genuine unification opportunity for round 8/9.

### What's dead (do not retry)
- **No local/cross-piece move can exclude the leaf directly** (round 7, confirmed): the domain
  `K=∏_kΔ_k` is an unconstrained product of simplices; the only feasible perturbations of a μ=3
  leaf are within its own piece (M3's symmetric shift, which on an EVEN block is a V-kink — no
  descent, no flat Φ-rise) or M2's two-pairs move (needs 4 equal copies in one piece, unavailable
  at μ_{k,j}=3). Confirmed again by inspection — no new local move found this round either.
- **"Bisect-instead" and "symmetric-to-degenerate"** one-liners (round 7, both refuted): changing
  global rank interleaving in uncontrolled ways; do not retry verbatim.
- **Treating Gap B as reducible to the dual route's Budget Lemma wholesale** — they are related in
  spirit (both budget accounting) but are formally different statements (global all-even vs.
  local shared-leaf); do not conflate them into one proof without separate justification.

### Numeric experiments (exact, via `Fraction`)

All computed with `python3`/`fractions.Fraction`, alternating sum `f = Σ(-1)^{i+1} a_i` on the
descending-sorted multiset.

1. **Baseline (round-7 example, n=2, 3 cuts, over budget):** `piece1={1}`, `piece2={4/3,2/3}`,
   `piece4={4/3,4/3,4/3}` → multiset `{4/3,4/3,4/3,4/3,1,2/3}`, `Σ=7=D_2`, **`f=1/3<1`**. Confirmed
   over-budget (3 cuts > n=2). The leaf (piece4) is at the very TOP of W_2.

2. **Same shape embedded at n=3, budget exactly matched (3 cuts, budget 3, leaf at TOP piece 8,
   donor = piece 4, pieces 2,1 uncut):** `piece8={8/3,8/3,8/3}`, `piece4={8/3,4/3}` — wait, actual
   construction used donor sharing `v=8/3` (leaf at top=8) with `piece4={8/3,4/3}`(1 cut), `piece2={2}`
   uncut, `piece1={1}` uncut → multiset `{8/3,8/3,8/3,8/3,2,4/3,1}`, `Σ=15=D_3`,
   **`f=5/3 ≥ 1`** (NOT a counterexample — Claim(3) survives).
   Block-formula check: the four `8/3`'s are an even block (μ=4, contributes 0); the *residual*
   `{2,4/3,1}` (piece2 uncut, donor leftover 4/3, piece1 uncut) alone has
   `f_residual = 2 − 4/3 + 1 = 5/3`, matching the total — confirms BF exactly, and shows the
   residual mini-system behaves like its own smaller extremal problem with `f≥1`.

3. **Leaf NOT at the top (n=3, leaf at piece 4, donor = piece 2, top piece 8 UNCUT, piece1
   uncut, 3 cuts, budget 3):** multiset `{8,4/3,4/3,4/3,4/3,2/3,1}` → **`f=23/3`**, far above 1
   (the uncut top piece 8 dominates the alternating sum at the `+` sign and swamps everything).

4. **Leaf at piece 4 with different donor placement, n=3 (`piece4` trisected, share via `piece2`,
   top `8` uncut) mirrored/variant:** **`f=23/3`** (same family) — confirms: whenever a *larger*
   piece is left fully uncut above the leaf, `f` is driven well above 1, not below.

5. **n=4, leaf at piece 4 (not top), tops 16,8 uncut, donor=piece2, piece1 uncut, 3 cuts,
   budget 4 (1 spare unused):** multiset with `{16,8,4/3,4/3,4/3,4/3,2/3,1}` → **`f=25/3`**.

6. **n=4, leaf at piece 8 (not top), donor = piece 4, top 16 uncut, pieces 2,1 uncut, 3 cuts,
   budget 4:** multiset `{16,8/3,8/3,8/3,8/3,4/3,2,1}` → **`f=43/3`**.

**Pattern (conjectural, strong evidence):** the round-7 `f=1/3` counterexample is *only* achievable
when the leaf sits at piece `2^n` (the TOP of the whole stick) **and** there is no piece above it —
which is only possible at all when `n` equals exactly the leaf's own level, i.e. the minimal
over-budget case n=2 itself (3 cuts > 2). As soon as the same leaf shape is embedded in any *larger*
`W_n` (so that the 3-cut construction actually fits the `≤n` budget), either (i) the leaf is forced
away from the true top (since something must occupy 2^n), and the necessarily-uncut top piece
dominates positively, pushing `f` far above 1; or (ii) the leaf *is* at the top, but then the
lower structure below it and the donor, minus the leaf's own block (BF-invisible), constitutes an
independent residual sub-problem whose alternating sum is itself `≥1` by the same recursive logic
(observed exactly: `f_residual({2,4/3,1})=5/3≥1`). In every embedding tried (5 distinct
constructions across n=3,4), **min f over the μ=3-even-leaf family was 5/3, well clear of 1** — no
counterexample with `f<1` was found once the construction is actually budget-feasible for its `n`.
This is a **conjecture** (small sample, hand-picked constructions, not an exhaustive search over
all embeddings/donor choices/spare-cut allocations) but it is consistent and suggests Lemma BD is
TRUE and provable via the induction-on-residual-budget route (opening 1/3 above), not via a
Φ-domination move.

### Most promising opening
**Opening 1 (direct cut-cost + Claim(N−3) induction).** The cleanest path: formalize "creating a
shared μ=3 even leaf costs ≥3 cuts" as an exact combinatorial fact, then show the *complement*
system (after removing the leaf's own BF-invisible even block) is a genuine `≤(N−3)`-cut-type
refinement to which the strong induction hypothesis Claim(N−3) directly applies — giving
`f(P)=f(\text{complement})≥1` (or `≥0` plus a parity/positivity top-up) with NO need to construct a
Φ-dominating competitor at all. This sidesteps the originally-envisioned "produce a degenerate
competitor with equal f" construction (never found in 2 rounds) in favor of a direct residual-mass
argument, matching what the 5 numerical experiments above all independently confirm (the residual
always resolves as its own smaller Claim instance with `f≥1`). This is a genuinely different,
simpler mechanism than Φ-domination and should be the round-8/9 target for Lemma BD.

### Knowledge-base entries to use
- **Extreme value theorem / Lagrange multipliers on a compact manifold** (Linear Algebra section)
  — underlies the existing Φ-maximal-minimizer machinery (already in use, no new KB entry needed
  for opening 1).
- **Pigeonhole / extremal principle**, **Invariants & monovariants** (Combinatorics section) —
  directly applicable to formalizing the "3-cut cost" combinatorial fact (a cut-counting
  pigeonhole akin to the certified `uncut-survivor` lemma).
- **Divisor analysis / superincreasing powers-of-two structure** (used pervasively already in
  Lemma CC+, POS-CHAR, top-piece-cut) — the same superincreasing bound `Σ_{a<k}2^a<2^k` is likely
  needed again for opening 1's "spare budget" accounting.

### Analogous past problems (cruxes)
I did not query the crux corpus this round (out of scope for the assigned deep-dive; the corpus
was already searched in prior rounds for this problem's general shape — alternating-sum / stick-
cutting games — with no closer analogue found for the specific micro-lemma "leaf costs ≥3 cuts").
If time permits next round, worth a targeted query on subtopic keywords like "extremal
multiset/alternating sum" or "matching/parity game" per `crux_moves_documentation.md`, but I judge
this specific sub-gap (a budget-counting induction on a highly problem-specific stick structure)
unlikely to have a close pre-2026 analogue; flagging "none found" rather than forcing a weak match.

### Prior progress
Everything in `self-similar-recursion.md` §0–§4 (reduction, S-core, M2, M3, M4, block formula) is
certified and unconditional. Gap B is pinned exactly as above; Lemma BD is unconstructed. No
regression this round — my numeric work is new supporting conjecture-level evidence for the
"opening 1" induction route, not a proof.

### Dead ends (do not retry)
- Any LOCAL move on the μ=3 leaf itself (M2/M3 exhausted — no other feasible direction exists in
  the unconstrained product-of-simplices domain).
- "Bisect-instead" / "symmetric-to-degenerate" one-liners (round 7 refuted).
- Treating Gap B as literally the same statement as the dual route's Budget Lemma (related, not
  identical — see "Relation" section above).
- Searching for a Φ-dominating degenerate competitor with EXACTLY equal f (attempted implicitly by
  round 7's framing, never constructed in 2 rounds) — the numerics above suggest this is the wrong
  target; the residual-induction route (opening 1) looks structurally cleaner and is better
  supported by the data.
