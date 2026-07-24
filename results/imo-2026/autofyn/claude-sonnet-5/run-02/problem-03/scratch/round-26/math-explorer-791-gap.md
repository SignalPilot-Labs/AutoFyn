## Scouting report: the (7.9.1) / MinFloor-MaxCeil residual gap (rank-pigeonhole-budget, §7.9-7.10)

### 0. What's actually on file

`rank-pigeonhole-budget.md`'s §7.9 (round 24) breaks Case (b)'s "$v\ge a$",
$T'$-cuts-$p_4$ sub-case into 4 breakpoint candidates for the free insert
value $b$ (Single-Insert-Point Vertex Lemma applied to $T=T'=\{c_1,c_2\}\cup
T'''$, $c_1\ge c_2$, $c_1+c_2=p_4$):
- $b=0$: closed via $(\star_{n-3})$.
- $b=p_4$: dominated by $b=c_1$ (Box-Endpoint Domination Fact), needs no bound.
- $b=c_1$: reduces via pair-cancellation to $A(\{c_2\}\cup T''')$ — an
  **open lower-bound recursion**, explicitly flagged in the file as "the
  sibling's $h(m)$-shaped object one level further down."
- $b=c_2$: reduces to $A(\{c_1\}\cup T''')=c_1-A(T''')$ (generic case,
  `sharp-dominant-removal-identity`), giving the target **upper bound**
  $$A(T''')\le c_1-f(n).\tag{7.9.1}$$

§7.10 (round 25) reduces (7.9.1) at its hardest instance (symmetric split
$c_1=c_2=p_4/2$) to $\mathrm{MaxCeil}(m)$, $m=n-3$, on the ratio-2 tail
$\sigma=\{p_5,\dots,p_{n+1}\}$, where (for a length-$\ell$ ratio-2 tail
$\sigma$, $R(\sigma)+\sigma_\ell=2\sigma_1$ certified identity):
$$\mathrm{MinFloor}(\ell):\ A(S)\ge\sigma_\ell\ \ (\le\ell-1\text{ cuts}),\qquad
\mathrm{MaxCeil}(\ell):\ A(S)\le\sigma_1-\sigma_\ell\ \ (\le\ell-2\text{ cuts}).$$
Each splits on whether $\sigma_1$ is cut. "Top untouched" is closed for
**both** — trivially for $\mathrm{MinFloor}$ (peel $\sigma_1$, Fact 2:
$A\le\mathrm{Total}$), and $\mathrm{MaxCeil}(\ell)$'s untouched branch
reduces exactly to $\mathrm{MinFloor}(\ell-1)$. "$\sigma_1$ cut" is open for
**both** quantities, hand-checked only at $\ell\le3$ (numerically
consistent, not proved).

### 1. Is this the same wall as Theorem 37's non-maximal-tie gap? — No, but one piece of it literally *is* the same object as a different part of Theorem 37's own file.

Read `greedy-halving-adversary.md` around Theorem 37 (line ~5010) and its
"Diagnostic finding" (line ~5062) carefully. Theorem 37 attacks the
**complementary** sub-case: $T'$ *leaves $p_4$ untouched*
($T'=\{p_4\}\cup T''$), symmetric split $a=b=p_4$. It proves $A(B)=A(T'')\ge
f(n)$ conditional on $(\star_{n-4})$, by rescaling $T''$ (a refinement of
$\{p_5,\dots\}$) down to a smaller ladder and invoking the standing
hypothesis directly — a one-step closure, no recursion needed.

Theorem 37's own **remaining gap** (its "Still open (i)") is: *within the
$T'$-untouched branch*, is the symmetric-split/$p_4$-untouched vertex really
the **global** minimizer over the whole $(b,T')$ family, or could $b$ tying
to some **non-maximal** element of $T''$ (not $p_4$) do worse? This is a
vertex-enumeration question internal to the $T'$-untouched branch. It is
**not** the same statement as (7.9.1) — (7.9.1) lives entirely inside the
*other* branch ($T'$ cuts $p_4$).

However, Theorem 37's own **"Diagnostic finding"** (the "$T'$ cuts $p_4$"
case it checked as a side investigation) is verbatim the same object as
rank-pigeonhole's §7.9.4 breakpoint $b=c_1$: both independently derive, by
the identical pair-cancellation step, that the residual is
$A(\{c_2\}\cup T''')$ (greedy's notation: $A(T'\setminus\{\max T'\})$ with
$T'=\{c_1,c_2\}\cup T'''$), and both explicitly flag it as "not a rescaled
ladder, hence not closable by the Cross-Level Rescaling Lemma; a genuine
recursion, one level down, of the *same shape* as the original problem."
So **this one piece is a confirmed, already-cross-referenced overlap** — a
real, useful triangulation (independent discovery of the identical
sub-object from two different starting points) but it is the $b=c_1$
breakpoint, **not** (7.9.1) (which is the *different* breakpoint $b=c_2$).

**Bottom line on question (1):** three genuinely distinct open items sit
inside Case (b)'s "$v\ge a$" branch, not one:
1. Theorem 37's internal non-maximal-tie enumeration ($T'$-untouched branch).
2. The $b=c_1$ recursion, $A(\{c_2\}\cup T''')$ ($T'$-cuts-$p_4$ branch) —
   independently hit by both files, still open, not (7.9.1).
3. (7.9.1) itself / $\mathrm{MaxCeil}(m)$'s "top cut" branch — the $b=c_2$
   breakpoint. Not (yet) attacked by `greedy-halving-adversary` at all.
Closing any one does **not** automatically close the others; they are
siblings sharing the same "odd-run/pair-cancellation collapses to a smaller
non-ladder residual" DNA, not literally the same inequality.

### 2. The high-value structural finding: MinFloor(ℓ) *is* the standing hypothesis $(\star_{\ell-1})$

Check the exact definitions. $(\star_m)$ (used throughout the whole project,
e.g. Theorem 36b, Theorem 37) means: *every legal response ($\le m$ cuts) to
the $m$-ladder ($m+1$ pieces, ratio 2) has $A\ge f(m)$* — i.e. it **is** the
project's own master theorem, unrestricted, at level $m$ (no Claim-A-style
"tail untouched" restriction).

$\mathrm{MinFloor}(\ell)$'s domain is exactly: a length-$\ell$ ratio-2 tail
($=$ an $(\ell-1)$-ladder), refined with $\le\ell-1$ cuts (the full legal
budget), target $A(S)\ge\sigma_\ell$ ($=f(\ell-1)$ in normalized units).
**This is not an approximation of $(\star_{\ell-1})$ — it is $(\star_{\ell-1})$
verbatim**, with $m=\ell-1$.

Consequences, not yet drawn out in the approach file:
- $\mathrm{MinFloor}(\ell)$'s "top untouched" branch, closed this round via
  one line, is **the well-known "$c=0$" sub-case** solved back in round 1-2
  of `greedy-halving-adversary` (dominant-element-removal identity) — real
  and correctly reusable, but not new content; it is a re-derivation, in
  new notation, of an old fact.
- $\mathrm{MinFloor}(\ell)$'s open "top cut" branch is **not** a fresh,
  bespoke sub-lemma to invent — it is exactly $(\star_{\ell-1})$'s own
  "$c\ge1$" case, i.e. the *entire remaining unsolved content of the whole
  project*, recursed to a smaller $n$. Tracing the index arithmetic: (7.9.1)
  $\Leftrightarrow\mathrm{MaxCeil}(m)$, $m=n-3$; its untouched branch
  $\Leftrightarrow\mathrm{MinFloor}(m-1)=\mathrm{MinFloor}(n-4)=(\star_{n-5})$.
  So (half of) (7.9.1)'s open content is precisely $(\star_{n-5})$,
  **already unconditionally TRUE whenever $n-5\le2$, i.e. $n\le7$** (since
  $(\star_1),(\star_2)$ are the fully-closed $n=1,2$ base cases on file).
  **This should be stated as "conditional on $(\star_{n-5})$" in the exact
  style already used for Theorem 36b/37**, not left as an undifferentiated
  "open gap requiring new machinery" — it is free for $n\le7$ and reduces
  the induction depth needed for larger $n$ to exactly what every other
  $(\star_{n-k})$-conditional result in the population already assumes.
  (Caveat: double-check the index arithmetic above independently before
  building on it — it was derived by direct substitution into the file's
  own definitions, not copied from any existing lemma.)
- $\mathrm{MaxCeil}(m)$'s **own** "top cut" branch (a separate item per
  §7.10.4, not yet reduced to anything named) is *not* obviously
  $(\star_{\cdot})$-shaped in the same way, since it is an upper-bound
  target ($A(S)\le\sigma_1-\sigma_\ell$), a different flavor from the
  project's lower-bound master statement. This piece genuinely looks like
  fresh content, not a restatement of the standing hypothesis.

### 3. Smallest concrete instance to hand-check

The file's own §7.10.6 only checks $\ell\le3$ **numerically** at
$\sigma=(4,2,1)$ and calls it "not proved for general $\sigma_1$-multi-way
splits." But $\ell=3$ has budget $\mathrm{MaxCeil}$: $\le1$ cut,
$\mathrm{MinFloor}$: $\le2$ cuts — small enough to close **exactly by hand**,
not just numerically. I did this by direct case-split (single free
variable, exactly the shape the certified Single-Insert-Point Vertex Lemma
already covers):

$\sigma=(4,2,1)$, $\mathrm{MaxCeil}(3)$ (need $A(S)\le3$), $\sigma_1=4$ cut
into $(a,4-a)$, rest $\{2,1\}$ untouched, WLOG $a\in(0,2]$:
- $a\in(0,1)$: sorted order $(4-a,2,1,a)$, $A=(4-a)-2+1-a=3-2a\le3$
  (holds for every $a>0$, strict).
- $a\in[1,2]$: sorted order $(4-a,2,a,1)$, $A=(4-a)-2+a-1=1\le3$ (holds
  with large margin).

So **$\mathrm{MaxCeil}(3)$'s "top cut" branch is fully, exactly closed by
hand** — a one-variable case split, no numerics needed. This one-variable
tightness (budget $\le1$ cut $\Rightarrow$ exactly one free coordinate)
means the certified **Single-Insert-Point Vertex Lemma** already suffices
here directly; §7.10.6's "not proved" framing for $\ell=3$ looks
overcautious — this specific instance is a same-round, low-risk closure
the team appears to have missed. I did the analogous check for
$\mathrm{MinFloor}(3)$ by a 500,000-trial exact-float random search over
all $\le2$-cut splits of $(4,2,1)$ with at least one cut on $\sigma_1$: the
minimum found was **exactly 1.0 $=\sigma_3$** in every run (e.g.
$S\approx(0.163,\,2.563,\,1.274,\,2,\,1)$, $A(S)=1.0$ exactly), never below
— consistent with, but (with 2 free coordinates) not yet a hand-proof of,
$\mathrm{MinFloor}(3)$'s open branch.

For a genuinely still-live (not hand-closable in one step) instance,
**$\ell=4$** is the right target: $\mathrm{MaxCeil}(4)$ has $\le2$ cuts
(two free coordinates once $\sigma_1$ is split — a real 2-D polytope, no
longer a trivial 1-D slope argument), corresponding via the chain above to
$m=n-3=4$, i.e. **$n=7$** in the original problem. Concretely:
$\sigma=(8,4,2,1)$ (or any ratio-2 4-tuple), $\sigma_1=8$ split into 2 or 3
parts using up to 2 cuts, remainder of $(4,2,1)$ possibly also touched
(within the shared 2-cut budget), target $A(S)\le\sigma_1-\sigma_4=8-1=7$.
This is the smallest instance exercising genuine multi-coordinate freedom
and is the natural next hand/exact-`Fraction` check.

### 4. Proposed mechanism

- **For $\mathrm{MaxCeil}(3)$/$\mathrm{MinFloor}(3)$ and likely
  $\mathrm{MaxCeil}(4)$/$\mathrm{MinFloor}(4)$:** don't invent new
  machinery — directly reuse the already-certified **Single-Insert-Point
  Vertex Lemma** (1 free coordinate: $\ell=3$ case, exactly the situation
  above) and the **Case-I-Closure-style exchange-smoothing-vertex-
  maximization** (certified, round 8; proved for exactly the shape "a box-
  constrained partition merged with a fixed ratio-2 tail," which is what a
  2-cuts-on-$\sigma_1$-plus-tail configuration looks like) for the 2-free-
  coordinate case. Both tools are already in the toolbox and were built for
  literally this vertex-reduction shape; the missing step in §7.10 looks
  like it was time-boxed before trying them, not that they were tried and
  found insufficient.
- **Naive combination check (result: insufficient, as expected).** I tested
  `Triangle Bound for A` ($A(X\cup Y)\le A(X)+A(Y)$) plus `Max Domination
  Lemma` ($A(X)\le\max(X)$) as a cheap shortcut for $\mathrm{MaxCeil}(3)$:
  splitting $S=F_1\cup\{2,1\}$ with $F_1=\{a,4-a\}$ gives
  $A(S)\le\max(F_1)+A(\{2,1\})=(4-a)+1=5-a$, which only implies the target
  $\le3$ when $a\ge2$ — **false for $a<2$** (matching the project's already-
  recorded pattern that `Fact 2`/naive combos are too lossy, e.g. §7.9.5's
  own finding that `Fact 2` alone fails for (7.9.1)). The exact hand
  computation above (§3) shows the true value is much smaller ($3-2a$ or
  $1$), so the *true* mechanism is the exact vertex/slope evaluation, not a
  generic sub-additivity bound — reinforcing that the Single-Insert-Point/
  exchange-smoothing route (which evaluates exactly, not via a lossy
  triangle inequality) is the right tool, not `Triangle Bound`+`Max
  Domination`.
- **Recommended framing for next round:** (a) explicitly hand-close
  $\mathrm{MaxCeil}(3)$ (done above, ready to drop in) and attempt
  $\mathrm{MaxCeil}(4)$/$\mathrm{MinFloor}(4)$ by the 2-coordinate
  exchange-smoothing machinery; (b) restate the $\mathrm{MinFloor}(\ell)$
  "top cut" branch's true logical status as "$\Leftarrow(\star_{\ell-1})$,
  unconditional for $\ell-1\le2$" rather than an undifferentiated new open
  item, and double-check the index chain in §2 above independently; (c)
  treat $\mathrm{MaxCeil}(m)$'s own "top cut" branch as the one piece that
  is genuinely new content requiring fresh work, separate from (and not
  reducible to) the standing hypothesis.
