# Proof-reviewer report — imo-2026-02, round 1

Problem: prove OM=ON, O=circumcentre(AKL), under angle conditions E1–E3. No final
answer to verify (pure proof). All three approaches self-reported `partial` — accurate.

## Independent verification I performed
- Re-derived symbolically (sympy): power-of-point L1 midpoint formulas, L2 reduction
  `pow(B)−pow(C)−(AB²−AC²)/2 = 2(pow(M)−pow(N))`, and complex L1
  `|OM|²−|ON|² = O+Ō−(a+ā)/2`. All reduce to 0 identically.
- Built a from-scratch PHYSICAL configuration (trig parametrization, θ∈{0.15,0.25,0.35}):
  K,L land inside the triangle, E1,E2,E3 all satisfied to ~1e-13, and OM=ON AND the core
  identity both hold to machine precision. This confirms (a) the theorem is TRUE, (b) the
  shared reduction is the true theorem, (c) the trig closing relations E2′,E3′ are correct.
- Adversarial branch check: a magnitude-only angle solver lands on spurious below-BC
  branches where OM≠ON. The orientation constraints ("K inside ∠LBA", "L inside ∠ACK")
  are load-bearing — they select the physical branch. Any final closing argument MUST use
  them; a branch-blind CAS elimination will fail (exactly the wall the trig/complex
  approaches hit).

## Per-approach verdicts

### power-of-point-BC — CHANGES REQUESTED (Status: partial) — CORRECT
Scores: Correctness 10/10 (of what is proven), Rigor 9/10, Progress 8/10.
Steps 1–3 (L2a, L1, L2) and L4 are gap-free and independently re-verified. The recorded
Status `partial` is accurate; no overclaim.
SINGLE REMAINING GAP: the **core identity** `pow(B,ω)−pow(C,ω)=(AB²−AC²)/2` is unproven.
Equivalent to pinning the second intersections `A'=AB∩ω`, `A''=AC∩ω`. The inscribed-angle
relations the file lists are automatic from concyclicity and do NOT inject E1–E3 — they
are necessary but not sufficient. Next round: attempt Law of Sines in △BA'K / △CA''L
closed against the cevian lemma L4, actually using θ,β,γ.

### trig-lawofsines — CHANGES REQUESTED (Status: partial) — CORRECT
Scores: Correctness 9/10, Rigor 8/10, Progress 8/10.
The parametrization, cevian formulas, reduction (T), and the closing relations E2′,E3′ are
correct — I confirmed E2′,E3′ reproduce the exact physical config. Status `partial`
accurate.
SINGLE REMAINING GAP: prove identity (T) from E2′,E3′. Currently NUMERIC ONLY. The build
correctly diagnoses that naive Gröbner ideal-membership fails on the spurious γ↦γ+π
branch. Next round: substitute the physical closed-form (cos2γ,sin2γ) solution of the
linear-in-2γ form of E3′ (sign fixed by 0<γ<C−θ), same for β, into (T), and simplify to 0
— a determinate single-variable-in-θ identity over a symbolic triangle.

### complex-swap-symmetry — CHANGES REQUESTED (Status: partial) — CORRECT
Scores: Correctness 8/10, Rigor 7/10, Progress 7/10.
L1 is clean and correct (certified). The circumcentre formula is correct. Status `partial`
accurate. TWO gaps: (i) L2 (the reality encoding of E1–E3) is NUMERICALLY PINNED, not
proven — its sign/handedness is inferred from "what the numeric solver returns"; this is
evidence, not a from-scratch derivation, so it is NOT gap-free. (ii) The crux `Tnum=0` is
50-digit numeric only; the exact saturation Gröbner certificate did not compute. Both are
real gaps.
SINGLE MOST IMPORTANT GAP: give L2 a rigorous directed-angle derivation (mod-π reality
follows from directed angles; the handedness must be argued from the containment
hypotheses, not from numerics), THEN attempt the saturation of (R1,R2,R3) by
D·(a±1)(k±1)(l±1) and reduce Tnum.

## Lemma certification
CERTIFIED (written to `results/imo-2026-02/lemmas/`):
- `reduction-power-to-core.md` — L2a + L1 + core reduction. Shared, highest-value.
- `cevian-lengths.md` — L4 (BK, CL). Elementary Law of Sines, gap-free.
- `complex-OM-ON-reduction.md` — complex L1 (`OM=ON⟺Re(O)=Re(a)/2`). Gap-free.

REJECTED:
- complex-swap-symmetry L2 (sign-correct reality encoding of E1–E3): the "∈ℝ" (mod-π)
  part is a legitimate directed-angle fact, but the product-vs-quotient handedness that
  makes it load-bearing was determined by numerics ("the solver returns..."), not proved.
  Fails the gap-free bar. Re-derive from the containment hypotheses to promote.

## Field-level note for next round's outliner
All three approaches share ONE wall: injecting E1–E3 into a cleanly-reduced identity.
power+trig are close (both bottom out on pow(M)=pow(N) / the coupled θ,β,γ system);
complex is the genuinely different object but its crux is likewise unclosed. The load-
bearing insight the reviewer surfaced: the orientation/containment constraints are what
select the physical branch and MUST enter the closing argument. Consider seeding a
genuinely different framing (Miquel point / spiral similarity tying K,L,A',A'') so the
field is not three variations hitting the same branch-selection wall.
