# Round 14 proof-reviewer report — imo-2026-03

## Scope of this review
Reviewed `results/imo-2026-03/approaches/potential-weighting-upper-bound.md` §19-§22 (round 14
outliner revision §21 + round 14 build §22), the new candidate lemma
`results/imo-2026-03/lemmas/shrink-list-monotonicity.md`, `results/imo-2026-03/current.md`, and the
prerequisite certified lemmas it cites (`general-rank-extraction-identity.md`,
`empty-background-and-background-splitting.md`). All claims re-derived and re-checked with fresh,
independently-written code (`/tmp/round-14/verify/mydefs.py` + 5 test scripts — not reused from the
builder's `/tmp/round-14/work/`, the outliner's, or any explorer's harness).

## 1. Shrink-List Monotonicity Lemma — VERDICT: CORRECT, CERTIFY

**Statement.** For any background multiset `C`, list `W`, `x\in W`:
`OPT_{+1}(C,W) \le OPT_{+1}(C,W\setminus\{x\})` (mirrored `\ge` at `\sigma=-1`), with `OPT_\sigma`
as defined in §13.2 (sigma-optimum of `e(C\cup K\text{-values}\cup M\text{-differences})` over all
Keep/Delete/Match selections of `W`, deleted elements contributing `0`).

**Independent re-derivation.** The proof is a one-line bijection: take a `W\setminus\{x\}`-optimal
selection, extend it by additionally deleting `x` (contributes `0` by the standing convention I
independently confirmed matches §13.2's own definition — the value fed to `e` is exactly
`C\cup K\text{-values}\cup M\text{-differences}`, with deleted elements simply absent). This extension
is a valid, not-necessarily-optimal member of `W`'s own search space with the identical value, so the
true optimum over the bigger space is at least as good in the appropriate direction. No hypothesis
on `C,W,x` is used anywhere — I confirmed this by direct re-derivation, not by reading the file's
proof and nodding along.

**Fresh computational check** (own harness, `Fraction`-exact, full brute-force enumeration of all
Keep/Delete/Match selections — not sampled DP): `800/800` trials (both signs, `|W|\le5`, arbitrary
`|C|\le3`, random rational values including half-integers), `0` violations. Independently reproduced
the file's own worked example (`C=\{5,8\},W=(10,8,7,2)`: `OPT_{+1}=0`) exactly, confirming my harness
matches the population's established convention before trusting any new result built on it.

**Verdict: certified.** Updated `lemmas/shrink-list-monotonicity.md`'s Status line from "proposed for
certification" to "CERTIFIED", recording this round's independent re-verification.

## 2. Per-Partner Domination Lemma — VERDICT: q<=3 proof is CORRECT and COMPLETE; q>=4 correctly left open

**Statement tested.** For a base-generator instance (`B_0=\{b_0\}`, sorted `Z_0=(z_1\ge\dots\ge z_q)`,
`A_1:=OPT_{+1}(\{b_0\},Z_0\setminus\{z_1\})`, and for every `l\in\{2,\dots,q\}`,
`d_l:=z_1-z_l`, `D_l:=|b_0-d_l|`, `A_{3,l}:=OPT_{+1}(\{b_0,d_l\},Z_0\setminus\{z_1,z_l\})`):
`A_{3,l}\ge\min(A_1,D_l)`, with **no** trigger hypothesis and **no** requirement that `l` be an argmin.

### (a) Is the q<=3 proof actually complete and correct, no hidden case gaps?

**q=2 base case.** Trivial (`Z_0\setminus\{z_1,z_2\}=\emptyset`, so `A_{3,2}=D_2` exactly, and
`\min(A_1,D_2)\le D_2` always). Correct, no issue.

**q=3 case (every l).** I independently re-derived the ENTIRE case analysis from scratch, symbolically
(`/tmp/round-14/verify/symbolic_q3.py`), before reading the builder's own algebra line-by-line, then
cross-checked:
- Re-derived the 3-case Rank-Extraction split for `keepval:=e(\{b_0,d_l,w\})` (`w` = the one residual
  element) by hand for all 6 sub-orderings (Case A: `d_l\ge\max(b_0,w)`; Case B: `d_l` strictly
  between; Case C: `d_l\le\min(b_0,w)`) — my independent hand/sympy derivation matches the file's
  claimed closed form (`d_l-|b_0-w|`, `b_0+w-d_l`, `|b_0-w|+d_l` respectively) exactly in every
  sub-ordering.
- Re-derived the two free bounds `A_1\le b_0` (delete both residual elements — an instance of the
  Shrink-List Corollary) and `A_1\le|b_0-w|` (delete `z_l`, keep `w` — a single valid candidate) —
  both trivially correct as bounds on a minimum over a search space containing these candidates.
- Re-derived, independently, that in EVERY sub-ordering of every case, either `keepval\ge A_1` (closing
  via monotonicity of `x\mapsto\min(D_l,x)`) or `keepval\ge D_l` (closing trivially, regardless of
  `A_1`, since `\min(A_1,D_l)\le D_l` always) — no sub-ordering is left uncovered. I explicitly
  re-verified each of the 6 branches (Case A/{w>=b0,w<b0}, Case B/{w>=b0,w<b0}, Case C collapses to one
  argument covering both sub-orderings) algebraically myself, not merely re-stating the file's claims.
- **No hidden case, no skipped sub-ordering, no circularity.** Everything used is either elementary
  algebra, the certified General Rank-Extraction Identity, or the certified Shrink-List Corollary.

**Verdict on (a): the q<=3 proof is genuinely complete and correct.** This is a real, non-conjectural,
fully rigorous elementary result — the first complete unconditional closure of any nontrivial instance
of the central remaining mechanism in this population's history on this gap.

**The "caught-and-fixed false start" claim — confirmed sound.** The file records that an earlier pass
used only the weaker bound `A_1\le|b_0-w|` throughout Case A and got stuck on a spurious "unclosed"
sub-case (`z_3>2b_0`). I independently checked: in the `w\ge b_0` sub-case of Case A, `keepval=
b_0+(d_l-w)`, and using only `A_1\le|b_0-w|=w-b_0` does NOT suffice in general (I constructed the
scenario `b_0=0,w=5,d_l=5`: `keepval=0`, and the weak bound only gives `A_1\le5`, insufficient to
conclude `keepval\ge A_1`). Switching to the sharper bound `A_1\le b_0` (using `d_l\ge w` from Case A's
own defining condition, so `keepval=b_0+(d_l-w)\ge b_0\ge A_1`) closes it immediately, exactly as the
file describes. **The fix is genuinely sound, independently re-derived from scratch, not merely
trusted from the prose.**

**Fresh computational corroboration** (own harness, brute-force `OPT`, `Fraction`-exact):
- Random sweep `q\in\{2,\dots,5\}`: `7,476` per-`l` checks, `0` violations.
- **Exhaustive** (not sampled) sweep `q=4`, half-integer alphabet `\{0,\dots,4\}` step `1/2`: `59,049`
  instances, `177,147` checks, `0` violations.
- **Exhaustive** sweep `q=5`, integer alphabet `\{0,\dots,4\}`: `15,625` instances, `62,500` checks,
  `0` violations.
These exceed the builder's own tested ranges (`q=4`: `3,100` random-ish; here fully exhaustive at a
comparable alphabet size) per the round-13 lesson about widening past a builder's own harness cap
before trusting a "clean" margin/conjecture — still zero violations, consistent with (not proof of)
the open `q\ge4` conjecture.

### (b) Does it genuinely imply Deletion-Suffices-for-`k^*`, and thus Gap 1a's 3-line closure, at least for q<=3?

**Yes, independently re-derived.** Given the trigger `M<A_1` at a specific index `l=k^*` (with
`M:=A_{3,k^*}` by definition — this does *not* require `k^*` to be a global argmin over other `l`,
only that we are examining this particular index), apply Per-Partner Domination at `l=k^*`:
`M=A_{3,k^*}\ge\min(A_1,D_{k^*})`. If this minimum were `A_1`, we'd get `M\ge A_1`, contradicting the
trigger — so the minimum must be `D_{k^*}`, giving `M\ge D_{k^*}`. Combined with the free (unconditional)
bound `M\le D_{k^*}` from the Shrink-List Corollary (`M=OPT_{+1}(\{b_0,d_{k^*}\},Z_1)\le
e(\{b_0,d_{k^*}\})=D_{k^*}`), this forces `M=D_{k^*}` exactly. I re-derived this chain from scratch and
found no gap — and confirmed it is **strictly simpler** than either of §21.1's original two routes
(neither of which succeeded), since it never invokes `k^*`'s *global* argmin property, only the
trigger at that one index.

Since Per-Partner Domination is now proved unconditionally for `q\le3`, this **does** give a genuine,
complete, unconditional proof of Deletion-Suffices-for-`k^*` whenever the base-generator instance has
`q=|Z_0|\le3` — a real special-case closure of Gap 1a, confirmed end-to-end by an independent fresh
base-generator harness (`test_delsuffices_q3.py`, not reusing the builder's `base_gen.py`): `6,942`
genuine triggered instances at `q\in\{2,3\}`, `M=D_{k^*}` exactly in **all** of them, `0` mismatches.
(For reference, I also ran the still-open `q\in\{4,5\}` regime: `754` triggered instances, also `0`
mismatches — consistent with, but not a proof of, the general conjecture.)

**It does NOT close Gap 1a in general** — base-generator instances can have arbitrary `q`, and the
theorem needs the general case. This matches the file's own honest self-assessment exactly.

### (c) Is the q>=4 gap honestly and precisely characterized, not silently assumed elsewhere?

**Yes.** I grepped the entire approach file for any claim that Gap 1a, Deletion-Suffices, or the
Per-Partner Domination Lemma is closed "in general" or unconditionally, and found none — the one place
the strongest language appears (§22's own section header: "found and corroborated that (if proved)
closes Gap 1a...") is explicitly conditional ("if proved"). The Status section (top of file) and §22's
own "Honest assessment" both explicitly and correctly state: `q\le3` proved, `q\ge4` open, "Gap 1a is
NOT fully closed this round... Status stays `partial`." The `|B_0|=0` (empty background) case, which
might otherwise seem like an unaddressed edge case for this `b_0`-scalar-notation lemma, is not a
silent gap either — it is already handled unconditionally by the pre-existing, independently-certified
Empty-Background Lemma (`lemmas/empty-background-and-background-splitting.md`, round 12), which the
population already established resolves `B_0=\emptyset` directly without needing any trigger/argmin
machinery at all (and a separately-certified structural fact shows `B_0=\emptyset` never even
triggers in the first place). No overclaim found anywhere in §21/§22 relating to this round's new
content.

## Overall verdict for `potential-weighting-upper-bound` (round 14)

**Status: partial** (matches the file's own self-reported Status — no downgrade or upgrade needed).
Real, substantial, precisely-bounded progress this round:
1. A new general-purpose lemma (Shrink-List Monotonicity) proved and certified in full, no scope
   restriction.
2. A new, strictly more general "Per-Partner Domination Lemma" found, that (a) implies
   Deletion-Suffices-for-`k^*` in three lines without needing `k^*`'s global-argmin-ness (a genuine
   simplification over every route tried in rounds 13 and earlier), and (b) is now **fully and
   rigorously proved** for the `q\le2,3` sub-case — the first complete, unconditional closure of any
   nontrivial instance of the central remaining Gap-1a mechanism produced by any round to date.
3. The general-`q` case (what the theorem actually needs) remains open, correctly and precisely
   flagged, not silently assumed anywhere else in the file.
4. The self-reported "caught-and-fixed false start" is a genuine, correctly-diagnosed-and-fixed issue,
   independently re-confirmed from scratch.

No error, missing case, circularity, or overclaim found anywhere in the reviewed material. This is
real forward motion on the single remaining bottleneck (Gap 1a of the upper-bound direction), though
the theorem as a whole remains unsolved — the general-`q` Per-Partner Domination Lemma, Gap 1b (Sum
Bound), and Gap 1c (half-step lemma) are all still open.

**Verdict: CHANGES REQUESTED** for `potential-weighting-upper-bound` (partial, real progress, no
RETHINK — the approach and its current mechanism are sound and should continue; the next concrete
target is the general-`q` induction for Per-Partner Domination, per the file's own §22 "Recommended
next steps," ideally checking the suspected — untested — link to Gap 1c's half-step lemma first,
since a positive answer there would unify two of the three remaining named gaps).

## current.md updates made
- Added a new "Approaches tried" entry (top of list) for this round's findings, matching the
  established file format.
- Added a "Shrink-List Monotonicity Lemma + Corollary" bullet to "Current best"'s certified-lemma
  list.
- Appended a "Round 14's net effect" paragraph to item 2 of "What remains open," describing the
  Per-Partner Domination Lemma's q<=3 closure and q>=4 open status.
- Status field left unchanged: `partial`.

## Lemma certification
- **`lemmas/shrink-list-monotonicity.md` — CERTIFIED** (Status line updated in place). Fully general,
  no `\mathcal F`-restriction, one-line proof, independently re-verified (see §1 above).
- The Per-Partner Domination Lemma itself is NOT yet promotable to `lemmas/` as a standalone file —
  it is only proved for `q\le3`, not in full generality, so it remains inside
  `potential-weighting-upper-bound.md` §22.2 as approach-local content, not a certified shared lemma
  (consistent with the file's own recommendation — it did not propose this for standalone
  certification, only Shrink-List Monotonicity).

## Ranking
Called `mcp__approach-ranker__record_outcome` for `potential-weighting-upper-bound`, round 14,
outcome `advanced` (real progress: a new certified general lemma plus a complete, non-conjectural
proof of a genuinely new, more general lemma for a real sub-case of the central remaining gap).

## Notes for next round
- **Recommended next attack (per the file's own §22, independently endorsed by this review):**
  extend the Per-Partner Domination Lemma from `q\le3` to general `q` via induction on `q`, peeling
  the top element of the residual list `Res:=Z_0\setminus\{z_1,z_l\}` via the certified Generalized
  Multi-Background Peeling Lemma's DELETE/KEEP/MATCH trichotomy, using the `q-1` case as IH; the new
  MATCH branch (absent at `q=3`, where the residual list is a singleton) is the one genuinely new
  sub-case to handle.
- **Check the suspected (untested) link between this induction and Gap 1c's half-step lemma before
  committing significant effort to either in isolation** — §22's own closing observation notes both
  reduce, in their general form, to a "does adding a background element `d` help a `\sigma=+1`
  minimizer" question of the same shape; a positive answer would unify two of the three remaining
  named gaps (1a's general-`q` case and 1c's half-step lemma) into one shared hard core. This is a
  cheap, concrete, single-instance check recommended as the very next step.
- Gaps 1b (Sum Bound, sharper "zero uniform additive slack" diagnosis this round) and 1c's half-step
  lemma were not attacked this round (all builder time went into Per-Partner Domination) — still open,
  unchanged in substance from round 13/14's outline.
