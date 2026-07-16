# Lemma: Quadratic modulus of continuity for h = f - id

**Statement.** Under the pinch hypotheses (pinch-identity) with h = f - id and h >= 0
(orbit-nonnegativity): |h(a) - h(b)| <= (a-b)^2 / (4 min(a,b)) for all a,b > 0.

**Proof.** Fix t>0, p>-t. Apply (R) at x=f(t), y=t+p; using f(f(t))=2f(t)-t gives
(2f(t)+p)^2 >= 4 f(t) f(t+p), so f(t+p) <= f(t)+p+p^2/(4f(t)), i.e. h(t+p)-h(t) <= p^2/(4 f(t)).
Applying this at (t,p)=(b,a-b) and (a,b-a) bounds both signed differences above by
(a-b)^2/(4 min(f(a),f(b))); since f>=id, min(f(a),f(b)) >= min(a,b). ∎

**Corollary (rigidity).** A function h on R_{>0} with |h(a)-h(b)| <= (a-b)^2/(4 min(a,b)) is constant:
for t0,L>0 partition t_i=t0+iL/N; telescoping gives |h(t0+L)-h(t0)| <= L^2/(4 t0 N) -> 0.

Certified round 1 (proof-reviewer). The modulus bound is used by both approaches (two-sided-orbit
uses the weaker constant 1/(2min) with the same proof plus a lower bound from (L)).
