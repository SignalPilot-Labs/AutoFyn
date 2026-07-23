## imo-2026-03 — MATCH-branch direct attack (Two-Touch's Match-Branch Domination)

### Headline finding (rigorous, not just corroborated): Two-Touch's Match-Branch Domination is an
EXACT corollary of Gap 1a's Per-Partner Domination Lemma — not merely "kin" to it, literally the
same inequality, via a clean 3-line reduction. This closes Two-Touch fully and unconditionally for
`|W|<=3` and reduces Two-Touch's entire general-`q` MATCH branch to Per-Partner Domination's already
-tracked general-`q` gap, with zero extra work once that closes.

**The reduction.** Recall Two-Touch's peeling trichotomy for `OPT_{+1}({b_0},W)` (`w_1:=max(W)`):
the MATCH branch, matching `w_1` with partner `w_j`, has value
`MATCH_j := OPT_{+1}({b_0,d_j}, W\{w_1,w_j})`, `d_j:=w_1-w_j`. **This is *literally* Gap 1a's own
`A_{3,l}` quantity** (`A_{3,l}:=OPT_{+1}(B_0\cup\{d_l\}, Z_0\setminus\{z_1,z_l\})`, `d_l:=z_1-z_l`),
under the pure renaming `B_0={b_0}\leftrightarrow\{b_0\}`, `Z_0\leftrightarrow W`, `l\leftrightarrow
j` — not an analogy, the identical definition. The needed target is
`MATCH_j\ge\mathrm{TwoTouch}(\{b_0\},W)=:TT`. Two already-available facts bound `A_1` and `D_l` (in
Gap 1a's own notation) below by `TT`:
1. `A_1:=OPT_{+1}(\{b_0\},W\setminus\{w_1\})` **is literally Two-Touch's own DELETE branch**,
   already **unconditionally proved `\ge TT`** by the file's own §26.5(b) (candidate-set-inclusion
   argument via the strong induction on `|W|`, no gap).
2. `D_l=D_j:=|b_0-d_j|=e(\{b_0,d_j\})` is **trivially** `\ge TT`, since `e(\{b_0,d_j\})` is
   *literally* one of `\mathrm{TwoTouch}(\{b_0\},W)`'s own candidate terms (matching `w_1,w_j` is
   one of TwoTouch's `\le2`-touch candidates by definition) — `TT\le D_j` by definition of the
   min, needing no proof at all.

So **`\min(A_1,D_j)\ge TT`** unconditionally (both terms individually `\ge TT`). Combined with
**Gap 1a's Per-Partner Domination Lemma** (`A_{3,l}\ge\min(A_1,D_l)`, proved `q\le3`, corroborated
general `q`): `MATCH_j=A_{3,j}\ge\min(A_1,D_j)\ge TT`, i.e. Match-Branch Domination, **exactly**,
with no residual gap beyond Per-Partner Domination itself.

**Consequence — Two-Touch is now unconditionally closed for `|W|\le3`.** At `|W|=3`, the MATCH
branch's sub-problem has `|X_j|=1`, i.e. exactly `q=3` in Gap 1a's own notation (`|Z_0|=3`) — the
regime Per-Partner Domination is **already fully proved** in, unconditionally. Combined with the
already-unconditional DELETE branch (every `|W|`) and KEEP branch (`b_0>w_1` unconditional; `b_0\le
w_1$ needs Three-Touch at `|W|-1=2`, which Lemma B this round already proves unconditionally for
`|W|\le3`, well within range), **all three branches of the `|W|=3` trichotomy are now unconditionally
closed** — Two-Touch (`\sigma=+1`) is fully proved for `|W|\le3`, strictly extending the previously
-proved base case (`|W|\le2`) by one level, via genuinely new content this round.

**At general `q\ge4`:** the reduction still holds (it uses no hypothesis beyond Per-Partner
Domination itself, which is `q`-parametrized identically), so **Match-Branch Domination is not
independent open content at any `q` — it is entirely subsumed by Per-Partner Domination's own
already-top-priority general-`q` gap.** This upgrades §27.2(e)'s "structural kinship, not proved
identical" note (round 17) to a fully proved identification for the `\sigma=+1` (Two-Touch) side. It
also means: a future round should **stop budgeting separate effort for "Match-Branch Domination"** as
a nominally distinct target — attacking Per-Partner Domination at general `q` (already flagged
highest-leverage) automatically closes this too.

**Computational corroboration of every non-reduction ingredient (fresh, bounded, exact-`Fraction`,
`/tmp/round-18/explore_match/`):**
- Direct re-verification of Match-Branch Domination itself (`MATCH_j\ge TT`, as previously reported):
  `0/910` (random, `q\in\{3,5\}`, `v_{\max}\le6`).
- The candidate reduction target `MATCH_j\ge\min(\mathrm{DELETE},|b_0-d_j|)` (i.e. `A_{3,j}\ge\min
  (A_1,D_j)`, restated in Two-Touch's own variables — this is the SAME Per-Partner Domination Lemma,
  re-tested from a completely different code path than any prior round's harness): **`0` failures
  across `\sim10{,}900` combined checks** — `0/2477` (three random batteries, `q\in\{3,\dots,8\}`,
  `v_{\max}\in\{8,10,15\}`, up to `50\%` duplicate-heavy), `0/1326` (two **exhaustive** grids,
  `q\le3,v_{\max}=3` and `q\le4,v_{\max}=2`), `0/3410` (three further random batteries testing this
  specific min-of-two-bound form), `0/60` (dyadic/superincreasing families `D_1,\dots,D_4`-shaped,
  directly relevant to the theorem's own extremal construction), `0/3610` (near-tie/duplicate-cluster
  adversarial family, after catching and fixing a generator bug that had produced *negative* `W`
  -values outside the problem's domain — the initial "15/1781 failures" were 100% artifacts of that
  bug, confirmed by re-running with the fix and getting `0/3610`; a fresh instance of Rule 14's lesson
  about verifying sampler validity before trusting a negative result).
- **Negative controls confirming both `A_1` and `D_j` are load-bearing** (neither term alone
  suffices, so this is a genuine two-term disjunction, not a disguised single bound): dropping `D_j`
  (testing `MATCH_j\ge A_1` alone) fails **`132/1204`, `151/1310`, `35/896`** (`\approx11$–`17\%`)
  across three batteries; dropping `A_1` (testing `MATCH_j\ge D_j` alone) fails **`656/1204`,
  `782/1310`, `650/896`** (`\approx54$–`73\%`) — both individually insufficient, matching exactly the
  qualitative shape of Gap 1a's own already-certified negative controls for Per-Partner Domination.

**Recommended concrete next step for the outliner/builder:** state this reduction as a formal 3-line
lemma in the approach file (it needs no new proof beyond citing §26.5(b)'s DELETE-branch proof, TT's
own definition, and Per-Partner Domination), certify the `|W|\le3` extension of Two-Touch as a genuine
new proved result, and retarget all future MATCH-branch build effort at Per-Partner Domination's
general-`q` closure exclusively — do not reopen "Match-Branch Domination" as a separately-tracked
open item.

### Secondary finding (negative/partial) — the naive `sigma=-1` mirror does NOT transfer; explains the
touch-depth asymmetry

Tried the obvious mirror for Three-Touch's own (still fully open) MATCH branch: a `\sigma=-1` "Mirror
Per-Partner Domination" candidate `A'_{3,l}:=OPT_{-1}(\{c,d_l\},\mathrm{Res})\le\max(A'_1,D'_l)`,
`A'_1:=OPT_{-1}(\{c\},Z\setminus\{z_1\})` (Three-Touch's own DELETE branch), `D'_l:=|c-d_l|`. **This
naive 2-term max FAILS at a real rate, not a corner case:** `130/876` (`14.8\%`), `101/922`
(`11.0\%`), `55/711` (`7.7\%`) across three random batteries (`q\in\{3,\dots,8\}`). Diagnosed by hand
(exact worked example `c=5,Z=(8,0,3,4,3,2)`): the maximizer's true winning strategy is often to
**additionally keep or match elements *within* `\mathrm{Res}` itself** (e.g. one concrete failure's
optimal witness is `\{c,d_l\}\cup\{z_m\}` for `z_m\in\mathrm{Res}`; another needs `\{c,d_l\}\cup\{|z_i
-z_j|\}$ for `i,j\in\mathrm{Res}`, a completely independent second match) — richness the 2-term bound
cannot see. **Tried augmenting with a 3rd term** (`\max_{z_m\in\mathrm{Res}}e(\{c,d_l,z_m\})`,
motivated directly by the diagnosed failure mode): failure rate drops to `\approx2$–`4\%` (`22/1064`,
`24/1170`, `24/896`, `33/877`) but is **still nonzero** — the residual failures trace to the *second*
diagnosed mechanism (matching two *other* `\mathrm{Res}` elements together), which a 3-term family
still can't express. **This is not a dead end to abandon outright, but it is genuinely harder than the
`\sigma=+1` side and should NOT be assumed to have a simple closed form** — the pattern (needing
richer and richer touch-structures the deeper you look) is exactly the same shape that already made
the general `|C|=2` Two-Touch formula FALSE (`\approx24$–`32\%$ failure, certified dead end, do not
re-derive it here either). **This computationally explains, for the first time, *why* the file's own
touch-depth asymmetry exists** (Two-Touch needs `\le2`, Three-Touch needs `\le3`): the maximization
side's own two-element background (`\{c,d_l\}`) can already be pushed down via candidates entirely
*inside* `\mathrm{Res}$ (both single-keep and match-pair), a genuine additional degree of freedom the
minimization side's Per-Partner Domination never needed (there, `\min(A_1,D_l)` sufficed because the
minimizer's smallest achievable value is always realized by "delete everything" or "keep/match only
the specific pair," never by *also* exploiting `\mathrm{Res}$'s internal structure — worth someone
double-checking why this asymmetry is directional, not just empirically confirming it, in a future
round if this exact mirror is revisited).

### Dead ends confirmed on record — do not re-attempt

- Round 17's "let `d` become optional instead of forced" reduction for Two-Touch's MATCH branch
  (`\mathrm{TwoTouch}(\{b_0\},X\cup\{d\})\ge\mathrm{TwoTouch}(\{b_0\},W)`) — **FALSE**,
  `b_0=5,W=(8,10,8),w_j=8` gives `d=2`, `\mathrm{TwoTouch}(\{5\},\{8,2\})=1<3=\mathrm{TwoTouch}(\{5\},
  \{8,10,8\})`. Confirmed still false, not retested (per instructions), just flagged as still-dead.
- The general `|C|=2` Two-Touch closed form (both as an equality and as a one-directional lower
  bound) — confirmed dead in prior rounds (`\approx24\%$/`35.8\%` failure); this round's
  `sigma=-1` mirror investigation independently re-confirms the *mechanism* behind that failure
  (internal-`\mathrm{Res}` richness) rather than the formula itself — do not resurrect either.
- My own initial "adversarial near-tie" sweep (`harness8.py`, uncorrected) reported `15/1781`
  failures for the MAIN (`\sigma=+1`) finding — **this was a generator bug** (produced negative,
  out-of-domain `W`-values), not a real counterexample; fixed version (`harness8b.py`) gives
  `0/3610`. Recorded here so a future round doesn't need to re-diagnose this if the raw log is ever
  consulted.

### What was NOT attempted this round (per dispatch scope)

Crux-corpus re-querying was not repeated — the file's existing `aimo-0960` mapping (§27.3, extremal
witness + secondary tie-break + local rewrite) remains the population's best-documented crux lead and
is unrelated to this round's MATCH-branch-specific computational task; no new corpus search was run.

### Summary for the outliner

1. **Certify-ready (module a short write-up):** Two-Touch's Match-Branch Domination `\equiv` Gap 1a's
   Per-Partner Domination (exact reduction, 3 lines, uses only already-proved/trivial ingredients).
   Two-Touch is now fully unconditionally proved for `|W|\le3` (new result this round). Retarget all
   future "MATCH branch" build effort onto Per-Partner Domination's general-`q` closure alone — for
   the `\sigma=+1` side, there is no longer a separate Two-Touch-specific MATCH problem.
2. **Genuinely harder, not a quick corollary:** Three-Touch's own MATCH branch needs its own richer
   mirror machinery (2-term mirror fails `\sim7$–`15\%`, 3-term reduces but doesn't close, `\sim2$–
   `4\%$ residual) — real, but incomplete, progress; flag as a separate, harder open item, not
   assumed free once Per-Partner Domination closes.
