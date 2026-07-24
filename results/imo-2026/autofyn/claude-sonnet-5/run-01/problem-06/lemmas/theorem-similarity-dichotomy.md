# Claims 1–3 and the Main Dichotomy Theorem (Similarity Dichotomy)

**Source.** `approaches/similarity-dichotomy-crux-adaptation.md` (Round 15,
Sections 2–6). A from-scratch translation, into `imo-2026-06`'s own
term/non-term vocabulary, of IMO Shortlist 2013 N5's official Solution 1
(crux `aimo-0030`, "Ana and Banana" — cross-checked directly against the
problem's own solution text in `past_problems_database.json`). Every step
is reproved here directly from the problem's recursive definition (via the
already-certified Lemma REC, `lemmas/lemma-REC-recursive-IN-OUT-
characterization.md`), including two similarity-preservation steps
(Case (i)/(ii) inside the Dichotomy Theorem below) that the official
solution states without proof.

**Preliminaries used throughout.** `k:=a_1`. **Corollary P″** (already
certified, `lemmas/lemma-P-prime-pairwise-intersecting.md`, unordered
form): for every `i\ne j`, `\gcd(a_i,a_j)>1` — immediate from the problem's
recursive definition (for `i<j`, `a_j`'s defining property applied at
`l=i`). "Small primes" `:=\{p\le k \text{ prime}\}`, similarity of
`n,n'\ge k`: `\sigma(n)=\sigma(n')` where `\sigma(n)=\{p\le k\text{ prime}:
p\mid n\}`.

## Claim 1 (multiple of a term is a term)

**Statement.** If `n` is a term and `n'\ge n` is a multiple of `n`, then
`n'` is also a term.

**Proof.** Trivial if `n'=n`. If `n'>n`, suppose toward contradiction `n'`
is a non-term. By Lemma REC there is a term `m` with `k\le m<n'`,
`\gcd(m,n')=1`. Since `n\mid n'`, any common factor of `m,n` divides `n'`
too, so `\gcd(m,n')=1\Rightarrow\gcd(m,n)=1`. But `m,n` are both terms, so
`\gcd(m,n)>1` by Corollary P″ — contradiction. `∎`

## Claim 2 (companion move, small-prime case)

**Statement.** Let `r,s` be positive integers with `rs\ge k`. If `rs` is a
non-term, then `r^2s` is also a non-term.

**Proof.** By Lemma REC there is a term `x` with `k\le x<rs`,
`\gcd(x,rs)=1`. Since `r,s\mid rs`, `\gcd(x,r)=\gcd(x,s)=1`, so
`\gcd(x,r^2s)=1` (every prime factor of `r^2s` divides `r` or `s`). Since
`r\ge1`, `rs\le r^2s`, so `x<rs\le r^2s`. By Lemma REC (⇐), `r^2s` is a
non-term. `∎`

**Contrapositive form actually used** (Theorem below, Case (i)): if
`r^2s` is a term **and** `rs\ge k`, then `rs` is a term. (The `rs\ge k`
clause is needed for "`rs` is a term" to be a meaningful, in-domain
statement; in every application below it is verified directly — see the
Theorem's proof, where `rs=e_0=c_0t_0'\ge c_0\ge k` since `t_0'\ge1`.)

## Claim 3 (companion move, big-prime case)

**Statement.** Let `p` be a prime with `p>k`, and let `n\ge k` be a
non-term. Then `np` is also a non-term.

**Proof.** By well-ordering, take a minimal counterexample: `n` minimal
among non-terms `\ge k` for which some prime `p>k` gives `np` a term.

*Step 1.* By Lemma REC, `n>k` is a non-term ⟹ a term `m` exists,
`k\le m<n`, `\gcd(m,n)=1`.

*Step 2.* Since `np` is a term and `m$ is a term with `m<n<np`, Lemma REC
(⇐, applied contrapositively to the term `np`) forces `\gcd(m,np)>1`;
combined with `\gcd(m,n)=1`, this gives `p\mid m`.

*Step 3.* Write `m=p^ry` with `r\ge1`, `p\nmid y`.

*Step 4.* If `y=1`: `m=p^r\ge p>k`, and `\gcd(k,m)=1` (no prime factor of
`k` can be `p`, as they are all `\le k<p`); by Lemma REC (⇐) with witness
`k$, `m$ would be a non-term, contradicting Step 1. So `y\ge2`.

*Step 5.* Let `\alpha\ge1` be minimal with `y^\alpha\ge k`; then
`y^{\alpha-1}<k` (trivially so if `\alpha=1`, reading `y^0=1<k`).

*Step 6.* `y^\alpha=y^{\alpha-1}y<ky<py=p^ry/p^{r-1}=m/p^{r-1}<n/p^{r-1}`
(using `m<n`), so `p^{r-1}y^\alpha<n`. Hence for `i=0,\dots,r-1`:
`k\le y^\alpha\le p^iy^\alpha\le p^{r-1}y^\alpha<n`.

*Step 7.* `\gcd(y,n)=1$ (as `y\mid m$, `\gcd(m,n)=1`) and `\gcd(y,p)=1`, so
`\gcd(y^\alpha,np)=1`. Since `np` is a term, if `y^\alpha` were also a term,
Corollary P″ would force `\gcd(np,y^\alpha)>1` — contradiction. So `y^\alpha`
is a non-term.

*Step 8.* By induction on `i=0,\dots,r-1` (base case Step 7): if
`p^iy^\alpha` is a non-term, then since `p^iy^\alpha<n$ (Step 6) and `n` was
chosen minimal among counterexamples, the pair `(p^iy^\alpha,p)` cannot
itself be a counterexample, forcing `p^{i+1}y^\alpha` to be a non-term.
Taking `i=r-1`: `p^ry^\alpha` is a non-term.

*Step 9.* `m=p^ry` divides `p^ry^\alpha=m\cdot y^{\alpha-1}$ (a genuine
positive-integer multiple, `y^{\alpha-1}\ge1$ since `y\ge2,\alpha\ge1`). If
`m` were a term, Claim 1 would force `p^ry^\alpha` to be a term, contradicting
Step 8. So `m` is a non-term — contradicting Step 1 (`m` is a term). This
contradiction proves Claim 3. `∎`

**Contrapositive form used** (Theorem below, Case (ii)): if `n\ge k`, `p>k`
prime, and `np` is a term, then `n` is a term. (As with Claim 2, the
domain check `n\ge k` is verified directly at the point of use:
`n=e_0=c_0t_0'\ge c_0\ge k`.)

## Main Dichotomy Theorem

**Statement.** If `n,n'\ge k` are similar (`\sigma(n)=\sigma(n')`), then
`n,n'` have the same term-status.

**Proof.**

*Step A (reduction).* It suffices to prove: if `c\ge k`, `d=ct` for some
positive integer `t`, and `c,d` are similar, then `c,d` have the same
status ("the sub-claim"). Given similar `n,n'\ge k`, set `d:=nn'`; `d\ge k$
and `\sigma(d)=\sigma(n)=\sigma(n')$ (a prime `p\le k` divides a product iff
it divides a factor, and by similarity `p\mid n\iff p\mid n'`). Apply the
sub-claim to `(n,d)$ (`t=n'`) and to `(n',d)` (`t=n`): both give `d` the
same status as `n$ and as `n'` respectively, so `n,n'` share `d`'s status.

*Step B (minimal counterexample on the sub-claim).* Suppose the sub-claim
fails for some pair; any counterexample has `t\ge2` (else `c=d` trivially
matches). Choose a counterexample `(c_0,d_0)` with `d_0$ minimal. By
Claim 1, if `c_0` were a term then `d_0$ (a multiple) would be too, giving
matching status — not a counterexample; so `c_0` is a non-term, and (only
two statuses possible, and they differ) `d_0` is a term.

Since `t_0\ge2` has a prime factor `p`; write `t_0=pt_0'` (`t_0'\ge1$
integer), so `d_0=c_0t_0=(c_0t_0')p`; set `e_0:=d_0/p=c_0t_0'`. Then
`c_0\mid e_0`, and — since `t_0'\ge1` — **`e_0=c_0t_0'\ge c_0\ge k`**, so
`e_0` is a valid (in-domain) term/non-term object; also `e_0<d_0` (as
`p\ge2`).

**Case (i): `p\le k`.** Since `p\mid d_0` and `\sigma(c_0)=\sigma(d_0)`
with `p\le k`, `p\mid c_0` too, so `p^2\mid d_0` (write `c_0=pc_0'`,
`t_0=pt_0'`, giving `d_0=p^2c_0't_0'$). By Claim 2's contrapositive with
`r=p,s=c_0't_0'` (valid: `rs=e_0\ge k` shown above; `r^2s=d_0` is a term),
`e_0=rs` is a term.

Check `(c_0,e_0)` is a similar-multiple pair: `c_0\mid e_0` shown; for
similarity, `p\mid e_0=d_0/p` (as `p^2\mid d_0`) matches `p\mid c_0`; for
any other small prime `q\ne p`, dividing by the single factor `p$ (coprime
to `q`) does not change `q`-adic valuation, so `q\mid e_0\iff q\mid d_0
\iff q\mid c_0`. Hence `\sigma(e_0)=\sigma(c_0)`.

**Case (ii): `p>k`.** `d_0=e_0p` is a term; by Claim 3's contrapositive
with `n:=e_0` (valid: `n=e_0\ge k` shown above), `e_0` is a term.
Similarity: `p>k` is not a small prime at all, so for every small prime
`q$, dividing by `p` doesn't change `q`-adic valuation: `q\mid e_0\iff
q\mid d_0\iff q\mid c_0`. Hence `\sigma(e_0)=\sigma(c_0)`.

In both cases, `(c_0,e_0)` is a similar-multiple pair with `c_0` a
non-term, `e_0` a term (different status) and `e_0<d_0` — contradicting
minimality of `d_0`. Both cases exhaust all possibilities for `p`
(`p\le k` or `p>k`), so no counterexample exists. `∎` (This proves the
sub-claim, hence, by Step A, the Dichotomy Theorem.)

**Certification.** Sorry-free. Every step re-derived from the problem's
own recursive definition via Lemma REC + Corollary P″ only (no external
citation used without reproof). The domain hypotheses of Claim 2/3's
contrapositives (`rs\ge k`, `n\ge k`) — which the official crux solution
does not separately flag — are here verified explicitly at the point of
use (`e_0=c_0t_0'\ge c_0\ge k`, since `t_0'\ge1`). Independently
re-verified by the round-15 proof-reviewer: hand re-derivation of every
step, plus exhaustive fresh-code stress tests of Claim 2 (20,000 random
trials, zero violations) and of the full Dichotomy Theorem via exhaustive
signature-vs-status scans on `a_1\in\{247,2747,4087,4199,21528751\}`
(159,000–255,000 integers scanned per case, zero violations), plus edge
cases `a_1\in\{2,3,4,5\}`.
