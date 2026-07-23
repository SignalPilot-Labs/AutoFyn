# Outline review — round 5 — imo-2026-03

All three new skeletons were independently re-derived/re-verified this round (not just
re-read): I re-implemented the D/M operation BFS/search machinery from scratch in Python
(exact `Fraction`/`int` arithmetic throughout, no floats) and re-ran every headline numeric
claim myself, extending several beyond the outline's own tested range. Details and code
inline below (all runs from `/tmp` this session).

## 1. `dyadic-cascade-induction` — new §5.3 (integer/superincreasing "no-early-zero" reframe)

**Verdict: CHANGES REQUESTED** (sound skeleton, one precisely-identified open lemma, real
independent verification support — this is legitimate new progress, not an overclaim).

Independent checks performed:
- **Integer Invariant (Step 1)** and **`e=0` characterization (Step 2)**: re-derived by hand
  from the definitions — both are correct and genuinely trivial (Step 1: `D`/`M` map integers
  to integers by construction; Step 2: `e(M)` is a sum of nonnegative gap terms by Fact 1's own
  proof, zero iff every term is zero, i.e. iff sorted `M` is literally a stack of exact
  duplicate pairs — I checked this requires equality specifically at *consecutive sorted rank*
  pairs `(1,2),(3,4),...`, which is exactly Lemma P's duplicate-pair shape, not a weaker
  condition). Both hold.
- **`min ops to e=0 = m+1` for `D_m`** — re-implemented the D/M-operation BFS from scratch
  (independent code, not the outliner's script) and reproduced `m+1` exactly for `m=1..5`
  (matching the outline), and *extended it further to `m=6,7`* (min ops `=7,8` respectively,
  both `=m+1`, zero exceptions) — this is new evidence beyond what the outline itself ran,
  strengthening the claim.
- **min `e` at exactly `m` ops `=1`** — re-verified independently for `m=1..5`, matches exactly.
- **Superincreasing stress test** — re-ran independently with 15 fresh random strictly
  superincreasing sequences (sizes 3–7, including boundary-tight ones where `a_i =
  sum(rest)+small`): **15/15 needed exactly `k` ops**, matching the outline's 13/13. However, I
  found a **nuance the outline's phrasing overstates**: testing 15 fresh random
  *non*-superincreasing sequences, only **6/15 (40%) admitted a shortcut** — the other 9/15
  still needed the full `k` ops despite not being (strictly) superincreasing. The outline's own
  5/5 sample happened to be 100% shortcut, which reads as "non-superincreasing ⟹ shortcut,"
  but that converse is **not true in general** — superincreasing-ness is a *sufficient*
  condition for "no early zero" (which is genuinely all Step 3's Main Claim needs), not a tight
  characterization. I also confirmed the **boundary case is genuinely critical**: taking
  `a_i = sum(rest)` *exactly* (non-strict superincreasing, the tightest possible violation)
  produces `(2^{k-1},...,2,1,1)` with a duplicate `1,1` pair, and this admits a **big** shortcut
  (`k=6`: 4 ops instead of 6) — confirming the *strict* inequality in the Lemma's hypothesis is
  load-bearing, not decorative. **Action for the builder:** state Step 3's lemma only as
  "strictly superincreasing ⟹ no shortcut" (sufficiency), not as "superincreasing-ness is
  *exactly* what's needed" (which reads as a two-sided characterization the data doesn't
  support) — this is a wording fix, not a mathematical error, and doesn't affect the logical
  chain to the Main Claim.
- **D/M-completeness citation**: correctly conditional ("provided the global minimizer's
  tie-dependency graph is not a nonempty union of directed cycles... never observed, not proved
  impossible") — matches `lemmas/dm-completeness-partial.md` verbatim, no overclaim. Good catch
  by this round's outliner in not repeating the round-4 trap.
- **Not a repeat of the "residual stays below ceiling" dead end**: Fact 5 (certified) shows the
  ceiling `max(M)` is always exactly reachable using `K-1` cuts on a `K`-element multiset — that
  dead end was about `e(residual)` staying below its own ceiling. Step 3's proposed invariant is
  a different claim (about individual *values* never tying an *untouched original*, i.e.
  preventing exact coincidental equality, not about `e` staying below a numeric threshold) — I
  checked these are not the same statement; no re-tread found.
- **Step 3 (the Main Claim) itself remains genuinely unproved** — correctly labeled as such,
  with two concrete flagged sub-points (interleaved `D`/`M` handling, non-contiguous index
  subsets) for the builder. This is the one real gap.

No fatal flaw. This is a well-scoped, well-verified new mechanism with real payoff if closed
(subsumes Branch A/B/Step 4 at once). Builder should attempt Step 3's induction directly, fix
the "exactly load-bearing" → "sufficient" wording, and keep §5–§5.2'' as the correct fallback
(already fully proved for its scope) regardless of §5.3's outcome.

## 2. `potential-weighting-upper-bound` — new §6 (chain-prefix + exact static allocation)

**Verdict: CHANGES REQUESTED** (genuinely new mechanism, independently confirmed distinct from
the dead bounded-lookahead family, strong numeric support, one clear next task).

Independent checks performed:
- **Re-implemented the whole mechanism from scratch** (chain-prefix generation + exhaustive
  one-shot-tail partition search, exact `Fraction` arithmetic) — reproduced the file's headline
  hard instance exactly: `A=(23,12,6,3)`, `m=3`: true (unrestricted) DM-search optimum `=2`
  (verified via a full independent exhaustive DM BFS, not just the chain-prefix family),
  pure one-shot-only optimum `=3` (fails target `44/15`), and the chain-prefix+tail family
  achieves exactly `2` at `c=2` — all three numbers match the outline exactly.
  - Pure one-shot alone genuinely is insufficient: confirmed the family collapses to `3` with
    no cascading option beating it (exhaustive partition search over the 4 elements).
- **Re-ran the stress test independently, 160 fresh random Case-(ii) trials, `m=2..5`** (own
  RNG seed, own generator) — **zero failures**. Extended further myself to `m=6,7` (15 trials
  each) and `m=8` (10 trials) — **zero failures**, directly answering the outline's own flagged
  "re-run at `m=7,8` before committing" open item with a real (if not exhaustive) answer: it
  still holds.
- **Winning `c` stays small**: across my independent trials the largest winning chain length
  observed was `c=1` (my random sample never needed `c=2`, but the outline's own hand-picked
  hard instance needed `c=2` — consistent, not contradictory, since hard instances are rare
  under uniform sampling). No instance in my search needed `c` scaling with `m`.
- **Genuinely distinct from the dead bounded-lookahead family**: I checked the structural
  claim directly — the dead family's failure mode was a **lossy scalar fallback**
  (`e_{m-\ell}\cdot S(\text{residual})`) after a *bounded* prefix, with the required prefix
  depth shown (round 4) to scale with the whole budget. This family instead computes the
  **exact** optimum of a *restricted* (non-cascading) but fully-searched finite space for the
  tail, and `c` ranges over the *entire* `0..m`, not a bounded constant. This is a real
  difference in kind (exact search over a restricted family vs. bounded search + lossy generic
  bound), not a relabeling — confirmed by direct code comparison, not just prose.

One thing worth flagging for the builder (not a blocker): the chain-prefix as defined is a
single serial "always merge the running top result against the next-largest untouched element"
pattern — a 1-parameter family, not the full generality of "any prefix of DM operations." It is
plausible (though untested) that some harder instance needs a chain that does *not* start from
`a_1`, or two independent partial chains. The outline already flags exactly this risk ("if `c`
is ever found to need to scale with `m`, report as new dead end") — recommend the builder also
specifically try to construct an adversarial instance targeting this exact failure mode (not
just random sampling) before investing in the Step 4 adjacency-conjecture proof.

## 3. `concavity-minimax-duality` — new §10 (1-Lipschitz weak-duality certificate)

**Verdict: CHANGES REQUESTED** (the proved lemma is correct and genuinely useful; the payoff
mechanism itself is honestly still speculative — this is the weakest of the three new items,
consistent with this slug's historically lowest Elo).

Independent checks performed:
- **Re-derived the weak-duality inequality from scratch**: for sorted descending
  `x_1\ge\dots\ge x_K\ge0` and 1-Lipschitz `g` with `g(0)=0`, pairing `(x_1,x_2),(x_3,x_4),...`
  (padding a virtual `x_{K+1}=0` if `K` odd, which contributes correctly to both sides since
  `g(0)=0`), each pair satisfies `x_{2i-1}-x_{2i} \ge |g(x_{2i-1})-g(x_{2i})| \ge
  g(x_{2i-1})-g(x_{2i})`, and summing reproduces `e(M)\ge e_g(M)` exactly, with equality at
  `g=\mathrm{id}`. This is correct and the 3-line proof is genuinely elementary (no OT
  machinery needed, matches the file's own claim). **Independently re-verified numerically**,
  3000 random trials (sizes 1–8, exact `Fraction`, using `clip(t,c)` as a family of 1-Lipschitz
  test functions), zero violations.
- **Not a rebrand of Fact 2 or the dead `Φ`**: checked directly — Fact 2 only uses the top
  element (a one-shot upper-direction bound); the dead `Φ` candidates required *per-step*
  monovariance (a much stronger, brittle condition, exactly why both died on a single `M`-move).
  This lemma requires only a *global* inequality at the final state, no step-by-step tracking.
  Genuinely different in kind. No re-tread found.
- **Assessment of "is a concrete certificate in reach, or does this relocate the difficulty?"**
  (per dispatch item 3): the outline is honest that `g=\mathrm{id}` gives zero slack (no help)
  and the one natural cheap candidate (`g=\min(t,e_m)`) is already refuted as too lossy. The
  proposed next step (a bounded LP-feasibility check on the known hard/tied sample points) is
  cheap and a fair diagnostic, but I'd flag more strongly than the outline does: **even if the
  LP is feasible on samples, this does not by itself show a closed-form `g_m` exists for every
  `m`** — extending a per-sample LP-feasible certificate to a provable, `m`-parametrized
  symbolic family is a separate, potentially-as-hard task (a general existence argument, not
  just curve-fitting). This is a real risk the outline underweights; it does not invalidate
  pursuing the LP check (still a fast, decisive, cheap next step, and a clean negative result if
  infeasible), but the builder should not treat "LP feasible on samples" as load-bearing
  progress toward a general proof — only as a go/no-go signal.

No fatal flaw, but this is the most speculative of the three: a real, correctly-proved general
lemma, with the actual hard part (constructing `g_m`) not yet even attempted, only diagnosed.

## Diversity check

The three approaches now attack genuinely different gaps with genuinely different mechanisms:
(a) dyadic-cascade-induction's §5.3 — an integer/parity non-vanishing argument for the *entire*
lower bound; (b) potential-weighting-upper-bound's §6 — an exact restricted-search policy family
for the upper bound's Case (ii); (c) concavity-minimax-duality's §10 — a certificate/duality
object for the lower bound, structurally unlike (a)'s casework-avoidance route (a needs one
combinatorial lemma about tie-avoidance; c needs one function-construction). No shared wall this
round — good diversity, no plateau-break trigger needed.

**One structural concern, not new this round but worth flagging since the round-5 outline
reinforces it explicitly**: `dyadic-cascade-induction`'s Case (ii) section is now an explicit
one-paragraph *pointer* deferring to `potential-weighting-upper-bound`'s unproven §6 result
rather than attempting its own general-`m` Case (ii) closure, and `potential-weighting-upper-
bound`'s own stated target is "Case (ii) specifically (Case (i) is dyadic-cascade-induction's)."
Taken together, these two files are dividing the upper-bound direction's two cases between them
rather than each independently attempting the whole upper bound — this brushes up against
CLAUDE.md's "not one proof split into pieces across sibling slugs" rule. I am not calling this a
RETHINK this round: the *mechanisms* genuinely differ (physical bisection+induction vs. D/M
exact-search policy), each file's induction skeleton is in principle general enough to attempt
either case, and the split tracks a real mathematical dichotomy in the problem (not an arbitrary
partition for convenience) — so this reads more as "two whole-attempt approaches that happen to
have each found their comparative advantage in one case" than "one proof mechanically cut in
half." But it should not calcify further: if a future round adds a *third* upper-bound approach
that also only attempts one case, or if either file's "import pointer" becomes permanent rather
than a temporary deferral, that would tip into the forbidden pattern. Flag for the orchestrator:
watch this, don't let it deepen.

## Dead-end check (per dispatch item 4)

- D/M-completeness overclaim: **not repeated** — both `dyadic-cascade-induction` §5.3 Step 0
  and (pre-existing) `concavity-minimax-duality` correctly cite `dm-completeness-partial.md`'s
  conditional scope verbatim.
- "For every `m`" induction silently assuming same-case residual: Step 3's Main Claim is
  explicitly marked unproved, not claimed closed — no overclaim to catch here this round.
- No new mechanism secretly duplicates global concavity, greedy Rule 1/2, bounded lookahead,
  merging monotonicity, or residual-stays-below-ceiling — checked each of the three new
  sections directly against these five dead ends above; none match.

## Ranking

Anchored to this round's independent verification: `dyadic-cascade-induction` retains the
strongest, most-verified, highest-payoff new content (extends its own numeric evidence beyond
what the outline itself tested, e.g. BFS to `m=7` not just `m=5`); `potential-weighting-upper-
bound`'s new mechanism is a genuine, well-tested improvement over its prior negative-only result
(independently re-verified and extended to `m=8`); `concavity-minimax-duality`'s new lemma is
correct but its payoff mechanism is the least concrete of the three (no concrete instance closed
yet, next step is diagnostic only). Ranked via `update_ranking`:
`dyadic-cascade-induction` beats `potential-weighting-upper-bound`,
`dyadic-cascade-induction` beats `concavity-minimax-duality`,
`potential-weighting-upper-bound` beats `concavity-minimax-duality`.
Resulting Elo: dyadic-cascade-induction 1659 (top), potential-weighting-upper-bound 1463,
concavity-minimax-duality 1390. `elementary-exchange-smoothing` untouched (retired, not
compared/ranked this round per dispatch).

All three approaches are pre-existing slugs (no new registration needed); no branching
requested this round (no `copy_approach` calls).

build set: dyadic-cascade-induction, potential-weighting-upper-bound, concavity-minimax-duality
