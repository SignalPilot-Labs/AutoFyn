# Lemma: Pinch identity

**Statement.** Let f: R_{>0} -> R_{>0} satisfy, for all x,y>0,
  (L) 2(x^2 + f(y)^2) >= (f(x)+y)^2 and (R) (f(x)+y)^2 >= 4 x f(y).
Then f(f(y)) = 2 f(y) - y for all y > 0.

**Proof.** Fix y>0 and set x = f(y) > 0. (R) gives (f(f(y))+y)^2 >= 4 f(y)^2; (L) gives
4 f(y)^2 = 2(f(y)^2+f(y)^2) >= (f(f(y))+y)^2. Both sides positive, so f(f(y))+y = 2 f(y). ∎

Certified round 1 (proof-reviewer). Used by modulus-telescope and two-sided-orbit.
