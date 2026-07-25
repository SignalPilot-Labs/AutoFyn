# Round 13 report — self-similar-induction-on-n

## Target
Extend GT($m$) (General Peeling Theorem, certified for $m=0,1,2,3$) to
general $m\ge4$, closing gap (a) of the shared Branch-I.A window at every
$\ell$ (currently closed only for $\ell=1,2,3,4$). Dispatched priority:
Route B (exchange-smoothing) primary, Route C (sibling LP-vertex import)
secondary, Route A/D (depth-parametrized induction) fallback.

## What was done
Pursued Route D (the depth-parametrized strengthened induction), since it
surfaced two fully-proved, reusable results before the round's budget ran
out. Routes B and C were **not attempted** this round.

**Result 1 — Monotonicity Reduction Lemma (proved in full, verified).**
A direct corollary of the already-certified Elementwise Monotonicity
Lemma: shrinking $D$'s coordinates (same count, same or smaller cap) down
to any target sum can only decrease $\mathrm{OddSum}(D\cup T)$. Corollary:
any future bounded-sum ($\mathrm{sum}(D)\le2^m$) proof of $\mathrm{GT}(m)$
automatically yields the *fully unrestricted-sum* statement for free —
this **completely and unconditionally closes the reviewer's flagged
large-sum / $p\ge3$ scope gap**, for every $m$ (not just $m\le3$).
Verified: `/tmp/verify_mono.py`, 5876 exact-`Fraction` trials, zero
violations.

**Result 2 — Unified Threshold-Pair-Peeling Lemma (proved in full,
verified, one bug found and fixed by self-review).** A clean rank-shift
identity replaces the ad hoc P1/P2/R1/R2 case list with one mechanism
valid for *any* count $q$ of elements exceeding the current threshold —
and, going beyond round 12's lemmas, shows that **every** $q\ge2$ (not
just $q=2$) closes the target unconditionally, independent of the excess
$e$ or of the remainder's structure. This collapses every level's case
split to three outcomes: $q=0$ (no progress, excess $+1$), $q=1$
(recurses into $\mathrm{GT}(k-1)$), $q\ge2$ (closes immediately). An
initial draft of this result mistakenly tried to force $q\ge2$ (even
case) through a second, unjustified Companion-Peeling step assuming
$R\le2^{k-2}$ — caught by re-derivation and a targeted numeric check
(`/tmp/verify_q_trivial.py`, 1129 trials) before being written into the
file; the corrected argument (trivial closure via $\sigma_q>2^{k-1}$ plus
$\mathrm{OddSum}/\mathrm{EvenSum}\ge0$, no recursion at all) is *stronger*
than the original draft, not just fixed.

A precise excess-accounting analysis (also new) shows the recursion on
$k$ is well-founded (terminates in $\le m$ steps, base case at $k=0$
proved infeasible for **every** excess level $e$ uniformly, replacing
round 12's per-$m$ hand-verified Feasibility Lemma) — but identifies two
remaining honest gaps: (i) the $q=1$ sub-case when excess $e\ge1$ lands in
a target that is neither trivial nor a plain smaller $\mathrm{GT}$
instance nor the clean boundary-excess family, and (ii) the "small-sum"
mirror of the whole argument (needed even at $e=0$, matching original
Lemma P1's own sum-dependent target) was not carried out this round.

## Outcome
**Status: partial** (unchanged). GT($m$) for $m\ge4$ — and hence gap (a)
of the shared window for $\ell\ge5$ — remains **open**. This round did
**not** close it, but: (a) fully and unconditionally resolved the
large-sum scope restriction the reviewer flagged on the certified
$m\le3$ lemma, (b) substantially simplified and generalized the
case-split machinery (three cases instead of five, $q\ge2$ unconditional
for any $q$), and (c) precisely isolated the two sub-cases that a future
round needs to close ($q=1$ under excess; the small-sum mirror
computation) rather than leaving the obstruction only vaguely
characterized as "$O(\log m)$ depth" as round 12 did. Both new lemmas
(Monotonicity Reduction, Unified Threshold-Pair-Peeling) are reusable
independent of whether the remaining gaps close, and are written into
`results/imo-2026-03/approaches/self-similar-induction-on-n.md` under
"Round 13" with numeric verification scripts referenced. Routes B and C
remain untried and are the natural next things to attempt if the
Route-D gaps above prove stubborn.

## Files touched
- `results/imo-2026-03/approaches/self-similar-induction-on-n.md` —
  appended "Round 13" section (Results 1–2, excess accounting, honest
  open-gaps statement, promotable-lemmas entries). No change to
  `## Status` (stays `partial`).
- No changes to `current.md` or `lemmas/` (reviewer-owned; nothing this
  round reached certification-ready completeness for a new lemma file —
  recommend the reviewer certify Result 1 and Result 2 into
  `lemmas/` if it re-verifies them, since both are self-contained and
  reusable regardless of the open gaps).
