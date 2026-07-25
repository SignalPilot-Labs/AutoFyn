## Theorem (Even-Seed Universal Lock)

If $a_1$ is even, then for every $n\ge1$: $a_n$ is even and
$a_{n+1}=a_n+2$. Consequently $a_n=a_1+2(n-1)$ for every $n\ge1$, so the
**full IMO conclusion holds** for this entire sub-family with $T=1$, $L=2$,
exactly from $n=1$, with no transient.

### Proof
Induction on $n\ge1$, proving simultaneously "$a_n$ is even" and
"$a_{n+1}=a_n+2$" (using `lemmas/minimum-gap-lemma.md`).

*Base case $n=1$:* $a_1$ even by hypothesis. $a_1+2$ is a valid candidate
for $a_2$ (only constraint is $i=1$: $\gcd(a_1+2,a_1)=\gcd(2,a_1)=2>1$).
By the Minimum Gap Lemma, $a_2\ge a_1+2$, and the only integer strictly
between $a_1$ and $a_1+2$ ($=a_1+1$) is excluded by that same lemma, so
$a_2=a_1+2$ exactly (valid and minimal). $a_2$ is then even.

*Inductive step:* Assume $a_1,\dots,a_n$ all even. Then $a_n+2$ is a valid
candidate for $a_{n+1}$: for every $i\le n$, $a_i$ and $a_n+2$ are both
even, so $\gcd(a_n+2,a_i)\ge2>1$. The only smaller candidate, $a_n+1$, is
excluded by the Minimum Gap Lemma (applied at index $n$, needing no
inductive hypothesis). Hence $a_{n+1}=a_n+2$ exactly, and this is even.

Telescoping gives $a_n=a_1+2(n-1)$ for every $n\ge1$; taking $T=1,L=2$,
$a_{n+1}=a_n+2$ for every $n\ge1$ is exactly the problem's conclusion, with
equality for every $n\ge1$, no transient. $\blacksquare$

### Verification
Direct simulation confirms $a_n=a_1+2(n-1)$ exactly for every tested even
$a_1$ (proof-reviewer independently re-ran the greedy simulation for
$a_1\in\{2,4,6,10,12,30,210,194,10^8\}$, 20 terms each: exact match in every
case, zero deviations).

### Scope
Completely and rigorously resolves the full IMO claim for the infinite
sub-family $\{a_1 : 2\mid a_1\}$. Does **not** extend to odd $a_1$: the
proof's only use of $p=2$ is that there is exactly one "in-between"
candidate ($a_n+1$) to exclude for a gap of $2$; for an odd prime $p:=\min
R(a_1)$, there would be $p-1\ge2$ in-between candidates
($a_n+1,\dots,a_n+p-1$), of which the free Minimum Gap Lemma only excludes
one ($a_n+1$), leaving $p-2\ge1$ candidates unaccounted for — and the
"lock" analogue is known to break for odd $p$ in concrete instances (e.g.
$a_1=35$, $p=5$: the lock breaks at $a_3$; `third-term-dichotomy-lemma.md`).

### Provenance
Proved in `approaches/renormalization-induction-on-seed.md`, §7.2–7.3, round
5. Independently re-derived and re-simulated by the proof-reviewer; no gap
found.
