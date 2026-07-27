# IMO 2026 P6 — greedy-gap / difference-sequence route

## imo-2026-06

**Framing.** Let $d_n=a_{n+1}-a_n$. The target $a_{n+T}=a_n+L$ is exactly "$(d_n)$ is eventually periodic with period $T$ and period-sum $L$." So this route attacks the gap sequence directly: identify a finite state governing $d_n$, show the update is deterministic, conclude eventual periodicity.

### Distinct openings (each a different whole-claim attack the outliner could build)

1. **Residue-block state machine (mod $L=\prod P$).** Conjecture (verified empirically, see below): there is a finite squarefree "essential" prime set $P$ and a *block* $B\subseteq \mathbb Z/L\mathbb Z$, $L=\prod_{p\in P}p$, such that (i) every tail term satisfies $a_n\bmod L\in B$; (ii) $B$ is pairwise-intersecting: any two $b,b'\in B$ share a prime of $P$; (iii) the transition is *purely cyclic on $B$*: from residue $r\in B$, $a_{n+1}$ is the smallest integer $>a_n$ whose residue is the next element of $B$ above $r$ (cyclically). Then $d_n=(\text{next}(r)-r)\bmod L\le L$, the state space is the finite set $B$ (or $\mathbb Z/L\mathbb Z$), update deterministic $\Rightarrow$ eventually periodic, $T=|B|$-ish, $L=\prod P$. **Verified for $a_1=15$:** $B=\{0,6,10,12,15,18,20,24\}\bmod 30$, $T=8$, $L=30$; the cyclic-next rule reproduces the sequence exactly (confirmed by code).

2. **"Smallest-valid-$m$" as CRT/Covering problem.** Reframe the greedy rule: $a_{n+1}$ is the least $m>a_n$ such that for every $i\le n$, $\exists$ prime $p\mid a_i$ with $p\mid m$. Equivalently the prime-divisor set $S(m)$ must *hit* every $S(a_i)$. Once $P$ stabilizes, this is a finite covering-residue condition: $m$ valid $\iff$ for each "constraint class" of prior terms, $m$ is divisible by some $p$ in that class. The least $m>a_n$ hitting a fixed finite family of residue (divisibility) conditions is periodic in $a_n\bmod L$ (it is the least element of a periodic set above $a_n$). This is the cleanest "finite state $\to$ periodic" lever — periodicity comes from the *periodicity of the set of valid residues mod $L$*, no need to track a moving state at all. This is arguably the most direct attack and does NOT need the block $B$ machinery, only "$P$ finite" + "valid set is periodic mod $L$."

3. **Bounded-gap + pigeonhole on residues (no explicit $P$ needed a priori).** Prove directly: (a) gaps $d_n$ are bounded by some constant $G$ (need: a valid $m$ always exists within $G$ of $a_n$); (b) then $a_n\bmod M$ (for a suitable $M$, e.g. $M=\prod_{p\le G} p$ or $M=$ lcm of primes $\le G$) evolves in a finite set; (c) once $a_n\bmod M$ repeats, the future repeats. The crux becomes "bounded gaps" rather than "finite $P$" — a possibly easier target. The link: a valid $m$ within $G$ exists iff the periodic residue set mod $L$ is nonempty in every window of length $G$; bounded gaps and finite-$P$ are dual. (This is the closest to the classical aimo-0678 "bound one coordinate, reduce the other mod lcm" move.)

### Candidate technique(s)
- **Finite-state / deterministic-update $\to$ eventual periodicity** (the core engine). Crux corpus analogues: `aimo-0678` (IMO-SL 2015, "eventually periodic" via bound + reduce mod lcm of bounded values $\to$ finite pairs), `aimo-0577` (IMO-SL 2022, invert update on finite invariant set $\to$ permutation $\to$ periodic orbit), `aimo-0982` (reduce digit-sampling to $2^n\bmod d$, eventually periodic).
- **Covering / hitting-set** language for the gcd condition ($S(m)$ hits every $S(a_i)$).
- **Bertrand / smooth-number** style bounding to control new-prime introduction (cf. `aimo-0682` smooth-part bound, `aimo-0415` size threshold forcing a prime-power factor).

### Cheap-kill candidates
- **$2\mid a_1$ $\Rightarrow$ $T=1,L=2$ trivially** (all terms even, smallest even $>a_n$ works; 2 covers every gcd). Similarly $a_1$ divisible by smallest prime $p$ and $a_1$ "small enough" $\Rightarrow T=1,L=p$. These are structural pruning for special starts but the problem needs the general case.
- **Pairwise-intersecting check:** in the periodic regime, validity of $m$ reduces to "$m\bmod L\in B$" only because $B$ is pairwise-intersecting under $P$; this is the injectivity that makes the state well-defined.

### Knowledge-base entries to use
- **Order of an element, Fermat/Euler** + **Linear recurrences** ("eventual periodicity of products of a sequence mod $m$") — the engine once state is reduced mod $L$.
- **Modular arithmetic, CRT** — to combine the per-prime divisibility conditions into "valid residues mod $L$."
- **Bertrand's postulate / smooth-number bounds** — to attack the crux (no new essential primes after a point).
- **Pigeonhole / extremal principle** — for the bounded-gap $\to$ residue-repeat step.

### Analogous past problems (cruxes)
- **`aimo-0678` (IMO-SL 2015)** — *the* closest analogue. Two coupled integer recurrences; crux: "Once one coordinate of a coupled integer recurrence is bounded, reduce the other modulo the lcm of all its bounded values; finitely many pairs forces the pair to be eventually periodic." Directly maps: bound the gap $d_n$ (or the prime set), reduce $a_n$ mod $L$, finite state $\to$ periodic.
- **`aimo-0577` (IMO-SL 2022)** — crux: "Invert a piecewise update map on a finite invariant set to show it is a permutation; the orbit is periodic." Maps to: show the residue update on $B$ is a bijection (inverse = previous element cyclically), hence every orbit is periodic (no preperiod needed).
- **`aimo-0982` (IMO-SL 2006)** — crux: reduce a subsequence sampled at moving indices to $2^n\bmod d$; factor $d=2^u v$, show $2^{n+w}\equiv2^n\pmod d$ for $n\ge u$ (eventual periodicity from finite modulus). Maps to: the "$\gcd(m,a_i)>1$" condition is periodic in $m\bmod L$, so $a_n\bmod L$ governs the future.

### Prior progress
None (round 1; workspace empty, no approaches registered).

### Dead ends (do not retry)
None yet.

### The crux / hard steps (in order of difficulty)

**CRUX 1 (the wall): the essential prime set $P$ is finite.** A prime $q$ is "essential" if it is ever the *unique* shared factor linking some new $a_{n+1}$ to some prior $a_i$ (i.e. needed). Free-rider primes (e.g. 7 dividing 70 and 84 while 2 also links them) are NOT essential. Empirically $P$ is always finite and small, but *proving no new essential prime appears* is the load-bearing step. Two sub-angles:
  - (a) *Bounded gaps imply finite essential primes.* If $d_n\le G$ eventually, then every $a_{n+1}\le a_n+G$; any prime $q>G$ dividing $a_{n+1}$ does so to the first power and $a_{n+1}/q < a_n/G+1$ — large primes are "thin" and can't be the unique link (pigeonhole: a large prime $q$ appears in $\le \lceil N/G\rceil$ terms up to $N$, and to be the unique link it must co-occur with... ). Needs care.
  - (b) *Self-sustaining block.* Once a candidate block $B$ (mod $L$) is pairwise-intersecting and "greedy-closed" (the cyclic-next residue is always $\le L$ away), no new essential prime is ever needed: the greedy finds a valid $m$ using only $P$ within distance $L$. So it suffices to exhibit, after a finite transient, a closed block — the essential primes are exactly those appearing in $B$. The transience comes from a finite "saturation" of prime introduction. This is circular-ish but can be broken by an extremal/maximality argument: take the *limit* block $B_\infty$ = union of all residues ever visited; show it stabilizes because each new essential prime strictly grows $L$ and... (need a bound on $|P|$).

**CRUX 2: validity reduces to residues mod $L$.** Once $P$ is fixed, $m$ is valid iff $S_P(m)=\{p\in P:p\mid m\}$ hits $S_P(a_i)$ for every prior $i$. In the periodic regime all prior residues lie in $B$, so this becomes "$m\bmod L\in B$" iff $B$ pairwise-intersecting. The subtlety: *transient* terms (before $B$ is reached) impose constraints not captured by $B$. Need: after some $N$, every prior $a_i$'s $P$-support is *superseded* by a block member — i.e. the block $B$ "covers" every transient constraint. Plausible because transients are finitely many and each is eventually dominated, but must be proved (not hand-waved).

**CRUX 3 (easy, once 1&2): finite state $\to$ periodic.** Standard. $a_n\bmod L$ finite, deterministic update $\Rightarrow$ eventually periodic. This is `aimo-0677`/`aimo-0577` territory.

### Experiments + data (conjecture, not proof)

Generated the greedy sequence for many $a_1$ (code: sympy `factorint`/`gcd`, naive $O(n^2)$ scan). Confirmed eventual periodicity in every case that terminated:

| $a_1$ | $T$ | $L$ | $P$ (prime factorization of $L$) |
|---|---|---|---|
| $15=3\cdot5$ | 8 | 30 | $\{2,3,5\}$ |
| $35=5\cdot7$ | 34 | 210 | $\{2,3,5,7\}$ |
| $45=3^2\cdot5$ | 8 | 30 | $\{2,3,5\}$ |
| $65=5\cdot13$ | 58 | 390 | $\{2,3,5,13\}$ |
| $77=7\cdot11$ | 18 | 154 | $\{2,7,11\}$ |
| $91=7\cdot13$ | 20 | 182 | $\{2,7,13\}$ |
| $143=11\cdot13$ | 64 | 858 | $\{2,3,11,13\}$ |
| $55=5\cdot11$ | 1 | 5 | $\{5\}$ |
| $85=5\cdot17$ | 1 | 5 | $\{5\}$ |
| $119=7\cdot17$ | 1 | 7 | $\{7\}$ |
| $133=7\cdot19$ | 1 | 7 | $\{7\}$ |
| $210,30,6,12$ | 1 | 2 | $\{2\}$ (any even $a_1$) |
| $3,21,33,231$ | 1 | 3 | $\{3\}$ (odd $a_1$ div by 3, not 2) |
| primes $p$ | 1 | $p$ | $\{p\}$ |

**Key empirical facts (conjecture):**
- $L$ is always **squarefree** = product of an essential prime set $P$. $T\le L$.
- If $2\mid a_1$: $P=\{2\}$, $T=1$. If $2\nmid a_1$ but $3\mid a_1$: $P=\{3\}$, $T=1$.
- For $a_1=pq$ ($p<q$ odd primes, $p\ge5$): there is a **threshold phenomenon** — small $q$ gives an "escape" ($P$ grows to include 2 and possibly 3 plus $p,q$, e.g. $35=5\cdot7\to\{2,3,5,7\}$, $65\to\{2,3,5,13\}$, $77\to\{2,7,11\}$), while large $q$ **collapses to $P=\{p\}$, $T=1$** (e.g. $55=5\cdot11\to\{5\}$, $85=5\cdot17\to\{5\}$, $119=7\cdot17\to\{7\}$). Mechanism: $a_2=p(q+1)$ is always even, introducing the free prime 2; whether 2 (and 3) get *locked as essential* depends on whether the greedy thereafter finds smaller non-$p$-multiple candidates (only possible when $q$ is small enough that $2q$-type links beat the next multiple of $p$). For large $q$, multiples of $p$ always win, $P$ collapses to $\{p\}$.
- For $a_1=15$: block $B=\{0,6,10,12,15,18,20,24\}\bmod30$; $B$ is pairwise-sharing-a-prime-under-$\{2,3,5\}$; the cyclic-next rule on $B$ reproduces the entire tail (code-verified). This validates the state-machine model of opening (1).
- $a_1=55$: tail is *all multiples of 5* ($+5$ each step), even though early terms are even — 2,3,11 all *drop out* as non-essential. Confirms "essential $\ne$ appears in factorization."
- $a_1=385=5\cdot7\cdot11$: no period found within 2000 terms (large/slow transient) — suggests the transient can be long and $L$ can be large; the proof must not assume a small bound. (Did not finish; budget.)

**Intuition for the outliner:** the proof almost certainly runs as *bound the essential prime set $P$ (CRUX 1) $\to$ reduce validity to residues mod $L=\prod P$ (CRUX 2) $\to$ finite-state periodicity (CRUX 3, free)*. The single hardest step is CRUX 1; the cleanest known lever is the **bounded-gap + smooth-number** angle (opening 3): prove $d_n\le G$ eventually (the periodic residue set mod $L$ is syndetic), which simultaneously gives finiteness of essential primes (any prime $>G$ can't be the unique link in a bounded-gap world) and the finite modulus. Opening 2 (valid-set-is-periodic) is the most direct if one can establish "$P$ finite" first via a maximality/saturation argument on the limit block $B_\infty$. Opening 1 gives the most explicit description of $T,L$ but requires the most machinery.
