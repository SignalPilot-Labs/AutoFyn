# outline-reviewer — IMO 2026 P6, round 129

Field: 7 approaches (δ, α, β, γ, ε, `smooth-window-crash`, `pstar-core-straggler`). The wall (saturated regime: prove $\mathcal M_n$ stabilizes / only finitely many primes enter minimal supports) is the only open piece. Freeze regime SOLVED (imported). This round the outliner opened one genuinely-new framing (`pstar-core-straggler`, Cov-monovariant, AVOIDS SPT), gave `smooth-window-crash` a real PARTIAL-scoped skeleton, advanced α/γ as W1-consumers, and moved to RETIRE ε and β. I concur.

## Verdicts

### pstar-core-straggler — APPROVE (new, registered at 1500; now 1530 after ranking)
Whole-claim attempt: yes — freeze branch imported, saturated branch via Cov-monovariant + crash-into-core, terminal self-blocking, δ finish. Targets the actual claim end to end.

Technique check (right technique?): The Cov-monovariant framing is the genuinely-different move the field needs. $\mathrm{Cov}(\mathcal M_n)=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}\subseteq P(a_1)$ is **tautologically** $\subseteq P(a_1)$ (finite by $a_1$'s factorization). Its monotonicity mechanism is sound and does NOT lean on the false free-rider universality: $\{2,p\}$'s only proper nonempty subsets are $\{2\}$ and $\{p\}$; both are singleton minimals $\Rightarrow$ `singleton-freeze` $\Rightarrow$ regime (F), excluded in (S). So in regime (S), $\{2,p\}$ persists once entered, hence $\mathrm{Cov}$ is monotone non-decreasing and stabilizes after $\le|P(a_1)|$ crashes. This is a clean refinement obstruction, not the refuted free-rider claim. It AVOIDS SPT (every minimal has a prime $\le p^*$) — Lemma C bounds crash primes $\subseteq P(a_1)$ by value-free structure, not entering primes by value. Confirmed: the framing survives if SPT/W1 fails. Good.

Does Lemma C secretly need SPT? No. Lemma C's mechanism is: $\{2,p\}$ is a transversal (2 hits core, $p$ hits straggler) $\Rightarrow$ $2p$-multiples valid $\Rightarrow$ smallest $\le a_n+2p\le a_n+\mathrm{mtp}$ (imported window) $\Rightarrow$ the greedy's smallest-first pick is the smooth $2^k\cdot p$. This is a smooth-number/value-dependent step, not "every minimal carries a small prime." It does not invoke SPT. Confirmed distinct wall.

CHANGES-REQUESTED note for the builder (fixable, does not block the build): **Lemma C has an unstated sub-claim** — that the straggler (a minimal $\not\ni 2$) actually *contains* a prime $p\in P(a_1)\setminus\mathrm{Cov}$. This does not follow from `common-primes-bounded` (that lemma bounds *common* primes, not straggler primes; a straggler's primes are not common). The straggler could in principle be $\subseteq\mathrm{Cov}$, or composed entirely of entering primes outside $P(a_1)$. The outline's Lemma D sub-case flags "$S=P(a_1)$ vs refinement" as CONJECTURE 6/6 — but Lemma C needs the weaker fact that *some* straggler prime lies in $P(a_1)\setminus\mathrm{Cov}$ *before* $\mathrm{Cov}$ saturates, which is not the same conjecture and is currently unjustified. The builder must either prove this (e.g. via the straggler being a refinement of $P(a_1)$, so $S\subseteq P(a_1)$, plus a counting argument that $S\not\subseteq\mathrm{Cov}$ while $\mathrm{Cov}\neq P(a_1)$ — the latter is NOT automatic and needs the greedy dynamics), or restructure Lemma C. Flag this explicitly; do not hand-wave it.

Also flag: Lemma A (core $\mathcal M_n^*$ stays nonempty) is not trivial — a core member $M\ni2$ can be refined by a straggler $S\not\ni2$ with $S\subsetneq M$ (e.g. $\{2,3,5\}\to\{3,5\}$), which does NOT trigger singleton-freeze and could empty the core. The outline marks Lemma A as GAP (honest), but the builder should note this is the real content of Lemma A, not a formality.

### smooth-window-crash — APPROVE (registered; now has a real PARTIAL-scoped body)
Whole-claim attempt: yes, but **honestly scoped** — closes GAP-1 (mtp bounded) only; GAP-3 (the wall) explicitly NOT closed, owned by pstar/α. The framing is upfront that SPT bounds mtp but not $P_{\ess}$ ($\{2,97\}$ antichain satisfies SPT, unbounded $P_{\ess}$). No overclaim: the scope statement (§6, §8) correctly separates "GAP-1 closed modulo W1+W2" from "wall open." Good.

Technique: W1 (mtp-witness carries a prime $\le p^*$) is honestly flagged as NOT a formality (constructible counterfamilies exist where $\prod T^*>\prod_{p\le p^*}p$ fails). W2 (strict-beat smooth-density) is the hard analytic step; the caveats are correctly listed (KB has no Dickman entry; asymptotic-vs-bounded-$x$ tension; validity conditions interact with density). The equality/strict-beat split correctly handles the REFUTED strict-beat linchpin (170/344 equality-promotions, $T^*$ is a transversal not a member so $P(a_{n+1})\supseteq T^*$ does not dominate). Sound skeleton; the gaps are load-bearing and honestly named with mechanisms.

### density-promotion-bound (α) — APPROVE (advance)
Advance is sound and disciplined: adopts W1 (owned by smooth) for GAP-1 closure via import, fixes the strict-beat linchpin (handles both equality- and strict-beats), and §5 explicitly forbids collapsing into pstar's Cov framing (preserves diversity). GAP-3 honestly open with the $\{2,97\}$ obstruction recorded. No overclaim. The freeze branch remains SOLVED (imported, unchanged). Build.

### bounded-gap-lcm-reduction (γ) — APPROVE (advance, thin)
Advance is correct but thin: imports W1 (closes GAP-1 conditionally), HOLDS on GAP-3 (finite-state route DEAD, unique-connector obstruction stands — both honestly recorded). γ's reusable asset (mtp monovariant) is already certified and imported by the field, so this round's standalone contribution is mostly articulation. Still worth building to keep the GAP-3 articulation alive and to record the dead finite-state route for future outliners. Build, but rank lowest of the live set.

### bertrand-dickson-eviction (β) — RETIRE
Concur with outliner. Doubly broken: (1) the eviction half uses the FALSE free-rider universality (refuted $a_1=15$ step 3); (2) circular $a_n$ bound (Lemma 5 bounds $a_i$ by $\prod O$ which depends on $a_{i-1}\to\infty$, so it bounds neither size nor count of essential primes). Bertrand eviction is DEAD (no dyadic interval forced to contain a new essential prime — admitted). Its one certified asset (`gap-bound-at-promotion`, cofactor $O=P(a_i)\cap P_{\ess,i-1}$ is a transversal, gap $\le\prod O$) is SUBSUMED by γ's `mtp-monovariant-and-gap-bound` (mtp is the min over all transversals; $\prod O$ is an instance). The conditional finish pipeline (Lemmas 7–9) is redundant with δ's certified post-stabilization machinery. No builder. Ranker: β loses to every live approach (Elo dropped to 1421, below γ).

### omega-induction-loaded (ε) — RETIRE
Concur with outliner. ω-only induction is DEAD (refuted $a_1=19549=113\cdot173$, $|P_{\ess}|=21$ depends on prime *sizes* not $\omega$; violates the NEVER rule). ε3 (smallest-missing-prime descent) folds into α's SPT — no standalone mechanism. Never built (no body file, `expanded=0`). No builder. Ranker: ε last in field (Elo 1310).

### transversal-single-cycle-finish (δ) — HOLD (not built this round)
Verified-milestone (conditional theorem, certified, computationally verified). It is a FINISH approach, not a wall-attacker; advancing it is premature until a wall-proof is certified. Correctly excluded from the build set. Stays at the top of the ranking (1672) as the reusable post-wall machinery.

## Diversity / single-gap-trap guard

The crash-step mechanisms are genuinely distinct:
1. **pstar** — Cov-completion: bounds CRASH primes $\subseteq P(a_1)$ via a bounded monotone subset; wall = smooth $2^k\cdot p$ forced. AVOIDS SPT.
2. **smooth** — smooth/rough-number density in the mtp-window: bounds ENTERING minimal's small prime (W1/W2 ⟹ SPT ⟹ GAP-1).
3. **α** — SPT (via W1 import) + crash-eviction for GAP-3 (TBD, forbidden from collapsing into Cov).
4. **γ** — mtp bounded via W1 import + honest GAP-3 (unique-connector, finite-state DEAD).

pstar is the field's only framing that survives a failure of SPT/W1 — the diversity guard is satisfied.

**Shared-gap risk (flagged, not fatal):** α, γ, and `smooth-window-crash` ALL depend on W1 (the mtp-witness-small-prime lemma). If W1 fails, GAP-1 stays open for all three simultaneously — they die together on GAP-1. This is the intentional convergent shared lemma (the outliner acknowledges it), and pstar is the independent survivor. The orchestrator should note: the field's GAP-1 attack is a single point of failure (W1) with one independent backup (pstar, which bypasses GAP-1 entirely).

**Partial shared-mechanism risk (flagged):** pstar's Lemma C and smooth's W2 BOTH invoke smooth-number reasoning at the crash step (pstar: smallest valid in window is $2^k\cdot p$; smooth: smallest valid below mtp-multiple is small-prime-divisible). If short-interval smooth-number density in bounded-$x$ regimes is unprovable, both could stall. They are NOT identical walls — pstar's is structurally constrained (specific $2^k\cdot p$ via the $\{2,p\}$ transversal, $p\in P(a_1)$), smooth's is a general density claim — so pstar's is the more constrained and likely easier. But the builder of pstar should prefer the structural $\{2,p\}$-transversal route over heavy Dickman density (consistent with the per-role NEVER: KB has no Dickman entry).

No two build-set approaches share the SAME wall via the SAME mechanism. Guard passes.

## Small-case sanity
- $a_1=15$: $\mathcal M=\{\{3,5\},\{2,3\},\{2,5\}\}$ (triangle), $T=8,L=30$. pstar's terminal self-blocking (Lemma D) with $P(a_1)=\{3,5\}$ gives family $\{\{3,5\},\{2,3\},\{2,5\}\}$ — matches (the 2-prime triangle is the $|P(a_1)|=2$ sub-case, self-blocking). ✓
- $a_1=175=5^2\cdot7$: mtp$=21=3\cdot7$ with 3 entering mid-evolution — confirms γ's "naive bound in $P(a_1)$ fails" and pstar's crash primes $\subseteq P(a_1)$ is a distinct claim (3 enters but is a crash prime only if $\{2,3\}\in\mathcal M$; here $P(a_1)=\{5,7\}$, so 3 is an entering free-rider, not a crash prime — consistent with pstar's scoping). ✓
- $\{2,97\}$ antichain: valid pairwise-intersecting family under SPT with $97\in P_{\ess}$ unbounded — confirms smooth/α/γ correctly do NOT claim SPT closes the wall. ✓

No contradictions with concrete instances.

## Ranking (head-to-head, anchored to last outcomes)
- δ (verified-milestone, certified) > α (advanced r2, freeze solved, GAP-S open) > pstar (new, sound skeleton, independent framing) > smooth (never-built, W1-owner) > γ (advanced, mtp certified but GAP-3 dead) > β (retired, subsumed) > ε (retired, never-built, ω-dead).
- δ and α anchor the top (certified progress); pstar slots above smooth because its framing survives a W1 failure (higher strategic value despite no certified progress); smooth above γ because smooth OWNS the shared W1 lemma while γ only imports it; β/ε sink as dead-ended. See `.ranking.json` for the Elo updates (δ 1672, α 1620, pstar 1530, smooth 1501, γ 1445, β 1421, ε 1310).

build set: pstar-core-straggler, smooth-window-crash, density-promotion-bound, bounded-gap-lcm-reduction
