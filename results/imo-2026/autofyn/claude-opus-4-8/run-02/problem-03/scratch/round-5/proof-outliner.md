## imo-2026-03

State recap: upper bound `c(n) ≤ 2^n/D_n` is FULLY PROVEN & CERTIFIED (`delete-subtract-reachability`
+ `subset-sum-pigeonhole`). Every approach below imports it and attacks the SOLE remaining gap: the
lower bound residual **(LBL)** = "every ≤n-cut refinement of `W_n={2^0,…,2^n}` has `f≥1`" at the
tied non-degenerate minimizer. Answer `c(n)=2^n/(2^{n+1}−1)`, `D_n=2^{n+1}−1`, numerically confirmed
(`min f=1`, n≤4). Two integrality routes have shared the tied-vertex wall for 2 rounds — I revise
BOTH with the explorers' concrete new leads AND seed two genuinely different non-integrality framings
(per CLAUDE.md's break-the-plateau mandate).

---

self-similar-recursion: revise
Target: `c(n)=2^n/(2^{n+1}−1)` end to end. UB imported (certified). LB = (LBL), closed by
  integrality AT THE Φ=Σx²-MAXIMAL minimizer via a GENERALIZED (multiplicity-aware) incidence forest.
Technique: strong induction on cut count `N`; at each step select the `Φ`-MAXIMAL global minimizer
  `P*` on the minimizer set `G`; show `P*` integer ⇒ Theorem F ⇒ `f≥1`. DROPS the false Lemma W
  entirely — no restriction of multiplicity edges to bisection leaves.
Skeleton:
  1. Reduce to (LBL); import UB — by certified layer-cake (Lemma L) + Lemma 0 + Invariant (I).
  2. Strong induction on `N`. Degenerate `P*` (some sub-piece 0) → drop it, apply Claim(N−1) — certified leg.
  3. Non-degenerate: choose `Φ`-MAX minimizer `P*` (Weierstrass, `Φ` strictly convex). Build the
     GENERALIZED incidence multigraph `H`: nodes = present pieces ∪ value-components; edge `(k,j)`
     of multiplicity `μ_{k,j}` = #sub-pieces of piece `2^k` in component `C_j` — NO restriction that
     `μ≥2` sit only at bisection leaves (this is the round-4 fix; the `{2,3,3}` killer has a `μ=2`
     edge at a DEGREE-2 piece and IS a forest that peels to integers).
  4. Lemma S′ (kernel-trivial + acyclic) — value vector `w` solves `Uw=(2^k)_k` (`U` = multiplicity
     matrix). Any nonzero `d` with `Ud=0` is a feasible sum-preserving shift line through `P*`:
     nonzero slope contradicts minimality, zero slope contradicts `Φ`-maximality (strict convexity
     of `Φ=Σx_i²` has no interior max on the flat segment). So `ker U={0}`; a cycle would exhibit a
     nonzero kernel vector, so `H` is a forest. [SALVAGES the sound half of the rejected Lemma S.]
  5. Lemma T′ (generalized leaf-peeling) — a degree-1 leaf piece `2^k` with single component of
     multiplicity `μ` gives `μ·w_j=2^k ⇒ w_j=2^k/μ`, INTEGER iff `μ | 2^k` (i.e. `μ` a power of 2).
     Peel, substitute integer into neighbours, repeat; forest ⇒ terminates with all `w_j∈ℤ`.
  6. Integer values, `Σ(P*)=Σ2^k=D_n` odd ⇒ Theorem F ⇒ `f(P*)` odd integer `≥1`. Closes Claim(N).
Key lemmas (claim + mechanism):
  - Lemma S′ — `ker U={0}` and `H` forest — because the ONLY feasible directions off `P*` are
    sum-preserving component shifts, and `Φ`-max + strict convexity kills the flat ones while
    minimality kills the sloped ones (the exact salvaged Lemma-S mechanism, now on a multiplicity graph).
  - Lemma T′ — forest with power-of-two-multiplicity leaves ⇒ integer values — because each peel
    divides `2^k` by `μ`, integral precisely when `μ∈{1,2,4,…}`.
  - **Lemma Φ-EVEN (THE new gap)** — at the `Φ`-MAX minimizer no piece is split into an
    odd-multiplicity (`μ≥3`) set of EQUAL sub-pieces — because equal parts LOCALLY MINIMIZE `Φ`
    (fixed sum+count ⇒ `Σx²` minimized at equality), so a global `Φ`-MAX can never sit at an
    odd-equal split: a feasible `Φ`-increasing perturbation staying in `G` (same `f`, by P1
    invisibility of the moved equal pair against a same-piece third) exists. This guarantees every
    leaf multiplicity in Lemma T′ is a power of 2 (`μ` even or 1), so peeling stays integral.
Open gaps:
  - **Lemma Φ-EVEN** — the odd-equal-split exclusion at the `Φ`-max vertex (the core new content;
    explorer's finding-2 gives exact numeric support: `{2,3,3}` `Φ=35` is dominated by a degenerate
    competitor `Φ=51`, the non-integer continuum `Φ≤45` — bad examples are NOT `Φ`-maximal).
  - The cycle⇒kernel step in Lemma S′ through MULTIPLICITY edges — with `μ_{k,j}>1` a cycle vector
    `d` must satisfy `μ`-ratio consistency around the loop; verify a nonzero `Ud=0` still exists (or
    argue full column rank directly). Builder must check, not assume.
Cases to cover: degenerate (certified); non-degenerate `Φ`-max with even-multiplicity leaves (peel),
  odd-multiplicity EQUAL splits (excluded by Φ-EVEN), simple cross-ties (0/1 forest edges).
Watch out for: MUST NOT reintroduce Lemma W (false — `{2,3,3}`) or GLOBAL integrality (false —
  continuum of non-integer `f=1` minimizers); integrality is claimed ONLY at the `Φ`-MAX point. The
  odd-multiplicity leaf is EXACTLY where non-integrality (`{4/3,4/3,4/3,…}`) arises — Φ-EVEN is
  load-bearing, not cosmetic. Cheap-check Φ-EVEN numerically on n=3,4 minimizers before writing.

---

block-recursion-tievertex: revise
Target: `c(n)=2^n/(2^{n+1}−1)` end to end; LB = (LBL) via integrality of the pure-cross-tie
  minimizer through Lemma UPM (unimodularity of the square 0/1 system `M'v=d`, `d`=distinct powers of 2).
Technique: LP-vertex classification; §2 within-piece-tie elimination (certified-ready Lemma BD);
  §3 square 0/1 system; **Lemma UPM proved in ONE SHOT via consecutive-ones total unimodularity from
  the stick's geometric interval structure** (replaces the stuck UPM-5 chorded-cycle casework).
Skeleton:
  1. Import reduction, UB, Theorem F, Lemma J (certified).
  2. LP-vertex classification, cases (a) degenerate / (b) tie-free / (c) within-piece tie /
     (d) pure cross-tie — but PATCH the taxonomy (see §2 fix).
  3. §2 HARDENED. (Explorer confirmed §2 as written likely has the Lemma-W failure mode: a surviving
     within-piece tie `(3,3)→(3±t)` is a genuine V-kink FACET `f=m+2|t|`, a valid terminal vertex the
     dichotomy omits.) Fix: add explicit terminal case (c′) = surviving within-piece tie block. Handle
     it directly, not by (false) elimination: Lemma BD localizes the block's contribution to
     `σ_a·f_block(w)` with `Σw_j=2^k`; combine block-by-block parity (Theorem F on the block sums)
     to still force `f≥1`. [Alternatively merge (c′) into §3 by allowing within-piece multiplicity
     in the incidence matrix — mirrors self-similar's generalized graph.]
  4. §3: pure cross-tie ⇒ square 0/1 system `M'v=d`, `v>0` distinct, `d`=distinct powers of 2.
  5. **Lemma UPM via consecutive-ones TU.** Order the `t` distinct VALUES by rank (descending).
     Claim each piece's set of value-columns is a CONTIGUOUS interval `[i_min(k),i_max(k)]` in this
     order (consecutive-ones property). A 0/1 matrix with consecutive-ones rows is TOTALLY UNIMODULAR
     ⇒ every square submatrix `det∈{0,±1}` ⇒ `det M'=±1` ⇒ `v∈ℤ` for ANY integer RHS. This kills ALL
     alternating cycles (chorded or not) at once, dissolving UPM-5, and explains the round-4 "holds
     for generic increasing RHS" note (TU is RHS-independent).
  6. Integer `v`, `Σ=D_n` odd ⇒ Theorem F ⇒ `f≥1`.
Key lemmas (claim + mechanism):
  - Lemma BD (ready to certify) — rank-contiguous block of one piece contributes `σ_a·f_block(w)`,
    because `σ_{a+j-1}=σ_a(−1)^{j-1}`.
  - §2-fix (c′ handling) — a surviving within-piece tie block still gives `f≥1` — because Lemma BD
    isolates its affine contribution and Theorem F/parity on the block sums (`Σ=2^k`) forces an
    integer floor (`{2,3,3}`⇒odd `f=1`). [mechanism to pin.]
  - Lemma UPM via TU — consecutive-ones ⇒ TU ⇒ `det=±1` — the classical interval-matrix TU criterion
    (NEW KB entry, cite the theorem, don't hand-wave). THE crux claim is the consecutive-ones
    property itself: cross-tie value-sharing respects the rank linear order.
Open gaps:
  - **Consecutive-ones property** — that each piece's value-columns form a rank-interval. UNVERIFIED;
    a closed alternating cycle is NOT interval-representable, so proving this AUTOMATICALLY excludes
    the hard cycles — but it needs a real geometric argument (stick position ↔ value rank) or a
    counterexample. If FALSE, fall back to the superincreasing-peel route (isolate the top exponent
    `2^{a_max} > Σ smaller`, peel downward).
  - §2-fix (c′): rigorous handling of the surviving within-piece tie (currently a real gap).
Cases to cover: (a) degenerate [certified], (b) tie-free [Lemma J], (c/c′) within-piece tie
  [hardened §2], (d) pure cross-tie [UPM via TU].
Watch out for: explorer's explicit `3×3` counterexample (`M=[[1,1,0],[0,1,1],[1,0,1]]`, `det=2`,
  `Mv=(3,5,4)`, `v=(1,2,3)`) proves "0/1 + positive distinct solution ⇒ unimodular" is FALSE for
  generic RHS — consecutive-ones/superincreasing is load-bearing, NOT incidental. So the interval
  structure must be PROVED, not assumed. Cheap-check: verify consecutive-ones on the n=3,4 cross-tie
  vertices (264/13800) numerically before committing; if it fails, this route dies fast and cleanly.

---

cut-budget-jacobsthal-recursion: new
Target: `c(n)=2^n/(2^{n+1}−1)` end to end; LB = (LBL) proved by induction on Xiang Yu's cut BUDGET,
  NEVER invoking integrality of any sub-piece. A genuinely different top-level target (bound the
  adversary recursion, not classify the minimizer) — far from both integrality routes.
Technique: discrete monovariant / DP on cut count, mirroring the CERTIFIED GAP-U
  delete-subtract-reachability template (which proved an UPPER invariant `g_b(P)≤s/D_b` by per-cut
  amortized accounting); here the MIRROR LOWER invariant, driven by the certified Lemma I two-band
  derivative — reuses proven machinery, no new tool.
Skeleton:
  1. Import reduction/UB. Target the floor identity `min_{≤k-cut refinements of W_n} f = f(W_{n−k})`,
     `f(W_m)=(2^{m+1}+(−1)^m)/3` (Jacobsthal; verified `f(W_0..5)=1,1,3,5,11,21`). At `k=n`:
     `f(W_0)=1` ⇒ (LBL).
  2. Certified Lemma I, two-band form: splitting a piece of value `V` into `V1≤V2` changes `f` by
     `±(band)±(band)`, each band length `min(V1,V2)`, one at the LOW and one at the HIGH end of the
     piece's occupied `t`-range in Lemma L's count function; the two signs are set by the CURRENT
     parity of `c(t)` in each band. This is an EXACT per-cut identity (not a bound).
  3. Key Lemma (per-cut floor / exchange): among all single cuts of ANY configuration reachable from
     `W_n` with `b−1` cuts still pending, the one minimizing `f` is DOMINATED by top-bisection of the
     current largest dyadic piece — i.e. no cut beats the Jacobsthal cascade step. Proved by a
     rearrangement/exchange argument on Lemma L's count function (no integrality).
  4. Induction on budget `b`: base `f(W_n)` odd integer `≥1`; each cut drops the floor by exactly the
     Jacobsthal decrement; after `n` cuts `f≥f(W_0)=1`.
Key lemmas (claim + mechanism):
  - Two-band per-cut identity — from certified Lemma I — the exact `Δf` of a single cut is a signed
    sum of two `min(V1,V2)`-length band contributions, signs from current parity.
  - Jacobsthal floor recursion `f(W_m)=2^m−f(W_{m−1})`, `f(W_0)=1` — the top-bisection cascade
    (certified Theorem G gives the `≤` tightness direction: adversary ACHIEVES it).
  - **Per-cut floor lower bound (THE gap)** — no single cut beats top-bisection against any reachable
    config — because scattering a cut among lower bands can only cancel `on`-parity it would otherwise
    add, dominated by concentrating the cut at the top piece; a Lemma-L rearrangement exchange.
Open gaps:
  - **The per-cut floor lower bound** (step 3) — that XY's optimal cut never beats the top-bisection
    cascade against ANY reachable configuration. This is the crux; the explorer flags that the band
    sign depends on the GLOBAL cut configuration, so the exchange must control WHICH piece is cut and
    in what ORDER (the same difficulty that forced round-1's Case-1/Case-2 split, now recast as an
    adversary-domination claim rather than vertex classification).
Cases to cover: none by geometry — the induction is on cut budget, not on minimizer type; the single
  case-split is "which piece XY cuts next," resolved by the domination lemma.
Watch out for: the identity `min_{≤k cuts}f(W_n)=f(W_{n−k})` is currently only an ENDPOINT numeric
  match, NOT a proven per-cut recursion — do NOT assume the recursion; prove the exchange. CHEAP-KILL
  FIRST: brute-force rational-VERTEX enumeration (not descent-heuristic search) to confirm
  `min_{≤k cuts}f(W_n)=f(W_{n−k})` EXACTLY for n≤4; if any config beats the floor for some `k<n`,
  this approach is dead immediately and cheaply.

---

pairing-injection-endgame: new
Target: `c(n)=2^n/(2^{n+1}−1)` end to end; LB = (LBL) via an EXPLICIT pairing/injection certificate
  on the endgame claim order — no minimizer, no vertex, no integrality. The FARTHEST framing from the
  field (game-strategy level), a diversity long-shot to break the 2-round integrality plateau.
Technique: pairing/involution certificate (structurally analogous to crux `aimo-0596`
  partner-mirroring with one floating seed); certified Lemma 0 (endgame-greedy): LB payoff `=Odd(P)`.
Skeleton:
  1. Import Lemma 0: `f=Odd(P)−Even(P)`, sums over odd/even descending ranks.
  2. Tag each sub-piece with its dyadic ORIGIN `2^k` (which original `W_n` piece it descends from).
  3. Construct an injection `φ`: even-rank sub-pieces → odd-rank sub-pieces with `φ(x)≥x` for all `x`,
     pairing keyed on origin (each even-rank sub-piece to an odd-rank sub-piece from the SAME or an
     ADJACENT dyadic block), leaving one unmatched odd-rank sub-piece of scaled mass `≥1`.
  4. `f = Σ_odd − Σ_even = Σ(unmatched odd) + Σ_x(φ(x)−x) ≥ mass(unmatched) ≥ 1`.
Key lemmas (claim + mechanism):
  - The injection exists with residual mass `≥1` — because `≤n` cuts and `Σ=D_n=2^{n+1}−1` leave a
    dyadic "surplus" band of scaled mass `≥1` that no origin-matched pair consumes. [construction to build.]
Open gaps:
  - **The entire injection construction** — no candidate `φ` exists yet; the residual-mass `≥1` bound
    is unproven. HIGH RISK / speculative — included as the deliberate far-field diversity seed.
Cases to cover: none pre-enumerated (construction task).
Watch out for: RANK order (not origin) determines who claims what, so an origin-based injection must
  PROVABLY respect actual claim order — this may be impossible (that is the risk). CHEAP-KILL FIRST:
  script the candidate pairing against `{2,3,3}` (`f=1`) and `{4/3,4/3,4/3,2,1}` (`f=5/3`) before any
  general proof; a quick pass/fail on two known hard instances. This is essentially strengthening the
  certified `f≥0` to `f≥1` combinatorially for NON-integer configs — the `≥1` must come from a genuine
  mass residual, not parity (parity `f=1/3` counterexamples exist at non-integer vertices).

---

Field summary for the outline-reviewer: two REVISED integrality routes with concrete new leads
(self-similar: generalized `Φ`-max forest + Lemma Φ-EVEN gap; block-recursion: consecutive-ones TU
one-shot + §2 hardening), and two NEW non-integrality framings (cut-budget Jacobsthal recursion —
strong, reuses certified GAP-U template + Lemma I; pairing-injection — far-field long-shot). The two
revises are the highest-probability closers; the two new slugs are the plateau-breaking diversity
CLAUDE.md mandates after 2 rounds on the shared integrality wall. Recommend build set include at least
one revise and the cut-budget new slug (with its cheap-kill vertex-enumeration run first).
