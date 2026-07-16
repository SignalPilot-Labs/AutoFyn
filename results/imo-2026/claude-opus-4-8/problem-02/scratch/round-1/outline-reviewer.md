# Outline Review — imo-2026-02 (Prove OM = ON)

Round 1, empty population. Four rival complete attempts submitted. I independently
re-verified every reformulation the field rests on against a valid configuration
(scalene A=(0.5,1.5), B=(0,0), C=(2,0), α=15°) using verify_config.py helpers.

## Numerical audit of the shared reformulations (all confirmed)

- OM = ON: 0.51036 = 0.51036 ✓
- pow(B,⊙AKL) − pow(C,⊙AKL) = (AB²−AC²)/2: −1.0000 = −1.0000 ✓
- Antipode A* = 2O−A: A*B = A*C = 1.02072 ✓; with A at origin, A*·(B−C) = −1.0 = (AB²−AC²)/2 ✓
- Cevian cot formula: cot∠KAB = 9.9021 = cot α + 2cot γ ✓; cot∠LAC = 6.2182 = cot α + 2cot β ✓
- Ratio crux MA′/NA″ = 1.34164 = b/c ✓
- Complex reality conditions C1, C2, C3 all real (Im ~1e-15) ✓

Every approach is anchored to a true, machine-precision reformulation. None repeats a
recorded dead end (concyclicities / spiral similarity — none of these approaches use them).
No approach is a slice of another: each targets OM = ON end to end. So no RETHINK.

---

## Per-approach verdicts

### trig-decoupled-bash — APPROVE
Technique sound: coordinates + law of sines, reduce OM=ON ⟺ O_x = (M_x+N_x)/2 via MN∥BC,
then a trig identity. The **decoupling** of constraints (I) [α,γ] and (II) [α,β] is a
genuine, numerically-confirmed structural asset that makes the grind tractable — this is
the most-likely-to-close computational route, and it carries a direct O_x fallback if the
cleaner MA′/NA″ = b/c framing stalls.
- Fix while building: (I),(II) have multiple roots — the file already flags this; you MUST
  pin the interior root and justify the selection, not just assert it.
- The "same functional form f by B↔C symmetry" mechanism (balance lemma) is the load-bearing
  claim — make the symmetry substitution explicit, don't assert f is identical.

### power-of-point-balance — APPROVE
Technique sound: pow(M)=pow(N) via secants through A, reducing to MA′/NA″ = b/c (confirmed).
Cleaner, human-readable if the ratio lemma closes. Note: this shares its crux (MA′/NA″=b/c)
with trig-decoupled-bash — they are distinct whole attempts (power/inscribed-angle vs
coordinate O_x), but if that ratio were false both die together; it is not false (verified),
so this is acceptable breadth, but I rank them close and deliberately keep a route that
bypasses the ratio in the build set (see below).
- Fix while building: Step 4 must use directed angles (mod 180°) to locate A′,A″; and Step 3's
  signed-power sign (A′∈(M,B), A″∈(N,C)) must be nailed so the unsigned ratio is the right statement.

### complex-reality-conditions — APPROVE (with a flagged optimism)
Technique sound and fully mechanical: A=0, three reality conditions, eliminate conjugates,
one Im-identity. This is the route that **bypasses the MA′/NA″=b/c crux entirely**, so it is
the field's true breadth insurance.
- **Correction (bookkeeping):** the circumcenter formula's denominator sign is off — I get
  O = (k|l̄|²−l|k̄|²)/(k̄l − kl̄) yielding the *negative* of the true (A-shifted) circumcenter;
  use denominator (k l̄ − k̄ l). Pin with numerics before trusting.
- **Flagged optimism (crux):** the claim "solve (C2),(C3) linearly for k̄,l̄" is too rosy —
  Cᵢ = C̄ᵢ cleared of denominators is degree-2 in the conjugate variables (e.g. (2l̄−c̄)(l̄−b̄)
  carries l̄²), not linear. The elimination is real but heavier than advertised; expect to need
  a resultant/Gröbner elimination discovered in sympy, then transcribed as named steps. Do NOT
  submit CAS output as the proof. This is why I rank it just below the two trig routes.

### antipode-perp-bisector — APPROVE, but HOLD (do not build this round)
The equivalence OM=ON ⟺ A*B=A*C is clean and confirmed, and A* = perp-to-AK-at-K ∩
perp-to-AL-at-L is a correct Thales location. But Step 4 (the synthetic proof of
A*B²−A*C²=0) is the entire difficulty and the outliner itself concedes it may not close
synthetically and may need a trig crutch borrowed from the other routes. Elegant long shot;
registered and kept live, but lower expected payoff this round. Build next round if a
computational route surfaces the identity that Step 4 needs.
- Note: Step 1's scalar form "(B−C)·A* = (AB²−AC²)/2" is an A-at-origin statement (correct as
  such — I verified −1.0 = −1.0 with A translated to 0); keep that framing explicit.

---

## Ranking (applied)

Registered all four (none cut). Head-to-head result:
- trig-decoupled-bash 1529.0
- power-of-point-balance 1514.5
- complex-reality-conditions 1502.4
- antipode-perp-bisector 1454.2

Rationale: all three of {trig, power, complex} beat antipode (tractable-in-principle vs a
long shot that admits it may not close). trig-decoupled > complex (decoupling makes it
tractable; complex's conjugate-elimination is heavier than claimed). trig ≈ power (draw —
shared crux, both clean). power ≈ complex (draw). No copy_approach: no approach has a proven
shared prefix with two viable completions yet.

## Build set rationale
Three parallel routes giving real breadth: **trig-decoupled-bash** (robust computational
safety net, most tractable), **power-of-point-balance** (cleanest human route), and
**complex-reality-conditions** (the one route that bypasses the MA′/NA″=b/c crux, so the
field does not all funnel through one gate — per the plateau-avoidance guidance). Antipode
held for next round.

build set: trig-decoupled-bash, complex-reality-conditions, power-of-point-balance
