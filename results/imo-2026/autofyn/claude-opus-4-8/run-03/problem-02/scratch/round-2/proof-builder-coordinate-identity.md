# Proof-builder report — coordinate-identity (imo-2026-02), round 2

## Result: Status = SOLVED

The one remaining gap (the Orientation Lemma) is now closed rigorously. The full proof is
written to `results/imo-2026-02/approaches/coordinate-identity.md` (Status: solved, Full proof
present). The coordinate-free orientation lemma is extracted to
`results/imo-2026-02/lemmas/orientation-sign.md` and PROPOSED for certification.

## What was closed
The round-1 gap: the algebraic engine needs the DIRECTED equations FK=FL=0, but the problem gives
only UNSIGNED angle equalities. Closed via a from-scratch, coordinate-free Orientation Lemma:

- **Lemma B (betweenness sign):** w=βy+γz, β,γ>0 ⟹ cross(y,w), cross(w,z), cross(y,z) share one
  sign (bilinearity). 
- **Lemma I (interior ⟹ positive combination):** X∈int△VYZ ⟹ X−V=β(Y−V)+γ(Z−V), β,γ>0, via
  signed-area barycentrics (α+β+γ=1, all positive ⟺ interior).
- **Fixed reference signs** (parameter-free, from Fact 0 midpoint-halving [NBC]=[MBC]=½[ABC]):
  cross(BA,BC)=−2[ABC]<0, cross(CA,CB)=+2[ABC]>0, cross(NB,NC)=cross(MB,MC)=+[ABC]>0.
- **Four target signs**, each a two-step chain (Lemma I to get a positive combination + Lemma B to
  transport the fixed sign): cross(BK,BL)<0, cross(NC,NL)<0, cross(CL,CK)>0, cross(MB,MK)>0.
- **Directed upgrade:** same sign + equal unsigned magnitude in (0,π) ⟹ literal directed-angle
  equality ⟹ EA=EB=0 with ε=+1.

## Reviewer corrections honored
1. Sign-naming: used cross(NB,NC)=+½h(p+q)>0 (NOT cross(NC,NB)); derived cross(NC,NL)<0 by
   cross(NL,NC)>0 then antisymmetry. Correct target −1.
2. σ-mirror reversal: did NOT transport signs through σ (it is a reflection, flips sign). Proved the
   Condition-B pair (cross(CL,CK), cross(MB,MK) both +) DIRECTLY at vertices C and M. Noted explicitly
   why the sign is + not −.
3. Deleted all "numerical model confirms the directed equality" sentences. Orientation is proved.
4. Scoped the §6 continuity argument strictly to the finite a_K·a_L=0 zero-set; stated it is NOT the
   orientation step.
5. Added the one-line ∠LBA,∠ACK∈(0,π) no-reflex check.
6. Rotation signs in §2 (clockwise BA→BK, CCW CA→CL) now JUSTIFIED by the orientation facts, not
   asserted.

## Independent verification done this build
- `/tmp/verify_engine.py` (sympy, from scratch): EA=u·FL, EB=v·FK (decoupled, FL∈v only quadratic,
  FK∈u only quadratic); leading coeffs a_K=−½(c²+s²)|AB|²W, a_L=½(c²+s²)|CA|²W match (8); pseudo-
  division R1 linear, R2=0; ideal identity a_K·a_L·T−(a_L·QK·FK+QL·FL)=0 residual EXACTLY 0.
- Fixed reference signs and half-vector identities cross(N−B,C−B)=½cross(A−B,C−B): exact-zero
  residual (sympy).
- One interior branch numerically (`/tmp` scan): all four target signs match
  (cross(BK,BL)=cross(NC,NL)<0, cross(CL,CK)=cross(MB,MK)>0). Cross-check only; proof is
  self-contained.

## For the reviewer
- `lemmas/orientation-sign.md` is coordinate-free (cross products / signed areas only) and importable
  by synthetic-sigma-spiral to replace its "[Verified numerically]" sign bullets in Steps 3–4.
  Recommend certifying it.
- The algebraic engine (ideal identity, remainder 0) was independently re-derived from scratch this
  round; not just imported.

## Recommended verdict: APPROVE (Status solved).
The proof is complete: reduction (certified) + orientation (proved, no numerics) + decoupling +
ideal identity (residual 0) + non-degeneracy (finite zero-set scoped continuity) ⟹ T=0 ⟹ OM=ON.
