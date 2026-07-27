# Outline review — IMO 2026 P6 (round 2)

Problem: greedy sequence $a_{n+1}=\min\{m>a_n:\gcd(m,a_i)>1\ \forall i\le n\}$; prove $\exists\,T,L>0$ with $a_{n+T}=a_n+L$ for all $n$.

Shared wall: **finiteness of $\mathcal M=\min\{P(a_i):i\ge1\}$** (equiv. $P_{\rm ess}$ finite / $\mathcal M_n$ stabilizes). The post-stabilization machinery (δ) is a verified milestone; nothing else needs re-proving there. The round-2 explorers split the wall into two termination regimes — **Freeze** (common prime → AP→$p^k$→singleton-freeze, certified engine) and **Saturated** (self-blocking fixed point) — both verified across ~150 seeds, neither subsuming the other. A complete wall-proof must handle both.

No new slugs to register (all five — α, β, γ, δ, ε — are already in the population from round 1). No copy/branch requested by the outliner. I rank the existing field and emit the build set.

## Per-approach verdicts

### α `density-promotion-bound` — APPROVE
REVISE: the dead density-monotonicity / LLL / Mertens frame is dropped; re-planned around the regime split (freeze OR saturated). This is a sound, genuinely whole-claim framing.

- **Freeze branch (F) is near-certified.** The chain common-prime-$p$ → $\{p\}$ transversal → greedy locks to diff $p$ → AP $a_n=p(c+n-1)$ → hits $p^k$ → singleton-freeze (certified lemma) is clean. I verified computationally that the F-lock gap concern (an entering small prime $q<p$ breaking the lock) is **empirically vacuous**: for $a_1\in\{273,413,893\}$ NO prime $q<p$ enters $P_{\rm ess}$ before the freeze. The reason is structural — once $p$ is common, any new minimal avoiding $p$ must hit every existing support via non-$p$ primes, all of which are $>p$ (since $p$ is $a_1$'s smallest factor and any entering essential prime must hit existing supports, forcing it $>p$). So non-$p$ transversals have product $>p=\mathrm{mtp}$, and the greedy prefers the multiple of $p$ within $p$. **GAP-F-lock is real but closeable** — the builder should prove the min-non-$p$-transversal product stays $>p$ via this mechanism (all non-$p$ structural primes $>p$); do NOT just cite empirical seeds.
- **Saturated branch (S) is the genuine wall (GAP-S).** The self-blocking fixed-point *criterion* is sound (saturation ⟹ no avoiding transversal ⟹ no promotion ⟹ stabilize — a clean structural argument). BUT the hard sub-claim "saturation is REACHED, not bypassed" is under-articulated: the only mechanism offered is "pigeonhole/size bound on the structural prime set capping $|\mathcal M|$," which is exactly the wall restated, not proved. The outline honestly flags this as "the single hardest gap in the field." Acceptable — it is the right framing for the hardest piece, and naming it honestly is the correct posture.
- **GAP-split** relies on GAP-S; fine.
- **Case coverage:** (F) common prime, (S) no common prime — exhaustive by construction. Sub-case of (S): $a_1=pq$ both odd ($K_3$). Covered.

Concerns the builder must address (not fatal):
- Do NOT assume $|\mathcal M|\le7$ without proof (empirical only).
- The regime is determined by whether $p$ REMAINS common throughout, not just at step 1 ($a_1=15$ saturates, $a_1=21$ freezes, both have smallest factor 3) — the split must be on the dynamic, not on $p$ alone.
- GAP-F-lock: prove the min-non-$p$-transversal product stays $>p$ via the "all non-$p$ structural primes $>p$" mechanism, handling entering primes $q<p$ (show they cannot enter because entering requires hitting existing supports, which forces primes $>p$).

Build it this round — the freeze branch is mostly certifiable and the saturated branch is the right attack on the wall.

### β `bertrand-dickson-eviction` — CHANGES REQUESTED (held from build set)
REVISE: Bertrand eviction dead; replaced by permanent-small-transversal persistence + mtp monovariant. The mtp machinery (steps 1, 3) is PROVABLE (one-liner from Lemma 3 + sharpened gap bound). BUT the crux has a flawed mechanism.

- **GAP-PERMANENT mechanism is a non-sequitur.** The outline argues: "multiples of $\prod T^*$ are valid and dense (within $G$), so $a_{n+1}$ is close to a multiple of $\prod T^*$ — but 'close to' does NOT mean 'divisible by.'" The outline itself admits persistence is NOT structural (two transversals need not intersect — verified) and NOT automatic. The mechanism offered ("close to a multiple") does NOT imply the greedy's pick carries a $T^*$ prime. The greedy picks the smallest VALID $m>a_n$; valid $m$ need only carry SOME transversal $T'$, not $T^*$ specifically. So persistence of $T^*$ requires proving every new minimal $M'=P(a_{n+1})$ intersects $T^*$ — i.e., the greedy's specific arithmetic pick always carries a $T^*$ prime. This is a real, hard, named crux, but the mechanism as stated does not yield it; it is currently a conjecture without a working proof handle.
- **Single-gap trap with γ (SEVERE).** β and γ share BOTH load-bearing gaps: GAP-PERMANENT (β) = GAP-1 (γ), and GAP-FINITE-STATE (β) = GAP-3 (γ). The outline itself flags both. β's step 4 routes through γ's finite-state template (the direct route is admitted circular). So β is essentially γ with an extra conjecture (permanent-transversal) layered on. If γ's gaps fail, β dies with it.

Verdict: CHANGES REQUESTED. The mtp monovariant is a real provable asset, but the permanent-transversal crux has no working mechanism and the approach shares both its gaps with γ. **Hold β from the build set this round.** Require the outliner/builder to diversify from γ before building: either (i) prove persistence via a real mechanism (e.g., the greedy's smallest-first pick IS forced to be a multiple of $\prod T^*$ because all smaller valid numbers are ruled out by the transversal structure — which reduces to α's F-lock mechanism, so check for overlap), or (ii) find a direct bounded-gap→finiteness argument INDEPENDENT of γ's finite-state template. If neither, β should be folded into γ.

### γ `bounded-gap-lcm-reduction` — APPROVE
NEW (build from scratch; currently empty held slug). Genuinely different framing: mtp monovariant + aimo-0678 finite-state template, NO regime split, NO density, NO Bertrand. Far from α (casework) and ε (s_n descent).

- **mtp-monotone (step 1) and sharpened-gap-bound (step 2) are PROVABLE** — one-liners from certified Lemma 3 (refinement shrinks transversals; min over smaller set grows) and the witness-transversal argument. These are certified-grade partial results ready to ship.
- **GAP-1 (mtp bounded):** honestly flagged, with the $2\,p_{\max}(a_1)$ dead end recorded ($a_1=175$). The outline offers TWO candidate mechanisms: permanent-transversal (shared with β) OR pigeonhole on small primes. The pigeonhole route (only $\pi(G)$ primes $\le G$ can appear in a witness transversal of product $\le G$, forcing an $|\mathcal M|$-vs-$G$ tradeoff) is genuinely independent of β and worth developing.
- **GAP-3 (bounded-gap → finiteness):** the HONEST OBSTRUCTION is excellent and correctly identifies the circularity: bounded gaps alone do NOT forbid a large essential prime $q>G$ being a unique connector between two minimals whose introducing terms are value-distance $\ge q$ apart; the aimo-0678 template had a CLOSED-FORM recurrence, but here the greedy depends on $\mathcal M_n$ (history), so "finite state determines next step" needs a real argument, not a template invocation. This is the sharpest articulation of the second sub-gap in the field.

Concerns the builder must address:
- **Diversify GAP-1 from β:** use the pigeonhole-on-small-primes route, NOT the permanent-transversal route, so γ and β don't share the same crux and die together.
- **GAP-3 is the harder of the two** — do not hand-wave "bounded gaps forbid large primes"; the honest obstruction (large $q$ as unique connector) must be confronted with a real finite-state argument or a novel bounded-gap→finiteness mechanism.

Build it this round — first build from scratch, genuinely new framing, two honest sub-gaps with named mechanisms.

### ε `omega-induction-loaded` — CHANGES REQUESTED (held from build set)
REVISE: ε1 (ω-only) dead; ε3 (smallest-missing-prime $s_n$ descent) is the re-plan. The $s_n$ non-decreasing lemma (step 1) is PROVABLE (essential primes are permanent). BUT ε3 is **not clearly a standalone whole-claim approach** — the outline itself admits this and recommends RETHINK/fold if GAP-ε-free-rider can't close independently.

- **GAP-ε-main ($s_n$ strictly increases) mechanism is conjectural.** "The greedy's dynamics force the smallest available prime $s$ to enter a new minimal support, exhausting avoiding transversals that avoid $s$" — but the greedy picks the smallest VALID $m>a_n$, which need not be a multiple of $s$. The mechanism does not yield the claim; it is a conjecture. No proof handle offered.
- **GAP-ε-free-rider standalone path is circular or requires import.** The outline's option (a) "bound the NUMBER of between-increase promotions" is circular with GAP-ε-main (both assert "finitely many promotions before $s_n$ rises"). Option (b) imports α's saturation result or γ's mtp bound — making ε a sub-lemma of α/γ, NOT a rival whole-claim approach. The CLAUDE.md rule "each slug is a rival complete attempt" is violated if ε folds.
- **Single-gap trap with α (saturated branch).** ε's step 3 (self-blocking threshold) and α's GAP-S (reach saturation) share the SAME terminal wall: "small primes flood in and force saturation." If that sub-claim is unprovable, both α's saturated branch and ε die together. The route differs (ε: $s_n$ descent; α: casework + pigeonhole on $|\mathcal M|$), but the wall is shared.
- ε's GAP-ε-free-rider may also import γ's mtp bound — another shared wall with γ.

Verdict: CHANGES REQUESTED. ε3 is genuinely different (descent on a well-ordered natural number) and the $s_n$ non-decreasing lemma is real, but the strict-increase mechanism is conjectural and the standalone path is circular/imports. **Hold ε from the build set this round.** Require the outliner to either (i) supply a real mechanism for $s_n$ strict increase (not "the greedy forces $s$") AND a non-circular standalone path for GAP-ε-free-rider, or (ii) RETHINK — retire ε and fold the $s_n$ descent into α's saturated branch as a sub-lemma. ε3 is at risk of being a piece of α, not a rival.

### δ `transversal-single-cycle-finish` — APPROVE (held from build set)
ADVANCE: parameterize the conditional theorem to import a wall-proof. Sound, non-circular (δ assumes $\mathcal M$ finite; the wall-proof proves it). BUT the advance is premature this round — no wall-proof is certified yet, so the "import interface" has nothing to import. Low value this round; it's a writing exercise. δ stays the certified absorber; advance it when a wall-proof lands (freeze-branch certification from α is the nearest candidate).

Hold δ from the build set this round. Its certified lemmas remain importable by α/γ; no re-proving needed.

## Diversity assessment (single-gap trap check)

The field has partially collapsed into two clusters:
- **Saturation cluster:** α (saturated branch, GAP-S) and ε (self-blocking threshold) BOTH need "small primes flood in and force saturation." Different routes (casework vs $s_n$ descent) but shared wall. **Flagged** — ε held this round; if α's saturated branch stalls next round, demand ε be retired/folded, and the outliner should open a genuinely different framing (not saturation-based).
- **mtp/finite-state cluster:** β and γ share BOTH load-bearing gaps (GAP-1/GAP-PERMANENT and GAP-3/GAP-FINITE-STATE). β is essentially γ + a conjecture. **Severe single-gap trap.** β held this round; require β to diversify (direct finiteness argument, not γ's template) or fold into γ.

The genuinely far-apart live wall-attacks this round are **α (regime casework: freeze branch near-certified + saturated wall)** and **γ (mtp monovariant + finite-state template, two sub-gaps)**. They share NO wall mechanism (α's wall = reach saturation; γ's wall = mtp bounded + bounded-gap→finiteness). δ is the certified absorber. Building α + γ makes real progress on the wall from two non-overlapping directions and avoids the single-gap trap.

ε (s_n descent) and β (permanent-transversal) are held to force diversification from α and γ respectively; both are at risk of folding if they cannot close their crux gaps independently.

## Ranking (head-to-head, anchored to last outcomes)

Anchored to last recorded outcomes: δ = verified-milestone (certified); α, β = partial (wall open); γ, ε = held/cold-start (no outcome). New signal this round: α revised (freeze branch near-certified, improved); β revised (mtp provable but permanent-transversal crux a non-sequitur, single-gap trap with γ); γ reframed cleaner with two honest sub-gaps (genuinely different); ε3 re-planned but at risk of folding (circular/imports, conjectural strict-increase).

- δ > α: δ certified; α's freeze branch near-certified but saturated wall open. δ still ahead.
- δ > γ, δ > β, δ > ε: δ certified milestone; the others have open walls.
- α > γ: α has a near-certified freeze branch (real progress); γ is cold-start with two open sub-gaps.
- α > β: α's freeze branch is certified-grade; β's permanent-transversal crux is a non-sequitur and shares both gaps with γ.
- α > ε: α's freeze branch near-certified; ε3 conjectural and at risk of folding.
- γ ≈ β (draw): they share both load-bearing gaps; β adds a conjecture (permanent-transversal), γ has cleaner articulation and the aimo-0678 template. Neither clearly ahead — draw.
- γ > ε: γ has a provable asset (mtp monovariant) and honest sub-gaps; ε's strict-increase is conjectural and the standalone path circular.
- β > ε: β has a provable asset (mtp monovariant); ε is mostly conjecture.

Result: δ > α > γ ≈ β > ε.

## Build set (round 2)

Two builders, both attacking the wall from non-overlapping directions (no single-gap trap), one near-certified sub-chain (α freeze branch) + one genuinely new framing built out for the first time (γ):

build set: density-promotion-bound, bounded-gap-lcm-reduction
