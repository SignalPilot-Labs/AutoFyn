# Review: imo-2026-05 (IMO 2026 P5)

## Verdict: APPROVE
## Status: solved

## Summary

The candidate proof in `results/imo-2026-05.md`, section "Full proof", is
correct and complete. I independently re-derived every load-bearing algebraic
step from scratch (symbolically via `sympy` where appropriate, and cross-checked
numerically with random-trial sandwich verification), and found no gap. The
claimed answer `f(x) = x + c`, `c ≥ 0`, is correct, and both directions
(necessity and sufficiency) are proven rigorously.

## Point-by-point independent verification

1. **FE derivation `f(f(y)) = 2f(y) - y` (Step 1).** Re-derived by hand: substituting
   `x := f(y0)` into the original three-term chain collapses both outer terms to
   `f(y0)` exactly (QM and GM of a repeated value), forcing the middle term
   `(f(f(y0))+y0)/2` to equal `f(y0)` on both sides, giving the FE. This is a
   direct computation at one specific, legitimately-chosen value of `x` (valid
   since `f(y0) ∈ R_{>0}`), not a hidden general lemma. Confirmed via sympy
   numerically for the eventual solution family (`f(f(y))-2f(y)+y` simplifies to
   `0` when `f=x+c`) — consistent with the claim. No gap.

2. **Orbit argument `f(x) ≥ x` (Step 2).** The recurrence `y_{n+2} = 2y_{n+1}-y_n`
   from the FE, applied at `y_n` (legitimately, since `y_n ∈ R_{>0}` is
   established first by induction using only that `f` maps `R_{>0}→R_{>0}`),
   gives the AP `y_n = y + n·d(y)` — I re-verified this induction is not
   circular (positivity of `y_n` is established *before* FE is applied at `y_n`).
   The contradiction for `d(y)<0`: choosing `N > -y/d(y)` (Archimedean property,
   legitimate since `-y/d(y) > 0` when `d(y)<0`) and multiplying the strict
   inequality by the *negative* number `d(y)` (correctly flips direction) gives
   `y_N < 0`, contradicting `y_N ∈ R_{>0}`. This is a genuine, complete proof by
   contradiction, not merely "suggestive" — it rigorously forces `d(y) ≥ 0` for
   every `y`. No gap.

3. **Squaring step (Step 3).** Both sides of each half of the chain are
   manifestly nonnegative (square roots, or `(f(x)+y)/2` with `f(x),y>0`), so
   squaring via the stated fact (Sq) (`t↦t²` strictly increasing on `[0,∞)`,
   hence an iff on nonnegative reals) is valid and preserves direction. I
   re-checked `GM-ineq`: `(f(x)+y)/2 ≥ √(xf(y))` squares correctly to
   `(f(x)+y)^2 ≥ 4xf(y)` (not `xf(y)`) — the factor of 4 from squaring `1/2` is
   present and correct in the write-up. No gap.

4. **Quadratic-defect identity (E).** I re-derived this completely independently
   with `sympy`:
   ```
   x, y, dx, dy = symbols(...)
   fx = x + dx; fy = y + dy
   diff = expand((2*fx - x + y)**2 - 4*fx*fy)
   claimed = expand((x-y)**2 + 4*fx*(dx-dy))
   simplify(diff - claimed)  →  0
   ```
   This is an *exact* polynomial identity, confirming `(2f(x)-x+y)^2 - 4f(x)f(y)
   = (x-y)^2 + 4f(x)(d(x)-d(y))` identically. Combined with the substitution
   `x → f(x)` in (GM-ineq) and elimination of `f(f(x))` via (FE) — both
   legitimate universal-statement instantiations — this proves (E) rigorously.
   No gap; the hand-derivation in the proof matches my from-scratch symbolic
   re-derivation term for term.

5. **Telescoping squeeze (Step 5).** Checked the partition construction
   (`x_i = a+iΔ`), both directions of the local bound (applying (E) at `(x_i,
   x_{i+1})` and at `(x_{i+1},x_i)`), the use of Step 2's bound `f(x_i) ≥ x_i ≥
   a` to get a uniform `≤ Δ²/(4a)` bound, the telescoping sums giving `d(b)-d(a)
   ≤ (b-a)²/(4aN)` and `d(a)-d(b) ≤ (b-a)²/(4aN)` for *every* `N`, and the
   proof-by-contradiction closing argument (assume `d(b)-d(a)=L>0`, pick `N >
   K/L` via Archimedean property, contradiction) for both directions
   simultaneously. This is fully rigorous — not a hand-wavy "let `N→∞`" but an
   explicit contradiction argument valid for arbitrary fixed `L>0`. The
   extension "for general `p≠q`, apply with `{a,b}=\{min,max\}`" is correctly
   noted as WLOG. No gap.

6. **Sufficiency.** Verified `f(x)=x+c` (`c≥0`) satisfies both inequalities:
   (a) symbolically, `f(x)+y = x+f(y)` identically reduces the chain to
   classical QM≥AM≥GM for `(x, f(y))`, proven from scratch via `(a-b)^2≥0`
   (matches sympy: `QM²-AM² = (a-b)²/4 ≥ 0`, `AM²-GM² = (a-b)²/4 ≥ 0`);
   (b) numerically, ran 20000-trial random checks in `python3` for `c ∈
   {0, 0.001, 1, 5, 100, 1e-6}` over `x,y ∈ (1e-4, 1000)` — zero violations in
   every case, confirming the algebra. Also confirmed `c<0` breaks the *domain*
   requirement `f:R_{>0}→R_{>0}` (not the inequality itself, where well-defined)
   — consistent with the proof's remark and with my own numeric check
   (`domain_violations>0`, `ineq_violations=0` for `c<0` restricted to the valid
   sub-domain). No gap.

7. **Hand-waving / circularity check.** Scanned the "Full proof" section for
   "clearly/obviously/it follows/by symmetry" used to skip a real step — found
   none; every step that could be non-trivial (squaring validity, induction
   base+step, Archimedean contradiction, telescoping sum, identity expansion)
   is written out explicitly. No circularity: Step 2 doesn't use Step 4/5;
   Step 4 uses only (GM-ineq) and (FE), not injectivity or the orbit-AP fact
   (correctly noted in the text). No appeal to "as in problem X" / crux-move
   citation inside the formal proof (the crux-corpus notes are confined to the
   separate "Notes for the outliner" section, outside the proof itself, so they
   are not load-bearing).

8. **Final answer / characterization.** Explicitly boxed: "the solutions are
   exactly `f(x)=x+c` for `x∈R_{>0}`, for an arbitrary constant `c≥0`." Both
   necessity (Part 1) and sufficiency (Part 2) are proven, matching CLAUDE.md's
   requirement for "determine all functions" problems (bound + construction).
   The cited KB entry ("Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM,
   Schur...") is confirmed to genuinely exist at `knowledge_base.md:33`.

## Extra independent sanity checks performed (beyond the write-up)

- Symbolic re-derivation of identity (4.2) from scratch via `sympy.expand` and
  `sympy.simplify` — exact match, difference is `0`.
- Numeric 20000-trial random verification of sufficiency for six values of `c`
  (including `c` very close to `0` and very large `c`) — zero violations.
- Numeric verification that a non-constant `d` (step function, jump at `x=10`)
  *fails* the original sandwich in ~0.5% of random trials, consistent with the
  necessity proof's conclusion that only constant `d` works.
- Verified the QM≥AM and AM≥GM squared identities independently reduce to
  `(a-b)²≥0` via `sympy.factor`.

## Conclusion

I could not find any actual gap, sign error, missing case, hidden circularity,
or unjustified step. The single load-bearing identity (E) and its consequence
(the Archimedean telescoping squeeze forcing `d` constant) are both fully
correct and rigorously argued. The Status `solved` recorded by the builder is
correct and should stand.
