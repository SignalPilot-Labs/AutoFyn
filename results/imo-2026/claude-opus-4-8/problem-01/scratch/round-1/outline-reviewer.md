# Outline review — imo-2026-01 (IMO 2026 P1)

Problem: 2026 integers >1; a move replaces m,n by gcd(m,n) and lcm(m,n)/gcd(m,n).
(a) exactly one M>1 survives after finitely many moves; (b) M is choice-independent.

I ran a 2000-board random simulation (2 <= N <= 7, entries in [2,60], 15 random
play-outs each). Every play-out terminated with **exactly one** entry >1, that
value was the **same across all 15 play-outs** of a board, and it equaled
`prod_p p^{d_p}` with `d_p = gcd` of the p-valuations. Zero counterexamples. The
mathematical spine of all three approaches is confirmed.

## Shared correctness checks (the dispatch's three flags)

- **"exactly one, not zero, not two."** Not two: termination means no move is
  possible, and a move only needs two entries >1, so the terminal count is <=1.
  Not zero: if the terminal board were all 1's then every E_p = {0,...,0}, so
  d_p = 0 for all p; by invariance the *initial* d_p = 0 for all p, contradicting
  d_{p_1} >= 1 for a prime p_1 dividing x_1. This is **not circular**: M>1 comes
  from the initial d_{p_1} >= 1 plus invariance, independent of the terminal
  read-off (the read-off only *computes* M once exactly-one is known). Sound in
  all three files. The "C drops by at most 1 per move" remark is a correct but
  redundant extra; the M>1 + termination pair already gives exactly-one.
- **Per-prime invariant extends to the whole multiset.** gcd(min(a,b),|a-b|) =
  gcd(a,b) preserves the gcd of the touched pair; the rest are untouched, and
  gcd(gcd(pair), rest) = gcd(whole) by associativity of gcd. This is the correct
  mechanism; each file flags it (GAP-4) rather than hand-waving it. Approved.
- **product-count lex is well-founded.** (P,C) on N x N with lexicographic order
  is a well-order, hence no infinite strictly-decreasing chain. Concretely: P is a
  positive integer that only decreases, so it takes finitely many values; between
  consecutive P-drops every move has g=1 and strictly lowers C (bounded by N), so
  only finitely many such moves. Valid. GAP-2 correctly demands this be *argued*,
  not asserted — the file's own "Watch out for" says the same. Approved.

## Per-approach verdicts

### omega-count-monovariant — APPROVE
W = sum_i Omega(x_i) + #{x_i>1}, non-negative integer. The 3-case move analysis
(g=1: Omega-sum flat, count -1; g>1 & m=n: Omega-sum -Omega(g)<=-1, count -1;
g>1 & m!=n: Omega-sum -Omega(g)<=-1, count 0) is correct and each case strictly
drops W. Case 3's "ab>1" claim is right: a!=b with gcd(a,b)=1 forces max(a,b)>=2.
Most elementary, tightest (a); likely the intended route. Gaps GAP-1..6 are the
right hard steps and each carries a stated mechanism. No changes needed.

### valuation-gcd — APPROVE
Same termination quantity as omega-count (T = sum Omega, plus C) but derived
through the per-prime picture, with the bridge identity
`sum_p min(v_p m, v_p n) = Omega(gcd(m,n))` linking per-prime S_p drops to the
Omega(g) drop — that identity is the one genuinely extra step vs. omega-count and
is correctly flagged (GAP-3). Strongest framing for (b): the invariant and the
monovariant are two faces of one Euclidean-step lemma. GAP-6 (finiteness of the
product: only primes dividing some initial entry have d_p>0) is correctly called
out. Approve.

### product-count-monovariant — APPROVE
Genuinely distinct termination mechanism (lexicographic (P,C), P the board
product) — the best route-diversity hedge, since it does not touch Omega at all
for (a). Product identity P_after = P_before/gcd(m,n) via g*(ab)=lcm(m,n)=mn/g is
correct. The one extra burden vs. the other two is the lex well-foundedness
argument (GAP-2), which is why it sits slightly below in the ranking, but it is
fully salvageable and correct. Approve.

## Route-diversity note
omega-count and valuation-gcd share the *same* termination monovariant
(sum Omega + count) — they differ only in framing (direct integer bookkeeping vs.
per-prime reduction). They are not the single-line trap because (b) is powered by
the invariant, not the monovariant, and the invariant is independently sound; but
the reviewer should note that if sum-Omega+count ever failed, both would fall
together. product-count is the true termination hedge. The (b)/invariant half is
shared by all three and is the natural candidate for a cached lemma
(`euclid-step-invariant`: gcd(min,|diff|)=gcd + v_p(gcd)/v_p(lcm) action).

## Ranking (registered + updated this round)
- valuation-gcd 1516.8
- omega-count-monovariant 1514.5
- product-count-monovariant 1468.7
(Top two at parity — draw between them; both beat product-count, which carries
the extra lex-well-foundedness step.)

## Build guidance
Build all three in parallel — they are short, fully outlined, and share
GAP-1/2/4/6 (key identity, valuation action, whole-multiset invariant, terminal
read-off). Have the first builder to certify the shared invariant deposit it as
`results/imo-2026-01/lemmas/euclid-step-invariant.md` for the others to import.

build set: omega-count-monovariant, valuation-gcd, product-count-monovariant
