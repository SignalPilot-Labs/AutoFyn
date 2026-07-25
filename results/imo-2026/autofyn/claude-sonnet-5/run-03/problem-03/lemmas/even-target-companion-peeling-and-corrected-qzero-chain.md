# Even-target Companion Peeling identity, and the corrected e-fold q=0-chain closed form

Certified round 17, from `approaches/self-similar-induction-on-n.md`, round-17
section ("Round 17: the corrected $e$-fold telescoping identity..."). Both
results below are independently re-derived and re-verified by the
proof-reviewer from scratch (own exact-`Fraction` scripts, not the builder's),
and are certified exactly as stated. **This file does NOT certify the round's
further headline claim ("Sub-case (i) Full Closure for every $e\ge1$")** — see
`current.md` for the precise, corrected scope of what that claim actually
establishes (a genuine residual gap was found in the odd-excess branch outside
the width-1 window; recorded there, not here).

## Even-target Companion Peeling identity (general, elementary)

**Statement.** For any finite multiset $S$ of positive reals with a unique
maximum $x$: $\mathrm{EvenSum}(S)=\mathrm{OddSum}(S\setminus\{x\})$.

**Proof.** Removing the unique maximum from a descending sort shifts every
remaining element's global rank down by exactly $1$, flipping parity; summing
over even-ranked elements of $S$ is therefore the same as summing over
odd-ranked elements of $S\setminus\{x\}$. $\blacksquare$

**Reviewer independent re-verification.** Own fresh script (`verify_general.py`),
$20{,}000$ random trials with a uniquely-determined maximum enforced: zero
violations. This is the direct complement of the file's original
(already-certified) Global-max Peeling identity
$\mathrm{OddSum}(S)=x+\mathrm{EvenSum}(S\setminus\{x\})$.

## Corrected $e$-fold $q=0$-chain closed form

**Setting.** Fix a finite multiset $D$ with $\max(D)\le2^k$ for some $k\ge1$;
$m\ge k+1$; write, for level index $i\ge1$, $O_i:=\mathrm{OddSum}(D\cup
\Gamma_{i-1})$, $E_i:=\mathrm{EvenSum}(D\cup\Gamma_{i-1})$ (so $\Gamma_{k-1}=
\{2^0,\ldots,2^{k-1}\}$).

**Statement.** Writing $e:=m-k$:
- if $e$ is even, $e=2t\ (t\ge1)$: $O_m=O_k+\dfrac{2^{m+1}-2^{k+1}}3$.
- if $e$ is odd, $e=2t+1\ (t\ge0)$: $O_m=2^k+E_k+\dfrac{2^{m+1}-2^{k+2}}3$
  (empty sum when $t=0$, i.e. $e=1$ reduces to $O_m=O_{k+1}=2^k+E_k$).

This supersedes, and corrects, the false one-step telescoping identity
attempted in round 16 (that identity implicitly assumed an $\mathrm{Odd}\to
\mathrm{Odd}$ recursion at each $q=0$ step; the true recursion couples
$\mathrm{OddSum}$ and $\mathrm{EvenSum}$, giving a ratio-$4$, not ratio-$2$,
geometric series with $\lceil e/2\rceil$ effective terms).

**Proof.** From the already-certified $q=0$ clause of the Unified
Threshold-Pair-Peeling Lemma (`lemmas/monotonicity-reduction-and-unified-
threshold-pair-peeling.md`, quoted there for $M=D\cup\Gamma_{k-1}$, $q=0$):
$O_j=2^{j-1}+E_{j-1}$ whenever $\max(D)\le2^{j-1}$. Combined with the
Even-target Companion Peeling identity above (applied with $S=D\cup
\Gamma_{j-1}$, unique max $2^{j-1}$ under the same hypothesis): $E_j=O_{j-1}$.
Composing these two facts at every level $j=k+1,\ldots,m$ (all satisfying
$\max(D)\le2^k\le2^{j-1}$) gives the two-term recursion $O_j=2^{j-1}+O_{j-2}$
for $j\ge k+2$, with boundary step $O_{k+1}=2^k+E_k$; unrolling this recursion
in both parities of $e$ gives the stated closed forms. $\blacksquare$

**Reviewer independent re-verification.** Own fresh scripts
(`verify.py`, `verify_chain.py`): Fact (a) ($O_j=2^{j-1}+E_{j-1}$, $20{,}000$
trials plus $5{,}000$ explicit-tie trials, zero violations), Fact (b)
($E_j=O_{j-1}$, $20{,}000$ trials plus $5{,}000$ tie trials, zero violations),
and the composed closed form directly against raw $\mathrm{OddSum}$
computation on the full multiset $D\cup\Gamma_{m-1}$ ($20{,}000$ random
trials, $k=1,\ldots,6$, $e=1,\ldots,8$, zero mismatches in either parity).
