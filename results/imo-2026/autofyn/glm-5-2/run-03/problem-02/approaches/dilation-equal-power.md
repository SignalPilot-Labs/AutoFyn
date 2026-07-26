## Status
unsolved

## Target
Prove OM = ON (M,N midpoints of AB,AC; K,L as in the statement; O = circumcenter of △AKL).

## Outline (dilation + power of a point — a transformation route)

This approach attacks via a *different reduction* than the cyclicity route: it
reframes the conclusion as an EQUAL-POWER statement of B and C with respect to
a dilated circumcircle, and chases that with power-of-a-point (not an angle
chase for concyclicity).

**Setup.** Let D = dilation centered at A, factor 2: D(M)=B, D(N)=C,
D(K)=K* (A,K,K* collinear, AK*=2·AK), D(L)=L* (similarly). Let O* = D(O).
Because D is a similarity, D sends the circumcircle of △AKL to the circumcircle
of △AK*L*, and sends its center O to O* = circumcenter of △AK*L*.

**Reduction of the conclusion.**
OM = ON  ⟺  O ∈ perp-bis(MN).
Since D carries perp-bis(MN) to perp-bis(BC) (D is a similarity sending M→B, N→C):
  OM = ON  ⟺  O* ∈ perp-bis(BC)  ⟺  O*B = O*C.
Because O*A = O*K* = O*L* = R* (circumradius of △AK*L*):
  O*B = O*C  ⟺  |O*B|² − R*² = |O*C|² − R*²
            ⟺  Pow_{(AK*L*)}(B) = Pow_{(AK*L*)}(C).
[This equivalence is elementary and exact; nothing to prove here.]

So the whole problem becomes:
  **CLAIM P.**  B and C have equal power with respect to the circumcircle of △AK*L*.

**Translating the angle conditions under D.** D fixes A and sends M→B, N→C.
The three angle equalities become statements about the *dilated* configuration
(A, B, C, K*, L*), with the original auxiliary points B,C,M,N now reinterpreted:
  (i)   ∠KBA = ∠ACL          — note B,C are FIXED by D (D fixes lines through
        external points? No — D moves points, but B,C are not images of
        anything under D; they are original points, D does NOT fix them).
        Careful: D sends M→B, N→C, K→K*, L→L*. The angle conditions involve the
        ORIGINAL points B, C, M, N, K, L. Under D they involve D(B), D(C)?  No:
        D is only applied to {M,N,K,L,O} (and A fixed). B, C are left in place
        because they are not in the domain of the dilation we use to redefine
        the picture. So the conditions rewrite as:
        (i)  ∠KBA = ∠ACL  →  ∠K* B' A = ∠A C' L*   where B' = D(B)=2B, C'=D(C)=2C
             (D sends the *ray* BK to the ray B'K*; BA to B'A; CL to C'L'; etc.)
        (ii) ∠LBK = ∠LNC  →  ∠L* B' K* = ∠L* C K*   (N→C under D)
        (iii)∠LCK = ∠BMK →  ∠L* C' K* = ∠(at B between B' and K*)  (M→B under D)
  [GAP-1: write the transformed conditions cleanly. The auxiliary points
  B'=2B, C'=2C appear; this is the bookkeeping risk noted by the explorer.]

**Strategy for CLAIM P (equal power).** Equal power of B and C wrt circle(AK*L*)
is equivalent (by the secant-tangent / power-of-a-point converse) to either:
  (P1) the radical axis of (AK*L*) and a circle through B,C symmetric wrt
       perp-bis(BC) passes through... [messy], OR
  (P2) B and C subtend supplementary / equal angles at the chord A K* (or A L*),
       i.e. ∠AK*B + ∠AK*C relations — NOT generally true, skip, OR
  (P3) the chord K*L* of circle(AK*L*) is seen from B and C under angles that
       combine, via (i)-(iii), to give equal powers.

The cleanest power-of-a-point route: compute
  Pow(B) = BK* · BQ  where Q = second intersection of line BK* with circle(AK*L*),
  Pow(C) = CL* · CR where R = second intersection of line CL* with circle(AK*L*),
and show BK*·BQ = CL*·CR. [GAP-2: this is the load-bearing computation.]
The angle conditions (i)-(iii) rewritten under D should give, via the inscribed-
angle theorem applied in circle(AK*L*), explicit values for ∠(BQ, BA) and ∠(CR, CA)
in terms of α,β,γ, which then feed a sine-rule computation of BQ and CR.

Mechanism (one-line reason to verify): under D, condition (ii) becomes
∠L*B'K* = ∠L*CK* — i.e. the chord K*L* of circle(AK*L*) is seen from B' and from
C under equal angles, so B' and C lie on a circle through K*,L*; combined with
condition (i) (which ties ∠K*B'A to ∠AC'L*) and the fact that A,K*,L* are on the
circle, this should force the second intersections Q,R to land symmetrically
enough that BK*·BQ = CL*·CR. The midpoint origin of B', C' (=2B, 2C from A) is
what makes the lengths match.

**Fallback within this framing:** if the secant computation is intractable, use
the radical-axis form (P1): exhibit a second circle Γ through B and C (e.g. the
circle with BC as chord and center on perp-bis(BC), for instance the circle
through A,B,C = circumcircle of ABC) and show the radical axis of (AK*L*) and
Γ is exactly perp-bis(BC) by showing two points on it are equidistant from B,C.
[GAP-3: pick Γ and verify.]

## Gaps
- GAP-1: clean statement of the three angle conditions under D(A,2), with the
  auxiliary points B'=2B, C'=2C handled without bookkeeping errors.
- GAP-2 (THE crux of this route): compute Pow(B) and Pow(C) wrt circle(AK*L*)
  via second intersections and show equality using (i)-(iii) and sine rule.
- GAP-3 (fallback): if direct power computation fails, identify a second circle
  Γ through B,C whose radical axis with (AK*L*) is perp-bis(BC).

## Cases to cover
None.

## Watch out for
- B'=D(B)=2B and C'=D(C)=2C are NOT the original B,C — easy to conflate. The
  power is taken at the ORIGINAL B,C, but the angle conditions after dilation
  involve B',C'. Keep these distinct.
- This route is genuinely different from the cyclicity route: it never constructs
  A* and never invokes a cyclic quadrilateral converse directly; the load-bearing
  step is a power computation, not an angle-equality chase.
- Do NOT confuse with the (recorded-dead-end) A-centered spiral similarity S_A;
  D is a pure dilation (ratio 2, no rotation), which is benign.
- Verify with the isosceles special case first (B',C' symmetric, everything
  collapses to a reflection) as a sanity check before chasing the general case.
