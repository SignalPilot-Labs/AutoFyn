# Lemma: Telescoping threshold identity

**Source:** `approaches/lp-duality-certificate.md`, round 9.

**Statement.** Write $a_k:=2^k/(2^{k+1}-1)$. For every $n\ge1$,
$$a_{n-1}=\frac{a_n}{2(1-a_n)}.$$

**Proof.** $a_k-\tfrac12=\dfrac{1}{2(2^{k+1}-1)}>0$ for every $k\ge0$
(direct computation), so $1-a_n=\dfrac{2^n-1}{2^{n+1}-1}=\dfrac{D_{n-1}}{D_n}$
where $D_k:=2^{k+1}-1$ (using $n\ge1$ so $D_{n-1}=2^n-1$ is defined).
Hence $a_n/(2(1-a_n)) = (2^n/D_n)/(2D_{n-1}/D_n) = 2^{n-1}/D_{n-1}=a_{n-1}$.
$\blacksquare$

**Status.** Proved in full, general $n\ge1$, elementary algebra — not a
finite check. Independently re-verified by the reviewer symbolically
(exact `Fraction`) for $n=1,\dots,14$, zero mismatches, and the algebraic
derivation re-checked by hand. This is the identity that makes
`bisect-top-recursive-identity`'s inductive threshold land exactly on
$a_n$ with zero slack (see the Corollary in the approach file, §2).

**Certified by:** proof-reviewer, round 9.
