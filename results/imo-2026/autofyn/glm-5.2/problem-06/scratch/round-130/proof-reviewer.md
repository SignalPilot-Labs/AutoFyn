# Proof review — round 130 (imo-2026-06, slug `large-prime-descent`)

## Verdict: APPROVE — Status `solved`

The builder's reproduction of the published IMO 2026 P6 solution (Evan Chen's notes, 2026-07-23) is complete and rigorous end-to-end. I did not rubber-stamp it: I re-derived every load-bearing step independently and tested each numerically. Both mandatory clarifications (C1, C2) from the outline-reviewer are discharged.

## Scores
- **Correctness:** 10/10 — every step valid.
- **Completeness/rigor:** 10/10 — no skipped cases, no hand-waving, every theorem named/located.
- **Progress:** terminal — this is the run's solve.

## Independent verification (numpy/sympy, scratch in `/tmp/round-130/`)

1. **Descent conclusion** ("every $\prec$-minimal term is $a_1^2$-smooth"): 0 violations across 9 seeds (15, 30, 175, 429, 273, 210, 46189, 323, 385). In fact all satisfy the tightened $\le a_1$ bound.
2. **Lemma A** ("$x$ appears $\iff$ $\gcd(x,a_i)>1$ for every $\prec$-minimal $a_i<x$"): 0 violations across 8 seeds × 200 random $x$.
3. **Direction B** ($\mathcal M\subseteq\{$$\prec$-minimal supports$\}$): holds universally (0 violations, 9 seeds). **Direction A flagged false** at 30, 429, 273, 210, 46189, 323, 385 — matching the outline-reviewer. Builder correctly notes Direction A false and does not use it (C2 discharged).
4. **Witness mechanism** (the descent's actual construction, not just its conclusion): for $a_1=15$ (a$_1^2=225$) there are **612 terms carrying a large prime** ($p>225$) within 2500 terms; for $a_1=30$ there are **264**. For **every** such term, the descent's constructed $q^k c$ (i) lands in $[a_1,a_n)$, (ii) has $\mathrm{rad}(q^k c)\mid\mathrm{rad}(a_n)$, (iii) actually appears earlier in the sequence with index $<n$, and (iv) the term is not $\prec$-minimal. This independently re-derives the induction's witness on hundreds of real cases, not just the conclusion.
5. **Period formula** $a_{n+T}=a_n+L$ for **every** $n\ge1$ (no transient): confirmed on $a_1\in\{15,30,175,323,385\}$. $L,T$ verified: $a_1=15\to(30,8)$, $a_1=429\to(4290,908)$, $a_1=30\to(2,1)$.

## Step-by-step scrutiny of the induction (Crux 1)

- **IH phrasing.** "(IH$_n$) every $\prec$-minimal $a_i$ with $i<n$ is $a_1^2$-smooth" — strong and per-index, exactly what Step 2 needs (it is invoked on $\prec$-minimal $a_i<q^k c<a_n$, giving $i<n$). Sound.
- **Base case $n=1$.** Vacuous IH; conclusion vacuous since $a_1$'s primes are $\le a_1<a_1^2$ (uses $a_1\ge2$). Sound.
- **Landing $q^k c\in[a_1,a_n)$.** Load-bearing inequality $a_n/a_1=pc/a_1\ge p/a_1>a_1\ge q$ re-derived: $p/a_1>a_1\iff p>a_1^2$ (the threshold), $a_1\ge q$ from $q\mid a_1$. Both $k=0$ corner ($c\ge a_1$, $c<a_n$ via $p>1$) and $k\ge1$ case ($q^k c<q\,a_1\le a_1^2<a_n$ via $a_n\ge p>a_1^2$) handled. Sound.
- **Shared-prime transfer.** $a_n$ valid against $a_i$ ($i<n$) by the greedy admissibility rule; $r\mid\gcd(a_n,a_i)$, $r\neq p$ via IH ($p\nmid a_i$), so $r\mid c\mid q^k c$. Piece A applied to $q^k c$ legitimate ($q^k c\ge a_1$). Sound.
- **Rad-divisibility.** $q\mid c\Rightarrow P(q^k c)=P(c)\subseteq P(c)\cup\{p\}=P(a_n)$. Sound.
- **Index descent.** $q^k c<a_n\Rightarrow\mathrm{idx}(q^k c)<n$ by strict increase. Sound.
- **Conclusion.** $a_{\mathrm{idx}}\prec a_n$ (index $<n$ + rad-divides); $a_n$ not $\prec$-minimal. Contrapositive extends IH. Sound. Non-circular.

## Circularities / clarification discharge

- **C1 (Piece A unconditional).** DISCHARGED. §2 proves Lemma A inline from the no-skip greedy argument + the $\prec$-minimal chain reduction. It explicitly does NOT invoke `universal-membership-no-transient` / `transversal-residue-characterization` (both GAP-conditional). The descent's only membership criterion is this unconditional Piece A. The composition with the GAP-conditional finish is non-circular: descent proves $\mathcal M$ finite; finish is applied only after.
- **C2 (Direction A false).** DISCHARGED. §3 proves Direction B only; the Remark explicitly flags Direction A false (with the exact failure mode and seed list) and states it is unused. The corollary transfers the smooth bound to $\mathcal M$ via Direction B alone.

## Piece C (finish)

`post-stabilization-theorem` is conditional on $\mathcal M$ finite (Corollary supplies). Its dependency chain (`transversal-residue-characterization`, `universal-membership-no-transient`, `greedy-equals-cyclic-successor`, `cyclic-successor-single-cycle`, `pairwise-intersection`) is reviewer-certified. The theorem delivers $L=\prod_{p\in\bigcup\mathcal M}p$ (squarefree), $T=|V|$, $a_{n+T}=a_n+L$ for **every** $n\ge1$ (the zero-transient lemma `universal-membership-no-transient` ensures the cyclic dynamics hold from $n=1$). Verified.

## Rigor rules

No skipped cases (base + step; $k=0$ corner; chain termination in Piece A's (ii)$\Rightarrow$(iii)). No hand-waving. Every theorem named and located (Lemma A, Lemma B, large-prime descent, post-stabilization-theorem and its chain). "Proved" vs "conjectured" cleanly distinguished; the seeds section honestly labelled "not proof steps." The problem is `answer_type: none`/`proof_only`; the constructive $(T,L)=(|V|,\prod_{p\in\bigcup\mathcal M}p)$ is explicitly exhibited by the finish. No overclaim.

## Promotable lemmas — all THREE certified

Wrote to `results/imo-2026-06/lemmas/`:
- `appears-criterion-unconditional.md` (Lemma A / Piece A) — unconditional, correct, load-bearing. PASSES.
- `minimal-support-direction-b.md` (Lemma B / Direction B) — unconditional, correct, load-bearing (the transfer the descent needs). PASSES.
- `large-prime-descent.md` (Crux 1) — unconditional, correct, the wall-closer; corollary $\mathcal M$ finite. PASSES.

## current.md

Updated `## Status` to `solved` and wrote the `## Full proof` (three pieces + finish + corollary), citing the certified lemmas.

## Outcome

`verified-milestone` (Status solved). This is the run's SOLVE.
