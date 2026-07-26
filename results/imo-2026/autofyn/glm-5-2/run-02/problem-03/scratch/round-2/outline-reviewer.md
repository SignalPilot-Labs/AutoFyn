# Outline review — imo-2026-03, round 2

Reviewer: outline-reviewer (the gate). Reviewed the 4-approach field (2 live stale revisions + 2 new) against the certified lemmas, the explorer reports, and cheap computational sanity checks. Verdicts and ranking below.

## Computations performed (to anchor verdicts)

1. **Mirror certificate** (claimed by `mirror-dyadic-saddle` step 3): Xiang marks at `1−x` for each Liu dyadic mark `x`. Computed the resulting oddsum for n=1..5. Result: **exactly `f(n)` in every case** (n=1→2/3, n=2→4/7, n=3→8/15, n=4→16/31, n=5→32/63). The rank-counting argument is sound: the merged symmetric partition has pairs `(2^k/D, 2^k/D)` for k=1..n−1 plus THREE copies of `1/D`, the three `1/D`'s occupy the last three ranks `2n−1, 2n, 2n+1`, and Liu (odd ranks) captures two of three. VERIFIED.
2. **Regime-N pairing lemma** (claimed by `two-regime-disjunctive` step 4 regime N: non-dominant ⟹ Xiang forces `A ≤ 0`, i.e. oddsum `≤ 1/2`): brute-forced Xiang's best response on six n=2 configs, dominant and non-dominant, on a D=280 grid. Result: **the claim is FALSE.** Every tested non-dominant config (e.g. pieces (0.36, 0.33, 0.31), L=0.36 < 4/11 regime-N threshold) gives min oddsum ≈ 0.503–0.525, strictly ABOVE 1/2. The cap IS `≤ f(2)=4/7` (so the upper bound holds), but NOT via `A ≤ 0`. The mechanism "greedy pairing drives every consecutive pair-excess `≤ 0`" is wrong — the sliver mode of the certified `U(1)` is itself a counterexample (pieces (0.55, 0.45, ε) have top pair-excess 0.1 > 0).
3. **Regime-D cap for dominant non-dyadic configs**: brute-forced Xiang's best response on six dominant non-dyadic n=2 configs (L=1/2, L=3/7, L=5/7). Result: **cap ≈ 0.50–0.504 in every case, WELL BELOW `f(2)=4/7`.** Only the true dyadic attains 4/7. So "cap tight only at dyadic" is CONFIRMED, but the regime-D *rescaling mechanism* (bisect L → IH on rest → `A ≤ α(n+1)`) is NOT what drives the bound for non-dyadic dominant configs — the cap is far below `α(n+1)`, achieved by some other strategy. The rescaling argument only fires when the rest IS the (scaled) n-dyadic.
4. **Single-aux `L*` strengthened IH** (claimed by `pairing-partner` revise, step 4 k=1 sub-case): `evensum({w} ∪ R') ≥ w` for `w ≤ R_largest`. Monte-Carlo (3000 trials, n=2,3,4). Result: **gap ≥ 0 in every case**, equality attained at the self-similar extremal for n=2,3. The `L*` claim is sound.

## Verdicts

### `two-regime-disjunctive` (new) — CHANGES REQUESTED

The disjunctive-invariant framing is the genuinely different route the round-1 shared-wall note asked for, and the "cap tight ONLY at the dyadic; cap well below `f(n)` elsewhere" insight is **computationally confirmed** (finding 3). The approach is salvageable and should be built. But the skeleton as written has three fixable flaws the builder must close:

- **F1 (regime-N lemma is FALSE — finding 2).** The claim "non-dominant ⟹ Xiang forces `A ≤ 0` (Liu `≤ 1/2 < f(n)`)" is verified false: non-dominant n=2 configs give cap ≈ 0.503–0.525 > 1/2. The cap IS `< f(n)` (so Lemma U holds in regime N), but the *mechanism* is NOT "pairing drives all pair-excesses ≤ 0." The builder must replace the regime-N mechanism with the actual one (likely a sliver/shave of the largest piece, generalizing the certified `U(1)` sliver mode — NOT a Hall/pairing argument). Do NOT assert `A ≤ 0`.
- **F2 (regime boundary mis-aligned with the certified `U(1)` base).** The outliner labels the n=1 sliver mode (`a ≥ 1/3`) the "regime-N prototype." But for `a ∈ (1/3, 1/2)`, the larger piece `1−a > a` — the config IS dominant by the outliner's own dominance definition, so it belongs to regime D, yet regime D's bisect/pair-pile strategy FAILS there (bisect gives `(1+a)/2 > 2/3 = f(1)`). The correct n=1 split is "bisect-feasible (`a ≤ 1/3`) vs sliver-required (`a ≥ 1/3`)," BOTH within the dominant regime. The regime boundary for general n is **dyadic vs non-dyadic** (where the rest is a scaled n-dyadic), NOT dominant vs non-dominant. The builder must re-identify the regime boundary so the n=1 two-mode base falls out as a clean special case.
- **F3 (regime-D rescaling is circular for arbitrary configs — finding 3).** The rescaling "the residual game on `R ∪ {L/2, L/2}` is an n-instance with value `α(n)` by IH" only fires when `R` (scaled) is itself the n-dyadic (the IH equality case). For a dominant but non-dyadic config the cap is ~0.5, achieved by some OTHER strategy, and the rescaling does not apply. So regime D as written does not prove the upper bound for arbitrary dominant configs; it only re-proves it at the dyadic (already certified via pair-pile). The builder must either (a) restrict regime D to "rest is n-dyadic" and put ALL other configs in a regime that caps `< f(n)` by a different mechanism, or (b) prove a weaker "≤ α(n+1)" bound that tolerates the interleaving correction.

Load-bearing lemmas identified with mechanism: yes (regime-N pairing lemma, regime-D rescaling lemma, dyadic-dominance identity) — but the first two's stated mechanisms are wrong (F1, F3). The dyadic-dominance identity `2L−1 = α(n+1)` is direct arithmetic and correct. Honest gaps are flagged. No circular reasoning beyond F3. No per-mark induction (respects the round-1 NEVER rule). No bare dominant-piece claim.

**Approved to build, with F1–F3 as required fixes.** Register.

### `mirror-dyadic-saddle` (new) — RETHINK

The mirror certificate itself is **verified correct** (finding 1: oddsum exactly `f(n)` for n=1..5 on the dyadic config). That is a genuine, clean, new contribution — a worthy replacement/simplification of the certified pair-pile as the dyadic-cap half of the saddle. **It should be proposed as a LEMMA** (candidate for certification) by whichever approach builds the dyadic cap this round.

BUT as a standalone APPROACH (a whole rival attempt at `c(n)`), `mirror-dyadic-saddle` is too close to the revised `induct-one-mark`: both are **round-level value induction on n** (`1/V(n+1)=1+1/(2V(n))`, Mersenne `B(n+1)=2B(n)+1`), both identify the `+1` as the interleaving-boundary correction, and both fall back to the separate (Lemma L + Lemma U) statements when the value-level argument does not close. The ONLY substantive difference is the dyadic-cap certificate (mirror vs certified pair-pile) — and that is a *technique* swap on the same sub-step, exactly the "approaches that only differ in technique" the orchestrator's rule forbids. They share the same wall (the `+1` interleaving correction), so they will stall together — the single-gap trap.

The approach is also honest about mirror being dyadic-only (verified: mirror FAILS on non-dyadic configs, e.g. Liu `{1/5, 2/5}` → mirror oddsum 3/5 > 4/7), so it does not itself close Lemma U and must delegate that to the sibling two-regime route.

**Do not build as a standalone approach.** Instead: tell the builder of `pairing-partner` or `induct-one-mark` to import/propose the mirror certificate as a lemma this round (it is cleaner than the pair-pile and verified), and send `mirror-dyadic-saddle` back to the outliner to re-plan as a GENUINELY different framing (e.g. a majorization/Schur-convexity route, which the two-regime explorer flagged as untested) if a third distinct framing is wanted. **Not registered.**

### `pairing-partner` (revise) — APPROVE

The revision plan is sound and the strongest lower-bound route in the field. Concretely:

- The `M ⊎ R` self-similar decomposition (Opening A/B from the lowerbound explorer) correctly disposes of the k=0 sub-case trivially (`global_A ≥ M − total(R) = 1/D(n+1)`, no induction) — verified the dyadic-dominance identity.
- The k=1 sub-case reduces cleanly to the single-aux `L*(n)` (verified, finding 4: gap ≥ 0 for n=2,3,4 with equality at the self-similar extremal). This is the cleanest close of the round-1 Lemma L interleaving gap so far.
- The k≥2 sub-case is honestly flagged OPEN (per-round peeling D1, or fallback D2 WLOG-k=1) — the multi-aux generalization is correctly identified as FALSE (the explorer's counterexample). Good — no recorded dead-end repeated.
- The Lemma U pivot to the two-regime split inherits `two-regime-disjunctive`'s regime-N flaw (F1 above); the builder must track that dependency and use the corrected regime-N mechanism once `two-regime-disjunctive` supplies it, NOT the false `A ≤ 0` pairing.

No circular reasoning, no per-mark induction, no bare dominant-piece claim, no Hall-on-non-dyadic retry. The `L*` lemma is named WITH its mechanism (case split `w` at even rank vs odd rank, using `oddsum(R') ≥ R_largest ≥ w` to compensate). **Approve.** Keep existing slug.

### `induct-one-mark` (revise) — APPROVE

The revision correctly retires the certified-false per-mark monovariant (round-1 NEVER rule) and upgrades to the round-level value recursion `1/V(n+1)=1+1/(2V(n))` (Mersenne `B(n+1)=2B(n)+1`) in A-space — the right framing consistent with the per-round value-recursion finding. The `+1` interleaving correction is honestly flagged as the load-bearing hard term with NO potential accounting identified (honest, not papered over). The fallback to separate (Lemma L + Lemma U) is explicit and the approach is solved as soon as both close, even if the unified value-recursion does not fire.

Caveats for the builder:
- The value-level recursion (step 4+5 unified) is aspirational and may not close — the builder should time-box it and fall back to importing Lemma L (from `pairing-partner`'s `L*` route) and Lemma U (from `two-regime-disjunctive`'s corrected two-regime) rather than re-deriving either.
- Do NOT re-attempt the per-mark monovariant (verified fatal); do NOT use the wrong recursion `V(n+1)=(1+V(n))/2` (the outliner correctly flags it).

**Approve.** Keep existing slug.

## Field diversity note for the orchestrator

The two live approaches (`pairing-partner`, `induct-one-mark`) plus `two-regime-disjunctive` give three genuinely-distinct framings: (a) M⊎R self-similar decomposition + single-aux dual IH (lower-bound-focused, Lemma L route); (b) round-level value recursion in A-space (unifying-recursion-focused, aspirational); (c) disjunctive two-regime invariant (upper-bound-focused, Lemma U route). They attack different halves of the problem and diverge on framing, so the field is broad. `mirror-dyadic-saddle` would have collapsed (b) into a near-twin; cutting it keeps the field at three distinct routes. The mirror certificate is salvaged as a lemma contribution rather than lost.

## Ranking (fed to `update_ranking`)

Comparisons (anchored to last outcomes + this review's findings):

1. `pairing-partner` > `induct-one-mark` — `pairing-partner` was `advanced` round 1 (strongest certified progress: Lemma G + pair-pile + ΔA all certified there) and this round adds the verified `L*` strengthened IH, closing the k=1 sub-case of Lemma L. `induct-one-mark` was `partial` and retired its signature per-mark technique; its revision is an honest aspirational fallback.
2. `pairing-partner` > `two-regime-disjunctive` — `pairing-partner` has certified progress and a verified strengthened IH; `two-regime-disjunctive` is new (cold-start) with a verified-FALSE regime-N lemma (F1) and a mis-aligned regime boundary (F2). Newcomer anchored below the established leader.
3. `induct-one-mark` draw `two-regime-disjunctive` — `induct-one-mark`'s revision is honest (retires the dead end, clean fallback) but aspirational (value-recursion likely won't close); `two-regime-disjunctive` has a genuinely different framing (more valuable to field breadth) but a verified-false load-bearing lemma. Balanced: a draw.

Final ranking (best-first): `pairing-partner`, `induct-one-mark` ≈ `two-regime-disjunctive` (tied by the draw), with `two-regime-disjunctive` carrying the framing-diversity premium. (Mirror-dyadic-saddle not ranked — RETHINK, not registered.)

## Registrations

- `two-regime-disjunctive`: NEW, approved → `register_approach`.
- `mirror-dyadic-saddle`: NEW, RETHINK → NOT registered (junk stays out of the pool; the approach goes back to the outliner for re-planning, its mirror certificate salvaged as a lemma contribution).
- `pairing-partner`, `induct-one-mark`: existing slugs, refreshed summaries, not re-registered.

## Build set

Three approaches, each a distinct framing:

- `pairing-partner` — close the k≥2 sub-case of Lemma L (per-round peeling D1) and prove `L*(n+1)` (Xiang-side dual); propose the **mirror certificate** as a lemma (replacing/simplifying pair-pile) since `mirror-dyadic-saddle` is cut.
- `two-regime-disjunctive` — fix F1 (regime-N mechanism: sliver/shave, NOT `A ≤ 0` pairing), fix F2 (regime boundary = dyadic vs non-dyadic, not dominant vs non-dominant), and either restrict regime D to "rest is n-dyadic" or prove a weaker `≤ α(n+1)` bound tolerating interleaving.
- `induct-one-mark` — attempt the round-level value recursion (time-boxed), fall back to importing Lemma L (from `pairing-partner`'s `L*`) and Lemma U (from `two-regime-disjunctive`'s corrected two-regime).

build set: two-regime-disjunctive, pairing-partner, induct-one-mark
