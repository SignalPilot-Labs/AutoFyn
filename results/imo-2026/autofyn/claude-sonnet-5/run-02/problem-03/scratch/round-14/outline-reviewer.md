## imo-2026-03 — round 14 outline review

### greedy-halving-adversary — verdict: CHANGES REQUESTED

**Critical finding: Step 1 ("Prerequisite fix, do first, it blocks
everything else this round") is unnecessary — the fix it describes was
already made and certified three rounds ago.** The outline (following the
`math-explorer-p2-dominance` report verbatim) claims
`simplex-exchange-smoothing-vertex-maximization` is still stated with pin
set $\{\tau_1,\dots,\tau_r\}$ (omitting $0$) and "was submitted but not
certified" in round 10, "still unresolved." I read the actual lemma file
(`results/imo-2026-03/lemmas/simplex-exchange-smoothing-vertex-maximization.md`)
and `current.md`'s round-11 entry directly:

- The lemma file's header is literally `## Statement (corrected, round 11)`,
  its pin set is already $\mathcal R=\{0,\tau_1,\dots,\tau_r\}$ (box-free,
  general reference multiset, no ladder assumption), and its certification
  note reads **"CERTIFIED — proof-reviewer, round 11"** with an
  independent multi-start Nelder-Mead re-verification (20 fresh test cases,
  zero mismatches) plus an algebraic cross-check via the (also certified)
  `zero-pin-harmlessness-lemma`.
- `current.md`'s round-11 log confirms this in prose: *"lp-duality-certificate
  completed both round-11 tasks. (a) Pin-set fix: proved the general,
  elementary Zero-Pin Harmlessness Lemma ... and used it to give a
  corrected, fully-reproved Simplex Vertex-Maximization Lemma (pin set now
  $\{0,\tau_1,\dots,\tau_r\}$ ...) — this genuinely closes the round-10 gap
  the reviewer had left uncertified."*

So this round's explorer report is stale/wrong (it describes the pre-round-11
state of the population, not the current state — the same failure mode
memory rule 11 warns about: paraphrasing a cited fix instead of grepping the
actual file). The outline inherited this error and turned it into a whole
mandatory Step 1 for the builder. Left as written, the builder would spend
real effort re-deriving a lemma that is already sitting certified in
`lemmas/`, ready to cite directly.

**Fix for the builder:** strike Step 1 entirely. Cite
`simplex-exchange-smoothing-vertex-maximization` (already certified, round
11, pin set $\{0,\tau_1,\dots,\tau_r\}$, box-free/general reference) and
`zero-pin-harmlessness-lemma` directly in Step 2 — no restatement or
re-certification needed. This actually *accelerates* the round: the
builder can go straight to the main target.

**Main target (Step 2) is sound and honestly scoped.** Independently
re-verified both directions numerically with my own fresh script (not the
explorer's):
- Ladder case: $A(F_2\cup R)\le p_2-A(R)$ for random legal splits $F_2$ of
  $p_2$ ($k=1..6$) against random legal refinements $R$ of the ratio-2 tail,
  $n=3..7$, 15000 trials — **zero violations**, matching the explorer's
  claim.
- Non-ladder counterexample ($\tau=\{49,2/5\}$, $m=203/4$): reproduced the
  explorer's refutation with my own script — found a violation
  ($A(F_2\cup\tau)=7254971/200000 > 43/20 = m-A(\tau)$) within a few hundred
  random trials. Confirms the "load-bearing structural caveat" (Step 3) is
  real and correctly required in the write-up, not an overclaim — the
  outline is honest that the stronger claim needs ladder/ratio-2 structure
  and explicitly forbids a generic-multiset proof attempt.

**Step 4 (small-Total(P) closure)** matches the explorer's finding 4
exactly (uses `dominant-element-removal-identity`, reduces to a strictly
weaker instance of the standard recursive bound) — sound as stated, no
issue.

**Merge-monotonicity dead end correctly excluded.** The outline explicitly
rules out single-step merge-monotonicity as the collapse mechanism for Step
2 (3844/16000 violations, consistent with the pre-existing
`splitting-monotonicity-refuted-dead-end`) — correctly not proposed as the
proof route.

Net: technique is right, main claim is honestly scoped and numerically
solid both ways (positive result + the counterexample bounding its scope);
the only defect is the redundant Step 1, which is a wording/dispatch fix,
not a mathematical flaw — hence CHANGES REQUESTED, not RETHINK.

### lp-duality-certificate — verdict: APPROVE

- **"Do not retry peel-and-recurse for case (b2)" is consistent with the
  explorer's algebraic proof.** The explorer derived, by hand, that
  peel-$p_1$-vs-$p_2$+full-$P(n-1)$ has *exact* threshold $p_2\ge a_nT/2$
  (reduces via `telescoping-threshold-identity` to precisely case (a)'s own
  boundary) and bisect-$p_1$-alone+full IH has exact threshold $p_1\ge
  a_nT$ (strictly inside Theorem A's $p_1\ge T/2$ region) — both zero-slack
  results, not numeric near-misses. The outline correctly elevates both to
  certified negative lemmas and forbids re-attempting any "strengthen the
  peel recursion" variant. This is the right instruction — a genuinely
  different mechanism (existence/pairing) is required, and the outline says
  so.
- **Bisect-Top-$k$ Lemma statement matches the explorer's derivation.**
  $\Phi\le(T+p_{k+1})/2\le a_nT$ whenever $p_{k+1}\le T/D_n$, via
  `pair-cancellation-identity` ($k$ times) + `max-domination-lemma`. I
  independently re-ran a smaller exact-`Fraction` check on the ladder
  itself (7 hit-cases across $n=1..7$) — zero violations, consistent with
  (though far smaller-scale than) the explorer's 5717-trial check. The
  outline honestly states the coverage is partial (5–13% of case-(b2)
  witnesses) — not overclaimed as a closure.
- **Vertex-restricted search plan (Step 3) is a legitimate, cheaper
  reformulation**, not a re-run of the timed-out continuum optimizer — it
  correctly reuses `per-piece-vertex-decomposition-theorem` (already proven
  marking-agnostic) to reduce to a finite family, addressing the exact
  failure mode (continuum DE timeout) the explorer hit.
- **Step 4's framing (existence/pairing claim rather than closed-form
  template) is consistent with finding 5**: the explorer observed the
  optimal cut allocation varies witness-to-witness with no fixed pattern —
  the outline correctly treats this as evidence for an existence-style
  target rather than proposing a specific (likely false) closed-form
  template.
- No case-coverage gaps, no circular steps, no repeat of a recorded dead
  end. This is a legitimate exploratory round (set up the search, get first
  results) rather than a closure — outline is honest that case (b2) stays
  open.

### Diversity note

Both approaches attack complementary halves of the theorem (lower bound
sub-cases vs. general upper bound case (b2)) — genuinely different targets,
not variations of one framing. No shared-gap plateau concern this round.

### Ranking

Both slugs already registered from prior rounds; no new slugs this round.
Cleared `stale` and updated Elo via `update_ranking`:
`rank-pigeonhole-budget` (verified-milestone, closed Claim A) > both
`greedy-halving-adversary` and `lp-duality-certificate` (still `partial`,
roughly equal incremental progress this round — declared a draw between
them, no clear ordering: greedy's headline claim is stronger/cleaner but
carries a wasted-prerequisite defect to fix; lp-duality's negative lemmas
are cleanly closed but the positive target (b2) is untouched).

build set: greedy-halving-adversary, lp-duality-certificate
