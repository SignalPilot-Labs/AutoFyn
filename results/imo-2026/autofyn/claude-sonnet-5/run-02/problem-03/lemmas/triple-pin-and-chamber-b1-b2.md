## Triple-Pin and Chamber B1/B2 chambers (n=3, m=4, case (b2) box)

**Source:** `lp-duality-certificate`, round 24, §R24.3.

**Triple-Pin (composition (2,0,0,0)).** Split p1 into v1=p2, v2=p3,
v3=p1-p2-p3 (two cuts); p2,p3,p4 untouched. Feasible iff p1 > p2+p3
(within case (b2)'s box, p1<T/2, so v3<p4 automatically once v3>0).
  Φ_TriplePin(p) = T - p1.
Proof: the two p2's and two p3's cross-cancel by odd-run-reduction,
leaving M'={p4,v3}; order p4>v3 holds automatically in-box; A(M')=
p4-v3 = p4-p1+p2+p3, giving Φ=(T+p4-p1+p2+p3)/2 = T-p1.

**Chamber B1/B2 (composition (1,0,1,0), completes round-23's Chamber B,
which had only one of two sub-cases).** Split p1 -> (p2, p1-p2); split
p3 -> (p3-(p1-p2), p1-p2). Requires p1>p2 and x:=p2+p3-p1>0 (i.e.
p2<p1<p2+p3). Two exhaustive sub-cases on x vs p4:
  - B2 (x>p4, i.e. p1<p2+p3-p4): Φ_B2(p) = p2+p3.
  - B1 (x<p4, i.e. p1>p2+p3-p4): Φ_B1(p) = p1+p4.
The two ranges tile (p2, p2+p3) exactly (shared boundary p2+p3-p4>p2
since p3>p4).

**P1P2-tied-to-p3 (composition (1,1,0,0)).** Split p1->(p3,p1-p3),
p2->(p3,p2-p3); requires p2>=2p3. Φ(p) = p1+p3.

**Proof-reviewer independent re-verification.** Wrote 3 independent
exact-`Fraction` scripts (20,000 random trials each, not the builder's
own): Triple-Pin, zero mismatches; Chamber B1/B2 (after catching and
fixing the reviewer's own first-draft script bug — it initially
double-counted p1's untouched-versus-split value, a self-caught error,
not a proof error — 14,932 in-feasibility-region trials, zero
mismatches once corrected); P1P2-tied-to-p3, zero mismatches (4,962
trials). All three formulas and feasibility regions confirmed correct.

**Certification.** CERTIFIED — all three chamber types, n=3 (m=4)
specific, unconditional within their stated feasibility regions.
