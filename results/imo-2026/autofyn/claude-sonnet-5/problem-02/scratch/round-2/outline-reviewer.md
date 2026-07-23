# Outline review — IMO-2026-02, round 2

## coordinate-trig-bash — CHANGES REQUESTED (build)

Verdict on the specific flagged concern (decoupling lemma, step 4): **the
concern is resolved — the claim is TRUE and has a one-line rigorous proof,
not a gap.** The outliner's worry ("arccos depends on magnitude, not just
direction") is unfounded here because of a cancellation the outline missed:

For vertex V with a *second* point P on a fixed ray from V, i.e. P = V + r·u
for a fixed unit vector u and free r>0, the angle ∠(V; P,Q) = arccos[(P−V)·(Q−V)
/ (|P−V||Q−V|)] = arccos[r·u·(Q−V) / (r|u||Q−V|)] = arccos[u·(Q−V)/(|u||Q−V|)]
— the factor r cancels exactly out of numerator and denominator, for every
r>0. So the angle at V between ray VP (P on a fixed ray from V) and ray VQ
depends on the *direction* u only, never on r, full stop — no magnitude
dependence survives. This is elementary but it is the correct mechanism, and
it settles both halves of the claim:
- F1 = ∠LBK − ∠LNC: at vertex B, ray BK has K = B + r1·u_K(θ) (K on a fixed
  ray *from B*), so ∠LBK depends on r2 (via L) and θ, never r1, by the fact
  above applied at V=B. At vertex N, ray NC is fixed (N, C both fixed given
  the triangle), ray NL depends on L (hence r2, θ) — no r1 dependence
  anywhere. So F1 = F1(θ, r2) only. ✓.
- F2 = ∠LCK − ∠BMK: symmetric argument at vertices C (ray CL fixed direction
  u_L(θ), independent of r2) and M (ray MB fixed, ray MK depends on r1,θ). So
  F2 = F2(θ, r1) only. ✓.

**Action for the builder:** replace the outline's tangled sub-lemma writeup
(steps 4's "Key lemmas" paragraph, which talks itself into confusion) with
this one-paragraph cancellation argument. It costs one line of algebra, not
a full symbolic-differentiation investigation — don't let the builder over-invest
here.

Remaining open content, genuinely open (not resolvable by the above):
- **Monotonicity (step 5).** F1 strictly monotone in r2 (θ fixed), F2
  strictly monotone in r1, is a real geometric claim needing its own proof
  (e.g. via the "angle subtended by a point receding along a fixed ray is
  monotone" fact) — not yet proved, correctly flagged as open. This is
  plausible and provable (classical fact, provable via law of sines in the
  moving triangle) but must be done rigorously, not asserted.
- **Endpoint signs.** r2→0, r2→r2max sign computations: open, should be
  tractable (degenerate limits) but not yet done.
- **Step 6 (final substitution).** Even after IVT pins down r1(θ), r2(θ) as
  unique roots, showing O_x−p/2 vanishes along the resulting curve is still
  open and may itself require nontrivial work (implicit differentiation or a
  restricted resultant). The outline honestly flags this as the approach's
  weakest-specified step — the builder should not claim the branch-isolation
  win alone counts as solving the problem.

Technique is sound, real machinery already certified (Lemmas 1–3), no
circularity. Approve to build with the above corrections.

## labeling-duality — CHANGES REQUESTED, with a genuine logical error to fix
before building further

**Step 2 of this round's revision is wrong as stated and must be corrected
before the builder proceeds**, or the round's build effort is wasted on a
step that can't work. The claim: "apply law of sines in triangle ABK ... to
get BK as an explicit trig function of θ, β (and AB)." This is false: BK
is *not* determined by θ and β alone. Triangle ABK has A, B fixed and K
constrained only to lie on the fixed ray from B at angle θ from BA (this is
literally coordinate-trig-bash's certified Lemma 3, K = B + r1·u_K(θ)) — the
length BK = r1 is a genuine free parameter, not a function of θ, β. It is
exactly the unknown that conditions (2) and (3) exist to pin down (this is
precisely the r1, r2 system that coordinate-trig-bash spent the whole round
setting up as F1(θ,r1,r2)=0, F2(θ,r1,r2)=0 — the *same* two remaining
conditions, in the same role). Labeling-duality's step 2 implicitly assumes
this free parameter is already fixed by θ, β alone, which would make the two
remaining conditions vacuous — a direct contradiction with the field's own
established structure (Lemma 3, already certified and reusable).

**What must change:** BK (and CL) should be treated as unknowns tied by
conditions (2) and (3) — i.e., the builder should set up exactly the same
r1(θ), r2(θ) system that coordinate-trig-bash's Lemma 3 defines (reuse it
rather than re-derive), and only THEN attempt to extract the ∠AKL, ∠ALK
data needed for the secant-through-A computation in steps 4–5, as functions
of the (still only implicitly characterized) r1, r2. If this synthetic route
does not actually shortcut past solving for r1, r2, it risks converging onto
the *same* underlying unsolved system as coordinate-trig-bash — flag this
overlap risk explicitly to the builder; it isn't a fatal issue, but the two
approaches may be closer than the outline currently claims (memory rule:
watch for shared-gap collapse across ostensibly different techniques).

Step 6 (radical axis fallback) is a legitimate cheap thing to try first
(a quick sympy check) before committing to the corrected step 2–5 chase.

Given the step-2 error, this is CHANGES REQUESTED, not RETHINK — the
underlying reduction (Step 1, already certified) is solid, the overall
target (deriving (TI) from the hypotheses) is the right thing to attack, and
the fix is a redirection of steps 2–5, not a wrong technique. But the
builder must be told explicitly not to write step 2 as given.

## antipode-perp-bisector — APPROVE (new, register, build)

This is the strongest diversification move on the table this round — a
genuinely different top-level target (a perpendicularity/incidence
statement via Thales, not a scalar power-of-a-point identity), which is
exactly what the field needs after two rounds converging on the same
underlying (TI)/O_x=p/2 gap (per memory rule 3 and CLAUDE.md's shared-gap
guidance).

Checked steps 1–4 by hand:
- A* := 2O−A. |A*−B| = |2(O−M)| = 2·OM and |A*−C| = 2·ON follow from direct
  substitution of M=(A+B)/2, N=(A+C)/2 — correct, no hidden case split, and
  this makes OM=ON ⟺ A*B=A*C unconditionally (any O, A, B, C). ✓
- ∠AKA* = ∠ALA* = 90° by Thales (AA* a diameter of Γ, K,L∈Γ) — correct,
  standard, no gap. ✓
- The reduction of the WHOLE problem to "show A*B=A*C where A* is the
  synthetic intersection of (⊥AK at K) and (⊥AL at L)" is therefore fully
  rigorous and gap-free through step 4.

Step 5 is honestly and entirely open — the outline does not overclaim it,
correctly labels it as the approach's whole remaining content, and
correctly notes it is a *different* claim from the two mechanisms already
refuted for two-step-spiral-chain (different point set: A*,K,B and A*,L,C
vs. the earlier B,K,L,N / C,K,L,M pairings), so it is not a repeat of a
recorded dead end. The proposed lever (right-triangle relations at K, L via
law of cosines, using BK, CL from labeling-duality-style law-of-sines work)
is a reasonable thing to try, with an explicit warning to numerically pin
down the orientation/sign convention (∠A*KB = 90°±∠AKB) before writing a
general proof — good practice, keep it.

No fatal flaw. Approve to build.

## nine-point-link, complex-circle-power — hold (not in build set)

Correctly left low priority by the outliner: both entirely unbuilt and
speculative, with no new lever proposed this round beyond "as already
written." Ranked below the three live/new approaches. No action needed
this round; revisit only if the build set stalls.

## Diversity assessment

Field now has three genuinely distinct top-level reductions in flight:
(TI) power-of-a-point (labeling-duality), coordinate O_x=p/2 with explicit
parametrization (coordinate-trig-bash), and A*B=A*C via Thales antipode
(antipode-perp-bisector). The first two still risk collapsing onto the same
underlying algebraic system (labeling-duality's corrected step 2 will
essentially reconstruct coordinate-trig-bash's r1(θ), r2(θ) system) — worth
watching next round, but antipode-perp-bisector is a real structural
departure (different target statement entirely, not just different
coordinates for the same one) and should be preserved as the field's
diversity anchor regardless of how the other two fare.

## Ranking

Registered antipode-perp-bisector (cold-start 1500) and ran update_ranking
across the whole field, anchoring the newcomer against established
approaches (dead-end two-step-spiral-chain loses to everything live;
unbuilt nine-point-link/complex-circle-power lose to concrete partial
approaches; antipode-perp-bisector drawn against the two other live leads
since all three now carry a comparable "clean reduction + one open step"
structure). Resulting order (best-first): coordinate-trig-bash (1596),
antipode-perp-bisector (1539), labeling-duality (1533), two-step-spiral-chain
(1472, dead-end), complex-circle-power (1446), nine-point-link (1414).

build set: coordinate-trig-bash, antipode-perp-bisector, labeling-duality
