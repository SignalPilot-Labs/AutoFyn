## imo-2026-06

### Headline reframe (binding on every approach below)
All three round-1 approaches (and this round's three explorers) converge on
one finding: the round-1 "central gap" — **S := {p : p | a_n for infinitely
many n} is finite** — is not merely unproved, it is **false**, and moreover
it is *inconsistent with the problem's own conclusion*. Proof: if
$a_{n+T}=a_n+L$ for all $n\ge n_0$ (what we must prove), fix a residue class
$n\equiv r\pmod T$, $n\ge n_0$; the values $a_r,a_r+L,a_r+2L,\dots$ form an
AP with common difference $L$. For **any** prime $p\nmid L$, $L$ is invertible
mod $p$, so this AP cycles through every residue mod $p$, hitting $0$ at
least once every $p$ steps — infinitely often. Hence $p\in S$ for every prime
$p\nmid L$: $S$ is cofinite in the primes, i.e. genuinely infinite. This is
confirmed independently by all three explorers' numerics (e.g. $a_1=15$: every
prime $\le 409$ recurs; $a_1=105$: prime 2 saturates to 98%).

**Consequence for the whole population.** Drop "S finite" permanently as a
target — it is refuted, not just hard. The correct finite object is $L$
itself (equivalently, the finite prime set $\mathrm{rad}(L)$), reached by a
**bounded, minimality-driven recruitment process** starting from
$P=\mathrm{rad}(a_1)$, not by an infinite-tail pigeonhole/counting argument
over $S$. Every approach below targets $L$ (or an equivalent finite covering
object) directly, using greedy minimality as an essential ingredient (per the
round-1 negative result: pure counting/pigeonhole on $\omega(a_n)$ or on
gap-size cannot work, confirmed twice more this round).

Two lemmas remain certified and reusable by every approach:
`lemmas/existence.md` (well-definedness), `lemmas/bounded-gap-via-rad-a1.md`
($a_{n+1}-a_n\le R:=\mathrm{rad}(a_1)$, hence $a_n=O(n)$).
`lemmas/every-term-meets-recurring-set.md` is **still true** (every $a_i$ is
divisible by some prime of $S$) but is now understood to be a weak fact about
an infinite set $S$, not a stepping stone to finiteness of $S$; it is not
useless (it still shows $a_i$ is never coprime-covered by "fresh" primes
alone) but no approach should try to leverage it toward "$S$ finite" again.

---

jacobsthal-covering-bound: advance
Target: there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for all $n\ge1$.
Technique: **explicit finite-state construction via a self-sufficiency
stopping criterion** — build the finite "active prime set" $Q$ by an explicit
phase induction from $P=\mathrm{rad}(a_1)$, using a genuine **monovariant**
(not a soft density/counting bound) to prove the induction terminates, then
finish with residue-mod-$L$ pigeonhole for $T$.
Skeleton:
  1. Define, for a nonempty finite prime set $Q$, the covering gap
     $g(Q):=\min(Q)$ (Lemma 1, already proved: every window of length $g(Q)$
     contains an integer divisible by some $p\in Q$) — by `lemmas/bounded-gap-via-rad-a1.md`'s
     method.
  2. Phase induction: $Q_0=P=\mathrm{rad}(a_1)$. At phase $j$, if the greedy
     choice $a_{n+1}$ (for the current frontier $n$) is always realizable
     using only primes of $Q_j$ (i.e. the "next multiple of $\prod Q_j$
     after $a_n$" candidate, which is always $\le a_n+g(Q_j)$ and always
     valid by Lemma 1 combined with "every $a_i$ divisible by some $p\in
     Q_j$", is never beaten by a smaller candidate that uses a prime outside
     $Q_j$), $Q_j$ is *self-sufficient*: stop, set $Q=Q_j$. Otherwise some
     term recruits a genuinely new prime $p_j\notin Q_j$ (because the
     smallest valid candidate at that step happens to be smaller than the
     guaranteed $Q_j$-candidate, and divisible by $p_j$ but by no prime of
     $Q_j$); set $Q_{j+1}=Q_j\cup\{p_j\}$.
  3. **Key Lemma (termination monovariant — the hard new step this round).**
     Any newly recruited prime $p_j$ at phase $j$ must satisfy
     $p_j\le a_n+g(Q_j) - a_n = g(Q_j)$ **is false in general** (rejected in
     explorer notes) — the correct monovariant must instead bound *how many
     times* recruitment can occur, not the size of each recruit. Use:
     each recruitment strictly decreases the "uncovered density"
     $1-d(Q_j)$ where $d(Q_j)=1-\prod_{p\in Q_j}(1-1/p)$, and — the genuinely
     new ingredient — a recruited prime $p_j$ can only ever be used to cover
     a *specific single* historic residue gap, so once $d(Q_j)$ exceeds the
     threshold $1-1/g(Q_j)$-type bound (an explicit, checkable inequality
     comparing $g(Q_j)$ against the density contributed by $Q_j$), no
     candidate using a prime outside $Q_j$ can ever again beat the guaranteed
     $Q_j$-candidate — because the guaranteed candidate is within $g(Q_j)$ of
     $a_n$ deterministically, while any competing outside-prime candidate
     needs to simultaneously satisfy *all* of the (growing) history's
     constraints, which becomes combinatorially harder each phase. Make this
     an explicit finite induction: show $g(Q_{j+1}) \le g(Q_j)$ is not
     required; instead show the number of phases is bounded by $|P|$ plus a
     bounded correction — **this is the step to hand the builder as the
     precise remaining computation**, using the numerically-observed pattern
     (`math-explorer-computational2.md`: $\{2,3\}$ or $\{2,3,5,7\}$ suffice in
     every tested case) as a guide for the shape of the bound, not as a
     substitute for the proof.
  4. Once $Q$ (hence $L=\prod_{p\in Q}p$) is fixed after finitely many phases,
     import the residue-pigeonhole finish (Lemma 3 of
     `active-set-stabilization.md` / Lemma 3 of
     `state-compactness-pigeonhole.md`, both already correct given $L$ finite)
     to get $T$ and finish periodicity for $n\ge n_1$, then extend to $n\ge1$
     (see active-set-stabilization's revised gap 2 below — same fix applies
     here since both approaches then share the identical finishing lemma).
Key lemmas (claim + mechanism):
  - $g(Q)=\min(Q)$ is a valid covering gap — because among any $\min(Q)$
    consecutive integers one is a multiple of $\min(Q)\in Q$.
  - **Self-sufficiency criterion**: once $Q_j$ crosses an explicit density
    threshold, no fresh prime can ever again produce a smaller candidate than
    the guaranteed $Q_j$-candidate — because the guaranteed candidate's
    location is a *fixed, deterministic* function of $a_n$ and $Q_j$ alone
    (next multiple of $\prod Q_j$), whereas a competing fresh-prime candidate
    must additionally clear every one of the (unboundedly many, and growing)
    historic gcd constraints, which only gets harder as history grows.
Open gaps: Step 3 (the termination monovariant / explicit phase-count bound)
is the one real remaining gap in this approach — everything else (Lemma 1,
the finishing pigeonhole in step 4) is already proved elsewhere in the
population and just needs importing.
Cases to cover: prime-power $a_1$ (zero phases, trivial); $a_1$ with a factor
of $2$ (numerically always $T=1,L=2$, likely a one-phase or zero-phase
argument); $a_1$ odd with $\ge2$ distinct prime factors (the hard case,
observed to sometimes take very long transients, e.g. $385$ not stabilized
in 40000 terms — the termination bound must NOT depend on transient length,
only on eventual existence of finite $L$).
Watch out for: do not assume $L=\mathrm{rad}(a_1)$ or any small closed-form
correction — refuted numerically (dropping AND recruitment both occur with
no clean pattern, `math-explorer-computational2.md`). Do not reuse the
round-1 counting argument ($K^2\le N\log_2 a_N$) — already proven insufficient.

---

active-set-stabilization: revise
Target: there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for all $n\ge1$.
Technique: keep the already-correct **finite-state pigeonhole on residues
mod $L$** conditional finish, but (a) retarget Hypothesis H's "$S$ finite"
premise to instead **import** jacobsthal-covering-bound's self-sufficiency
lemma once certified (so this approach becomes: "given jacobsthal's $L$,
finish periodicity" — a genuine division of labor, not duplication, since
jacobsthal supplies $L$ and this approach supplies $T$ + the prefix fix),
and (b) close the flagged secondary gap (extend $a_{n+T}=a_n+L$ from
$n\ge n_1$ down to all $n\ge1$) by **redefining the pigeonhole state from
$n=1$ onward**, per `math-explorer-minimality.md` opening 2's numerical
observation that no prefix-patching was needed in any tested case.
Skeleton:
  1. Import $L=\prod_{p\in Q}p$ finite from jacobsthal-covering-bound (once
     certified) — do not re-derive.
  2. Redefine the state used for pigeonhole to be valid **from $n=1$**:
     $\sigma(n) = (a_n \bmod L,\ \{a_i \bmod L : 1\le i\le n\})$ for **every**
     $n\ge1$ (not just $n\ge N_0$) — this is well-defined immediately since
     $a_n \bmod L$ and the finite history multiset make sense from the start;
     the only reason round 1's write-up restricted to $n\ge N_0$ was because
     $L$ itself wasn't yet known to be finite/fixed, a problem solved by step 1.
  3. $\sigma$ takes values in a finite set ($L\cdot 2^L$ possibilities), so by
     pigeonhole among $n=1,2,3,\dots$ there exist $n_1<n_2$ (both $\ge1$, no
     lower cutoff needed) with $\sigma(n_1)=\sigma(n_2)$.
  4. Induct exactly as in the round-1 write-up (already fully correct once
     $\sigma(n_1)=\sigma(n_2)$ is established from $n=1$): $a_{n_2+j}=a_{n_1+j}+
     \Delta$ for all $j\ge0$, giving $a_{n+T}=a_n+L'$ for **all** $n\ge n_1$
     with $T=n_2-n_1$, $L'=a_{n_2}-a_{n_1}$.
  5. **Extend down to $n<n_1$ without the earlier flawed "multiple of $T$"
     trick**: instead, apply the *same* pigeonhole state argument but seeded
     at $n=1$ specifically — i.e. show $\sigma(1)$ itself recurs (there exists
     $n_2'>1$ with $\sigma(n_2')=\sigma(1)$, since $\sigma$ has finitely many
     values and takes value $\sigma(1)$ at $n=1$, so by the pigeonhole
     argument in step 3 applied to the sub-orbit starting exactly at $n=1$,
     some later index repeats it — this is the same pigeonhole, just anchored
     at the smallest index instead of an arbitrary large one). This gives
     $a_{1+T_1}=a_1+L_1'$ directly, and one more induction shows
     $a_{n+T_1}=a_n+L_1'$ for **all** $n\ge1$ (the induction of step 4 applies
     verbatim starting from $n=1$). Take $T=T_1$, $L=L_1'$ (a common multiple
     of the two witnesses if they differ, via one further gcd/lcm step, is a
     routine, fully explicit finish — not the vague "choose $k$" argument that
     failed in round 1).
Key lemmas: same self-sufficiency-derived $L$ (imported from
jacobsthal-covering-bound), plus the (now for-real "from $n=1$") pigeonhole
recurrence of $\sigma$.
Open gaps: depends entirely on jacobsthal-covering-bound's Key Lemma (step 3
there) being closed; the finish here (steps 2–5) is otherwise complete
modulo carefully writing out step 5's "anchor pigeonhole at $n=1$" argument,
which is routine but must actually be written (not asserted).
Cases to cover: none beyond jacobsthal's.
Watch out for: do not repeat round 1's "choose $k$ large enough" prefix
patch — it was shown (round 1, honestly) not to close; the fix here is to
run the *same* pigeonhole mechanism anchored at $n=1$, not to multiply $T$.

---

state-compactness-pigeonhole: revise
Target: there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for all $n\ge1$.
Technique: pivot away from duplicating active-set-stabilization's residue
pigeonhole (too close in mechanism — both proved the identical conditional
finish in round 1) toward the genuinely different **complement-set framing**
(`math-explorer-altframe.md` opening 4): study $B:=\mathbb Z_{>1}\setminus
\{a_n\}$ (the "rejected" integers) instead of the sequence itself, and show
$B$ is eventually a **finite union of full residue classes mod some $L$**
directly — periodicity of $(a_n)$ then follows for free (the accepted
sequence is exactly the increasing enumeration of the complement of $B$).
Skeleton:
  1. By `lemmas/bounded-gap-via-rad-a1.md`, every window $(x,x+R]$
     ($R=\mathrm{rad}(a_1)$) contains an accepted term, so $B$ has bounded
     gaps too and density $<1$ in every long window — a purely
     complement-side restatement of the certified lemma, no new content yet.
  2. **Key reduction.** $m\in B$ (i.e. $m$ is skipped) iff $m\le a_1$, or $m$
     fails the gcd test against some earlier accepted term, i.e.
     $\gcd(m,a_i)=1$ for **all** $i$ with $a_i<m$ — i.e. $m$ is coprime to
     every term accepted so far. Equivalently, using $R(m)$ = prime factors
     of $m$: $m\in B$ iff no accepted $a_i<m$ shares a prime factor with $m$.
     Reformulate: define, for each prime $p$, $f(p) := $ the least accepted
     term divisible by $p$ if one exists (else $\infty$); then $m$ is
     accepted iff $m>a_1$ and for every $i\le n$ (equivalently, once we know
     the recurring/active prime set), some prime of $m$ has $f(p)$ already
     "activated" against all constraints — this must be worked out carefully
     (this is the actual new content the builder must supply, not assumed).
  3. **Claim.** Once the same finite prime set $Q$ from jacobsthal's
     self-sufficiency criterion is reached, $B$ restricted to integers
     $>a_{n^*}$ ($n^*$ = the stabilization index) is *exactly*
     $\{m>a_{n^*} : R(m)\cap Q=\emptyset\}$ — a finite union of residue
     classes mod $L=\prod_{p\in Q}p$ (namely all residues coprime to $L$),
     hence *manifestly* eventually periodic as a set with period exactly
     $L$ (a stronger, more transparent periodicity statement than
     "eventually periodic difference sequence," since it's periodicity of a
     *set*, which trivially implies periodicity of its enumeration's
     differences).
  4. From step 3, derive $a_{n+T}=a_n+L$ directly: the accepted sequence
     restricted to $n>n^*$ is the increasing enumeration of
     $\{m>a_{n^*}: \gcd(m,L)>1\}$ — a set manifestly periodic mod $L$ with
     $T=$ number of residues mod $L$ sharing a factor with $L$ (an explicit,
     computable count, $L-\phi(L)$-ish, no separate pigeonhole needed for
     $T$: it falls out of step 3's structural claim).
  5. Extend to $n\le n^*$: same finitely-many-terms fix needed as in
     active-set-stabilization's revised step 5 (shared secondary gap, same
     fix applies).
Key lemmas (claim + mechanism):
  - $B\cap(a_{n^*},\infty) = \{m : \gcd(m,L)=1\}$ once $Q$ is self-sufficient
    — because self-sufficiency (jacobsthal's criterion) means precisely that
    *no* integer coprime to $L$ can ever be accepted past $n^*$ (it would
    have to be validated by some prime outside $Q$ against some historic
    term, impossible once $Q$ is self-sufficient) **and** every integer
    sharing a factor with $L$ that appears after $a_{n^*}$ is accepted
    (because it clears every gcd constraint automatically via its $Q$-factor,
    since every historic term is $Q$-covered).
Open gaps: step 2 (the precise per-$m$ acceptance criterion) and step 3's
"exactly" claim both need genuine proof, not just restatement — in
particular the "every $Q$-sharing $m$ IS accepted" direction requires ruling
out that some smaller non-$Q$-sharing candidate always wins first, which is
circular with jacobsthal's self-sufficiency lemma; so this approach's real
open gap is the *same* self-sufficiency lemma as jacobsthal-covering-bound,
approached from the complement side, offering a second independent route to
close it (or at least a cross-check).
Cases to cover: same as jacobsthal's.
Watch out for: do not conflate "$B$ has bounded gaps" (already known, weak)
with "$B$ is eventually periodic as a set" (the real claim, unproven) — the
former does not imply the latter without the self-sufficiency argument.

---

growth-rate-contradiction: revise
Target: there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for all $n\ge1$.
Technique: pivot its already-certified bounded-gap machinery toward a
**quantitative cost-comparison / density-of-small-primes** argument
(`math-explorer-altframe.md` opening 3, `math-explorer-minimality.md` opening
3), replacing its refuted "bound the count of freshly recruited primes"
mechanism with a directional inequality: show that once the active set $Q$
covers a high enough density, using an active prime is *always* strictly
cheaper (produces a smaller candidate) than any fresh prime larger than an
explicit threshold depending on $Q$ — i.e. attack the same self-sufficiency
threshold as jacobsthal, but via an explicit two-candidate size inequality
rather than a phase-count induction, as an independent check / alternative
route.
Skeleton:
  1. Reuse `lemmas/bounded-gap-via-rad-a1.md` verbatim: $a_{n+1}-a_n\le R$
     always, $R$ fixed.
  2. **New Key Lemma (quantitative threshold, the actual new content).** Fix
     $n$ and a finite active set $Q$ known to cover every $a_i$, $i\le n$
     (i.e. $R(a_i)\cap Q\ne\emptyset$ for all $i\le n$; true for $Q\supseteq
     \mathrm{rad}(a_1)$ by the bounded-gap lemma's own Fact). Let
     $M_Q$ = least multiple of $\prod_{p\in Q}p$ exceeding $a_n$ (a
     guaranteed valid candidate, $M_Q\le a_n+\prod_{p\in Q}p$ trivially but
     in fact $\le a_n+g(Q)$ using the sharper covering gap $g(Q)=\min(Q)$).
     Claim: **any prime $p_0\notin Q$ can only ever produce a smaller
     candidate than $M_Q$ if $p_0$ divides some integer in the (short,
     length-$g(Q)$) window $(a_n,M_Q)$ that is ALSO divisible by enough of
     $Q$'s complementary structure to clear every other historic constraint
     — an event of "density" $\le 1/p_0$ within that window** — so as $Q$
     grows and $g(Q)$ shrinks, the window shrinks, and only smaller and
     smaller primes $p_0<g(Q)$ can possibly beat $M_Q$; once $g(Q)$ falls
     below the least prime not in $Q$, recruitment is structurally
     impossible. This inequality (precise form: a fresh-prime candidate
     $m<M_Q$ forces $p_0\mid m$ with $a_n<m<a_n+g(Q)$, hence $p_0\le
     m-a_n<g(Q)$, i.e. **$p_0<g(Q)$ is a genuinely NECESSARY condition for a
     new recruit** — note this direction is correct and different from the
     false converse rejected in jacobsthal's write-up) gives an **explicit,
     checkable, and correct** upper bound on any freshly-recruitable prime
     at each phase: $p_0 < g(Q_j)$.
  3. Since $g(Q_j)=\min(Q_j)$ is bounded (by $\min(P)\le R$) and only
     decreases or stays the same-order as $Q_j$ grows (adding a new small
     prime can only decrease $\min(Q_j)$, and once $\min(Q_j)$ is already the
     smallest possible prime 2, no further shrinkage is possible), the
     sequence of newly recruited primes $p_0<p_1<\dots$ is bounded above by
     the FIXED constant $\min(P)$ (or 2, whichever is reached first) —
     hence **only finitely many distinct primes can ever be recruited**
     (all recruits satisfy $p_j < g(Q_j) \le \min(P)$, a fixed finite bound
     independent of $j$), closing the central gap **unconditionally and
     explicitly**, without an abstract density/potential argument.
  4. Once the recruitment process is shown finite (step 3), finish exactly
     as active-set-stabilization's revised residue-pigeonhole argument.
Key lemmas (claim + mechanism):
  - **$p_0<g(Q_j)$ is necessary for recruitment** — because the recruited
    candidate $m$ must beat the guaranteed $Q_j$-candidate $M_{Q_j}\le
    a_n+g(Q_j)$, so $m-a_n<g(Q_j)$, and since $p_0\mid m$ with $m\le a_n+
    p_0\cdot k$ for some $k\ge1$... **caution:** this step needs $p_0 \mid m$
    to force $p_0 \le m - a_n$ only when $m$ is the FIRST multiple of $p_0$
    exceeding $a_n$; if $m$ is a later multiple this bound fails. This is
    the one place the argument in step 2 needs to be tightened by the
    builder — flagged explicitly as a possible hole, not glossed over.
Open gaps: Step 2's inequality as stated may only bound the *first* time
$p_0$ could be used, not rule out $p_0$ being used via a later multiple;
the builder must either (a) show the greedy process only ever recruits via
the *first* available multiple (plausible, since minimality always takes
the smallest candidate — worth checking against the certified bounded-gap
lemma's proof method) or (b) find the correct quantitative substitute.
This is a real, not yet closed, gap — but a strictly more concrete one than
round 1's abstract "self-sufficiency" phrasing, and gives the builder an
explicit inequality to either prove or refute computationally first.
Cases to cover: same as jacobsthal's; additionally must check the borderline
case $Q_j=\{2\}$ already (no smaller prime exists, so recruitment must have
already stopped) as a sanity floor.
Watch out for: do not repeat the round-1-refuted "bound freshly recruited
primes via gap-size" mechanism verbatim — that bounded gap size given a
fixed recruit, the wrong direction; this revision bounds the recruit's size
given the (already fixed, structural) gap $g(Q_j)$, the correct direction,
per the negative result recorded in `growth-rate-contradiction.md`.

---

bounded-window-tournament: new
Target: there exist $T,L\ge1$ with $a_{n+T}=a_n+L$ for all $n\ge1$.
Technique: **direct explicit construction** (no abstract compactness /
pigeonhole at all) — treat the choice of $a_{n+1}$ as a finite "tournament"
each step among at most $R=\mathrm{rad}(a_1)$ many literal candidate
integers (already guaranteed by `lemmas/bounded-gap-via-rad-a1.md` to lie in
the window $(a_n,a_n+R]$), and track a genuinely finite, explicit
combinatorial state (not a soft potential) that determines the winner.
Skeleton:
  1. By the bounded-gap lemma, $a_{n+1}\in(a_n,a_n+R]$ always: a window of
     at most $R-1$ literal candidates. Minimality: $a_{n+1}$ is the least
     $m$ in this window with $\gcd(m,a_i)>1$ for all $i\le n$.
  2. For each $n$, define the **rejection pattern** $\rho(n):\{1,\dots,R\}\to
     \{0,1\}$ where $\rho(n)(k)=1$ iff $a_n+k$ is a valid candidate for
     $a_{n+1}$'s "successor pool" (i.e. would satisfy every historic gcd
     constraint if reached) — this is a fixed-size ($2^R$-valued) piece of
     data at each $n$, **not requiring knowledge of the infinite history
     directly**, because whether $a_n+k$ clears constraint $i$ depends only
     on $\gcd(a_n+k,a_i)$, and (key claim, to prove) this in turn depends
     only on $a_n+k \bmod \mathrm{rad}(a_i)$ — since $\mathrm{rad}(a_i)$'s
     prime factors are what matter, and by Lemma 2 (every-term-meets-S) each
     $a_i$ shares a prime with the growing active set, the relevant modulus
     across all $i\le n$ stabilizes to a bounded set of primes actually used.
  3. **Key Lemma (state boundedness — the load-bearing new claim).** The map
     $n\mapsto \rho(n)$ (restricted to which of the finitely many candidates
     $a_n+1,\dots,a_n+R$ are blocked by *some* historic constraint) takes
     values in a set of size at most $2^R$ (trivially finite), so by
     pigeonhole two indices $n_1<n_2$ share $\rho(n_1)=\rho(n_2)$ — BUT the
     real content needed is that $\rho(n)$ together with $a_n\bmod L$ (for
     the eventual $L$) actually determines $a_{n+1}-a_n$ **deterministically
     forward**, which requires showing $\rho$ is itself eventually constant
     (not just recurring), because a merely-recurring $\rho$ does not yet
     give a forward-deterministic dynamical system (that needs the FULL
     future rejection pattern, not just a snapshot, to match) — this is
     exactly the same "state = residue mod L" content as
     active-set-stabilization's Hypothesis H, but framed here as a
     finite-window combinatorial object instead of a residue-multiset,
     giving a possibly more tractable/explicit object for the builder to
     bound directly (e.g. by relating $\rho(n)$ to $a_n \bmod L$ once $L$ is
     known from jacobsthal, showing $\rho(n)$ is literally a function of
     $a_n \bmod L$ alone once the active set stabilizes).
  4. Once $\rho$ is shown to stabilize (or be periodic) as a function of
     $a_n\bmod L$, periodicity $a_{n+T}=a_n+L$ follows immediately and
     explicitly with $T$ = size of the resulting cycle among residues mod
     $L$ — no separate abstract pigeonhole needed beyond the finite check
     of $\rho$ vs. residue.
Key lemmas: same self-sufficiency content as jacobsthal / active-set, but
packaged as an explicit finite bit-vector $\rho(n)\in\{0,1\}^{R}$ rather than
an abstract prime set or residue multiset — this is a genuinely different
bookkeeping device (bounded window contents, directly computable/checkable
on small examples) that may be easier for the builder to verify by explicit
small-case computation (e.g. $a_1=15$: $R=15$, $\rho$ has only $2^{15}$
possible values, small enough to literally simulate and check convergence).
Open gaps: step 3 (showing $\rho$ becomes a pure function of $a_n \bmod L$,
not just eventually-recurring) is the whole content; this is a reformulation
of the central gap, offered as an alternative, more concrete/checkable
bookkeeping route, not a solved gap.
Cases to cover: same as jacobsthal's; use $a_1=15$ or $35$ as the worked
small example to sanity-check $\rho$'s behavior directly by computation
before generalizing.
Watch out for: $\rho(n)$ as defined depends a priori on the WHOLE history
$i\le n$, not just a bounded window — the claim that it reduces to a bounded
function of $a_n \bmod L$ needs the same self-sufficiency content as the
other approaches; don't let the builder assume this reduction for free.

---

Note on the profinite/compactness framing (`math-explorer-altframe.md`
opening 2): not opened as a slug this round — it introduces a new,
unverified "the limit residue configuration must be rational" gap that is
not obviously easier than the current central gap, and no concrete
mechanism was found to close it. Keep in reserve if all five approaches
above stall for another round, but do not dilute the field with it now.
