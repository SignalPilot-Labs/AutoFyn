## Statement

Let $F,G$ be finite multisets of positive reals, $r:=\mathrm{Total}(G)$ (no
dominance assumption on $F$ vs. $G$ required). Let $u(x):=\mathbb
1[N_F(x)\text{ odd}]$, $v(x):=\mathbb 1[N_G(x)\text{ odd}]$ where
$N_F,N_G$ count elements exceeding $x$. Then
$$A(F\cup G) = A(F)+A(G) - 2\int_0^r u(x)v(x)\,dx.$$

## Proof

See `results/imo-2026-03/approaches/greedy-halving-adversary.md`, Lemma 8
(round 2): split the defining integral of $A(F\cup G)$ (from the certified
`integral-alternating-sum-formula` lemma) at $x=r$; for $x\ge r$, $G$
contributes nothing so $N_{F\cup G}=N_F$; for $x<r$, parity of $N_{F\cup
G}=N_F+N_G$ is the XOR of $u,v$, and for $\{0,1\}$-valued indicators
$u\oplus v = u+v-2uv$.

## Certification note (proof-reviewer, round 2)

Independently re-verified by an exact-`Fraction` brute-force script computing
both sides via breakpoint integration: 1000 random pairs of multisets (sizes
1–5 each) — zero mismatches. The written proof's algebra (XOR identity for
$\{0,1\}$-valued indicators, and the two-range integral split) is sound on
independent re-derivation. Fully general — no dominance or game-specific
assumption needed; this is the correct general tool for splitting Xiang Yu's
cut budget between any two parts of a configuration and strictly subsumes
`dominant-element-removal-identity` (set $G=\{M_1\}$: then $v\equiv1$ on
$[0,M_1)$ and the cross term collapses to $\int_0^\rho u$ when $M_1>\rho$,
recovering that lemma — consistency check passed by hand). Certified
correct.
