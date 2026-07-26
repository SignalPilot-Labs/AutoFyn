# Deficit-sum + pairing cut entry (Mulan's triangle game)

**Statement.** Suppose θ=180°/n for an integer n≥3 (so θ≤60°). From any triangle state with no angle a positive multiple of θ, Mulan can force BOTH children to contain a positive multiple of θ in a single move, via the round-up deficit function.

**Definitions.** For x∈(0,180°), let m_x = min{m∈Z_{≥1}: mθ≥x} ∈ {1,…,n} and d(x) = m_xθ − x ∈ [0,θ). Note d(x)=0 ⟺ x is a positive multiple of θ; if x is θ-safe then d(x)∈(0,θ). Call x "top" if m_x=n, i.e. x∈(180°−θ,180°).

**Deficit-sum lemma.** If a+b+c=180°=nθ and none of a,b,c is a multiple of θ, then d(a)+d(b)+d(c) ∈ {θ, 2θ}.
*Proof.* Write a=m_aθ−d(a) etc. Summing: 180°=(m_a+m_b+m_c)θ − (d(a)+d(b)+d(c)), so d-sum = (m_a+m_b+m_c−n)θ, an integer multiple of θ. Each d∈(0,θ), so d-sum∈(0,3θ). It is >0 (sum of positive terms) and <3θ (strict), so it lies in {θ,2θ}. ∎

**Pairing lemma (refined).** Under the hypotheses above, there exist distinct angles u,v among {a,b,c} with d(u)<v AND m_u≤n−1.
*Proof.* θ≤60° (n≥3) ⟹ a "top" angle is >120°, so two top angles would sum >240°>180°: at most one top angle. Suppose no valid pairing exists: for every non-top u and every v≠u, d(u)≥v.
- *Case |T|=0 (no top; all m≤n−1).* Cyclic pairs give d(a)≥b, d(b)≥c, d(c)≥a; summing, d-sum ≥ a+b+c = 180° = nθ. But d-sum ≤2θ ⟹ n≤2, contradicting n≥3.
- *Case |T|=1 (c top, m_c=n; a,b non-top).* a+b=180°−c<θ ⟹ a,b∈(0,θ), m_a=m_b=1, d(a)=θ−a, d(b)=θ−b. Negation vs v=c: d(a)≥c ⟺ b≥180°−θ; d(b)≥c ⟺ a≥180°−θ. So a,b≥180°−θ ⟹ a+b≥2(180°−θ)≥240° (θ≤60°); but a+b<180°<240°. Contradiction.
Both cases contradict, so a valid pairing exists. ∎

**Pairing cut.** Pick distinct u,v from the pairing lemma (d(u)<v, m_u≤n−1); let w be the third angle. Mulan cuts at the vertex with angle v, parameter α=d(u). Legal: d(u)>0 (u safe), d(u)<v (pairing). By the cut-geometry lemma the children are
  C1 = (d(u), u, 180°−u−d(u)) = (d(u), u, (n−m_u)θ),
  C2 = (v−d(u), w, u+d(u)) = (v−d(u), w, m_uθ).
C1 contains (n−m_u)θ (positive since m_u≤n−1) and C2 contains m_uθ (positive since m_u≥1). Both children marked. Positivity: d(u)>0, u>0, (n−m_u)θ>0; v−d(u)>0 (pairing), w>0, m_uθ>0. ∎

**n=2 direct 90°-trick.** For n=2 (θ=90°), from any triangle with no 90° angle, at least two angles B,C<90°; A=180°−B−C≠90°. Cut at vertex A, α=90°−B (legal: α>0 since B<90°; α<A since C<90°). Children (90°−B,B,90°) and (A−90°+B,C,90°); both contain 90°=θ.

**Certified by:** proof-reviewer, round 1. **Source:** approaches/safe-unsafe-pairing.md §II.3–II.6.
