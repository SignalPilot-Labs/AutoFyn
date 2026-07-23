# Outline review — imo-2026-04, round 1

Note for the orchestrator: `problems.jsonl` lists `imo-2026-04` as `"difficulty_level": "medium"`
(rating 7), not `"hard"`. CLAUDE.md says runs target only the 39 `hard` entries. This run was
already fixed on this problem before I was dispatched, so I reviewed it as instructed, but flag
the mismatch for the record.

## Sanity checks I ran (Bash/python3, before trusting the outline)

1. **Chain lemma S1** (angle = kθ ⇒ Mulan wins in ≤ k−1 moves by shaving a1=θ each round,
   Shan-Yu forced to keep the (k−1)θ-carrying child to avoid instant loss): verified by hand
   algebra on the child formulas. Sound induction, correct base case (k=1 = immediate win).
   Minor: `resonance-lattice-invariant.md`'s written child1 formula "(k−1)θ − Y" is an algebra
   slip (should be Z+(k−1)θ), but it's harmless since child1 already contains θ exactly and the
   lemma doesn't depend on child1's third angle.
2. **One-move universal double-forcing only at θ=90°**: solved the two affine equations
   "child1 hits θ" and "child2 hits θ" for the same a1, over all pairings; the *only* pairing
   that becomes an identity in (X,Y,Z) (rather than a codimension-1 special condition like X=2θ)
   is Z+X−θ = θ−Y ⇔ X+Y+Z=2θ ⇔ θ=90°. This matches what all three explorers and all four
   outline files independently claim. Confirms that for n≥3 sufficiency genuinely needs a
   multi-move construction (S2), not a one-shot identity — so the outline is right to flag S2's
   general-n proof as a real (if "mechanical") gap, not a triviality.
3. **θ>90° acute-triangle defense** (foundation of `interval-partition-topological`'s base case):
   ran 2000 random-triangle trials — every cut of an acute triangle leaves at least one acute
   child. No counterexample found. This base case is solid.
4. Attempted a brute-force adversarial search (bounded depth, grid-sampled a1) to spot-check the
   θ=180/n conjecture more broadly; it was too slow/coarse to be informative at reasonable depth
   and grid resolution given the time budget, so I did not get independent confirmation of the
   full conjecture — this is a residual risk that should be watched, not evidence against it (the
   three explorers' independent convergence up to n=6 is still the best evidence in hand).

## Per-approach verdicts

### resonance-lattice-invariant — CHANGES REQUESTED
- Whole-attempt: yes (targets full iff, states both directions).
- Sufficiency (S1, S2) is shared/imported, sound as far as it goes (see checks above); S2's
  general-n proof is still open — legitimate shared gap, not fatal.
- Necessity: the outline is commendably honest that its own headline mechanism ("lattice
  membership") does NOT obviously survive Mulan's continuum choice of a1, and says so explicitly
  rather than hand-waving over it ("the central gap Lemma N1 must resolve"). That is the correct
  way to flag an unresolved lemma (mechanism named, but admitted unproven) — acceptable to build
  on, but the builder must not quietly assume the "candidate fix" works; it is untested.
- Issue: Lemma N1's fallback ("track only survivor's independence from θ mod 180") is close in
  substance to `algebraic-independence-generic`'s N2 explicit-irrational-triangle idea. Builder
  should make sure this doesn't collapse into literally the same construction under a different
  name — if it does, note that explicitly rather than presenting it as an independent invariant.
- Verdict: buildable, with the explicit instruction that N1 must produce a genuine invariant
  Shan-Yu's *selection* (not Mulan's cut) can maintain, and must show why "closer to violating
  independence" case doesn't leak through in finitely many steps.

### interval-partition-topological — CHANGES REQUESTED (strongest of the four)
- Whole-attempt: yes.
- Base case (θ>90°, acute-triangle defense) is fully proved and independently re-verified by me
  (2000 trials, zero counterexamples) — genuinely gap-free, a solid anchor.
- Gap: N1 (generalizing "at most one angle ≥90°" to a general-n cell-compatibility condition) is
  not yet even *identified* — the outline admits the right "automatic fact from X+Y+Z=180" for
  general θ "needs to be discovered." This is more exploratory than the other approaches' gaps
  (which at least name a candidate mechanism), so treat this as the approach's central risk: it
  is possible no such clean per-cell complementary threshold exists for n≥3, in which case this
  approach still needs a fallback. Builder should test the n=3 (θ=60, non-resonant nearby value
  e.g. θ=50 or θ=70) case concretely by hand/computer before assuming the "safe" set structure
  scales, since a false generalization here would sink the whole approach.
- N2 (explicit safe-start construction) is correctly flagged as needing an actual example, not
  an existence appeal — good adherence to the "no hand-waving" rule; needs to be delivered
  explicitly by the builder, not left as "generic works."
- Verdict: buildable — most independent/novel mechanism, and its base case is unusually solid
  for round 1; the general-n gap is real but this approach at least has a genuinely proven anchor
  to extend from, which the others lack.

### algebraic-independence-generic — CHANGES REQUESTED
- Whole-attempt: yes.
- One-move classification (N1, k=1 case: identity-collapse iff θ=90°) is correct — matches my
  independent derivation in check 2. Good, this part is solid, not just asserted.
- Gap: the "multi-move resonance-distance potential" (N1's inductive extension to general k) is
  the load-bearing claim and is explicitly un-formalized ("not yet defined"). This is honestly
  flagged, not hidden — acceptable to hand to a builder, but the builder must actually construct
  the potential function and prove the "≤1 resonance-step per move" bound; a mere restatement of
  the intuition would not satisfy the no-hand-waving rule.
- N2 (irrational X0/θ blocking all resonances at once) is a clean, genuinely explicit
  construction — good, addresses the countable-union subtlety correctly in principle.
- Verdict: buildable, but flag to the builder that its core mechanism (identity-collapse
  classification extended over k moves) is mathematically the same computation
  `game-tree-backward-induction` relies on (see below) — only one of the two need fully solve it.

### game-tree-backward-induction — CHANGES REQUESTED, deprioritized this round
- Whole-attempt: yes, formally well-posed (W/L backward induction is a legitimate technique here,
  and the outline correctly restricts to ordinary induction on move-count since the win condition
  is "finitely many moves" — no ordinal-induction subtlety, correctly noted).
- Issue (the reason I'm not building this one now): the load-bearing step, "W_k is a finite union
  of hyperplane pieces, closed under one more recursive step," is — by the outline's own
  admission — "the same underlying algebra as algebraic-independence-generic's N1," just repackaged
  as a topological closure claim instead of a potential function. This is two slugs converging on
  one wall dressed differently, which is exactly the shared-gap risk CLAUDE.md warns about. It is
  not a *fragment* of one proof (each file is a complete top-to-bottom attempt), but the necessity
  mechanisms are not actually independent evidence — if the shared hard lemma fails, both die
  together. I am not cutting it (RETHINK) because the closure framing is a legitimate alternate
  packaging that might expose a cleaner induction than the potential-function framing, and a future
  round might profit from comparing the two once one is further along — but there is no reason to
  spend a builder on it in the very round where the essentially-identical
  `algebraic-independence-generic` is already being built.

## Diversity assessment

Two genuinely distinct necessity *mechanisms* are on the table this round:
(a) explicit invariant/cell/lattice tracking (`interval-partition-topological`,
`resonance-lattice-invariant`) and (b) counting/potential-function on Mulan's degrees of freedom
(`algebraic-independence-generic`, `game-tree-backward-induction` — near-duplicates of each
other). Building one from each pair this round preserves real diversity without spending two
builders on the same underlying algebra. If both (a)-approaches and the built (b)-approach stall
on their respective N1's for 2+ rounds, the orchestrator should ask next round's outliner for a
genuinely different framing (e.g., a direct explicit Shan-Yu strategy stated as a formula, rather
than an invariant/potential abstraction) rather than a fifth variant of "find the right preserved
quantity."

## Build set

interval-partition-topological (strongest anchor, most novel mechanism), resonance-lattice-invariant
(distinct invariant framing, honest about its own risk), algebraic-independence-generic
(represents the counting/potential framing; game-tree-backward-induction shares its hard lemma
and is deprioritized this round, kept in the ranked population for later).

build set: interval-partition-topological, resonance-lattice-invariant, algebraic-independence-generic
