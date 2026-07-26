# Round 7 proof-reviewer report — `imo-2026-06` (PIVOT ROUND)

Start: 2026-07-25 20:05 UTC. Reviewed all THREE builder attempts. Every load-bearing computational claim reproduced independently with the corrected naive $O(N^2)$ gcd-greedy (gold standard; cross-checked bit-exact vs `/tmp/round-6/mt_greedy.py` on $a_1\in\{15,77,375,9375\}$; NEVER `/tmp/round-4/fast_greedy.py`). Smallest cases hand-enumerated first ($D_0$ for $a_1=15$ = $\{3,5,6,9,10,12,15\}$, size 7, matching `D_n-slack-obstruction`).

## Refutation re-verified (compact)

$a_1=375=3\cdot5^3$: naive greedy → MT stabilizes to $\{2,3,5,7,19\}$ (reviewer-confirmed, stable from step 6 to $N=1500$); $T=852$, $L=3990=2\cdot3\cdot5\cdot7\cdot19$ (run-state-verified, period needs $N>2T$); governing prime $19>15=\operatorname{rad}(a_1)$. $a_1=9375=3\cdot5^5$: MT final $=\{2,3,5,7,67\}$ (reviewer-confirmed at $N=4000$); $T=3108$, $L=14070=2\cdot3\cdot5\cdot7\cdot67$ (run-state-verified); gov $67>15$. The THEOREM holds in both (periodic); only $q\le\operatorname{rad}(a_1)$ is false. Real Gap A = FINITENESS of governing primes.

---

## Approach 1: `f-of-a1-bounded-nonresidue-statistic`

**Builder self-report: unsolved / DEAD.** I concur — RETHINK.

**Adversarial verification of the three load-bearing claims:**

(a) **Tautology claim — CONFIRMED.** The outline-reviewer's "$k_*=1$ for $\{15,35,77,91,847,375\}$" tested the map $\sigma_n\to d_{n+1}$. But $d_{n+1}=\min D_n$ IS the greedy rule (certified `linchpin-and-gap-bound` + `D_n-slack-obstruction` Step 1), and $D_n\subseteq\sigma_n$ for $k\ge1$, so $d_{n+1}$ is a FUNCTION of $\sigma_n$. Hence $\sigma_n=\sigma_{n'}\Rightarrow d_{n+1}=d_{n'+1}$ trivially — 0 conflicts universally. I reproduced this on $a_1\in\{15,77,375\}$: 0 conflicts at $k=1$ on the increment-projection in every case. This is a tautology; it proves nothing about forward-determinism. The outline-reviewer's "APPROVE — most promising line in 7 rounds" was an artifact of this error.

(b) **Set-to-set $k_*\approx T$, realized $\approx T$ — CONFIRMED.** I reproduced the genuine load-bearing map $\sigma_n\to\sigma_{n+1}$ (set-to-set, equivalently $\sigma_n\to D_{n+1}$):

| $a_1$ | $M_1$ | $T$ | $k_*$ (my repro) | realized @ $k_*$ | realized$/T$ |
|---|---|---|---|---|---|
| 15 | 15 | 8 | 1 | 10 | 1.25 |
| 77 | 77 | 18 | 1 | 21 | 1.17 |
| 375 | 15 | 852 | 100 | 858 | 1.01 |

$a_1=375$: $k_*=100$ (first 0-conflict window), realized $858\approx T=852$. The builder's table said $k_*\in(65,128]$, realized $858$ — my $k_*=100$ is within $(65,128]$ and the realized count matches EXACTLY. The rad-77 pair small member ($a_1=77$: $k_*=1$) matches. (I could not independently verify $a_1=847$ — $N>2T=3488$ with $M_1=77$ makes the $D_n$-computation $O(N^2M_1)\approx1.2$B ops, infeasible in pure Python in the time budget — but the $a_1=375$ reproduction confirms the mechanism and the $a_1=77$ member of the rad-77 pair is confirmed.) The realized-state-count $\approx T$ is the EXACT signature of the round-4 `increment-window-automaton` / `T-unbounded-in-$M_1$` fence — now EXTENDED to the set-valued $D_n$-window: the per-step richness ($|D_n|\ge2$ almost everywhere) is exactly offset by greater orbit-wide variety (the orbit visits $\approx T$ distinct $D$-configurations).

(c) **Circularity — SOUND.** In the periodic regime with period $T$, $a_{n+T}=a_n+L$ implies $a_{n+T}+d=a_n+d+L$ for each $d$; the constraint set $\mathcal F_{n+T}$ stabilizes to the periodic admissible structure (every term in $\mathcal B_\infty$ by `every-term-in-binfinity`; the stabilized admissible set is $L$-periodic by `distinct-supports-stabilize`'s corollary conditional on Gap A — which the periodic regime presupposes). Hence $D_{n+T}=D_n$, $\sigma_{n+T}=\sigma_n$, so the forward map is single-valued at every $k\ge T$; therefore $k_*\le T$ always in the periodic regime, and "finiteness of $k_*$"$\equiv$"finiteness of $T$"$\equiv$the theorem. The linear $k_*\approx cT$ tracking across $\{175,375,847,9375\}$ (builder's table) is empirical evidence that no local structural $f(a_1)$-bound on $k_*$ independent of $T$ exists.

**Verdict: RETHINK.** The route is dead — collapses to (round-4 fence extended to set-valued windows) + (tautology-trap) + (circularity). The $f(a_1)$-vs-$f(\mathrm{rad})$ distinction is real ($k_*$ is genuinely NOT $f(\mathrm{rad})$-bounded — rad-77 pair: $a_1=77\to k_*=1$ vs $a_1=847\to k_*\in(65,128]$ at the same $\mathrm{rad}=77$), but $k_*\approx cT$ makes the state-space bound $2^{k_*\cdot M_1}$ astronomical AND its finiteness is circular with periodicity. The rad-77 fence is "respected" only vacuously (circularly).

**Certified deliverable:** the negative fence **`Dn-window-forward-determinism-tautology-trap`** (7th structural fence) — written to `lemmas/Dn-window-forward-determinism-tautology-trap.md`. Genuinely new on TWO counts: (1) the tautology-trap (methodological — the min-projection $\sigma_n\to d_{n+1}=\min D_n$ is trivially single-valued; fences the specific mis-testing error that produced the round-7 false-positive); (2) extends the round-4 `increment-window-automaton` / `T-unbounded-in-$M_1$` fence from single-valued ($d_n$) windows to SET-VALUED ($D_n$) windows (the $D_n$-window's per-step richness does NOT escape the realized$\approx T$ signature). NOT in the 16-dead/6-fence list.

---

## Approach 2: `parametric-recruitment-family`

**Builder self-report: partial.** I downgrade the ROUTE to RETHINK (the hole-patching framing is fatally broken), but certify the negative fence + record the single-case bedrock.

**Adversarial verification:**

(a) **Cofactor-collapse (96.6% out-of-skeleton) — CONFIRMED EXACT.** For $a_1=9375$, $N=4000$, governing $\{2,3,5,7,67\}$: my independent MT-greedy gives $3864/4000=96.6\%$ of terms carry a prime outside the governing skeleton — bit-exact match to the builder. The greedy does NOT stay within the governing skeleton; it routinely picks terms carrying transient primes.

(b) **Non-monotonicity (115 grow / 7 shrink, 75-prime flush) — CONFIRMED (minor count discrepancy).** My MT-greedy on $a_1=9375$, $N=4000$: $115$ grow-events, $7$ shrink-events — EXACT match to the builder. The single-step flush at $n=222$ removes $76$ transient primes at once (builder said 75; my independent count is 76 — a one-off under-count by the builder, consistent with the round-6 rule that builders/explorers under-count). Distinct MT-primes ever seen: $110$ (builder: "109+"); transient: $105$ (builder: "109+ minus 5 governing"). The qualitative structural claim — the MT-prime set is deeply non-monotone, with a single step flushing ~75 transient primes — is CONFIRMED. Final MT-primes $=\{2,3,5,7,67\}$ (builder-matched). (Note: my period detection on short $N=4000<T=3108\times2$ gave a false $T=46$; the run-state-verified $T=3108$, $L=14070$ stands. The MT-evolution, not period detection, is the load-bearing claim here and is confirmed.)

(c) **`hole-patching-strict-shrink-refuted` genuinely new — YES.** The non-monotonicity obstruction (a) is genuinely new: NO prior fence in the 16-dead/6-fence list records that the MT-prime set is non-monotone (transient primes both enter AND exit), making the skeleton $G_k=\bigcup\operatorname{MT}(\mathcal F_k)$ non-monotone and the hole-set modulus $L_k$ re-defined at every event. The framing class (structural-covering) is genuinely new (not cofactor/residue/monovariant/variational/Schur/primal-dual/syndetic). The cofactor-collapse half (b) points to the existing `window-uniqueness-reduces-to-cofactor` / `schur-cofactor-premise-fails-in-periodic-regime` (it is the APPLICATION of those certified fences to the hole-patching framing) — but the non-monotonicity half (a) is a new structural observation no prior fence records.

(d) **The $3\cdot5^e$ MT-stabilization bedrock for $a_1=375$ — CONFIRMED, but NOT a general lemma.** Reviewer-reproduced: MT stabilizes to $\{2,3,5,7,19\}$ from step 6, $5$ transversals ($\{2,3\},\{2,5,7\},\{2,5,19\},\{3,5\},\{3,7,19\}$), stable to $N=1500$. But this is a SINGLE-CASE computational verification, not a structural theorem — the builder explicitly and honestly says "It is a verified instance, not a structural theorem — it does not explain WHY the MT stabilizes, only THAT it does for this $a_1$." It is NOT certifiable as a general reusable lemma. I record it in `current.md` as a computational fact (one starting value out of infinitely many; does NOT prove the theorem for $a_1=9375$ or arbitrary $a_1$).

**Verdict: RETHINK** (the hole-patching framing's load-bearing invariant — strict-shrink of the hole-set — is REFUTED (non-monotone), and the termination half collapses to the cofactor-bound wall (circular). The route cannot close Gap A. This mirrors the round-5 two-coincidence/deviation-index pattern: dead route, but a certified negative fence + a recorded computational bedrock survive as deliverables.)

**Certified deliverable:** the negative fence **`hole-patching-strict-shrink-refuted`** (8th structural fence, structural-covering class) — written to `lemmas/hole-patching-strict-shrink-refuted.md`. (The $a_1=375$ single-case bedrock is recorded in `current.md` but NOT certified as a lemma — it is a finite-computational check for one starting value, not a general theorem.)

---

## Approach 3: `p1-equals-2-direct` (revised)

**Builder self-report: partial.** I concur — CHANGES REQUESTED (Status partial).

**Adversarial verification:**

(a) **Strengthened `cofactor-P1-divisibility` — CONFIRMED (with a proof correction).** Reviewer-reproduced for $a_1=375$, $N=3000$, governing $G=\{2,3,5,7,19\}$, $P_1=\{3,5\}$:

| $r$ | $r$-multiples | cofactor-fails ($k$ not div by 3 or 5) |
|---|---|---|
| $r=2$ | $2517$ | $0$ |
| $r=7$ | $550$ | $0$ |
| $r=19$ | $210$ | $0$ |
| $r=3$ (in $P_1$, expect fails) | $2824$ | $1257$ |
| $r=5$ (in $P_1$, expect fails) | $1113$ | $141$ |

EXACT match to the builder's table ($2517/550/210$ multiples, $0$ fails; $1257/141$ fails for $r\in P_1$). The strengthened hypothesis ("any governing $r\notin P_1$", not only the hypothetical $r>M_1$) is verified on the refutation witness's ACTUAL governing primes $\{2,7,19\}$.

**Proof correction (rigor gap found and fixed).** The builder's Step-10 proof asserts "$T$ contains exactly one of $\{p,q\}$", via "$\{p,q\}\not\subseteq T$ (else $T$ not minimal) + $T\cap\{p,q\}\ne\varnothing$ (transversality)". This inference is ONLY valid when $T\ne\{p,q\}$: for $T=\{p,q\}$, "$\{p,q\}\not\subseteq T$" is FALSE (they're equal), and the "drop $T\setminus\{p,q\}$, still a transversal" argument fails (it would leave $\varnothing$, which is not a transversal). The $T=\{p,q\}$ case is SKIPPED — a rigor violation (CLAUDE.md: "No skipped cases"). HOWEVER, the conclusion still holds for $T=\{p,q\}$: in the "$r\notin T$" branch (which applies since $r\notin\{p,q\}=T$), $\operatorname{rad}(T)=pq\mid m=rk$ with $\gcd(r,pq)=1$ gives $pq\mid k$, hence $p\mid k$ (and $q\mid k$). The fix: replace "exactly one of $\{p,q\}$" with "at least one of $\{p,q\}$ in $T$" (pick any $p^*\in T\cap\{p,q\}$; the rest of the proof uses only $p^*\in T$ and $p^*\ne r$). I have rewritten `lemmas/cofactor-P1-divisibility.md` with the corrected proof. The lemma is SOUND (computationally verified, conclusion correct, proof now complete).

The "minimality-of-$r$ crutch dropped" claim is verified: the corrected proof uses ONLY `binfinity-divisibility-progression-structure` + `P1-minimal-transversal-lemma` (incomparability) + coprimality — NO minimal-criminal hypothesis. The strengthening is genuine.

(b) **Step-11 collapse (3 obstructions) — SOUND.** (1) Cofactor not small: the strengthened lemma forces $p\mid k$ or $q\mid k$ (a single small-prime factor), but $k=a_{n_i}/r_i\in\{pj:j\ge1\}\cup\{qj:j\ge1\}$, an INFINITE set — the "small-cofactor" premise is false. (2) Trivial $r\le a_{n_1}\le a_1+(n_1-1)M_1$ bound is VACUOUS (bounds $n_1$ given $r$, not the cardinality of $G$). (3) Circularity: making the slot-counting rigorous requires bounding WHICH primes appear in $k$'s full factorization, which IS Gap A (by `schur-cofactor-premise-fails-in-periodic-regime`: in any periodic realization the cofactor AP $k_{i+s}=k_i+L/r$ has infinitely many prime divisors by classical Schur). The $|P_1|=2$ specialization hits the SAME cofactor-bound wall as the general case. Sound.

(c) **`p1eq2-finiteness-slot-counting-circular` — REJECTED as SUBSUMED.** The proposed fence says "the $|P_1|=2$ slot-counting finiteness argument via the cofactor-P1-divisibility lever is circular (needs the full cofactor factorization = Gap A)." This is a SPECIALIZATION of the already-certified general cofactor fences: `window-uniqueness-reduces-to-cofactor` (the cofactor-bound step) + `schur-cofactor-premise-fails-in-periodic-regime` (the cofactor-prime-set is infinite in the periodic regime). Moreover, the "floor-not-ceiling" limitation of the cofactor-P1-divisibility lever is ALREADY documented in that lemma's own Scope/limitation section ("Weak — forces only $k\ge\min(p,q)\ge3$; no upper bound on $k$; does NOT close Gap A"). Per the reviewer per-role rule ("certify the general one, reject the specialization as subsumed to avoid lemma-cache clutter"), this fence is REJECTED. The rejection is recorded in `current.md`.

**Verdict: CHANGES REQUESTED** (Status partial). The strengthened `cofactor-P1-divisibility` is certified (refines the existing lemma; proof corrected). The finiteness Step 11 is an explicit GAP collapsing to the cofactor-bound wall. The route is NOT dead (the certified lever survives, strengthened) but NOT solved — a genuinely new ingredient not reducing to cofactor-factorization-bounding would be needed to close Step 11; none is on the table within this framing.

---

## Per-slug verdict block

- **`f-of-a1-bounded-nonresidue-statistic`** → **RETHINK** (Status unsolved). The outline-reviewer's APPROVE was based on a tautology ($\sigma_n\to d_{n+1}=\min D_n$ trivially single-valued); the load-bearing set-to-set map collapses to the round-4 fence (realized $\approx T$, extended to set-valued windows — reviewer-confirmed: $a_1=375$ $k_*=100$, realized $858\approx T=852$) + circularity ($k_*\le T$). Negative fence `Dn-window-forward-determinism-tautology-trap` CERTIFIED.

- **`parametric-recruitment-family`** → **RETHINK** (Status unsolved for the route). The hole-patching framing's strict-shrink invariant is REFUTED (MT-prime set non-monotone: $115$ grow/$7$ shrink, flush $76$ at $n=222$ — reviewer-confirmed) and the termination half collapses to the cofactor-bound wall ($96.6\%$ of $a_1=9375$ terms out-of-skeleton — reviewer-confirmed exact). Negative fence `hole-patching-strict-shrink-refuted` CERTIFIED; $a_1=375$ single-case bedrock recorded (not a general lemma).

- **`p1-equals-2-direct`** (revised) → **CHANGES REQUESTED** (Status partial). Strengthened `cofactor-P1-divisibility` CERTIFIED (refines the existing lemma; reviewer-verified $0$ fails for $a_1=375$, $r\in\{2,7,19\}$; proof corrected — the "$T=\{p,q\}$" skipped case is fixed by "at least one of $\{p,q\}$" replacing "exactly one"). Finiteness Step 11 is an explicit GAP collapsing to the cofactor-bound wall (3 sound obstructions). Proposed fence `p1eq2-finiteness-slot-counting-circular` REJECTED as subsumed by the existing general cofactor fences.

## Certified lemmas / fences this round

- **NEW (2):** `Dn-window-forward-determinism-tautology-trap` (−, 7th structural fence; extends round-4 fence to set-valued windows + records the tautology-trap), `hole-patching-strict-shrink-refuted` (−, 8th structural fence, structural-covering class; non-monotonicity of MT-prime set genuinely new, cofactor-collapse half points to existing fences).
- **REFINED (1, count unchanged):** `cofactor-P1-divisibility` — strengthened (hypothesis relaxed to "any governing $r\notin P_1$"; minimal-criminal crutch dropped; proof corrected to handle $T=\{p,q\}$).
- **REJECTED (1):** `p1eq2-finiteness-slot-counting-circular` — subsumed by `window-uniqueness-reduces-to-cofactor` + `schur-cofactor-premise-fails-in-periodic-regime` + the `cofactor-P1-divisibility` lemma's own documented limitation.

**Totals: 32 certified lemmas (was 30); 8 structural fences (was 6); ~19 dead mechanisms (was ~16).** The pivot did NOT close Gap A (all three approaches collapsed to the cofactor-bound wall or the round-4 window-state fence). The deliverable: the refutation + 2 new fences + the strengthened lever + the corrected fence-scope. Status stays `partial`.
