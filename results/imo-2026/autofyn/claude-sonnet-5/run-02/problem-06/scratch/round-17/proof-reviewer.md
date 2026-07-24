# Proof review — round 17 — imo-2026-06

## Build set this round: `self-absorbing-by-construction` (only slug built)

### Summary verdict

**CHANGES REQUESTED** (Status: **partial** — matches the builder's own honest
self-report). The new Vacuous/Weak Self-Absorption Lemma is correct and has
been certified. The 3-apparent-counterexample numeric investigation is
correct for 2 of 3 seeds and genuinely inaccurate for the third
(`a_1=255255`); this does not affect the correctness of the certified lemma
or invalidate the honestly-open NTBT conjecture, but it does mean the
approach's evidentiary claim ("all 3 apparent counterexamples resolved") is
not fully established. The conjecture NTBT remains open and honestly reported
as such — no overclaim on the central open item.

---

## 1. Vacuous/Weak Self-Absorption Lemma — VERIFIED CORRECT, unconditional

Claim (approach file §2): if `N(Q) ≤ 1` then `S_0 := Q` is self-absorbing
(`Q⁺ = Q`), so the absorption chain terminates in zero rounds with `S* = Q`.

Independent re-derivation from scratch:

- `N(Q) = 0`: `⋃_{j=1}^{0} P(a_j)` is a union over the empty range
  `{j : 1 ≤ j ≤ 0}`, which is genuinely empty — no integer satisfies
  `1 ≤ j ≤ 0`. So the union is `∅` and `Q⁺ = Q ∪ ∅ = Q`. Correct, and the
  "vacuous" framing is accurate (the self-absorption condition holds because
  it quantifies over an empty index range, not because a nontrivial
  containment was checked).
- `N(Q) = 1`: `⋃_{j=1}^{1} P(a_j) = P(a_1)`. Since `Q := P(a_1)` by
  definition, this union equals `Q` exactly. So `Q⁺ = Q ∪ Q = Q`. Correct —
  this is a direct, immediate consequence of how `Q` is defined, not a
  nontrivial fact requiring FAH or any other open hypothesis.

Both cases are exhaustive (`N(Q) ≤ 1` literally means `N(Q) ∈ {0,1}`, and
`N(Q)` is a specific well-defined nonnegative integer by the certified
Persistent-Type Pigeonhole, so the case split is total and disjoint). The
lemma depends only on already-certified machinery
(`persistent-type-pigeonhole.md`, the absorption operator from
`self-absorbing-core-theorem.md`) and elementary set-theoretic unpacking of
definitions. No circularity: it does not invoke FAH, NTBT, or any other open
hypothesis at any point.

This is a simple lemma (essentially unpacking two definitions), but it is
correct, non-trivial in the sense that it identifies the SHARP sufficient
condition (`N(Q) ≤ 1`, not merely `N(Q)=0`, matching the builder's own
"weak" framing), and genuinely useful: it gives the minimal possible terminal
core `S*=Q` for hypothesis H2 whenever the condition holds, collapsing the
remaining content (if NTBT is ever proved) to bare FAH at `Q` — no core
enlargement needed at all. **Certified** to
`results/imo-2026-06/lemmas/vacuous-self-absorption-lemma.md`.

## 2. Numeric investigation — INDEPENDENTLY RE-SIMULATED FROM SCRATCH

Wrote a fresh, independent Python greedy-sequence generator (trial-division
gcd-based, no shared code with the builder) and an independent base-type /
occurrence-list analysis. Method: generate the exact greedy sequence for a
given `a_1` up to a specified length, compute `τ(n) := P(a_n) ∩ Q` for each
`n`, and directly enumerate occurrence lists per type (not just the
tail-persistence proxy).

**`a_1 = 30030` (2|a_1, |Q|=6).** Generated 60,000 terms (~95s). At window
15,000 the tail-persistence proxy shows exactly one exception, `n=1` (matches
builder). At window 30,000+ zero exceptions (matches builder). Direct
occurrence check of the full-`Q` type: **`{2,3,5,7,11,13}` occurs at
`n = 1, 15016, 30031, 45046`** (gap exactly 15015) — EXACT match to the
builder's reported numbers. Genuine window artifact, confirmed independently.

**`a_1 = 15015` (odd, |Q|=5).** Generated 30,000 terms (~24s). At window 4000,
two exceptions (`n=1` and `n=1544`, `N(Q)` proxy `=1544`) — matches builder.
At window 8000+, zero exceptions — matches builder. Direct occurrence check:
**`{3,5,7,11,13}` occurs at `n = 1, 4629, 9257, 13885, 18513, 23141, 27769`**
(gap ≈4628, constant) — EXACT match to the builder's reported numbers.
Genuine window artifact, confirmed independently.

**`a_1 = 255255` (odd, |Q|=6) — DISCREPANCY FOUND.** The builder claims:
"extending the window to 40000 confirmed a second occurrence for every one of
these five previously-single-occurrence types... the sole remaining
single-occurrence type at window 40000 is the full-`Q` type." I generated
45,000 terms (~56s) and did an EXHAUSTIVE enumeration of every type with
exactly one occurrence in the window (not just re-checking the builder's
5 previously-flagged types) — this is the key methodological difference from
the builder's own re-check, which only revisited its already-named list.
Result at window 40,000/45,000: **THREE** single-occurrence types, not one:

```
[3, 5, 7, 11, 13, 17]  -> [1]          (the full-Q type, as the builder found)
[3, 7, 11, 13, 17]     -> [16311]      (NOT mentioned anywhere in the builder's file)
[5, 7, 11, 13, 17]     -> [27184]      (NOT mentioned anywhere in the builder's file)
```

Extending further to window 65,000 (~120s more): the `{3,7,11,13,17}` type
recurs (no longer single-occurrence — consistent with the window-artifact
story), but **`{5,7,11,13,17}` remains single-occurrence** (still only at
`n=27184`, no second occurrence in the next 37,816 terms) — a longer
observation gap than any of the confirmed-genuine recurring types in this
seed needed to show their second occurrence (the builder's own five
confirmed-recurring types' second occurrences all appeared between roughly
4,000 and 27,000 terms after their first).

**Assessment.** This does not refute NTBT (the type could still recur at a
larger window than tested, exactly as the builder's own resolved cases did),
and it does not touch the correctness of the certified Vacuous/Weak
Self-Absorption Lemma (unconditional, independent of this seed's specific
numerics). But the builder's specific claim — "the sole remaining
single-occurrence type is the full-Q type" — is **false as stated at window
40,000**, because a second, unflagged candidate exists and remains unresolved
25,000+ terms beyond first occurrence. This is a genuine inaccuracy in the
supporting numeric evidence, traceable to a methodological gap: the builder's
"re-check the 5 previously-flagged types" approach cannot catch a NEW
single-occurrence type that only becomes visible once the window is extended
past where it was first flagged. An exhaustive re-enumeration at each window
size (not just a re-check of a fixed named list) is needed and was not done.

## 3. NTBT conjecture — correctly reported as open, no overclaim

The central conjecture (`N(Q) ≤ 1` for every `a_1 > 1`) is explicitly and
correctly reported as unproved, with two attempted proof routes (density/
recurrence-forcing via class-blind lemmas; reduction to/from FAH) both
honestly shown to fail, matching the standing class-blindness diagnosis and
the round-15 finding that H2-native quantities are logically distinct from
FAH. No overclaim: the file's own Status and "What this does and does not
establish" section correctly separates the proved lemma from the open
conjecture. This review's finding (§2 above) if anything *strengthens* the
case that the numeric evidence for NTBT is weaker/messier than the file
represents — a useful correction for the next round, not a reason to
downgrade the file's honesty about the conjecture itself, which remains
correctly labeled unproved throughout.

## 4. Overclaim / rigor check

- Status claimed by builder: `partial`. Confirmed correct — matches my
  findings exactly (a genuine lemma, an open conjecture, honestly reported).
- No hand-waving found in the Lemma's proof (§2 of the approach file) — both
  cases are spelled out explicitly, including the "empty union" edge case.
- The "Combining both parts"/citation-gap trap pattern (memory rules 27–28)
  does not apply here — the lemma is fully self-contained, no citation
  substitutes for a derivation.
- The one issue found (§2 numeric inaccuracy for `a_1=255255`) is a
  supporting-evidence error, not a proof-step error, and does not change the
  Status from `partial`.

## Actions taken

- **Certified** `results/imo-2026-06/lemmas/vacuous-self-absorption-lemma.md`
  (Vacuous/Weak Self-Absorption Lemma, unconditional, gap-free).
- **Updated** `results/imo-2026-06/current.md` `## Status` (new round-17
  paragraph prepended) and `## Approaches tried` (new round-17 entry for
  `self-absorbing-by-construction`), both reflecting the CHANGES REQUESTED
  verdict and the specific `a_1=255255` inaccuracy for the next round to
  investigate (extend the window further on the unresolved
  `{5,7,11,13,17}` type, first occurrence `n=27184`, unresolved through
  `n=65000`).
- **Recorded outcome** via `record_outcome` (`self-absorbing-by-construction`,
  round 17, outcome `partial`).
- Did NOT re-attempt `type-alphabet-counting-bound` (correctly RETHINK'd
  pre-build by the outline-reviewer, not built this round, not reviewed here).

## Gap for next round (precise)

For `a_1 = 255255`, the type `{5,7,11,13,17}` (`τ(27184)`) is the current
most concrete open candidate for a genuine (non-window-artifact) failure of
NTBT — or, if it eventually recurs at a large enough window, the fourth
resolved window artifact. Next round should extend the simulation
(recommend window ≥ 150,000–200,000, budget permitting) specifically on this
type before either (a) declaring `a_1=255255` fully resolved, or (b)
promoting it to a genuine reported counterexample candidate for NTBT. Do not
reuse the builder's "re-check the 5 previously-flagged types" methodology —
always re-enumerate ALL single-occurrence types fresh at each window size
(see the new memory rule appended this round).
