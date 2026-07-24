## Proposition 29b (partial closure of the $\ell(F)=2$, $P\ne\varnothing$ sub-case)

**Status: partial-progress lemma — covers only $\tau_P<p_3$, not the full
sub-case.** Certified here as a reusable partial result, not as a complete
closure of the $\ell(F)=2$, $P\ne\varnothing$ branch.

**Statement.** Fix $n\ge3$ and suppose the standing hypothesis $L(n-1)$
holds (the full unrestricted lower bound one level down, already used
throughout this branch, e.g. by Proposition 26). Let $F=\{v_1,v_2\}\cup P$
with $\ell(F)=2$, $v_1\ge p_2>v_2$, $P$ a nonempty exact pairing with
$\tau_P:=\mathrm{Total}(P)$, and $G'$ any legal refinement of
$\{p_3,\dots,p_{n+1}\}$. If
$$\tau_P\ <\ p_3\ (=p_2/2),$$
then $A(F\cup G')\ge f(n)$ (where $f(n)=a_n=1/(2^{n+1}-1)$).

## Proof

By Proposition 26's reduction (Steps 2-3, which apply verbatim here since
the closed form of $\psi(t):=A(\{t\}\cup P\cup G')$ does not depend on $P$'s
presence — an elementary generalization of the certified fact that exact
pairs are parity-invisible when unioned with an arbitrary reference set: if
$P$ consists of exact equal-value pairs, $N_P(x)$ is even for every $x$, so
$u_{\{t\}\cup P\cup G'}(x)=u_{\{t\}\cup G'}(x)$ pointwise for every $x$),
it suffices to bound $\psi(t^*)$ at $t^*:=p_2-\tau_P$ (the boundary value):
$$\psi(t^*)=A(\{t^*\}\cup G')\ \le\ p_2-f(n) \tag{$\ast$}$$
implies $A(F\cup G')\ge f(n)$.

Since $G'$ is a legal refinement of $\{p_3,\dots,p_{n+1}\}$, by
`safe-window-lemma` one level down, $\max(G')\le p_3$. Since $\tau_P<p_3$,
$$t^*=p_2-\tau_P\ >\ p_2-p_3\ =\ p_3\ \ge\ \max(G')$$
(using $p_2=2p_3$). So $t^*>\max(G')$ strictly, the exact hypothesis of the
certified `sharp-dominant-removal-identity` ($A(\{f_1\}\cup T)=f_1-A(T)$
whenever $f_1>\max(T)$). Applying it with $f_1=t^*$, $T=G'$:
$$A(\{t^*\}\cup G')=t^*-A(G').$$
By `tail-self-similarity` and the standing $L(n-1)$ hypothesis (applied to
the rescaled tail, exactly as in Proposition 26), $A(G')\ge f(n)$. Hence
$$A(\{t^*\}\cup G')=t^*-A(G')\ \le\ t^*-f(n)\ =\ (p_2-\tau_P)-f(n)\ <\ p_2-f(n)$$
(using $\tau_P>0$). This proves $(\ast)$. $\blacksquare$

**Scope note:** the complementary range $\tau_P\ge p_3$ is explicitly **not**
covered — there $t^*\le\max(G')$ can fail to hold, `sharp-dominant-removal-
identity`'s hypothesis genuinely fails, and this is diagnosed (not resolved)
as the same "$v<s$" recursive obstruction Proposition 24 flags one level
down.

## Certification note (proof-reviewer, round 14)

Independently re-verified: (i) the "$P$'s exact pairs are parity-invisible
even when unioned with an extra multiset $G$" generalization, via a fresh
20,000-trial exact-`Fraction` script — zero mismatches; (ii)
`sharp-dominant-removal-identity`'s statement $A(\{f_1\}\cup T)=f_1-A(T)$
for $f_1>\max(T)$, fresh 20,000-trial script — zero mismatches; (iii) the
algebraic chain $t^*=p_2-\tau_P>p_3\ge\max(G')$ under $\tau_P<p_3$; (iv) an
end-to-end simulation on the actual ladder ($n=5$, random $F=\{v_1,v_2\}\cup
P$ satisfying the sub-case-(c) constraints with $\tau_P<p_3$, random legal
$G'$ with correctly-capped remaining cut budget): 3000 valid trials, zero
violations of $A(F\cup G')\ge f(n)$. No gap found in the stated scope.
Correctly and honestly scoped — the file's own text does not claim the
complementary range $\tau_P\ge p_3$ is closed. Certified as a genuine
partial-progress result.

**Origin:** `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
round 14, Proposition 29b.

## Reviewer correction (round 15) — CONFIRMED PROOF GAP, downgraded from full certification

Round 15's `greedy-halving-adversary` builder flagged a likely notational
inconsistency in the proof above; the round-15 proof-reviewer independently
investigated and **confirms this is a real proof gap, not merely cosmetic
notation.**

**The problem.** The Statement above defines $G'$ as "any legal refinement of
$\{p_3,\dots,p_{n+1}\}$" — i.e. **excluding** $p_2$ — whereas the sibling
result this proof imports verbatim (`Proposition 26`) defines its own $G'$ as
a refinement of the *full* tail $\{p_2,\dots,p_{n+1}\}$, **including** $p_2$.
Since $p_2$ must appear *somewhere* in any physically legal final multiset
(it cannot simply be absent), the theorem's real content requires $G'$ to
include $p_2$ (untouched, or itself split). But the proof's Step 4 citation
("$G'$ is a legal refinement of $\{p_3,\dots,p_{n+1}\}$, so by
`safe-window-lemma` one level down, $\max(G')\le p_3$") is **only true when
$p_2$ is excluded from $G'$** — if $p_2$ remains untouched inside the real
$G'$, $\max(G')=p_2>p_3$, and the cited bound is false.

**Independent verification of the gap (round-15 reviewer, fresh scripts, not
the builder's own).** Directly simulating the *actual* game object — $F$
built from a genuine $\ell(F)=2$, $P\neq\varnothing$ split of $p_1$
satisfying $\tau_P<p_3$, unioned with $G'$ = the physically correct **full**
tail refinement (which may leave $p_2$ untouched) — confirms $\max(G')\le p_3$
is false whenever $p_2$ is untouched, exactly as flagged. This means the
proof step as written does **not** establish the theorem for the
game-legal reading of $G'$.

**But no counterexample to the conclusion itself was found.** An adversarial
grid search (fine grid, $n=3,\dots,7$, $G'=$ the full tail entirely
untouched — the specific configuration that breaks the cited step) found
**zero violations** of $A(F\cup G')\ge f(n)$; margins were tiny but strictly
positive ($\approx0.002\times f(n)$ at $n=3$, $\approx0.004\times f(n)$ at
$n=4$, growing for $n\ge5$) — consistent with, and independently confirming,
round 15's own `margin_check.py` finding. So the **stated conclusion appears
to still be true**, but **this specific certified proof does not establish
it** for the game-legal (full-tail) reading of $G'$.

**Status downgraded: this lemma's proof, as written, is NOT valid for the
full-tail (game-legal) reading of $G'$.** It remains a correctly-proved
statement only under the narrower, non-game-legal reading where $G'$
literally excludes $p_2$ (which does not by itself close any part of the
actual lower-bound target, since a real final multiset cannot omit $p_2$).
Do not treat `proposition-29b-partial-closure` as closing any part of the
$\tau_P<p_3$ branch until a corrected proof (handling $\max(G')\le p_2$
rather than $p_3$, or otherwise reworking Step 4) is supplied and
re-verified. Downstream results that cite this lemma (e.g. round-15's Target
B diagnosis, which correctly did *not* rely on it being closed) should be
checked for any other silent dependency on it.
