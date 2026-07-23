# Round 13 proof-review — `potential-weighting-upper-bound` §20

Reviewed: `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §20 (this round's
build, appended after §17–19), `/tmp/round-13/proof-builder-potential-weighting-upper-bound.md`,
`/tmp/round-13/outline-reviewer.md` (what §20 was dispatched to address), and the certified
`lemmas/empty-background-and-background-splitting.md`. All computation below is **fresh, from
scratch** (`/tmp/round-13/reviewer-work/`), not reusing the builder's, outliner's, or any
explorer's harness. My own `mydefs.py` (own `e()`, own `gen_selections`, own `OPT_sigma`/
`OPT_KD_sigma` brute force) was validated bit-for-bit against the file's own three worked examples
before being trusted (`OPT_{+1}([5,8],(10,8,7,2))=0/OPT\_KD=2`; `OPT_{+1}([1],(10,8,7))=0/1`;
`OPT_{-1}([2,4],(5,3))=4` — all reproduced exactly).

## 1. No-Gap Lemma's corrected half-open scope — CORRECT, independently re-derived

Re-derived the `h:=|\{c\in C:c\ge w_1\}|` case analysis from scratch for `C=\{x,y\}` (`x<y`)
myself, by hand, before running any code: `w_1>y\Rightarrow h=0`; `w_1=y\Rightarrow h=1` (equality
counts as dominating at the high end only); `x<w_1<y\Rightarrow h=1`; `w_1=x\Rightarrow h=2`;
`w_1<x\Rightarrow h=2`. This reproduces the builder's claim exactly: `h=1` iff `w_1` lies in the
**half-open** interval `(\min(x,y),\max(x,y)]` — the correction (from the outline-reviewer's
flagged open-interval imprecision) is mathematically right, not merely re-asserted.

The propagation argument (DELETE only removes `W`-elements, never touches `C`; KEEP at `h=0`
leaves `C` unchanged) is independent of whether the forbidden interval is open, closed, or
half-open — re-traced this myself and confirm it goes through unchanged for the corrected
statement, exactly as claimed.

**Independent fresh corroboration** (own `base_gen.py`, own trigger/argmin/`k^*` construction,
not the builder's `base_generator_instances`):
- Random sweep, `q\in\{3..7\}`, `v_{\max}\in\{1..5\}`, `20{,}000` raw trials: `2955` triggered
  instances, `7293` `z_j` checks, `0` strict violations, `0` half-open violations, `0` tie-hi,
  `0` tie-lo.
- **Exhaustive** (not sampled) sweep, `q\in\{3,4,5\},v_{\max}\in\{3,4\}`: `66`/`208`/`604`/`650`
  triggered instances (`66`/`416`/`1208`/`1950` checks) — `0`/`0`/`0`/`0` on all four counters,
  every case. (My instance counts differ from the builder's own exhaustive figures, expected from
  a different enumeration convention — I do not dedupe orderings of `Z_0` — but the qualitative
  finding, `0` violations everywhere, matches exactly.)
- Own from-scratch rational hill-climb (own perturbation code, not the outline-reviewer's
  `hillclimb_tie.py` nor the builder's `hillclimb_nogap.py`), step size down to `1/16`, `q=6`,
  60 restarts: best (smallest) margin found `=1/8`, **never `0` or negative** — consistent with
  the builder's own finding (infimum `0`, tight, never crossed) and independently corroborating it
  is not an "integer artifact."

**Verdict on this part: correct, no gap found.** The correction is real and precisely targeted at
the outline-reviewer's flagged issue.

## 2. Coincidence Identity and the swap construction — the trivial identity is correct; I went
further than the builder's own report and independently verified the associated **construction**
is a genuinely valid witness (not just an asserted one)

`d_i-d_l=z_l-z_i` is immediate substitution, correct, no issue.

The file additionally *describes* (§20.1) a construction: given an optimal witness `\eta^*` of
`A_{3,k^*}` that keeps `z_j`, build a new selection `\eta'` for `A_{3,j}` by swapping the
background token `d_{k^*}\to d_j` and giving `z_{k^*}` the "Keep" role vacated by `z_j`. The file
states this "is a valid selection... giving a genuine upper bound `A_{3,j}\le e(F')`" but does not
report having checked this claim computationally — it only reports the (separate, honestly
incomplete) sign argument as unfinished. **I independently implemented and tested this exact
construction from scratch** (own `swap_construction_value`, not reusing any of the builder's code):
across `813` triggered base-generator instances (fresh, `q\in\{4..7\}`, various `v_{\max}$), found
`1853` genuine "`\eta^*` keeps some `z_j`" events, and checked `A_{3,j}\le` the constructed value in
**every single one** (`1853/1853`, `0` failures). This corroborates that the construction really is
a legal witness (not merely a plausible-sounding assertion) — a positive finding beyond what the
builder's own write-up explicitly verified, though it does not change the bottom line: the sign
argument connecting this bound to a contradiction (needed to actually prove Gap 1a via this route)
is still missing, exactly as the file honestly states.

**Verdict on this part: correct and, on independent testing, sound as far as it goes; still
honestly incomplete, matching the file's own claim.**

## 3. Sum Bound `rest=empty` sub-case — **a genuine numerical overclaim found: the builder's "≥3×
margin, comfortably above the 2× needed" claim is FALSE as a general statement**

This is the one substantive problem this round. The file states (§20.2): "the ratio
`w_1/|c_1-c_2|` was never below `3`... a comfortable factor-of-1.5 margin... suggesting real
unused slack." I set out to independently re-verify this by constructing genuine `\mathrm{rest}=
\emptyset` nodes (own code, own `build_trigger`, checking `\max(c_1,c_2)<w_1:=\min(Z_1\text{'s
values})` after peeling, i.e. the base generator's own top level when `|Z_1|=1`, which already
satisfies `\mathrm{rest}=\emptyset` trivially — the simplest, most direct instance of the exact
sub-case the file discusses).

- Random sweep with the builder's own tested scale (`q\le6,v_{\max}\le7$-ish): reproduces "ratio
  never below 3" at that scale (min ratio found `4.0` in a first small pass).
- **Widening the value range** (still tiny, `v_{\max}` up to `10`, `q=3`, exhaustive not sampled)
  immediately finds counterexamples to "never below 3": `v_{\max}=8` gives the builder's own
  example almost exactly (`C=(3,1),w_1=6`, ratio `3.0`, exact match), but `v_{\max}=10` finds
  `C=(4,1),w_1=8$, ratio `8/3\approx2.667` — **below the claimed floor of `3`.**
- Pushing further (own exhaustive `q=3` sweep, `v_{\max}\in\{12,14,16,20\}`) reveals a **clean
  explicit family**: `Z_0=(n,n,n+1)`, `b_0=n/2$ (`n` even, `n>2`). By hand (and cross-checked in
  code for `n=4,\dots,1000`): `A_1=n/2` (every branch ties at `n/2`), `A_{3,\cdot}=n/2-1<A_1`
  (triggered for every `n>2`), `c_1=n/2,c_2=1`, `Z_1=\{n\}` (the sole surviving duplicate),
  `w_1=n`, ratio `=n/(n/2-1)=2n/(n-2)`. This **strictly decreases toward `2`** as `n\to\infty`
  (`n=4:4.0`; `n=10:2.5`; `n=100:\approx2.041`; `n=1000:\approx2.004$) — **always `>2` (the actual
  Sum Bound itself is never violated, `0` counterexamples found to `w_1\ge2|c_1-c_2|` in any test,
  including a broader random sweep up to `v_{\max}=50`, `40{,}000` trials) but with NO comfortable
  margin at all in the limit** — the true infimum of this ratio over genuine `\mathcal F`-provenance
  `\mathrm{rest}=\emptyset` nodes is exactly `2`, matching the bound's own tightness, not `3`.

**Root cause of the builder's error, precisely identified:** the builder's own saved harness
(`explore_sumbound.py`, inspected directly) caps `v_{\max}=5` (and a second pass `v_{\max}=6`) —
far too narrow a value range to reach the `(n,n,n+1)` family's asymptotic regime, which only
separates itself from `3` once `n\gtrsim8`. This is a **sampling-artifact overclaim**: a genuine,
reproducible inaccuracy in a computational finding presented as established ("comfortable margin,"
"real unused slack") that is not corroborated once the search is widened even slightly beyond the
builder's own tested range.

**This does not break Gap 1b itself** (the Sum Bound conjecture `w_1\ge2|c_1-c_2|` survives every
one of my own tests, `0` violations, ratio `\to2` but never below `2`) — if anything this is a MORE
useful and MORE precise finding for the next round than the builder's own (it tells a future prover
the bound is asymptotically **tight**, so a proof attempt should not expect slack to exploit, in
direct contradiction to the file's own "suggesting real unused slack" framing, which risks
misdirecting a future round). **Action required:** §20.2's "≥3× margin" / "comfortable factor-of-1.5
margin" claim must be corrected to reflect the true asymptotic infimum of `2` (tight), with the
`(n,n,n+1)`/`b_0=n/2` family flagged as the extremal witness family, before this section is treated
as reliable groundwork for a future attempt.

## 4. Gap 1c counterexample `C=[3],W=(4,1,0)` — reproduced exactly, genuinely outside `\mathcal F`'s
own provenance scope, no contradiction with other findings

Independently recomputed: `OPT_{+1}([3],(4,1,0))=0`, achieved by **exactly** two optimal witnesses,
`\{M(4,1),K(0)\}` and `\{M(4,1),D(0)\}$ — both matching `w_1=4`. `OPT\_KD_{+1}([3],(4,1,0))=1`.
Matches the file's claim bit-for-bit, including the exact witness set. This is a genuine
forced-matching event at background size `1`.

**Checked the provenance question explicitly** (per the dispatch): does this contradict `|C|=2`
always holding at the base generator (§19.1, "`|C|=2` always at the base generator")? No — `C=[3]`
has size `1`, which the file's own already-established structural fact says never arises as a
genuine base-generator background (`B_1=B_0\cup\{d_{k^*}\}$ always has size exactly `2`). So this
counterexample is correctly outside `\mathcal F`'s own scope, exactly as the builder describes —
it refutes the *fully general, provenance-free* claim (a legitimate, useful negative result) without
creating any tension with the separately-maintained "`0` forced-matching events within `\mathcal F`"
finding. **Independently re-confirmed the latter too**, with a fresh from-scratch DELETE/KEEP
closure walk (own `closure_walk.py`, own construction, not reusing the builder's): `302` triggered
base generators, `2122` closure nodes to depth 3, **`0`** forced-matching events; and, as an
additional cross-check not explicitly requested but directly relevant, Claim A itself
(`\mathrm{OPT}_\sigma=\mathrm{OPT\_KD}_\sigma`) checked on the same walk, `3426` nodes, **`0`**
violations — consistent with everything on file.

**Verdict on this part: correct, no error found.**

## 5. Status

The builder's own Status header ("partial — unchanged, no gap closed this round") is accurate and
not overclaimed anywhere in the file — none of Gaps 1a/1b/1c is proved; §20.4's own honest summary
matches what was actually established. `current.md`'s Status correctly stays `partial` — no full,
rigorous proof exists for any `m` beyond what was already on record, let alone for general `n`.

## Certification of promotable lemmas

**Coincidence Identity** — declined for standalone certification. It is a one-line algebraic
identity (`d_i-d_l=z_l-z_i`, immediate substitution) with no independent reusability beyond its
single, still-incomplete application in §20.1; the builder itself flags it as "likely too
minor/incomplete-in-its-application to certify... yet." I agree — certifying it as a separate
`lemmas/` file would not meet the bar of a genuinely reusable, general-purpose fact distinct from
its one current (unfinished) use. It remains on file in §20.1 for the next round to build on.

No other new lemma was proposed for certification this round.

## Verdict: **CHANGES REQUESTED** (Status: `partial`)

The technique (strong induction via the `\mathcal F`-scope reduction, now with the No-Gap Lemma's
scope precisely corrected) remains sound; real, well-verified progress was made (the half-open
correction, the swap-construction's independently-confirmed validity, the Gap 1c negative result).
**One genuine numerical inaccuracy was found and must be fixed before the next round treats §20.2 as
reliable:** the "Sum Bound `rest=\emptyset$ sub-case has a comfortable `\ge3\times` margin" claim is
false — an explicit family (`Z_0=(n,n,n+1),b_0=n/2`) drives the ratio down to an asymptotic infimum
of exactly `2` (tight, not `3`), a sampling artifact of the builder's own narrow tested value range
(`v_{\max}\le7`). This does not break the Sum Bound conjecture itself (still `0` violations found,
including in my own broader sweep) and does not change the file's own honest `partial` Status, but
it is a concrete, previously-undetected error the next builder must correct rather than build on.
**Exact gap list carried forward, unchanged in substance, with one correction:**
1. Gap 1a (No-Gap base case) — statement now correctly scoped (half-open); the base-case proof
   itself (using `k^*`'s global-argmin property and the trigger `M<A_1`) remains open. The
   Coincidence-Identity swap construction is available and independently confirmed valid, but the
   sign argument connecting it to a contradiction is not yet built.
2. Gap 1b (Sum Bound) and 1b' (its `\sigma=-1` mirror, still unformulated) — remain open; **the
   `rest=\emptyset` sub-case's true difficulty should be recorded as "asymptotically tight at ratio
   `2`," not "comfortable margin,"** per finding 3 above.
3. Gap 1c (MATCH-vs-DEL/KEEP) — the cheapest fully-general shortcut is correctly ruled out
   (confirmed); the existence claim within `\mathcal F` itself remains open, direct construction is
   the recommended next step, unchanged.

Route: **CHANGES REQUESTED** — re-dispatch `potential-weighting-upper-bound`'s builder to (a) correct
the Sum Bound margin claim in §20.2 (cheap, a documentation fix, not a new proof attempt) and (b)
continue attacking Gaps 1a/1b/1c per the existing priority order.
