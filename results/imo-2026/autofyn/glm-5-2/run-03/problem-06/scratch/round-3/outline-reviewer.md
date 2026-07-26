# outline-reviewer — round 3 — imo-2026-06 (stall-trigger)

Start: 2026-07-25 16:39 UTC. Stall trigger fired (3rd round on Gap A; 3 of 4 attack mechanisms certified dead on the SAME obstruction in round 2). My gate duties: ensure ≥1 genuinely-different framing enters the build set, cut doomed lines, rank the whole field, emit the build set. I did NOT rubber-stamp the outliner — one of its four "genuinely-different" slugs is cut (RETHINK) because the outliner itself admits its key lemma IS Gap A.

## Cross-cutting findings

**The field has NOT actually diversified away from the cofactor-bound wall.** Of the four proposed slugs, THREE (`increment-pigeonhole-window`, `crt-period-lifting`, `p1-equals-2-direct`) bottom out — by the outliner's OWN admission, in prose — on the same conjecture "every governing prime $q$ satisfies $q\le M_1=\operatorname{rad}(a_1)$" or its finiteness equivalent. That is Gap A. Only `integer-monovariant-transfer` has a chance of being orthogonal, and even there the load-bearing statistic is UNIDENTIFIED. This is the single-gap trap CLAUDE.md warns about: if the cofactor-bound conjecture is true but unprovable by these mechanisms, three of four new slugs die together. I flag this for the orchestrator: the genuinely-different escape, if it exists, is `integer-monovariant-transfer` (and possibly a future framing the outliner has not yet surfaced — covering-systems was scouted this round and certified a relabeling, so it is NOT one).

**Negative lemma `syndetic-divisible-closed-not-periodic` — RECOMMEND CERTIFICATION.** The counterexample $B=6\mathbb Z\cup\bigcup_{p\equiv1(4)}p\mathbb Z$ is divisibility-closed, syndetic (gaps $\le6$), and aperiodic (structural proof via Dirichlet: pick prime $q\equiv3\bmod4$, $\gcd(q,6)=1$, $q>L$; then $q\notin B$ but $q+L\in B$ for a density-$1/2$ subfamily — contradiction to $L$-periodicity). This is a sound, non-circular guardrail: it PROVES any viable proof of $\mathcal B_\infty$'s periodicity MUST use a greedy-specific DYNAMIC property (cyclic-successor generation order, or a bounded non-residue statistic), NOT pure statics (divisibility-closure + syndeticity). All four new framings should import it as a fence. The proof-reviewer should certify it as `lemmas/syndetic-divisible-closed-not-periodic.md`.

**Retirements confirmed.** `growing-modulus-descent` (monovariant $w_n$ provably non-monotone, $a_1=116$) and `witness-density-recurrence` (Step 5 circular, minimal-criminal rescue not well-founded) are certified dead-end in round 2; both are RETIRED from the build pool. Their negative lemmas (`monovariant-non-monotonicity`; the sound sub-lemma W1 spacing $\le M_1/q$ if any new framing needs it) stay certified. `transversal-saturation` and `prime-power-dichotomy` stay in the population as certified-lemma SOURCES only (13 certified lemmas importable); the dead `aimo-0030` strip is NOT advanced.

---

## Per-slug review

### integer-monovariant-transfer — Verdict: CHANGES REQUESTED (the stall-trigger's genuinely-different framing; buildable but the engine is unspecified)

**Framing assessment.** This is the ONLY one of the four proposed slugs that is NOT, by the outliner's own prose, a restatement of Gap A. The route (an `aimo-0134`-style integer-valued statistic on the orbit, integrality upgrades a strict inequality to weak monotonicity, eventual constancy, transfer back to $d_n$ via finite-state pigeonhole) does not pass through transversals, MT, or a residue modulus. It is genuinely non-transversal and non-modular. This satisfies the stall-trigger's "≥1 genuinely-different framing" requirement.

**Why CHANGES REQUESTED, not APPROVE.** The load-bearing step (step 3) is, by the outliner's explicit admission, UNIDENTIFIED: "the actual statistic and the greedy-forced strict inequality that drives its monotonicity are not yet identified." This is not a peripheral gap — it is the entire engine. The candidate $c_n=M_1 b_n-(a_n-a_1)$ (shortfall below the block ceiling) is offered, but the outliner itself flags that $b_n=\lfloor(a_n-a_1)/M_1\rfloor$ is "NOT forced divisible by anything," so the `aimo-0134` strict-inequality-via-divisibility mechanism does NOT port. The transfer step (step 4) is also not closed: the state $(c_n,\text{recent }d\text{-window})$ is finite, but the TRANSITION depends on $S(a_{n+1})$'s free-rider primes — the finite-statistic explorer certified this leak is real (89 conflicts for $a_1=385$ on $a_n\bmod 385$). If the chosen statistic is a residue in disguise, the negative lemma `syndetic-divisible-closed-not-periodic` kills it.

**Required fixes during build (builder must close these or the approach dies):**
1. Identify a CONCRETE integer-valued statistic $c_n$ that is (a) NOT a function of $a_n\bmod L_0$ for any $L_0<L$ (the minimal functional modulus is $L$ itself — verified), and (b) a DYNAMIC function of the recent orbit segment (the negative lemma forces this).
2. Exhibit a CONCRETE greedy-forced strict inequality driving $c_n$'s monotonicity — coming from "the greedy pick is the SMALLEST admissible" (no admissible $m\in(a_n,a_{n+1})$), NOT from a divisibility (the `aimo-0134` divisibility lever does not port).
3. Verify the candidate against the LOCK cases (should give $c_n\equiv0$) and the hard 385/1309/2085 cases (large period) — the explorer's table gives ground truth.
4. The transfer step must NOT relapse into a residue statistic; if the only eventual-constancy mechanism available is "$a_n\bmod L$ is eventually fixed," that IS Gap A and the approach collapses.

**Verdict.** Sound as a direction; the engine is a hope, not a lemma. CHANGES REQUESTED — pursue it, but the builder is on notice that an unspecified statistic with no monotonicity mechanism is the whole ballgame. If the builder cannot concretize step 3 this round, the approach should be marked unsolved next round.

---

### increment-pigeonhole-window — Verdict: RETHINK (the outliner admits the key lemma IS Gap A; relabeling, not a genuinely-different framing; NOT registered)

**Framing assessment.** The outliner's step 4 says, verbatim: "KEY LEMMA (load-bearing, = Gap A restated in increment language, but cleanly isolated)." The finite-statistic explorer scouted this exact route and CERTIFIED it is Gap A in disguise: the transition $\sigma_n\to\sigma_{n+1}$ is provably NOT determined by $\sigma_n$ (or by $(\sigma_n,a_n\bmod M_1)$), because the free-rider primes of $S(a_{n+1})$ are not captured by the state — concretely, 89 conflicts for $a_1=385$ on $a_n\bmod 385$. The only escape is bounding the free-rider primes, which IS Gap A. The fallback sub-lemma ("realized window-state set has size exactly $T$") is ALSO Gap A — it requires knowing $L$ to prove, and proving it without knowing $L$ is the wall.

**Why RETHINK.** This is not a whole attempt at a different route — by the outliner's own admission it is Gap A "restated in increment language." CLAUDE.md: a slug is a whole attempt, not a diagnostic. The "clean isolation" of the wall has diagnostic value (it sharpens the cofactor-bound statement into "only primes $\le M_1$ ever act as the unique connector reducing $d_n$ below the $P_1$-skeleton value"), but that sharpened statement is a sub-lemma to IMPORT into other framings, not a standalone proof. Building this slug produces no new proof — it re-derives the wall in window language. A doomed line: NOT registered, NOT in the build set. The sharpened cofactor-bound statement should be recorded as a sub-lemma in `current.md` for `integer-monovariant-transfer` / `crt-period-lifting` / `p1-equals-2-direct` to import.

**Not registered, not built.** The genuinely-different slot is filled by `integer-monovariant-transfer`.

---

### crt-period-lifting — Verdict: CHANGES REQUESTED (genuinely-different framing, but TWO hard gaps, one of which is Gap A; buildable, does NOT bypass Gap A)

**Framing assessment.** The `aimo-0231` CRT fiber-lifting template (bound per-prime return-time growth by the fiber size of $\mathbb Z/L_{k+1}\mathbb Z\to\mathbb Z/L_k\mathbb Z$) is a genuinely-different framing — it is inductive/CRT, not transversal/strip/monovariant/density. It targets the whole theorem end-to-end from the certified LOCK base.

**Two load-bearing gaps (both honestly flagged by the outliner):**
1. **The lift bound for the GREEDY successor (step 3).** The `aimo-0231` crux is for a polynomial iterate; the greedy cyclic successor is NOT a polynomial iterate, and admissibility couples all primes simultaneously, so "CRT does NOT cleanly decouple" (outliner's own warning). The fiber-count must be RE-PROVED for the cyclic-successor map. This is a real, non-circular, non-Gap-A gap — but it is open and may not hold.
2. **Finiteness of the governing set (step 4 = Gap A).** The outliner admits: "this IS Gap A, but the inductive fiber structure gives a cleaner handle than the strip." KEY LEMMA 2 ("governing primes finite and $\le M_1$") is the cofactor-bound conjecture. If (1) holds but (2) fails, the approach dies. This is the single-gap-trap risk shared with `p1-equals-2-direct`.

**Additional concerns from the explorer (induction-on-P1):** the drop-$r$ quotient map is DEAD (not-$r$ sub-sequence does NOT match $\operatorname{greedy}(a_1/r)$, verified $a_1=385,r=11$); $v_p(a_n)$ does NOT stabilize (fluctuates in the tail for $a_1=385$); the governing set is NOT $P_1\cup\{2,3\}$ ($2085$ has $139\in P_1$ but $139\notin$ governing set). The induction is on governing primes ADDED via CRT fiber lifting, NOT on $|P_1|$ via quotient descent — the builder must respect this.

**Required fixes during build:**
1. Prove the per-prime lift factor $\le r$ for the GREEDY cyclic successor (not a polynomial iterate) — or prove the lift factor is bounded by SOME explicit function, even if not $\le r$.
2. Confront the finiteness step honestly: do NOT assume "governing primes $\le M_1$" — if the lift bound (1) can be combined with a density/growth argument to bound the governing set without assuming Gap A, that is the win. If not, the approach is honest-dead on Gap A, not a stealth-assumption.
3. Handle the lift order: $|P_1|=3$ is mostly EASIER than $|P_1|=2$ (non-$P_1$ gov $\subseteq\{2,3\}$ except $385$); do not assume monotonicity in $|P_1|$.

**Verdict.** Different framing, sound direction, two open gaps (one is Gap A). CHANGES REQUESTED — pursue, but the builder must not assume Gap A away.

---

### p1-equals-2-direct — Verdict: CHANGES REQUESTED (legitimate partial base-case, NEW lever, but shares the cofactor-bound wall with crt-period-lifting = single-gap-trap risk)

**Framing assessment.** This is a SPECIALIZATION (shrink the theorem to $|P_1|\ge3$ by solving $|P_1|=2$ NON-LOCK directly), not a whole-theorem proof — step 5 explicitly defers the general case to `crt-period-lifting`. CLAUDE.md prefers whole attempts, but a structural-induction BASE CASE that shrinks the theorem and gives a new lever is a legitimate partial target, and the LOCK base is already certified. It is not "one proof split across sibling slugs" in the forbidden sense — it is a base case paired with a different (CRT-lifting) inductive step; the two are rival framings that happen to compose.

**The NEW lever (genuinely unavailable for $|P_1|\ge3$).** Step 2 is a real elementary win: $a_2=a_1+p_{\rm sm}=p_{\rm sm}(q+1)$ is even (since $q$ odd prime $\Rightarrow q+1$ even), so $2$ enters provably at $n=2$. After $n=2$, $2$-multiples occur at density $1/2\gg1/p_{\rm sm}$. This density dominance is a mechanism ABSENT for $|P_1|\ge3$ (where no single prime dominates), so it is a genuine narrowing of the wall, not just a relabeling.

**The wall (step 3).** KEY LEMMA "governing primes $\le M_1$ for $|P_1|=2$ NON-LOCK" is Gap A specialized. The explorer (induction-on-P1) confirmed empirically (15+ squarefree + non-squarefree cases) the conjecture holds but found NO non-circular density mechanism to prove it — and the absolute-constant strengthening is FALSE ($a_1=847$ has gov prime $41$; $a_1=175$ has $13$). The "2-density dominance forces witnesses to be 2-multiples, gap bound bounds the cofactor" mechanism is a TARGET, not a proof. This is the single-gap-trap: if the cofactor bound is unprovable here, this slug AND `crt-period-lifting` die together.

**Required fixes during build:**
1. Make the 2-density-dominance mechanism RIGOROUS, not empirical: prove that after $n=2$, the smallest-admissible candidate is always $2$-divisible in the $|P_1|=2$ NON-LOCK regime (the explorer flagged this as a "might exist" — the builder must either prove it or show where it breaks).
2. Classify the LOCK coverage for $|P_1|=2$ (step 1) — no clean closed-form found; $a_1=p^k q$ locks iff a power $p^j$ is reached before a blocking term, depending on $q+1$'s factorization. The builder should at minimum enumerate the NON-LOCK conditions precisely.
3. Do NOT re-attempt the `aimo-0030` strip in the $|P_1|=2$ specialization (the admissibility-transfer obstruction re-appears regardless of $|P_1|$ — certified dead).
4. Be honest that this is a partial: even fully solved, it leaves $|P_1|\ge3$ open (deferred to `crt-period-lifting`).

**Verdict.** Legitimate base-case attack with a new lever; shares the cofactor-bound wall. CHANGES REQUESTED — pursue as a partial, flag the single-gap-trap risk explicitly.

---

## Diversity-of-thought assessment (for the orchestrator)

The field has diversified in FRAMING (monovariant, CRT-lifting, structural-induction base) but NOT in WALL: three of four new slugs still bottom out on the cofactor-bound conjecture "governing primes $\le M_1$." The genuinely-orthogonal escape is `integer-monovariant-transfer` alone, and even there the engine is a hope. If `integer-monovariant-transfer` dies next round (builder cannot find a non-residue dynamic statistic with a monotonicity mechanism), the orchestrator should tell next round's outliner to open a framing that attacks the problem from a representation NOT based on "bound the governing primes" at all — e.g. a direct argument on the increment sequence $(d_n)$ as a substitutional/morphism object, or a dynamical-systems/ergodic angle on the cyclic-successor map. The three explorers this round collectively certified that finite-statistic, sieve, and modular framings ALL collapse to Gap A; the untried orthogonal directions are dynamic-systems / combinatorics-on-words flavored.

## Build set

build set: integer-monovariant-transfer, crt-period-lifting, p1-equals-2-direct
