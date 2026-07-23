## Status
solved

## Round 15 update (headline — read this first)

**THE GENERAL PROBLEM IS SOLVED.** Approach
`similarity-dichotomy-crux-adaptation` produced a complete, gap-free,
from-scratch proof of the problem's exact statement — for **every**
starting value `a_1>1`, there exist positive integers `T,L` with
`a_{n+T}=a_n+L` for **every** `n\ge1` (not just eventually) — by adapting
IMO Shortlist 2013 N5's official Solution 1 ("Ana and Banana," crux
`aimo-0030`) into `imo-2026-06`'s own recursive vocabulary, re-proving
every step from scratch (including two "similarity is preserved" steps
the official solution states without proof), and adding a new exact
periodicity corollary (Section 7 below) beyond what the crux itself
needed. This supersedes all 14 prior rounds' FCBC/Conjecture-(JW)/
Corollary-MSF apparatus **for the purpose of the problem's literal
conclusion** — that apparatus remains valid, certified, independently
interesting content about finer structure (minimal `T,L`, minimal
covering set `H`) the problem does not ask about.

**Proof-reviewer's independent verification (maximal adversarial scrutiny,
per this workspace's 14-round history of catching real overclaims).**
Independently re-derived, line by line, every one of: Lemma REC, Corollary
P″, Claims 1/2/3, the Main Dichotomy Theorem (both minimal-counterexample
cases `p\le k`/`p>k`), and the periodicity corollary's interleaving
argument (Steps 1–7). Cross-checked the crux adaptation directly against
`aimo-0030`'s official solution text (`past_problems_database.json`) —
confirmed IMO-SL 2013 N5 exactly, confirmed the file re-derives Claims 1–3
and the Dichotomy Theorem from scratch in the problem's own language
rather than importing them, and confirmed the two similarity-preservation
steps the crux leaves implicit (dividing by a small vs. big prime `p`
preserves `\sigma`) are here proved explicitly. Wrote entirely fresh
Python (no reuse of the builder's scripts) and:
- Exactly reproduced the builder's periodicity table for `a_1\in
  \{6,10,12,15\}` (`T,L` values `(15,30),(105,210),(1155,2310),
  (8008,30030)` — matches `L/L_0=T/T_0=1001` for `a_1=15`'s
  independently-certified minimal period `(8,30)`, confirming the theorem
  gives a valid, if non-minimal, multiple), **plus 8 NEW values not tested
  by the builder** (`a_1\in\{2,3,4,5,7,9,11,14\}`, including the smallest
  possible edge cases `a_1=2,3`), zero exceptions in every case across
  thousands of checked indices.
- Ran an **exhaustive** (not sampled) small-prime-signature-vs-term-status
  scan directly testing the Main Dichotomy Theorem itself (the true
  load-bearing final ingredient) on all 4 of this workspace's historically
  hardest test cases, **including the longest-standing hardest recurring
  instance `a_1=21{,}528{,}751`**: zero violations across `172{,}236`
  (`a_1=247`), `223{,}697` (`2747`), `255{,}338` (`4087`), `79{,}442`
  (`4199`), and `169{,}436` (`21528751`) consecutive integers scanned,
  spanning `17{,}731`–`159{,}319` distinct signatures per case.
- Independently stress-tested Lemma REC (random-sample, 3000 trials per
  case on `a_1\in\{247,2747,21528751\}`, zero violations) and Claim 2
  (20,000 random trials on `a_1=247,21528751`, zero violations).
- Found **one genuine but purely cosmetic documentation gap**: the
  Dichotomy Theorem's proof invokes Claim 2's/Claim 3's contrapositive
  forms (`r^2s` term `\Rightarrow rs` term; `np` term `\Rightarrow n`
  term), each of which needs its target (`rs`, resp. `n`) to actually lie
  in the term/non-term domain (`\ge k`) for the conclusion to be
  meaningful — the original file does not spell out why this holds at the
  point of use. On inspection this is a genuine, unconditional, one-line
  consequence of already-stated facts (`e_0=c_0t_0'\ge c_0\ge k`, since
  `t_0'\ge1`), true in **both** cases of the Dichotomy proof, requiring no
  new idea — **not** a break in the argument's validity, unlike this
  workspace's prior real catches (e.g. round 1's Lemma S′, round 12's
  Backbone-Permanence overclaim). Per this workspace's established
  practice (repair genuinely trivial, one-line gaps rather than reject
  outright, and say so explicitly), this has been patched into the
  certified lemma write-up below and into `lemmas/theorem-similarity-
  dichotomy.md`. No other gap, of any size, was found after this
  reviewer's full line-by-line re-derivation of every claim.

**Verdict: `similarity-dichotomy-crux-adaptation` — APPROVE (Status
`solved`).** This is the terminal result for this run: the general
problem (every `a_1`) is now proved, not merely a further instance or
reduction.

**The other two builds this round, reviewed independently and unaffected
in their own correctness by the result above (their own verdicts are
`CHANGES REQUESTED`, now of reduced overall importance since the general
problem is solved by a different approach, but still genuine, correctly
self-scoped progress worth recording):**

- `forced-primes-well-ordering` (Corollary CRR, "Common-Recruiter Reuse"):
  a correct, honestly-scoped one-line generalization of the already-
  certified Lemma WF (re-aims an already-on-file witness at *every* core
  disjoint from its own, not just the one originally targeted) — closes
  4 more disjoint core-pair channels of `a_1=21{,}528{,}751` (now `5/6`
  channels closed; channel `(\{1061\},\{103,197\})` honestly left open,
  with fresh evidence — a second, structurally different escape bundle
  `\{11,5,23\}` at `n=30{,}000` — that a single fixed `W` is not known to
  close it). Proof-reviewer independently re-derived Corollary CRR's proof
  and re-verified all 4 witness factorizations via `sympy.factorint`
  against a fresh independent generator: exact match
  (`a_{1405}=2^{11}\cdot103^2`, `a_{11812}=3^7\cdot103^2`,
  `a_{27832}=7^4\cdot103^2`, `a_{2575}=2^2\cdot3^4\cdot7^3\cdot197`). No
  gap found. Certified as-is (no new lemma file needed beyond what's
  already certified; Corollary CRR is explicitly, honestly described by
  its own author as adding "no new mathematics" to already-certified
  Lemma WF, only a reusable bookkeeping fact).
- `intersecting-family-covering-construction` (Theorem EI,
  Existence-Insufficiency): a rigorous, correctly-scoped negative result
  closing the "intermediate mechanism" gap round 14's reviewer left open —
  proves that *no* bounded-modulus/CRT/pigeonhole mechanism that only ever
  certifies *existence* (not universal admissibility) of an admissible
  type-`S'` candidate, for any window size or witness combination, can
  establish `\mathrm{BRL}(S')`/`G`-eventual-periodicity, via a clean
  Type-Symmetry argument (Lemma TS: the identical density argument
  equally certifies every other disjoint core type, so it cannot single
  out `S'`) plus Automatic Admissibility for non-disjoint types (Lemma AA)
  and the trivial Global-Minimum characterization (Lemma GM). Correctly
  and explicitly **not** a claim that `\mathrm{BRL}(S')` is false — this
  is now moot for the overall problem, since the general theorem is
  proved by the sibling approach above without needing
  `\mathrm{BRL}(S')`/`G`-periodicity/FCBC at all. Proof-reviewer confirmed
  Lemma TS/AA/GM and Theorem EI's 3-step proof are each individually
  sound, no smuggled assumption, no overclaim (the file explicitly and
  correctly disclaims refuting `\mathrm{BRL}(S')` itself). No gap found.

## Approaches tried

- `similarity-dichotomy-crux-adaptation` (round 15) — **WORKED. Full
  solution of the general problem.** See Full proof below.
- `forced-primes-well-ordering` (rounds 3–15) — extensive real progress:
  produced this workspace's first 2 fully solved concrete instances
  (`a_1=247,4199`), Corollary CRR closing 4 more channels of
  `a_1=21528751`, the Sandwich Uniqueness Lemma, Channel Assembly/
  Splitting Theorems, and much certified machinery (see `lemmas/`); never
  itself closed the general theorem, superseded in that role by
  `similarity-dichotomy-crux-adaptation` but its certified lemmas remain
  independently valid and reusable.
- `intersecting-family-covering-construction` (rounds 1–15) — extensive
  real progress: Theorem 5.1 (Master Conditional Theorem, FCBC ⟹ whole
  problem, exact periodicity from `n=1`), Theorem MO/Theorem EI
  (impossibility results for whole mechanism families), Lemma WO/WO++,
  and much certified machinery; top-Elo approach for most of the run's
  history via Theorem 5.1's conditional closure; superseded as the
  terminal result by `similarity-dichotomy-crux-adaptation`'s
  unconditional proof.
- `sunflower-bundle-closure`, `sunflower-inadmissibility-toolkit`,
  `persistent-backbone-monovariant`, `explicit-window-backbone-
  construction`, `imprint-automaton-periodicity`, `core-depth-induction`,
  `witness-chaining-universal-existence` — all made genuine certified
  progress toward the FCBC/Conjecture-(JW)/Corollary-MSF apparatus (3 more
  solved concrete instances `2747,4087,15`, Corollary MSF, many certified
  lemmas — see `lemmas/`); none closed the general theorem; all superseded
  in that role.
- `backbone-existence-crt`, `bounded-gap-density-covering`,
  `global-recruiter-finiteness`, `core-antichain-content-freeze` — dead
  ends / parked, see round-by-round history in `/tmp/memory/run_state.md`
  and prior round reports for exact reasons (not repeated here since the
  problem is now solved).

## Current best

Superseded by the Full proof below (Status is `solved`).

## Full proof

*(Self-contained; adapted from IMO Shortlist 2013 N5's official Solution 1,
crux `aimo-0030`, with every step re-derived from `imo-2026-06`'s own
recursive definition, plus a new periodicity corollary, Section 7, beyond
what the crux itself needed.)*

### 0. Setup and terminology

Fix the sequence `(a_n)_{n\ge1}` as in the problem statement, and write
`k:=a_1>1`. Since `a_{n+1}>a_n` for every `n`, the sequence is strictly
increasing, hence unbounded, and `a_n\ge k` for every `n`.

**Terms and non-terms.** Call an integer `n\ge k` a *term* if `n=a_j` for
some `j\ge1`, and a *non-term* otherwise (integers `<k` are not
classified). Note `k=a_1` is always a term.

**Small primes and signature.** Let `P:=\prod_{p\le k\text{ prime}}p`
(finite). For `n\ge k`, its *small prime set* is `\sigma(n):=\{p\le k
\text{ prime}:p\mid n\}`. Call `n,n'\ge k` *similar* if `\sigma(n)=
\sigma(n')`.

**Elementary fact.** If `n\equiv n'\pmod P` (both `\ge k`) then `n,n'` are
similar: for every prime `p\le k`, `p\mid P`, so `n\equiv n'\pmod p`,
hence `p\mid n\iff p\mid n'`.

### 1. Lemma REC (recursive IN/OUT characterization)

**Lemma REC.** Let `n>k` be an integer. Then `n` is a non-term if and only
if there exists a term `m` with `k\le m<n` and `\gcd(m,n)=1`.

*Proof.* (⇐) If a term `m` with `k\le m<n`, `\gcd(m,n)=1` exists, and `n`
were a term `n=a_j`, then `m=a_i` for some `i<j` (strictly increasing
sequence), and the recursive definition of `a_j` (which requires
`\gcd(a_j,a_l)>1` for all `l\le j-1`, in particular `l=i`) gives
`\gcd(m,n)>1` — contradiction. So `n` is a non-term.

(⇒) If `n>k` is a non-term: since `(a_i)` is unbounded and `a_1=k<n`, let
`j:=\max\{i:a_i<n\}` (finite, nonempty). Then `a_j<n`, and by maximality
`a_{j+1}\ge n`; since `n` is a non-term, `a_{j+1}\ne n`, so `a_j<n<a_{j+1}`.
As `a_{j+1}` is the *smallest* integer `>a_j` satisfying `\gcd(\cdot,a_i)>1`
for all `i\le j`, and `n` is a smaller candidate, `n` must fail: some
`i\le j` has `\gcd(n,a_i)=1`. Set `m:=a_i` — a term with `k\le m\le a_j<n`,
`\gcd(m,n)=1`. `∎`

### 2. Corollary P″ (any two terms share a common factor)

**Corollary P″.** For every `i\ne j`, `\gcd(a_i,a_j)>1`.

*Proof.* WLOG `i<j`. By definition `a_j` satisfies `\gcd(a_j,a_l)>1` for
every `l=1,\dots,j-1`; take `l=i`. `∎`

### 3. Claim 1 (multiple of a term is a term)

**Claim 1.** If `n` is a term and `n'\ge n` is a multiple of `n`, then `n'`
is also a term.

*Proof.* Trivial if `n'=n`. If `n'>n`, suppose toward contradiction `n'` is
a non-term; by Lemma REC there is a term `m` with `k\le m<n'`,
`\gcd(m,n')=1`. Since `n\mid n'`, `\gcd(m,n')=1\Rightarrow\gcd(m,n)=1`. But
`m,n` both terms give `\gcd(m,n)>1` by Corollary P″ — contradiction. `∎`

### 4. Claim 2 (companion move, small-prime case)

**Claim 2.** Let `r,s` be positive integers with `rs\ge k`. If `rs` is a
non-term, then `r^2s` is also a non-term.

*Proof.* By Lemma REC there is a term `x`, `k\le x<rs`, `\gcd(x,rs)=1`.
Since `r,s\mid rs`, `\gcd(x,r)=\gcd(x,s)=1`, so `\gcd(x,r^2s)=1`. Since
`r\ge1`, `rs\le r^2s`, so `x<rs\le r^2s`. By Lemma REC (⇐), `r^2s` is a
non-term. `∎`

**Contrapositive (used later, with the domain check spelled out at the
point of use):** if `r^2s` is a term **and** `rs\ge k`, then `rs` is a
term.

### 5. Claim 3 (companion move, big-prime case)

**Claim 3.** Let `p` be a prime with `p>k`, and `n\ge k` a non-term. Then
`np` is also a non-term.

*Proof.* By well-ordering, suppose not, and take a minimal counterexample
`n` (with witnessing prime `p>k`: `n` non-term, `np` term).

*Step 1.* By Lemma REC, a term `m` exists with `k\le m<n`, `\gcd(m,n)=1`.

*Step 2.* Since `np` is a term and `m<n<np` is a term, Lemma REC (⇐)
applied contrapositively to `np` forces `\gcd(m,np)>1`; with `\gcd(m,n)=1`
this gives `p\mid m`.

*Step 3.* Write `m=p^ry`, `r\ge1`, `p\nmid y`.

*Step 4.* If `y=1`: `m=p^r\ge p>k`, and `\gcd(k,m)=1` (all prime factors of
`k` are `\le k<p`); by Lemma REC (⇐) with witness `k`, `m` would be a
non-term, contradicting Step 1. So `y\ge2`.

*Step 5.* Let `\alpha\ge1` minimal with `y^\alpha\ge k`; then
`y^{\alpha-1}<k`.

*Step 6.* `y^\alpha=y^{\alpha-1}y<ky<py=p^ry/p^{r-1}=m/p^{r-1}<n/p^{r-1}`,
so `p^{r-1}y^\alpha<n`. Hence for `i=0,\dots,r-1`:
`k\le y^\alpha\le p^iy^\alpha\le p^{r-1}y^\alpha<n`.

*Step 7.* `\gcd(y,n)=1` (as `y\mid m`, `\gcd(m,n)=1`), `\gcd(y,p)=1`, so
`\gcd(y^\alpha,np)=1`. Since `np` is a term, `y^\alpha` cannot also be a
term (Corollary P″ would force `\gcd(np,y^\alpha)>1`). So `y^\alpha` is a
non-term.

*Step 8.* Induction on `i=0,\dots,r-1` (base `i=0`: Step 7): if
`p^iy^\alpha` is a non-term, then (since `p^iy^\alpha<n`, Step 6, and `n`
is the minimal counterexample) `(p^iy^\alpha,p)` cannot be a
counterexample, so `p^{i+1}y^\alpha` must be a non-term. Taking `i=r-1`:
`p^ry^\alpha` is a non-term.

*Step 9.* `m=p^ry` divides `p^ry^\alpha=m\cdot y^{\alpha-1}` (a genuine
positive-integer multiple since `y^{\alpha-1}\ge1`). If `m` were a term,
Claim 1 would force `p^ry^\alpha` to be a term, contradicting Step 8. So
`m` is a non-term — contradicting Step 1. `∎`

**Contrapositive (used later, domain check spelled out at point of use):**
if `n\ge k`, `p>k` prime, and `np` is a term, then `n` is a term.

### 6. Main Dichotomy Theorem

**Theorem.** If `n,n'\ge k` are similar, then `n,n'` have the same
term-status.

*Proof.*

**Step A (reduction).** It suffices to show: if `c\ge k`, `d=ct` for a
positive integer `t`, and `c,d` similar, then `c,d` share status (the
"sub-claim"). Given similar `n,n'\ge k`, set `d:=nn'`; then `d\ge k` and
`\sigma(d)=\sigma(n)=\sigma(n')` (a prime `p\le k` divides `nn'` iff it
divides `n` or `n'`, and by similarity these coincide). Applying the
sub-claim to `(n,d)` and `(n',d)` shows `n,n'` both share `d`'s status,
hence each other's.

**Step B (minimal counterexample).** Suppose the sub-claim fails; any
counterexample has `t\ge2`. Take a counterexample `(c_0,d_0)` with `d_0`
minimal. By Claim 1, `c_0` cannot be a term (else `d_0` would match), so
`c_0` is a non-term and `d_0` (the only remaining status) is a term.

Since `t_0\ge2` has a prime factor `p`, write `t_0=pt_0'` (`t_0'\ge1`
integer); set `e_0:=d_0/p=c_0t_0'`. Then `c_0\mid e_0`, and since
`t_0'\ge1`, **`e_0=c_0t_0'\ge c_0\ge k`** — so `e_0` is validly in the
term/non-term domain. Also `e_0<d_0` (`p\ge2`).

**Case (i): `p\le k`.** Since `p\mid d_0` and `\sigma(c_0)=\sigma(d_0)`
with `p\le k`, `p\mid c_0` too; writing `c_0=pc_0'`, `t_0=pt_0'` gives
`d_0=p^2(c_0't_0')`, so `p^2\mid d_0`. Apply Claim 2's contrapositive with
`r:=p,s:=c_0't_0'` (valid: `rs=e_0\ge k` as shown; `r^2s=d_0` is a term):
`e_0=rs` is a term. Similarity of `(c_0,e_0)`: `p\mid e_0` (from `p^2\mid
d_0`) matches `p\mid c_0`; for any small prime `q\ne p`, removing the
single factor `p` from `d_0` doesn't change `q`-adic valuation, so `q\mid
e_0\iff q\mid d_0\iff q\mid c_0` (similarity of `c_0,d_0`). So
`\sigma(e_0)=\sigma(c_0)`.

**Case (ii): `p>k`.** `d_0=e_0p` is a term; Claim 3's contrapositive with
`n:=e_0` (valid: `e_0\ge k` as shown) gives `e_0` is a term. Similarity:
`p>k` is not a small prime, so removing it from `d_0` doesn't change any
small-prime valuation: `q\mid e_0\iff q\mid d_0\iff q\mid c_0` for every
small `q`. So `\sigma(e_0)=\sigma(c_0)`.

In both cases, `(c_0,e_0)` is a similar-multiple pair with `c_0` a
non-term, `e_0` a term, `e_0<d_0` — contradicting minimality of `d_0`.
Since `p\le k` or `p>k` exhausts all possibilities, no counterexample
exists. `∎` (proves the sub-claim, hence, by Step A, the Theorem).

### 7. Periodicity corollary (new content, resolves the problem)

Recall `P=\prod_{p\le k}p` (finite).

**Step 1.** By the elementary fact + Dichotomy Theorem, every residue
class mod `P` (restricted to integers `\ge k`) is uniformly all-term
("good") or all-non-term ("bad").

**Step 2.** Hence `\{n\ge k:n\text{ term}\}=\{n\ge k:n\bmod P\text{ good}\}`.
Since `k\bmod P` is good (`k` is always a term), the number `T` of good
residues in `\{0,\dots,P-1\}` satisfies `1\le T\le P`.

**Step 3.** Let `\beta_1<\cdots<\beta_T` be the unique representatives of
the good residues in `[k,k+P)`; `\beta_1=k`.

**Step 4 (interleaving).** The term set equals `\bigcup_{l=1}^T\{\beta_l
+jP:j\ge0\}`. Within each "block" `j` the `T` values are sorted increasing;
consecutive blocks don't overlap since `\beta_T-\beta_1<P` (both in a
length-`P` interval). So the sorted enumeration `g_1<g_2<\cdots` of the
union satisfies `g_{mT+l}=\beta_l+mP` for all `m\ge0`, `l\in\{1,\dots,T\}`.

**Step 5.** For every `n\ge1`, writing `n=mT+l` (`1\le l\le T`):
`g_{n+T}=\beta_l+(m+1)P=g_n+P`.

**Step 6.** Since `(a_n)_{n\ge1}` is by definition the strictly increasing
enumeration of the term set, and that set equals the explicit union just
sorted, uniqueness of the increasing enumeration gives `g_n=a_n` for every
`n\ge1`.

**Conclusion.** Setting `T:=\#\{\text{good residues mod }P\}`,
`L:=P=\prod_{p\le a_1}p`, we have `1\le T\le P` and
$$a_{n+T}=a_n+L\qquad\text{for every positive integer }n.$$
This is exactly the problem's required conclusion. `∎`

### 8. Verification (numerical, corroborating, not load-bearing)

The argument above is fully self-contained. As an end-to-end sanity
check, both the original builder and (independently, with fresh code) the
round-15 reviewer verified `a_{n+T}=a_n+L` with zero exceptions for
`a_1\in\{2,3,4,5,6,7,9,10,11,12,14,15\}` (12 values; e.g. `a_1=15` gives
`T=8008,L=30030`, a genuine positive-integer multiple —
`1001\times(8,30)` — of this workspace's independently certified minimal
period `(8,30)`, consistent since the problem only asks for existence of
*some* valid `T,L`), and the Main Dichotomy Theorem itself (the load
-bearing final ingredient) was exhaustively verified via small-prime
-signature-vs-term-status scans on `a_1\in\{247,2747,4087,4199,
21528751\}` (the last being this workspace's longest-standing hardest
recurring test case), scanning `79{,}442`–`255{,}338` consecutive
integers per case with **zero violations**.

### 9. Answer

`T` and `L` exist explicitly for every `a_1>1`: `L=\prod_{p\le a_1\text{
prime}}p`, and `T` is the number of residues `r\bmod L` such that every
integer `\ge a_1` congruent to `r` is a term of the sequence (equivalently,
the number of distinct residue classes taken by the sequence before its
pattern of residues repeats) — both finite, both `\ge1`, and
`a_{n+T}=a_n+L` holds for **every** `n\ge1`, as required.

## Promotable lemmas (certified this round)

- `lemmas/lemma-REC-recursive-IN-OUT-characterization.md` — Lemma REC.
- `lemmas/theorem-similarity-dichotomy.md` — Corollary P″ (restated),
  Claims 1–3, Main Dichotomy Theorem.
- `lemmas/theorem-periodicity-from-dichotomy.md` — the periodicity
  corollary that resolves the whole problem.

All prior rounds' certified lemmas (`lemmas/*.md`, ~65 files) remain valid
and are retained: they constitute an independently interesting body of
results about the problem's finer structure (minimal periods, minimal
covering sets, the FCBC/Conjecture-(JW)/Corollary-MSF apparatus) that the
problem itself does not require, now that the general theorem is proved
by the route above.
