## Status
solved

## Approaches tried
- Round 1 (outline): sketched strong induction on `k`, the number of board
  entries `>1` ("active" entries), with a two-entry sub-lemma as the reduction
  gadget. Self-flagged gap: the write-up only proved termination for the
  strategy "isolate and fully resolve one pair before starting another," which
  is an *existence* argument, not the *universal* statement the problem asks
  for (termination "regardless of the choices of Confucius").
- Round 1 (outline-reviewer): confirmed the gap is real but fixable without
  abandoning the induction-on-`k` framing, via inducting on the *first move of
  an arbitrary sequence* rather than assuming a strategy shape. The reviewer's
  sketch of the case split ("gcd = 1 drops active count by 2, gcd > 1 drops it
  by 1") turns out to contain an arithmetic slip — worked out in full below,
  the correct dichotomy is "drops by 1" vs. "stays the same," and the "stays
  the same" case (e.g. `m=4,n=6 \mapsto (2,6)`, both still `>1`) cannot be
  ruled out by active count alone. This build closes the gap fully by pairing
  the induction on `k` with a *second*, bounded quantity `\Sigma` that strictly
  decreases whenever the active count is preserved, and proving the resulting
  two-level (nested) strong induction is well-founded from first principles
  (no black-box citation of lexicographic well-ordering). This is a complete,
  self-contained fix: **every** legal move, regardless of which pair Confucius
  picks and regardless of interleaving, is shown to strictly decrease the pair
  `(k,\Sigma)` in the sense made precise below, and this alone (plus a short
  induction) suffices for termination with exactly one survivor. Part (b) is
  proved from scratch (not merely imported) since no certified lemma file
  exists yet for this problem.
- Outcome: gap closed, both parts proved in full — see Full proof below.

## Current best
Superseded by the Full proof below (Status: solved).

## Full proof

Throughout, the blackboard is modeled as a fixed set of `2026` **positions**
`1,\dots,2026`; a *board* `B` is an assignment of a positive integer to each
position. Call a position **active** in `B` if its entry is `>1`. A **legal
move** on `B` picks two distinct active positions `i\neq j$ with entries
`m,n>1`, and produces the board `B'` that agrees with `B` outside `\{i,j\}`
and has, at `\{i,j\}` (in either order), the values
$$g=\gcd(m,n), \qquad q=\operatorname{lcm}(m,n)/\gcd(m,n).$$
A move is possible on `B` iff `B` has at least two active positions. Confucius
plays a **maximal sequence** of legal moves: he keeps playing while a legal
move exists, by hypothesis of the problem ("continues to make moves while it
is possible to do so"); we must show every such sequence, for every possible
sequence of pair-choices, is finite, ends with exactly one active position,
and that the surviving value `M` there is the same for every such sequence.

### 0. The per-prime reduction (elementary number theory)

Fix a prime `p`. For a positive integer `x`, `v_p(x)` denotes its `p`-adic
valuation. Two standard facts about `\gcd` and `\operatorname{lcm}`, both
immediate from unique factorization (Fundamental Theorem of Arithmetic):
for all positive integers `m,n`,
$$v_p(\gcd(m,n)) = \min(v_p(m),v_p(n)), \qquad v_p(\operatorname{lcm}(m,n)) = \max(v_p(m),v_p(n)).$$
Since `\gcd(m,n)` divides `m`, hence divides `\operatorname{lcm}(m,n)`, the
quotient `q=\operatorname{lcm}(m,n)/\gcd(m,n)` is a positive integer, and
$$v_p(q) = v_p(\operatorname{lcm}(m,n)) - v_p(\gcd(m,n)) = \max(v_p(m),v_p(n)) - \min(v_p(m),v_p(n)) = |v_p(m)-v_p(n)|.$$

So, writing `a=v_p(m)`, `b=v_p(n)`, a legal move replaces the exponent pair
`(a,b)` **simultaneously for every prime `p`** by
$$(v_p(g),v_p(q)) = (\min(a,b), |a-b|). \tag{$\ast$}$$
This is one step of the subtractive Euclidean algorithm run in parallel across
all "prime lanes." We record the two identities that drive the whole proof.

**Lemma I1 (monovariant inequality).** For nonnegative integers `a,b`,
$$\min(a,b)^2 + |a-b|^2 \;\le\; a^2+b^2,$$
with equality if and only if `\min(a,b)=0`.

*Proof.* By symmetry assume `a\le b`. Then `\min(a,b)=a` and `|a-b|=b-a`, so
$$a^2+b^2 - \big(a^2+(b-a)^2\big) = b^2-(b-a)^2 = \big(b-(b-a)\big)\big(b+(b-a)\big) = a(2b-a).$$
Since `0\le a\le b`, we have `2b-a \ge 2a-a = a \ge 0`, so `a(2b-a)\ge 0`,
giving the inequality. If `a=0` the difference is `0\cdot(2b)=0`, equality. If
`a>0`, then `2b-a\ge b \ge a>0`, so `a(2b-a)>0`, strict inequality. Hence
equality holds exactly when `a=0=\min(a,b)`. $\blacksquare$

**Lemma I2 (gcd invariance under one Euclidean step).** For nonnegative
integers `a,b`,
$$\gcd(\min(a,b),|a-b|) = \gcd(a,b)$$
(with the convention `\gcd(0,0)=0`, `\gcd(x,0)=\gcd(0,x)=x`).

*Proof.* If `a=b`, both sides are `\gcd(a,a)... ` — handle directly: if `a=b`
then `\min(a,b)=a`, `|a-b|=0`, and `\gcd(a,0)=a=\gcd(a,a)`(taking `\gcd(a,a)=a`
by definition of gcd of two equal numbers, consistent for `a=0` too under our
convention). Now assume `a\ne b`; by symmetry assume `a<b`, so
`\min(a,b)=a`, `|a-b|=b-a`. We show `\gcd(a,b-a)=\gcd(a,b)` by showing the two
pairs have identical sets of common divisors. If `d\mid a` and `d\mid b`, then
`d\mid (b-a)`, so `d` is a common divisor of `a,b-a`. Conversely if `d\mid a`
and `d\mid(b-a)`, then `d\mid \big((b-a)+a\big)=b`, so `d` is a common divisor
of `a,b`. Hence `\{a,b\}` and `\{a,b-a\}` have the same common divisors, so
the same greatest common divisor. $\blacksquare$

**Lemma L1 ("not both trivial").** If `m,n>1`, then `g=\gcd(m,n)` and
`q=\operatorname{lcm}(m,n)/\gcd(m,n)` are not both equal to `1`.

*Proof.* By definition `g\cdot q = \gcd(m,n)\cdot\big(\operatorname{lcm}(m,n)/\gcd(m,n)\big) = \operatorname{lcm}(m,n)`.
Since `m` divides `\operatorname{lcm}(m,n)`, we have `\operatorname{lcm}(m,n)\ge m>1`. So
`g\cdot q = \operatorname{lcm}(m,n) > 1`, which is impossible if `g=q=1` (as `1\cdot1=1`).
$\blacksquare$

### 1. Two global quantities

For a board `B`, let
$$k(B) = \#\{\text{active positions of } B\}\ \in\{0,1,\dots,2026\},$$
$$\Sigma(B) = \sum_{i=1}^{2026}\ \sum_{p\ \text{prime}} v_p\big(B(i)\big)^2.$$

`\Sigma(B)` is a well-defined nonnegative integer: for each fixed position
`i`, by the Fundamental Theorem of Arithmetic `B(i)` has only finitely many
prime divisors, so `v_p(B(i))^2` is nonzero for only finitely many `p`; summing
this finite quantity over the `2026` positions gives a finite sum.

### 2. The Single-Move Lemma (handles an arbitrary move, arbitrary pair choice)

This is the step that removes the "strategy-shape" assumption from the round-1
draft: it is a statement about **one legal move on one board**, true no matter
which two active positions Confucius chooses and no matter what has happened
before or will happen after.

**Lemma SM (Single-Move Lemma).** Let `B` be a board with `k(B)\ge 2`, and let
`B'` be the board obtained from `B` by any one legal move. Then exactly one of
the following holds:

- **(Drop)** `k(B') = k(B)-1`, or
- **(Stall)** `k(B') = k(B)` and `\Sigma(B') < \Sigma(B)`.

In particular `k(B')\in\{k(B)-1,k(B)\}` always (the active count never
increases and never drops by more than `1`), and `\Sigma(B')\le \Sigma(B)`
always (with strict decrease forced whenever the active count does not drop).

*Proof.* Say the move is applied to positions `i\ne j` with entries `m,n>1`,
producing `g,q` at `i,j` and leaving all other positions unchanged. Since only
positions `i,j` change, and `m,n` were both active (contributing `2` to
`k(B)`), we have
$$k(B') - k(B) = \#\{x\in\{g,q\}: x>1\} - 2.$$
By Lemma L1, not both `g,q` equal `1`, so `\#\{x\in\{g,q\}:x>1\}\in\{1,2\}`.
This gives the two cases:

- If exactly one of `g,q` is `>1` (i.e. the other equals `1`): `k(B')=k(B)-1`.
  This happens precisely when `\gcd(m,n)=1$ (then `g=1,q=\operatorname{lcm}(m,n)/1 = mn/1\cdot$
  — more precisely `q=\operatorname{lcm}(m,n)>1$ since `\operatorname{lcm}(m,n)\ge m>1`), or when `q=1`,
  i.e. `\operatorname{lcm}(m,n)=\gcd(m,n)`, which forces `m=n` (since always
  `\gcd(m,n)\mid m,n\mid \operatorname{lcm}(m,n)`, equality of the two ends forces `m=n`),
  giving `g=m=n>1`.
- If both `g,q>1`: `k(B')=k(B)`. By definition of `g`, `g=\gcd(m,n)>1` means
  some prime `p` divides both `m,n`, i.e. `\min(v_p(m),v_p(n))>0` for that `p`.

We now verify `\Sigma` behaves as claimed. Write `\Delta_p := v_p(g)^2+v_p(q)^2
- v_p(m)^2-v_p(n)^2` for the change in the `p`-lane contribution of positions
`i,j` (all other positions/lanes are untouched, so they contribute `0` to
`\Sigma(B')-\Sigma(B)`). By identity `(\ast)` and Lemma I1 (applied with
`a=v_p(m),b=v_p(n)`), `\Delta_p \le 0` for **every** prime `p`, with `\Delta_p<0`
exactly for those `p` with `\min(v_p(m),v_p(n))>0`, i.e. `p\mid\gcd(m,n)`. Hence
$$\Sigma(B')-\Sigma(B) = \sum_p \Delta_p \ \le\ 0,$$
always (proving `\Sigma(B')\le\Sigma(B)$ unconditionally), and this sum is
**strictly** negative whenever at least one term `\Delta_p<0`, i.e. whenever
`\gcd(m,n)>1` (some prime divides it). In the Stall case we showed `g>1`, i.e.
`\gcd(m,n)>1`, so `\Sigma` strictly decreases there. This proves the Lemma.
$\blacksquare$

(Two remarks the reader may cross-check against the round-1 sketch: (i) the
active count can only drop by `0` or `1` per move — it can *never* drop by
`2` — because Lemma L1 forbids both `g,q` from being `1` simultaneously; the
round-1 outline-review's suggestion that "`gcd(m,n)=1` drops the active count
by `2`" was a slip, corrected here. (ii) The Stall case is realized, e.g.
`m=4,n=6`: `\gcd(4,6)=2`, `\operatorname{lcm}(4,6)/\gcd(4,6)=12/2=6`, so `(g,q)=(2,6)`, both
`>1`, and indeed `k` is unchanged — this is exactly why the active count alone
cannot serve as the induction's sole decreasing quantity, and why `\Sigma` is
genuinely needed as a second ingredient.)

### 3. Part (a): termination with exactly one survivor, for every sequence of moves

We prove, by **strong induction on the active count `k`**, the following
statement — note it quantifies over *every* sequence of legal moves, not a
particular strategy, which is exactly what closes the round-1 gap.

**Theorem P(k).** For every board `B` with `k(B)=k`, there is no infinite
sequence of legal moves starting at `B`; consequently every maximal sequence
of legal moves starting at `B` (i.e. one that is continued exactly as long as
a legal move exists) is finite, and its terminal board `B^\*` satisfies
`k(B^\*) = 1` if `k\ge1`, and `k(B^\*)=0` if `k=0`.

*Base cases `k=0` and `k=1`.* If `k(B)\in\{0,1\}` there are fewer than two
active positions, so no legal move exists on `B` at all. The (unique) maximal
sequence of legal moves from `B` is the empty sequence, of length `0`
(certainly finite), with terminal board `B^\*=B`, so `k(B^\*)=k(B)=k`,
matching the claim (`f(0)=0`, `f(1)=1`).

*Inductive step, `k\ge 2`.* Assume `P(k')` holds for every `k'<k` (strong
induction hypothesis). We prove `P(k)` by a **second, nested strong induction,
this time on `\Sigma(B)`** for boards `B` with `k(B)=k` fixed; this is where
Lemma SM's "Stall" case is absorbed. Concretely we prove:

**Claim Q(s):** for every board `B` with `k(B)=k` and `\Sigma(B)=s`, there is
no infinite sequence of legal moves starting at `B`, and every maximal such
sequence is finite with terminal active count `1`.

Strong induction on the nonnegative integer `s`.

Let `B` have `k(B)=k\ge2`, `\Sigma(B)=s`, and suppose `Q(s')` holds for every
`s'<s` (this is now inner strong induction, nested inside the outer induction
on `k`, with the outer hypothesis `P(k')$, `k'<k`, also available throughout).
Let `\sigma` be **any** sequence of legal moves starting at `B` — arbitrary,
not assumed to follow any particular strategy. Since `k(B)=k\ge2`, at least
one legal move exists, so if `\sigma` is nonempty its first move, `\mathrm{Move}_1`,
is applied to *some* pair of active positions (Confucius's arbitrary choice)
producing a board `B_1`. By Lemma SM (applied to this single move — the lemma
places no restriction on which pair was chosen), exactly one of:

- **(Drop)** `k(B_1)=k-1`. Then `k(B_1)<k`, so by the outer induction
  hypothesis `P(k-1)` (legitimate: `k-1<k`), there is no infinite sequence of
  legal moves starting at `B_1`, and every maximal such sequence from `B_1`
  ends with active count `f(k-1)=1` (since `k-1\ge1$ as `k\ge2`). The tail
  `\sigma'=(\mathrm{Move}_2,\mathrm{Move}_3,\dots)` of `\sigma` is exactly such a
  sequence of legal moves starting at `B_1` (legality of each `\mathrm{Move}_{i}$,
  `i\ge2`, on the board reached after `i-1$ moves is part of the hypothesis
  that `\sigma$ is a sequence of legal moves). By `P(k-1)`, `\sigma'` is
  finite, so `\sigma = (\mathrm{Move}_1)\frown\sigma'` is finite; and `\sigma` is
  maximal (no further legal move after its last entry) exactly when `\sigma'`
  is maximal for `B_1` (these are literally the same condition, since
  maximality only depends on whether a legal move exists at the final board
  reached, and `\sigma,\sigma'` reach the same final board), in which case the
  terminal active count is `1` by `P(k-1)`.

- **(Stall)** `k(B_1)=k` and `\Sigma(B_1) < s`. Then `B_1` has `k(B_1)=k$ (same
  as `B`) and `\Sigma(B_1)=s_1<s`. By the inner induction hypothesis
  `Q(s_1)` (legitimate: `s_1<s`, and `Q` is being proved by induction on `s`
  for the fixed outer value `k`), there is no infinite sequence of legal
  moves starting at `B_1`, and every maximal such sequence from `B_1` ends
  with active count `1`. Exactly as in the Drop case, the tail
  `\sigma'=(\mathrm{Move}_2,\dots)` is such a sequence starting at `B_1`, so
  `\sigma'$ is finite, hence `\sigma$ is finite, and if `\sigma` is maximal
  then so is `\sigma'` and it terminates with active count `1`.

In both cases `\sigma` is finite, and if maximal it ends at active count `1`.
If `\sigma$ is empty (only possible in principle if no legal move exists on
`B`, but `k(B)=k\ge2` guarantees one does, so this case does not occur), there
is nothing to prove. This establishes `Q(s)` for the given `k`, completing the
inner induction, hence `Q(s)` holds for every `s\ge0` with `k(B)=k` fixed, which
is exactly the statement `P(k)$ restricted to boards of active count `k`.
This completes the outer induction, so `P(k)` holds for every `k\ge0`. $\blacksquare$

**Remark on well-foundedness.** The two nested inductions above are precisely
an elementary, self-contained proof that the pair `(k(B_i),\Sigma(B_i))`,
tracked along any sequence of legal moves `B=B_0,B_1,B_2,\dots`, cannot decrease
forever, without invoking lexicographic well-ordering of `\mathbb N\times\mathbb N`
as a black box: the outer induction on `k` handles all moves that drop the
active count (finitely many, since `k` is a nonnegative integer that never
increases), and for each fixed value of `k` the inner induction on `\Sigma`
handles all moves that *stall* at that `k`-level (finitely many, since
`\Sigma` is a nonnegative integer that strictly decreases on every such move,
by Lemma SM). No move is left unaccounted for, and no assumption is made
about *which* pair of active positions is chosen at any step — this is
exactly the fix requested for the round-1 gap: induction proceeds move-by-move
along an arbitrary sequence, not along a fixed "resolve one pair, then the
next" strategy.

**Application to the problem.** The initial board `B^{(0)}` has all `2026`
entries `>1$ (given), so `k(B^{(0)})=2026\ge1`. By `P(2026)`, Confucius's play
(which is, by the problem's own rule "continues to make moves while it is
possible to do so," a maximal sequence of legal moves) is finite and
terminates at a board with **exactly one** active position. This proves part
(a) completely: after finitely many moves, exactly one integer `M>1` remains
on the board, regardless of Confucius's choices at every step.

### 4. Part (b): the survivor `M` is independent of Confucius's choices

For each prime `p`, define
$$G_p \;=\; \gcd\big(v_p(a_1),\dots,v_p(a_{2026})\big),$$
the gcd of the `p`-adic valuations of the `2026$ initial board entries
`a_1,\dots,a_{2026}` (with the convention, as in Lemma I2, that
`\gcd(0,\dots,0)=0` and `\gcd` of a multiset containing at least one positive
value ignores the zeros, i.e. equals the ordinary gcd of the positive entries
present — this is the standard extension of gcd to include `0` as an
identity element, consistent with `\gcd(x,0)=x`).

**Lemma GP (invariance of `G_p`).** For every prime `p`, the quantity
`G_p(B) := \gcd\big(v_p(B(1)),\dots,v_p(B(2026))\big)` is unchanged by every
legal move: if `B'` is obtained from `B` by one legal move, `G_p(B')=G_p(B)`
for every prime `p`.

*Proof.* Fix `p` and let the move act on positions `i\ne j`, entries `m,n`,
producing `g,q` per `(\ast)`: `v_p(g)=\min(a,b)$, `v_p(q)=|a-b|$ where
`a=v_p(m)`, `b=v_p(n)`. All other positions' `p`-valuations are unchanged. Let
`R` denote the multiset of `p`-valuations at the `2024` positions other than
`i,j` (identical for `B` and `B'`), and let `r=\gcd(R)` (with `r=0` if `R` is
all zero, per convention). By the standard fact that gcd distributes over
concatenation of multisets — `\gcd(R\cup\{a,b\}) = \gcd\big(\gcd(R),a,b\big) =
\gcd\big(r,\gcd(a,b)\big)` — which follows directly from the definition of gcd
as the greatest common divisor of a set (a common divisor of `R\cup\{a,b\}` is
exactly a common divisor of `r` and of `\{a,b\}`, i.e. a common divisor of `r`
and `\gcd(a,b)`, and the largest such is `\gcd(r,\gcd(a,b))`), we get
$$G_p(B) = \gcd\big(r,\gcd(a,b)\big), \qquad G_p(B') = \gcd\big(r,\gcd(\min(a,b),|a-b|)\big).$$
By Lemma I2, `\gcd(\min(a,b),|a-b|)=\gcd(a,b)`, so the two expressions for
`G_p(B)` and `G_p(B')` are identical. Hence `G_p(B')=G_p(B)`. $\blacksquare$

**Reconstruction of `M`.** By induction on the number of moves played (Lemma
GP gives invariance across a single move; iterating, `G_p` is the same at
every board reached along any legal play, in particular at the initial board
`B^{(0)}` and at the terminal board `B^{\*}`), for every prime `p`,
$$G_p(B^{\*}) = G_p(B^{(0)}) = G_p \quad\text{(as defined above from the initial data).}$$
By part (a), `B^{\*}` has exactly one active position, holding a value `M>1`,
and all other `2025` positions hold `1`. Hence for each prime `p`, the
multiset of `p`-valuations at `B^{\*}` is `\{v_p(M),0,0,\dots,0\}` (`2025`
zeros), whose gcd is `v_p(M)` itself (by the convention `\gcd(x,0,\dots,0)=x`,
which follows since `x` divides itself and every divisor of `x` is a common
divisor of `\{x,0,\dots,0\}$, while any common divisor of this multiset must
in particular divide `x`, so the greatest common divisor is exactly `x`).
Therefore
$$v_p(M) = G_p(B^{\*}) = G_p \qquad\text{for every prime } p.$$
By the Fundamental Theorem of Arithmetic (unique factorization determines a
positive integer from its full list of `p`-adic valuations), this determines
`M` uniquely:
$$M \;=\; \prod_{p\ \text{prime}} p^{\,G_p}.$$

This product is well-defined (finite): `G_p=0` for every prime `p` that
divides none of `a_1,\dots,a_{2026}` (since then all `2026` valuations at `p`
are `0`, so `G_p=\gcd(0,\dots,0)=0`), so only the finitely many primes
dividing at least one `a_i` can contribute a factor `>1`; thus `M` is a
well-defined positive integer determined entirely by the multiset of initial
board entries `a_1,\dots,a_{2026}`, with **no dependence on the sequence of
moves Confucius chooses** — the right-hand side `\prod_p p^{G_p}` is a
function of the initial board only. This proves part (b).

(For completeness: `M>1`, consistent with part (a), since the initial board
has every `a_i>1`, so at least one prime `p_0` divides `a_1$, giving
`v_{p_0}(a_1)>0$; as `\gcd` of a multiset of nonnegative integers is `0` only
if all of them are `0`, and `v_{p_0}(a_1)>0`, we get `G_{p_0}>0`, so
`M\ge p_0^{G_{p_0}} > 1`.)

$\blacksquare$ (Both parts (a) and (b) are proved.)

## Promotable lemmas

- **Lemma I1 (monovariant inequality)** — `\min(a,b)^2+|a-b|^2 \le a^2+b^2` for
  nonnegative integers `a,b`, with equality iff `\min(a,b)=0`. Proved in full
  in Section 0 above (elementary algebraic identity, WLOG `a\le b` reduction).
  Reusable verbatim by any approach to this problem needing the per-prime
  reduction.
- **Lemma I2 (gcd invariance under one Euclidean step)** — `\gcd(\min(a,b),
  |a-b|) = \gcd(a,b)` for nonnegative integers `a,b`. Proved in full in
  Section 0 (common-divisor-set argument). Reusable verbatim.
- **Lemma L1 ("not both trivial")** — for `m,n>1`, `\gcd(m,n)` and
  `\operatorname{lcm}(m,n)/\gcd(m,n)` are not both `1`, via
  `\gcd(m,n)\cdot(\operatorname{lcm}(m,n)/\gcd(m,n)) = \operatorname{lcm}(m,n) \ge m > 1`. Proved in
  full in Section 0. (Note: corrects a related identity that appeared with a
  typo — `g\cdot q = \operatorname{lcm}(m,n)`, not `mn` — in at least one sibling
  approach; the conclusion "not both trivial" is unaffected, but the
  intermediate identity should read `\operatorname{lcm}(m,n)`.)
- **Lemma SM (Single-Move Lemma)** — for any legal move on a board with
  `k(B)\ge2` active entries, the active count `k` and quadratic potential
  `\Sigma` satisfy exactly one of: `k` drops by `1` (any `\Sigma` change), or
  `k` is unchanged and `\Sigma` strictly decreases. Proved in full in Section
  2, using only I1, I2, L1 and the per-prime identity `(\ast)`. This is a
  genuinely reusable, move-local (strategy-independent) lemma — stronger than
  the sibling approaches' single "lexicographic potential decreases" claim,
  since it separates the two cases explicitly and could be reused by any
  approach wanting an explicit termination bound (`\le k(B)+\Sigma(B)` total
  moves, since the active count can drop at most `k(B)` times and, between
  consecutive drops, `\Sigma` — which never increases — can absorb at most
  `\Sigma(B)` many stalling moves).
- **Lemma GP (`G_p` invariance)** — for every prime `p`, `G_p(B)=\gcd` of the
  board's `p`-adic valuations is unchanged by every legal move. Proved in full
  in Section 4 via gcd-distributes-over-concatenation + Lemma I2. Identical in
  content to the invariant used by the sibling approaches for part (b);
  proved here independently and completely, safe to certify as the canonical
  part-(b) lemma for this problem.
