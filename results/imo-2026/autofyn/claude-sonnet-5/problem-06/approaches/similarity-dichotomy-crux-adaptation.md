## Status
solved

## Approaches tried
- Round 15 (this round, first build of this slug): full from-scratch
  translation of the official IMO Shortlist 2013 N5 ("Ana and Banana",
  crux `aimo-0030`) similarity-dichotomy proof (Solution 1, the one built
  on Claims 1–3) into `imo-2026-06`'s own recursive language, closing
  every gap the outline (and the outline-reviewer) flagged as RECON-only:
  the IN/OUT bridge lemma (Lemma REC), Claims 1/2/3 in full, the Main
  Dichotomy Theorem (full minimal-counterexample argument, both the
  `p≤k` and `p>k` cases, including the "similarity is preserved when
  dividing by `p`" step the official solution states without proof), and
  the mod-`P` periodicity corollary with an explicit, fully-justified
  interleaving argument giving exact (not eventual) periodicity from
  `n=1`. **Outcome: WORKED — this closes the general problem for every
  `a_1`, superseding all 14 rounds of FCBC/Conjecture-(JW)/Corollary-MSF
  apparatus for the purpose of the problem's literal conclusion** (that
  apparatus remains a valid, independently interesting body of certified
  results about finer structure — minimal `H`, minimal period — which the
  problem does not ask for). Numerically re-verified every claim (Claims
  1–3, the Dichotomy, and the final periodicity formula) on multiple
  fresh `a_1` values as an end-to-end sanity check (not a substitute for
  the proof, which is self-contained below).

## Current best
Complete, from-scratch, rigorous proof of the full problem — see below.

## Full proof

### 0. Setup and terminology

Fix the sequence $(a_n)_{n\ge1}$ as in the problem statement, and write
$k:=a_1$ (so $k$ is an integer $>1$). Since $a_{n+1}>a_n$ for every $n$,
the sequence is strictly increasing; in particular $a_n\ge k$ for every
$n$, and $(a_n)$ is unbounded (a strictly increasing sequence of
integers has no upper bound).

**Terms and non-terms.** Call an integer $n\ge k$ a *term* if $n=a_j$ for
some index $j\ge1$, and a *non-term* otherwise. (We only ever classify
integers $\ge k$; integers $<k$ play no role.) Note $k=a_1$ is always a
term, by definition of the sequence.

**Small primes and signature.** Let
$$P:=\prod_{p\le k,\ p\text{ prime}} p.$$
This is a finite product, since only finitely many primes are $\le k$
(a fixed positive integer). For an integer $n\ge k$, define its *small
prime set* $\sigma(n):=\{p\le k \text{ prime} : p\mid n\}$. Call two
integers $n,n'\ge k$ *similar* if $\sigma(n)=\sigma(n')$.

**Elementary fact (residue determines signature).** If $n\equiv n'
\pmod P$ then $n,n'$ are similar. *Proof:* for every prime $p\le k$,
$p\mid P$, so $n\equiv n'\pmod p$; hence $p\mid n \iff p\mid n'$. Since
this holds for every prime $p\le k$, $\sigma(n)=\sigma(n')$. $\blacksquare$

### 1. Lemma REC (recursive IN/OUT characterization)

**Lemma REC.** Let $n>k$ be an integer. Then $n$ is a non-term if and
only if there exists a term $m$ with $k\le m<n$ and $\gcd(m,n)=1$.

*Proof.*

($\Leftarrow$) Suppose some term $m$ satisfies $k\le m<n$ and
$\gcd(m,n)=1$. Suppose toward a contradiction that $n$ is itself a term,
say $n=a_j$. Since $m$ is a term with $m<n=a_j$ and the sequence is
strictly increasing, $m=a_i$ for some index $i<j$ (an earlier index of
the same strictly increasing sequence). By the recursive definition of
$a_j=a_{(j-1)+1}$: $a_j$ is required to satisfy $\gcd(a_j,a_l)>1$ for
every $l=1,\dots,j-1$; taking $l=i$ (valid since $i\le j-1$) gives
$\gcd(a_j,a_i)=\gcd(n,m)>1$, contradicting $\gcd(m,n)=1$. Hence $n$ is
not a term, i.e. $n$ is a non-term.

($\Rightarrow$) Suppose $n>k$ is a non-term. Since $(a_i)$ is unbounded
and $a_1=k<n$, the set $\{i : a_i<n\}$ is a finite nonempty set of
positive integers (nonempty since $a_1=k<n$; finite since $(a_i)$ is
strictly increasing hence eventually exceeds $n$); let $j$ be its
maximum. So $a_j<n$, and by maximality of $j$, $a_{j+1}\ge n$ (if
$a_{j+1}<n$ then $j+1$ would also lie in the set, contradicting
maximality). If $a_{j+1}=n$ then $n$ would be a term, contradicting the
hypothesis; so $a_{j+1}>n$, and we have
$$a_j<n<a_{j+1}.$$
By the recursive definition, $a_{j+1}$ is the **smallest** integer
greater than $a_j$ satisfying $\gcd(\cdot,a_i)>1$ for all $i=1,\dots,j$.
Since $n$ is an integer with $a_j<n<a_{j+1}$, $n$ is a strictly smaller
candidate than $a_{j+1}$, so $n$ must fail the required condition:
there exists $i\le j$ with $\gcd(n,a_i)=1$. Set $m:=a_i$. Then $m$ is a
term, $m=a_i\le a_j<n$ so $m<n$, and $m\ge a_1=k$ (as $i\ge1$). Also
$\gcd(m,n)=1$. This is the required witness. $\blacksquare$

(For $n=k$ itself, there is no candidate $m$ with $k\le m<k$, and
indeed $k=a_1$ is always a term — this is the base case, consistent
with the biconditional read vacuously.)

### 2. Corollary P″ (any two terms share a common factor)

This fact is already certified in this workspace
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`, "Corollary
P″", itself an immediate unordered restatement of the certified Lemma P′,
`lemmas/lemma-P-prime-pairwise-intersecting.md`). We restate and use it
as-is (no new content needed):

**Corollary P″.** For every $i\ne j$, $\gcd(a_i,a_j)>1$.

*Proof (reproduced for self-containedness).* WLOG $i<j$. By definition,
$a_j=a_{(j-1)+1}$ satisfies $\gcd(a_j,a_l)>1$ for every $l=1,\dots,j-1$;
taking $l=i$ gives $\gcd(a_i,a_j)>1$. $\blacksquare$

Equivalently: **any two terms have $\gcd>1$.**

### 3. Claim 1 (multiple of a term is a term)

**Claim 1.** If $n$ is a term and $n'\ge n$ is a multiple of $n$, then
$n'$ is also a term.

*Proof.* If $n'=n$ this is trivial. Suppose $n'>n$ and, toward a
contradiction, that $n'$ is a non-term. Since $n'>n\ge k$, in particular
$n'>k$, so by Lemma REC ($\Rightarrow$) there is a term $m$ with $k\le
m<n'$ and $\gcd(m,n')=1$. Since $n\mid n'$, any common factor of $m$ and
$n$ would also be a common factor of $m$ and $n'$; as $\gcd(m,n')=1$,
this forces $\gcd(m,n)=1$. But $m$ and $n$ are both terms, so by
Corollary P″, $\gcd(m,n)>1$ — contradiction. Hence $n'$ is a term.
$\blacksquare$

### 4. Claim 2 (companion move, small-prime case)

**Claim 2.** Let $r,s$ be positive integers with $rs\ge k$. If $rs$ is a
non-term, then $r^2s$ is also a non-term.

*Proof.* Since $rs$ is a non-term and $k=a_1$ is always a term, $rs\ne
k$, so $rs>k$. By Lemma REC ($\Rightarrow$) there is a term $x$ with
$k\le x<rs$ and $\gcd(x,rs)=1$.

Since $r\mid rs$ and $s\mid rs$, $\gcd(x,rs)=1$ forces $\gcd(x,r)=1$ and
$\gcd(x,s)=1$. Any prime dividing $r^2s$ divides $r$ or $s$; since $x$
shares no prime with either, $\gcd(x,r^2s)=1$.

Also, since $r\ge1$, $r^2\ge r$, so multiplying by $s\ge1>0$ gives
$rs\le r^2s$. Combined with $x<rs$ (strict), we get $x<rs\le r^2s$, i.e.
$x<r^2s$.

So $x$ is a term with $k\le x<r^2s$ and $\gcd(x,r^2s)=1$. By Lemma REC
($\Leftarrow$), $r^2s$ is a non-term. $\blacksquare$

**Contrapositive (used later):** if $r^2s$ is a term, then $rs$ is a
term.

### 5. Claim 3 (companion move, big-prime case)

**Claim 3.** Let $p$ be a prime with $p>k$, and let $n\ge k$ be a
non-term. Then $np$ is also a non-term.

*Proof.* Since $k=a_1$ is always a term, a non-term $n\ge k$ satisfies
$n\ne k$, hence $n>k$.

Suppose, toward a contradiction, that Claim 3 fails for some pair
$(n,p)$ (i.e. $n>k$ is a non-term, $p>k$ is prime, but $np$ **is** a
term). Among all such counterexample values of $n$ (ranging over all
primes $p>k$ that could pair with them), the set of possible $n$ is a
nonempty subset of the positive integers, so by well-ordering it has a
least element; fix such a minimal counterexample $n$, together with a
witnessing prime $p>k$ (so $n$ is a non-term, $np$ is a term).

**Step 1: find $m$.** Since $n>k$ is a non-term, Lemma REC
($\Rightarrow$) gives a term $m$ with $k\le m<n$ and $\gcd(m,n)=1$.

**Step 2: $p\mid m$.** Since $np$ is a term (the assumed counterexample)
and $m$ is a term with $m<n<np$ (as $p\ge2$), Lemma REC ($\Leftarrow$)
applied contrapositively to $np$ (which IS a term) tells us there is
**no** term strictly below $np$ that is coprime to $np$; since $m$ is a
term with $m<np$, we must have $\gcd(m,np)>1$. We already know
$\gcd(m,n)=1$ (Step 1), so this excess common factor must come from $p$:
$\gcd(m,p)>1$, i.e. (as $p$ is prime) $p\mid m$.

**Step 3: factor $m$.** Write $m=p^r y$ with $r\ge1$ (the exact power of
$p$ dividing $m$) and $p\nmid y$ ($y\ge1$ an integer).

**Step 4: $y\ne1$.** Suppose $y=1$, so $m=p^r$. Since $p>k$ and $r\ge1$,
$m=p^r\ge p>k$. Any prime factor of $k$ is $\le k<p$, so $p\nmid k$;
hence $\gcd(k,m)=\gcd(k,p^r)=1$. Now $k$ is a term with $k<m$ and
$\gcd(k,m)=1$; by Lemma REC ($\Leftarrow$), $m$ is a non-term. But $m$
was chosen (Step 1) to be a term — contradiction. Hence $y\ge2$.

**Step 5: choose $\alpha$.** Since $y\ge2$, the powers $y^1<y^2<\cdots$
increase without bound, so there is a least positive integer $\alpha$
with $y^\alpha\ge k$ (necessarily $\alpha\ge1$ since $y^0=1<k$, as
$k\ge2$); by minimality of $\alpha$, if $\alpha>1$ then $y^{\alpha-1}<k$,
and this inequality also holds trivially when $\alpha=1$ (reading it as
$y^0=1<k$). So in all cases $y^{\alpha-1}<k$.

**Step 6: size bound.** We derive $p^{r-1}y^\alpha<n$:
$$y^\alpha=y^{\alpha-1}\cdot y<k\cdot y \quad(\text{Step 5}),$$
$$k\cdot y<p\cdot y\quad(\text{since }k<p),$$
$$p\cdot y=\frac{p^r y}{p^{r-1}}=\frac{m}{p^{r-1}}\quad(\text{Step 3}),$$
$$\frac{m}{p^{r-1}}<\frac{n}{p^{r-1}}\quad(\text{since }m<n,\ p^{r-1}>0).$$
Chaining these: $y^\alpha<n/p^{r-1}$, i.e. $p^{r-1}y^\alpha<n$.
Consequently, for every $i=0,1,\dots,r-1$: $p^iy^\alpha\le p^{r-1}y^\alpha<n$
(as $p^i\le p^{r-1}$ for $i\le r-1$), and $p^iy^\alpha\ge y^\alpha\ge k$
(Step 5, and $p^i\ge1$). So all of $y^\alpha,py^\alpha,\dots,
p^{r-1}y^\alpha$ lie in $[k,n)$.

**Step 7: $y^\alpha$ is a non-term.** Since $\gcd(m,n)=1$ and $y\mid m$
(Step 3), $\gcd(y,n)\mid\gcd(m,n)=1$, so $\gcd(y,n)=1$. Also $\gcd(y,p)=1$
since $p\nmid y$. Hence $\gcd(y,np)=1$, and therefore $\gcd(y^\alpha,np)=1$
as well. Now $np$ is a term (the counterexample assumption). If $y^\alpha$
were also a term, then $np$ and $y^\alpha$ would be two terms with
$\gcd(np,y^\alpha)=1$, contradicting Corollary P″ (any two terms have
$\gcd>1$). Hence $y^\alpha$ is a non-term.

**Step 8: propagate by minimality.** We show by induction on
$i=0,1,\dots,r-1$ that $p^iy^\alpha$ is a non-term (the case $i=0$ is
Step 7). Suppose $p^iy^\alpha$ ($0\le i\le r-1$) is a non-term. By Step
6, $p^iy^\alpha\in[k,n)$, i.e. $p^iy^\alpha<n$. Since $n$ was chosen as
the **minimal** value that can appear (with some prime $>k$) as a
counterexample to Claim 3, and $p^iy^\alpha<n$ is a non-term with the
prime $p>k$ available, the pair $(p^iy^\alpha,p)$ **cannot** be a
counterexample (else it would contradict minimality of $n$); hence
$p^iy^\alpha\cdot p=p^{i+1}y^\alpha$ must be a non-term. This completes
the induction, and in particular (taking $i=r-1$):
$$p^ry^\alpha\text{ is a non-term.}$$

**Step 9: final contradiction.** Since $\alpha\ge1$, $y\mid y^\alpha$, so
$m=p^ry$ divides $p^ry^\alpha$. If $m$ were a term, then by Claim 1 (a
multiple of a term is a term), $p^ry^\alpha$ would be a term too —
contradicting Step 8. Hence $m$ must be a non-term. But $m$ was chosen
in Step 1 to be a term — a direct contradiction.

This contradiction shows no counterexample to Claim 3 can exist.
$\blacksquare$

**Contrapositive (used later):** if $n\ge k$, $p>k$ prime, and $np$ is a
term, then $n$ is a term.

### 6. Main Dichotomy Theorem

**Theorem (Dichotomy).** If $n,n'\ge k$ are similar (i.e. $\sigma(n)=
\sigma(n')$), then $n$ and $n'$ have the same term-status (both terms
or both non-terms).

*Proof.*

**Step A: reduction to the divisor/multiple case.** It suffices to
prove the following sub-claim:

> **Sub-claim.** If $c\ge k$ and $d=ct$ for some positive integer $t$,
> and $c,d$ are similar, then $c,d$ have the same term-status.

Indeed, given similar $n,n'\ge k$, let $d:=nn'$. First, $d\ge k$: since
$n'\ge k\ge2>1$, we have $d=n\cdot n'\ge n\ge k$. Second, $d$ is similar
to both $n$ and $n'$: writing $\Sigma:=\sigma(n)=\sigma(n')$, for any
prime $p\le k$, $p\mid d=nn' \iff p\mid n\text{ or }p\mid n'$
(prime dividing a product divides a factor); since $n,n'$ are similar,
$p\mid n \iff p\in\Sigma \iff p\mid n'$, so $p\mid d\iff p\in\Sigma$.
Hence $\sigma(d)=\Sigma=\sigma(n)=\sigma(n')$. Since $d$ is a multiple
of $n$ (namely $d=n\cdot n'$) and similar to $n$, the sub-claim (with
$c=n,t=n'$) gives $n,d$ same status. Since $d$ is also a multiple of
$n'$ (namely $d=n'\cdot n$) and similar to $n'$, the sub-claim (with
$c=n',t=n$) gives $n',d$ same status. Combining, $n$ and $n'$ have the
same status as $d$, hence the same status as each other.

**Step B: proof of the sub-claim by minimal counterexample.** Suppose
the sub-claim is false for some pair $(c,d)$ as described. Note that any
counterexample automatically has $d\ne c$ (if $d=c$ they trivially have
the same status), so $t\ge2$ for any counterexample. Among all
counterexample pairs $(c,d)$, choose one, $(c_0,d_0)$, with $d_0$
minimal (well-ordering: $d_0$ ranges over a nonempty subset of the
positive integers).

By Claim 1: if $c_0$ were a term, then since $d_0$ is a multiple of
$c_0$, $d_0$ would also be a term, so $c_0,d_0$ would have the same
status — not a counterexample. Since $(c_0,d_0)$ **is** a counterexample
(different statuses), $c_0$ must be a non-term, and (by Claim 1's
contrapositive being unusable the other way, simply by exhaustion of the
only two statuses) $d_0$ must be a term.

Since $d_0=c_0t_0$ with $t_0\ge2$, the integer $t_0$ has at least one
prime factor; fix a prime $p\mid t_0$. Write $t_0=p\cdot t_0'$ for a
positive integer $t_0'$; then
$$d_0=c_0t_0=c_0\cdot p\cdot t_0' = (c_0t_0')\cdot p,$$
so, setting $e_0:=d_0/p=c_0t_0'$, we have $c_0\mid e_0$ (with $e_0=
c_0t_0'$) and $e_0<d_0$ (as $p\ge2$).

We split into two exhaustive, mutually exclusive cases on the prime $p$
(either $p\le k$ or $p>k$).

**Case (i): $p\le k$.** Since $p\mid d_0$ (as $p\mid t_0\mid$ the
quotient $d_0/c_0$, hence $p\mid d_0$) and $c_0,d_0$ are similar
($\sigma(c_0)=\sigma(d_0)$) and $p\le k$, we get $p\in\sigma(d_0)=
\sigma(c_0)$, i.e. $p\mid c_0$. So $p\mid c_0$ and $p\mid t_0$; writing
$c_0=p c_0'$, $t_0=pt_0'$, we get
$$d_0=c_0t_0=p c_0'\cdot p t_0' = p^2(c_0't_0'),$$
so $p^2\mid d_0$. Applying Claim 2's contrapositive with $r:=p$,
$s:=c_0't_0'$ (so $r^2s=d_0$ is a term, hence $rs=p\cdot c_0't_0'=
e_0=d_0/p$ is a term as well).

We now check $(c_0,e_0)$ is again a similar-multiple pair, so that it
qualifies as a legitimate counterexample: we already have $c_0\mid e_0$.
For similarity, we check $\sigma(e_0)=\sigma(c_0)$: for the prime $p$
itself, since $p^2\mid d_0$, $p\mid d_0/p=e_0$, so $p\in\sigma(e_0)$,
matching $p\in\sigma(c_0)$ (shown above) $=\sigma(d_0)$. For any other
small prime $q\le k$, $q\ne p$: since $q,p$ are distinct primes,
dividing $d_0$ by the single factor $p$ does not change the $q$-adic
valuation, i.e. $q\mid e_0=d_0/p \iff q\mid d_0$; combined with
$\sigma(d_0)=\sigma(c_0)$, we get $q\mid e_0\iff q\mid c_0$. Hence
$\sigma(e_0)=\sigma(c_0)$, i.e. $c_0,e_0$ are similar.

So $(c_0,e_0)$ is a similar-multiple pair with $c_0$ a non-term
(unchanged from before) and $e_0$ a term (just shown) — a genuine
counterexample to the sub-claim — with $e_0<d_0$. This contradicts the
minimality of $d_0$.

**Case (ii): $p>k$.** Here $p\mid d_0=e_0\cdot p$, so $e_0=d_0/p$ is an
integer, and $d_0=e_0\cdot p$ is a term (unchanged: $d_0$ is a term).
Since $p>k$ is prime, Claim 3's contrapositive (with $n:=e_0$) gives:
$e_0\cdot p=d_0$ is a term $\implies e_0$ is a term.

We again check $(c_0,e_0)$ is a similar-multiple pair: $c_0\mid e_0$ was
already shown (generic, independent of the case). For similarity: since
$p>k$, $p$ is not among the small primes at all, so for every small
prime $q\le k$ we automatically have $q\ne p$, and (as in Case (i)'s
argument for primes $\ne p$) dividing by the single factor $p$ (coprime
to $q$) does not change $q$-adic valuation: $q\mid e_0=d_0/p \iff q\mid
d_0$. Combined with $\sigma(d_0)=\sigma(c_0)$, this gives $\sigma(e_0)=
\sigma(c_0)$.

So again $(c_0,e_0)$ is a similar-multiple pair with $c_0$ a non-term,
$e_0$ a term, and $e_0<d_0$ — contradicting minimality of $d_0$.

Both cases (i) and (ii) — which exhaust all possibilities for the prime
$p$ — lead to a contradiction. Hence no counterexample $(c_0,d_0)$ can
exist, proving the sub-claim, and (by Step A) the Dichotomy Theorem.
$\blacksquare$

### 7. Periodicity corollary

We now derive the problem's conclusion. Recall $P=\prod_{p\le k}p$
(finite, Section 0).

**Step 1 (residue classes have uniform status).** By the elementary
fact of Section 0, if $n\equiv n'\pmod P$ (both $\ge k$) then $n,n'$ are
similar, so by the Dichotomy Theorem they have the same term-status.
Hence, for each residue $r\in\{0,1,\dots,P-1\}$, **all** integers $n\ge
k$ with $n\equiv r\pmod P$ have the same status; call $r$ *good* if
that common status is "term", and *bad* otherwise.

**Step 2 (terms $=$ union of good classes).** By definition, if $n\ge k$
is a term, then $n\bmod P$ is a good residue (as $n$ itself witnesses
it). Conversely, if $r$ is a good residue, then by Step 1 **every**
integer $\ge k$ congruent to $r\pmod P$ is a term. Hence:
$$\{n\ge k : n\text{ is a term}\}=\{n\ge k: n\bmod P\text{ is good}\}.$$

**Step 3 (the count $T$).** Let $T$ be the number of good residues among
$\{0,1,\dots,P-1\}$. Since $k\bmod P$ is good ($k=a_1$ is a term), $T\ge
1$; and trivially $T\le P$.

**Step 4 (base representatives).** List the good residues, and for each
let $\beta$ be the unique integer in the half-open interval $[k,k+P)$
congruent to that residue mod $P$ (existence and uniqueness: the $P$
integers $k,k+1,\dots,k+P-1$ are a complete residue system mod $P$).
Sort these $T$ base representatives increasingly:
$$k=\beta_1<\beta_2<\cdots<\beta_T<k+P$$
(that $\beta_1=k$: since all $\beta_l\ge k$, and $k$ itself is one of
the $\beta_l$'s as $k\bmod P$ is good, the smallest possible value $k$
is attained, so $\beta_1=k$).

By Step 2, the full set of terms restricted to $[k,\infty)$ (which is
**all** terms, since every $a_i\ge k$) is exactly
$$\{n\ge k : n\text{ is a term}\}=\bigcup_{l=1}^{T}\{\beta_l+jP : j=0,1,2,\dots\}.$$

**Step 5 (sorting the union: the interleaving lemma).** We claim the
sorted enumeration of the right-hand union is
$$\beta_1,\ \beta_2,\ \dots,\ \beta_T,\ \ \beta_1+P,\ \beta_2+P,\ \dots,
\ \beta_T+P,\ \ \beta_1+2P,\ \dots$$
i.e., writing $g_1<g_2<g_3<\cdots$ for the increasing enumeration of the
union, $g_{mT+l}=\beta_l+mP$ for every $m\ge0$ and $l\in\{1,\dots,T\}$
(indices $1$-based).

*Proof.* First, within a fixed "block" $m$, the $T$ values $\beta_1+mP<
\beta_2+mP<\cdots<\beta_T+mP$ are already in increasing order (as
$\beta_1<\cdots<\beta_T$). Second, the largest value of block $m$ is
strictly less than the smallest value of block $m+1$:
$$\beta_T+mP<\beta_1+(m+1)P \iff \beta_T-\beta_1<P,$$
and indeed $\beta_T-\beta_1<P$ because both $\beta_1,\beta_T\in[k,k+P)$,
an interval of length $P$ (so $\beta_T<k+P\le\beta_1+P$, giving
$\beta_T-\beta_1<P$). Since every element of the union lies in exactly
one block (each element $\beta_l+jP$ for $j\ge0$ belongs to block $j$),
and blocks are totally ordered relative to each other (each entirely
below the next), the fully sorted list is obtained by concatenating the
(already sorted) blocks $0,1,2,\dots$ in order — which is precisely
$g_{mT+l}=\beta_l+mP$. $\blacksquare$

**Step 6 (exact periodicity of the merged sequence).** From Step 5, for
every $n\ge1$, writing $n=mT+l$ with $m\ge0$, $1\le l\le T$:
$$g_{n+T}=g_{(m+1)T+l}=\beta_l+(m+1)P=(\beta_l+mP)+P=g_n+P.$$
So $g_{n+T}=g_n+P$ for **every** $n\ge1$.

**Step 7 (identifying $g_n$ with $a_n$).** By Step 2, $\{g_1,g_2,\dots\}$
(the sorted enumeration of the union) equals the set of all terms of
the original sequence. But $(a_n)_{n\ge1}$ is, by its own definition,
*the* strictly increasing enumeration of that same set (each $a_n$ is a
term, and every term equals some $a_n$, by definition of "term"). Since
a set of positive integers has a unique strictly increasing enumeration,
$g_n=a_n$ for every $n\ge1$.

**Conclusion.** Setting
$$T:=\#\{r\in\{0,\dots,P-1\} : r\text{ is a good residue mod }P\},
\qquad L:=P=\prod_{p\le a_1,\ p\text{ prime}}p,$$
we have shown $1\le T\le P$ and, from Step 6–7,
$$a_{n+T}=a_n+L\qquad\text{for every positive integer }n.$$
This is exactly the required conclusion. $\blacksquare$

### 8. Sanity checks (numerical, corroborating but not substituting for the proof above)

All of the following were computed directly (plain Python, exact integer
arithmetic, gcd via the Euclidean algorithm, no external claims taken on
faith) as an end-to-end confirmation that the theorem chain above is
internally consistent with this workspace's own prior certified data and
with fresh test cases:

- **Claim 2**: $20{,}000$ random $(r,s)$ pairs with $rs,r^2s$ in the
  generated range of the $a_1=15$ sequence ($5{,}075$ valid instances):
  zero violations.
- **Claim 3**: exhaustive check of every non-term $n$ in $[15,\text{max
  generated value}/23]$ against every prime $23\le p\le 199$ ($2{,}520$
  instances): zero violations.
- **Main Dichotomy / periodicity mechanism**, checked end-to-end on
  four values of $a_1$ by explicitly computing $P=\prod_{p\le a_1}p$,
  determining every good residue mod $P$ from a directly-generated
  sequence, and verifying $a_{n+T}=a_n+P$ for every available $n$:

  | $a_1$ | $P$ | $T$ |
  |---|---|---|
  | 6 | 30 | 15 |
  | 10 | 210 | 105 |
  | 12 | 2310 | 1155 |
  | 15 | 30030 | 8008 |

  In every case, $a_{n+T}=a_n+P$ held with **zero exceptions** across
  every checked $n$ (thousands of values per case). In particular for
  $a_1=15$: $P=30{,}030=1001\times30$ and $T=8{,}008=1001\times8$ — this
  is a **valid, non-minimal** multiple of this workspace's own
  independently-certified minimal period $(T_0,L_0)=(8,30)$ for
  $a_1=15$ (round-1 result), exactly as the outline-reviewer predicted
  and corrected (the outline's original Step 6 wording, "reproduce
  $T=8,L=30$ exactly," was imprecise — the correct check, done here, is
  that the formula's $(T,L)$ is a positive-integer multiple of the
  certified minimal period, which it is: $L/L_0=P/30=1001$ and
  $T/T_0=8008/8=1001$, the same multiplier). This is consistent because
  the problem only requires existence of *some* valid $T,L$, not
  minimality — the theorem above proves exactly that, and needs no
  further correction.

These checks corroborate the proof but are not load-bearing: the
argument in Sections 1–7 is self-contained and does not depend on any
numerical computation.

### 9. Summary of what was adapted from the crux, and what is new

- Claims 1, 2, 3 and the Main Dichotomy Theorem's proof strategy
  (minimal-counterexample induction, the $p\le k$/$p>k$ case split) are
  translations of IMO Shortlist 2013 N5's official Solution 1 (crux
  `aimo-0030`, verified directly against the problem's own solution
  text retrieved from `past_problems_database.json`), rewritten entirely
  in this problem's own recursive vocabulary (terms/non-terms of
  $(a_n)$) rather than the original "good/bad number" game language, with
  every step re-derived from scratch — including several details the
  official solution states without proof (e.g. that dividing by the
  chosen prime $p$ preserves similarity in both the $p\le k$ and $p>k$
  cases, Section 6 Case (i)/(ii)) — and Claim 1 additionally uses this
  workspace's own already-certified Corollary P″ for a shorter proof
  than the original.
- Lemma REC (Section 1) makes explicit and proves from scratch the
  bridge between the problem's own recursive definition and the
  IN/OUT-style case analysis the official solution's argument
  implicitly relies on (this is the gap flagged by the round-15
  outline-reviewer as missing from the outline; it is fully proved here).
- The periodicity corollary (Section 7) is new content beyond the crux
  (the official solution only needs the Dichotomy for its own literal
  conclusion, part (a) of the shortlist problem; part (b), periodicity
  of the "good/bad" word, is stated in Comment 3 without full proof and
  only up to "the period divides $P$" — our Section 7 gives a complete,
  self-contained, **exact** periodicity proof from $n=1$, with fully
  explicit $T,L$, going beyond what the official solution needed).

### 10. Relation to the rest of this workspace

This proof is entirely self-contained and does **not** use FCBC,
Theorem 5.1, any covering set $H$, Conjecture (JW)/(WCE), Corollary MSF,
or any of the core-decomposition/witness-chaining apparatus built in
rounds 1–14 — it only uses this workspace's Lemma P′/Corollary P″
(already certified, Section 2). That apparatus remains valid and
certified but is no longer needed to establish the problem's stated
conclusion; it remains of independent interest for finer questions (the
*minimal* $T,L$, or the structure of the minimal covering set $H$) that
this problem does not ask about.

## Reviewer verdict (round 15)

**APPROVE — Status confirmed `solved`.** Independently re-derived every
step from scratch (Lemma REC, Corollary P″, Claims 1–3, the Main Dichotomy
Theorem's both cases, and the periodicity corollary's interleaving
argument), cross-checked the crux adaptation against `aimo-0030`'s
official solution text, and ran extensive fresh-code numerical
verification (12 periodicity-table values incl. 8 new, exhaustive
Dichotomy-Theorem signature scans on 5 hard cases incl. `a_1=21528751`
with zero violations, plus Lemma REC/Claim 2 stress tests). Found one
purely cosmetic documentation gap (Claim 2/3's contrapositives need an
explicit domain check `rs\ge k`/`n\ge k` at the point of use in the
Dichotomy Theorem's proof — true and one-line-derivable from already
-stated facts, not a break in validity) and patched it into the certified
lemma write-up (`lemmas/theorem-similarity-dichotomy.md`) and into
`current.md`'s Full proof. No other gap found. This result supersedes the
FCBC/Conjecture-(JW) apparatus for the problem's literal conclusion; see
`current.md` for the full write-up and cross-approach discussion.

## Promotable lemmas

The following are proved in full above and are recommended for
certification into `results/imo-2026-06/lemmas/`:

- **Lemma REC** (Section 1): for $n>k=a_1$, $n$ is a non-term iff there
  is a term $m$ with $k\le m<n$, $\gcd(m,n)=1$. Fully proved from the
  problem's own recursive definition; no other lemma needed.
- **Claim 1** (Section 3, multiple-of-a-term-is-a-term): fully proved,
  cites only Lemma REC + already-certified Corollary P″.
- **Claim 2** (Section 4): $rs\ge k$ non-term $\implies r^2s$ non-term.
  Fully proved, cites only Lemma REC.
- **Claim 3** (Section 5): $p>k$ prime, $n\ge k$ non-term $\implies np$
  non-term. Fully proved (minimal-counterexample argument), cites Lemma
  REC, Claim 1, and Corollary P″.
- **Main Dichotomy Theorem** (Section 6): $n,n'\ge k$ similar
  $\implies$ same term-status. Fully proved, cites Claims 1–3.
- **Interleaving/Periodicity Theorem** (Section 7): explicit $T,L$ with
  $a_{n+T}=a_n+L$ for every $n\ge1$, $L=\prod_{p\le a_1}p$, $T=$ number
  of good residues mod $L$. Fully proved, cites the Dichotomy Theorem.
  This is the theorem that resolves the whole problem.
