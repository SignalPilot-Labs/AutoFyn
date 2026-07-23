# Outline review — round 18, imo-2026-03, §29 of `potential-weighting-upper-bound`

Independently re-verified all four subsections of §29 with a fresh, from-scratch harness
(`/tmp/round-18/outline-review-verify/core.py` — brute-force `e()`, `all_selections`, `OPT_sigma`,
validated first against all 4 of the file's own worked examples, bit-for-bit: `OPT_{+1}([5,8],(10,8,
7,2))=0`, `OPT_{-1}=10`, `OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4` — all reproduced
exactly before trusting the harness for anything new). Not reusing any explorer's or the outliner's
own scripts.

## §29.1 — Match-Branch-Domination-via-Per-Partner-Domination

**Verdict: correct, the renaming is exact, no hidden hypothesis. Ready to certify as stated.**

- Re-derived the renaming by hand: Two-Touch's `MATCH_j := OPT_{+1}({b_0,d_j}, W\{w_1,w_j})` and
  Gap 1a's `A_{3,l} := OPT_{+1}(B_0\cup\{d_l\}, Z_0\{z_1,z_l\})` are the identical formula under
  `Z_0\leftrightarrow W`, `l\leftrightarrow j` — literally, not merely structurally similar.
- Independently confirmed both trivial ingredients: `A_1 \ge TT` (150 fresh `(b_0,W)` instances,
  `|W|\in\{2,...,5\}`, `0` failures) and `D_j\ge TT` (same sweep, `0` failures, and it really is a
  trivial by-definition fact — `TwoTouch`'s own candidate list literally contains `e(\{b_0,d_j\})`).
- Independently re-verified Per-Partner Domination itself (not trusting the citation): `0/600`
  random (`q\le5`), `0/3125` **exhaustive** (`q=4`, 5-value grid) — matches the population's
  standing "proved `q\le3`, corroborated `q\ge4`, zero known counterexample" status.
- End-to-end: directly computed `MATCH_j` via brute force (not via the intermediate lemma chain)
  and checked `MATCH_j\ge TT` for `150` fresh `(b_0,W)` instances (all partners `j`, `|W|\le5`):
  **`0` failures.**
- Independently re-verified the headline consequence ("Two-Touch fully proved for `|W|\le3`") by
  **exhaustive** brute force at `|W|=3` on a 5-value grid: `OPT_{+1}(\{b_0\},W)=\mathrm{TwoTouch}
  (b_0,W)` in **`625/625`** instances, `0` mismatches.
- Traced §26.5(b)'s DELETE-branch proof (the ingredient `A_1\ge TT`) to confirm it is **not**
  secretly circular through Per-Partner Domination or Match-Branch Domination — it is a standard
  strong-induction step (candidate-list-subset argument, IH at `|W|-1` only) with no dependency on
  either. Confirmed no circularity in this ingredient.
- Confirmed the file's own honesty: §29.1 repeatedly and correctly states this does **not** close
  Per-Partner Domination's general-`q` gap (checked via grep — the caveat appears in the lemma's own
  "Open dependency" paragraph and in item (iii) of the section's "Watch out for" list). No overclaim.

**One non-fatal rigor gap not currently flagged anywhere in the file, worth adding to the next
round's "Watch out for" list.** §25.2 (round 16) suggests that Per-Partner Domination's own
general-`q` proof may use **Two-Touch's closed form** as an ingredient for bounding `A_1` (`"turns
an open-ended search for a sufficient bound family into 'plug in the exact value'"`). If a future
builder actually does this, note the index structure carefully: Two-Touch's MATCH branch at level
`|W|=n` needs Per-Partner Domination **at the same size** `q=n` (§29.1, confirmed above, exact
renaming `Z_0=W`), while Per-Partner Domination at `q=n` would then need Two-Touch **at the strictly
smaller size** `|W|=n-1` (since `A_1` ranges over `Z_0\setminus\{z_1\}`, size `n-1`). This is a
well-founded joint induction (mirrors the already-verified, round-17-checked Two-Touch/Three-Touch
mutual induction) **only if built level-by-level** (Two-Touch(`n-1`) before Per-Partner-Domination
(`n`) before Two-Touch(`n`)) — it would become circular if either lemma were proved as a single
flat "for all sizes" statement that internally needs the other at an unbounded/same size. Nothing in
§29 currently flags this dependency-ordering requirement explicitly (unlike Two-Touch/Three-Touch's
mutual induction, which §28.4(d) does explicitly verify for well-foundedness). Recommend the
outliner add one sentence to §29's "Watch out for" list requiring any future general-`q`
Per-Partner-Domination proof that uses Two-Touch as an ingredient to state and verify this
level-ordering explicitly, the same way §28.4(d) did for Two-Touch/Three-Touch.

## §29.2 — Three-Touch MATCH Sibling-Domination Lemma (σ=-1)

**Verdict: correctly stated as an unproved-but-heavily-corroborated candidate; my fresh, wider
sweep confirms all three legs of the asymmetry-disambiguation table independently, including the
part the dispatch specifically asked me not to take on faith (the σ=+1 mirror's failure).**

- `\sigma=-1` candidate itself (`MATCH_val\le\max(DELETE_val,KEEP_val)`, true recursive branch
  values, single background `c`): **`0/400`** fresh random instances (`|Z|\in\{2,...,5\}`), `0`
  failures — survives.
- `\sigma=+1` mirror (does `MATCH_val` ever strictly beat `\min(DELETE_val,KEEP_val)` under
  minimization?): **`42/400 = 10.5\%`** — confirmed to genuinely fail, same order of magnitude as
  the file's cited `\approx13\%` (this is Two-Touch's own already-open MATCH problem, correctly
  *not* conflated with §29.2's candidate). Concrete failing instance reproduced and hand-checked:
  `c=7/2, Z=(6,3/2,0)`: `DEL=2, KEEP=5/2, MATCH=1 < \min(DEL,KEEP)=2`.
- `\sigma=-1` scalar-proxy "Mirror Per-Partner Domination" (`D'_l:=|c-d_l|` instead of the true
  `KEEP_val`): **`124/999 = 12.4\%`** failures — confirmed to genuinely fail, squarely inside the
  file's cited `\approx7$–`15\%` range.
- All three legs land where the file claims: the true-branch-value `\sigma=-1` version alone
  survives; the `\sigma=+1` mirror and the scalar-proxy `\sigma=-1` version are both genuinely,
  independently confirmed false, at consistent rates. **No conflation risk found — the
  disambiguation table is accurate, not merely asserted.**
- Confirmed the section is honestly labeled "no proof written" — correct, this remains a strong
  corroborated conjecture, not a closed lemma.

## §29.3 — Gap 1c case (a), δ_c/δ_d split

**Verdict: sub-target 1 (δ_d≥0) independently reproduces cleanly WITHIN genuine `\mathcal
F`-provenance — but I found it is emphatically NOT a provenance-free fact, a real clarification the
file's current wording risks obscuring. Sub-target 2's framing is well-posed, not a relabeling.**

- Built my own from-scratch `\mathcal F`-provenance generator (base generator `(b_0,Z_0)`, genuine
  trigger `M<A_1`, `k^*` a true global argmin of `A_{3,l}` via exhaustive computation over every
  `l`, `B_1:=\{b_0,d_{k^*}\}`, `\mathrm{Res}:=Z_0\setminus\{z_1,z_{k^*}\}`) — different code path
  from any explorer's or the outliner's own harness. Found 250 genuine instances; within them,
  isolated **155** genuine case-(a) events (`\xi^*` nonempty, `B_1\cup\{d\}\cup\xi^*` duplicate-free)
  and tested `\delta_d\ge0` for **every** choice of dropped element `x\in\xi^*` (not just nearest):
  **`0/155` failures**, minimum observed margin `1` — independently reproduces the file's finding.
- **New finding, not currently in the file: `\delta_d\ge0` is FALSE once genuine `\mathcal
  F`-provenance is dropped, even while keeping the exact same construction shape** (`M:=B\cup(\xi^*
  \setminus\{x\})`, `\xi^*` a genuine sparsest optimal witness of `OPT_{+1}(B\cup\{d\},X)` for
  *arbitrary* `(B,X,d)`, not required to arise from a real trigger+argmin descent): **`178/1050
  \approx17\%` failures.** Concrete counterexample, hand-verified: `B=[9/2], X=[1/2,6], d=3/2`;
  brute force gives sparsest optimum `\xi^*=\{11/2\}` (value `5/2`, via matching `1/2` and `6`);
  dropping the sole element, `M=[9/2]`, `\delta_d=e([9/2,3/2])-e([9/2])=3-9/2=-3/2<0`.
- **Why this matters:** §29.3's own wording ("This suggests `\delta_d\ge0` is a fact about
  `B_1\cup(\xi^*\setminus\{\text{anything removed}\})` and `d` alone... plausibly provable... without
  needing the nearest-`c` property at all") is defensible as written (it only claims independence
  from the *tie-break choice*, which my test also confirms — `0/155` held for every `x`, not just
  nearest), but is one easy misreading away from "provenance-free," which I've now shown is false.
  This is the exact same failure pattern this project has hit repeatedly (No-Gap Lemma, half-step
  lemma, Deletion-Suffices, Sum Bound — see `run_state.md` Rules) — **every load-bearing positional
  fact in this proof needs genuine trigger+global-argmin provenance, and δ_d≥0 is no exception.**
  Recommend the outliner add an explicit line to §29's "Watch out for" list: *do not attempt a
  provenance-free symbolic proof of `\delta_d\ge0` — it is false in general (counterexample on
  file above); any proof must use `\mathcal F`-provenance, most likely through the same
  trigger/global-argmin mechanism as every other closed piece of this proof.*
- **Well-posedness check (requested explicitly):** the `\delta_d/\delta_c` split is a genuine,
  non-circular algebraic decomposition (Insertion-Difference Identity applied twice, `d` then `c`,
  both well-defined numeric quantities given `M,d,c`) — not a relabeling of the original target.
  Re-derived by hand: `RHS-e(M) = \delta_d+\delta_c` is an identity, and sub-target 2's claim
  (`\delta_c\ge-\delta_d`) is a legitimate, smaller-scope target once `\delta_d\ge0` is granted.
- Cross-check of the full nearest-`c` construction (the real end-to-end case-(a) target): **100**
  fresh genuine case-(a) instances, nearest-`c` chosen — `\delta_c` negative in **100/100** (file
  cites `\approx94\%`; my smaller/differently-parametrized sample landing at 100% is consistent
  sampling variance, not a discrepancy) — and the combined margin `RHS-e(M)=\delta_d+\delta_c`
  **never negative** (`0/100`, min margin `1/2`), corroborating case (a)'s actual target
  independently, not just the sub-target-1 split.

## Overclaims / circular reasoning / missing cases — overall §29 check

- No case-coverage gaps found: §29.1 covers all partners `j` uniformly (Per-Partner Domination is
  itself per-partner, no missing index); §29.2 covers all match partners uniformly under `\sigma=
  -1`; §29.3's case (a) is one arm of an already-exhaustive 3-way (a)/(b)/(c) split from §27.3,
  unchanged and not re-litigated here.
- No circularity found in §29.1's own proof (traced above). The one joint-induction well-foundedness
  concern (Two-Touch ↔ Per-Partner Domination, flagged above) is a **forward-looking risk for a
  future proof attempt**, not a flaw in anything actually written this round — §29.1's own 3-line
  proof uses nothing beyond already-certified/trivial facts and is genuinely correct as stated.
- Confirmed §29.1 honestly does NOT claim Per-Partner Domination is closed at general `q` (checked
  explicitly, see above) — the "quietly leaves it open" failure mode the dispatch asked me to check
  for does not occur; the file is explicit in multiple places.
- §29.4's priority ordering and "Watch out for" list are internally consistent with everything I
  independently re-derived; the two additions above (joint-induction ordering for §29.1's future use
  of Two-Touch; provenance-dependence of §29.3's `\delta_d\ge0`) are the only gaps I found, both
  non-fatal, both easy one-paragraph additions for the builder to carry forward.

## Population / ranking

Single live slug (`potential-weighting-upper-bound`); `dyadic-cascade-induction` and
`concavity-minimax-duality` remain correctly benched (no new leverage claimed or found this round,
reconfirmed). Registered no new approach (slug unchanged, already in the population). Ranked the
sampled field against the whole population per the standing protocol: `dyadic-cascade-induction`
(verified-milestone, top) beats `potential-weighting-upper-bound` (still `partial`, real but
incomplete progress on the standing bottleneck); `potential-weighting-upper-bound` beats both
benched/inactive `concavity-minimax-duality` and retired `elementary-exchange-smoothing` (no new
leverage from either, consistent with every prior round's comparison). This clears the `stale` flag
set by last round's reviewer.

## Recommendation for this round's build

§29.1 is ready to certify as written (near-zero cost, genuine closed result — Two-Touch fully proved
`|W|\le3` — independently reconfirmed above). §29.2 is the best risk-adjusted target (0 counterexamples
across a genuinely wide, freshly-reproduced sweep, with a concrete recommended proof shape — the
exchange argument comparing an optimal MATCH witness against an explicit KEEP-side witness built from
it). §29.3 sub-target 1 (`\delta_d\ge0`) is a real, independently-reproduced, low-risk target for a
third parallel thread, **provided** the builder is told explicitly (per the caution above) that it
must use genuine `\mathcal F`-provenance and not attempt a provenance-free proof.

**Build order for the single builder/thread(s) this round, in priority order:**
1. §29.1 — write up and certify formally (cheapest, real result, do not skip).
2. §29.2 — attempt the exchange-argument proof of the σ=-1 sibling-domination candidate.
3. §29.3 sub-target 1 — attempt `\delta_d\ge0` as its own standalone lemma, using genuine
   `\mathcal F`-provenance (trigger + global-argmin descent) throughout, explicitly not a
   provenance-free argument.
4. If a builder reaches Per-Partner Domination's general-`q` closure via Two-Touch's closed form
   (§25.2's suggested route), require it to explicitly verify the level-ordering (Two-Touch(`n-1`)
   → Per-Partner-Domination(`n`) → Two-Touch(`n`)) is well-founded before proceeding, per the new
   caution above.

build set: potential-weighting-upper-bound
