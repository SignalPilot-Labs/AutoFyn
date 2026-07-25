## Lemma (Well-definedness of the pattern-violation quantity $w_n(M)$)

Fix a finite $Q\supseteq R(a_1)$ and modulus $M\ge1$. For $n\ge n_1(Q,M)$
(the simultaneous stabilization index of `prefix-support-stabilization.md`),
define the predicted pattern $\pi_{n+1}(M):=\{p\in Q:(n{+}1)\bmod M\in
S_\infty(p,M)\}$, say $m$ *matches* the prediction for $n+1$ if
$R(m)\cap Q=\pi_{n+1}(M)$ exactly, and
$$w_n(M):=\min\{m>a_n : m\text{ does not match the prediction for }n+1\}.$$
Then $w_n(M)$ is well-defined and $w_n(M)\le a_n+\mathrm{lcm}(Q)$.

### Proof
Let $N:=\mathrm{lcm}(Q)$. Divisibility by any $p\in Q$ depends only on $m
\bmod p$, hence only on $m\bmod N$ (since $p\mid N$), so "matches the
prediction" is a union of full residue classes mod $N$. If
$\pi_{n+1}(M)\ne Q$: any $m\equiv0\pmod N$ has $R(m)\cap Q=Q\ne\pi_{n+1}(M)$,
so it fails to match, giving a non-matching integer in $(a_n,a_n+N]$. If
$\pi_{n+1}(M)=Q$: any $m\equiv1\pmod N$ has $R(m)\cap Q=\emptyset\ne Q$
(since $Q\ne\emptyset$, as $Q\supseteq R(a_1)$ and $a_1>1$), likewise
non-matching. Either way a full residue class mod $N$ inside $(a_n,a_n+N]$
fails to match, giving $w_n(M)\le a_n+N$. $\blacksquare$

### Status
Well-definedness is fully proved. **Monotonicity of $w_n(M)$ in $n$** (the
property that would make it a useful monovariant for the central gap) is
**not** established — see `aimo-0678-mechanism-inapplicability.md` for a
negative diagnosis of the natural proof route.

### Provenance
Proved in `approaches/frozen-invariant-monovariant.md`, §2.2 (Lemma 2),
round 5. Independently re-derived by the proof-reviewer via the residue-
class-partition argument; no gap found.
