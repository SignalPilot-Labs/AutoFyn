## Build report: greedy-halving-adversary, round 32

### Task
Close $h(m)$'s vertex $c=t\in S''$ Case (ii) ("$q_2$ untouched in $S''$,
$t\ne q_2$") via Fact 2 ($A(S)\le\mathrm{Total}(S)$) + refinement-invariant
mass conservation + the ratio-2 ladder telescoping identity, extract Fact 2
as a standalone certified-candidate lemma, and check whether this closes
$h(3)$'s entire simultaneous-cuts piece.

### What was done
1. **Extracted `fact-2-alternating-sum-leq-total`** as a standalone lemma
   file (`results/imo-2026-03/lemmas/fact-2-alternating-sum-leq-total.md`,
   PROPOSED, awaiting reviewer certification): $A(S)\le\mathrm{Total}(S)$
   for any finite multiset of nonnegative reals, proved by pairing
   consecutive sorted elements (each pair's difference is $\le$ its sum
   since the smaller of the pair is $\ge0$). Noted this is already an
   implicit consequence of the certified `integral-alternating-sum-formula`
   lemma's stated corollary — the content isn't new, only the by-name
   citability.
2. **Proved Case (ii) closure unconditionally for every $m\ge3$**: combined
   Fact 2, an elementary mass-conservation-under-refinement fact (splitting
   preserves total sum), a self-contained re-derivation of the shifted-index
   ladder telescoping identity $\mathrm{Total}(\{q_3,\dots,q_{m+1}\})=
   q_2-f(m)$ (geometric sum, one index down from the identity used
   throughout Theorems 38/42), and `sharp-dominant-removal-identity`
   (certified, round 4) to peel $q_2$ off. Result:
   $A(\{q_2\}\cup(S''\setminus\{t,q_2\}))\ge f(m)+t>f(m)$, strict slack
   exactly $t$, for every legal $S''$ and every $t\ne q_2$ — no vertex
   enumeration, no dependence on $\mathrm{MaxCeil}(m\ge5)$.
3. **Checked $h(3)$'s status directly** (per the outline's request, not
   just pattern-assumed): at $m=3$, $S''$'s budget is exactly $1$ cut over
   the $3$-rung tail $\{q_2,q_3,q_4\}=\{4/15,2/15,1/15\}$, giving an
   exhaustive, disjoint 4-type enumeration (Type 0 = no cut, Type A =
   $q_2$ split, Type B = $q_3$ split, Type C = $q_4$ split). Types 0, B, C
   are covered "for free" by the two general (any-$m$) theorems (the
   "$t=q_2$ untouched" sub-case from Round 31, and this round's Case (ii)),
   since $q_2$ remains untouched in all three types. **Type A** (the
   genuinely new "$q_2$ itself split" sub-case, previously only partially
   handled for the worst-case split point) was closed by a **direct
   $m=3$-specific hand computation** for every split point $u\in(0,q_2/2]$
   and every choice of $t\in S''$, using `pair-cancellation-identity`
   (certified, unconditional) to cancel the inserted pair $\{q_2,q_2\}$ and
   then elementary sorting/casework on 4 explicit values. Found: closes for
   every $u$ and every $t$, tight only at the single boundary point
   $u=q_2/2$ (where the two fragments of $q_2$ tie with $q_3$).
   **Conclusion: $h(3)$'s vertex $c=t\in S''$ is fully closed, and since the
   other four vertex types of $h(3)$'s "simultaneous" piece were already
   closed (Rounds 29–31), and the "$q_1$-untouched" and
   "single-cut-tail-untouched" pieces were already closed (Rounds 28–30),
   $h(3)$ is now fully, unconditionally closed** — modulo only the same
   pre-existing $(\star_3)$ standing dependency used throughout the rest of
   the file (not a new gap). Honestly scoped that this does **not**
   generalize to $m\ge4$: at $m\ge4$, $S''$'s budget of $\ge2$ cuts admits
   shapes (e.g. $q_2$ split with nontrivial remaining budget on the rest of
   the tail) genuinely absent from $m=3$'s enumeration, and no progress on
   those was made or claimed this round.
4. **Numerically cross-checked** both new results (Case (ii)'s general
   theorem across $m=3..7$, 500+ trials each; the $m=3$ Type A computation,
   2000 trials) via a fresh exact-`Fraction` script — zero violations in
   all cases, consistent with the hand-derived formulas.

### Corrections made to stale text
Updated the "Summary of Round 31" and "Open gaps" sections to flag that the
round-31-era "$h(m)$ is not closed for any $m\ge3$" statement is now
superseded for $m=3$ specifically (added a "Round 32 status (read first)"
block at the top of "Open gaps"). Corrected an imprecise claim in a first
draft of the new $h(3)$-closure paragraph ("$h(3)$'s only two pieces are
these two") to the accurate three-piece decomposition ($q_1$-untouched via
Theorem 42, single-cut-tail-untouched via Rounds 29–30, simultaneous via
Rounds 31–32) before finalizing.

### Status
Set to `partial` (unchanged) — the whole problem (general $n$) is not
solved; $h(m)$ for $m\ge4$ remains open (Case (i)'s general split-rung
sub-case, and $c=x$ for $m\ge5$, shared with `rank-pigeonhole-budget`'s
$\mathrm{MaxCeil}(m\ge5)$). But a genuine, concrete, unconditional
sub-result was completed this round: $h(3)$ is now fully closed, and the
new Case (ii) theorem is a general (any-$m$) reusable building block.

### Promotable lemmas
- **Fact 2** (`fact-2-alternating-sum-leq-total`, new standalone file this
  round): $A(S)\le\mathrm{Total}(S)$ for any finite multiset of nonnegative
  reals — proved in full (pairing argument), independent of the ladder
  structure, general-purpose. Already informally used in
  `rank-pigeonhole-budget.md` §5.2; now citable by name from any file.
- **Case (ii) closure theorem** (in `greedy-halving-adversary.md`, "Round
  32: Case (ii) closed"): for every $m\ge3$, every legal $S''$ leaving
  $q_2$ untouched, and every $t\in S''\setminus\{q_2\}$,
  $A(\{q_2\}\cup(S''\setminus\{t,q_2\}))\ge f(m)+t>f(m)$ — fully general in
  $m$, proof is 4 short elementary steps, no case restriction. Worth
  certifying as its own lemma file if the reviewer wants it citable by the
  sibling `rank-pigeonhole-budget` approach too (it is a genuinely new,
  general "punctured tail" bound not previously on file anywhere).

Files touched:
- `/home/agentuser/repo/results/imo-2026-03/approaches/greedy-halving-adversary.md`
  (new "Approaches tried" bullet; new "Round 32: Case (ii) closed" section;
  new "Checking $h(3)$" section; corrected/updated Summary and Open-gaps
  bookkeeping).
- `/home/agentuser/repo/results/imo-2026-03/lemmas/fact-2-alternating-sum-leq-total.md`
  (new, PROPOSED).
