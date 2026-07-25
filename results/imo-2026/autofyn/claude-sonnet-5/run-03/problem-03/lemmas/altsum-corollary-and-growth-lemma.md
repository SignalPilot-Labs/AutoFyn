# AltSum Corollary and Growth Lemma

Certified round 14 (proof-reviewer), from `self-similar-induction-on-n.md`.

## AltSum Corollary

**Statement.** For any finite multiset $N$ of positive reals,
$0\le\mathrm{AltSum}(N)\le\max(N)$ (with $\mathrm{AltSum}(\varnothing):=0$,
$\max(\varnothing):=0$).

**Proof.** Induction on $|N|$, via the Peeling identity
$\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}(N\setminus\{\max N\})$ (removing
the maximum flips every remaining element's rank parity). If
$0\le\mathrm{AltSum}(N')\le\max(N')\le\max(N)$ for $N':=N\setminus\{\max N\}$
(inductive hypothesis), then
$\mathrm{AltSum}(N)=\max(N)-\mathrm{AltSum}(N')\in[\max(N)-\max(N),\,
\max(N)-0]=[0,\max(N)]$. Base case $N=\varnothing$ trivial. $\blacksquare$

**Reviewer independent verification.** Own exact-`Fraction` script, 20000
random multisets (size $0$–$10$, random positive rationals): zero
violations.

## Growth Lemma

**Statement.** Fix $m\ge1$, $2\le k\le m+1$. Let $D$ be a multiset of $k$
positive reals, each in $(0,2^{m-1}]$, with $\mathrm{sum}(D)\le2^m$. Then
there is $D''$ with the same count and cap, $\mathrm{sum}(D'')=2^m$ exactly,
obtained from $D$ by weakly increasing each sorted coordinate. Consequently
(by the certified Elementwise Monotonicity Lemma, applied one coordinate at
a time in the increasing direction), for any fixed finite multiset $T$:
$\mathrm{OddSum}(D\cup T)\le\mathrm{OddSum}(D''\cup T)$.

**Proof.** The maximum reachable sum with $k\ge2$ coordinates capped at
$2^{m-1}$ is $k\cdot2^{m-1}\ge2\cdot2^{m-1}=2^m\ge\mathrm{sum}(D)$, so $2^m$
lies in $[\mathrm{sum}(D),k\cdot2^{m-1}]$. Saturate coordinates one at a
time (raise the current one toward $2^{m-1}$, move to the next once
saturated); the running total rises continuously from $\mathrm{sum}(D)$ to
$k\cdot2^{m-1}\ge2^m$, so by the intermediate value theorem it passes
through $2^m$ exactly; stop there. Every coordinate only increases and none
exceeds $2^{m-1}$. $\blacksquare$ The monotonicity conclusion is the
already-certified Elementwise Monotonicity Lemma
(`lemmas/window-reduction-theorem-and-elementwise-monotonicity.md`), applied
symmetrically (increasing direction) to how the certified Monotonicity
Reduction Lemma applies it (decreasing direction).

**Reviewer independent verification.** Confirmed the elementary feasibility
argument by direct construction (own script) for $m=1,\dots,6$, $k=2,\dots,
m+1$, 500 random trials each: constructed $D''$ always has
$\mathrm{sum}(D'')=2^m$ exactly, every coordinate $\le2^{m-1}$, obtained by
coordinatewise weak increase from $D$. The monotonicity direction itself
reuses the already-certified Elementwise Monotonicity Lemma (not re-verified
here; re-verification of that lemma was done when it was originally
certified).

## Scope note

These two lemmas are elementary and general-purpose (not specific to any
open sub-case). They are used in `self-similar-induction-on-n.md`'s round-14
"Small-Sum Reduction Theorem," which is **not** certified here: that theorem
is explicitly flagged by its own builder as incomplete ("modulo one flagged
tie detail" — the case where the Growth Lemma's saturating construction
produces a coordinate exactly at the cap $2^{m-1}$, which needs a
not-yet-completed continuity/limiting reduction via the certified
Tie-Neutrality Lemma). Only the two lemmas above (AltSum Corollary, Growth
Lemma), which are unconditionally proved with no open gap, are certified.
