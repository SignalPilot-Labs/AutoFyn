## Build report — greedy-exchange-cost-potential, round 13

**Task (dispatched):** formalize and certify the "No-Restart Lemma" as a standing
defensive/bookkeeping lemma — NOT a new FAH attempt. Prove in general (not just the
a_1=15 example) that restarting the greedy process at a later index a_{n_0} as a
fresh seed produces a sequence that structurally diverges from the true
continuation, because dropping the constraints from earlier terms a_1,...,a_{n_0-1}
can only ADMIT more candidates as legal, never fewer.

**What was done.**

1. Set up precisely: the true sequence `(a_n)` vs. the restarted sequence `(b_k)`
   seeded at `b_1 := a_{n_0}` for fixed `n_0 ≥ 2`.
2. Proved the unconditional monotonicity inequality `b_2 ≤ a_{n_0+1}` for every
   `n_0 ≥ 2`, with no hypothesis: legality against the true process's full
   constraint set `{1,...,n_0}` implies legality against the restarted process's
   singleton constraint set `{n_0}` (a conjunction can only get weaker as conjuncts
   are dropped), so the restarted candidate set is a superset, hence its minimum is
   ≤ the true minimum.
3. Identified and proved the precise generic sufficient condition (H') for strict
   divergence `b_2 < a_{n_0+1}`: existence of `j < n_0` and `c` in the open interval
   `(a_{n_0}, a_{n_0+1})` legal against `b_1 = a_{n_0}` alone but illegal against the
   forgotten earlier term `a_j`. Explained why this is the generic case (any
   `a_j > 1` has infinitely many coprime integers, generically landing in any given
   window), not a contrived edge case.
4. Correctly isolated the sole degenerate case `n_0 = 1` (empty forgotten history,
   the two recursions coincide by construction) and excluded it from the Lemma's
   hypotheses.
5. Independently re-verified the worked example `a_1 = 15` by a fresh Python
   simulation this round (matches the dispatch's stated numbers exactly): true
   sequence `15,18,20,24,30,36,40,42,45,48,50,54`; restarting at `a_5=30` gives
   `30,32,34,36,38,40,42,44`, diverging at the very next term (`32` vs true `a_6=36`),
   with explicit witness `j=1, c=32` (`gcd(32,30)=2>1` but `gcd(32,15)=1`).
6. Proved a Corollary making the intended defensive use precise: any restart-based
   induction (on `ω(a_1)`, or a minimal-counterexample descent swapping the true tail
   for a fresh-seed continuation) is invalid unless it explicitly carries the full
   original constraint set forward — at which point it is no longer a genuine
   dimension reduction. This retroactively explains why rounds 3, 5, and 8's
   restart-style arguments (most notably round 8's falsified Seed-Coupling Lemma)
   independently failed.
7. Explicitly scoped what the Lemma does NOT claim (does not assert divergence for
   every `n_0`, only under (H'); makes no claim about FAH/Symmetric FAH/gap (†)).

**Output files:**
- `/home/agentuser/repo/results/imo-2026-06/lemmas/no-restart-lemma.md` — the
  certified standing lemma, unconditional, no gaps (self-contained proof).
- `/home/agentuser/repo/results/imo-2026-06/approaches/greedy-exchange-cost-potential.md`
  — updated `## Status` header with a new round-13 paragraph, and appended a full
  "ROUND 13" section with the complete write-up.

**Verification performed.** Independent fresh Python simulation of both the true
and restarted greedy recursions for `a_1 = 15`, matching the dispatch's stated
numbers exactly (`true` sequence and `restarted-from-a5` sequence both reproduced
digit-for-digit).

**Status:** `partial` (unchanged for the approach overall — this round's task was
explicitly scoped as not touching the main crux, FAH/Symmetric FAH, which remains
open on its eighth consecutive round with no genuinely new mechanism this round).
The No-Restart Lemma itself is fully proved and certified with no gaps.

**Promotable lemmas this round:**
- **No-Restart Lemma** (`lemmas/no-restart-lemma.md`) — proved in full, already
  certified directly in this build (per dispatch instruction to certify it as a
  standing lemma). Reusable by any future approach as a citable reason to reject
  restart-based induction attempts on this problem's greedy recursion.
