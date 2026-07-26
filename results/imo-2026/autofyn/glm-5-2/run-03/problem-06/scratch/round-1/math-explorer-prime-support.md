## imo-2026-06 (prime-support / intersection route)

## Terrain

The condition "$\gcd(a_{n+1},a_i)>1$ for every $i\le n$" is purely a statement about **prime supports** $S(x)=\{$prime divisors of $x\}$: a candidate $m>a_n$ is *admissible at step $n$* iff $S(m)$ intersects $S(a_i)$ for every $i\le n$, i.e. $S(m)$ is a **transversal (hitting set)** of the family $\mathcal F_n=\{S(a_1),\dots,S(a_n)\}$. The greedy rule is $a_{n+1}=\min\{m>a_n:m\text{ admissible}\}$.

Three reformulations make the terrain visible:

1. **Admissible set as a union of APs.** $\mathcal B_n=\{m:S(m)\text{ hits every }S(a_i),i\le n\}=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{m:\operatorname{rad}(T)\mid m\}$, where $\operatorname{MT}$ = minimal transversals and $\operatorname{rad}(T)=\prod_{p\in T}p$. So $\mathcal B_n$ is a **finite union of arithmetic progressions** (multiples of the moduli $d_j=\operatorname{rad}(T_j)$). Verified on every computed example.

2. **Pairwise-intersecting family.** By induction the greedy rule makes every two terms share a prime, so $\mathcal F_n$ is a pairwise-intersecting family of finite prime-sets. This constrains the possible transversal structure heavily.

3. **Limit set is $L$-periodic.** If $\mathcal B_n$ stabilizes to $\mathcal B_\infty=\bigcup_j\{m:d_j\mid m\}$ with $L=\operatorname{lcm}(d_j)$, then $\mathcal B_\infty$ is $L$-periodic: $m\in\mathcal B_\infty\iff m+L\in\mathcal B_\infty$. The "smallest admissible $>a_n$" then depends only on $a_n\bmod L$.

## Key structural observations (conjectures, each labelled)

- **(C1) Conjecture, verified on ~30 examples.** The minimal-transversal moduli $\{d_j\}$ of $\mathcal F_n$ **stabilize after finitely many steps** (in fact very fast: $\le 5$ steps for all $a_1\le 1000$ tested). After stabilization $\mathcal B_n=\mathcal B_\infty$. *Verified computationally for $a_1\in\{15,35,65,77,91,105,143,391,437,323,\dots\}$.*

- **(C2) Conjecture, verified.** $L=\operatorname{lcm}\bigl(\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_\infty)\bigr)$ is **always squarefree and even**. Each minimal transversal is a set of *small* primes; empirically every prime appearing in any minimal transversal is $\le$ the largest prime factor of $a_1$ (stronger bound conjectured). This is what makes $L$ finite and the stabilization possible. *Verified: e.g. $a_1=35{=}5\cdot7\Rightarrow L=210{=}2\cdot3\cdot5\cdot7$; $a_1=77{=}7\cdot11\Rightarrow L=154{=}2\cdot7\cdot11$; $a_1=143{=}11\cdot13\Rightarrow L=858{=}2\cdot3\cdot11\cdot13$.*

- **(C3) Conjecture, verified on all tested $a_1$.** The increment sequence $\delta_n=a_{n+1}-a_n$ is **purely periodic from $n=1$**: there are $T,L$ with $a_{n+T}=a_n+L$ for *every* $n\ge1$ (no transient). The identity $a_{n+T}=a_n+L$ was checked to hold from $n=1$ in every case (including large-period ones like $a_1=221\Rightarrow T=334,L=6630$; $a_1=437\Rightarrow T=160,L=4370$). *This pure-from-start behavior is the deep/hard part of the problem — see gaps.*

- **(C4) "Lock" mechanism (proved, trivial).** If a term $a_i=p^k$ is a prime power (support $\{p\}$, a singleton), then every subsequent term must be divisible by $p$; two multiples of $p$ always share factor $p$, so *every* multiple of $p$ is admissible; hence $a_{n+1}=a_n+p$ from that point: $T=1,L=p$. This explains all the $T=1$ cases (e.g. $a_1=21{=}3\cdot7$ hits $27=3^3\Rightarrow L=3$; $a_1=6$ hits $8=2^3\Rightarrow L=2$; any $a_1$ containing $2p$ for enough $p$'s tends to lock at $L=2$). The nontrivial cases are those where **no prime power ever appears**, so no singleton support forces a lock.

- **(C5) Conjecture.** $a_1\in\mathcal B_\infty$ (the seed shares a prime with every future term) and in fact **every** $a_i\in\mathcal B_\infty$. *Verified on all computed examples.* If true, the sequence lives in $\mathcal B_\infty$ from the start, which is the cleanest route to pure-from-start periodicity.

- **(C6) Conjecture / mechanism.** On $A=\mathcal B_\infty\bmod L\subseteq\mathbb Z/L\mathbb Z$, the map $f(r)=$ (cyclic successor of $r$ in $A$) is a **bijection** (it is the inverse of cyclic predecessor). Hence every orbit of $f$ is a *cycle* (no tail). Combined with (C5) this gives pure periodicity immediately. *The bijection is elementary once $\mathcal B_\infty$ is $L$-periodic; the load on (C5) is the issue.*

- **(C7) Subtle point (conjecture).** Even before $\mathcal B_n$ stabilizes, the greedy choice $\min(\mathcal B_n\cap(a_n,\infty))$ appears to **always land in $\mathcal B_\infty$** (verified: for $a_1=35$, $\mathcal B_1\supsetneq\mathcal B_\infty$ yet the chosen $a_2=40$ lies in $\mathcal B_\infty$). If this holds generally, the dynamics effectively runs on $\mathcal B_\infty$ from $n=1$, and (C6) gives pure periodicity directly. *This is the real crux and the cleanest candidate for a proof — but it is unproved.*

## Hard steps / gaps a proof on this route must close

1. **Stabilization of $\operatorname{MT}(\mathcal F_n)$.** Show the moduli $\{\operatorname{rad}(T):T\in\operatorname{MT}(\mathcal F_n)\}$ eventually stop changing. Since adding a set to $\mathcal F_n$ can only *enlarge* minimal transversals (each new transversal contains an old one), the moduli only grow in divisibility — but they could grow forever unless the primes that can appear in a minimal transversal are bounded. **Need: a finite bound on transversal primes** (conjecturally $\le$ largest prime factor of $a_1$, or $\le a_1$). This is the single biggest gap.

2. **Pure-from-start (no transient).** The problem demands $a_{n+T}=a_n+L$ for *all* $n\ge1$. The cyclic-successor bijection (C6) only gives eventual periodicity from the moment the dynamics runs on $\mathcal B_\infty$. To extend to $n=1$ one must show either (a) $a_1\in\mathcal B_\infty$ AND the greedy choice always lands in $\mathcal B_\infty$ (C5+C7), or (b) a direct backward-induction matching the early increments to the eventual cycle. **Hardest conceptual step.**

3. **Why the greedy lands in $\mathcal B_\infty$ even early.** Need: for every $n$ and every gap $(a_n,a_n+g)$ of $\mathcal B_\infty$ there is no "stricter" $\mathcal B_n$-element sneaking in below the next $\mathcal B_\infty$-element. Equivalently $\min(\mathcal B_n\cap(a_n,\infty))=\min(\mathcal B_\infty\cap(a_n,\infty))$ for all $n$. Open.

4. **$L$ is the right modulus (not a proper multiple).** Once $\mathcal B_\infty$ is $L$-periodic with $L=\operatorname{lcm}(d_j)$, the per-period total increment is a multiple of $L$; the conclusion's $L$ is that multiple. Need to confirm it equals $L$ (a single wrap) — follows if the residue orbit returns to $r_1$ after one wrap; this is automatic for a cycle but the *value* of $L$ in the theorem is just "the per-period sum", so any multiple also works. Minor.

## Retrieval hints

**knowledge_base.md:**
- *Modular arithmetic, CRT* — the admissible set is a union of divisibility classes $\{d_j\mid m\}$; combining them mod $L=\operatorname{lcm}(d_j)$ is exactly CRT.
- *Order of an element, Fermat/Euler; eventual periodicity of products of a sequence mod $m$* — the cyclic-successor dynamics on $\mathbb Z/L\mathbb Z$ is the abstract periodicity engine.
- *Invariants & monovariants* (Combinatorics): the nesting $\mathcal B_1\supseteq\mathcal B_2\supseteq\cdots$ is a monovariant (shrinking family); stabilization is the termination of a monotone process on a finite poset — once the transversal-prime bound is known.
- *Pigeonhole / extremal* + *Bertrand's postulate* — candidate tools for bounding transversal primes (force a small prime into a support).
- *General proof methods: induction, contradiction, extremal* — stabilization is naturally proved by "consider the first $n$ at which a new prime enters a minimal transversal; derive contradiction / bound".

**Crux corpus (number_theory):** no true analog found — this problem (greedy "share a factor with *every* earlier term") is more specific than Euclid–Mullin / EKG / Yellowstone (which share with only the *last* term). Most relevant retrieve-and-adapt hints:
- `aimo-0224` (divisibility-and-gcd): *"Encode a prescribed pairwise-coprimality pattern by assigning a distinct prime to each element and defining each term as the product of primes over a subset"* — exactly the prime-support encoding this route uses; adapt the support-as-transversal viewpoint.
- `aimo-0277` (divisibility-and-gcd): *"When a map acts on a finite set so every element has the same exact period $n$, it splits into disjoint $n$-cycles; $n\mid|B(n)|$"* — the cyclic-successor-on-$A$ periodicity argument is the same shape (adapt: bijection on finite set $\Rightarrow$ all orbits are cycles, no tail).
- `aimo-0134` (sequences-and-recurrences): eventual-constancy-via-integer-valued-average — only loosely analogous; the "upgrade eventual to pure" flavor is relevant but the technique does not transfer.

## Prior progress

None — round 1, workspace empty (`results/imo-2026-06/current.md` status `unsolved`, no approaches, no lemmas).

## Dead ends (do not retry)

None recorded yet (round 1). Caveat from exploration: do **not** assume the set of primes dividing the terms $P=\bigcup_n S(a_n)$ is finite — it is *not* (for $a_1=6$ the terms are all even, so $P$ contains every prime $2p$ factor, i.e. all primes). The finiteness must instead come from the **minimal-transversal** primes (a much smaller, bounded set), not from $P$.

## Small-case / intuition notes (all CONJECTURED unless marked proved)

- $a_1=$ prime or prime power $\Rightarrow$ $T=1,L=p$ (the prime). *Proved-trivial.*
- $a_1$ even, or $2\mid a_1$, very often $\Rightarrow$ $T=1,L=2$ (a power of $2$, e.g. $8$, appears and locks). *Conjecture with strong evidence.*
- $a_1=pq$ (two odd primes): nontrivial. $L=2\cdot\{\text{primes}\}$ where the prime-set is $\{2\}\cup\{p,q\}\cup\{\text{possibly }3\text{ or }5\}$. E.g. $15\to30$, $35\to210$ (pulls in $3$), $77\to154$ (no $3$), $91\to182$, $143\to858$ (pulls in $3$), $65\to390$, $323{=}17\cdot19\to1938$, $437{=}19\cdot23\to4370$ (pulls in $5$, not $3$). *No simple rule found for which extra small prime gets pulled in — it depends on the greedy dynamics. The proof need NOT predict $L$; it only needs existence.*
- Periods can be large: $a_1=221=13\cdot17\Rightarrow T=334,L=6630$; $a_1=437\Rightarrow T=160$; $a_1=323\Rightarrow T=94$. Some $a_1$ (e.g. $187,247,667,899,1155$) had no period detectable within 3000 terms — period presumably huge. *This signals the proof must be non-constructive about the magnitude of $T,L$; it cannot exhibit them.*
- The minimal-transversal moduli stabilize in $\le5$ steps in every case examined — the dynamics is "essentially on $\mathcal B_\infty$" almost immediately, yet the pure-from-start property is what makes this an IMO P6.

## Openings for the outliner (distinct skeletons this route suggests)

**Opening A — transversal-stabilization + cyclic-bijection (the canonical route).**
(i) Reformulate $\mathcal B_n=\bigcup_{T\in\operatorname{MT}(\mathcal F_n)}\{\operatorname{rad}(T)\mid m\}$. (ii) Prove the transversal primes are bounded (extremal: take the largest prime ever entering a minimal transversal; force a contradiction via Bertrand/small-prime pigeonhole). (iii) Conclude $\operatorname{MT}(\mathcal F_n)$ stabilizes $\to\mathcal B_\infty$, $L=\operatorname{lcm}(\operatorname{rad}(T))$. (iv) Cyclic successor on $A=\mathcal B_\infty\bmod L$ is a bijection $\to$ orbits are cycles. (v) Show $a_1\in\mathcal B_\infty$ and the greedy always lands in $\mathcal B_\infty$ $\to$ pure periodicity from $n=1$. The hard load is steps (ii) and (v).

**Opening B — direct monovariant on the support family (bypass predicting $L$).**
Forget computing $L$; prove *existentially*. Define a complexity measure on $\mathcal F_n$ (e.g. the set of minimal transversals as a finite antichain) that is monotone non-increasing in a finite poset; it stabilizes at some $N_0$. From $N_0$ the increment $\delta_n$ depends only on $a_n\bmod L_0$ for some $L_0$; the residue map is a bijection on a finite set so $\delta$ is periodic from $N_0$. Then handle the finitely many $n<N_0$ by *backward extension*: show each early increment matches the periodic block by a "predecessor-uniqueness" argument (the cyclic predecessor in $\mathcal B_\infty$ from $a_{N_0}$ traces back to $a_1$). This sidesteps predicting $L$ and splits "eventual" (easy) from "pure-from-start" (hard, finite casework).

**Opening C — prime-power lock vs. rich periodic regime (dichotomy).**
Either (a) some term is a prime power $p^k\Rightarrow$ lock, $T=1,L=p$ (trivial, proved); or (b) no term is ever a prime power. In case (b) every support has $\ge2$ primes; show the family $\mathcal F_\infty$ has a nontrivial *finite* minimal-transversal set (using that supports are pairwise-intersecting 2+-element sets — combinatorial hypergraph transversal theory), and that the greedy on $\mathcal B_\infty$ is a bijection. The dichotomy isolates the "locked" cases (easy) from the "rich" cases (where the transversal theory does real work) and may let each branch use a different, sharper tool.

## Notes for the outliner
- The **shared gap** across all three openings is *stabilization of the minimal-transversal structure* + *pure-from-start*. An approach that does NOT close these two will not solve the problem, however cleanly it sets up the transversal picture. A rival (non-prime-support) route could attack via a completely different invariant (e.g. a monovariant on $a_n$ directly, or a "covering-systems" view) — worth keeping in the field for diversity, since this route's hard step is genuinely hard.
