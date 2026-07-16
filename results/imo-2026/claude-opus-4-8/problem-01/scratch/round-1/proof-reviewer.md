# Proof review — imo-2026-01 (IMO 2026 P1), round 1

Problem: 2026 integers > 1; a move replaces m>1, n>1 by gcd(m,n) and lcm(m,n)/gcd(m,n).
(a) Prove exactly one entry M > 1 survives after finitely many moves.
(b) Prove M is independent of the choices. `task: proof_only`, no numeric answer.

## Independent verification (my own re-derivation)
- Brute-force simulation, 3000 random boards (N=2..6, entries 2..60) x 8 random
  play-outs each: EVERY play-out terminated, left EXACTLY one entry > 1, and that
  survivor equalled prod_p p^{gcd_i v_p(x_i)} across all play-outs of a board.
  0 discrepancies.
- Verified the two load-bearing identities for all a,b in [0,30):
  gcd(min(a,b),|a-b|) = gcd(a,b) and min(a,b)+|a-b| = max(a,b), including the
  flagged edge cases a=0, b=0, a=b. 0 failures.
- Re-derived the monovariant drop from scratch:
  Omega(g)+Omega(h)-Omega(m)-Omega(n) = -Omega(g) (via sum_p max = sum_p(a+b) - sum_p min
  and sum_p min = Omega(gcd)). Confirms (*) in all three files.

I checked every flagged load-bearing point (1-8). All hold.

---

## valuation-gcd — Verdict: APPROVE (Status: solved)
- Lemma 0 (min/max/|diff| valuations): derived from FTA, not asserted. Correct.
- Lemma 2 (gcd(min,|diff|)=gcd) proven by identical common-divisor-set argument,
  edge cases explicit. Correct.
- Monovariant T = sumOmega + count, 2-case (g=1 / g>1): Delta T <= -1 in both.
  Arithmetic correct; the m=n subcase is noted and handled. Exhaustive/disjoint.
- Whole-multiset d_p invariance uses gcd associativity correctly:
  gcd(R,a,b)=gcd(r,gcd(a,b)) and Lemma 2. Correct.
- "Not zero" is NON-circular: d_{p_1}>=1 from the initial board via a prime dividing
  x_1, carried to the terminal board by invariance; terminal all-1 => d=0 contradiction.
  The C*=1 conclusion does not assume itself. Correct.
- Terminal read-off d_p = v_p(M') then M'=M by FTA. Correct.
- Minor presentational note (not a defect): Part (a) defers "not zero" to Part (b);
  the logic is sound and non-circular, just organised across parts.
Recorded: verified-milestone.

## omega-count-monovariant — Verdict: APPROVE (Status: solved)
- Lemma 0.1 (valuations, gcd*lcm=mn), 0.2 (gcd theory: universal property via
  Bezout, associativity, list characterization, zero-iff-all-zero), 0.3 (Euclidean
  step) all fully proven. Correct.
- Output form h=ab with m=ga,n=gb,gcd(a,b)=1 derived correctly.
- W = sumOmega + count, clean 3-case split (g=1; g>1,m=n; g>1,m!=n): each gives
  Delta W <= -1; cases exhaustive and disjoint; the count change is computed exactly
  in each. This is the cleanest, most self-contained case analysis. Correct.
- d_p invariance and "not zero" proven within Part (a) itself (no forward reference),
  non-circular: D_{p_1}>=1 from FTA on an initial entry vs terminal all-1 => 0.
- Part (b): v_p(M)=D_p, M=prod p^{D_p}, finite product, choice-independent. Correct.
Recorded: verified-milestone. Adopted as the basis for current.md Full proof.

## product-count-monovariant — Verdict: APPROVE (Status: solved)
- Lemma 1 / Cor 2: g*h = lcm = mn/g, so a move maps board product P -> P/g. Correct.
- Lex monovariant (P,C): g>1 => P strictly drops (P/g <= P/2); g=1 => P fixed and
  C drops by 1 (h=mn>1). Cases exhaustive (g>=1) and disjoint. Correct.
- Lemma 4 (well-foundedness of lex order): proven from scratch by infinite descent
  — first coordinate is a non-increasing positive-integer sequence that stabilizes,
  then the second is a strictly decreasing non-negative-integer sequence, impossible.
  NOT merely asserted. Correct.
- Lemmas 5-7 (Euclidean step, valuation action, d_p invariance via associativity):
  all fully proven. "Not zero" in Section 4 non-circular (d_{p_1}>=1 vs terminal 0).
- Part (b): M = prod p^{d_p}, plus a worked {4,8} -> survivor 2 check. Correct.
Recorded: verified-milestone.

---

## Builder Status accuracy
All three builders marked `solved`; each is in fact a complete, gap-free proof of
both parts. Statuses are accurate.

## Lemma certification
`lemmas/euclid-step-invariant.md` — CERTIFIED. Statements (A) valuation action,
(B) min+|diff|=max, (C) gcd(min,|diff|)=gcd, (D) whole-multiset d_p invariance are
correct, no stronger than what is proved, and sorry-free. Verified computationally.
Status line in the file updated to CERTIFIED.

## Actions taken
- record_outcome: verified-milestone for all three slugs (round 1).
- current.md: Status set to `solved`; Full proof written (based on the
  omega-count-monovariant route, the cleanest self-contained argument).
- Lemma certified in place.

## Overall
The run's goal is met: a complete, rigorous, verified proof of both (a) and (b)
exists (three independent ones). Answer M = prod_p p^{gcd_i v_p(x_i)}.
