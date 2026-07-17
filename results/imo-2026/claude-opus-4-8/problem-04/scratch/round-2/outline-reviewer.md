# Outline review — imo-2026-04 (Mulan's Triangle Game), round 2

Answer under review: **Mulan wins iff θ = 90°/n, n ∈ ℤ⁺** (i.e. 90/θ ∈ ℤ⁺). Round-1's {90/2^k} is a
strict subset and is correctly discarded.

## Verification of the SETTLED machinery (done before ranking)

- **S1 — ⊇ construction (θ=90°/n forceable).** VERIFIED. I re-derived and machine-checked the full
  game tree (exact rationals, all Shan-Yu branch choices) for n = 1,2,3,4,5,6,7,10 against four
  structurally different starts (generic, very obtuse, equilateral, near-degenerate): Mulan forces θ
  in every leaf. The 90°-fork (cut vertex A with acute B,C at x=90−B → both children get 90 at the
  foot; x∈(0,A) checked: A−x=90−C>0, x=90−B>0) and the θ-peel (vertex mθ split at x=θ → child1 holds
  θ so Shan-Yu is forced to child2={(m−1)θ,C,θ+B}) are both algebraically exact and B,C-independent.
  Sound, no gap.
- **S2 — θ>90° impossibility.** VERIFIED by hand. The 4-combination device classification is
  correct: (x=θ, A−x=θ)→A=2θ; (x=θ, x+B=θ)→B=0 degenerate; (180−x−B=θ, A−x=θ)→C=0 degenerate;
  (180−x−B=θ, x+B=θ)→θ=90. So "both children contain θ" ⟺ θ=90° or A=2θ. For θ>90°: 90-device off,
  2θ>180° impossible ⟹ W₁=W₀, and the induction W_k=W₀ ⟹ W_{k+1}=W₀ closes it with no gap. The AND-OR
  reachability framing (Mulan picks split = OR, Shan-Yu picks child = AND) is the right model.
- **S3 — closure set C(θ), θ∈C(θ) ⟺ θ=90/n.** Plausible and consistent with the BFS the explorer
  reports; the arithmetic (every element is 90/2^a − mθ; = θ ⟺ θ=90/integer) is coherent. This is
  invoked by all three approaches but is only load-bearing once the Guaranteed-Constant Lemma routes
  the forced constant into C(θ) — the builders should still write out the "no element equals θ unless
  θ=90/n" step rather than cite it. Not a fatal concern.

**Bottom line on the settled parts:** the two done halves (⊇ and θ>90°) are genuinely airtight; the
entire remaining difficulty is honestly isolated to one lemma. No circular reasoning: every approach
marks the crux as an explicit GAP rather than assuming it.

## The shared crux (intrinsic, not a defect)

All three approaches reduce the open half (θ<90°, θ∉{90/n}) to the **Guaranteed-Constant Lemma**:
every Shan-Yu-immune angle-value Mulan can force is algebraic over ℚ(θ) and lies in C(θ), hence θ
forceable ⟹ θ∈C(θ) ⟹ θ=90/n. This shared crux is intrinsic to the problem, not an artifact of lazy
outlining — I accept it. The question is whether the three engines are diverse enough not to die
together. My read:

- **B (and-or-closure-rank-induction)** is the genuinely distinct framing: attacker-side, a structural
  well-founded induction on the winning-set rank W_k, no genericity/field machinery. Cleanest and it
  unifies both directions. Primary.
- **A (transcendence-genericity-invariant)** and **C (explicit-shanyu-peel-potential)** are both
  defender-side "maintain a safe invariant on the kept child from a generic seed" arguments — the same
  *mode*, differing only in formalism (field-theoretic algebraic-independence vs. a discrete
  potential + explicit child-choice rule). They are the two closest members of the field. I am keeping
  both as hedges because (i) the outliner's evidence that the *naive* form of A already collapses under
  the x=c−B move shows the field route is fragile, so C's concrete potential is a real alternative
  bookkeeping, and (ii) the population is empty and momentum matters — but the orchestrator should note
  that if both stall on the identical c−B stress-test next round, they are effectively one line and one
  should be dropped in favor of a fourth, farther framing.

## Per-approach verdicts

### and-or-closure-rank-induction — APPROVE
Right technique (well-founded induction on game rank; matches the AND-OR model that already proved
S2). Whole-problem attempt, not a fragment. Sound skeleton; no circular step. Real gap (step 2/3): the
*lift* of the 2-device classification from "both children contain θ" (W₀) to "both children carry a
possibly-different C(θ)-value" (W_k). The load-bearing sub-claim — two children carrying *different*
C(θ)-values force a C(θ)-value in the parent via the split map, using closure under /2 and −θ — is the
place a counterexample would surface if the answer were wrong, so the builder must actually run the
split-formula algebra for the two-different-values case, not wave "same two generators." Flagged, not
fatal.

### explicit-shanyu-peel-potential — APPROVE
Right technique (explicit defender strategy + monovariant; KB "Invariants & monovariants"). Whole
attempt. The mechanism is stated with a real hinge (Φ non-collapse: a single split cannot create a
finite-d angle unless a parent had one). Gap = step 4 (Φ=∞ preserved). Two things the builder MUST
nail (already correctly flagged by the outliner): (a) make d well-defined and provably ∞ on the generic
start — this needs θ∉C(θ) ⟹ no finite chain, i.e. it depends on S3; (b) the x=c−B collapse move, where
both children drop to tr.deg 1 and one can be handed θ — must show the *other* child keeps Φ=∞. If step
(b) fails, this approach is dead, so it is the first thing to test. Not fatal on paper.

### transcendence-genericity-invariant — APPROVE (with a live caution)
Right technique in principle (self-restoring field invariant over ℚ(θ), adapting aimo-0236's
stay-one-step-ahead pattern — but NOT its 2-adic content, correctly warned). Whole attempt. The
invariant is well-defined (each angle is algebraic-and-in-C(θ), or transcendental, never θ). Caution:
the naive tr.deg-2 version is already known FALSE (the x=c−B move collapses both children), so the
refined "track the algebraic part in C(θ)" clause is doing all the work and its self-restoration (step
5) is the whole difficulty — the builder must show that when Mulan picks x algebraic to manufacture a
new constant in one child, the θ-free child Shan-Yu keeps still satisfies clause (a)/(b). This is the
most delicate of the three; ranked lowest for that reason, but it is a legitimate independent engine,
not doomed. APPROVE.

## Diversity note for the orchestrator
Field is 1 truly-distinct framing (B, attacker/structural) + 2 same-mode defender-invariant variants
(A, C). If A and C both bottom out on the identical x=c−B stress-test in a future round, treat the field
as collapsed-to-one-mode and commission a genuinely farther framing (e.g. a direct algebraic
characterization of the reachable-constant set, or a compactness/degree argument) rather than a third
defender invariant.

## Ranking (all new, cold-start; ranked by route strength)
- and-or-closure-rank-induction — 1531 (primary; cleanest, most distinct)
- explicit-shanyu-peel-potential — 1500 (concrete, checkable hedge)
- transcendence-genericity-invariant — 1469 (most delicate; naive form already collapsed)

No copy/branch warranted this round — the three are already distinct slugs, not one proof split into
pieces, and no single approach has a proven prefix with two rival completions.

build set: and-or-closure-rank-induction, explicit-shanyu-peel-potential, transcendence-genericity-invariant
