# Round 5 proof-reviewer report — imo-2026-02

Reviewed all four built approaches. Independently rebuilt every load-bearing
new symbolic claim from scratch (own `sympy` scripts — not the builders'
code, not trusting displayed formulas without re-derivation). No approach
reaches `solved` this round. `current.md` Status remains `partial`, updated
with a new "Round 5" adjudication section (preserving all prior rounds).

## 1. `coordinate-bash-resultant-boundary` — CHANGES REQUESTED (Status: partial)

**Claim under test**: the new §11 sign lemma `A_2<0` and the resultant
identity `Res_{s2}(G2a,L1)=4u(1+u^2)^3 F1 F2`, plus the disclosure that
`G2b` is not yet ruled out.

**Independent verification (full rebuild, own script):**
- Recovered the exact `G_{2a}(s_2,u,a,b,cc)` polynomial from the
  already-certified `coordinate-bash-resultant.md` §4 (not re-derived from
  the eq2/hypothesis-2 construction itself — this base object has already
  been independently reproduced by the proof-reviewer in rounds 2–4 and is
  not re-litigated here).
- Rebuilt `L=C+s_2R(\beta)(A-C)`, `d(\beta)=(-\cos\beta,\sin\beta)` and
  `\mathrm{cross}(d,L-B)` from the raw geometric definitions (own
  Weierstrass substitution). **Caught and fixed a genuine tooling pitfall**:
  using `sympy.together()` then manually clearing the printed denominator
  gives a numerator that is NOT fully reduced (it can carry a spurious
  extra common factor with the denominator); using `sympy.cancel()`
  (coprime numerator/denominator) is required. After the fix, the exactly
  reduced numerator is affine in `s_2` with `P(u)=(1+u^2)F_1(u)` and
  `Q(u)=-4bu^3+4bu+cc\,u^4-6cc\,u^2+cc` — **exact match** with the file's
  Lemma 11.5 (zero symbolic difference).
- Extracted the coefficient of `s_2^2` in `G_{2a}` directly: equals
  `2(1+u^2)(cc(u^2-1)-2bu)`, **exact match** with Lemma 11.7's `A_2`
  formula. The sign proof (`A_2<0` throughout the valid range, via a case
  split on `\mathrm{sign}(b)`, trivial for `b\ge0`, a `\tan`-comparison
  `\angle B<\theta_0` for `b<0`) is elementary and correct — checked by
  hand, no gap.
- Computed `\mathrm{Res}_{s_2}(G_{2a},L_1)` via `sympy.resultant` from the
  exact `G_{2a}` and `L_1=P+s_2Q` polynomials (all four quantities now
  independently reconstructed, not copied). Result: **exactly**
  `4u(1+u^2)^3F_1F_2`, symbolic difference `0` after `sympy.expand`. This
  is a genuine, fully general (all `a,b,cc,u`) polynomial identity,
  independently re-confirmed, not merely re-reported.

**Verdict on §11**: Theorem 11.8 (and its `\sigma`-mirror Theorem 11.10) is
**correct and completely proved** — a real, closed, rigorous result: for
every triangle and every `\beta` in the valid range, exactly one of the two
roots of `G_{2a}(s_2)=0` satisfies the cross-product-sign test for "K
inside angle LBA" (given `L\in\triangle BNC`). No gap found.

**What remains open (correctly, honestly disclosed by the file, not
overclaimed)**: the extraneous branch `G_{2b}`'s leading coefficient `B_2`
does not have fixed sign across triangles (checked only numerically, 3000
samples) — so `G_{2b}` is not yet ruled out as a competing solution; the
magnitude bound `t_1<t_1^{\max}(\beta)` (flagged since round 4) is still
needed; and the population's standing conjecture that `G_{2a}=0` (not
`G_{2b}=0`) is itself the geometrically genuine branch is *used*, not
re-derived, by §11. Gap 2 (branch selection) is **not** closed. Status
`partial` is accurate; no overclaiming found.

**Certified**: `lemmas/cross-product-sign-selection-G2a.md`.

## 2. `ptolemy-trig-identity` — CHANGES REQUESTED (Status: partial)

**Claim under test**: the resultant-elimination reduction of `F>4` to
`\Psi(\tau,A,C)>0`, and the exact value `\Psi(0,A,C)=4\sin^3A\sin B\sin C`.

**Independent verification (full rebuild, own script, algebraic-symbol
technique to avoid slow trig simplification — `sa,ca,sc,cc` for
`\sin A,\cos A,\sin C,\cos C`, `\sin B=sa\cdot cc+ca\cdot sc`):**
- Rebuilt `\tilde P_1,\tilde Q_1,\tilde R_1` (Step 1's direct quadratic for
  `U=\cot\alpha`) two ways: (a) directly from the file's displayed
  formulas, (b) independently, by substituting `U=p+2x` (`p=\cot\theta`)
  into the already-certified `\cot\psi`-quadratic `c_1x^2+b_1x+a_1=0` and
  checking proportionality numerically at a generic point (`\theta=0.37,
  A=1.1,C=0.65`). **Confirmed proportional** — identical ratio
  `≈1.7385` across all three coefficients (`U^2,U^1,U^0`), i.e. the same
  equation up to an overall nonzero scalar. Step 1 is correct.
- Rebuilt `\Phi(U)=\tilde P_2n^2-\tilde Q_2nm+\tilde R_2m^2` and
  `\mathrm{Res}_U(\tilde P_1U^2+\tilde Q_1U+\tilde R_1,\Phi)` from scratch
  via `sympy.resultant`, then divided by the file's claimed prefactor
  `4\sin^2A\cdot(\tau\cos C-\sin C)\cdot(\sin B-\tau\cos B)`. **Found a
  genuine factor-of-4 discrepancy**: the remainder of this division is `0`
  (confirming the two linear factors and the divisibility structure are
  correct), but the resulting quotient's value at `\tau=0` is
  `\sin^3A\sin B\sin C` — one quarter of the file's own claimed
  `\Psi(0,A,C)=4\sin^3A\sin B\sin C`. Re-tried with the prefactor
  **without** the leading `4` (`\sin^2A\cdot(\ldots)` only): remainder
  still `0`, and the quotient's value at `\tau=0` is **exactly**
  `4\sin^3A\sin B\sin C`, matching the file's claim precisely. Confirmed
  at a second, independent rational-trig test triangle (both with exact
  `sympy.Rational` arithmetic, no floating-point rounding). **This is a
  cosmetic transcription error** — a stray factor of `4` in the displayed
  prefactor constant — analogous to prior rounds' "cosmetic, not
  substantive" write-up bugs (per the standing memory rule): the degree-6
  structure, both spurious linear factors, and the stated value of
  `\Psi(0,A,C)` are all correct once the constant is fixed.
- Step 4 (the two spurious linear factors `\tau\cos C-\sin C`,
  `\sin B-\tau\cos B` vanish only at the domain boundaries `\theta=C,B`,
  hence never on the open domain `0<\theta<\min(B,C)`) is an elementary
  `\tan`-injectivity argument, checked by hand — correct, no gap.
- Step 6 (domain path-connectedness) is a straightforward convexity/IVT
  topology argument — correct, no gap.

**Verdict**: the resultant-elimination technique and its main quantitative
output (`\Psi`, degree 6, `\Psi(0,A,C)=4\sin^3A\sin B\sin C`) are
substantively correct; one cosmetic constant needs fixing in the writeup
(now corrected in the certified lemma). `\Psi(\tau,A,C)>0$ for `\tau\ne0`
remains open — honestly disclosed as numeric-only (20,000 samples, zero
violations), not proved. The base-point evaluation (`F-4>0` at
`A=B=C=\pi/3,\theta=\pi/6`) is disclosed as 60-digit numerical, not exact
symbolic — also honest. Status `partial` accurate; no overclaiming found
beyond the now-corrected cosmetic constant.

**Certified (with correction)**:
`lemmas/ptolemy-resultant-elimination-to-sextic.md`.

## 3. `ptolemy-trig-identity-synthetic` — CHANGES REQUESTED (Status: partial)

**Claim under test**: Lemma T's reformulation, and the three negative
auxiliary-circle searches.

**Assessment**: Lemma T (`\angle BAK<\angle BAL \iff x_Ky_L-x_Ly_K>0`) is
elementary and correct — cotangent is strictly decreasing on `(0,\pi)`, and
the algebra clearing `y_K,y_L>0` denominators is straightforward; checked
by hand, no gap. The "Remark" (an independent foot-of-perpendicular
re-derivation of the sibling's `\cot\alpha=\cot\theta+2\cot\psi` identity)
is a genuinely different, more elementary proof (right-triangle
trigonometry only) — checked by hand, correct, and a nice reusable
contribution. Search 3 (the circle `A,K,L,Q` itself cannot be used) is
logically airtight: using the target circle's existence to derive the
target order is transparently circular. Searches 1–2 (nine-point circle;
circle through `B,C`) give *informal* dimension-count / non-constant-angle
arguments, not formal impossibility proofs — but the file does not
overclaim them as such; it explicitly frames them as "reasoned negative
evidence" while conceding no fixed circle was rigorously ruled out in full
generality. This is honest self-labeling, consistent with `partial`.

**Verdict**: real, if modest, new content (Lemma T + its remark), and
useful, honestly-hedged negative information for the population (searches
1-3). Does not independently close the shared gap — the file itself
correctly says so. No overclaiming found. Not certifying Lemma T as a
standalone lemma file this round (folded into the sibling's bookkeeping
instead) since it does not yet unlock further progress beyond restating
the target in a new form; can be certified once/if it's actually load-
bearing for a completed proof.

## 4. `fixed-point-concyclic` — CHANGES REQUESTED (Status: partial)

**Claim under test**: the negative/retirement diagnosis — that no ideal
generator of the "ratio-is-real" species can repair the Step-4 gap.

**Assessment**: §5.1's structural point (an open betweenness condition
cannot literally be a polynomial ideal generator without asserting a false
boundary equality) is correct and elementary — a clean codimension
argument. §5.3's general dimension/type argument (no finite extension by
"ratio-is-real"-species generators can force `T` into the ideal, because
the missing constraint is the antiholomorphic reality condition
`\mathrm{Kb}=\bar K$ etc., invisible to any polynomial ideal in the
independent variables) is valid reasoning and does not depend on
re-verifying §5.2's specific displayed Gröbner remainder — I did not
independently recompute §5.2's exact polynomial remainder this round (time
budget), but the round's headline conclusion ("this method, not just this
round's choice of generators, cannot be repaired") follows from §5.3 alone.
This is flagged here as the one piece not independently re-derived this
round (a modest verification gap on my part, not a claim of error in the
file) — future rounds' reviewers should spot-check §5.2's remainder
directly if this route is revisited.

**Verdict**: a genuine, precisely-diagnosed negative result, correctly not
overclaimed as closing the gap (the file explicitly frames it as retiring
one lever, not the whole route). Status `partial` accurate.

## Summary of actions taken

- All four approaches: **CHANGES REQUESTED**. None reach `solved`.
- Certified two new lemmas:
  - `lemmas/cross-product-sign-selection-G2a.md` (Theorem 11.8/11.10, fully
    independently re-verified, no gap).
  - `lemmas/ptolemy-resultant-elimination-to-sextic.md` (Round 5's
    resultant-elimination technique, certified **with a corrected
    constant** — the file's displayed `4\sin^2A` prefactor should be
    `\sin^2A`; this is documented as a cosmetic fix, not a retraction).
- `results/imo-2026-02/current.md` updated: new "Round 5" adjudication
  section added (preserving all prior rounds' history), Status remains
  `partial`.
- No lemma rejected this round (Lemma T from
  `ptolemy-trig-identity-synthetic` intentionally not promoted to a
  standalone file yet, per above — not a rejection of correctness, just
  not yet load-bearing).

## Net progress signal for the ranking

The strongest fully-independently-verified new result this round is
`coordinate-bash-resultant-boundary`'s Theorem 11.8 — a complete, gap-free,
all-triangle proof that "K inside angle LBA" selects a unique root of
`G_{2a}=0`. This is genuine progress on gap 2 (branch selection) but does
NOT close it: `G_{2b}` is not yet ruled out, and the magnitude bound and
the "G_{2a} is the genuine branch" identification remain open. Separately,
`ptolemy-trig-identity`'s route is now reduced to a single radical-free
sextic positivity claim (`\Psi>0`), a genuine simplification in kind from
two nested square roots — its single remaining gap is now about as sharp as
any in the whole population. Both routes remain live and roughly
comparably close to a full solve; recommend continuing to push both next
round, and specifically prioritizing an attempt at `\Psi(\tau,A,C)>0`
symbolically (e.g. via an SOS/Positivstellensatz search now that it is
polynomial and radical-free) as the single most concretely tractable
remaining target in the whole population.
