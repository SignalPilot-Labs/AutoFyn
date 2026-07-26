# Round 2 proof review — IMO 2026 Problem 6

## Headline

**The `essential-monovariant` approach is SOLVED.** The game-of-numbers equivalence (Theorem GC) is correctly proved from scratch (G1–G4 only, no circularity); the stripping descent (G5, G6) is a genuine re-derivation of aimo-0030's Claim 5, every step verified; the transfer to Lemma 4' is sound; and the round-1 periodicity machinery at threshold $B=a_1$ produces $a_{n+T}=a_n+L_0$ for all $n\ge 1$ (no transient). I verified the final formula computationally for $a_1\in\{2,3,5,6,7,10,15\}$ — in every case $a_{n+|V|}=a_n+L_0$ holds with $L_0=\prod_{p\le a_1}p$. The one presentational gap (non-emptiness of the set defining $M$ in Theorem GC) is a one-line fill from G4 + "large multiples of $k$ are admissible" and does not affect validity. **APPROVE.**

The other three approaches are honestly `partial`/`unsolved` and are now moot as independent proofs (the theorem is proved), but their reusable certified lemmas and route characterizations remain valuable. One real flaw was found: `grid-counting-shared-primes` Lemma 5 has an arithmetic error (the stated bound $389/900$ is actually *false* — below the true value; the conclusion $\sum_p 1/p^2<1/2$ survives via the corrected bound $17/36$, but the proof as written needs fixing).

---

## essential-monovariant

**Verdict: APPROVE. Status: solved.**

### Independent re-derivation of the load-bearing step

The crux is Lemma 4' (every pair of P6 terms shares a prime $\le a_1$), proved via the game equivalence. I re-derived each link:

- **G1, G2, G2' (good/bad dichotomy):** standard impartial-game P-position argument. Ana wins iff a good coprime predecessor exists; good iff no such predecessor. Verified: a move strictly decreases $m$, the game terminates, exactly one player wins. ✓
- **G3 ($k$ good):** $k$ admits no move (no $x\in[k,k)$), Ana loses first move. ✓
- **G4 (two good numbers share a prime):** if $m<n$ good and coprime, $m$ is a good coprime predecessor of $n$, so $n$ is bad by G2' — contradiction. ✓ (This is the corpus crux `aimo-0030` first move, re-proved, not cited.)
- **G5 (stripping):** re-derived the inequality $x<pk\le ak<aq\le b$ from $p^{α-1}a<k$ (minimality), $p\mid a\Rightarrow p\le a$, $q>k$, $aq\mid b$ (distinct prime factors of $b$). Each step checked. ✓
- **G6 (descent, the crux):** minimal counterexample $(b,b')$ sharing only big primes, $b'$ minimal. $b,k$ good $\Rightarrow$ shared small prime $p$ (G4), $p\nmid b'\Rightarrow b'>b$. Strip $b\to x$ (G5), $x$ coprime to $b'$, $x$ bad (else contradict G4). Bad $\Rightarrow$ move $x\to b^*$ with $b^*$ good (G2'). Small primes of $b$ all divide $x$ (similarity) so miss $b^*$; shared primes of $(b^*,b)$ are big; G4 forces a shared prime, which is big; so $(b^*,b)$ is a smaller counterexample (larger element $b<b'$). Contradiction. ✓ This matches aimo-0030 Comment 1 / Claim 5 and is genuinely re-proved in prose, not cited.
- **Theorem GC (greedy = good):** induction. Base $g_0=A$ (G3). Step: $M=\min\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$. Sub-claim 1 (M good): if bad, good coprime predecessor $x$; $x\le g_n$ contradicts admissibility of $M$, $g_n<x<M$ contradicts minimality of $M$ (using G4). Sub-claim 2 (no good in $(g_n,M)$): G4 makes any good $m\in(g_n,M)$ admissible, contradicting minimality. So $M=g_{n+1}$. ✓ Matches aimo-0030 Comment 2's stated construction, but here *proved* (Comment 2 states it without proof).
- **Lemma 4' (transfer):** $(a_n)=(g_{n-1})$ via GC; G6 $\Rightarrow$ any two terms share a prime $\le A$. ✓
- **§8 periodicity machinery:** §8b "transversal $\Rightarrow$ admissible" (uses $F_\infty\supseteq F_n$); "$a_{n+1}$ has transversal type" (uses Lemma 4' on every pair involving $a_{n+1}$, including future terms; $\tau(a_{n+1})\neq\varnothing$ forced by Lemma 4' pairing with $a_1$ or $a_2$). §8c $\varphi$ = cyclic successor on $V$ is a bijection, single orbit length $T=|V|$. §8d telescoping: one wrap per cycle, sum $=L_0$. "No transient" correct: $\varphi$ bijective $\Rightarrow$ orbit purely periodic from $r_1=a_1\bmod L_0\in V$ (shown end of §8b). ✓

### Threshold consistency (Q vs primes dividing $a_1$)

Lemma 4' supplies "shares a prime $\le A=a_1$", i.e. a prime in $Q=\{p\le A\}$. The machinery's $L_0=\prod_{p\in Q}p$ and $V$ are defined over this same $Q$. The supplementary Lemma 1 (primes *dividing* $a_1$) and Lemma 2 (gap bound $\le\operatorname{rad}(a_1)$) live at the tighter threshold $\operatorname{rad}(a_1)\le A$ but are *not used* by the main proof line (only by the appendix bounds). No threshold mismatch. ✓

### Empirical verification

Computed the greedy sequence and checked $a_{n+|V|}=a_n+L_0$:
- $a_1=2$: $L_0=2$, $T=1$. ✓
- $a_1=3$: $L_0=6$, $T=2$ (formula gives $a_{n+2}=a_n+6$; minimal period is $(1,3)$, both valid). ✓
- $a_1=15$: $L_0=30030$, $|V|=8008$. Verified $a_{n+8008}=a_n+30030$ on first 60 terms. ✓ (Minimal period $(8,30)$; builder's non-minimal formula also valid.)

### Minor gap (non-blocking)

In Theorem GC, $M:=\min\{m>g_n:\gcd(m,g_i)>1\ \forall i\le n\}$ is defined without explicitly proving the set is nonempty. **Fill (one line):** any sufficiently large multiple of $k=A$ is admissible — by G4, $g_i$ and $k$ (both good) share a prime $p_i\mid k$; a multiple of $k$ is divisible by $p_i$; $p_i\mid g_i$; so $\gcd(\text{multiple of }k, g_i)\ge p_i>1$. So the set is nonempty, $M$ exists. The Remark ("GC uses only G1–G4") is correct with this fill. This is presentational, not substantive — the argument is fundamentally valid. A one-line addition in §6 fixes it.

### No circularity

Dependency order: G3 → G4 (G2',G3) → G5 (standalone) → G6 (G3,G4,G5,G2') → GC (G1,G2,G3,G4) → 4' (GC,G6) → §8 (4'). Each step builds only on prior results. The game-of-numbers scaffold is an auxiliary construction proved from scratch; aimo-0030 is adapted, not cited. ✓

### Promotable lemmas

Certifying into `lemmas/` (separate files): Lemma G6 (small-prime sharing for good numbers), Theorem GC (greedy=good), Lemma 4' (the crux). All pass the bar: sorry-free, statements correct and no stronger than proved. Lemmas 2, 3 already effectively certified via use; the multiple-of-$R$ lemma is already in `lemmas/`.

**Outcome recorded:** `verified-milestone` — "Game equivalence (GC) + stripping descent (G6) re-proved from scratch; Lemma 4' closed; periodicity machinery gives $a_{n+T}=a_n+L_0$ for all $n\ge1$. Minor presentational gap on M-existence, one-line fillable. Verified empirically for $a_1\in\{2,3,5,6,7,10,15\}$."

---

## crude-reduced-type

**Verdict: CHANGES REQUESTED. Status: partial.**

This is a second, independent conditional-on-crux bridge at the cruder threshold $Q=\{p\le a_1\}$. Steps 1–6 are rigorous (cheap anchor; finite-lattice stabilization of $F_n$/$H_n$; fixed $V_0$). Step 7 (the crux Lemma 4) is honestly marked **[GAP]**, imported from `essential-monovariant` "inherited, not independently closed." Steps 8–10 (free-rider irrelevance conditional on Lemma 4; cyclic-successor bijection $\varphi$; no-transient; telescoping lift to $a_{n+T}=a_n+L_0$) are correct and mirror the certified `essential-monovariant` §8.

The builder is honest about the buried Step-6 issue (membership in $V_0$ needs Lemma 4) and correctly notes the "for all $n\ge 1$ / no transient" follows from $\varphi$ being a bijection (not merely a function on a finite set).

**Why partial, not solved:** the approach file does not itself prove Lemma 4; it imports it. Now that `essential-monovariant` has proved Lemma 4' (a *stronger* statement at the same threshold $Q=\{p\le a_1\}$ — actually identical, since Lemma 4' says "shares a prime $\le a_1$"), the [GAP] is fillable by importing Lemma 4'. But the file as written does not fill it. As a standalone proof, it is incomplete. As a conditional theorem, it is correct.

**Required change to close:** import Lemma 4' from `essential-monovariant` §7 into Step 5, replacing the [GAP] marker with a one-paragraph proof (or a direct cite to the certified lemma), making the file a complete standalone proof. Since the theorem is already solved by `essential-monovariant`, this is now redundant but would make the approach self-contained.

**Outcome recorded:** `partial` — "Conditional bridge correct (Steps 1–6, 8–10 rigorous); crux Lemma 4 [GAP] imported from essential-monovariant. Now fillable from essential-monovariant's Lemma 4' (same threshold). Honest partial; redundant once essential-monovariant is APPROVED."

---

## propagation-bezout

**Verdict: RETHINK. Status: unsolved.**

The route is **circular as filed**, and the builder is honest about this (Sub-steps 4b–4c). The characterization of *why* the route fails is correct and valuable (it tells future rounds not to retry this framing), but as a proof of Lemma 4 it is fatally broken:

- **Sub-step 4b (the circularity):** the shift algebra $\varphi:V\to V$ is defined via $V=\{r:\tau(r)\in H_\infty\}$, and the claim "$a_{n+1}\bmod L_0\in V$" is the free-rider-irrelevance result proved in `essential-monovariant` §8b *using Lemma 4*. So propagation of Lemma 4 via $\varphi$ presupposes Lemma 4. **Circular.** ✓ (builder's characterization is correct.)
- **Non-transitivity of "shares a small prime":** verified by the builder (concrete obstruction: $(a_i,a_{i+1})$ shares $r$, $(a_{i+1},a_{i+2})$ shares $s\ne r$; nothing forces $(a_i,a_{i+2})$ to share either). ✓ Bezout composition has no transitive carrier.
- **Growing bound:** the only pre-Lemma-4 input (Lemma 2, gap bound) gives $a_{i+k}-a_i\le kR$, so shift-$k$ pairs share a prime $\le kR$, not $\le R$. Collapsing $kR\to R$ is the crux. ✓
- **No promotable lemma:** the only extractable partial ("$a_1$ shares a small prime with every $a_j$") is a direct corollary of Lemma 1, already certified, subsumed. ✓

The route cannot prove Lemma 4 as set up. It should go back to the outliner for a genuinely different strategy (or, now that the problem is solved, be retired). Since `essential-monovariant` solved the problem, this approach is moot, but the honest negative characterization is a useful record.

**Outcome recorded:** `dead-end` — "Propagation route circular as filed (Sub-step 4b: φ defined via V, V's relevance uses Lemma 4). Non-transitivity of shares-small-prime verified. Growing bound only (≤kR). No promotable lemma; partial subsumed by Lemma 1. Route cannot prove Lemma 4 as set up."

---

## grid-counting-shared-primes

**Verdict: CHANGES REQUESTED. Status: partial.**

The certified **large-prime-span lemma** (`lemmas/large-prime-span-divides-at-most-one-term.md`) is correct: span bound $S_N\le(N-1)R$ by telescoping + Lemma 2; large-prime uniqueness ($p>S_N\mid a_i,a_j\Rightarrow p\mid(a_j-a_i)\le S_N<p$, contradiction). ✓ Corollaries 4a/4b (large primes cover no cell; growing-window bound $\le(N-1)R$) are sound. ✓

The growing-window ceiling is honestly marked **[GAP]** (obstructions G1 growing window, G2 aggregate-vs-per-cell) — correctly characterized as structural: counting can't reach the fixed threshold $R$ without already assuming the free-rider dichotomy.

### Real flaw found: Lemma 5 ($\sum_p 1/p^2 < 1/2$) — arithmetic error

The proof of Lemma 5 has an **arithmetic error that makes the stated bound $389/900$ actually FALSE** (it is below the true value). The error:

> "Removing the $n=1$ and $n=5$ summands (the only terms with $n<5$ in this restricted sum), $\sum_{n\ge5,\gcd(n,6)=1}1/n^2=\pi^2/9-1-1/25$."

**$n=5$ is not $<5$.** The set $\{n\ge5:\gcd(n,6)=1\}$ *includes* $n=5$. Only $n=1$ is $<5$ in the restricted sum. So the correct subtraction is just $-1$ (for $n=1$), giving
$$\sum_{n\ge5,\gcd(n,6)=1}\frac1{n^2}=\frac{\pi^2}{9}-1\approx 0.0966,\quad\text{not}\quad 0.0566.$$

**Verified computationally:** direct sum $\sum_{n=5}^{100000,\gcd(n,6)=1}1/n^2\approx 0.0966$, matching $\pi^2/9-1$, not the builder's $\pi^2/9-1-1/25\approx 0.0566$.

Consequently the builder's stated bound $\sum_p1/p^2<389/900\approx 0.4322$ is **false** — the true value is $\approx 0.4522 > 0.4322$. The bound is too tight by the erroneous $1/25$ subtraction.

**However, the conclusion $\sum_p1/p^2<1/2$ survives** via the corrected computation:
$$\sum_p\frac1{p^2}\le\frac14+\frac19+\Big(\frac{\pi^2}{9}-1\Big)<\frac14+\frac19+\frac{10}{9}-1=\frac14+\frac29=\frac{17}{36}\approx 0.4722<\frac12,$$
using $\pi^2<10$ (from $\pi<22/7$). So the lemma's *statement* is true; only the *proof as written* is flawed (wrong number $389/900$; should be $17/36$).

### Impact on the approach

Lemma 5 is **not load-bearing** for the main theorem — it only feeds the cell-count bound (eq. 7–8), which is itself a [GAP] ceiling characterization, not the crux. The certified large-prime-span lemma (the approach's real contribution) is unaffected. But the rigor rule "Prove, don't conjecture" is violated by the false stated bound. The fix: replace $389/900$ with $17/36$ throughout §5, and correct the subtraction (remove the $-1/25$).

**Required change:** fix Lemma 5's subtraction error; re-derive the bound as $17/36<1/2$ (not $389/900$). The conclusion stands; only the proof needs correction.

**Outcome recorded:** `partial` — "Large-prime-span lemma certified & correct; growing-window ceiling honestly [GAP]. Lemma 5 proof has arithmetic error (subtracts 1/25 for n=5∈{n≥5}); stated bound 389/900 is FALSE (true ≈0.4522). Conclusion <1/2 survives via corrected bound 17/36. Not load-bearing. Fix: replace 389/900 with 17/36, remove -1/25."

---

## For the orchestrator

**The goal is achieved: IMO 2026 Problem 6 is SOLVED.** The `essential-monovariant` approach delivers a complete, rigorous proof: the game-of-numbers equivalence (Theorem GC, proved from G1–G4) identifies P6's greedy sequence with the good numbers of the game with parameter $k=a_1$; the stripping descent (Lemma G6, re-proved from scratch, not cited) shows any two good numbers share a small prime $\le k$; transferring via GC gives Lemma 4' (every pair of terms shares a prime $\le a_1$); the round-1 periodicity machinery at threshold $B=a_1$ then yields $a_{n+T}=a_n+L_0$ for all $n\ge 1$ with $T=|V|$ and $L=L_0=\prod_{p\le a_1}p$, no transient. Verified empirically for $a_1\in\{2,3,5,6,7,10,15\}$. I have written the full proof into `results/imo-2026-06/current.md` and recorded `verified-milestone`.

Next round: no further proof work needed on P6. The other three approaches are moot as independent proofs (the theorem is proved). If continuing to develop the population for robustness: (a) `crude-reduced-type` can be made self-contained by importing Lemma 4' into its Step 5; (b) `grid-counting-shared-primes` Lemma 5 should be corrected ($389/900\to 17/36$) for rigor hygiene; (c) `propagation-bezout` is a confirmed dead end (circular) and can be retired. Recommend closing the run — the headline `solved` is recorded.
