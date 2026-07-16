# imo-2026-05 — current

## Status
solved

## Approaches tried
- modulus-telescope — SOS sufficiency; x=f(y) pinch f(f(y))=2f(y)-y; h=f-id>=0 via orbit iterates;
  quadratic modulus |h(a)-h(b)|<=(a-b)^2/(4 min(a,b)) (from the RIGHT inequality applied at both
  endpoints); telescoped over a uniform partition to force h constant. Reviewer-verified, no gap. SOLVED.
- two-sided-orbit — same prefix; two-sided modulus |h(b)-h(a)|<=(b-a)^2/(2 min(a,b)) (upper from R,
  lower from L); orbit-interleaving forces all positive values of h equal, then continuity (from the
  modulus) + IVT rules out a zero. Reviewer-verified, no gap. SOLVED (independent finish).
- modulus-derivative — not built this round.

## Current best
Complete proof of both directions. Answer: exactly f(x) = x + c for constants c >= 0.

## Full proof

We prove the solution set is exactly { f(x) = x + c : c >= 0 }.

Since every quantity under a square root and every middle term (f(x)+y)/2 is positive, squaring the
given chain is an equivalence. For all x,y>0 the hypothesis is equivalent to
  (L)  2(x^2 + f(y)^2) >= (f(x) + y)^2,
  (R)  (f(x) + y)^2 >= 4 x f(y).
Write h := f - id, so h(x) = f(x) - x.

### Part I — Sufficiency.
Let c >= 0 and f(x) = x + c > 0. Then f(x) + y = x + f(y), so the middle term is the arithmetic mean
(x + f(y))/2. Both slacks are perfect squares:
  2(x^2 + f(y)^2) - (x + f(y))^2 = (x - f(y))^2 >= 0   [QM-AM, an exact SOS],
  (x + f(y))^2 - 4 x f(y) = (x - f(y))^2 >= 0           [AM-GM, an exact SOS].
(Both identities verified symbolically.) Hence every f(x) = x + c with c >= 0 is a solution. This
verifies the answer by direct substitution.

### Part II — Necessity.
Let f satisfy (L),(R) for all x,y>0.

**Step 1 (Pinch).** Fix y>0; substitute x = f(y) (positive). (R) gives (f(f(y))+y)^2 >= 4 f(y)^2 and
(L) gives 4 f(y)^2 >= (f(f(y))+y)^2; both sides positive, so f(f(y)) + y = 2 f(y), i.e.
  f(f(y)) = 2 f(y) - y   for all y>0.

**Step 2 (Orbit + positivity).** From Step 1, h(f(y)) = f(f(y)) - f(y) = f(y) - y = h(y). By induction
f^n(z) = z + n h(z) for all n>=1 (f^{n+1}(y) = f^n(f(y)) = f(y) + n h(f(y)) = y + (n+1) h(y)). If
h(y) < 0 then f^n(y) = y + n h(y) -> -infinity, contradicting f > 0. Hence h(y) >= 0, i.e. f(y) >= y.

**Step 3 (Quadratic modulus).** Fix t>0 and let p > -t, so t+p>0. Apply (R) at x = f(t), y = t+p;
using f(f(t)) = 2 f(t) - t,
  (2 f(t) + p)^2 >= 4 f(t) f(t+p)  =>  f(t+p) <= f(t) + p + p^2/(4 f(t)),
hence h(t+p) - h(t) <= p^2/(4 f(t)). Applying this with (t,p) = (b, a-b) and with (a, b-a) bounds both
h(a)-h(b) and h(b)-h(a) from above by (a-b)^2/(4 min(f(a),f(b))); since f(a) >= a, f(b) >= b,
  |h(a) - h(b)| <= (a-b)^2 / (4 min(a,b))   for all a,b>0.

**Step 4 (h constant).** Fix t0>0, L>0. Partition t_i = t0 + iL/N, i = 0..N. Since t_i >= t0 and
min(t_{i+1}, t_i) = t_i,
  |h(t0+L) - h(t0)| <= sum_{i} |h(t_{i+1}) - h(t_i)| <= N * (L/N)^2/(4 t0) = L^2/(4 t0 N) -> 0.
The left side is independent of N, so h(t0+L) = h(t0). As t0, L range over R_{>0}, h is constant; call
it c. By Step 2, c >= 0. Hence f(x) = x + c with c >= 0.

### Conclusion.
Part I: every f(x) = x + c, c >= 0 works. Part II: every solution has that form. Therefore the
complete solution set is
  { f(x) = x + c : c >= 0 }.
Verified by substitution (Part I: both slacks equal (x - f(y))^2 >= 0). ∎
