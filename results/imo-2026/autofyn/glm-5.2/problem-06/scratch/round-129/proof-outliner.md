# proof-outliner field — IMO 2026 P6, round 129

The wall (only open piece): **SATURATED regime — prove $\mathcal M_n$ stabilizes / only finitely many primes enter minimal supports.** Freeze regime SOLVED (imported, not re-proved). Case split (F)/(S) exhaustive. The field has CONVERGED on "bound the entering primes by value / SPT" (real convergence, confirmed by both explorers); this round's diversity lives at the CRASH step (SPT-density vs Cov-monovariant vs analytic smooth-density), NOT three flavors of SPT. The linchpin premise "promotions are strict-beats" is REFUTED (170/344 are equality-promotions) — every approach that touched it is corrected.

## imo-2026-06

### pstar-core-straggler: new
Target: the whole eventual-arithmetic claim (freeze branch imported; saturated branch via Cov-monovariant + crash-into-core).
Technique: structural — restricted-common-prime core collapse + bounded Cov monovariant + smooth-number crash-into-core. Distinct from SPT: bounds CRASH primes $\subseteq P(a_1)$ (finite by construction), NOT entering primes; entering large primes are evicted free-riders.
Skeleton:
  1. Trivial collapses (even / prime power) → `singleton-freeze` (import). Assume $a_1$ odd, $\ge2$ prime factors. Case split (F)/(S) (`common-primes-bounded`). — by imported lemmas
  2. (F) freeze: `freeze-lock`+AP$\to p^k$+`singleton-freeze` (import). — by imported lemmas
  3. (S) Lemma A: $2$ enters at $a_2$ (odd $a_1$) and stays common to the core $\mathcal M_n^*=\{M\in\mathcal M_n:2\in M\}$ — by refinement obstruction (singleton-$\{2\}$/$\{p\}$ would be freeze events, excluded in (S)). [GAP]
  4. Lemma B: $\mathrm{Cov}(\mathcal M_n)=\{p\in P(a_1):\{2,p\}\in\mathcal M_n\}$ monotone $\subseteq P(a_1)$ — by KB *Invariants & monovariants*; persistence sub-step: $\{2,p\}$ has no proper nonempty subset but $\{2\},\{p\}$ (freeze events). [GAP: persistence — NOT the false free-rider universality]
  5. Lemma C (THE WALL): if $\mathrm{Cov}\neq P(a_1)$, a crash $\{2,p\}$ ($p\in P(a_1)\setminus\mathrm{Cov}$) eventually arrives — by $2$ common to core + $p$ in straggler ⟹ $\{2,p\}$ transversal ⟹ multiples of $2p$ valid ⟹ smallest $\le a_n+2p\le a_n+\mathrm{mtp}$ (import `mtp-monovariant-and-gap-bound`) ⟹ $2^k\cdot p$ forced as greedy pick (smooth-number event). [HARD GAP, value-dependent]
  6. Lemma D: $\mathrm{Cov}=P(a_1)$ ⟹ family $=\{P(a_1)\}\cup\{\{2,p\}:p\in P(a_1)\}$ self-blocking (transversal uses 2 ⟹ misses straggler ⟹ also hits a straggler-prime $p$ ⟹ $\{2,p\}\subseteq$ transversal; or avoids 2 ⟹ contains all $P(a_1)=$ straggler) — by `Sat-criterion` ⟹ frozen ⟹ `post-stabilization-theorem`. [structural; sub-case $S=P(a_1)$ vs refinement CONJECTURE 6/6]
  7. Conclusion: (F) solved, (S) conditional on Lemma C.
Key lemmas (claim + mechanism):
  - Lemma B (Cov monovariant) — because $\{2,p\}$'s only proper subsets are $\{2\},\{p\}$, both freeze events excluded in (S), so $\{2,p\}$ persists; $\mathrm{Cov}\subseteq P(a_1)$ is a bounded monotone integer-quantity.
  - Lemma C (crash inevitability) — because $2$ common to core + $p$ in straggler makes $\{2,p\}$ a transversal, so $2p$-multiples are valid within the mtp-window, and the smallest is the smooth $2^k\cdot p$.
  - Lemma D (self-blocking) — because any transversal either contains $\{2,p\}$ for some $p$ (if it uses 2) or contains the whole straggler $P(a_1)$ (if it avoids 2).
Open gaps: Lemma A (2-core persistence), Lemma B sub-step ($\{2,p\}$ persistence — refinement obstruction), Lemma C (smooth-number crash forced — the wall), Lemma D sub-case ($S=P(a_1)$).
Cases: even/prime-power (freeze); odd $\ge2$ factors regime (F) (freeze, import); odd $\ge2$ factors regime (S) (Cov route); 2-prime saturated (triangle terminal — verify separately).
Watch out for: free-rider universality is FALSE ($a_1=15$ step 3) — use only the crash-refines-large-primes subset relation; $|M|\le7$ REFUTED ($a_1=5005$ $|M|=31$); Dickson/multiset WQO fails (incomparable adds grow it); crash primes $\subseteq P(a_1)$ but crash TERMS can be large (value-dependent).

### smooth-window-crash: build (registered, was empty — now has a real skeleton)
Target: prove SPT / mtp bounded (closes GAP-1); HONESTLY PARTIAL — does NOT alone close the wall ($\{2,97\}$ obstruction under SPT).
Technique: analytic — mtp-witness-small-prime structural lemma (W1) + short-interval smooth/rough-number density (W2). Distinct at the crash step: density of smooth numbers vs the greedy's pick.
Skeleton:
  1. Import `mtp-monovariant-and-gap-bound` (window $(a_n,a_n+\mathrm{mtp}]$, mtp-multiple valid). Trivial collapses + case split (F)/(S) (import). — by imported lemmas
  2. Lemma W1 (witness carries small prime, CONJECTURE 0 viol 26 seeds): mtp-witness $T^*$ of $\mathcal M_n$ always contains a prime $\le p^*$. [GAP — direct combinatorial proof attempted; cheap kill NOT a formality (constructible counterfamilies); folds into SPT if it fails]
  3. Corollary (equality-case trivial): if $a_{n+1}=$ mtp-multiple (170/344 promotions + all non-promotions), $P(a_{n+1})\supseteq T^*$ ⟹ small-prime-divisible. — by W1. [Corrects the strict-beat linchpin: $T^*$ is a transversal not a member, so ⊇T* does not dominate]
  4. Lemma W2 (strict-beat smooth-density, HARD): smallest valid in $(a_n,\text{mtp-multiple})$ carries a prime $\le p^*$ — by smooth-number density (multiples of 2 density 1/2, …) vs $p^*$-rough sparsity in short intervals. [HARD GAP — Dickman/Brun-sieve, NOT in KB, asymptotic vs bounded-$x$ tension]
  5. Lemma W3 (SPT): W1+W2 ⟹ every entering minimal has $\min\le p^*$ ⟹ $\mathrm{mtp}\le\prod_{p\le p^*}p$ bounded ⟹ GAP-1 CLOSED. — by KB *Invariants & monovariants*
  6. Honest scope: SPT closes GAP-1 only; $\{2,97\}$ is a valid minimal under SPT with $97\in P_{\ess}$ unbounded ⟹ GAP-3/wall NOT closed. Needs crash-eviction partner (owned by `pstar-core-straggler` / α). — by the $\{2,97\}$ counterfamily
  7. Finish: conditional on the wall (NOT supplied here) → `post-stabilization-theorem` (import).
Key lemmas:
  - W1 (witness small prime) — because $T^*$ avoiding all small primes has $\prod T^*\ge\mathrm{nextprime}(p^*)\cdot\ldots$, but this does NOT exceed $\prod_{p\le p^*}p$ automatically (genuinely tight, not a formality).
  - W2 (strict-beat smooth density) — because small-prime multiples are denser than $p^*$-rough numbers in short intervals.
Open gaps: W1, W2 (the wall of THIS approach), GAP-3 (honestly open, owned elsewhere).
Cases: equality-promotions (170/344, trivial via W1) vs strict-beats (174/344, W2); non-promotions (trivial).
Watch out for: strict-beat linchpin REFUTED (170/344 equality) — handle both cases; "2 always in witness" FALSE ($a_1=175$, 2 in T* only 2/81) — witness small prime varies; SPT does NOT close the wall; KB has no Dickman entry — cite externally + re-prove, or find elementary substitute.

### density-promotion-bound (α): advance
Target: the whole claim (freeze branch SOLVED; saturated branch GAP-S). STAYS on the SPT route (does NOT adopt the p*-core decomposition — that is `pstar-core-straggler`'s distinct framing; adopting it would duplicate and re-form the single-gap trap).
Skeleton (additions to the existing file):
  1. Freeze branch (F): SOLVED (import, unchanged). — by `freeze-lock`+`singleton-freeze`
  2. (S) GAP-1: ADOPT the mtp-witness-small-prime lemma (W1, owned by `smooth-window-crash`) once certified → import → $\mathrm{mtp}\le\prod_{p\le p^*}p$ bounded → GAP-1 closed. — by importing W1 + KB *Invariants & monovariants*
  3. (S) Fix the strict-beat linchpin: handle equality-promotions (170/344) trivially via W1 (T* ⊆ P(a_{n+1}), small prime inherited for free) AND strict-beats (174/344) via W2 (smooth-density, GAP). Do NOT build on "all promotions are strict-beats" — REFUTED. — by the equality/strict-beat split
  4. (S) GAP-3 articulation: SPT bounds mtp but NOT $P_{\ess}$ — the $\{2,97\}$ antichain is a valid pairwise-intersecting family under SPT with unbounded $P_{\ess}$. HONEST: GAP-3 remains open under SPT alone. The pigeonhole-on-small-primes route (α's §5c route 2) hits this same $\{2,97\}$ wall — record it; do NOT claim SPT alone closes GAP-S. — by the $\{2,97\}$ counterfamily
  5. (S) Sketch the crash-eviction partner for GAP-3 only if it does NOT collapse into `pstar-core-straggler`'s Cov framing (to preserve diversity); otherwise flag GAP-3 as the open piece awaiting a partner. — by refinement subset relation
  6. Finish: `post-stabilization-theorem` (import, conditional on the wall).
Key lemmas:
  - GAP-1 closure via W1 — because the mtp-witness carries a small prime, so $S=P_{\ess}\cap\{p\le p^*\}$ is a transversal with bounded product.
  - GAP-3 obstruction — because $\{\{2,q\}:q>p^*\}$ is an infinite pairwise-intersecting antichain all satisfying SPT, so SPT $\not\Rightarrow$ $P_{\ess}$ finite.
Open gaps: GAP-3 (the wall under SPT — the $\{2,97\}$ obstruction; needs a crash-eviction or finite-state partner).
Watch out for: do NOT adopt p*-core (duplicates `pstar-core-straggler`); fix the strict-beat premise; SPT $\ne$ wall.

### bounded-gap-lcm-reduction (γ): advance
Target: the whole claim (mtp monovariant certified; GAP-1 + GAP-3 the two sub-gaps).
Skeleton (additions to the existing file):
  1. mtp monovariant + global gap bound: CERTIFIED (import, unchanged). — by `mtp-monovariant-and-gap-bound`
  2. GAP-1: IMPORT the mtp-witness-small-prime lemma (W1, owned by `smooth-window-crash`) → $\mathrm{mtp}\le\prod_{p\le p^*}p$ bounded → GAP-1 CLOSED. — by importing W1 + KB *Invariants & monovariants*
  3. GAP-3: HOLD — the `aimo-0678` finite-state lcm-reduction is DEAD for bypassing (entering primes unbounded, confirmed round-3 finite-state lens); the unique-connector obstruction stands (the free-rider universality that would refute it is FALSE — $a_1=15$ step 3 counterexample). Honest: GAP-3 open. — by the dead finite-state route + the standing unique-connector obstruction
  4. Finish: conditional on GAP-3 (not supplied here) → `post-stabilization-theorem` (import).
Key lemmas:
  - GAP-1 closure — because W1 ⟹ SPT ⟹ bounded mtp.
  - GAP-3 obstruction — because bounded gaps admit a large fresh prime $q>G$ as unique connector (many small-gap terms in between all hit by $M'\setminus\{q\}$); the free-rider property that would refute it fails at crash events.
Open gaps: GAP-3 (the finite-state route dead; the unique-connector obstruction stands; needs a genuinely new mechanism, possibly the Cov-monovariant from `pstar-core-straggler`).
Watch out for: do NOT claim the free-rider property is universal (FALSE); the finite-state route is dead; GAP-1 and GAP-3 are independent (closing GAP-1 does not close GAP-3).

### omega-induction-loaded (ε): retire
Verdict: RETIRE. ω-only induction is DEAD (refuted $a_1=19549=113\cdot173$, $|P_{\ess}|=21$ depends on prime sizes not $\omega$). ε3 (smallest-missing-prime descent) folds into α's SPT — no standalone mechanism. Never built (no body file). The ranker entry should be retired; no builder dispatched.

### bertrand-dickson-eviction (β): retire (fold)
Verdict: RETIRE. Doubly broken: (1) uses the FALSE free-rider universality; (2) circular $a_n$ bound (bounds $a_n$ by termination). Bertrand eviction DEAD (no dyadic interval forced). Its one certified asset (`gap-bound-at-promotion`, Lemma 5 cofactor arithmetic: $O=P(a_i)\cap P_{\ess,i-1}$ is a transversal, gap $\le\prod O$) is SUBSUMED by γ's `mtp-monovariant-and-gap-bound` (mtp is the min over all transversals; $\prod O$ is an instance). Fold the cofactor intuition into the shared mtp lemma (already done). The ranker entry should be retired; no builder dispatched.

---

## Diversity / single-gap-trap guard
- **GAP-1 (mtp bounded via SPT / witness-small-prime)**: CONVERGENT shared lemma, intentionally shared by α, γ, `smooth-window-crash`. If SPT is false, these three die together — but they are NOT the whole field.
- **The wall (GAP-S / GAP-3)**: attacked by THREE genuinely different mechanisms:
  1. `pstar-core-straggler` — Cov monovariant bounds CRASH primes $\subseteq P(a_1)$; wall = smooth-number crash inevitability (Lemma C). AVOIDS SPT entirely.
  2. α — SPT + crash-eviction (if it does not collapse into pstar) / honest $\{2,97\}$ obstruction.
  3. γ — finite-state lcm-reduction (dead) / honest unique-connector obstruction.
- `pstar-core-straggler` is the genuinely-different framing the field needs: it does not bound entering primes by value at all; its wall (Lemma C) is a different hard step from SPT. If SPT fails, `pstar-core-straggler` survives.
- The hard steps are genuinely distinct: SPT (every minimal carries a small prime) vs Cov-completion (crash primes $\subseteq P(a_1)$) vs smooth-density (smallest valid in window is small-prime-divisible). Three different crash mechanisms.

build set: pstar-core-straggler, smooth-window-crash, density-promotion-bound, bounded-gap-lcm-reduction
