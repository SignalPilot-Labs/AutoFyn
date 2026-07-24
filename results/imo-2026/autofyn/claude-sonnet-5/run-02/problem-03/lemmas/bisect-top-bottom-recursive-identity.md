# Lemma: Bisect-top-bottom recursive identity (Theorem D′) and Bisect-top-two identity (Theorem E)

**Source:** `approaches/lp-duality-certificate.md`, round 9.

**Theorem D′.** For any marking $p_1\ge\cdots\ge p_m>0$ ($m\ge2$),
bisecting $p_1$ and $p_m$ simultaneously (2 cuts) and applying any further
legal strategy to the untouched middle $\{p_2,\dots,p_{m-1}\}$ (budget
$n-2$), producing refinement $M'$ with value $\Phi'$, yields exactly
$$\Phi(\text{combined})=\frac{p_1+p_m}{2}+\Phi'.$$

**Theorem E.** For $m\ge3$, bisecting $p_1,p_2$ simultaneously (2 cuts)
and recursing on $\{p_3,\dots,p_m\}$ (budget $n-2$) with tail value
$\Phi'$ yields exactly $\Phi(\text{combined})=(p_1+p_2)/2+\Phi'$.

**Proof (both).** Same structure as `bisect-top-recursive-identity`,
applying `pair-cancellation-identity` twice (once per exact pair). Final
multiset $=\{a/2,a/2,b/2,b/2\}\cup M'$ for the two bisected values $a,b$;
$A(\text{final})=A(M')$, and $\Phi(\text{combined})=(a+b)/2+\Phi'$ by the
same total-bookkeeping algebra. $\blacksquare$

**Status.** Both proved in full, unconditional, general $m$ — exact
bookkeeping identities. Independently re-verified by the reviewer with
2000 random exact-`Fraction` trials each, zero mismatches. Strictly
generalize the (previously certified-in-substance) Theorem D
"bisect-top-bottom-identity" special case.

**Also certified alongside (exact threshold algebra, Theorem D′'s
IH-ceiling version):**
- $s^\ast=\frac32 a_n T$ is the exact threshold on $s:=p_1+p_m$ above which
  substituting the inductive ceiling $\Phi'\le a_{n-2}T''$ into Theorem D′
  certifies $\Phi_{\min}\le a_nT$ — derived in closed form for every
  $n\ge2$, reviewer-reverified symbolically for $n=2,\dots,19$.
- **Negative result (equal-pieces insufficiency):** for every $n\ge2$, the
  equal-pieces marking has $s=2T/(n+1)<s^\ast$, i.e. is never certified by
  this route — proved in general by direct algebra
  ($8-2^{2-n}<3(n+1)$ for all $n\ge2$), reviewer-reverified for
  $n=2,\dots,19$.

**Certified by:** proof-reviewer, round 9.
