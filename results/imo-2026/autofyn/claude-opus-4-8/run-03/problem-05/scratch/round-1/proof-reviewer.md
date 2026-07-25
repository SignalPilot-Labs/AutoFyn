# Proof review — imo-2026-05 (IMO 2026 P5)

Problem: find all f:ℝ_{>0}→ℝ_{>0} with √((x²+f(y)²)/2) ≥ (f(x)+y)/2 ≥ √(x f(y)).
Claimed answer: f(x)=x+c, c≥0. Confirmed correct (numerically: family satisfies both bounds for
c∈{0,0.3,1,5}; f=2x and a two-valued shift both fail, as the proof requires).

All three candidates share one spine (Lemmas A/C + marching lemma) and differ only in the Section-5
endgame. I re-derived every load-bearing identity independently with sympy and re-checked all
analytic/topological steps by hand. Verdicts below are independent.

## Verified independently (shared core — holds for all three)
- **Section 0 squaring:** √A≥M≥√B ⟺ A≥M²≥B for positive A,M,B; L,R obtained by squaring and ×4. Correct.
- **Easy direction:** both defects = ((x−y)−c)². Verified: R-defect and L-defect each reduce to
  ((x−y)−c)²−0. c≥0 forced by codomain (x→0⁺). No solutions missed — exhaustiveness (below) shows d is
  constant, so the family is exactly {x+c : c≥0}; c is not any real (c<0 leaves ℝ_{>0}), and no non-shift
  solution survives.
- **Lemma A** f(f(y))=2f(y)−y: x=f(y) makes both bounds tight; both sides positive so square roots valid.
  Re-derived, correct.
- **Lemma B** injectivity, **Lemma C** (d(f(y))=d(y), fⁿ(y)=y+n d(y), d≥0): correct; induction and the
  positivity-of-iterates argument for d≥0 are valid.
- **R-test / L-test identities** ((p+2a+q)²−4(p+a)(q+b)=(p−q)²+4(a−b)(p+a), etc.): sympy-verified = 0.
- **Marching lemma (Section 4):** with a>0 the smaller-value orbit marches to ∞ while the other orbit is
  kept within a fixed gap (floor construction), so bounded square < linear→∞. Valid; needs the smaller
  value positive, which is exactly why the {0,b} case is separate. Leaves range(d)⊆{0,b}.

## orbit-crossing — APPROVE (Status: solved)
Endgame: proves F open via L(x,p) (defect quadratic negative on I_p; roots (b+p)±√(4bp+2b²), disc/4
=4bp+2b² verified; p∈I_p verified). Then F open+proper in connected (0,∞) ⇒ not clopen ⇒ ∃ boundary
t∈closure(F)\F, so t∈G; p_n∈F→t; R(x,y) gives (p_n−t)²≥4b p_n → 0≥4bt>0, contradiction. All identities
verified; boundary/limit argument airtight. Minor imprecision: "I_p⊆F" should read "I_p∩(0,∞)⊆F"
(the interval may reach ≤0); does not affect openness of F. Not a gap. Complete and rigorous.

## monotonicity-orbits — APPROVE (Status: solved)
Endgame is the cleanest: L(q,p) gives (p−q)²≥b²+2b(p+q)≥b², i.e. |p−q|≥b for all p∈F,q∈G (identity
verified). Then with δ=min(b,p)/2 both F and G are open (x>p/2>0 keeps points in domain; |x−p|<b excludes
the other set), two nonempty disjoint open sets can't cover connected (0,∞). Fully rigorous. (Note: the
file's "Approaches tried" honestly records that the original monotonicity-first plan was blocked and this
is a separation-based completion — the recorded solved Status is correct.)

## shift-family-sos — APPROVE (Status: solved)
Endgame: L*: (x−p)²−b(2x+2p+b)≥0 forced for x∈G, but the quadratic is <0 on I_p∋p ⇒ F open; R*:
(x−p)²−4bp≥0 forced for p∈F, but <0 on J_x∋x ⇒ G open. Both identities and both center-checks
(b²<2b(b+2p), b²<b(b+x)) verified. Connectedness contradiction. Fully rigorous.

## Connectedness endgame — is it airtight?
Yes. In every version F,G partition (0,∞); the marching lemma+d≥0 guarantee no third value, so F∪G=(0,∞)
with F∩G=∅. Case 3 assumes both nonempty (b=0 handled separately as c=0). Openness is established from
raw inequalities that must hold at every (x,y), and (0,∞) connected forbids a two-open-set partition.
The "open band around a fixed point" is genuine: L at a fixed/shift pair yields a strict quadratic
inequality with two real roots straddling the fixed point, so a whole open interval of would-be shift
points is excluded — L really forces it. No empty-set or boundary loophole: the contradiction is reached
precisely because both sets are assumed nonempty.

## Promotable lemmas — certified (admitted to results/imo-2026-05/lemmas/)
- composite-identity.md (Lemma A) — passes.
- orbit-arithmetic.md (Lemma C) — passes.
- marching-one-positive-value.md (Lemma D + R-test) — passes.
- fixed-shift-separation.md (F/G separation+openness endgame) — passes.

## Actions
- current.md created (reviewer-owned) with Status: solved and the consolidated Full proof.
- record_outcome: verified-milestone for all three slugs.

## Verdicts
- orbit-crossing: APPROVE (solved)
- monotonicity-orbits: APPROVE (solved)
- shift-family-sos: APPROVE (solved)
