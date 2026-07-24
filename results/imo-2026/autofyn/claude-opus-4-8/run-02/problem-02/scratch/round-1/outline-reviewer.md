# Outline review — imo-2026-02 (round 1)

Problem: `OM = ON`, O = circumcenter(AKL), M,N midpoints of AB,AC, with the 3 angle
conditions. Answer type: none (pure proof).

## Shared grounding — independently re-verified

I rebuilt the configuration from scratch (rotated-ray parametrization by θ, fsolve on
the two remaining angle conditions) on a scalene triangle A=(1.3,4), B=(0,0), C=(5,0)
and confirmed at θ=0.2,0.35,0.5:
- `OM − ON = O(1e-14)`, all three angle conditions satisfied to ~1e-14;
- reduction `OB²−OC² = (AB²−AC²)/2` holds to ~1e-13;
- `AK ≠ AL` (2.86 vs 3.31, etc.) — confirms the ruled-out isosceles-from-A shortcut.

So the three shared claims the whole field rests on are solid: the goal reduction, the
1-parameter family structure, and the list of numerically-FALSE shortcuts (AK=AL,
∠BAK=∠CAL, spiral-at-A, {A,K,L,B,C} concyclic, BK tangent). No approach leans on a
false fact. Good — the field is honestly grounded.

## Diversity check — PASS (with a caveat)

The three genuinely diverge on the engine: brute trig identity vs. synthetic
spiral+involution vs. power-of-a-point. They share only the *reduction* (which is
proved/elementary, not a gap), so a wrong reduction cannot kill all three — the
reduction is verified. This is the right kind of spread for round 1. Caveat: two of the
three (spiral-involution, equal-power-secants) route through the *same object* — the
second intersection / spiral control on ⊙AKL driven by conditions 2,3 — and both flag
that same bridge as their crux GAP. If both stall next round, that is the shared wall to
attack with a new framing; the trig route is the insurance that does not touch it.

---

## trig-metric-identity — APPROVE (field leader)

Framing sound. L1 (goal reduction) is the verified, elementary vector identity — not a
gap. The spine (parametrize by θ, law of sines in ABK/ACL, resolve conditions 2,3 for
r_K,r_L, compute AO·(C−B), show the θ-identity vanishes) is a valid deductive chain with
no circularity. The marked gaps are the RIGHT gaps: GAP-A (closed/implicit r_K(θ),r_L(θ))
and GAP-B (identity ≡ 0). Crucially this approach has a **legitimate rigorous fallback**:
exact symbolic verification (sympy) with A,B,C symbolic and θ a symbol, via the
rotated-ray parametrization — an exact zero certifies the *whole* family, not one config.
That makes it the most likely to actually close.

Issues / what to enforce while building:
- The angle conditions are equalities of *unsigned* angles (arctan of ratios). When the
  builder converts to equations, it must fix branches via the region hypotheses (K in
  ∠LBA, L in ∠ACK, K∈△BMC, L∈△BNC) — do NOT square-and-hope, which introduces spurious
  roots. L2 (unique positive r_K,r_L per θ by monotonicity) is needed for well-posedness
  and must be argued, not asserted.
- If the hand identity (L3) is intractable, the sympy route is acceptable ONLY if it is
  a genuinely exact (rational-function-in-tan(θ/2), symbolic-coordinate) zero — a
  high-precision numeric sweep is NOT a proof. Make the symbolic nature explicit.

## equal-power-secants — CHANGES REQUESTED

Framing sound and the reformulation is exact: since A∈⊙AKL, `OM²−ON² = pow_M − pow_N`
(L1 correct, verified). GAP-1 (control the secant's second intersection from the angle
data) is the right crux. But one stated mechanism is imprecise and must be fixed before
it can be trusted:

- **L2 mislabels an external angle as inscribed.** The outline says "∠LCK is the
  inscribed angle in ⊙AKL subtending chord KL from C." But C is NOT on ⊙AKL (explicitly
  one of the ruled-out facts). ∠LCK is the angle chord KL subtends from an *external*
  point C, which is (inscribed angle) ∓ (arc correction) — it does NOT equal the
  inscribed angle. Building L2 as literally "inscribed angle at C" is a wrong step. The
  builder must recast the second-intersection control correctly: e.g. use the
  tangent-secant / directed-angle relation between the secant MK direction and chord
  KL/AK with C as an external reference, keeping every length signed. This is fixable
  within the framing (the power identity is real), but the mechanism as written is not
  valid — hence CHANGES REQUESTED, not APPROVE.
- Secant choice (a) through A gives MA=AB/2, NA=AC/2 cleanly; prefer it and keep signs.

## spiral-involution — APPROVE for one build attempt, GAP-1 is make-or-break (RETHINK risk)

The σ-invariance discovery (L1) is a genuine, deep structural fact and I credit it: the
hypothesis set is fixed by the formal involution (cond 1 fixed, cond 2↔3). The outliner's
own warning is correct and I echo it as the decisive risk:

- **GAP-1 / L3 is the whole ballgame and is currently unjustified.** A single equal-angle
  (cond 3: ∠LCK=∠BMK) gives ONE pair of corresponding angles for the putative spiral at
  K (L↦B, C↦M ⇒ need △KLC ~ △KBM). A genuine similarity needs a SECOND independent angle
  (or the ratio KL/KC = KB/KM). The claim that L2 (`∠LBA+∠NLC=π`) supplies it is asserted,
  not shown — and L2 itself chains several angle-sum steps that must be checked with
  directed angles (the "∠LBA = ∠ACL+∠LNC" step assumes a specific betweenness). If L2
  does not deliver the second angle, this route is a true dead end.
- Correctly warns σ is FORMAL, not an isometry when AB≠AC — good, it does not overclaim
  "O fixed by reflection." The operative spirals are at K,L, not A (A-spiral is false).

Verdict: not *outright* doomed — the σ symmetry is real and the second angle plausibly
comes from L2 + betweenness — so it earns one build attempt in an empty round-1 pool. But
the builder must attack GAP-1 FIRST and honestly: if the second angle cannot be produced
from L2/region constraints, report RETHINK rather than paper over it. Do not present a
one-angle equality as a similarity.

## Ranking

trig-metric-identity (1531) > equal-power-secants (1501) > spiral-involution (1468).
Anchored on: tractability + a rigorous fallback that certifies the whole family (trig);
sound framing with one fixable mechanism error (power); real structural insight but an
unresolved crux that may be fatal (spiral).

## Selection

Round 1, empty population, three far-apart framings. Build all three in parallel to
maximize coverage — none is outright doomed. Each builder must respect the flags above
(trig: branch/sign + exact-symbolic-only fallback; power: repair the external-angle
mislabel; spiral: resolve GAP-1 first or RETHINK).

build set: trig-metric-identity, equal-power-secants, spiral-involution
