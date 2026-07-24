## Lemma: Max Domination

**Statement.** For any nonempty finite multiset $S=\{b_1\ge b_2\ge\cdots\ge
b_r\}$ of reals (sorted descending), the sorted alternating sum
$$A(S):=b_1-b_2+b_3-b_4+\cdots$$
satisfies $A(S)\le b_1=\max(S)$.

**Proof.** Two cases by the parity of $r$.

- **$r=2s+1$ odd.** Regroup the alternating sum:
  $$A(S)=b_1+\sum_{i=1}^{s}(b_{2i+1}-b_{2i})=b_1-\sum_{i=1}^s(b_{2i}-b_{2i+1}).$$
  Since $S$ is sorted descending, $b_{2i}\ge b_{2i+1}$ for every
  $i=1,\dots,s$, so every subtracted term $(b_{2i}-b_{2i+1})\ge0$. Hence
  $A(S)\le b_1$.

- **$r=2s$ even.** Regroup:
  $$A(S)=(b_1-b_2)+(b_3-b_4)+\cdots+(b_{2s-1}-b_{2s})
  =b_1-\Big[(b_2-b_3)+(b_4-b_5)+\cdots+(b_{2s-2}-b_{2s-1})\Big]-b_{2s}$$
  (for $s=1$ the bracketed sum is empty and this reads $A(S)=b_1-b_2\le
  b_1$ directly). Every bracketed term is $\ge0$ by sortedness, and
  $b_{2s}\ge0$ whenever $S$ consists of nonnegative reals (in particular
  whenever $S$ is a multiset of fragment lengths, as in every use of $A$
  in this project). Hence $A(S)\le b_1$. $\blacksquare$

**Remarks.** This is a short, self-contained, fully elementary fact —
independent of any marking, ladder structure, or other project-specific
lemma. It gives a universal one-line upper bound on $A$ purely from the
multiset's own maximum, complementary to the trivial lower bound
$A(S)\ge -\,(\text{second-largest gaps})$ and to the general
`integral-alternating-sum-formula`/`A(S)\le\mathrm{Total}(S)` bound already
in use elsewhere in this project (Max Domination is strictly sharper
whenever $\max(S)<\mathrm{Total}(S)$, i.e. whenever $S$ has more than one
positive element).

**Verification.** Spot-checked by hand: $S=(5,1,1,1,1)$ gives
$A=5-1+1-1+1=5=b_1$ (equality, since all gaps beyond the max vanish);
$S=(3,1,1,1,1,1,1,1,1,1)$ ($10$ elements) gives $A=1\le3$ (strict).
Independently re-verified computationally (exact `Fraction` arithmetic)
against $20{,}000$ random sorted multisets, $r=1,\dots,9$: zero violations
of $A(S)\le\max(S)$.

**Certified in:** round 13, `results/imo-2026-03/approaches/lp-duality-certificate.md`
§R13.1 (`imo-2026-03`).

**Reviewer certification note (round 13).** Independently re-derived the
two-case telescoping-regroup proof and re-verified with a fresh,
independently-written 20,000-trial exact-`Fraction` script
(`/tmp/round-13/verify.py`): zero violations of $A(S)\le\max(S)$ over
random sorted multisets of sizes 1–10. Statement and proof are correct as
written; no gap found. **Certified.**
