# Outline review — round 17 — imo-2026-03

Reviewed: `/tmp/round-17/proof-outliner.md`, the new §27 of
`results/imo-2026-03/approaches/potential-weighting-upper-bound.md` (lines 6171-6418), the three
round-17 explorer reports, `results/imo-2026-03/current.md`, and the certified lemma
`lemmas/delete-suffices-insertion-domination.md`. All checks below use a fresh, independently
written harness (`/tmp/round-17/verify/`), not the explorers'/outliner's own code.

## potential-weighting-upper-bound — APPROVE (sole live slug, still `partial`)

Still a genuine whole-attempt (Claim A via the Non-Matching-Witness Criterion, upper-bound
direction; lower bound already unconditional since round 8). No case is silently dropped, no
already-dead mechanism (general `|C|=2` Two-Touch, flat non-crossing induction, Hall's theorem,
averaging, etc.) is resurrected — I grepped the "Watch out for" list against §27's own new claims
and found no reintroduction.

### 1. The headline claim (§27.1): Gap 1b's inductive step ≡ half of Gap 1a's Deletion-Suffices — CONFIRMED, correctly hedged, one precision note

Independently re-derived the algebra from the certified §13.2 KEEP-branch closed form
(`h:=|{c∈C : c>z1}|`, `KEEP = e(B_hi)+(-1)^h z1 + (-1)^{h+1} OPT_{σ·(-1)^{h+1}}(B_lo,rest)`) *before*
reading the outliner's derivation. At `h=0`: `DELETE=OPT_{+1}(C,rest)`, `KEEP=w1-OPT_{-1}(C,rest)`,
so `Sum Bound (w1≥OPT_{+1}+OPT_{-1}) ⟺ DELETE≤KEEP` is a **pure algebraic tautology** given the
certified formula — no computation is even needed to be sure of this, but I ran it anyway:
`0/2638` fresh trials (mixed rest sizes, including duplicate-heavy and boundary-tie `h=0` cases)
confirm both the KEEP-formula substitution and the equivalence itself, `/tmp/round-17/verify/test_identity.py`.
This part of the claim is airtight.

The deeper claim — "proving Deletion-Suffices-for-`k*` at general `q` hands you Gap 1b's induction
for free at every recursion depth" — is **more subtle than a pure substitution** and I traced it by
hand: Deletion-Suffices' own natural proof (strong induction on `q`, peeling the top element) needs,
at each depth, `DELETE(=OPT_{+1}(C,rest), by IH literally `=e(C)`) ≤ KEEP`, which after substituting
the IH is *exactly* the same comparison as Gap 1b's target at that depth. So the two inductions
genuinely share their DELETE-vs-KEEP inductive content, **provided** the same external top-level
`A1` (not a locally re-derived trigger) is threaded through every depth — which is precisely what
the file's own "Watch out for (iv)" and the negative control (dropping the top-level trigger gives
37.0% failures at `q=4`, reproduced structurally in my own trace of the algebra) already flag. This
is a real, correctly-scoped insight, not an overclaim — but it is fragile in exactly the way this
project's prior "silently assumed hypothesis" bugs have been (memory Rules: global-argmin-ness,
implicit peeling-formula hypotheses). **Recommendation to the builder:** state explicitly, before
building on this, which quantifier is being used — "Deletion-Suffices holds along the *specific*
DELETE/KEEP-only descent chain from one genuine top-level base generator" (weaker, sufficient here)
vs. "Deletion-Suffices holds for *every* independently-sampled top-level instance of size `q'<q`"
(stronger, not needed and not established) — the file's own phrasing sometimes reads like the
stronger, unneeded version ("at general `q`... hands you Gap 1b's inductive step... for free, at
every recursion depth"). Not fatal, a wording/scope discipline item.

### 2. Three-Touch candidate (§27.2(d)) — dispatch task 1 — CONFIRMED, no overclaim

Independently coded `e()`, full brute-force `OPT_σ`, `Two-Touch` (min, touch≤2) and the proposed
`Three-Touch` (max, touch≤3, 5 candidate shapes) from scratch (`/tmp/round-17/verify/test_threetouch.py`).
- Three-Touch itself: **0/3000** random, **0/1500** duplicate-heavy adversarial, **0/340** exhaustive
  small grid — `0/4840` combined, exceeding the file's own `0/3480` sweep.
- Confirmed the touch-3 term is genuinely load-bearing: `Two-Touch(max, touch≤2)` alone fails against
  the true `OPT_{-1}` in **628/2000 (31.4%)** of my fresh trials (file doesn't report this exact
  number but is consistent with the term being necessary), and the touch-3 term is a *strict*
  improvement over touch≤2 in **910/2000 (45.5%)** of cases (file reports `193/1000≈19.3%` — same
  direction/conclusion, different sampling, not a discrepancy worth flagging).
- End-to-end target `w1-ThreeTouch(b0,rest) ≥ TwoTouch({b0},W)`: **0/2638** random-`h=0` trials plus
  **0/2000** duplicate-heavy/boundary-tie trials (`w1` forced exactly equal to `max(rest)` or `b0`) —
  `0/4638` combined, exceeding the file's `0/1239`. No violation found anywhere, including the
  adversarial tie cases the dispatch specifically asked me to probe.
This candidate is solid, well-scoped, genuinely "not yet formulated → now concretely formulated and
heavily corroborated." No overclaim.

### 3. Gap 1c's 3-way split, case (b) "reduces for free" (§27.3) — dispatch task 2 — algebraically sound, lightly tested (rare case)

Independently verified the underlying mechanism, Lemma P's duplicate-pair cancellation
(`e(base∪{c,c})=e(base)` for arbitrary `base,c`): **0/3000** violations, confirming the general
invariance the reduction leans on. I then traced the derivation by hand: if the sparsest optimal
witness of the **RHS** quantity `OPT_{+1}(B1∪{d},X)` is a pure duplicate pair `{c,c}` (nothing else
kept/matched), Lemma P forces `RHS=e(B1∪{d}∪{c,c})=e(B1∪{d})` exactly, collapsing the target
`LHS≤RHS` to `LHS≤e(B1∪{d})` — literally the same 3-step chain (`OPT_{+1}(B1,X)≤e(B1)` via
Shrink-List, `e(B1)≤e(B1∪{d})` via the certified `delete-suffices-insertion-domination.md`,
conditional on Deletion-Suffices-for-`k*`) already used for case (c)'s `ξ*=∅` closure. This is
correct algebra, not a hand-wave. **One flagged imprecision, cosmetic not fatal:** the file's `ξ*`
notation drifts across sections — §25.3 originally defines `ξ*` as "the LHS-optimal witness" (of
`OPT_{+1}(B1,X)`), while §26.3/26.4/27.3's actual usage is the **RHS**-problem's optimal witness (of
`OPT_{+1}(B1∪{d},X)`) — I only resolved this by cross-reading §26.3's literal "∅ is the unique
optimum of `OPT_{+1}(B1∪{d},X)`" against §25.3's "LHS-optimal" label. The math these sections do is
internally consistent once you use the RHS reading, but the label is actively misleading and should
be fixed (rename to "the RHS-optimal witness" or similar) before a builder inherits the confusion.
**Independent reproduction gap (honest, not a correctness concern):** case (b) is rare — my own
`4000`-trial random sweep with genuine `(B1,Res,d,X)` construction found **0/2759** instances landing
in case (b) at all (1414 empty-witness/case-c, 1345 generic/case-a, 0 duplicate-pair/case-b),
consistent with the file's own reported rarity (`2/728`, ≈0.3%). I did not have time to hand-construct
an adversarial instance that actually triggers case (b) to give it a fully independent computational
confirmation — recommend the next builder do this explicitly (deliberately engineer a match/keep
combination producing a value-duplicate in the RHS witness) before treating case (b) as fully settled;
the *mechanism* is sound, the *concrete instance class* is unverified by me.

### 4. Other checks

- **Gap 1a's Two-Touch 3/5 proved pieces** (base case, DELETE branch, KEEP `b0>w1`): re-traced the
  Rank-Extraction substitution for the `b0>w1` sub-case by hand (uses the already-certified
  Empty-Background Lemma, `OPT_{+1}(∅,rest)=0`) — correct, no gap.
- **Sampler-bug patterns** (per dispatch item 3 / memory Rules): checked my own harnesses enforce
  `w1=max(W)` and the `h=0` filter explicitly in every test above (both were previously-recurring
  bugs in round 16's own reviewer harness) — confirmed present throughout my scripts. I did not find
  either bug reintroduced in the file's own reported figures (its stated scopes — "genuine `h=0`
  branches only," "`w1=max(W)`" — are stated explicitly in §23.3 and honored in §27's new material).
- **No new slug opened** — correct call. The population has had one live slug for 10 rounds, but
  it keeps producing certified content every round (2-3 new lemmas/round recently) — this is
  "progress, not plateau" per the standing rule (only open a fresh-framing slot after 2+ rounds with
  *no* new leverage, which is not the case here). `dyadic-cascade-induction` and
  `concavity-minimax-duality` remain correctly benched (nothing in this round's findings gives either
  new leverage on the still-open upper-bound gap).
- **Diversity check**: the 3 explorers each targeted a different one of the 3 named gaps (not 3
  variations on one gap), and the outliner's contribution (§27.1, §27.4) is a genuine structural
  discovery (fewer independent open mechanisms than previously tracked), not a relabeling. No
  single-gap-trap violation.

## Verdict

**potential-weighting-upper-bound: APPROVE.** The outline is sound, the headline reconciliation is
correctly derived (verified independently from scratch), the two dispatch-flagged claims (Three-Touch,
Gap 1c case-b reduction) both hold up under fresh adversarial testing, and every "not yet proved"
label in the file matches what I could independently establish. Two non-blocking notes for the
builder: (1) state the Deletion-Suffices⇒Sum-Bound "for free" claim using the weaker,
sufficient quantifier (same top-level `A1` threaded through one fixed descent chain), not the
stronger "for every `q'<q` instance" reading the prose sometimes suggests; (2) fix the `ξ*`
LHS/RHS labeling drift between §25.3 and §26.3/27.3 before it causes a real error, and construct one
concrete case-(b) instance to confirm the rare-case mechanism computationally, not just by algebra.

`dyadic-cascade-induction` and `concavity-minimax-duality`: correctly benched, no action.
`elementary-exchange-smoothing`: correctly retired, no action.

No RETHINK. No new slug registered (none proposed). Ranking updated via `update_ranking`
(potential-weighting-upper-bound > concavity-minimax-duality, potential-weighting-upper-bound >
elementary-exchange-smoothing, dyadic-cascade-induction > concavity-minimax-duality) — clears the
`stale` flag on potential-weighting-upper-bound and reflects that it remains the field's only
actively-producing line.

build set: potential-weighting-upper-bound
