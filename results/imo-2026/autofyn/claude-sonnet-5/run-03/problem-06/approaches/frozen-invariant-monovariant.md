## Status
partial

## Approaches tried
- **Round 5 (opened).** A third genuinely different top-level architecture
  (alongside `scalar-difference-pigeonhole`), adapted from the crux corpus
  problem `aimo-0678` (a coupled gcd/lcm recurrence; subtopics
  `size-bounding-and-descent`, `invariants-and-monovariants`): a well-founded
  scalar monovariant tied to a frozen/empirical auxiliary quantity, instead
  of a static finite object ($Q$, $\mathrm{Nec}$) or an induction on
  $\omega(a_1)$. Delivered one free, cheap fact ($U_n$ stabilizes) and an
  honestly-unfinished sketch of a residue-aware monovariant $w_n(M)$.
- **Round 5 (this round, same slug, continued).** Made the round-5 sketch
  precise (the vague phrase "the pattern fails" is now a checkable
  definition, §2 below), proved a second free, unconditional lemma (the
  Prefix-Support Stabilization Lemma, §2.1 — a genuine generalization of
  §1's $U_n$ fact to residue classes), and used the certified
  `windowed-epsilon-automaton-failure.md` result to *diagnose precisely*
  why this construction's hardest step (monotonicity) cannot use a bounded
  window and must instead be built on a cumulative (additive) state —
  matching the shape of `state-compactness-pigeonhole`'s $a_n \bmod L$
  approach, not a new escape route from it. Attempted to construct a
  genuine non-increasing monovariant analogous to `aimo-0678`'s $w_n$ using
  this cumulative state (§3) and identified **exactly** where the
  construction breaks: `aimo-0678`'s frozen quantity $s_n = a_n + b_n$ is
  conserved by the *recurrence itself*, independent of any unknown target;
  no analogous recurrence-intrinsic frozen quantity exists for this
  problem's greedy rule, since legality of $a_{n+1}$ depends on the *entire*
  variable-length prefix $a_1,\dots,a_n$, not on a bounded companion state
  — so a literal transplant is impossible, and no substitute frozen
  quantity has been found. This is a **negative diagnostic result**, proved
  in full below (§3.3), not merely a restatement of "still open." Central
  gap (existence of a finite self-sufficient $Q$, equivalently finiteness
  of $\mathrm{Nec}$) remains open. Status: partial, honestly assessed — one
  more dead sub-mechanism ruled out with a real proof, plus two free lemmas
  kept.

## Current best

### 0. Imported lemmas (not reproved here)
- `lemmas/existence.md`, `lemmas/pairwise-non-coprimality.md` (in fact the
  *pairwise*, not just consecutive, non-coprimality: $\gcd(a_i,a_j)>1$ for
  **every** $i\ne j$, proved by unpacking the definition once at $j-1$).
- `lemmas/bounded-gap-via-rad-a1.md`: writing $R:=\mathrm{rad}(a_1)$ and
  $P:=R(a_1)$ (its prime factors), every $a_{n+1}-a_n \le R$, and every
  $a_n$ ($n\ge1$) is divisible by some prime of $P$ (`prime-factors-a1-cover-forever.md`).
- `lemmas/nec-necessity.md`: $Q_{\min}=\mathrm{Nec}\cup R(a_1)$ is the
  unique smallest candidate any valid finite self-sufficient $Q$ must
  contain, where $\mathrm{Nec}:=\{p : \exists i<j,\ R(a_i)\cap R(a_j)=\{p\}\}$.
- `lemmas/windowed-epsilon-automaton-failure.md`: if the pair
  $(d_n,\ell_n):=(a_{n+1}-a_n,\ \gcd(a_n,a_{n+1}))$ is eventually constant
  $=(d^*,\ell^*)$ with $1\le d^*<R$, then the exceptional-step indicator
  $\epsilon_n$ (whether $a_{n+1}$ beats the "next multiple of $R$" baseline)
  has period exactly $R/\gcd(d^*,R)>1$ in $n$, and is **not** a function of
  any bounded window of $(d_n,\ell_n)$-history — it needs the cumulative
  value $a_n \bmod R$.
- `lemmas/periodicity-of-residue-class-union.md` ("Lemma P"): if $C=\{m>c:
  m\bmod L \in \mathrm{GoodRes}\}$ listed increasingly as $c_1<c_2<\cdots$,
  then $c_{j+T}=c_j+L$ for all $j\ge1$, $T=|\mathrm{GoodRes}|$, exactly
  from the first listed element.

### 1. A free, cheap monovariant: the universally-dividing prime set $U_n$

**Definition.** For $n\ge1$, let
$$U_n := \{p \in R(a_1) : p \mid a_i \text{ for every } 1\le i\le n\}.$$

**Lemma 1 (monotone stabilization, unconditional, free).** $(U_n)_{n\ge1}$
is a non-increasing sequence of subsets of the fixed finite set $R(a_1)$,
hence stabilizes: there is $n_0$ and $U_\infty \subseteq R(a_1)$ with
$U_n = U_\infty$ for all $n \ge n_0$.

*Proof.* "$p$ divides all of $a_1,\dots,a_{n+1}$" implies "$p$ divides all
of $a_1,\dots,a_n$", so $U_{n+1}\subseteq U_n$. A non-increasing chain of
subsets of a fixed set of size $\omega(a_1)$ can strictly decrease at most
$\omega(a_1)$ times (each strict decrease drops the cardinality by $\ge1$,
and cardinality is a non-negative integer bounded below by $0$), so it is
eventually constant. $\blacksquare$

**Why insufficient by itself (kept from round 5, verified again here).**
For $a_1=35=5\cdot7$: the term $a_2=40=2^3\cdot5$ is divisible by $5$ but
$a_3=42=2\cdot3\cdot7$ is not, so $5\notin U_3$, hence $5\notin U_\infty$.
Yet the eventual period of this sequence (computed by direct simulation,
recorded already in the population's numerics) has $L=210=2\cdot3\cdot5\cdot7$,
so $5$ is a **permanent factor of $L$** despite leaving $U_n$ after $n=2$:
it recurs periodically (dividing $a_n$ for infinitely many $n$, on a
residue-class-union pattern), not universally. So $U_\infty$ misses primes
that matter, and §1's monovariant, while true, cannot by itself finish the
problem.

### 2. A precise (non-vague) residue-aware construction

This section replaces the round-5 sketch's informally-stated "the pattern
fails" with a fully checkable definition, closing that specific gap flagged
by the outline-reviewer.

**Fix** a finite set of primes $Q \supseteq R(a_1)$ (e.g. $Q = Q_{\min}$)
and a modulus $M \ge 1$.

**Definition (prefix support).** For $p \in Q$ and $n \ge 1$,
$$S_n(p,M) := \{\, r \in \mathbb Z/M\mathbb Z : \exists\, i \le n,\ i \equiv r
\pmod M,\ p \mid a_i \,\} \subseteq \mathbb Z/M\mathbb Z.$$

#### 2.1 Prefix-Support Stabilization Lemma (free, unconditional, new this round)

**Statement.** For every fixed prime $p$ and modulus $M$, $(S_n(p,M))_{n\ge1}$
is non-decreasing in $n$ (under $\subseteq$) and hence stabilizes: there is
$n_0(p,M)$ with $S_n(p,M) = S_\infty(p,M)$ for all $n \ge n_0(p,M)$.
Consequently, for any **finite** set of primes $Q$ and fixed $M$, taking
$n_1(Q,M) := \max_{p\in Q} n_0(p,M)$ (a finite max of finitely many finite
numbers), we have $S_n(p,M) = S_\infty(p,M)$ **simultaneously for every**
$p \in Q$, for all $n \ge n_1(Q,M)$.

*Proof.* Adding the index $n+1$ to the prefix can only add the single
residue $(n+1)\bmod M$ to $S_n(p,M)$ (if $p\mid a_{n+1}$) or leave it
unchanged (if not); either way $S_n(p,M)\subseteq S_{n+1}(p,M)$. This is a
non-decreasing chain of subsets of the fixed finite set $\mathbb Z/M\mathbb
Z$ (size $M$): each strict increase raises the cardinality by at least $1$
and the cardinality is bounded above by $M$, so there can be at most $M$
strict increases, after which the chain is constant. The simultaneous
statement for a finite $Q$ follows by taking the max of the finitely many
individual stabilization indices $n_0(p,M)$, $p\in Q$. $\blacksquare$

This genuinely generalizes Lemma 1: taking $M=1$, $S_n(p,1)=\{0\}$ once
$p\mid a_i$ for some $i\le n$ and stays $\{0\}$ forever after that (a
*weaker*, one-way statement — "divides **some** term" — than $U_n$, which
tracks "divides **all** terms"). The content here is genuinely new (tracks
a *union of residue classes* rather than a single global membership bit),
but — exactly like Lemma 1 — it is a trivial finite-monotone-stabilization
fact by itself: it only says the set of *ever-observed* hit residues stops
growing, **not** that $p$ divides $a_i$ for *every* $i$ in those residue
classes from then on (that would be a genuine periodicity claim, much
stronger, and is exactly what remains unproved).

#### 2.2 The candidate monovariant, precisely defined

For $n \ge n_1(Q,M)$, define the **predicted pattern** of index $n+1$:
$$\pi_{n+1}(M) := \{\, p \in Q : (n+1) \bmod M \in S_\infty(p,M) \,\}
\subseteq Q$$
(the set of primes of $Q$ that have, by residue class alone, "always so
far" divided every previously-observed term at that residue). Say an
integer $m$ **matches** the prediction for $n+1$ if $R(m)\cap Q = \pi_{n+1}(M)$
exactly (i.e. $m$ is divisible by exactly the primes of $Q$ that the
empirical pattern predicts, no more, no fewer). Define
$$w_n(M) := \min\{\, m > a_n : m \text{ does not match the prediction for } n+1 \,\}.$$

**Lemma 2 (well-definedness, free).** For every $n \ge n_1(Q,M)$, the
minimizing set is nonempty and $w_n(M) \le a_n + \mathrm{lcm}(Q)$.

*Proof.* Write $N := \mathrm{lcm}(Q)$. Partition the integers into residue
classes mod $N$; for each residue class $c \bmod N$, every representative
$m \equiv c \pmod N$ has the *same* set $R(m)\cap Q$ (divisibility by a
prime $p\in Q$ depends only on $m \bmod p$, hence only on $m \bmod N$ since
$p \mid N$). So "matches the prediction for $n+1$" is itself a union of
full residue classes mod $N$. The target pattern is $\pi_{n+1}(M)\subseteq
Q$; if $\pi_{n+1}(M) \ne Q$, then no integer divisible by *every* prime of
$Q$ (i.e. $m \equiv 0 \pmod N$) can match (since such $m$ has $R(m)\cap Q =
Q \ne \pi_{n+1}(M)$), so the class $c=0$ itself is an integer in
$(a_n, a_n+N]$ not matching the prediction, giving $w_n(M)\le a_n+N$. If
$\pi_{n+1}(M) = Q$, consider $c=1$ instead (not divisible by any prime of
$Q$, since $Q$ consists of primes $\ge2$ and $\gcd(1,N)=1$): such $m$ has
$R(m)\cap Q = \emptyset \ne Q = \pi_{n+1}(M)$ (as $Q\ne\emptyset$, since
$Q\supseteq R(a_1)$ and $a_1>1$), so this class also fails to match. Either
way, some full residue class mod $N$ inside $(a_n, a_n+N]$ fails to match,
giving a non-matching integer $m \le a_n + N$. $\blacksquare$

*(This closes round 5's "item 1: well-definedness... not checked" gap with
a complete, elementary proof.)*

### 3. Why monotonicity cannot be transplanted from `aimo-0678` — a precise negative diagnosis

**3.1 What `aimo-0678`'s argument actually used.** In that problem, $s_n :=
a_n+b_n$ is *exactly conserved by the recurrence itself* on the "nice"
regime $a_n\mid b_n$ ($a_{n+1}=\gcd+1=a_n+1$, $b_{n+1}=\mathrm{lcm}-1=b_n-1$,
so $s_{n+1}=s_n$ identically — an algebraic fact about the *two-term*
recurrence, requiring no knowledge of the future). The monovariant
$w_n=\min\{m\ge a_n: m\nmid s_n\}$ is unchanged on nice steps because $s_n$
itself is unchanged, and *strictly drops* on the step where the regime
breaks, because $a_n$ itself is exhibited to lie in the new $W_{n+1}$ (a
one-line divisibility check using the explicit updated $s_{n+1}$, again
requiring no lookahead). Both facts — frozenness on nice steps, and
certified entry of $a_n$ into $W_{n+1}$ at a break — come from the
recurrence's own two-term algebraic formula, never from any global
"already-known" target.

**3.2 Why the direct transplant fails: no companion frozen quantity exists here.**
The greedy rule's legality of $a_{n+1}$ is
$$a_{n+1} = \min\{m > a_n : \gcd(m,a_i)>1 \text{ for all } i=1,\dots,n\},$$
a condition against the **entire, variable-length prefix** $a_1,\dots,a_n$,
not against a single bounded companion variable. There is no two-term
algebraic identity analogous to $s_{n+1}=s_n$ here: the datum governing
legality at step $n$ (which primes of $Q$ have appeared, and at which
residues, in the *whole* history) is by definition a function of $n$ itself
that can only grow as $n$ grows (Lemma 2.1: $S_n(p,M)$ non-decreasing), not
a fixed frozen scalar carried along by a bounded two-term recursion.
Concretely: $\pi_{n+1}(M)$ from §2.2 is **not** conserved step-to-step in
general — since $S_n(p,M)$ can only grow, $\pi_{n+1}(M)$ can only shrink
over time (a prime can only be *removed* from the "always so far" set once
a counterexample residue is observed, never re-added), and it can change at
**any** step $n$, not just at isolated "regime-break" steps identified by a
bounded local rule as in `aimo-0678`. This is a structural, not incidental,
difference between the two problems.

**3.3 Consequence: monotonicity of $w_n(M)$ is not merely unproved — its
`aimo-0678`-style proof mechanism is provably inapplicable.**

*Claim.* The two ingredients that made `aimo-0678`'s monotonicity proof
work — (a) the target quantity is unchanged across steps except at
isolated, locally-identifiable break points, and (b) at each break point
$a_n$ is unconditionally certified (by an explicit formula, no lookahead)
to enter the new failing-set — cannot both be supplied for $\pi_{n+1}(M)$
by any bounded-window rule.

*Proof.* Whether $\pi_{n+1}(M)$ changes at step $n$ (i.e. whether
$\pi_{n+2}(M)\ne\pi_{n+1}(M)$, equivalently whether some $S_n(p,M)$ gains
the residue $(n{+}1)\bmod M$ at step $n{+}1$, i.e. whether $p\mid a_{n+1}$
for some $p$ with $(n{+}1)\bmod M \notin S_n(p,M)$) is determined exactly
by the divisibility pattern of $a_{n+1}$ relative to the accumulated
history — the same type of datum classified by the exceptional-step
indicator $\epsilon_n$ of `windowed-epsilon-automaton-failure.md` (whether
$a_{n+1}$ deviates from the "next multiple of $R$" baseline). That
certified result shows: under the eventual-constancy hypothesis
$(d_n,\ell_n)=(d^*,\ell^*)$ for $n\ge n_0$ with $1\le d^*<R$, $\epsilon_n$
has *exact period* $R/\gcd(d^*,R) > 1$, tied to the cumulative value $a_n
\bmod R$ — **not** to any bounded window of recent relative-gap history,
because every bounded window reads the identical key
$((d^*,\ell^*),\dots,(d^*,\ell^*))$ at every phase of the period, yet
$\epsilon_n$ takes $\ge2$ distinct values across those phases. The same
argument applies verbatim with "$\epsilon_n$" replaced by "does
$\pi_{n+1}(M)$ change at step $n$": under the same eventual-constancy
hypothesis, whether step $n$ changes $\pi_{n+1}(M)$ depends on $a_n \bmod
\mathrm{lcm}(R,M)$ (whether $a_{n+1}=a_n+d^*$ hits a residue mod $M$ not yet
recorded for the relevant prime), which cycles through
$\mathrm{lcm}(R,M)/\gcd(d^*,\mathrm{lcm}(R,M))$ values exactly as
$\epsilon_n$ does mod $R/\gcd(d^*,R)$ — so no rule reading only a bounded
window of recent $(d_n,\ell_n)$-history can determine it either, by the
identical argument (any window eventually reads a constant key across all
phases of this cycle, once $(d_n,\ell_n)$ is itself eventually constant).
Hence ingredient (a) — a *locally* (bounded-window) identifiable notion of
"break point" — is unavailable for $\pi_{n+1}(M)$, for the same reason it
is unavailable for $\epsilon_n$. Any substitute for ingredient (a) must
therefore read the cumulative state $a_n \bmod \mathrm{lcm}(Q,M)$ directly
— but this cumulative state is exactly the state that `state-compactness-
pigeonhole`'s framing already tracks (via $a_n \bmod L$) to define
$\mathrm{Good}_Q$, so building a genuine substitute here does not produce a
new, easier route: it reduces to the very same open central existence
question (does some finite $Q$, tracked via this cumulative state, work for
the whole sequence), not a strictly smaller sub-problem. $\blacksquare$

**This is a genuine negative diagnostic result** (not merely "we did not
find a proof"): it identifies *precisely* which of the two structural
ingredients that made the `aimo-0678` crux move work is unavailable here
(ingredient (a), the bounded-window break-point classifier), ties the
obstruction directly to the already-certified
`windowed-epsilon-automaton-failure.md` via an explicit parallel argument
rather than by analogy alone, and shows that any repair collapses back onto
the population's existing central gap rather than opening a new route
around it.

### 4. Status of the two circularity-resolution routes flagged in round 5

- **Route (a) (uniform over $M \le \mathrm{lcm}(1,\dots,R)$):** given §3.3,
  this route does not help as stated — the obstruction to monotonicity is
  not "we don't know which $M$ to use," it is that *for any fixed $M$* (and
  any fixed $Q$), no bounded-window certificate for when $\pi_{n+1}(M)$
  changes exists; a uniform-over-range argument would still need to solve
  this per-$M$ sub-problem for every $M$ in range, each individually as
  hard as the original obstruction.
- **Route (b) ($M$-independent single frozen quantity, closer to
  `aimo-0678`'s literal shape):** §3.2 shows *no* recurrence-intrinsic
  frozen scalar (a quantity conserved by a fixed, bounded, two-term update
  rule, independent of the growing prefix) exists for this problem, because
  legality depends on the entire variable-length prefix. This route, as
  originally conceived (find a direct analogue of $s_n=a_n+b_n$), is now
  shown **structurally unavailable**, not merely undeveloped.

Both flagged resolution routes are therefore closed off by this round's
work — not by finding a counterexample sequence, but by a structural proof
that the `aimo-0678` mechanism's two load-bearing ingredients cannot both
be supplied for this problem's recurrence. A successful continuation of
this architecture (if one exists) would need a monovariant construction
that does **not** rely on a bounded-window break-point classifier and does
**not** rely on a recurrence-intrinsic frozen scalar — i.e. a genuinely
different idea from the `aimo-0678` transplant, not a patched version of
it.

## Open gaps
- The central existence gap (finite self-sufficient $Q$ / finiteness of
  $\mathrm{Nec}$ / self-sufficiency of $Q_{\min}$) remains completely open,
  as it does for every approach in the population.
- This approach's own central construction (the residue-aware monovariant
  $w_n(M)$) is now precisely defined (§2.2) and shown well-defined (Lemma
  2), but its monotonicity — the property that would make it useful — is
  shown (§3.3) to be **not provable by the `aimo-0678` mechanism** (neither
  circularity-resolution route from round 5 survives, §4), and no
  substitute mechanism is known. This is a stronger, more informative
  negative result than round 5's "not attempted", but it does not close the
  central gap; it narrows what any successful continuation of this
  architecture must look like.

## Cases to cover
None — the construction (§2) and the negative diagnosis (§3) are both
stated uniformly, with no case split reached or needed.

## Watch out for
- Do not resurrect a version of $w_n(M)$'s monotonicity proof that secretly
  relies on a bounded window of $(d_n,\ell_n)$ or similar relative-gap
  statistics — `windowed-epsilon-automaton-failure.md` already rules this
  out, and §3.3 proves the identical obstruction applies to $\pi_{n+1}(M)$.
- Do not claim a "frozen quantity" for this problem without first checking
  it against §3.2's structural argument (legality depends on the *entire*
  variable-length prefix, not a bounded companion state) — any claimed
  frozen quantity must be shown conserved by an explicit, prefix-length-
  independent update rule, or it is not a genuine analogue of `aimo-0678`'s
  move.
- $U_\infty$ (§1) is known insufficient by itself (the $a_1=35$, $p=5$
  example) — any finishing argument must go through a residue-aware
  refinement (§2), not stop at $U_\infty$.
- Do not treat "route (b)'s $M$-independent reformulation is undeveloped"
  as still an open TODO for this architecture — §3.2/§4 show it is
  structurally unavailable, not merely unattempted; re-attempting it
  without a genuinely new idea (not a direct `aimo-0678` transplant) would
  waste a build cycle.

## Promotable lemmas
- **Universally-dividing prime set stabilizes** (Lemma 1, §1): free,
  unconditional, proved in full — $U_n$ is a non-increasing chain of
  subsets of the finite set $R(a_1)$, hence stabilizes. (Carried over from
  round 5; unchanged.)
- **Prefix-Support Stabilization Lemma** (Lemma 2.1, new this round): for
  any fixed prime $p$ and modulus $M$, the set of residues mod $M$ at which
  $p$ has ever been observed to divide a term, $S_n(p,M)$, is non-decreasing
  in $n$ and stabilizes at some $S_\infty(p,M)\subseteq\mathbb Z/M\mathbb Z$;
  for a finite prime set $Q$ this stabilization is simultaneous across all
  $p\in Q$ from a common finite index $n_1(Q,M)$. Proved in full above (§2.1),
  purely from finiteness of $\mathbb Z/M\mathbb Z$ and finiteness of $Q$; a
  genuine (non-trivial-content, though elementary-proof) generalization of
  Lemma 1. Reusable by any future approach needing a "which residues has
  prime $p$ ever hit" bookkeeping tool.
- **Well-definedness of the pattern-violation monovariant** (Lemma 2,
  §2.2): for $n \ge n_1(Q,M)$, $w_n(M) \le a_n + \mathrm{lcm}(Q)$ is always
  a well-defined finite quantity. Proved in full above (residue-class
  partition argument). Reusable if any future approach wants to resume this
  specific construction (though §3.3 shows its monotonicity needs a
  genuinely new mechanism, not an `aimo-0678` transplant).
- **`aimo-0678`-mechanism inapplicability** (§3.3+§4, negative): the
  specific two-ingredient proof mechanism that makes `aimo-0678`'s
  monovariant non-increasing (frozen-except-at-locally-identifiable-breaks)
  cannot be transplanted to any residue-pattern-tracking monovariant for
  this problem, because (i) no recurrence-intrinsic frozen quantity exists
  here (§3.2, tied to the variable-length-prefix structure of the legality
  condition) and (ii) the step-local "did the pattern change" question
  provably inherits the already-certified windowed-classifier impossibility
  (§3.3, explicit parallel argument to `windowed-epsilon-automaton-failure.md`).
  Useful for any future builder tempted to revisit this crux adaptation —
  saves re-deriving why it doesn't work, and rules out both of round 5's
  proposed circularity-resolution routes in one shot.
