# Approach: profile-class-recruitment

## Status
partial

## Approaches tried
- (round 2, outline) Diversity-hedge framing of the (HS) finiteness nucleus, kept far from the
  extremal-descent route: reframe finiteness as termination of a greedy "recruitment" process over
  a FIXED finite profile alphabet. Reduction Lemmas 1–6 imported (certified). Steps 1–3 rigorous;
  Step 4 (recruitment termination) is the open nucleus.
- (round 2, build) **partial.** Rendered Steps 1–3 fully rigorous (Step B; finite-profile-alphabet
  reduction of (HS) to finitely many cross-pair types; gap-divides-difference connector bound) and
  added a **new rigorous reduction** (Step 4a: every type in which a profile occurs only finitely
  often is hit by a finite set for free), shrinking the open gap to (REC): for each of the finitely
  many types whose two classes are BOTH infinite, a finite prime set hits every cross pair. Step 4b
  (recruitment termination / cheapest-patch monovariant) remains an **explicit unproved gap**.

## Current best

The whole problem is reviewer-certified reduced (exact periodicity from n=1, no pre-period) to

> **(HS).** There is a finite set of primes S such that every pair of terms shares a prime in S.

(Certified in `lemmas/enumeration-and-bounded-gaps.md`, `lemmas/finite-hitting-set-periodicity.md`;
imported, not re-proved.) This approach reframes (HS) over a **fixed finite alphabet** and proves
rigorously (Steps B, 2, 3, 4a below): (HS) is equivalent to **(REC)** — for each of the finitely
many disjoint-profile types $\{\pi,\pi'\}$ whose two classes are **both infinite**, a finite prime
set hits every cross pair of that type. **(REC) is the single remaining open gap.**

---

## The proof so far (Steps 1–3 rigorous; Step 4a rigorous; Step 4b an explicit open gap)

### Setup and imported certified facts

Let $a_1<a_2<a_3<\cdots$ be the greedy sequence: $a_{n+1}$ is the least integer $>a_n$ with
$\gcd(a_{n+1},a_i)>1$ for all $i\le n$. Write $S_0=\operatorname{supp}(a_1)$ (the primes dividing
$a_1$), a **fixed finite** set, and $R=\operatorname{rad}(a_1)=\prod_{p\in S_0}p$. A **term** is an
element $a_n$; all terms are $\ge a_1>1$. For an integer $x>1$, $\operatorname{supp}(x)$ is its set
of prime factors.

Imported reviewer-certified results (proofs in `lemmas/enumeration-and-bounded-gaps.md`):

- **Lemma 1 (pairwise non-coprimality).** For all $m\ne n$, $\gcd(a_m,a_n)>1$: any two distinct
  terms share a prime factor.
- **Lemma 2 (enumeration / greedy minimality).** $(a_n)$ is the strictly increasing enumeration of
  $A\cap[a_1,\infty)$, where $A=\{x>1:\gcd(x,a_i)>1\ \forall i\}$; and
  $a_{n+1}=\min\{x>a_n:\gcd(x,a_i)>1\ \forall i\le n\}$.
- **Lemma 3 (bounded gaps).** $a_{n+1}-a_n\le R$ for all $n$.

Periodicity machine (proof in `lemmas/finite-hitting-set-periodicity.md`):

- **Lemma HS→P.** Call a finite prime set $S$ a **hitting set** if every pair of terms shares a
  prime in $S$. If $S$ is a finite hitting set, then with $L=\prod_{p\in S}p$ and
  $T=|A\cap[a_1,a_1+L)|\ge1$ we have $a_{n+T}=a_n+L$ for every $n\ge1$.

So it suffices to **produce one finite hitting set $S$.** That is the entire remaining task.

---

### Step B (every term has a prime factor in $S_0$)

**Claim.** For every $n$, $\operatorname{supp}(a_n)\cap S_0\ne\emptyset$.

*Proof.* If $n=1$: $a_1>1$ has a prime factor, which lies in $S_0=\operatorname{supp}(a_1)$. If
$n>1$: $a_n$ and $a_1$ are distinct terms, so by **Lemma 1** $\gcd(a_n,a_1)>1$; any prime $p$
dividing this gcd divides $a_1$ (hence $p\in S_0$) and divides $a_n$. $\square$

---

### Step 2 (finite profile alphabet; reduction of (HS) to cross-pair types)

For each term $a_n$ define its **profile**
$$\tau(n):=\operatorname{supp}(a_n)\cap S_0\subseteq S_0 .$$
By **Step B**, $\tau(n)\ne\emptyset$. As $S_0$ is fixed and finite, $\tau$ takes at most
$2^{|S_0|}-1$ distinct values — a **fixed finite alphabet**, independent of $n$.

**(Intersecting profiles are hit by $S_0$.)** If $\tau(i)\cap\tau(j)\ne\emptyset$, any prime
$p\in\tau(i)\cap\tau(j)\subseteq S_0$ divides both $a_i,a_j$, so the pair is hit by $p\in S_0$.

Call $\{a_i,a_j\}$ a **cross pair** if $\tau(i)\cap\tau(j)=\emptyset$. By **Lemma 1** a cross pair
shares *some* prime $p$; and $p\notin S_0$, since $p\in S_0$ would put $p\in\tau(i)\cap\tau(j)$,
contradicting disjointness. So **every common prime of a cross pair lies outside $S_0$.**

Group cross pairs by **type**: the unordered pair of profiles $\{\tau(i),\tau(j)\}$, a pair of
disjoint nonempty subsets of $S_0$. There are at most $\binom{2^{|S_0|}-1}{2}$ types — a **fixed
finite** index set.

**Reduction.** Suppose that for each type $\{\pi,\pi'\}$ there is a finite prime set $P_{\pi,\pi'}$
hitting every cross pair of that type. Then
$$S:=S_0\cup\bigcup_{\{\pi,\pi'\}}P_{\pi,\pi'}$$
is **finite** (finite union of finite sets) and a hitting set: intersecting-profile pairs are hit
by $S_0\subseteq S$; a cross pair of type $\{\pi,\pi'\}$ is hit by $P_{\pi,\pi'}\subseteq S$. By
**Lemma HS→P** this proves the theorem. It remains to supply the finite sets $P_{\pi,\pi'}$.

---

### Step 3 (gap divides difference — connector-size bound)

**Claim.** If a prime $p$ divides both $a_i$ and $a_j$ ($i<j$), then $p\mid a_j-a_i$ and
$p\le a_j-a_i\le (j-i)R$.

*Proof.* $p\mid a_i,\ p\mid a_j\Rightarrow p\mid(a_j-a_i)$. As $a_i<a_j$, $a_j-a_i$ is a positive
multiple of $p$, so $p\le a_j-a_i$. Telescoping **Lemma 3**,
$a_j-a_i=\sum_{k=i}^{j-1}(a_{k+1}-a_k)\le (j-i)R$. $\square$

**Consequence.** A cross pair whose only common prime is a large $p$ must be far apart in index:
$j-i\ge p/R$. Cross pairs close in index can only be connected by small primes ($\le(j-i)R$). This
is the size control the recruitment argument (Step 4b) means to exploit.

---

### Step 4a (finitely-occurring profiles drop out — RIGOROUS)

**Claim.** If in a type $\{\pi,\pi'\}$ at least one profile — say $\pi$ — occurs only finitely often
(only finitely many terms have profile $\pi$), then a finite prime set hits every cross pair of
type $\{\pi,\pi'\}$.

*Proof.* Let $F=\{a_i:\tau(i)=\pi\}$ be finite. Every cross pair of type $\{\pi,\pi'\}$ has one
member in $F$. Fix $a_i\in F$: by **Lemma 1**, $a_i$ shares a prime with every other term, and each
such shared prime divides $a_i$, hence lies in the finite set $\operatorname{supp}(a_i)$. So every
cross pair of type $\{\pi,\pi'\}$ containing $a_i$ is hit by $\operatorname{supp}(a_i)$. Taking the
union over the finitely many $a_i\in F$,
$$P_{\pi,\pi'}:=\bigcup_{a_i\in F}\operatorname{supp}(a_i)$$
is a **finite** prime set hitting every cross pair of type $\{\pi,\pi'\}$. $\square$

By **Step 4a**, the only types still needing an argument are those in which **both** profiles occur
infinitely often — at most $\binom{2^{|S_0|}-1}{2}$ of them. Thus (HS) is reduced to:

> **(REC) — the open nucleus.** For every type $\{\pi,\pi'\}$ (disjoint nonempty
> $\pi,\pi'\subseteq S_0$) whose **both** classes are infinite, there is a **finite** set of primes
> hitting every cross pair of type $\{\pi,\pi'\}$.

If **(REC)** holds, then together with Step 4a it supplies a finite $P_{\pi,\pi'}$ for *every* type,
and Step 2 + Lemma HS→P finish. Note **(REC) $\Rightarrow$ (HS) $\Rightarrow$ theorem** is now
rigorous; only (REC) itself is open.

---

### Step 4b (recruitment termination — EXPLICIT OPEN GAP, NOT PROVED)

**(REC) is not proved in this approach.** We record the conjectured mechanism honestly so no later
agent mistakes it for a completed step.

*Conjectured mechanism (cheapest-patch recruitment monovariant).* Fix a type $\{\pi,\pi'\}$ with
both classes infinite. Numerical evidence (explorer reports `math-explorer-greedy.md`,
`math-explorer-covering.md`; 12 starting values, up to 1400 terms) shows the primes that ever
connect a cross pair form a **small fixed set** — the smallest primes not in $S_0$, recruited in
roughly increasing order (e.g. $a_1=385$: extra primes $\{2,3,13,19\}$; identical set at $N=600$ and
$N=1400$). The intended argument:

1. Some small prime $r\notin S_0$ eventually divides both a $\pi$-term and a $\pi'$-term (is
   "recruited" for this type).
2. **Greedy minimality** (Lemma 2: $a_{n+1}$ is the *least* admissible integer $>a_n$) should then
   force every later cross pair of this type to be hittable by an already-recruited small prime:
   when $a_n$ is chosen, a candidate in the length-$\le R$ window $(a_{n-1},a_{n-1}+R]$ divisible by
   an already-recruited $r$ (and by a prime of $S_0$, so admissible) is available and small, so the
   greedy rule never reaches out to a **fresh large** prime as a sole connector.
3. By **Step 3**, a fresh large sole connector $p$ forces its witnessing pair to have index gap
   $\ge p/R\to\infty$; the claim is that over such a span the finite profile structure has already
   recurred and produced a small shared connector, contradicting $p$ being the *sole* connector.

*Why this is only a conjecture here.* Step (2) requires proving that a suitable
already-recruited-$r$-divisible admissible candidate genuinely lies in *every* relevant window and
is genuinely preferred by the greedy rule over any fresh-large-prime alternative — the
"cheapest patch is always available and always cheaper" claim. That is exactly the greedy-minimality
lemma the round-1 counting wall lacked, and it is **not established**. Step (3) likewise assumes an
unproved recurrence. We do **not** claim (REC); it is the open nucleus. We explicitly do **not**
reintroduce any $\sum 1/p^2$ density argument (proven insufficient in round 1: it cannot exclude
sparse density-zero disjoint-profile families).

---

## Open gaps

**(REC)** (Step 4b, recruitment termination): for each type whose two classes are both infinite, a
finite prime set hits every cross pair of that type. The conjectured cheapest-patch monovariant is
stated but unproved. This is the diversity hedge; the descent route
(`admissible-set-periodicity`) is the expected closer. Everything else — Steps B, 2, 3, 4a and the
implication (REC) ⇒ theorem — is rigorous.

## Promotable lemmas

- **Profile-alphabet reduction of (HS).** With $\tau(n)=\operatorname{supp}(a_n)\cap S_0$: $\tau(n)$
  is a nonempty subset of the fixed finite $S_0$; $S_0$ hits every intersecting-profile pair; and
  (HS) holds iff for each of the finitely many types $\{\pi,\pi'\}$ (disjoint nonempty
  $\pi,\pi'\subseteq S_0$) **whose both classes are infinite** a finite prime set hits every cross
  pair of that type. Proved in full above (Steps B, 2, 4a) from certified Lemmas 1–3. Reusable by
  any profile-based attack on (HS).
- **Gap-divides-difference connector bound.** If a prime $p$ divides both $a_i,a_j$ ($i<j$) then
  $p\mid a_j-a_i$ and $p\le a_j-a_i\le(j-i)R$. Proved in full (Step 3) from Lemma 3. Reusable.
