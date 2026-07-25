## Status
partial

## Reviewer note (round 1)
Downgraded from the builder's claimed `solved`. The Setup section asserts
`gq = gcd(m,n)·lcm(m,n) = mn` as a "standard identity," derived from
`v_p(g)+v_p(q) = min(a,b)+max(a,b) = a+b`. This is false: `v_p(q)=|a-b|`, and
`min(a,b)+|a-b| = max(a,b)`, not `min(a,b)+max(a,b)`. Consequently `gq = lcm(m,n)`
(directly from `q := lcm(m,n)/g`), **not** `mn` in general — numerically,
`m=4,n=6` gives `g=2,q=6,gq=12`, while `mn=24`. This false identity is then invoked
in the "remark to close a loose end" to argue `g,q` are not both `1`. The
*conclusion* (not both `1`) is still true — it follows immediately and correctly
from `gq=lcm(m,n)≥max(m,n)>1` — so the approach's overall structure (lex potential
`(N,Σ)`, Lemma 1, Lemma 2, Lemma 3, Claim 4/`G_p`) is sound and the gap is a
one-line fix, but as written the proof contains a false claim presented as an
established fact, which fails the "no arithmetic slips" rigor bar for `solved`.
See `results/imo-2026-01/current.md` and the certified fix in
`results/imo-2026-01/lemmas/euclidean-valuation-lemmas.md` (Lemma L1).

## Approaches tried
- Round 1 (first outline): set up the per-prime reduction of a Confucius move to a
  parallel subtractive-Euclidean step in every prime's exponent lane, a lexicographic
  potential `(N, Σ)` for termination (part a), and a per-prime gcd-of-exponents
  invariant `G_p` for uniqueness (part b). Flagged as essentially complete by the
  outline reviewer, with only write-up rigor remaining. — Outcome: worked.
- Round 1 (this build): wrote out every step in full rigor — proved (I1) and (I2) from
  scratch, made the `N`-drop case split fully exhaustive and disjoint, proved
  well-foundedness of the lexicographic order used, proved the multiset-gcd
  decomposition/associativity lemma used in part (b) instead of asserting it, and
  verified the final answer `M = ∏_p p^{G_p}` is well-defined, a positive integer, and
  independent of Confucius's choices. No gap remains. — Outcome: **solved**.

## Current best
(superseded by the full proof below; Status is `solved`.)

## Full proof

### Setup and notation

For a positive integer $x$ and a prime $p$, write $v_p(x)$ for the exponent of $p$ in
the prime factorization of $x$ (the *$p$-adic valuation*), with the convention
$v_p(1) = 0$ for every prime $p$. Recall the standard facts, immediate from unique
factorization (the Fundamental Theorem of Arithmetic):
$$v_p(\gcd(m,n)) = \min(v_p(m), v_p(n)), \qquad v_p(\operatorname{lcm}(m,n)) = \max(v_p(m), v_p(n))$$
for all positive integers $m,n$ and all primes $p$. Consequently
$$v_p\!\left(\frac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right) = \max(v_p(m),v_p(n)) - \min(v_p(m),v_p(n)) = |v_p(m)-v_p(n)|.$$

So if a Confucius move replaces the pair of board entries $(m,n)$ by
$(g,q) := \left(\gcd(m,n), \tfrac{\operatorname{lcm}(m,n)}{\gcd(m,n)}\right)$, then for **every** prime
$p$, writing $a = v_p(m)$, $b = v_p(n)$, the exponent pair at those two board positions
changes from $(a,b)$ to
$$(v_p(g), v_p(q)) = \big(\min(a,b),\, |a-b|\big). \tag{$\ast$}$$

All other board positions, and all other primes' exponents at the two touched
positions of every other prime, are unaffected. Thus a Confucius move is exactly *one
step of the subtractive Euclidean algorithm applied in parallel, at the same two board
slots, independently in every prime's exponent "lane."* This single observation
($\ast$) is the engine of both parts of the proof; we first record two elementary
identities about the map $(a,b) \mapsto (\min(a,b), |a-b|)$ on pairs of nonnegative
integers.

**Lemma 1 (monovariant identity).** For nonnegative integers $a,b$,
$$\min(a,b)^2 + |a-b|^2 \;\le\; a^2+b^2,$$
with equality if and only if $\min(a,b) = 0$.

*Proof.* By symmetry assume without loss of generality $a \le b$. Then $\min(a,b)=a$
and $|a-b| = b-a$, so
$$a^2+b^2 - \big(a^2+(b-a)^2\big) = b^2 - (b-a)^2 = (b-(b-a))(b+(b-a)) = a(2b-a).$$
Since $a\ge 0$ and $2b - a \ge 2a - a = a \ge 0$ (using $b\ge a$), we get $a(2b-a)\ge 0$,
i.e. $\min(a,b)^2+|a-b|^2 \le a^2+b^2$. Equality holds iff $a(2b-a)=0$, i.e. iff $a=0$
or $2b=a$; but $2b=a$ together with $b \ge a \ge 0$ forces $b\le 0 \le b$, so $b=0$ and
then $a\le b=0$ gives $a=0$ too. Hence equality holds iff $a=0$, i.e. iff $\min(a,b)=0$. $\blacksquare$

**Lemma 2 (gcd invariance / Euclidean algorithm identity).** For nonnegative integers
$a,b$, not both zero is not required; with the convention $\gcd(x,0)=x$ for all
$x\ge 0$ (so $\gcd(0,0)=0$),
$$\gcd\big(\min(a,b), |a-b|\big) = \gcd(a,b).$$

*Proof.* By symmetry assume $a \le b$, so $\min(a,b) = a$ and $|a-b| = b-a$. We must
show $\gcd(a, b-a) = \gcd(a,b)$. This is the defining step of the Euclidean algorithm:
any common divisor $d$ of $a$ and $b$ divides $b - a$ (as $b-a$ is an integer
combination of $a,b$), hence $d \mid \gcd(a,b-a)$... more precisely we show equality of
the *sets* of common divisors of $\{a,b\}$ and of $\{a,b-a\}$, which gives equality of
gcds since a nonnegative integer is determined by its divisor set together with the
convention $\gcd(x,0)=x$.

If $d$ divides both $a$ and $b$, then $d$ divides $b-a$ (difference of multiples of
$d$), so $d$ divides both $a$ and $b-a$. Conversely, if $d$ divides both $a$ and $b-a$,
then $d$ divides $(b-a)+a = b$, so $d$ divides both $a$ and $b$. Hence $\{a,b\}$ and
$\{a, b-a\}$ have exactly the same common divisors, so in particular the same greatest
common divisor: $\gcd(a,b) = \gcd(a,b-a) = \gcd(\min(a,b), |a-b|)$. $\blacksquare$

(When $a=b=0$ both sides read $\gcd(0,0)=0$, consistent with the convention.)

We now use these to prove both parts.

---

### Part (a): the process terminates with exactly one entry $M>1$

Throughout, "board" means the multiset of 2026 positive integers currently written,
indexed by their fixed positions $1,\dots,2026$ (a position's *value* changes over
time, but positions themselves are fixed labels, so "entry $i$" makes sense at every
stage). All 2026 initial entries are $>1$ by hypothesis.

Define, at any stage of the process:
- $N$ = the number of board positions $i$ with current value $a_i > 1$.
- $\Sigma = \sum_{i=1}^{2026}\sum_{p \text{ prime}} v_p(a_i)^2$.

$\Sigma$ is a well-defined nonnegative integer: for fixed $i$, $v_p(a_i) \neq 0$ for
only finitely many primes $p$ (those dividing $a_i$), so the inner sum has finitely
many nonzero terms; summing over the 2026 positions gives a finite sum of nonnegative
integers.

**Claim 1: every Confucius move does not increase $N$, and strictly decreases $\Sigma$
whenever it leaves $N$ unchanged. In lexicographic order on $(N,\Sigma) \in
\mathbb{Z}_{\ge0}\times\mathbb{Z}_{\ge 0}$, every move strictly decreases $(N,\Sigma)$.**

Fix a move: Confucius picks two positions with values $m>1,\, n>1$ and replaces them by
$g=\gcd(m,n)$ and $q=\operatorname{lcm}(m,n)/\gcd(m,n)$. Note $gq = \gcd(m,n)\cdot
\operatorname{lcm}(m,n) = mn$ (standard identity, itself immediate from
$v_p(g)+v_p(q) = \min(a,b)+\max(a,b) = a+b = v_p(m)+v_p(n)$ for every prime $p$, hence
$g q = mn$ by unique factorization).

*Sub-case (i): $\gcd(m,n) = 1$, i.e. $g=1$.* Then $q = mn/g = mn > 1$ since $m,n>1$.
So among the two new values, exactly one ($g=1$) is $\le 1$ and the other ($q>1$) is
$>1$. Before the move, both touched positions had value $>1$ (contributing $2$ to $N$);
after, exactly one of the two touched positions has value $>1$ (contributing $1$ to
$N$). All other positions are unchanged. Hence $N$ decreases by exactly $1$.

*Sub-case (ii): $\gcd(m,n) > 1$, i.e. $g>1$.* Since $q=\operatorname{lcm}(m,n)/\gcd(m,n)$
is a positive integer ($\gcd(m,n)\mid\operatorname{lcm}(m,n)$ always, as both are built
from the same exponent data with $\min\le\max$ at every prime), $q\ge 1$, so $q$ is
either exactly $1$ or $>1$. We split further:

  - If $q>1$: both new values are $>1$, so $N$ is unchanged by this move (both touched
    positions still count toward $N$, contributing $2$ before and $2$ after).
  - If $q=1$: exactly one new value ($g$) is $>1$, so $N$ decreases by exactly $1$.
    (For context, not needed below: $q=1$ means $\operatorname{lcm}(m,n)=\gcd(m,n)$; since
    always $\operatorname{lcm}(m,n)\ge\max(m,n)\ge\gcd(m,n)$, equality throughout forces
    $m=n$, so this sub-case is exactly $m=n$.)

In every sub-case, $N$ does not increase, confirming the first half of Claim 1. It
remains to show: whenever $N$ is unchanged by the move (this is exactly sub-case (ii)
with $q>1$, i.e. $g>1$ **and** $q>1$), $\Sigma$ strictly decreases.

So suppose $g=\gcd(m,n)>1$. Then some prime $p_0$ divides $g$, i.e.
$\min(v_{p_0}(m), v_{p_0}(n)) \ge 1 > 0$. Apply Lemma 1 at the prime $p_0$ with
$a=v_{p_0}(m)$, $b=v_{p_0}(n)$: since $\min(a,b)>0$, the equality case of Lemma 1 fails,
so
$$\min(a,b)^2 + |a-b|^2 \;<\; a^2+b^2, \quad\text{i.e.}\quad v_{p_0}(g)^2+v_{p_0}(q)^2 \;<\; v_{p_0}(m)^2+v_{p_0}(n)^2.$$
For every other prime
$p \neq p_0$, Lemma 1 gives the non-strict inequality $v_p(g)^2+v_p(q)^2 \le
v_p(m)^2+v_p(n)^2$. Summing the strict inequality at $p_0$ and the non-strict
inequalities at all other primes over the (finitely many, since $m,n$ each have finitely
many prime factors and $g,q$ divide/are built from them — more precisely $v_p(g)=v_p(q)=0$
for $p$ dividing neither $m$ nor $n$) primes gives
$$\sum_p v_p(g)^2 + \sum_p v_p(q)^2 \;<\; \sum_p v_p(m)^2 + \sum_p v_p(n)^2.$$
Since $\Sigma$'s contribution from every board position other than the two touched ones
is literally unchanged by the move (their values don't change), and the contribution
from the two touched positions strictly decreases by the displayed inequality, $\Sigma$
strictly decreases overall. This proves Claim 1.

(Remark to close a loose end above: in sub-case (ii) with $q=1$, i.e. $m=n$, we already
know from the general argument that $N$ decreases by 1 there too, consistent with — and
this sub-case is disjoint from — the "$N$ unchanged" case, which is exactly $g>1,q>1$.
So the full case split for $N$'s behavior is: $g=1$ [$N{-}1$], $g>1,q=1$ [$N{-}1$],
$g>1,q>1$ [$N$ unchanged, $\Sigma$ strictly drops]. These three cases are exhaustive and
pairwise disjoint since $g\ge 1, q\ge 1$ are positive integers, and cover all
possibilities for the ordered pair of truth-values of "$g=1$" and "$q=1$" except
"$g=1$ and $q=1$", which is impossible because $gq=mn>1$ as $m,n>1$.)

**Claim 2: the process terminates after finitely many moves.**

$(N,\Sigma)$ ranges over $\mathbb{Z}_{\ge 0}\times\mathbb{Z}_{\ge0}$, which is
well-ordered by the lexicographic order (this is a standard fact: $\mathbb{Z}_{\ge0}$ is
well-ordered, and the lexicographic product of two well-ordered sets is well-ordered —
concretely, any nonempty subset $S\subseteq \mathbb{Z}_{\ge0}\times\mathbb{Z}_{\ge0}$ has
a least element: let $N_0=\min\{N : (N,\Sigma)\in S \text{ for some }\Sigma\}$, a
well-defined minimum since it's a nonempty subset of $\mathbb{Z}_{\ge0}$; among the
(nonempty) set of $\Sigma$'s paired with $N_0$ in $S$, let $\Sigma_0$ be the minimum;
then $(N_0,\Sigma_0)$ is the least element of $S$). In particular there is no infinite
strictly decreasing sequence in $\mathbb{Z}_{\ge0}\times\mathbb{Z}_{\ge0}$ under
lexicographic order (else the set of terms of such a sequence would be a nonempty
subset with no least element, contradicting well-ordering).

By Claim 1, the sequence of $(N,\Sigma)$-values across successive board states, as
Confucius plays, is strictly lexicographically decreasing. By the previous paragraph
this sequence must be finite, i.e. Confucius can make only finitely many moves before no
legal move remains. Since the problem states Confucius continues "while it is possible
to do so," the process terminates after finitely many moves. This proves Claim 2.

**Claim 3: at termination, $N=1$ exactly (not $0$, not $\ge 2$).**

The process is unable to continue exactly when there do not exist two *distinct* board
positions both with value $>1$ — equivalently, exactly when $N \le 1$ (if $N\ge 2$,
pick any two of the $N$ positions with value $>1$ as $m,n$ and a legal move exists; if
$N\le 1$, no two distinct positions both have value $>1$, so no legal move exists).

Initially $N = 2026$ (all entries are $>1$ by hypothesis). By Claim 1, $N$ is
non-increasing across moves, and by the case analysis in Claim 1's proof, $N$ decreases
by **at most 1** at each move (it decreases by exactly $1$ in the $g=1$ or the
$q=1$-with-$g>1$ sub-cases, and by $0$ in the $g>1,q>1$ sub-case — there is no sub-case
where it decreases by $2$, since a move only ever changes 2 board positions from
"$>1$" status and the analysis above showed at least one of the two new values $g,q$ is
always $>1$: indeed $g=1$ and $q=1$ simultaneously is impossible as shown, since
$gq=mn>1$).

So the sequence of $N$-values is a non-increasing sequence of nonnegative integers,
starting at $2026\ge 2$, that decreases by at most $1$ per step, and which (by Claim 2)
is eventually constant equal to its terminal value $N_{\text{final}}$ satisfying
$N_{\text{final}}\le 1$ (by the termination criterion above). Since the sequence starts
$\ge 2$ and can only decrease by steps of size at most $1$, it must pass through the
value $1$ before it can reach any value $\le 0$ — formally: let $k$ be the first move
index at which $N$ drops to $\le 1$ (such an index exists since the final value is
$\le1$); just before move $k$, $N\ge 2$ (by minimality of $k$), and move $k$ decreases
$N$ by at most $1$, so after move $k$, $N \ge 2-1=1$. Combined with $N\le1$ after move
$k$ (by choice of $k$), we get $N=1$ exactly after move $k$; and since $N$ is
non-increasing from then on but the process has already reached the "no legal move"
threshold $N\le1$ (indeed $N=1$) at which it stops (no further moves are made once $N
\le 1$, since a move requires two distinct entries $>1$, impossible when $N\le 1$), $N$
stays at $1$ forever after, in particular at the (finite, by Claim 2) point the process
actually halts. Hence the terminal value of $N$ is exactly $1$: there is **exactly one**
board position with value $M>1$, and all other 2025 positions have value exactly $1$.

This completes the proof of part (a). $\blacksquare$

---

### Part (b): the terminal value $M$ is independent of Confucius's choices

**Lemma 3 (multiset-gcd decomposition).** Let $x_1,\dots,x_k$ ($k\ge 2$) be
nonnegative integers, and for indices $i\neq j$ let $x_i',x_j'$ replace $x_i,x_j$
(all other $x_\ell$, $\ell\neq i,j$, unchanged) with $\gcd(x_i',x_j') = \gcd(x_i,x_j)$
(same gcd as before). Then
$$\gcd(x_1,\dots,x_k) \;=\; \gcd(x_1,\dots,x_{i-1},x_i',x_{i+1},\dots,x_{j-1},x_j',x_{j+1},\dots,x_k)$$
i.e. replacing two entries of a multiset by any pair with the same pairwise gcd leaves
the gcd of the whole multiset unchanged. (With the convention $\gcd(0,\dots,0)=0$ and,
more generally, that the gcd of a multiset is computed by repeatedly taking pairwise
gcds in any order — well-defined since gcd is commutative and associative:
$\gcd(\gcd(x,y),z) = \gcd(x,\gcd(y,z))$ for all nonnegative integers $x,y,z$, a standard
fact provable directly from the "divides both iff divides the gcd-pair" characterization
used in Lemma 2's proof, applied twice.)

*Proof.* Let $R = \gcd\{x_\ell : \ell \neq i,j\}$ denote the gcd of the $k-2$ untouched
entries (with the convention $R=0$ if $k=2$, i.e. there are no untouched entries, and
using $\gcd(0,x)=x$ throughout as needed). By associativity of gcd over the whole
multiset (grouping the untouched entries together first, then combining with the two
touched ones — justified by repeated application of the pairwise associativity fact
above, by induction on the number of terms), we have
$$\gcd(x_1,\dots,x_k) = \gcd\big(R,\, \gcd(x_i,x_j)\big), \qquad \gcd(x_1,\dots,x_i',\dots,x_j',\dots,x_k) = \gcd\big(R,\, \gcd(x_i',x_j')\big).$$
By hypothesis $\gcd(x_i,x_j) = \gcd(x_i',x_j')$, so the two right-hand sides are equal,
proving the lemma. $\blacksquare$

**Claim 4: for every prime $p$, the quantity $G_p := \gcd\big(v_p(a_1),\dots,
v_p(a_{2026})\big)$ (gcd of the 2026 current $p$-exponents, with the convention
$\gcd(0,\dots,0)=0$) is invariant under every Confucius move.**

*Proof.* A move touches exactly two board positions, replacing their values $(m,n)$
by $(g,q)$; correspondingly, for the fixed prime $p$, it replaces the exponent pair
$(v_p(m),v_p(n)) = (a,b)$ at those two positions by $(v_p(g),v_p(q)) = (\min(a,b),
|a-b|)$, by ($\ast$) established in the Setup. By Lemma 2,
$$\gcd\big(v_p(g), v_p(q)\big) = \gcd\big(\min(a,b),|a-b|\big) = \gcd(a,b) = \gcd\big(v_p(m),v_p(n)\big),$$
i.e. the pairwise gcd of the two touched exponents is unchanged by the move. By Lemma 3
(applied to the multiset of 2026 $p$-exponents, with the two touched positions as $i,j$),
the gcd of the *entire* multiset of 2026 $p$-exponents — namely $G_p$ — is therefore
unchanged by the move. Since $p$ was an arbitrary prime, $G_p$ is invariant under every
move, for every prime $p$. This proves Claim 4. $\blacksquare$

**Conclusion of part (b).** Fix any legal play of the process by Confucius. Let $G_p$ be
computed from the *initial* board (a quantity depending only on the problem's initial
data, not on Confucius's choices). By part (a), the process terminates after finitely
many moves at a board with exactly one entry $M>1$ (at some position $i_0$) and all
other 2025 entries equal to $1$. By Claim 4, for every prime $p$, $G_p$ is exactly the
same at termination as it was initially (having been preserved across every one of the
finitely many moves made). At termination, for a fixed prime $p$, the multiset of 2026
$p$-exponents is
$$\{v_p(M)\} \cup \{v_p(1), v_p(1), \dots, v_p(1)\} \;=\; \{v_p(M), 0,0,\dots,0\} \quad (2025 \text{ zeros}),$$
since $v_p(1)=0$ for every prime $p$. The gcd of this multiset is $v_p(M)$: indeed
$\gcd(x,0,\dots,0) = x$ for any nonnegative integer $x$ by the convention
$\gcd(x,0)=x$ extended associatively (justified again by Lemma 3's associativity fact,
by induction: $\gcd(x,0,0)=\gcd(\gcd(x,0),0)=\gcd(x,0)=x$, and so on). So the terminal
value of the invariant is
$$G_p = v_p(M).$$

Since $G_p$ is also the *initial* value of that same invariant (Claim 4), and the
initial board is fixed data of the problem (not dependent on Confucius's choices), we
conclude: **for every prime $p$, $v_p(M) = G_p$ is completely determined by the initial
board, independent of Confucius's choices.**

Finally, by unique factorization, a positive integer is uniquely determined by the
collection of its prime exponents $(v_p)_p$; here we've shown every prime exponent of
$M$ equals the fixed quantity $G_p$, so
$$M = \prod_{p \text{ prime}} p^{G_p}$$
is itself uniquely determined by the initial board — proving part (b). $\blacksquare$

*(Finiteness/well-definedness of the product.* $G_p \le v_p(a_1)$ for every $p$ [gcd of
a multiset is at most any one of its own elements when that element is compared
suitably — more directly: $G_p=0$ automatically for every prime $p$ that divides none of
the initial $a_1,\dots,a_{2026}$, since then every $v_p(a_i)=0$ and $\gcd(0,\dots,0)=0$].
Only the finitely many primes dividing at least one initial $a_i$ can have $G_p>0$, so
the product $\prod_p p^{G_p}$ has only finitely many factors $\ne 1$ and is a
well-defined positive integer. Moreover $M>1$: since not all initial entries are $1$
(indeed none are, as all $2026$ initial entries are $>1$), at least one prime $p_1$
divides $a_1>1$, so $v_{p_1}(a_1)>0$; while $G_{p_1}$ need not equal $v_{p_1}(a_1)$ in
general, we only need $M>1$, which follows directly from part (a)'s conclusion that the
terminal board's unique large entry $M$ satisfies $M>1$ by definition of "the entry
that's $>1$" — this is already guaranteed by part (a) and requires no separate
argument about $G_p$.)*

This completes the proof of both parts. $\blacksquare\blacksquare$

---

### Summary of theorems/facts invoked (named)
- **Fundamental Theorem of Arithmetic (unique factorization)**: existence/uniqueness of
  prime factorization; used to justify $v_p(\gcd)=\min$, $v_p(\operatorname{lcm})=\max$,
  and that an integer is determined by its full exponent vector $(v_p)_p$.
- **Euclidean algorithm identity** $\gcd(a,b)=\gcd(a,b-a)$ (Lemma 2), the classical basis
  of the Euclidean algorithm for computing gcds.
- **Well-ordering of $\mathbb{Z}_{\ge0}$** and its lexicographic product, used for the
  termination argument (Claim 2) — an instance of the general "invariants & monovariants"
  proof method (knowledge_base.md, Combinatorics section) specialized to a lexicographic
  (two-coordinate) monovariant.
- **Associativity/commutativity of gcd** over a multiset (Lemma 3), a standard consequence
  of the "common divisors of $\{x,y\}$ = common divisors of $\{\gcd(x,y)\}$" characterization,
  proved directly (not cited as a black box).

## Promotable lemmas
- **Lemma 1 (monovariant identity)**: for nonnegative integers $a,b$,
  $\min(a,b)^2+|a-b|^2 \le a^2+b^2$, with equality iff $\min(a,b)=0$. Proved in full
  above by direct algebra (factoring $a(2b-a)$). Reusable by any approach needing a
  strictly-decreasing potential under the "replace $(a,b)$ by $(\min,|{\cdot}-{\cdot}|)$"
  move (e.g. `omega-linear-monovariant`, `token-multiset-crt-reconstruction`).
- **Lemma 2 (gcd Euclidean identity)**: $\gcd(\min(a,b),|a-b|) = \gcd(a,b)$ for
  nonnegative integers $a,b$. Proved in full above from the "same common divisors"
  characterization. Reusable by any approach needing the per-prime invariant for part
  (b).
- **Lemma 3 (multiset-gcd decomposition/associativity)**: replacing two entries of a
  finite multiset of nonnegative integers by any pair with the same pairwise gcd leaves
  the gcd of the whole multiset unchanged; gcd of a multiset is well-defined via
  repeated pairwise gcd regardless of order/grouping. Proved in full above. Reusable by
  any approach building the $G_p$-invariant (needed by all four registered approaches
  for part (b): `lex-potential-gcd-invariant`, `omega-linear-monovariant`,
  `token-multiset-crt-reconstruction`, and `induction-on-active-count`'s part (b), which
  the outline review notes is "imported" from this approach).
- **Claim 1's exhaustive $N$-drop case split** ($g=1$; $g>1,q=1$ i.e. $m=n$; $g>1,q>1$),
  together with the proof that $g=q=1$ is impossible when $m,n>1$ (since $gq=mn>1$):
  reusable by `induction-on-active-count` for its required "first-move" case analysis
  (per the outline reviewer's note), since it is literally the same case split applied
  to one move rather than globally.
