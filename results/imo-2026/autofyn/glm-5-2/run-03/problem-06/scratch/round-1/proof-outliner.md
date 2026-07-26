## imo-2026-06

Population is empty (round 1, confirmed via `sample_approaches`). Opening a field of 4 rival approaches, each a whole attempt at the full claim "$\exists T,L:\ a_{n+T}=a_n+L\ \forall n$", diversifying in **framing/spine**, not technique. All four build on the proved linchpins (every $a_n$ has a prime factor of $a_1$; gaps $d_n\le M_1:=\operatorname{rad}(a_1)$; linear growth) and respect the recorded dead-end: do NOT conclude periodicity from "small-prime constraint family stabilizes" — large free-rider primes stay non-redundant for $a_1=385$ past 12000 terms.

---

### `transversal-saturation`
**new** — canonical finite-state route (framing 1).
**Target:** full claim, end to end.
**Framing.** Reformulate admissibility as a hitting-set (transversal) problem on the family $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$ of prime-supports: $\mathcal B_n=\{m:S(m)\text{ hits every }S(a_i)\}=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{m:\operatorname{rad}(T)\mid m\}$, a finite union of APs. Show this union stabilizes to an $L$-periodic set $\mathcal B_\infty$; the cyclic-successor map on $A=\mathcal B_\infty\bmod L$ is a bijection (inverse of cyclic predecessor), so every orbit is a *cycle* with no tail. Conclude $a_{n+T}=a_n+L$.
**Skeleton:**
  1. Linchpin: every $a_n$ is divisible by some $p\mid a_1$ — by the condition with $i=1$. *(proved)*
  2. Gap bound: $d_n=a_{n+1}-a_n\le M_1=\operatorname{rad}(a_1)$ — the candidate $a_n+M_1$ is a multiple of every $p\mid a_1$, hence hits every $a_i$. *(proved)*
  3. Pairwise-intersecting: $\mathcal F_n$ is pairwise-intersecting ($a_j$ must share a prime with $a_i$ for $i<j$). *(proved, one line)*
  4. **(GAP A — the wall)** The set of primes that ever enter a *minimal transversal* of $\mathcal F_n$ is finite. Equivalently: only finitely many "non-redundant" primes ever appear. Mechanism to attempt: each non-redundant insertion strictly shrinks the antichain $\operatorname{MT}(\mathcal F_n)$; the antichain lives in a finite poset *once a bound on transversal primes is known* — and the bound is what must be proved. Candidate mechanism (unproved): a non-redundant prime $q>M_1$ entering forces a minimal transversal avoiding a $P_1$-prime to strictly shrink; only finitely many such "avoid-a-$P_1$-prime" configurations exist, so only finitely many $q$ can be witnessed before the avoid-configurations are exhausted.
  5. Stabilization: once Gap A falls, $\operatorname{MT}(\mathcal F_n)$ is a non-increasing antichain in a finite poset ⇒ stabilizes at some $N_0$ to $\operatorname{MT}(\mathcal F_\infty)$. Set $L=\operatorname{lcm}\{\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_\infty)\}$; $\mathcal B_\infty$ is $L$-periodic.
  6. Cyclic successor $f:A\to A$ ($f(r)$=least element of $A$ cyclically after $r$) is a bijection ⇒ every orbit is a cycle (no tail).
  7. **(GAP B — pure-from-start)** $a_1\in\mathcal B_\infty$ and the greedy choice always lands in $\mathcal B_\infty$ even before $N_0$: $\min(\mathcal B_n\cap(a_n,\infty))=\min(\mathcal B_\infty\cap(a_n,\infty))$ for all $n$. Mechanism: backward extension — trace the cyclic predecessor in $\mathcal B_\infty$ back from $a_{N_0}$ and match to $a_1$ by uniqueness of the greedy choice; or prove $\mathcal B_n\supseteq\mathcal B_\infty$ is "looser" only above $a_n+M_1$ so it cannot produce a smaller admissible candidate than $\mathcal B_\infty$ within the gap window.
  8. Combine 6+7: orbit of $a_1\bmod L$ under $f$ is a cycle of length $T=|A|$ (or a divisor), per-period total increment $=L$ ⇒ $a_{n+T}=a_n+L$ for all $n\ge1$.
**Key lemmas:**
  - Linchpin + gap bound *(proved, cite compute/prime-support scouts)*.
  - **(GAP A)** Finiteness of transversal primes — because each non-redundant insertion shrinks the avoid-a-$P_1$-prime sub-antichain and there are finitely many such sub-antichains.
  - **(GAP B)** Greedy always lands in $\mathcal B_\infty$ — because $\mathcal B_n$ only tightens $\mathcal B_\infty$ and the tightening cannot beat the next $\mathcal B_\infty$-element within the gap window $[a_n,a_n+M_1]$.
**Open gaps:** A (transversal-prime finiteness), B (pure-from-start).
**Cases to cover:** even $a_1$ (trivial $T=1,L=2$); $a_1$ prime power (trivial $T=1,L=p$); general.
**Watch out for:** the 385 trap — do NOT substitute "small-prime family stabilizes" for Gap A; free-rider primes $>M_1$ are exactly what Gap A must tame. The "bijection ⇒ no tail" step (6) is elementary *once* $\mathcal B_\infty$ exists; all the load is in A and B.
**Why far from the others:** it is the only approach that puts the *antichain-shrinking monovariant* as the spine and pins the wall as "bound transversal primes via avoid-$P_1$-prime configurations." The dichotomy approach splits on lock; the growing-modulus approach grows $L$ explicitly; the type-replacement approach competes free-riders of the same type.

---

### `prime-power-dichotomy`
**new** — lock vs no-lock (framing 3).
**Target:** full claim.
**Framing.** Split on whether any term is a prime power. If yes, the sequence *locks*: singleton support $\{p\}$ forces every later term to be a $p$-multiple, and the greedy becomes $a_{n+1}=a_n+p$. If no term is ever a prime power, every support has size $\ge2$; use this extra structure (pairwise-intersecting family with no singleton) to prove a sharper transversal-prime bound than the general case admits, then close via the same cyclic-successor endgame as `transversal-saturation` but with a cleaner, smaller $L$.
**Skeleton:**
  1. Linchpin + gap bound *(proved, as above)*.
  2. **(LOCK CASE, proved)** If some $a_i=p^k$ (support $\{p\}$), every later term is a $p$-multiple (must share with $a_i$); any two $p$-multiples share $p$; so every $p$-multiple $>a_n$ is admissible ⇒ greedy picks $a_n+p$. Hence $T=1,L=p$. Done in this branch.
  3. **(NO-LOCK CASE)** Assume no $a_i$ is a prime power, so $|S(a_i)|\ge2$ for all $i$.
  4. **(GAP C — no-lock structural bound)** In a pairwise-intersecting family with every set of size $\ge2$, generated by this greedy, prove the minimal-transversal primes are bounded — conjecturally by $M_1$ itself or by $2\cdot p_{\min}(a_1)$ (matches the empirical max-gap $=2p_{\min}$). Mechanism to attempt: in the no-lock regime, every $P_1$-prime recurs as a divisor of infinitely many terms (else the terms avoiding it would have supports shrinking to a singleton $\Rightarrow$ lock, contradiction); hence every minimal transversal is "carried" by recurring $P_1$-primes and large free-riders are forced redundant faster.
  5. Stabilization of $\operatorname{MT}(\mathcal F_n)$ in the no-lock regime (consequence of Gap C, finite poset).
  6. Cyclic-successor bijection on $\mathcal B_\infty\bmod L$ ⇒ cycle ⇒ $a_{n+T}=a_n+L$.
  7. Pure-from-start: in the no-lock case the gap distribution is tight (empirically $\le2p_{\min}$, provably $\le M_1$); combine with the bijection/cycle and backward-extension as in `transversal-saturation` Gap B — but the no-lock structural bound may make the backward step cleaner (the greedy never needs large primes within the tight window).
**Key lemmas:**
  - Lock lemma *(proved)*.
  - **(GAP C)** No-lock ⇒ minimal-transversal primes bounded — because every $P_1$-prime recurs (else lock), forcing large free-riders redundant.
  - Gap B (pure-from-start) — reuses the backward-extension mechanism.
**Open gaps:** C (no-lock structural bound), B (pure-from-start, possibly easier here).
**Cases to cover:** (i) lock (some $a_i=p^k$); (ii) no-lock. Exhaustive.
**Watch out for:** must prove the dichotomy is exhaustive (either some term is a prime power, or none is — trivially exhaustive) and that the no-lock case genuinely yields a *sharper* bound than the general Gap A (else this collapses into `transversal-saturation` with an unnecessary split). The "every $P_1$-prime recurs" sub-lemma is the load-bearing new idea and may itself fail (e.g. one $P_1$-prime might drop out without forcing a lock) — flag it.
**Why far from the others:** it is the only approach that *splits* and gets a whole branch (lock) for free, attacking only the no-lock regime with extra structural hypotheses. Its hard step (Gap C) uses the "size-$\ge2$ + no singleton ever" hypothesis, a mechanism unavailable to approaches 1/3/4 which must work in full generality.

---

### `growing-modulus-descent`
**new** — explicit-$L$ construction via a growing modulus with descent termination (framing 2).
**Target:** full claim, with $L$ constructed (not just witnessed).
**Framing.** Do NOT go through "stabilize $\mathcal B_n$ then conclude periodic." Instead *construct* the modulus $L$ inductively: start $L_0=\operatorname{rad}(a_1)$; whenever a "pulled-in" prime $q$ (a non-$P_1$ prime entering some minimal transversal) appears, enlarge $L_{k+1}=L_k\cdot q$; prove this growth process terminates by a descent on a finite "free-rider inventory"; once $L$ stops growing, show the greedy on residues $\bmod L$ is a cyclic successor (bijection on a finite residue set), giving the AP directly — the cyclic-bijection argument replaces the "stabilize then pigeonhole" step.
**Skeleton:**
  1. Linchpin + gap bound *(proved)*.
  2. Define a *pulled-in prime*: $q\notin P_1$ that lies in some minimal transversal of $\mathcal F_n$ at some $n$. Each pulled-in prime enlarges the candidate modulus: $L = \operatorname{lcm}(P_1\cup\{\text{pulled-in primes}\})$.
  3. **(GAP D — descent termination)** The set of pulled-in primes is finite. Mechanism (genuinely different from Gap A): attach to each pulled-in prime $q$ its *witness type* $=\{(p,S(a_i)\cap P_1):q\in T,\ T\text{ minimal transversal avoiding }p\}$, a finite object (since $P_1$ finite and $S(a_i)\cap P_1\subseteq2^{P_1}$). Define an integer-valued rank $r(q)$ strictly decreasing along the order of pull-in events within a fixed type. Since ranks are non-negative, only finitely many pull-in events per type; finitely many types ⇒ finitely many pulled-in primes ⇒ $L$ stabilizes at some $L^*$.
  4. Once $L^*$ stable, the admissible set $\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\{m:\operatorname{rad}(T)\mid m\}$ is $L^*$-periodic.
  5. **(GAP E — greedy = cyclic successor)** At this stage, prove the greedy picks the cyclic successor of $a_n$ in $\mathcal B_\infty\bmod L^*$: i.e. $\min(\mathcal B_\infty\cap(a_n,\infty))$ is admissible at step $n$ (no hidden constraint from $\mathcal F_n\setminus\mathcal F_\infty$ bites first). Bijection $\Rightarrow$ cycle $\Rightarrow$ $a_{n+T}=a_n+L^*$.
  6. Pure-from-start: as in Gap B, backward extension; here the hope is that the descent termination itself supplies an *index* after which $L$ is fixed, and one separately matches the finitely many early terms.
**Key lemmas:**
  - Gap D (descent on pull-in types) — because rank $r(q)$ strictly decreases per type and types are finite.
  - Gap E (greedy = cyclic successor once $L^*$ fixed).
  - Gap B (pure-from-start).
**Open gaps:** D, E, B.
**Cases to cover:** even / prime-power / general (general handled here).
**Watch out for:** the "rank" in Gap D must be concretely defined and strictly decreasing — a vague descent is the failure mode. Gap E is essentially Gap B restated; do not assume stabilization of $L$ alone forces the greedy to coincide with the cyclic successor (the 385 data shows $\mathcal B_n$'s small-prime part stabilizes long before the greedy becomes periodic). The cyclic-bijection step is sound only *after* Gap E.
**Why far from the others:** it is the only approach that *constructs $L$ explicitly* and uses the modulus-growth + descent as the spine, not the antichain monovariant. Its gap (D) is a typed descent, structurally different from Gap A's "shrink the antichain" and Gap C's "no-lock structure."

---

### `free-rider-type-replacement`
**new** — pigeonhole on free-rider types with a same-type replacement lemma (framing 1 variant, different mechanism).
**Target:** full claim.
**Framing.** Bypass the global antichain monovariant. Classify each non-redundant ("free-rider") prime $q$ by a finite *type* determined by $P_1$ alone (which $P_1$-primes co-occur with $q$ in its witnessing term, and which $P_1$-primes the witnessing minimal transversal avoids). Prove a *same-type replacement lemma*: two free-riders of the same type cannot both persist — the later one makes the earlier redundant. Hence at most (number of types) free-riders ever persist simultaneously; the active free-rider set is finite and eventually constant; reduce to the finite-state endgame.
**Skeleton:**
  1. Linchpin + gap bound *(proved)*.
  2. Define type of a non-redundant prime $q$ at its insertion: $\tau(q)=(A(q),B(q))$ where $A(q)=S(a_i)\cap P_1$ for the witnessing term $a_i$ (the term whose non-redundancy forces $q$ in), and $B(q)\subseteq P_1$ is the set of $P_1$-primes avoided by some minimal transversal $T$ with $q\in T$. Both $A,B\subseteq2^{P_1}$, finitely many types.
  3. **(GAP F — same-type replacement)** If two non-redundant primes $q_1<q_2$ (in insertion order) have the same type $\tau$, then $q_1$ becomes redundant after $q_2$'s insertion. Mechanism: same type ⇒ the constraint forcing $q_1$ is subsumed by the constraint forcing $q_2$ (they index the same "avoidance pattern" in $\mathcal F_n$); once $q_2$ is pinned, every minimal transversal using $q_1$ is dominated by one using $q_2$, so $q_1$ leaves the minimal-transversal family. *(this is the load-bearing new lemma — flag as unproved)*.
  4. Consequence: at most $|2^{P_1}\times2^{P_1}|$ non-redundant large primes are *active* at any step. The active free-rider set $Q_n$ is non-decreasing-bounded ⇒ eventually constant $Q_\infty$ (each slot can turn over only when a same-type replacement occurs, and replacements strictly increase the witnessing $a_i$, bounded by... )
  5. **(GAP G — turnover terminates)** The replacement chain in each type-slot terminates (each replacement strictly increases the witnessing term's value, but values are unbounded — so need a different descent; e.g. the replaced prime's set of "covered" transversals strictly grows, bounded above by $2^{|\operatorname{MT}|}$). 
  6. Once $Q_\infty$ stable, $\operatorname{MT}(\mathcal F_n)$ stabilizes (primes bounded by $P_1\cup Q_\infty\cup\{\text{small}\}$) ⇒ $\mathcal B_\infty$ $L$-periodic.
  7. Cyclic-successor bijection ⇒ cycle ⇒ AP; pure-from-start via backward extension (Gap B).
**Key lemmas:**
  - **(GAP F)** Same-type replacement — because same-type free-riders index the same avoidance pattern, so the later dominates the earlier in every minimal transversal.
  - **(GAP G)** Replacement turnover terminates — because each replacement strictly grows the set of covered transversals, bounded by $2^{|\operatorname{MT}|}$.
  - Gap B (pure-from-start).
**Open gaps:** F, G, B.
**Cases to cover:** general (lock cases subsumed).
**Watch out for:** Gap F is the crux and may be FALSE — same-type primes might coexist without replacement. If so, this approach dies; but the type classification is fine-grained enough (using the avoided-$P_1$-prime set) that replacement is plausible. Gap G's descent must not be on the witnessing $a_i$ value (unbounded) — it must be on a finite coverage set.
**Why far from the others:** it is the only approach whose spine is *competition/replacement among free-riders of the same type*, not a global monovariant or a growing modulus. It localizes the finiteness to per-type slots, a genuinely different mechanism from the antichain descent (approach 1), the no-lock split (approach 2), and the modulus-growth (approach 3).

---

### Proposed slugs (build set candidates)

- `transversal-saturation` — canonical antichain-monovariant route; gaps A (transversal-prime finiteness) and B (pure-from-start).
- `prime-power-dichotomy` — lock branch free, no-lock branch uses size-$\ge2$ structure for a sharper bound; gap C.
- `growing-modulus-descent` — construct $L$ inductively, prove growth terminates by typed descent; gaps D, E.
- `free-rider-type-replacement` — same-type replacement lemma bounds active free-riders; gaps F, G.

All four share the PROVED foundation (linchpin + gap bound) and the cyclic-successor endgame; they differ in the *spine* used to prove finiteness of the governing prime set — antichain shrink / no-lock structure / typed descent on $L$ / type-competition. None routes through the false "small-prime family stabilizes" step.
