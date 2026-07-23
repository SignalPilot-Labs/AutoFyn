# Round 19 outline review — imo-2026-03

Independently re-verified everything with fresh, from-scratch code (`/tmp/round-19/verify/*.py`),
not reusing any explorer's or outliner's harness. Definitions (`e`, `all_selections`, `OPT`) re-derived
from `/tmp/round-16/proof-reviewer-verify/defs.py` and cross-checked against the file's own 4 worked
sanity examples before use (all matched exactly: `OPT_{+1}([5,8],(10,8,7,2))=0`,
`OPT_{-1}([5,8],(10,8,7,2))=10`, `OPT_{+1}([1],(10,8,7))=0`, `OPT_{-1}([2,4],(5,3))=4`).

## 1. `potential-weighting-upper-bound.md` §31 and §32

### §31 — Generalized Touch-Bound Lemma candidate (general `|C|=k`)

Verdict: **sound as a stated candidate, correctly labeled CONJECTURAL, no overclaim.**

- Re-implemented `touch<=k` candidate evaluation from scratch (independent of the file's/explorer's
  code) and re-tested the two load-bearing numeric claims:
  - `|C|=2`, `touch<=4` closed form vs true `OPT_{+1}`: **0/3000** fresh random trials — reproduces
    the file's `>10,000 combined, 0 failures` claim.
  - `|C|=2`, the already-dead `touch<=2` formula: **423/2160 (19.6%)** failures — matches the file's
    cited "18-24%" almost exactly, confirming the `touch<=2` dead end is correctly distinguished from
    the new `touch<=4` candidate (these are genuinely different thresholds, not a relabeled retry).
  - The claimed `k=3` threshold-separating evidence (`2k=6` vs `k+2=5`): built a fresh test forcing
    `|W|\in\{6,7\}` (large enough that `touch\le5` and `touch\le6` actually differ from the true
    optimum): **`touch<=5` (k+2) failed 3/600**, **`touch<=6` (2k) failed 0/600** — independently
    confirms `2k` is the right threshold identification, not `k+2`, exactly as the file claims.
- The section is honestly scoped: Step 3 (inductive step peeling one element of `C`) and Step 4
  (finite case analysis) are both explicitly marked "not attempted" — no hidden proof-by-assertion.
  The "watch out for" note correctly warns against conflating this with the dead `touch<=2` formula
  and against reusing Background-Release Domination's two already-dead chaining routes without
  re-checking. No fatal flaw; this is legitimate exploratory scaffolding, not a load-bearing claim
  presented as proved.

### §32 — candidate proof of the KEEP `b0<=w1` sub-case of Two-Touch at `|W|=3`

Verdict: **sound as a stated candidate, correctly hedged, no overclaim — and I could not find a
counterexample to any of the 6 sub-claims (target, 5 per-term bounds, Two-Variable Reflection Bound).**

- Confirmed `ThreeTouch(b0,rest)` at `|rest|=2` is validly cited: Lemma B
  (`lemmas/max-element-triple-identity-and-threetouch-basecase.md`) is certified unconditionally for
  `|W|<=3`, and `|rest|=2<=3` — this is a correct in-scope citation, not an extension past what was
  certified (unlike the round-18 overclaim this section explicitly says not to repeat).
- Independently re-derived the min-of-terms reduction (`w1-max_i(A_i)=min_i(w1-A_i)`, elementary) —
  confirmed correct.
- Re-implemented `TwoTouch`/`ThreeTouch` from scratch and tested the target `(*)`
  `w1-ThreeTouch(b0,rest)>=TwoTouch(b0,W)` plus all 5 per-term claims (`w1-A_i>=TT` for `i=1..5`) plus
  the new Two-Variable Reflection Bound (`w1-|b0-w|>=|b0-(w1-w)|`):
  - **20,000 fresh random trials** (`0<=w3<=w2<=w1<=20`, `0<=b0<=w1`): **0 failures on all 7 checks**.
  - **Exhaustive integer grid** `w1,w2,w3,b0 \in \{0,...,8\}` (1155 tuples) and again `\{0,...,12\}`
    (4550 tuples): **0 failures**, pushed past what the file itself reports tested.
  - Symbolically re-derived (`sympy`) the three case-differences inside the Two-Variable Reflection
    Bound's proof and the `A1-A4=w2-w3>=0` step used in sub-claim 3/4: all match the file's claimed
    algebra exactly (`2w`, `2(w1-b0)`, `w2-w3` — all `>=0` under the stated hypotheses).
- **No overclaim found in the scope-limiting language.** The file's Status line and §32.5 item 3 both
  explicitly say the target is a "STRONG CANDIDATE PROOF, not yet independently re-derived by anyone
  besides the reporting explorer" and explicitly forbid writing "Two-Touch fully proved at `|W|<=3`"
  into `current.md` until a reviewer independently confirms §32.1-§32.4 — this is exactly the fix
  round 18's proof-reviewer demanded, correctly applied this time. `current.md` itself is unchanged
  this round (still round-18's narrowed, correctly-hedged text) — confirmed via `git diff`, no
  premature promotion happened.
- Minor, non-blocking note for the builder: §32.3 sub-claim 3/4's intermediate region-split algebra
  (the four inequalities `w1+w2>=2b0`, etc.) was not independently re-derived symbolically term-by-term
  by me — only the *outer* target and the two witnesses I traced. Since the outer target and all 5
  per-term bounds independently verify to 0 failures on both a wide random sweep and two exhaustive
  grids, this is not a blocking concern, but the builder should still write out that intermediate
  algebra explicitly rather than skip it, since "0 failures on the final inequality" doesn't by itself
  certify each internal case-split step is stated correctly.

## 2. New slug `pigeonhole-subset-sum-upper-bound.md`

Verdict: **APPROVE — genuine, complete, structurally distinct rival attempt at the whole upper-bound
direction; the outliner's own honesty about the falsified sub-mechanism is correct and the remaining
gap is real (neither silently closed nor silently unclosable).**

- **Whole-attempt check:** imports Slack Collapse, Lemma D/M, and the unconditional lower bound
  (`all-cycles-resolution.md` + `superincreasing-no-early-zero.md`) purely by citation — does not
  re-derive them, and does not reuse any of `potential-weighting-upper-bound`'s recursive
  DELETE/KEEP/MATCH machinery. Its own novel content (pigeonhole + signed-sum realizability +
  combination) targets the theorem's actual claim end to end, not a fragment. Confirmed genuinely
  different framing (non-recursive, no induction on background/list size at all), satisfying the
  plateau-break mandate (shared machinery has been the single bottleneck for rounds 14-18).
- **Pigeonhole margin (Step 1), re-verified from scratch:** built an independent exhaustive subset-sum
  + min-distinct-subset-gap harness (not reusing the file's code) and pushed the range past what's
  reported (`k` up to 6): tested `k=1..7`, `1395` trials, **0 failures** — the elementary pigeonhole
  argument is correct as stated, no casework issue found.
- **Lemma D/M citation check:** re-read `lemmas/dm-operation-reformulation.md` directly — confirmed it
  places no restriction on which pair `M` acts on, and is explicitly certified only as
  *achievable/sufficient*, not exhaustive — exactly matching this route's use (an upper-bound argument
  only needs a sufficient strategy, not the true optimum; correctly used here per the standing
  distinction memo'd from round 2).
- **Counterexample `X=(36,48,4)` to the explorer's "same-sign-tied" mechanism, independently
  reproduced:** computed all 8 sign patterns from scratch — true minimum is `8` at `eps*=(+,-,+)`
  (`36-48+4=-8`), confirmed `36` and `4` share sign `+1` and are **not** tied (`36\ne4`), confirming the
  claimed contradiction argument breaks exactly as described. Ran a fresh, independently-coded version
  of the "same-sign nonzero elements under an optimal pattern must be tied" claim over `3000` fresh
  random instances: **2092/3000 (~70%) violated** — same order of magnitude as the file's reported
  `2351/3000 (~78%)`, confirming this is a common failure, not a contrived edge case, and the diagnosis
  ("the specific proof mechanism is false, but the Lemma's conclusion still appears true") is honestly
  and correctly stated, not swept under the rug.
- **Existence claim (the surviving, still-open core of Step 2), pushed past the file's own tested
  range:** independent memoized brute-force merge-tree search, `|X|` up to `6` (`600` trials, past the
  file's `|X|<=5`) — **0 failures**; pushed further to `|X|\in\{6,7\}` on a bounded value range (`150`
  trials, memo size `3396` states) — **0 failures**. This is real, fresh, citable corroboration beyond
  what's currently on file, still not a proof — correctly reported as open, not closed.
- **Dead-end distinction check:** re-read the round-4 "no fixed lookahead depth suffices" dead end —
  confirmed it concerns a *single fixed rule* always working, a strictly stronger and different claim
  from this route's "*some* merge order exists" (existence only). The file's own §6 correctly draws
  this line; I agree it is not a rehash of the round-4 dead end.
- **Open gap is real:** Step 2 (Signed-Sum Realizability Lemma) has no valid proof on file anywhere —
  confirmed by reading §2.2/§4/§7 end-to-end; nothing is silently assumed discharged, and the gap is
  not vacuous or trivially closeable by the already-certified machinery (Lemma D/M only supplies
  *achievability* of a given operation sequence, not which sequence realizes the sign-optimal value).

No issues found that block building this slug.

## 3. `dyadic-cascade-induction` and `concavity-minimax-duality`

Confirmed via `git diff HEAD~1 HEAD -- results/imo-2026-03/` that neither file was touched this round
(only `potential-weighting-upper-bound.md`, `.ranking.json`, `current.md`, and the new pigeonhole file
changed). The outliner's claim that neither math-explorer touched the lower-bound direction or the
benched approaches' own machinery is correct — both remain correctly benched with no new leverage,
consistent with the standing rule since round 9-11.

## Diversity note

The field is no longer a single-framing monoculture: `potential-weighting-upper-bound`'s recursive
background-tracking machinery and the new `pigeonhole-subset-sum-upper-bound`'s pigeonhole/signed-sum
route are genuinely different techniques attacking the same upper-bound target, satisfying CLAUDE.md's
diversity requirement after 6 rounds (14-18) of a single shared wall. Both approaches' critical-path
gaps (§31/§32's open items; the Signed-Sum Realizability Lemma) are independent of each other — a
future round finding the Signed-Sum Realizability Lemma false in general would not invalidate
`potential-weighting-upper-bound`'s progress, and vice versa. This is the correct shape per the
"break a shared-gap plateau" orchestrator rule.

## Ranking

Registered `pigeonhole-subset-sum-upper-bound` (cold-start 1500). Ran `update_ranking` anchoring the
new slug against the existing field: lost to `potential-weighting-upper-bound` and
`dyadic-cascade-induction` (both far more mature — 14 and 6 rounds of certified progress respectively,
including a verified milestone for `dyadic-cascade-induction`) but beat `concavity-minimax-duality`
(long-benched, weakest live Elo, Local Claim still open with admittedly no further leverage even if
closed) and `elementary-exchange-smoothing` (retired/dormant). Reaffirmed
`potential-weighting-upper-bound` over `concavity-minimax-duality`. Resulting order:
`dyadic-cascade-induction` (1729, benched) > `potential-weighting-upper-bound` (1596, live) >
`pigeonhole-subset-sum-upper-bound` (1501, live, new) > `elementary-exchange-smoothing` (1398, retired)
> `concavity-minimax-duality` (1276, benched).

## Build set

Both live, gap-bearing approaches: the established leader (with two new, correctly-hedged, well-
corroborated candidate lemmas ready for a builder to formalize/independently re-derive) and the new
plateau-breaking route (with one proved step, one genuinely open but heavily-corroborated existence
lemma, and a correctly-diagnosed dead sub-mechanism to avoid repeating).

build set: potential-weighting-upper-bound, pigeonhole-subset-sum-upper-bound
