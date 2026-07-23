# proof-builder report — explicit-window-backbone-construction (round 9)

## Status: partial (unchanged in kind; substantially strengthened evidence base)

## What I did

Per dispatch, addressed the outline-reviewer's two required items:

1. **Step 3 (Small-Uniform-Hit) corrected to an honest open empirical
   claim.** Verified directly that the Domination Lemma (`lemmas/
   domination-lemma.md`) bounds *frequency* of a term's dominant prime
   factor's recurrence, not its *magnitude* — it gives no reason the
   dominant prime lies in any fixed small set. Step 3 is not free; the built
   file now says so plainly, with expanded empirical support (zero terms
   with radical disjoint from `H` across all 11 tested `a_1` values, up to
   `N=3,000,000` on the hardest case).

2. **Bridge-prime-patch finiteness investigated directly**, the round's
   assigned crux. Fresh Python (`/tmp/round-9/work/gen.py` and friends — a
   gcd-only, factoring-free sequence generator using the certified Lemma W3
   minimal-radical antichain for speed, cross-validated against the direct
   definition before trusting large runs):
   - Reproduced the outline-reviewer's `a_1=21528751` counterexample exactly
     (`n=596` vs `n=863`, disjoint `H`-signatures, bridge prime `97` via
     `gcd`), then extended verification of the patched candidate **10×**
     past the reviewer's tested range: zero further violations from
     `n=300,000` to `n=3,000,000` (303 distinct signatures checked at the
     end).
   - Generated and tested **10 new `a_1` values** with `21528751`-style
     widely-spread 2/3/4-prime cores (primes from 17 to over 1000), each to
     `N` between `300,000` and `500,000`. Found: **9 of 10 need zero patch**
     (the literal small-6 candidate already works); **1 new hard instance**
     found, `a_1=9,674,419=79·151·811`, needing exactly one bridge prime,
     `23` (found at `n=12` vs `n=15`). No instance across all 11 tested
     needed more than one bridge prime, and both nonzero patches found are
     themselves small primes (`23`, `97`), not primes scaling with `a_1`.
   - Tested a **single fixed universal candidate**,
     `H_100 := P_1 ∪ {primes ≤ 100}` (25 small primes, no per-`a_1` tuning),
     against all 11 `a_1` values at the same `N` as above: **zero
     violations in every case**, including both hard instances
     (`21,528,751` to `N=3,000,000`; `9,674,419`, which defeated the
     un-enlarged candidate). This is a genuinely new, more general and more
     falsifiable candidate than the round-9 outline's original guess.

3. **Did not close FCBC for any fixed `H`.** I looked for (and did not
   find or complete) a proof mechanism: combining the certified Domination
   Lemma with the certified Lemma 1 (uniform gap bound) only yields a bound
   on how *often* a term's dominant prime recurs (`Ω(n/log n)` prior terms),
   never a bound on the prime's *magnitude* — the same count-vs-size
   obstruction that defeated the whole `(UB_S)` family in rounds 4–8, now
   located inside Step 4 instead of resolved. I record this honestly as the
   precise remaining gap rather than papering over it. By the already-
   certified Pool Lemma (this file's own Lemma W4, round 4), "some finite
   `Π` works" is logically *equivalent* to FCBC, not an easier target — so
   even the striking 11/11 empirical success of `H_100` is evidence, not
   a proof, and I say so explicitly in the file.

## Where the work lives

- `results/imo-2026-06/approaches/explicit-window-backbone-construction.md`
  — new "Round 9 build" section (top of file, after Status), updated
  "Approaches tried" entry, updated "Current best" pointer. All prior
  rounds' certified content (Lemmas W1–W4, still fully rigorous and
  unconditional) is preserved unchanged.
- `/tmp/round-9/work/` — all Python scripts and raw output logs
  (`gen.py`, `analyze.py`, `batch_test.py`, `batch_test2.py`,
  `batch_test3.py`, `final_check.py`, `out2.log`, `out3.log`,
  `final_out.log`, `seq_21528751.pkl`) — fully reproducible.

## Verdict (self-assessed)

Status stays `partial`. No new certified lemma this round (the work is
computational/diagnostic, correctly not promoted). The concrete, sharpened
open gap for future rounds: prove (or refute) that `H_100 := P_1 ∪
{primes ≤ 100}` (or some fixed-shape enlargement of it) is a covering set
for *every* `a_1`, equivalently close the "count vs. magnitude" gap in the
Domination Lemma's application — i.e. show the greedy rule's dominant prime
at each step is not just frequent but also bounded in size. No such bound
was found or attempted at proof-strength this round; this is the
recommended concrete target for whichever approach attacks this gap next.
