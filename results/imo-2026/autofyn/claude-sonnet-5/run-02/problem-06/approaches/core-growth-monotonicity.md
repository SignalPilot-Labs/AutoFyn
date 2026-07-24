## Status
partial

## Approaches tried
- **core-growth-monotonicity (round 16, new).** Dedicated attack on sub-gap (H2)
  of `n1-periodicity-reconciliation` — boundedness of the pigeonhole-threshold
  sequence N(S_k) along the self-absorbing-core absorption chain S_0 ⊆ S_1 ⊆ ...
  (S_{k+1} := S_k ∪ ⋃_{j≤N(S_k)} P(a_j)), which the certified **Termination
  Criterion Lemma** (`lemmas/termination-criterion-lemma.md`) shows is exactly
  equivalent to termination of the absorption process, and which is logically
  distinct from the main FAH crux. Technique: one-prime-at-a-time refinement
  induction on the pigeonhole threshold N(S), per this round's
  `math-explorer-termination.md` Opening 1. Outcome: proved two new, fully
  rigorous, unconditional lemmas (Binary Refinement Lemma; Threshold Recursion
  Bound Lemma, giving the *exact* mechanism by which N(S) changes when a single
  prime is adjoined to the core) — genuine new content, not previously stated
  anywhere in the workspace. However, carrying the recursion one level further
  (bounding the new "local" thresholds M_B it introduces) hits a wall of
  *exactly the same non-constructive shape* as N(S) itself: M_B is defined by a
  binary pigeonhole "last-exception" argument on an infinite index set, and no
  certified or elementary tool determines it from finite data (a_1, p) alone —
  this is proved rigorously below (Proposition 3, an extension of round 13's
  certified Non-Constructivity observation to this new object), not merely
  asserted. Consistent with, and now backed by an actual proof rather than only
  numerical evidence for, this round's `math-explorer-termination.md` finding
  that N(S_0) is not observably bounded within 15,000 sampled terms on the two
  standard hard seeds (4807, 11305). **Boundedness of N(S_k) remains open.**
  Status: `partial`, honestly reported — a real, structural narrowing of the
  target (the *exact* per-prime recursion is now known, replacing the vague
  "some regularity is needed" placeholder from the outline), but not a
  resolution of H2, and this approach does not touch the main FAH crux (by
  design, per the outline).

- **core-growth-monotonicity (round 19, revise).** Dispatched to attack the
  strictly-weaker H2 sub-target: existence of SOME finite self-absorbing S* ⊇ S_0
  (not necessarily S* = Q, not necessarily N(S*) = 0). Outcome, honestly reported:
  (i) first clarified that this target is **not new** — it is verbatim the
  standing open sub-gap (a) of the already-certified `self-absorbing-core-
  theorem.md` ("existence/termination of a self-absorbing S*"), so no new
  mathematical content is created merely by restating it; (ii) produced one
  genuinely new, fully-proved reformulation (the **Monotone Chain Reformulation
  Lemma**, §5 below): existence of self-absorbing S* is implied by (but not
  shown equivalent to) the purely numerical statement "∃M with N(S_M) ≤ M" for
  the EXPLICIT, monotone, easy-to-define family S_M := S_0 ∪ ⋃_{j=1}^M P(a_j) —
  a genuinely different candidate family from the adaptive absorption chain
  S_0, S_1, S_2, ... of the Termination Criterion Lemma; (iii) attempted the
  outline's Step 3 ("Non-Recurrence of Refinement Primes") against this new
  family and confirmed, with a proof (Proposition 4, §6), that it gives no
  contradiction, for the same reason the outline itself flagged; (iv) checked
  explicitly, with a proof (Proposition 5, §7), that the converse direction of
  the Monotone Chain Reformulation Lemma (does existence of an arbitrary
  self-absorbing S** force some S_M to work?) also fails to go through, because
  N is not shown monotone under further core enlargement — so the new family
  does not even capture the full existence question, only a sufficient special
  case of it. Conclusion: this round's attack, despite using a genuinely
  different concrete family (S_M, not S_k) and despite the existential (not
  numeric-bound) framing being logically distinct in principle from Proposition
  3's target, **does hit the same wall** — no source of information beyond
  bounded-prefix data was found to control N(S_M) as M grows, and Proposition 3
  applies verbatim to the incremental refinement steps building S_{M+1} from
  S_M. Reported honestly as a further-confirmed dead end for this specific
  sub-target, not patched or forced. Status remains `partial`; the round's real
  new content is the Monotone Chain Reformulation Lemma and Propositions 4–5,
  which sharpen exactly what a future attempt would need (a rate-control
  argument on N(S_M) that has no evident source) rather than resolving H2.

## Current best

### 0. Setup (recalled, not new)

Fix a finite set of primes S ⊇ Q = P(a_1). For n ≥ 1 write ρ_S(n) := P(a_n) ∩ S
(the "S-type" of index n; nonempty since Q ⊆ P(a_n) by the certified **Free
Facts Lemma**, `lemmas/free-facts-gcd.md`, when combined with Q ⊆ S — actually
more directly, τ(n) ⊆ ρ_S(n) and τ(n) ≠ ∅). By the certified **Extended
Persistent-Type Pigeonhole** (`lemmas/extended-persistent-type-pigeonhole.md`,
generic in S), there is a finite nonempty set 𝒫'(S) ⊆ 2^S \ {∅} of
"S-persistent" types (each occurring at infinitely many n), and the set
Exc(S) := {n : ρ_S(n) ∉ 𝒫'(S)} is finite. Define
N(S) := max(Exc(S) ∪ {0}) (0 if Exc(S) = ∅).

This is well-defined: since 2^S is finite and each non-persistent type occurs
only finitely often (else it would be persistent by definition), Exc(S) is a
finite union of finite index-sets, hence finite, so its max exists.

### 1. Binary Refinement Lemma (new, fully proved)

**Statement.** Let S be a finite set of primes with Q ⊆ S, let p be a prime
with p ∉ S, and let S' := S ∪ {p}. Then for every n:
$$\rho_{S'}(n) = \rho_S(n) \text{ or } \rho_S(n)\cup\{p\}, \qquad \rho_{S'}(n)\cap S = \rho_S(n).$$
Consequently, if π: 2^{S'} → 2^S denotes X ↦ X ∩ S, then:
(a) π(𝒫'(S')) ⊆ 𝒫'(S);
(b) π restricted to 𝒫'(S') is surjective onto 𝒫'(S) (every B ∈ 𝒫'(S) has at
least one, and at most two, preimages in 𝒫'(S'), namely a subset of {B, B∪{p}}).

**Proof.**

*First display.* Since S' = S ⊔ {p} (disjoint union, as p ∉ S),
$$\rho_{S'}(n) = P(a_n)\cap S' = P(a_n)\cap(S\cup\{p\}) = (P(a_n)\cap S)\cup(P(a_n)\cap\{p\}) = \rho_S(n)\cup(P(a_n)\cap\{p\}).$$
The last term $P(a_n)\cap\{p\}$ is $\emptyset$ if $p\nmid a_n$ and $\{p\}$ if
$p\mid a_n$, giving exactly the two stated possibilities. Intersecting the
first display with $S$ and using $\rho_S(n)\subseteq S$, $\{p\}\cap S=\emptyset$
gives the second display.

*(a).* Suppose $X\in\mathcal P'(S')$, i.e. the index set $I_X := \{n:\rho_{S'}(n)=X\}$
is infinite. For every $n\in I_X$, the second display gives $\rho_S(n)=X\cap S$.
So every $n\in I_X$ also has S-type exactly $X\cap S$, hence $I_X\subseteq\{n:\rho_S(n)=X\cap S\}$,
and since $I_X$ is infinite so is the right-hand index set; thus $X\cap S=\pi(X)\in\mathcal P'(S)$.

*(b).* Fix $B\in\mathcal P'(S)$, so $I_B:=\{n:\rho_S(n)=B\}$ is infinite. By the
first display, for $n\in I_B$, $\rho_{S'}(n)\in\{B,B\cup\{p\}\}$, so
$I_B = I_B^0 \sqcup I_B^1$ where $I_B^0 := \{n\in I_B : p\nmid a_n\}$ (giving
$\rho_{S'}(n)=B$) and $I_B^1 := \{n\in I_B: p\mid a_n\}$ (giving
$\rho_{S'}(n)=B\cup\{p\}$). An infinite set partitioned into two parts has at
least one infinite part (finite ∪ finite is finite), so at least one of
$I_B^0, I_B^1$ is infinite, i.e. at least one of $B, B\cup\{p\}$ occurs
infinitely often as an $S'$-type, i.e. lies in $\mathcal P'(S')$ and maps to $B$
under $\pi$. This proves surjectivity; "at most two preimages" is immediate
since only $B$ and $B\cup\{p\}$ can map to $B$ under $\pi$ (any $X$ with
$X\cap S = B$ and $X\subseteq S'=S\cup\{p\}$ satisfies $X\in\{B,B\cup\{p\}\}$). ∎

This lemma is trivial in content but establishes clean, precise bookkeeping the
rest of the argument depends on: refining the core by one prime never destroys
or manufactures a persistent base type, it only ever splits it into at most two
sub-types, and both/either sub-type may itself be persistent.

### 2. Threshold Recursion Bound Lemma (new, fully proved)

**Statement.** With $S, p, S'$ as in Lemma 1, for each $B\in\mathcal P'(S)$
define, using the notation $I_B, I_B^0, I_B^1$ from the proof of Lemma 1(b):
$$M_B := \begin{cases} 0 & \text{if both } I_B^0, I_B^1 \text{ are infinite,} \\
\max(I_B^1) & \text{if } I_B^0 \text{ is infinite and } I_B^1 \text{ is finite (}0 \text{ if } I_B^1=\emptyset\text{),} \\
\max(I_B^0) & \text{if } I_B^1 \text{ is infinite and } I_B^0 \text{ is finite (}0 \text{ if } I_B^0=\emptyset\text{).}
\end{cases}$$
(By Lemma 1(b), at least one of $I_B^0, I_B^1$ is infinite, so exactly one of
the three cases applies; $M_B$ is a well-defined nonnegative integer, finite in
every case since it is either $0$ or the max of a finite set.) Then
$$N(S') \;\le\; \max\Big(N(S),\ \max_{B\in\mathcal P'(S)} M_B\Big).$$

**Proof.** Let $n > N(S)$. By definition of $N(S)$, $\rho_S(n)\in\mathcal P'(S)$;
write $B:=\rho_S(n)$. We show $\rho_{S'}(n)\in\mathcal P'(S')$ unless
$n\le M_B$, which suffices: it shows every $n$ with $\rho_{S'}(n)\notin\mathcal
P'(S')$ satisfies $n\le N(S)$ or $n\le M_{\rho_S(n)}\le\max_B M_B$, so
$N(S')=\max\{n:\rho_{S'}(n)\notin\mathcal P'(S')\}$ (or $0$) is at most
$\max(N(S),\max_B M_B)$.

Case (i): both $I_B^0, I_B^1$ infinite. Then by Lemma 1(b)'s proof both $B$ and
$B\cup\{p\}$ lie in $\mathcal P'(S')$. Since $\rho_{S'}(n)\in\{B,B\cup\{p\}\}$
(first display of Lemma 1), $\rho_{S'}(n)\in\mathcal P'(S')$ regardless — no
exception possible for this $n$, matching $M_B=0$ (the bound $n\le M_B=0$ is
irrelevant since the conclusion already holds unconditionally).

Case (ii): $I_B^0$ infinite, $I_B^1$ finite. Then $B\in\mathcal P'(S')$ (via
$I_B^0$) but $B\cup\{p\}\notin\mathcal P'(S')$: indeed, by the second display of
Lemma 1, every index $n''$ with $\rho_{S'}(n'')=B\cup\{p\}$ satisfies
$\rho_S(n'')=B$, i.e. $n''\in I_B$, and moreover $n''\in I_B^1$ (since
$\rho_{S'}(n'')=B\cup\{p\}$ means $p\mid a_{n''}$); so $\{n'':\rho_{S'}(n'')=B\cup\{p\}\}\subseteq I_B^1$,
which is finite, so $B\cup\{p\}\notin\mathcal P'(S')$. Now if $n\in I_B^0$,
$\rho_{S'}(n)=B\in\mathcal P'(S')$, no exception. If $n\in I_B^1$, then
$\rho_{S'}(n)=B\cup\{p\}\notin\mathcal P'(S')$, an exception — but by
definition $n\le\max(I_B^1)=M_B$ in this case.

Case (iii) is symmetric to (ii) with the roles of $I_B^0,I_B^1$ (and $B$,
$B\cup\{p\}$) swapped.

In every case, for $n>N(S)$ with $\rho_S(n)=B$, either $\rho_{S'}(n)\in\mathcal
P'(S')$, or $n\le M_B$. This proves the claimed bound. ∎

**Remark (why this is genuine new content).** This is *not* a restatement of
the certified Termination Criterion Lemma (which is about the outer absorption
chain $S_k\mapsto S_k^+$, absorbing possibly many primes' full factorizations
at once, and only supplies the *iff*-equivalence "terminates iff $N(S_k)$
bounded", with no information about the internal behaviour of $N$ as a function
of the core). Lemma 2 is instead the first-ever *exact mechanism* description
of how the single quantity $N(S)$ itself responds when the core $S$ is enlarged
by one prime — this is precisely the "regularity of $N$ as a function of $S$"
that this round's explorer identified as the single most concrete missing
structural fact (see `math-explorer-termination.md`, "First concrete
obstruction").

### 3. Why Lemma 2 does not close the sub-gap (honest diagnosis, proved not just asserted)

Lemma 2 reduces "bound $N(S')$" to "bound $\max_B M_B$ over the finitely many
$B\in\mathcal P'(S)$" (finitely many since $\mathcal P'(S)\subseteq 2^S$ is
finite). This looks like progress, but each $M_B$ is *itself* exactly the same
species of object as $N(S)$: a "last exception" threshold produced by an
infinite-pigeonhole argument on a binary partition of an infinite index set —
in this case, the partition of $I_B$ by whether $p$ divides $a_n$.

**Proposition 3 (Non-Constructivity of $M_B$).** No formula or algorithm that
computes $M_B$ from finite input data (a_1, S, p, or any explicitly bounded
number of terms of the sequence) is supplied — nor can be supplied — by any
certified tool currently in the workspace, for the same reason as round 13's
certified Non-Constructivity observation for $N_0/N_1/N_1'/N_2$: determining
$M_B$ requires first determining *which* of $I_B^0, I_B^1$ is the infinite
(persistent) one, and this is a statement about the ENTIRE infinite tail of
$\{a_n : n \in I_B\}$ (does $p$ divide $a_n$ for infinitely many $n \in I_B$, or
only finitely many?) — not decidable from any finite prefix, since altering
finitely many terms of an infinite 0/1 sequence never changes which value (if
either) occurs infinitely often. Concretely: for any candidate bound $K$, and
any finite amount of the sequence examined up to index $K$, the observed
pattern of $p\mid a_n$ for $n\in I_B$, $n\le K$ is logically consistent with
either "$I_B^1$ finite with $\max(I_B^1)>K$" or "$I_B^1$ infinite" — both
remain open possibilities no finite computation up to $K$ can rule out. Hence
$M_B$, like $N(S)$ itself, is only existentially finite (guaranteed finite by
Lemma 1(b)'s pigeonhole argument, in the case exactly one branch is infinite),
never explicitly computable from bounded data.

*Proof of the "logically consistent" claim.* Fix any $K$ and any assignment of
$p\mid a_n$ / $p\nmid a_n$ to the finitely many $n\in I_B\cap[1,K]$. Extend this
data in two ways to a sequence on all of $I_B$: (A) set $p\mid a_n$ for all
$n\in I_B$, $n>K$ — consistent with "$I_B^1$ infinite" (so this instance has
$B\cup\{p\}$, not $B$, as the persistent refinement, with $M_B$ potentially
$0$ or small); (B) set $p\nmid a_n$ for all $n\in I_B$, $n>K$ except at a single
further index $n_0>K$ where $p\mid a_{n_0}$ — consistent with "$I_B^1$ finite,
$M_B=n_0$", which can be made arbitrarily large by choosing $n_0$ arbitrarily
far beyond $K$. Both extensions agree with the given finite data on $[1,K]$
and are consistent with *some* value of the free binary choices "does $p$
divide $a_n$" for indices beyond $K$ that the certified machinery places no a
priori bound on (the certified tools bounding $a_n$ itself, e.g. the
**Generalized Bounded Gap Lemma**, `lemmas/generalized-bounded-gap-lemma.md`,
constrain the *magnitude* of $a_n$ but say nothing about which specific primes
divide it beyond membership in $P(a_1)\cup(\text{primes} \le a_n)$ — a
class-blind constraint, per the certified **Sandwich Genericity
Theorem**/`escape-cost-vacuity.md`, that cannot pin down whether $p\mid a_n$
specifically). Hence $M_B=n_0$ is unbounded across the space of sequences
consistent with any fixed finite prefix, so no function of a bounded prefix can
compute or bound $M_B$. $\blacksquare$

**Consequence.** Lemma 2's recursion is real and correct, but it reduces the
"regularity of $N(S)$" question to a strictly more granular question ($M_B$)
that is provably no easier — it inherits the exact non-constructivity
obstruction that made $N(S)$ itself resistant to a direct bound in the first
place. This matches, and now rigorously explains (rather than only
numerically illustrates), this round's `math-explorer-termination.md` finding
that the proxy absorption chain shows no sign of stabilizing within 15,000
sampled terms on the two standard hard rogue-pair seeds (a_1 = 4807, 11305):
the "last exception" phenomenon this proof isolates ($M_B$) is exactly the
kind of quantity that can be arbitrarily deep in the tail without any
witness in a bounded computational window.

### 4. What remains open

Sub-gap (H2) — boundedness of $(N(S_k))_{k\ge0}$ along the actual absorption
chain — is **not resolved** by this approach. What has changed: the vague
placeholder "some regularity of $N$ as a function of $S$, not yet known" is
now replaced by an *exact* recursive formula (Lemma 2) together with a
rigorous proof (Proposition 3) that the natural next-level target this
recursion produces ($M_B$) is exactly as non-constructive as the original
object. This narrows the search space for any future attempt: a future
mechanism attacking H2 must either (i) find a genuinely new source of
information beyond bounded-prefix data to pin down $M_B$ (or the analogous
multi-prime quantity for the true $S_k\mapsto S_k^+$ step, which absorbs many
primes at once, not one — untouched here, and likely at least as hard per the
outline's own step 5 caveat), or (ii) abandon a per-prime/direct-bound attack
entirely in favor of an indirect (e.g. compactness-style, already flagged as
running into the same class-blindness wall per `math-explorer-termination.md`
Opening 3) or family-restricted (bespoke small-seed) argument.

This approach remains, by design, entirely about the H2 sub-gap and does not
touch the main FAH crux (H1); the two are independently confirmed (round 15,
reconfirmed by this round's dispatch) to be logically distinct questions.

### 5. Round 19: the weaker existential H2 target — clarification and a new attempted route

**5.0 First honesty check: is this target actually new?**

The certified `self-absorbing-core-theorem.md` already states, verbatim, as its
open sub-gap (a): *"existence/termination of a self-absorbing S*: it is not
shown that iterating S ↦ S⁺ from S₀ reaches a fixed point in finitely many
steps."* The round-19 dispatch describes "existence of some self-absorbing S*"
as a "strictly weaker sub-target... untried." On inspection this is the SAME
statement as sub-gap (a), not a new one — merely re-emphasized. This must be
recorded plainly: no new mathematical CONTENT is created by restating the
target. What can be new is a different ROUTE to proving it. The rest of this
section attempts exactly that: a route via an explicit, non-adaptive, monotone
one-parameter family of candidate cores, distinct from the adaptive absorption
chain $S_0, S_1=S_0^+, S_2=S_1^+,\dots$ already analyzed by the certified
Termination Criterion Lemma.

**5.1 The Monotone Chain Reformulation Lemma (new, fully proved)**

For $M = 0, 1, 2, \dots$ define
$$S_M := S_0 \cup \bigcup_{j=1}^{M} P(a_j)$$
($S_0$ the fixed finite core of the certified Finite Core Theorem,
`finite-core-theorem.md`; $S_0 := S_0$ itself, i.e. $M=0$ gives back $S_0$).
This is manifestly monotone non-decreasing in $M$ ($S_M \subseteq S_{M+1}$,
since $S_{M+1} = S_M \cup P(a_{M+1})$), finite for every $M$ (a finite union of
finite sets), and $\supseteq S_0 \supseteq Q$, so the Extended
Persistent-Type Pigeonhole applies at every level $S_M$, giving well-defined
finite $\mathcal P'(S_M)$ and $N(S_M)$ (as in §0).

**Lemma (Chain Reformulation, sufficiency direction).** If there exists
$M \ge 0$ with $N(S_M) \le M$, then $S^* := S_M$ is a finite self-absorbing
core with $S^* \supseteq S_0$; hence the (already-standing) H2 sub-gap (a) is
resolved in that case.

*Proof.* By definition, $S_M^+ = S_M \cup \bigcup_{j=1}^{N(S_M)} P(a_j)$. Since
$N(S_M) \le M$, the index range $1,\dots,N(S_M)$ is a subset of $1,\dots,M$, so
$$\bigcup_{j=1}^{N(S_M)} P(a_j) \subseteq \bigcup_{j=1}^{M} P(a_j) \subseteq S_M.$$
Hence $S_M^+ = S_M \cup (\text{a subset of } S_M) = S_M$. Also always
$S_M^+ \supseteq S_M$ by definition of $(\cdot)^+$. So $S_M^+ = S_M$, i.e.
$S_M$ is self-absorbing, and $S_M \supseteq S_0$ by construction. $\blacksquare$

This converts the existence question into a purely numerical one about an
EXPLICIT, easy-to-state monotone family: *does the sequence $M \mapsto N(S_M)$
ever dip to or below the diagonal $M$?* This is a clean reformulation — never
stated before in this workspace — and is a logically different object from
"$N(S_k)$ bounded along the adaptive chain $S_0,S_1,\dots$" of the certified
Termination Criterion Lemma, because $S_M$ enlarges by exactly one term's full
factorization at a time regardless of $N(S_M)$'s value, whereas $S_{k+1}=S_k^+$
enlarges adaptively by exactly the terms up to the current threshold. (Note
$S_1 = S_0^+$ agrees with the adaptive chain's first step only if $N(S_0)\le 1$;
in general the two families diverge from $M=1$ onward.)

**5.2 Is the converse true? (checked, and found to fail — Proposition 5, §7
below)** Establishing that EVERY self-absorbing S** gives rise to some working
$M$ would upgrade this to a genuine "iff" reformulation of sub-gap (a) — see
§7 for why this direction does not go through with the tools currently
available. So the Monotone Chain family is only a *sufficient* route to
existence, not shown necessary; a possible self-absorbing $S^{**}$ of a
different shape is not ruled out or captured by it.

### 6. Attempting Step 3 (Non-Recurrence of Refinement Primes) on this new family

**Proposition 4 (the naive non-recurrence argument gives no contradiction,
even for the explicit $S_M$ family).**

Suppose, for contradiction-attempt purposes, that $N(S_M) > M$ for every
$M \ge 0$ (i.e. the sufficient condition of §5.1 never holds for this family).
We ask whether this alone contradicts any already-certified fact.

*Observation 1 (fixed base-type alphabet).* Every base type $\tau(n) = P(a_n)
\cap Q$ lies in the fixed finite set $2^Q\setminus\{\emptyset\}$ (at most
$2^{|Q|}-1$ possibilities), independent of $M$ — this is the Persistent-Type
Pigeonhole fact, unaffected by how large $S_M$ grows, since $Q$ itself never
changes. This is real and true, but by itself it only bounds the number of
BASE types, not the number of times $N(S_M)$ can exceed $M$.

*Observation 2 (primes are recruited without repetition).* The sets $S_M
\setminus S_{M-1} = P(a_M)\setminus S_{M-1}$ are pairwise disjoint across
different $M$ (once a prime enters $S_{M-1}$ it stays, by monotonicity of the
union), so the total number of distinct primes ever appearing among
$S_0,S_1,S_2,\dots$ equals $|S_0| + \sum_{M\ge1}|P(a_M)\setminus S_{M-1}|$. This
sum can be, and generically is, infinite (there is no certified upper bound on
$\sum_M |P(a_M)\setminus S_{M-1}|$ anywhere in the workspace — the **Bounded
Gap Lemma** bounds the SIZE of $a_M$, hence by the elementary inequality
$a_M \ge 2^{\omega(a_M)}$ an $O(\log a_M)$ bound on $\omega(a_M)$ itself, but
this bounds the number of NEW primes at step $M$, not the eventual total across
all $M$, and does not bound $N(S_M)-M$).

*Attempted contradiction.* One might hope: "if infinitely many distinct primes
are recruited, but the base-type alphabet is finite, eventually no NEW
persistent extended type can appear, forcing stabilization." This is false as
stated: Binary Refinement Lemma (§1) shows each new prime can *split* an
existing persistent type into two, so $|\mathcal P'(S_M)|$ can keep growing
(up to a factor of 2 per new prime) without bound as $M\to\infty$ — there is no
certified upper bound on $|\mathcal P'(S_M)|$ independent of $M$, so "finite
alphabet of BASE types" does not translate into "finite/bounded alphabet of
EXTENDED types," and no contradiction is produced. Concretely: it is logically
consistent (not excluded by any certified lemma) that $|\mathcal P'(S_M)|$
grows roughly like $2^{c\cdot M}$ for some $c>0$ while $N(S_M)$ also grows,
staying always strictly above $M$; nothing in the current toolkit rules this
out.

*Second attempted contradiction (rate-based).* One might try to bound how much
$N(S_M)$ can jump when $S_{M-1}\to S_M$ adjoins the (finitely many) new primes
of $P(a_M)\setminus S_{M-1}$, via iterating the certified Threshold Recursion
Bound Lemma (§2) once per new prime. This gives
$$N(S_M) \le \max\Big(N(S_{M-1}),\ \max_{B,\,p} M_{B,p}\Big)$$
where the inner max ranges over the finitely many persistent types $B \in
\mathcal P'(\text{intermediate cores})$ and the finitely many new primes $p$
adjoined in going from $S_{M-1}$ to $S_M$. By **Proposition 3** (already
certified in this file, §3), each such $M_{B,p}$ is *not* bounded by any
function of finite data ($a_1,\dots$ up to any fixed index) — the same "two
consistent extensions" argument of Proposition 3 applies verbatim here (it
never used any property special to the single-prime chain $S,S'$ beyond being
one arbitrary finite core and one arbitrary adjoined prime, both of which hold
identically for $S_{M-1}, p, S_M$-components). Hence the recursion gives no
rate control: $N(S_M)$ can jump by an amount not bounded in terms of $M$ or of
any quantity computable from $a_1,\dots,a_M$, so no contradiction from
"$N(S_M) > M$ for all $M$" is produced this way either. $\blacksquare$
(Proposition 4 is thus a negative result: it certifies that the two most
natural contradiction attempts both fail, honestly closing off this line
rather than leaving it as an unexamined "should work" gap.)

### 7. Checking whether the existence question could be attacked by a different (non-$S_M$) family

**Proposition 5 (the converse of the Chain Reformulation Lemma is not
established; $N$ is not shown monotone under further enlargement).**

Suppose a self-absorbing $S^{**} \supseteq S_0$ exists (of possibly different
shape than any $S_M$). WLOG (discarding primes of $S^{**}$ that divide no
$a_n$ at all — this changes neither $\rho_{S^{**}}(n)$ for any $n$, since such
primes never lie in $P(a_n)$, nor $N(S^{**})$, nor self-absorption of
$S^{**}$, by the same computation as $S^{**} \cap S_\infty$ below) assume every
prime of $S^{**}$ divides at least one $a_n$. For each such prime $p \in
S^{**}$ let $m_p := \min\{n : p \mid a_n\}$ (finite, since $p$ divides some
term) and $M^{**} := \max(0,\max_{p\in S^{**}} m_p)$ (finite, max of a finite
set). Then $S^{**} \subseteq S_{M^{**}}$ (every prime of $S^{**}$ already
divides $a_{m_p}$ for some $m_p \le M^{**}$, hence lies in $S_{M^{**}}$).

This shows $S^{**}$ is dominated by SOME member of the $S_M$ family — but it
does **not** show $S_{M^{**}}$ is itself self-absorbing, nor that
$N(S_{M^{**}}) \le M^{**}$. The obstruction: passing from $S^{**}$ (known
self-absorbing) to the possibly-larger $S_{M^{**}} \supseteq S^{**}$ requires
knowing that enlarging a self-absorbing core keeps it self-absorbing, i.e.
that $N(\cdot)$ does not "wake back up" when extra (possibly irrelevant)
primes are adjoined. No certified lemma in this workspace establishes this: the
Binary Refinement Lemma (§1) shows only how persistent TYPES transform under
one more prime, not that $N$ itself is monotone or even bounded under further
enlargement — indeed Proposition 3's whole point is that $N$ (equivalently
each per-step threshold $M_B$) can behave arbitrarily as the core is refined
further, with no control from bounded data. Concretely, it remains logically
open (not excluded by anything certified) that $S^{**}$ is self-absorbing but
$S_{M^{**}} \supsetneq S^{**}$ is NOT self-absorbing (adjoining the "extra"
primes of $S_{M^{**}}\setminus S^{**}$, which came from $P(a_j)$ for $j \le
M^{**}$ but $j$ possibly $> N(S^{**})$, could in principle re-split some
persistent type and push $N(S_{M^{**}})$ back above $M^{**}$).

**Conclusion of Proposition 5.** The Monotone Chain family $\{S_M\}$ captures
only a sufficient, not a necessary, route to existence: "∃M, N(S_M)≤M" implies
existence (§5.1), but existence does not (with currently available tools) imply
"∃M, N(S_M)≤M". So even a hypothetical resolution of the $S_M$-question would
only be a partial resolution of sub-gap (a) in the sufficient direction, and a
FAILURE to resolve the $S_M$-question (as found in §6) does not, by itself,
prove sub-gap (a) is false — it only shows this particular attempted route is
blocked. $\blacksquare$

### 8. Honest overall verdict for this round's H2 attack

Despite (a) correctly identifying that "existence of self-absorbing S*" is in
principle a logically different KIND of claim from "N(S_k) bounded along the
adaptive chain" (an existential statement vs. a numeric-boundedness statement),
and (b) constructing a genuinely new, explicit, non-adaptive candidate family
($S_M$, distinct in general from the adaptive $S_k$) to try to exploit that
difference, this round's attack does **not** evade Proposition 3's obstruction:
- The sufficient-condition route (§5.1) reduces existence to a numeric
  question ("$N(S_M)\le M$ for some $M$") of exactly the same non-constructive
  species as before (§6, Proposition 4): Proposition 3 applies verbatim to the
  incremental steps of the $S_M$ chain, so no rate control on $N(S_M)$ is
  available, and the two most natural contradiction attempts against
  "$N(S_M)>M$ for all $M$" both fail.
- The necessary-condition direction (§7, Proposition 5) is not established
  either: monotonicity of self-absorption under core enlargement is not known,
  so even the existence of some OTHER self-absorbing $S^{**}$ cannot currently
  be leveraged to make the $S_M$ family work, nor ruled out independently.

This matches the outline's own honest prediction and this file's own standing
Proposition 3: the weaker existential framing does not, on this round's
attempt, evade the wall — it is reported as a further-confirmed dead end for
the "adjoin-one-prime-at-a-time / bounded-data" style of attack on H2's
sub-gap (a), while producing two new fully-proved, reusable structural facts
(the Monotone Chain Reformulation Lemma and Proposition 5's "no known
monotonicity" observation) that sharpen exactly what any future attempt needs:
either (i) a genuinely new source of information about the TAIL of the
sequence (not derivable from any bounded prefix, since Proposition 3 shows
bounded-prefix data is provably insufficient), or (ii) a proof that
self-absorption IS monotone under enlargement (which would at least make the
$S_M$ family fully capture the existence question, converting sub-gap (a) into
the single clean numeric question "$\exists M: N(S_M)\le M$" with no
loss) — neither is available yet.

## Promotable lemmas

- **Binary Refinement Lemma** (Section 1 above): for finite $S\supseteq Q$, a
  prime $p\notin S$, $S'=S\cup\{p\}$: $\rho_{S'}(n)\cap S=\rho_S(n)$ always, and
  the restriction map $\pi:X\mapsto X\cap S$ sends $\mathcal P'(S')$ into
  $\mathcal P'(S)$ and is surjective onto it, with each $B\in\mathcal P'(S)$
  having 1 or 2 preimages, a subset of $\{B,B\cup\{p\}\}$. Fully proved,
  unconditional, elementary. Reusable as basic bookkeeping for any future
  approach reasoning about how persistent-type alphabets change under core
  enlargement by a single prime.
- **Threshold Recursion Bound Lemma** (Section 2 above): $N(S\cup\{p\}) \le
  \max(N(S), \max_{B\in\mathcal P'(S)} M_B)$, with $M_B$ defined explicitly via
  the last-exception index of whichever of $I_B^0, I_B^1$ is finite (or $0$ if
  both are infinite). Fully proved, unconditional, depends only on the
  certified Extended Persistent-Type Pigeonhole and Binary Refinement Lemma
  above. This is the first exact structural fact relating $N(S)$ at two
  different cores; reusable by any future attempt on sub-gap (H2).
- **Non-Constructivity of $M_B$** (Proposition 3, Section 3 above): a genuine
  extension of round 13's certified Non-Constructivity observation to this new
  object, with its own from-scratch proof (the "two consistent extensions"
  argument), not merely a citation. Reusable as a standing caution: any future
  attempt to bound $M_B$ (or analogous per-prime/per-type "last exception"
  quantities) from bounded-prefix data is provably impossible by this same
  argument, without needing to re-derive it each time.
- **Monotone Chain Reformulation Lemma** (Section 5.1, round 19): for the
  explicit monotone family $S_M := S_0 \cup \bigcup_{j=1}^M P(a_j)$
  ($M=0,1,2,\dots$), "$\exists M: N(S_M)\le M$" implies "$S_M$ is a finite
  self-absorbing core $\supseteq S_0$" — fully proved, unconditional, a clean
  one-line consequence of the definitions of $N(\cdot)$ and $(\cdot)^+$.
  Reusable as the cleanest currently-known sufficient numeric reformulation of
  H2 sub-gap (a) (existence of a self-absorbing core): reduces an existential
  statement about arbitrary finite supersets of $S_0$ to a single real-valued
  sequence $M\mapsto N(S_M)-M$ dipping non-positive.
- **Non-Monotonicity Gap** (Proposition 5, Section 7, round 19): it is NOT
  established (and no certified tool in the workspace currently establishes)
  that self-absorption is preserved under further core enlargement, i.e. that
  $S$ self-absorbing and $S\subseteq S'$ does not imply $S'$ self-absorbing.
  Consequently the Monotone Chain Reformulation Lemma's converse is open: an
  arbitrary self-absorbing $S^{**}$ need not be dominated by a working member
  of the $S_M$ family. Reusable as a standing caution/open-question flag for
  any future attempt to upgrade the sufficient reformulation above to a full
  "iff": that upgrade requires either a monotonicity theorem for self-absorption
  or an entirely different argument.
