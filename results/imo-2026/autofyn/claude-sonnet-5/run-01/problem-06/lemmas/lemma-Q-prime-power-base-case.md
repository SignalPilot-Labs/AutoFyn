# Lemma Q (prime-power base case)

**Statement.** With `(a_n)` as in the problem, if `a_1=p^e` for a single prime `p`
and integer `e\ge1` (in particular whenever `a_1` is even, taking `p=2`), then
`a_n=a_1+p(n-1)` for every `n\ge1`. Consequently `T=1,\ L=p` satisfy
`a_{n+1}=a_n+L` for every `n\ge1`, proving the problem's conclusion exactly for
this family, from `n=1`.

**Proof.** Induction on `n`. The claim holds trivially for `n=1`. Suppose
`a_1,\dots,a_n` are all multiples of `p` (true for `n=1`; this is the inductive
hypothesis for general `n`, and note `\mathrm{rad}(a_1)=\{p\}`, so by Lemma P
`\gcd(x,a_1)>1 \iff p\mid x` for any candidate `x`).

*No candidate strictly between `a_n` and `a_n+p` is admissible.* For `1\le j\le p-1`,
`a_n+j` is not a multiple of `p` (since `a_n` is a multiple of `p` and `p` is prime,
no integer strictly between two consecutive multiples of `p` is itself a multiple of
`p`). Hence `\gcd(a_n+j,a_1)=\gcd(a_n+j,p^e)=1`, so `a_n+j` fails the required
condition against `i=1` and is inadmissible.

*`a_n+p` is admissible.* It is a multiple of `p`, and by the inductive hypothesis
every `a_i` (`i\le n`) is also a multiple of `p`, so `\gcd(a_n+p,a_i)\ge p>1` for
every `i\le n`.

Since every integer strictly between `a_n` and `a_n+p` is inadmissible and `a_n+p`
is admissible, `a_{n+1}=a_n+p` exactly, and `a_n+p` is again a multiple of `p`,
closing the induction. $\blacksquare$

**Source.** Proved identically (word-for-word the same argument) in all three round-1
approach files: `backbone-existence-crt.md` (Section 2), `intersecting-family-covering-construction.md`
("Lemma Q"), and `bounded-gap-density-covering.md` ("Free Lemma Q").

**Certification.** No hypotheses beyond the problem's own definition and elementary
number theory (consecutive multiples of a prime); no gaps. Certified `solved`-quality
(sorry-free) by the round-1 proof-reviewer. Disposes of the entire `|\mathrm{rad}(a_1)|=1`
family, including every even `a_1`, completely and exactly from `n=1`. (Superseded, for
this specific family, by the strictly more general Lemma S′ below — but Lemma Q's proof
is simpler and self-contained, so it is kept as the base case.)
