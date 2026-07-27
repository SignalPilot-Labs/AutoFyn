# Outline review — IMO 2026 P6 (round 1)

Problem: greedy sequence $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$; prove $\exists T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

Shared wall (as framed by the field): prove the persistent/structural prime set $P$ is finite and the minimal-support family $\mathcal M$ stabilizes. Every naive route needs this; the field's value is in *diversifying the mechanism* for it (or sidestepping). I reviewed 5 approaches. No cuts (RETHINK) this round — all five are legitimate whole-claim attempts with genuinely distinct mechanisms and no two share a wall via the same mechanism (the single-gap trap is avoided). Two are held out of the build set for fixable gaps.

## Per-approach verdicts

### density-promotion-bound (α) — APPROVE
Whole-claim, attacks the wall head-on via Mertens/$\sum 1/p$ transversal-density. Real, concretely-articulated mechanism; the hard gap (step 3: density bound on the *transversal* set surviving correlated minimal-support constraints) is correctly identified and is the genuine crux, not a hidden circularity.

Concerns the builder must address (not fatal):
- **Monotonicity direction.** Promoting a new structural prime $p$ means some $a_i$ has support $\{p\}$ (or $p$ is the sole satisfier), so the valid set $R$ *shrinks* (a new "hit $p$" constraint appears). The argument needs "valid set stays dense enough to outbid new large primes *even as it shrinks*." The skeleton's phrasing "$\sum 1/p$ exceeds any single-prime cover once $S$ large" can read as if density grows with $|S|$ — it does not necessarily. The lower bound must be on $|R|/L$ *after* all promotions, shown to still beat the sparse-multiples of any would-be new prime $q$. This is the real sub-step; do not gloss it.
- **Step 2 induction base:** "support of every term contains a structural prime" — needs the contradiction-handling spelled out, as the outliner notes.
- **Step 6 single-cycle / period-sum $=L$:** shared with δ; import from δ rather than re-proving.

Build it this round.

### bertrand-dickson-eviction (β) — APPROVE (with risk flag)
Whole-claim, distinct mechanism (WQO/Dickson + Bertrand eviction, not analytic density). Dickson's lemma is a standard short hammer and gives a clean finish *once* the ambient prime set is bounded.

Key risk the builder must confront:
- **Eviction constant $C$ must be uniform / evolution-independent.** Dickson requires the ambient prime set fixed *before* application. The eviction lemma (step 1) must produce a single $C$ depending only on $a_1$ (or a universal bound), not one that drifts with the sequence's evolution. The sub-claim "current minimal supports are hittable by small primes already collected" risks circularity (it is essentially what we are proving). The builder should either (i) make the eviction inductive on a *rank* that is bounded a priori, or (ii) show Bertrand gives a composite transversal below $q$ using *only* primes already known persistent, breaking the circle. If the circle cannot be broken, this line is in trouble — but it is a real, distinct mechanism worth a builder this round.

Build it this round.

### bounded-gap-lcm-reduction (γ) — CHANGES REQUESTED (held from build set)
Whole-claim, genuinely dual target (bound gaps $d_n\le G$, then reduce mod $\operatorname{lcm}(1..G)$). BUT:
- **The central lemma (step 1) has no working mechanism.** The only candidate offered ($G=\prod_{p\mid a_1}p$, multiples of $a_1$ are always valid) is refuted by the outliner itself: multiples of $a_1$ hit only those $a_i$ sharing a factor with $a_1$, not all $a_i$. The outliner concedes "this gap is genuinely open."
- **Likely collapses to the wall.** The outliner flags the real danger: in the periodic regime gaps are $\le L$, so "bounded gaps" is essentially equivalent to "$L$ finite" — proving syndeticity of the valid set almost certainly routes back through finiteness of $P$. If so this approach does not sidestep the wall; it renames it.

Registered (it is a valid, distinct population member — not a cut), but **excluded from the build set**. It needs a real, independent mechanism for the bounded-gap lemma before it earns builder time. Outliner/next round: either supply a concrete syndeticity argument not reducing to $P$ finite, or reclassify γ as a corollary of α/β.

### transversal-single-cycle-finish (δ) — APPROVE
Whole-claim (assumes $\mathcal M$ stabilizes, leaves that as an explicit gap, proves everything else). This is the right *specialty* approach: it isolates the distinctive hard step **every** route needs but none other names — the single-cycle / period-sum-$=L$ lemma — plus it produces certified-importable machinery (free-rider lemma, squarefree-$L$, CRT residue set $R$, deterministic greedy map $\varphi$).

Concerns the builder must address:
- **Single-cycle lemma mechanism is currently insufficient.** The outliner correctly notes "pairwise-intersecting $\Rightarrow$ connected cyclic order is false in general" (two intersecting clusters with no cross-bridge). The builder must find the *extra* ingredient from the greedy's smallest-first rule that forces cross-cluster bridges, or exhibit why the actual $\mathcal M$ families arising here cannot split. This is the distinctive gap; do not paper over it.
- **Transient absorption:** data suggests transient length 0 (corpus explorer: holds from $n=1$ in 8/8 cases), but "data suggests" is not a proof. Either prove transient 0 or handle by redefining $T,L$ to start after the transient (the problem statement allows "for all $n$" only if transient is 0; otherwise the theorem's quantifier needs the absorbed version — check carefully).

Build it this round. Its certified lemmas (free-rider, squarefree-$L$) are explicitly importable by α and β, so building δ in parallel de-risks the field.

### omega-induction-loaded (ε) — CHANGES REQUESTED (held from build set)
Genuinely different framing (structural induction on $\omega(a_1)$). BUT:
- **Promotion-size lemma is circular** (the outliner admits "Circular — needs care"). Bounding $|S|$ by induction on $k$ requires showing promotions only add bounded many primes, which is the wall in disguise.
- **The loaded conjecture $|S|\le g(\omega(a_1))$ is empirical and falsifiable.** My quick computational check on $\omega=2$ starts ($pq$, primes $\le 73$, 120 terms) found $|S|$ reaching 5 (e.g. $a_1=187=11\cdot17\to S=\{2,3,7,11,17\}$, $a_1=221\to |S|=5$). So $g(2)\ge 5$; whether it stays bounded for *all* $pq$ (incl. very large $q$) is unknown, and the greedy-gap explorer noted $a_1=385$ ($\omega=3$) doesn't settle within 2000 terms — large-$\omega$ behavior is uncharted. A single counterexample kills the approach.

Registered (distinct framing, testable), but **excluded from the build set**. Recommendation (matches outliner): run a broader computational sweep on $\omega=2$ starts ($pq$, primes up to ~200, longer runs) and a few $\omega=3$ starts before promoting ε to the build set. If $|S|$ stays bounded, promote next round; if it grows, drop.

## Diversity assessment (single-gap trap check)

The field does NOT collapse to one mechanism. α (analytic density), β (WQO+Bertrand), γ (dual bounded-gap), δ (leaves wall, attacks single-cycle), ε (structural induction) attack the wall — or sidestep/reframe it — via five different mechanisms. Caveat for the orchestrator: α, β, δ, ε all *pass through* the conclusion "$\mathcal M$ stabilizes" (δ/ε leave it as a gap, α/β attack it). γ is the only one that potentially avoids it, and γ is the weakest (likely collapses back). So **4 of 5 approaches share the wall's *conclusion* even though they diversify its *mechanism*** — acceptable diversity, but if α and β both stall next round, the field is effectively stuck on one wall and the orchestrator should demand a genuinely different framing (e.g. a direct construction of $T,L$ from $\mathcal M$ without finite-state periodicity, or a density-bound that does not go through "structural prime" at all).

## Ranking (head-to-head, cold-start field)

All five are new (Elo 1500). I anchored comparisons on framing strength, mechanism closeability, and reusability of certified output, not on sibling-only separation.

- δ > α: δ produces certified reusable machinery (free-rider, squarefree-$L$, residue map) regardless of the wall; α's ceiling is higher (it can fell the wall) but its density gap is the hardest open problem in the field. Round-1 productivity favors δ slightly.
- α > β: α's mechanism is more concretely articulated and the gap more sharply identified; β's eviction-constant circularity is more severe.
- β > ε: β has a real mechanism aimed at the wall; ε is speculative/circular.
- ε > γ: ε's framing is genuinely distinct and the conjecture is testable; γ's central lemma has *no* mechanism and likely collapses to the wall.
- Reinforcing (transitive): δ > γ, δ > ε, α > γ, α > ε, β > γ.

Result: δ 1545, α 1530, β 1514, ε 1471, γ 1440.

## Build set (round 1)

Three builders, diverse (two wall-mechanisms + the finish specialty that supplies importable lemmas to both):

build set: density-promotion-bound, bertrand-dickson-eviction, transversal-single-cycle-finish
