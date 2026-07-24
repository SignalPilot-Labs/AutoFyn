# Outline review — imo-2026-01 (round 1)

Problem: 2026 integers >1; move replaces m,n with gcd(m,n) and lcm(m,n)/gcd(m,n). (a) exactly one M>1
remains after finitely many moves; (b) M is choice-independent.

Computational sanity (ran over ~2000 random boards, 40 random play-orders each): every play halts with
exactly one survivor, the survivor is identical across all orders, and it equals ∏_p p^{g_p} with
g_p = gcd_i v_p(x_i). The whole field's shared core fact — move = (a,b)↦(min(a,b),|a-b|) per prime — is
confirmed. The false shortcuts (M=gcd, M=lcm) are correctly flagged and avoided.

---

## perprime-valuation — APPROVE (frontrunner, build)

Sound end to end and self-contained. The two engines are the right tools:
- Part (b) invariant g_p: `gcd(min(a,b),|a-b|)=gcd(a,b)` is a genuine one-step subtractive-Euclid
  identity (mechanism stated, edges a=b/a=0 handled), lifted to the multiset by associativity of gcd.
- Part (a) monovariant: lex (Ω_total, C) strictly drops — Ω_total by Ω(gcd(m,n)) when gcd>1, else C by 1
  in the gcd=1 subcase. Both branches present; ℕ² lex is well-founded. Correct.
- The subtle point is correctly identified: "exactly one" is NOT pure monovariant — ruling out zero
  survivors needs the (b) invariant (some g_p≥1). Step 5 supplies it. Good.

No circularity, all cases covered, both bound-and-value present. Builder should just close G1–G5 as stated;
none is a hidden hard lemma — they are rigor/bookkeeping (unique factorization for L1, gcd-with-0
conventions for L2, summation bookkeeping for L3). This is the clear build target.

## descent-induction — APPROVE (build as the second, diversity route-B)

Technique (minimal-counterexample on lex (Ω_total,C)) is valid and olympiad-idiomatic. Cases identical /
disjoint-commute / share-one-cell are the correct and complete first-move trichotomy. Verified: for the
share-one 3-cell obstacle {4,6,9}, the two branches {2,6,9} and {3,4,6} DO have genuine common reducts
before the terminal (e.g. (2,3,6),(1,2,3)), so joinability is real, not vacuous — G1 is closable.

CHANGES-REQUESTED-level caveats for the builder (do not block, but must be honored):
- **The 3-cell joinability (G1) must exhibit an explicit common reduct or invoke the g_p invariant
  DIRECTLY (prime-by-prime), never "both reach a normal form and normal forms are unique" — that is
  circular** (it assumes the very uniqueness being proved). Import perprime-valuation L2 as the
  certificate; that dependency is honest, not circular.
- Well-foundedness of the descent and that each case routes both plays through a *strictly smaller*
  common board must be explicit before invoking minimality.

Honest diversity assessment: this proves (b) without ever naming ∏p^{g_p}, which is a genuinely different
write-up matching exactly what part (b) asks — real value. But it leans on the same gcd fact as the
primary, so it is diversity-of-framing, not a fully independent route. Acceptable as the second build.

## confluence-newman — APPROVE (register, do NOT build this round)

Technique (ARS + Newman's Lemma) is sound: WCR here is *multi-step* joinability (the {4,6,9} branches meet
at common reducts, verified), so the route is NOT the false one-step diamond and is NOT inherently
circular. Its part (b) = uniqueness of normal form is the cleanest match to the question.

Reason it is not in the build set: it is **mathematically the same proof as descent-induction** — Newman's
Lemma is itself proved by well-founded induction on the terminating order, i.e. the minimal-counterexample
descent. It shares the identical 3-cell crux and the same L2 import, but carries an *extra* obligation
(state and prove Newman's Lemma from scratch, absent from the KB) with no compensating gain over descent.
For a builder who must produce full rigor, that extra machinery is pure added gap-surface. So between the
two route-B siblings, descent-induction dominates on rigor-risk for identical diversity. It stays in the
population (ranked just below descent) as a backup framing; if descent stalls on G1 next round, promote it.

---

## Field / diversity note for the orchestrator

All three approaches rest on the SAME load-bearing fact: the per-prime subtractive-Euclid identity and the
g_p = gcd_i v_p(x_i) invariant. The two route-B approaches (descent, confluence) additionally share one
crux (3-cell joinability) and both must import L2. This is a low-diversity field — a single wall (the gcd
invariant) underlies everything. It is not alarming here because the primary is complete and elementary and
the core fact is verified true, so the field is not at risk of a shared *dead end*; but if perprime-valuation
were to hit trouble, the siblings would not rescue it. No action needed this round (problem looks
straightforwardly solvable via the primary). If it plateaus, next round's outliner should seek a framing
that does not route through g_p (e.g. a direct pairing/group-structure argument on ∏ ℤ/… ), though none is
needed on current evidence.

Ranking: perprime-valuation 1531 > descent-induction 1501 > confluence-newman 1468.

build set: perprime-valuation, descent-induction
