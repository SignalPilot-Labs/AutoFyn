# Review: imo-2026-05, "Proof outline (proof-outliner, round 2)"

## Verdict: APPROVE

The technique is sound, the skeleton is logically valid, every load-bearing
lemma is stated with a checkable mechanism, and I independently re-derived the
two algebraic claims that matter most (step 1's FE derivation and step 3's
"quadratic-defect" identity) both by hand and with `sympy`; both check out
exactly. Step 4's telescoping/Archimedean squeeze — the part most likely to
hide a one-sided-bound bug — is airtight when checked term by term. The
builder can proceed to write the full prose proof from this outline.

## Independent verification performed

1. **Step 1 (FE derivation), re-checked by hand and symbolically.**
   With `x := f(y0)`, `sqrt((f(y0)^2+f(y0)^2)/2) = f(y0)` and
   `sqrt(f(y0)*f(y0)) = f(y0)` — confirmed with sympy (`fy0` treated as an
   opaque positive symbol). The chain collapses to `f(y0) ≥ (f(f(y0))+y0)/2 ≥
   f(y0)`, forcing `f(f(y)) = 2f(y)-y`. This is a direct computation (not a
   disguised appeal to "equality case of QM-AM-GM for a *general* pair"), so
   it's legitimate as claimed. **Confirmed correct.**

2. **Step 3, the (E) identity, verified symbolically two independent ways**
   (once with `fx, fy` opaque symbols and derived `dx = fx-x, dy=fy-y`, once
   with `d(x), d(y)` as the primary symbols and `f(x)=x+d(x)`): in both cases
   ```
   (2f(x) - x + y)^2 - 4f(x)f(y)  -  [4f(x)(d(x)-d(y)) + (y-x)^2]  =  0
   ```
   identically (sympy `expand`/`simplify` returns exactly `0`). So (E) is not
   an approximation or a "morally true" claim — it is an *exact* algebraic
   rearrangement of `(GM-ineq)` after the substitution `x → f(x)` and the
   elimination of `f(f(x))` via (FE). This is the mechanism the outline
   claims, and it is correct.

3. **Step 4, the telescoping squeeze, re-derived term by term (not just
   trusted).**
   - From (E) with `(x,y) = (x_i, x_{i+1})`: `4f(x_i)(d(x_i)-d(x_{i+1})) +
     Δ² ≥ 0` ⟹ `d(x_{i+1}) - d(x_i) ≤ Δ²/(4f(x_i))`. Matches the outline.
   - From (E) with `(x,y) = (x_{i+1}, x_i)`: `4f(x_{i+1})(d(x_{i+1})-d(x_i)) +
     Δ² ≥ 0` ⟹ `d(x_i) - d(x_{i+1}) ≤ Δ²/(4f(x_{i+1}))`. Matches the outline.
   - Both denominators are legitimately bounded below by `a` using **step
     2's already-proved fact `f(t) ≥ t`** applied at `t = x_i` (or `x_{i+1}`)
     together with `x_i ≥ a` for every partition point in `[a,b]`. This is
     the correct, non-circular use of step 2 (it only needs `f ≥ id`, not
     the full orbit machinery, and step 2 was proved before (E) was even
     introduced, so there is no circularity).
   - Telescoping the first family over `i=0,…,N-1` gives `d(b)-d(a) ≤
     (b-a)²/(4aN)`; telescoping the second gives `d(a)-d(b) ≤
     (b-a)²/(4aN)`. **Both** directions are obtained — this is not a
     one-sided bound, contrary to the risk flagged in the review brief. Since
     `a>0` is fixed and `N` ranges over all positive integers, the RHS → 0
     while the LHS is independent of `N`; a fixed real number bounded above
     by a sequence tending to `0` (for *every* `N`, not just in a limit) must
     be `≤ 0` — a legitimate Archimedean-property argument, not hidden
     calculus. Applying this to both directions forces `d(a) = d(b)`.
   - Endpoint/domain check: `a>0` strictly (domain excludes `0`), so the
     denominator bound `f(x_i) ≥ a > 0` never degenerates; no division by
     zero or boundary issue. Confirmed.

4. **Step 2 (orbit argument), both cases considered.** The outline correctly
   treats `d(y) ≥ 0` as the only viable case by deriving a contradiction from
   the alternative `d(y) < 0` (which forces `y_n = y+n·d(y) → -∞`,
   contradicting `y_n ∈ R_{>0}` for all `n`). This is a genuine
   case-exhaustion (not an unjustified "clearly positive"), and it does not
   presuppose the conclusion `f(x) ≥ x` anywhere in its own derivation.

5. **No circularity in the dependency graph.** Step 3's (E) uses only (FE)
   from step 1 — verified: the substitution and elimination touch only
   `f(f(x))`, and (FE) is the only fact invoked. Step 4 uses (E) plus the
   already-proved `f ≥ id` from step 2. Injectivity and the orbit-AP fact are
   correctly flagged as *not* on the critical path (true — I checked (E)'s
   derivation does not use injectivity anywhere). No lemma is used before it
   is proved.

6. **Sufficiency direction (step 5) is fully explicit and correctly cross-
   checked.** `f(x)=x+c ⟹ f(x)+y = x+f(y)` identically ⟹ middle term equals
   `AM(x,f(y))` exactly ⟹ chain reduces to classical QM-AM-GM (`knowledge_base.md`
   line 33, "Standard inequalities: AM-GM, Cauchy-Schwarz, QM-AM, Schur").
   `c ≥ 0` is independently re-derived from the codomain constraint alone
   (`f(y)=y+c>0` for `y` near `0^+` forces `c≥0`), which is a genuine
   independent consistency check against step 4's conclusion, not a
   redundant restatement.

7. **Domain coverage.** All steps operate over the full stated domain
   `x,y ∈ R_{>0}` with no silently dropped subcase: (FE) holds for every
   `y0>0` (arbitrary substitution); (E) holds for every `x,y>0`; the
   partition argument covers every pair `a<b` in `R_{>0}` (and the case
   `a=b` for the final "`d` is globally constant" claim is trivial, `d(a) =
   d(a)`, and doesn't need separate treatment — worth the builder adding one
   sentence for completeness but not a gap in the outline). Necessity
   (steps 1–4) and sufficiency (step 5) are both present, satisfying
   CLAUDE.md's "determine all functions" requirement (an `iff` characterization).

8. **Consistency with recorded dead ends.** Cross-checked against
   `results/imo-2026-05.md`'s "Approaches tried": the outline does not repeat
   the refuted "answer is `f(x)=x` alone" claim, and it explicitly builds on
   (not repeats) the previously-proved facts 3–4. The "y=f(x)" and "x=y"
   substitutions are correctly noted as dead ends already checked and not
   re-attempted. Good use of prior negative results.

## Minor items for the builder (not blocking, cosmetic/rigor-polish only)

- In step 4's final sentence ("Since `a<b` were arbitrary, `d` is constant on
  all of `R_{>0}`"), the builder should add one explicit sentence handling
  the extension to *all* pairs `p,q` (not just `p<q`): for `p≠q`, WLOG
  `p<q`, apply the result to get `d(p)=d(q)`; for `p=q` it's trivial. This is
  a one-line addition, not a structural gap.
- When writing the final proof, restate explicitly (as the outline's "Watch
  out" section already flags) that `(QM-ineq)` is used only once, in step 1
  — the builder should make sure the written proof doesn't implicitly reuse
  it anywhere in steps 3–4 (it doesn't, per my check above, but this is worth
  a one-line remark in the final write-up for the reviewer's benefit).
- Name the classical inequality explicitly in the final proof text (`QM ≥
  AM ≥ GM` for two positive reals) with its `knowledge_base.md` citation, as
  the outline's step 5 / "Watch out" section already instructs — just
  flagging it's a hard requirement per CLAUDE.md's "Name your tools" rule,
  not something the outline got wrong.

## Bottom line

Both potentially fragile pieces of algebra (the FE derivation and the
quadratic-defect identity) check out **exactly**, symbolically, with no
approximation. The telescoping argument produces **two-sided** bounds (not a
one-sided bound that would only give an inequality, not equality), and
correctly invokes the Archimedean property rather than hidden continuity or
calculus. Case coverage (necessity + sufficiency, full domain) is complete.
No dead end from `results/imo-2026-05.md` is being repeated. **Approve** —
the proof-builder should proceed to write this up as a full rigorous proof,
addressing only the cosmetic items above.
