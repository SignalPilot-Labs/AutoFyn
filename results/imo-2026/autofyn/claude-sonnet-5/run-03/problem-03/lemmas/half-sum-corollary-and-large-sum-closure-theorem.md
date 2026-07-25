# Half-Sum Corollary and Large-Sum Closure Theorem

Certified round 16 (proof-reviewer), from `approaches/self-similar-induction-on-n.md`
(round 16, "Round 16: Step 3 corrected ..." section, Steps 1–2 only — see
the **rejection notice** below for what is *not* certified from that
section).

**IMPORTANT — scope correction.** The same round-16 section's Step 0 and
Step 3 (its "Sub-case (i) Full Closure for $e\ge1$" theorem, and the
underlying claim that a $q=0$-chain of length $e$ gives
$\mathrm{OddSum}(D\cup\Gamma_{j-1})=2^{j-1}+\mathrm{OddSum}(D\cup\Gamma_{j-2})$
at every step) is **false** and is **explicitly rejected**, not certified —
see `approaches/self-similar-induction-on-n.md`'s round-16 section for the
still-standing (uncorrected) text, and the proof-reviewer round-16 report
for the exact counterexample. Only the two elementary, independently
re-verified facts below are certified.

## Half-Sum Corollary

**Statement.** For any finite multiset $N$ of positive reals (no cap on
count or values), $\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$.

**Proof.** By the certified Lemma AS
(`lemmas/altsum-reformulation-and-single-insertion.md`),
$\mathrm{OddSum}(N)=(\mathrm{sum}(N)+\mathrm{AltSum}(N))/2$. By the
certified AltSum Corollary (`lemmas/altsum-corollary-and-growth-lemma.md`),
$\mathrm{AltSum}(N)\ge0$ unconditionally. Substituting gives
$\mathrm{OddSum}(N)\ge\mathrm{sum}(N)/2$. $\blacksquare$

Elementary and immediate from two already-certified facts; not previously
recorded as a standalone reusable tool. (Reviewer note: this is the same
content as `reciprocal-potential-induction-on-n.md`'s independently-stated
"Universal Floor Lemma," proved the same way from the pair-consecutive-terms
argument directly — the two proofs are different derivations of the same
elementary fact, cross-validating it. No separate certification needed for
that file's restatement.)

## Large-Sum Closure Theorem

**Statement.** For every $k\ge1$, every $m\ge k+1$ (excess $e:=m-k\ge1$),
every $a_1\in(2^{k-1},2^k]$, and every finite multiset $R$ of positive
reals with $\mathrm{sum}(R)=2^m-a_1$ (arbitrary count, arbitrary individual
values — **no cap on $\max(R)$ needed**):
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ \ge\ 2^k-a_1.$$

**Proof.** By the Half-Sum Corollary applied to $N:=R\cup\Gamma_{k-2}$,
using $\mathrm{sum}(\Gamma_{k-2})=2^{k-1}-1$:
$$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge\frac{(2^m-a_1)+2^{k-1}-1}2.$$
It suffices that $2^m+a_1\ge\tfrac32\cdot2^k+1$. Since $m\ge k+1$,
$2^m\ge2^{k+1}$; since $a_1>2^{k-1}$, $2^m+a_1>2^{k+1}+2^{k-1}=\tfrac52\cdot
2^k\ge\tfrac32\cdot2^k+1$ (the last step is $2^k\ge1$, true for $k\ge0$).
$\blacksquare$

**Reviewer independent verification** (own from-scratch exact-`Fraction`
script, not the builder's): 20,000 random trials, $k=1,\ldots,10$,
$e=1,\ldots,10$, $a_1$ random in $(2^{k-1},2^k]$, $R$ of random count
$0$–$8$ with arbitrary values (no cap) summing to $2^m-a_1$ — zero
violations. This matches the builder's own independent stress test
(30,000+28,851+20,000 trials, zero violations).

## Scope note — what this does NOT establish

This lemma is a correct, general, standalone fact about $R\cup\Gamma_{k-2}$
given the exact hypothesis $\mathrm{sum}(R)=2^m-a_1$. It does **not** by
itself establish anything about $D\cup\Gamma_{m-1}$ for a $q=0$-chain
starting from level $m$: the round-16 file's attempt to connect the two via
repeated application of the $q=0$ case of the Unified Threshold-Pair-Peeling
Lemma is **algebraically wrong** — that certified lemma's own $q=0$ clause
states $\mathrm{OddSum}(M)=2^{k-1}+\mathrm{EvenSum}(D\cup\Gamma_{k-2})$ (an
$\mathrm{Odd}\to\mathrm{Even}$ conversion, not $\mathrm{Odd}\to\mathrm{Odd}$
as the round-16 file's Step 0 restates it), so naively iterating "add
$2^{j-1}$, drop the Γ-index by 1, keep calling it OddSum" is false in
general (reviewer's own exact-`Fraction` script: 1998/2000 mismatches at a
single step; a concrete integer counterexample at $D=\varnothing$, $m=7$,
$k=4$: true $\mathrm{OddSum}(\Gamma_6)=85\ne122=(2^7-2^4)+\mathrm{OddSum}
(\Gamma_3)$). Consequently the round-16 "Sub-case (i) Full Closure for
$e\ge1$" theorem, which is built on this broken chain, is **false as
stated** — a direct counterexample was found (see the proof-reviewer
round-16 report): $k=1,e=1,m=2$, $a_1=99/50\in(1,2]$,
$R=\{19/50,9/25,17/25,3/5\}$ (each $\le2^{k-1}=1$),
$\mathrm{sum}(D)=4=2^m$, yet $\mathrm{OddSum}(D\cup\Gamma_{m-1})=99/25=3.96<
4$. **GT($m$)'s sub-case (i) is NOT closed for $e\ge1$**; it remains open,
exactly as before round 16 (round 15's own, narrower, correctly-proved
Sub-case (i) Window Reduction Theorem, requiring $a_1\ge2^{k-1}+1$, still
stands and is unaffected).

## Reusable by

Any approach needing a cap-free lower bound on $\mathrm{OddSum}$ of an
arbitrary-valued multiset from its sum alone (Half-Sum Corollary), or the
specific arithmetic threshold computation for $R\cup\Gamma_{k-2}$ under a
"large, $2^m$-scale" sum hypothesis (Large-Sum Closure Theorem) — but any
future use combining this with a $q=0$-chain must first correctly re-derive
the Odd/Even alternation (see Scope note above), not reuse the round-16
file's Step 0 as written.
