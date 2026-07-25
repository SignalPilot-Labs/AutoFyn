# Certified (round 4): Odd-Even Domination, EvenSum floor, and the Large-Violation-Depth Theorem

Certified from `approaches/greedy-reduction-geometric.md` (round 4, Section
8). Proof-reviewer independently reproduced the exact closed-form
computation at $m=8$ (equal 9-way split, `OddSum = 2653/9 > 256`, exact
rational arithmetic) and stress-tested the theorem's hypothesis region with
an independent random-instance generator (no violations found across
$m=8,\dots,12$, tens of thousands of trials).

**Lemma 7 (Odd-Even Domination).** For any finite multiset $N$ of positive
reals, $\mathrm{OddSum}(N)\ge\mathrm{EvenSum}(N)$. (Elementary pairing
argument on consecutive sorted terms.)

**Lemma 7′ (EvenSum floor).** For any nonempty finite multiset $X$ with
$g=\max(X)$, $T'=\mathrm{sum}(X)$: $\mathrm{EvenSum}(X)\ge(T'-g)/2$.

**Theorem (Large-Violation-Depth closure).** Let $m\ge3$, $A=\{a_1\ge\cdots
\ge a_j>0\}$ a partition of $2^m$ into $j\le m+1$ parts, and
$\Gamma_{m-1}=\{2^{m-1},\dots,2^0\}$ (LB's untouched tail, TOP-ONLY
scenario). If $a_1<2^{m-3}$ (violation depth $d\ge3$) then
$\mathrm{OddSum}(A\cup\Gamma_{m-1})>2^m$ strictly.

**Scope, proved honestly (do not overclaim beyond this):**
- Vacuous for $3\le m\le7$ (pigeonhole on $\le m+1$ fragments forces
  $a_1\ge2^m/(m+1)\ge2^{m-3}$ in that range); first non-vacuous at $m=8$.
- Does **not** extend to violation depth $d=1$ (the identical technique
  provably fails there, by a margin growing like $-\Theta(2^{m-1})$ — proved,
  not merely "not yet closed").
- Structurally **inapplicable** at any even depth $d$ (would require
  OddSum-superadditivity, which is false in general — explicit
  counterexample $P=\{3\},Q=\{2,1\}$ given in the source file).
- Combined with the certified Dominant-Chain Theorem (depth $d=0$), the only
  remaining open region of TOP-ONLY is $2^{m-3}\le a_1<2^{m-1}$
  (violation depths $d\in\{1,2\}$). TOP-ONLY itself, and the fully general
  Case 2, remain open.

**Reusable by:** any approach working the complementary (non-Dominant-Chain)
regime of the lower-bound direction; the Odd-Even Domination and EvenSum
floor lemmas are also general-purpose, independent of the geometric
structure.
