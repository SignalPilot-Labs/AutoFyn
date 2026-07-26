# proof-reviewer — round 2 — imo-2026-06

Start: 2026-07-25 16:09 UTC. Four builds reviewed independently. Every load-bearing claim re-derived / re-computed in Python (sympy factorint, brute-force MT).

## transversal-saturation — Status: partial — Verdict: CHANGES REQUESTED

### Positive results (verified, certified)

- **Lemma A** (smallest-multiple structure): if $q>M_1\ge d_{i-1}$ and $q\mid a_i$, then $a_i=q\lceil(a_{i-1}+1)/q\rceil$. Independent re-derivation: the gap bound gives $a_i-a_{i-1}<q$, so $a_i$ is a multiple of $q$ in the length-$q$ interval $(a_{i-1},a_{i-1}+q]$, which contains exactly one multiple of $q$. Sound. Certified `lemmas/lemma-A-smallest-multiple.md`.
- **Corollary A1** ($q\nmid a_{i-1}$) and **A2** (predecessor shares a small prime $\le M_1$): both follow by elementary divisibility + pairwise intersection. Sound. Certified with A.
- **Lemma B** ($T\setminus\{q\}$ transverses $\mathcal F_{i-1}$ for smallest-index private witness): the contradiction is $j<i$ with $S(a_j)\cap T=\{q\}$, contradicting smallest-index choice. Sound. Certified `lemmas/lemma-B-transversal.md`.
- **Lemma C** (size-bound no-go): case (i) $d_{i-1}\le A\Rightarrow x_0=a_i$ (verified: $a_7=418,A=22,a_6=406\Rightarrow 22\lceil407/22\rceil=418$); case (ii) $d_{i-1}>A\Rightarrow$ all multiples of $A$ in $(a_{i-1},a_i)$ inadmissible by greedy minimality. Sound. Certified as a negative lemma `lemmas/lemma-C-strip-no-go.md`.

### No-go findings (verified)

- **$p^kA$ exponential blowup**: for $a_1=385,q=19$, witness $a_5=399\Rightarrow x=7^2\cdot21=1029\gg399$; witness $a_7=418\Rightarrow x=11^2\cdot22=2662\gg418$. Re-computed independently — matches. Range $x\in[686,4802]\gg a_i\in[399,1064]$ confirmed.
- **Admissibility-transfer obstruction**: 51 pairs sharing only 19 in the first 700 terms of $a_1=385$ — re-counted, matches exactly. The obstructed pair $a_5=399$ vs $a_7=418$ (intersection $\{19\}$) verified; $a_5$ is a no-obstruction witness in $T=\{2,11,19\}$ (shares 7,3,7,3 with earlier terms), $a_7$ in $T=\{3,7,19\}$ is obstructed. Verified.
- **Step 7 correction**: $a_1=385$ IS periodic from $n=1$ ($L=43890=2\cdot3\cdot5\cdot7\cdot11\cdot19$, governing primes $\le M_1=385$) — consistent with the certified `gap-f-refuted` lemma.

### Verdict
Real progress (4 promotable lemmas certified: A/A2/B/C) and a rigorous no-go on the strip. But Gap A remains open and the strip formulation is a dead-end. The builder's self-claim (partial, CHANGES REQUESTED) is accurate. CHANGES REQUESTED — but the "change" required is a *different mechanism* for Gap A, not a patch to the strip.

---

## prime-power-dichotomy — Status: partial — Verdict: CHANGES REQUESTED

### Positive results (verified, certified)

- **C.3 fix (distinct-supports-stabilize)**: the round-1 false claim "MT is a non-increasing antichain under set addition" (counterexample $F=\{\{1,2\}\}$, add $\{2,3\}$, gains $\{1,3\}$ — re-verified) is replaced by: (a) `mt-depends-on-set-system` (MT depends only on the distinct member-sets — standard, sound, certified); (b) `distinct-supports-stabilize` (conditional on Gap C: $\mathcal D_n\subseteq 2^{\{p\le B\}}$ increasing ⇒ stabilizes ⇒ MT stabilizes ⇒ $\mathcal B_\infty$ $L$-periodic — sound, certified). This is the correct reduction from Gap A/C to periodicity.
- **Gap B closed** (imported `greedy-equals-cyclic-successor`); **endgame imported** (`cyclic-successor-bijection`); **LOCK branch** certified (`lock-lemma`).
- **private-set-structure (no-lock)** lemma: every large prime $t\in T$ is witnessed by a term whose $P_1$-part lies in $P_1\setminus T$. Definitional + linchpin. Sound, certified.

### No-go finding (verified)
The NO-LOCK strip (C.4) is explicitly declared as the SAME `aimo-0030` crux as transversal-saturation Step 7 (shared dependency, not re-proved). Since that crux is now shown obstructed (Lemma C no-go + 51 obstructed pairs), the NO-LOCK branch is conditional on a lemma that is now a certified dead-end. The $|S(a_i)|\ge2$ sharpening is a genuine minor strengthening (one extra small prime) but does not close the load-bearing sub-lemma — the builder does not claim it does.

### Verdict
C.3 fix is sound and the promotable lemmas are certified. Gap C remains open and is the same wall as Gap A. The builder's self-claim (partial, CHANGES REQUESTED) is accurate. CHANGES REQUESTED.

---

## growing-modulus-descent — Status: unsolved (dead-end) — Verdict: RETHINK

### No-go finding (verified rigorously)

The monovariant $w_n=\min\{q>M_1:q\in\bigcup\operatorname{MT}(\mathcal F_n)\}$ is **provably non-monotone** in the real greedy sequence.

Killing counterexample $a_1=116=2^2\cdot29$, $M_1=58$. Re-derived greedy sequence: $116,118,120,122,124,126,128,\dots$ (steps by 2, locks at $a_7=128=2^7$). Brute-force MT re-computed independently:
- $n=1$: MT=$\{\{2\},\{29\}\}$, $w_1=+\infty$.
- $n=2$: MT=$\{\{2\},\{29,59\}\}$, $w_2=59$ (large prime $59>58$ enters via $\{29,59\}$ while $\{2\}$ persists).
- $n=7$: MT=$\{\{2\}\}$, $w_7=+\infty$ (lock).

$w_n=(+\infty,59,\dots,59,+\infty)$ — non-monotone under either convention. The "covered stays covered" anchor $\{2\}$ is present at $n=1$ and persists to the lock, yet $59$ enters MT at $n=2$. The structural family $a_1=p^e q$ realizes the abstract counterexample. Confirmed: every non-vacuous case is a LOCK case (handled by `lock-lemma`); non-LOCK cases are vacuous ($w_n\equiv+\infty$). The monovariant never does useful work.

Certified as negative lemma `lemmas/monovariant-non-monotonicity.md`.

### Verdict
The approach as set up (MT-frontier monovariant) cannot work — provably. The builder's self-claim (partial/RETHINK, recommend RETIRE) is accurate and if anything understated (this is unsolved/dead-end, not partial). RETHINK — retire the monovariant framing; back to outliner for a genuinely-different framing.

---

## witness-density-recurrence — Status: unsolved (dead-end) — Verdict: RETHINK

### Positive result (verified but NOT certifiable)

- **Lemma W1** (witness-index spacing): $i_{k+1}-i_k\ge q/M_1$. Re-derived: distinct multiples of $q$ differ by $\ge q$; gap bound $\sum d_n\le(i_{k+1}-i_k)M_1$; combine. Sound. BUT conditional on Premise W0 (governing $\Rightarrow$ infinitely many distinct private witnesses), which is plausible but **unproved** (the reduction "governing $\Rightarrow q$ divides infinitely many $a_i$" is non-trivial; $q$ could in principle divide finitely many terms yet stay in MT via a growing $T_k\setminus\{q\}$). The builder correctly does NOT propose W1 for certification. I agree — not certified.

### No-go finding (circularity, verified)

Step 5 (covering-capacity density lower bound) is **circular**:
- The covering capacity of $T\setminus\{q\}$ is UNBOUNDED for the greedy family *unless the primes in intermediate supports are bounded* — and bounding those IS Gap A.
- **Transient primes give unbounded covering capacity compatibly with Gap A**: a transient prime $r$ (in $G_n$ for finitely many $n$) can serve as a hitter in a $q$-free MT during its finite lifetime; fresh transient primes take over. Verified the empirical setup: $a_1=145$ locks at $n=97$ ($a_{97}=625=5^4$, $L=5$); $a_1=2085$ has term-primes reaching $2621>M_1=2085$ — transient primes can exceed $M_1$.
- **Minimal-criminal rescue fails (two independent reasons, both sound)**: (i) choosing $q$ = smallest governing prime $>M_1$ excludes only primes in $(M_1,q)$ from being *governing* — it does not bound *transient* primes (which can be arbitrarily large, compatibly with Gap A); (ii) governing primes $\ge q$ (other than $q$) are not handled — the "induction on the order of governing primes $>M_1$" pushes the problem UP ($r\ge q$, not $<q$), not down, so it is not well-founded.

The builder's honest self-marking (RETHINK candidate, circular, no false proof presented) is accurate. The density-counting costume founders on the same covering-capacity obstruction as the strip.

### Verdict
The load-bearing mechanism is structurally circular and the rescue is not well-founded. The approach cannot close Gap A as set up. RETHINK — retire unless a genuinely non-circular density lower bound (not via covering capacity of $T\setminus\{q\}$) is found.

---

## Headline finding for the orchestrator

**All four live approaches have hit a concrete wall on the SAME crux**, and three distinct attack mechanisms have now been *certified dead* this round:

| Mechanism | Approach | Verdict | Reason |
|---|---|---|---|
| one-shot prime-factor strip (`aimo-0030`) | transversal-saturation / prime-power-dichotomy | dead (Lemma C no-go) | size-bound structural no-go + admissibility-transfer obstruction (51 obstructed pairs) |
| MT-frontier monovariant (`aimo-0678`) | growing-modulus-descent | dead | $w_n$ provably non-monotone ($a_1=116$) |
| density/covering-capacity lower bound | witness-density-recurrence | circular | covering capacity unbounded compatibly with Gap A; minimal-criminal induction not well-founded |

**The common obstruction:** bounding which primes appear in the term supports $S(a_j)$ between consecutive large-prime witnesses IS Gap A, and no greedy-coupling mechanism has been found to bound them without assuming Gap A. The abstract pairwise-intersecting structure is insufficient (star $\{\{1,j\}:j\ge2\}$); the greedy coupling ($d_n\le M_1$, terms in $\mathcal B_\infty$, cyclic-successor structure) is essential but, as yet, not leveraged into a non-circular bound.

**Stall-trigger status (per CLAUDE.md):** this is the 2nd round on Gap A. Round 1 had 4 approaches registered; round 2 killed 3 of the 4 attack mechanisms (strip, monovariant, density) and confirmed they share one wall. Round 3 is the 3-round stall trigger — **force the outliner to open ≥1 genuinely-different framing, NOT a Gap-A variation.**

### Suggested genuinely-different framings (NOT yet tried; none pass through "bound the primes entering MT of $\mathcal F_\infty$")

1. **Finite-automaton / finite-sufficient-statistic framing.** The greedy rule $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$ is deterministic but history-dependent. The transversal framing's finite statistic is "MT($\mathcal F_n$)" — unbounded (Gap A). A different framing would seek a *different* finite sufficient statistic for the greedy pick (e.g. a bounded function of $a_n\bmod L_0$ for some $L_0$ derived from $a_1$'s prime structure, plus a bounded "state" summarizing the admissibility constraints). If a finite sufficient statistic exists, pigeonhole gives eventual periodicity of the increment $d_n$ (which takes values in $\{1,\dots,M_1\}$, already finite), hence of $a_n$, directly — no transversals, no Gap A.
2. **Structural induction on $|P_1|=|S(a_1)|$.** Base $|P_1|=1$ is the lock case (solved). For $|P_1|=2$ ($a_1=pq$ or $p^k q$), attempt a direct CRT/valuation analysis to prove periodicity unconditionally, then induct on $|P_1|$ by finding a "reducible" prime whose removal descends to a smaller-support sub-problem. This bypasses the transversal framework entirely.
3. **Covering-systems / sieve framing.** The "bad" integers (coprime to some prior term) form a growing union of residue classes modulo each $a_i$. Reframe as a covering-systems question: when does the forbidden set become periodic? The gap bound $d_n\le M_1$ makes $a_n$ grow linearly, so the moduli grow slowly — a sieve-type argument (large sieve / Lovász local?) may bound the number of distinct residue-class patterns without going through transversals.
4. **Direct induction on the stabilized increment pattern.** Compute (empirically) that $d_n$ is eventually periodic *from $n=1$* in every tested case, and attempt to prove the increment sequence $(d_n)$ is eventually periodic directly from the greedy rule + gap bound, without ever forming $\mathcal B_\infty$ or MT.

These framings are genuinely orthogonal to the transversal/hitting-set route that all four current approaches share.

## Per-slug routing

- `transversal-saturation` — CHANGES REQUESTED (partial: Lemmas A/A2/B/C certified; strip dead; Gap A open — need a different mechanism, NOT a strip patch).
- `prime-power-dichotomy` — CHANGES REQUESTED (partial: C.3 fix certified; LOCK + endgame + Gap B solid; Gap C = shared wall, open).
- `growing-modulus-descent` — RETHINK (unsolved/dead-end: monovariant provably non-monotone; retire the framing).
- `witness-density-recurrence` — RETHINK (unsolved/dead-end: Step 5 circular, minimal-criminal rescue not well-founded; retire unless a non-circular density lower bound appears).

**Headline:** Gap A is the single wall; three of four attack mechanisms are now certified dead-ends on the SAME obstruction (covering-capacity unboundedness compatibly with Gap A). Round 3 must force a genuinely-different framing (finite-automaton / structural induction on $|P_1|$ / covering-systems / direct increment-pattern induction) — NOT another Gap-A variation.
