## imo-2026-03

**Per explicit dispatch this round: the sole build target is `potential-weighting-upper-bound`,
revised in place (new §19 appended to `results/imo-2026-03/approaches/potential-weighting-upper-
bound.md`). `dyadic-cascade-induction` and `concavity-minimax-duality` remain benched — none of
this round's three explorers produced a genuinely new idea for either, so per the run-state Rules
they are not un-benched. No new slug opened, no split of the shared gap across slugs (CLAUDE.md's
single-gap-trap rule).**

potential-weighting-upper-bound: revise (Gap 1 / Claim A re-planned, §19 appended)
Target: the whole theorem's remaining open direction — the upper bound `c(n)\le 2^n/(2^{n+1}-1)`
for every Liu Bang opening, currently blocked entirely on one inequality (Claim A / "No-Second-
Trigger at every depth of the scope family `\mathcal F`"), whose closure (per the certified
Match-Free-Recovery <=> SAR/RDRC equivalence, §17.4) finishes the upper-bound induction's tight case.
Technique: strong induction on `|W|` within `\mathcal F` (established, §17.5), now sharpened by (i) a
new structural lemma that (conjecturally) eliminates one whole branch of the `|C_{\mathrm{lo}}|`
case split, and (ii) a two-part decomposition of the surviving hard case combining an
already-certified splitting lemma with a crux-corpus-derived extremal-witness proof shape.

Skeleton (unchanged parent structure, §17.5, plus this round's refinement):
  1. Claim A holds on the dominated tail unconditionally — CLOSED (Empty-Background +
     Background-Splitting Lemmas, round 12, certified).
  2. By the certified Background-Splitting Corollary, Claim A's residual content is confined to
     `|C_{\mathrm{lo}}|\in\{1,2\}` at each node — by round-13 reconciliation (§19.2-19.4), IF the new
     No-Gap Lemma (below) holds, `|C_{\mathrm{lo}}|=1` never actually occurs in `\mathcal F`, so the
     residual content is confined to the single case `|C_{\mathrm{lo}}|=2` only.
  3. At `|C_{\mathrm{lo}}|=2`, split Claim A into KEEP-vs-DEL (the "Sum Bound," §19.5(a)) and
     MATCH-vs-{DEL,KEEP} (the hard, still entirely unaddressed direction, §19.5(b)).
  4. Close each half — the outline stops here; both remain open gaps for the builder.

Key lemmas (claim + mechanism):
  - **No-Gap Lemma (new, conjectured, §19.3)** — at the base generator, no element of `Z_1` lies
    strictly between `\min(b_0,d_{k^*})` and `\max(b_0,d_{k^*})` — because `h:=|\{c\in C:c\ge w_1\}|`
    using the certified `\ge`-convention means "`h=1` occurs" is *literally* the same event as "`w_1`
    (itself an element of `Z_1`) lies weakly between `b_0,d_{k^*}`," so ruling this out at every
    element of `Z_1` (not just the current max) kills `|C_{\mathrm{lo}}|=1` at every future node too,
    since DELETE/KEEP-while-`h=0` never changes `C` and only ever shrinks `W` — the inductive step is
    then completely free, and the entire lemma's content collapses to one base-case check, which is
    exactly where `k^*`'s GLOBAL (not just pairwise) argmin-over-`l` property must be invoked (not
    yet done anywhere in the existing reductions) via a Rank-Extraction/Background-Splitting
    comparison of `A_{3,k^*}` against a hypothetical `A_{3,j}` for the offending `z_j`.
  - **Sum Bound (candidate, §19.5(a))** — `w_1\ge\mathrm{OPT}_{+1}(C,\mathrm{rest})+\mathrm{OPT}_{-1}
    (C,\mathrm{rest})` at `\sigma=+1`, because (via the certified Rank-Extraction closed form at
    `h=0`) this is exactly "KEEP `\ge` DEL" — corroborated on genuine `\mathcal F`-nodes but
    decisively refuted as a free-standing (non-provenance) fact, so the proof must use `C=\{b_0,
    d_{k^*}\}`'s specific tie to `Z_0`/the trigger.
  - **Extremal-witness + secondary tie-break + local rewrite (candidate technique, §19.5(b), adapted
    from crux corpus `aimo-0960`/`aimo-0438`/`aimo-0666`)** — assume every optimal witness matches
    `w_1`, pick the one minimizing the matched gap (or maximizing untouched background elements),
    then a local rewrite (computed exactly via the certified Rank-Extraction Identity) contradicts
    either optimality or the tie-break's own extremality — because this is the closest transferable
    "prove some extremal object avoids property X" proof shape found in the corpus, though the exact
    rewrite identity is bespoke and not yet derived.

Open gaps (named, in build-order priority):
  - **Gap 1a** — No-Gap Lemma's base case (highest priority: closes conditionally on nothing else).
  - **Gap 1b / 1b'** — Sum Bound at `\sigma=+1` (already conjectured) and its unformulated `\sigma=-1`
    mirror.
  - **Gap 1c** — MATCH-vs-DEL/KEEP, the central unaddressed hard content; try (i) showing the
    "forced-matching" contradiction hypothesis is vacuous on `\mathcal F` (never once observed to
    occur, `0/417` and reconfirmed this round) via direct construction FIRST — cheaper if it works —
    before (ii) the heavier extremal-rewrite argument.
  - **Gap 1d (fallback only)** — the general, provenance-free `|C_{\mathrm{lo}}|=1` lemma
    (`math-explorer-shallowest-case.md`), needed only if Gap 1a is later refuted at some depth; its
    own circularity risk (MATCH branch regenerates a 2-element background) is flagged, not resolved.

Cases to cover: `\sigma\in\{+1,-1\}` throughout (both occur at `|C_{\mathrm{lo}}|=2`, confirmed
non-vacuous by the round-12 outline-reviewer's own large sweep, unchanged this round); the tie
convention `h:=|\{c\in C:c\ge w_1\}|` (uses `\ge`, not `>`) must be tracked precisely in Gap 1a/1b.

Watch out for:
  - **The reconciliation in §19.2 is conditional, not a proof.** `math-explorer-argmin-construction`'s
    No-Gap fact (`0/2059`, propagated to `0/3623` across depth `\le5`) and
    `math-explorer-shallowest-case`'s "`|C_{\mathrm{lo}}|=1` is a real, reachable case" claim are
    **not actually contradictory in the data** — the latter never tested whether `h=1` arises from
    genuine `\mathcal F`-provenance, it deliberately tested a decoupled, more general statement. Do
    not treat No-Gap as proved; it is a strong, corroborated conjecture whose base case has not been
    attempted by any of this round's explorers (out of scope for scouting).
  - **The circularity flagged by `math-explorer-shallowest-case`** (the `|C_{\mathrm{lo}}|=1` MATCH
    branch regenerates a `|C|=2` background, so its proof may not be independent of the harder case)
    is defused *only if* No-Gap holds and `|C_{\mathrm{lo}}|=1` is truly vacuous in `\mathcal F` — if
    a future adversarial sweep finds a genuine `|C_{\mathrm{lo}}|=1` node, this circularity risk
    becomes live again and must be resolved head-on (e.g., by inducting on a well-founded measure
    such as recursion depth that decreases even when the background's *size* does not, so that the
    `|C_{\mathrm{lo}}|=1` node's MATCH-branch recursive call to a `|C|=2` instance is still a smaller
    instance in the induction's actual measure) — flagged as an open risk for the builder, not solved
    here.
  - Do not conflate the Sign-Determined DEL/KEEP-Suffices conjecture (explorer a, finding 1) with
    Gap 1d's general lemma — the former is a repackaging of Gaps 1b+1c together (once both are
    proved, DEL/KEEP-suffices follows immediately), not a third independent target; a build round
    should not spend effort proving it directly as a separate claim.
  - FSI, averaging (both variants), Hall's/bipartite matching, and the "`\mathcal F` collapses to a
    chain" simplification are all confirmed dead ends this round (re-checked/re-flagged by the
    explorers, no reversal) — do not revisit any of them for Gap 1.

No other approaches are proposed this round (per explicit dispatch: one slug, no split, others
remain benched pending a genuinely new idea).
