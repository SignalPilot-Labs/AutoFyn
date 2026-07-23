## imo-2026-03

dyadic-cascade-induction: revise (scope correction only, no new mathematical content)
Target: the whole theorem — `c(n)=2^n/(2^{n+1}-1)`, both directions, for every `n`. This slug's
own contribution: the lower bound against `D_m` for every `m` (§5.5.6, fully closed since round 8)
plus the shared Lemma G/P/D-M induction scaffolding used by the whole population.
Technique: strong induction on `m` (self-similar top-piece peeling for the lower bound; case split
`a_1\ge2a_2` vs `a_1<2a_2` for the upper bound), joint across Case (i)/(ii).
Skeleton: unchanged from round 8 — see §2/§5/§5.5 in the file. This round only corrects the
top-level narrative:
  1. Confirm (explorer-verified, re-traced) that Case (i)'s inductive step at level `m` invokes
     the FULL joint IH (both cases) at level `m-1` on an arbitrary residual — Case (i) and Case
     (ii) are not independently generalizable; they share one strong induction on `m`.
  2. Confirm the lower bound (§5.3 + §5.5) needs no induction on `n`/`m` at all — it is a direct
     invariant argument, already unconditional for every `m`.
  3. Conclude: "general `n\ge4`" is not a 4th open item distinct from item 2/6 in current.md's
     "what remains open" list — it is exactly `potential-weighting-upper-bound`'s aggregated
     Small-Gap Crossing-Domination Lemma, viewed from a different index name. Once that lemma
     closes, the joint induction on `m` closes for every `n` at once.
Key lemmas (claim + mechanism): none new — this revision imports the already-certified
Superincreasing No-Early-Zero Lemma, All-Cycles Resolution (round 8), and the round-3 finding
about Case (i)/(ii) coupling (re-verified, not re-derived, by this round's explorer).
Open gaps: this slug's own remaining useful work is now purely on the upper bound: (a) once
`potential-weighting-upper-bound` closes the aggregated lemma, assemble the final "for every `m`,
both cases, joint induction ⟹ every `n`" write-up explicitly in this file (currently scattered
across §2d/§5/the round-9 Status note); (b) no independent mechanism for the upper bound is
proposed here — none needed, since the sibling's lemma is provably sufficient and necessary for
this route.
Cases to cover: none new (the case-split structure — Case (i) `a_1\ge2a_2` vs Case (ii)
`a_1<2a_2` — is unchanged; both already coupled, not independently splittable across `n`).
Watch out for: do NOT let a future round re-read `current.md`'s stale "n≥4, both directions,
untouched" phrasing as license to open a 5th slug for "general n" — this round's explorer
(`math-explorer-n-general.md`) traced the induction precisely and confirmed it has zero
independent leverage beyond the sibling's existing gap (single-gap-trap). Also do not revive the
`c(n)=2c(n-1)/(2c(n-1)+1)` recursion as a shortcut — re-confirmed this round (upper-bound side is
literally Case (i)'s own circular mechanism; lower-bound side is strictly subsumed by the
already-certified non-inductive §5.3/§5.5 result).

potential-weighting-upper-bound: revise (new skeleton, §12, for the sole remaining upper-bound gap)
Target: the whole theorem's upper-bound direction — for every Liu Bang opening `A` and every `m`,
Xiang Yu can force `e(\text{final})\le e_m\cdot S(A)` — via the certified reduction (Slack
Collapse) to proving `OPT(Y,p-1)=NC(Y,p-1)` for arbitrary `Y,p`.
Technique: strong induction on `p`, applying the certified Extreme-Element Peeling Lemma
recursively one level deeper (inside `INSERT_OPT`/`INSERT_NC` themselves), generalizing the
lemma's background-value bookkeeping from "0 or 1 fixed external constants" to "a finite set of
fixed external constants," anchored by a new unconditional "full-slack" base case.
Skeleton:
  1. Base case `|Z|\le1` — trivial (no crossing possible).
  2. Base case, full slack (`b'=|Z|` exactly, no genuine inside/outside split) — the new
     Full-Slack Insertion Lemma (§12.1, open, but a scoped, bounded sub-task): plausibly provable
     by adapting the certified Fact 5 (chain-cancellation/full-budget achievability)'s own proof
     technique, not just importing its statement.
  3. Inductive step: peel `Z`'s own extreme element `z_1` via the DELETE/KEEP/MATCH trichotomy,
     carrying the externally-fixed background value(s) as inert constants throughout — DELETE and
     MATCH reduce cleanly (MATCH grows the background set by one, motivating a generalized
     multi-background Peeling Lemma); KEEP needs a new case split on whether `v^\dagger` or `z_1`
     is larger before Fact 3's block-extraction applies (not automatic here, unlike the top level).
  4. Close by strong induction on `|Z|+b'` (strictly decreasing at every step, so termination is
     immediate); specialize to background set `=\{y_1-y_j\}` and take `\min_j` to recover the
     aggregated Small-Gap Crossing-Domination Lemma.
Key lemmas (claim + mechanism):
  - Full-Slack Insertion Lemma — because at budget `=|Z|` no non-crossing selection is ever
    budget-constrained out of matching what an OPT-optimal crossing selection could achieve, so
    the crossing/non-crossing value gap collapses to zero (Fact-5-style "full budget removes every
    obstruction" argument).
  - Generalized (multi-background) Extreme-Element Peeling Lemma — because none of the three
    certified bijection proofs (§11.2) actually used that the background set has size `\le1`;
    re-running the same three arguments with an arbitrary finite inert background set should be a
    free generalization.
Open gaps: the Full-Slack Insertion Lemma; the multi-background Peeling Lemma's extension; the
KEEP-branch `v^\dagger\gtrless z_1` case split. Fallback, untried: crux `aimo-0558`'s
forced-inclusion-charged-to-a-distinct-skipped-element proof shape, flagged as a genuinely
different technique if the recursive route stalls.
Cases to cover: KEEP branch's 2-way order split (`v^\dagger>z_1` vs `v^\dagger<z_1`, handled
symmetrically); confirm the multi-background set's growth still terminates (it does — `|Z|+b'`
strictly decreases every step, background set can grow by at most 1 per MATCH step and the total
number of MATCH steps is bounded by the original finite budget).
Watch out for: do NOT assume `v^\dagger` is always the current maximum when invoking Fact 3 one
level into the recursion — this was automatic at the top level (`y_1` is always `Y`'s max) but is
NOT automatic here. Do NOT re-attempt the now-refuted "re-route `y_1`'s partner to an endpoint of
the offending crossing arc" as a one-step surgery (fails ~14% of trials, concrete counterexample
`Y=(463,461,372,291,237,180)`) — any future use of that idea must be recursive/global, not a
one-shot swap.

concavity-minimax-duality: revise (new skeleton, §14, for the "e_{g*} minimum is 1" gap)
Target: the whole theorem's lower bound, via an independent 1-Lipschitz-certificate route (an
alternative to `dyadic-cascade-induction`'s D/M-completeness route) — specifically, prove the
candidate certificate `g^*` satisfies `e_{g^*}(M)\ge1` for every state `M` reachable from `D_m`,
every `m`.
Technique: reduce the target to one precise structural (set-membership) invariant — the
Distinct-Bucket Lemma — via an elementary, already-verified implication, then prove that
invariant by extending the certified Superincreasing No-Early-Zero Lemma's token-tracking
induction.
Skeleton:
  1. Closed form `g^*(t)=\text{bit\_length}(t-1)+1` (§14.1, elementary, verified `t=0..39`) —
     makes `g^*`'s level sets exactly the dyadic doubling brackets.
  2. State the Distinct-Bucket Lemma precisely (§14.2): no two elements of any `D_m`-reachable
     state ever share a `g^*`-bucket. Open — 0 violations on exhaustive BFS `m\le7` + 80,000
     random walks to `m=15`, not proved.
  3. Prove (already done, elementary, §14.3): Distinct-Bucket + the certified
     Integer-Preservation Lemma ⟹ sorted reachable-state bucket indices are strictly decreasing
     positive integers ⟹ pairing consecutive terms gives `e_{g^*}(M)\ge\lceil|M|/2\rceil\ge1`.
     This step needs no further work — it is a complete 5-line argument, independently checked.
  4. Prove the Distinct-Bucket Lemma itself (§14.4, the sole remaining open step): extend the
     certified token/signed-sum invariant (Superincreasing No-Early-Zero Lemma) from "never
     exactly 0" to "no dyadic level `j` is ever occupied by two simultaneously-active tokens' own
     highest-surviving power" — by induction on operation count, using the same dominance
     mechanism (an `M` operation on two tokens can only leave the higher of their two
     highest-surviving levels occupied).
Key lemmas (claim + mechanism):
  - Distinct-Bucket Lemma — because every active value is a signed combination of a
    pairwise-disjoint-support subset of the original powers of 2 (already-certified token
    invariant), and the classical superincreasing/knapsack fact pins such a combination's
    magnitude to the doubling bracket of its highest-surviving power, so two simultaneously-active
    tokens sharing a bracket would require two tokens with the same highest-surviving level —
    ruled out by extending the existing dominance argument.
  - (already proved, restated as a lemma) Distinct-Bucket ⟹ `e_{g^*}\ge\lceil|M|/2\rceil` —
    because strictly decreasing positive integers, paired consecutively, each contribute `\ge1` to
    the alternating sum.
Open gaps: the Distinct-Bucket Lemma (§14.4) — the single remaining task, everything downstream
of it is already closed.
Cases to cover: the induction (§14.4) must handle both `D` (delete) and `M` (bisect/replace)
operations, and both "new value created has a fresh highest-surviving level" and "operation
leaves the highest-surviving level of an existing token unchanged" sub-cases — mirror the
already-certified No-Early-Zero Lemma's own case structure (it already handles `D`/`M` uniformly).
Watch out for: do NOT reuse the naive Kraft-sum potential `\Phi(M)=\sum 2^{-(g^*(v)-1)}` as a
direct edge-wise monovariant — tested this round, FALSE (1.5-3% of BFS edges increase it,
concrete failure rates given at `m=2..5`). Do NOT re-attempt single-operation/edge-wise
monovariance of `e_{g^*}` itself — already a confirmed dead end (round 8, exact counterexample
`(32,8,4)\to(8,4)`, drop of 4) — the Distinct-Bucket route is a state-level structural invariant,
not a scalar potential, and is not affected by that dead end.

elementary-exchange-smoothing: retired, unchanged. No further action this round — its content is
fully absorbed into `lemmas/vertex-lemma.md`; no genuinely new, non-redundant target has been
found for it since round 4.

(No 5th slug opened. This round's plateau-break explorer traced the induction structure precisely
and confirmed "general n≥4" would just relabel `potential-weighting-upper-bound`'s existing gap —
a textbook single-gap-trap. Per dispatch, declined.)
