# Proof Review — imo-2026-01, round 1

Problem: IMO 2026 P1 (the Confucius gcd/lcm blackboard, 2026 integers >1). Move replaces $(m,n)$ by $(\gcd(m,n),\,\operatorname{lcm}(m,n)/\gcd(m,n))$. (a) termination with exactly one $M>1$; (b) $M$ is choice-independent. `answer_type: none` (proof only).

## Approach 1: `perprime-gcd-lexmonovariant` — Status claimed: solved

### Load-bearing steps independently re-derived

1. **Per-prime move action** $(\alpha,\beta)\mapsto(\min(\alpha,\beta),|\alpha-\beta|)$. Correct: $v_p(\gcd)=\min$, and $v_p(\operatorname{lcm}/\gcd)=\max-\min=|\alpha-\beta|$. Verified.

2. **Invariant $D_p=\gcd$ of the $p$-valuation multiset.** The Euclidean identity $\gcd(\min(\alpha,\beta),|\alpha-\beta|)=\gcd(\alpha,\beta)$ (proof's (I3)) is correct: wlog $\alpha\le\beta$, then $\gcd(\alpha,\beta-\alpha)=\gcd(\alpha,\beta)$ is the standard Euclidean step. Replacing the pair $(\alpha,\beta)$ in the multiset by two numbers with the same pairwise gcd leaves $\gcd$ of the whole multiset unchanged (gcd factors through pairwise gcds). Correct.

3. **$\Omega$-drop identity = $\Omega(g)$, NOT $2\Omega(g)$.** Per-prime: old contribution $\alpha+\beta$; new contribution $\min(\alpha,\beta)+|\alpha-\beta|=\max(\alpha,\beta)$; drop $=(\alpha+\beta)-\max(\alpha,\beta)=\min(\alpha,\beta)=v_p(g)$. Sum over $p$: $\Delta=\Omega(g)$. Verified computationally on 100,000 random pairs (0 mismatches). The proof's earlier slip is corrected in the right place and re-derived per-prime; the case-$(ii)$ algebra also gives $\Omega(g)$ via complete additivity. Correct.

4. **Lex monovariant $(\Omega,K)$, three exhaustive cases.**
   - (i) $g=1$: forces $m\ne n$ (since $m=n>1\Rightarrow g=m>1$). $\Omega$ unchanged, $ab\ge b>1$ so $K$ drops by 1. Correct.
   - (ii) $g>1$, $m\ne n$: $(a,b)\ne(1,1)$ so $ab\ge 2$, $K$ unchanged, $\Omega$ drops by $\Omega(g)\ge 1$. Correct.
   - (iii) $g>1$, $m=n$: $m=n=g$, new pair $(g,1)$, both $\Omega$ and $K$ drop. Correct.
   Exhaustive: $g=1$ or $g>1$; if $g=1$ then $m\ne n$; if $g>1$ then $m=n$ or $m\ne n$. All three cases covered, disjoint. Verified computationally (lex strict decrease on 500 random plays, all hold).

5. **Termination.** Lex order on $\mathbb{N}_0\times\{0,\dots,2026\}$ is well-founded; finite total move bound. Correct.

6. **Stuck $\Leftrightarrow K\le 1$.** Trivial (move needs two $>1$).

7. **Ruling out $K=0$.** Convention $\gcd(x,0)=x$, $\gcd(0,\dots,0)=0$. If terminal all-ones, $D_p=0$ for all $p$; by invariance $d_p=0$ for all $p$; $d_p=0$ forces all initial $p$-valuations to be $0$ (gcd of nonneg integers is $0$ iff all are $0$); hence all initial $a_i=1$, contradiction. The sharper positive-direction parenthetical is also correct *given the convention*: $\gcd(0,k)=k$, so zeros are identities and $d_p\ge 1$ whenever some initial entry is divisible by $p$. Verified.

8. **Part (b): $v_p(M)=d_p$, $M=\prod p^{d_p}$.** At terminal $\{M,1,\dots,1\}$, $D_p=\gcd(v_p(M),0,\dots,0)=v_p(M)$; invariance gives $v_p(M)=d_p$. Finitely many primes divide initial entries, so the product is finite. $M$ depends only on the initial board. Correct. Verified computationally: initial $\{12,18,30,7,100,9,25\}$ gives $M=210$ across 200 random plays, matching $\prod p^{d_p}=2^1 3^1 5^1 7^1$; and $\gcd$ of the numbers $=1\ne M$, confirming the "M is not the gcd of the numbers" note.

### Verdict
Every load-bearing identity re-derived independently and verified. No gaps, no skipped cases, no hand-waving, no circularity. The corrected $\Omega(g)$ (not $2\Omega(g)$) drop is properly re-derived. The "exactly one $>1$" ruling-out of the all-ones terminus is rigorous (uses $d_p=0\Rightarrow$ all initial valuations zero). $M=\prod p^{d_p}$ is correctly derived; the $M\ne\gcd$ of numbers note is consistent and verified.

**Status: solved. Verdict: APPROVE.**

---

## Approach 2: `confluence-newman` — Status claimed: partial

### What is proven on this route

- **Part (a) in full** via the same $(\Omega,K)$ lex monovariant and $d_p$ invariant (Sections 2–3). The three-case analysis, the $\Omega(g)$ drop identity (with proof via complete additivity, $\Omega(h)=\Omega(m)+\Omega(n)-2\Omega(g)$, so $\Omega(g)+\Omega(h)=\Omega(m)+\Omega(n)-\Omega(g)$), termination, stuck$\Leftrightarrow\le 1$, and ruling out $K=0$ are all correct and match the approved approach. Part (a) is genuinely solved on this route.

- **Part (b): reduction to local confluence.** Newman's lemma (1942) is stated precisely and correctly: terminating + locally confluent $\Rightarrow$ confluent $\Rightarrow$ unique normal form. The system is terminating (proven), so (b) follows from local confluence. Correct reduction.

- **Local confluence $\to$ two critical-pair shapes.** The case split (A disjoint, B overlapping, C coincident) is exhaustive on pairs of positions; case C is trivial (symmetric rule, no divergence). Correct.

- **Case A (disjoint redexes) proven.** Disjoint moves act on independent entries; one-step commutation gives the common reduct. Correct.

### The gap (case B)

- **Case B (overlapping redexes, three entries $\{a,b,c\}$, moves on $(a,b)$ vs $(a,c)$): NOT proven.** The approach honestly admits this. No explicit common reduct is exhibited. The natural symmetric two-step completion fails (4869/5000 random triples). No fixed 1-step mutual completion exists (e.g. $\{35,16,42\}$). Joins are real but deep (up to $3+3=6$ moves) with no fixed pattern. The per-prime 1D local confluence argument (which works because the 1D system has unique normal form $\{d_p,0,\dots,0\}$) does NOT lift to the whole-number system, because a whole-number move fires the per-prime move on all primes simultaneously and the per-prime joining sequences need not synchronize. This obstruction is correctly identified.

- **The confluence route's central step — local confluence at case B — is hand-waved in the sense that it is asserted true empirically (2000/2000) but NOT proven.** The approach is honest about this: it explicitly does not present empirical confirmation as a proof step. So the route is genuinely `partial`, not `solved`.

### Verdict
Part (a) solved on this route; part (b) reduced correctly to the open case-B joinability. The local-confluence / critical-pair-joinability step is the load-bearing gap: it is *not* proven with an explicit common reduct, and the approach admits this. This is real progress (correct reduction machinery + half of local confluence proven) but a real gap remains.

**Status: partial. Verdict: CHANGES REQUESTED.**

**Specific gap to close:** prove case-B joinability — exhibit, for arbitrary $\{a,b,c\}>1$, an explicit common reduct of
$$B_1=\{\gcd(a,b),\,\operatorname{lcm}(a,b)/\gcd(a,b),\,c\},\quad B_2=\{\gcd(a,c),\,b,\,\operatorname{lcm}(a,c)/\gcd(a,c)\},$$
or prove it via a genuine lifting argument (not the failed per-prime synchronization). The empirical evidence (2000/2000) suggests it is true, but a proof is required. Alternatively, abandon the confluence framing and route (b) through the direct $d_p$ invariant (which is already the APPROVE'd approach).

---

## Shared lemma: `perprime-invariant-and-lexmonovariant.md`

Certify. The lemma (per-prime move action, $D_p$ invariance, $(\Omega,K)$ lex monovariant with the $\Omega(g)$ drop and exhaustive three-case analysis) is proved in full in the APPROVE'd approach. Statement is correct and no stronger than what is proved; `sorry`-free. Promotable to `results/imo-2026-01/lemmas/` (already present there). The lemma file's "Key identity used" correctly states $\Omega$-drop $=\Omega(g)$ (with the per-prime derivation), matching the corrected proof. Certified.

---

## Summary

- `perprime-gcd-lexmonovariant`: APPROVE (Status solved). Both parts complete and correct; verified computationally.
- `confluence-newman`: CHANGES REQUESTED (Status partial). Part (a) solved; part (b) reduced to open case-B local-confluence joinability — the load-bearing step is asserted empirically, not proven.

perprime-gcd-lexmonovariant: APPROVE
confluence-newman: CHANGES REQUESTED
