## Statement

Fix $n$, $m=n+1$, $\mathcal P=\{p\in\mathbb R^m:p_1\ge\cdots\ge p_m>0\}$, and
a full type $(\mathbf c,\tau,\pi)$ (as defined in
`within-chamber-affinity-theorem`, R20.1) with joint mass-conservation
matrix $M(\tau)$ invertible. Let $U=U(\mathbf c,\tau,\pi)\subseteq\mathcal
P$ be the chamber on which some global minimizer of $\Phi$ realizes this
type, and recall (`within-chamber-affinity-theorem`) that on $U$,
$\Phi_{\min}(p)=T(p)-E(F^\ast(p))$ is affine in $p$, with every slot value
$F_{i,l}(p)$ given by a fixed affine formula $F^\tau_{i,l}(p)$ (extendable
to all of $\mathcal P$, whether or not it is feasible/optimal there).

Then:

1. **($U$ is a $p$-space polyhedron.)** $U$ equals the set of $p\in\mathcal
   P$ satisfying finitely many affine inequalities: (a) feasibility
   $F^\tau_{i,l}(p)\ge0$ for every slot; (b) order, $F^\tau_s(p)\ge
   F^\tau_{s'}(p)$ for every pair of slots ranked $s$ above $s'$ by $\pi$;
   (c) type-optimality, $\ell_\tau(p)\le\ell_{\tau'}(p)$ for every other
   full type $\tau'$ available at level $n$ (finitely many, by the finite
   combinatorial nature of type data and by `vertex-minimum-theorem`'s own
   finiteness of the vertex family), where $\ell_\tau(p):=T(p)-E(F^\tau(p))$
   is the globally-defined affine candidate objective.
2. **(Chamber-Vertex Theorem.)** On the bounded slice $\overline
   {U\cap\{T=1\}}$ (a polytope, by 1 plus boundedness of $\mathcal
   P\cap\{T=1\}$), the affine functional $g(p):=a_nT(p)-\Phi_{\min}(p)$
   attains its minimum at one of the polytope's finitely many vertices,
   each pinned by $\dim(\mathcal P\cap\{T=1\})$ independent tight
   constraints drawn from families (a)/(b)/(c) (or their closures) together
   with $T=1$. Consequently $g\ge0$ throughout $U\cap\{T=1\}$ iff $g\ge0$ at
   every vertex of $\overline{U\cap\{T=1\}}$.
3. **(Strict-Box compactness corollary, for case (b2)'s box specifically —
   scope corrected in round 23; see the round-22 reviewer note below, now
   folded into the statement rather than left standing as an overclaim.)**
   Case (b2)'s box $\mathrm{Box}=\{p_1<T/2,\ T/D_n<p_2<a_nT/2\}$ is open, so
   a vertex of $\overline{U\cap\mathrm{Box}\cap\{T=1\}}$ may lie on
   $\overline{\mathrm{Box}}\setminus\mathrm{Box}$, not in $\mathrm{Box}$
   itself. This is not a gap **provided each of the three Box walls is
   itself already closed at the $n$ in question** — which is true
   unconditionally only for $n\le3$, and otherwise only conditionally:
   - $p_2=T/D_n$ (case b1) is the boundary of $p_2\le T/D_n$, closed via the
     Max Domination Lemma / `unconditional-p2-threshold-closure` —
     **unconditionally, for every $n\ge1$.**
   - $p_1=T/2$ is the boundary of $p_1\ge T/2$, closed via Theorem C$'$ —
     **unconditionally only for $n\le3$**; extending it past $n=3$ needs
     the $p_1<T/2$ regime (case (b2) itself) closed one level down first,
     a genuine induction coupling, not a free extension.
   - $p_2=a_nT/2$ is the boundary of case (a), $p_2\ge a_nT/2$, closed via
     Theorem B's recursive sufficient condition — **conditional** on the
     standing strong-induction hypothesis one level down (the same
     hypothesis this whole file's induction rests on), not unconditionally
     established at every $n$.

   Consequently: **at $n\le3$, all three walls are unconditionally closed
   (since "one level down" from $n\le3$ is $n\le2$, already fully closed in
   this project), so the corollary below applies with zero caveats; at
   $n\ge4$, the corollary is conditional on the standing strong-induction
   hypothesis (specifically, on the $p_1\ge T/2$ closure extending past
   $n=3$, which is not yet established).** This is a scope correction, not a
   retraction: the boundary-sharing *mechanism* itself is correct and
   general — only the claim that all three input closures are unconditional
   at *every* $n$ was an overclaim, now removed. Modulo that scoping,
   $g\ge0$ at every vertex of $\overline{U\cap\mathrm{Box}\cap\{T=1\}}$
   lying in $\mathrm{Box}$ itself (checked via 2, the new machinery)
   together with $g\ge0$ at every vertex on
   $\overline{\mathrm{Box}}\setminus\mathrm{Box}$ (covered by the three
   cited theorems to the extent they are closed at the given $n$) implies
   $g\ge0$ throughout $U\cap\mathrm{Box}$.

## Honest scope

This theorem is **conditional**, with the same hypothesis inherited
verbatim from `within-chamber-affinity-theorem`: it requires $M(\tau)$
invertible, and item 1's characterization of $U$ via condition (c) is only
fully justified against a competing type $\tau'$ when either $M(\tau')$ is
also invertible, or $\tau'$ falls in R20.4's "generic singular" sub-case
(automatically a wall, hence droppable from the finite list without
affecting $U$'s interior). R20.4's "residual coincidence" sub-case (where
$M(\tau')$ is singular but the compatibility functionals vanish
identically) is **not** resolved here — inherited as open exactly as
`within-chamber-affinity-theorem` already flags it, not a new gap.

Item 2 (the vertex-attainment fact itself) is unconditional given item 1;
item 3's compactness-fix *mechanism* (boundary-sharing with three adjacent
regions) is general and reusable for any future chamber-by-chamber
evaluation attempt, but its actual *applicability* is $n$-dependent, as
corrected above: **unconditional only at $n\le3$**, and conditional on the
standing strong-induction hypothesis for $n\ge4$ (since the $p_1\ge T/2$
wall and case (a) are each only closed at those respective scopes, not for
every $n$). This replaces the round-22 text's "unconditional and general
(it does not depend on $n$...)" claim, which was an overclaim caught and
corrected by the round-22 reviewer (see the correction note below) and is
now folded directly into item 3's statement above.

**This theorem does not close case (b2).** It converts "prove
$\Phi_{\min}(p)\le a_nT$ throughout case (b2)'s box" into "prove it at
finitely many characterized vertices per chamber, ranging over the
finitely many chambers that meet the box" — a well-posed finite question,
not yet executed for any $n$. The round-20 chamber-count growth signal
(composition-level density $\approx28\%\to64\%$ from $n=3$ to $n=4$ on
sampled points) remains an open risk for whether this finite question stays
tractable as $n\to\infty$.

## Proof

See `results/imo-2026-03/approaches/lp-duality-certificate.md`,
"Round 22 build", §R22.1 (Lemma R22.1 and Theorem R22.2, full proof) and
§R22.2 (the Corollary proving item 3 above). §R22.1.1 gives a concrete,
numerically-verified non-empty worked chamber at $n=3$ (composition
$(1,1,0,0)$, closed form $\Phi_{\min}(p)=p_1/2+p_3+p_4$ on its chamber,
walls $p_1\ge2p_3$ and $p_2\le p_3+p_4$), confirming the theorem's
hypotheses are met by a genuine, non-vacuous case-(b2) example, not merely
formally consistent.

Sketch: Lemma R22.1 shows $U$ literally equals the (a)/(b)/(c)-cut-out set,
by unwinding what "$p\in U$" means (some global minimizer realizes $\tau$)
in both directions, using invertibility of $M(\tau)$ to get a single-valued
affine candidate $F^\tau(p)$ everywhere, and `vertex-minimum-theorem`'s
finiteness to know the true minimum is always realized by *some* type.
Theorem R22.2 is then the standard convex-geometry fact — already invoked
by `vertex-minimum-theorem` — that a bounded polyhedron is the convex hull
of finitely many vertices, and an affine functional on it attains its
extrema there (a one-line convex-combination argument). The compactness
corollary is boundary-sharing: the open Box's missing boundary is exactly
covered, wall-by-wall, by three theorems already certified elsewhere in
this file, so no new machinery is needed there.

## Reviewer correction (round 22) — item 3 is NOT unconditional/general as stated

**Addressed in round 23**: the correction below has been folded directly
into item 3's statement and the "Honest scope" section above (rather than
left as a standalone note contradicting the main text). Retained here
verbatim for the record of what was found and why.

**CERTIFIED WITH CORRECTION.** Items 1–2 (Lemma R22.1 and the Chamber-Vertex
Theorem proper) are correct, and are certified as stated: a conditional
(invertibility-dependent) polyhedral/vertex characterization of $U$ in
$p$-space, independently re-derived by the reviewer.

**Item 3's "boundary-sharing" Corollary, however, overclaims.** The text
above (and this file's own "Honest scope" §, second paragraph) states that
item 3 "is unconditional and general (it does not depend on $n$...)" and
that all three Box walls are "already-unconditionally-closed adjacent
region[s]." This is **false as stated**, by cross-reference against
`approaches/lp-duality-certificate.md`'s own record elsewhere in the same
file:

- The $p_1\ge T/2$ wall region is **only** closed unconditionally for
  $n\le3$ ("§4. $p_1\ge T/2$ closed rigorously and unconditionally for
  $n\le3$"; explicitly re-affirmed at "giving a genuine, complete closure
  of $p_1\ge T/2$ **only for $n\le3$**" in the Round-9 write-up). Extending
  past $n=3$ requires the $p_1<T/2$ regime (case (b2) itself!) to be closed
  one level down first — the file's own diagnosis of a genuine coupling,
  not a free extension. It is **not** "closed for every $n$."
- Case (a) $p_2\ge a_nT/2$ is explicitly labeled **"conditional, known"**
  elsewhere in the same approach file (e.g. the Round-19 re-confirmation
  list, item 1): its proof invokes the strong induction hypothesis
  $\Phi_{\min}(S')\le a_{m-2}T'$ one level down, which is exactly the same
  standing hypothesis this whole file's induction rests on — it is **not**
  "already-unconditionally-closed" in an absolute sense at every $n$; it
  is closed *modulo* the same overall induction that has not yet reached
  general $n$ (since case (b2) itself is what remains open at every level).
- Only the $p_2\le T/D_n$ wall (case (b1), via the Max Domination
  Lemma / `unconditional-p2-threshold-closure`) is genuinely,
  unconditionally general for every $n$ — this one is correctly described.

**Consequence.** The Corollary "$g\ge0$ at box-boundary vertices, hence
throughout $U\cap\mathrm{Box}$" is therefore only established as literally
unconditional at $n\le3$ (where all three walls' covering regions really
are unconditionally closed); for $n\ge4$ it is conditional on the same
standing strong-induction hypothesis every other conditional result in
this project already carries (in particular, on the $p_1\ge T/2$ regime's
own — currently unproven for $n\ge4$ — closure). This does **not**
invalidate items 1–2, and does not retract the genuine value of the
boundary-sharing *idea* (it is the right mechanism, once its two
input theorems are actually available at the relevant $n$) — but item 3
must be re-stated as conditional (or explicitly scoped to $n\le3$) before
being cited as a general closure. Reviewer independently found this by
cross-referencing this exact approach file's own §4 / Round-9 / Round-19
text (lines documented in `current.md`'s round-22 entry), not by
re-deriving new mathematics — a citation-consistency bug, not a proof bug
in items 1–2.

**Recommendation for round 23:** rewrite item 3 as: *"...each already
established at least for $n\le3$ (unconditionally) — resp. conditionally
on the standing strong induction hypothesis at larger $n$..."*, and
correct the "Honest scope" paragraph's "unconditional and general"
sentence accordingly.

## Round-26 note: case (a) is $p_2\ge a_nT/2$, not $p_1\ge T/2$

This file's item 3 and "Honest scope" section refer to two separate
adjacent regions to case (b2)'s box: a "$p_1\ge T/2$" wall (Theorem A/C$'$)
and a "case (a), $p_2\ge a_nT/2$" wall (Theorem B's Corollary). At $n=3$,
`approaches/lp-duality-certificate.md`'s round 25 conflated these two into
one ("case (a) ($p_1\ge T/2$)"), a citation bug fixed in that file's
round-26 section: the actual third piece of the $n=3$ upper-bound
trichotomy is $p_2\ge a_3T/2=4T/15$ (Theorem B's Corollary, discharged
unconditionally at $n=3$ by `n2-upper-bound-lp-argument`), **not**
$p_1\ge T/2$ — the two walls are genuinely different regions, and only
the $p_2\ge a_nT/2$ one is used in the final $n=3$ assembly. This does not
change anything in this file's own statement (which already correctly
lists both walls separately) — it only corrects how the approach file had
been *citing* this file's decomposition. See
`approaches/lp-duality-certificate.md`, §R26.1–R26.3, for the corrected
$n=3$ assembly in full.
