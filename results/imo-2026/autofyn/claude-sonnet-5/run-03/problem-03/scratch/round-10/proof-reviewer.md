# Proof review — round 10 — imo-2026-03

Reviewed all four built slugs independently. Method: for each round-10 claim,
re-derived the key identity/algebra/construction from scratch with my own
`python3`/`Fraction` scripts (not the builders'), and traced hypotheses of any
cited certified lemma against the actual instantiation. All four approaches
report Status `partial` honestly — no overclaim found in any of them (no
Status was mismatched with what is actually proved). All four made genuine,
verifiable progress this round.

---

## 1. global-lp-vertex-sufficiency — CHANGES REQUESTED (Status: partial)

**Claim under test:** the round-9 reviewer-found gap (candidate functional
list $L$ for the Finite-Cell Affine-Vertex Reduction Theorem missing $p_k$) is
fixed; plus three new theorems (Region-Vertex Classification, Boundary
Continuity, exact vertex closure via $k$-Anchor-Merge) fully close the
region-only candidate sub-list $Q_{\mathrm{region}}$.

**Verification performed:**
- Re-derived the sign function $N(n,j)=j(2n+1-2^{n+1})+(2^{n+2}-n^2-n-2)$
  independently and computed it for $n=2,\dots,9$, all $j$: matches the file's
  closed form and sign claims (A, B, C) exactly, including the special
  identity $N(n,2)=n(3-n)$ (so $e_2$ crosses the sign boundary exactly at
  $n=2,3$).
- Independently reconstructed the coordinates of $e_0$ and $e_1$ from the
  file's closed-form slack formulas, applied the stated $k$-Anchor-Merge
  construction literally (including the untouched copy of each paired piece
  at multiplicity 2, a known past bug class in this project), and computed
  OddSum by direct sort-and-sum for $n=2,\dots,8$ (14 instances total): every
  instance matches the claimed parity rule exactly ($\mathrm{OddSum}=1/2$
  when the pair count $k$ is even, $=c(n)$ when odd), zero deviation.
- Checked the fix itself: $L$ without $p_k$ is indeed unbounded and admits
  $p_k<0$ (the gap the round-9 reviewer found); adding $p_k$ restores
  boundedness, and $p_i\ge0$ for $i<k$ remains redundant given the gap chain
  once $p_k\ge0$ holds — a correct, narrow, targeted fix, exactly as
  diagnosed last round.
- Lemmas 4.1/4.2 (cell-wise constancy; closed-cell boundary via
  density+continuity) are unaffected by the fix, since they only use
  finiteness/affineness of $L$, never an enumerated member list — confirmed
  by re-reading both proofs.
- Small-Mass Insertion Lemma and Boundary Continuity Theorem: elementary
  telescoping-sum / Lipschitz-sandwich arguments, checked step by step, no
  gap found.

**Verdict.** All claimed new content this round is correct. The theorem is
genuinely stronger than round 9 (round 9 only fixed the mechanism in
principle; round 10 actually closes an entire, previously-unaddressed
sub-family of candidates, $Q_{\mathrm{region}}$, in closed form for all
$n\ge2$). The approach is honest that the $\Sigma$-shape part of the
candidate set $Q$ (and the lack of a bound on $|\Sigma(n,k)|$) remains
entirely untouched, so the Existence Theorem itself is still open. Status
`partial` is correct — no overclaim. **CHANGES REQUESTED**: next round should
target either a bound on $|\Sigma(n,k)|$ restricted to few-split-piece shapes
(per the file's own priority list), or turn Section 5's numeric $n=6$,
3-piece survivor-closing construction into an exact-arithmetic result.

**Certified:**
`results/imo-2026-03/lemmas/finite-cell-vertex-reduction-and-region-classification.md`
— the corrected Finite-Cell Affine-Vertex Reduction Theorem, Small-Mass
Insertion Lemma, Boundary Continuity Theorem, Region-Vertex Classification
Theorem, and the exact closure of the region-only genuine vertices.

---

## 2. greedy-reduction-geometric — CHANGES REQUESTED (Status: partial)

**Claim under test:** Lemma M ($B''$-Banking Lemma) proved via the general
Theorem 7 (correcting the outline's citation of the insufficient Theorem 7a);
the "Candidate Swap Lemma" (natural additive-combination mechanism) is
refuted by an exact counterexample; Level-Absorption reduced to a $k=2$ base
case.

**Verification performed:**
- Checked Lemma M's instantiation of Theorem 7 (Joint Dominance-Chain
  Closure, top-levels-clear — this approach's own already-established
  content from round 5, not a borrowed crux) at parameters $(m',k')=(m-2,
  k-2)$: every hypothesis (range $0\le k'\le m'$, Dominance-Chain property
  and sum cap on $B''$, unsplit-top-levels shape of $S'''$) is met exactly as
  claimed. The correction (Theorem 7a is only the $k'=1$ base case,
  insufficient once $B''$ has $\ge2$ elements) is itself correct and
  precisely diagnosed.
- Independently re-checked the counterexample to the Candidate Swap Lemma by
  hand: $Q=\varnothing$, $b=10$, $P=\{6,6\}$. Hypotheses hold
  ($\mathrm{sum}(P)=12\ge10$, $\max(P)=6<10$). $\mathrm{OddSum}(P)$: sorted
  $\{6,6\}$, only rank-1 counts, so $\mathrm{OddSum}(P)=6$.
  $\mathrm{OddSum}(\{b\})=10$. $6<10$ — a genuine, verified violation. This
  is a clean, correct, easily-checked refutation.

**Verdict.** Both the positive result (Lemma M) and the negative result
(Candidate Swap refutation) are correct as claimed. Level-Absorption remains
open, honestly reported (the file explicitly states this, does not overclaim
a closure). The reduction to a $k=2$ base case is a real narrowing, though
only numerically supported (not proved) — correctly flagged as such. Status
`partial` is accurate. **CHANGES REQUESTED**: next round should attempt the
$k=2$ base case directly (the file's own recommended next step), which is now
a clean, self-contained target free of the $B''$ recursion layer.

**Certified:**
`results/imo-2026-03/lemmas/level-absorption-banking-lemma-and-swap-refutation.md`
— Lemma M and the Candidate Swap Lemma's refutation (recorded as a negative
result to prevent future rounds retrying the same mechanism).

---

## 3. self-similar-induction-on-n — CHANGES REQUESTED (Status: partial)

**Claim under test:** Lemma TPI (Tiny-Piece Insertion Monotonicity) proved in
full, closing gap (b)(i) of the Branch-I.A window's monotonicity question; an
"endpoint reduction identity" for gap (a), via the certified Companion
Peeling Lemma.

**Verification performed:**
- Lemma TPI: elementary three-line rank-shift argument (inserting an element
  $\delta\le\min(M)$ places it at the new last rank, contributing $\delta$
  only if the new total size is odd). Re-derived independently — correct,
  and correctly distinguished from the certified Schur-monotonicity dead end
  (this hypothesis, "$\delta$ below every element," is exactly the safe case).
- Endpoint reduction identity: re-derived the algebra independently.
  $\mathrm{sum}(D\cup T)=(2^{\ell-1}+\varepsilon)+(2^\ell-1)$; using
  $\mathrm{OddSum}+\mathrm{EvenSum}=\mathrm{sum}$ and the Companion Peeling
  Lemma ($\mathrm{EvenSum}(D\cup T)=\mathrm{OddSum}(D\cup T')$ since
  $2^{\ell-1}$ is the unique max), the target inequality
  $\mathrm{OddSum}(D\cup T)\le2^\ell+\varepsilon-1$ is exactly equivalent to
  $\mathrm{OddSum}(D\cup T')\ge2^{\ell-1}$. Confirmed correct by direct
  algebra.
- The file's own honest diagnosis — that the reduced target is structurally
  the same as the file's still-open $j\ge2$ trichotomy, one level down, not a
  smaller problem — is consistent with what I verified: the reduction is an
  exact equivalence, not a simplification into an already-solved case.

**Note on the dispatch summary.** The round-10 dispatch description claims
this approach "corrected a stale outliner claim about idx=1." I searched the
file for any mention of `idx` and found none — that correction (about the
triangular family's Multi-Piece Necessity, closed round 8) belongs entirely
to `lp-duality-split-polytope`'s file, which does make exactly this
correction. This appears to be a copy/mixup in the round's dispatch text, not
an actual false claim by `self-similar-induction-on-n` itself — no penalty
applied to this approach for it, but flagged so the mixup isn't propagated.

**Verdict.** Both results are correct and honestly scoped: gap (b)(i) is
genuinely closed; gap (a) is reduced (a real, exact equivalence) but not
closed, and the file correctly refuses to claim otherwise. Status `partial`
is accurate. **CHANGES REQUESTED**: next round's most concrete target is the
now-precisely-reduced $j=1$ sub-case of the window's top endpoint (the file's
own flagged "most promising concrete next step").

**Certified:**
`results/imo-2026-03/lemmas/tiny-piece-insertion-monotonicity-and-endpoint-reduction.md`
— Lemma TPI and the endpoint reduction identity.

---

## 4. lp-duality-split-polytope — CHANGES REQUESTED (Status: partial)

**Claim under test:** (i) correction that the round-10 outliner's "open
idx=1" claim is stale (already closed round 8); (ii) a new Multi-Piece
Sufficiency Theorem for the triangular family, full-budget construction,
every $n\ge3$.

**Verification performed:**
- (i) Checked against `current.md`'s own history and
  `lemmas/idx1-closure-and-full-multi-piece-necessity.md` (exists, certified
  round 8): confirms the file's correction is accurate — the round-10
  outliner's dispatch was indeed stale on this specific point.
- (ii) Independently re-implemented the construction from scratch in exact
  `Fraction` arithmetic (own script, not the builder's): for every $N=4,
  \dots,39$ (36 instances), verified the fragment multiset sums exactly to
  $D_n$, computed the *correctly-signed* alternating sum (caught and fixed a
  bug in my own first verification pass — I had implemented "sum of
  odd-ranked elements" instead of a true alternating $+,-,+,-,\dots$ sum;
  once corrected, the construction's claimed value $\mathrm{AltSum}(X')=
  2\varepsilon_N$ matched exactly in all 36 cases), and confirmed the final
  $\mathrm{OddSum}=\tfrac12+\tfrac12(c(n)-\tfrac12)$ is exactly correct and
  strictly less than $c(n)$ in every instance.
- Checked the scaling identity $\mathrm{OddSum}(X)=\tfrac12+\tfrac d2
  \mathrm{AltSum}(X')$ and the threshold bound $\mathrm{Thr}(N)<1$ for
  $N\ge4$ (induction, base case $N=4$: $10\le14$): both correct.

**Verdict.** Both claims hold up under independent, from-scratch verification.
This is a genuine, complete, exact-arithmetic positive result — not merely a
narrowing of the round-9 negative finding — giving a full
Necessity+Sufficiency picture for the triangular family specifically. The
file is explicit and correct that this does not resolve the general
upper-bound direction (relies on the AP-specific landmark structure; a
numerical check confirms the analogous construction fails on LB's own
geometric partition). Status `partial` is accurate (correctly does not claim
the general theorem). **CHANGES REQUESTED**: the approach's remaining role is
tool-supply to `global-lp-vertex-sufficiency`, or attempting the general
(non-AP) balanced-region sufficiency question directly.

**Certified:**
`results/imo-2026-03/lemmas/multi-piece-sufficiency-triangular-family.md` —
the Multi-Piece Sufficiency Theorem.

---

## Summary

| Slug | Status (true) | Verdict | New certified lemma |
|---|---|---|---|
| global-lp-vertex-sufficiency | partial | CHANGES REQUESTED | finite-cell-vertex-reduction-and-region-classification.md |
| greedy-reduction-geometric | partial | CHANGES REQUESTED | level-absorption-banking-lemma-and-swap-refutation.md |
| self-similar-induction-on-n | partial | CHANGES REQUESTED | tiny-piece-insertion-monotonicity-and-endpoint-reduction.md |
| lp-duality-split-polytope | partial | CHANGES REQUESTED | multi-piece-sufficiency-triangular-family.md |

No approach reached `solved` this round; no overclaim was found in any of the
four files (all Status labels match reality). `results/imo-2026-03/current.md`
updated with round-10 entries and a refreshed "Current best" reflecting all
four narrowings. All four `record_outcome` calls logged as `advanced`.

The overall problem (imo-2026-03) remains `partial`. The two genuinely open
gaps are unchanged in kind but narrower: (1) lower bound — the Branch-I.A
window (endpoint + gap (b)(i) settled, gap (a) reduced to the file's own
still-open $j\ge2$ trichotomy, gap (b)(ii) untouched) and Level-Absorption
(now a single $k=2$ base case); (2) upper bound — the balanced region's
$\Sigma$-shape candidate classification (region-only part now fully closed).
