## Lemma (Translation compatibility of the gcd-constraint)

Let $m, y, L$ be positive integers with $\mathrm{rad}(y) \mid L$ (every prime
factor of $y$ divides $L$). Then
$$\gcd(m, y) > 1 \iff \gcd(m+L, y) > 1.$$

### Proof
$\gcd(m,y) > 1$ iff some prime $p \mid y$ also divides $m$. For every prime
$p \mid y$, the hypothesis gives $p \mid L$, so $m \equiv m+L \pmod p$; hence
$p \mid m \iff p \mid (m+L)$. This equivalence holds simultaneously for
every prime factor of $y$, so the set of common prime factors of $(m,y)$
equals the set of common prime factors of $(m+L,y)$; in particular one set
is nonempty iff the other is. $\blacksquare$

### Provenance
Proved in `approaches/active-set-stabilization.md`, round 2. Elementary,
general-purpose modular-arithmetic fact with no dependence on any other
lemma for this problem. Verified by the proof-reviewer, round 2: correct as
stated and independent of imo-2026-06's specific sequence.

### Caveat
By itself this lemma is only a **sufficient** condition for shift-invariance
of a single constraint (against a single fixed $a_i$ with
$\mathrm{rad}(a_i) \mid L$) — it is **not** sufficient to conclude
periodicity of the whole greedy sequence: in the worked numerical example
($a_1=15$), a term such as $a_8=42=2\cdot3\cdot7$ has $\mathrm{rad}(a_8)=42
\nmid 30=L$, yet periodicity with period $L=30$ still holds through and past
index $8$. So this lemma isolates one sufficient (but not necessary)
mechanism; the true reason periodicity holds is more delicate and not fully
identified by any approach so far.
