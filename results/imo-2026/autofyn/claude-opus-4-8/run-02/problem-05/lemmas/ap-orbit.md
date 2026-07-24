# Lemma: AP-orbit and g ≥ 0 (certified round 1)

**Statement.** Under (FE) f(f(y))=2f(y)−y (hence under the chain), with g=f−id: for every y>0 the
forward orbit x_n=f^n(y) satisfies x_n = y + n·g(y) (n≥0); g(f(y))=g(y) (orbit-invariance); and,
using positivity of the codomain, g(y) ≥ 0 for all y>0.

**Proof.** g(f(y))=f(f(y))−f(y)=(2f(y)−y)−f(y)=f(y)−y=g(y). With x₀=y, x_{n+1}=f(x_n), (FE) at x_n
gives x_{n+2}=2x_{n+1}−x_n, so consecutive differences are constant =g(y), whence x_n=y+n·g(y). Each
x_n∈R_>0; if g(y)<0 then x_n→−∞, contradiction. So g(y)≥0. ∎

Certified: reviewer verified. Used in orbit-distance Part III.
