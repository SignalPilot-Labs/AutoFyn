# Outline review — imo-2026-05 (round 1)

Problem: find all f:R_{>0}->R_{>0} with sqrt((x^2+f(y)^2)/2) >= (f(x)+y)/2 >= sqrt(x f(y)) for all x,y>0.
Claimed answer: exactly f(x)=x+c, c>=0.

All three approaches share a verified prefix; they differ only in how they close the hard
"h=f-id is a nonnegative constant" step. I re-derived every load-bearing identity symbolically
(sympy) before ruling — all pass:

- Sufficiency: for f(x)=x+c the middle term is AM(x,f(y)) and BOTH slacks equal (x-f(y))^2 exactly
  (`2(x^2+f(y)^2)-(f(x)+y)^2 = (x-f(y))^2`, `(f(x)+y)^2-4x f(y) = (x-f(y))^2`). Verified = 0.
- Pinch x=f(y): QM=GM=f(y) collapses the sandwich, forcing f(f(y))=2f(y)-y. Structurally sound.
- (U) right bound: (2f(t)+p)^2 >= 4 f(t) f(t+p) => h(t+p)-h(t) <= p^2/(4f(t)). Identity verified = 0.
- Left bound: 2f(t)^2+2f(t+p)^2 >= (2f(t)+p)^2 => f(t+p)^2 >= (f(t)+p)^2 - p^2/2. Identity verified = 0.

Critical check requested (invalidity of the naive "combined" inequality): confirmed. None of the
surviving approaches subtracts the two inequalities or manipulates them jointly. Each uses only a
single one-sided bound at a time — (U) comes purely from the RIGHT inequality at x=f(t); the lower
bound comes purely from the LEFT inequality at x=f(t). No cross-subtraction. Good.

No circularity in step 4: (U) uses the exact identity f(f(t))=2f(t)-y (step 2), not the conclusion.

---

## modulus-telescope — APPROVE (flagship; essentially a complete proof)
Route: SOS sufficiency -> pinch f(f)=2f-id -> h>=0 via f^n(y)=y+n h(y) positivity -> (U) ->
symmetrize |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)) -> telescope [t0,t0+L] in N steps, total O(L^2/(N t0))->0.
Every step verified. The telescoping finish is airtight and calculus-free: min f on [t0,t0+L] >= t0
(from f>=id), so the constant 1/(4t0) is uniform and the N-term sum vanishes as N->inf. This is a
whole, end-to-end attempt at the actual claim, both directions, c>=0 in / c<0 out covered.
Issues: none load-bearing. Builder must write the O(p^2) symmetrization and the Riemann-sum limit
in full (no "clearly"), and state f>=id explicitly before using min(a,b) in the denominator.

## modulus-derivative — APPROVE (valid, but redundant with the flagship)
Identical prefix and same (U); only the finish differs: difference quotient <= |b-a|/(4 min)->0 gives
h'==0, plus Lipschitz-continuity, then "derivative 0 on an interval => constant" by MVT. Logically
valid and the domain (0,inf) is a genuine interval so no piecewise-constant escape. But this is a
strictly heavier version of the same limiting argument the telescope already runs — it adds MVT
machinery for no extra reach and shares lemma (U) entirely, so it provides little independence.
Kept in the population (registered), not built this round.
Issue: cite the "differentiable, h'==0 => constant" theorem by name and its continuity hypothesis.

## two-sided-orbit — APPROVE with CHANGES (independence hedge; one real gap)
Genuinely different: derives the LOWER modulus from the LEFT inequality (independent of (U)) for
two-sided control |h(a)-h(b)| <= (a-b)^2/(2 min), then an orbit-interleaving contradiction with NO
calculus. Value: it leans on the left inequality and a calculus-free finish, so it survives if (U)
or the limiting finishes are ever disputed. Both modulus bounds verified.
Load-bearing gap (already flagged by the outliner, must be closed, not hand-waved):
- Step 7 fixed-point sub-case c1=0. If h(a)=0 then a_n=a is bounded, min(a,b_m) stays finite, and the
  squeeze |c1-c2| <= c2^2/(2 min) does NOT vanish — the orbit argument fails exactly there. The file's
  fallback is to telescope, which collapses it into modulus-telescope. Builder must supply an
  independent closing of c1=0 (e.g. bound c2 directly by applying step 6 between b and b+eps on the
  moving orbit, or drive both indices on the c2-orbit), or this route loses its independence claim.
- Minor: the stated lower bound -p^2/(2(f(t)+p)) is looser than the tight -p^2/(4(f(t)+p)); harmless
  (still a valid lower bound) but note it's not tight.

---

## Ranking (registered + folded this round)
- modulus-telescope  1531  — complete, self-contained, fully verified. Beats both siblings.
- modulus-derivative 1501  — valid but redundant finish on the same (U).
- two-sided-orbit    1468  — real independence, but its independent finish has a genuine c1=0 gap.

Comparisons applied: telescope > orbit (complete vs gap), telescope > derivative (self-contained vs
extra MVT dependency), derivative > orbit (complete route vs gap).

## Build set rationale
Build the flagship (strongest, near-complete) plus the independence hedge (distinct mechanism, leans
on the LEFT inequality so the field doesn't die if (U) is ever disputed). modulus-derivative is held
back this round: it shares (U) and the whole prefix with telescope and only swaps the limiting finish,
so building it adds effort without adding coverage — telescope already subsumes its reach.

build set: modulus-telescope, two-sided-orbit
