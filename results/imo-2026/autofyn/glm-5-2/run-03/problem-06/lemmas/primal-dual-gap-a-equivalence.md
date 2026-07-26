# Lemma: primal-dual-gap-a-equivalence (structural, NEGATIVE-fence)

*Certified: round 4 (reviewer). Source: `approaches/primal-minimal-support-stabilization.md`, Lemma 1. Verified computationally on $a_1\in\{15,35,77,91\}$ and on a synthetic non-self-dual family ($\operatorname{MT}(\operatorname{MT}(F))=\operatorname{MS}$ confirmed).*

## Statement

Let $\mathcal F_\infty=\{S(a_i):i\ge1\}$ (the family of prime-supports of greedy terms, multiplicity ignored), let $\operatorname{MS}_\infty$ denote the inclusion-minimal elements of $\mathcal F_\infty$ (the **PRIMAL** minimal-support antichain), and let $\operatorname{MT}(\mathcal F_\infty)$ denote the family of minimal transversals of $\mathcal F_\infty$ (the **DUAL**). Consider:

- (P) $\operatorname{MS}_\infty$ is finite and $\bigcup_{S\in\operatorname{MS}_\infty}S\subseteq G$ for some finite prime set $G$.
- (D) $\operatorname{MT}(\mathcal F_\infty)$ is finite and $\bigcup_{T\in\operatorname{MT}(\mathcal F_\infty)}T\subseteq G'$ for some finite prime set $G'$.

Then (P) $\iff$ (D). Moreover, under either hypothesis, $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)$ and $\operatorname{MS}_\infty=\operatorname{MT}(\operatorname{MT}(\mathcal F_\infty))$ (the blocker involution).

## Proof

Uses the classical **blocker involution** on clutters (Sperner families / antichains) over a finite ground (Edmonds–Fulkerson 1970; Schrijver, *Theory of Linear and Integer Programming*): **if $\mathcal C$ is a clutter over a finite ground $X$, then $b(b(\mathcal C))=\mathcal C$, where $b(\mathcal C):=\operatorname{MT}(\mathcal C)$ is the blocker (family of minimal hitting sets).** This is a finite combinatorial identity; it does not presuppose Gap A.

Two preliminaries (both reviewer-certified in `mt-depends-on-set-system`):

(A) $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)$. Every $S\in\mathcal F_\infty$ contains some $S_0\in\operatorname{MS}_\infty$ (start from $S$, delete primes preserving the member-superset relation; terminate by finiteness of $S$). A set $T$ hits every $S\in\mathcal F_\infty$ iff it hits every $S_0\in\operatorname{MS}_\infty$ (forward: $T\cap S_0\ne\varnothing\Rightarrow T\cap S\ne\varnothing$; backward: every $S$ contains some $S_0$). Minimality is a property of the transversal family, so $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)$.

(B) $\operatorname{MS}_\infty$ is a clutter (antichain) over its ground $\bigcup\operatorname{MS}_\infty$ by definition (inclusion-minimal = no member contains another).

**($\Rightarrow$) Assume (P).** $\operatorname{MS}_\infty$ is a clutter over the finite ground $X:=\bigcup\operatorname{MS}_\infty\subseteq G$. By (A), $\operatorname{MT}(\mathcal F_\infty)=\operatorname{MT}(\operatorname{MS}_\infty)=b(\operatorname{MS}_\infty)$, which is a finite clutter over $X$ (a finite ground admits finitely many subsets, hence finitely many minimal hitting sets). So (D) holds with $G'=X\subseteq G$. ✓

**($\Leftarrow$) Assume (D).** $\operatorname{MT}(\mathcal F_\infty)$ is a finite clutter over the finite ground $Y:=\bigcup\operatorname{MT}(\mathcal F_\infty)\subseteq G'$. Every $S\in\operatorname{MS}_\infty$ is a transversal of $\operatorname{MT}(\mathcal F_\infty)$: $S=S(a_j)$ for some $j$, and every $T\in\operatorname{MT}(\mathcal F_\infty)$ is a transversal of $\mathcal F_\infty$ hence $T\cap S(a_j)\ne\varnothing$, i.e. $S\cap T\ne\varnothing$. As a transversal, $S\subseteq Y$. So $\bigcup\operatorname{MS}_\infty\subseteq Y$ is finite; $\operatorname{MS}_\infty$ is a clutter over the finite ground $Y$. The blocker involution gives $b(b(\operatorname{MS}_\infty))=\operatorname{MS}_\infty$. Combined with (A) ($b(\operatorname{MS}_\infty)=\operatorname{MT}(\mathcal F_\infty)$), $\operatorname{MT}(\operatorname{MT}(\mathcal F_\infty))=b(b(\operatorname{MS}_\infty))=\operatorname{MS}_\infty$; in particular $\operatorname{MS}_\infty$ is the blocker of the finite clutter $\operatorname{MT}(\mathcal F_\infty)$ over $Y$, hence finite. So (P) holds with $G=Y\subseteq G'$. ✓ ∎

## Consequence (fencing)

The primal-minimal-support stabilization target (P) is **literally equivalent** to the dual Gap A target (D), via the classical blocker involution — NOT a bypass. Any future primal-framing attack on Gap A is, by this lemma, an attack on the dual MT-finiteness wall. The hope that the primal admits a direct greedy-minimality argument the dual lacks must be borne by a *mechanism*, not by the framing.

## Tools

Classical blocker involution on clutters (Edmonds–Fulkerson 1970; Schrijver) — named hypergraph-theoretic identity, finite-combinatorial, no Gap-A presupposition. `mt-depends-on-set-system` (MT depends only on distinct member-sets; symmetric variant for primal).
