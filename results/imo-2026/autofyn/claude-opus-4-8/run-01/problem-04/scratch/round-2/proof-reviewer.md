# Proof-reviewer report — imo-2026-04 (Mulan's Triangle Game), round 2

## Central adjudication: the correct answer is θ = 180°/m, m ∈ ℤ, m ≥ 2

Equivalently **180/θ ∈ ℤ and θ ≤ 90°**. The rival "dyadic 90/θ" characterization (claiming
θ=72°, 80°, 40° winnable) is **WRONG**.

Evidence and reasoning (independently derived):
- **⊇ verified rigorously.** For θ=180/m, one "seed a multiple" move on the largest vertex places
  a multiple jθ in BOTH children (the child-2 P-angle x+B sweeps (B,180−C), an interval that must
  contain a multiple; else all angles ≤ θ ≤ 90, impossible), and "peel" jθ→(j−1)θ→…→θ finishes.
  I re-derived Lemma B and checked its interval condition over m∈{2,…,12} on 200 random triangles
  each (all hold), and re-checked the θ=60 two-move win by hand: (62,59,59)→x=61 gives
  {61,59,60}∈W₀ and {1,59,120}; then bisect 120 → both children contain 60.
- **θ>90 impossibility verified.** Device classification (both children get θ ⟺ θ=90 or vertex
  =2θ) forces W(θ)=W₀; independently, from "all angles < θ" Shan-Yu can always keep a child with
  all angles < θ (forcing both children ≥ θ needs the cut-vertex angle > θ, unavailable). Both
  arguments agree: θ>90 never winnable.
- **Why 180 (not 90) is the modulus:** a cut creates two supplementary P-angles jθ and 180−jθ;
  both are multiples of θ simultaneously ⟺ 180/θ ∈ ℤ. This is exactly the both-children-forced
  device, and it is why 60=180/3, 36=180/5, 180/7, … (odd m) ARE winnable — refuting {90/n} — and
  why 72=90·4/5, 80=90·8/9 are NOT (180/72=2.5, 180/80=2.25 ∉ ℤ).
- **Reduced-game (constant/junk AND–OR) search, exact arithmetic.** From an all-generic start, a
  forced win exists at "depth 1" (one seed move) for every 180/m tested {90,60,45,36,30}; for
  {72,80,40,50,70,54} the sound search found NO forced win. This is a lower bound on Mulan's
  power (a win found is a real win), so it confirms 60/45/36/… winnable; and it finds nothing for
  72/80/40 — matching both integer approaches' independent exact searches.
- The dyadic approach has **no construction** for its extra ground (its G1 is admitted open) and
  its own search on 72 was "inconclusive (budget exceeded)". So there is zero positive evidence
  that 72/80 are winnable, and direct evidence they are not.

**Caveat:** the ⊆ direction for 0<θ<90, 180/θ∉ℤ (Shan-Yu survives against all adaptive play) is
NOT rigorously proven by any approach — it is the shared open crux. So the answer is settled up to
this survival gap; the problem is **not solved**.

---

## Per-slug verdicts

### and-or-closure-rank-induction — CHANGES REQUESTED (Status: partial) ✓ recorded status correct
Scores: Correctness 10/10, Completeness 6/10, Progress 8/10.
- Complete, rigorous ⊇ construction for all m≥2 (fork/interval + peel) — verified.
- Complete θ>90 impossibility via Lemma D — verified.
- Forcing-value semigroup (θ∈G, G+G⊆G) — correct.
- Honestly marks the ⊆ gap: the x=c−B "algebraic collapse" where a child goes fully algebraic yet
  stays safe, which the naive "has a transcendental angle" invariant does not track. This is the
  real crux. Builder's `partial` is CORRECT (no overclaim).
- **Gap to close:** characterize the safe algebraic set 𝒞(θ) and prove S={≥1 transcendental angle,
  no F-angle} (or its enlargement) is closed under Shan-Yu response for 0<θ<90, 180/θ∉ℤ.
Strongest of the three. Route: re-dispatch this builder to attack the survival closure.

### transcendence-genericity-invariant — CHANGES REQUESTED (Status: partial) ✓ recorded status correct
Scores: Correctness 10/10, Completeness 6/10, Progress 8/10.
- Same correct answer θ=180/m. Complete rigorous ⊇ (Lemma A peel + Lemma B seed — I verified
  Lemma B's interval argument in full) and complete θ>90 (device classification).
- Direction III (generic survival) open; framework (algebraic vs transcendental over ℚ(θ),
  invariant P) set up but self-restoration unproven — correctly flags that a pure
  transcendence-degree invariant fails and the metric constraint x∈(0,A) must be combined with the
  algebra. Builder's `partial` is CORRECT.
- Genuinely diversifies from the and-or approach (field-theoretic vs rank-induction), worth keeping
  live. **Gap identical in spirit:** close the self-restoration lemma (combine algebraic bookkeeping
  with the metric interval constraint). Route: re-dispatch to close survival.

### explicit-shanyu-peel-potential — RETHINK (Status: unsolved as an approach to the true answer)
Scores: Correctness 7/10 (sub-lemmas fine, headline conjecture false), Completeness 3/10,
Progress 3/10.
- Its proven pieces are correct: Lemma 0/0′, S1 (90/n construction, a subset of 180/m), the θ=60
  refutation of {90/n}, the device lemma, S2 (θ>90). These are valid but **subsumed** by the two
  integer approaches (which prove the full 180/m construction, not just the even subfamily).
- **Fatal flaw:** its headline "corrected conjecture" — winnable ⟺ θ≤90 and 90/θ dyadic, with
  72,80,40 explicitly claimed winnable — is FALSE. The generator analysis (module
  M=90ℤ[1/2]+θℤ[1/2], "bisection generator v↦v/2") is a broken invariant: bisection is a downward
  step (2v→v), not an upward generator, and the "+θ" generator requires simultaneous control of
  both children, which the supplement obstruction blocks precisely when 180/θ∉ℤ. Continuing to
  build its G1 (dyadic construction for 72,80) and G2 (dyadic survival) is chasing a false target.
- Builder marked `partial`; I DOWNGRADE the approach to RETHINK because its organizing conjecture
  (the target answer) is wrong, so the line cannot reach the solution as set up. Recorded outcome:
  dead-end. Its correct lemmas are preserved via the certified lemma files.

---

## Certified promotable lemmas (written to results/imo-2026-04/lemmas/)
- `cevian-split-normal-form.md` — cevian normal form + AND–OR winning-set characterization. PASS.
- `construction-180-over-m.md` — ⊇ direction: θ=180/m winnable (Lemma A peel + Lemma B seed).
  PASS (statement matches proof; interval argument verified).
- `device-classification-theta-gt-90.md` — both children get θ ⟺ θ=90 or vertex=2θ; hence θ>90
  never winnable. PASS.

REJECTED for promotion: the dyadic "Guaranteed-Constant / module M" lemma (explicit-shanyu) —
statement false (implies 72,80 winnable). The "full characterization Mulan wins ⟺ 180/θ∈ℤ" is NOT
certified as a lemma because its ⊆ half (survival for 180/θ∉ℤ) is unproven — only the ⊇ half and
the θ>90 half are certified.

## current.md
Updated by the reviewer: Status = partial; Current best records the correct answer θ=180/m,
the certified ⊇ and θ>90 results, and the precise open survival gap.
