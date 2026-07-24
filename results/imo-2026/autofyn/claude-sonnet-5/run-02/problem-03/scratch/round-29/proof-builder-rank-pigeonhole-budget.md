# Build report — rank-pigeonhole-budget, round 29

## Task
Close (as much as possible of) the 6-shape residual of $(\star_3)=
\mathrm{MinFloor}(4)$ left open by round 28: shapes $(1,1,0,1),(1,1,1,0),
(1,2,0,0),(2,0,0,1),(2,0,1,0),(2,1,0,0)$, while fixing the outline-
reviewer's flagged citation-mismatch bug (round-29 outline proposed
misapplying `single-insert-point-vertex-lemma`, proved only for a single
free coordinate against a fixed rest, to mass-conserving coupled
coordinate pairs like $(f_1,f_2,f_3)$ summing to $\pi_1$ — the true slope
there is $\pm2$, not $\pm1$).

## What was done
1. **Fixed the bug** by proving a new, fully general, elementary lemma
   from scratch — the **Pair-Insertion Ordering Lemma** — rather than
   invoking `single-insert-point-vertex-lemma` incorrectly or the more
   abstract `vertex-minimum-theorem` machinery (compactness + exchange
   smoothing) for what is really an elementary $4$-element sorted-rank
   computation. Two forms: "between" ($q\le w\le p$) and "above" ($w\ge
   p\ge q$), both proved by a direct trichotomy on the free coordinate
   $x$ against the pinned sorted order of $\{p,q,w\}$ — no gap, no
   numerics in the proof itself.
2. Applied the lemma to **fully close shape $(2,0,1,0)$** on its entire
   domain, both directions: the previously-open residual $f_1<4$ closes
   by an exact polynomial-positivity check in each of the lemma's 4
   cases; the previously-claimed $f_1>4$ branch was independently
   re-confirmed by a fresh 200,000-trial exact-`Fraction` check.
3. Applied the mirrored ("above") form to **fully close shape
   $(2,0,0,1)$'s residual regime** ($f_1<4$) by hand; its complementary
   regime ($f_1\ge4$) is confirmed by a fresh 300,000-trial check but not
   yet hand-derived — an honestly narrower residual than before.
4. The remaining 4 shapes — $(1,1,0,1),(1,1,1,0),(1,2,0,0),(2,1,0,0)$ —
   were **not** attempted this round due to time; flagged as the concrete
   next step, since the new lemma is expected (not yet verified) to apply
   to each by the same peel-then-insert pattern.
5. Wrote a first draft of the middle-case algebra that did not close
   cleanly with crude per-term bounds; replaced it with a clean exact
   polynomial-substitution argument that does close every case — the
   file documents this honestly (the aborted first attempt is summarized,
   not left as a dangling unresolved gap) rather than hiding the false
   start.

## Net status
$(\star_3)$ is **not** closed this round. Progress: 1 of 6 residual
shapes fully closed, 1 of 6 half-closed (one regime remains numerically-
only), 4 of 6 untouched. The outline-reviewer's flagged citation bug is
fixed with a correct, reusable, proven replacement tool
(`pair-insertion-ordering-lemma`, submitted to `lemmas/` for
certification). Status of the approach file remains `partial` (Claim A's
own status, `solved`, is unaffected — this is all addendum work toward
$(\star_3)$/Claim A's residual sub-obstruction).

## Files
- `results/imo-2026-03/approaches/rank-pigeonhole-budget.md` — new §7.17,
  updated `Approaches tried` and `Current best` sections.
- `results/imo-2026-03/lemmas/pair-insertion-ordering-lemma.md` — new,
  submitted for certification.
- Verification scripts (not part of the written proof, cross-checks
  only): `/tmp/verify_shape.py`, `/tmp/check_f1_above4.py`,
  `/tmp/check_2001_full.py`, `/tmp/search_210b.py`,
  `/tmp/search_210_general.py`, `/tmp/explore.py`, `/tmp/explore2.py`.
