# Outline review — imo-2026-04 (Mulan's triangle game), round 1

## Ruling on the contested answer
**The field should back θ = 180°/N (integer N ≥ 2), i.e. 180/θ ∈ ℤ.** The rival
"θ ∈ ℚ·180 ∩ (0,90]" answer is REFUTED, and the discriminator (θ=72°) is airtight.

Decisive mechanism (verified by hand and by computation):
- Cut mechanics confirmed: cutting (A,B,C) from vertex A with x∈(0,A) gives
  Child1=(x,B,A+C−x), Child2=(A−x,C,x+B); the two new P-angles A+C−x and x+B are
  supplementary (sum 180), and B,C are inherited unchanged.
- **Closure lemma is sound.** With safe set S = {no angle is a positive-integer multiple
  of θ}, forcing BOTH children non-safe requires one of A=(n+m)θ, B=(m−n)θ, C=(n−m)θ
  (parent-angle multiples, excluded on S) or A+C−x=nθ ∧ x+B=mθ ⟹ adding gives
  180=(n+m)θ ⟹ 180/θ∈ℤ. So for θ≠180/N Mulan can never force both children non-safe;
  Shan-Yu keeps a safe child forever from start (θ/2,θ/2,180−θ)∈S. I checked all four
  combinations by hand — the split is exhaustive (the only free child angles are x, A±x,
  x+B, A+C−x; B,C are safe by hypothesis).
- **θ=72° test passes for Shan-Yu.** 180/72=2.5∉ℤ, so the closure lemma applies and
  (36,36,108)∈S survives. Grid scan (600k cuts across all three vertices) found NO cut
  making both children non-safe — matches the algebra. Mulan cannot force 2θ=144°. The
  rival's Part C is false.
- Winning side verified concretely: θ=90 supplementary trick (x=90−B ∈(0,A), both children
  90°); θ=36 both-multiples cut x=A+C−nθ gives children carrying nθ and (5−n)θ (e.g.
  n=2 → 72°,108°), then descent. Both check out numerically.

Note the impossibility via the closure lemma covers **all** θ≠180/N uniformly — including
θ>90° and irrational θ — so the rival's (correct) Parts A and B are already subsumed and
nothing is lost by cutting it.

---

## safe-set-invariant — APPROVE
Right technique, both sides sound, gaps are genuine edge-cases and closable.
- Part A (impossibility) is essentially complete and rigorous as written; the 4-case
  closure split is exhaustive and each case lands cleanly. This is the strongest part of
  the whole field and should be treated as the shared certified lemma.
- Part B (sufficiency): the both-multiples cut and the multiplicity descent are correct and
  numerically confirmed. Build-time gaps to close (do NOT hand-wave):
  - **G1**: existence of integer n with C<nθ<A+C for the chosen largest vertex, AND the
    branch where the *starting* triangle already carries a higher multiple jθ (then A+C=nθ
    hides a parent multiple B=(N−n)θ) — route those directly to Phase 2. State x∈(0,A)
    explicitly. Prove largest angle > θ strictly for N≥3 (largest ≥60 ≥θ, ≠θ ⟹ >θ; θ=60
    forces equilateral=win). This is the one real gap.
  - **G2**: positivity of every intermediate angle in the descent and the k=2 terminal
    (both children θ). Straightforward but must be written.
  - **G3**: N=2 realizability of x=90−B∈(0,A) by choosing the vertex opposite the two acute
    angles — verified numerically, just needs the "every triangle has ≥2 acute angles" line.
  - **G4**: state that cuts from B and C give the same four identities by symmetry (no fifth
    case), so the closure argument is vertex-independent.

## force-2theta-bisect — APPROVE (hedge, ranked below)
Same correct answer, same impossibility (imported), winning side reframed as "descend to 2θ
then bisect." Sound, but note: bisecting a 2θ vertex (cut x=θ) IS exactly the k=2 step of
safe-set-invariant's descent, and it shares the same load-bearing chain-entry gap (G1). So
it is not a genuinely independent route so much as an alternate framing / rigor hedge — kept
because a second builder on the winning side is cheap and de-risks the descent write-up.
- Must special-case N=2 (2θ=180° is degenerate — use the direct 90-90 win, not bisection);
  the outline already flags this (G4).
- Do NOT claim chain entry for θ≠180/N — correctly flagged; keep that guard in the proof.

## rational-below-90 — RETHINK / CUT (not registered)
Carries a definitively wrong answer. Part C ("rational θ≤90 ⟹ Mulan forces 2θ") is FALSE at
θ=72° — refuted by the closure lemma above and by the grid scan. Its correct Parts A (θ>90
loses) and B (irrational loses) are already subsumed by safe-set-invariant's closure lemma
(both classes satisfy θ≠180/N), so cutting it loses nothing. Recorded the cut reason in the
approach file's ## Approaches tried. Not registered in the population.

---

## Ranking (this round)
- Registered: safe-set-invariant (1516), force-2theta-bisect (1484).
- Comparison: safe-set-invariant > force-2theta-bisect — the former is a complete self-
  contained two-sided attempt with the impossibility essentially proven; the latter imports
  that impossibility and re-frames the same descent, so it is strictly the more derivative.
- rational-below-90 cut (wrong answer), not ranked.

## Guidance for next round
Both survivors share gap G1 (chain-entry / both-multiples cut from an arbitrary Shan-Yu
start). It is not a plateau yet (round 1) and is numerically confirmed to be closable, so no
bypass is needed now. If G1 resists in a later round, task an explorer with a winning-side
route that does not go through the both-multiples cut.

build set: safe-set-invariant, force-2theta-bisect
