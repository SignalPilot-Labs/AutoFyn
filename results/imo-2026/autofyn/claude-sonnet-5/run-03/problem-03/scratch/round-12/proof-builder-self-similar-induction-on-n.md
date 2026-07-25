# Round 12 summary — self-similar-induction-on-n

## What was targeted
Round 12's primary target: the shared Branch-I.A window, specifically gap
(a) of the window (the endpoint-reduction identity's target
$\mathrm{OddSum}(D\cup\Gamma_{\ell-2})\ge2^{\ell-1}$), via strong induction
on $\ell$ mirroring round 8's Branch-II mechanism. Secondary target:
import the Rank-Pinning technique into the Middle-Regime Vertex Reduction
Theorem's $m=3,4,5$ closures.

## What was achieved (primary target)
A new **General Theorem $\mathrm{GT}(m)$**: for any multiset $D$ with
$|D|\le m+1$, $\max(D)\le2^m$, $\mathrm{OddSum}(D\cup\Gamma_{m-1})\ge
\min(\mathrm{sum}(D),2^m)$ — proved **in full, for every admissible $D$**
(not a numerically-found vertex) for $m=0,1,2,3$, via a case split
($p=\#\{a_i>2^{m-1}\}\in\{0,1,2\}$, with the $p=0$ residual further split
by $r=\#\{a_i>2^{m-2}\}\in\{0,1,2\}$) that reduces each case to a lower
$\mathrm{GT}(m')$ or closes it unconditionally. Every non-base peeling
identity used was independently stress-tested with 3000 exact-`Fraction`
random trials each (zero mismatches); the final theorem itself was
additionally cross-checked against 4000+ structured (weighted-random and
tied-pair grid, per the round's warning against naive gradient search)
instances for $m$ up to 7, zero violations found.

**Corollary:** gap (a) of the Branch-I.A window (the window's top
endpoint, all admissible $D$, not one witness) is now proved for
$\ell=1,2,3,4$. Combined with the already-certified Theorem W (left
endpoint) and Lemma TPI (gap (b)(i)), **the window is now fully closed at
$\ell=1,2,3,4$**. General $\ell\ge5$ remains open: the case split's
residual sub-case ($r=0$, i.e. $\max(D)\le2^{m-2}$ with the full $m+1$
piece budget) becomes feasible only from $m=4$ onward (proved exactly, a
clean feasibility threshold), and closing it needs one more level of the
same self-similar recursion — identified precisely, not completed. This
was a **self-caught false start** corrected before use: an initial attempt
to cite the certified Dominant-Chain Theorem directly does not apply
(its Dominance-Chain hypothesis is much stronger than $\max(D)\le2^m$),
and an intermediate derivation slip (conflating $\mathrm{OddSum}$ vs.
$\mathrm{EvenSum}$ after a Global-max peel) was caught by a numerical
cross-check before being written up as a claim.

## What was not attempted
Target 2 (Rank-Pinning import into the Middle-Regime Vertex Reduction
Theorem's $m=3,4,5$ closures) was not attempted this round — all time
went to Target 1, which yielded a stronger kind of result (general, not
vertex-numerical). No changes were made to the Middle-Regime section.
Route (b) (exchange-smoothing toward tied-pair canonical families,
crux-adapted) was also not attempted, superseded by the more immediately
tractable GT($m$) route.

## Files changed
- `results/imo-2026-03/approaches/self-similar-induction-on-n.md` — new
  "Round 12" section appended (General Theorem GT(m), Lemmas P2/P1/R2/R1,
  Feasibility Lemma, induction closing $m=0,1,2,3$, corollary on the
  window, honest scope for $m\ge4$).
- Status remains `partial` (accurate: real, verified, general-purpose
  progress; the window and the overall problem are not fully solved).

## Suggested next steps
1. Close the $m\ge4$ residual ($r=0$/$s$-recursion) to extend the window's
   top-endpoint closure to all $\ell$ — likely needs one clean uniform
   induction (not a growing tower of ad hoc splits); the self-similar
   structure is now explicit.
2. Target 2 (Rank-Pinning import) is still open and should be picked up
   next round if not done by a parallel builder.
3. Gap (b)(ii) (piece-cap-saturated monotonicity) remains completely
   untouched.
