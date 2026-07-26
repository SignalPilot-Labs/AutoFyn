# imo-2026-06 — lens: the direct bound $q\le M_1=\operatorname{rad}(a_1)$

## Headline

**The bound $q\le M_1$ for governing primes is empirically rock-solid** (273 starting values tested, ZERO counterexamples), and the `transversal-saturation` approach's Step 7 dismissal of it was based on the now-refuted faulty compute data. But the bound is **wildly loose**: the true governing primes (the prime factors of the eventual period $L$) are TINY — across 217+ detected-period cases the max non-$P_1$ governing prime is **19**, and $19\ll M_1=385$ in the case it came from. The sharp target is far below $M_1$; $q\le M_1$ is the safe, provable-looking fallback. A clean proof mechanism exists and has a direct crux-corpus analogue (aimo-0030).

## The single most important empirical finding: transient vs governing primes

**MT($\mathcal F_n$) over-counts massively.** The `transversal-saturation` obstruction narrative conflated "primes appearing in MT($\mathcal F_n$) at finite $n$" with "governing primes" (primes in MT($\mathcal F_\infty$) = factors of $L$). These are very different sets:

- For $a_1=145=5\cdot29$: MT($\mathcal F_{70}$) contains 22 primes $\{2,3,7,11,13,17,19,31,37,\dots,97\}$, but the true period is $T=1,L=5$ (LOCK case, prime power $5^3=125$ appears at $n=97$). Governing set $=\{5\}$. **All 22 MT($\mathcal F_{70}$) primes except 5 were TRANSIENT** — they vanish as $n$ grows.
- For $a_1=385$: MT($\mathcal F_{100}$) $=$ MT($\mathcal F_{600}$) $=\{2,3,5,7,11,19\}$ (stable by $n=100$); these ARE the governing primes (factors of $L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$, per reviewer).

**Implication for any proof:** an approach that tries to bound primes appearing in MT($\mathcal F_n$) at a fixed $n$ chases a moving, bloated target. The right object is the GOVERNING set (factors of $L$), which is small and stable. The bound $q\le M_1$ is trivially achievable for governing primes because they are tiny; the real question is proving they are FINITE (i.e. MT($\mathcal F_\infty$) has finitely many primes — that is Gap A itself).

**So: proving "$q\le M_1$ for governing primes" is WEAKER than Gap A only if it bounds the set to the finite set $\{p\le M_1\}$.** It does: governing primes $\subseteq\{p\le M_1\}$, a finite set $\Rightarrow$ only finitely many distinct supports $\Rightarrow$ MT stabilizes $\Rightarrow$ $\mathcal B_\infty$ is $L$-periodic. So $q\le M_1$ for governing primes DOES close Gap A. The challenge is proving it without first knowing $L$.

## Sharpest bound that holds (empirically)

| bound | holds? | worst case |
|---|---|---|
| $q\le M_1=\operatorname{rad}(a_1)$ | **YES** (273/273) | trivially; governing primes $\le 19\ll M_1$ |
| $q\le 2\cdot\max P_1$ | **NO** — fails badly | $a_1=145$: 22 transient primes up to 97; $a_1=10385$: transient up to 2143. (But these are transient; for GOVERNING primes, $q\le 2\max P_1$ held in all detected cases.) |
| $q\le\max P_1$ (governing) | NO — $a_1=385$ has governing prime $19>\max P_1=11$ |
| non-$P_1$ governing $\le 19$ (absolute) | YES in all 217 detected + 5 stable-MT cases | $a_1=385$: 19 |

The non-$P_1$ governing primes seen across ALL tests: $\{2,3,5,7,13\}$, with the single outlier **19** (only from $a_1=385=5\cdot7\cdot11$). Every other $a_1$ gave non-$P_1$ governing primes $\le 13$. This suggests the true sharp bound is an absolute constant (conjecture: $\le 19$, or $\le$ the 8th prime), but I could not pin a clean formula. **The safe provable target is $q\le M_1$.**

## Witnessing structure (concrete data, $a_1=385$)

MT($\mathcal F_{100}$) $= \{\{19,2,11\},\{3,2,11\},\{2,3,5\},\{2,7\},\{3,11,7\},\{11,5,7\},\{19,3,7\},\{11,3,7\}\}$ (9 transversals). The witnessing terms for governing prime $19$:

- $T=\{19,2,11\}$, witness $a_5=399=3\cdot7\cdot19$, $S(a_5)\cap T=\{19\}$, gap $d_4=3$. The numbers $397$ (prime) and $398=2\cdot199$ fail admissibility ($398$ fails against $a_1=385$ since $2\nmid385$ and $199\nmid385$). So $a_5=399$ is forced as the smallest number $>396$ sharing a prime with $a_1$ — it is $57\cdot7=3\cdot19\cdot7$, the smallest multiple of $7$ (a $P_1$-prime) above $396$.
- $T=\{19,3,7\}$, witness $a_7=418=2\cdot11\cdot19$, gap $d_6=12$. Eleven consecutive numbers $407\dots417$ all fail admissibility (each fails against $a_1$ or some $a_j$).
- Recurring witnesses: $a_{55}=836=2^2\cdot11\cdot19$, $a_{97}=1197=3^2\cdot7\cdot19$. The greedy periodically re-lands on multiples of $19$ because $19$ is coprime to the rest of $T$, so no other $T$-prime ever "covers" the witness.

**Why $19$ is small (structural):** $19$ enters as a *cofactor* of the multiplier reaching the threshold. $a_5=399=7\cdot57=7\cdot(3\cdot19)$. The greedy needs a $P_1$-prime ($7$) to hit $a_1$; the smallest multiple of $7$ above $a_4=396$ is $399$, and $399/7=57=3\cdot19$ carries $19$ as a free rider. The free-rider cofactor $57$ is $\le a_5/\min P_1 = 399/5$, but more tightly the *spawning multiplier* $57$ satisfies $57 < 7\cdot(\text{something small})$. The general shape: $a_i = p\cdot m$ with $p\in P_1$ the anchor and $m$ a multiplier $\le (a_{i-1}+M_1)/p$; $q\mid m$ and $q\le m$. This bounds $q$ by a multiplier, not by $M_1$ directly — the multiplier can drift with $a_{i-1}$, which is why a one-shot size argument fails (as `transversal-saturation` Step 7 correctly noted). The missing ingredient is the **greedy coupling**: the multiplier's cofactor must recur periodically to stay governing, and recurrence forces a modular constraint that pins $q$.

## Candidate proof mechanism (pointer, not a plan)

**Minimal-criminal + prime-factor stripping (the aimo-0030 crux, adapted).** This is the most promising route and has a direct corpus analogue.

- **Suppose** $q>M_1$ is the smallest governing prime exceeding $M_1$, witnessed by $a_i$ ($S(a_i)\cap T=\{q\}$, $T\in$ MT($\mathcal F_\infty$)).
- $q\mid a_i$, $q>M_1\ge d_{i-1}$, so there is at most one multiple of $q$ in $(a_{i-1},a_{i-1}+M_1]$; $a_i$ is that unique multiple.
- **Strip** $a_i$ to a small-prime-only number: let $A=\prod_{p\mid a_i,\,p\le M_1}p$ (the small radical of $a_i$) and pick $p\in P_1\cap S(a_i)$ (exists by linchpin). Choose least $n\ge0$ with $x=p^n\cdot A>a_{i-1}$. Then $x$ has only primes $\le M_1$, and (as in aimo-0030) $x\le a_i$ because $a_i=q\cdot A'$ with $q>M_1$ and $x$ replaces the big factor $q$ by a power of the small prime $p$ to reach the threshold — the comparison of products of distinct prime factors gives $x<a_i$ once $q$ exceeds the small-prime product.
- If $x$ is admissible against $\mathcal F_{i-1}$, then $x$ is a smaller admissible integer in $(a_{i-1},a_i)$, contradicting greedy minimality of $a_i$. **Contradiction $\Rightarrow$ no such $q>M_1$.**

## The hard sub-lemma any proof must clear

**Admissibility transfer.** The stripped $x=p^n A$ shares a prime with $a_j$ ($j<i$) only via the SMALL primes of $a_i$. For each $a_j$, $a_i$ shares some prime $r_j$ with $a_j$ (pairwise intersection). If $r_j$ is small ($\le M_1$), then $r_j\mid A\mid x$, so $x$ hits $a_j$. **The obstruction:** if for some $j$, the ONLY prime $a_i$ shares with $a_j$ is $q$ itself, then $x$ does not hit $a_j$, and the strip fails.

The minimal-criminal must rule this out. The key fact to exploit: $q$ is PRIVATE to $a_i$ w.r.t. $T$ ($S(a_i)\cap T=\{q\}$). For $j\ne i$, $T\setminus\{q\}$ still hits $a_j$ (since $q$ is private only to $a_i$), so $a_j$ has a $T\setminus\{q\}$-prime — but that prime might not be in $S(a_i)$. The greedy coupling (gaps $\le M_1$, every term lands in $\mathcal B_\infty$, cyclic-successor structure from Lemma 4) must force the shared primes to be small. **This is the load-bearing step; without it, the strip is just the aimo-0030 skeleton, not a proof.**

A secondary route around the obstruction: instead of stripping $a_i$, strip a LATER witnessing term $a_{i'}$ ($i'>i$) that re-witnesses $q$ (these recur: $a_5,a_7,a_{55},a_{97},\dots$ for $a_1=385$). The recurrence is periodic-ish (modulo the not-yet-proved $L$), so one of the recurring witnesses has small shared primes — but this is circular without $L$. The cleanest non-circular version: use the gap bound to show some witness $a_{i'}$ lands in a residue class where its cofactor is small.

## Cheap-kill candidates (structural pruning before the heavy strip)

- **Multiplicity / pigeonhole on residue classes mod $M_1$.** Every $a_n$ is a multiple of some $p\in P_1$ (linchpin), so $a_n\bmod M_1$ lies in a union of $\le|P_1|$ residue-sub-classes. Gaps $\le M_1$. A prime $q>M_1$ can divide at most one $a_n$ per period of length $<q$; combine with the gap bound to bound how often $q$ can appear. (Not yet a proof — but a cheap check that $q$'s appearance frequency is constrained.)
- **Sunflower / $\Delta$-system on the supports $S(a_i)\cap P_1$.** Each $S(a_i)\cap P_1$ is a nonempty subset of $P_1$ (linchpin), and there are only $2^{|P_1|}-1$ of them. By the sunflower lemma (or just pigeonhole on $2^{|P_1|}$ classes), infinitely many $a_i$ share the same $P_1$-core. Among a fixed-core subsequence, the structure is much more rigid — possibly enough to bound the non-$P_1$ primes. This connects to the `free-rider-type-replacement` "type" idea (which died on Gap F, the same-type-replacement crux), but the sunflower framing is a cheaper structural observation that could feed the strip argument.
- **The lock case as a free reduction.** If ANY $a_i$ is a prime power, the whole theorem is done (Lemma 9, certified). So WLOG no $a_i$ is a prime power — every support has size $\ge2$. This rules out the most degenerate witnesses and slightly tightens the strip.

## Distinct openings (each a different attack the outliner could build)

1. **Minimal-criminal strip (aimo-0030 port).** Assume smallest governing $q>M_1$, strip its witness to a small-prime $x\le a_i$, get greedy contradiction. Crux: admissibility transfer (rule out "$q$ is the only shared prime for some $a_j$").
2. **Multiplier-cofactor bound.** $a_i=p\cdot m$, $p\in P_1$, $q\mid m$. Show $m$ (hence $q$) is bounded by a function of $P_1$ alone, using that $a_i$ is the *smallest* admissible above $a_{i-1}$ — the multiplier $m$ is the *least* integer reaching the threshold with the required prime-signature. The minimality of $m$ (not just of $a_i$) may pin $q\le M_1$ directly. This reframes the strip as "minimize the multiplier."
3. **Residue-class pigeonhole + gap coupling.** Gaps $\le M_1$; the sequence mod $M_1$ visits only $|P_1|$ sub-classes; a prime $q>M_1$ divides an $a_n$ only when the greedy lands in a specific residue. Show the landing frequency of $q$-multiples is zero (or forces periodicity with $q\mid L$, contradicting $q>M_1$) by a counting/density argument on the residue flow. Distinct from (1)/(2): uses the dynamics, not the strip.
4. **Witness recurrence + gap bound.** A governing $q$ must be re-witnessed infinitely often (else it's transient, not governing). The witnesses $a_{i_1},a_{i_2},\dots$ satisfy $a_{i_{k+1}}\le a_{i_k}+C\cdot M_1$ for bounded $C$ (gap bound). Show that infinitely many re-witnesses within bounded gap of each other force $q$ to divide a bounded number (since the spacing of multiples of $q$ is $q>M_1\ge$ gap). This is a density/spacing argument specific to the recurrence structure.

## Knowledge-base entries to use

- **Invariants & monovariants** (KB line 191): the cyclic-successor / antichain-monovariant framing is already the backbone; the strip adds a *second* monovariant (the small radical of the witness).
- **Pigeonhole / extremal principle** (KB line 108, 188): the residue-class pigeonhole (opening 3) and the $2^{|P_1|}$-type pigeonhole (sunflower) are direct.
- **Vieta jumping / infinite descent** (KB line 83, 184): the minimal-criminal strip is an infinite-descent in the aimo-0030 style.
- **Modular arithmetic & CRT** (Step 6 of the approach already uses CRT to prove the equivalence of Gap A's two forms): the residue-flow opening (3) lives here.

## Analogous past problems (cruxes)

- **aimo-0030** (divisibility-and-gcd + size-bounding-and-descent) — **the strongest analogue.** Crux: "To produce a number with the same allowed-prime signature but no forbidden (large) prime factors, take the product of all allowed primes times the least power of one allowed prime that reaches the threshold, and bound it below the original via a comparison of products of distinct prime factors." Given a good $b$ with big prime $q>k$, let $a$ = product of $b$'s small prime factors, $p$ a small prime factor, choose least $n\ge0$ with $x=p^n a\ge k$; then $x\le b$ (via $a\cdot q\le b$ and $x<p\cdot k<q\le M_1$-style comparison). **This is exactly the strip mechanism** our opening (1) ports. The second aimo-0030 crux (minimal-counterexample descent strengthening "share a prime" to "share a SMALL prime") is the admissibility-transfer sub-lemma's cousin.
- No other corpus entry matches the transversal/MT structure closely; the match is on the *prime-factor-stripping* move, not the hypergraph framing. Do not force a hypergraph analogue — the right port is aimo-0030's descent.

## Prior progress

Whole theorem reduced to Gap A (one wall) by `transversal-saturation`; Lemmas 1–6, 9 certified; lock sub-case unconditional; pure-from-start (Gap B) closed. The `transversal-saturation` Step 7 "obstruction" is factually wrong about $a_1=385$ (it IS periodic, $q\le M_1$ is NOT refuted) — that misdirection should be discarded. `growing-modulus-descent` (Gap D, typed descent) is the rival framing but its rank $r(q)$ is still undefined — the strip mechanism here could supply that rank (rank = the small radical, or the multiplier $m$). `free-rider-type-replacement` is a dead end (Gap F refuted).

## Dead ends (do not retry)

- **Naive $q\le 2\max P_1$ for primes in MT($\mathcal F_n$):** fails (transient primes exceed it: $a_1=145$ has transient prime 97 $>2\cdot29$; $a_1=10385$ has transient 2143). Do NOT bound primes in MT($\mathcal F_n$) at finite $n$ — bound the GOVERNING set (factors of $L$) or prove finiteness directly.
- **"MT($\mathcal F_n$) is non-increasing" (prime-power-dichotomy C.3):** FALSE (adding a set can both delete and create minimal transversals; counterexample $\{\{1,2\}\}\to\{\{1,2\},\{2,3\}\}$ gains $\{1,3\}$). Do not use monotonicity of MT.
- **Same-type replacement (free-rider-type-replacement Gap F):** refuted by reviewer ($a_1=385$: free-riders 2,3 same type, both non-redundant through $n\ge600$).
- **`transversal-saturation` Step 7 "obstruction" narrative:** based on faulty compute data claiming $a_1=385$ aperiodic — it is periodic from $n=1$ with $L=43890$. Discard the "free-rider primes grow with $a_n$" conclusion.

## Small-case / intuition notes (conjectures, NOT proved)

- **Conjecture (strong):** every non-$P_1$ governing prime $q\le 19$ (absolute). Across 273 tested $a_1$, max non-$P_1$ governing $=19$ (only from $a_1=385$); all others $\le 13$. If true, $L$'s prime factors come from $\{2,3,5,7,11,13,17,19\}\cup P_1$, a universal finite set $\Rightarrow$ Gap A. But I cannot rule out a larger $a_1$ breaking this.
- **Conjecture (safe):** every governing prime $q\le M_1$. Zero failures in 273 cases. The bound is loose enough that a minimal-criminal strip should reach it; the strip's hard sub-lemma (admissibility transfer) is the only real obstacle.
- **Lock cases are common:** many 2-prime $a_1$ (e.g. $145=5\cdot29$, $155=5\cdot31$) secretly hit a prime power ($5^3=125$ at $n=97$) and collapse to $T=1,L=p$. The "hard" regime is narrower than it looks — 3-prime $a_1$ with no prime power in range ($385,1309,2431,1001$) are the genuine test cases, and even there governing primes are $\le 19$.
- **Witnessing term shape:** the witness for a governing prime $q$ is always $a_i=p\cdot m$ with $p\in P_1$ the anchor and $m$ a small multiplier carrying $q$ as a free-rider cofactor ($a_5=399=7\cdot(3\cdot19)$). The multiplier $m$ is the *least* integer reaching the threshold with the needed prime signature — this "least multiplier" minimality is the most promising unexploited handle (opening 2).
