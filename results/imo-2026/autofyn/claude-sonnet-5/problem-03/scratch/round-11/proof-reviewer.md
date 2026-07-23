# proof-reviewer report — round 11, `potential-weighting-upper-bound`

## Scope

Adversarially re-verified this round's single build, targeting the Refined Delete-Recovery
Conjecture (§15.4) via its round-11 sharpening, Sharp Argmin Recovery (SAR, §16.1), the new Forced
Swap Inequality lemma (§16.2), and three negative results (§16.3). All computation done with
fresh, independently-written code (`mydefs.py` and 6 driver scripts, `/tmp/round-11-review/work/`),
sanity-checked against the file's own stated `|B|=2` counterexample value (`OPT=0,TAGGED=1` for
`B={2,4},Z=(6,3,2,1)`) before trusting it for anything new — matched exactly.

## 1. Forced Swap Inequality (§16.2) — CONFIRMED, genuinely new, general, sound

Re-derived the proof symbolically from the prose alone: the four-point crossing `1<i<k^*<j` has
exactly two non-crossing repairs (disjoint `(1,i)&(k^*,j)`, nested `(1,j)&(i,k^*)`); each repair
is shown to be a *valid* (not necessarily optimal) witness for the corresponding branch `A_{3,i}`
or `A_{3,j}`, and since `k^*` is a *global* argmin, `M\le A_{3,i}` (resp. `A_{3,j}`) `\le` the
repair's value. No gap found; needs no restriction on `|B|`; does not depend on any conjectural
material (only the raw `OPT` definitions).

Independently coded from scratch and run: **1289/1289 fresh crossing-pair checks, 0 violations**
(`q=3..7`, background size `0`–`4`, random exact integers), corroborating the builder's own
3336/3336 (after their self-caught, honestly-documented harness bug). **Certified** to
`lemmas/forced-swap-inequality.md`.

## 2. Sharp Argmin Recovery (§16.1) — NOT falsified by a fresh, independently-designed adversarial
battery; still an open conjecture

Rather than reusing the builder's embedding attack, I ran three genuinely different attacks:
- **Exhaustive (not sampled) sweeps** at `q=4` (`vmax=6`), `q=5` (`vmax=5`), `q=6` (`vmax=4`):
  657 total triggered instances, 0 violations.
- **A tie-focused adversarial search** targeting SAR's own "ANY tied argmin" universal quantifier
  (SAR requires recovery at *every* index achieving the min, not just some one) — random
  small-value-range, structured arithmetic-progression, heavy-duplicate, and
  dyadic/perturbed-dyadic families: 230 genuine tie-events (>1 simultaneous argmin), 944
  per-argmin checks, 0 violations.
- **A from-scratch hill-climbing/simulated-annealing search** explicitly designed to *minimize*
  the recovery slack `B_{3,k^*}-A_{3,k^*}` toward a violation (score<0), across two independent
  runs: 8508 total triggered evaluations, minimal slack found across all runs `=0`, never
  negative.

SAR survives all three. This does not prove it, but it is a materially different (and, on the tie
front, arguably sharper) stress test than either the builder's or the round-11 outline-reviewer's
own embedding attack, and it found nothing.

## 3. The three negative results (§16.3)

- **16.3.2 (`|B|=3` counterexample to unrestricted SAR):** re-derived bit-for-bit —
  `B=(0,6,4),Z=(10,8,5,4,3,1)`: `A_1=1`, `A_{3,k}$ values `\{1,1,0,1,2\}` (matching exactly, in the
  same order), `M=0` at `z_{k^*}=4`, `A_{3,k^*}=0\ne B_{3,k^*}=1` (confirmed with the file's own
  split convention, `split=2` on the residual `(8,5,3,1)`). **Confirmed exactly.**
- **16.3.3 (GML/"one-step compatible winner" counterexample):** re-derived exactly —
  `C=[6],W=(8,7,7,4,1),s=3`: `OPT(C,W)=0`, DELETE branch `OPT(C,W\{8\})=0` (a "compatible" winner
  by GML's own criterion), yet `TAGGED(C,W,3)=1\ne0`. **Confirmed exactly.**
- **16.3.1 (averaging doesn't recover the optimum):** the *substance* is confirmed via a
  properly-rescoped fresh test (restricted to the actual SAR argmin branch and `|B|\le1`, matching
  the conjecture's own scope, since an unscoped sweep over all branches produces many degenerate
  ties that are not a fair test): **0 non-trivial successes out of 5776 argmin-branch crossing
  instances.** However, **the file's one specific worked example does not reproduce**: independent
  recomputation of `B=[1],Z=(9,8,8,8,5,3,0)` gives the two argmin-branch alternatives as `\{0,2\}`
  (`M=0`), not the claimed `\{1,1\}` — the qualitative conclusion (average `=1>M=0`) is unaffected,
  but the specific numbers were a transcription slip, not a verified computation. **Fixed
  in-file** (§16.3.1) and noted in the certified lemma's verification section, since it does not
  change the soundness of anything certified or the Status.

## 4. Is the "not solved" self-assessment correct?

Yes — checked for both directions of error:
- **Not undersold:** no proof of SAR/RDRC was found by any of my independent attempts either; the
  Forced Swap Inequality does not, by itself or via the tested repair mechanisms (averaging), close
  the gap. No hidden closure was missed.
- **Not oversold:** the Forced Swap Inequality's proof is genuinely correct and general (verified
  above); the three negative results are (modulo the one now-fixed transcription slip) genuinely
  correct; SAR's survival under three fresh, differently-designed adversarial batteries is real,
  reported, non-fabricated corroboration, not a "clean sweep" claim dressed up as more than it is —
  the file and the builder's own report both explicitly and repeatedly flag SAR/RDRC as unproved.

No error was found that would change Status in either direction. This is genuine incremental
progress (one new certified lemma, a sharper reformulation, three negative results narrowing the
technique space) on a still-open conjecture — squarely `partial` under CLAUDE.md's definitions.

## 5. Verdict

- **Forced Swap Inequality:** certified, `lemmas/forced-swap-inequality.md`.
- **`current.md`:** updated (Approaches tried entry, Current best certified-lemma list, item 2 of
  "what remains open", closing summary paragraph). Status remains `partial`.
- **Approach file:** one-line correction applied to §16.3.1's worked example (transcription slip,
  not a soundness issue).
- **Ranker:** `record_outcome` called, `outcome=partial`.

This is real, correctly-scoped progress, not a closure, and not a regression. The mechanism (SAR /
Forced Swap Inequality / recursive-compatible-family diagnosis) remains viable for a future round;
nothing here suggests RETHINK is warranted.

verdict: potential-weighting-upper-bound = CHANGES_REQUESTED
