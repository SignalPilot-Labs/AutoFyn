## Theorem (Transient-free finishing, CONDITIONAL on the Unified Central Claim)

**This lemma is conditional.** It does not by itself advance the central
gap; it shows what follows immediately once the central gap is closed.

### Statement
Suppose there is a finite set of primes $Q\supseteq R(a_1)$ such that
$\mathrm{Good}_Q(a_n)$ holds for every $n\ge1$ (the "Unified Central
Claim" for $Q$ — see `reduction-lemma-ss1-vs-unified-claim.md`). Let
$L:=\prod_{q\in Q}q$, $T:=|\mathrm{GoodRes}(Q)|\ge1$. Then
$$a_{n+T}=a_n+L\qquad\text{for every }n\ge1$$
— exact periodicity from the very first term, with **no transient**.

### Proof sketch (full proof in `approaches/state-compactness-pigeonhole.md` §9.4)
By the Reduction Lemma, the hypothesis gives Hypothesis SS$(Q,1)$.
Step 1: $A=\{m\ge a_1:\mathrm{Good}_Q(m)\}$ (both inclusions proved
directly from Hypothesis SS$(Q,1)$ and maximality of indices with
$a_n<m$). Step 2: by CRT, $\mathrm{Good}_Q$ depends only on $m\bmod L$, so
$A$ is exactly the set $C$ of the certified
`periodicity-of-residue-class-union.md` (Lemma P) with $c=a_1-1$. Step 3:
Lemma P gives $c_{j+T}=c_j+L$ for *every* $j\ge1$; since $c_j=a_j$
(as $A$ listed increasingly is $(a_n)_{n\ge1}$ by definition), this is
exactly $a_{n+T}=a_n+L$ for every $n\ge1$.

### Provenance
`approaches/state-compactness-pigeonhole.md`, round 3, §9.4. Verified by
the proof-reviewer round 3: correctly composes the certified
`reduction-lemma-ss1-vs-unified-claim.md` with the certified
`periodicity-of-residue-class-union.md`; no gap found.

### Status
Conditional on the Unified Central Claim (existence of a finite $Q$ with
$\mathrm{Good}_Q(a_n)$ true for all $n\ge1$) — **not proved** by any
approach in the population as of round 3. Once that claim is discharged
for some $Q$, this theorem completes the proof of the problem in one step
(no separate "prefix-extension" argument needed).
