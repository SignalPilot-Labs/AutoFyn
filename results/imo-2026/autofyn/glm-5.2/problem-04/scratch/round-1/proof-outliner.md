## imo-2026-04

Answer (conjecture, cross-confirmed by all three explorers and numerically verified):
Mulan can guarantee victory in finitely many steps **iff** `180°/θ ∈ ℤ`, i.e.
`θ = 180°/n` for an integer `n ≥ 2`. Equivalently the winning set is
`{90°, 60°, 45°, 36°, 30°, …}`. Every other `θ` (all `θ > 90°`, and every `θ < 90°`
with `180/θ ∉ ℤ` such as `50°, 72°, 80°, 54°`) is a Shan-Yu escape. This is a
`compute_and_prove` characterization: each approach below proves BOTH directions
end to end.

Core reduction (shared by all approaches; established rigorously by the explorers):
a cut from perimeter point `P` to the vertex with angle `C`, parameter `γ ∈ (0,C)`
(piece of `C` adjacent to `A`), yields children
`T1 = (A, γ, 180−A−γ)`, `T2 = (B, C−γ, A+γ)`. The two new angles at `P` are
`p1 = 180−A−γ`, `p2 = A+γ`, and **`p1 + p2 = 180`** (supplementary) — the single
load-bearing geometric fact. Mulan wins the next check iff the KEPT child contains
`θ`; since Shan-Yu chooses which child to keep, a one-move forced win requires BOTH
children to contain an angle that is a multiple of `θ` (the target `θ` itself, or a
higher multiple which the descent then reduces to `θ`).

Define `B_θ = {kθ : k ∈ ℤ_{≥1}, 0 < kθ < 180°}` (positive multiples of `θ` below `180°`)
and `S_θ = {(A,B,C) : no angle lies in B_θ}` (the "safe" / `B_θ`-free region).
Note `180° ∉ B_θ` (strict upper bound): when `180/θ = n ∈ ℤ`, `B_θ = {θ,2θ,…,(n−1)θ}`.

---

### direct-four-case-interval : new
Target: the full characterization (both directions), via the canonical direct proof.
Technique: casework (four-term closure) for necessity + induction on the multiple-index
(Lemma R) plus an interval-contains-integer forcing move (Lemma F) for sufficiency.
Skeleton:
  1. State the one-move transition `T1=(A,γ,180−A−γ)`, `T2=(B,C−γ,A+γ)`, `p1+p2=180`. — by the supplementary-angle fact (geometry: angles at a point on a line).
  2. (Necessity, closure of `S_θ` when `180/θ ∉ ℤ`.) Take a `B_θ`-free triple `(A,B,C)`. Suppose Mulan cuts at vertex `C` with `γ` and BOTH children leave `S_θ` (each acquires a `B_θ`-angle). Since `B` is not in `B_θ`, child2's bad angle is `A−γ` or `B+γ`; since `A` is not in `B_θ`, child1's bad angle is `γ` or `A+C−γ`. Four cases on which of `γ`, `A+C−γ` (=p1) and `A−γ`, `B+γ` (=p2) are multiples of `θ`:
     (i) `γ=k₁θ ∧ A−γ=k₂θ` ⟹ `A=(k₁+k₂)θ ∈ B_θ`, contradiction.
     (ii) `γ=k₁θ ∧ B+γ=k₂θ` ⟹ `B=(k₂−k₁)θ ∈ B_θ`, contradiction.
     (iii) `A+C−γ=k₁θ ∧ A−γ=k₂θ` ⟹ subtract: `C=(k₁−k₂)θ ∈ B_θ`, contradiction.
     (iv) `A+C−γ=k₁θ ∧ B+γ=k₂θ` ⟹ add: `A+B+C=180=(k₁+k₂)θ` ⟹ `180/θ ∈ ℤ`. — by casework on the four linear combinations of `γ`; the contradictions are the four-case closure.
  3. (Necessity, nonempty `S_θ` + escape.) When `180/θ ∉ ℤ`, the equilateral `(60,60,60)` is `B_θ`-free: `60=kθ ⟹ θ=60/k ⟹ 180/θ=3k ∈ ℤ`, contradiction. So `60 ∉ B_θ`. By step 2 every cut from a `B_θ`-free triple leaves at least one `B_θ`-free child; Shan-Yu opens equilateral and always keeps a `B_θ`-free child, so `θ` (and every multiple) never appears. Mulan loses. — by invariant preservation of `S_θ` (Invariants & monovariants KB).
  4. (Sufficiency, base / `n=2`.) If `θ=90°` (`n=2`): from any non-right triangle, split the largest angle `C`; the two smaller angles `A,B` satisfy `A,B<90°` (at most one angle `≥90`, and it is the largest). Set `γ=90−A ∈ (0,C)` (since `A<90` and `A+C=180−B>90`). Then `p1=p2=90`: both children contain `90°`, forced one-move win. — by the supplementary fact + the "at most one angle > 90°" triangle fact.
  5. (Sufficiency, reduce a multiple — Lemma R, for `n≥3`.) If a triple has an angle `= mθ` (`2≤m≤n−1`) at vertex `C`, Mulan sets `γ=θ` (valid: `θ<mθ=C`). Child1 `=(A,θ,180−A−θ)` contains `θ` (win if kept). Child2 `=(B,(m−1)θ,A+θ)` contains `(m−1)θ`. Shan-Yu must keep child2 to survive, reducing the multiple `mθ → (m−1)θ`. Induct on `m`; base `m=1` is an immediate win (the triple already contains `θ`). So a triple carrying an `mθ`-angle is a win in `≤ m−1 ≤ n−2` further moves. Verify child2's three angles stay positive: `(m−1)θ>0` (since `m≥2`), `A+θ<180` (since `A<180−θ` as `A` is a non-`θ`-adjacent angle… check `A+θ<180 ⟺ A<180−θ`, true because `A < A+B+C−θ = 180−θ` when `B+C>θ`, which holds as `B,C>0` and one of them `≥ mθ≥2θ>θ`... verify carefully). — by induction on the integer `m` (Induction KB).
  6. (Sufficiency, reach a multiple from anywhere — Lemma F, for `n≥3`.) From a triple with NO `B_θ`-angle, split the largest angle `C`. Then `C≥60°` (largest angle) and `θ=180/n≤60°` (since `n≥3`); `C` is not a multiple of `θ` and `C≥θ`, hence `C>θ`, so `C/θ>1`. The open interval `(A/θ,(A+C)/θ)` has length `C/θ>1`, hence contains an integer `k` strictly inside. Set `γ=kθ−A ∈ (0,C)` (strict). Then `p2=A+γ=kθ` and `p1=180−kθ=(n−k)θ`. Bounds: `k>A/θ≥0 ⟹ k≥1`; `k<(A+C)/θ=(180−B)/θ=n−B/θ<n ⟹ k≤n−1`, so both `p1,p2` are positive multiples of `θ`. Both children carry a `B_θ`-angle; by Lemma R both are wins. So Mulan wins in `≤ 1+(n−2)=n−1` moves total. — by "an open interval of length `>1` contains an integer" (Pigeonhole/extremal KB).
  7. Combine: `180/θ∈ℤ` (steps 4–6) ⟹ Mulan wins from every opening in `≤ n−1` moves; `180/θ∉ℤ` (steps 2–3) ⟹ Shan-Yu escapes. State the answer `{180°/n : n≥2}`. — by the dichotomy.
Key lemmas (claim + one-line mechanism):
  - Lemma R (reduce `mθ` to `(m−1)θ`): cuts the `mθ`-angle at `γ=θ`, child1 already has `θ`, child2 inherits `(m−1)θ` — mechanism: `mθ−θ=(m−1)θ` arithmetic, induction on `m`.
  - Lemma F (reach a multiple from a generic triple): split the largest angle so `C/θ>1`, the interval `(A/θ,(A+C)/θ)` of length `>1` contains an integer `k`, both `P`-angles become multiples — mechanism: supplementary `P`-angles sum to `180=nθ` so both are multiples of `θ`.
  - Four-case closure: both children leaving `S_θ` forces one of `A,B,C,180` to be a multiple; in `S_θ` the first three are excluded, leaving only `180` — mechanism: the four linear combinations of `γ` telescope to `A`, `B`, `C`, `180`.
  - Equilateral is `B_θ`-free in all escape cases: `60∈B_θ ⟺ 180/θ∈ℤ` — mechanism: `60=kθ ⟺ 180/θ=3k`.
Open gaps (builder fills):
  - Step 5: rigorous positivity check for child2's third angle `A+θ` at EVERY induction step (not just the first), especially when `m=n−1`; confirm the `mθ`-angle always remains a clean splittable angle of the kept child (Shan-Yu could in principle keep a child where the multiple sits as a `P`-angle rather than an inherited vertex angle — verify Lemma R's induction is robust to which child carries the multiple).
  - Step 6: confirm `k` strictly inside the OPEN interval gives `γ∈(0,C)` STRICT (cut is non-degenerate, `P` not a vertex) and that `p1=(n−k)θ` is strictly positive (`n−k≥1`, shown) and `<180` (`k≥1`, shown). Handle the boundary where `A/θ` or `(A+C)/θ` is itself an integer (the strict-inequality formulation excludes endpoints, but state it).
  - Step 5/6 interface: after Lemma F's move, the kept child carries an `mθ`-angle where `m` could be `k` or `n−k`; Lemma R must apply to whichever Shan-Yu picks — confirm Lemma R covers all `m∈{1,…,n−1}`.
  - Step 4 (`n=2`): verify the "split the largest angle gives both smaller angles `<90°`" claim for obtuse AND acute non-right triangles; rule out the right-triangle opening (already a win, trivial).
Cases to cover: `n=2` (`θ=90`, special move, step 4); `n≥3` (interval lemma, steps 5–6); `θ>90°` (falls under necessity, `180/θ<2` non-integer, equilateral safe); irrational `180/θ` and rational-non-`1/n` `180/θ` (both covered uniformly by the four-case closure — no separate handling needed, but state this uniformity explicitly).
Watch out for:
  - The single-gap trap: this approach's sufficiency rests on the interval lemma + Lemma R induction. If the induction has a hidden flaw (e.g. the multiple migrates to a `P`-angle where `γ=θ` is not a valid cut), the whole sufficiency collapses. The builder must trace the multiple's LOCATION through the induction, not just its value.
  - Do NOT frame the winning region as merely `{triples containing θ}` — the closure is on the full ladder `B_θ`, and the induction climbs down the ladder. (Recorded dead-end warning from the explorer.)
  - `180°` is NOT in `B_θ` (strict). Use this consistently or the `n∈ℤ` win case breaks.

---

### attractor-level-fixpoint : new
Target: the full characterization, packaged as a game-theoretic least/greatest-fixed-point duality with an explicit finite move bound and a determinacy (no-draw) clause.
Technique: attractor / winning-region recursion (games-and-strategy KB, `aimo-0225` analogue) — define `W` as the least fixed point of "contains `θ` OR `∃` cut with both children in `W`", stratify by level `W_k`, prove `W = everything` iff `180/θ∈ℤ`; the complement `S` is the greatest fixed point, shown to be `B_θ`-free triples by the same four-case algebra. The distinctive contribution is the logical structure (complementarity, finite rank) rather than new algebra.
Skeleton:
  1. Define the state space `X = {(A,B,C) : A,B,C>0, A+B+C=180}` (open 2-simplex). Define `W₀ = {triples with an angle `=θ`}` and `W_{k+1} = W_k ∪ {T ∈ X : ∃ cut of T with both children in W_k}`. Set `W = ⋃_{k≥0} W_k` (least fixed point of the "can force a win in `≤k` moves" operator). `T ∈ W_k` ⟺ Mulan can force a win from `T` in `≤k` moves regardless of Shan-Yu.
  2. Define `S` = greatest fixed point of "avoids `θ` AND every cut has some child in `S`" (the Shan-Yu-safe region). Standard reachability-game duality: `W` and `S` are complements in `X` (a state is either winning-for-Mulan or safe-for-Shan-Yu — no draw). Cite the games-and-strategy / fixed-point duality (the game is an open reachability game; determinacy holds by transfinite back-and-forth, and here the iteration stabilizes at a low stage). — by game determinacy (the "no middle ground" lemma).
  3. (Necessity: `S = B_θ`-free triples when `180/θ∉ℤ`.) Show `S ⊇ B_θ`-free and `S ⊆ B_θ`-free. (⊇) `B_θ`-free triples avoid `θ`; the four-case closure (same algebra as direct approach step 2) shows every cut from a `B_θ`-free triple has a `B_θ`-free child, so `B_θ`-free ⊆ `S`. (⊆) If a triple has a `B_θ`-angle, it is not in `S` (it either already contains `θ`, or contains a higher multiple and is reachable-down by Lemma R, so Mulan forces). So `S = B_θ`-free, nonempty (equilateral) when `180/θ∉ℤ`, and `S=∅` when `180/θ∈ℤ` (then `180∈`-multiple makes the closure fail). — by the four-case closure + equilateral witness.
  4. (Sufficiency: `W = X` when `180/θ∈ℤ`, with explicit level bound.) Prove `W_k ⊇ {triples whose minimal multiple-index `≤ k`}` (Lemma R packaged: an `mθ`-angle triple lies in `W_{m−1}`), and `W_1 ⊇ {triples carrying a `B_θ`-angle}` (a one-move forcing move — Lemma F — puts any generic triple into `W_1`... actually Lemma F puts both children into `B_θ`-bearing, i.e. into `W_{n−2}` by Lemma R; so a generic triple lies in `W_{1+(n−2)}=W_{n−1}`). Conclude `W_{n−1}=X`: every triple is winning in `≤n−1` moves. The `n=2` base uses the special `γ=90−A` move (both children get `90°`, so `W_1=X`). — by induction on the level / multiple-index.
  5. Combine via duality (step 2): `180/θ∈ℤ ⟹ S=∅ ⟹ W=X` (Mulan wins everywhere, finitely); `180/θ∉ℤ ⟹ S≠∅` (equilateral) `⟹ W≠X`, and Shan-Yu opens in `S` to escape. State the answer. — by the complementarity `W∪S=X, W∩S=∅`.
Key lemmas (claim + one-line mechanism):
  - Least/greatest fixed-point complementarity: `W` (Mulan's attractor) and `S` (Shan-Yu's greatest safe set) partition `X` — mechanism: reachability-game determinacy (no draw possible because the target is closed and moves are continuous, so the transfinite iteration stabilizes and covers every state).
  - Level bound `W_{n−1}=X` when `180/θ∈ℤ` — mechanism: Lemma F forces into `B_θ`-bearing in one move (cost 1), Lemma R reduces the multiple-index `m→m−1` per move (cost `≤m−1≤n−2`), total `≤n−1`.
  - `S = B_θ`-free (the four-case closure, restated as a fixed-point characterization) — mechanism: same four linear combinations of `γ`.
Open gaps (builder fills):
  - Step 2 (HARD STEP, expected hardest): write the determinacy / no-draw argument cleanly for this specific (uncountable) state space. Reachability games on uncountable spaces need transfinite ordinal iteration; the builder must show it stabilizes at a COUNTABLE stage here (because `W` is reached by the concrete level stratification in step 4, giving a countable `n−1` bound, and `S` is the explicit `B_θ`-free set). Concretely: prove `W_{n−1}=X` (step 4) makes the transfinite attractor collapse at stage `ω` (inde at finite stage `n−1`), and `S` is exactly its complement — so no state is left undetermined. This is the distinctive hard gap of this framing; the direct approach sidesteps it by giving explicit strategies for both sides.
  - Step 4: re-verify Lemma R and Lemma F hold (same gaps as the direct approach — positivity of induction children, strict interval containment). This approach reuses that algebra; if the direct approach's induction has a flaw, this one inherits it (shared-gap risk — but the logical packaging is distinct, so the approaches are not single-gap-duplicates: their distinct hard gap is the determinacy argument).
  - Step 3 (⊆): make rigorous that a `B_θ`-bearing triple is not in `S` — needs Lemma R (a higher multiple is reducible, so Mulan forces), i.e. the "reachability down the ladder" claim. Prove the ladder is well-founded (indices decrease strictly).
Cases to cover: same `n=2` vs `n≥3` split for the sufficiency engine; necessity uniform via four-case (state the uniformity).
Watch out for:
  - The determinacy argument is the load-bearing distinctive step; if the state space's uncountability blocks a clean complementarity statement, this framing fails where the direct one succeeds. Have a fallback: the explicit strategies (direct approach) already give a constructive partition, so determinacy can be deduced from "explicit Mulan strategy + explicit Shan-Yu strategy cover all cases" rather than from transfixed game theory.
  - Do not let `W_k` be mis-defined as merely `{contains θ}`-closure-in-one-step; the levels must accumulate via the "BOTH children in `W_{k−1}`" operator or the rank bound is wrong.

---

### chip-transfer-monovariant : new
Target: the full characterization, via a number-theoretic / Euclidean-descent route: rescale to `q_i = (angle_i)/θ` (sum `= n` when `180/θ = n ∈ ℤ`) and seek a strictly-decreasing real-valued monovariant under the forced chip-transfer `(q_A,q_B,q_C)→(q_C,q_A−1,q_B+1)` (Mulan's `t=1` forcing move), proving termination at a coordinate `=1` (i.e. an angle `=θ`).
Technique: invariants & monovariants + Euclidean-descent (aimo-0440 USAMO 2008 analogue — subtract-preserves-lattice + `L1`-monovariant → reach zero; ADAPT, do not cite); necessity via Kronecker/Weyl density (irrational `θ/180`) + explicit periodic orbit (rational non-`1/n`).
Skeleton:
  1. Rescale: `q_i = (angle_i)/θ`; the angle-sum becomes `q_A+q_B+q_C = N := 180/θ` (a real `>1`). An angle `=θ` ⟺ some `q_i = 1`. Mulan wins iff she can force a coordinate to `1`. — by change of variables (Pólya: substitute).
  2. (Sufficiency, when `N=n∈ℤ`.) The four quantities `(A,B,C,180°)` satisfy the integer linear relation `q_A+q_B+q_C = n` (integer). Mulan's forcing move `t=1` (cut parameter `γ=θ`): whenever a coordinate `q_A>1`, child1 contains `θ` (`q=1`), so Shan-Yu is forced to keep child2 `=(q_C, q_A−1, q_B+1)`. Net transition `(q_A,q_B,q_C)⟼(q_C,q_A−1,q_B+1)` — a "transfer 1 from coordinate `A` to coordinate `B`", sum `n` conserved, valid while the cut coordinate exceeds `1`. — by the supplementary-`P`-angle fact + integer relation.
  3. (HARD STEP — the monovariant.) Find a real-valued `Φ(q_A,q_B,q_C) ≥ 0` that STRICTLY decreases under the transfer and is bounded below, so the process terminates (and termination forces a coordinate to hit `1`, since the only obstruction to continuing is all coordinates `≤1`, which with integer sum `n≥2` forces some coordinate `=1`). Candidate potentials to test: `Σ{q_i}` (sum of fractional parts — invariant under transfer, NOT decreasing — rules out); `Σ q_i²` (Δ`=2(q_B−q_A)+2`, sign indeterminate — rules out); `max q_i − min q_i` (spread); `Σ |q_i − n/3|`; the number of coordinates `∉ [1,?]`. The honest gap: the reduction explorer could not exhibit a working monovariant for the transfer op (unlike aimo-0440's subtract op). The builder must either FIND one, or fall back to the interval lemma (Lemma F of the direct approach) which does not need a monovariant — in which case this approach converges to the direct one. — by monovariant descent (Invariants & monovariants KB; aimo-0440 L1-coefficient principle adapted).
  4. (Sufficiency, fallback / co-engine.) If step 3's monovariant is not found, use the interval lemma directly in `q`-space: from a generic triple split the largest coordinate `q_C>1` (since `q_C≥N/3=n/3≥1`, and `q_C≠1` so `q_C>1`); the interval `(q_A, q_A+q_C)` of length `q_C>1` contains an integer `k`, set `t=k−q_A`, both `P`-coordinates `q_A+t=k`, `N−(q_A+t)=n−k` are integers in `{1,…,n−1}`; both children carry an integer coordinate, and the induction (Lemma R in `q`-space: `m→m−1`) drives a coordinate to `1`. — by "open interval of length `>1` contains an integer" + induction.
  5. (Necessity, irrational `N`.) If `180/θ` is irrational, `θ/180` irrational. Exhibit a Shan-Yu escape via Kronecker/Weyl: maintain a triple whose three fractional parts `{q_i}` (mod 1) all stay bounded away from `0` (so no coordinate is an integer, in particular none `=1`). Under a cut, the new `q`-coordinates are `t, N−q_A−t, q_A−t, q_B+t`; by choosing `t` Mulan perturbs fractional parts, but Shan-Yu's keep-selects among two children — show (via density of the rotation `t↦t+1` mod the pair-sum, or directly via the four-case closure) that some child maintains all fractional parts nonzero. Honest note: the four-case closure (direct approach) already proves this uniformly for ALL non-integer `N` without a Kronecker sub-case; the Kronecker route is a genuinely different mathematical home but is HEAVIER and splits into sub-cases. — by Kronecker/Weyl equidistribution (KB) OR the four-case closure as fallback.
  6. (Necessity, rational non-`1/n` `N=p/q`, `q≥2`.) E.g. `θ=72°` (`N=5/2`). Exhibit an explicit Shan-Yu periodic escape (the reduction explorer flagged a `t=1` cycle for `θ=72°` from the equilateral). Prove the equilateral orbit under Mulan's best play is periodic and avoids coordinate `=1`. Again, the four-case closure covers this uniformly; the explicit-cycle route is the distinctively number-theoretic alternative. — by explicit orbit construction + the four-case closure as safety net.
  7. Combine: `N∈ℤ` (steps 2–4) ⟹ win; `N∉ℤ` (steps 5–6, or uniformly the four-case closure) ⟹ escape. State the answer.
Key lemmas (claim + one-line mechanism):
  - (Conjectured, UNPROVEN) Existence of a strict monovariant for the transfer `(q_A,q_B,q_C)→(q_C,q_A−1,q_B+1)` — mechanism: NONE YET IDENTIFIED; this is the approach's defining hard gap. The integer-sum invariant alone does not give descent (it is conserved).
  - (Fallback) Interval lemma in `q`-space: the interval `(q_A, q_A+q_C)` of length `q_C>1` contains an integer — mechanism: `q_C≥n/3≥1` and `q_C≠1` ⟹ `q_C>1`.
  - Necessity (irrational): Kronecker density keeps fractional parts off `0` — mechanism: irrational rotations have dense orbits, so Mulan cannot pin a coordinate to exactly `1`.
  - Necessity (rational non-1/n): explicit periodic orbit — mechanism: finite orbit of the equilateral under the transfer avoids coordinate `1`.
Open gaps (builder fills):
  - Step 3 (HARD STEP, expected hardest of the WHOLE FIELD): FIND the monovariant, or PROVE none exists for the transfer op (which would force the fallback). This is the genuinely different engine attempt; if it succeeds, it gives a cleaner bound than the interval lemma; if it fails, the approach reduces to the direct one.
  - Step 5: the Kronecker escape for irrational `N` must be made rigorous (show Shan-Yu has a REPLY keeping fractional parts nonzero, not just that Mulan cannot pin — the four-case closure gives the reply directly; the Kronecker route must reconstruct it).
  - Step 6: verify the explicit periodic orbit for `θ=72°` (and general `N=p/q`) actually avoids coordinate `=1` under ALL of Mulan's moves (not just the `t=1` greedy — Mulan may play any `t`). This is the same hard sub-case the reduction explorer left UNRESOLVED; the four-case closure resolves it, but the pure-orbit route must too.
Cases to cover: `N` irrational (step 5); `N=p/q` rational non-integer (step 6); `N=n∈ℤ` (steps 2–4); `n=2` within step 4 (interval lemma with `n=2` needs the special move since `q_C` may be `<1`... actually for `n=2`, `q_i` sum to 2, largest `q_C≥2/3`; but `q_C>1` is NOT guaranteed — so the `n=2` special move `γ=90−A` is needed here too).
Watch out for:
  - The single-gap trap (SHARED with direct approach): if step 3 fails and the approach falls back to the interval lemma (step 4), it becomes a packaging variant of `direct-four-case-interval`. The builder must either find the monovariant (keeping the approach distinct) or honestly mark the approach as converging to the direct proof. Do NOT pretend a failed monovariant is a different proof.
  - The `θ=72°` (and all `N=p/q`) sub-case is the reduction explorer's flagged "decisive test case": the pure `t=1` greedy CYCLES and does not win. The answer (escape) is correct, but the pure-orbit necessity proof must handle Mulan's non-`t=1` moves too. If it cannot, fall back to the four-case closure.
  - Generic triangles have REAL `q_i` (not integer), so there is no lattice to descend on directly — the monovariant must be real-valued, which is why the aim o-0440 integer-coefficient `L1` norm does not transfer verbatim.

---

### modular-residue-orbit : new
Target: the full characterization, with the NECESSITY direction carried by a modular-residue / rotation-orbit argument (a different mathematical home from the four-case casework) and the SUFFICIENCY direction by the interval lemma.
Technique: reformulate `B_θ`-freeness as "all angle-residues mod `θ` are nonzero" and analyze the orbit of the residue triple under cuts; necessity via the invariant "the total residue `180 mod θ` is nonzero when `180/θ∉ℤ`" plus the four-case closure restated in modular language (the cut permutes/redistributes residues but cannot drive all to zero); sufficiency via the interval lemma. Distinctive for the one-line modular punchline on necessity.
Skeleton:
  1. Work in the circle group `G = ℝ/θℤ`. The residue of an angle `α` is `ρ(α) = α mod θ ∈ [0,θ)`. An angle is a positive multiple of `θ` below `180` iff its residue is `0` (and `0<α<180`). The total: `ρ(A)+ρ(B)+ρ(C) ≡ A+B+C = 180 (mod θ)`. — by modular arithmetic (KB).
  2. (Necessity invariant.) When `180/θ ∉ ℤ`, the total residue `180 mod θ ≠ 0` is a FIXED nonzero value. Claim: the set `{(A,B,C) : ρ(A),ρ(B),ρ(C) all nonzero}` is Shan-Yu-closed. — by the invariant "total residue `≠ 0`" (Invariants KB).
  3. (HARD STEP — closure in modular language.) PROVE the claim of step 2: under any Mulan cut from a triple with all residues nonzero, at least one child keeps all residues nonzero. The one-line invariant "total residue `≠0`" ALONE does NOT suffice (one residue could be `0` while the others sum to the nonzero total), so the builder must re-derive the four-term closure in modular form: if both children had a zero-residue angle, the four linear combinations of `γ` (exactly as in the direct approach) force `ρ(A)=0` or `ρ(B)=0` or `ρ(C)=0` or `ρ(180)=0`; in `S_θ` the first three are excluded, leaving `ρ(180)=0` i.e. `180/θ∈ℤ`. So the modular framing REQUIRES the four-case algebra — it is NOT an independent engine, but a reformulation that makes the punchline "`180 mod θ ≠ 0` ⇒ `θ` never appears" one line once the closure is established. — by casework on residues (four linear combinations of `γ`, restated mod `θ`).
  4. (Necessity, nonempty + escape.) Equilateral `(60,60,60)`: `ρ(60)≠0` when `180/θ∉ℤ` (as `60∈θℤ ⟺ 180/θ∈ℤ`). So all three residues nonzero; by step 3 closure, Shan-Yu keeps a no-zero-residue child forever; `θ` (zero residue) never appears. — by the modular closure + equilateral witness.
  5. (Sufficiency, `180/θ=n∈ℤ`.) When `180 mod θ = 0`, the total residue is `0`, the invariant dies, and Mulan forces. Use the interval lemma (split largest angle `C`, interval `(A/θ,(A+C)/θ)` of length `C/θ>1` contains integer `k`, both `P`-angles `kθ,(n−k)θ`), then Lemma R (induction `m→m−1`). `n=2` special move `γ=90−A`. — by the interval-contains-integer + induction (same engine as direct approach, restated).
  6. Combine and state the answer `{180°/n : n≥2}`. — by the dichotomy `ρ(180)=0` vs `≠0`.
Key lemmas (claim + one-line mechanism):
  - Modular closure: a cut from an all-nonzero-residue triple leaves an all-nonzero-residue child unless `ρ(180)=0` — mechanism: the four linear combinations of `γ` mod `θ` force a parent residue (or `180`'s residue) to vanish.
  - Equilateral residue nonzero: `ρ(60)≠0 ⟺ 180/θ∉ℤ` — mechanism: `60∈θℤ ⟺ 180/θ=3k∈ℤ`.
  - Interval lemma (sufficiency) — mechanism: `C/θ>1` ⇒ open interval of length `>1` contains an integer.
Open gaps (builder fills):
  - Step 3 (HARD STEP): the modular framing's closure IS the four-case algebra; the builder must decide whether the modular language adds rigor/clarity or is merely a restatement. If it is merely a restatement, this approach is a packaging variant of `direct-four-case-interval` for necessity (shared-gap risk). The genuinely different contribution is only the one-line "total residue `≠0`" summary — which, as noted, does not by itself prove closure. So this approach's distinctiveness is THIN; the builder should either find a genuine modular argument (e.g. a residue-orbit dynamics argument that avoids the four-case casework) or honestly mark convergence.
  - Step 5: same interval-lemma + Lemma R gaps as the direct approach (positivity, strict containment).
Cases to cover: `n=2` special move (step 5); `n≥3` interval; `θ>90°` (necessity, `ρ(180)≠0`); irrational and rational-non-1/n `180/θ` (both uniformly `ρ(180)≠0`, covered by the modular closure — state the uniformity).
Watch out for:
  - THIN distinctiveness: this approach shares both the necessity algebra (four-case) and the sufficiency engine (interval lemma) with `direct-four-case-interval`. Its only claim to being a rival is the modular viewpoint. The builder must either justify it as a genuinely cleaner presentation (valuable as a cross-check / alternative writeup) or concede it is a packaging variant. Do NOT field it as independent if the modular argument reduces verbatim to the four-case.
  - The "total residue `≠0`" invariant alone is INSUFFICIENT (one residue can be `0`); do not present it as the whole proof.

---

### Field summary

Four approaches, all targeting the full characterization end to end. Framing diversity:
- `direct-four-case-interval` — canonical direct proof (casework + interval + induction). The leader; both engines numerically verified.
- `attractor-level-fixpoint` — game-theoretic fixed-point duality; distinctive hard gap is the determinacy/no-draw argument (a genuinely different logical contribution, not shared algebra).
- `chip-transfer-monovariant` — number-theoretic Euclidean-descent home (aimo-0440 analogue); distinctive hard gap is the (currently non-existent) transfer monovariant. RISKIEST; likely to converge to the direct approach if the monovariant is not found, but fields a genuinely different engine attempt.
- `modular-residue-orbit` — modular-arithmetic home for necessity; THINNEST distinctiveness (likely a packaging variant of the direct necessity), but offers a cleaner punchline and a cross-check.

Shared-gap audit (single-gap-trap check): the necessity direction has essentially ONE correct engine (the four-case closure), so `direct-four-case-interval`, `attractor-level-fixpoint` (step 3), `chip-transfer-monovariant` (fallback), and `modular-residue-orbit` (step 3) ALL use it. If the four-case closure has a hidden flaw, all four die together on necessity. Mitigation: the four-case closure is short and verified (numerically + algebraically above); the real diversity is in the SUFFICIENCY engine (direct interval lemma vs chip-transfer monovariant vs attractor level-stratification) and in the logical packaging (determinacy, modular). The `chip-transfer-monovariant` approach is the only one attempting a genuinely different sufficiency engine; if it succeeds it breaks the shared-wall risk on the sufficiency side. Recommend the builder prioritize (a) closing the direct approach's induction/interval gaps rigorously, (b) attempting the chip-transfer monovariant, and (c) writing the attractor determinacy argument — these three are where genuine new ground is possible.

build set: direct-four-case-interval, attractor-level-fixpoint, chip-transfer-monovariant, modular-residue-orbit
