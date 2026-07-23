## imo-2026-04 (Mulan's Triangle Game) — arithmetic "guaranteed-constant set" lens

### Setup recap (not new — for context)
Answer is settled: Mulan wins iff θ=180/m, m∈ℤ≥2. ⊇ and θ>90 impossibility are certified
(`lemmas/cevian-split-normal-form.md`, `lemmas/construction-180-over-m.md`,
`lemmas/device-classification-theta-gt-90.md`). The single open gap is ⊆ for 0<θ<90,
180/θ∉ℤ: Shan-Yu survives forever. Both live approaches (`and-or-closure-rank-induction`,
`transcendence-genericity-invariant`) reduce this to a "self-restoring safe-set" closure and
both get stuck at the same obstacle: the **x=c−B "algebraic collapse"** move, where Mulan cuts
a transcendental vertex A at x = jθ−B (B a transcendental neighbor), sending child2's P-angle
to the exact constant jθ while child1 keeps a "mixed" state {x, B, 180−jθ} — x,B transcendental
but algebraically related (x+B=jθ), and 180−jθ a genuine algebraic constant that is NOT itself a
multiple of θ. The prior transcendence-degree invariant ("has a transcendental angle") cannot
certify child1 stays safe going forward, because further cuts can chip away at x or B using the
now-present constant 180−jθ as a new "anchor."

### The reframing: forcing values as a ℤ-module quotient invariant

Define, as both approaches already do, the **forcing-value set** G ⊆ (0,180): v∈G iff every
triangle with an angle = v lies in W(θ) (Mulan wins from it, for ANY values of the other two
angles). Both approaches prove, unconditionally in θ (no need for 180/θ∈ℤ):
- θ∈G (trivial, W₀);
- **G+G⊆G** (split the (s+t)-vertex at x=s, using the SAME context-free cut regardless of the
  neighbors);
- hence **{mθ : m≥1, mθ<180} ⊆ G always** (this is the "peel" gadget — it does NOT require
  180/θ∈ℤ; that hypothesis is only needed for *seeding a multiple into both children
  simultaneously*, not for peeling a multiple down to θ once it exists in one child).

The natural conjecture (both approaches' real target, stated but not closed) is **G = {mθ:m≥1}
exactly** when 180/θ∉ℤ. My reframing recasts *why* this should be true, and — more importantly —
gives the induction a genuinely different bookkeeping device than transcendence degree:

**The ℤ-module M := ℤ + ℤθ ⊂ ℝ, graded by the "θ-coordinate."**
Every constant (algebraic-over-ℚ(θ)) angle value that appears via the game's *context-dependent
collapse move* (x chosen as jθ−B, or any composition thereof) lands in M = ℤ+ℤθ, i.e. is of the
form a+bθ for integers a,b. (This is because 180∈ℤ and the only "constant-injecting" operation
identified so far is subtracting/adding θ or 180 via the supplementary-P-angle mechanism —
NOT arbitrary field operations.)

- If θ is **irrational**: 1,θ are ℚ-linearly independent, so the representation a+bθ is unique.
  Define π: M → ℤ by π(a+bθ)=a (quotient by the subgroup ℤθ). The dangerous set {mθ:m≥1} is
  exactly π⁻¹(0) ∩ ℝ_{>0}. **180/θ∉ℤ ⟺ π(180)=1≠0.**
- If θ is **rational** = p/q (lowest terms): M = ℤ+ℤ(p/q) = (1/q)ℤ (since gcd(p,q)=1), and
  ⟨θ⟩=(p/q)ℤ. π: M → M/⟨θ⟩ ≅ ℤ/pℤ, sending k/q ↦ k mod p. Dangerous set = π⁻¹(0)∩ℝ_{>0}.
  **180/θ∉ℤ ⟺ p∤180 ⟺ π(180)≠0 in ℤ/pℤ.**

Both cases unify: **π(180) ≠ 0 exactly captures "180/θ∉ℤ."**

**Supplement-nonvanishing lemma (verified, one line, matches Lemma D combo-4 of both live
approaches but now purely arithmetic).** A single cut's two P-angles p,q satisfy p+q=180 exactly,
so π(p)+π(q)=π(180)≠0. Hence **p,q cannot both be 0 in the quotient** — i.e. cannot both be
(positive) multiples of θ — whenever 180/θ∉ℤ. Checked numerically for θ=50,72,40,80 (all give
180/θ = 18/5, 5/2, 9/2, 9/4 — never an integer, confirming m1+m2=180/θ has no integer solution,
i.e. the two P-angles can never simultaneously be positive-integer multiples of θ). This is a
strictly cleaner restatement of Lemma D's case (4) — it makes the "why 180 not 90" mechanism a
one-line group-theory fact instead of four case-by-case eliminations.

### Does this survive the x=c−B collapse where the naive invariant failed?

**Yes, in the sense that it correctly re-derives child1's safety in the collapse example**:
child1 = {x, B, 180−jθ}. The constant here is 180−jθ = 1·180 + (−j)θ, i.e. π(180−jθ) = π(180) ≠ 0
— NOT in the kernel, i.e. NOT a multiple of θ. So the invariant "no angle's π-image is 0" is
preserved by child1 (its one constant angle is safely off the dangerous ray), exactly matching
what the transcendence-degree invariant could only assert weakly ("child1 is safe because it's
not literally θ" — true but not obviously self-sustaining). The module/quotient framing gives a
QUANTITATIVE reason child1 stays off-target permanently under further peeling: peeling only ever
shifts a constant by ±θ (changes b, not a in the a+bθ coordinates, i.e. π is invariant under
±θ shifts) or, via a fresh collapse on child1's OTHER vertex, shifts by a multiple of θ using a
DIFFERENT neighbor as anchor — but every single new collapse still splits π(180)≠0 into two
summands that can't both vanish, by the same lemma applied one level deeper. This suggests an
induction on the NUMBER of already-constant angles / the "π-nonzero forever" property, rather
than on transcendence degree — a genuinely different bookkeeping axis from what both live
approaches use.

**Where it does NOT yet close the gap (the honest remaining difficulty):**
1. **Denominator-escaping moves.** The module M=ℤ+ℤθ is not closed under moves like x=c/2 for a
   constant c (halving introduces (1/2)ℤ-coefficients). I checked by hand: for θ irrational and
   c=a+bθ with a≠0 (safe), c/2 = a/2+(b/2)θ equals mθ only if a/2=(m−b/2)θ, forcing θ rational
   (contradiction) unless a=0 — so halving a safe constant stays safe, for θ irrational. The
   rational-θ case needs a parallel (mod-p, careful with denominators) argument — NOT done here,
   flagged as a genuine sub-case to close.
2. **Arbitrary x, not of "peel" or "collapse" form.** The module argument only tracks angles that
   arise via the SPECIFIC operations {+θ, −θ, supplement (180−·), halving}. A fully general x
   (e.g. an arbitrary real chosen by Mulan with no simple relation to previous constants) could in
   principle inject a constant NOT lying in the ℤ[1/2]+ℤ[1/2]θ closure — need to show any such x
   that produces a genuinely NEW dangerous constant must, in fact, be forced through the
   supplement/peel mechanism (i.e. any P-angle equal to mθ is, BY DEFINITION of the cevian
   formula, either x, A−x, 180−x−B, or x+B — always an affine ℤ-combination of x and the
   pre-existing angles A,B,C — so if A,B,C are already confined to M (or its ℚ-span), x itself
   is the only "free" parameter, and demanding a P-angle = mθ pins x to an M-element automatically).
   This suggests the module-closure claim is actually easier to establish than first appears
   (constants are forced to be affine in x, and Mulan controls x, but the RESULTING constant's
   π-image is determined algebraically) — worth the outliner's attention as a possible shortcut
   past the "arbitrary x" worry.
3. **Multi-generation compounding is still not fully checked.** I did NOT verify (nor should I,
   per scope) that iterating the collapse+peel moves through many generations, with Shan-Yu
   adversarially discarding, never accumulates enough algebraic structure to defeat the invariant.
   The module/quotient recasting is a candidate SHARPER invariant than transcendence degree, not
   a finished proof.

### Distinct openings for the outliner (this lens's contribution)
1. **Replace the transcendence-degree invariant with the ℤ-module quotient invariant** π:
   M=ℤ+ℤθ → M/⟨θ⟩, dangerous = ker(π)∩ℝ_{>0}. Prove by strong induction (on move count, or on a
   well-founded measure like "number of constant angles present") that the invariant "every
   constant angle of T has π-image ≠0" is preserved by at least one child of every split, given
   180/θ∉ℤ. This is a strictly more refined bookkeeping device than "transcendental vs algebraic"
   — it tracks WHICH constant, not just whether an angle is constant, which is exactly what's
   needed to see through the x=c−B collapse (§ above shows it succeeds on the one documented
   collapse instance).
2. **Reduce further: show every P-angle Mulan can ever pin to a specific target is an affine
   ℤ-combination of x and the current triangle's angles** (see point 2 above) — this could let the
   outliner sidestep "arbitrary x" worries entirely by observing the game's constant-injecting
   power is always mediated through the same {±θ, 180−·} operations, i.e. G's structure as an
   additive semigroup (already proven G+G⊆G) is the ENTIRE story, and G=⟨θ⟩⁺ (positive part of
   the cyclic group generated by θ inside M) is forced by π(180)≠0 alone, without needing a
   separate transcendence argument at all.
3. **Fold the θ-rational and θ-irrational cases into one statement** via M/⟨θ⟩ (≅ℤ or ≅ℤ/pℤ) —
   this uniformly explains why 180/θ∈ℤ is exactly the boundary in BOTH cases, which the existing
   approaches handle somewhat separately (they mostly work with θ irrational intuition / generic
   transcendental start, and note but don't unify the rational case).

### Candidate technique(s)
Group/module-theoretic quotient invariant (π: ℤ+ℤθ → (ℤ+ℤθ)/⟨θ⟩) replacing the transcendence-
degree bookkeeping; combined with the already-certified device-classification (Lemma D) and
forcing-value semigroup (G+G⊆G, θ∈G) from `and-or-closure-rank-induction`. This is a refinement
of, not a replacement for, the existing framework — it should be presented as strengthening the
SAME approach's safe-set S, not a fourth rival approach.

### Cheap-kill candidates
- The supplement-nonvanishing lemma (π(180)≠0 ⟹ two P-angles can't both vanish in the quotient)
  is a cheap, fully rigorous one-liner that should replace Lemma D's 4-case elimination for the
  θ<90 sub-case — same content, cleaner and directly generalizable to multi-step induction.
- None obvious yet for closing the full multi-generation induction (that's the real remaining
  work, not a cheap kill).

### Knowledge-base entries to use
- **Invariants & monovariants** (combinatorics section, as flagged by round-2 explorer) — this
  quotient-map invariant is a concrete instance: an algebraic (module-quotient) invariant instead
  of a numeric monovariant.
- No KB entry specifically for ℤ-module/quotient game invariants; this is being built from
  scratch, informed by the standard "supplementary angle" cevian formula already certified in
  `lemmas/cevian-split-normal-form.md`.

### Analogous past problems (cruxes)
Re-scoped from round-2's search (games-and-strategy / processes-and-algorithms subtopics; no new
geometry-forcing-game cruxes found). `aimo-0236`'s general PATTERN — "defender maintains a
valuation/invariant that a forced move cannot simultaneously violate in both branches" — is
structurally the right template for the induction here (already flagged in round 2), but its
specific p-adic content still does not transfer; the analog here is a module-quotient valuation
(the a-coordinate in ℤ+ℤθ, or the mod-p residue), not a p-adic order. No closer match found for
this specific supplementary-angle-splitting mechanism.

### Prior progress
Per `current.md`: ⊇ and θ>90 impossibility fully certified. The ⊆ survival gap (0<θ<90,
180/θ∉ℤ) is open in both live approaches, both citing the same x=c−B collapse as the blocker.

### Dead ends (do not retry)
- **explicit-shanyu-peel-potential's "dyadic 90/θ" claim** — already refuted (RETHINK verdict,
  round 2); do not resurrect.
- **Pure transcendence-degree invariant (has a transcendental angle) as the sole safe-set
  criterion** — proven insufficient by both live approaches (the x=c−B collapse defeats it). The
  module-quotient refinement above is offered as a strictly finer replacement, not a new attempt
  from scratch — the outliner should graft it onto `and-or-closure-rank-induction`'s existing
  safe-set S rather than restart.

### Small-case / intuition notes
- **Verified (exact `Fraction` arithmetic, seconds):** for θ∈{50,72,40,80} (all 180/θ∉ℤ), the
  equation m1+m2=180/θ has no integer solution, confirming the supplement-nonvanishing lemma
  numerically for the specific denominators these round-2 counterexample searches used. For
  θ∈{60,36,90,45,180/7} (all 180/θ∈ℤ), the same check correctly flags them as the winnable
  (skip) case. This is consistent with, and gives an arithmetic explanation for, the reviewer's
  exhaustive forced-win search results (winnable exactly for 180/θ∈ℤ≥2).
- **Conjecture (structural, not yet proven):** G = {mθ:m≥1}∩(0,180) exactly when 180/θ∉ℤ, i.e.
  the forcing-value semigroup literally IS the module-quotient kernel's positive part — this
  restates the whole ⊆ direction as "the semigroup generated by θ under the game's operations
  doesn't leak outside ⟨θ⟩⁺," which is a clean, checkable target for the next round's induction.
