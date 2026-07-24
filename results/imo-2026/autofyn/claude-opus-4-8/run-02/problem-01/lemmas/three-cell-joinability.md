# Lemma (3-cell joinability, critical pair) — CERTIFIED round 1

Let x,y,z>1 be the values at three distinct cells X,Y,Z of a board B. Let B'=combine{X,Y},
B''=combine{Y,Z}. Then B' and B'' have a common reduct W (using only moves among {X,Y,Z}): W carries
the value multiset {s,1,1} on {X,Y,Z} and the original values elsewhere, where
```
s = ∏_p p^{g_p},  g_p = gcd(v_p(x), v_p(y), v_p(z)).
```
Proof (explicit reduct, NON-circular — not "normal forms are unique"): run any maximal sequence of
moves restricted to {X,Y,Z} from B'; it terminates (lex monovariant) with ≤1 of X,Y,Z having value
>1. Throughout, g_p^{XYZ}=g_p (gcd-of-valuations invariant, since every combined pair ⊆{X,Y,Z}). At
the halt with survivor value t: g_p = gcd(v_p(t),0,0)=v_p(t), forcing t=s. Same from B''. The two
results agree as value multisets (2023 untouched cells + {s,1,1}), so W is a common reduct.

Certified by proof-reviewer, round 1 (example {4,6,9}: s=6, both branches reach {2,3,6}→…→{6,1,1}).
Source: descent-induction §6 (Lemma 5).
