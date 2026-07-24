# Builder report — equal-power-secants (imo-2026-02), round 1

Status written: **partial**.

## What I proved (rigorous, complete)
**L1 — Power reformulation.** `OM = ON ⟺ pow_M(⊙AKL) = pow_N(⊙AKL) ⟺ AO·BC = (AC²−AB²)/4`.
Full proof in the approach file: power of a point (`pow_X = |OX|²−R²`), then a vector
expansion with `A` as origin using `|OA|=R` and `AM=½AB, AN=½AC`. All identities
sympy-verified exactly (`powM`, `powN` closed forms; `pow_M−pow_N ≡ AO·BC+(AB²−AC²)/4`).
The inside/outside-circle sign issue is absorbed by the `|OX|²−R²` form — no case split.
This is promotable as the canonical restated target for the whole field.

## The distinctive engine is refuted (honest gap, not papered over)
The outline's crux GAP-1 — control the secant's second intersection `K₂`(on `MK`), `L₂`(on
`NL`) with `⊙AKL` from the angle data — has **no valid mechanism**. On the solved
1-parameter family (scalene, θ=15/25/35°, correct containment branch, OM=ON to ~1e-13):
- The two candidate spiral similarities (`△KCL∼△KMB` from cond3, `△LBK∼△LNC` from cond2)
  need second angles `∠KLC=θ`, `∠LKB=θ`. Both FALSE (measured 145–167°, 125–144°).
- No 4-subset of `{A,B,C,M,N,K,L}` is concyclic across the family (only trivial collinear
  triples). Confirms `B,C∉⊙AKL`; the outline's "∠LCK inscribed at C" (the reviewer's
  flagged error) has no salvage circle.
- `K₂` is not a distinguished point (≠A, ∉ line AC, no θ-linked arc).

The only *computable* secant is through `A` (line AB/AC), and it collapses **exactly** onto
(★), using none of the angle hypotheses. So the power framing gives a correct
reformulation but no leverage independent of locating `O`.

## Remaining gap
Prove `AO·BC = (AC²−AB²)/4` from the three angle conditions. This is the SAME crux as the
trig-metric approach (pin AO / triangle AKL from the angle data). Power-of-a-point offers
no shortcut past it.

## Spec concerns — RETHINK-leaning
This approach is **not an independent engine**; it is a correct reformulation equal to the
shared reduction, plus a distinctive move (secant-through-K/L) that is now numerically
refuted. Recommendation for the orchestrator/outliner:
- Keep **L1 as a certified lemma** (clean, reusable) — worth promoting to `lemmas/`.
- Do NOT re-dispatch this slug to chase secant-second-intersection control; that wall is
  documented as dead. If kept alive, it must be **re-planned (RETHINK)** to actually
  compute `O` — at which point it merges into the trig/metric route and stops being a
  far-apart framing. Better: retire the distinctive engine and let trig-metric own the
  reduction, freeing a population slot for a genuinely new framing (the outline-reviewer
  already flagged spiral-involution + this one share the same wall).

## Files
- /home/agentuser/repo/results/imo-2026-02/approaches/equal-power-secants.md (Status: partial)
