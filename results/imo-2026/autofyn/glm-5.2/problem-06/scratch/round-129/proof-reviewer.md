# proof-reviewer — IMO 2026 P6, round 129

Reviewed all four built approaches adversarially. Each judged on its own. All four are **partial** — the wall (saturated-regime termination / finiteness of $\mathcal M$) remains open in every approach. None is solved; none is fatally broken. The field-wide W1-correction (W1 does NOT close GAP-1; the bound needs full SPT = W1∧W2; the $\{2,q\}$ antichain shows SPT does NOT bound $P_{\mathrm{ess}}$) was made **honestly by all four** — no residual "W1 ⟹ mtp bounded" overclaim survives in any file.

## Computational verification performed (numpy/sympy)

- **pstar Lemma C-ref** (a1=35): terminal $\mathcal M=\{\{2,3,7\},\{2,5\},\{3,5\},\{5,7\}\}$ confirmed; self-blocking confirmed; $\mathrm{Cov}=\{5\}\subsetneq P(a_1)=\{5,7\}$ confirmed. (a1=175: terminal $\{\{5,7\},\{2,3,5\},\{2,13,7\},\{3,7\},\{13,3,5\}\}$, $\mathrm{Cov}=\emptyset\subsetneq P(a_1)$, confirmed.) The self-refutation is correct and honestly narrowed.
- **pstar Lemma B (Cov monovariant)**: Cov monotone non-decreasing, 0 violations on 175 (and 35); $\{2,p\}$-persistence (once entered, stays) 0 violations; crash primes $\subseteq P(a_1)$. The refinement obstruction ($\{2,p\}$'s only proper nonempty subsets are $\{2\},\{p\}$; both singletons ⟹ `singleton-freeze` ⟹ regime (F), excluded in (S)) is airtight structurally.
- **pstar §5.3 straggler⊇Cov**: the minimals are themselves members of $\mathcal F_n$ (each $M\in\mathcal M_n$ equals some $P(a_k)$), so `pairwise-intersection` of the terms directly gives pairwise-intersection of the minimals; hence a straggler $S\not\ni2$ meets $\{2,p\}$ forcing $p\in S$. Verified 0 violations on 8 seeds. (Not load-bearing for Lemma B, correctly noted.)
- **pstar GAP-A** (core nonempty): core empty only at $n=1$ (before 2 enters) on 175; nonempty for $n\ge2$. Honest "unproved, not load-bearing" — correct.
- **smooth/α equality-promotion linchpin refutation**: at equality-promotions, the mtp-witness $T^*$ is a transversal of $\mathcal M_n$ but NOT a member of $\mathcal M_n$ (verified on seeds 15,35,175,429); $P(a_{n+1})\supseteq T^*$ does NOT dominate. So equality-promotions ARE genuine new minimals. The refuted round-3 premise is correctly fixed; both cases (equality + strict-beat) are now handled. (The "170/344" exact count is seed/window-dependent; the qualitative fact holds.)
- **γ Prop 2.2 (W1 does not bound the product)**: $T^*=\{5,97\}$, $p^*=5$: satisfies W1 ($5\le5$) yet product $485>30=\mathrm{primorial}(5)$. Confirmed. This is the key field-correcting verdict.
- **{2,q} GAP-3 obstruction** (α Lemma 9 / smooth §7): $\{\{2,q\}:q>p^*\}$ pairwise-intersecting, antichain, SPT-true ($\min=2\le p^*$), unbounded $P_{\mathrm{ess}}$. Confirmed. SPT closes GAP-1 (mtp≤primorial) but not GAP-3 — all approaches state this correctly.
- **No circular imports**: every imported lemma (`pairwise-intersection`, `freeze-lock`, `singleton-freeze`, `common-primes-bounded`, `mtp-monovariant-and-gap-bound`, `Sat-criterion`) is unconditional; `post-stabilization-theorem` is conditional-on-$\mathcal M$-finite and used only in the finish (not to prove the wall). No approach proves the wall by importing a lemma that itself requires the wall.

## Per-approach verdicts

### pstar-core-straggler — CHANGES REQUESTED (partial, ADVANCED)

**Status (file): partial.** Honest. Verdict: **partial, advanced.**

The genuinely-new SPT-free framing. Proved in full: Lemma A (2-entry), Lemma B (Cov monovariant — the load-bearing new structural result), Lemma D (star+straggler self-blocking). The refinement obstruction in Lemma B is airtight: a two-element set $\{2,p\}$'s only proper nonempty subsets are $\{2\},\{p\}$; both are singletons ⟹ `singleton-freeze` ⟹ regime (F), excluded in (S); hence $\{2,p\}$ persists once entered, Cov is a bounded monotone subset of the finite set $P(a_1)$, stabilizing after $\le|P(a_1)|$ $\{2,p\}$-crashes. This is a real partial invariant that bounds the $\{2,p\}$-crash count and crash primes SPT-free (survives a failure of SPT/W1 — the field's only such framing).

The self-refutation of the original Lemma C ("crash forced to Cov=$P(a_1)$") is correct and honest — verified counterexamples (a1=35,175,323,385,4199) terminate self-blocking with Cov⊊$P(a_1)$. The narrowing to the broader wall (GAP-S': termination after Cov stabilizes) is honest, not a cover: the approach explicitly states Cov bounds only $\{2,p\}$-crashes, not straggler/$\{2,p,q\}$-type/free-rider crashes, and that GAP-S' is the same hard wall as α's GAP-S.

**Gap remaining (GAP-S'):** prove the saturated regime terminates after Cov stabilizes — i.e. that the post-stabilization promotions (straggler refinements, free-rider-carrying core crashes) exhaust themselves and reach a self-blocking family. This is the same wall as α's GAP-S; the Cov-monovariant narrows but does not close it. Sub-gap GAP-A (core nonempty throughout (S)) is unproved but correctly flagged as non-load-bearing for Lemma B.

No overclaim. No skipped case. Case split (prime-power / (F) / (S)) exhaustive; even-$a_1$ coverage honestly discussed. Promotable lemmas (Cov-monovariant, star+straggler self-blocking, entering-2) all pass the bar — **certified** into `lemmas/`.

### smooth-window-crash — CHANGES REQUESTED (partial)

**Status (file): partial.** Honest. Verdict: **partial.**

Rigorously proved: Entering-2 Lemma (E1, unconditional, clean gcd argument) and the Equality-Case Corollary (C1, conditional on W1). The promotion dichotomy (equality vs strict-beat) is exhaustive by `mtp-monovariant-and-gap-bound` (the mtp-multiple is valid and ≤ $a_n+\mathrm{mtp}$). The refuted linchpin (equality-promotions are NOT dominated) is correctly fixed.

**Gaps remaining:** W1 (mtp-witness carries a prime ≤ $p^*$) — 0-violation conjecture, direct combinatorial proof fails because $\mathrm{nextprime}(p^*)^2<\mathrm{primorial}(p^*)$ (verified for $p^*\in\{3,\ldots,41\}$), so the cheap structural kill is not a formality; W2 (strict-beat smooth-density) — the hard analytic step, no KB entry (Dickman/Brun sieve absent), asymptotic-vs-bounded-$x$ tension, unproven; GAP-3 (the wall) — honestly NOT closed, owned by pstar/α.

**Field-correction made honestly:** §6 Corollary correctly states "GAP-1 closed conditional on SPT" (not on W1); §7 explicitly flags "$\{2,97\}$ obstruction: SPT bounds mtp but does NOT bound $P_{\mathrm{ess}}$." No residual "W1 ⟹ mtp bounded" overclaim. The scoping (GAP-1 specialist, deliberately not a whole-wall solver) is upfront and correct.

No overclaim. Promotable lemma (Entering-2) passes — **certified**.

### density-promotion-bound (α) — CHANGES REQUESTED (partial, ADVANCED)

**Status (file): partial.** Honest. Verdict: **partial, advanced.**

Freeze branch (F) closed end-to-end (imported, unchanged, correct). Saturated branch: the load-bearing correctness fix this round is the linchpin correction (§5c: equality-promotions are genuine new minimals because $T^*$ is a transversal, not a member) and the W1-vs-SPT distinction (§5e "Critical correction": W1 does NOT bound mtp; the bound requires SPT = W1-on-equality ∧ W2-on-strict-beat). GAP-1 reduced to SPT (rigorous implication, Prop in §5d). GAP-3 open with the rigorous $\{2,q\}$ obstruction (Lemma 9). The `freeze-lock` "equivalence" overclaim is struck (§4a remark).

**Gaps remaining:** W1, W2 (both open conjectures, 0 violations on 6 standard seeds); GAP-3 (open, needs crash-eviction partner owned by pstar — α correctly does NOT collapse into pstar's Cov framing, preserving diversity).

**Field-correction made honestly:** §5e explicitly states "W1 does NOT by itself bound mtp... the bound requires SPT"; the outliner's erroneous "W1 ⟹ mtp ≤ primorial" is corrected. No residual overclaim.

No overclaim. Promotable lemmas (common-primes-bounded, Sat-criterion, $\{2,q\}$-obstruction) pass — **certified** into `lemmas/` (mtp-density = mtp-monovariant, already certified; freeze-lock already certified).

### bounded-gap-lcm-reduction (γ) — CHANGES REQUESTED (partial, thin)

**Status (file): partial.** Honest. Verdict: **partial** (thin this round).

The certified asset (mtp monovariant, r2) is unchanged and imported across the field. This round's standalone contribution is the **crux verdict**: Prop 2.2 (W1 does NOT bound the mtp product — counterfamily $T^*=\{5,97\}$, verified); Prop 2.4 (SPT ⟹ mtp≤primorial, the correct GAP-1 closer); the SPT-vs-W1 independence remark (2.5); and the GAP-3 articulation (unique-connector obstruction stands; free-rider-eviction does NOT refute it under γ's pure "gaps ≤ G" hypothesis because eviction needs the crash mechanism; `aimo-0678` lcm-reduction finite-state route DEAD; strong free-rider universality FALSE, refuted by a1=15 where entering prime 2 persists essential). All verdicts correct and honestly recorded.

**Gaps remaining:** GAP-1 (open, reduces to unproven SPT); GAP-3 (open, superseded by pstar's direct Cov+crash route which bypasses GAP-3 entirely). γ is no longer a plausible standalone solver — both sub-gaps open — but remains the cleanest carrier of the mtp monovariant. No new promotable lemmas (Prop 2.2 is a negative verdict; Prop 2.4 conditional on unproven SPT).

**Field-correction made honestly:** §2.1 "CRUX VERDICT: W1 does NOT bound the mtp product" with explicit counterfamily. No residual overclaim. The run_state instruction "field should stop citing W1 as a GAP-1 closer" is satisfied by γ's verdict.

No overclaim. No promotable lemmas this round (correctly flagged).

## Field-wide assessment

- **No approach is solved.** The wall (saturated-regime termination) remains open in all four. Full proof stays "(none yet — wall open)".
- **The W1-correction is honest across the field.** α (§5e), γ (§2.1), smooth (§6-§7) all correctly distinguish W1 (witness carries small prime — does NOT bound the product) from SPT (every minimal carries a small prime — DOES bound the product via the small-prime-set transversal). pstar avoids the issue entirely (SPT-free). No residual overclaim.
- **Diversity guard intact.** pstar (SPT-free Cov-monovariant) is the field's only framing that survives a W1/SPT failure — the single-point-of-failure on GAP-1 (α, γ, smooth all depend on W1) has one independent backup.
- **6 new lemmas certified** into `lemmas/`: cov-monovariant, star-straggler-self-blocking, entering-2, common-primes-bounded, sat-criterion, two-q-gap3-obstruction (16 total).
