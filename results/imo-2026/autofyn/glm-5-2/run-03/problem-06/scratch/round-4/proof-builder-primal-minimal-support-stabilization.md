# Round 4 proof-builder — `primal-minimal-support-stabilization`

## What I proved

Two structural lemmas in full (both proposed for certification into `results/imo-2026-06/lemmas/`):

### Lemma 1: primal–dual equivalence of Gap A (proposed cert name: `primal-dual-gap-a-equivalence`)
*Statement.* With $\mathcal F_\infty=\{S(a_i):i\ge1\}$, $\operatorname{MS}_\infty$ = inclusion-minimal elements of $\mathcal F_\infty$ (PRIMAL), $\operatorname{MT}(\mathcal F_\infty)$ = minimal transversals (DUAL), the two assertions
- (P) $\operatorname{MS}_\infty$ finite + $\bigcup\operatorname{MS}_\infty\subseteq G$ (finite prime set),
- (D) $\operatorname{MT}(\mathcal F_\infty)$ finite + $\bigcup\operatorname{MT}(\mathcal F_\infty)\subseteq G'$ (finite prime set, = Gap A)

are equivalent. Concretely $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)$ and $\operatorname{MS}_\infty=\operatorname{MT}(\operatorname{MT}(\mathcal F_\infty))$.

*Proof.* Classical blocker involution $b(b(\mathcal C))=\mathcal C$ on clutters over a finite ground (Schrijver / Edmonds–Fulkerson), combined with the redundancy-removal identity $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)$ (a transversal of $\mathcal F_\infty$ iff a transversal of $\operatorname{MS}_\infty$, since every $S\in\mathcal F_\infty$ contains some minimal element). Both directions transfer the bound: $\bigcup\operatorname{MT}(\mathcal F_\infty)\subseteq\bigcup\operatorname{MS}_\infty\subseteq G$ under (P); conversely every $S\in\operatorname{MS}_\infty$ is a transversal of $\operatorname{MT}(\mathcal F_\infty)$ hence $S\subseteq\bigcup\operatorname{MT}(\mathcal F_\infty)\subseteq G'$ under (D). Verified computationally on $a_1\in\{15,35,77,91\}$ and on a synthetic non-self-dual family. Full proof in the approach file.

*Consequence:* the primal framing is NOT a bypass of Gap A — its target (P) is literally the same wall as (D). Any future primal-framing retry hits this equivalence.

### Lemma 2: window-uniqueness reduces to cofactor-bound (proposed cert name: `window-uniqueness-reduces-to-cofactor`)
*Statement.* If the greedy picks $a_{n+1}=m$ with $q>M_1$ dividing $m$, then (i) $m$ is the unique $q$-multiple in the window $[a_n+1,a_n+M_1]$ of size $M_1<q$; (ii) writing $m=kq$, $m$ admissible $\iff$ primefactors$(k)$ hits every $q$-free minimal in $\operatorname{MS}_n$; (iii) proving "no prime $q>M_1$ enters a minimal support" via window-uniqueness requires either (a) primefactors$(k)$ fails the transversal, or (b) a smaller admissible $m'\in(a_n,kq)$ exists — both require bounding primefactors$(k)$, the cofactor-bound step certified dead for `witness-density-recurrence` (R2) and `crt-period-lifting` (R3).

*Proof.* Window size $M_1<q$ ⇒ consecutive $q$-multiples differ by $q>M_1=|W|$ ⇒ at most one in $W$; if $q\mid m\in W$, $m$ is it. Admissibility decomposes by cases on whether $q\in S$. Both continuations (a)/(b) explicitly require controlling primefactors$(k)$ or primefactors$(m')$. ∎

*Verification.* On $a_1=116$ (LOCK-at-2), 154 big-prime-entry events, all with exactly one $q$-multiple in the window — confirms (i). The carrying term is $m=a_n+2$ throughout, giving $k=m/q$ with $2\mid k$ (lock prime trivializes the transversal) — this is exactly why LOCK admits big transient primes. NON-LOCK cases have no such trivialization.

## Empirical silver lining (CONJECTURE, not proved)
Across 19 NON-LOCK $a_1$ (incl. $a_1\in\{15,35,77,91,143,175,385,847,1309,2085,39270,510510,\dots\}$, 80k+ greedy steps): NO prime $>M_1=\operatorname{rad}(a_1)$ enters ANY minimal support at ANY finite $n$. This is STRONGER than the standing conjecture "governing primes $q\le M_1$" — it asserts the bound holds at every finite stage, not just in $\operatorname{MS}_\infty$. Still no non-circular proof; Lemma 2 shows the natural mechanism (window-uniqueness) reduces to the cofactor wall.

## Gaps remaining
- **Step 4 (load-bearing) unproved.** Lemmas 1–2 show it cannot be proved in the primal without either a genuinely new greedy-dynamic ingredient that does NOT reduce to bounding primefactors$(k)$, or re-proving the cofactor bound (certified dead). Five candidate ingredients (window-uniqueness, multi-big-prime coincidence, blocker-incomparability, lock-prime triviality, spacing/density) were tested and documented as failed — all reduce to cofactor or fail to bound.

## Fencing value
The two lemmas fence off future primal-framing retries (any "primal minimal-support" attack is equivalent to Gap A by Lemma 1; any "window-local greedy-minimality" attack unpacks to the cofactor wall by Lemma 2). This is the round-4 fallback contribution mandated by the outline-reviewer.

## Tools / cruxes used
- `linchpin-and-gap-bound` (gap bound $d_n\le M_1$) — certified R1.
- `mt-depends-on-set-system` (MT depends only on distinct member-sets) — certified R2; symmetric variant used for primal.
- `binfinity-divisibility-progression-structure` ($\mathcal B_\infty=\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}\operatorname{rad}(T)\mathbb Z$) — certified R3.
- `cyclic-successor-bijection` + `greedy-equals-cyclic-successor` (endgame) — certified R1.
- `lock-lemma`, `syndetic-divisible-closed-not-periodic` (guardrail), `aimo-0134-obstruction` (fence).
- Classical blocker involution on clutters (Edmonds–Fulkerson 1970; Schrijver) — named hypergraph-theoretic identity, proved finite-combinatorial, does not presuppose Gap A. No crux from `crux_moves_documentation.md` supplies the confinement/finiteness bound (`aimo-0577` endgame-structural match already certified; the confinement step requires single-modulus $\gcd(a,d)=1$ absent here).
- Computations: reused `/tmp/round-4/analyze385.py`, `multicheck.py`; new probes `duality_probe.py`, `transient_probe.py`, `transient2.py`, `transient3.py`, `window_probe.py` (all under `/tmp/round-4/`).

## Files touched
- `/home/agentuser/repo/results/imo-2026-06/approaches/primal-minimal-support-stabilization.md` (the approach; full proof with two lemmas in full, conditional chain rigorous modulo Step 4, Step 4 honestly open).

## verdict-request: CHANGES REQUESTED
The approach is partial: two reusable structural lemmas are proved in full (proposed for certification), the conditional chain is rigorous modulo the open Step 4, and the framing is honestly fenced off as equivalent to Gap A. Not solved; the load-bearing Step 4 cannot be closed with the current primal mechanism (Lemma 2). The negative-equivalence contribution is genuine progress on a deep-stall problem but does not solve the theorem.
