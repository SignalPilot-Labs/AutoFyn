# Outliner report — imo-2026-01 (IMO 2026 P1)

## imo-2026-01

The mathematics is fully scouted and converges across all three explorers.
Per prime p, a move sends the valuation pair (v_p m, v_p n) -> (min, |diff|)
(subtractive Euclidean step). Invariant per prime: d_p = gcd of the whole
valuation multiset, via gcd(min(a,b),|a-b|)=gcd(a,b). Terminal survivor
M = prod_p p^{d_p}. Part (a) = termination monovariant + "M>1 so exactly one";
part (b) = the d_p invariant reads off M uniquely. The rivals differ in the
TERMINATION MONOVARIANT and in how (a) connects to (b). Population was empty;
these are three new approaches. No cheap one-move kill avoids both parts —
(a) genuinely needs a strict monovariant, (b) genuinely needs the invariant.

Retrieved cruxes that transfer: **aimo-0440** (blackboard subtractive Euclidean
step, L1-norm monovariant, gcd as preserved quantity), **aimo-0236** (v_p as
monovariant + invariant), **aimo-0893** (Euclidean step preserving gcd) —
adapted into the key identity and d_p invariant below. All must be proved from
scratch; they are hints, not citations.

---

omega-count-monovariant: new
Target: full problem (a)+(b): exactly one M>1 survives after finitely many moves,
  and M is choice-independent.
Technique: single integer monovariant W = sum_i Omega(x_i) + #{x_i>1} (Invariants
  & monovariants, KB line 117) with 3-case move analysis for (a); per-prime
  d_p = gcd(v_p) invariant for (b), separately.
Skeleton:
  1. Move normal form (m,n)->(g, ab), g=gcd(m,n) — by lcm/gcd = mn/g^2 = ab.
  2. W strictly decreases by >=1 each move — by 3-case Omega+count analysis.
  3. W>=0 integer => process stops with <=1 entry >1 — by well-ordering.
  4. d_p = gcd(v_p multiset) invariant — by gcd(min,|diff|)=gcd(a,b).
  5. Terminal survivor M has v_p(M)=d_p, so M=prod p^{d_p}, choice-independent.
  6. M>1 (some d_{p_1}>=1) + "count drops <=1 per move" => exactly one survivor.
Key lemmas (claim + mechanism):
  - gcd(min(a,b),|a-b|)=gcd(a,b) — because it is the subtractive Euclidean step
    gcd(a,b)=gcd(a,b-a); handles a=b, a=0 via gcd(k,0)=k.
  - W drops each move — because Omega-sum drops by Omega(g) (>=1 if g>1, 0 if g=1)
    and the count-of-(>1) drops by 1 exactly when g=1 produces a 1.
  - M>1 — because every initial entry >1 has a prime factor p_1, so
    d_{p_1}=gcd(...,v_{p_1}(x_1),...) >= 1.
Open gaps: GAP-1..GAP-6 in the approach file (key identity; valuation action;
  W all 3 cases incl. ab>1 in case 3; whole-multiset invariant; exactly-one
  bridge; terminal read-off).
Cases to cover: move cases g=1 / g>1&m=n / g>1&m!=n; terminal count 0 vs 1.
Watch out for: Omega-sum alone is not strict (flat at g=1) — the +count term is
  load-bearing; case 3 needs ab>1; gcd(k,0)=k convention.

---

product-count-monovariant: new
Target: full problem (a)+(b), as above.
Technique: lexicographic monovariant (P, C), P = product of whole board,
  C = #{>1}; each move divides P by g or (if g=1) fixes P and drops C. (b) via
  the same d_p invariant.
Skeleton:
  1. P_after = P_before / gcd(m,n) — by g·(ab)=lcm(m,n)=mn/g.
  2. (P,C) strictly lex-decreases each move — P drops if g>1, else C drops.
  3. Lex order on non-neg integer pairs is well-founded => termination, C<=1.
  4. d_p invariant; M=prod p^{d_p}; M>1; exactly one survivor. (shared with above)
Key lemmas (claim + mechanism):
  - P divides by g each move — because the two outputs multiply to lcm(m,n)=mn/g.
  - Lex termination — because P (>=1) strictly decreases only finitely often, and
    between P-drops C strictly decreases and is bounded by N.
  - d_p invariant + M>1 — same mechanisms as omega-count-monovariant.
Open gaps: GAP-1..GAP-6 in the file (product identity; lex well-foundedness;
  key identity+valuation action; whole-multiset invariant; M>1/exactly-one;
  terminal read-off).
Cases to cover: g>1 (P drops) vs g=1 (C drops); terminal count 0 vs 1.
Watch out for: P alone is NOT a monovariant — the lex well-foundedness must be
  argued, not asserted; keep the 1-entries in P consistently.

---

valuation-gcd: new
Target: full problem (a)+(b), as above.
Technique: unified per-prime framework — every board move is one subtractive
  Euclidean step in each valuation multiset E_p; termination from the total sum
  T = sum_i Omega = sum_p S_p (non-increasing) + count, uniqueness from d_p=gcd(E_p)
  invariant. Both parts are two facets of ONE step-lemma.
Skeleton:
  1. Board move = (min,|diff|) step in every E_p simultaneously — by valuation of
     gcd/lcm.
  2. Each S_p non-increasing (drops by min(alpha,beta)); T = sum Omega drops by
     Omega(g); with C, (T,C) strictly decreases => termination, C<=1.
  3. d_p = gcd(E_p) invariant (Euclidean identity) => M=prod p^{d_p} unique, M>1,
     exactly one survivor.
Key lemmas (claim + mechanism):
  - min(a,b)+|a-b| = max(a,b) => S_p drops by min(a,b) >=0 — bridge
    sum_p min(v_p m, v_p n) = Omega(gcd(m,n)) links per-prime drops to Omega(g).
  - gcd(min,|diff|)=gcd(a,b) => d_p invariant.
Open gaps: GAP-1..GAP-7 in the file (valuation action; key identity; S_p drop &
  Omega bridge; whole-multiset invariant; termination+exactly-one; product
  finiteness; terminal read-off).
Cases to cover: g>1 (T drops) vs g=1 (T flat, C drops); terminal count 0 vs 1.
Watch out for: do NOT argue "each E_p terminates independently" — one board move
  steps all primes at once, so termination needs ONE global monovariant (T+C);
  keep per-prime only for the invariant.

---

## Nomination for the build set
All three are NEW and should be REGISTERED by the outline-reviewer (population
was empty; no .ranking.json yet). Recommend building all three in parallel —
they are short, fully-outlined, and share GAP-1/2/4/6/7 (key identity, valuation
action, whole-multiset invariant, terminal read-off), so a certified lemma from
whichever builder finishes first can be cached in results/imo-2026-01/lemmas/
and imported by the others. Priority if only two builders run:
  1. omega-count-monovariant (most elementary, likely intended, tightest (a)).
  2. valuation-gcd (unifies (a)+(b); strongest for (b)).
  3. product-count-monovariant (distinct termination mechanism; good hedge).

Suggested shared lemma to certify early: `euclid-step-invariant`
(gcd(min(a,b),|a-b|)=gcd(a,b) + the v_p(gcd)/v_p(lcm) action) — reused by all
three approaches.

build set: omega-count-monovariant, valuation-gcd, product-count-monovariant
