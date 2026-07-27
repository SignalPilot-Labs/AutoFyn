# Outline review: imo-2026-02 (OM = ON)

## Verdict: CHANGES REQUESTED

The technique (antipode reduction + analytic coordinate proof) is sound and the
spine is correct. I independently verified the reduction and the analytic
machinery numerically (see below). But the load-bearing step 6 — the claim that
the target identity (*) "vanishes identically" after substituting Eq K / Eq L —
has no real mechanism and is, as stated, circular. That gap is fixable, but the
builder must commit to a concrete verification strategy before filling in. Eq K
is also under-specified. Do NOT send this to the builder as-is expecting the
algebra to "just work."

---

## What I verified (numerical, independent)

Triangle A=(0,0), B=(4,0), C=(1.5,3), alpha in {5,10,15,20,30,40}°, solving the
full nonlinear system for beta,gamma so that K = BK∩MK lies on CK and L = BL∩CL
lies on NL (the two incidence constraints). All confirmed to ~1e-12:

- OM = ON.
- A' = 2O - A satisfies A'K ⊥ AK and A'L ⊥ AL (dot ~1e-16).
- The linear-system formula A' = (|L|²·JK − |K|²·JL)/(K×L) equals 2O − A to
  ~1e-16. (I checked the derivation: JK·K=0, JK·L=K×L, JL·K=−(K×L), JL·L=0, so
  the formula solves A'·K=|K|² and A'·L=|L|². Correct.)
- The target identity (*) 2[|L|²(JK)·(C−B) − |K|²(JL)·(C−B)] = (|C|²−|B|²)(K×L)
  vanishes on the locus.

So the reduction, the perpendicular characterization A'=perp(K)∩perp(L), the
linear-system setup, and the target identity are all correct. Concerns #1 and #2
of the dispatch pass on the *setup*. The problem is purely in step 6's
verification.

---

## Issues (the builder must address these)

### 1. Step 6's load-bearing lemma is circular as stated (the main problem)

The outline's stated mechanism for "(*) vanishes under Eq K, Eq L" is:
"the trig-Ceva relations are precisely the algebraic relations making K lie on
CK and L lie on NL, so substituting them turns (*) into 0."

This is **not a mechanism** — it is a restatement of the goal. "The constraints
define the 1-parameter locus, and the theorem holds on that locus, therefore the
target polynomial is zero modulo the constraints" is exactly what must be
proved. The outline gives no reason the target polynomial lies in the ideal
⟨conK, conL⟩, no substitution order, no factorization. The builder cannot
inherit this and "fill in the gaps" because the gap IS the proof.

**Required fix.** The outline must specify a concrete certification route. Two
options:
  (a) **CAS certificate.** Polynomialize (replace sin/cos of α,β,γ,𝔄 by
      independent symbols sα,cα,…, dropping the unit-circle relations — if it
      vanishes in the free polynomial ring modulo the two constraint polynomials
      it is a fortiori a trigonometric identity). Then show the target
      polynomial reduces to 0 modulo ⟨conK, conL⟩ via an explicit Groebner
      reduction or an explicit exhibited combination
      target = P·conK + Q·conL. **WARNING:** a naive lex Groebner basis over all
      8 sin/cos variables timed out in my test (>2 min). The builder MUST use a
      cheaper route: e.g. solve conK for one linear variable (say sγ or cγ)
      explicitly — conK is *linear* in sγ,cγ because the direction offset enters
      linearly — substitute into the target, and similarly use conL. The
      constraints are linear in the trig functions of the constrained angles, so
      elimination should be cheap. The outline should say this.
  (b) **Synthetic angle chase (the listed fallback).** Currently "not yet
      worked out." If the builder cannot certify (a), this must become a real
      proof, not a fallback bullet. The target ∠A'BC = ∠BCA' should be chased
      using the six directions; the outline should at least sketch the two
      expressions.

Pick one and commit; do not leave step 6 as "it vanishes."

### 2. Eq K / Eq L are under-specified

The written Eq K contains an undefined angle χ ("sin(α+γ−C+χ)") and a vague
"analogous relation (Eq L) of the same shape." The builder cannot use an
equation with a free symbol. The two constraints are simply the cross-product
incidence conditions

  conK = (K − C) × dir(CK) = 0,    conL = (L − N) × dir(NL) = 0,

each *linear* in (sγ,cγ) and (sβ,cβ) respectively. The outline should state them
in this clean cross-product form (the trig-Ceva framing is optional packaging
and currently obscures more than it reveals). Drop χ.

### 3. 1-parameter structure and use of the constraints — OK

Concern #3 checks out. The three angle equalities define α,β,γ and the six
directions (each equality is consumed by parametrizing a direction pair). That
leaves two *incidence* constraints (K∈CK, L∈NL) = Eq K, Eq L, on three
parameters → 1 free. The proof does genuinely use Eq K/Eq L (they are the locus
defining equations, not assumed). This is correct; no change needed, but the
builder must make sure the parametrization in step 3 is built from BK∩MK and
BL∩CL only (two lines each), with CK and NL reserved as the constraints — the
outline already warns about this ("Don't re-parametrize K by all three lines");
good.

### 4. Branch / orientation — mostly OK, one hardcoding to relax

The outline hardcodes "NL dir = 𝔄 − β" (clockwise). This is correct for the
standard placement (AB on +x, C above the axis so NB is clockwise from NC), and
my numerical solve using the sign-aware "rotate NC toward NB" confirms it. The
builder should keep the standard placement (A at origin, AB on +x, C in upper
half-plane, 0<𝔄<π) and state that in this frame all the sign choices
(BK=π−α, BL=π−α−β, CL=𝔄+π+α, CK=𝔄+π+α+γ, MK=γ, NL=𝔄−β) are forced. Do NOT
claim generality for an arbitrary un-oriented triangle; the frame is part of the
proof. The interior-angle range 0<α, 0<α+γ<C, 0<α+β<B must be stated to keep
sines positive (no sign flips in trig Ceva / cross products). Also note: my
solver found spurious extra branches (β ≈ 204°, 1283°) that also satisfy the
incidence equations; the identity holds there too (good, it's more general), but
the *interior* branch is what the problem states, so the construction must
verify K∈△BMC, L∈△BNC, K∈∠LBA, L∈∠ACK explicitly.

### 5. Continuity hand-wave for degenerate limits

Step "Cases to cover" dismisses α→0 limits "by continuity." For a proof-only
Olympiad problem with a fixed nondegenerate configuration this is acceptable,
but the builder should note the configuration is *open* (strict inequalities),
so the identity need only hold on the open set — no limit argument is actually
required. Remove the "follows by continuity" phrasing; it invites a
non-rigorous reading of a step that needs no limit.

---

## Summary for the builder

- Spine (antipode + homothety reduction, A'=perp(K)∩perp(L), the linear system
  A'·K=|K|², A'·L=|L|², the formula A'=(|L|²JK−|K|²JL)/(K×L), and the target
  identity (*)): **all correct, verified. Build on this.**
- **Before filling in step 6, decide and state the certification route.** The
  cheap path: write conK, conL as cross-product incidences (linear in sγ,cγ
  and sβ,cβ), eliminate those four trig variables by direct substitution
  (linear solve), and simplify. Do NOT run an unconstrained 8-variable Groebner
  basis — it will not finish. If the linear-elimination simplification does not
  collapse to 0 by hand, produce a CAS certificate and include it.
- Rewrite Eq K/Eq L as the two cross-product equations; remove χ.
- Keep the standard oriented frame; state the interior-angle range; verify
  interior placement of K,L.
- If the algebra truly resists, the synthetic fallback (chase
  ∠A'BC = ∠BCA') must be promoted to a real proof — do not leave it as an
  unworked bullet.

The technique is right; the gaps are in specification of the hardest step.
Fixable, so: **CHANGES REQUESTED**.
