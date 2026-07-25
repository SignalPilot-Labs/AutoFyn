# Lemma (reduction of OM=ON) — CERTIFIED (round 1, proof-reviewer)

**Statement.** Let ω = ⊙(AKL) with circumcentre O and radius R, and let M, N be the
midpoints of AB, AC. Put c = AB, b = AC. Then, with A taken as the origin (so M = B/2,
N = C/2),

  OM = ON  ⟺  O·(B − C) = (|B|² − |C|²)/4  ⟺  pow(B,ω) − pow(C,ω) = (c² − b²)/2.

(Equivalently, without fixing the origin: OM = ON ⟺ pow(M,ω) = pow(N,ω), and when M,N lie
strictly inside ω between A and the second intersections X = AB∩ω, Y = AC∩ω, this reads
c·MX = b·NY.)

**Proof.** With A = 0, M = (A+B)/2 = B/2 and N = C/2. Then
  OM² − ON² = |O − B/2|² − |O − C/2|²
            = (|O|² − O·B + |B|²/4) − (|O|² − O·C + |C|²/4)
            = −O·(B − C) + (|B|² − |C|²)/4.
Since OM,ON ≥ 0, OM = ON ⟺ OM² = ON² ⟺ O·(B − C) = (|B|² − |C|²)/4.

Power form: for any P, pow(P,ω) = |P−O|² − R² with R = OA = |O| (A on ω). Hence
pow(B) − pow(C) = |B−O|² − |C−O|² = |B|² − |C|² − 2O·(B−C). Substituting the criterion
gives pow(B) − pow(C) = (|B|²−|C|²) − (|B|²−|C|²)/2 = (c²−b²)/2. ∎

This is elementary and unconditional (no interiority needed for the first two forms). The
c·MX=b·NY form requires M,N strictly inside ω between A and X,Y (a configuration fact).

**Certified by:** proof-reviewer, round 1. Independently checked (algebra elementary;
numeric confirmation 2·O_x = M_x+N_x across the admissible family). Proved identically as
"Lemma 1" of `pow-reduction-trig` and "Lemma R / Step 1" of `synthetic-sigma-spiral`.
