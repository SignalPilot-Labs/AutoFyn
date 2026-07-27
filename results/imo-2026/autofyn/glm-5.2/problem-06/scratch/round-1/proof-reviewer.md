# Proof review — IMO 2026 Problem 6 (round 1)

Reviewer verdicts (per approach). All three approaches are **partial**: each correctly and rigorously reduces the whole theorem to the single open wall "the family $\mathcal M=\min\{P(a_i):i\ge1\}$ of minimal prime-supports is finite," and each proves a complete conditional pipeline (transversal-residue characterization, universal-membership/no-transient, greedy=cyclic-successor, single-cycle, period-sum=$L$). The wall itself is attacked by α (Mertens density) and β (Bertrand + Dickson), but neither closes. δ deliberately leaves the wall to the others and only states the conditional theorem.

## Computational verification (python3 + sympy)

I independently re-derived the transversal/cycle structure for the requested cases:

- **$a_1=15$.** $\mathcal M^*=\{\{2,3\},\{2,5\},\{3,5\}\}$, $P=\{2,3,5\}$, $L=30$, $V=\{0,6,10,12,15,18,20,24\}$, $T=8$. Confirmed: every $a_n\bmod 30\in V$ (no transient), the cyclic successor on $V$ reproduces the greedy sequence from $n=1$, and $a_{n+8}=a_n+30$ for all $n$ in range. Matches δ's claim exactly.
- **$a_1=429=3\cdot11\cdot13$.** $\mathcal M^*$ has 5 supports ($\{2,3\},\{2,5,11\},\{2,5,13\},\{3,5\},\{3,11,13\}$), $P=\{2,3,5,11,13\}$, $L=4290$, $|V|=908$. Confirmed (2000 terms): universal membership, cyclic-successor reproduces from $n=1$, $a_{n+908}=a_n+4290$. Matches δ. Also observed $\mathcal M_n$ is NOT monotone — supports get refined away ($\{29,3,5\}$, $\{3,5,31\}$, $\{11,3,5\}$ appear in $\mathcal M_{20}$ then vanish), confirming the well-founded-refinement structure β's Lemma 4 describes.
- **$a_1=30$ (the antichain correction).** $P(a_1)=\{2,3,5\}\in\mathcal M_1$; then $a_2=32$ so $\{2\}\in\mathcal M_2\supsetneq$-refines $\{2,3,5\}$. Both $\{2,3,5\}$ and $\{2\}$ are ever-minimal, with $\{2\}\subsetneq\{2,3,5\}$. So ever-minimal supports are **NOT** an inclusion-antichain. β's self-correction (Remark after Lemma 4) is verified and correct. The sequence then freezes ($L=2,T=1$, $a_{n+1}=a_n+2$) — the singleton-freeze case.

## Judgment of the shared conditional lemmas (judged once)

These appear in all three approaches; I re-derived each from scratch.

1. **Transversal characterization / free-rider invisibility.** "$m$ admissible iff $m\bmod L\in V$." Uses $\bigcup\mathcal M=P$ (so primes outside $P$ lie in no minimal support and are invisible to the hitting condition) and CRT over squarefree $L$. **Correct.** No induction hiding here — under GAP it is the one-liner δ says it is.
2. **Universal membership / no-transient.** "Every $a_n\bmod L\in V$." Argument: each $M'\in\mathcal M^*$ equals $P(a_j)$ for some $j$ (minimal elements are members of $\mathcal F$); by the greedy rule, every two terms share a prime (for $i<j$, $a_j$ was chosen with $\gcd(a_j,a_i)>1$), so $P(a_n)\cap M'\neq\emptyset$ by the trichotomy $j<n/j>n/j=n$. **Correct and airtight.** The "no transient" claim is genuine, not a gap — verified computationally. This discharges the outliner's transient-absorption worry.
3. **Greedy = cyclic successor.** Two inequalities: $V\subseteq V_n$ (hitting $\mathcal M^*$ implies hitting $\mathcal M_n$: each $M'\in\mathcal M_n$ either stays in $\mathcal M^*$ or contains some $M\in\mathcal M^*$, $M\subseteq M'$, so hitting $M$ hits $M'$) gives $a_{n+1}\le\min(V\cap(a_n,\infty))$; and $a_{n+1}\in V$ (Lemma 2) with $a_{n+1}>a_n$ gives $a_{n+1}\ge\min(V\cap(a_n,\infty))$. **Correct.**
4. **Single cycle.** The cyclic successor on the increasingly-listed finite set $V$ is tautologically the one cycle $(v_0\,v_1\,\cdots\,v_{k-1})$. **Correct, trivial.** The outliner's "several sub-cycles" worry was indeed a misdefinition (conflating with a pairwise-intersection-based jump map) — δ's dissolution is right.
5. **Period-sum $=L$.** Telescopes to $L$ since $v_0=0$. **Correct.**

So the conditional theorem "$\mathcal M$ finite $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$" is a **verified milestone**: a real, rigorous, useful result that closes everything except the wall.

## Wall-attack scrutiny

### α — `density-promotion-bound` — does the density argument prove $P$ finite? **No (honestly flagged).**

The density mechanism is set up (Mertens 3rd theorem stated as a named standard fact; Lemma 6 proves $V$ has density $\ge1/L$ *conditional on* $\mathcal M$ finite). But the builder explicitly identifies the monotonicity-direction obstruction: promoting a new prime into $P$ *adds* a minimal support and hence *shrinks* $R$ (and $V$), so a density lower bound on $V$ does not grow with $|P|$. The needed sub-lemma (D-weak: a bound $B$ on all primes appearing in any member of $\mathcal M$) is left as **GAP-D**. No overclaim — the Status is honestly `partial`. The conditional pipeline (Lemmas 1–5) is the same as δ's and is correct. **The density attack is the most promising route but is not closed.**

### β — `bertrand-dickson-eviction` — does Bertrand bound the count of essential primes, or is it circular? **Not circular, but too weak (honestly flagged).**

- Lemma 5 (gap bound at promotion): $a_i-a_{i-1}\le\prod_{p\in O}p$ where $O=P(a_i)\cap P_{\mathrm{ess},i-1}$. Re-derived: $P(a_i)$ is a transversal of $\mathcal M_{i-1}$; new primes $N$ lie in no member of $\mathcal M_{i-1}$ (else they'd be old), so the hitting is all done by $O$, making $O$ a transversal; multiples of $L_O=\prod O$ are then transversals; the smallest such above $a_{i-1}$ is within $L_O$, bounding the greedy choice. **Correct, non-circular** (uses only old essential primes, not the finiteness of $P_{\mathrm{ess}}$).
- But the bound depends on $a_{i-1}\to\infty$, so it bounds neither prime sizes nor promotion count. The Bertrand postulate is invoked but, as the builder honestly admits, there is no dyadic interval forced to contain a *new* essential prime — the gap structure is exactly what Lemma 5 bounds (with the $a_{i-1}$ dependence). So Bertrand does not evict. **No circularity; the obstruction is genuine $a_{i-1}$ growth.**
- Lemma 6 (Dickson): correctly noted to be moot — Dickson gives no infinite antichain only *after* a finite universe bound is known, and that bound IS the wall.
- The antichain claim: the builder self-corrected — ever-minimal supports are NOT an antichain (verified on $a_1=30$). The corrected Lemma 4 states only pairwise-intersection + well-foundedness, and explicitly notes this does not force finiteness (the $\{\{2,p\}\}$ counterexample). Honest and correct.

So β contributes a real proven partial result (Lemma 5) plus the same conditional pipeline, but the wall is open. Status honestly `partial`.

### δ — `transversal-single-cycle-finish` — conditional theorem only.

Does not attack the wall; states the conditional theorem in the cleanest form and discharges the single-cycle/transient/free-rider worries. All lemmas correct (as above). The distinctive output is the post-stabilization machine, which is the verified milestone. Status honestly `partial` (wall explicitly left as GAP).

## Per-approach verdicts

### `density-promotion-bound` (α)
- **Correctness:** high. Conditional pipeline (Lemmas 1–5) correct; density engine (Lemma 6) correct as a conditional; Mertens stated correctly.
- **Completeness:** GAP-D open. The density bound surviving correlated minimal-support constraints is the crux, not established. No skipped cases, no hand-waving beyond the explicit gap.
- **Progress:** full conditional reduction + the density attack set up and its precise obstruction identified.
- **True Status: partial.** Builder's Status (partial) is correct — no overclaim.
- **Verdict: CHANGES REQUESTED.** Gap to close: GAP-D — prove $\mathcal M$ finite (e.g. a density/inclusion-exclusion/LLL bound on $|R|/L$ *after* all promotions that beats the sparsity of multiples of any would-be new prime $q$, surviving the pairwise-intersecting-antichain correlation of $\mathcal M$).

### `bertrand-dickson-eviction` (β)
- **Correctness:** high. Lemmas 1–5 and 7–9 correct; antichain correction verified.
- **Completeness:** wall open; Lemma 5 insufficient; Bertrand does not evict (honestly admitted).
- **Progress:** Lemma 5 (gap bound at promotion) is a genuine proven partial result toward the wall; full conditional pipeline.
- **True Status: partial.** Builder's Status (partial) correct.
- **Verdict: CHANGES REQUESTED.** Gap to close: bound the *count* of promotions / essential primes without invoking $a_{i-1}$ — the current bound is too weak. Consider coupling Lemma 5 with a density argument (α's route) or a structural induction on $\omega(a_1)$.

### `transversal-single-cycle-finish` (δ)
- **Correctness:** high. Theorem A and Lemmas 1–5 fully rigorous under GAP; verified computationally on the two requested cases.
- **Completeness:** the conditional theorem is complete; the wall (GAP) is left to α/β by design.
- **Progress:** the verified milestone — the cleanest statement of the post-stabilization machinery.
- **True Status: partial** (wall open). Builder's Status (partial) correct.
- **Verdict: CHANGES REQUESTED.** (The conditional theorem itself is a verified milestone, but the approach as a whole is still partial because the wall is open.) Gap: prove $\mathcal M$ finite. This approach will not close the wall itself; it imports any proof of GAP from α/β.

## Certified promotable lemmas

All pass the full bar (statements correct, proved, conditional-only-where-flagged, no `sorry`, no stronger-than-proved). Admitted to `results/imo-2026-06/lemmas/`:

- `pairwise-intersection` (α Lemma 1, unconditional): every two terms share a prime; hence every $a_n$'s support hits $\mathcal M^*$.
- `transversal-residue-characterization` (δ Lemma 1 / α Lemma 2 / β Lemma 7, cond. on GAP): $m$ admissible iff $m\bmod L\in V$; free-rider primes invisible.
- `universal-membership-no-transient` (δ Lemma 2 / α Lemma 1 corollary / β Lemma 8 part 1, cond. on GAP): $a_n\bmod L\in V$ for every $n\ge1$.
- `greedy-equals-cyclic-successor` (δ Lemma 3 / α Lemma 3 / β Lemma 8 part 2, cond. on GAP): $a_{n+1}=\min\{m>a_n:m\bmod L\in V\}$.
- `cyclic-successor-single-cycle` (δ Lemmas 4–5 / α Lemma 5 / β Lemma 9, cond. on GAP): $\varphi$ is one $|V|$-cycle, period-sum $=L$.
- `post-stabilization-theorem` (δ Theorem A, cond. on GAP): $\mathcal M$ finite $\Rightarrow$ $a_{n+T}=a_n+L$ for all $n\ge1$.
- `gap-bound-at-promotion` (β Lemma 5, unconditional): at a promotion step $i\ge2$, $a_i-a_{i-1}\le\prod_{p\in O}p$ where $O=P(a_i)\cap P_{\mathrm{ess},i-1}$.
- `singleton-freeze` (β Lemma 2, unconditional): if $\{p\}\in\mathcal M_n$ then $\mathcal M$ is frozen from $n$.

No rejections — every flagged lemma passed.

## Goal Progress

- **Status: partial.** No approach solved; all three correctly reduce the theorem to the single wall "finiteness of $\mathcal M$."
- **Top approach context:** δ is the verified milestone (clean conditional theorem); α (density) is the most promising wall-attack but unproven; β (gap bound) is a proven partial result insufficient to close.
- **Single biggest blocker (the wall):** Prove the family $\mathcal M=\min\{P(a_i):i\ge1\}$ of minimal prime-supports is finite (equivalently, the essential-prime set $P_{\mathrm{ess}}=\bigcup\mathcal M$ is finite / $\mathcal M_n$ stabilizes). The crux sub-lemma (α's D-weak): a uniform bound $B$ on all primes appearing in any minimal support. The obstruction: promoting a new prime *shrinks* the valid set $V$, so density does not grow with $|P|$; and β's gap bound carries an $a_{i-1}\to\infty$ dependence. A density/LLL bound on transversal density surviving the pairwise-intersecting-antichain correlation of $\mathcal M$, or a structural induction bounding $|P_{\mathrm{ess}}|$ in terms of $\omega(a_1)$, is the natural next attack.
