# Round 5 proof-reviewer report — imo-2026-03

All three built approaches reviewed adversarially. All independent recomputation was done with
exact `Fraction`/integer arithmetic (scripts run in `/tmp/verify_step3.py`,
`/tmp/verify_slack.py`, `/tmp/verify_oneshot.py`, `/tmp/verify_concavity.py`). No hidden
overclaims found in any of the three files' own Status sections — all three correctly stay
`partial`. Problem-level `current.md` Status also correctly stays `partial`.

---

## 1. `dyadic-cascade-induction` — VERDICT: **APPROVE the new lemma content / CHANGES REQUESTED for the approach**

(Per CLAUDE.md's per-approach routing: the approach's own Status is `partial`, not `solved`, so
the routing verdict for the *slug* is **CHANGES REQUESTED**. The new §5.3 result itself is
fully correct and is certified as a standalone lemma — see below.)

**What was claimed.** A full proof of the "Superincreasing No-Early-Zero Lemma": for strictly
superincreasing `a_1>...>a_k>0`, no legal sequence of `t<k` D/M operations ever reaches `e=0`.
Claimed this makes the D/M-*sequence* lower bound `h(D_m,m)\ge e_m\cdot S(D_m)` unconditional
for every `m`, with the promotion to the true *physical* lower bound still gated on the
pre-existing `lemmas/dm-completeness-partial.md` "all-cycles" caveat.

**Independent verification performed.**
- Re-derived the whole 4-step proof (3.1 non-vanishing signed subset sum; 3.2 token invariant
  by induction on operation count; 3.3 corollary of pairwise-distinct positive active tokens;
  3.4 strict alternating sum of distinct positives is positive; 3.5 assembling the theorem) from
  scratch. No gap found. Checked in particular:
  - **Base case**: trivial, distinct singletons, correctly handled.
  - **Every D/M operation type covered**: `D(x)` (token retirement, no new ties possible — both
    invariants trivially preserved) and `M(x,y)` (disjoint-union index sets, correctly derived
    equation for the new signed sum) are both explicitly handled — no operation type is
    skipped.
  - **"Index sets stay pairwise disjoint" is proved, not assumed**: (I1) is established by
    induction alongside (I2), using only that `S(x)`,`S(y)` were already disjoint from every
    other active set at the previous step — a clean, non-circular induction.
  - **The classical superincreasing fact (3.1)** is correctly stated (`a_i > a_{i+1}+...+a_k`
    for all `i<k`) and its proof (isolate the min-index term, bound the rest by the
    superincreasing hypothesis, reverse triangle inequality) is standard and correct.
  - **Rescaling (§3.7)**: `e` scales linearly under positive scalar multiplication (order is
    preserved under positive scaling, so the alternating-sum formula scales termwise); D/M
    sequences on `D_m` and its normalization `\widetilde D_m` are in an explicit,
    order-preserving bijection. Both claims correctly and explicitly proved (not left
    implicit, as the file itself notes was a prior-round gap).
- **Independent computational check** (exhaustive, not sampled): exact-integer BFS over the
  entire D/M-reachable state space from `D_m`, `m=1..5` — confirmed the minimum number of
  operations to reach `e=0` is exactly `m+1=k` in every case (matching the theorem exactly,
  not merely `\ge`), and the minimum `e` after exactly `m` operations is exactly `1` in every
  case. Also ran 15 fresh random strictly superincreasing sequences (sizes 3–5, built
  bottom-up to guarantee the superincreasing property): every one required exactly `k`
  operations to reach `e=0`, zero exceptions — corroborating the *general* form of the theorem,
  not just the `D_m` specialization.
- **Honest-accounting check**: confirmed the file does NOT claim this closes the physical lower
  bound outright — §5.3's closing "Watch out for" section explicitly and correctly states the
  all-cycles caveat is inherited, unresolved, unaffected by this round's work. This matches the
  dispatch's framing exactly. No overclaim.

**Verdict on the new content.** Correct, complete, rigorous, independently re-verified both
symbolically and by exhaustive computation. **Certified as a new lemma:**
`results/imo-2026-03/lemmas/superincreasing-no-early-zero.md`.

**Verdict on the approach file as a whole.** `partial` (correctly self-reported). Real,
substantial new progress (an entire previously-open sub-mechanism — the D/M-sequence lower
bound across every `m` — is now unconditionally closed), but the approach does not close the
theorem: Case (ii) upper bound at general `m` remains open, and the physical (non-D/M) lower
bound still needs the all-cycles caveat. **Routing: CHANGES REQUESTED** (not RETHINK — this is
squarely "correct progress, real gap remains," per CLAUDE.md's definition, not a broken
approach).

**Gap for the next round to attack (this file specifically):** the "all-cycles" tie-dependency
caveat in `dm-completeness-partial.md` is now the *sole* remaining obstruction on the
lower-bound side (for this approach's route). Either prove it cannot occur for `A=D_m`
specifically, or find/rule out a genuine all-cycles configuration.

---

## 2. `potential-weighting-upper-bound` — VERDICT: **CHANGES REQUESTED**

**What was claimed.** A "Slack Collapse" lemma: if `k\le m` (Liu Bang uses fewer than `n`
marks), Xiang Yu trivially forces `e=0`, reducing the entire upper-bound induction (Case (i)
and (ii), every `m`) to the tight sub-case `k=m+1`. Also: falsification of the outline's
"sorted-adjacency" conjecture with two exact counterexamples; a replacement "non-crossing
matching+deletion" conjecture, stress-tested but honestly reported as unproved; a ruled-out
local uncrossing-exchange proof technique.

**Independent verification performed.**
- **Slack Collapse lemma**: re-derived from scratch as an immediate corollary of the
  already-certified Fact 5 (chain-cancellation). Independently re-implemented Fact 5's
  recursive construction (2000 random trials, exact `Fraction`, sizes 0–6): `e=0` achieved
  using exactly `L` cuts in every trial, zero violations — confirms the mechanism the lemma
  invokes. The corollary ("reduces the WHOLE upper-bound induction... to k=m+1") is a
  correct, direct restatement: the theorem's claim is only non-trivial when `k=m+1` (using all
  `n` marks), and Slack Collapse disposes of every `k<m+1` configuration unconditionally,
  independent of case or specific values — verified this is not a narrower claim in disguise
  (checked: no hidden restriction to only the top-level game — since any residual sub-problem
  with `k'<m'+1` at ANY point is equally covered by the same lemma, applied directly to that
  residual). No misuse of the certified-dead-end "residual stays below ceiling" argument — this
  is a different, valid use of Fact 5 (exact achievability of `e=0`, not a lossy bound).
- **Falsification counterexamples, recomputed independently** via a from-scratch exhaustive
  one-shot-allocation search (own implementation, not reusing the file's code):
  - `A=(82,66,47,40)`, `m=3`: unrestricted best `=5` (exact match to `{35,40}` via deleting 66,
    matching `(82,47)\to35`), adjacent-only best `=7` (exact match, via deleting `82,66`,
    keeping `{47,40}`) — **both values and both winning selections reproduced bit-for-bit.**
  - `A=(46,44,31,21,15)`, `m=4`: unrestricted best `=0` (`\{15,15\}` tie), adjacent-only best
    `=2` (`\{46,44\}`) — **reproduced exactly.**
  - Local-uncrossing counterexample `Y=(43,33,20,16,11,8,2)`: crossing pairing gives `e=15`,
    both alternatives (nested, disjoint) give `e=25` — **all three values reproduced exactly**
    by independent computation.
- **Honesty check on the non-crossing conjecture**: confirmed the file repeatedly and
  explicitly labels it "NOT proved," "numerically supported... but not proved," and gives an
  explicit counterexample ruling out the natural proof technique (local exchange) rather than
  silently omitting the negative finding. No overclaim.

**Verdict on the new content.** The Slack Collapse lemma is correct, general, and independently
re-verified. **Certified as a new lemma:** `results/imo-2026-03/lemmas/slack-collapse.md`. The
falsification and the honest negative results are all independently confirmed accurate.

**Verdict on the approach file as a whole.** `partial` (correctly self-reported): real new
lemma content (narrows the open case to `k=m+1`), a genuine falsification (prevents a future
round from building on a false conjecture), and an honestly-reported unproved replacement
conjecture with one ruled-out proof technique. The central Case (ii) mechanism is still open.
**Routing: CHANGES REQUESTED.**

**Gap for the next round:** prove the non-crossing matching+deletion conjecture (§7.3) — the
concrete, sharpened target — via a genuinely global argument (e.g. a DP/induction on the
non-crossing-partition recursion), since the natural local-exchange technique is now a
confirmed dead end for it.

---

## 3. `concavity-minimax-duality` — VERDICT: **CHANGES REQUESTED**

**What was claimed.** Two new general lemmas: Cascade reachability (`D_j\to D_{j-1}` via a
single `M(2^j,2^{j-1})`, hence `D_j\to\{1\}` in exactly `j` ops) and Forced-value Lemmas A/B
(any valid 1-Lipschitz weak-duality certificate `g` must have `g(1)=1`, `g(2)=2` exactly, for
every `m`), plus two exact refutations of clip candidates `\min(t,1)` and `\min(t,2)`. No
working closed-form `g_m` found — reported honestly as still open.

**Independent verification performed.**
- **1-Lipschitz weak-duality lemma**: the pairing/triangle-inequality proof is standard and
  correct; re-checked line by line, no gap.
- **Cascade reachability**: independently recomputed `M(2^j,2^{j-1})` applied to `D_j` for
  `j=1..6` — exact match to `D_{j-1}` in every case. Full cascade `D_j\to\{1\}` confirmed to
  take exactly `j` operations for `j=1..6`.
- **Forced-value Lemma A/B proofs**: re-derived from scratch — both are short, correct
  sandwich arguments (reachability witness + Lipschitz bound in each direction), no gap.
- **`\min(t,1)` refutation**: independently recomputed `e_g(D_m)` with `g=\min(t,1)` for
  `m=1..6` — confirmed exactly `0` for every odd `m`, `1` for every even `m`, matching the
  file's closed-form telescoping claim exactly (not merely a stress-test-consistent value).
- **`\min(t,2)` refutation**: independently confirmed the witness `(4,2,\tfrac12,\tfrac12)` is
  reachable from `D_m` within `m-1\le m` operations for `m=2..6` (cascade to `D_2`, then bisect
  the trailing `1`) — exact match to the file's construction in every case, and the forced
  contradiction (`g(4)\ge3` vs. `\min(4,2)=2`) is correctly derived.
- **Circularity finding (§11.2)**: the argument that any finite sample on which the raw claim
  is already known to hold makes the LP trivially feasible via `g=\mathrm{id}` is a valid,
  elementary observation (since `e_{\mathrm{id}}=e` exactly by the weak-duality lemma's own
  equality case) — correctly identified as undermining the naive "run the LP, report SAT" plan
  from §10, and reported as a genuine methodological finding rather than buried.
- **No-overclaim check**: confirmed the file explicitly and repeatedly states "no working `g_m`
  was found this round" and frames Steps 11.6–11.7's irregular LP output and failed 2-slope
  family as negative results, not partial successes. No dead-end mechanism (global concavity of
  `g`, greedy Rule 1/2, bounded lookahead, merging monotonicity, residual-stays-below-ceiling)
  is silently reintroduced anywhere in §10–§11.

**Verdict on the new content.** All claims correct and independently re-verified exactly.
**Certified as a new lemma:**
`results/imo-2026-03/lemmas/lipschitz-certificate-and-forced-values.md` (bundling the weak-duality
lemma, cascade reachability, and Forced-Value Lemmas A/B — all fully general-purpose and
reusable).

**Verdict on the approach file as a whole.** `partial` (correctly self-reported): real
structural progress (necessary conditions any certificate must satisfy, two candidates exactly
refuted, a methodological trap identified and avoided), but the central goal (a working
closed-form `g_m`) remains unfound. **Routing: CHANGES REQUESTED.**

**Gap for the next round:** the file's own flagged next step — a recursive ansatz
`g(2^{j+1}):=g(2^j)+1+(\text{something}\le2^j-1)` built from the general
`(2^{j+1},2^j,\tfrac1{2^k},\tfrac1{2^k})`-type witness family (generalizing the Step 11.5
witness beyond `j=1`) — is untested and the most concrete lead.

---

## Cross-cutting checks (per dispatch)

- **No certified dead end silently reintroduced.** Checked explicitly against all six flagged
  dead ends (global concavity of `g`; greedy Rule 1/Rule 2; bounded lookahead; merging
  monotonicity; residual-stays-below-ceiling; unconditional/unqualified D/M-completeness). None
  reappear. In particular: `potential-weighting-upper-bound`'s Slack Collapse correctly uses
  Fact 5 for *exact* achievability (a different use from the dead "residual stays below
  ceiling" argument, which was about a *lossy bound* on a residual, not exact achievability —
  confirmed these are genuinely distinct uses of the same underlying Fact 5, not a reintroduction).
  `dyadic-cascade-induction`'s §5.3 correctly treats D/M-completeness as still conditional
  (citing the certified `dm-completeness-partial.md`, not claiming it unconditionally).
- **No "for every m" overclaim secretly only holding through small m.** All three new "for
  every m" claims (No-Early-Zero Lemma, Slack Collapse, Forced-Value Lemmas A/B) were checked
  for whether their inductive/computational verification actually covers the general-`m`
  argument (not just tested small cases) — in all three, the *proof* itself is `m`-free
  (parametrized abstractly, not case-split by `m`), and the computational checks (BFS up to
  `m=5..6`) are corroboration, not the load-bearing argument. No hidden small-`m`-only
  dependency found.

## Certified lemmas this round

1. `results/imo-2026-03/lemmas/superincreasing-no-early-zero.md` (from `dyadic-cascade-induction`)
2. `results/imo-2026-03/lemmas/slack-collapse.md` (from `potential-weighting-upper-bound`)
3. `results/imo-2026-03/lemmas/lipschitz-certificate-and-forced-values.md` (from `concavity-minimax-duality`)

## `current.md` updates

Updated `## Status` (stays `partial`), `## Approaches tried` (added round-5 entries for all
three slugs with certification notes), and `## Current best` (added the three new certified
lemmas, sharpened the "what remains open" list to reflect that both the lower-bound gap and the
upper-bound gap are now each reduced to a single, precisely-isolated open sub-problem across
every `m`, rather than the previous per-instance/per-technique framing).

## Outcomes recorded (`mcp__approach-ranker__record_outcome`)

- `dyadic-cascade-induction`: `advanced` — Superincreasing No-Early-Zero Lemma closes the
  D/M-sequence lower bound unconditionally for every m.
- `potential-weighting-upper-bound`: `advanced` — Slack Collapse lemma reduces the whole
  upper-bound induction to k=m+1; sorted-adjacency falsified, non-crossing replacement proposed.
- `concavity-minimax-duality`: `advanced` — Cascade reachability + Forced-Value Lemmas A/B give
  exact refutations of two candidate certificates; honest circularity finding on the LP check.

## Summary verdicts

| Slug | Status (true) | Verdict |
|---|---|---|
| `dyadic-cascade-induction` | `partial` | CHANGES REQUESTED |
| `potential-weighting-upper-bound` | `partial` | CHANGES REQUESTED |
| `concavity-minimax-duality` | `partial` | CHANGES REQUESTED |

No RETHINK this round — all three approaches remain viable and made genuine, independently
verified progress. No APPROVE — the theorem (both directions, all `n`) is not yet fully proved;
`current.md`'s Status correctly stays `partial`.
