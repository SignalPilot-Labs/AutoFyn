## imo-2026-06 (lens: direct attack on the Finite Covering Backbone Conjecture)

### Scope
Dispatch asked for three things: (a) can round-2's second-moment/Cauchy-Schwarz
plan (opening 2 of `math-explorer-backbone-finiteness.md`) be retargeted at the
Finite Covering Backbone Conjecture (FCBC) instead of the refuted (⋆); (b) what
invariant survives both NC1 (`a_1=221`) and NC2 (`a_1=375`); (c) any other
genuinely promising route, including whether the Domination Lemma's `O(log n)`
bound can be sharpened or whether there's a structural (non-growth-rate) reason
for finiteness. All numerics below use exact-integer trial-division (`sympy`
for small runs, a sieve of smallest-prime-factor for larger runs), reproducing
the recursive rule directly — no periodicity or backbone is ever assumed as
input, only computed from the raw sequence.

### (b) first, because it drives everything else: the invariant that survives NC1/NC2

I computed, for several Case-II values of `a_1`, `D_n(p):=|\{i\le n:p\mid
a_i\}|` for every prime `p` that ever appears, at large `n` (up to `N=40000`
for the hardest stress case `a_1=247`). Two completely different behaviors
emerge cleanly, confirmed to 3-4 significant figures at `N=15000`:

- **"Generic" primes**: `D_n(p)/n \to 1/p` almost exactly (e.g. for `a_1=247`,
  `N=15000`: `p=23`: density `0.0434` vs `1/23=0.0435`; `p=37`: `0.0271` vs
  `0.0270`; matches to the noise floor `O(1/\sqrt N)`).
- **"Amplified" primes**: `D_n(p)/n` is bounded well *above* `1/p`, by a
  constant that does not shrink as `n\to\infty` (e.g. `a_1=247`: `p=13`,
  density `0.6545` vs `1/p=0.0769`, excess `+0.578`; `p=2`, density `0.846` vs
  `0.5`, excess `+0.346`).

Define `H_\rho:=\{p : \liminf_n (D_n(p)-n/p)/n > 0\}` ("positive excess
density over the generic 1/p rate"). Testing this against every solved/known-
period case in the workspace:
- `a_1=15` (solved, `T=8,L=30`): `H_\rho=\{2,3,5\}=\mathrm{rad}(30)=\mathrm{rad}(L)` exactly.
- `a_1=33,55,85` (Case I, `T=1`): `H_\rho=\{p\}=\mathrm{rad}(L)` exactly (the
  single saturating prime).
- `a_1=105` (period detected numerically, `T=58,L=210`): `H_\rho=\{2,3,5,7\}
  =\mathrm{rad}(210)=\mathrm{rad}(L)` exactly.
- `a_1=65` (period detected, `T=58,L=390`): `H_\rho=\{2,3,5,13\}=\mathrm{rad}
  (390)=\mathrm{rad}(L)` exactly (checked the raw densities by hand since a
  naive ratio-threshold missed `p=2` at ratio `1.48` — the *absolute* excess
  `0.24` is unambiguous).
- `a_1=221` (NC1's counterexample): `H_\rho=\{2,3,5,13,17\}` at `N=4000`. This
  **includes `5`**, the exact prime NC1 proved is `w(4,5)`, the surprise
  witness not in `S_0`. It **excludes `7`**, which *is* in `S_0` (it divides
  `a_3=238`) but never becomes amplified — it stays at exactly generic
  density `1/7` for the whole run. So `H_\rho` gets NC1's counterexample
  *right* where the naive "read off `S_0`" idea got it wrong: it correctly
  predicts `5` belongs to the backbone and `7` does not, despite `7` appearing
  earlier in the trace.
- `a_1=375` (NC2's counterexample): amplified primes found are `\{2,3\}` at
  `N=4000` (small `L=15`); `19` (NC2's witness `w(3,7)=19`, which exceeds
  `L=\mathrm{rad}(a_1)`) was not yet distinguishable as amplified vs generic
  at this sample size — worth a longer run next round, flagged as unfinished
  business, not a refutation.
- `a_1=143,1001` (period not detected within 60): `H_\rho=\{2,3,11,13\}` and
  `\{2,7,11,13\}` respectively, both small and stable from early on.

**Conjecture (new this round, not previously stated in the workspace):
`H_\rho` is finite and equals `\mathrm{rad}(L_{\mathrm{per}})`**, where
`L_{\mathrm{per}}` is the sequence's eventual periodic gap (Theorem 2.4's
`L_{\mathrm{per}}`). This is *evidence-labeled conjecture*, not a proof, but it
is a genuinely new invariant that (i) is well-defined without presupposing
periodicity (it's a statement about `\liminf` of an explicit arithmetic
function of the raw sequence), (ii) correctly discriminates NC1's `5` (in) vs
`7` (out), and (iii) matches `\mathrm{rad}(L)` exactly on every case where `L`
is independently known. **This is the concrete answer to (b)**: the invariant
that survives both counterexamples is *asymptotic density strictly above the
"chance" rate `1/p`* — not "appeared before some collapse index" (NC1) and not
"divides `a_1`" (NC2).

**Caveat / why this doesn't trivially close the gap**: proving `H_\rho` is
finite from first principles (without circularly assuming eventual
periodicity, which is what would explain why generic primes hit exactly
density `1/p`) is exactly as hard as the original conjecture — I did not find
an unconditional proof that generic primes have density `\to 1/p`. The
already-certified interval-packing bound only gives density `\le L/p` (a
constant multiple of `1/p`, not `1/p` itself), so it does not by itself
force `H_\rho` finite. Flagging this as the right *target* for a future
builder, not a closed sub-lemma.

### (a) retargeting the second-moment/Cauchy-Schwarz plan

Worked the algebra through explicitly (not attempted in any prior round).
Round 2's opening 2 wanted to bound `r_n:=`(number of distinct primes that
have ever been the Domination-Lemma argmax by step `n`) via Cauchy-Schwarz on
`\Sigma_q D_n(q)^2` restricted to `q\le C\log n` (opening 1's size bound).
Carrying this out:
- `\Sigma_q D_n(q) = \Sigma_{i\le n}\omega(a_i) = O(n\log n)` (Lemma 1 bounds
  each `a_i`, so `\omega(a_i)=O(\log i)`).
- The interval-packing bound `D_n(q)\le(n-1)L/q+1` gives, summed over primes
  `q\le C\log n` and using Mertens (`\Sigma_p 1/p^2=O(1)`,
  `\Sigma_{p\le x}1/p=O(\log\log x)`): `\Sigma_q D_n(q)^2 = O(n^2L^2) +
  O(nL\log\log\log n) + O(\log n/\log\log n)`, i.e. **dominated by an
  `\Theta(n^2)` term** coming from the convergent `\Sigma 1/p^2` piece.
- But `(\Sigma_q D_n(q))^2=O(n^2\log^2n)`, and Cauchy-Schwarz gives
  `(\Sigma_qD_n(q))^2\le r_n\cdot\Sigma_qD_n(q)^2`, i.e.
  `r_n\ge\Omega(n^2\log^2n)/O(n^2)=\Omega(\log^2n)` — this is a **lower**
  bound on `r_n`, the wrong direction; it does not upper-bound `r_n` at all.
  The naive Cauchy-Schwarz direction here is useless for proving finiteness.
- **Retargeted, sharper version (new this round, using the (b) invariant):**
  the right quantity to bound is not raw `D_n(q)^2` but *excess-squared*
  `\Sigma_q(D_n(q)-n/q)^2`. Numerically (from the `a_1=247` data), each
  amplified prime contributes `\Theta(n^2)` to this sum (excess grows
  linearly in `n`, so its square is quadratic), while each generic prime
  contributes only `O(1)` or `O(n)` (bounded fluctuation around the `1/p`
  rate). If one could prove `\Sigma_q(D_n(q)-n/q)^2=o(n^2)` **unconditionally**
  (from the recursive rule alone, no periodicity assumed), that would force
  the *number* of primes achieving genuine `\Theta(n)` excess to be `O(1)`,
  i.e. would prove `H_\rho` finite directly (each such prime alone would
  already saturate an `\Omega(n^2)` share of a sub-quadratic total). **This is
  a real reformulation of opening 2's idea, but the required variance bound
  is a nontrivial analytic claim** (a Turán–Kubilius-type second-moment
  estimate adapted to this greedily-selected, non-random subsequence, not a
  standard one from the KB) — I could not find a short proof and do not
  believe it is a cheap win. Recommend flagging to the outliner as a coherent
  but hard analytic sub-target, not a quick close.
- **Bottom line on (a):** the *literal* opening-2 plan (raw `D_n(q)^2`, all
  primes `\le C\log n`) does not work — it gives a lower, not upper, bound on
  `r_n`. The *retargeted* excess-squared version is a better-posed analytic
  question but still open and hard; do not expect a builder to close it
  quickly.

### (c) sharpening the O(log n) bound / structural route via the Domination Lemma

Re-derived `persistent-backbone-monovariant`'s `O(\log n)` bound on the
dominant prime `q^*` more carefully: `q^*\le r\cdot a_n/n` where
`r=\omega(a_{n+1})`. Since `a_n/n\to L` (a genuine **constant**, not growing —
`a_n\le a_1+(n-1)L` gives `a_n/n\to L` exactly), **all of the `O(\log n)`
growth in the existing bound comes from `r=\omega(a_{n+1})` alone**, not from
`a_n/n`. This means: **if `\omega(a_n)` is uniformly bounded (not growing with
`n`), then `q^*` is uniformly bounded too** — collapsing the whole backbone-
finiteness question to a single cleaner claim: *is `\omega(a_n)` bounded?*

I tested this numerically, and it is a genuinely new, promising empirical
finding not previously in the workspace:
- `a_1=247`: `\omega(a_n)\le6` for all `n\le15000`; pushing to `n=40000`,
  the max ticks up to `7` (first hit at `n\approx17770`) and then **stays at 7
  through `n=40000`** (no further growth over the next 22000 terms tested).
- `a_1=65,1001`: `\omega(a_n)\le6` throughout `8000` terms, average around
  `3.6`-`3.7`, no visible growth trend.
- This is much tighter than the pessimistic worst-case `\omega(a_n)\le\log_2
  a_n=O(\log n)` used in the existing bound — the true value stays in the
  single digits over tens of thousands of terms, essentially flat, not
  growing like `\log n` (for `a_1=247` at `n=40000`, `a_n\approx1.1\times10^6`,
  so `\log_2 a_n\approx20`, vs. observed `\omega(a_n)\le7` — a factor of `3`
  tighter, and the gap should widen further as `n` grows since `\log_2 a_n`
  keeps climbing while `\omega` appears to plateau).

**This reframes (c)'s question precisely: is there a structural (not
growth-rate) reason `\omega(a_n)` stays bounded?** A plausible mechanism (not
worked out, flagged for the outliner): since `a_{n+1}` is the *smallest*
admissible integer in a window of length `\le L` above `a_n` (Lemma 1), and
admissibility against `n` prior terms is most cheaply satisfied by reusing a
*few* already-recruited high-density (amplified) primes rather than by
using many small one-off primes, the greedy/minimality of the rule may itself
be an implicit pressure toward *smooth-but-not-too-smooth* numbers built from
a bounded palette — this is exactly the kind of claim a monovariant/induction
argument (not a counting/density argument) would prove, e.g. "if
`\omega(a_i)\le M` for all `i\le n` and the current backbone has stabilized,
then `\omega(a_{n+1})\le M`" as an inductive invariant. **I did not attempt to
prove this** (per dispatch scope — flagging the opening, not developing it).

**One caveat**: the `7` appearing only at `n\approx17770` (not from the
start) shows this quantity is *not* monotone/obviously bounded by inspection
alone — it can still creep up slowly (loglog-type growth is not ruled out by
this data). The evidence supports "grows extremely slowly, if at all" more
strongly than "is provably constant"; recommend the outliner treat "`\omega
(a_n)` is `O(1)`" and "`\omega(a_n)=O(\log\log n)` (Hardy–Ramanujan-typical
rate, still enough since `\log\log` grows arbitrarily slowly but is still
unbounded, so this would NOT by itself finish backbone finiteness)" as two
distinct possible targets, and prioritize determining which via either a
longer simulation (e.g. `a_1=247` to `n=200000+`) or a direct structural
argument, before committing builder effort to a full proof either way.

### Distinct openings (summary for the outliner)

1. **The excess-density invariant `H_\rho`** (new this round): a well-defined,
   circularity-free (no periodicity assumed) reformulation of "backbone"
   that correctly discriminates NC1/NC2's counterexamples. Proving `H_\rho`
   finite is a cleaner restatement of FCBC; the missing unconditional
   ingredient is a proof that "generic" (non-recruited) primes have density
   `\to1/p` (currently only bounded by `\le L/p` via interval-packing, a
   weaker bound by a constant factor `L`).
2. **`\omega(a_n)` boundedness** (new this round): a sharper, more concrete
   sub-target than the existing `O(\log n)` dominant-prime bound — if
   `\omega(a_n)=O(1)`, then `q^*=O(1)` follows immediately from
   already-certified Domination Lemma + Lemma 1 algebra (no new heavy
   machinery needed, just the observation that `a_n/n\to L` is a genuine
   constant). Strongly supported numerically (single digits, near-flat, over
   tens of thousands of terms) but not proven, and the evidence is
   ambiguous between "truly bounded" and "extremely slow growth."
3. **Retargeted second moment on excess, not raw counts** (opening (a)
   above): a coherent but hard analytic reformulation of round 2's opening 2;
   the literal original plan does not work (wrong direction of inequality).
4. **Monovariant / well-ordering** (round 2's opening 3, aimo-0678-style,
   still unattempted): given that `H_\rho\approx\mathrm{rad}(L_{\mathrm{per}})`
   ties the backbone conjecturally to the periodic structure itself, proving
   backbone-finiteness and periodicity *together* by one induction (as
   `run_state.md`'s Rules already recommend) looks structurally more natural
   than proving backbone-finiteness first as a standalone fact — the density
   route keeps needing periodicity-flavored facts (density `=1/p`) to close.

### Candidate technique(s)
- Strong induction / monovariant on a combined invariant tracking both
  `\omega(a_n)` (or the amplified-prime set seen so far) and the residue
  pattern simultaneously, rather than a pure density/counting argument.
- If a density route is pursued anyway: prove `D_n(p)\le n/p+O(1)` (not just
  `\le nL/p+O(1)`) for primes `p` outside a to-be-determined finite exceptional
  set — this is the precise unconditional statement needed to make `H_\rho`
  well-defined and finite without presupposing periodicity.

### Cheap-kill candidates
- None new this round that fully close the gap. The closest to "cheap": since
  `q^*\le r\cdot a_n/n` and `a_n/n\to L` (constant, not growing), **any**
  future proof that `\omega(a_{n+1})` is bounded by a constant `M`
  immediately upgrades to `q^*\le M\cdot L` (a genuine constant bound on the
  dominant prime, hence finiteness of the set of ever-dominant primes) via
  already-certified lemmas alone — this three-line deduction is worth
  certifying as its own small lemma ("Dominant prime bound in terms of
  `\omega`") regardless of whether `\omega(a_n)` boundedness itself gets
  proved this round or a later one, since it cleanly isolates the remaining
  work into exactly one sub-claim.

### Knowledge-base entries to use
- **Standard inequalities: Cauchy-Schwarz** (KB, generic entry) — needed for
  the (retargeted, still-open) excess-squared version of opening (a).
- **Pigeonhole / extremal principle** — underlies both the Domination Lemma
  and any bounded-`\omega` inductive argument.
- No KB entry for Mertens' theorems, Turán–Kubilius, or Hardy–Ramanujan exists
  (checked again this round; matches round 2's finding) — any such estimate
  used must be derived/cited from scratch, not invoked as a named KB tool.

### Analogous past problems (cruxes)
Re-confirming round 2's findings after independently checking the corpus this
round with keyword queries around "bounded number of prime factors,"
"density," "covering system," "excess" — no new, better match surfaced. The
best analogs remain, as round 2 found:
- **`aimo-0678`** (ISL 2015 N4) — still the best structural analog: proves
  eventual periodicity of a different greedy integer recursion via a genuine
  monovariant (`w_n=\min\{m\ge a_n:m\nmid s_n\}`, shown non-increasing), not a
  density argument. Given this round's finding that the density route keeps
  running into periodicity-flavored circularity (the `1/p` density fact), this
  crux's mechanism looks like the more promising direction to actually adapt,
  not just a "plateau-break insurance" option.
- **`aimo-0727`** (ISL 2023) — the "bounded quotient `\Leftrightarrow` finite
  prime confinement" mechanism remains the closest corpus precedent for the
  *shape* of the Finite Covering Backbone Conjecture itself, run in the
  direction we want (still not adapted; the right quotient for our sequence
  is still unidentified).
- No new analog found for the specific `\omega(a_n)` boundedness question
  (opening 2/(c) above) — this looks like genuinely new territory for this
  problem, not a transplant from the corpus.

### Prior progress
See `current.md` and `lemmas/lemma-C-global-intersection-collapse.md`,
`lemmas/proposition-NC1-*.md`, `lemmas/proposition-NC2-*.md` (all certified,
summarized accurately in the round-2 Eval History — not re-derived here).
Domination Lemma and Lemma 1 remain the only certified quantitative tools;
this round's contribution is (i) the `H_\rho` excess-density invariant, (ii)
the algebra showing `a_n/n\to L` isolates all `O(\log n)` growth into
`\omega(a_{n+1})` alone, (iii) numerical evidence that `\omega(a_n)` is much
smaller and flatter than the existing worst-case bound suggests, (iv) a
worked-through demonstration that the literal second-moment/Cauchy-Schwarz
plan from round 2 does not close the gap (wrong inequality direction), with a
harder but better-posed retargeted version identified instead.

### Dead ends (do not retry)
- **Literal opening-2 Cauchy-Schwarz on raw `\Sigma_q D_n(q)^2`** (round 2's
  proposal, worked through in full this round): gives `r_n=\Omega(\log^2n)`
  as a *lower* bound, the wrong direction to prove `r_n` finite. Do not retry
  this exact formulation; if pursuing a second-moment idea, use the
  excess-squared reformulation above instead (still open, but at least
  pointed the right direction).
- Confirmed (not retried) round 2's dead ends still stand: `bounded-gap-
  density-covering`'s original Step 3, `minimal-witness-index-descent`, the
  refuted `H_n` and `(\star)` framings — none revisited here, consistent with
  `run_state.md` Rules.

### Small-case / intuition notes (all labeled conjecture)
- `H_\rho:=\{p:\liminf_n(D_n(p)-n/p)/n>0\}` empirically equals
  `\mathrm{rad}(L_{\mathrm{per}})` on every case with known period (`a_1\in
  \{15,33,55,65,85,105\}`), and is small (`\le5` primes) and apparently stable
  from early `n` on every Case-II example tested (`a_1\in\{143,221,247,375,
  1001\}`) — strong support for FCBC itself, consistent with (and sharpening)
  round 2's numerics.
- `\omega(a_n)` stays in the single digits (`\le6`–`7`) across tens of
  thousands of terms for every example tried, including the hardest stress
  case `a_1=247` pushed to `n=40000` — far tighter than the `O(\log n)`
  worst case, but the one observed late increase (`6\to7` at `n\approx17770`,
  a full `17000` terms into the run) means "bounded" is not yet distinguished
  numerically from "extremely slowly growing"; a longer run (`n\gtrsim2\times
  10^5`) would sharpen this further if a future round wants more evidence
  before committing to a proof attempt.
