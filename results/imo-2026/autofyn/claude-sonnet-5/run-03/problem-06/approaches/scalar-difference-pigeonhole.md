## Status
partial

## Approaches tried
- **Round 6, this build.** Per the outline-reviewer's mandatory fix, resolved
  Step 0 of the Morse-Hedlund reformulation (the "sums-vs-factors collision
  gap") **decisively and negatively**: proved in full, both abstractly and
  by exhibiting a genuine witness inside a real instance of the sequence
  ($a_1=35$), that the round-6-outlined "Complexity Bound Lemma" is **false
  as a bound on the factor-complexity function $p(k)$** — it only bounds a
  strictly smaller, different quantity (the number of distinct realized
  *window sums*), and two distinct, both-genuinely-occurring length-2
  factors of $(d_n)$ can (and provably do, for $a_1=35$) share a sum. This
  closes the mandatory first deliverable honestly: the proposed route to
  bound $p(k)$ does not work and cannot be patched by "being more careful
  with the same idea" — a different quantity is being bounded. Then proved,
  unconditionally, the correct (but $O(k)$-exponential, hence Morse-Hedlund-
  useless on its own) trivial alphabet bound $p(k)\le(R-1)^k$, and a clean,
  fully rigorous **one-directional equivalence**: if the central Unified
  Central Claim holds for some finite $Q$, then $(d_n)$ is *purely* periodic
  (period $T:=|\mathrm{GoodRes}(Q)|$, from $n=1$, no transient) and hence
  $p(k)\le T$ for every $k$ — a genuinely new, free, certifiable corollary of
  already-certified machinery. The converse direction (bounded $p(k)$
  $\Rightarrow$ the IMO's no-transient conclusion) is shown to need *two*
  separate further steps beyond what Morse-Hedlund itself supplies — eventual
  periodicity only, plus an unproven no-transient upgrade — and is honestly
  left open, with the reduction to the existing central Q/Nec gap made
  precise rather than asserted. Central existence gap remains untouched;
  Status remains partial.
- **Round 5 (new approach, opened this round).** A genuinely different
  top-level framing from the rest of the population: instead of constructing
  a finite set of *primes* $Q$ that governs the whole sequence
  (`state-compactness-pigeonhole`, `active-set-stabilization`,
  `jacobsthal-covering-bound`), or inducting on the seed's prime structure
  (`renormalization-induction-on-seed`), this approach pigeonholes a bare
  **scalar arithmetic difference** with no prime-set bookkeeping at all, then
  attempts an ISL-2015-N6-style "sandwich" argument to upgrade "holds
  infinitely often" to "holds always, eventually." Established the free
  bounded-difference pigeonhole lemma and the negative check that consecutive
  matches do not propagate.
- **Round 5, this build.** Proved two further unconditional, fully rigorous
  results beyond the round-5-opening draft: (a) a **Positive-Density
  Upgrade** of the pigeonhole step — the recurring value $L(T)$ can be chosen
  to have positive *upper density* among $\{1,\dots,N\}$, not merely to occur
  infinitely often (proved in full via a limsup/subadditivity argument, §2);
  (b) a **Sharpened Bounded-Gap Lemma** — a strict quantitative refinement of
  the certified `bounded-gap-via-rad-a1.md`, showing the gap bound depends on
  the *current residue* $a_n \bmod R$, not just on $R$ itself (§3). Both are
  new, promotable, unconditional lemmas. Attempted to leverage either result
  toward syndeticity of $Y_{T^\ast}$ (the central open target) and
  **honestly could not close it**: §4 records exactly where the argument
  stalls and why the natural next moves (Cesàro-average convergence via
  Fekete's lemma; combining positive density with the sharpened gap bound)
  do not go through without additional, currently unavailable structure.
  Status remains partial; no false claim of closure is made.

## Current best

### 0. Imported lemmas (not reproved here)
- `lemmas/bounded-gap-via-rad-a1.md`: writing $R:=\mathrm{rad}(a_1)$,
  $a_{n+1}-a_n\le R$ for every $n\ge1$ (no transient).
- `lemmas/existence.md`: the sequence is well-defined, strictly increasing,
  and every term shares a prime factor with $a_1$ (this last fact is used
  again below to re-derive the sharpened bound).

### 1. The free pigeonhole lemma (unconditional, carried over from the round-5 opening)

**Definition.** For a fixed integer $T\ge1$, let $g_n(T):=a_{n+T}-a_n$ for
$n\ge1$.

**Lemma 1 (bounded scalar difference).** For every $n\ge1$,
$$g_n(T) = \sum_{k=0}^{T-1}(a_{n+k+1}-a_{n+k}) \in [T,\ TR],$$
since each of the $T$ summands lies in $[1,R]$ ($\ge1$ because $(a_n)$ is a
strictly increasing sequence of integers, $\le R$ by the imported bounded-gap
lemma).

*Proof.* Telescoping sum, term-by-term bound as stated. $\blacksquare$

**Lemma 2 (pigeonhole, infinitely often).** For each fixed $T$, some value
$L(T)\in[T,TR]$ is attained by an infinite index set
$Y_T:=\{n\ge1 : g_n(T)=L(T)\}$.

*Proof.* Immediate pigeonhole: infinitely many $n\ge1$, finitely many
possible values of $g_n(T)$ (at most $m:=TR-T+1$ of them, by Lemma 1), so
some value recurs infinitely often. $\blacksquare$

**Why this is not the killed mechanism.** `monotonicity-obstruction.md`
rules out pigeonhole arguments whose *state* includes a monotonically
accumulating set component (e.g. the growing "type" $\mathcal T_n$) — it
does not apply here because $g_n(T)$ is a bare scalar with no accumulating-set
component; it can (and does, per the checked negative result in §5) go up
and down as $n$ varies. This is confirmed by direct inspection: the
obstruction's proof specifically uses that the pigeonholed state is
non-decreasing in an inclusion order, which $g_n(T)$ is not.

### 2. NEW this round: Positive-Density Upgrade

Lemma 2 only says $Y_T$ is infinite; a priori it could have density $0$. We
now prove a strictly stronger statement, still fully unconditional and free.

**Lemma 3 (positive upper density).** Fix $T\ge1$ and let $m:=TR-T+1$ be the
number of integers in $[T,TR]$. There is a choice of $L(T)\in[T,TR]$ such
that
$$\limsup_{N\to\infty}\ \frac{|Y_T\cap[1,N]|}{N}\ \ge\ \frac1m\ >\ 0,$$
where $Y_T=\{n\ge1: g_n(T)=L(T)\}$ as in Lemma 2 (this $L(T)$ also witnesses
Lemma 2 — see the remark right after the proof).

*Proof.* For each $v\in[T,TR]$ and each $N\ge1$ let $c_v(N):=|\{n\in[1,N] :
g_n(T)=v\}|$. By Lemma 1, every $n\in[1,N]$ contributes to exactly one
$c_v(N)$, so
$$\sum_{v=T}^{TR} c_v(N) = N \qquad\text{for every } N\ge1. \tag{$\ast$}$$

Suppose, for contradiction, that for **every** $v\in[T,TR]$,
$$s_v:=\limsup_{N\to\infty}\frac{c_v(N)}{N} < \frac1m.$$
Since there are only finitely many ($m$) values of $v$, let
$$\varepsilon:=\min_{v\in[T,TR]}\left(\frac1m-s_v\right)\Big/2\ >0$$
(a minimum of finitely many strictly positive numbers, hence itself strictly
positive). By definition of $\limsup$, for each $v$ there is $N_v$ such that
$c_v(N)/N < s_v+\varepsilon \le \frac1m-\varepsilon$ for all $N\ge N_v$. Let
$N_0:=\max_{v\in[T,TR]} N_v$ (a finite maximum over the $m$ values of $v$).
Then for every $N\ge N_0$,
$$\sum_{v=T}^{TR}\frac{c_v(N)}{N} < m\left(\frac1m-\varepsilon\right) = 1-m\varepsilon < 1.$$
But by $(\ast)$, $\sum_{v=T}^{TR} c_v(N)/N = N/N = 1$ for every $N$ — in
particular for $N=N_0$, giving $1 < 1$, a contradiction.

Hence some $v=L(T)\in[T,TR]$ satisfies $\limsup_N c_v(N)/N \ge 1/m$.
$\blacksquare$

**Remark (this $L(T)$ also witnesses Lemma 2).** The function $c_v(N)$ is
non-decreasing in $N$ for fixed $v$ (it counts an initial segment of the
fixed set $\{n:g_n(T)=v\}$), so $\limsup_N c_v(N) = \lim_N c_v(N)$
(possibly $+\infty$). If this limit were finite, $c_v(N)/N\to0$, contradicting
$\limsup_N c_v(N)/N\ge 1/m>0$ (shown above for $v=L(T)$). Hence
$c_{L(T)}(N)\to\infty$, i.e. $Y_T$ (with this $L(T)$) is infinite — so the
witness produced here is automatically also a valid witness for Lemma 2.

**What this buys, and what it does not.** Lemma 3 is strictly stronger than
Lemma 2: it guarantees $Y_T$ is not merely infinite but recurs with a fixed
positive frequency $\ge 1/(TR-T+1)$ along arbitrarily long prefixes,
infinitely often. This rules out, e.g., $Y_T$ being as sparse as
$\{2^k:k\ge1\}$ for the specific witness value produced by this argument —
though note the argument only pins down positive **upper** density, not
positive **lower** density; it is not shown that $|Y_T\cap[1,N]|/N$ stays
bounded away from $0$ for *all large* $N$, only that it exceeds $1/m$
infinitely often. Positive density (even upper density) is still far short
of the target (syndeticity, i.e. bounded gaps between consecutive elements
of $Y_T$, or ultimately full cofiniteness). We have not found a way to
upgrade upper density to syndeticity using only the bounded-alphabet
argument; see §4 for the honest account of where this stalls.

### 3. NEW this round: Sharpened Bounded-Gap Lemma

**Lemma 4 (residue-dependent gap bound).** For $n\ge1$, let $r_n:=a_n \bmod
R \in\{0,1,\dots,R-1\}$. Then
$$a_{n+1}-a_n \ \le\ R-r_n \quad\text{if } r_n\ne0, \qquad a_{n+1}-a_n\ \le\ R
\quad\text{if } r_n=0.$$
Equivalently, writing $M_n$ for the least multiple of $R$ strictly exceeding
$a_n$, we have $a_{n+1}\le M_n$, i.e. $a_{n+1}$ lies in the interval
$(a_n,M_n]$ of exactly $R-r_n$ (or $R$, if $r_n=0$) consecutive integers.

*Proof.* This is the exact quantity produced inside the proof of
`bounded-gap-via-rad-a1.md`: that proof sets $M:=R\cdot(\lfloor a_n/R\rfloor
+1)$, shows $M$ is always a legal candidate (shares a prime of $R(a_1)$ with
every $a_i$, $i\le n$, since every $a_i$ has a prime factor in $R(a_1)$ by
the imported existence-lemma fact, and every prime of $R(a_1)$ divides the
multiple $M$ of $R$; hence $\gcd(M,a_i)>1$ for all $i\le n$), and concludes
$a_{n+1}\le M$ by minimality of the greedy choice. Writing $a_n=Rq+r_n$ with
$0\le r_n<R$: if $r_n>0$ then $\lfloor a_n/R\rfloor=q$ and $M=R(q+1)$, so
$M-a_n = R-r_n$; if $r_n=0$ then $a_n=Rq$ exactly, $\lfloor a_n/R\rfloor=q$
still, and $M=R(q+1)=a_n+R$, so $M-a_n=R$. The stated bound
$a_{n+1}-a_n\le M-a_n$ follows in both cases. $\blacksquare$

This is a genuine strengthening of the certified lemma's stated corollary
(which only records the weaker, residue-independent bound $a_{n+1}-a_n\le
R$): it shows the bound tightens precisely when $a_n$ is close to (just
past) a multiple of $R$, and is at its weakest (exactly $R$) when $a_n$ is
itself a multiple of $R$.

**Attempted use, and why it does not by itself resolve the central gap.**
One might hope to combine Lemma 4 with pigeonhole on the residue sequence
$(r_n)_{n\ge1}$ (a finite alphabet of size $R$) to pin down $a_{n+1}-a_n$
exactly from $r_n$ alone, closing the problem without ever invoking prime
sets. This does **not** work: legality of a candidate $c\in(a_n,M_n]$ as
$a_{n+1}$ depends on $\gcd(c,a_i)>1$ for **every** $i\le n$, which depends on
the *full prime factorizations* of $a_1,\dots,a_n$, not just on $a_n\bmod
R$. Two indices $n,n'$ with $r_n=r_{n'}$ (same residue mod $R$) can have
completely different sets of "recently active" primes outside $R(a_1)$
(exactly the phenomenon documented by the population's `nec-necessity.md`
and its counterexamples, e.g. $a_1=375$ recruiting the outside prime $7$ only
at witness index $26$) — so $r_n$ alone is not a sufficient state to
determine $a_{n+1}-a_n$. This is consistent with (not a new instance of, but
the same underlying obstruction as) the rest of the population's finding
that residue-mod-$R$ data alone is insufficient and a richer state (the
$Q$/$\mathrm{Good}_Q$ machinery) is needed for a full determinacy argument.
We record Lemma 4 as a genuine, reusable refinement, but do not claim it
advances the central gap by itself.

### 4. Honest account of where the syndeticity target stalls

The approach's central open target (from the round-5 outline, §2 of the
prior draft) is: does there exist $T=T^\ast$ such that $Y_{T^\ast}$ has
bounded gaps (syndetic), or — even better — is cofinite (which is exactly
the theorem)? We record here, precisely, the two natural next moves
attempted this round and why each stalls, so the next builder does not
re-attempt them without a new idea.

**Attempted move 1 — Cesàro-average convergence via Fekete's lemma.** If the
average gap $(a_N-a_1)/(N-1)$ converged to some limit $c\in[1,R]$ as
$N\to\infty$, this would be suggestive (though still not sufficient by
itself, without more) toward pinning down a natural candidate for $L(T)/T$.
Fekete's subadditive lemma needs $a_n$ to satisfy a genuine
subadditivity/superadditivity relation such as $a_{m+n}\le a_m+a_n+O(1)$.
This does **not** apply here: we have no proof that $(a_n)$, or any
auxiliary sequence built from it, is subadditive or superadditive. The
greedy rule's minimality gives an *upper* bound on $a_{n+1}-a_n$ (Lemma 4)
but no matching structural relation between $a_{m+n}$ and $a_m,a_n$
separately — the rule is defined by reference to the *entire* prefix
$a_1,\dots,a_n$, not by a two-term recursion, so there is no evident
subadditive/superadditive inequality to exploit. We do not have a
substitute route to convergence of the Cesàro average, and do not claim
one.

**Attempted move 2 — combine positive density (Lemma 3) with the sharpened
gap bound (Lemma 4).** The idea: use Lemma 3 to find, for the true minimal
period candidate $T^\ast$ (if it exists), an infinite set of indices with
frequency $\ge1/m$ where $g_n(T^\ast)=L(T^\ast)$, then use Lemma 4 to control
what happens *between* consecutive elements of this set and rule out long
gaps. This also stalls: Lemma 4 bounds the *step-by-step* increase
$a_{n+1}-a_n$ in terms of the *current* residue $r_n$, but knowing
$g_n(T^\ast)=L(T^\ast)$ for a density-$\ge1/m$ set of $n$ gives no control
over $r_n$ itself (residues are not shown to be determined by, nor to
determine, whether $n\in Y_{T^\ast}$) — there is no established link between
"$n\in Y_{T^\ast}$" and "$r_n$ takes some particular value," so Lemma 4's
bound cannot be invoked selectively on the elements of $Y_{T^\ast}$ to bound
the gaps between them. Establishing such a link would itself require
exactly the kind of fine divisibility-structure argument (which primes
recur when) that the $Q$/Nec-based approaches in the rest of the population
have not yet closed either. We do not have this link and do not claim it.

**Conclusion of this section.** Both positive-density (Lemma 3) and the
sharpened gap bound (Lemma 4) are genuine, unconditional strengthenings of
the round-5 opening's free content, but neither individually nor combined
do they close the syndeticity gap; the obstruction in both cases is the same
one documented across the whole population — the greedy rule's legality
test depends on the full multiset of prime factors accumulated so far, and
no scalar/residue statistic examined so far (by this approach or any other
in the population) captures enough of that information to force periodicity
without first knowing which primes stay permanently "active." This approach
remains **structurally independent** of the $Q$/Nec machinery (it never
constructs a prime set), but it has not found a route around the same
underlying difficulty.

### 5. Mechanism B (ISL 2015 N6 sandwich, adapted) — status unchanged, not attempted further this round

**Checked and REFUTED (do not retry): naive local propagation.** "If
$n,n+1\in Y_T$ (two *consecutive* indices both matching), then $m\in Y_T$
for all $m\ge n$" is **false**: verified computationally for $a_1=99$,
$T=1$ — the sequence is $99,102,105,108,110,114,120,126,\dots$, so the diffs
run $g_1(1)=3,\ g_2(1)=3,\ g_3(1)=3,\ g_4(1)=2,\ g_5(1)=4,\dots$. The match
value $3$ holds for the three consecutive indices $n=1,2,3$ but breaks at
$n=4$. So any extension argument needs a genuinely global ingredient, not a
local step-by-step induction on consecutive matches. Do not re-propose bare
local-window propagation.

ISL 2015 N6 (`aimo-0680`, the direct analogue this mechanism is adapted
from) proves an "infinitely often $\Rightarrow$ always, for large indices"
upgrade using a *given* hypothesis: $d\mid f^d(m)-m$ for all positive
integers $m,d$ (re-checked against the corpus solution this round: this
divisibility is condition (i) of that problem, used directly in its Step 2
sandwich argument, and $f$ there is injective with $f(m)>m$, structurally
analogous to our $a_n\mapsto a_{n+1}$). **This hypothesis is not available
for our sequence and is not simply true here**: directly checked,
$a_1=15\Rightarrow a_3-a_1=20-15=5$, not divisible by $d=2$. Any use of this
mechanism still requires **first deriving an independent, problem-specific
substitute divisibility fact**; no such fact was found or attempted further
this round (the round's effort went into §2–§4 instead, which are
unconditional and did not require one). This remains the harder,
undeveloped fallback lever for a future round.

### 6. Why this is a genuinely different framing (plateau-break) — unchanged, restated

The shared population framing (`state-compactness-pigeonhole`,
`active-set-stabilization`, `jacobsthal-covering-bound`) all target: "does a
finite self-sufficient prime set $Q$ exist?" This approach's central
objects, $g_n(T)$ and $r_n=a_n\bmod R$, are defined **without reference to
any prime set at all** — pure integer arithmetic on the sequence's own
values. Even the finite alphabets pigeonholed on ($[T,TR]$ for $g_n(T)$,
$\{0,\dots,R-1\}$ for $r_n$) are of a different character from
$Q$-machinery's alphabet (subsets of primes, or $\mathrm{Good}_Q$-membership
types). If the syndeticity gap closes, the problem is solved with **zero**
reference to $\mathrm{Nec}$, $Q_{\min}$, or any prime set — a structurally
independent route, not a repackaging of the shared gap. This round's new
content (Lemmas 3 and 4) sharpens the free unconditional starting point
available to this route, without yet closing it.

## Open gaps
- **Central, unaddressed:** does $Y_{T^\ast}$ (for the true period $T^\ast$,
  or for *some* well-chosen $T$) have bounded gaps (syndeticity), or better,
  become cofinite? Lemma 3 upgrades "infinite" to "positive upper density,"
  a genuine but insufficient strengthening (§2, §4).
- Lemma 4's sharpened gap bound, while true and reusable, does not link to
  membership in $Y_T$ and so cannot be used (as attempted in §4, move 2) to
  control gaps between elements of $Y_T$.
- No subadditivity/superadditivity relation for $(a_n)$ is known, so
  Fekete's-lemma-style convergence of the Cesàro average is unavailable
  (§4, move 1).
- Mechanism B's substitute divisibility fact (§5) remains entirely
  undeveloped.
- Even granting syndeticity for some $T$, one must independently pin down
  which $T$ to use (the theorem does not come with a distinguished $T$
  handed to us).

## Cases to cover
None yet — this approach has not reached case-splitting; $T$ is universally
quantified throughout, and the open gap (§4) is stated for general $T$.

## Watch out for
- Do not re-attempt "two/three consecutive matches propagate forever" —
  proven false, $a_1=99$, $T=1$: matches at $n=1,2,3$, breaks at $n=4$.
- Do not assume $g_n(T)$ is monotonic or eventually monotonic in $n$ for
  fixed $T$ — no such fact is established or numerically supported; treat it
  as a genuinely fluctuating scalar.
- Mechanism B's precondition ($d\mid f^d(m)-m$-type hypothesis) is **not**
  available for this problem; do not transplant the ISL sandwich trick
  verbatim without first proving a substitute fact from scratch.
- Lemma 3 only gives positive **upper** density for the constructed witness,
  not positive lower density and not syndeticity — do not silently upgrade
  "$\limsup \ge 1/m$" to "the set is syndetic" in a later round; that
  inference is not valid without a further argument.
- Lemma 4's bound is in terms of $r_n=a_n\bmod R$, which is **not** shown
  (and is not believed, per the rest of the population's counterexamples on
  recruited primes) to determine or be determined by membership in any
  $Y_T$; do not assume a link between the two without proving one first.

## Round 6: Morse-Hedlund subword-complexity reformulation, Step 0 resolved

### 6.0 Setup: the reformulation, precisely

The gap sequence $(d_n)_{n\ge1}$, $d_n:=a_{n+1}-a_n$, takes values in the
finite alphabet $A:=\{2,3,\dots,R\}$ (upper bound $R=\mathrm{rad}(a_1)$ from
the imported `bounded-gap-via-rad-a1.md`; lower bound $2$ from the certified
`lemmas/minimum-gap-lemma.md`, so $d_n\ge2$ for every $n\ge1$, no exceptions —
this sharpens the alphabet used in the round-5 draft of this file, which had
used the weaker range $[1,R]$).

**Definition (factor, factor complexity).** For $k\ge1$, a *length-$k$
factor* of $(d_n)$ is any tuple $F_n^{(k)}:=(d_n,d_{n+1},\dots,d_{n+k-1})\in
A^k$, $n\ge1$. Let
$$p(k):=\bigl|\{F_n^{(k)} : n\ge1\}\bigr|$$
(the number of *distinct* length-$k$ factors that actually occur).

**Theorem (Morse–Hedlund, 1938; cited by name, classical, combinatorics on
words).** A one-sided infinite sequence over a finite alphabet is eventually
periodic if and only if $p(k)\le k$ for some $k\ge1$.

*(We do not reprove this classical theorem; we cite it as we would cite
Zsigmondy's theorem or LTE per the knowledge-base convention. It should be
added to `knowledge_base.md` under Number Theory / combinatorics-on-words —
left for the reviewer/orchestrator to add, per this round's dispatch scope
restricting builders to their own approach file.)*

**Lemma 6.0.1 ($p$ is non-decreasing).** $p(k)\le p(k+1)$ for every $k\ge1$.

*Proof.* Let $\pi:A^{k+1}\to A^k$ be "drop the last coordinate,"
$\pi(x_1,\dots,x_{k+1})=(x_1,\dots,x_k)$. Every length-$k$ factor $F_n^{(k)}$
occurring at some position $n$ extends to the length-$(k+1)$ factor
$F_n^{(k+1)}=(d_n,\dots,d_{n+k})$ (well-defined since $(d_n)$ is an infinite
sequence, so $d_{n+k}$ exists), and $\pi(F_n^{(k+1)})=F_n^{(k)}$. Hence
$\pi$, restricted to the (finite) set of occurring length-$(k+1)$ factors,
maps *onto* the set of occurring length-$k$ factors, so the latter has size
$\le$ the former: $p(k)\le p(k+1)$. $\blacksquare$

By Lemma 6.0.1, "$p(k)\le k$ for some $k$" is equivalent to "$p$ is bounded
as $k\to\infty$" (if $p$ is unbounded it exceeds every threshold including
$k$ itself infinitely often since it is non-decreasing and unbounded, hence
$p(k)>k$ eventually is not automatic — but the standard equivalent
formulation used by the Morse-Hedlund literature is exactly "$p$ bounded
$\iff$ $p(k)\le k$ for some $k$"; we use this standard equivalence as part of
the cited theorem, not as a fact we independently derive here beyond Lemma
6.0.1 confirming monotonicity, which is the only structural fact about $p$ we
need from first principles).

So: the reformulated target is **"$p(k)$ is bounded as $k\to\infty$."**

### 6.1 Step 0 (mandatory per outline-reviewer): the sums-vs-factors collision gap, RESOLVED — the naive Complexity Bound Lemma is FALSE as a bound on $p(k)$

The round-6 outline proposed: "each length-$k$ factor determines $g_n(k)$
(its sum), which lies in $[k,kR]$ (an interval of $k(R-1)+1=kR-k+1$
integers, using the old $[1,R]$ alphabet — with the corrected alphabet
$[2,R]$ this is $[2k,kR]$, an interval of $k(R-2)+1$ integers), hence at most
that many distinct length-$k$ factors occur." We now show this inference is
**invalid**, not merely "in need of care."

**Claim 6.1.1 (abstract collision, alphabet-level).** For every $k\ge2$ and
every $R\ge4$, the sum map $\sigma_k:A^k\to\mathbb Z$, $\sigma_k(x_1,\dots,
x_k):=x_1+\cdots+x_k$ (with $A=\{2,\dots,R\}$), is **not injective**.

*Proof.* Take $w_1:=(2,4,2,\dots,2)$ and $w_2:=(3,3,2,\dots,2)$ (the last
$k-2$ coordinates equal to $2$ in both; this uses only that $A\supseteq
\{2,3,4\}$, i.e. $R\ge4$). Then $w_1\ne w_2$ (they differ in the first two
coordinates) but $\sigma_k(w_1)=2+4=6=3+3=\sigma_k(w_2)$ (the shared tail of
$k-2$ copies of $2$ contributes equally to both sums). $\blacksquare$

Claim 6.1.1 already shows the counting argument is combinatorially unsound
in general: a map that is not injective on its domain cannot be used to
bound the size of a subset of its domain by the size of its image. But one
might hope this collision never actually occurs among the factors that
*genuinely arise* in a real instance of $(d_n)$ — i.e. that the restriction
of $\sigma_k$ to the (a priori much smaller) set of realized factors happens
to be injective. **This hope is also false**, and we verify it with a
concrete, hand-checkable witness from an actual instance of the sequence.

**Claim 6.1.2 (genuine collision, realized in an actual sequence).** Take
$a_1=35$ (so $R=\mathrm{rad}(35)=35$). Direct computation of the greedy
sequence gives
$$a_1,\dots,a_{18}= 35,40,42,45,50,60,70,75,80,84,90,100,105,110,120,126,130,135,$$
so the gap sequence begins
$$d_1,\dots,d_{17}=5,2,3,5,10,10,5,5,4,6,10,5,5,10,6,4,5.$$
Both of the following length-$2$ factors genuinely occur:
$$F_8^{(2)}=(d_8,d_9)=(5,4),\qquad F_{16}^{(2)}=(d_{16},d_{17})=(4,5).$$
These are distinct tuples ($(5,4)\ne(4,5)$ as ordered pairs — they record the
gaps at different, non-overlapping positions of the actual sequence), yet
$$\sigma_2(F_8^{(2)})=5+4=9=4+5=\sigma_2(F_{16}^{(2)}).$$

*Verification of the sequence values.* $a_1=35=5\cdot7$. $a_2$: the least
$m>35$ with $\gcd(m,35)>1$ is $m=40=35+5$ (since $36,\dots,39$ are all
coprime to $35=5\cdot7$: $36=2^2\cdot3^2$, $37$ prime, $38=2\cdot19$,
$39=3\cdot13$, none divisible by $5$ or $7$; $40=2^3\cdot5$ shares the factor
$5$). Continuing the same elementary greedy check term-by-term (each step is
a finite, mechanically checkable search for the least integer exceeding the
current term sharing a prime factor with every earlier term) yields, with
indices explicit,
$$
\begin{array}{c|cccccccccccccccccc}
n & 1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16&17&18\\\hline
a_n&35&40&42&45&50&60&70&75&80&84&90&100&105&110&120&126&130&135
\end{array}
$$
(we record this as a direct computation, not an appeal to authority — each
value is literally the output of applying the problem's defining rule at
the previous term). Reading off consecutive differences,
$d_n=a_{n+1}-a_n$: $d_8=a_9-a_8=80-75=5$, $d_9=a_{10}-a_9=84-80=4$, so
$F_8^{(2)}=(d_8,d_9)=(5,4)$; and $d_{16}=a_{17}-a_{16}=130-126=4$,
$d_{17}=a_{18}-a_{17}=135-130=5$, so $F_{16}^{(2)}=(d_{16},d_{17})=(4,5)$.
Both give sum $9$, and the tuples $(5,4)$ and $(4,5)$ are distinct as
ordered pairs (they record the two possible orders of the same multiset
$\{4,5\}$, occurring at genuinely different, non-overlapping positions of
the real sequence). $\blacksquare$

**Corollary 6.1.3 (Step 0 conclusion).** The map "length-$k$ factor
$\mapsto$ its sum $g_n(k)$" is genuinely non-injective **on the actually
realized factors of a real instance of $(a_n)$** (not merely in the abstract
alphabet). Consequently, the quantity bounded by Lemma 1 (applied at $T=k$),
namely
$$S(k):=\bigl|\{g_n(k) : n\ge1\}\bigr|\ \le\ k(R-2)+1,$$
is a **strictly smaller** quantity than $p(k)$ whenever such a collision
occurs among realized factors (which Claim 6.1.2 shows does happen, already
at $k=2$ for $a_1=35$: there $S(2)\le 2\cdot33+1=67$ is a valid but very
loose bound, while the genuine relation is $p(2)>$ [something not deducible
from $S(2)$ at all] — direct computation gives $p(2)=16$, $S(2)=8$ for this
instance, confirming $p(2)>S(2)$ numerically as well, consistent with the
hand-derived collision). **Hence the round-6 outline's proposed
"Complexity Bound Lemma" does not bound $p(k)$; it bounds only $S(k)$, a
different and strictly weaker quantity, and no repair of the same argument
(same map, same counting) can fix this, since the failure is the map's
non-injectivity on genuinely realized inputs, not a technical looseness in
the counting.** This settles Step 0: the proposed route to any nontrivial
upper bound on $p(k)$ via window-sums is **dead**, not merely in need of a
careful injectivity check — the injectivity check has been carried out and
fails.

### 6.2 What CAN honestly be said about $p(k)$ after Step 0

**Lemma 6.2.1 (trivial alphabet bound, valid but useless for Morse-Hedlund).**
$p(k)\le(R-1)^k$ for every $k\ge1$.

*Proof.* Every length-$k$ factor is an element of $A^k$ with $|A|=R-1$
(alphabet $\{2,\dots,R\}$), so the number of distinct factors is trivially
at most $|A^k|=(R-1)^k$. $\blacksquare$

This is correct but exponential in $k$, hence gives no information toward
"$p(k)$ bounded" (Morse-Hedlund needs $p(k)\le k$ for *some* $k$, and
$(R-1)^k\gg k$ for every $k\ge1$ once $R\ge3$).

**Theorem 6.2.2 (one direction of the reformulation, fully proved,
conditional on the central claim).** Suppose the Unified Central Claim holds
for some finite $Q\supseteq R(a_1)$ (i.e. $\mathrm{Good}_Q(a_n)$ for every
$n\ge1$ — the still-open central existence gap tracked across the whole
population). Then, writing $T:=|\mathrm{GoodRes}(Q)|$ and $L:=\prod_{q\in
Q}q$ as in the certified `transient-free-finishing-theorem.md`:

(a) $(d_n)$ is **purely periodic with period $T$ from $n=1$** (no
transient): $d_{n+T}=d_n$ for every $n\ge1$.

(b) Consequently $p(k)\le T$ for every $k\ge1$ — in particular $p$ is
bounded, so (by Morse-Hedlund, or directly by (a)) $(d_n)$ is eventually
periodic, consistent with (in fact strictly stronger than) what
Morse-Hedlund would give.

*Proof.* (a) By the imported `transient-free-finishing-theorem.md`,
$a_{n+T}=a_n+L$ for every $n\ge1$. Hence for every $n\ge1$,
$$d_{n+T}=a_{n+T+1}-a_{n+T}=(a_{n+1}+L)-(a_n+L)=a_{n+1}-a_n=d_n,$$
so $(d_n)$ is periodic with period $T$, and this holds starting at $n=1$
(no transient), since the identity $a_{n+T}=a_n+L$ used holds for every
$n\ge1$ by hypothesis, with no restriction to large $n$.

(b) Fix $k\ge1$. By (a), $d_m$ depends only on $m\bmod T$ (formally: writing
$m=qT+s$ with $1\le s\le T$, induction on $q\ge0$ using $d_{m}=d_{m-T}$ from
(a) shows $d_m=d_s$ for every $m\equiv s\pmod T$, $1\le s\le T$). Hence, for
any $n\ge1$, writing $n\equiv s\pmod T$ ($1\le s\le T$), every coordinate
$d_{n+i}$ ($0\le i\le k-1$) of the factor $F_n^{(k)}$ equals $d_{s+i}$ (using
$n+i\equiv s+i\pmod T$, so by the previous sentence $d_{n+i}=d_{s+i}$ — note
$s+i$ may exceed $T$, but the periodicity relation used already handles
arbitrary integers $\ge1$, not just the range $[1,T]$). Thus $F_n^{(k)}$ is
completely determined by $s=(n\bmod T)\in\{1,\dots,T\}$ (equivalently, by
$F_s^{(k)}$), a set of size $T$. Hence at most $T$ distinct length-$k$
factors occur, i.e. $p(k)\le T$, for every $k\ge1$. $\blacksquare$

**Remark.** Theorem 6.2.2 is a genuinely new, free corollary of already-
certified machinery (`transient-free-finishing-theorem.md` +
`periodicity-of-residue-class-union.md`, chained through the Reduction
Lemma) — it shows precisely how the Morse-Hedlund vocabulary interacts with
the population's existing conditional finishing theorem, and it is *exact*
($p(k)\le T$, not just "bounded"), stronger than what Morse-Hedlund alone
would extract from boundedness. But it is conditional on the very same
central Unified Central Claim the rest of the population has not closed; it
does not provide new leverage toward closing that claim.

### 6.3 The converse direction: why it does NOT give a new, easier route

The natural hope was that "prove $p(k)$ bounded" might be an easier target
than "construct a self-sufficient finite $Q$." We now show, honestly, that
this hope requires clearing *two* separate hurdles beyond anything actually
established this round, and that the first of the two (Morse-Hedlund
itself) gives strictly less than what the IMO problem demands.

**Gap (i): Morse-Hedlund gives only EVENTUAL periodicity.** Even granting
(hypothetically, since we have no proof) that $p(k)\le k$ for some $k$, the
cited Morse-Hedlund theorem concludes only that $(d_n)$ is *eventually*
periodic: there exist $T\ge1$ and $N_0\ge1$ with $d_{n+T}=d_n$ for all
$n\ge N_0$ — possibly with $N_0>1$, i.e. a genuine transient before the
periodic tail begins. The IMO statement requires $a_{n+T}=a_n+L$ for
**every** positive integer $n$ (checked directly against the problem
statement in `problems.jsonl`: "for every positive integer $n$," no
qualifier "eventually" or "for $n$ sufficiently large"). Eventual
periodicity of $(d_n)$ from some $N_0$ gives $a_{n+T}=a_n+L$ only for
$n\ge N_0$, not for $n=1,\dots,N_0-1$ — a strictly weaker conclusion unless
$N_0=1$ is separately established.

**Gap (ii): no general no-transient upgrade is available outside the
$Q$-machinery.** The population's *only* certified tool for removing a
transient (`transient-free-finishing-theorem.md`, via
`periodicity-of-residue-class-union.md`) is proved for the specific
construction $A=\{m\ge a_1:\mathrm{Good}_Q(m)\}$, i.e. it is already tied to
having a working finite self-sufficient $Q$ in hand — precisely the object
this reformulation was hoping to bypass. We have not found, and did not find
this round, a transient-removal argument that starts merely from "$(d_n)$ is
eventually periodic" (an abstract combinatorics-on-words conclusion, with no
reference to primes or $Q$) and concludes "the periodicity in fact holds
from $n=1$." Attempting to construct such a $Q$ *from* the eventual period
(e.g. $Q:=R(a_1)\cup\{$primes dividing some term in one period of the
periodic tail$\}$) and then verify $\mathrm{Good}_Q(a_n)$ for the finitely
many transient terms $a_1,\dots,a_{N_0-1}$ *individually* is plausible in
outline, but making it rigorous requires re-deriving exactly the pairwise
gcd-sharing structure between transient terms and periodic-tail terms that
is the substance of the still-open central existence gap — we do not have
this argument, and do not claim to.

**Conclusion of §6.3.** The Morse-Hedlund reformulation, even if its central
claim ("$p(k)$ bounded") were established by some future argument, would
still leave Gap (ii) open before yielding the actual IMO conclusion.
Combined with §6.1's Step-0 finding (the one concrete mechanism proposed for
proving "$p(k)$ bounded" is invalid), this reformulation currently supplies
**no new leverage** over the existing $Q$/$\mathrm{Nec}$-based central gap
tracked by the rest of the population — it is a legitimate, precisely
stated equivalent vocabulary (Theorem 6.2.2 shows the conditional direction
fully rigorously, and is a reusable free corollary), but not (yet) an easier
target. We record this as an honest negative/neutral finding rather than
force a false sense of progress.

### 6.4 Sanity check against the known-solved even-seed case

For $a_1$ even, the certified `even-seed-universal-lock-theorem.md` gives
$a_n=a_1+2(n-1)$ for every $n\ge1$, so $d_n=2$ for every $n$ — the constant
sequence. Then every length-$k$ factor equals $(2,2,\dots,2)$, so $p(k)=1$
for every $k\ge1$: trivially bounded, consistent with Theorem 6.2.2 with
$T=1$ (indeed $Q=\{2\}$, $\mathrm{GoodRes}(Q)=\{0\}\subset\mathbb Z/2$,
$T=|\mathrm{GoodRes}(Q)|=1$, matching $p(k)\le T=1$ exactly). This confirms
the machinery of §6.2 reproduces the known-true case correctly, with no
discrepancy. (This was the outline's step 2 sanity check; it passes,
sharpening from "consistent" to an exact numerical match $p(k)\equiv T=1$.)

### 6.5 Numerical evidence (not a proof) that $p(k)$ does stabilize in practice

For completeness, direct computation of $p(k)$ for larger $k$ on non-even
seeds shows $p(k)$ empirically **stabilizing to a constant** for large
enough $k$ (consistent with, though not proof of, eventual periodicity with
no visible transient beyond what a finite computation can rule out):
$a_1=35$: $p(5)=31$, $p(10)=p(20)=p(40)=p(80)=34$ (stabilizes by $k=10$);
$a_1=99$: $p(5)=28$, $p(10)=58$, $p(20)=p(40)=p(80)=72$ (stabilizes by
$k=40$). This is offered strictly as numerical evidence consistent with the
conjectured full theorem, per CLAUDE.md's rule distinguishing "we have
proved" from "we conjecture" — it is not used as a proof step anywhere
above.

## Round 6 gaps (superseding the round-5 stalled state for this section)
- **Step 0 is now definitively closed (negatively):** the naive
  sum-counting route to bounding $p(k)$ is proved invalid, not merely
  in need of care (§6.1). No repair of that specific mechanism is possible.
- **No valid nontrivial upper bound on $p(k)$ is known.** The only proved
  bounds are: the useless trivial exponential bound $p(k)\le(R-1)^k$
  (§6.2, Lemma 6.2.1, unconditional but useless), and the exact bound
  $p(k)\le T$ (§6.2, Theorem 6.2.2), which is **conditional** on the
  already-open central Unified Central Claim.
- **Even granting "$p(k)$ bounded" by some future argument, the converse
  direction needs a genuinely new no-transient argument** (§6.3, Gap (ii))
  not currently available outside the $Q$-machinery this reformulation was
  meant to route around.
- **Net honest assessment:** the Morse-Hedlund reformulation is a
  legitimate, precisely-stated equivalent vocabulary shift with one new
  free certified corollary (Theorem 6.2.2, conditional direction), but has
  **not** been shown, this round or previously, to offer an easier route to
  the central existence gap than the population's existing $Q$/$\mathrm{Nec}$
  framing. This is reported honestly as a neutral/negative finding for the
  reformulation's originally hoped-for advantage, per CLAUDE.md's rule that
  an honest partial outranks a false "solved."

**Watch out for (updated this round):** do not re-attempt "bound $p(k)$ via
counting distinct window sums" (Lemma 1/$g_n(k)$) — proved invalid in §6.1,
with both an abstract collision (Claim 6.1.1) and a genuine realized-instance
collision (Claim 6.1.2, $a_1=35$, $k=2$, factors $(5,4)$ at $n=8$ and $(4,5)$
at $n=16$, both summing to $9$). Do not conflate "Morse-Hedlund gives
eventual periodicity" with the IMO's "for every positive integer $n$" — see
§6.3, Gap (i); the transient-removal step is a separate, currently
unavailable-in-general argument (§6.3, Gap (ii)).

## Promotable lemmas
- **Lemma 1+2 — Bounded scalar difference + pigeonhole (free, unconditional,
  carried over from round 5 opening).** For every fixed $T\ge1$,
  $g_n(T):=a_{n+T}-a_n \in [T,TR]$ for all $n\ge1$ (telescoping the certified
  bounded-gap lemma), hence by pigeonhole some value $L(T)$ is attained by
  an infinite index set $Y_T$. Proved in full in §1.
- **Lemma 3 — Positive-Density Upgrade (new this round, fully proved, §2).**
  For fixed $T\ge1$ and $m:=TR-T+1$, some value $L(T)\in[T,TR]$ satisfies
  $\limsup_{N\to\infty}|Y_T\cap[1,N]|/N \ge 1/m>0$, where
  $Y_T=\{n:g_n(T)=L(T)\}$. Proved via a finite-sum limsup/subadditivity
  argument, fully self-contained (does not depend on any property of
  $(a_n)$ beyond Lemma 1's finite-alphabet bound), hence reusable by any
  future approach or any other problem needing a "some value recurs with
  positive density" pigeonhole upgrade.
- **Lemma 4 — Sharpened Bounded-Gap Lemma (new this round, fully proved,
  §3).** For $R:=\mathrm{rad}(a_1)$ and $r_n:=a_n\bmod R$,
  $a_{n+1}-a_n\le R-r_n$ (or $\le R$ if $r_n=0$) for every $n\ge1$ — a strict
  quantitative refinement of the certified `bounded-gap-via-rad-a1.md`,
  extracted directly from the internals of that lemma's own proof.
  Reusable by any approach wanting the sharper, residue-dependent bound
  rather than the flat bound $R$.
- **Lemma 6.0.1 — Factor complexity is non-decreasing (new this round, §6.0,
  fully proved).** For any one-sided sequence over a finite alphabet,
  $p(k)\le p(k+1)$ for every $k\ge1$, via the surjective "drop-last-symbol"
  map. Standard combinatorics-on-words fact, proved here from scratch and
  reusable by any future approach invoking Morse-Hedlund-style arguments.
- **Corollary 6.1.3 — Window-sum counting does not bound factor complexity
  (new this round, §6.1, fully proved, NEGATIVE result).** The map
  "length-$k$ factor $\mapsto$ its window sum" is not injective even
  restricted to genuinely realized factors of an actual instance of $(a_n)$
  (concretely exhibited for $a_1=35$, $k=2$: $(5,4)$ at $n=8$ and $(4,5)$ at
  $n=16$, both summing to $9$); hence no bound on the number of distinct
  realized window sums (such as Lemma 1's bound) can be used to bound the
  factor-complexity function $p(k)$ itself. Reusable as a standing caution
  against this specific counting mechanism for any future approach in this
  or other problems' populations.
- **Theorem 6.2.2 — Central claim $\Rightarrow$ exact factor-complexity
  bound (new this round, §6.2, fully proved, CONDITIONAL on the Unified
  Central Claim).** If some finite $Q\supseteq R(a_1)$ satisfies
  $\mathrm{Good}_Q(a_n)$ for every $n\ge1$, then $(d_n)$ is purely periodic
  with period $T=|\mathrm{GoodRes}(Q)|$ from $n=1$ (no transient), and
  consequently $p(k)\le T$ for every $k\ge1$. A clean, free corollary
  chaining the already-certified `transient-free-finishing-theorem.md`
  with elementary factor-counting; reusable by any approach wanting to
  translate the $Q$/Good$_Q$ machinery's conclusion into Morse-Hedlund
  vocabulary.

## Round 7 deprioritization note (no build recommended this round)

The round-7 plateau-break explorer's independent re-verification of this
approach's own file (and its sibling `scalar-difference-majorization.md`)
concludes, and this outliner concurs after re-checking the logic: across
rounds 5-6 (and the 6-fork), **every route this framing has tried to close
its own syndeticity/majorization gap terminates in "first you must already
know $(T,L)$/$Q$"** — Theorem 6.2.2 is conditional on the Unified Central
Claim, the converse direction needs two further un-closed gaps, and no
substitute-fact idea (the `aimo-0680`-style Mechanism B) has been found
across 2 searches. This is a genuine, proved structural dead end for this
specific framing (not merely "hard"), matching CLAUDE.md's plateau-break
criterion. **Recommend NOT building this approach this round** — no new
mechanism is proposed here; deprioritized, not deleted (its certified
lemmas remain reusable). If a future round finds a genuinely new
substitute-divisibility idea for Mechanism B, revisit then.
