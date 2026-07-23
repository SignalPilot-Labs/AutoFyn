## imo-2026-03

### Assigned lens
Direct attack on the half-step lemma (Gap 1c's central remaining piece), using k*'s true
global-argmin property and the top-level trigger, per the round-15/round-24.1 simplified scope
(only TOP-LEVEL F-provenance needed, not recursive argmin-ness at every level).

### Headline finding — a genuine constructive proof STRATEGY found and heavily corroborated
(not yet a full proof; the crux-inspired "extremal witness + secondary tie-break + local rewrite"
shape, requested since round 13 and never previously built, now has a concrete, working candidate)

**Setup used (matches §21.3/§23.1/§24.1 exactly).** Built genuine base generators `(b0,Z0)`:
`A1 = OPT_{+1}({b0}, Z0\{z1})`; `A_{3,l} = OPT_{+1}({b0,d_l}, Z0\{z1,zl})` for every `l`
(`d_l=|z1-zl|`); `M=min_l A_{3,l}`, `k*=argmin`; trigger `M<A1`; `B1={b0,d_{k*}}`,
`Res=Z1=Z0\{z1,z_{k*}}`. Implemented `OPT_sigma(C,W)` directly from its defining recursion
(§13.2: DELETE / KEEP / MATCH-with-any-partner trichotomy, exact `Fraction` arithmetic, memoized)
— not the closed-form KEEP formula, the raw definition, so no risk of inheriting an algebra bug
from the file. Validated the implementation reproduces the file's own worked examples exactly
before trusting it for new claims.

**The half-step, precisely, as tested:** for `u1:=max(Res)`, any partner `uj\in Res\setminus\{u1\}`,
`d:=|u1-uj|`, `X:=Res\setminus\{u1,uj\}`:
```
OPT_{+1}(B1 u {d}, X)  >=  OPT_{+1}(B1, X)
```

**Step 1 (re-confirmation, wider than any prior round).** Re-ran the exact §24.1 check with fully
generic (co-prime-denominator, no artificial duplicates) values at `q=5,6,7`: **0/1297** violations,
and — critically — **0 exact ties** at generic values (every margin strictly positive); ties/exact
equality (margin `=0`) only appear when the instance has genuine duplicate/rational-coincidence
structure (confirmed by rerunning with small-alphabet duplicate-heavy data: `763` tight instances
out of `1297` checks). This is a clean new observation: **strict inequality holds generically, with
equality occurring exactly at duplicate/coincidence configurations** — consistent with (and a useful
diagnostic signature for) a Lemma-P-style cancellation mechanism sitting at the boundary, not a
separate/unrelated failure mode.

**Step 2 (the naive "same-witness" transfer attempt — tried, and FAILS, worth recording as a dead
end).** The most obvious proof attempt: let `xi*` be the optimal selection of `X` achieving
`OPT_{+1}(B1 u {d}, X)` (the LHS optimum), and try to show `OPT_{+1}(B1,X) <= e(B1 u xi*)` directly
via **insertion-monotonicity of `e`** at the multiset `M := B1 u xi*` (i.e. try to show inserting `d`
into `M` cannot decrease `e`). Derived the exact algebraic criterion via the certified **General
Rank-Extraction Identity** (`lemmas/general-rank-extraction-identity.md`): writing `h := #{m in M :
m>d}$ and `tail_d := \{m in M: m<=d\}`,
```
e(M u {d}) - e(M) = (-1)^h * (d - 2*e(tail_d))
```
(derived from two applications of Rank-Extraction, one for `e(M)` via block extraction at rank
`h+1`, one for `e(M u {d})` directly — a clean, reusable identity in its own right, worth recording
even though the attempt built on it fails). **Tested this specific criterion at `M = B1 u xi*`
(`xi*` = the LHS's own optimal selection): FAILS in a substantial fraction of triggered instances**
(concrete counterexample family found, e.g. `b0=239, Z0=(734/7,487/7,553/11,265/11,13/7)` — see
`/tmp/round-16/work/reduction.py` output). So the "same selection, just drop `d`" witness transfer
is **not** a valid proof mechanism, even though the parent half-step claim is true — confirms the
claim is genuinely non-trivial (not a one-liner), consistent with 3 prior rounds' difficulty.

**Step 3 (the working construction — extremal witness + secondary tie-break + local rewrite,
finally instantiated for this problem).** Instead of reusing `xi*` verbatim, apply exactly the
crux-inspired shape flagged since round 13 (aimo-0960/aimo-0438/aimo-0666): take the LHS-optimal
witness `xi*` (the *extremal witness*), pick out its element **closest to `d`** (the *secondary
tie-break criterion*: `c := argmin_{x in xi*} |x-d|`), then **locally rewrite** by dropping `c` from
the selection (realizable as an actual selection of `X`: if `c` came from a KEEP, delete that one
`X`-element instead; if `c` came from a MATCH of two `X`-elements, delete both of them instead of
matching). **Conjecture (new this round): `e(B1 u (xi* \ {c})) <= OPT_{+1}(B1 u {d}, X)` always** —
i.e. "drop the LHS-witness element nearest to `d`" gives a valid `X`-selection whose value already
beats (or ties) the LHS optimum, which combined with the trivial fact
`OPT_{+1}(B1,X) <= e(B1 u (xi*\{c}))` (any realizable selection upper-bounds the true optimum)
**directly proves the half-step lemma in 3 lines, given this one construction lemma.**

**Computational status of Step 3's construction lemma: strong, zero counterexamples across several
independently-varied batteries, min margin exactly `0` (tight, never negative):**
- Generic-value sweep (`q=5,6,7,8`, mixed integer/rational, `vmax` up to `997`): `511` checks, `0`
  failures (`/tmp/round-16/work/reduction3.py`).
- Small/duplicate-heavy sweep (`q<=7`, values drawn from small pools of size `3-5`, designed to
  maximize ties/duplicates — the regime where the naive Step-2 mechanism is least trustworthy):
  `408` checks, `0` failures (`/tmp/round-16/work/reduction4.py`).
- Original mixed sweep: `348` checks, `0` failures, plus an explicit **exists-some-single-drop**
  check confirming the "drop nearest" choice specifically (not just "some drop exists") is what
  works (`/tmp/round-16/work/reduction2.py`).
- **Combined: ~1,267 checks across 3 independently-coded batteries, 0 violations, min margin `=0`.**
  This is a smaller sample than some other lemmas' corroboration in this population (time budget),
  but it is a genuinely new, previously-untested construction, not a re-run of an old one, and the
  three batteries were deliberately designed to stress different regimes (generic/large-scale,
  small-duplicate-heavy, and an exhaustive "does any single-drop work" check ruling out that the
  "nearest" choice is a coincidence rather than the mechanism).

**What remains to actually PROVE Step 3's construction lemma (not done this round — this is exactly
where a builder should start).** The natural approach is the same Rank-Extraction machinery from
Step 2, applied differently: since `c` is chosen to be *closest* to `d` (not just any element of
`xi*`), the pair `(c,d)` should admit a bound via the same insertion identity, but now comparing
`e(B1 u (xi*\{c}) u {d})` (a valid re-arrangement of the SAME multiset as `B1 u {d} u xi*`, just with
`c` "extracted" instead of `d`) to `e(B1 u (xi*\{c}))` — i.e. this is again a single-element
insertion identity (insert `d` into `M' := B1 u (xi*\{c})`), and now the "closest" choice of `c`
should be exactly what controls `tail_d`'s value in the Step-2 criterion favorably. This looks like
a genuinely tractable algebra exercise (not a new search), flagged as the concrete next step, not
attempted further per my scouting role.

### Distinct openings
1. **(Primary, new this round) The nearest-neighbor local-rewrite construction (Step 3 above)** —
   a concrete, previously-untried instantiation of the crux-inspired proof shape, strongly
   corroborated, with a clear residual algebraic obligation (one more Rank-Extraction-style
   computation, not a fresh search).
2. The already-flagged (round 15) suspected link to Gap 1a's generalized `A1`-bound family — this
   round's sibling explorer (`math-explorer-gap1a-A1bound.md`) found the analogous `|C|=1`
   "Two-Touch" mechanism does NOT transfer to `|C|=2` (24% failure rate) — confirms the half-step
   (which lives at `|C|=2`, `C=B1`) genuinely needs its own argument, not a borrowed `|C|=1` trick.
   This is consistent with, not contradicting, the new Step-3 finding above (Step 3 is not a
   Two-Touch-style closed form, it's a witness-transfer argument, a structurally different
   mechanism).
3. The Step-2 insertion-monotonicity identity (`e(M u {d}) - e(M) = (-1)^h(d-2e(tail_d))`) is a
   clean, general, reusable fact in its own right (no `F`-provenance needed) even though the naive
   application fails — worth recording as a lemma candidate independent of whether Step 3 closes.

### Candidate technique(s)
- Rank-Extraction-based algebraic proof of Step 3's nearest-neighbor construction lemma (see "what
  remains" above) — the recommended concrete next attempt.
- If Step 3 resists a direct algebraic proof, consider strong induction on `|X|` (as §17.5's overall
  skeleton suggests) with Step 3's construction as the inductive step's core witness-transfer tool.

### Cheap-kill candidates
- Do NOT re-attempt the "same-selection, just drop `d`" transfer (Step 2) as a proof mechanism — it
  is confirmed FALSE as a general argument (concrete counterexamples found this round), even though
  the parent claim holds; a proof must use the *nearest-neighbor* rewrite (Step 3) or something
  equally non-trivial, not naive reuse of `xi*`.
- The `|C|=1` Two-Touch characterization (sibling report) does not transfer to this `|C|=2` setting
  — do not attempt to reuse it verbatim for the half-step.

### Knowledge-base entries to use
- `lemmas/general-rank-extraction-identity.md` — directly used (twice: once to derive the Step-2
  insertion-difference identity, and it is the natural tool for Step 3's residual proof obligation).
- `lemmas/shrink-list-monotonicity.md` — used implicitly to confirm `xi*\{c}` remains realizable
  and that trivial upper/lower-bound directions are as expected.
- `lemmas/duplicate-pair-invariance.md` (Lemma P) — explains the observed "equality only at
  duplicate/coincidence configurations" signature (Step 1).
- `lemmas/background-release-domination.md` and `lemmas/three-bound-domination-and-keep-top-bound.md`
  — checked as candidate chaining tools (Background-Release chaining, per round 15's already-dead
  routes) but not used in the working Step-3 mechanism; consistent with round 15's finding that
  those two chaining routes don't close this gap.

### Analogous past problems (cruxes)
Per the dispatch, the relevant crux SHAPE (not a subject-matter match) remains
"extremal witness + secondary tie-break + local rewrite" from `aimo-0960`, `aimo-0438`, `aimo-0666`
(already identified in round 13, recorded in `potential-weighting-upper-bound.md` §19.3). This
round is the first to actually **instantiate** that shape concretely for this problem (extremal
witness = `xi*`, secondary tie-break = "closest to `d`", local rewrite = "drop it") rather than just
flagging it as a recommended technique — see Step 3 above. No new crux match found beyond this
(re-confirms round 13's/round-16-sibling's assessment that no closer subject-matter analog exists
in the corpus for this bespoke background-carrying alternating-sum recursion).

### Prior progress
`potential-weighting-upper-bound.md` §21.3/§23.1/§24.1: half-step lemma's hypothesis simplified to
top-level-only F-provenance (round 15, independently reproduced 3x); half-step itself unproved
before this round, corroborated `0/15,175`+ violations across rounds 15-16 but with no working
proof strategy on file. **This round's new content: the naive transfer mechanism is now known to
FAIL (a real negative result, not previously on file), and a working (though still unproved)
replacement construction — the nearest-neighbor local rewrite — is now identified and corroborated
across ~1,267 fresh checks with 0 violations.**

### Dead ends (do not retry)
- Step 2's "same-selection, drop `d`" witness transfer — confirmed FALSE this round as a proof
  mechanism (concrete counterexamples in `/tmp/round-16/work/reduction.py` output), even though the
  parent half-step claim holds. Any future attempt at a direct proof must not rely on reusing `xi*`
  unmodified.
- (Reconfirmed from round 15, §23.2) Full telescoping of Background-Release Domination to a
  background-free bound, and single-release direct chaining against `A1` — both still dead, not
  revisited this round, no new evidence either way.

### Small-case / intuition notes (all conjectural, computational evidence only, not proofs)
- The half-step lemma's equality set (margin `=0`) appears to coincide exactly with instances
  containing duplicate/rational-coincidence structure (Lemma-P-style); generic (algebraically
  independent) values give strict inequality every time, `0/1297` in this round's dedicated check —
  a useful signature for anyone attempting a case-split proof (generic case vs. duplicate case).
- The nearest-neighbor local-rewrite construction (Step 3) is conjectured to hold unconditionally
  within the (simplified, top-level-only) `F`-provenance scope, based on ~1,267 zero-violation
  checks across three independently-designed batteries (generic-large, duplicate-heavy, and an
  explicit "does any single-drop work" exhaustiveness check) — not yet proved, but the strongest,
  most concrete lead on this gap to date, and a genuine (not cosmetic) instantiation of the
  previously-only-recommended crux proof shape.
