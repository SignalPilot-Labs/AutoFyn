## imo-2026-06 — route (b): direct ERGODIC / pigeonhole argument on the realized orbit of the WINDOW-STATE; prove the realized state SET is finite WITHOUT requiring the transition to be finitely determined.

Start 2026-07-25 17:08 UTC. Inputs read: `run_state.md` (round-3 directive, 7 dead mechanisms, all rules), `current.md` (Gap A = finiteness of governing primes / L-periodicity of B_∞; endgame + pure-from-start + LOCK all certified), the 21 certified lemmas (esp. `linchpin-and-gap-bound` d_n≤M_1, `greedy-equals-cyclic-successor`, `cyclic-successor-bijection`, `syndetic-divisible-closed-not-periodic` (−), `binfinity-divisibility-progression-structure`), the three round-3 explorer reports, `knowledge_base.md`, `crux_moves_documentation.md`, and the crux corpus.

### The precise statement that would close Gap A via this framing

(*) *There exists a finite state space $\Sigma$ and a state $\sigma_n\in\Sigma$ computable from the orbit prefix $(a_1,\dots,a_n)$ such that (i) $\sigma_{n+1}$ is a single-valued function of $\sigma_n$ on the realized orbit (i.e. $\sigma_i=\sigma_j\Rightarrow\sigma_{i+1}=\sigma_{j+1}$), and (ii) the realized set $\{\sigma_n:n\ge1\}$ is FINITE, provably so WITHOUT invoking finiteness of governing primes.*

If (*) holds, pigeonhole gives $i<j$ with $\sigma_i=\sigma_j$; single-valuedness makes the future from $i$ and $j$ identical, so $(\sigma_n)$ is eventually periodic; then $d_n$ (a function of $\sigma_n$, since $d_n=\min\{k\le M_1:\sigma_n(k)=1\}$ in the admissibility-window reading) is eventually periodic; `greedy-equals-cyclic-successor` + `cyclic-successor-bijection` upgrade "eventual" to "from $n=1$" and give $a_{n+T}=a_n+L$. **No MT, no B_∞.** This is the genuine prize of the route.

### Distinct openings surfaced

1. **Markov admissibility-window state (the cleanest, already killed in round 3 — recorded to fence off).** $\sigma_n:\{1,\dots,M_1\}\to\{0,1\}$, $\sigma_n(k)=1$ iff $a_n+k$ is admissible at step $n$. State space $\le 2^{M_1}$ (finite). $d_n=\min\{k:\sigma_n(k)=1\}$. The transition $\sigma_n\to\sigma_{n+1}$ = shift window by $d_n$ + impose the new constraint from $a_{n+1}=a_n+d_n$. **The leak (round-3 finite-statistic explorer):** the new constraint's $P_1$-part is determined by $(a_n\bmod M_1)+d_n$, but the NON-$P_1$ primes of $a_{n+1}$ are not captured by $\sigma_n$ or by $a_n\bmod M_1$. Plugging the leak = bounding which non-$P_1$ primes ever act as the unique connector = Gap A. **Do not re-open this exact state.**

2. **$d$-window state $\sigma_n=(d_{n-k+1},\dots,d_n)$ — the route's empirically-CORRECT statistic (the new contribution of this scout).** Since $d_n\in\{1,\dots,M_1\}$ (alphabet size $M_1$), for FIXED $k$ the state space is $\le M_1^k$ (finite). I verified computationally (efficient sim from `/tmp/round-3/sim.py`):

   | $a_1$ | $M_1$ | $T$ | pre | $\max d$ | minimal $k$ (cycle) | $|$realized $k$-windows$|$ over whole orbit |
   |---|---|---|---|---|---|---|
   | 15 | 15 | 8 | 0 | 6 | 2 | 8 ($=T$) |
   | 77 | 77 | 18 | 0 | 14 | 2 | 18 ($=T$) |
   | 91 | 91 | 20 | 0 | 14 | 2 | 20 ($=T$) |
   | 35 | 35 | 34 | 0 | 10 | 6 | 34 ($=T$) |
   | 143 | 143 | 64 | 0 | 22 | 6 | 64 ($=T$) |
   | 741/145/116 (LOCK) | — | 1 | 0 | — | 1 | 1 ($=T$) |
   | 1309 | 1309 | 912 | 0 | 14 | **22** | 912 ($=T$) |
   | 847 | 77 | 1744 | 0 | 14 | **$>24$** | unresolved at $k\le24$ |
   | 175 | 35 | 274 | 0 | 21 | **$>24$** | unresolved at $k\le24$ |
   | 2085 | 2085 | 1372 | 0 | 6 | **$>24$** | unresolved at $k\le24$ |
   | 385 | 385 | 5088 | 0 | 14 | **$>24$** | unresolved at $k\le24$ |

   **Two empirical facts (CONJECTURE, not proved):**
   (C1) For every resolved case, the minimal $k$ making $d_n$ a single-valued function of the $k$-window on the cycle exists, and the realized $k$-window set over the WHOLE orbit equals $T$ exactly — i.e. the transition is a single cycle on the realized set, with no pre-period (matches `greedy-equals-cyclic-successor`, periodic from $n=1$).
   (C2) The minimal $k$ is **unbounded a priori in $M_1$**: $k=22$ for $a_1=1309$ ($M_1=1309$) but $k>24$ for $a_1=847$ ($M_1=77$, much smaller). No clean relation $k\le f(M_1)$ is visible; small $M_1$ does NOT mean small $k$.

   **Why (C1) doesn't close the route.** The proof of (*) needs (a) the realized set to be finite — trivially true for fixed $k$ (size $\le M_1^k$) — AND (b) single-valuedness. Pigeonhole on a finite alphabet gives *some* $i<j$ with the same $k$-window, but if single-valuedness FAILS for that $k$ (which it does for $k< $ the minimal), the equal states do NOT force equal futures. To get single-valuedness we must take $k\ge k_{\min}$, and $k_{\min}$ is exactly the quantity for which no a-priori bound exists. So the route closes Gap A iff one can bound $k_{\min}$ a priori, and that bound IS the Gap-A content (the minimal $k$ for single-valuedness is essentially the length over which the free-rider primes "wash out" — the same content as "the active non-$P_1$ primes form a finite set," i.e. Gap A).

3. **Richer non-residue dynamic state — the syndetic-guardrail-respecting alternative the lens asks about.** I tested $\sigma_n=(d_n,\;\text{set of primes }p\le M_1\text{ dividing some }a_i\text{ in window }[n-w+1,n])$ for $w\in\{4,8,16,32\}$. Result: **NOT single-valued, and the realized set grows with the orbit length** (for $a_1=385$, $w=8$: $|$realized$|\approx 10812\gg T=5088$, with 144 conflicts; for $a_1=847$, $w=8$: 3453 realized, 999 conflicts). This richer state is WORSE than the bare $d$-window — it overfits by capturing absolute-value drift via the active-prime multiset, and the transition leaks harder. **Do not pursue the active-prime state.**

4. **Poincaré recurrence without single-valuedness — the lens's literal "finite WITHOUT finitely determined."** This version does NOT work: a finite realized set with a LEAKY transition does not force periodicity. Concrete reason matching the guardrail: a finite-state *transducer* (leaky transition reading an external input) can produce aperiodic output words over a finite alphabet — exactly the mechanism `syndetic-divisible-closed-not-periodic` formalizes (the aperiodic $B=6\mathbb Z\cup\bigcup_{p\equiv1(4)}p\mathbb Z$ is a finite-statistic-ish, syndetic, divisibility-closed object that is aperiodic). So pigeonhole-on-equal-states REQUIRES single-valuedness of the transition on the realized set; bare finiteness of the realized set is insufficient. The lens's literal hope is therefore too weak; one MUST also prove single-valuedness, which lands back at opening 2's $k_{\min}$ bound.

### The hard step and the obstruction

The hard step is: **find an a-priori bound on the window length $k$ (or, equivalently, on the size of the "active non-$P_1$ prime set" that a finite dynamic state must remember) in terms of $M_1$ alone, proved from the greedy rule + $d_n\le M_1$ without passing through Gap A.** The obstruction is that this bound is empirically FALSE for small, natural statistics: $k_{\min}>24$ for $a_1=847$ ($M_1=77$) and $a_1=385$ ($M_1=385$), so no small universal $k$ exists; and the only statistic that does become single-valued (the bare $d$-window at $k=k_{\min}$) has $k_{\min}$ depending on the very free-rider-prime structure whose finiteness is Gap A. The cofactor-circularity wall (7 dead mechanisms) reappears here as: "the window must be long enough to average out the free-rider primes, and bounding how long IS bounding the free-rider primes."

### GUARDRAIL (mandatory, cited)

`syndetic-divisible-closed-not-periodic` (certified negative): the set $B=6\mathbb Z\cup\bigcup_{p\equiv1(4)}p\mathbb Z$ is divisibility-closed, syndetic (gaps $\le6$), and aperiodic. A finite alphabet + deterministic greedy-LOCAL rule is NOT enough to force periodicity; the leaky-transition version of the ergodic route is exactly the kind of "finite-statistic + bounded gaps" object this counterexample refutes. **Any viable ergodic proof MUST exhibit a greedy-specific dynamic property that the counterexample lacks, beyond "the realized $d$-alphabet is finite and the gaps are bounded."** The greedy-specific property on offer here is *single-valuedness of the transition on a finite realized state set*; but proving that single-valuedness holds for a bounded $k$ is the open step, and the counterexample warns that "the realized state set is finite" alone will not do.

### Knowledge-base entries to use

- `linchpin-and-gap-bound` (certified) — $d_n\le M_1$: the ONLY input making the $d$-alphabet finite ($\{1,\dots,M_1\}$); underwrites the $M_1^k$ state-space bound.
- `greedy-equals-cyclic-successor` (certified) — the orbit is the increasing enumeration of $\mathcal B_\infty$ from $n=1$; underwrites "periodic from $n=1$" once (*) is proved (no transient to handle).
- `cyclic-successor-bijection` (certified, conditional on Gap A) — the endgame this route would feed into; but note (*) would make the endgame unconditional.
- `syndetic-divisible-closed-not-periodic` (certified −) — the guardrail (cited above).
- `binfinity-divisibility-progression-structure` (certified) — confirms the static limit of the route is exactly Gap A ($\mathcal B_\infty=\bigcup_{T\in\mathrm{MT}}\mathrm{rad}(T)\mathbb Z$, periodicity = finiteness of the prime union = Gap A); the ergodic route must NOT collapse to this static identity.

### Analogous past problems (cruxes)

- **`aimo-0577` (IMO-SL 2022 N3)** — *strongest structural analogue.* Crux: "Invert a piecewise update map on a finite invariant set to show it is a permutation, then read off the backward iterates." Concretely: the confinement bound $0<x<ad$ gives a finite invariant set $S=\{x:0<x<ad,\gcd(x,d)=1\}$; the update $f$ has an explicit inverse on $S$; hence $f$ is a permutation of $S$; hence the orbit of $x_1=1$ is periodic. **This is exactly the ergodic route's template:** (i) confinement bound → finite invariant set; (ii) invertibility → permutation; (iii) periodicity. **Why it ports only conditionally:** in our problem the confinement is on $d_n$ ($\le M_1$, a finite alphabet) NOT on $a_n$ (which grows unboundedly — there is no finite box the orbit lives in, unlike aimo-0577's $0<x<ad$); and the map (cyclic-successor $\varphi$) is invertible on $A=\mathcal B_\infty\bmod L$ ONLY conditional on Gap A (`cyclic-successor-bijection`). So aimo-0577's two ingredients are exactly our two walls. Its contribution is the SHAPE — "confinement bound + explicit inverse ⇒ permutation ⇒ periodicity" — and the route should look for an analogue of the confinement box that lives on the *increment* level, not the *value* level. **Analogue ports in shape, not in mechanism; do not cite as a theorem.**
- **`aimo-0678` (NT, modular-arithmetic-and-CRT)** — *already a certified dead-end for this problem.* Crux: "Once one coordinate of a coupled integer recurrence is bounded, reduce the other coordinate mod lcm of the bounded coordinate's values, turning the state pair into a finite deterministic map." This is the same shape (bounded coordinate → finite state → periodicity). Round-2 showed the MT-frontier monovariant $w_n$ is provably non-monotone in the real greedy ($a_1=116$), killing this crux's adaptation. Do not re-attempt.
- **`aimo-0796` (IMO-SL 2007 C4, combinatorics/pigeonhole)** — *closest pigeonhole-on-realized-state analogue.* Crux: "Bound the reachable state space to force a repeated configuration contradicting a strict monovariant" — each coordinate stays in a bounded integer range → at most $n^n$ sequences → pigeonhole → two equal states → contradict strict monovariant. The shape (finite reachable set + pigeonhole) is the ergodic route's skeleton; but aimo-0796 derives the contradiction from a STRICT monovariant, and `aimo-0134-obstruction` (certified −) fences off monovariants for our problem (constant gap bound, no shrinking range). The pigeonhole-without-monovariant half transfers; the monovariant half does not.
- **`aimo-0916` (IMO-SL 2020 C7, processes-and-algorithms)** — *auxiliary.* Crux: "Stabilize a descending chain of images of a self-map on a finite set, then take the power that restricts to the identity on the stable core." Useful IF one already has a finite deterministic self-map (the route's goal); does not help get there.
- No crux in the corpus treats "greedy gcd-driven sequence → periodic" directly (confirmed round 3); the matches above are on the *finite-state-pigeonhole / permutation-on-finite-set* moves, not on the hypergraph content.

### Prior progress

Whole theorem reduced to Gap A; endgame, pure-from-start, LOCK all certified. This route does NOT add a certified lemma. Its **new conjectural outputs** (needing proof): (C1) $d_n$ is a function of a finite $d$-window with $k=k_{\min}(a_1)$ on the whole orbit from $n=1$ (empirically universal across 13 resolved cases); (C2) the realized $k_{\min}$-window set has size exactly $T$ (the period). Neither is proved; both are restatements of periodicity (= Gap A) in increment language.

### Dead ends (do not retry, route-specific)

- **Markov admissibility-window $\sigma_n$** (opening 1): transition leaks the non-$P_1$ primes of $a_{n+1}$; plugging the leak = Gap A (round 3). Certified dead by the round-3 finite-statistic explorer.
- **Active-prime richer state** $(d_n,\{\text{small primes in recent window}\})$ (opening 3): NOT single-valued; realized set grows with orbit length. Refuted by direct computation this round (144 conflicts for $a_1=385,w=8$; 999 for $a_1=847,w=8$).
- **"Finite alphabet + deterministic walk ⇒ periodic" WITHOUT single-valuedness** (opening 4, the lens's literal literal): REFUTED by `syndetic-divisible-closed-not-periodic` (a finite-statistic-ish syndetic divisibility-closed set is aperiodic). The transition MUST be single-valued on the realized set; bare finiteness does not suffice.
- **Residue-mod-$L_0$ statistic for $L_0<L$**: minimal functional $L_0=L$ (round 3). Do not key on $a_n\bmod L_0$.

### Small-case / intuition notes (labeled CONJECTURE / VERIFIED)

- VERIFIED (13 cases this round, efficient sim): the minimal $d$-window length $k_{\min}$ making $d_n$ single-valued on the cycle exists for every resolved $a_1$; the realized $k_{\min}$-window set over the whole orbit equals $T$ exactly; periodic from $n=1$ (pre=0). Matches `greedy-equals-cyclic-successor`.
- VERIFIED: $k_{\min}$ is NOT bounded by any small function of $M_1$. $k_{\min}=22$ for $a_1=1309$ ($M_1=1309$) but $k_{\min}>24$ for $a_1=847$ ($M_1=77$) and $a_1=385$ ($M_1=385$). Small $M_1$ does NOT imply small $k_{\min}$. CONJECTURE: $k_{\min}$ is unbounded in $M_1$; if true, opening 2 has no a-priori bound and the route is dead.
- CONJECTURE (the route's only live sliver): there MIGHT exist a non-$d$-window, non-active-prime dynamic state (e.g. a "witness-prime sequence" quantized modulo the $P_1$-skeleton, or a gap-pattern of recent large-prime witnesses) with both bounded realized set AND single-valued transition, that escapes the $k_{\min}$-unbounded obstruction. Not found in this scout; the obvious candidates (openings 1, 3) are refuted.

### Verdict

**Promising-but-conditional, leaning DEAD.** The ergodic route is the cleanest rephrasing of Gap A into increment language, and it has a genuine empirical anchor (C1: the realized $k_{\min}$-window set equals $T$ exactly, transition is a single cycle from $n=1$ — verified 13 cases). But the lens's literal escape ("finite realized set WITHOUT finitely determined transition") is REFUTED by `syndetic-divisible-closed-not-periodic`: pigeonhole-on-equal-states REQUIRES single-valuedness of the transition, which is the very step that costs Gap A. The route closes Gap A iff one can bound $k_{\min}$ (the window length at which the $d$-transition becomes single-valued) a priori in $M_1$; the data REFUTES any small bound ($k_{\min}>24$ for $M_1=77$), and the only live sliver is the existence of an as-yet-unfound non-$d$-window, non-active-prime dynamic state with both properties. **Do not open a standalone ergodic slug at the bare $d$-window state — it will hit the $k_{\min}$ wall, which is Gap A.** Open it ONLY if the outliner can name a concrete non-residue dynamic state whose single-valuedness can be proved from the greedy rule + $d_n\le M_1$ directly (not from finiteness of governing primes).

### Sharpest sub-problem for a builder

**Find — or prove the non-existence of — a dynamic state $\sigma_n$ on the greedy orbit such that (a) $\sigma_{n+1}$ is a single-valued function of $\sigma_n$ on the realized orbit, (b) $|\{\sigma_n:n\ge1\}|$ is bounded a priori by a function of $M_1=\operatorname{rad}(a_1)$ alone, and (c) the bound does NOT pass through finiteness of the governing primes.** Concretely: either exhibit such a $\sigma_n$ (the $d$-window fails (b) since $k_{\min}>24$ for $M_1=77$; the active-prime state fails (a)); or prove that ANY such $\sigma_n$ encodes the active non-$P_1$ primes and so (b) is equivalent to Gap A — which would certify the route dead and close the lens. The first test a builder should run: search, over $a_1\in\{847,175,385,2085\}$ (the $k_{\min}>24$ cases), for a dynamic state built from the *witness-prime sequence* (which prime of $S(a_{n+1})$ realizes the admissibility — a $P_1$-indexed object, hence a priori finite) whose realized set is bounded by $2^{|P_1|}$ and whose transition is single-valued. If that fails, the route is dead.
