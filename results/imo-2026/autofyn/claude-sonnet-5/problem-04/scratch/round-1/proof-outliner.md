## imo-2026-04

Conjectured answer (convergent across all 3 explorers, strong symbolic evidence up to
n=6): **Mulan wins iff θ = 180°/n for some integer n ≥ 2.** All four approaches below
share the sufficiency direction (solid, low-risk, needs only a general-n write-up of an
identity already verified case-by-case for n=2..6) and differ in their necessity
mechanism (θ ≠ 180/n ⇒ Shan-Yu escapes forever) — the field's central open gap. Round 1:
no prior approaches existed, so all four are **new**.

Shared setup (all four files use this): triangle (X,Y,Z), X+Y+Z=180. A move: pick apex
angle X, pick a1 ∈ (0,X) (Mulan's continuum choice), giving
  child1 = (Y, a1, Z+X−a1),  child2 = (Z, X−a1, Y+a1).
Shan-Yu keeps one child; loop checks for angle=θ at the top.

---

resonance-lattice-invariant: new
Target: full iff-characterization (θ=180/n for integer n≥2) — sufficiency + necessity.
Technique: chain/induction for sufficiency; a residue/lattice (number-theoretic)
invariant for necessity, generalizing the "pure-shave" mod-θ residue argument found by
the angle-arithmetic explorer to Shan-Yu's actual adversarial survivor-selection under
Mulan's full continuum freedom on a1.
Skeleton:
  1. Chain lemma S1: angle=kθ present ⇒ Mulan wins in ≤k−1 moves (cut at a1=θ, induct on
     k) — by direct algebra on child formulas.
  2. Universal boundary identity S2: for θ=180/n, exhibit a move from ANY (X,Y,Z) forcing
     an angle of (n−1)θ or θ into the survivor, with the dependence on the non-apex
     angles cancelling algebraically (verified for n=2,3,4,5,6 by explorers; needs a
     single symbolic proof for general n) — by direct algebra + induction on n.
  3. Necessity: define invariant "no current angle ≡0 mod θ, and X0,Y0 chosen
     ℚ-independent from θ mod 180" and show Shan-Yu's chosen survivor preserves it despite
     Mulan's continuum a1 — by casework on which child avoids θ.
  4. Conclude: L (Shan-Yu-safe states) is nonempty and reachable-preserving whenever
     θ≠180/n, so Shan-Yu wins forever; combine with 1-2 for the full iff.
Key lemmas:
  - S1 — because cutting the kθ apex at a1=θ literally splits off one exact θ and
    passes (k−1)θ to the other child.
  - S2 — because at θ=180/n the "other two angles" cancel out of the forcing equation
    (an identity in Y,Z, not a hyperplane condition on them).
  - N1 (the real gap) — needs a genuine invariant Mulan cannot break with her continuum
    choice of a1, since a1 is NOT restricted to any lattice a priori; the "pure-shave"
    residue argument only works for a restricted sub-game and must be extended or
    replaced.
Open gaps: general-n proof of S2 (mechanical, low risk); N1 is the load-bearing
unresolved lemma — the fix (tracking survivor's independence from θ rather than a fixed
lattice) is only sketched, not proven.
Cases to cover: sufficiency induction base case k=1; necessity must handle both "only one
child avoids θ" and "neither child even close to θ" sub-cases.
Watch out for: a1 is Mulan's free real choice — do not assume downstream angles stay in
any fixed lattice unless proven; this was the flaw in the naive "pure-shave-only"
argument the angle-arithmetic explorer already flagged.

---

interval-partition-topological: new
Target: full iff-characterization — sufficiency + necessity.
Technique: sufficiency as above (imported); necessity via a topological interval-cell
invariant generalizing the ALREADY FULLY PROVED θ>90° "acute-triangle" defense (clean,
gap-free, reuse verbatim) to all non-resonant θ≤90°.
Skeleton:
  1. Reuse S1, S2 (sufficiency) from `resonance-lattice-invariant.md` once certified.
  2. Base case θ>90° (already fully solved, no gap): partition into acute/non-acute;
     show every cut of an acute triangle leaves ≥1 acute child (complementary threshold
     a1=90−Y) — by direct case algebra (fully done by game-strategy explorer).
  3. Generalize: partition (0,180) into cells C_k=(kθ,(k+1)θ], define "θ-safe" triangles,
     prove Lemma N1 (a cut of a θ-safe triangle always leaves ≥1 safe child, unless
     180/θ∈ℤ) via the same threshold-complementarity mechanism scaled to n cells.
  4. Lemma N2: explicit safe starting triangle (all 3 angles strictly interior to
     distinct cells) exists for every non-resonant θ.
  5. Conclude necessity: Shan-Yu starts safe, always picks the safe child forever.
Key lemmas:
  - Base θ>90° case — because obtuseness of the two candidate children is governed by
    complementary sides of the single threshold a1=90−Y (already verified).
  - N1 (the gap) — the n=2 (θ=90) threshold-complementarity must be shown to generalize
    to n cells without a resonance collapse, for arbitrary non-integer 180/θ.
  - N2 — explicit construction, not just measure-zero-avoidance existence claim (rigor
    rule: must be explicit).
Open gaps: N1's general-n threshold complementarity is unproven outside n=2; must find
the correct "automatic fact from X+Y+Z=180" that plays the role of "≤1 angle ≥90°" for
general θ.
Cases to cover: n=180/θ irrational (cells never resonate — should be the easy sub-case);
n=180/θ rational non-integer (p/q, q>1) — must show cells still don't force resonance;
this is the sharpest case, easy to get wrong.
Watch out for: boundary angles (exactly kθ) need a strict-inequality convention or the
"safe" set could be ill-defined at cell edges.

---

algebraic-independence-generic: new
Target: full iff-characterization — sufficiency + necessity.
Technique: sufficiency imported; necessity via explicit generic (irrational-ratio)
starting triangle + a degrees-of-freedom / identity-collapse counting argument on
Mulan's single real parameter a1 per move.
Skeleton:
  1. Reuse S1, S2.
  2. Lemma N1: classify (over all 6 apex/labelling choices) when "child1 hits θ" and
     "child2 hits θ" can hold for the SAME a1 identically in (X,Y,Z) — shown (by all
     3 explorers, for one move) to force θ=90 only; extend this single-move
     classification across a bounded k-move composed system by strong induction on k,
     showing the "resonance gap" a generic triangle maintains can shrink by at most 1
     step per move, so it is never closed in finite time unless 180/θ∈ℤ.
  3. Lemma N2: explicit starting triangle with X0/θ, Y0/θ, Z0/θ all irrational (pick X0/θ
     irrational; this single condition rules out ALL rational-multiple resonances at
     every depth at once, a clean fix for the "countably many hyperplanes as k→∞" issue).
  4. Conclude necessity from N1+N2.
Key lemmas:
  - N1 one-move classification — because the two "hits θ" equations are affine in a1,
    so simultaneous universal solvability is an identity-in-(Y,Z) question, solved by
    direct elimination (already done for k=1 by explorers).
  - N1 multi-move extension (the gap) — needs an explicit "resonance distance" potential
    function that changes by ≤1 per move; not yet defined.
  - N2 — irrationality of X0/θ blocks resonance at ALL depths simultaneously, avoiding a
    countable-union subtlety other approaches must handle move-by-move.
Open gaps: the multi-move resonance-distance potential in N1 is the central unproven
claim; the k=1 case is solid but induction to unbounded k is not yet formalized.
Cases to cover: all 6 apex/labelling cases at k=1 (mechanical, low risk); the inductive
step for general k (the real difficulty).
Watch out for: "irrational X0/θ" blocks EXACT resonance, but must also verify it doesn't
accidentally block Shan-Yu's own possible use of a fortunate move — irrelevant since only
Mulan drives a1; still confirm no circularity in the argument.

---

game-tree-backward-induction: new
Target: full iff-characterization — sufficiency + necessity.
Technique: sufficiency imported; necessity via formal Win/Loss (N/P-position) backward
induction on the full triangle-state space, adapting the proof STYLE (not the numbers)
of crux `aimo-0225` (isosceles counter game, 2-adic-valuation Win/Loss classification).
Skeleton:
  1. Reuse S1, S2.
  2. Define W ⊆ S (2-simplex of triangles) as the least set containing {angle=θ} and
     closed under "∃ move forcing both children into W" (backward induction, W=∪W_k).
  3. Lemma N1: each W_k is a finite union of affine-hyperplane pieces (angle ≡0 mod θ in
     a derived sense) — inductive symbolic computation across all apex/labelling cases,
     showing the recursive "forcing" condition never generates a 2-dimensional open
     patch unless it collapses to all of S (which happens exactly at θ=180/n).
  4. Lemma N2: if W ≠ S, then L=S\W is open dense; Shan-Yu picks any point of L and, by
     definition of L, always has ≥1 child in L available — explicit escape rule.
  5. Conclude the full iff from N1 (classifies exactly when W=S) + N2 (turns W≠S into an
     actual strategy).
Key lemmas:
  - N1 (the gap) — hyperplane-closure is preserved by the recursive "exists a1 forcing
    both children in W_k" operation because that condition is itself an affine equation
    in the current angles (shared computation with algebraic-independence-generic's N1),
    so the inductive class of "definable-by-hyperplanes" sets is closed under one more
    step, EXCEPT when it degenerates to everything.
  - N2 — follows directly from L being defined as the complement of W: no state in L can
    have ALL of its move-images forced-into-W, else it would already be in W by
    definition — near-immediate once N1 pins down W's structure.
Open gaps: N1's "closure under recursion" claim across all k is the hard inductive step
(the same underlying algebra as algebraic-independence-generic's N1 but packaged as a
topological/set-theoretic closure argument rather than a potential function) — this is
the most structurally rigorous framing but requires the most careful bookkeeping across
6 labelling cases × unbounded induction depth.
Cases to cover: same 6 apex/labelling cases as the other approaches at each level k;
must also confirm W_0 (the base case, angle=θ exactly) is itself a valid finite
hyperplane union (trivial, 3 pieces).
Watch out for: rigor requires showing the LEAST closed set W really equals ∪W_k (no
transfinite subtlety — argue by the finite-game-length hypothesis, since "wins in
finitely many steps" means ordinary induction on move-count suffices, no need for
ordinal induction beyond ω).

---

Notes for the outline-reviewer: all four approaches are genuinely different in
mechanism for necessity (lattice/residue vs topological-cell vs
algebraic-independence/counting vs formal backward-induction game theory), while
legitimately sharing the sufficiency direction per the dispatch instructions. The
θ>90° sub-case (already a complete, gap-free proof from the game-strategy explorer) is
folded into `interval-partition-topological` as its clean base case, but should also be
cited/reused as a sanity check by the other three (any correct necessity mechanism must
reduce to it when θ>90°, since 180/n≤90 for all n≥2). Recommend the build set include
at least 3 of these 4 to preserve diversity — do not let the population collapse to a
single necessity mechanism this early, since none of the four gaps (N1 in each file) is
yet closed and it's unclear a priori which mechanism will actually go through.
