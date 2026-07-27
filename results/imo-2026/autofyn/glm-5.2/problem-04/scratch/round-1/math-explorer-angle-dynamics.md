## imo-2026-04

### CONJECTURE (strong, numerically verified to discretization limit)
Mulan can guarantee victory in finitely many steps **iff** `180°/θ` is an integer, i.e.
`θ = 180°/n` for some integer `n ≥ 2` (the set `{90, 60, 45, 36, 30, 20, 18, 15, …, 1°, …}`).
Equivalently: `θ` is a divisor of `180°` in the sense `180°/θ ∈ {2,3,4,…}`. Every other
`θ` (including all `θ>90°`, and all `θ<90°` with `180°/θ∉ℤ` such as `50,72,80,54,100,7,…`)
is a Shan-Yu escape.

Both directions are clean and the mechanism is pinned down exactly below. This is not
a guess — the forward strategy and the backward closed-region argument are each verified
exhaustively on the `h=1°` grid (2700 triples) for `n∈{2,3,4,5,6,9,10,12,180}` and for
non-integer `180/θ ∈ {50,72,54,80,100,91,7}`.

---

### (1) The one-move transition on the angle triple — the core reduction

Let the current triangle have angles `(A,B,C)`, `A+B+C=180`. Mulan chooses a point `P` on
the side opposite vertex `C` (she may pick any of the three sides — equivalently any vertex
to be the "split" vertex). Let `γ ∈ (0,C)` be the piece of `C` adjacent to `A` (so `C−γ` is
adjacent to `B`). The cut `CP` produces two triangles:

  - **T1 = (A, γ, 180−A−γ)**  (the piece at vertex `A`)
  - **T2 = (B, C−γ, A+γ)**   (the piece at vertex `B`)

Both sums equal 180 (check: `B+(C−γ)+(A+γ)=A+B+C=180` ✓). The two angles at `P` are
`p1 := 180−A−γ` (in T1) and `p2 := A+γ` (in T2), and **`p1 + p2 = 180`** (supplementary).
This supplementary relation is the single load-bearing geometric fact. Everything else is
arithmetic on the triple.

So one move = (pick which of A,B,C to split, pick `γ`). The "new" angles Mulan can create
are `γ`, `180−A−γ`, `C−γ`, `A+γ` (the angles `A` and `B` are inherited unchanged from the
parent). Shan-Yu then discards one child, keeping the other as the new `T`.

**Key Mulan objective.** Mulan wins the *next* check iff the kept triangle contains `θ`.
Since Shan-Yu chooses the kept one, Mulan wins in one move iff she can make **both** children
contain `θ`.

---

### (2) What Mulan can force vs what Shan-Yu can deny

Work in the variable `n := 180/θ` (not necessarily integer yet). An angle is a "**multiple
of θ**" if it equals `kθ` for some integer `k≥1`. Let `S` = triples with **no** angle a
multiple of `θ` ("safe" region); `Sᶜ` = triples with at least one multiple-of-`θ` angle.

**Both-children-have-a-multiple-of-θ condition.** With parent angles `A,B,C` and the four
new angles `γ, p1=180−A−γ, C−γ, p2=A+γ`, both children lie in `Sᶜ` iff
`(γ mult ∨ p1 mult) ∧ (C−γ mult ∨ p2 mult)` (since `A,B` inherited). Expanding the AND
gives four terms, each forced to a parent invariant:

  1. `γ mult ∧ (C−γ) mult` ⟹ `γ+(C−γ)=C` is a multiple of `θ` ⟹ **C mult**.
  2. `γ mult ∧ p2 mult` ⟹ `p2−γ = A` is a multiple of `θ` ⟹ **A mult**.
  3. `p1 mult ∧ (C−γ) mult` ⟹ (substitute `γ=180−A−mθ` and `γ=C−nθ`) `180−A−C = B` is a multiple of `θ` ⟹ **B mult**.
  4. `p1 mult ∧ p2 mult` ⟹ `p1+p2 = 180` is a multiple of `θ` ⟹ **180 mult**, i.e. `180/θ ∈ ℤ`.

So: **Mulan can make both children lie in `Sᶜ` only if at least one of `A,B,C,180` is a
multiple of `θ`.** For a parent in `S`, `A,B,C` are all non-multiples, so the *only*
remaining door is term 4 — `180` being a multiple of `θ`, i.e. `n=180/θ` an integer.

- If `n∈ℤ` (forward case): term 4 is *possible*, and Mulan exploits it (see (3)).
- If `n∉ℤ` (backward case): **all four doors are shut**; from any parent in `S`, Mulan
  *cannot* make both children leave `S`. At least one child stays in `S`, and Shan-Yu
  keeps it. `θ` (= `1·θ`, a multiple of `θ`) never appears. **`S` is Shan-Yu-closed.**
  Verified: 0 violations across all tested non-integer `n`.

This single dichotomy IS the theorem. The boundary `180/θ∈ℤ` is exactly where term 4
switches from impossible to exploitable.

---

### (3) Reachable / attractor-set picture

**Backward (n∉ℤ):** `S` is nonempty (take any generic triangle, e.g. angles `(ε,ε,180−2ε)`
with `ε` irrational-ish so no angle hits a multiple of `θ`; such `ε` exist because the
multiples of `θ` are countable and `(0,180)` is not). Shan-Yu opens in `S` and, by closure,
stays in `S` forever. Mulan loses. **Attractor = `Sᶜ` only; not the whole space.**

**Forward (n∈ℤ, n≥2):** the attractor is the *entire* state space. Two lemmas close it.

  - **Lemma R (reduce a multiple).** If a triple has an angle `= mθ` (`1≤m≤n−1`), Mulan
    splits *that* angle at `γ=θ`. Child1 `= (A, θ, …)` already contains `θ` → if kept, the
    next check fires and Mulan wins immediately. Child2 `= (B, (m−1)θ, A+θ)` contains
    `(m−1)θ`. Shan-Yu must keep child2 to survive (when `m≥2`), reducing the multiple by 1.
    Induct on `m`; base `m=2` makes *both* children contain `θ` (a forced win regardless).
    So a triple with an `mθ`-angle is a win in `≤ m−1` moves. (Validity: `γ=θ<C=mθ` needs
    `m>1` ✓; child2's angles are all positive ✓; the `mθ`-angle survives as a clean angle
    in child2 so the induction iterates ✓.)

  - **Lemma F (reach a multiple from anywhere).** From a triple with *no* multiple-of-`θ`
    angle, Mulan splits the **largest** angle `C` (so the two non-split angles `A,B` are the
    two smaller). For `n≥3`, `C ≥ 60° ≥ θ = 180/n` (since `n≥3 ⇒ θ≤60`), and `C` is not a
    multiple of `θ`, so `C > θ`, giving `C/θ > 1`. The open interval `(A/θ, (A+C)/θ)` has
    length `C/θ > 1`, hence contains an integer `k` strictly inside; set `γ = kθ − A`.
    Then `γ ∈ (0,C)` (from `k` strictly inside), `p2 = A+γ = kθ`, `p1 = 180−A−γ = (n−k)θ`,
    **both** `P`-angles are multiples of `θ` ⟹ both children lie in `Sᶜ` ⟹ by Lemma R
    both are Mulan wins. (For `n=2`, `θ=90`: same argument, `k=1`, requires the two
    non-split angles `A,B<90`, which holds because we split the largest angle of a non-right
    triangle — either all-acute or obtuse gives the other two `<90`.)

    `k` is automatically in `{1,…,n−1}`: `kθ=p2<180=nθ` gives `k<n`, and `k>A/θ>0` gives
    `k≥1`. ✓

Verified exhaustively (h=1° grid): the "split-largest + integer-in-interval" move
produces two children each carrying a multiple of `θ` for **every** triple and every
`n∈{2,3,4,5,6,9,10,12,180}` — 0 failures.

So: `n∈ℤ` ⟹ attractor = all triples ⟹ Mulan wins from any opening, in `≤ (n−1)`-ish moves
(Lemma F gives one move into `Sᶜ`; Lemma R takes `≤ m−1 ≤ n−2` more). Finiteness is
explicit.

---

### (4) Small-case / intuition notes (all conjecture confirmed by computation)

  - `θ=60 (n=3)`: level data — `W0`={has 60} (60 triples), `W1`={has 60 or 120} (+30),
    `W2`=all (+2610). Max 2 moves. Generic example `(50,55,75)`: split `75`... actually
    the found move splits `C=55`?? — the found forcing move was `(A,B,C,γ)=(75,50,55,45)`:
    `p1=60, p2=120`. Both children `(45,60,75)` and `(10,50,120)` carry a multiple. ✓
  - `θ=90 (n=2)`: family-(b) move `γ=90−A` makes both `P`-angles `=90`; works from any
    non-right triangle (split the largest angle; the other two are `≤90`).
  - `θ=36 (n=5)`, triple `(1,1,178)`: `C=178`, `A=1`, interval `(1/36, 179/36)≈(0.028,4.97)`,
    `k=4`, `γ=143`, `p1=36`, `p2=144`. Both children carry a multiple. ✓
  - `θ=50` (n=3.6, fails): `|S|=2581` safe triples, all avoiding `{50,100,150}`; Mulan
    has *no* move making both children enter `Sᶜ` (0 violations). Equilateral `60-60-60` is
    in `S` and is a valid Shan-Yu opening.
  - `θ=72` (n=2.5), `θ=54` (n=10/3), `θ=80` (n=2.25), `θ=100,91,7`: all fail, all with `S`
    closed and nonempty. The safe region is *the same* "no multiple-of-θ angle" set across
    all of them.
  - `θ=1°` (n=180): works (verified). So the winning set is infinite and accumulates at 0.

**Label:** the above is *conjecture confirmed by exhaustive grid computation*, not a
certificate. The continuous case (real `θ`, real angles) is not covered by a grid; the
proof must handle it. But the argument in (2)–(3) is purely algebraic (no discreteness),
so it should port directly.

---

### (5) Hardest step / gap a proof must close

The hardest single step is **Lemma F's interval argument in the continuous (non-grid)
setting**, specifically:

  - (a) proving "an open interval of length `>1` contains an integer" cleanly handles the
    strict-inequality boundary (when `C/θ` is exactly an integer-plus-epsilon, or when `A/θ`
    is itself an integer) — need `γ∈(0,C)` *strict*, and the two children's multiple-angles
    must be *strictly positive* (an angle of `0` is illegal). Edge: if `kθ−A=0` or `=C` the
    cut degenerates; the strict-integer-inside formulation already excludes this but the
    proof must say so.
  - (b) verifying the induction in Lemma R never produces a degenerate child2 (e.g. when
    `m=n−1` and the *other* inherited angle `A+θ` accidentally exceeds `180` or coincides
    with a multiple — does the `mθ`-angle always remain a *clean, splittable* angle of
    child2?). The grid confirms it, but a continuous proof must check `γ=θ<C=mθ` strictly
    and child2 positivity for every step.
  - (c) the **non-emptiness of `S` for the backward direction** when `n∉ℤ`: must *exhibit*
    a triangle with no angle a multiple of `θ`. Easy (generic existence) but must be stated;
    for `θ>90` the only multiple `<180` is `θ` itself, so any triangle avoiding `θ` works
    (e.g. equilateral if `60≠θ`).

There is **no** deeper gap: the four-term closure (2) and the interval lemma (3) are the
whole story. No heavy machinery needed.

---

### (6) Candidate approach framings for the outliner (distinct, not technique-variants)

  - **Framing A — "Supplementary `P`-angles + the four-term closure" (the direct one).**
    Define `S` = no-multiple-of-`θ` region. State the one-move transition; derive the four
    terms (1–4) showing "both children in `Sᶜ`" requires one of `A,B,C,180` to be a
    multiple of `θ`. Split into the two cases `180/θ∈ℤ` / `∉ℤ`. Forward: Lemmas R + F
    (split largest, interval-contains-integer). Backward: `S` closed + nonempty. This is
    the canonical shortest proof; the outliner's default.

  - **Framing B — "Attractor / backward-induction on the state space".** Frame the whole
    thing as a game on the compact state space of angle-triples; define the winning region
    `W` as the least fixpoint of "already has `θ`" ∪ "can force both children into `W`".
    Show `W = everything` iff `n∈ℤ` by exhibiting the closed cofinite (complement) set `S`
    when `n∉ℤ`, and the explicit level-stratification (`W_k` = triples from which Mulan
    reaches a multiple-of-`θ` angle in `≤k` moves) when `n∈ℤ`. Same core lemmas, but
    packaged as a game-theory fixpoint argument (cleaner for the "finitely many steps"
    clause, since the level bound gives termination explicitly).

  - **Framing C — "Potential / monovariant: count of non-`θ`-multiple angles".** Define a
    potential `Φ(T) =` (number of angles of `T` that are NOT multiples of `θ`) or the
    minimal multiple-index. Forward: show Mulan can strictly drive down the minimal
    multiple-index (Lemma R) and reach it in one step from anywhere (Lemma F); Shan-Yu's
    discard cannot increase it past what Mulan just forced. Backward: exhibit `S` as a
    fixed point where `Φ=3` is invariant under Shan-Yu's best response. Sells the
    "finitely many steps" as a bounded-potential descent. (Spiritually akin to
    aimo-0236's "nurse a token above a threshold" escape invariant.)

---

### Knowledge-base entries to use
- **Invariants & monovariants** (Combinatorics) — the closed set `S` is an invariant region;
  Lemma R's multiple-index is a strict monovariant.
- **General: Invariant / monovariant; Pigeonhole / extremal; Contrapositive** — backward
  direction is a contrapositive ("if `n∉ℤ`, escape").
- **Pólya heuristics: Work backward; Solve a simpler case; Reformulate** — the
  angle-triple reformulation is the reformulation that cracks it.
- (No geometry theorems needed beyond "angles at a point on a line are supplementary" and
  "angle sum = 180"; no trig, no Ceva, no coordinates.)

### Analogous past problems (cruxes)
- **aimo-0445** (games-and-strategy, "double threat") — *analogous in spirit to the forward
  direction*: Mulan's winning move creates a position where BOTH children are winning, so
  Shan-Yu's single discard cannot avoid the threat. Crux: "make a single move that creates
  two independent one-move winning completions, so the opponent's one removal cannot block
  both." Same logic as "both `P`-angles are multiples of `θ`."
- **aimo-0236** (games-and-strategy, "nurse a token / invariant region closed under
  opponent moves") — *analogous to the backward direction*: Shan-Yu maintains an invariant
  region `S` (no multiple-of-`θ` angle) that survives every Mulan move, so the target
  `θ` is never reached — exactly "have that player nurse a single token so a driving
  valuation stays above the threshold; close with a two-part induction showing the
  threshold holds before AND after each opponent move."
- No genuinely *geometric* analog exists in the corpus (geometry cruxes are not extracted;
  the documentation says so). The closest structural analogues are the two game cruxes above.

### Prior progress
None — round 1, empty workspace (`results/imo-2026-04/` has no approaches, no lemmas, no
`current.md`). This report is the first reconnaissance.

### Dead ends (do not retry)
None yet (round 1). The one tempting but *wrong* reduction to avoid: trying to prove the
result by only tracking whether `θ` itself appears (the `m=1` level). That stalls because
generic triangles have no `θ`-angle and no `2θ`-angle either; the *correct* invariant is the
full ladder of multiples `θ,2θ,…,(n−1)θ` and the closed set `S` = "none of them." Do not
frame the winning region as merely `{has θ}` — it must be the iterated attractor / the
`S`-vs-`Sᶜ` dichotomy.

### Distinct openings (summary)
1. The four-term algebraic closure on `S` — the cleanest direct proof (Framing A).
2. The game-theoretic attractor fixpoint on the angle-triple state space (Framing B) — best
   for nailing the "finitely many steps" clause with an explicit level bound.
3. The monovariant / potential descent on the minimal multiple-index (Framing C) — best for
   a tight move-count bound and a clean Shan-Yu-escape invariant.
All three rest on the *same* two facts (supplementary `P`-angles; interval-of-length-`>1`
contains an integer); they are packaging variants, but the outliner should pick the one
whose rigor flow is cleanest — Framing A is recommended.
