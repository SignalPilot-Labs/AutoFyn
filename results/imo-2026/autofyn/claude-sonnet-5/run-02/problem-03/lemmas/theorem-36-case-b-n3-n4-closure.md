## Theorem 36 — Case (b) ("$p_3$ is cut") of Theorem 35's residual middle band, closed at $n=3$ (vacuous) and $n=4$ (direct computation) — new round 20, certified by reviewer

**Scope.** This closes the target $(\Diamond)$: $\Delta(n,v)\le v-f(n)$
for $\Delta(n,v):=A(R')-2A(R'_{>v})$, restricted to the sub-family of legal
$R'$ (a $\le(n-3)$-cut refinement of the ratio-2 tail $\{p_3,\dots,
p_{n+1}\}$, total $s$) in which $R'$'s own top piece $p_3$ is cut — "Case
(b)" of Theorem 35 (`greedy-halving-adversary.md` §Theorem 35). **This
lemma is explicitly scoped to $(\Diamond)$, not the strictly stronger
epsilon-aware target $(\Diamond')$** ($\Delta(n,v)\le v-f(n)-2v\epsilon(v)$,
$\epsilon(v)=\mathbb1[|R'_{>v}|\text{ odd}]$) needed for the full two-variable
middle-band claim when $\epsilon(v)=1$ — that bridge remains open on both
sibling fronts (see reviewer note, round 20).

**Statement.**
- *$n=3$:* Case (b) is vacuous — the corrected cut-budget cap forces $R'$
  to use $0$ cuts total, so $p_3$ cannot be split at all.
- *$n=4$:* for every legal Case-(b) response $R'=\{a,b,p_4,p_5\}$
  ($a+b=p_3$, $a\ge p_4\ge b>0$) and every $v\in(0,s)$, $\Delta(4,v)\le
  v-f(4)$ holds unconditionally (no induction hypothesis).

**Proof.**
- *$n=3$:* mass conservation forces $\ge1$ cut to split $p_3=\{a,b\}$
  ($a,b>0$); the total budget at $n=3$ is $n-3=0$; hence Case (b) cannot
  occur. Every legal $R'$ at $n=3$ is $\{p_3,p_4\}=\tau$, untouched.
- *$n=4$:* budget is $n-3=1$; Case (b) requires $\ge1$ cut on $p_3$, so
  that single cut is the entire budget and $T'=\{p_4,p_5\}$ is forced
  untouched. Writing $u:=f(4)=p_5$ (so $p_4=2u,p_3=4u,p_2=8u,s=7u$), split
  on $b\in[u,2u]$ vs. $b\in(0,u)$ (exhaustive, disjoint, since $b\le p_4=2u$
  always): in each sub-case, $A(R')$ is a closed form in $b$ (constant $u$
  in sub-case I; $3u-2b$ in sub-case II), and $R'_{>v}$ changes only at the
  (at most) four breakpoints $\{b,u,2u,a\}\cup\{a\}$, giving five
  sub-ranges of $v$ per sub-case, each with a closed-form $\Delta(4,v)$;
  the target inequality is checked directly (algebraically) at each
  sub-range's hardest point. All ten sub-range checks close, several with
  exact equality at isolated points (e.g. $v=a$ or the boundary tie
  $a=b=2u$), consistent with this being a tight bound.

**Reviewer independent verification (round 20).** Re-derived the $n=3$
vacuity argument from scratch (matches). For $n=4$: wrote a fresh script
(structurally independent of the builder's) re-deriving all ten closed-form
sub-range formulas against direct sort-and-alternate computation
(20,000 trials/sub-case, zero mismatches), confirmed the boundary tie
$a=b=2u$ explicitly (exact equality $\Delta=v-u$ at $v=2u$), and ran a
separate fully-continuous-random check (500,000 trials, $b,v$ both
uniform over their full legal ranges, not restricted to breakpoints): zero
violations, minimum margin $77/31{,}000{,}000\approx2.5\times10^{-6}>0$.
**Certified.**

**What this does NOT establish.** General $n\ge5$ (Case (b)'s budget
$n-3\ge2$ allows $T'$ to carry cuts and multi-cut-on-$p_3$ responses,
neither reached by this mechanism); and — for every $n$ including $3,4$ —
the epsilon-aware bridge to the true two-variable middle-band target
$(\Diamond')$ when $\epsilon(v)=1$ (see reviewer's round-20 finding that
this gap is non-vacuous even at $n=3,4$, though numerically confirmed true
end-to-end there).
