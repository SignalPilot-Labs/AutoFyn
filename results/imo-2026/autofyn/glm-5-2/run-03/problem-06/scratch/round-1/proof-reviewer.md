# proof-reviewer — imo-2026-06 (round 1)

Reviewed three built approaches: `transversal-saturation`, `prime-power-dichotomy`, `free-rider-type-replacement`. (The fourth registered slug `growing-modulus-descent` was NOT built this round; not reviewed.) All three share a proved foundation (linchpin + gap bound + pairwise-intersecting supports + hitting-set reformulation + conditional cyclic-successor endgame), which I verified independently and certify into `lemmas/`.

I re-derived the load-bearing steps from scratch and ran Python to check the algebra and small cases. **Two significant findings beyond the per-approach verdicts:**

**(F1) The compute-explorer report's headline "a_1=385 is aperiodic through 12000 terms" is FALSE.** Direct computation: for $a_1=385$, the full minimal-transversal family (including the prime $19$, which the explorer missed by restricting to primes $\le Q=11$) **stabilizes at $n=38$** to exactly 7 transversals $\{2,7\},\{2,3,5\},\{2,3,11\},\{2,11,19\},\{3,7,11\},\{3,7,19\},\{5,7,11\}$, with $L=\operatorname{lcm}(\operatorname{rad})=43890$ and $|A|=T=5088$. The cyclic-successor map on $A$ predicts $a_{n+1}\bmod L$ with **zero mismatches over 600 terms**, and the pure-from-start equality $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ holds for all 700 terms tested. The explorer's autocorrelation test only checked $T\le3000$; the true period $5088>3000$. Same story for $1309, 2431$ (claimed "aperiodic"; actually stable from $n\approx50$, all non-redundant primes $\le17\le M_1$).

**(F2) The naive bound $q\le M_1=\operatorname{rad}(a_1)$ on non-redundant primes holds in ALL 80+ starting values tested** (including every claimed-"hard" case: $385,1309,2431,741,957,1023,1131$). For $a_1=741$ the non-redundant set transiently grows to 84 primes (max $541<M_1=741$) before the sequence LOCKS at $3^k$ and collapses to $\{3\}$. If $q\le M_1$ is provable, Gap A closes immediately (primes $\le M_1$ finite ⇒ distinct supports stabilize ⇒ $\operatorname{MT}$ stabilizes ⇒ $\mathcal B_\infty$ $L$-periodic). **None of the three approaches found this; `transversal-saturation` actively (and wrongly) dismissed it.** This is the most promising unexplored direction and should be routed to next round's outliner/builder.

---

## `transversal-saturation` — Status: partial — Verdict: CHANGES REQUESTED

**What's proved (sound, verified):**
- Lemma 1 (linchpin) + Corollary (gap bound $d_n\le M_1$): correct. Verified on 80+ cases.
- Lemma 2 (pairwise-intersecting supports): correct (one-line: $a_j$ admissible against $a_i$).
- Lemma 3 (every term $\in\mathcal B_\infty$): correct, uses Lemma 2. Verified for $a_1=385$ (all 700 terms lie in $\mathcal B_{38}$).
- Lemma 4 (greedy = cyclic successor in $\mathcal B_\infty$ from $n=1$, pure-from-start): correct. Verified for $a_1=385$: $a_{n+1}=\min(\mathcal B_\infty\cap(a_n,\infty))$ with **0 failures over 700 terms**. This UNCONDITIONALLY closes the "pure-from-start" wall (Gap B) modulo the periodicity of $\mathcal B_\infty$ itself.
- Lemmas 5–6 (cyclic-successor bijection ⇒ single $|A|$-cycle ⇒ $a_{n+T}=a_n+L$ for all $n\ge1$, conditional on $\mathcal B_\infty$ $L$-periodic): correct. Verified for $a_1=385$: $T=5088$, $L=43890$, cyclic successor matches with 0 mismatches.
- Lemma 9 (lock: prime-power term ⇒ $T=1,L=p$): correct, verified for $a_1\in\{6,21,33,50\}$.
- Step 6 equivalence (Gap A "$\mathcal B_\infty$ $L$-periodic" ⇔ "finitely many governing primes"): the ⇐ direction is clean; the ⇒ direction uses an intricate CRT "shift a witness off its private prime" trick, plausibly correct but not the load-bearing part.

**The reduction to Gap A is SOUND.** Gap A is the only remaining wall in this framing. This matches the approach's self-assessment.

**Gaps / errors found:**
1. **(Factual error, Step 7, lines 110 & 138)** The "obstruction" narrative claims: "for $a_1=385$ the sequence is aperiodic through 12000 terms while the small-prime ($\le 11$) constraint family has stabilized by term 225 — meaning free-rider primes (necessarily $>11$, and by the data growing with $a_n$) keep entering minimal transversals." and "The naive size bound $q\le M_1$ is **false**... refuted by the $a_1=385$ data." **Both claims are FALSE.** Per finding (F1): $a_1=385$ is periodic from $n=1$ (stabilizes at $n=38$); only ONE free-rider prime $>11$ (namely $19$) ever enters, once, at $n\le38$; it does NOT grow. Per finding (F2): $q\le M_1$ HOLDS for $a_1=385$ (max non-redundant prime $19\le385=M_1$) and in every case tested. The approach misread the faulty compute-explorer data and dismissed the very bound that appears to close Gap A.
2. **(Honest gap)** Gap A itself is open — correctly flagged.
3. **(Minor, Step 7 "open sub-lemma")** The observation that the abstract pairwise-intersecting structure is insufficient (star $\{\{1,j\}:j\ge2\}$ counterexample) is a valid abstract point, but it does not bear on the greedy-coupled problem (the star is not realized by any $a_1$). Keep but contextualize.

**Why not APPROVE:** Gap A is open; the theorem is not proved. Why not RETHINK: the reduction is sound and the route is alive; the builder should be sent back to close Gap A, ideally by attempting the $q\le M_1$ bound the approach wrongly dismissed.

**Builder status field says `partial`.** Correct. Do not upgrade.

---

## `prime-power-dichotomy` — Status: partial — Verdict: CHANGES REQUESTED

**What's proved (sound, verified):**
- Section A foundation (Linchpin, Gap bound, Pairwise-intersecting): correct (shared).
- **Lemma LOCK (Section B): SOUND and rigorously proved.** I re-derived each step:
  - (1) $p\mid a_1$: $a_i=p^k$ admissible ⇒ $\gcd(a_i,a_1)>1$ ⇒ $p\mid a_1$. ✓
  - (2) $p\mid a_j\ \forall j$: three ranges ($j=i$ trivial; $j<i$ via $a_i$'s admissibility forcing $p$ to be the shared prime; $j>i$ via later terms' admissibility against $a_i$). ✓
  - (3) $a_{n+1}=a_n+p$: lower bound from "$a_{n+1},a_n$ both $p$-multiples, distinct" ⇒ $a_{n+1}\ge a_n+p$; upper bound from "$a_n+p$ is a $p$-multiple hence admissible" ⇒ $a_{n+1}\le a_n+p$. ✓
  - Verified computationally for $a_1\in\{6,21,33,50\}$ (lock at $8,27,81,64$ resp.; $a_n=a_1+p(n-1)$ holds from $n=1$). The $a_1=33$ case (locks at $81=3^4$ after 16 steps) confirms the lemma holds even when the lock appears late.
- Section C.1 transversal reformulation: correct, standard.
- C.2 private-set structure lemma: correctly stated; honest that it does not close Gap C. The invalid "else lock" mechanism was **honestly removed** — no false claim left. Confirmed.

**Gaps / errors found:**
1. **(Flawed justification, C.3, line 106)** The conditional endgame asserts: "The family $\operatorname{MT}(\mathcal F_n)$ is a non-increasing antichain in the finite Boolean lattice on $\mathcal Q_\infty$ (adding a set to $\mathcal F_n$ can only enlarge transversals, hence can only *remove* elements from $\operatorname{MT}$)." **This is FALSE.** Adding a set to a hypergraph can both delete AND create minimal transversals. Concrete counterexample: $F=\{\{1,2\}\}$ has $\operatorname{MT}=\{\{1\},\{2\}\}$; adding $\{2,3\}$ gives $F'=\{\{1,2\},\{2,3\}\}$ with $\operatorname{MT}=\{\{2\},\{1,3\}\}$ — the transversal $\{1,3\}$ is newly created (it was a non-minimal transversal of $F$, now minimal). So $\operatorname{MT}$ is NOT monotone. The **conclusion** (stabilization under Gap C) is still TRUE, but via a different argument: under Gap C the prime set $\mathcal Q_\infty$ is finite, so the set of *distinct supports* $\{S(a_i):i\le n\}$ is an increasing family bounded by $2^{\mathcal Q_\infty}$, hence stabilizes; and $\operatorname{MT}$ depends only on the set of distinct supports (duplicates impose no new constraint), so $\operatorname{MT}$ stabilizes. The builder must replace the flawed monotonicity claim with this correct argument.
2. **(Honest gaps)** Gap C (finiteness of minimal-transversal primes in no-lock regime) OPEN. Gap B (pure-from-start) OPEN here — though note it is CLOSED unconditionally by the `transversal-saturation` Lemma 4 (importable). The builder should import that lemma rather than re-prove Gap B.

**Why not APPROVE:** LOCK branch is complete but the NO-LOCK branch is open (Gap C); the conditional endgame has a flawed justification. Why not RETHINK: the LOCK lemma is genuine certified progress (a real lemma for the cache) and the dichotomy framing is sound; send back to close Gap C (consider the $q\le M_1$ direction) and fix C.3.

**Builder status field says `partial`.** Correct. Do not upgrade.

---

## `free-rider-type-replacement` — Status: unsolved — Verdict: RETHINK

**What's proved (sound, shared, verified):**
- Foundation Lemmas 1–4 (linchpin, gap bound, pairwise-intersecting, hitting-set reformulation): correct.
- Lemma 5 (finite type set, $\le 4^{|P_1|}$ types): correct (both components in $2^{P_1}$).
- Lemma 6 (cyclic-successor bijection on $A=\mathcal B_\infty\bmod L$): correct (matches the transversal-saturation Lemma 5).
- Lemma 7 (periodicity conditional on Gaps A & B): correct.

**The approach-specific crux (Gap F, same-type replacement) is REFUTED — and the refutation is CORRECT.** I independently verified the refutation's key claims for $a_1=385$:
- The sequence starts $385,390,392,396,399,406,418,420,434,448,450,462,\dots$ ✓ (matches).
- MT stabilizes at $n=38$ to 7 transversals, $L=43890$, $T=5088$ ✓ (matches — I computed this directly).
- Non-redundant primes $=\{2,3,5,7,11,19\}$, stable through $n\ge600$ ✓ (verified via my own non-redundancy characterization, validated against brute-force MT on small $a_1=15$).
- $\tau(2)=\tau(3)=(\{5\},\{5,7,11\})$ ✓ (verified by hand from the 7 transversals: for $q=2$, MTs containing 2 are $\{2,7\},\{2,3,5\},\{2,3,11\},\{2,11,19\}$, giving $B(2)=\{5,7,11\}$; symmetrically for $q=3$).
- Both $2$ and $3$ non-redundant through $n\ge600$ with no replacement ✓.
So Gap F is genuinely false, and the approach honestly records this (the builder REFUTED its own crux). The "approach cannot yield a proof via same-type replacement" is correct.

**Gaps / errors found:** None beyond the (honestly recorded) dead crux. The approach's positive claim that $a_1=385$ stabilizes at $n=38$ with $T=5088$ is CORRECT (contradicting the compute explorer, but the approach got it right). The approach correctly notes it collapses to the same wall as `transversal-saturation` (Gap A) with no new mechanism.

**Why RETHINK (not CHANGES REQUESTED):** The approach's specific route (type-competition / same-type replacement) is fatally broken — the crux is refuted, not merely open. There is no "fix" within this framing; the finiteness wall it renames is identical to Gap A, which `transversal-saturation` already attacks more directly. The approach must go back to the outliner for a genuinely different strategy (or be folded into `transversal-saturation` as a contributor of the shared endgame + the Gap F dead-end record).

**Builder status field says `partial`.** I judge this **too generous**: the approach-SPECIFIC contribution (type classification + replacement) is refuted; the shared foundation is real but redundant (every approach has it). The approach as a distinct route is a dead-end. True Status: **unsolved**. The certified shared lemmas and the Gap F dead-end record are the usable outputs.

---

## Certified promotable lemmas (written to `results/imo-2026-06/lemmas/`)

All correctly and rigorously proved; reviewer-certified; importable by any approach:
- `linchpin-and-gap-bound.md` — linchpin + $d_n\le M_1$ (foundation).
- `pairwise-intersecting-supports.md` — $S(a_i)\cap S(a_j)\ne\varnothing$.
- `every-term-in-binfinity.md` — $a_k\in\mathcal B_\infty$ (Lemma 3 of transversal-saturation).
- `greedy-equals-cyclic-successor.md` — pure-from-start resolved unconditionally (Lemma 4). This is the most valuable shared lemma: it closes Gap B for ALL approaches.
- `lock-lemma.md` — prime-power term ⇒ $T=1,L=p$ (Lemma 9 / Lemma LOCK).
- `cyclic-successor-bijection.md` — bijection ⇒ single cycle ⇒ $a_{n+T}=a_n+L$ (conditional on Gap A).

Rejected: none (all proposed lemmas that were actually proved passed; the proposed "Lemma 6 cyclic successor" from free-rider is the same as transversal-saturation's Lemma 5 — certified once).

Dead-end record (not a positive lemma): `gap-f-refuted.md` — same-type replacement is FALSE; do not retry. Includes the correction to the compute-explorer's aperiodicity claim.

---

## Goal Progress (ranking snapshot)

From `results/imo-2026-06/approaches/.ranking.json` (pre-review, all stale=false, no outcomes yet):

| slug | Elo | last outcome | built r1? |
|---|---|---|---|
| transversal-saturation | 1545.8 | — | yes |
| prime-power-dichotomy | 1515.4 | — | yes |
| growing-modulus-descent | 1470.3 | — | no (held back) |
| free-rider-type-replacement | 1468.5 | — | yes |

After this review: `transversal-saturation` and `prime-power-dichotomy` remain the live leaders (real certified progress; both at `partial`, route alive). `free-rider-type-replacement` is a dead-end (RETHINK). The shared foundation + endgame are now in `lemmas/`, so any future approach (including a revived `growing-modulus-descent` or a new framing attacking $q\le M_1$) can import them.

**Headline for the orchestrator:** No solve this round. The single most important finding is (F2): the bound $q\le M_1=\operatorname{rad}(a_1)$ on non-redundant primes holds empirically across all tested $a_1$ (including the claimed-"hard" $385,1309,2431,741$) and would close Gap A immediately if proved. Next round's outliner should put ≥1 approach on proving this bound directly (or the sharper empirical variant), which is a genuinely different sub-task from the antichain-shrink / type-competition framings that currently populate the field. The field has NOT collapsed to one framing yet (the dichotomy and the dead type-competition are genuinely different), but the two live approaches both bottom out on the same Gap A wall — the $q\le M_1$ direction is the untried attack on that wall.

---

## Routing (per slug)

- **`transversal-saturation`** → CHANGES REQUESTED. Send back to the builder to (a) correct the Step 7 factual errors (a_1=385 is periodic, $q\le M_1$ is NOT refuted), and (b) attempt to PROVE $q\le M_1$ (or the sharper bound) — this is the most promising route to closing Gap A. Status stays `partial`.
- **`prime-power-dichotomy`** → CHANGES REQUESTED. Send back to (a) fix the C.3 monotonicity flaw (replace with the "distinct supports stabilize" argument), (b) import `greedy-equals-cyclic-successor` from `lemmas/` to close Gap B for free, (c) attack Gap C — consider the $q\le M_1$ direction in the no-lock regime. Status stays `partial`.
- **`free-rider-type-replacement`** → RETHINK. The approach-specific crux is refuted. Send back to the outliner for a different strategy, or fold its shared outputs (already in `lemmas/`) into the other approaches and retire the slug. Status: `unsolved` (downgraded from the builder's `partial`).
