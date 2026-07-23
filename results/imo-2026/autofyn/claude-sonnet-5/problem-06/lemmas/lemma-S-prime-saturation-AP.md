# Lemma S′ (single-prime saturation implies exact arithmetic progression)

**Statement.** With `(a_n)` as in the problem, suppose there is a prime `p` such
that `p\mid a_n` for *every* `n\ge1` (i.e. `p` "saturates" the whole sequence, not
merely infinitely many terms). Then `a_n=a_1+p(n-1)` for every `n\ge1`.

**Proof (reviewer-corrected — see note below).** Strong induction on `n`, using the
global saturation hypothesis as a known fact about the (unique, fully determined)
sequence `(a_n)`. Base case `n=1` is trivial. Suppose `a_j=a_1+p(j-1)` for
`j=1,\dots,n` (so in particular `p\mid a_j` for every `j\le n`); we show
`a_{n+1}=a_n+p`.

*`a_n+p` is admissible.* For every `j\le n`, `p\mid a_j` (inductive hypothesis) and
`p\mid(a_n+p)`, so `\gcd(a_n+p,a_j)\ge p>1`. Since `a_{n+1}` is by definition the
smallest integer `>a_n` satisfying this admissibility condition against every
`j\le n`, and `a_n+p` is one such admissible integer, we get `a_{n+1}\le a_n+p`.

*`a_{n+1}=a_n+p` exactly.* Suppose for contradiction `a_{n+1}<a_n+p`, i.e.
`a_n<a_{n+1}<a_n+p`. Since `a_n` is a multiple of `p` (inductive hypothesis) and
`p` is prime, no integer strictly between `a_n` and the next multiple `a_n+p` is
itself a multiple of `p`; hence `p\nmid a_{n+1}`. But the global saturation
hypothesis, applied at index `n+1`, says `p\mid a_{n+1}` — a contradiction. Hence
`a_{n+1}=a_n+p`, completing the induction. $\blacksquare$

**Source and correction.** The statement and the "admissibility of `a_n+p`" half of
the proof are exactly as given in `approaches/intersecting-family-covering-construction.md`
("Lemma S′"). **The round-1 proof-reviewer found and fixed a gap in the original
write-up's second half**: the original text argued "if `x` (with `a_n<x<a_n+p`)
were admissible it would have to equal `a_{n+1}` by minimality of the true `a_{n+1}`"
— this is not correctly justified as stated, since minimality of `a_{n+1}` among
admissible candidates only gives `a_{n+1}\le x` when `x` is admissible, not
`x=a_{n+1}` (a smaller admissible candidate could a priori exist between `a_n` and
`x`). The corrected argument above avoids this by working directly with `a_{n+1}`
itself (never introducing an arbitrary intermediate `x`): it uses only `a_{n+1}\le a_n+p`
(from admissibility of `a_n+p` and minimality — a valid use of minimality, giving
`\le` not `=`) together with the parity-of-multiples-of-`p` argument already used
correctly elsewhere in the same file (Lemma Q's proof) to rule out
`a_n<a_{n+1}<a_n+p`. The conclusion (the lemma's statement) is unchanged and is
correct; only the proof's middle step needed repair, and the repair uses no
mathematical content beyond what was already elsewhere in the same approach file.

**Certification.** With the above correction, the proof is complete and gap-free,
using only the global saturation hypothesis, Lemma P (for admissibility bookkeeping,
implicitly), and elementary properties of multiples of a prime. Certified
`solved`-quality (sorry-free, statement unchanged from the original, exactly as
strong as originally claimed — a conditional lemma valid whenever a global
saturating prime exists) by the round-1 proof-reviewer.

**Use.** Strictly generalizes Lemma Q (which is the special case `a_1=p^e`, forcing
`p\mid a_1` trivially with no other prime factors): Lemma S′'s hypothesis can hold
even when `a_1` has other prime factors too (verified computationally for
`a_1\in\{21,33,39,55,57,69,85\}`, where `a_1` is not a prime power but a single
prime `p\in\{3,5\}` still divides every term). Together with the trivial dichotomy
"either some prime saturates every term, or no prime does," Lemma S′ gives a
complete, rigorous resolution of the entire "single global saturating prime" family
(Case I of `intersecting-family-covering-construction.md`'s Proposition D). It does
**not** address the case where no single prime saturates every term (Case II,
witnessed to be non-vacuous by `a_1=15`, where none of `2,3,5` divides every term),
which remains the open content of the whole problem.
