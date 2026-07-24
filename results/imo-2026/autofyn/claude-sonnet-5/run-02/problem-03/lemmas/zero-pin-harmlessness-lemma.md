## Statement

Let $M$ be any finite multiset of nonnegative reals and let
$M^+ := M\cup\{0\}$ (adjoin one element of value $0$). Then
$\mathrm{Total}(M^+)=\mathrm{Total}(M)$, $E(M^+)=E(M)$, $O(M^+)=O(M)$,
$A(M^+)=A(M)$, and $\Phi(M^+)=\Phi(M)$, where $O,E$ denote the sum of
elements at odd/even sorted rank (rank $1$ = largest), $A=O-E$,
$\Phi=(\mathrm{Total}+A)/2$.

**Corollary (iterated).** For any $q\ge0$, adjoining $q$ zero-valued
elements to $M$ leaves $\mathrm{Total},O,E,A,\Phi$ all unchanged.

## Proof

See `results/imo-2026-03/approaches/lp-duality-certificate.md`, §R11.1.
Sort $M$ descending as $L_1\ge\dots\ge L_k\ge0$. Since $0\le L_k$, the
appended $0$ occupies rank $k+1$ in $M^+$ (or, if $M$ already contains
zeros, some rank among the tied group of zeros — immaterial since all
zero-valued elements contribute $0$ to $O$ and $E$ regardless of which
exact rank they occupy). Hence $L_1,\dots,L_k$ keep their original ranks,
so $O(M^+)=O(M)$, $E(M^+)=E(M)$ (the appended element contributes $0$ to
whichever of $O,E$ it lands in). The rest follows by definition
($A=O-E$, $\mathrm{Total}(M^+)=\mathrm{Total}(M)+0$,
$\Phi=(\mathrm{Total}+A)/2$). The iterated corollary is immediate
induction on $q$.

## Certification note

**CERTIFIED — proof-reviewer, round 11.** A short, fully general,
elementary, marking-independent fact (no ladder structure, no rationality,
no dependence on any other lemma in the population beyond the shared
claiming-subgame definitions of $O,E,A,\Phi$). Reviewer independently
re-derived the proof from scratch (agrees) and spot-checked the claim
numerically on several random multisets with zero, one, and several
appended zeros — trivially confirmed. Reusable anywhere a "does a
degenerate/zero-length fragment matter" question arises.
