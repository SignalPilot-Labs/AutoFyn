## imo-2026-01

valuation-invariant: new
Target: Prove (a) after finitely many moves exactly one M > 1 remains, and (b) M is independent of choices
Technique: p-adic valuation invariant (d_p = gcd of all v_p values) + lexicographic monovariant (Omega, count)
Skeleton:
  1. Decompose operation per prime: (v_p(m), v_p(n)) -> (min, |diff|) — direct computation
  2. Euclidean identity: gcd(min(a,b), |a-b|) = gcd(a,b) — standard Euclidean step
  3. d_p = gcd(v_p(x_1), ..., v_p(x_2026)) is invariant — by Euclidean identity
  4. Terminal state: {M, 1,...,1} has v_p(M) = d_p for all p — by gcd(a,0) = a
  5. M = prod_p p^{d_p} is determined by initial config — part (b) done
  6. Monovariant (T, N) = (Sigma Omega(x_i), count >1) strictly decreases lex — case analysis
  7. N >= 1 at termination since M > 1 (some d_p >= 1) — part (a) done
Key lemmas (claim + the one-line mechanism that makes it true):
  - gcd(min(a,b), |a-b|) = gcd(a,b) — because gcd(a, b-a) = gcd(a,b) (Euclidean algorithm)
  - d_p preserved under each move — because the Euclidean identity preserves gcd of the pair
  - M > 1 — because each initial x_i > 1 contributes v_p >= 1 for some p, so d_p >= 1 for that p
Open gaps: none — complete outline, builder writes full proof
Cases to cover: gcd > 1 with both outputs > 1; gcd > 1 with one output = 1 (m = n); gcd = 1 (coprime)
Watch out for: gcd(a,0) = a convention is essential; don't confuse M with gcd of initial numbers

product-monovariant: new
Target: Prove (a) after finitely many moves exactly one M > 1 remains, and (b) M is independent of choices
Technique: single combined monovariant Q = P * 2^N (decreases by factor >= 2 each step) + p-adic invariant
Skeleton:
  1. Define Q = (prod x_i) * 2^{count >1} — positive integer
  2. Case gcd >= 2, ab >= 2: P -> P/gcd, N unchanged, Q -> Q/gcd <= Q/2 — direct
  3. Case gcd >= 2, ab = 1 (m = n): P -> P/d, N -> N-1, Q -> Q/(2d) <= Q/4 — direct
  4. Case gcd = 1: P unchanged, N -> N-1, Q -> Q/2 — direct
  5. Q decreases by factor >= 2, so process terminates in <= log_2(Q_init) steps — part (a) termination
  6. No move produces two 1s, so N >= 1 at termination — part (a) exactly one
  7. Same p-adic invariant d_p = gcd of valuations — part (b)
Key lemmas (claim + the one-line mechanism that makes it true):
  - Q = P * 2^N decreases by >= 2 — because either P shrinks (gcd > 1) or N shrinks (gcd = 1)
  - No move outputs two 1s — because gcd = 1 means ab = mn >= 4, and gcd > 1 means gcd >= 2
  - d_p invariance — same Euclidean identity as above
Open gaps: verify "no two 1s" claim explicitly (straightforward)
Cases to cover: same three cases as above
Watch out for: must explicitly check all 3 cases for Q decreasing; P >= 2 throughout needs the "no two 1s" fact
