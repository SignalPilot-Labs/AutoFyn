# Round 12 proof-outliner report

**Action taken:** revised `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` in
place (no new slug opened — single-gap-trap avoided per CLAUDE.md/standing rule). Added a round-12
note to the top `## Status` block and a new `### 17` section (~150 lines) building a skeleton
around the two convergent round-12 findings.

## What the three explorers found

- `math-explorer-aimo0198-averaging.md`: **confirmed dead end.** Neither a state-independent sum
  identity nor an existential all-partners-average bound survives past a vacuous `q=3` case; the
  existential bound succeeds in only 1.5–17.7% of triggered instances and trends to 0% by `q=6,7`.
  Even in the best case it could only reach the weaker existential RDRC, never index-exact SAR.
  **Do not revisit.**
- `math-explorer-global-witness.md`: **No-Second-Trigger** — one level inside the argmin-branch
  residual `(B_1,Z_1)`, the residual's own MATCH branch never strictly beats its own DELETE branch
  (~12,000 evaluations, 0 violations at depth 2), *provided* ties are canonically broken toward
  DELETE/KEEP (a forced-tie adversarial probe found a genuine violation one level further in
  otherwise).
- `math-explorer-recursive-invariant.md`: **Delete-Suffices** — the entire residual sub-problem
  `(B_1,Z_1)` achieves its true unrestricted optimum using only Keep/Delete, never matching, at
  any depth (2870+ trials, 0 violations; two negative controls confirm both "true global argmin"
  and "trigger holds" are load-bearing, not cosmetic).

## The reconciliation (new §17)

These are **not literally the same statement as tested** — Delete-Suffices is the closed,
all-depths claim; No-Second-Trigger (as tested) is a one-step fact about the very first peel. §17
defines a precise scope family `F` (triples `(C,W,σ)` generated from a base `|B_0|≤1` trigger by
closing only under DELETE/KEEP, explicitly *not* under MATCH) and shows, by routine strong
induction on `|W|`, that **Delete-Suffices for `F` is exactly equivalent to "No-Second-Trigger
promoted to hold at every node of `F`, with the tie-break rule folded in"** — i.e., the two
explorers found the same mechanism from opposite ends: one the closed target, one its own
inductive step. Neither explorer tested the fully-promoted (all-depths) version directly — that's
the central gap.

The unified target is named the **Match-Free Recovery Lemma**: for every `(C,W,σ)∈F`,
`OPT_σ(C,W) = OPT_KD_σ(C,W)` (KD = Keep/Delete-only optimum). §17.4 gives the one-line derivation
that this trivially implies SAR (an all-K/D witness has zero arcs, hence is vacuously non-crossing
and vacuously compatible with any split) — explaining *why* this route can succeed where the
"one-step compatible winner" GML skeleton failed (§16.3.3): GML's hypothesis needed
split-compatibility re-certified at every depth (and was shown to evaporate one level down);
Match-Free Recovery's hypothesis is arc-free, so nothing can ever conflict with a future split.

## Gaps identified (§17.6)

1. **Gap 1 (central, open):** the "No-Second-Trigger at every node of `F`" inequality itself —
   corroborated at depth 1–2 only, not proved, not tested at depth ≥3 under the correct tie-break,
   nor at scale for `σ=-1`.
2. **Gap 2 (bookkeeping, believed easy, unwritten):** `OPT_KD_σ` obeys the identical DELETE/KEEP
   trichotomy (with the same Rank-Extraction closed form) as `OPT_σ` restricted to `M=∅`.
3. **Gap 3 (the `σ=-1` sub-case):** §15.4's own flagged-but-unverified observation that the max-side
   trigger may never fire at all — if true, Claim A is vacuous on `σ=-1` nodes, roughly halving the
   remaining casework.
4. **Gap 4 (scope-closure sanity, near-free once 1–3 are proved):** `F`'s construction forbids a
   MATCH closure, so every member has `|C|≤2` by construction — automatically staying clear of the
   confirmed-FALSE `|B|=3` generalization (§16.3.2); worth stating as an explicit corollary.

## Build order and pre-build sanity sweep (§17.7–§17.8)

Recommended order: Gap 2 (cheap, mechanical) → Gap 3 (cheap, halves casework if it goes through) →
Gap 1 (central; first try adapting the Forced Swap Inequality's global-argmin-chaining technique to
`(C,W)`'s own argmin, flagged as *not obviously sufficient* — may need a genuinely new inequality)
→ assemble the induction and close SAR via the §17.4 corollary. Named tools: General
Rank-Extraction Identity (directly reusable for the KEEP closed form) and Forced Swap Inequality
(closest certified relative for Gap 1, applicability explicitly flagged as unverified, not assumed).

Recommended cheap pre-build sweep before committing a full build round: (a) exhaustive (not
sampled) `q=7,8` sweeps propagated through 2–3 levels of DELETE/KEEP recursion, not just the base
generator; (b) adversarial hill-climbing/simulated-annealing minimizing/maximizing
`OPT_KD_σ - OPT_σ` toward a violation at multiple depths, including the forced-tie variant that
already found a violation at depth 3 without the tie-break rule; (c) a dedicated exhaustive check
of the `σ=-1`/`|B|=0` "vacuous match branch" observations (Gap 3), currently the least-tested piece
of the skeleton.

## File changes

- `results/imo-2026-03/approaches/potential-weighting-upper-bound.md`: added a round-12 note in the
  top `## Status` block (after the round-11 builder note) and a new `### 17` section (§17.1–§17.8,
  ~150 lines) at the end of the file. No other files touched; no new slug registered.
