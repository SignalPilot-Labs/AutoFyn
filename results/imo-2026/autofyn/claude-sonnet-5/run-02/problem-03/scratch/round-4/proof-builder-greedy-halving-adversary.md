# Build report — greedy-halving-adversary, round 4

## What was attempted

Per the outline's move (a): retry Proposition 10's "Missing inequality"
using this round's new exact ladder identities ($p_i=2p_{i+1}$,
$p_i-\sum_{j>i}p_j=f(n)$ constant). Worked the algebra by hand and
cross-checked every step with exact `Fraction` arithmetic (scripts in
`/tmp/round-4/`: `check1.py`, `check2.py`, `check3.py`,
`verify_general.py`).

## What was found

1. **A real, previously-unfilled gap in Proposition 10 itself.** The
   proposition's statement promised to "treat the two cases $f_1>r$ and
   $f_1\le r$" but only the $f_1>r$ case was ever written out. Filled in
   the missing case (new Lemma 10) — a direct instantiation of the
   already-certified `cross-term-identity-threshold`, no new machinery
   needed.
2. **A genuinely new, fully rigorous partial result (Proposition 13).**
   If Xiang Yu spends his $c=1$ cut on $p_1$ *symmetrically*
   ($f_1=f_2=p_1/2$), the cross term in Proposition 10 vanishes
   identically (both fragments equal $\Rightarrow$ the odd-parity
   indicator of $F$ is identically $0$), collapsing the whole argument to
   $A(F\cup G')=A(G')$. Combined with the exact **tail self-similarity**
   fact (the ladder's tail, rescaled, is *exactly* the $(n-1)$-ladder —
   proved cleanly from the round-4 identities, new Lemma 11) and the exact
   identity $r\cdot f(n-1)=a_n$ (new Lemma 12), a clean strong-induction
   argument shows: for *every* legal tail refinement $G'$ (not a
   restricted family), $\Phi\ge p_1$. This is **unconditionally proved for
   $n=3$** (since $c(2)=4/7$'s lower-bound half is already fully certified)
   and a valid conditional/recursive reduction for general $n$.
3. **The residual gap is now sharper and localized.** Asymmetric $c=1$
   splits: numerically dominated by the symmetric split (checked $n=3$,
   several $f_1$ values, random search), but the natural
   "derivative-in-imbalance" proof attempt fails to be sign-definite (it
   depends on $G'$'s fine local structure at two specific points, not
   aggregate quantities). A concrete near-optimal witness at $n=3$,
   $f_1=0.6p_1$ shows the trade-off exactly: the cross-term integral
   saturates its trivial bound ($I=(f_1-f_2)/2$ exactly) while $A(G')$
   sits strictly above its recursive-minimum baseline to compensate — a
   clean illustration of the anti-concentration phenomenon, but not a
   proof. $c\ge2$ is untouched (the vanishing-cross-term mechanism needs
   exactly two equal fragments).

## Honest assessment

This is real forward progress — a filled rigor gap, one new fully-closed
sub-case for $n=3$, and a reusable recursive reduction/technique for
general $n$ — but it does **not** close Proposition 10's Missing
Inequality in general. Per the outline's move (b), the fallback is
recorded explicitly in the approach file: if the sibling
`rank-pigeonhole-budget` (this round's discrete pigeonhole/majorization
recast) succeeds in closing the same gap, future builders on this
approach should import that result rather than re-attempting the integral
route a further time. The new lemmas (`tail-self-similarity`,
`symmetric-split-c1-lower-bound`) are general-purpose and independent of
which route eventually closes the residual gap.

## Files changed

- `results/imo-2026-03/approaches/greedy-halving-adversary.md` — added
  Lemmas 10–12, Proposition 13, updated Status/Approaches
  tried/Current best/Open gaps/Promotable lemmas.
- `results/imo-2026-03/lemmas/tail-self-similarity.md` — new, proposed for
  certification.
- `results/imo-2026-03/lemmas/symmetric-split-c1-lower-bound.md` — new,
  proposed for certification.
- `results/imo-2026-03/current.md` — appended round-4 summary to
  `greedy-halving-adversary`'s entry under Approaches tried.

Status remains `partial` (unchanged) — the general lower bound for $c\ge1$
is still open, now with two new lemmas and a fully closed $n=3$ sub-case.
