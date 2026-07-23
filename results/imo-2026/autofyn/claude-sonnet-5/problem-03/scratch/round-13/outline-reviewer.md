## imo-2026-03 — round 13 outline review

Reviewed: `potential-weighting-upper-bound.md` §19 (Round-13 outliner revision, appended after
§17–18), the three round-13 explorer reports, `current.md`, and the certified
`lemmas/empty-background-and-background-splitting.md`. Only one slug is on the table this round
(sole build target per explicit dispatch); `dyadic-cascade-induction` and
`concavity-minimax-duality` remain benched.

### Independent re-verification (fresh code, `/tmp/round-13/reviewer-work/`, not reusing any
explorer's or builder's harness)

Built `defs.py` (own `e()`, own recursive `selections()` generator, own `OPT_sigma`/`OPT_KD_sigma`
brute force) and validated it bit-for-bit against the file's own three worked examples before
trusting it: `OPT_{+1}([5,8],(10,8,7,2))=0`/`OPT_KD=2`; `OPT_{+1}([1],(10,8,7))=0`/`OPT_KD=1`;
`OPT_{-1}([2,4],(5,3))=4` — all matched exactly.

**1. No-Gap consequence ("h never equals 1 at genuine F-provenance nodes").** Wrote my own
`base_gen.py` implementing the actual base-generator construction from scratch (real trigger
`M<A_1`, real global-argmin `k^*` over `A_{3,l}`, `B_1:=B_0\cup\{d_{k^*}\}`, `Z_1`), independent of
the explorers' `defs.py`/`gen_F.py`. Random sweep (3000 configs, small-and-large value ranges,
`|B_0|\in\{0,1\}$): `604` triggered nodes checked, `h==1` count `0`, No-Gap (strict betweenness)
violations `0`. A second, deliberately tie-heavy sweep (`vmax\in\{1,2,3,4\}`, `20000` configs):
`3955` nodes, `0`/`0` again. An **exhaustive** (not sampled) sweep, `q\in\{3,4,5\}`, values in
`{0,1,2,3}`, every `B_0\in\{\emptyset,0,1,2,3\}`: `70` triggered instances, `155` nodes, `0`/`0`/`0`
ties. Extended the walk through DELETE/KEEP closure to depth 4 (own `closure_walk.py`): background
size/`h` pairs observed were exactly `(0,0)`, `(2,0)`, `(2,2)` — **never** `(2,1)` or any size-1
background, across `600` base-generator instances. This independently corroborates both the
No-Gap fact and its "`|C|` stays `\{0,2\}`, never `1`" consequence from scratch.

**2. The tie/boundary subtlety — a real, previously-unflagged logical gap in §19.3's literal
statement, worth surfacing to the builder even though my own search didn't break it.** §19.2's
reconciliation argument requires ruling out `h=1`, which (per the certified `\ge`/`<` convention)
occurs exactly when `w_1` lies **weakly** between `\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})` —
i.e. including the boundary case `w_1=\min(\cdot)` or `w_1=\max(\cdot)$ exactly. But §19.3's
**Conjectured Lemma is stated with "lies strictly between"** (open interval). A lemma proved
exactly as literally worded would **not** by itself rule out the tie/boundary case, so `h=1` could
in principle still occur via `w_1$ exactly equal to `b_0` or `d_{k^*}`, even if the strict-interior
statement is fully proved. I specifically hunted for this: a targeted hill-climb
(`hillclimb_tie.py`, 40 random restarts, 300 perturbation steps each, `q=6`, explicitly minimizing
`\min(|w_1-\min(B_1)|,|w_1-\max(B_1)|)` toward `0`) found a best-ever gap of exactly `1`, **never
`0`**, across the whole search — real (if informal) corroboration that ties don't occur, but this
is not proved, and no report (builder's or any of the three explorers') addresses it. **Action for
the builder:** either strengthen Gap 1a's target to the closed interval (`w_1\notin[\min,\max]`
unless it equals an endpoint that's still excluded by a separate tie-exclusion argument) or prove
ties are impossible as an explicit corollary before treating "No-Gap disproved via strict
betweenness" as sufficient to kill the `|C_{\mathrm{lo}}|=1` branch. This is a fixable
precision gap, not a fatal one (my own fresh adversarial search corroborates the needed stronger
statement, it just isn't what's literally written).

**3. Sum Bound (§19.5(a), Gap 1b).** Reproduced with my own harness restricted to genuine
non-dominated (`\sigma=+1`) base-generator nodes: `105/105`, `0` violations — corroborates the
builder's own `112/112`.

**4. Claim A / Match-Free Recovery directly, at deeper `\mathcal F` nodes (not just the base
generator).** Walked DELETE/KEEP closure to depth 3 from `300` fresh base-generator triggers
(`532` total nodes, own harness, own closure implementation using the file's own `h`/`C_{lo}$
conventions for the two closure rules): `0` violations of `\mathrm{OPT}_\sigma=\mathrm{OPT\_KD}_\sigma`
— consistent with everything on file and with rounds 9–12's much larger sweeps. No new
counterexample found anywhere.

### Assessment of the two dual `h`-conventions

§17.2's own `\mathcal F`-generation KEEP-closure rule uses `h:=|\{c\in C:c>w_1\}|$ (strict) /
`C_{\mathrm{lo}}:=\{c\le w_1\}`, while the certified Background-Splitting Lemma (used to *analyze*
Claim A at a given node) uses `h:=|\{c\ge w_{\max}\}|$ (weak) / `C_{\mathrm{lo}}:=\{c<w_{\max}\}`.
These are **different conventions for different purposes**, and I verified they coincide exactly
in the regime that matters (both background elements strictly below `w_1`, i.e. no ties) — my
`closure_walk.py` uses the §17.2 convention to build `\mathcal F`'s closure and confirms `C`'s
invariance is exactly as claimed. This is fine as used, but it is genuinely easy to mix up (two `h`
symbols, two conventions, in the same file) — flagging this as a documentation risk the builder
should keep straight, not a substantive error.

### Well-posedness / dead-end / single-gap-trap check

- **One whole attempt, not a fragment.** §19 is a revision-in-place of `potential-weighting-
  upper-bound` targeting the theorem's actual remaining direction (the upper bound, via the
  now-standard Claim-A reduction); no split across slugs. Consistent with CLAUDE.md.
- **No repeated dead end.** FSI, both averaging variants, Hall's/bipartite framing, and the
  "`\mathcal F` collapses to a chain" simplification are all correctly *not* revisited (the
  crux-search explorer explicitly re-confirmed the chain-collapse idea is false and flagged it as
  a dead end this round — good hygiene, not a regression).
- **The circularity concern is correctly scoped as conditional, not resolved.** §19.2/§19.6 (Gap
  1d) honestly keep the general (non-`\mathcal F`) `|C_{\mathrm{lo}}|=1` lemma as an explicit
  fallback rather than quietly assuming it's unnecessary — correct, not an overclaim.
- **Gaps 1a–1d are precisely stated** (each with a named target, a named mechanism/tool, and a
  build-order priority) — well-posed for a builder, modulo the point-2 precision fix above.
- **Diversity check.** `dyadic-cascade-induction` (fully closed its own milestone, round 8) and
  `concavity-minimax-duality` (open Local Claim, no new leverage on the theorem's actually-open
  items even if closed) remain benched — correctly, since none of this round's three explorers
  targeted either and none surfaced a new idea for them. No new plateau signal beyond what's
  already on record (Gap 1/Claim A has now been the sole open front for 5+ rounds — worth a fresh,
  genuinely different framing from a future explorer if round 14 stalls again on Gap 1c, but this
  round's narrowing (No-Gap eliminating a whole branch) is real forward progress, not another lap
  on the same wall).

### Verdict

**`potential-weighting-upper-bound` (§19 revision): CHANGES REQUESTED.**

The technique (strong induction on `|W|` within `\mathcal F`, now sharpened by the No-Gap
elimination of the `|C_{\mathrm{lo}}|=1` branch and the two-part KEEP-vs-DEL / MATCH-vs-DEL/KEEP
split at `|C_{\mathrm{lo}}|=2`) is sound and well-motivated; no circular reasoning, no repeated
dead end, no missing case in the case split as stated (both signs `\sigma=\pm1` are correctly
tracked). Specific fixes needed before/while building:
1. **Gap 1a's literal statement is under-strength** (strict betweenness does not, on its face,
   rule out the tie/boundary case that also produces `h=1`) — restate to cover the closed
   interval, or add an explicit tie-exclusion corollary, before treating it as closing the whole
   `|C_{\mathrm{lo}}|=1` branch. (New finding this round, independently corroborated but not
   fatal — my own targeted adversarial search found no tie, best gap `1`, never `0`.)
2. Gap 1b' (`\sigma=-1` mirror of the Sum Bound) is correctly flagged as unformulated — cheap,
   do in parallel with 1b, no change needed to the plan.
3. Keep the two `h`-conventions (§17.2's strict vs. the certified Background-Splitting's weak)
   explicit and separately labeled in any write-up — a clarity risk, not a soundness one, given my
   check that they coincide in the tie-free regime.

None of these are fatal to the approach; they are exactly the kind of fixable gap CHANGES REQUESTED
is for. Proceed with the build in the stated order (1a → 1b/1b' → 1c(i) then 1c(ii) → 1d fallback
only if 1a fails), with the builder explicitly addressing point 1 as part of closing Gap 1a.

### Ranking

Only `potential-weighting-upper-bound` was built/revised this round; the other two live approaches
were not touched (no new explorer targeted them). Clearing `potential-weighting-upper-bound`'s
`stale` flag against the established field, anchored to prior-round evidence already on record:
`dyadic-cascade-induction` already delivered a fully-closed, reviewer-verified milestone (the
unconditional lower bound against `D_m`, every `m`) and remains the strongest approach in the
population; `potential-weighting-upper-bound` continues to make real, well-verified incremental
progress on the sole remaining open front (this round: one whole branch of the case split
conjecturally eliminated, two lemmas corroborated) but the central inequality is still open, so it
ranks below `dyadic-cascade-induction`; `concavity-minimax-duality`'s open Local Claim, even if
closed, would not provide new leverage on the theorem's actually-open items (its own file's honest
scope note), so it ranks below `potential-weighting-upper-bound`. No new slug registered (a
revision keeps its existing slug); no copy warranted (no branch point proposed this round).

Comparisons submitted:
- `dyadic-cascade-induction` beats `potential-weighting-upper-bound` (closed milestone vs. still-open
  central gap).
- `potential-weighting-upper-bound` beats `concavity-minimax-duality` (concrete, provenance-tied
  narrowing of the theorem's actually-open direction vs. an open Local Claim that wouldn't add new
  leverage even if closed).
- `dyadic-cascade-induction` beats `concavity-minimax-duality` (same reasoning, transitively
  consistent with prior rounds' ordering).

build set: potential-weighting-upper-bound
