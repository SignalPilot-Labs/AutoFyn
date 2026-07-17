# Lemma `sandwich-collapse` (★)

**Statement.** For any f:(0,∞)→(0,∞) satisfying the P5 sandwich (†), one has
  f(f(y)) = 2f(y) − y   for all y>0.
Consequences (same proof): with g:=f−id, the forward orbit is fⁿ(y)=y+n·g(y), g≥0, g is
orbit-invariant (g(f(y))=g(y)), and f is injective.

**Proof.** Squaring (†) gives (L²) 2(x²+f(y)²)≥(f(x)+y)² and (R²) (f(x)+y)²≥4x f(y). Put x=f(y):
(R²) yields (f(f(y))+y)²≥4f(y)², so f(f(y))+y≥2f(y); (L²) yields (2f(y))²≥(f(f(y))+y)², so
f(f(y))+y≤2f(y). Hence f(f(y))=2f(y)−y. Iterating at aₙ=fⁿ(y) gives aₙ₊₂=2aₙ₊₁−aₙ, so
aₙ=y+n g(y); positivity of all aₙ forces g(y)≥0; g(f(y))=f(f(y))−f(y)=g(y). Injectivity: f(a)=f(b)
⇒ 2f(a)−a=2f(b)−b ⇒ a=b.

**Certified** (proof-reviewer, round 1): correct; identities sympy-verified.
