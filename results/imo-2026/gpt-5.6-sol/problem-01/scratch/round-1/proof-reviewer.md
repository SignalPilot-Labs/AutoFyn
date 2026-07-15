## product-support-descent

**Verdict:** APPROVE  
**True Status:** solved (the builder's recorded Status is correct)  
**Scores:** Correctness 10/10; Completeness / rigor 10/10; Progress 10/10.

The proof answers both parts of the actual problem: it proves finite termination with exactly one terminal nonunit and proves that this nonunit is independent of all move choices.

The load-bearing termination identity was independently re-derived. For \(d=\gcd(m,n)\) and \(L=\operatorname{lcm}(m,n)\), the replacement product is \(d(L/d)=L=mn/d\), hence \(P(B')=P(B)/d\). If \(d=1\), the pair becomes \((1,mn)\), so \(r\) falls by one and \(F=2^rP\) is halved. If \(d>1\), \(r\) cannot increase and \(P\) is divided by \(d\ge2\), so \(F\) again strictly decreases. This is an integer-valued, bounded-below monovariant and proves termination without an omitted equal-input case.

The load-bearing valuation transformation was also independently checked:
\[
(x,y)\mapsto(\min(x,y),|x-y|).
\]
All configurations are present: \((0,0)\), exactly one zero in either order, unequal positive exponents in either order, and equal positive exponents. In each configuration the selected places have positive support after the move exactly when they had it before, and their positive exponents have the same common divisors. The argument explicitly adjoins unchanged exponents, so it establishes the global gcd invariant rather than merely a two-entry invariant. It also separately excludes new primes.

Consequently every initially occurring prime persists, so a terminal board cannot be all ones. Terminality gives at most one nonunit, and persistence gives at least one, establishing the exact-one claim. At the terminal board each occurring prime has the singleton positive valuation \(v_p(M)\), forcing \(v_p(M)=g_p\); absent primes remain absent. Unique factorization then proves the displayed formula for \(M\), which establishes choice-independence.

Small-case computational verification over every pair \(2\le m,n<80\) reproduced the strict scalar descent and all positive-valuation gcd identities.

**Promotable lemmas:** Certified `product-support-termination` and `positive-valuation-euclidean-invariant`; both are fully proved and stated no more strongly than the proof warrants. They were admitted to the shared lemma cache.

**Ranking outcome recorded:** `verified-milestone` for round 1. Elo remains 1514.5981711137829 pending the next ranking update; expanded is now 1 and stale is true.

## omega-lexicographic-euclid

**Verdict:** APPROVE  
**True Status:** solved (the builder's recorded Status is correct)  
**Scores:** Correctness 10/10; Completeness / rigor 10/10; Progress 10/10.

This is a self-contained complete proof, even though its identification stage uses the same natural primewise invariant as the other approach. It does not cite or depend on the other approach.

The load-bearing termination computation was independently re-derived. Complete additivity of \(\Omega\), \(mn=dL\), and \(L=d(L/d)\) imply
\[
\Omega(m)+\Omega(n)-\Omega(d)-\Omega(L/d)=\Omega(d).
\]
Thus \(S(B)-S(B')=\Omega(d)\). For \(d>1\), \(S\) strictly decreases. For \(d=1\), the replacement is \((1,mn)\), so \(S\) is fixed and \(r\) decreases by one. The lexicographic termination explanation is sound: \(S\) has only finitely many possible strict decreases from its finite initial value, and each constant-\(S\) run contains at most 2026 strict decreases of \(r\). No possibility of infinitely many alternating runs is left, because there are only finitely many decreases of \(S\).

The valuation transformation and all zero/equality/order cases are correctly and exhaustively handled. In particular, support cannot vanish in the equal-positive case, since \((x,x)\mapsto(x,0)\), and no prime can appear from \((0,0)\). The proof correctly explains why adjoining all unchanged positive exponents preserves equality of the global sets of common divisors. This establishes support persistence and the invariant \(I_p\).

The exact-one and independence deductions are complete: persistence of every initially occurring prime rules out the all-ones terminal board; inability to move gives at most one nonunit; and the terminal singleton valuations determine the same integer
\[
M=\prod_{p\in P}p^{g_p}
\]
for every play. The initial prime set is correctly shown finite and nonempty.

Small-case computational verification over every pair \(2\le m,n<80\) reproduced the exact \(\Omega\)-change and all positive-valuation gcd identities.

**Promotable lemmas:** Certified `lexicographic-multiplicity-descent` and `positive-valuation-euclidean-invariant`. The latter coincides with the already certified shared lemma, so only one cache file is needed. Both statements are fully justified.

**Ranking outcome recorded:** `verified-milestone` for round 1. Elo remains 1517.4018288862171 pending the next ranking update; expanded is now 1 and stale is true.

## Workspace decision

`current.md` is set to `solved` and contains the shorter approved product-support proof. The shared lemma cache contains the two termination lemmas and the common positive-valuation invariant.

Goal Progress: solved — 2/2 built approaches APPROVE and have round-1 `verified-milestone` outcomes; `omega-lexicographic-euclid` leads the current Elo table at 1517.4018288862171, followed by `product-support-descent` at 1514.5981711137829 (both expanded=1, stale=true pending outline-reviewer ranking update); the other registered approaches remain unbuilt.
