## Status
unsolved

## Approaches tried
(none yet — first outline, round 1)

## Current best

### Framing: decouple into 2026-slot per-prime "games," reconstruct via CRT-style product
Rather than working with the numbers directly, represent the board state at any time as
a function `p \mapsto (e_p(1),\dots,e_p(2026))` from primes to length-2026 exponent
vectors, where `e_p(i) = v_p(\text{entry } i)`. Since a number is determined by its full
exponent vector across primes (`x = \prod_p p^{v_p(x)}`), the whole board state is
**exactly equivalent** to this collection of vectors — one independent "lane" per prime
— and a single Confucius move on positions `(i,j)` acts on ALL lanes at once, in each
lane replacing the pair `(e_p(i),e_p(j))` by `(\min,\, |{\rm diff}|)`, but leaving all
other lanes' *other* coordinates untouched and leaving every lane's move **synchronized**
to the same pair of positions `(i,j)$.

This bijective reformulation is used to organize the proof around two clean, logically
separate lemmas, then a reconstruction step:

**Lemma A (single-lane invariant, prime-independent).** Fix one prime `p` and look ONLY
at its lane `(e_p(1),\dots,e_p(2026)) \in \mathbb{Z}_{\ge0}^{2026}`. Under the repeated
rule "pick two coordinates `i,j`, replace `(e_p(i),e_p(j))` by
`(\min(e_p(i),e_p(j)), |e_p(i)-e_p(j)|)`" (a rule that is *well-defined and meaningful
on this lane alone*, independent of what happens in any other prime's lane, since the
rule only ever reads `e_p(i), e_p(j)$), the quantity
`G_p := \gcd(e_p(1),\dots,e_p(2026))` (convention `\gcd(0,\dots,0)=0$) is an exact
invariant of the lane, for ANY sequence of coordinate-pairs chosen (not just the ones
Confucius actually picks) — by the identity `\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ plus
multiset-gcd associativity. This is a purely single-lane statement, provable without
reference to the other primes or to the actual board numbers at all.

**Lemma B (part a, cross-lane termination).** The *actual* board process synchronizes
all lanes' moves to the same coordinate pair `(i,j)` each step (this is where the primes
"couple"), chosen by Confucius subject to the legality rule "both entries `i,j` are `>1$
as ACTUAL numbers," i.e. NOT lane-independent — legality depends on the OR/AND across
lanes (entry `i$ is `>1$ iff SOME lane has `e_p(i)>0$). Termination is proved exactly as
in the sibling `lex-potential-gcd-invariant` approach via the lexicographic potential
`(N, \Sigma)$ with `N$= count of positions with some lane nonzero (`=` count of actual
board entries `>1$) and `\Sigma = \sum_p \sum_i e_p(i)^2$ — same proof, just phrased in
lane language: `\Sigma$ strictly drops in the touched lane whenever some prime divides
both `m,n$ (i.e. the touched pair shares a lane where both coordinates are positive),
`N$ drops by exactly 1 exactly when no lane has both coordinates positive, i.e. the two
actual numbers are coprime.

**Reconstruction (part b).** At termination (`N=1$ by Lemma B, exactly one position `M$
survives), EVERY lane's exponent vector is now `(0,\dots,0,v_p(M),0,\dots,0)$ (nonzero
only possibly at position `M`), so by Lemma A applied independently to each lane,
`G_p = v_p(M)$ for every prime `p`, where `G_p$ was fixed from the START (Lemma A says
it's invariant under the WHOLE history of moves applied to that lane, and every move
Confucius makes IS a valid lane-move for every prime simultaneously). Hence
`M = \prod_p p^{G_p}$, independent of Confucius's choices — this is forced purely by
recombining the (per-prime-independent) Lemma A conclusions via the prime factorization
bijection `x \leftrightarrow (v_p(x))_p$ (the "CRT-style" reconstruction — really just
unique factorization, not literally CRT, but organizationally analogous: solve each
prime's sub-problem independently, then reassemble via unique factorization).

### Why this framing is a genuinely different organization (not just a relabeling)
The primary approach proves the invariant `G_p$ "in-line" while tracking the whole board.
Here, Lemma A is stated and proved as a **fully self-contained single-sequence fact**
about `\mathbb{Z}_{\ge0}^{2026}$ under an abstract coordinate-pair rule, with NO reference
to Confucius, other primes, or actual numbers — making it reusable/citable and easier to
audit in isolation (a reviewer can check Lemma A is correct without thinking about the
whole board at all), and it cleanly isolates exactly where cross-prime coupling enters
the proof (only in Lemma B, the legality condition and the termination count `N`).

## Key lemmas
- Lemma A: single-lane gcd invariant `G_p = \gcd(e_p(1),\dots,e_p(2026))$, proved via
  (I2) `\gcd(\min(a,b),|a-b|)=\gcd(a,b)$ + multiset-gcd associativity — identical
  underlying identity to the other approaches, but stated/proved as an abstract fact
  about `\mathbb{Z}_{\ge0}^{2026}$-sequences, decoupled from the board.
- Lemma B: `(N,\Sigma)$ lexicographic termination, same mechanism as the primary
  approach's part (a) (imported/re-derived).
- Unique factorization `x = \prod_p p^{v_p(x)}$ as the reconstruction bridge.

## Open gaps
- Lemma A as stated needs the caveat spelled out: it holds "for any sequence of moves
  applied to the lane," but the actual constraint is that Confucius's moves are
  synchronized across lanes and gated by a legality condition depending on the actual
  numbers, not on any single lane. The builder must make explicit that Lemma A's
  invariance holds regardless of which coordinate pairs are chosen and in which order
  (this is true and easy — `G_p$ invariance never used the legality/coupling condition
  at all) — but must NOT accidentally suggest Lemma A alone determines termination or
  legality (it doesn't; that's Lemma B's job).
- The "CRT-style" language should be softened/clarified in the write-up: this is really
  just unique factorization (fundamental theorem of arithmetic), not the Chinese
  Remainder Theorem; avoid overclaiming a CRT citation that isn't accurate.
- Same underlying case analysis as the primary approach for Lemma B; no new gap there,
  but must be written out fully by the builder (not just "same as sibling approach" —
  self-contained rigor required per CLAUDE.md).

## Cases to cover
- Same as primary approach's cases (gcd(m,n)=1 vs >1) for Lemma B.
- Additionally: primes `p` dividing none of the `a_i` (handled automatically,
  `G_p=0`, contributes `p^0=1` to the product, i.e. doesn't appear in `M`).

## Watch out for
- Don't let "CRT-style reconstruction" become a hand-wave — the actual mechanism is
  unique factorization; each prime's lane result `v_p(M)=G_p` must be established
  individually and then the numbers multiplied out, this is elementary but must be
  stated precisely (not "by CRT" citation without justification).
- This approach's real value is expository/organizational (isolating the per-prime
  argument as a standalone lemma); if the reviewer finds it doesn't add rigor beyond
  the primary approach, it's a legitimate candidate to fold into / drop in favor of
  the primary approach rather than force independent development.
