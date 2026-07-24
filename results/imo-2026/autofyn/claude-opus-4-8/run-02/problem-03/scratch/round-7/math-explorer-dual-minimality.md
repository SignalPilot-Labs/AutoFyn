## imo-2026-03 (Route 2 dual: minimality ⇒ Gap D at minimizers + Positivity)

### Distinct openings

1. **Naive KKT / complementary-slackness "single Lagrange multiplier per piece" idea — TESTED, REFUTED.**
   Idea: within a fixed rank-order chamber, minimizing the linear functional `sᵀx` over the product-of-simplices
   polytope `∏_k Δ_k` gives (for a non-degenerate `x_i>0`) the stationarity condition `s_i = μ_{k(i)}` (a single
   scalar per piece `k`), which would force every value-class touched by a given piece to carry the *same* sign
   `s_j`, and hence hand you an explicit integer dual `λ_k=σ(k)∈{-1,0,1}` almost for free. **This is FALSE at
   ties.** The subgradient of the rank/alternating-sum functional at a tied value-class of size `μ_j≥2` is not a
   single number but the full interval `[-1,1]` (any tie-breaking permutation reshuffles which raw sub-piece gets
   which of the block's alternating ranks), so naive per-coordinate KKT is vacuous whenever `μ_j≥2`, which is
   exactly the generic case at a tied minimizer. **Numerically confirmed dead**: enumerated all S-core
   (`ker U=0`) tied configurations for `n=2` (17 configs) and `n=3` (136 configs) via exact rational
   `U w = b` solves; the "same-sign-per-piece" property FAILS on 4/17 (n=2) and 83/136 (n=3) of all S-core
   configs, and — critically — still fails even restricted to the actual `f=1` global minimizers: **2/4 (n=2)
   and 5/9 (n=3) minimizers violate it.** So this is not merely a non-minimizer artifact; it is flatly false as
   a structural fact about minimizers. Do not pursue naive per-variable KKT/complementary-slackness for Gap D —
   the real constraint must come from the *secondary* Φ-maximality selection among the (larger) tied-minimizer
   set, i.e. it is a second-order / nested optimization fact, consistent with what `phimax-trivial-kernel`
   (S-core) already captures — this line does not add anything beyond what's certified.

2. **"μ_j odd ⇒ μ_j = 1" conjecture at minimizers — TESTED, REFUTED (with an important caveat).**
   If true this would trivialize Gap D (each odd class would carry a single sub-piece, and an explicit
   `λ_k=±1,0` dual would follow directly from the block structure). Counterexample found by exhaustive search:
   `n=2`, `U=[[0,1],[1,0],[2,0]]`, `w=(2,1)`, `mu=[3,1]`, giving the config `{2,2,2,1}` (piece "2" untouched,
   piece "4" bisected into `2,2`) with `f=1` (a genuine global minimizer) — value-class `w=2` has `μ_j=3` (odd,
   `s_j=+1`), **not** `μ_j=1`. **However this counterexample is entirely integer/dyadic** (an exact bisection of
   a power-of-two piece), so it already lies in the case CLOSED by `integer-parity-alt-sum` (Theorem F) — it is
   *not* an instance of the open non-integer tied residual. Re-running the search restricted to integer-valued
   `w`, and separately hunting specifically for **non-integer** `f=1` minimizers for `n=2` (mult ≤4, rowcap 3)
   and `n=3` (mult ≤3, rowcap up to 4): **found ZERO non-integer S-core minimizers** in either search (147
   configs enumerated for n=3). This is consistent with (and sharpens) the existing conjecture that Gap D +
   integrality hold exactly at the true minimizer, but the μ_j=1 mechanism specifically is refuted as the
   *reason why* — whatever forces integrality at minimizers is not simply "odd classes are singletons."

3. **A genuinely different top-level target: attack `f ≥ 1` on S-core configs as ONE continuous inequality,
   bypassing the Gap-D/Positivity SPLIT entirely.** Instead of (a) proving `f∈ℤ` via an integer dual `λ` and
   then (b) separately proving `f≠0`, ask directly: does any S-core (`ker U=0`, `Uw=b`, `w` positive
   strictly-decreasing) configuration satisfy `0 < f < 1`? If this continuous inequality can be shown directly
   (e.g. via a bound on `f` in terms of `1/|det(U)|` combined with a *separate*, purely combinatorial bound that
   any S-core config reachable in ≤n cuts has `|det(U)| ≤` some explicit small value, or via a direct
   Cramer's-rule argument), Gap D and Positivity dissolve simultaneously as a corollary rather than needing two
   independent proofs. Concretely, for the SQUARE case (`p=n+1`), Cramer's rule gives
   `w_j = det(U_j)/det(U)` (`U_j`= U with column j replaced by b), so `f = Σ_j s_j·det(U_j) / det(U)`, an exact
   ratio of two INTEGERS (since U, b are integer matrices) — `f·det(U) ∈ ℤ`. If one could show this numerator
   is nonzero (⇔ Positivity, in integer form) AND `|det(U)|=1` (⇔ Gap A/Gap D exactly, since for square U the
   maximal-minor gcd condition IS `|det U|=1`), one gets `f ≥ 1` directly — but this is exactly the SAME
   underlying fact (minimality⇒benign U) already flagged in current.md as the shared wall, just written via
   Cramer's rule instead of Smith normal form; it is a cleaner presentation, not an escape. For the NON-SQUARE
   case (`p<n+1`, overdetermined `Uw=b`), solvability itself is already a strong constraint — numerically I
   split the `n=3` search by `p` and found Gap-D failures occur at BOTH `p=3` (6/47 configs, non-square) and
   `p=4` (28/88, square); non-squareness alone does not make Gap D easier or automatic, so this avenue does not
   cheaply bypass the wall either, but the *split by p* (fewer classes ⇒ more overdetermined ⇒ possibly a
   cleaner minimality argument for small p) may be worth a dedicated look — most FAILING configs concentrate at
   `p=n+1` (square, maximal number of distinct classes), suggesting minimizers may have a bias toward SMALL p
   (few distinct value-classes) — an unexplored angle: does Φ-maximality or minimality force p small, and does
   small p make Gap D easier? Flagging as untested but promising; did not have budget to pursue further this
   round.

4. **Positivity gap: no new mechanism found, but strong numerical support for the "budget" route.**
   Searched S-core configs of `n=2,3` for any `f=0` occurrence; found NONE (0/17 for n=2, 0/136 for n=3, within
   the search's mult/rowcap bounds). This is consistent with (but does not prove) the existing conjectured
   mechanism in `dual-integer-certificate.md` §4 ("all-even needs `N≥n+1` cuts, one more than the `≤n` budget
   allows"). I did not find a clean proof of this budget statement, nor a working alternative to the refuted
   λ₀-parity mechanism, within this round's time. This remains genuinely open.

### Candidate technique(s)
- Cramer's-rule reformulation of Lemma DUAL for the square case (`f = Σ s_j det(U_j)/det(U)`) — a clean
  restatement, not a new lever, but may make the outliner's writeup crisper (ties Gap D directly to `det U=±1`
  rather than the abstract lattice-gcd language, in the square case).
- Splitting the Gap-D analysis by `p` (number of distinct value-classes) — the failure rate concentrates at
  `p=n+1` (square/maximal); worth checking whether minimality biases toward small `p`.
- Still recommend: **do not** re-attempt naive per-variable KKT/complementary-slackness (dead, item 1); **do
  not** re-attempt "μ_j odd ⇒ μ_j=1" as a blanket minimizer fact (dead, item 2, though the refuting example is
  itself in the already-closed integer/dyadic case — a useful footnote, not a new gap).

### Cheap-kill candidates
- None new found this round beyond what's already certified (S-core / phimax-trivial-kernel already IS the
  cheap structural pruning available). The `p`-split observation (item 3) is a possible pigeonhole-style cheap
  kill if it can be shown minimizers always have small `p` — untested.

### Knowledge-base entries to use
- No new `knowledge_base.md` entries beyond what prior rounds already use (Φ-maximal selection / convexity,
  unimodularity). Grepped for "unimodular / lattice / determinant / Cramer" — only a passing lattice-counting
  entry, not directly applicable.

### Analogous past problems (cruxes)
- Searched `past_crux_moves_database.json` for unimodular/determinant/lattice/KKT techniques. Two weak
  analogies, neither a strong match:
  - `aimo-0180` (combinatorics, `bijections-and-encoding` + `extremal-principle`): reads `|det(P_i,P_j)|=1` as
    a unimodular-triangle-area condition and bounds the count of such "good" pairs via a farthest-point
    extremal argument. Loosely analogous in spirit (unimodularity + an extremal/farthest selection playing the
    role our Φ-maximality plays) but the combinatorial content (counting good pairs among lattice points) is
    unrelated to our incidence-matrix Gap D. Not a genuine template.
  - `aimo-0149` (combinatorics, `extremal-principle`): characterizes the unknown configuration as the *unique*
    weight-maximizing N-point set (a concave weight function peaking on the true set) — structurally similar in
    flavor to our Φ=Σx² secondary-maximality selection among tied minimizers, but the mechanism (concave
    single-variable weight vs. our multi-piece incidence-matrix lattice condition) doesn't transfer concretely.
  - **No genuinely analogous crux found** for the specific Gap-D (integer solvability of `Uᵀλ=s` restricted to
    minimizers of a combinatorial game) — this appears to be a bespoke structure without a close corpus match.

### Prior progress
- Lemma DUAL (dual-value-identity, certified): `f=sᵀw=λᵀb` for any rational `λ` solving `Uᵀλ=s`.
- Fact (gap-d-not-universal, certified): Gap D fails off the minimizer set (`{2,4/3,4/3,4/3,1}`, `det U=±3`).
- This round's additions (not yet certified — report only, for outliner to decide): the KKT/same-sign-per-piece
  refutation and the μ_j=1 refutation (both negative results, prevent future re-attempts); the Cramer's-rule
  reformulation; the `p`-split observation (positive-lead, untested).

### Dead ends (do not retry)
- Naive per-variable KKT/complementary-slackness ("each piece's non-degenerate sub-pieces share one Lagrange
  multiplier / one sign") — REFUTED both generally on S-core configs (83/136 for n=3) and specifically at
  minimizers (5/9 for n=3). The subgradient at any tied value-class of size ≥2 is the full interval `[-1,1]`,
  not a point, so this KKT form is vacuous exactly where it would need to bite.
- "μ_j odd ⇒ μ_j=1" as a blanket minimizer property — REFUTED by the dyadic bisection example `{2,2,2,1}`
  (n=2, f=1, μ=3 class). (Caveat: this counterexample is itself already in the CLOSED integer/dyadic case, so
  it doesn't touch the open non-integer residual directly, but it kills the conjecture as stated.)
- λ₀-parity Positivity mechanism — already flagged dead in round 6, reconfirmed no alternative found this round.

### Small-case / intuition notes (conjectural, numerically checked)
- Exhaustive rational search (n=2: 17 S-core configs; n=3: 136–147 S-core configs, mult ≤3-4, cut-budget-
  respecting) found **zero** non-integer `f=1` minimizers and **zero** `f=0` S-core configs — strong numerical
  support for both Gap D and Positivity holding exactly at minimizers, consistent with all prior rounds, but
  the search space is still small (bounded multiplicities/row-cap) and not a proof.
- Gap-D failures split by number of distinct value-classes `p`: for n=3, failures occur at both `p=3`
  (6/47, non-square/overdetermined) and `p=4` (28/88, square) — non-squareness does not automatically save Gap
  D, but the *concentration* of failures at `p=n+1` (maximal p) is suggestive that minimizers may be biased
  toward smaller `p` — an untested, potentially fruitful cheap structural lead for next round.
