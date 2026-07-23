## imo-2026-03 — Gap 1a (No-Gap Lemma base case)

- **Distinct openings surfaced:**
  1. **(Main finding, new) A1-side route, not the A_{3,j}-vs-A_{3,k*} swap route.** Instead of
     attacking Gap 1a via the §20.1 Coincidence-Identity swap (comparing `A_{3,k^*}` directly to
     `A_{3,j}` and needing to control the sign of a shift `\delta=z_{k^*}-z_j` — the thing round 13
     got stuck on), attack it via **`A_1`'s own trivial upper bound**. For *any* `j` (any value at
     all, no hypothesis needed): the selection "keep `z_j`, delete every other element of
     `Z_0\{z_1\}`" is a valid selection witnessing `A_1\le|b_0-z_j|` — this needs no lemma, it is a
     single concrete selection. Combined with a new sub-fact (below), this gives a complete,
     elementary, sign-unambiguous proof of the half-open No-Gap Lemma.
  2. **New conjectural sub-lemma isolated computationally (not yet proved): "Deletion-Suffices for
     `k^*`".** At a genuine base-generator instance with trigger `M<A_1` and `k^*` a global argmin,
     `M=A_{3,k^*}` is **always exactly** `|b_0-d_{k^*}|` — i.e. the argmin's own recursive
     sub-problem `OPT_{+1}(B_0\cup\{d_{k^*}\},Z_0\setminus\{z_1,z_{k^*}\})` is always optimized by
     the trivial "delete everything in the residual list" selection; no cleverer KEEP/MATCH
     combination inside the residual ever helps, *conditional on the trigger+global-argmin
     hypotheses*. **This is not a free/trivial fact in general** — I hand-built a non-triggered
     counterexample where it fails (`Z0=[100,98,70,60],b0=10,kstar`→`zk=98,dk=2`: `D=|10-2|=8` but
     `M=2` via matching the residual pair `(70,60)`, a genuine Lemma-P-style duplicate cancellation
     `{10,2,10}\to2`) — so it genuinely depends on the trigger/argmin hypotheses, it is not vacuous.
     But within genuine trigger+argmin scope it held with **zero exceptions** across: an exhaustive
     sweep (`q\le5,v_{\max}=4`, `360` triggered instances), a broad random sweep (`q\in[3,8],
     v_{\max}\in\{2,\dots,12\}$, both `|B_0|=0,1`, `1376` triggered `|B_0|=1` instances), and three
     separate wide-range random searches (`\sim20,000$–`60,000` raw trials each, `v_{\max}` up to
     `25`) specifically hunting for `M<D` inside genuine trigger scope — **0 found in every
     battery.** Given this sub-lemma, Gap 1a follows immediately: if `z_j\in(\min(b_0,d_{k^*}),
     \max(b_0,d_{k^*})]`, then `|b_0-z_j|\le|b_0-d_{k^*}|=D=M` (monotonicity of `|b_0-\cdot|` on
     each side of `b_0`, elementary), so `A_1\le|b_0-z_j|\le M`, contradicting the strict trigger
     `M<A_1`. **This also correctly explains the half-open shape**: at `z_j=\max(b_0,d_{k^*})`
     exactly, `|b_0-z_j|=D=M` exactly (not `<M`), but `A_1\le M` still contradicts the *strict*
     inequality `M<A_1` — matching why the boundary tie must be included in the forbidden set,
     without needing a separate case.
  3. **Bonus observation, not required but consistent:** the same argument, run at `z_j=
     \min(b_0,d_{k^*})` exactly, *also* gives `A_1\le M`, i.e. it suggests the interval might
     actually be forbidden as **fully closed** `[\min,\max]`, not just half-open — a strictly
     stronger fact than what §19/§20 need. Not tested to the same depth; flagged as a free
     strengthening to check, not a requirement (the closed-interval case corresponds to `h=2`,
     which is already handled separately, so proving it costs nothing extra but isn't blocking).
  4. **Mechanism-discovery method (useful precedent for future gaps):** I found this by *perturbing*
     `z_j` into the forbidden interval on real triggered instances and asking which hypothesis
     breaks (trigger, or `k^*`'s global-argmin-ness) — **not** by trying to prove the swap
     construction directly. Across `2000+` perturbation checks (fixing the earlier bug where a
     naive perturbation could accidentally exceed `z_1`, invalidating the whole instance — see Dead
     end below), the trigger broke `129/129` times a genuine forced-interval-entry was tested,
     **the global-argmin property never broke even once** (`0` cases of "trigger survives, argmin
     breaks"). This is a strong signal about *which* of the two hypotheses is doing the real work,
     and pointed directly at finding #1/#2 above.

- **Candidate technique(s):** elementary case-by-`\mathrm{sign}(b_0-d_{k^*})` direct construction
  (a single explicit K/D selection), **not** an extremal-witness/contradiction/local-rewrite
  argument — Gap 1a looks structurally *easier* than Gaps 1b/1c and does not need the crux-inspired
  "extremal witness + secondary tie-break" shape flagged for those. The remaining work is entirely
  contained in proving the new Deletion-Suffices sub-lemma (candidate proof idea, untested: suppose
  for contradiction some selection of `Z_0\setminus\{z_1,z_{k^*}\}` beats `D=|b_0-d_{k^*}|`; the
  *same* selection, embedded inside `A_1`'s search space (which is `Z_0\setminus\{z_1\}=
  (Z_0\setminus\{z_1,z_{k^*}\})\cup\{z_{k^*}\}`, one element larger), plus deleting `z_{k^*}$ too,
  reproduces a value `\le` that same improved number for `A_1` directly, which is suspicious given
  the trigger needs `A_1>M` — OR the same improving selection, re-embedded with a *different* match
  partner for `z_1`, might reduce some other `A_{3,l}` below `M`, contradicting `k^*`'s global
  minimality. Neither direction is worked out — this is the concrete next construction to attempt,
  and it looks tractable since it only needs a **single re-use of an already-hypothesized good
  selection**, not a value-shift/sign analysis.

- **Cheap-kill candidates:** none further beyond what's above — the "keep `z_j`+`b_0`, delete
  everything else" bound is itself already a cheap, fully elementary kill of most of Gap 1a's
  difficulty; what's left (Deletion-Suffices) is a clean scalar/sub-problem-value question, not a
  casework-heavy one.

- **Knowledge-base entries to use:** Fact 1 & 2 (`lemmas/dominant-extraction.md`, `e(M)\ge0`,
  `e(M)\le\max(M)`) — used implicitly in bounding `A_1`'s trivial selection; Fact 3/General
  Rank-Extraction Identity (`lemmas/general-rank-extraction-identity.md`) is the natural tool to
  formalize "embedding a Zrest-selection into `A_1`'s bigger list" in the Deletion-Suffices proof
  attempt above (it is precisely a rank-extraction of `z_{k^*}` from `A_1`'s own list). Lemma P
  (duplicate-pair cancellation) is exactly the mechanism behind my hand-built non-triggered
  counterexample to Deletion-Suffices (`{10,2,10}\to2`) — worth having on hand as the concrete
  "what could go wrong" picture when attempting the sub-lemma's proof.

- **Analogous past problems (cruxes):** none newly relevant beyond what round 13 already
  identified (`aimo-0960`/`aimo-0438`/`aimo-0666`'s extremal-witness shape) — but that shape is for
  Gaps 1b/1c, **not** for this simplified Gap 1a route, which is now a direct elementary
  construction, closer in spirit to a basic dominance/monotonicity argument than an extremal-witness
  argument. I did not find a crux corpus match for "argmin's own recursive value equals the naive
  full-deletion bound" — this looks like a bespoke fact about this problem's specific OPT
  recursion, not a transferable crux move.

- **Prior progress:** No-Gap Lemma corrected to precise half-open form (round 13), Coincidence
  Identity + swap construction proved valid as an upper bound but with an uncontrolled sign
  (round 13) — **this round's finding is a genuinely different, simpler route that does not use the
  Coincidence Identity at all**, isolating the entire remaining difficulty into one new, sharply
  stated, computationally well-corroborated (but unproved) sub-lemma (Deletion-Suffices for `k^*`).

- **Dead ends (do not retry):** (a) naively perturbing `z_j` to "test" No-Gap by simply moving its
  value without checking it stays `<z_1` is **invalid** — if the perturbed value exceeds the
  original `z_1`, the entire base-generator structure changes (the perturbed element becomes the new
  `z_1`), giving a spurious, meaningless "no violation broke" or "violation" result; always cap any
  such perturbation strictly below `z_1` (I hit this bug first, producing a misleading initial
  result before fixing it — see Small-case notes). (b) The originally-planned continuation of
  round 13's Coincidence-Identity swap construction (directly comparing `A_{3,k^*}` and `A_{3,j}`
  and trying to pin a sign on `\delta=z_{k^*}-z_j`) is **not disproved**, but this round's
  perturbation experiments suggest it is not the natural lever: forcing `z_j` into the interval
  never broke `k^*`'s own global-argmin-ness (`0/129`+ cases), it only ever broke the trigger — so a
  proof attempt built around "`A_{3,j}<M`" is fighting an uphill, possibly false-shaped battle,
  while the `A_1`-side route matches the data cleanly. Do not abandon the Coincidence Identity as
  definitely useless (it may still help formalize Deletion-Suffices itself, e.g. relating `A_1` and
  `A_{3,k^*}` structurally), but do not spend further effort trying to make the direct
  `A_{3,k^*}`-vs-`A_{3,j}` sign comparison work as the top-level mechanism.

- **Small-case / intuition notes (all labeled conjecture unless marked "proved"):**
  - **Proved (elementary, this round):** for any `j`, `A_1\le|b_0-z_j|` — a single valid selection,
    no hypothesis needed. Verified by direct construction, not merely sampled.
  - **Conjectured, strongly corroborated (this round):** Deletion-Suffices, `M=|b_0-d_{k^*}|`
    exactly whenever the trigger `M<A_1` holds and `k^*` is a genuine global argmin — `0` violations
    across `360` exhaustive + `1376`+`\sim6600`+`\sim19500` random-search triggered instances (total
    well over `27,000` genuine trigger+argmin checks across several distinct search strategies,
    `v_{\max}` up to `25`), **and** confirmed to be a real (non-vacuous, non-trivial) hypothesis —
    it demonstrably fails outside genuine trigger scope (hand-built counterexample
    `Z0=[100,98,70,60],b_0=10`, `D=8\ne M=2`, achieved via a Lemma-P-style duplicate cancellation on
    the matched difference `70-60=10=b_0`).
  - **Conjectured (not required, bonus):** the forbidden set for `z_j` may actually be the fully
    *closed* interval `[\min(b_0,d_{k^*}),\max(b_0,d_{k^*})]`, one notch stronger than the certified
    half-open form — the same `A_1\le|b_0-z_j|\le M` argument goes through unchanged at both
    endpoints. Not independently verified to the same depth as the half-open form; a cheap thing for
    the next builder to check for free while proving Gap 1a, but not blocking.
  - Given Deletion-Suffices, the full Gap 1a proof (modulo that one sub-lemma) is now a **three-line
    elementary argument** with no sign ambiguity — this looks like the cheapest remaining hard
    content in the whole population's open-gap list, and should be prioritized before Gaps 1b/1c.
