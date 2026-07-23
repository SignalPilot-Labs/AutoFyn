# Outline review — imo-2026-04 (round 3 outline)

## Verdict: CHANGES REQUESTED

The core technique is sound and I independently re-derived (by hand and by
sympy) the two load-bearing identities; they are correct, not hand-waved. The
conjectured answer set (θ = 180°/n, n≥2 integer) is consistent with all
sanity checks I ran. However, three genuine gaps must be closed before this
is a complete proof — none require a new technique, but each is currently
asserted rather than proven.

## What checks out (verified independently)

- **L/R formulas.** L(t)=(t,β,α+γ−t), R(t)=(α−t,γ,β+t) confirmed correct
  (standard angle-sum decomposition).
- **Move 1 (transfer).** t=θ on α>θ makes L(θ) contain θ exactly, so Shan-Yu
  is *forced* to keep R(θ)=(α−θ,γ,β+θ) — this is not "Shan-Yu's best move,"
  it's a hard consequence of the game rule (keeping L ends the game
  immediately as an Mulan win). No leap here.
- **Move 2 (helper-reset), re-derived from scratch via sympy:**
  L(θ−β) = (θ−β, β, 180−θ), R(θ−β) = (α+β−θ, γ, θ). This confirms the
  "universal constant 180−θ" claim exactly and independent of α, γ — it is a
  genuine consequence of α+β+γ=180, not a hidden assumption. R contains θ
  exactly, so Shan-Yu is forced into L, landing on (θ−β, β, 180−θ) regardless
  of the original triangle. This is the single most important claim in the
  outline and it is correct.
- **Survival congruence lemma (the part the task flagged as most likely to
  have a gap): it does NOT have the gap.** I re-derived it for arbitrary real
  t (not restricted to Move-1/Move-2 special values): L bad ⟺ t≡0 or
  t≡α+γ (mod θ); R bad ⟺ t≡α or t≡−β (mod θ). Both bad forces one of
  α≡0, β≡0, γ≡0, or α+β+γ=180≡0 (mod θ) — I checked all four
  t-pairings by hand and they match exactly. Since the invariant excludes the
  first three and θ∤180 excludes the fourth, *every* Mulan move (any vertex,
  any real t) leaves at least one safe child. This genuinely covers the fully
  general move, addressing the concern raised in the assignment.
- Small cases: θ=90° (n=2) traced numerically on (100,50,30) — Move 2 there
  collapses to a double win since 180−θ=θ when θ=90 (both branches hit 90°),
  consistent with "n=2 needs only the final Move-2 step." θ=50° (non-member,
  180/50=3.6): confirmed Shan-Yu has a valid initial triangle avoiding
  multiples of 50° (e.g. (10,80,90)) and that a generic Move-1/Move-2-style
  attack on it leaves a safe branch, matching the lemma.

## Gaps that must be closed by the builder (not fatal, but currently just asserted)

1. **Case-3 → case-1/2 handoff in the winning skeleton is not actually
   justified as written.** Step 3 says "attacker = whichever current angle
   ≥θ" after the Move-1 loop produces helper h<θ, but the outline never
   proves such an angle (or a valid Move-2 pair) still exists post-loop. I
   checked this by hand: after the loop the triangle is (h,X,Y) with
   X+Y=180−h>180−θ, and this new triple must be re-run through the
   *same* room-condition case split (it will land in case 1 or 2, both of
   which fire immediately) — but the outline never states this reapplication
   explicitly. The builder must add: "reapply the room-condition lemma to
   the post-loop triangle, not just the original one," with the case-1/2
   argument spelled out concretely for that triangle, not merely assumed.
2. **Existence of Shan-Yu's initial "generic" triangle (survival direction)
   is asserted, not constructed.** "Measure zero / generic" is fine as
   outline-stage language but the builder must give an explicit example (or a
   clean finite-avoidance argument: only countably many bad lines in the
   2-parameter simplex, for *any* real θ with 180/θ∉ℤ) — currently listed as
   an open item in the outline's own "Watch out for," correctly flagged but
   must be resolved, not left generic.
3. **Congruence lemma must be restated symmetrically for all 3 attack
   choices** (attacking via β or γ, not just α) — trivial by relabeling, but
   currently only proven for one labeling; state it explicitly rather than
   leaving it implicit.
4. Minor: state explicitly why Shan-Yu's choice of which of β/γ absorbs +θ
   during iterated Move 1 is immaterial to the final win (it is, since only
   the decreasing coordinate matters) — one sentence needed to avoid the
   reviewer flagging it as unaddressed.

## No fatal flaw found
No dead end from `results/imo-2026-04.md` is being repeated; the technique
(forced-move reduction + mod-θ invariant) is the right one and both
directions are mechanically justified, not just plausible. Builder should
proceed, closing gaps 1–4 above with full rigor (especially #1, which is the
one place a reviewer could plausibly reject the proof as incomplete).
