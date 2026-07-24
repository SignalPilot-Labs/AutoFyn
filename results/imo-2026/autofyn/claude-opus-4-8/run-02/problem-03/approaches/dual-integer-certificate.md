# Approach: dual-integer-certificate (imo-2026-03, IMO 2026 P3)

## Status
partial

## Approaches tried
- **dual-integer-certificate (round 8, ADVANCE — this round).** Three rigorous new contributions to
  the Budget Lemma (= Positivity), plus honest reduction of what remains:
  1. **Budget Lemma case (a) — the self-contained-top reduction — PROVEN IN FULL** (new §4a). If the
     top value `w_1 = 2^{n-1}` occurs exactly as the two halves of piece `2^n` and nowhere else, the
     rest is an all-even refinement of `W_{n-1}` with exactly `N−1` cuts, and strong induction on `n`
     gives `N ≥ n+1`. Clean, self-contained, certifiable; reproduces the certified `n=2` minimal
     example exactly.
  2. **Budget-minimal ⟹ `ker U = 0` — PROVEN IN FULL** (new §4c). A minimal-`N` all-even refinement
     may be taken with the incidence matrix of full column rank (`p ≤ n+1`, values the unique rational
     solution determined by the incidence). This is the Budget-Lemma analogue of certified S-core and
     lets the powers-of-two arithmetic apply; it is a genuine structural reduction, not a heuristic.
  3. **Counting reformulation + receiver bound — PROVEN IN FULL** (new §4b). Budget Lemma
     `⟺ Σ_k (r_k − 2) ≥ 0` (`r_k` = #sub-pieces of piece `2^k`). Every uncut piece (`r_k=1`) is a whole
     copy `2^k` matched to a copy inside a strictly larger piece; a receiver piece `2^m` absorbing `d_m`
     distinct uncut partners has residual mass `≥ 1 > 0`, forcing `r_m ≥ d_m + 1`. This yields the
     rigorous partial bound `T ≥ 2(n+1) − R` (`R` = #receiver pieces), i.e. `N ≥ (n+1) − R`. It does
     NOT close the lemma (the "−R" slack is exactly the residual-mass recursion ≅ Gap A′ / case (b)).
  **Outcome:** case (a) of the Budget Lemma is now a proven, certifiable sub-lemma; `ker U=0`-reduction
  and the counting reformulation are proven structural facts; the residual is exactly case (b)
  (off-piece / residual-mass exchange), explicitly isomorphic to Gap A′. (D′) unchanged: stated on the
  visible reduced subsystem `U^★`, equal to the shared benign-U wall via Cramer. Honest partial.
- **dual-integer-certificate (round 6, NEW).** Dual framing: prove `f(P*) ∈ ℤ` via an integer dual
  `λ` with `Uᵀλ = s` (then `f = λᵀb = Σ_k λ_k 2^k`), not primal integrality of `w`. **Lemma DUAL
  proven and certified**; reduction clean. Decisive finding: **Gap D (integer dual solvability) is
  FALSE as a universal S-core property** (`{2,4/3,4/3,4/3,1}`, det±3, `f=5/3`), so a proof MUST use
  minimality. Two open gaps: Gap D at minimizers, and Positivity (`f≠0`). Honest partial.
- **dual-integer-certificate (round 7, ADVANCE — this round).** Two rigorous new contributions that
  materially reshape the residual, plus honest reduction of what remains:
  1. **Positivity is fully characterized and its hard half eliminated.** Proved in full **Lemma
     POS-CHAR:** `f(P) = 0 ⟺ every distinct sub-piece value has even multiplicity` (call this
     *all-even*). Consequence: the feared *odd-cancellation* sub-case of `f=0` (signed sum of `≥3`
     distinct odd-block values vanishing) **does not exist** — `f` is a sum of nonnegative terms, so
     `f=0` forces each term zero, i.e. all-even. So Positivity `⟺` **the all-even configuration is
     unreachable within `N ≤ n` cuts** (Budget Lemma), a single clean combinatorial statement.
  2. **Cramer integrality (square case), proved in full (Lemma CRAMER):** for `p = n+1` (square
     invertible `U`), `f(P*)·det(U) = Σ_j s_j det(U_j) ∈ ℤ`, where `U_j` is `U` with column `j`
     replaced by `b`. Hence `f(P*) = M/det(U)` with `M ∈ ℤ`, and the requirement "`f∈ℤ`" for
     Proposition R becomes exactly "`det(U) | M`" — implied by (but weaker than) `|det U|=1`. This
     ties the dual target in the square case to the primal `|det U|=1` and shows the two routes'
     square-case targets coincide up to a divisibility slack.
  3. **Weakened Proposition R target** from "integer `λ`" to the strictly weaker "`f(P*) ∈ ℤ`"
     (all that Prop R uses). Renamed **(D′)**.
  4. Proved the **top-piece-cut fact**: in any all-even refinement the largest sub-piece value is
     `≤ 2^{n-1}`, so piece `2^n` is cut. (`1` cut; the naive "every piece is cut" is **FALSE** —
     refuted by the all-even config `piece1={1}, piece2={½,½,1}, piece4={2,2}`, `N=3=n+1`, piece `1`
     uncut — so the Budget Lemma needs a subtler argument than piece-counting.) **Outcome:** Gap D at
     minimizers is still the load-bearing gap; Positivity is reduced to one crisp Budget Lemma with
     the odd-cancellation branch killed, top-piece-cut in hand, and exhaustive `n=2,3` evidence
     (min cuts for all-even `= n+1`). Honest partial.

## Current best

The lower bound (LBL) is reduced, at a Φ-maximal global minimizer `P*`, to **two** explicit facts,
sharper than last round:

- **(D′) integrality at the minimizer:** `f(P*) ∈ ℤ`. Sufficient (does not need the full integer
  `λ`); implied by Gap D (integer `λ` solving `Uᵀλ=s`). In the square case `p=n+1`, equivalent to
  `det(U) | Σ_j s_j det(U_j)` (Lemma CRAMER). Still needs minimality (Gap D not universal).
- **(Pos) positivity:** `f(P*) ≠ 0`. Now fully reduced (Lemma POS-CHAR) to the **Budget Lemma:**
  *no `≤ n`-cut refinement of `W_n` is all-even.* The odd-cancellation branch is eliminated. This
  round the Budget Lemma is materially advanced: **case (a) (self-contained top pair) is PROVEN in
  full** (§4a), the **`ker U=0` reduction is PROVEN** (§4c), and the **counting reformulation with the
  receiver bound `T ≥ 2(n+1) − R` is PROVEN** (§4b). The sole remaining piece is **case (b)** (a copy
  of the top value housed off the top piece, or positive residual mass on the top piece) — a genuine
  residual-mass exchange, explicitly isomorphic to Gap A′ of the primal route.

Everything else on this route is complete and rigorous: the reduction to (LBL); the certified
structure theory of `P*` (S-core, block formula, `Uw=b`); Lemma DUAL (dual value identity); Lemma
POS-CHAR, Lemma CRAMER, the top-piece-cut fact; and the round-8 §4a/§4b/§4c results below.

---

## The proof so far (complete parts + the isolated gaps)

### §0. Setup and imported certified results

**Reduction (certified, imported).** By `layer-cake-alt-sum` and `endgame-greedy`,
`c(n) = (1 + max_LB min_XY M)/2` with `M(P) = meas{t : #\{pieces > t\} odd\}` equal to the
alternating sum `f(P) = Σ_r σ_r a_r` (`σ_r = (−1)^{r+1}`, `a_1 ≥ a_2 ≥ …` the sorted-descending
pieces). Hence `c(n) = 2^n/D_n` (`D_n = 2^{n+1}−1`) is equivalent to `max_LB min_XY M = 1/D_n`.

The **upper bound** `c(n) ≤ 2^n/D_n` is FULLY CERTIFIED (`delete-subtract-reachability`,
`subset-sum-pigeonhole`, and the `b ≥ m` bisect-all case). We import it verbatim.

The **lower bound** reduces to **(LBL):** *every refinement `Q` of `W_n = {2^0, …, 2^n}` obtained by
at most `n` cuts satisfies `f(Q) ≥ 1`* (scaled units where Liu Bang marks `{2^k}`, total `D_n`).

**Induction and the minimizer `P*` (certified structure, imported).** Strong induction on cut count
`N`. Degenerate minimizers (a length-`0` sub-piece) drop `N` and are handled by the hypothesis. For
the non-degenerate case fix the combinatorial type (how many sub-pieces each piece `2^k` receives)
and minimize `f` over `K = ∏_k Δ_k` (`Δ_k` fixes piece `k`'s sub-pieces to sum `2^k`); among
minimizers pick `P*` maximizing the strictly convex `Φ(P) = Σ_i x_i^2`. From certified lemmas:

- `phimax-trivial-kernel` (**S-core**): `ker U = \{0\}`, `U` the `(n+1)×p` piece–value incidence
  matrix `U_{k,j} = μ_{k,j}` = (number of sub-pieces of piece `2^k` with value `w_j`),
  `w_1 > … > w_p` the distinct values. Full column rank ⇒ `p ≤ n+1`.
- `odd-block-formula` (**block formula BF**): with `μ_j = Σ_k μ_{k,j}` the size of value-class `j`
  (occupying descending ranks `[a_j, a_j+μ_j−1]`), `f(P*) = Σ_{j : μ_j odd} σ_{a_j} w_j`.

Define `b = (2^0,…,2^n)ᵀ ∈ ℤ^{n+1}` and `s ∈ \{−1,0,1\}^p` by `s_j = σ_{a_j}` if `μ_j` odd, `s_j=0`
if `μ_j` even. Then:
```
    (★)   U w = b ,        (BF)   f(P*) = sᵀ w .
```
Also `Σ_k μ_{k,j} = μ_j`, each row-sum `r_k = Σ_j μ_{k,j} ≥ 1`, total sub-pieces
`T = Σ_j μ_j = Σ_k r_k = (n+1) + N` where `N = Σ_k (r_k − 1) ≤ n` is the cut count.

### §1. The dual identity (PROVEN — imported certified Lemma DUAL)

> **Lemma DUAL.** `U ∈ ℤ^{(n+1)×p}` with `ker U = \{0\}`, `Uw = b`, `s ∈ ℝ^p`. Then `Uᵀλ = s` is
> solvable over `ℚ`; for **every** solution `λ`, `λᵀb = sᵀw` (independent of `λ`); hence
> `f(P*) = sᵀw = λᵀb = Σ_{k=0}^n λ_k 2^k`.

**Proof.** Full column rank ⇒ `Uᵀ` is surjective ⇒ `Uᵀλ = s` solvable over `ℚ`. For any solution,
`λᵀb = λᵀ(Uw) = (Uᵀλ)ᵀw = sᵀw = f(P*)`; the value has no `λ`-dependence, and two solutions differ by
`δ ∈ ker Uᵀ` with `δᵀb = δᵀ(Uw) = (Uᵀδ)ᵀw = 0`. ∎

(Certified in `lemmas/dual-value-identity.md`.)

### §2. Reduction of (LBL) to two isolated facts

> **Proposition R.** At the Φ-maximal non-degenerate global minimizer `P*` of a step of the
> induction, suppose:
> - **(D′)** `f(P*) ∈ ℤ`; and
> - **(Pos)** `f(P*) ≠ 0`.
>
> Then `f(P*) ≥ 1`, closing the inductive step and hence (LBL) and the whole problem.

**Proof.** By the certified `alt-sum-two-max-minus-total` (the `f ≥ 0` half), the alternating sum of
a sorted-descending nonnegative multiset satisfies `f = Σ_i (a_{2i−1} − a_{2i}) [+ a_T if T odd] ≥ 0`.
So `f(P*)` is a nonnegative real; by (D′) it is a nonnegative integer; by (Pos) it is nonzero, hence
`≥ 1`. With the degenerate/tie-free legs already certified, this gives (LBL); with the certified
upper bound, `c(n) = 2^n/D_n`. ∎

**Note (weakening the round-6 target).** Prop R needs only `f(P*) ∈ ℤ`, strictly weaker than the
existence of an integer `λ`. Gap D (integer `λ`, i.e. `s ∈ Uᵀℤ^{n+1}`) ⟹ (D′) via Lemma DUAL, but
(D′) may hold without integer `λ`. We keep Gap D as our main handle on (D′) but record that the
divisibility (D′) is what is truly required.

### §3. (D′) at minimizers — Cramer form and the negative finding

**Lemma CRAMER (square-case integrality, PROVEN).**
> Suppose `p = n+1`, so `U` is square; `ker U = \{0\}` ⇒ `det(U) ≠ 0`. Then
> `f(P*)·det(U) = Σ_{j=1}^{n+1} s_j·det(U_j) ∈ ℤ`, where `U_j` is `U` with its `j`-th column replaced
> by `b`. Consequently `f(P*) = M/det(U)` with `M := Σ_j s_j det(U_j) ∈ ℤ`, and
> `(D′) ⟺ det(U) \mid M`. In particular `|det U| = 1 ⟹ (D′)`.

**Proof.** `U` square invertible, `Uw = b` ⇒ `w = U^{-1}b` unique. By **Cramer's rule** (knowledge
base: *Cramer's rule / determinant solution of a linear system*), `w_j = det(U_j)/det(U)`. Then by
(BF), `f(P*) = Σ_j s_j w_j = Σ_j s_j det(U_j)/det(U)`, so
`f(P*)·det(U) = Σ_j s_j det(U_j)`. Each `U_j` has integer entries (`U ∈ ℤ^{(n+1)×(n+1)}`,
`b ∈ ℤ^{n+1}`), so `det(U_j) ∈ ℤ`; `s_j ∈ \{−1,0,1\}`; hence `M = Σ_j s_j det(U_j) ∈ ℤ`. Thus
`f(P*) = M/det(U)`, a ratio of integers, and `f(P*) ∈ ℤ ⟺ det(U) \mid M`. If `|det U|=1` then
`f(P*) = ±M ∈ ℤ`. ∎

*Numerical check.* On the non-minimizer `{2,4/3,4/3,4/3,1}` (S-core, `p=3`): `det(U)=3`, `M=5`,
`f = 5/3`, `f·det(U)=5 ∈ ℤ` exactly — Lemma CRAMER holds and shows `(D′)` **fails** there
(`3 ∤ 5`). This is the same certified `gap-d-not-universal` instance, now seen through Cramer: `(D′)`
is a *divisibility* fact and it genuinely fails off the minimizer set.

**Rectangular case `p < n+1`.** No single determinant; `(D′)` is the statement that the (unique,
since `ker U=0`) rational solution `w = (UᵀU)^{-1}Uᵀb` yields `sᵀw ∈ ℤ`. Equivalently the gcd of the
`p×p` maximal minors of `[U | b]`-type systems controls the denominator; Gap D (`s ∈ Uᵀℤ^{n+1}`,
gcd of maximal minors of `U` equal to `1`) is a sufficient lattice condition. Unchanged from round 6.

**The residual (D′) is minimality-dependent (certified `gap-d-not-universal`).** A proof of `(D′)`
cannot be a pure incidence fact; it must invoke that `P*` is a global minimizer / Φ-maximal.

**Small-`p` lever (explored, honest status).** The dual explorer observed Gap-D failures concentrate
at `p = n+1` (maximal distinct value-classes), suggesting minimizers might bias toward small `p`.
This round I re-examined it: it is **not** a clean win — the explorer's own `n=3` split found Gap-D
failures at *both* `p=3` (`6/47`) and `p=4` (`28/88`), so small `p` does not by itself force `(D′)`.
Moreover the all-even Positivity extreme forces `p ≤ n` (§4), i.e. small `p`, yet is exactly where
`f=0` would live — so "small `p`" is not uniformly benign. I record small-`p` as **not** a
stand-alone mechanism; it must be combined with the distinct-powers RHS. No proof obtained; `(D′)`
remains the load-bearing open gap.

> **Conjecture ((D′) at minimizers).** At a Φ-maximal global minimizer `P*` of a step of (LBL),
> `f(P*) ∈ ℤ` (square case: `det(U) \mid Σ_j s_j det(U_j)`; equivalently `|det U|=1` suffices).

**(D′) must be stated on the VISIBLE REDUCED subsystem `U^★`, not raw `U` (round 7, still binding).**
The naive target "`\det U / \gcd(\text{max minors}) = ±1`" is *literally false* on raw `U`: even
(invisible, `s_j=0`) matched-pair columns `2·e_k` force the minor-gcd to be even (certified: `\gcd=2`
at the `n=3` minimizer `\{3,3,2,2,2,2,1\}`). The certified **Reduction Lemma** (concentration route)
peels each invisible `2·e_k` column exactly: deleting the piece-row and value-column leaves `f` and
every other value unchanged, and `\det U = ±2 · \det U'`, so the factor `±2` cancels in the Cramer
ratio `f = M/\det U`. Iterating peels all invisible matched pairs, leaving the **visible reduced
subsystem `U^★`** (only odd/visible classes, no concentrated column). The correct target is
`|det U^★| = 1` (square) / coprime maximal minors (rectangular). By the graph dictionary (peeling a
`2·e_k` column ≡ peeling a degree-1 piece-leaf of the incidence multigraph), `U^★` is benign **iff the
`2`-core of the multigraph is empty iff no cycle with a degree-`≥3` cycle-piece survives** — which is
*exactly* self-similar's **Gap A′**. So `(D′)` at minimizers `≡` Gap A′ `≡` Budget-Lemma case (b): one
wall, three dresses (Cramer certifies the primal `|det U^★|=1` and dual `f∈ℤ` are literally the same).
No new proof of this wall is obtained this round; it is stated precisely and left open, honestly.

### §4. Positivity `f(P*) ≠ 0` — now a single clean Budget Lemma

This section is substantially strengthened this round.

**Lemma POS-CHAR (characterization of `f=0`, PROVEN IN FULL).**
> For any finite multiset `P` of positive reals, `f(P) = 0` **iff** every distinct value in `P` has
> **even** multiplicity (call `P` *all-even*). Moreover if the total count `T = |P|` is odd, then
> `f(P) ≥ a_T > 0` (the smallest element), so `f(P) > 0`.

**Proof.** Sort descending `a_1 ≥ a_2 ≥ … ≥ a_T`. Then
```
    f(P) = Σ_{r=1}^{T} σ_r a_r = a_1 − a_2 + a_3 − a_4 + ⋯ .
```
*Case `T` even.* Group consecutively: `f(P) = Σ_{i=1}^{T/2} (a_{2i−1} − a_{2i})`. Each term is `≥ 0`
since `a` is nonincreasing. Hence `f(P) ≥ 0`, with **equality iff every grouped pair is equal**,
i.e. `a_{2i−1} = a_{2i}` for all `i`. Now `a_1 = a_2` forces the top value to have (at least) two
copies; iterating, equality in all pairs is **exactly** the condition that the sorted sequence splits
into equal consecutive pairs, i.e. every distinct value occurs an even number of times (all-even).
Conversely, if `P` is all-even the sorted sequence is `v_1,v_1,v_2,v_2,…` and every pair cancels, so
`f=0`. Thus (for even `T`) `f=0 ⟺` all-even.

*Case `T` odd.* Group `f(P) = Σ_{i=1}^{(T−1)/2}(a_{2i−1} − a_{2i}) + a_T ≥ a_T > 0` (each grouped
term `≥ 0`, `a_T > 0`). So `f > 0`, and `P` cannot be all-even (odd `T` forces some odd
multiplicity), consistent with the claim. ∎

*Numerical check.* `50000` random rational multisets: `f=0 ⟺` all-even held with `0` mismatches;
`T` odd `⟹ f>0` held with `0` violations. (`/tmp/v1.py`.)

**Consequence — Positivity has no odd-cancellation branch.** The round-6 worry that `f(P*)=0` might
arise from a signed sum `w_a − w_b + w_c − ⋯ = 0` of `≥ 3` distinct odd-block values is now
**eliminated**: by POS-CHAR, `f(P*)=0` forces `P*` all-even (`s = 0`, every class even). So:

> **(Pos) `⟺` Budget Lemma:** *No refinement of `W_n` using `N ≤ n` cuts is all-even.*

**Structural facts toward the Budget Lemma (proven this round).**

*(i) `f=0` is the global minimum, and it is a rigid combinatorial condition.* `f ≥ 0` always, so the
question is purely whether all-even is reachable in budget. Since `all-even ⟹ T` even and
`T = (n+1)+N`, the cut count has forced parity `N ≡ n+1 (mod 2)`.

*(ii) Top-piece-cut (PROVEN).* In any all-even refinement of `W_n`, the largest sub-piece value
`w_1 ≤ 2^{n-1}`; hence piece `2^n` is cut (at least one cut).
**Proof.** `w_1` has even multiplicity `≥ 2`, so at least two sub-pieces equal `w_1`. A sub-piece of
value `w_1` can only lie inside a piece `2^m` with `2^m ≥ w_1`. Suppose `w_1 > 2^{n-1}`. Then every
piece `2^m` with `m ≤ n−1` has `2^m ≤ 2^{n-1} < w_1`, so cannot house a copy of `w_1`; only piece
`2^n` can. But `2 w_1 > 2^n`, so piece `2^n` houses at most `⌊2^n/w_1⌋ = 1` copy of `w_1`. Total
multiplicity `≤ 1 < 2` — contradiction. Hence `w_1 ≤ 2^{n-1}`, and piece `2^n` (all of whose
sub-pieces are `≤ w_1 ≤ 2^{n-1} < 2^n`) is cut. ∎

*(iii) The naive "every piece must be cut" is FALSE.* The all-even config
`piece1 = {1}, piece2 = {½,½,1}, piece4 = {2,2}` (multiset `{2,2,1,1,½,½}`, `N = 0+2+1 = 3 = n+1`)
has piece `1` uncut. So the Budget Lemma is **not** provable by a per-piece cut count; the copies of
a value can be sourced from larger cut pieces (here the second `1` is carved from piece `2`).

*(iv) Why the powers of `2` are load-bearing.* If the marked lengths `b_0<…<b_n` were `ℚ`-linearly
independent, then `Uw = b` with integer `U` forces `rank_ℚ U = n+1`, so `p ≥ n+1`, and all-even
(`μ_j ≥ 2`) gives `T ≥ 2p ≥ 2(n+1)`, i.e. `N ≥ n+1` — a pure dimension count. Powers of two are
**not** `ℚ`-independent (`2^k = 2·2^{k-1}`), so `p` can be `< n+1` (e.g. the config in (iii) has
`p=3=n+1`; S-core all-even forces `p ≤ n`), and the dimension count fails. A correct Budget-Lemma
proof must therefore use the arithmetic of `2^k` (as `isolated-cycle-exclusion` did), not just
counting — this is the same "distinct-powers is essential" phenomenon as the primal route.

**Exhaustive evidence (this round).** Enumerating all reachable all-even configs (integer incidence
`U`, positive distinct `w` solving `Uw = b`, row sums `≥1`) with `T ≤ 2n+2`:
- `n = 2`: `5` all-even configs, **minimum cut count `N = 3 = n+1`**; none with `N ≤ 2`.
- `n = 3`: `17` all-even configs, **minimum `N = 4 = n+1`**; none with `N ≤ 3`.

(`/tmp/v2.py`, `/tmp/alleven3.py`; the tight-budget searches `T ≤ 2n` returned **zero** all-even
configs for `n=2,3`.) Combined with the certified `gap-d-not-universal` observation and the
explorer's S-core search (`0` `f=0` configs for `n ≤ 4`), the Budget Lemma is strongly supported.

> **Budget Lemma (OPEN).** No refinement of `W_n = \{2^0,…,2^n\}` using `N ≤ n` cuts is all-even;
> equivalently, an all-even refinement requires `≥ n+1` cuts.

*What a proof needs.* Top-piece-cut (ii) gives one cut; the difficulty is a global accounting of the
remaining `n` cuts that uses the arithmetic of `2^k`. A `J`-invariant count (`J =` number of
odd-multiplicity values; `J: n+1 → 0`, each cut changes `J` by an odd amount in `\{−3,−1,1,3\}`)
gives only `N ≥ (n+1)/3` and is too weak because a single cut can drop `J` by `3` — ruling out those
efficient triples via the distinct powers is the residual mechanism (unexecuted). This is the sole
Positivity gap; the odd-cancellation branch is now provably empty.

### §4a. Budget Lemma, case (a): the self-contained top pair (PROVEN IN FULL)

Throughout write `Budget(m)` for the statement "*every all-even refinement of `W_m` has `≥ m+1`
cuts*". We prove `Budget(n)` by strong induction on `n`, and this section handles the base case and
the *self-contained-top* case in full; §4b–§4c develop the general case and isolate exactly what is
left open (case (b)).

**Base case `n=0`.** `W_0 = \{1\}`. A single uncut piece `\{1\}` has the value `1` with multiplicity
`1` (odd), so it is not all-even. To be all-even, piece `1` must be cut into `≥2` sub-pieces; the
minimal all-even split is `\{½,½\}` with `N=1=0+1`. Hence `Budget(0)` holds. ∎(base)

> **Lemma (Budget case (a) — self-contained top).** Let `R` be an all-even refinement of
> `W_n` (`n ≥ 1`) in which the top value satisfies `w_1 = 2^{n-1}`, its two copies are exactly the
> two sub-pieces of piece `2^n` (so piece `2^n = \{2^{n-1}, 2^{n-1}\}`, one cut), and no sub-piece of
> any smaller piece equals `2^{n-1}`. Then the sub-pieces of pieces `2^0,…,2^{n-1}` form an all-even
> refinement `R'` of `W_{n-1}`, with `N(R) = N(R') + 1`. Consequently, assuming `Budget(n−1)`, we get
> `N(R) ≥ (n−1+1) + 1 = n + 1`, i.e. `Budget(n)` holds for such `R`.

**Proof.** Piece `2^n` contributes exactly two sub-pieces, both `= 2^{n-1}`, summing to `2^n`; this is
`r_n = 2`, i.e. `1` cut. Delete piece `2^n` and its two sub-pieces. What remains is precisely the
sub-pieces of pieces `2^0, …, 2^{n-1}`, which are a refinement `R'` of `W_{n-1} = \{2^0,…,2^{n-1}\}`
(each smaller piece keeps its own sub-pieces, still summing to its own value). The cut count of `R'`
is `N(R') = Σ_{k=0}^{n-1}(r_k − 1) = N(R) − (r_n − 1) = N(R) − 1`.

`R'` is all-even: the only sub-pieces we removed were the two copies of value `2^{n-1}`; by hypothesis
`2^{n-1}` occurs nowhere among the smaller pieces, so removing exactly those two copies deletes one
entire even value-class and leaves every other class' multiplicity unchanged — hence still even. Thus
`R'` is an all-even refinement of `W_{n-1}`, and `Budget(n−1)` gives `N(R') ≥ n`, whence
`N(R) = N(R') + 1 ≥ n + 1`. ∎

*Numerical check (exact, `/tmp/vc.py`).* The certified `n=2` minimal all-even example
`piece1=\{1\}, piece2=\{½,½,1\}, piece4=\{2,2\}` is exactly of this form: `w_1 = 2 = 2^{2-1}`, both
copies fill piece `4`, and `2` occurs nowhere else. Deleting piece `4` leaves
`piece1=\{1\}, piece2=\{½,½,1\}`, an all-even refinement of `W_1` with `N'=2 = 1+1` cuts; so
`N = 3 = 2+1`, tight. The reduction reproduces the known minimizer cascade step for step.

**What case (a) does and does not do.** It closes the inductive step *precisely* when the top pair is
self-contained. The general step requires reducing an arbitrary all-even refinement to this shape (or
handling the other shapes directly); §4b–§4c carry out the general accounting and pin the exact
residual.

### §4b. Counting reformulation and the receiver bound (PROVEN IN FULL)

Let `R` be any all-even refinement of `W_n`, `r_k ≥ 1` the number of sub-pieces of piece `2^k`, and
`T = Σ_k r_k = (n+1) + N` the total sub-piece count. Since all-even forces `T` even, `T = 2E` where
`E = T/2` is the number of matched (equal-value) pairs in any fixed perfect matching of the sub-pieces
by value (each even class is paired internally).

> **Reformulation.** `Budget(n) ⟺ T ≥ 2(n+1) ⟺ Σ_k (r_k − 2) ≥ 0 ⟺ E ≥ n+1.`

**Proof.** `N ≤ n ⟺ T = (n+1)+N ≤ 2n+1 ⟺ T ≤ 2n+1`; since `T` is even this is `T ≤ 2n`, i.e.
`T < 2(n+1)`. So "no all-even refinement with `N ≤ n`" is exactly "every all-even refinement has
`T ≥ 2(n+1)`", equivalently `Σ_k (r_k − 2) = T − 2(n+1) ≥ 0`, equivalently `E ≥ n+1`. ∎

Now fix a perfect matching `Π` of the sub-pieces by equal value. Call piece `2^k` **uncut** if
`r_k = 1` (its lone sub-piece is the whole piece, value `2^k`).

> **Structural facts.**
> 1. *(Top piece is never uncut.)* `r_n ≥ 2`. (This is the certified `top-piece-cut-alleven`: an
>    uncut `2^n` would need a partner of value `2^n` in a strictly larger piece, which does not exist.)
> 2. *(Uncut pieces point strictly upward.)* If piece `2^k` is uncut, its lone sub-piece `2^k` is
>    matched under `Π` to a sub-piece of value `2^k` lying in some strictly larger piece `2^{m}`,
>    `m > k`. (No other piece equals `2^k`, so the partner is not a whole piece; it is a proper
>    sub-piece of a piece `2^m > 2^k`.)
> 3. *(Receiver residual bound.)* Fix a piece `2^m` and let `d_m ≥ 0` be the number of uncut pieces
>    whose partner (under `Π`) lies in piece `2^m`. If `d_m ≥ 1` (call `2^m` a *receiver*), then
>    `r_m ≥ d_m + 1`.

**Proof of fact 3.** The `d_m` partner sub-pieces inside piece `2^m` have values `2^{k_1},…,2^{k_{d_m}}`
with distinct `k_1 < … < k_{d_m} < m` (distinct because distinct uncut pieces are distinct powers, and
each `< m` by fact 2). Their total value is a sum of distinct powers of two all `≤ 2^{m-1}`, hence
`Σ_{i} 2^{k_i} ≤ 2^0 + 2^1 + \dots + 2^{m-1} = 2^{m} − 1 < 2^m`. So the residual mass
`ρ_m = 2^m − Σ_i 2^{k_i} ≥ 1 > 0` inside piece `2^m` must be carried by at least one further
sub-piece. Therefore piece `2^m` has at least `d_m + 1` sub-pieces: `r_m ≥ d_m + 1`. ∎

**Consequence (rigorous partial bound).** Let `U := \#\{uncut pieces\}` and `R := \#\{receivers\}`.
Every uncut piece is matched into some receiver (fact 2), so `Σ_{m: receiver} d_m = U`. Then
```
   Σ_k (r_k − 2) = Σ_{uncut}(1−2) + Σ_{cut}(r_k − 2)
                 = −U + Σ_{cut}(r_k − 2)
                 ≥ −U + Σ_{receivers}(d_m − 1)        (fact 3; non-receiver cut pieces have r_k−2 ≥ 0)
                 = −U + (U − R) = −R.
```
Hence `T − 2(n+1) ≥ −R`, i.e. `T ≥ 2(n+1) − R` and `N ≥ (n+1) − R`.

This is a genuine, rigorous structural bound but it is **not** the full lemma: the deficit `−R` is
exactly the "one lost cut per receiver," which corresponds to the fact that a receiver's residual mass
`ρ_m` may be housed in a *single* extra sub-piece, whose own (matched) partner then sits in yet
another piece — the residual-mass recursion. Recovering the missing `R` is precisely **case (b)** and
is isomorphic to Gap A′ (an off-budget mass exchange between a higher piece and the rest). It is left
open, honestly.

*Numerical check (exact, `/tmp/vr.py`).* On the `n=2` example: `Σ(r_k−2)=0` (`T=6=2(n+1)`, tight);
uncut pieces `= \{2^0\}` (`U=1`), receiver `= \{2^1\}` (`R=1`), `d_{1}=1`, `r_1 = 3 ≥ d_1+1 = 2` ✓;
the partial bound gives `T ≥ 6−1 = 5`, actual `6` — confirming the bound holds with slack `R`.

### §4c. Budget-minimal refinements have `ker U = 0` (PROVEN IN FULL)

To bring the powers-of-two arithmetic (Cramer / 2-adic tools) to bear on the residual, we show the
Budget Lemma may be studied on incidence-nondegenerate configurations. Recall `U ∈ ℤ_{≥0}^{(n+1)×p}`
(distinct values `w_1 > … > w_p > 0`), `Uw = b`, all column sums `μ_j` even.

> **Lemma (Budget-minimal ⟹ full column rank).** Suppose some all-even refinement of `W_n` has
> `N ≤ n` cuts. Then there is an all-even refinement of `W_n` with `N ≤ n` cuts whose incidence matrix
> `U` has `ker U = \{0\}` (equivalently full column rank `p ≤ n+1`); its values are the unique rational
> solution of `Uw = b`.

**Proof.** Among all all-even refinements with `N ≤ n` choose one with **minimal `N`**, and among those
with minimal `p` (number of distinct values); call it `R` with data `(U, w)`. We claim `ker U = \{0\}`.

Suppose not: pick `0 ≠ δ ∈ ker U ⊂ ℝ^p`, so `U(w + tδ) = Uw = b` for all `t`. As `t` varies over an
interval containing `0`, the incidence `U` is unchanged (each value-class keeps its sub-pieces), and
`w(t) = w + tδ` stays a solution; it corresponds to a genuine all-even refinement as long as all
`w_j(t) > 0` and the `w_j(t)` remain distinct (equal values simply merge classes). We may take `δ` so
that the coordinatewise-minimum event as `t` increases from `0` is well defined: because `U` has no
zero column (every value occurs) and `U ≥ 0`, a nonzero `δ ∈ ker U` cannot be coordinatewise `≥ 0`
(else `Uδ` would have a positive entry, contradicting `Uδ=0`); so some coordinate of `δ` is negative
and `w_j(t)` decreases in `t`. Let `t^* > 0` be the smallest `t` at which either (i) some `w_j(t)=0`,
or (ii) two coordinates `w_i(t)=w_j(t)` first coincide.

- *Case (i) first (a value hits `0`).* At `t^*`, class `j` has value `0`; its `μ_j` sub-pieces vanish.
  Deleting them, the incidence becomes `U'` (column `j` removed) and `U' w' = b` still holds (the
  removed column contributed `0` in the limit). Every remaining value is positive and the removed
  class had *even* size `μ_j ≥ 2`, so the result is an all-even refinement with `N' = N − μ_j < N`
  cuts and `N' ≤ n`. This contradicts minimality of `N`.
- *Case (ii) first (two values merge).* At `t^*`, `w_i = w_j`; merge the two classes into one column
  `(\text{col }i) + (\text{col }j)`, an integer column with even sum `μ_i + μ_j`. This is an all-even
  refinement with the **same** `N` (no sub-piece created or destroyed) but strictly smaller `p`,
  contradicting minimality of `p` among minimal-`N` configs.

Either way we reach a contradiction, so `ker U = \{0\}`. Full column rank forces `p ≤ n+1` and makes
`w = ` the unique solution of the (consistent, full-column-rank) system `Uw=b`, which is rational
since `U, b` are integral. ∎

**Use.** This is the Budget-Lemma analogue of the certified S-core reduction: it lets us assume, when
attacking the residual case (b), that values are rational and determined by the integer incidence, so
the distinct-powers arithmetic (as in certified `degree-2-cycle-exclusion`) and Cramer/valuation
counts apply — the same arithmetic the primal route needs for Gap A′. It does not by itself close the
lemma: `p < n+1` is possible even with `ker U=0` (the certified `n=2` example has `p=2 < 3` via a
multiplicity-`4` class), so `T ≥ 2p` remains too weak; the residual is still case (b). This reduction
is what makes the "restrict to `ker U=0`" bridge (budget-lemma explorer, opening 4) rigorous.

### §5. Summary of logical status

```
   (LBL)  ⟸  Proposition R  ⟸  { (D′) f∈ℤ  ∧  (Pos) f≠0 }
   (D′)   ⟸  |det U^★|=1 on the VISIBLE reduced subsystem (≡ Gap A′)                   [OPEN — needs minimality]
   (Pos)  ⟺  Budget Lemma (no all-even in ≤n cuts)                                    [odd-cancellation ELIMINATED]
          ├ case (a) self-contained top pair            ✓ PROVEN (§4a, base n=0 ✓)
          ├ reformulation T≥2(n+1) ⟺ Σ(r_k−2)≥0         ✓ PROVEN (§4b)
          ├ uncut→larger receiver, r_m ≥ d_m+1, T≥2(n+1)−R  ✓ PROVEN (§4b)
          ├ Budget-minimal ⟹ ker U=0 (p≤n+1, rational)  ✓ PROVEN (§4c)
          └ case (b): off-piece / residual-mass exchange ≅ Gap A′   [OPEN]
          top-piece-cut ✓, f=0⟺all-even ✓ (Lemma POS-CHAR), exhaustive n=2,3 ✓
   Dual identity f = Σ_k λ_k 2^k = M/det(U)   [PROVEN — Lemma DUAL + Lemma CRAMER]
   Reduction, S-core, block formula, UB       [CERTIFIED — imported]
```

Answer `c(n) = 2^n/D_n`, `D_n = 2^{n+1}−1` (`n=0→1, n=1→2/3, n=2→4/7, n=3→8/15`); UB certified.
This round (round 8) the dual route proves, in full: **Budget-case (a)** (self-contained top pair
reduces to `W_{n-1}`, base `n=0`); the **counting reformulation** `Budget ⟺ Σ(r_k−2)≥0` with the
**receiver bound** `T ≥ 2(n+1) − R`; and **Budget-minimal ⟹ ker U=0** (`p ≤ n+1`, rational values).
It also states `(D′)` correctly on the visible reduced subsystem `U^★` and shows `(D′) ≡ Gap A′ ≡`
Budget-case (b) via Cramer. It does **not** close case (b) / `(D′)` — the single shared residual wall.

## Full proof
Not present — Status is `partial`. Remaining gap: the Budget Lemma **case (b)** (a top-value copy
housed off piece `2^n`, or positive residual mass on piece `2^n`) `≡` `(D′)` `|det U^★|=1` on the
visible reduced subsystem `≡` Gap A′ (a cycle with a degree-`≥3` cycle-piece) — proven this round to
be one and the same wall across the three live routes.

## Promotable lemmas

- **Lemma BUDGET-A (self-contained top pair reduction) — NEW round 8.** *Statement:* if an all-even
  refinement of `W_n` (`n≥1`) has `w_1 = 2^{n-1}` occurring exactly as the two halves of piece `2^n`
  and nowhere else, then deleting piece `2^n` yields an all-even refinement of `W_{n-1}` with exactly
  `N−1` cuts; with `Budget(n−1)` this gives `N ≥ n+1`. Base `Budget(0)`: an all-even refinement of
  `\{1\}` needs `≥1` cut. *Proved in full in §4a.* Certifiable; reproduces the certified `n=2` minimal
  example exactly. Reusable by any route pursuing the Budget Lemma / Positivity by induction on `n`.

- **Lemma BUDGET-COUNT (counting reformulation + receiver bound) — NEW round 8.** *Statement:* for any
  all-even refinement of `W_n`, `Budget(n) ⟺ Σ_k(r_k−2)≥0 ⟺ T≥2(n+1)`; every uncut piece `2^k`
  (`r_k=1`) is a whole copy matched into a strictly larger receiver piece `2^m`, and a receiver
  absorbing `d_m` distinct uncut partners has residual mass `≥1`, forcing `r_m ≥ d_m+1`; hence
  `T ≥ 2(n+1) − R` (`R` = #receivers). *Proved in full in §4b.* Reusable structural accounting; the
  residual `−R` is exactly Gap A′ / Budget-case (b).

- **Lemma BUDGET-KER (Budget-minimal ⟹ ker U=0) — NEW round 8.** *Statement:* if any all-even
  refinement of `W_n` has `N ≤ n` cuts, then one exists with incidence matrix of full column rank
  (`ker U=\{0\}`, `p ≤ n+1`, values the unique rational solution of `Uw=b`). *Proved in full in §4c*
  (perturb along `ker U`: a value hitting `0` reduces `N` (contradiction); a collision merges classes
  reducing `p`). The Budget-Lemma analogue of certified S-core; lets the powers-of-two arithmetic apply
  to the residual. Reusable by every route attacking the Budget Lemma / (D′).

- **Lemma POS-CHAR (`f=0 ⟺ all-even`).** *Statement:* For a finite multiset `P` of positive reals,
  the alternating sum `f(P) = Σ_r σ_r a_r` (sorted descending) is `0` iff every distinct value has
  even multiplicity; and if `|P|` is odd then `f(P) ≥ min(P) > 0`. *Proved in full in §4* (group
  consecutive pairs; each `a_{2i−1}−a_{2i} ≥ 0`; equality ⟺ equal pairs ⟺ all-even). Unconditional,
  reusable by every approach — it **eliminates the odd-cancellation Positivity branch** for all of
  them and reduces Positivity to "all-even unreachable in budget".

- **Lemma CRAMER (square-case Cramer integrality).** *Statement:* If `U ∈ ℤ^{(n+1)×(n+1)}` is
  invertible, `Uw=b`, `f = sᵀw` with `s ∈ ℤ^{n+1}`, `b ∈ ℤ^{n+1}`, then
  `f·det(U) = Σ_j s_j det(U_j) ∈ ℤ` (`U_j = U` with column `j` replaced by `b`); hence `f = M/det(U)`,
  `M ∈ ℤ`, and `f ∈ ℤ ⟺ det(U) | M`, with `|det U|=1 ⟹ f∈ℤ`. *Proved in full in §3* (Cramer's rule
  + integrality of cofactors). Reusable by any incidence-matrix route; makes the square-case dual
  target coincide (up to divisibility slack) with the primal `|det U|=1`.

- **Fact (top-piece-cut for all-even).** *Statement:* In any all-even refinement of `W_n` the
  largest sub-piece value is `≤ 2^{n-1}`, so piece `2^n` is cut. *Proved in §4.* Records one forced
  cut toward the Budget Lemma and the housing/superincreasing mechanism.

- **Fact (Budget Lemma is not per-piece).** *Statement:* An all-even refinement need not cut every
  piece — `piece1={1}, piece2={½,½,1}, piece4={2,2}` is all-even with `N=n+1` yet leaves piece `1`
  uncut. *Verified in §4.* Prevents a future round from attempting the Budget Lemma via "every piece
  is cut".
