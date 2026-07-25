## imo-2026-02

### Scope of this report
Lens: hunt for a genuinely new SYNTHETIC (non-coordinate-bash) mechanism to prove
`A,K,L,Q` concyclic (`Q` := reflection of `A` in the perpendicular bisector of `MN`,
equivalently the foot of the perpendicular from `O_{ABC}` onto the line through `A`
parallel to `BC` — both already certified in
`lemmas/amnq-concyclic-and-reduction.md` / `lemmas/q-as-foot-of-perpendicular-from-
circumcenter.md`). This is the single load-bearing gap shared by
`spiral-similarity-bootstrap` (the population's only non-coordinate route) and,
transitively, the whole problem. I did **not** attempt a proof; below is
reconnaissance only, each candidate mechanism checked numerically against a
genuine solution family (constructed via `scipy.fsolve` on H2/H3 with H1 encoded
by construction, containments verified) on 3 independent scalene triangles.

### Distinct openings (mechanisms tried, each numerically tested)

1. **New, simpler synthetic description of `Q` found and verified (positive,
   modest but real).** `Q = (\text{line through } A \text{ parallel to } BC) \cap
   (\text{perpendicular bisector of } BC)`. Verified numerically: `|QB|-|QC| = 0`
   to machine precision (`~10^-16`) on all 3 test triangles, confirming `Q` lies on
   the perpendicular bisector of `BC` (not just of `MN`) — a fact not stated in
   either certified `Q`-lemma. This is a strictly more elementary characterization
   than "foot of perpendicular from `O_{ABC}`" (no circumcenter needed at all,
   just: intersect two elementary lines both definable from `A,B,C` alone). Proof
   sketch (not carried out in full, but the mechanism is clear and elementary): the
   line through `O_{ABC}` perpendicular to `BC` *is* the perpendicular bisector of
   `BC` (since `O_{ABC}` lies on it by definition of circumcenter); the foot of
   perpendicular from `O_{ABC}` onto the line `A + t(C-B)` is the point where the
   perpendicular *to that line* through `O_{ABC}` meets it, and that perpendicular
   direction is exactly the `BC`-perpendicular direction — so the foot lies on
   both the parallel-to-`BC` line through `A` and on the perpendicular bisector of
   `BC` simultaneously, hence equals their intersection. This is a clean two-line
   intersection with no circumcenter/circumradius arithmetic needed once granted
   — worth having the outliner adopt as the standard definition of `Q` going
   forward (simpler than both current phrasings), though it does not by itself
   close the concyclicity gap.

   **Checked and explicitly REJECTED as a shortcut**: `Q` is NOT the reflection of
   `A` over the perpendicular bisector of `BC` (that different point, `A*`, sits
   on the circumcircle of `ABC` since the perpendicular bisector of `BC` passes
   through `O_{ABC}`, i.e. is a "diameter line" of the circumcircle — `A*` is the
   classical arc-reflection point with `A*B=AC, A*C=AB`). Numerically confirmed
   `Q \ne A*` (`|Q-A*|` was `0.3`–`1.3` in absolute terms across the 3 triangles,
   nowhere near `0`) despite both lying on the line through `A` parallel to `BC`
   in different senses (one is the projection-intersection, the other a genuine
   reflection) — do not conflate these two constructions.

2. **Radical-axis / circle-membership candidates (all tested, all FALSE).**
   Tested whether any of the following natural circles/quadruples are concyclic
   (own `fsolve`-built genuine solutions, 3 triangles × 3 `phi` values each,
   circumcenter/radius computed from raw coordinates, residual `|O-P|-R`
   reported):
   - `B,N,Q,L` concyclic — **false**, residual `~0.04`–`0.44`, growing with `phi`
     (not even phi-independent).
   - `C,M,Q,K` concyclic — **false**, residual `~-0.06`–`-0.10`.
   - `B,N,L,K` concyclic — **false**, residual `~-0.04`–`-0.16`.
   - `B,M,C,Q` concyclic (i.e. does the circle `(BMC)` pass through `Q`?) — 
     **false** (residual is a nonzero constant per triangle, as expected since
     none of `B,M,C,Q` depend on `K,L,\varphi` at all — a sanity check, not
     informative about the family).
   - Nine-point circle of `ABC` (tested via `M,N,\text{midpoint}(B,C)` circumcircle)
     passing through `Q` — **false**, residual `~0.07`–`0.49`, again phi-independent
     (again just checks a fixed fact, and it's false).
   None of these single-shot "obvious" concyclicities hold — so a one-line
   radical-axis argument using `(BMC)`, `(BNC)`, or the nine-point circle directly
   does not exist at this level of naivety. This rules out the simplest forms of
   opening (1)/(4) in the dispatch; a correct mechanism, if radical-axis-based,
   must use a *combination* (radical center of three circles, or a moving circle)
   rather than any single fixed auxiliary circle through `Q`.

3. **Extending the population's own general one-angle lemma to H1 directly —
   tested and FALSE, a genuine (if quick) dead end worth recording.** Applying
   the certified general lemma (`spiral-similarity-bootstrap.md`, "General lemma")
   with `P=B,Q=C,X=A,Y=K,Z=L` to hypothesis H1 (`\angle KBA = \angle ACL`) in the
   hope of getting `\angle BAC = \angle(BK,CL)` (a fixed-vs-moving-line relation
   that would have been very useful) is **numerically false**: the actual gap
   `\angle(BK,CL) - \angle BAC` is **not** zero but equals `2\varphi` (mod 180°,
   matching to 6 decimals, confirmed on two different triangles with the *same*
   `phi` giving the *same* gap `17.19°, 22.92°, 28.65°` at `\varphi=0.15,0.20,0.25`
   rad respectively `= 2\varphi` in degrees exactly) — i.e. this specific
   assignment of the lemma to H1 does not apply (likely a vertex/direction
   mismatch in how H1's angle is measured relative to the lemma's hypothesis
   shape) and produces a quantity that genuinely drifts with the free parameter,
   confirming it is not a shortcut. **Do not re-attempt this exact assignment.**
   A different assignment of the same general lemma to H1 (with different
   `P,Q,X,Y,Z` choices) has not been tried and remains open.

4. **Ptolemy / trig-identity route — not newly explored here (already the
   subject of a separate dead-ended population approach,
   `ptolemy-trig-identity`, stuck on a `Psi>0` positivity gap per current.md);
   no new sub-mechanism found this round distinct from that stuck gap.** Since
   concyclicity of `A,K,L,Q` is exactly the target, Ptolemy's relation on the
   (already-known-to-hold) cyclic quadrilateral is a consequence, not a proof
   mechanism, unless one can independently derive the Ptolemy *product identity*
   from H1–H3 and match it — this was not attempted fresh here since it
   duplicates the existing stuck route; flagging so the outliner does not
   re-dispatch the same wall under a "new" name.

### Candidate technique(s)
- The most concrete *unexplored* opening is: apply the certified general
  one-angle lemma (already proved, reusable) to H1 with a **different** point
  assignment than mechanism 3 above (many `(P,Q,X,Y,Z)` assignments are
  possible; only one was tested and it failed) — worth a systematic short sweep
  of assignments before abandoning this family of moves entirely.
- Given `QB=QC` (new finding, opening 1) and `AQ \parallel BC`, a directed-angle
  chase anchored at `Q` using the inscribed-angle criterion `\angle(QK,QA) =
  \angle(LK,LA)` combined with Lemmas A/B (which already give `\angle BLN` and
  `\angle CKM` in terms of lines `BK,AC` / `CL,AB`) is the same target the
  approach file's own Open gap 1 already identifies as the natural next step —
  this exploration did not find a shortcut around actually doing that chase.
- No Miquel-point configuration was found whose Miquel point is `L` or `K` or
  `Q` from the tested combinations (`B,N,L,K` and permutations above); this
  avenue is weaker than hoped but not exhaustively ruled out (only 3 of many
  possible quadruples tested).

### Cheap-kill candidates
None found this round beyond the 5 ruled out in mechanism 2 above — every
"obvious" fixed-circle-through-`Q` guess is false, so no cheap radical-axis kill
exists at this level; the problem's difficulty appears genuinely load-bearing at
the concyclicity step, not hiding an easy shortcut.

### Knowledge-base entries to use
- "Synthetic toolkit" entry (`knowledge_base.md` line ~129): power of a point/
  concyclicity criterion, spiral similarity, inversion — spiral similarity is the
  one actively in use (via the general lemma); inversion untested this round
  (could be tried centered at `A` or `Q` next, mapping the concyclicity target to
  a collinearity — not attempted here, worth flagging as an unexplored opening).
- Ptolemy / Miquel-point entry (line ~132–134) — Miquel point tested (3
  quadruples, all false); Ptolemy already the subject of a separately stuck
  approach.

### Analogous past problems (cruxes)
The crux corpus documentation states explicitly: **"geometry — Not in the corpus
yet; the problems DB includes geometry problems with solutions, but no geometry
cruxes have been extracted."** So there is no geometry subtopic to filter by and
no crux-move analogy is retrievable for this problem via the corpus mechanism as
built. None to report — do not force a match from another domain.

### Prior progress
Unconditional reduction `OM=ON \iff A,K,L,Q` concyclic is fully certified
(`lemmas/amnq-concyclic-and-reduction.md`, `lemmas/q-as-foot-of-perpendicular-
from-circumcenter.md`). `spiral-similarity-bootstrap.md`'s directed-angle
Corollary `\angle BLN + \angle CKM \equiv 0 \pmod\pi` is proved and correct (hand
+ 6-decimal numeric check), but — confirmed again this round — does not by
itself bridge to `Q`. This round's own new content: the simpler `Q =
(\text{line through }A\parallel BC)\cap(\text{perp. bisector of }BC)`
characterization (opening 1), and the five ruled-out concyclicity/radical-axis
guesses (opening 2) plus the one ruled-out general-lemma assignment to H1
(opening 3).

### Dead ends (do not retry)
- `B,N,Q,L`, `C,M,Q,K`, `B,N,L,K` concyclic — all false (see opening 2).
- Nine-point circle of `ABC` through `Q` — false.
- General lemma applied to H1 with `(P,Q,X,Y,Z)=(B,C,A,K,L)` — false, gives a
  `phi`-dependent (not fixed) angle gap; do not reuse this exact assignment.
- `Q` = reflection of `A` over the perpendicular bisector of `BC` — this is a
  **different** point (the classical arc-reflection point on the circumcircle,
  `A*`); confirmed `Q \ne A*` numerically. Do not conflate.
- (Inherited, reconfirmed by the approach file itself, not retested by me but
  cross-checked as plausible) full triangle similarities from a single
  hypothesis angle (`\triangle LBK \sim \triangle LNC` etc.) — dead end.
- (Inherited) `O` equal to a fixed point (circumcenter/nine-point center) — `O`
  demonstrably moves along a line, not a point.

### Small-case / intuition notes (all conjectural / numeric, not proofs)
- The concyclicity `A,K,L,Q` itself is confirmed to `10^{-10}`–`10^{-14}`
  residual on every genuine solution instance tested (this round: 3 triangles ×
  3–4 `phi` values each, consistent with the approach file's own 3-triangle
  check) — very strong numeric evidence it is exactly true, reinforcing that the
  problem's difficulty is real (a true, nontrivial synthetic fact), not an
  artifact of a wrong reduction.
- `QB=QC` (new, opening 1) suggests any successful synthetic chase should try to
  exploit the isosceles triangle `QBC` explicitly (e.g. `\angle QBC = \angle QCB`
  as a usable equal-angle pair alongside H1–H3), which none of the current
  population's files currently use.
- The one tested new angle relation (opening 3) scaling as `2\varphi` rather
  than being fixed is a useful negative data point: it shows that *not every*
  natural angle built from `B,K,C,L` is `\varphi`-independent — only specific
  combinations (like the already-proved `\angle BLN+\angle CKM$) are — so any
  new proposed identity should first be checked for `\varphi`-independence
  numerically (varying `phi` while holding the triangle fixed) before investing
  in a hand proof; this is a cheap, fast filter and should be standard practice
  for any future synthetic-lens explorer or outliner on this route.
