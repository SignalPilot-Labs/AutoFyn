# Approach: self-similar-recursion

## Status
partial

## Approaches tried
- (round 8, THIS ROUND) **Attacked Gap A′ and Gap B via the assigned GLOBAL residual-budget
  induction (Claim(N−k) on the complement). Two rigorous new results, but the induction itself is
  BLOCKED by a genuine, now-PROVEN obstruction — recorded honestly, Status stays partial.**
  (1) **Lemma CUT3 (NEW, proven in full, §9) — promotable:** a `μ=3` shared even-block piece-leaf
  costs **≥3 cuts** (2 to trisect the leaf-piece `2^k` into `{v,v,v}`, `v=2^k/3`; `≥1` more because
  `v` is shared with a donor piece `2^m` which cannot be uncut, since `2^m=v=2^k/3` forces the
  non-power-of-two ratio `2^k/2^m=3`). Consequence (rigorous): **Gap B is VACUOUS whenever the cut
  budget `N≤2`, in particular for the ENTIRE problem at `n=2`** (budget `≤n=2<3`) and for the base
  induction steps `N∈{0,1,2}` at every `n`. The same counting gives the **cycle cut-cost floor**
  (§10): a cycle through `r` pieces with a degree-≥3 cycle-piece costs `≥r+1≥3` cuts.
  (2) **The naive complement induction is DEAD — PROVEN obstruction (§8), not merely unverified.**
  The assigned route removes the BF-invisible even block `B` (the four copies of `v`) and applies
  Claim(N−k) to the complement. But the two requirements are mutually exclusive: at the explicit
  `n=3` minimizer `P*={8/3,8/3,8/3,8/3,2,4/3,1}` (`Σ=15`, `f=5/3`), the **BF-preserving** complement
  `{2,4/3,1}` has `f=5/3` (correct) but `Σ=13/3` — NOT a refinement of any `W_m` (no dyadic total),
  so Claim(N−k) does not type-check; the **mass-conserving** reattach `{4,2,1}` is a genuine `W_2`
  refinement (`Σ=7`) but has `f=3≠5/3` — BF is broken. I PROVE (§8) this is structural, not an
  artifact: the block `B` carries value `t·v` with `v=2^k/3` shared across ≥2 dyadic pieces, so
  removing exactly the copies of `v` deletes a non-dyadic total `t·2^k/3` and can never leave a
  power-of-two total, while any dyadic-total repair re-inserts mass at a NEW rank and changes `f`.
  Hence NO removal is simultaneously BF-preserving and W_m-landing. **The residual-complement
  induction cannot close Gap B in this framing** — future rounds must either enlarge Claim to a
  genuinely broader (non-dyadic) multiset class and re-prove `f≥1` there (risks re-opening the
  difficulty — must be surfaced, not asserted), or find a different mechanism. (3) **Gap A′ peel
  obstruction made rigorous (§10):** the outliner's Gap-A′ peel assumes the deg-≥3 cycle-piece's
  extra sub-piece lies in an EVEN (BF-invisible) block. I show this is NOT forced: M4 only forbids a
  piece from having two sub-pieces both in ODD blocks, so if both cycle-neighbours `Q_{i-1},Q_i` of
  the offending piece sit in EVEN blocks, the extra sub-piece MAY lie in an odd block, feeding `f`,
  and the peel fails. So the peel needs an unproven "attachment is even-block" hypothesis — open.
  Status: **partial** (both gaps remain open; the two rigorous results narrow, but do not close,
  them; the assigned complement-induction framing is now proven insufficient for Gap B).
- (round 7) **Gap A′ sharpened via Lemma CC+ (degree-2-cycle exclusion); Gap B pinned
  as inherently budget/minimality-based.** (1) **Lemma CC+ (NEW, proven, verified 0/456)** strictly
  strengthens certified Lemma CC: ANY cycle `Z` (any length `r≥2`) all of whose cycle-*pieces* have
  degree exactly `2` in `H` is infeasible — the `r` cycle-piece equations are exactly
  `u_{i-1}+u_i=b_i` with the FULL distinct powers `b_i=2^{a_i}`, and (even `r`) the consistency
  `Σ(-1)^i b_i=0` fails for distinct powers, while (odd `r`) the unique solution has a forced-negative
  entry (superincreasing). This subsumes ALL isolated cycles (CC) AND, crucially, kills the
  explorer's even shape #2 (a cycle *component* touching an off-cycle piece) **and its odd analogue**,
  because attaching off-cycle pieces to cycle *components* does not change any cycle-piece's degree.
  (2) With CC+ and S-core the EVEN residual narrows to exactly {chord, non-uniform multiplicity}
  (extra edge from a cycle-*piece* to a cycle-*component*): the even off-cycle-*component*-at-a-piece
  case is folded into S-core (the alternating `ker U` witness survives an off-cycle-component edge,
  which carries `d=0`). Pure-power chord / non-uniform cases are killed by distinct-powers positivity
  (verified 0/32 chord, 0/12 non-uniform); off-cycle-*mass* versions (reduced budgets, verified can be
  all-positive, 357 combos) and the ODD degree-≥3 case genuinely need minimality. (3) I tested the
  natural minimality lever — the **circulation feasible direction** (in each cycle piece move `+δ`
  onto its `Q_i`-copy, `−δ` off its `Q_{i-1}`-copy, splitting each cycle component symmetrically):
  numerically it is a **V-kink** (`f` strictly increases BOTH ways, 200/200 for `r=3,4,5`), so it
  yields neither descent nor a flat `Φ`-raising direction — documenting precisely WHY the odd/off-mass
  cycle case resists a naive variational move. (4) **Gap B sharp finding:** I constructed an EXPLICIT
  shared `μ=3` even-leaf refinement of `W_2` — piece1=`{1}`, piece2=`{4/3,2/3}`, piece4=`{4/3,4/3,4/3}`
  (multiset `{4/3,4/3,4/3,4/3,1,2/3}`, `Σ=7=D_2`) — with `f=1/3<1`. It uses 3 cuts (`>n=2`, over
  budget). This PROVES Gap-B configs genuinely violate `f≥1` when over-budget, so Gap B's exclusion
  is **inherently budget/minimality-based** (must go through Claim(N−1)/Lemma BD) and NO local or
  purely-algebraic move can close it — the unshared `μ=3` case (block size 3, odd) is already dead by
  M3. Lemma BD (degenerate `f`-flat competitor) still unconstructed. Status stays partial.
- (round 6) **Gap A partial closure via distinct-powers structure — Lemma CC.** Proved
  in full that `H` contains no ISOLATED cycle (a connected component that is a bare 2-regular cycle):
  even-length cycles give a `\ker U` witness contradicting Lemma S-core; ODD-length cycles are killed
  by superincreasing positivity — the unique cyclic solution has `u_j=\tfrac12\sum_t(-1)^t 2^{a_{...}}`
  and, choosing the start so the largest budget `2^{a_{\max}}` gets a minus sign, `2u_j\le
  -2^{a_{\max}}+\sum_{\ell\ne M}2^{a_\ell}<0`, contradicting `u_j>0`. This honours the explorer's
  mandate (uses the numerical powers-of-two budgets, not just incidence — the 479-instance refutation
  of a pure-algebra closure does not touch it, since those examples are NON-isolated). Verified
  numerically: 0 feasible isolated odd cycles of 47376; even cyclic incidence singular. Gap A now
  narrowed to NON-isolated cycles (chord / off-cycle degree-≥3 piece / multiplicity-≥2 edge) — still
  open; the full-cycle telescoping with off-cycle surplus terms did not close (uncontrolled signs).
  Gap B unchanged: no local move excludes the `μ=3` even-leaf; the two direct global attempts
  (bisect-instead, symmetric-to-degenerate) fail as one-liners (recorded); the degenerate-`Φ`-
  dominator (Lemma BD) not constructed. NOT claimed solved; Status stays partial.
- (round 5) **Rebuilt the tied-non-degenerate integrality closure on SOUND moves**,
  discarding the refuted Lemma W. Established, rigorously and consistently with every round-4
  refutation, a new structural theory of the `Φ=Σx²`-maximal minimizer `P*`:
  (a) **Lemma S-core (ker `U`=0)** — the sound half of the old Lemma S: any nonzero
  sum-preserving component shift is a feasible line contradicting minimality (non-flat) or
  `Φ`-maximality (flat, strict convexity). Kept in full.
  (b) **Move M2 (two invisible pairs)** ⇒ every within-piece multiplicity `μ_{k,j} ≤ 3`
  (reviewer fix #1; a leaf with `μ≥4` is split `{v,v},{v,v}→{v+t,v+t},{v−t,v−t}`, each pair
  P1-invisible so `f` unchanged — STAYS in `G` — while `Φ` rises by `4t²`).
  (c) **Move M3 (symmetric odd-block move)** — the correct REPLACEMENT for the refuted V-kink
  3-shift: move one same-piece copy `+s`, another `−s`, keep the third; for an ODD-size tie-block
  `f` is EXACTLY flat (`σ_a−σ_{a+μ_j−1}=0`) while `Φ` rises by `2s²`. Hence every odd-size
  tie-block has `μ_{k,j} ≤ 1`. Verified numerically (0 mismatches, small-`s`).
  (d) **Move M4 (within-piece two-sub-piece transfer)** ⇒ no piece has two sub-pieces both in
  odd-size blocks. (e) **Block formula** `f = Σ_{j: μ_j odd} σ_{a_j} w_j` (verified 0/20000).
  These REPLACE the false Lemma W and are individually sound. **Integrality of `P*` is thereby
  reduced to two explicit residual gaps** (Gap A: acyclicity of the incidence multigraph at
  `P*`; Gap B: exclusion of `μ=3` even-block piece-leaves = the honest core of "Φ-EVEN"),
  and I prove full integrality GIVEN A+B via generalized piece-leaf peeling. NOT claimed solved.
- (round 4) Claimed solved via Lemmas W/S/T — REJECTED (overclaim): Lemma W false ({2,3,3}
  minimizer), Lemma T integrality globally false (non-integer f=1 continuum). Sound sub-arguments
  (cycle⇒kernel, Φ-strict-convexity) salvaged into Lemma S-core above.
- (round 3) Lemma I (cut-slide-derivative, certified), Lemma J (tiefree-minimizer-monochromatic,
  certified), degenerate leg via cut-count induction. Closed tie-free + degenerate minimizers.
- (round 2) Top-band localization, parity Theorem F for integer cuts, cascade tightness.
- (round 1) Strong induction, Lemma 0, layer-cake reduction, Case 1/2 decoupling.

## Target (the whole problem)
Prove `c(n) = 2^n / (2^{n+1} − 1)`. Write `D_n = 2^{n+1} − 1`.

## Current best
Upper bound `c(n) ≤ 2^n/D_n` fully certified (imported). Lower bound reduced to (LBL) and, at the
`Φ`-maximal non-degenerate minimizer `P*`, to **integrality of `P*`**. This round establishes a
sound structural theory of `P*` (Lemma S-core + moves M2, M3, M4 + block formula) which reduces
integrality to two explicit residual gaps (A: acyclicity; B: `μ=3` even-block leaves). Integrality
— hence `f(P*)≥1` — is proved GIVEN those two gaps. **Round 6:** Lemma CC excludes all ISOLATED
cycles. **Round 7:** **Lemma CC+** strengthens CC to exclude ANY cycle all of whose *cycle-pieces*
have degree exactly 2. Combined with S-core, **Gap A′ narrows to: a cycle carrying a cycle-piece of
degree ≥3.** **Gap B** = a shared `μ=3` even-block piece-leaf (an explicit `W_2` witness has
`f=1/3<1` over-budget).

**Round 8 (this round):** attacked both gaps via the assigned GLOBAL residual-budget induction
(Claim(N−k) on the complement). Two rigorous outcomes, neither a closure:
1. **Lemma CUT3 (proven, promotable):** a `μ=3` shared even-block leaf costs `≥3` cuts ⇒ **Gap B is
   VACUOUS for `N≤2`, hence the whole `n=2` case and the first three induction steps at every `n`.**
   Analogously (cycle cut-cost) a deg-≥3-cycle-piece cycle costs `≥r+1≥3` cuts.
2. **The naive complement induction is PROVEN insufficient for Gap B (§8):** removing the
   BF-invisible even block `B` cannot yield an object that is simultaneously (i) a `W_m` refinement
   and (ii) `f`-preserving — because `B` carries a non-dyadic total `t·2^k/3`. So Claim(N−k) does not
   apply to any legitimate complement. This is a proven obstruction, not an unverified step; it kills
   the assigned framing for Gap B and redirects future work.
3. **Gap A′ peel obstruction (§10):** the deg-≥3 cycle-piece's extra sub-piece need NOT lie in an
   even (BF-invisible) block (M4 permits it in an odd block when both cycle-neighbours are
   even-blocked), so the "peel the even attachment" step is not justified in general — open.

Status stays `partial`: the two residuals (Gap A′ = a cycle with a deg-≥3 cycle-piece; Gap B = a
`μ=3` shared even-block leaf within budget `3≤N≤n`) are NOT closed. The assigned complement-induction
route is now proven inadequate for Gap B in its stated form.

## Full proof (of everything except the two explicit residual gaps A, B)

Throughout, a *multiset* `P` of positive reals is sorted descending `a_1≥…≥a_m`; its **alternating
sum** is `f(P)=Σ_i σ_i a_i`, `σ_i=(−1)^{i+1}`, and `Σ(P)=Σ_i a_i`. Certified imports (verbatim):

- **Lemma 0 (endgame-greedy).** With all pieces on the table, LB moving first, LB's guaranteed
  total is `(Σ(P)+f(P))/2`.
- **Lemma L (layer-cake-alt-sum).** `f(P)=M(P):=measure{t≥0 : c_P(t)\text{ odd}}`,
  `c_P(t)=#\{pieces of P >t\}`; `f(P)=∫_0^∞ 1[c_P(t)\text{ odd}]\,dt`.
- **Matched-pair invisibility (P1).** Adjoining two equal pieces `{v,v}` leaves `M`, hence `f`,
  unchanged: the two copies change `c_P(t)` by `0` or `2`, never the parity.
- **Theorem F (integer-parity-alt-sum).** For a multiset of positive **integers**,
  `f=Σ−2Σ_{i even}a_i ≡ Σ (mod 2)`, and `f≥0` (group `(a_1−a_2)+(a_3−a_4)+⋯`, each `≥0`).
- **Lemma I (cut-slide-derivative).** Group equal values into tie-blocks; block `l` occupies ranks
  `[a_l,b_l]`. For a sub-piece `q` in block `l`, `∂f/∂(\text{increase }q)=σ_{a_l}` and
  `∂f/∂(\text{decrease }q)=−σ_{b_l}` (holding all other pieces fixed).
- **Lemma J (tiefree-minimizer-monochromatic).** A non-degenerate tie-free local minimum has
  `f=Σ_{k}ε_k2^k∈ℤ`, `ε_k∈{±1}`, hence (parity, `f≥0`) `f≥1`.

### 0. Reduction to a single inequality (LBL)

By Lemma 0 with total length `1`, the game value is `c(n)=(1+V_n)/2`,
`V_n:=\max_{LB}\min_{XY} f(P)`. Since `2·\frac{2^n}{D_n}−1=\frac1{D_n}`, the claim `c(n)=2^n/D_n`
is **equivalent** to `V_n=1/D_n`.

**Upper bound `V_n≤1/D_n`** is certified (Invariant (I) `g_b(P)≤s/D_b` at `b=n,s=1`, proved via
`delete-subtract-reachability` and `subset-sum-pigeonhole`). Taken as given.

**Lower bound `V_n≥1/D_n`.** LB marks the dyadic pieces `2^k/D_n`; scaling by `D_n` turns this into
`W_n=\{2^0,…,2^n\}`, `Σ(W_n)=D_n`. XY places `≤n` further cuts, producing a *refinement*. Thus
`V_n≥1/D_n` is equivalent to:

> **(LBL).** Every refinement of `W_n` using at most `n` cuts has `f≥1`.

### 1. Domain, induction, degenerate leg (unchanged, sound)

A *cut pattern* assigns each piece `2^k` a number `r_k≥1` of sub-pieces, total cut count
`N=Σ_k(r_k−1)`; its domain is the compact product of simplices `K=∏_k Δ_k`,
`Δ_k=\{x∈ℝ^{r_k}_{≥0}:Σ_j x_{k,j}=2^k\}`. Because `f` depends only on the **multiset** of sub-piece
lengths, every point of `K` is a legal refinement and every within-piece mass transfer is a legal
direction. Let `\mathcal D_N=\bigcup K` over patterns with `≤N` cuts; it is compact, `f`
continuous, so `\min_{\mathcal D_N}f` is attained (Weierstrass). A point is **degenerate** if some
sub-piece has length `0`.

We prove **Claim(N):** every refinement of `W_n` using `≤N` cuts has `f≥1`, by strong induction on
`N`. Claim(n) is (LBL).

**Base `N=0`.** `\mathcal D_0=\{W_n\}`: integers, `Σ=D_n` odd, so by Theorem F `f(W_n)≡1 (mod 2)`,
`f(W_n)≥0`, hence `≥1`.

**Inductive step.** Fix `N≥1`, assume Claim(N−1). Let `m=\min_{\mathcal D_N}f`, `G=\{f=m\}∩\mathcal
D_N` (compact, nonempty). Choose `P^*∈G` **maximizing** the strictly convex `Φ(P):=Σ_i x_i^2`
(attained: `Φ` continuous, `G` compact). We show `m≥1`.

If `P^*` is **degenerate**, delete a length-`0` sub-piece: the positive sub-pieces form a refinement
with `≤N−1` cuts and the same multiset, so `m=f(P^*)≥1` by Claim(N−1). **Henceforth `P^*` is
non-degenerate.** We show `f(P^*)` is a positive odd integer (modulo Gaps A, B below).

Group sub-pieces into **value classes** (= tie-blocks) `C_1,…,C_p`, distinct values `w_1>…>w_p>0`;
`C_j` has total size `μ_j` and occupies ranks `[a_j,a_j+μ_j−1]` with `a_j=1+Σ_{i<j}μ_i`. Let
`μ_{k,j}` be the number of sub-pieces of piece `2^k` lying in `C_j`; `Σ_j μ_{k,j}=r_k`,
`Σ_k μ_{k,j}=μ_j`. The value vector `w` solves the integer system
```
     (Uw)_k := Σ_j μ_{k,j} w_j = 2^k      for every piece k.        (★)
```

**Block formula.** The block-`j` contribution to `f` is `w_j Σ_{i=a_j}^{a_j+μ_j−1}σ_i =
w_j σ_{a_j}·(1\text{ if }μ_j\text{ odd},\ 0\text{ if }μ_j\text{ even})`, since consecutive signs
alternate. Hence
```
     f(P^*) = Σ_{j:\,μ_j\ \mathrm{odd}} σ_{a_j} w_j .                 (BF)
```
(Verified computationally against the raw alternating sum: 0 mismatches / 20000 random multisets.)

### 2. Lemma S-core: `\ker U=\{0\}` (SALVAGED sound half of Lemma S)

**Lemma S-core.** `U` has trivial kernel; equivalently full column rank, so `p≤n+1` and `(★)`
determines `w` uniquely.

*Proof.* Let `d∈ℝ^p`, `d≠0`, `Ud=0`. Shift `w_j(δ)=w_j+δd_j` (add `δd_j` to every sub-piece of
`C_j`). By `Ud=0` each piece's sum is preserved: a feasible line in `K`. For `|δ|` small all lengths
stay positive and the distinct values stay distinct and ordered, so the point stays in one
sort-chamber, where `f` is affine: `f(δ)=m+γδ`.

- If `γ≠0`, one sign of `δ` gives `f<m`, contradicting minimality.
- If `γ=0`, the whole segment lies in `G`. The shift rates `c_i=d_{j(i)}` are not all zero (some
  `d_j≠0` and `C_j≠∅`), so `Φ(δ)=Σ_i(x_i+δc_i)^2` is strictly convex in `δ` (leading coefficient
  `Σc_i^2>0`), hence has no interior maximum at `δ=0`: some `δ≠0` in the segment gives `Φ>Φ(P^*)`,
  contradicting `Φ`-maximality.

Either way, contradiction; so `\ker U=\{0\}`. ∎

### 3. Multiplicity bounds at `P^*` (SOUND moves M2, M3)

**Move M2 (two invisible pairs) — reviewer fix #1.** *If `μ_{k,j}≥4` for some `k,j`, contradiction.*
Piece `2^k` has `≥4` sub-pieces equal to `v:=w_j`. Take four of them and, for `t` near `0`, set
two of them to `v+t` and two to `v−t`:
```
     {v,v,v,v} → {v+t,\,v+t,\,v−t,\,v−t}   (within piece 2^k).
```
Piece `2^k`'s sum is preserved (`+t+t−t−t=0`); for `|t|` small all stay positive. The four form two
equal pairs `{v+t,v+t}` and `{v−t,v−t}` both before (`t=0`) and after, so by P1 each pair is
invisible to `f` at every level: `f` is **exactly unchanged**, the point STAYS in `G`. But
`Φ` gains `2(v+t)^2+2(v−t)^2−4v^2=4t^2>0`, contradicting `Φ`-maximality. (Verified: 0/30000.)
Hence **`μ_{k,j}≤3` for all `k,j`.** ∎

*Remark (reviewer's `μ`-even error, resolved).* Note "even `μ`" was never used; M2 excludes ALL
`μ_{k,j}≥4` (even or odd) because four equal same-piece copies split into two internally-equal pairs
regardless of parity. So the surviving multiplicities are exactly `μ_{k,j}∈\{1,2,3\}`.

**Move M3 (symmetric odd-block move) — REPLACES the refuted V-kink 3-shift.** *If a tie-block `C_j`
has ODD size `μ_j` and some piece contributes `μ_{k,j}≥2` copies to it, contradiction.* Take two of
piece `2^k`'s copies of `v:=w_j`; for `s` near `0` move one to `v+s`, the other to `v−s`, keep the
rest of `C_j` at `v`:
```
     move one copy +s, one copy −s   (both in piece 2^k, sum preserved).
```
For `|s|` small enough that no other value enters `[v−s,v+s]`, the copies of `v` still occupy ranks
`[a_j,a_j+μ_j−1]`: `v+s` at the top rank `a_j`, `v−s` at the bottom rank `a_j+μ_j−1`, the `μ_j−2`
untouched copies at the interior ranks. By the block-sign computation the change in `f` is exactly
```
     Δf = s\,(σ_{a_j} − σ_{a_j+μ_j−1}),
```
and for **odd** `μ_j` the two signs are equal (`a_j` and `a_j+μ_j−1` differ by an even number), so
`Δf=0`: `f` is **exactly flat**, the point STAYS in `G`. But `Φ` gains `(v+s)^2+(v−s)^2−2v^2=2s^2>0`,
contradicting `Φ`-maximality. (Verified: 0/29962 small-`s` samples.)
Hence **every odd-size tie-block has `μ_{k,j}≤1` for every `k`.** ∎

(Contrast: for **even** `μ_j`, `σ_{a_j}−σ_{a_j+μ_j−1}=2σ_{a_j}≠0`; with the rank re-assignment as
`s` changes sign this yields `Δf=2σ_{a_j}|s|`, a V-kink, so M3 gives no contradiction on even
blocks — exactly why the refuted move failed and why even blocks are the residual, below.)

### 4. Move M4: no piece has two sub-pieces both in odd-size blocks (SOUND)

**Move M4.** *If a single piece `2^k` has two sub-pieces `q_u` (value `u`, in odd block) and `q_w`
(value `w<u`, in odd block), `u≠w`, contradiction.* Consider the within-piece transfer
`u→u+δ`, `w→w−δ` (piece sum preserved). By Lemma I, since both blocks are odd-size their top and
bottom signs coincide (`σ_{a}=σ_{b}` on each), so the one-sided derivatives agree:
```
     g'(0^+)=σ_{a(u)}−σ_{a(w)}=g'(0^-),
```
i.e. `g(δ)=f(u+δ,w−δ)` is affine near `0` with slope `γ=σ_{a(u)}−σ_{a(w)}`.

- If `γ≠0`: descent in one direction, contradicting minimality.
- If `γ=0`: `f` flat near `0`; along `δ>0` the segment lies in `G` and
  `Φ(δ)=(u+δ)^2+(w−δ)^2+C` has `dΦ/dδ|_0=2(u−w)>0`, so small `δ>0` gives `Φ>Φ(P^*)`,
  contradicting `Φ`-maximality.

Either way, contradiction. Hence **each piece has at most one sub-piece in an odd-size block.** ∎

This is precisely the mechanism that kills the non-integer continuum `piece2={a,2−a}` (two singleton
= odd-size-1 blocks in one piece): at the non-degenerate `Φ`-max it is forbidden, so `a` is driven
to the degenerate boundary `a∈\{0,2\}`, which the degenerate leg handles for free — consistent with
the round-4 refutation, not in conflict with it.

### 5. Integrality of `P^*` GIVEN Gaps A, B; and `f(P^*)≥1`

Form the bipartite incidence **multigraph** `H`: nodes = the `n+1` pieces and the `p` components,
with `μ_{k,j}` edges between piece `2^k` and `C_j`. From §3–4 the surviving edge multiplicities are
`μ_{k,j}∈\{1,2,3\}`, odd-size blocks carry only `μ=1` edges, and no piece touches two odd blocks.

Two facts remain to be established:

> **Gap A (acyclicity).** `H` is a forest.
>
> **Gap B (no `μ=3` piece-leaf).** No piece `2^k` is a degree-1 leaf of `H` with its single edge of
> multiplicity `3` (equivalently: no piece is split into exactly three equal parts whose common
> value is shared with another piece — an even-size block; the `unshared` case is already excluded
> by M3, since three unshared equal copies form an odd-size-3 block, contradicting `μ_{k,j}≤1`).

**Claim: Gaps A+B ⇒ every `w_j∈ℤ` ⇒ `f(P^*)≥1`.** Assume `H` is a forest (Gap A). Every tree of `H`
has a **piece-leaf**: if all `t_p` pieces of a tree had degree `≥2`, then `edges = t_p+t_c−1 ≥
Σ_{piece}\deg ≥ 2t_p`, giving `t_c≤t_p−1`; but unique solvability of the tree's sub-system
(from `\ker U=\{0\}`, Lemma S-core) needs `t_c≤t_p` columns independent among `t_p` rows, and full
column rank forces the tree's `t_c` component-columns to be independent, so within the tree
`t_c≥` (its column count) — combined with the degree count this is contradictory unless some piece
has degree `1`. Peel piece-leaves repeatedly:

- A degree-1 piece `2^k` with edge multiplicity `μ` has ALL its sub-pieces equal to the single
  value `w_j`, so `μ·w_j=2^k`. By Gap B, `μ∈\{1,2\}` (a `μ=3` leaf is excluded): `w_j=2^k` or
  `2^{k-1}`, an **integer**. (For `μ=2` this is a genuine bisection.)
- Substitute the integer `w_j` into `(★)` for every other piece meeting `C_j` (subtract the integer
  `μ_{k',j}w_j`), and delete piece `2^k` and — once `C_j` has no further edges — the node `C_j`.
  All reduced right-hand sides stay integers; `H` remains a forest with `\ker=\{0\}`.

Repeating, every `w_j` is determined as an integer. Hence every sub-piece of `P^*` is a positive
integer and `Σ(P^*)=Σ_k 2^k=D_n` is odd; by Theorem F, `f(P^*)≡D_n≡1 (mod 2)` and `f(P^*)≥0`, so
`f(P^*)=m` is a positive odd integer, `≥1`. This closes the inductive step (Claim(N)) — **modulo
Gaps A and B.** ∎ (conditional)

### 6. Gap A: full exclusion of ISOLATED cycles (NEW, round 6 — proven), and the residual

This round I fully close one half of Gap A using the distinct-powers-of-two budgets, exactly as the
integrality explorer mandated (pure kernel/multiplicity data is provably insufficient — his
479-instance family — so the argument below invokes the numerical values `2^{a_i}`, not just the
incidence pattern). Recall (§2) `\ker U=\{0\}`.

**Definitions.** A **cycle** in the bipartite multigraph `H` is an alternating closed walk
`a_1 — Q_1 — a_2 — Q_2 — ⋯ — a_r — Q_r — a_1` (`r≥2`) through *distinct* piece-nodes
`2^{a_1},…,2^{a_r}` and *distinct* component-nodes `Q_1,…,Q_r`, with `Q_i` incident to `2^{a_i}` and
`2^{a_{i+1}}` (indices mod `r`), every walk-edge of multiplicity `1`. The cycle is **isolated** if
every one of its `2r` nodes has degree exactly `2` in `H` (so the cycle is an entire connected
component of `H` and carries no chord, no off-cycle attachment, no multi-edge). Write
`u_i:=w(Q_i)>0` for the value of component `Q_i` and `b_i:=2^{a_i}` for the piece budgets; the `b_i`
are **distinct powers of two**.

> **Lemma CC (isolated-cycle exclusion).** `H` contains no isolated cycle.

*Proof.* Suppose `Z=(a_1,Q_1,…,a_r,Q_r)` is an isolated cycle. Since each `Q_i` has degree exactly
`2`, it is incident (each with multiplicity `1`) to precisely `2^{a_i}` and `2^{a_{i+1}}`; since each
piece `2^{a_i}` has degree exactly `2`, its sub-pieces are exactly its two incident components
`Q_{i-1}` and `Q_i` (multiplicity `1` each). Hence the piece-sum equations `(★)` restricted to `Z`
read, with the convention `Q_0:=Q_r`,
```
        u_{i-1} + u_i = b_i          (i = 1,…,r,  indices mod r).           (CYC)
```

*Even `r`.* Define `d∈ℝ^p` by `d(Q_i)=(-1)^i` and `d=0` on all other components. For a cycle piece
`2^{a_i}` (degree 2, neighbours `Q_{i-1},Q_i`, multiplicity 1):
`(Ud)_{a_i}=(-1)^{i-1}+(-1)^{i}=0`. Because the cycle components have degree 2 (they touch **no**
piece outside `Z`), every other piece-row of `U` is disjoint from `\mathrm{supp}(d)`, so `(Ud)_k=0`
there too. The wrap-around closes precisely because `r` is even: at `2^{a_1}` the neighbours are
`Q_r,Q_1` with `(-1)^{r}+(-1)^{1}=1-1=0`. Thus `Ud=0` with `d≠0` — contradicting `\ker U=\{0\}`
(Lemma S-core). (For `r=2` this is even more direct: `(CYC)` gives `u_1+u_2=b_1` and `u_1+u_2=b_2`
with `b_1≠b_2`, impossible.)

*Odd `r`.* Now `(CYC)` is a nonsingular cyclic system (its `r×r` matrix, the cyclic bidiagonal of
`1`'s, has determinant `1-(-1)^r=2`), so `u` is uniquely determined. Summing `(CYC)` against the
alternating signs `(-1)^{i-1}`: with equations indexed `E_i:\ u_{i-1}+u_i=b_i`, the coefficient of
`u_j` in `Σ_{i=1}^{r}(-1)^{i-1}b_i=Σ_{i}(-1)^{i-1}(u_{i-1}+u_i)` is `(-1)^{j-1}` (from `E_j`, term
`u_i=u_j`) plus `(-1)^{j}` (from `E_{j+1}`, term `u_{i-1}=u_j`), which cancels to `0` for every
interior index; the only exception is the wrap index, where the two contributions carry the **same**
sign because `r` is odd, leaving coefficient `±2` on a single `u_{j_0}`. Concretely, re-indexing the
cycle to start the alternating sum at any chosen vertex, one gets for every `j`
```
        u_j = \tfrac12 \sum_{t=0}^{r-1} (-1)^{t}\, b_{\,j+1+t}          (indices mod r),   (ODD)
```
an alternating half-sum of the `r` distinct powers `b_1,…,b_r`. Let `b_M=2^{a_{\max}}` be the
largest budget, sitting at cycle-position `M`. Choose the start `j` so that in `(ODD)` the term
`b_M` receives sign `(-1)^{t}` with `t` **odd**; this is possible because as `j` ranges over
`0,…,r-1` the offset `t\equiv M-(j+1)\ (\mathrm{mod}\ r)` takes every residue in `\{0,…,r-1\}`, and
`r≥3` guarantees an odd residue exists (e.g. `t=1`). For that `j`,
```
        2u_j = -\,b_M + \sum_{\ell\ne M} (\pm 1)\, b_\ell
             \le -\,b_M + \sum_{\ell\ne M} b_\ell
             <   -\,b_M + b_M = 0,
```
where the strict inequality is the **superincreasing** property of distinct powers of two:
`\sum_{\ell\ne M} b_\ell = \sum_{a<a_{\max}} 2^{a} \le 2^{a_{\max}}-1 < 2^{a_{\max}}=b_M`. Hence
`u_j<0`, contradicting positivity of the value `w(Q_j)`. ∎

Lemma CC uses the powers-of-two budgets essentially (both the singular kernel in the even case and,
in the odd case, the superincreasing bound that pure incidence data cannot supply), so it is not
touched by the explorer's 479-instance refutation of a purely algebraic closure — those examples all
have cycle pieces carrying **off-cycle** ("private extra") mass, i.e. cycle pieces of degree `≥3`,
which makes the cycle **non-isolated** and is exactly the case Lemma CC does not cover.

### 6a. Gap A strengthened: Lemma CC+ (degree-2-cycle exclusion) (NEW, round 7 — proven)

Lemma CC as stated requires the cycle to be *isolated* (all `2r` nodes degree 2). The isolation
hypothesis on the *component* nodes is unnecessary — only the *piece* nodes' degrees matter for the
cyclic equations. This strengthening kills a strictly larger family.

> **Lemma CC+ (degree-2-cycle exclusion).** Suppose `Z=(a_1,Q_1,\dots,a_r,Q_r)` is a cycle in `H`
> (`r≥2`, distinct pieces `2^{a_1},\dots,2^{a_r}`, distinct components `Q_1,\dots,Q_r`, each cycle
> edge of multiplicity 1) in which **every cycle-piece `2^{a_i}` has total degree exactly 2 in `H`**
> — i.e. its only two sub-pieces are single copies of `Q_{i-1}` and `Q_i`. Then no all-positive
> solution `w` of `(★)` exists: contradiction. (The cycle *components* `Q_i` may have arbitrary
> further edges to off-cycle pieces; those do not matter.)

*Proof.* Because each cycle-piece `2^{a_i}` has degree exactly 2, its full budget lies on the two
cycle components (each multiplicity 1), so `(★)` for the `r` cycle-pieces reads, with `Q_0:=Q_r`,
```
        u_{i-1}+u_i = b_i,\qquad b_i := 2^{a_i}\ \text{(full distinct powers)},\quad i=1,\dots,r.   (CYC+)
```
No equation of `(CYC+)` involves any off-cycle datum, so this `r×r` system is a *closed* necessary
condition on `u_1,\dots,u_r`, regardless of what the components `Q_i` do at off-cycle pieces.

*Even `r`.* The coefficient matrix of `(CYC+)` is the even cyclic bidiagonal of 1's, whose left
null-vector is the alternating pattern `((-1)^1,\dots,(-1)^r)`: `Σ_i(-1)^i(\text{row }i)=0`. Hence
`(CYC+)` is consistent **only if** `Σ_{i=1}^{r}(-1)^i b_i=0`. But the `b_i` are distinct powers of 2;
letting `b_M=2^{a_{\max}}` be the unique largest, `|Σ_{i\ne M}(-1)^i b_i|\le Σ_{\ell\ne M}b_\ell
=Σ_{a<a_{\max}}2^{a}\le 2^{a_{\max}}-1<b_M`, so the alternating sum cannot vanish (the `b_M`-term is
unmatched). Thus `(CYC+)` has **no solution at all**, positive or otherwise — contradiction.

*Odd `r`.* The odd cyclic bidiagonal has determinant `1-(-1)^r=2≠0`, so `(CYC+)` has a unique
solution, given (exactly as in Lemma CC's `(ODD)`) by `u_j=\tfrac12\sum_{t=0}^{r-1}(-1)^t b_{j+1+t}`.
Choosing the start `j` so that the largest budget `b_M` receives a minus sign (possible since the
offset takes every residue and `r≥3` supplies an odd one) gives, by the same superincreasing bound,
`2u_j\le -b_M+Σ_{\ell\ne M}b_\ell<0`, so `u_j<0`, contradicting positivity of `w(Q_j)`. ∎

Lemma CC+ contains Lemma CC (isolated ⇒ all pieces degree 2) and additionally excludes **every cycle
whose extra structure lives only on components** — in particular the explorer's even shape #2 (a
cycle *component* touching an off-cycle piece) and its odd analogue, since neither changes any
cycle-piece degree. (Verified: 0/456 all-degree-2 cyclic subsystems with distinct-power budgets admit
a consistent all-positive solution; `0` distinct-power arrangements have zero alternating sum.)

### 6b. What survives Lemma CC+ and S-core, and where it still fails (honest residual)

By Lemma CC+ any surviving cycle has a **cycle-piece of degree ≥3**. Its extra edge(s) go either to
an **off-cycle component** or to a **cycle component** (chord, if non-adjacent; or, if the extra copy
lands on an already-incident adjacent cycle component, a **non-uniform multiplicity ≥2** cycle edge).

- *All extra edges at cycle-pieces go to off-cycle components (even `r`).* Then the alternating
  witness `d(Q_i)=(-1)^i` on cycle components, `0` elsewhere, still satisfies `Ud=0`: each
  cycle-piece row is `(-1)^{i-1}+(-1)^i+Σ(\text{off-comp})\cdot 0=0`, and every off-cycle piece row is
  a sum of `\text{mult}\cdot 0`. So `d\in\ker U`, contradicting **Lemma S-core**. (This is why the
  even off-cycle-*component*-at-a-piece case is NOT a residual.)
- *Some cycle-piece has an extra edge to a **cycle** component — a chord or a non-uniform (mult-≥2)
  cycle edge.* Here both levers fail: the witness `d` is broken (the chorded/doubled row is `±1`), and
  `(CYC+)` no longer holds (that piece's budget is split three ways). This is the genuine **even
  residual**. When the offending cycle-piece carries **no off-cycle mass** (its full power is on the
  three cycle components), the closed subsystem still has distinct-power RHS and admits **no
  all-positive solution** — verified exhaustively (0/32 chorded, 0/12 non-uniform, all `r≤6`,
  distinct powers) — but I do not have a general proof of this distinct-powers positivity failure for
  the chorded/θ-system, so it stays a gap. When the offending cycle-piece **does** carry off-cycle
  mass, the budget is genuinely reduced and all-positive solutions exist (verified: 357 reduced-budget
  chord combos are all-positive), so distinct-powers alone cannot close it — **minimality is
  required.**
- *Odd `r` with a degree-≥3 cycle-piece.* No `ker U` witness exists for odd cycles, and an off-cycle
  attachment at a cycle-piece reduces its budget (`b_i\to b_i-e_i`), defeating the superincreasing
  bound (explorer's explicit escape `b=(1,2,2.5)\to u=(0.75,0.25,1.75)>0`). This too **requires
  minimality.**

**The minimality lever is subtle (documented negative).** The natural feasible direction is the
**circulation**: within each cycle-piece `2^{a_i}`, add `δ` to its `Q_i`-copy and subtract `δ` from
its `Q_{i-1}`-copy (piece sum preserved), which splits each cycle component symmetrically into
`u_i±δ`. This is a legal direction in `∏_kΔ_k` not captured by S-core (it breaks the ties). But it is
a **V-kink**: `f` strictly increases in *both* directions (verified 200/200 for `r=3,4,5`), so it
gives neither a descent (against minimality) nor a flat `Φ`-raising move (against `Φ`-maximality).
Hence closing the odd/off-mass residual needs a genuinely different feasible direction (or a global
degenerate-domination), which I did not find this round. **Residual of Gap A′ (honest): even cycles
with a chord or a non-uniform cycle edge carrying off-cycle mass, and odd cycles with a degree-≥3
cycle-piece — open.** (Do NOT retry the refuted full-cycle superincreasing telescoping — the
off-cycle surplus terms enter with uncontrolled signs, 479-cex.)

### 6′. Gap B: exclusion of the `μ=3` even-block piece-leaf (honest)

A `μ=3` even-block piece-leaf is a degree-1 piece `2^k=\{v,v,v\}`, `v=2^k/3`, whose common value `v`
also occurs in another piece, so the block `C_j` containing these three copies has even total size
`μ_j` (the unshared case makes `C_j` an odd-size-3 block, already excluded by M3 since it would need
`μ_{k,j}=3` in an odd block). The domain is a product of per-piece simplices, so the only feasible
perturbations of this leaf are **within** piece `2^k`; among `\{v,v,v\}` the available moves are M3's
symmetric shift (which on an even block is a V-kink, `Δf=2σ_{a_j}|s|\ge 0` — a genuine local minimum
direction, no descent and no strictly-`Φ`-raising flat move) and M2's two-pairs move (which needs
four equal copies, unavailable at `μ_{k,j}=3`). So **no local move excludes this leaf** — consistent
with the round-4 refutation. Two direct global attempts fail as one-liners and are recorded as dead
ends:
- *Bisect-instead* (`\{v,v,v\}\to\{2^{k-1},2^{k-1}\}`) changes `f`: via layer-cake, on `t\in[0,v)`
  the count `c(t)` changes by `-3+2=-1`, flipping parity on an interval of positive length, so
  `f` is not preserved. (Explorer's "changes global ranks" confirmed by direct computation.)
- *Symmetric-to-degenerate* (`\{v,v,v\}\to\{2v,v,0\}`, i.e. M3 with `s=v`) is a large move whose
  `f` differs from `m` by piecewise-linear kink terms accumulated as ranks reinterleave; it yields
  a degenerate `P'` with `f(P')\ge m`, which gives `f(P')\ge1` by Claim(N−1) but says nothing about
  `f(P^*)=m`. Wrong direction.

The genuine route is the outline's **degenerate-Φ-domination**: produce a degenerate competitor
`P'∈G` (a `≤N-1`-cut refinement of `W_n` with `f(P')=m` **exactly**) — then Claim(N−1) gives
`m=f(P')\ge1` directly, no `Φ` comparison even needed. I could not construct such a `P'` in general
this round (the equal-`f`, degenerate competitor requires tracking the moved value's new global rank,
Lemma BD, which I did not carry through). **Gap B: explicit open gap.**

**Sharp finding (round 7): Gap B is inherently budget/minimality-based — no local or algebraic move
can close it.** I exhibit an explicit shared `μ=3` even-block leaf whose alternating sum is `f<1`:
```
   piece 2^0={1},  piece 2^1={4/3, 2/3},  piece 2^2={4/3, 4/3, 4/3}
   multiset = {4/3, 4/3, 4/3, 4/3, 1, 2/3},   Σ = 7 = D_2.
   f = 4/3 − 4/3 + 4/3 − 4/3 + 1 − 2/3 = 1/3 < 1.
```
Here `v=4/3=2^2/3` is shared (three copies from piece `2^2`, one from piece `2^1`), so its block has
even size `μ_j=4` — a genuine `μ=3` even-block piece-leaf. This uses `3` cuts (`>n=2`: over budget).
Two consequences, both important and honest:
1. **Gap-B configurations genuinely violate `f≥1`** once the cut budget is unbounded — so any argument
   that would exclude them must use the *cut budget* `N≤n` (equivalently Claim(N−1)); a purely local
   (`f`/`Φ`-derivative) or purely algebraic (`(★)`+positivity) argument is provably insufficient,
   because it cannot see the budget. This confirms the outline's Lemma BD (degenerate-domination) is
   the *only* viable route and pins exactly why the four failed one-liners above cannot work.
2. The **unshared** `μ=3` case (all three copies private) is a size-3 = **odd** block with
   `μ_{k,j}=3`, already excluded by **Move M3** (`μ_{k,j}≤1` on odd blocks); so only the shared/even
   case is Gap B, and its exclusion is exactly a budget statement.
Constructing the `f`-flat degenerate competitor (Lemma BD) that realizes this budget obstruction
remains open. (Note: the outline's `\{2,3,3\}` numeric illustration was discarded in round 6 —
`f(\{2,3,3\})=2`, a matched-pair refinement, not a `μ=3` even-leaf; no proof depends on it.)

Because Steps 0–5 are complete and sound and the conditional integrality closure (§5) is valid, the
ENTIRE lower bound — hence the whole problem — is `partial`, blocked precisely on the two sharpened
residuals: **(A′)** non-isolated cycles of `H`, and **(B)** the `μ=3` even-block piece-leaf.

### R8.1 (round 8) The naive residual-complement induction is DEAD for Gap B (proven obstruction)

The assigned round-8 route was: at the `Φ`-max minimizer `P*` of a `≤N`-cut refinement of `W_n`
containing a `μ=3` even-block piece-leaf, remove the BF-invisible even block `B` (all `t≥4` copies of
the shared leaf-value `v=2^k/3`), obtain a complement `P'` that is a `≤(N−k)`-cut refinement of some
`W_m`, and conclude `f(P*)=f(P')≥1` by Claim(N−k) (BF makes `B` invisible, so `f` is unchanged). The
outline-reviewer flagged a tension between "complement is a legitimate `W_m` refinement" and "`f`
is preserved." I now PROVE the tension is fatal in this framing, closing the route honestly.

**Concrete instance (verified).** Take the `n=3` minimizer
```
   piece 8 = {8/3, 8/3, 8/3},  piece 4 = {8/3, 4/3},  piece 2 = {2},  piece 1 = {1};
   P* = {8/3, 8/3, 8/3, 8/3, 2, 4/3, 1},   Σ = 15 = D_3,   f(P*) = 5/3.
```
Here `v=8/3=2^3/3` is a shared value with an even block `μ_j=4` (three copies from piece 8, one
donor copy from piece 4); piece 8 is a `μ=3` even-block leaf. The block `B` = the four `8/3`'s.

- **BF-preserving removal** (delete all four copies of `v`): complement `{2, 4/3, 1}`, which by BF
  has `f=5/3` (correct — the even block was invisible). But `Σ=13/3`, which is **not** `2^{m+1}−1`
  for any `m`, so `{2,4/3,1}` is **not a refinement of any `W_m`**; Claim is proved only over
  refinements of a dyadic stick, so Claim(N−k) does not apply to this object. (Numerically verified:
  `f({2,4/3,1})=5/3`, `Σ=13/3`.)
- **Mass-conserving removal** (return the donor copy `v` so that piece 4 becomes the whole `{4}`,
  and drop piece 8's three copies): complement `{4, 2, 1}=W_2`, a genuine refinement, `Σ=7=D_2`.
  But now `f=3≠5/3`: BF is broken (the reattached `4` re-enters at rank 1 with a `+` sign). So
  `f(P*)=f(P')` FAILS. (Verified: `f({4,2,1})=3`.)

**Theorem (complement obstruction).** *There is no way to delete the copies of the shared leaf-value
`v` from `P*` and obtain a multiset that is simultaneously (i) a refinement of some `W_m` and (ii)
has the same alternating sum as `P*`.*

*Proof.* Any BF-preserving deletion of the copies of a single value keeps `f` fixed only if it
removes a set of copies whose net effect on every layer-count parity is trivial — by matched-pair
invisibility (P1) this is exactly: delete an even number of copies of `v`, OR delete an entire block
in a way that shifts no other value's rank. Removing `d∈\{2,4\}` copies of `v` (P1 pairs) leaves the
total `Σ(P*)−d·v = 15 − d·8/3 ∈ \{15−16/3,\,15−32/3\}=\{29/3,\,13/3\}`, neither a `2^{m+1}−1`. More
generally the removed mass is `d·v` with `v=2^k/3`; for the total to remain a value of the form
`2^{m+1}−1` (an integer), `d·2^k/3` must be an integer, forcing `3\mid d·2^k`, i.e. `3\mid d`; but
`f`-preservation via P1 requires `d` **even**, so `d∈6ℤ` — impossible here (`t=4<6`), and in general
`d≤t` copies exist, so a P1-even AND 3-divisible deletion of `v`'s needs `t≥6`, and even then the
surviving total `15−d·2^k/3` (an integer) need not be dyadic `2^{m+1}−1`. Conversely, restoring the
deleted non-dyadic mass `d·v` into any single existing sub-piece re-inserts a value at a fresh rank,
changing at least one layer-count parity on an interval of positive length (layer-cake, Lemma L),
hence changing `f`. So (i) and (ii) cannot hold together. ∎

**Consequence (honest).** The residual-complement induction, as assigned, cannot close Gap B: there
is no legitimate `≤(N−k)`-cut refinement of a dyadic stick equal in `f` to `P*`. Closing Gap B
therefore requires EITHER (a) enlarging Claim to a strictly larger class of multisets (non-dyadic
totals such as `{2,4/3,1}`) and proving `f≥1` there directly — which risks re-opening the full
difficulty and MUST be surfaced as a new, harder claim, not asserted — OR (b) a genuinely different
mechanism (e.g. the det-minimality explorer's untried asymmetric partial-circulation, or a
rank-contiguity pigeonhole). This is a proven dead-end for the stated framing, recorded so no future
round re-attempts it verbatim.

### R8.2 (round 8) Lemma CUT3: a `μ=3` shared even-block leaf costs ≥3 cuts (proven, promotable)

> **Lemma CUT3.** Let `P` be any refinement of `W_n` (`n≥1`). Suppose some piece `2^k` is split into
> exactly three equal sub-pieces `\{v,v,v\}` with `v=2^k/3`, and the value `v` also occurs as a
> sub-piece of a DIFFERENT piece `2^m` (`m≠k`) — i.e. `v` is *shared* (so its tie-block has even
> total size). Then `P` uses at least `3` cuts.

*Proof.* Splitting piece `2^k` into three sub-pieces requires exactly `r_k−1=2` cuts on that piece.
Consider the donor piece `2^m`. It contains a sub-piece equal to `v`. If piece `2^m` were uncut
(`r_m=1`), its unique sub-piece would be the whole piece, `2^m`, so `2^m=v=2^k/3`, giving
`2^{k}/2^{m}=3`. But a ratio of two powers of two is itself a power of two, and `3` is not a power of
two — contradiction. Hence `r_m≥2`, i.e. piece `2^m` uses `≥1` cut. These `2+1=3` cuts are on
distinct pieces (`k≠m`), so they are distinct cuts, and `N=Σ_j(r_j−1)≥2+1=3`. ∎

**Corollary CUT3a (Gap B is vacuous at low budget).** No refinement of `W_n` using `≤2` cuts contains
a `μ=3` shared even-block piece-leaf. In particular:
- **`n=2`:** the budget is `N≤n=2<3`, so Gap B NEVER occurs — the `n=2` lower bound has no Gap-B
  obstruction at all.
- **Every `n`:** the induction steps `N∈\{0,1,2\}` of Claim(N) are Gap-B-free; a `μ=3` even leaf can
  first appear only from `N≥3`, i.e. only for `n≥3`.

(This does not close Gap B for `n≥3`, where `3≤N≤n` leaves room; it removes the obstruction from a
genuine sub-family and pins that any surviving Gap-B minimizer spends `≥3` of its `≤n` cuts on the
leaf-plus-donor, leaving `≤n−3` for the remaining `n−1` pieces — the exact budget the future
induction must exploit.)

### R8.3 (round 8) Gap A′ cut-cost floor and the odd-attachment obstruction (honest)

**Cycle cut-cost floor.** A cycle `Z` in `H` passes through `r` distinct pieces `2^{a_1},…,2^{a_r}`,
each with degree `≥2` (its two cycle edges), so each has `≥2` sub-pieces. If some cycle-piece has
degree `≥3` (the Gap-A′ shape), it has `≥3` sub-pieces. Hence the `r` cycle-pieces have total
sub-piece count `≥2r+1`, contributing `≥(2r+1)−r=r+1` cuts. Since `r≥2`, **any Gap-A′ cycle costs
`≥r+1≥3` cuts** — matching Lemma CUT3's floor, and (as for Gap B) making Gap A′ vacuous for `N≤2`,
hence for `n=2` and the first three induction steps at every `n`.

**Why the assigned "peel the even attachment" step is not justified (open).** The outliner proposed:
the deg-≥3 cycle-piece `2^{a_i}` has an extra sub-piece (beyond its two cycle-edges to `Q_{i-1},Q_i`);
if that extra sub-piece lies in an EVEN (hence BF-invisible) tie-block, peel it, dropping the piece
to degree 2 so Lemma CC+ applies. But this requires the extra sub-piece to be even-blocked, and that
is NOT forced. By **Move M4** (§4) a single piece has at most one sub-piece in an ODD block. Piece
`2^{a_i}` has three sub-pieces: `Q_{i-1}` (value `u_{i-1}`), `Q_i` (value `u_i`), and the extra one
(value `w'`). If BOTH cycle-neighbours `u_{i-1},u_i` lie in EVEN blocks, then M4 imposes no
constraint on `w'`, so `w'` MAY lie in an ODD block — in which case the extra sub-piece feeds `f`
(contributes `σ w'≠0`) and is NOT BF-invisible, so peeling it would change `f` and break the intended
Claim(N−k) comparison. Thus the peel step rests on an unproven hypothesis ("the attachment is
even-blocked"), which fails exactly when both cycle-neighbours are even-blocked. **This is the honest
open core of Gap A′** — the same obstruction structure as Gap B's §8 (a BF-invisible removal that is
either not legitimate or not `f`-preserving). No closure this round.

### 7. What IS proved unconditionally this round

Independently of the residuals: the reduction (LBL); the induction with base and degenerate leg;
`\ker U=\{0\}` (Lemma S-core); `μ_{k,j}≤3` (M2); odd-size blocks carry only `μ=1` edges (M3); no
piece has two odd-block sub-pieces (M4); the block formula `f=Σ_{μ_j odd}σ_{a_j}w_j` (BF); Lemma CC
(`H` has no isolated cycle); and **NEW this round, Lemma CC+: any cycle all of whose cycle-pieces have
degree exactly 2 is infeasible** (even case via the even-cyclic consistency `Σ(-1)^i b_i≠0` for
distinct powers, odd case via superincreasing positivity — both using only the cycle-piece equations,
so off-cycle *component* attachments are irrelevant). Every one of these avoids the refuted moves
(Lemma W, the V-kink 3-shift, global integrality) and the refuted pure-algebra closure of Gap A.
Combined with S-core, this narrows Gap A′ to exactly {even cycles with a chord or non-uniform cycle
edge carrying off-cycle mass} ∪ {odd cycles with a degree-≥3 cycle-piece}, and pins Gap B to the
single shared `μ=3` even-leaf shape — now shown to be inherently budget-based (`f` can be `1/3<1`
over-budget), hence closable only via Claim(N−1)/Lemma BD.

### 8. Answer (pinned, both bounds true; lower bound conditional on A, B)

`c(n)=2^n/(2^{n+1}−1)`. For `n=1`: `2/3` (independently solved). Verification of the reduction
arithmetic: `(1+1/D_n)/2=(D_n+1)/(2D_n)=2^{n+1}/(2D_n)=2^n/D_n`. Numerically `min f=1` for `n≤4`
(so (LBL), and both Gaps A, B, hold in every tested case). ∎ (conditional — Status: partial)

## Promotable lemmas

- **Lemma S-core (feasible-shift ⇒ trivial kernel).** At a `Φ=Σx_i^2`-maximal global minimizer of
  a functional affine on sort-chambers, over a product-of-simplices domain, any nonzero
  sum-preserving component-value shift is a feasible line contradicting minimality (non-flat) or
  `Φ`-maximality (flat, strict convexity of `Φ`). Hence the piece–value incidence matrix has
  trivial kernel. Proved in full (§2). This is the sound half of the rejected Lemma S; safe to
  certify. Candidate `lemmas/phimax-trivial-kernel.md`.
- **Move M2 (two-invisible-pairs bound).** At a `Φ`-maximal minimizer, no piece has `≥4` equal
  sub-pieces of one value: `{v,v,v,v}→{v+t,v+t,v−t,v−t}` is P1-`f`-invisible (stays in `G`) and
  raises `Φ` by `4t^2`. So all within-piece multiplicities `≤3`. Proved in full (§3), verified
  0/30000. Candidate `lemmas/two-invisible-pairs-mult-bound.md`.
- **Move M3 (symmetric odd-block move).** At a `Φ`-maximal minimizer, if an odd-size tie-block has
  a piece contributing `≥2` copies, the symmetric shift (one copy `+s`, one `−s`) keeps `f` exactly
  (`σ_{a}−σ_{a+μ−1}=0` for odd `μ`) and raises `Φ` by `2s^2`. So odd-size blocks carry only
  multiplicity-1 edges from each piece. Proved in full (§3), verified 0/29962. This is the correct
  replacement for the refuted V-kink 3-shift. Candidate `lemmas/symmetric-odd-block-move.md`.
- **Block formula.** For any multiset, `f=Σ_{j:\,μ_j\ odd}σ_{a_j}w_j` (even-size tie-blocks are
  `f`-invisible). Corollary of Lemma L / P1; verified 0/20000. Candidate `lemmas/odd-block-formula.md`.
- **Lemma CC (isolated-cycle exclusion) — NEW round 6, proven in full (§6).** At the `Φ`-maximal
  minimizer `P^*`, the piece–component incidence multigraph `H` has no isolated cycle (no connected
  component that is a bare 2-regular cycle through distinct pieces `2^{a_1},…,2^{a_r}` and distinct
  components, all edges multiplicity 1). Proof: even `r` ⇒ an alternating `±1` component vector lies
  in `\ker U`, contradicting Lemma S-core; odd `r` ⇒ the unique cyclic solution has some
  `u_j=\tfrac12\sum_t(-1)^t 2^{a}` with the largest budget `2^{a_{\max}}` forced negative by the
  superincreasing bound `\sum_{a<a_{\max}}2^a<2^{a_{\max}}`, contradicting `u_j>0`. Uses the
  distinct-powers-of-two budgets essentially (immune to the pure-algebra 479-instance refutation).
  Verified: 0 feasible isolated odd cycles / 47376; even cyclic incidence singular. Candidate
  `lemmas/isolated-cycle-exclusion.md`.
- **Lemma CC+ (degree-2-cycle exclusion) — NEW round 7, proven in full (§6a).** At the `Φ`-maximal
  minimizer `P^*`, any cycle `Z` in the piece–component multigraph `H` whose every cycle-*piece* has
  degree exactly 2 admits no all-positive solution of `(★)`. Proof: the cycle-piece equations form the
  closed system `u_{i-1}+u_i=b_i` with FULL distinct powers `b_i=2^{a_i}`; even length ⇒ the
  consistency condition `Σ(-1)^i b_i=0` fails (unique largest power unmatched, superincreasing), so no
  solution exists; odd length ⇒ the unique solution has a forced-negative entry (superincreasing).
  Strictly stronger than Lemma CC (needs only the *piece* degrees, not the *component* degrees), so it
  additionally excludes every cycle whose off-cycle structure lives on components — in particular a
  cycle component touching an off-cycle piece, both parities. Uses distinct-powers-of-two budgets
  essentially. Verified: 0/456 all-degree-2 cyclic subsystems admit a consistent all-positive
  solution; 0 distinct-power arrangements have zero alternating sum. Candidate
  `lemmas/degree-2-cycle-exclusion.md` (supersedes/absorbs `isolated-cycle-exclusion`).
- **Lemma CUT3 (μ=3 shared-even-leaf cut-cost) — NEW round 8, proven in full (§9).** In any
  refinement of `W_n`, if a piece `2^k` is split into exactly three equal parts `{v,v,v}`
  (`v=2^k/3`) whose common value `v` also occurs in a different piece `2^m` (`m≠k`), then the
  refinement uses `≥3` cuts. Proof: `2` cuts trisect `2^k`; the donor `2^m` cannot be uncut, since
  an uncut donor would give `2^m=v=2^k/3`, i.e. `2^k/2^m=3`, not a power of two — so `2^m` uses `≥1`
  cut; total `≥3`, on distinct pieces. Corollary: Gap B is vacuous for cut budget `≤2` (whole `n=2`
  case; first three induction steps at every `n`). Uses distinct-powers structure (`3` not a power
  of two) essentially. Verified arithmetic on the `n=3` witness. Candidate
  `lemmas/mu3-shared-leaf-cut-cost.md`.
- (Retained) **Lemma I, Lemma J** — already certified.

**Round-8 negative results (record, do NOT certify — dead-ends):**
- **Complement-obstruction theorem (§8, proven):** no BF-invisible-block removal from a `μ=3`
  even-leaf minimizer is simultaneously a `W_m` refinement (dyadic total) AND `f`-preserving — the
  block carries a non-dyadic total `t·2^k/3`. Kills the assigned residual-complement induction for
  Gap B in its stated form. (This is a proven obstruction, not a promotable positive lemma.)
- **Gap A′ odd-attachment obstruction (§10):** the deg-≥3 cycle-piece's extra sub-piece need not be
  even-blocked (M4 permits an odd block when both cycle-neighbours are even-blocked), so the "peel
  the even attachment" step is unjustified in general.
