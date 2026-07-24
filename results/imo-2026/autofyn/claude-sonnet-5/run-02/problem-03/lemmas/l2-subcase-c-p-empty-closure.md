# ℓ(F)=2 Sub-case (c) Closure at P=∅ (Proposition 26)

**Source:** `results/imo-2026-03/approaches/greedy-halving-adversary.md`,
Proposition 26 (round 12).

**Statement.** Fix the $n$-ladder ($n\ge2$) and suppose $L(n-1)$ holds
(every legal Xiang-Yu response, budget $\le n-1$, to the $(n-1)$-ladder has
$A\ge f(n-1)$). Let $F=\{v_1,v_2\}$ with $v_1+v_2=p_1$, $v_1>v_2>0$ (the
unique-minimal-cut, $c=1$ split of $p_1$; automatically $v_1\ge p_2>v_2$ by
the doubling identity $p_1=2p_2$). Let $G'$ be any legal refinement of the
tail using $\le n-1$ cuts. Then
$$A(F\cup G')\ \ge\ f(n).$$

**Proof mechanism** (see approach file for full derivation): (1) Lemma 25's
sub-case (c) identity reduces the claim to $A(\{v_2\}\cup G')\le
(p_1-v_2)-f(n)$; (2) the certified `cross-term-identity-threshold` (Lemma 8)
gives an explicit closed form $\varphi(t):=A(\{t\}\cup G')$, purely
algebraic in the real variable $t$; (3) $D(t):=((p_1-t)-f(n))-\varphi(t)$
has derivative $\le0$ a.e. (since $\varphi'(t)=1-2v_{G'}(t)\in\{-1,1\}$), so
$D$ is non-increasing on $(0,p_2]$, reducing the claim to the single
boundary check $D(p_2)\ge0$; (4) at $t=p_2$, `safe-window-lemma` gives the
exact truncation $\int_0^{p_2}v_{G'}=A(G')$, so $\varphi(p_2)=p_2-A(G')$,
and $D(p_2)\ge0\iff A(G')\ge f(n)$ — exactly `tail-self-similarity` +
$L(n-1)$ applied to the rescaled tail (using $G'$'s full $(n-1)$-cut
budget).

**Scope — exactly as proved, no more.** This closes sub-case (c)
(the mixed regime $v_1\ge p_2>v_2$ of the $\ell(F)=2$ branch) **only** for
$P=\varnothing$, i.e. the minimal-cut $c=1$ split of $p_1$ into exactly two
unequal fragments with no further exact pairing. The $P\ne\varnothing$
extension ($c\ge3$) is explicitly **not** covered — the approach file gives
a precise diagnosis of why the mechanism breaks there (the safe-window
truncation identity is exact only at $t=p_2$, not at the shifted boundary
$t^*=p_2-\mathrm{Total}(P)<p_2$) and records it as a distinct, still-open
item.

**Verification.** Reviewer-independently re-verified, round 12
(`/tmp/round-12/verify_prop26_independent.py`, fresh script, not the
builder's own): (i) the final bound $A(F\cup G')\ge f(n)$ directly, 7500
trials, $n=2,\dots,6$, random $v_2\in(0,p_2)$ and random legal $G'$ of
budget $\le n-1$, zero violations; (ii) the Lemma-25 sub-case (c) identity
$A(F\cup G')=v_1-A(\{v_2\}\cup G')$, 5000 trials, zero mismatches; (iii)
the endpoint identity $\varphi(p_2)=p_2-A(G')$, 2500 trials, zero
mismatches; (iv) the monotonicity of $D(t)$ along 6 sampled points per
trial, 4800 trials, zero violations. All checks independent of the
builder's own `/tmp/round-12/check_subcase_c.py`.

**Dependencies (all already certified):** `cross-term-identity-threshold`
(Lemma 8), `safe-window-lemma`, `tail-self-similarity`, `l2-general-exact-
identity` (Lemma 25), `general-ladder-dominance` (Lemma 23, for
$p_1=2p_2$).

**Certified by:** proof-reviewer, round 12. CERTIFIED — for its exact
scope ($P=\varnothing$ instance of sub-case (c), conditional on $L(n-1)$).
Not certified as a closure of sub-case (c) in general — the $P\ne\varnothing$
complement remains open and is a separate, precisely-diagnosed item on
record in the approach file.
