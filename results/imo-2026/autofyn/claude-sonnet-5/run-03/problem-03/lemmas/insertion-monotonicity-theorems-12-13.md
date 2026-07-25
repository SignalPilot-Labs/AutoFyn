## Theorem 12/13 (Insertion Monotonicity): inserting positive mass into any multiset never decreases OddSum

Certified round 8. Proved in `approaches/greedy-reduction-geometric.md`
(round 8, section "12. Round 8: Insertion-Robustness closed in full").
Used to close Open Sub-Problem A (Insertion-Robustness of Theorem 7) in
full, unconditionally, dropping the previously-hypothesized cap
$\max(R_1)\le\mu_1$ entirely (shown unneeded).

**Theorem 12 (Single-Insertion Monotonicity).** Let $N$ be any finite
multiset of positive reals and $v>0$. Then
$$\mathrm{OddSum}(N\cup\{v\})\ \ge\ \mathrm{OddSum}(N),$$
and moreover $\mathrm{OddSum}(N\cup\{v\})\le\mathrm{OddSum}(N)+v$.

**Proof (reviewer's independent re-derivation, confirming the approach
file's).** Sort $N$ descending; inserting $v$ at sorted position $p+1$
(i.e. exactly $p$ elements of $N$ exceed $v$) shifts every element
originally at rank $\ge p+1$ down by one rank, flipping its parity, and
inserts $v$ itself at rank $p+1$.

- If $p$ is even (so $v$ lands at an odd rank, contributing $+v$ to the
  new OddSum): let $\mathrm{Suf}$ be the suffix of $N$ from original rank
  $p+1$ on. Since $p$ is even, original rank parities on $\mathrm{Suf}$
  agree with $\mathrm{Suf}$'s own relative rank parities (both start "odd"
  at the first suffix element). The rank-shift flips every suffix
  element's counted/uncounted status, so the suffix's net contribution
  changes by $-\mathrm{AltSum}(\mathrm{Suf})$ (using $\mathrm{Suf}$'s own
  sorted order). Total change $=v-\mathrm{AltSum}(\mathrm{Suf})$. Since $v$
  must exceed every element of $\mathrm{Suf}$ (it was inserted above them),
  $v>\max(\mathrm{Suf})\ge\mathrm{AltSum}(\mathrm{Suf})$ (Upper-bound fact),
  so the change is $>0$ (in particular $\ge0$), and since
  $\mathrm{AltSum}(\mathrm{Suf})\ge0$ (Nonnegativity fact) the change is
  also $\le v$.
- If $p$ is odd ($v$ lands at an even rank, contributing $0$): original
  rank parities on $\mathrm{Suf}$ are exactly flipped relative to
  $\mathrm{Suf}$'s own relative ranks, so the net change from the suffix is
  $+\mathrm{AltSum}(\mathrm{Suf})\ge0$ (Nonnegativity fact), and $v$
  contributes $0$, so total change $=\mathrm{AltSum}(\mathrm{Suf})\in
  [0,\max(\mathrm{Suf})]\subseteq[0,v]$ (since $v\ge\max(\mathrm{Suf})$ here
  too — $v$ sits above the suffix regardless of parity).

Both cases give change $\in[0,v]$. $\blacksquare$

**Theorem 13 (General Insertion Monotonicity).** For any finite multisets
$N,R$ of positive reals: $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$.

**Proof.** Induction on $|R|$, chaining Theorem 12 one element at a time:
inserting elements of $R$ one at a time into $N$ (in any order) can only
weakly increase OddSum at each step by Theorem 12, so the final value
$\mathrm{OddSum}(N\cup R)$ is $\ge\mathrm{OddSum}(N)$. $\blacksquare$

**Reviewer verification (round 8, independent, exact `Fraction`
arithmetic, from-scratch script).**
- Re-derived the rank-shift/parity argument above independently from the
  approach file's own write-up (same conclusion, written without reading
  the file's derivation line-by-line first, as a genuine independent
  re-proof), including checking the boundary case where $v$ ties with an
  element of $N$ (peel/insert conventions handle ties by "insert one copy
  at that rank," harmless).
- 50,000 random trials, $|N|,|R|\in\{1,\ldots,6\}$, random positive
  rationals (including many forced ties via small integer values): zero
  violations of $\mathrm{OddSum}(N\cup R)\ge\mathrm{OddSum}(N)$.

**Application (Open Sub-Problem A, closed).** Given $(B',S'')$ satisfying
Theorem 7's hypotheses (so $\mathrm{OddSum}(B'\cup S'')\ge S'$ already
known) and any finite multiset $R_1$ of positive reals (no restriction on
$\max(R_1)$ needed): by Theorem 13 with $N:=B'\cup S''$, $R:=R_1$,
$$\mathrm{OddSum}(B'\cup S''\cup R_1)\ge\mathrm{OddSum}(B'\cup S'')\ge S'.$$
This settles Open Sub-Problem A (Insertion-Robustness of Theorem 7) in
full, unconditionally — the hypothesis $\max(R_1)\le\mu_1$ present in the
sub-problem's original statement was never needed. Reviewer confirms this
chain of inequalities is a direct, correct application (no gap).

**Scope note.** This closes Subcase (a) ($\mu_1\ge b_2$) of the inductive
step of Theorem 7'$(m,k;L)$ in `greedy-reduction-geometric`. Subcase (b)
(Open Sub-Problem B, Level-Absorption) remains open and is untouched by
this result.
