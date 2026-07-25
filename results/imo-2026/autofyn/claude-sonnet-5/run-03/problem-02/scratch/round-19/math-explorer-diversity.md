## imo-2026-02 (diversity insurance: spiral-similarity-bootstrap, route (b))

**Choice made.** Read both backup routes in full (round 15-18 history in
`current.md`, plus the full current text of both
`coordinate-bash-resultant-boundary-pointwise-sos.md` and
`spiral-similarity-bootstrap.md`). Chose route **(b) spiral-similarity-bootstrap**:
it has fresh synthetic content (Lemmas A, B, and the parameter-free Corollary
`∠BLN + ∠CKM ≡ 0 (mod π)`, all hand-proved and reviewer-untested this round)
and one clearly-stated open bridge to `O, M, N` — a much more concrete,
independently-checkable next step than route (a)'s SOS Gram-matrix
degeneracy, which after 4 rounds (15-18) of diagnostics has narrowed the
*mystery* (which directions are unexplained) but has produced no new
algebraic lever and the round-18 report's own honest conclusion is that the
dominant explaining direction is witness-dependent (not uniform) — i.e. it
is not clear the degeneracy has a clean closed-form characterization at all,
as opposed to just being a genuinely singular ansatz that needs an enlarged
basis. Route (a) also requires standing up a `cvxpy`/SDP pipeline to make
any further progress, which is a heavier lift for a single-round scouting
pass than direct synthetic/coordinate experiments on route (b).

### Numeric setup

Built genuine solution instances of the full hypothesis set (H1)-(H3) plus
the ray/interior structure, independently of the file's own scripts: fixed
$A=(0.3,1.1), B=(-1,0), C=(1.3,-0.1)$ (same triangle as the file, for
comparability). Parametrized the 1-parameter family by
$\varphi=\angle KBA=\angle ACL$ (which encodes H1 by construction): $K$ lies
on the ray from $B$ obtained by rotating $\vec{BA}$ by $-\varphi$, $L$ on
the ray from $C$ obtained by rotating $\vec{CA}$ by $+\varphi$; then solved
the two remaining scalar equations (H2, H3) for the two ray-distances via
`scipy.optimize.fsolve`. Verified for a dense range $\varphi\in[0.15,0.65]$
that: (i) `fsolve` converges (ier=1), (ii) $K$ inside $\triangle BMC$, $L$
inside $\triangle BNC$ (both true throughout the tested range), (iii) the
containment identities $\angle LBK+\angle KBA=\angle LBA$ and
$\angle ACL+\angle LCK=\angle ACK$ hold (i.e. $K$ genuinely between rays
$BL,BA$ and $L$ genuinely between rays $CA,CK$, confirming the sign
convention used in the file's directed-angle setup, at least on this dense
range — this is a small independent partial corroboration of the file's
**Open gap 2**, though only numeric/instance-based, not a general proof).
Confirmed $OM=ON$ to $\sim10^{-11}$–$10^{-14}$ at every tested $\varphi$
(15 points), consistent with the problem statement and with the file's own
prior numeric confirmation — no surprises, but a clean independent rebuild
(own `fsolve`-based construction, not reusing the file's own least-squares
script) is itself useful cross-validation.

### Concrete new findings (probing the "power of M, N" bridge the dispatch asked about)

1. **$\mathrm{pow}(M,\omega_{AKL}) = \mathrm{pow}(N,\omega_{AKL})$ holds
   exactly (to numeric precision) throughout the family** — trivially
   equivalent to $OM=ON$ (both use the same radius $r=OA$), so this is not
   new content by itself, but confirms the power-of-a-point framing is at
   least consistent as a target.
2. **A genuinely useful reduction, confirmed numerically and then verified
   algebraically by hand: $OM^2-ON^2$ is an *affine-linear* function of $O$
   alone** (using $M=(A+B)/2$, $N=(A+C)/2$):
   $$OM^2-ON^2 = O\cdot(C-B) + \tfrac14\big(2A\cdot(B-C)+|B|^2-|C|^2\big).$$
   Setting $A$ at the origin (the file's own coordinate convention) this is
   exactly $O\cdot(C-B) - \tfrac14(|B|^2-|C|^2)$, matching the sign of the
   identity **already cited in the file's "Confirmation of the target line
   ℓ" paragraph**, $O\cdot(C-B)=(|C|^2-|B|^2)/4$ — so this is an
   independent re-derivation of an already-known fact, not new, but it
   pins down *exactly* what must be proved: a **single linear functional of
   $O$** is fixed, i.e. $O$ lies on a specific fixed line perpendicular to
   $BC$ (since $MN\parallel BC$ by the midline theorem, "perpendicular
   bisector of $MN$" and "perpendicular to $BC$" are the same direction —
   this equivalence, though elementary, does not appear to be spelled out
   explicitly anywhere in the file and may be a useful explicit lemma to
   record: **reduce "$OM=ON$" to "$O$ lies on the fixed line through
   $\mathrm{midpoint}(A,O_{ABC})$ perpendicular to $BC$" using $MN\parallel
   BC$ and the perpendicular-bisector characterization** — this converts
   the 2D target ($OM=ON$, a distance equality) into a 1D linear
   functional-vanishing target, which may be easier to attack via the
   $\angle BLN+\angle CKM\equiv0$ Corollary since that Corollary is itself
   an angle statement, naturally suited to a sine-rule computation of a
   linear projection).
3. **Ruled out (numerically, cleanly) as a mechanism**: no simple constant
   ratio holds among $AK/AB$, $AL/AC$ (varies $0.65\to0.83$ and
   $0.67\to0.86$ respectively over the tested range — confirms and
   reproduces the file's own already-recorded dead end that
   $AB/AK\ne AC/AL$, i.e. no spiral similarity at $A$ sending
   $B\mapsto C,K\mapsto L$). Also ruled out: $AK\cdot AC = AL\cdot AB$ (a
   natural "crossed" spiral-similarity power-type identity) — not constant
   and not equal at any single instance tested (e.g. at $\varphi=0.2$:
   $AK\cdot AC=1.730$ vs $AL\cdot AB=1.786$, a $\sim3\%$ gap, well outside
   numeric noise). Also ruled out $BK\cdot AC = CL\cdot AB$ (ratio drifts
   from $\approx1.06$ to $\approx1.27$ over the family) — so **no natural
   two-term power/similarity product across the $B,K$ and $C,L$ data is
   family-invariant**; whatever identity closes the gap must involve $O$
   (or the circle $(AKL)$) more essentially than a bare side-length
   product.
4. **A genuinely new, clean confirmed fact**: $\mathrm{pow}(B,\omega_{AKL})
   -\mathrm{pow}(C,\omega_{AKL})$ is **exactly constant across the family**
   (verified to 5 significant figures at 4 sample $\varphi$ values,
   $\approx0.23$ throughout) — but on reflection this is *also* not new
   content: $\mathrm{pow}(B)-\mathrm{pow}(C)=OB^2-OC^2$ is affine-linear in
   $O$ exactly like item 2's quantity, and is constant along *any* line
   through the direction perpendicular to $BC$ — so this is simply
   restating "$O$ moves on a fixed line perpendicular to $BC$" (already
   established) in a different but equivalent guise, not an independent
   new lever. Flagging this explicitly so a future round does not waste
   time treating it as a fresh clue.
5. Attempted (but did not complete, per the "one line and stop" scouting
   rule) the second-intersection idea from the file's own Open gap 1: found
   the second intersection $P_{AB}$ of line $AB$ with $\omega_{AKL}$ and
   $P_{AC}$ of line $AC$ with $\omega_{AKL}$ numerically; no simple
   constant ratio $AP_{AB}/AB$ vs $AP_{AC}/AC$ was found (they drift apart,
   $0.59\to0.75$ vs $0.61\to0.80$, staying close but not equal — a
   $\lesssim3\%$ gap at every tested point, consistent but not conclusively
   ruling out a more refined relation e.g. involving $AM,AN$ rather than
   $AB,AC$ directly). This specific idea (compare $P_{AB}, P_{AC}$ against
   $M,N$ directly, not $A,B,C$) was **not fully tested** — a concrete,
   cheap next check for a future round: compute $MP_{AB}$ and $NP_{AC}$ (or
   the *signed* power expressions $MA\cdot MP_{AB}$ vs $NA\cdot NP_{AC}$,
   which by definition already equal $\mathrm{pow}(M),\mathrm{pow}(N)$ and
   are known equal — so this reduces to nothing new beyond item 1) — this
   avenue looks like a dead end for producing new leverage, since any
   "power of $M$/$N$" computation is definitionally exactly the OM=ON
   target restated, not a route around it.

### Net assessment for route (b)

No breakthrough found this round; the concrete synthetic bridge from
Lemma A / Lemma B / the Corollary ($\angle BLN+\angle CKM\equiv0$) to
$O$'s linear-functional characterization (item 2 above) remains open. The
most promising concrete next step, sharper than the file's own current
"Open gaps" wording: **use the Extended Law of Sines on the still-moving
circles implicit in Lemma A ($\angle BLN=\angle(BK,AC)$, i.e. an inscribed
angle at $L$ subtending chord $BN$ of some circle through $B,L,N$) and
Lemma B symmetrically, to express $AK$ and $AL$ (or, more usefully, the
position of $O$ projected onto the $BC$-perpendicular direction) as
explicit trigonometric functions of $\angle A, \angle B,\angle C$ and the
family parameter $\varphi$, then substitute into item 2's linear identity
$O\cdot(C-B)=(|C|^2-|B|^2)/4$ and check whether the $\varphi$-dependence
cancels algebraically** — this has not been attempted in any approach file
to date (the file's own "Full completion" gap description is vaguer,
citing "power of $M,N$" and "second intersections" without this specific
sine-rule substitution route). This is a concrete lead, not a proof —
flagging it for the outliner to consider as a possible next dispatch for
this approach, while noting item 5 (bare second-intersection power
comparisons) is very likely a dead end as a *route around* OM=ON rather
than a route *to* it.

### Route (a) — not pursued computationally this round (time-budget
choice), brief note only

Per the round-18 report, route (a)'s own honest finding is that the
dominant "explaining" direction of the 3 residual near-null eigenvectors
differs between the two tested witnesses (`n_2`'s root at witness 1 vs
`n4sq`'s root at witness 2), which is itself evidence *against* there being
a single clean algebraic characterization (e.g. a uniform repeated-root
condition) — if the mechanism were witness-independent, both witnesses
should implicate the same generator. This is worth flagging to the
outliner as a reason to deprioritize further diagnostic SDP rounds on (a)
in favor of either (i) an enlarged ansatz (more generators / higher degree,
as round 16's own recommendation already suggested and no round has yet
tried) or (ii) the option this report focuses on, deepening route (b).

## Distinct openings surfaced
- Route (b): reduce $OM=ON$ to the single linear functional
  $O\cdot(C-B)=(|C|^2-|B|^2)/4$ (equivalently "$O$ lies on the fixed line
  through $\mathrm{midpoint}(A,O_{ABC})$ perpendicular to $BC$," using
  $MN\parallel BC$) and attack it via an explicit Extended-Law-of-Sines
  parametrization of $O$'s position using Lemma A/B's inscribed-angle
  content and the family parameter $\varphi$ — new, not attempted before.
- Route (b), ruled out this round: any bare two-term power/similarity
  product across $\{AK,AL,BK,CL,AB,AC\}$ (items 3-4) — do not re-try these
  exact combinations.
- Route (a): the "clean uniform algebraic degeneracy locus" hypothesis is
  weakened (not ruled out, but weakened) by round 18's own witness-dependence
  finding; an enlarged-ansatz approach is likely a better use of a future
  round's SDP budget than further single-witness diagnostics.

## Candidate technique(s)
Route (b): directed-angle chase (already partly done) + Extended Law of
Sines + linear-functional reduction of $OM=ON$ (item 2's identity, an
elementary equivalent restatement worth writing up explicitly as a citable
sub-lemma). Route (a): SOS/Positivstellensatz certificate search, likely
needs a larger generator/degree basis rather than more diagnostics at fixed
size.

## Cheap-kill candidates
None found this round beyond the already-recorded dead ends (naive spiral
similarity, full triangle similarity, O = fixed point) — see "ruled out"
items above for two more specific product identities now also ruled out.

## Knowledge-base entries to use
`knowledge_base.md`'s generic "Synthetic toolkit" entry (line ~129):
angle chasing, power of a point, spiral similarity — no problem-specific
entry exists; the population is already using the relevant generic tools.

## Analogous past problems (cruxes)
Not queried this round (dispatch was narrowly scoped to numeric/structural
probing of the two named backup routes, and time budget was spent on that);
if a future round wants crux-corpus support for route (b), search subtopic
"circumcenter"/"midpoint"/"spiral similarity" per
`crux_moves_documentation.md`'s subtopics index (not done here — flagging
as unexplored, not "none found").

## Prior progress
Route (b) (`spiral-similarity-bootstrap.md`): Lemma A
($\angle BLN=\angle(BK,AC)$), Lemma B ($\angle CKM=\angle(CL,AB)$), and the
Corollary ($\angle BLN+\angle CKM\equiv0\pmod\pi$) — all proved and
independently spot-checked this round (numeric instances, 15 fresh
$\varphi$ samples, consistent). Route (a)
(`coordinate-bash-resultant-boundary-pointwise-sos.md`): 4 rounds of SDP
Gram-matrix degeneracy diagnostics (rounds 15-18), no certificate, gap not
closed — not independently re-run this round.

## Dead ends (do not retry)
- Route (b): spiral similarity at $A$ sending $B\mapsto C,K\mapsto L$
  (angles don't match, ratios don't match — reconfirmed again this round).
- Route (b): $AK\cdot AC=AL\cdot AB$ and $BK\cdot AC=CL\cdot AB$ — both
  numerically ruled out this round (new finding, not previously recorded
  in the file).
- Route (b): "power of $M$/$N$" via second-intersection points $P_{AB},
  P_{AC}$ compared directly against $A,B,C$-only ratios — no simple
  relation found; likely circular (restates OM=ON rather than bypassing
  it) — flagged as low-value for future rounds unless combined with the
  sine-rule idea above.
- Route (a): "second independent complex-conjugate near-double root" —
  already ruled out in round 18, reconfirmed by re-reading, not re-tested
  here.

## Small-case / intuition notes
All numeric checks in this report are **numeric evidence only**, not proof.
The linear-functional reduction (item 2) is elementary algebra (exact,
not numeric) once $MN\parallel BC$ is invoked, and is worth stating as a
clean explicit sub-lemma in the approach file even though it's a
restatement of an already-known fact, since it sharpens exactly what
Lemma A/B need to feed into.
