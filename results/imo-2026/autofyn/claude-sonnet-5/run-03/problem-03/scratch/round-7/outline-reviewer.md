# outline-reviewer report — imo-2026-03, round 7

## 1. Retirement of `layer-cake-parity-reframing`

Confirmed justified. Checked its ranker record: `last_round: 4`, `last_note`
records a completed proved negative result (the Coupling Obstruction) with
no half-finished thread. It has been idle in rounds 5 and 6 (no builder
touched it, no other approach's open items reference it), and `current.md`'s
dead-end list already independently corroborates "majorization/suffix-
domination monotonicity" (a related mechanism) as a proved dead end via
`dyadic-potential-invariant`, so the field isn't losing a live lead by
dropping this slug. Its three lemmas (layer-cake identity, per-piece
additivity of the threshold count, single-cut marginal-effect formula) are
generic and reusable — agree with the outliner's flag to promote them to
`knowledge_base.md`; recommending this to the orchestrator/reviewer since
promotion is outside this tool's scope. Not registering it for a build this
round; leaving its ranker entry as-is (stale, `last_round: 4`) since it is
paused, not deleted — it can be revived later if a lead reopens.

## 2. Soundness check of the 4 continuing approaches' new targets

**`self-similar-induction-on-n` — bug fix instruction verified sound.**
Read the file's Round 6 section (lines 967–1230) and the certified lemma
file `lemmas/theorem2gen-bounds-and-l0-reduction.md`. Confirmed the
mechanics: `C := B \ {b1}` where `B` is itself a bounded-piece-count
multiset from the outer `Case-B(m,k)` induction (piece count tied to the
outer recursion's budget `k`), so `C` inherits a piece bound from `B` minus
one removed element. The current boxed statement of `L0(ℓ,ε)` in both the
approach file (line 999) and the certified lemma (line 48–50) states only
`sum(C)=2^ℓ+ε` and `max(C)≤2^ℓ-ε` — no piece-count constraint — which is
strictly weaker than what the actual derivation produces (`C` comes from a
bounded-piece `B`), so it is over-general and can be false where the true,
piece-bounded statement is not. This is consistent with the failure mode:
an unconstrained multiset can spread `2^ℓ+ε` of mass across arbitrarily many
small pieces below every tail level, starving `OddSum` far more effectively
than a bounded-piece configurations can. The outliner's corrected statement
(`≤ℓ+1` parts) restores the missing hypothesis and matches the shape of the
outer induction's own piece budget. This is a real, load-bearing fix, not
cosmetic — both files must be amended before any further building on
`L0(ℓ,ε)` this round, exactly as Step 0 instructs. Approved as written.

Step 1 (Branch I.B, two-peel) and Step 2 (order-statistics, only with
remaining time, explicitly barred from a third dichotomy level to avoid
reproducing the known regress) are both well-scoped, incremental, and
consistent with the file's own risk note about infinite regress. Approved.

**`greedy-reduction-geometric` — stress-test-first instruction is sound
methodology.** The outliner correctly identifies that the existing
Insertion-Robustness test family (`k'=1`) is structurally incapable of
producing a counterexample (constant, non-tight margin by the peel
identity) — this is a valid observation, not just a hedge, and directing
the builder to test Level-Absorption first (completely unexamined,
"must-supply-a-deficit" character genuinely different from Insertion-
Robustness's "must-not-hurt" character) is the correct order of operations
before sinking proof effort into an untested claim. Approved.

**`universal-halving-adversary` — boundary-layer redirect is sound.** The
explorer's finding (failure rate rises monotonically toward `p1→1/2⁻`,
saturating near the boundary where the file's own `p1≥1/2` construction is
already unconditionally closed) is a natural continuity/perturbation
target, structurally different from another Anchor-Merge `k` variant (which
round 6 already proved is not monotonically beneficial past `k=2`). The
explicit bar on further `k`-variant testing is correct — that mechanism is
evidenced-exhausted, not merely unlucky. Approved.

**`lp-duality-split-polytope` — highest-priority target is sound and
correctly scoped.** The reduction `excess(n) ≥ 1/((n+1)(n+2))` closing the
whole general-`n` Multi-Piece-Necessity theorem is already certified
(`lemmas/target-excess-identity.md`, round 6) — the outliner is not
introducing new unverified machinery, only asking to prove an inequality
weaker than the already-rejected exact equality conjecture (a strictly
easier target, since round 6 showed the equality form is false at `n=6`
while the numeric evidence for the one-sided inequality survives `n≤16`
with no violation). Requiring exact re-certification at `n=7,8,9` before
attempting the general proof is good discipline (matches the project's
standing "verify before build" pattern from rounds 5–6). Approved as the
highest-value target this round — correctly flagged, since it is the only
approach whose target, if closed, finishes an entire open theorem rather
than narrowing a residual.

No soundness objections to any of the four continuing approaches' revised
targets. No approach proposes re-litigating a documented dead end
(majorization/Schur-monotonicity, `k≥3` Anchor-Merge, third-level dichotomy
regress, literal Cut-Reallocation Exchange Lemma) — checked each target
against `current.md`'s dead-end list explicitly.

## 3. Ranking

Folded round 6's outcomes into Elo via `mcp__approach-ranker__update_ranking`
(all four continuing approaches recorded `advanced` with real, independently
reviewer-verified progress in round 6; relative comparisons reflect the
amount/quality of that progress — `universal-halving-adversary`'s three
certified theorems plus a proved negative result led the round, followed by
a near-draw between `greedy-reduction-geometric` (unconditional base-case
theorem plus a clean exhaustive reduction) and `self-similar-induction-on-n`
(a real bug catch plus a clean equivalence and partial closure), with
`lp-duality-split-polytope` last among the four by this round's realized
progress even though its forward-looking target is now rated highest
priority for round 7). No new approach registered and no copy made — the
outliner opened no new slug this round.

Post-update standings (best-first):
1. `universal-halving-adversary` — 1681.9
2. `greedy-reduction-geometric` — 1550.1
3. `self-similar-induction-on-n` — 1535.1
4. `lp-duality-split-polytope` — 1466.4
5. `layer-cake-parity-reframing` — 1417.4 (retired from rotation, untouched)
6. `dyadic-potential-invariant` — 1349.3 (dead end, untouched)

## 4. Build set

All four continuing approaches carry live, well-scoped, non-duplicated
targets this round; none should be dropped. Dispatching one proof-builder
per slug, each with the outliner's per-approach instructions above
(`self-similar-induction-on-n` must do Step 0's bug fix first).

build set: self-similar-induction-on-n, greedy-reduction-geometric, universal-halving-adversary, lp-duality-split-polytope
