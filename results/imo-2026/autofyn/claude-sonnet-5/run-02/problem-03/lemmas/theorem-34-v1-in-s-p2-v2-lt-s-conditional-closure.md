# Lemma: Theorem 34 — sub-case (b), $v_1\in(s,p_2)$, $v_2<s$, $v_1+v_2\le p_2$ closure

**CORRECTION (round 19 — supersedes the round-18 hypothesis below).** The
round-18 statement's hypothesis "$R'$ uses $\le n-2$ cuts" is too
generous. Producing $F=\{v_1,v_2\}\cup P$ with $P$ nonempty and
exactly-paired (forced whenever $v_1+v_2<p_1$, the genuinely new content
of this sub-case) costs $\ge3$ cuts on $p_1$ (minimum piece count from
$\{v_1,v_2\}$ plus one matched pair is $4$, requiring $\ge3$ cuts), leaving
at most $n-3$ cuts for $R'$ — not $n-2$. This is not cosmetic: exact
`Fraction` search finds genuine counterexamples to the target inequality
$\Delta(n,v)\le v-f(n)$ under the wrong $n-2$ cap (at every tested
$n=3,4,5,6$), and zero violations under the corrected $n-3$ cap. The proof
below is unaffected step-for-step (it never uses any upper bound on $R'$'s
cut count beyond what is needed to invoke $(\star_{n-2})$ on $R'/s$, and
$n-3<n-2$ automatically satisfies that weaker requirement) — only the
**hypothesis** changes, from "$\le n-2$ cuts" to "$\le n-3$ cuts." See
`approaches/greedy-halving-adversary.md`, "Theorem 34 (corrected, round
19)" for the full derivation and the counterexample search. **Any future
citation of this lemma must use the corrected $\le n-3$ hypothesis below,
not the original round-18 $\le n-2$ version.**

**Source:** `approaches/greedy-halving-adversary.md`, round 18 (proof),
round 19 (hypothesis correction).

**Statement (corrected).** Fix $n\ge3$ and suppose $(\star_{n-2})$ holds
(every legal Xiang-Yu response, $\le n-2$ cuts, to the $(n-2)$-ladder has
$A\ge f(n-2)$; unconditional for $n\le4$). Let $F=\{v_1,v_2\}\cup P$ with
$\ell(F)=2$, $P$ pairing up exactly, $v_1\in(s,p_2)$, $v_2\in(0,s)$, and
$v_1+v_2\le p_2$. Let $G'=\{p_2\}\cup R'$ where $R'$ is a legal refinement
of $\{p_3,\dots,p_{n+1}\}$ using $\le n-3$ cuts (the actual game-legal cap
for this configuration, per the correction above). Then
$$A(F\cup G')\ \ge\ f(n).$$

**Proof.** Write $J_0:=\int_0^{v_2}u_{R'}(x)\,dx$. Since $v_2<s\le v_1$,
$[v_2,v_1)=[v_2,s)\cup[s,v_1)$ with $u_{R'}\equiv0$ on $[s,v_1)$ (as in
Theorem 33), so $\int_{v_2}^{v_1}u_{R'}=\int_{v_2}^{s}u_{R'}=A(R')-J_0$.
Substituting into the Step-1 identity,
$$A(F\cup G')=p_2-A(R')-(v_1-v_2)+2(A(R')-J_0)=p_2+A(R')-2J_0-(v_1-v_2).$$
Since $u_{R'}$ is $\{0,1\}$-valued, $J_0\le v_2$, so
$$A(F\cup G')\ge p_2+A(R')-2v_2-(v_1-v_2)=p_2+A(R')-(v_1+v_2).$$
By `tail-self-similarity` and $(\star_{n-2})$ applied to $R'/s$ (legal
since $R'$ uses $\le n-3\le n-2$ cuts, so is in particular a legal
$\le(n-2)$-cut response, and $\{p_3,\dots,p_{n+1}\}/s$ is exactly
the $(n-2)$-ladder), $A(R')\ge s\cdot f(n-2)=f(n)$ (cross-level identity,
as in Proposition 24). Substituting and using $v_1+v_2\le p_2$,
$$A(F\cup G')\ge p_2+f(n)-(v_1+v_2)\ge p_2+f(n)-p_2=f(n).\qquad\blacksquare$$

**Status.** Proved in full, conditional on $(\star_{n-2})$; unconditional
for $n\le4$ (same conditioning discipline as Proposition 24). Hypothesis
on $R'$'s cut budget corrected to $\le n-3$ as of round 19 (see correction
note above) — this narrows, and does not invalidate, the round-18 proof.

**Independent verification (reviewer, round 18, cap-corrected round 19).**
Fresh 12,000-trial exact-`Fraction` script, $n=3,\dots,6$ (3000 trials per
$n$), with $R'$ cut-budget capped at $n-2$ (round-18 script — **now known
to be the wrong, too-generous cap**), $v_1\in(s,p_2)$, $v_2\in(0,\min(s,
p_2-v_1))$ enforced (both $v_2<s$ and $v_1+v_2\le p_2$): zero violations
of *this lemma's own target* ($A(F\cup G')\ge f(n)$, a weaker statement
than $\Delta(n,v)\le v-f(n)$) were found even under the wrong cap — this
lemma's proof only ever needs $A(R')\ge f(n)$, which round 18's script
happened to test correctly; it is the *separate*, sharper target
$\Delta(n,v)\le v-f(n)$ (relevant to the still-open middle band, not to
this lemma's own already-closed statement) where the $n-2$ vs. $n-3$ cap
distinction is load-bearing. Round 19 (proof-reviewer): independently
re-derived the $\ge3$-cuts piece-counting argument for the corrected cap
and independently re-verified, with a freshly written script, that
$\Delta(n,v)\le v-f(n)$ has genuine counterexamples under the (wrong)
$n-2$ cap at $n=3,4,5$ and zero violations under the corrected $n-3$ cap
at $n=3,\dots,6$ — CERTIFIED, with the corrected hypothesis.

**Scope.** Closes the sub-branch $v_2\in(0,p_2-v_1]$ of $v_2<s$ (note
$p_2-v_1<f(n)<s$ always here since $v_1>s$, so this range is entirely
inside $v_2<s$). Combined with Theorem 33's $v_2\in[s,v_1)$, the residual
open band is $v_2\in(p_2-v_1,s)$ for each $v_1\in(s,p_2)$ — not
negligible in width, and diagnosed (not closed) as the same round-15/16
crux (an upper bound on the truncated sum $A(R'_{>v_2})$).

**Certified by:** proof-reviewer, round 18 — independently re-derived the
proof by hand and re-verified numerically with a fresh script: CERTIFIED.
