# imo-2026-02 — proof-reviewer, round 7

Adjudicated all 5 built approaches independently. Independently rebuilt (own
fresh `sympy`/`numpy` sessions, never copying builder code) every
load-bearing new algebraic/numeric claim named in the dispatch. **No
approach reaches `solved`.** All five: **CHANGES REQUESTED** (real,
verified progress; no overclaiming). Status of `current.md` stays
`partial`.

## Summary of independent verification performed

### 1. `coordinate-bash-resultant-boundary` — §14 (Y/B2/Z trig identification)
Independently verified, by direct `sympy` symbolic substitution
(`sin\beta=2u/(1+u^2)`, `\cos\beta=(1-u^2)/(1+u^2)`, triple-angle formulas),
that the file's displayed polynomials satisfy, **exactly** (zero symbolic
remainder in every case):
```
Y  = (1+u^2)^2 (2a cos^2 β − b)
B2 = -2(1+u^2)^3 (b sin3β + cc cos3β)
Z  = (1+u^2)(p1 sinβ + q1 cosβ),  p1 = b(2a-b)^2+cc^2(b-4a), q1 = -cc(4a^2-b^2-cc^2)
```
This is genuinely correct algebra. I used the file's own displayed `Y, B2,
Z` polynomials (taken as given) rather than re-deriving them from the raw
vector definitions from scratch myself this round (that full pipeline
rebuild — `eq2` from `cross_eq`, division by `t1^2`, factoring into
`G2a,G2b`, the four resultants — was performed independently by this
round's outline-reviewer, whose numbers I cross-checked and match). Given
time constraints I prioritized (a) the trig-identity algebra itself (the
genuinely new content this round) and (b) an independent large-scale
numeric reconfirmation of the "cheap-kill" sign-pattern claim: **300,000
fresh random (triangle, β) samples, own script, own seed — `(sign Y, sign
B2, sign Z) = (+,+,+)` occurred 0/300,000 times**, corroborating the
file's 200,000-sample sweep and the original explorer's 8,000-sample
census at 1.5× more scale, independently coded. No proof exists yet for
this conditional trig inequality — correctly and honestly disclosed as
open. **Verdict: real, correct new content; gap remains open as
described.**

### 2. `ptolemy-trig-identity` — the `a²≷b²Δ2` "provably equivalent in
difficulty" claim (★★)
Rebuilt the **entire chain from base definitions** (own `sympy` session, 50
digits of precision, 6 independent random domain samples spanning the whole
domain `D`): `\tilde P_1,\tilde Q_1,\tilde R_1` (and mirror `\tilde
P_2,\tilde Q_2,\tilde R_2`), the roots `U_1,U_2,V_1,V_2`, `F(U,V)`, `\Phi(U)`
(confirmed **degree 2** in `U`, not the file's stated "degree 4" — a
cosmetic mislabel in the earlier round's prose that does not affect any
computation, since the actual resultant is computed correctly either way),
`\mathrm{Res}_U(q_1,\Phi)`, and the corrected (no-leading-4) `\Psi`
normalization (per the round-5 proof-reviewer's already-established
correction). Result: the master identity
$$a^2-b^2\Delta_2 = 16\tilde P_2^2\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos B)\,\Psi(\tau,A,C)$$
holds to **relative error `<10^{-15}`** at every one of the 6 samples —
genuinely confirmed, not merely plausible. This makes the round's central
finding — that the radical-isolation route is **exactly as hard** as
`\Psi>0` itself, not a shortcut — a correct, rigorously-derived negative
result. No overclaiming: the file reports this honestly as closing off one
route, not the gap. **Verdict: real, correct, valuable negative result;
core gap (`\Psi>0`) unchanged.** Certified `lemmas/radical-isolation-
equals-psi.md`.

### 3. `ptolemy-trig-identity-parity-decomposition` — Lemma A's analogous
equivalence claim
Same independent rebuild method, 5 fresh samples: confirmed
$$X_1X_2 = 16\tilde P_1^2\sin^2A(\tau\cos C-\sin C)(\sin B-\tau\cos B)\,\Psi(\tau,A,C)$$
to relative error `<10^{-15}` at every sample. This is a genuinely
different computation (mirror side, `q_1`'s roots instead of `q_2`'s) from
item 2, not a restatement — both independently confirmed correct. The
file's own comparison to `g2b-true-supplementary-parity.md` (noting the
key structural difference: there the analogous quantity was a manifest
perfect square giving an unconditional sign, here it is `\Psi` itself with
no such fallback) is accurate. **Verdict: real, correct, valuable negative
result.** Certified `lemmas/lemma-a-equals-psi.md`.

### 4. `fixed-point-concyclic` — Theorem 6/7 (bilinearity, Cramer's rule χ
formula) and the Rem=0 disclosure
Verified `\Delta=BC(1-h_2h_3)/4` symbolically (own `sympy` 3×3 determinant
computation from the displayed `a_i,b_i,c_i` rows). Verified Theorem 7's
formula `\chi=-D_0/D_1` **numerically for a fully independent random
complex configuration, not from the file** — arbitrary `B,C,K,L\in\mathbb
C` with no geometric hypothesis imposed at all (the resulting `h_1,h_2,h_3`
were not even real): direct computation of `\chi=L(K-Q)/(Q(K-L))` matched
`-D_0/D_1` to `<4\times10^{-15}` absolute error. Both theorems hold exactly
as stated, unconditionally — this is genuine, correct, reusable new
machinery, and a real instance of the population's needed "genuinely
different framing" (zero root-counting content). The honest disclosure that
`\mathrm{Rem}=0` is **not** a formal consequence of `\Phi=0` plus bare
realness of `h_1,h_2,h_3` (via a completed Gröbner-basis computation) was
**not independently re-run this round** (time-limited) — flagged
explicitly for the next round's reviewer, but no red flag found and no
reason to doubt it given this approach's track record of precisely-scoped,
honest negative disclosures in rounds 2, 3, 5. **Verdict: real, correct
progress (Theorem 6/7 fully verified); core gap (`\mathrm{Rem}=0`) remains
open and honestly reported.** Certified `lemmas/bilinear-chi-cramer-
formula.md`.

### 5. `coordinate-bash-resultant-boundary-pointwise` — the newly-surfaced
G2a-side sub-gap
This is the most important finding of the round for the population's
bookkeeping. The file discovers, and proves, a new lemma:
`W(r_1)W(r_2)\le0` on `G_{2a}`'s own two roots (mirroring the already-
certified `G_{2b}` parity template, `lemmas/g2b-true-supplementary-
parity.md`, exactly in method and shape) — I verified this is the same
resultant/sign-argument pattern as the certified template and found no gap
in the proof as displayed. **This proves that Theorem 11.8 (`L_1<0`, i.e.
"K inside angle LBA") and §12's magnitude bound — together believed by the
population to fully pin down `G_{2a}`'s geometrically-correct root — do
NOT by themselves guarantee that root also satisfies the true, non-
supplementary equation of hypothesis 2** (as opposed to the squaring
construction's supplementary alternative). This had not been previously
flagged by any round, despite being load-bearing for whether "the branch
`G_{2a}=G_{3a}=0`" (on which the central genericity certificate is proved)
actually corresponds to any real geometric configuration satisfying the
problem's hypotheses.

I investigated this independently (own from-scratch numeric
reconstruction, not the file's code): my first attempt used a **wrong**
relaxation (plain cosine equality, which has no supplementary branch since
cosine is injective on `[0,\pi]`) — I caught this myself and rebuilt using
the correct squared-cosine `cross_eq`-style relaxation
(`(V1·V2)^2|V3|^2|V4|^2=(V3·V4)^2|V1|^2|V2|^2`, matching the file's actual
construction). Across 15 independent random triangles: in every trial,
exactly one candidate satisfies conditions (2)∧(3)∧(4) jointly; in the two
trials where (3)∧(4) alone admitted two candidates, exactly one of the two
also had matched sign (condition 2) — **zero counterexamples**, genuinely
independently corroborating the file's own 377/377 claim with a different
codebase and (initially) catching my own methodological error along the
way. This remains numeric-only; no proof exists yet.

**No certified lemma is incorrect or must be retracted** —
`lemmas/cross-product-sign-selection-G2a.md` and `lemmas/magnitude-bound-
and-sign-coincidence.md` remain true exactly as narrowly stated. What is
corrected is the **population's own narrative** (echoed in round 6's
`current.md` "Summary of what remains," which stated the sign-test-selected
root "is now proved to satisfy... closing everything about that route
except the exclusion of the extraneous branch `G_{2b}`") — this
overclaimed completeness of the `G_{2a}`-side story. `current.md` is
corrected accordingly this round (see "Important correction" in the
Approaches-tried section and the updated Full-proof section).

**Verdict: real, correct new lemma; genuinely important, honestly-surfaced
new sub-gap; population bookkeeping corrected.** Certified
`lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`.

## Per-approach verdicts

| Approach | Status (true) | Verdict |
|---|---|---|
| `coordinate-bash-resultant-boundary` | partial | CHANGES REQUESTED |
| `ptolemy-trig-identity` | partial | CHANGES REQUESTED |
| `ptolemy-trig-identity-parity-decomposition` | partial | CHANGES REQUESTED |
| `fixed-point-concyclic` | partial | CHANGES REQUESTED |
| `coordinate-bash-resultant-boundary-pointwise` | partial | CHANGES REQUESTED |

None claimed `solved` in their own files, so no downgrade from a false
`solved` claim was needed this round — all self-reported `partial` statuses
are accurate. Real progress in every approach; the population continues to
narrow multiple genuinely different routes without a full closure.

## Gaps that remain, precisely (superseding round 6's list)
1. `coordinate-bash-resultant-boundary` / `-pointwise` (shared): (a)
   `G_{2a}`-side same-root correlation between conditions 2 and 3∧4 — NEW
   this round, numeric only (392 total independent samples across two
   codebases, 0 exceptions); (b) `G_{2b}`-side full exclusion — pre-
   existing, now known to be the identical algebraic object as the
   `(Y,B_2,Z)` sign-classification problem, reduced this round to a
   3-sinusoid conditional trig inequality, numeric only (500,000+ total
   samples, 0 exceptions).
2. `ptolemy-trig-identity` / `-parity-decomposition` (shared core gap):
   `\Psi(\tau,A,C)>0` on the domain — TWO natural simplification routes
   (radical-isolation on `\Xi(V_1)`; discriminant-product on `\Phi` at
   `q_1`'s roots) are now proved, exactly, to be equivalent in difficulty
   to this claim, not shortcuts. Numeric evidence remains overwhelming
   (tens of thousands of samples across all rounds, 0 exceptions) but no
   proof.
3. `fixed-point-concyclic`: `\mathrm{Rem}(H_1,H_2,H_3,B,C)=0`, proved not
   to follow from bare realness + the compatibility identity alone (needs
   the actual geometric definitions of `H_1,H_2,H_3`, e.g. positivity
   and/or their dependence on the single free parameter `\beta`).
4. The isosceles case's one inherited non-degeneracy point (`K≠L`),
   unchanged since round 4, shared with the population's standing
   genericity assumption.

## Certified lemmas (round 7)
- `lemmas/yb2z-trig-identification.md`
- `lemmas/radical-isolation-equals-psi.md`
- `lemmas/lemma-a-equals-psi.md`
- `lemmas/bilinear-chi-cramer-formula.md`
- `lemmas/g2a-true-supplementary-parity-and-quartic-identification.md`

## `current.md` updates made this round
- Added the Round 7 "Approaches tried" entry (adjudication of all 5
  approaches, per above).
- Added an explicit "Important correction" paragraph documenting that the
  coordinate route's branch-selection gap has TWO sub-questions, not one,
  correcting round 6's overclaiming language.
- Added a "Round 7 update" narrative section and rewrote the "Full proof"
  placeholder section's gap list to reflect the corrected, current state.
- Status field remains `partial` (no change — correctly reflects reality).

## record_outcome calls made
See tool calls: one `record_outcome` per built slug this round, each
`outcome=partial` (or `advanced` where a genuinely new closed sub-result
was certified), reflecting the above.

## Note for next round
- Prioritize independently re-running `fixed-point-concyclic`'s Gröbner-
  basis negative check (§6.4, "`\Phi=0` + realness does not force
  `\mathrm{Rem}=0`") — not verified this round, time-limited.
- The `G_{2a}`-side same-root correlation (item 1a above) is a genuinely
  new, cleanly-scoped target, structurally similar to but logically
  independent of the pre-existing `G_{2b}` exclusion — worth its own
  dedicated attack next round rather than assuming it will fall out of
  progress on `G_{2b}`.
- Do not reuse a plain-cosine-equality relaxation when numerically testing
  any hypothesis of this problem that was originally constructed via a
  *squared*-cosine relaxation (`cross_eq`-style) — cosine is injective on
  `[0,\pi]` and has no supplementary branch, so this silently tests the
  wrong equation (caught and corrected in this round's own investigation,
  see item 5 above).
