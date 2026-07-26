# proof-reviewer — imo-2026-06, round 5

Reviewed both round-5 built approaches adversarially. Each re-derived from scratch and checked computationally where claimed. Verdict: **BOTH RETHINK (dead-end)** — round 5 found NO genuinely-new non-circular insight; both routes collapse to fences. **Recommend CONSOLIDATE next round.**

---

## Approach 1: `two-coincidence-periodicity` — Verdict: RETHINK (Status unsolved; route dead)

**Builder Status:** partial. **My verdict: RETHINK.** The route is dead (its antecedent IS Gap A); the builder's "partial" is a slight overclaim on the ROUTE, but the proven lemma survives.

### Re-derivation of the load-bearing claim (Lemma 1, the `aimo-0907 criterion)

I re-derived both parts from scratch:

- **(A) One self-coincidence ⇒ eventual periodicity.** $f^a(x)=f^b(x)$, $\delta=b-a>0$. Apply $f^k$ (single-valuedness ⇒ equal inputs give equal outputs): $f^{a+k}(x)=f^{a+\delta+k}(x)=f^{b+k}(x)$ for all $k\ge0$. ✓ Trivial single-valuedness propagation; correct.
- **(B) Two between-orbit coincidences at distinct offsets ⇒ finiteness.** $f^n(x)=f^m(y)$, $f^p(x)=f^q(y)$, $n-m\ne p-q$. WLOG $n-m>p-q$, $\Delta=(n-m)-(p-q)>0$. Apply $f^p$ to the first: $f^{p+n}(x)=f^{p+m}(y)$. Apply $f^n$ to the second: $f^{n+p}(x)=f^{n+q}(y)$. LHS equal ⇒ $f^{p+m}(y)=f^{n+q}(y)$; $(n+q)-(p+m)=\Delta>0$ ⇒ self-coincidence of $O(y)$ at offset $\Delta$ ⇒ by (A) $O(y)$ eventually periodic ⇒ finite as a set ⇒ contradicts self-coincidence-free hypothesis. ✓ Correct.

The lemma is sound. **Certified as `aimo-0907-coincidence-criterion`** (positive, reusable tool; consumer supplies the forward-deterministic map).

### Mechanism-confusion flag (outline-reviewer) — resolved honestly and correctly

The outline-reviewer flagged that the "two coincidences" role is muddled and that the outliner's "no finiteness assumption" claim is false (Step 3's pigeonhole IS a finiteness assumption). The builder resolved this correctly:

- For a **single** forward-deterministic orbit, **one** self-coincidence already gives eventual periodicity (part A — trivial). The "second coincidence" is REDUNDANT for the orbit itself.
- The genuine two-coincidence content (part B) is a **between-orbits** mechanism; our greedy problem has a single orbit, so (B) does not port.
- The route's true load-bearing antecedent is "exhibit a finite **forward-deterministic DETERMINING** statistic $\alpha$" (forward-deterministic so a pigeonhole self-coincidence propagates by (A); determining so $\alpha$-periodicity lifts to $d$-periodicity). This is **exactly Gap A** (finiteness of the determining state $=$ $L$-periodicity of $\mathcal B_\infty$ $=$ finiteness of governing primes). The route does NOT go around Gap A; it presupposes it.

I confirm this resolution: it is the correct reading of `aimo-0907`. The "second coincidence" (outline GAP A3) is moot — there is no first propagating coincidence to double.

### T-unbounded-in-$M_1$ impossibility — independently verified

The builder fences the $f(M_1)$-bounded sub-case with the new T-unbounded-in-$M_1$ impossibility (rad-77 witness). I verified independently:
- $a_1=77=7\cdot11$, $M_1=77$: greedy period $T=18$, $L=154$ (400 terms). ✓
- $a_1=847=7\cdot121$, $\operatorname{rad}(847)=77$, same $M_1=77$: greedy period $T=1744$, $L=18942$ (4000 terms, $d_n\le14\le77$). ✓

$97\times$ jump in $T$ at the same $M_1$. So any $f(M_1)$-bounded forward-deterministic determining $\alpha$ would force $T\le|\text{alphabet}|\le f(M_1)$ — contradiction. The fence is real.

### First coincidence (Step 3) — sound but finiteness-assuming

Pigeonhole on the finite alphabet $\Sigma=\{1,\dots,M_1\}$ (size $M_1$, by `linchpin-and-gap-bound`) gives indices $a<b$ with $\alpha_a=\alpha_b$ for either named abstraction, with $b-a\le|\text{alphabet}|$. This is sound (the alphabet is finite unconditionally) and non-circular (it does not invoke the cofactor AP). ✓ It is, however, a finiteness assumption (the outline-reviewer's flag), and as the builder notes it is *only* a coincidence of the abstraction symbol, not of any determining state.

### Second coincidence — honestly flagged as a gap (not exhibited computationally)

The dispatch asked: did the builder exhibit a second coincidence computationally, or flag it honestly? The builder did NOT run a second-coincidence search; instead they resolved the mechanism confusion theoretically (the second coincidence is redundant for a single orbit; the genuine two-coincidence mechanism is between-orbits and does not port). This is an **honest flag**: the second coincidence is shown to be MOOT, not exhibited. The load shifts to the forward-determinism + determining of $\alpha$, which is Gap A.

I independently confirmed the builder's read-out is consistent: the witness-prime abstraction has only 2–3 realized symbols and many self-coincidences (its period $T(\alpha)$ divides $T(d)$), so "two coincidences" trivially exist — but they do not lift to $d$-periodicity because $\alpha$ is not determining.

### Computational probe — independently re-run, all rows match

I ran my own corrected greedy on $a_1\in\{15,35,77,91,175\}$ (periods $T=8,34,18,20,274$; $L=30,210,154,182,2730$; $d_n\le M_1$ re-confirmed in every case). Forward-determinism conflict counts for the witness-prime-tuple abstraction (every realized symbol has $\ge2$ distinct successors):

| $a_1$ | $T(d)$ | $T(\alpha)$ | $\alpha$ realized | fwd-det conflicts | det-$d$ conflicts |
|------|------|------|------|------|------|
| 15 | 8 | 4 | 2 | 2 | 2 |
| 35 | 34 | 34 | 2 | 2 | 2 |
| 77 | 18 | 18 | 2 | 2 | 2 |
| 91 | 20 | 10 | 2 | 2 | 2 |
| 175 | 274 | 274 | 3 | 3 | 3 |

All rows match the builder's table (modulo the $d_n$-itself and $a_n\bmod M_1$ columns, which I also re-verified: $d_n$ conflicts $4/6/8/8/12$; $a\bmod M_1$ conflicts $1/6/1/1/8$). The witness-prime word's period is a proper divisor of $T(d)$ when smaller ($a_1=15$: $4|8$; $a_1=91$: $10|20$) — the structural sub-period leak. **Every named abstraction is NOT forward-deterministic** (branch (iii) of Step 4); the antecedent of Lemma 1(A) cannot be met by any of them.

### Does the approach secretly re-walk a fenced step?

- **Substitution/morphic fence?** No. The route is a coincidence-doubling argument (pigeonhole self-coincidence + propagation by single-valuedness), NOT a fixed-point-of-a-substitution argument. It does not presuppose the period via $\sigma:w\to ww$.
- **Ergodic-window/increment-automaton fence?** No, not directly. The route does NOT require window-length-determined single-valuedness of a $d$-window state; its abstractions are 1-step (witness-prime-tuple, $d_n$, $a_n\bmod M_1$). BUT the $f(M_1)$-bounded sub-case IS fenced by the new T-unbounded-in-$M_1$ impossibility, which subsumes the modular-residue/ergodic-window/increment-automaton fences for $f(M_1)$-bounded statistics. The builder is honest about this.
- **Cofactor fence?** The route does not invoke cofactors; it collapses to Gap A via the equivalence "finite forward-deterministic determining $\alpha$ $\iff$ $L$-periodic $\mathcal B_\infty$ $\iff$ finite governing primes" (the round-1 endgame). This is not a re-walk of the cofactor strip; it is the coincidence-doubling route reaching the same wall by a different path.

### Score

- **Correctness:** 4/4 (Lemma 1 re-proved correctly; probe honest and matched; resolution of mechanism confusion correct).
- **Completeness/rigor:** 3/3 (every step justified; the gap (∗) is explicit; the fence is verified).
- **Progress:** 2/3 (one reusable lemma certified + a clean diagnosis that the route collapses to Gap A; but the route itself is dead — no new positive advance toward solving).

### Verdict: **RETHINK** (Status unsolved). The route is fatally broken: its antecedent IS Gap A, the $f(M_1)$-bounded sub-case is fenced, and no non-$f(M_1)$-bounded finite determining $\alpha$ is identified. The builder's own recommendation is "retire and consolidate." The `aimo-0907` criterion is the one salvageable deliverable (certified). The builder's Status=partial is a slight overclaim on the route; I downgrade the route to dead, but the lemma stands.

---

## Approach 2: `deviation-index-descent` — Verdict: RETHINK (Status unsolved; route dead)

**Builder Status:** partial. **My verdict: RETHINK.** B2 is refuted by TWO independent fences; the route cannot work as set up. The dispatch explicitly prescribes RETHINK for this case, and I confirm it. Two salvageable lemmas.

### B1 (candidate-period pigeonhole-existence) — genuinely sound and non-circular

I re-derived B1: the increment-word is infinite (greedy never terminates, $d_n\ge1$) over the finite alphabet $\Sigma=\{1,\dots,M_1\}$ (`linchpin-and-gap-bound`). For each $w\ge1$, at most $M_1^w$ distinct length-$w$ blocks; infinite pigeonhole ⇒ two windows coincide ⇒ $P_0=j-i$ is a candidate period. Non-circularity check: hypothesis = "infinite word over finite alphabet" (both unconditional); conclusion = "a coincidence exists." No mention of periodicity, $\mathcal B_\infty$, MT, governing primes, or any Gap-A-adjacent quantity. ✓ **Certified as `candidate-period-pigeonhole-existence`** (positive, elementary).

The caveat is honest and verified: $P_0(w)$ is NOT necessarily a period for small $w$ (see B2-Sharp below).

### Mount (Steps 1–6 of `minimal-criminal-schur-contradiction`) — imported correctly, NOT re-walking the fenced Schur Step 7

The builder cites the mount by name and does NOT re-derive the (fenced) Schur cofactor Step 7 (`schur-cofactor-premise-fails-in-periodic-regime`). The well-ordering transfers from governing primes to deviation-indices by the same well-ordering of $\mathbb N$ — a legitimate re-targeting, not a re-walk of the Schur mechanism. The forced-increment identity $d_{m-1}=q-(a_{m-1}\bmod q)$ at $q$-multiple steps is the mount's only greedy-dynamic ingredient (per the `syndetic-divisible-closed-not-periodic` guardrail). ✓ Imported correctly.

### B2 — REFUTED as uniform mechanism; I verified BOTH fences independently

#### (B2-a) Cofactor-bound fence — algebraically verified

The builder's claim: the shift-by-$C$ ($C:=a_{j_0}-a_{i_0}$, constant on $[i_0,n_0]$ by telescoping: $a_{m+P_0+1}-a_{m+P_0}=d_{m+P_0}=d_m=a_{m+1}-a_m$ so $a_{m+P_0}-a_m$ is constant $=C$) does NOT preserve the admissibility structure. The deviation at $n_0$ means $a_{n_0+1+P_0}\ne a_{n_0+1}+C$; the admissibility mismatch between thread $A=(a_{i_0},\dots,a_{n_0})$ and thread $B=(a_{i_0+P_0},\dots,a_{n_0+P_0})=A+C$ hinges on $\gcd(a_{n_0+1}+C, a_{j-P_0}+C)$ vs $\gcd(a_{n_0+1}, a_{j-P_0})$.

I verified the algebra: adding $C$ to both arguments of a gcd does NOT preserve it in general (e.g. $\gcd(2,3)=1$ but $\gcd(2+C,3+C)$ varies with $C$). For the shift to preserve admissibility for ALL pairs, $C$ must be divisible by every prime appearing in any $a_k$ for $k\in[i_0,n_0]$ — i.e. $C$ divisible by every governing prime. This is a cofactor-type bound (bounding which primes divide $C=\sum$ of one period of $d$ is Gap-A-adjacent), fenced by `window-uniqueness-reduces-to-cofactor`, `lemma-C-strip-no-go`, `schur-cofactor-premise-fails-in-periodic-regime`. ✓ The fence the outline-reviewer warned about is confirmed.

#### (B2-Sharp) Increment-window-automaton fence — computationally verified

The builder's computational witness: $a_1=35$, $M_1=35$, true $T=34$, $L=210$. With $w=2$: $P_0(2)=5$ (a valid length-2 coincidence at $i_0=5$, $j_0=10$), but $d_8=4\ne10=d_{13}$ — a real deviation at $n_0=8$. With $w=8$: $P_0(8)=34=T$, no deviation.

I ran my own corrected greedy on $a_1=35$ (400 terms) and verified:
- $d_{5..14}=(10,5,5,4,6,10,5,5,10,6)$ — matches the builder exactly.
- Length-2 window at $i=5$: $(d_5,d_6)=(10,5)$; at $j=10$: $(d_{10},d_{11})=(10,5)$ — match ✓. So $P_0=5$ is a valid candidate from B1 with $w=2$.
- $d_8=4$, $d_{13}=d_{8+5}=10$ — deviation at $n_0=8$ ✓. $P_0=5$ is NOT a period.
- With $w=8$: smallest-offset coincidence is $i=0$, $j=34$, $P_0=34=T$, no deviation in 400 terms ✓.

(Independently I found the smallest-offset coincidence for $w=2$ is actually $P_0=3$ at $(i,j)=(23,26)$, also not a period — the builder's "first" wording is imprecise, but the substantive claim — that B1 with $w=2$ can produce a non-period candidate — is correct and verified. The descent's success depends on picking the RIGHT coincidence; B2 as a UNIFORM mechanism (works for whatever B1 produces) would falsely conclude periodicity for $w=2$.)

**Consequence confirmed:** B2 cannot be uniform in $w$. For B2 to have a chance, $w\ge w_{\min}$ (minimal window-length recovering the true period), and $w_{\min}$ is UNBOUNDED in $M_1$ (the round-4 `ergodic-window-state / increment-window-automaton` fence). This is a DIFFERENT fence from (B2-a) — the increment-window-automaton fence, not the cofactor-bound fence — but it is fenced nonetheless. ✓ **Certified as `deviation-descent-blocked-by-wmin-fence`** (negative, structural).

#### Forced-increment identity does NOT rescue B2 — verified

The mount's only greedy-dynamic ingredient is the forced-increment identity $d_{m-1}=q-(a_{m-1}\bmod q)$ at $q$-multiple steps. The builder's claim: it is FORWARD and LOCAL (determines $d_{m-1}$ at $q$-multiple steps from the residue); the descent needs BACKWARD and GLOBAL. I confirm:
1. The deviation index $n_0$ is set by the $d$-word coincidence structure, NOT by the $q$-multiple pattern — so we cannot ensure $a_{n_0+1}$ is a $q$-multiple. ✓
2. Even if both $a_{n_0+1}$ and $a_{n_0+1+P_0}$ were $q$-multiples, the deviation $d_{n_0+P_0}\ne d_{n_0}$ becomes $(a_{n_0}+C)\bmod q \ne a_{n_0}\bmod q$, i.e. $q\nmid C$ — a statement about $C,q$, not a smaller-index deviation. Turning "$q\nmid C$" into a deviation at $m<n_0$ would require the $q$-multiple pattern to itself deviate from $P_0$-periodicity — circular. ✓

The forced-increment identity is the wrong shape; it does not close B2.

### Does the approach secretly re-walk a fenced step?

- The **framing** (descent on the first deviation index) is genuinely different from the increment-window-automaton framing (pigeonhole-on-equal-window-states requires single-valuedness of the window-state transition; the deviation-descent does not).
- BUT the **load-bearing step** (B2) reduces to needing $w\ge w_{\min}$, which IS the increment-window-automaton fence. The builder is honest about this (Step 4'/4''). This is not a SECRET re-walk — it is an explicit, diagnosed collapse to a fence.
- The Schur Step 7 (fenced) is NOT re-walked; the mount's Steps 1–6 are imported unchanged. ✓

### Score

- **Correctness:** 4/4 (B1 sound; B2 refutation algebraically and computationally verified by me).
- **Completeness/rigor:** 3/3 (B2 gap explicit; two fences both verified; forced-increment non-rescue verified).
- **Progress:** 2/3 (two salvageable lemmas — one positive, one negative structural fence; but the route is dead).

### Verdict: **RETHINK** (Status unsolved). B2 is provably uncloseable with the current setup (two independent fences; the only greedy-dynamic ingredient is the wrong shape). The approach must go back to the outliner for a different strategy; the deviation-descent as set up cannot work. The dispatch explicitly prescribes RETHINK for this case, and I confirm.

---

## Lemma certifications (round 5)

Certified (3 new, total 28):
1. **`aimo-0907-coincidence-criterion`** (positive, reusable tool) — from `two-coincidence-periodicity`. Parts A+B re-proved from scratch and reviewer-verified; sound; consumer supplies the forward-deterministic map. Written to `lemmas/aimo-0907-coincidence-criterion.md`.
2. **`candidate-period-pigeonhole-existence`** (positive, elementary) — from `deviation-index-descent`. Infinite pigeonhole on finite alphabet $\Sigma=\{1,\dots,M_1\}$; non-circular; caveat honest. Written to `lemmas/candidate-period-pigeonhole-existence.md`.
3. **`deviation-descent-blocked-by-wmin-fence`** (negative, structural fence) — from `deviation-index-descent`. The deviation-index descent is blocked by TWO independent fences (cofactor-bound via shift-by-$C$ AND increment-window-automaton via $w_{\min}$ unbounded in $M_1$); forced-increment identity does not rescue. Written to `lemmas/deviation-descent-blocked-by-wmin-fence.md`.

Rejected: none (both builders' three proposals all certified).

---

## `current.md` update summary

- `## Status`: **partial** (unchanged — Gap A still open; no solve).
- `## Approaches tried`: appended the two round-5 attempts with RETHINK verdicts and full reasoning.
- `## Current best`: appended the round-5 sharpening (wall resists ~13 mechanisms with FOUR structural fences now; the round-5 coincidence-doubling and deviation-descent routes both collapse to fences; the T-unbounded-in-$M_1$ impossibility is the new strong negative deliverable, reviewer-verified).
- `## Full proof`: not presented (no slug solved); the round-5 negative fences and reusable tools added to the lemma list.
- Lemma count: 25 → 28.

---

## Round-5 directive (the 5th round on Gap A — CONSOLIDATE?)

**Did round 5 find a genuinely-new non-circular insight?** **No.** Both round-5 approaches were genuinely-different framings (coincidence-doubling goes AROUND Gap A in principle; deviation-descent re-targets the certified mount from the prime $q$ to the deviation index), and both were built honestly and rigorously. But both collapsed to fences:

- `two-coincidence-periodicity`: the route's antecedent (finite forward-deterministic determining $\alpha$) IS Gap A; the $f(M_1)$-bounded sub-case is fenced by the new T-unbounded-in-$M_1$ impossibility; the genuine two-coincidence mechanism is between-orbits and does not port to the single greedy orbit. No non-$f(M_1)$-bounded finite determining $\alpha$ identified.
- `deviation-index-descent`: B2 (the descent) is refuted by TWO independent fences (cofactor-bound via shift-by-$C$, AND increment-window-automaton via $w_{\min}$ unbounded in $M_1$); the only greedy-dynamic ingredient (forced-increment identity) is the wrong shape (forward/local vs backward/global).

**Both approaches collapse to fences.** The wall now resists ~13 mechanisms with FOUR structural fences (syndetic-divisible, primal$\equiv$dual, Schur-premise-false, + the round-5 T-unbounded-in-$M_1$ impossibility subsuming the modular-residue/ergodic-window/increment-automaton fences for $f(M_1)$-bounded statistics). The $q\le M_1$ conjecture is almost certainly true (273+ cases, 0 failures) but, per the accumulated fences, NOT provable by any cofactor/transversal/MT/statics/monovariant/residue/finite-pigeonhole-state/Schur/primal/coincidence-doubling/deviation-descent route.

**Recommendation: CONSOLIDATE next round.** This is the 4th round on Gap A; the round-state's STALL CRITICAL path says "if round 5 fails to find a genuinely-new insight, CONSOLIDATE." Round 5 did not find one. The certified conditional proof (Gap A $\Rightarrow$ endgame $\Rightarrow$ $a_{n+T}=a_n+L$ from $n=1$) + LOCK sub-case + 28 certified lemmas (incl. 7 negative/structural fences) + the sharp T-unbounded-in-$M_1$ impossibility constitute substantial partial progress on a genuinely IMO-P6-hard problem. A non-circular proof, if one exists, would require a genuinely new idea not in the fenced list — and after 5 rounds and ~13 dead mechanisms, the honest assessment is that such an idea is not reachable with the tools and corpus on the table. Write up the partial deliverable as the run's output.

If one more round is attempted, the ONLY genuinely-untried candidates remaining (per the round-state) are: (a) a p-adic local-global argument analyzing $v_p(a_n)$ per small prime (note: round-4 outliner found $v_2$ reaches 13 not periodic-with-$T$ for $a_1=385$ — verify whether per-prime valuation stabilizes with a DIFFERENT period); (b) a direct olympiad-style "minimal counterexample on the sequence" not via transversals. Both are long shots. If the orchestrator elects one more round, dispatch ONE explorer on (a) and ONE on (b); if neither surfaces a non-fenced mechanism, CONSOLIDATE unconditionally.

---

## Status
partial

## Goal Progress
Round 5: both new approaches (two-coincidence-periodicity, deviation-index-descent) RETHINK (dead-end); 3 lemmas certified (aimo-0907-coincidence-criterion +, candidate-period-pigeonhole-existence +, deviation-descent-blocked-by-wmin-fence −); total 28 lemmas, 7 negative/structural fences; wall resists ~13 mechanisms; T-unbounded-in-M_1 impossibility reviewer-verified (a_1=77→T=18 vs a_1=847→T=1744); B2-Sharp refutation reviewer-verified (a_1=35, w=2, P_0=5, d_8=4≠10=d_13). No genuinely-new non-circular insight found. **CONSOLIDATE next round.**
