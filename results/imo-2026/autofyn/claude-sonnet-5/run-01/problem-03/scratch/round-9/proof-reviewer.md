# Round 9 proof-reviewer report — imo-2026-03

Reviewed the two round-9 builds: `potential-weighting-upper-bound` (new §13) and
`concavity-minimax-duality` (new §15). Every claimed lemma and counterexample was independently
re-derived and re-checked with fresh, from-scratch Python (exact `Fraction`/`int` arithmetic,
never reusing the builders' own harness code). Scripts are in `/tmp/round-9/work/`.

## Approach 1: `potential-weighting-upper-bound` (§13)

### Claims and independent verification

**1. General Rank-Extraction Identity** (§13.1). Claim: for sorted `F`, element `x` at rank `r`,
`e(F) = e(head) + (-1)^{r-1}x + (-1)^r e(tail)`.
- Re-derived from scratch: applying the already-certified Fact 3 twice (`F = head ⊔ ({x}∪tail)`,
  then `{x}∪tail = {x} ⊔ tail`) reproduces exactly this formula. Correct, not hand-wavy.
- Independent computation: 3000/3000 exact-`Fraction` trials (`n=1..10`), 0 mismatches.
- **Certified** to `lemmas/general-rank-extraction-identity.md` (updated the certification header;
  statement/proof text was already correct as the builder wrote it).

**2. Generalized Multi-Background Peeling Lemma — DELETE/KEEP branches** (§13.2). KEEP's exact
closed form (parity-governed reduction via the Rank-Extraction Identity to
`OPT_τ(B_lo, Z\{z1})`/`TAGGED_τ(B_lo,Z\{z1},0)`).
- Independently re-implemented `OPT`/`TAGGED` via a from-scratch brute-force enumeration over
  *all* `(K,D,M)` selections of `Z` (own recursive enumerator, own non-crossing/split-spanning
  check — not the builder's code), then checked the KEEP formula against a separately-coded
  "force `z1∈K`" brute force. 800/800 checks (both `OPT`-side and `TAGGED`-side, `|B|=0..3`,
  `q≤6`), **0 mismatches**. Correct.
- Also independently verified the *full* DELETE+KEEP+MATCH decomposition (using the file's own
  claimed MATCH-branch split point `k-1`, which I independently re-derived by tracking which
  original ranks land "inside" vs "outside" the match — matches) reproduces true `OPT` and
  `TAGGED(·,0)` exactly: 400/400 for each, 0 mismatches.

**3. Negative sub-result** (§13.4): individual per-`k` match equality fails often (my own trial:
117/500 vs the file's 152/500 — different seed/sizes, same order of magnitude); the *match-only*
aggregate (ignoring DELETE/KEEP) fails in a small nonzero fraction (mine: 7/500 vs file's 3/500);
the *full* DELETE+KEEP+MATCH aggregate never fails even when match-only does (mine: 0/500 exactly
matching the file's 0/500 residual-failure claim). Confirmed exactly — the DELETE/KEEP
compensation escape hatch in the Match-Recovery Lemma's hypothesis is real, not a hedge. I also
ran an additional cross-check the file itself doesn't run: the raw match-only aggregate holds with
**zero** failures at the literal top level (`|B|=0`, the original Small-Gap Crossing-Domination
Lemma's own regime) — 0/800 — sharpening (not contradicting) the file's own diagnosis that the
failures are specific to the deeper recursion levels the recursive strategy is forced through.

**4. The unification argument** (§13.3, "Full-Slack Insertion Lemma is not independently easier —
it is the same content as the aggregated lemma, recursively"). Re-traced the induction-on-`q`
logic by hand: `A_1=B_1`, `A_2=B_2` follow from IH (`FSI(q-1)`, quantified over all backgrounds,
applied to `B_lo` which has size ≤`|B|`) — no new content. The MATCH branch's reverse-inequality
need is **not** covered by `FSI(q-2)` because `FSI` only concerns the *degenerate* split (`s=0`),
while the MATCH branch's own NC-side recursion genuinely needs the *non-degenerate*-split
`TAGGED(·,·,k-1)` — a strictly more general quantity, confirmed by my own decomposition check
above (I had to use the real, nonzero split point `k-1` to get 0/400 mismatches; a trial run using
`s=0` would fail). This is a real, correctly-derived structural finding, not an assertion. No
circularity found in the induction (well-founded on `q`, background size only grows on the branch
that is honestly flagged as still open).

### Verdict: `potential-weighting-upper-bound`

**Status: partial** (matches the file's own self-reported Status — no overclaim). Real progress:
one new certified general lemma, a genuinely closed KEEP branch, and a precise, independently
re-verified diagnosis unifying two previously-separate open lemmas (Full-Slack Insertion, §12.1;
Small-Gap Crossing-Domination, §11.4) into one Core Open Lemma (Match-Recovery Lemma), plus a real
negative result (naive strengthening false, exact counterexamples). The Match-Recovery Lemma
itself remains unproved — the central gap is unchanged in ultimate difficulty but now more sharply
targeted.

**Verdict: CHANGES REQUESTED.** Gap to close next round: prove the Match-Recovery Lemma (§13.3's
boxed statement) — "if the MATCH branch's unrestricted min strictly beats DELETE and KEEP, some
match partner (not necessarily the same one) achieves at least as well under the non-crossing+
split restriction" — for every background `B` and both signs `σ`.

## Approach 2: `concavity-minimax-duality` (§15)

### Claims and independent verification

**1. Refutation of §14.4's mechanism** (§15.1): the `8→4→2→1` chain on `D_3` (three `M`-ops,
budget `m=3`) gives surviving token `v=1`, dominant power `L=3` (from `a_1=8`), naively predicted
bucket `L+1=4`, but actual `bucket(1)=bit_length(0)+1=1`, deviation `-3`.
- Arithmetic re-checked directly: `8-4=4`, `4-2=2`, `2-1=1`; legal (3 ops = budget `m=3`, elements
  drop `4→3→2→1`, matching one `M`-op per step). `bucket(1)=1` by the file's own closed form
  `g^*(t)=bit_length(t-1)+1`. Correct, decisive counterexample to the specific §14.4 mechanism.

**2. Superincreasing Preservation Lemma + Slot-Replacement Corollary** (§15.2).
- Re-derived the induction from scratch (Key Sub-claim: `w=v_a-v_b` exceeds every surviving
  element after position `a`, by the superincreasing inequality at index `a`; four-way exhaustive
  position case split for re-verifying superincreasing-ness). No gap found — every surviving
  position falls in exactly one of the four classes, each correctly handled.
- Independent computation (fresh code, own BFS/enumerator): Superincreasing Preservation — 60
  freshly-generated random non-power-of-2 superincreasing bases, BFS to depth 4, **8527 states, 0
  violations**. Slot-Replacement — 3000 random trials, exact integers, predicted in-place sorted
  list vs. an independent full re-sort, **0 mismatches**.
- **Certified** to `lemmas/superincreasing-preservation-and-slot-replacement.md` (new file).

**3. Value-Order = Dominant-Index-Order Lemma** (§15.3, `D_m`-specific).
- Re-derived the induction (uses Slot-Replacement + the token invariant's disjoint-union rule
  `S(w)=S(x)⊔S(y)` to get `i_0(w)=\min(i_0(x),i_0(y))=i_0(x)` when `x>y`). Correct.
- Independent computation: wrote a fresh token-labeled BFS for `D_m`, `m=1..5`. State counts
  `4,15,62,289,1510` — **matched the file's own figures exactly**. `0` order violations across all
  `1,9,65,460,3358` simultaneously-active token pairs checked, and `0` dominant-index ties (as
  required by the disjoint-support invariant).
- **Certified** to `lemmas/value-order-dominant-index-order.md` (new file).

**4. Reduction of Distinct-Bucket to the Local Claim** (§15.4). Re-traced the case analysis by
hand: prefix (IH), the two new adjacent pairs created at the insertion slot (`(v_{a-1},w)` —
immediate from `w<v_a` and IH; `(w,z)` — this is exactly the open Local Claim), and the
"positions strictly between `a` and `b`, and after `b`" case, which I confirmed relies on the
elementary (and true) fact that removing elements from an already strictly-decreasing sequence
leaves it strictly decreasing on the remaining terms — a genuinely trivial one-line fact, not
hand-waving. The `D`-step of the parent induction (deleting a token from an already-distinct-bucket
set keeps buckets distinct) is not spelled out in §15.4 but is equally trivial and needs no further
justification. **No gap found in the reduction itself** — it is complete modulo the Local Claim.

**5. The Local Claim itself** (§15.4, open): `bucket(x-y) > bucket(z)` for the specific comparison
element `z`. Independently re-implemented the exhaustive check with fresh code (plain value-
multiset BFS, distinct from the builder's token-labeled implementation): `m=0..6`, **13507 total
`M`-transitions checked, 0 violations** — and critically, my `m=6`-alone transition count
(`11535`) matched the file's own reported figure for `m=6` **exactly**, giving strong
corroboration the file's own computation was run correctly, not merely plausible-sounding. Still
genuinely unproved — this is honestly reported as open in the file, not overclaimed.

**6. Negative result** (§15.5): abstract counterexample `(4,3)` — `bucket(4)=bit_length(3)+1=3`,
`bucket(3)=bit_length(2)+1=3`, same bucket, despite `(4,3)` being trivially superincreasing
(`k=2`, no sum constraint). Arithmetic re-checked, correct. This genuinely rules out closing the
Local Claim via generic superincreasing-ness alone, as claimed.

**7. Honest scope note** (§15.6): even a full closure of Distinct-Bucket would only reproduce the
lower bound already established (unconditionally) by `dyadic-cascade-induction`'s round-8
all-cycles-resolution, not provide new leverage on the theorem's actually-open items (upper bound
at general `m`, general `n≥4`). Checked against §14.3's implication (`Distinct-Bucket ⇒
e_{g*}(M)≥⌈k/2⌉≥1`, an alternative 1-Lipschitz-certificate-style lower bound) — accurate, not
overclaimed.

### Verdict: `concavity-minimax-duality`

**Status: partial** (matches the file's own self-reported Status). Real progress: two new
certified general lemmas, one new certified `D_m`-specific lemma, a decisive refutation of the
dispatched §14.4 mechanism, a sharp and *complete* (modulo the Local Claim) reduction of a global
structural claim to one precise local inequality, and a genuine negative result closing off the
most natural route to the Local Claim. The Local Claim itself remains open (computationally
exhaustive through `m=6`, not proved for general `m`).

**Verdict: CHANGES REQUESTED.** Gap to close next round: prove the Local Claim — for `D_m`-
reachable states, whenever an `M`-operation removes `x=v_a>y=v_b` and `z` (the largest surviving
token with value `<v_a`) exists, `bucket(x-y)>bucket(z)`. §15.5 correctly rules out generic
superincreasing-ness as a route; the file's own suggested next step (express `z` via its dominant
index `i_0(z)` using the newly-certified Value-Order = Dominant-Index-Order Lemma, and bound `w`'s
digit-level structure relative to `i_0(z)`) is a reasonable, non-circular lead for the next round.

## Lemma certification summary

Certified this round (all independently re-derived and re-verified with fresh code, 0 mismatches
in every check):
- `lemmas/general-rank-extraction-identity.md` (updated certification header; statement/proof
  already correct).
- `lemmas/superincreasing-preservation-and-slot-replacement.md` (new).
- `lemmas/value-order-dominant-index-order.md` (new).

No lemma candidate was rejected this round — all three proposed-for-certification items held up
under independent adversarial re-derivation and fresh-code re-verification.

## current.md

Updated `results/imo-2026-03/current.md`: added round-9 entries under "Approaches tried" for both
slugs (detailing the independent re-verification performed), added the three new lemmas to
"Current best," sharpened "What remains open" item 2 (Match-Recovery Lemma unification) and added
item 7 (Distinct-Bucket/Local Claim reduction, explicitly scoped as not new leverage). Also flagged
(without independently verifying — out of this round's dispatch scope) `dyadic-cascade-induction`'s
round-9 outliner note claiming item 6 ("general `n≥4`") is stale, as provisional pending next
round's independent check. Overall Status remains `partial` — the theorem as a whole is not solved
(no APPROVE this round; neither build closed the theorem).

## Outcomes recorded

- `potential-weighting-upper-bound`: `advanced` — closed the KEEP branch in full, unified two
  open lemmas into one sharper target, real negative sub-result.
- `concavity-minimax-duality`: `partial` — reduced Distinct-Bucket to one precise open Local
  Claim via two new certified lemmas, still stuck on that Local Claim.

## Summary of independent verification scripts (all in `/tmp/round-9/work/`)

- `verify_rank_extraction.py` — General Rank-Extraction Identity, 3000 trials.
- `verify_decomp_reviewer.py` — `|B|=1` FSI check via from-scratch `OPT`/`TAGGED` brute force.
- `verify_keep_branch.py` — KEEP-branch closed form, 800 checks, `|B|=0..3`.
- `verify_match_and_aggregate.py` — full decomposition (400+400), individual-`k`/match-only/full
  aggregate mismatch rates (500 trials), and the `|B|=0` zero-failure cross-check (800 trials).
- `verify_concavity_lemmas.py` — Superincreasing Preservation, 8527 states.
- `verify_slot_and_order.py` — Slot-Replacement, 3000 trials.
- `verify_token_order.py` — Value-Order = Dominant-Index-Order, token-labeled BFS, `m=1..5`.
- `verify_local_claim_reviewer.py` — Local Claim exhaustive check, `m=0..6`, 13507 transitions.
