## imo-2026-03 — lens: Budget Lemma (Positivity gap, dual-integer-certificate)

### Exact statement to prove
`W_n = {2^0, 2^1, ..., 2^n}` (n+1 "pieces"). A **refinement** replaces each piece `2^k` by a
finite set of positive sub-pieces summing to `2^k` (a "cut" = one extra sub-piece; if piece `k`
gets `r_k ≥ 1` sub-pieces that is `r_k − 1` cuts). Total cuts `N = Σ_k (r_k−1)`; total sub-piece
count `T = Σ_k r_k = (n+1) + N`. A refinement is **all-even** if every distinct value occurring
among the `T` sub-pieces has even multiplicity (equivalently, by certified `pos-char`, iff
`f = 0`, the alternating sum of the sorted-descending sub-pieces).

**Budget Lemma (still OPEN):** no all-even refinement of `W_n` exists with `N ≤ n` cuts;
equivalently every all-even refinement needs `N ≥ n+1` (`T ≥ 2n+2`).

Algebraically: let `U ∈ ℤ_{≥0}^{(n+1)×p}` be the piece×value incidence matrix (row sums `r_k≥1`,
`p` = number of distinct sub-piece values `w_1>...>w_p>0`), `b=(1,2,...,2^n)ᵀ`. All-even means
every column sum `μ_j = Σ_k U_{k,j}` is even. Want: `Uw=b`, all `μ_j` even `⟹ Σ_j μ_j ≥ 2(n+1)`.

### What I verified computationally this round (exact, sympy/Fraction, brute force)
- **n=2:** exhaustive search over integer incidence matrices (row sums ≤4, all p=1,2,3) found
  **no** all-even solution with `N ≤ 1` (only candidate below the parity-forced floor `N=3`).
  Minimum confirmed `N=3=n+1`. One example at `p=2` (fewer than `n+1` distinct values!):
  `U` rows `(0,1),(0,2),(2,1)` giving `w=(3/2,1)`, column sums `(2,4)` — **all-even with only 2
  distinct values**, `T=6=2(n+1)`, `N=3`. This refutes any "p ≥ n+1 forces the bound" reduction
  (see Cheap-kill candidates below — it looked promising, it's FALSE).
- **n=3:** exhaustive search (row-sum cap 4, p=2,3,4) found **no** all-even config with
  `N ≤ 2`. Consistent with explorer/round-7's exhaustive claim (min `N=4=n+1`).
- Parity fact (cheap, exact): all-even `⟹ T` even `⟹ N ≡ n+1 (mod 2)`. For `n=2` this alone
  excludes `N=2` but NOT `N=1` — the real work is ruling out `N=1` (done above by search, not yet
  by proof).

### Distinct proof openings
1. **Peeling induction via top-piece-cut, case-split on residual mass (most promising this round).**
   By certified `top-piece-cut-alleven`, the top value `w_1 ≤ 2^{n-1}` and piece `2^n` is cut. Two
   sub-cases on how the (≥2, even) copies of `w_1` are housed:
   - *(a) exactly 2 copies of `w_1`, both inside piece `2^n`, and `2w_1 = 2^n` exactly (`w_1=2^{n-1}`,
     residual `R = 2^n − 2w_1 = 0`).* Then piece `2^n` contributes exactly 1 cut and vanishes from
     the accounting entirely; the remaining refinement (of `W_{n-1} = {2^0,...,2^{n-1}}` only) is
     **itself all-even** (the two `w_1` copies are fully self-contained) — apply the Budget Lemma
     inductively to `W_{n-1}`: `N' ≥ n` by induction, total `N = 1 + N' ≥ n+1`. **I verified this
     case exactly reproduces the certified n=2 minimal example**: top piece `{2,2}` (`w_1=2=2^{2-1}`,
     `R=0`, 1 cut), and the leftover refinement of `W_1={1,2}` is `piece1={1}, piece2={½,½,1}` —
     itself all-even (`1` has mult 2, `½` has mult 2) with exactly `N'=2=Budget(W_1)` cuts. Clean,
     closes tight.
   - *(b) `w_1 < 2^{n-1}` strictly, or `w_1=2^{n-1}` but a copy of `w_1` is housed OUTSIDE piece `2^n`
     (e.g. piece `2^{n-1}` left uncut and equal to `w_1`), or piece `2^n` has residual mass
     `R = 2^n − (\text{mass of } w_1\text{-copies in it}) > 0` that must be absorbed elsewhere.*
     This is the hard case — the residual `R` (or the "extra" `w_1` copy sourced from a smaller
     piece) couples piece `2^n`'s cut-budget to the rest of the pieces in a way NOT reducible to a
     clean `W_{n-1}` instance. **This is structurally the SAME difficulty as the self-similar
     route's Gap A′ residual ("a cycle carrying a cycle-piece of degree ≥3" / off-cycle mass) — an
     off-budget mass exchange between the top piece and the rest.** Flag this explicitly for the
     outliner: closing Budget-Lemma case (b) may require (or be equivalent to) closing Gap A′.
   - Recommend: build out case (a) as a clean certifiable sub-lemma (it is a genuine, self-contained
     induction step), and treat case (b) as the residual — explicitly cross-reference it against
     Gap A′ so effort isn't duplicated across routes.
2. **Matched-pair / reachability duality (uses certified GAP-U machinery).** All-even ⟺ the `T`
   sub-pieces admit a perfect matching by equal value (pair up each even class). This is exactly
   the "invisible matched pair" object from certified `delete-subtract-reachability` /
   `subset-sum-pigeonhole` (used to PROVE the upper bound). Idea: run the DELETE/SUBTRACT reduction
   (which collapses `m` visible pieces to 1 in `m−1` steps) in **reverse** — an all-even multiset,
   viewed via its pairing, should be "buildable" from `W_n` using exactly the SUBTRACT-inverse and
   DELETE-inverse moves, and count how many such moves are forced. This reuses certified machinery
   instead of building new tools, but I did NOT work out whether it actually forces `N≥n+1` — flagged
   as unexecuted, promising because it's a reuse of an airtight existing lemma rather than new
   arithmetic.
3. **Direct dimension/rank argument — REFUTED as stated.** The natural idea "all-even needs `p≥n+1`
   distinct values (else `rank_ℚ U < n+1` can't hit the independent-looking `b`), and all-even gives
   `T≥2p≥2(n+1)`" is **FALSE** as a clean 2-step argument: the `n=2` example above has `p=2<n+1=3`
   but still `T=2(n+1)` because one value class has multiplicity 4 (not 2). So `T≥2p` is true but
   not tight when `p<n+1`; a workable version of this lever would need `Σμ_j = T` directly, not
   `2p`, i.e. it collapses back to needing the full accounting — no shortcut found here.
4. **2-adic valuation / superincreasing telescoping analogous to `degree-2-cycle-exclusion`.** Not
   directly applicable since sub-piece values need not be rational a priori (only forced rational
   when `p ≤ n+1` and `ker U=0`, via Cramer). Possible angle: restrict to `ker U=0` configs first
   (argue, as in S-core, that a MINIMAL-`N` all-even config must have `ker U=0` — else a value could
   be perturbed to reduce mass while staying all-even, contradicting minimality) — this ports the
   S-core machinery to the Budget Lemma and may let the primal route's arithmetic tools apply
   directly. Unexecuted; flagged as a bridge.

### Cheap-kill candidates
- Parity floor `N ≡ n+1 (mod 2)` — cheap, already known, insufficient alone (rules out only every
  other value of `N`).
- `p ≥ n+1` as a stand-alone lever — **REFUTED** this round (see opening 3 / the `p=2,n=2` example).
  Do not propose this to the outliner as a quick win.
- "Every piece is cut" — already REFUTED (certified companion fact in `top-piece-cut-alleven.md`).

### Knowledge-base entries to use
- Cramer's rule / determinant solution of linear systems (already used via certified Lemma CRAMER;
  relevant again if pursuing opening 4's `ker U=0` restriction).
- Any KB entries on induction/strong induction and monovariants — the peeling induction (opening 1)
  is a textbook strong-induction-on-`n` shape once case (a)/(b) is settled.
- (Check `knowledge_base.md` for an explicit "invariant/monovariant" or "extremal principle" entry
  to formalize opening 1's induction rigorously — I did not find a dedicated new entry beyond what's
  already cited by the certified lemmas in this route.)

### Analogous past problems (cruxes)
Searched `combinatorics` subtopics `p-adic-valuation`, `invariants-and-monovariants`,
`size-bounding-and-descent` for powers-of-two / parity / even-multiplicity techniques.
- **aimo-0019** (paint-pot game on `[0,1]` with dyadic ink `1/2^m`): crux "bound a family of
  dyadic-length pieces of pairwise distinct sizes by twice the largest, via the geometric sum of
  distinct negative powers of two." Same *flavor* (dyadic pieces, distinctness, geometric-sum
  bounding) but the game mechanics are different (adversarial ink-depletion, not a fixed-budget
  cut-count problem) — **partial analogy only**, useful for the "bound by twice the largest" style
  argument (echoes top-piece-cut's `w_1≤2^{n-1}` bound) but not a template for the Budget Lemma's
  accounting.
- **aimo-0236** (Alice/Bob board game with `+a` / `/2` moves, terminates iff `ν_2(x)<ν_2(a)` for
  all `x`): crux is a clean `ν_2`-invariant argument. Genuinely different problem (no all-even /
  cut-count structure) but illustrates the general pattern "count total `ν_2` across a multiset as
  an exact move-count" — a template shape (if a rational reformulation of the Budget Lemma's `w_j`
  values is found) but **not directly transplantable** since our `w_j` are not integers in general.
- No crux found that is a close structural match to "minimum cuts to make a superincreasing
  sequence's refinement all-even" — report this as **no strong match**, do not force either of the
  above as a template; they're technique-flavor hints only.

### Prior progress (from dual-integer-certificate.md, certified)
- Lemma POS-CHAR (certified): `f=0 ⟺ all-even`; odd-`T ⟹ f>0`. Kills odd-cancellation branch.
- Lemma CRAMER (certified): square-case `f·det(U) ∈ ℤ`.
- top-piece-cut-alleven (certified): `w_1 ≤ 2^{n-1}`, piece `2^n` cut; "every piece cut" refuted.
- Exhaustive n=2 (5 all-even configs, min N=3), n=3 (17 configs, min N=4) — I independently
  re-verified the N-minimum claim by a from-scratch brute-force search this round (different code
  path, same conclusion): no config with `N≤n-1` for n=2,3.

### Dead ends (do not retry)
- `p≥n+1` as a stand-alone forcing mechanism for the Budget Lemma — REFUTED this round (n=2 example
  with `p=2`, `T=6=2(n+1)` via one multiplicity-4 class).
- "Every piece must be cut" — already certified-refuted (companion fact in top-piece-cut-alleven.md).
- Odd-cancellation branch of Positivity — already CLOSED (POS-CHAR).

### Small-case / intuition notes (labeled conjecture except where noted PROVEN)
- CONJECTURE (numerically confirmed n=2,3, exhaustively within bounded search): Budget Lemma is
  true, min `N = n+1` exactly, achieved with the top-piece pair `w_1=2^{n-1}` (residual `R=0`
  case) recursively cascading down to `W_0={1}` (trivially needs 0 further all-even work since a
  single element can't be all-even alone... actually base case: for `n=0`, `W_0={1}`, an all-even
  refinement of a single piece needs `≥1` cut to split `1` into `{v,v}` — matches `N≥0+1=1`).
  Suggests the induction bottoms out cleanly at `n=0`, reinforcing opening 1 as the right shape.
- PROVEN this round (exact computation): the `n=2` certified minimal all-even example decomposes
  EXACTLY per opening 1's case (a) (`R=0` induction), giving concrete evidence the peeling induction
  is the right proof shape, contingent on handling case (b) (residual/off-piece mass) — which looks
  isomorphic to Gap A′.

### Which opening looks most promising to close this round
**Opening 1 (peeling induction, case (a) proven exactly by example, case (b) open)** — recommend
building this out as the primary attempt. Its case (a) is a genuinely NEW, self-contained,
provable induction step (not yet certified anywhere) that would handle a meaningful sub-case
outright. Its case (b) should be EXPLICITLY flagged to the outliner as likely equivalent in
difficulty to Gap A′ (self-similar route) — if so, closing either one first may crack both, which
is consistent with round 7's "all three routes hit one wall" observation. Opening 2 (reuse of
certified DELETE/SUBTRACT reachability machinery) is the best "cheap, no-new-arithmetic" fallback
if opening 1's case (b) resists — it reuses airtight existing lemmas rather than inventing a new
invariant.
