## imo-2026-03 (lens: Claim (B) — closing the "p2-cut complement" of Proposition 22)

### Scope of this report
Scouting only (no proof attempted). Focus: (a) precisely diagnose what breaks in
Proposition 22's mechanism when $p_2$ (equivalently $q_1$ in the rescaled picture)
is itself cut by $G'$; (b) whether $v<p_2$ shares machinery with the p2-cut case;
(c) an actual attempt to resolve numerically whether $\ell(F)\ge2$ ever violates
Claim (B).

### 1. What exactly breaks when $p_2$ is cut (the open complement of Proposition 22)

Proposition 22's argument, rescaled to the $(n-1)$-ladder $Q=\{q_1,\dots,q_{m+1}\}$
($m=n-1$), is a **single dominant-element peel**: it assumes $G'$ leaves $q_1$
untouched, so the refined multiset is exactly $\{q_1\}\cup R'$ with $R'$ a
refinement of $Q$'s own tail $R=\{q_2,\dots,q_{m+1}\}$. This lets it invoke
`dominant-element-removal-identity` (Lemma 7) verbatim: $A=q_1-A(R')$, because
$q_1$ alone exceeds the total of *everything else in the multiset*
($q_1 > \mathrm{Total}(R) = 1-q_1$, verified: $q_1>1/2\iff 2^{m+1}>2^{m+1}-1$, true).

**The break:** the moment $G'$ spends even one cut on $q_1$ (i.e. "cuts $p_2$"
in the unrescaled picture), $q_1$ no longer exists as a single element of the
final multiset — it is replaced by $\ge2$ fragments summing to $q_1$. Lemma 7
needs one literal dominant *element*, not a dominant *total*; there is no
longer any single fragment guaranteed to exceed the total of all the rest
(fragments of $q_1$ are each $<q_1$, and $q_1$ was only barely dominant —
$q_1>1-q_1$ by margin $2/(2^{m+1}-1)$ — so no fragment of $q_1$ below, say,
$q_1/2$ can inherit the dominance). **Concretely checked:** the smallest
possible fragment of a 1-cut split of $q_1$ can be made arbitrarily small, and
then trivially fails $M_1>T-M_1$. So Lemma 7 is simply inapplicable to the
p2-cut sub-case; a literally different tool is needed, not a tweak of the same
one.

### 2. The self-similarity opening (the main new observation this round)

Once $q_1$ is cut, the sub-instance $(q_1\text{'s split})\cup R'$ has **exactly
the same shape** as the *original* problem's $\ell(F)=1,\,v\ge p_2$ setup, one
level down: Xiang Yu splits the current ladder's top piece ($q_1$, playing the
role $p_1$ played at level $n$), and refines the current ladder's own tail
($R$, playing the role $\tau$ played at level $n$). This is a genuine
structural recursion, not a superficial analogy — `tail-self-similarity`
already establishes $R/(1-q_1)$ is exactly the $(m-1)$-ladder.

**Concrete opening:** if $q_1$'s own split (induced by $G'$'s cuts that land in
$[0,p_2]$) again has odd-run-length exactly 1 with residual $w\ge q_2$ (the
*current* ladder's own second piece), then Proposition 20's identity applies
recursively at level $m=n-1$: $A(q_1\text{-split}\cup R')=w-A(R')$, and one can
try to chain Proposition 21/22's argument down another level. This gives a
concrete, well-defined **recursive plan**: attack the p2-cut complement not as
a single new lemma but as a second application of the *already-proved*
Prop 20–22 machinery to the rescaled sub-instance.

**Why this does not close the gap by itself (the catch, must be flagged to the
outliner):** the recursion only fires when $q_1$'s own split again lands in the
"$\ell=1$, $w\ge q_2$" family. In general $G'$'s cuts inside $[0,p_2]$ can
produce **any** split of $q_1$ — $\ell=0$ (exact bisection, covered instead by
the already-certified `cross-term-vanishing-lemma` for fully-paired splits),
$\ell=1,w<q_2$ (this is the **same open $v<p_2$ case**, recursed one level
down, not resolved), or $\ell\ge2$ (the still-open general case, numerically
supported this round but not proved — see §3). So the p2-cut complement is
**not a free corollary**; it is *exactly the same open problem* (the union of
all three still-open branches) posed one level lower, on a strictly smaller
ladder. A correct strong induction on $n$ that closes all of $(\dagger)$
(hence Claim B on the $\ell(F)=1,v\ge p_2$ family) would need the **full**
inductive hypothesis at $n-2$ (not just the bare lower bound $(\star_{n-2})$
Proposition 22 currently uses) — i.e. it would need to already know Claim B
in general one level down, which is circular unless every branch (fully-paired,
$v\ge p_2$, $v<p_2$, $\ell\ge2$) is independently closed at *every* level as
part of one simultaneous strong induction. **Net: the self-similarity is real
and structurally clean, but it converts "close the p2-cut complement" into
"close the whole open problem for $n-2$" — it is a reformulation, not a
reduction to something easier**, mirroring the diagnosis already on file for
`lp-duality-certificate`'s Theorem C′ coupling (round 9) and
`case-ii-exact-peel-identity` (round 7): this is the third independent place
in this project where an "exact identity" reduction turns out to be logically
equivalent to (not weaker than) the target.

### 3. The $v<p_2$ case: separate mechanism, or shares machinery with p2-cut?

**Largely a separate mechanism**, per the approach file's own honest diagnosis
(confirmed here): Proposition 20's truncation trick needs $v\ge p_2$ essentially
(to make `safe-window-lemma` kill $v_{G'}$ on the tail past $p_2$). For
$v<p_2$, $\int_0^v v_{G'}\,dx$ does not obviously collapse to $A(G')$ or any
other clean closed form.

**One new idea worth flagging (untested, not developed into a proof):**
when $v<p_2$ and $G'$ leaves $p_2$ itself untouched, $p_2$ becomes the single
largest element among $P\cup\{v\}\cup G'$ (since $v<p_2$ and, by
`safe-window-lemma`, every fragment of $G'$ is $\le p_2$ too — but ties are
possible). Checked numerically whether $p_2$ dominates the *whole* rest of the
multiset (i.e. whether Lemma 7 could be invoked with $M_1=p_2$): this
requires $p_2>1-p_2$, i.e. $p_2>1/2$ — **false** for every ladder (verified
exactly: $p_2=2^{n-1}/(2^{n+1}-1)<1/2$ for all $n\ge2$, e.g. $n=2$: $2/7$).
So a direct "peel $p_2$ instead of $p_1$" move does **not** satisfy Lemma 7's
hypothesis against the *entire* remaining multiset — only against $\tau$'s own
residual tail $\{p_3,\dots,p_{n+1}\}$ alone (verified: $p_2>1/4$ always, which
is exactly the scale-invariant dominance fact already used inside
`tail-self-similarity`/Proposition 22, just one level up from where it's
normally applied). This rules out the most obvious "swap the dominant
element" idea as stated; a genuinely different decomposition of the multiset
(e.g. peeling $p_2$ against just $\tau\setminus\{p_2\}$ while separately
tracking $v$ and $P$'s interaction with $p_2$) would be needed, and was not
found this round. **Recommendation: treat $v<p_2$ as its own open item, not
a free consequence of closing p2-cut**, though both items would benefit from
the same underlying missing tool (an *exact*, not just lower-bound, handle
on a foreign/reduced tail instance) — consistent with round 7/9's repeated
diagnosis that this is the single deepest missing tool in the whole project.

### 4. Numeric resolution attempt: does $\ell(F)\ge2$ ever violate Claim (B)?

Ran two independent, from-scratch searches (not reusing round-9's scripts,
which no longer exist on disk) filtering directly on Xiang Yu's split $F$ of
$p_1$ alone (not the whole-multiset proxy $\ell(S)$ round 9 flagged as
non-isolating):

**(a) Uniform random search, exact `Fraction`,** filtering strictly to
configurations with $\ell(F)\ge2$ (computed on $F$ alone before fusing with
$G'$), $n=2,\dots,6$, 60,000 trials each (`/tmp/round-10/check_ellF_ge2.py`):
zero violations of $A(F\cup G')\ge f(n)$ at every $n$; at $n=2,3,4$ the search
found the bound achieved with **exact equality** ($\text{margin}=0$) at
genuine $\ell(F)\ge2$ configurations, not just near-degenerate ones.

**(b) Coordinate-descent/local-search global minimization of $\Phi$**
(float, then structurally inspected — `/tmp/round-10/local_search_ellF.py`),
searching over Xiang Yu's actual mark positions (not the $F$/$G'$ split
directly, to avoid biasing toward any one decomposition), $n=3,4,5$, 40
restarts × 4000 iterations each: every restart converges to $\Phi=a_n$ exactly
(margin $0$ to float precision), and the minimizing configurations
consistently involve **multiple nonzero fragments of $p_1$** (i.e. genuine
$\ell(F)\ge2$-flavored splits, not $\ell(F)\in\{0,1\}$) — though the smallest
fragment shrinks toward $0$ as the search converges, suggesting these
particular minimizers are converging toward the already-known $c=n$
"cascading/rescaled-ladder" boundary family (`rescaled-ladder-c-equals-n-
achievability`) rather than exposing a new interior tie-vertex family.

**Conclusion (numeric, not a proof):** across both a broad filtered random
search and an unconstrained global-minimization search, **no evidence of a
violation for $\ell(F)\ge2$ was found** up to $n=6$. This is a genuine (if
partial) resolution of round 9's "unresolved numerically" flag — the honest
answer this round is "searched harder, still no counterexample," which
supports (but does not prove) that $\ell(F)\ge2$ does not need separate,
harder-than-$\ell\le1$ treatment; the difficulty is likely uniform across
$\ell(F)$ values, i.e. the *same* missing exact-tail-bound tool, not an
extra obstruction specific to higher $\ell$.

### Distinct openings for the outliner
1. **Recursive self-similar attack on the p2-cut complement** (§2): apply
   Prop 20/21 recursively to the rescaled sub-instance $(Q,\text{split of }q_1,R)$.
   Concrete but **only closes the p2-cut complement's own "$\ell=1,w\ge q_2$"
   branch**, deferring the rest (fully-paired via `cross-term-vanishing-lemma`,
   $\ell\ge2$ still fully open, $v<p_2$-at-that-level still open) — genuine
   partial progress in a well-defined recursive shape, not a full closure.
2. **A full simultaneous strong induction across $n$** that assumes the
   *entire* theorem (all branches) below $n$, rather than incrementally
   patching one branch at a time — matches the self-similarity found in §2,
   and is the natural way to make Proposition 22's technique actually close
   $(\dagger)$ in full, but requires closing $\ell\ge2$ and $v<p_2$ at every
   level too (not avoided, just made explicit and uniform).
3. **Attack $v<p_2$ directly via a two-piece decomposition** (peel $p_2$
   against $\tau\setminus\{p_2\}$ only, then separately bound the
   $v$/$P$-vs-$p_2$ interaction) — an idea, not a lemma; §3's "swap the
   dominant element" naive version is ruled out, but a partial/two-step
   version was not tried.
4. **Target the general missing tool directly**, per round 7/9's repeated
   diagnosis: an *exact* (not floor/lower-bound) evaluation of $A$ on a
   reduced tail sub-instance under a budget restriction. Every route in this
   project (Case I of Claim A, $(\star\star)$, Prop 20-22, LP-duality's
   Theorem C′ coupling) ends up needing this same missing exactness. A
   dedicated approach whose *sole* target is this one general fact (rather
   than another attempt to route around it) has not yet been tried as its
   own top-level slug.

### Candidate technique(s)
- Strong induction on $n$ with the *full* theorem as IH (not a weaker
  corollary), guided by `tail-self-similarity`'s rescaling.
- `dominant-element-removal-identity` / `sharp-dominant-removal-identity`
  remain the only "exact peel" tools on file; both require a literal
  dominant element, which is exactly what the p2-cut case removes — any
  new tool must handle a *split* dominant piece, not a whole one.

### Cheap-kill candidates
- None found for closing the gap. One useful negative cheap-check: "peel
  $p_2$ against the whole remaining multiset" fails outright ($p_2<1/2$
  always) — rules out the most obvious naive fix in one line, saving a
  builder from re-deriving this.

### Knowledge-base entries to use
- No new generic `knowledge_base.md` entries beyond what's already cited
  (Induction/strong induction, Pigeonhole/extremal — both already the basis
  of every lemma on file). The problem's difficulty is now entirely in the
  problem-specific ladder machinery, not in retrieving a fresh KB technique.

### Analogous past problems (cruxes)
Not separately queried this round (out of scope for this lens per the
dispatch — the crux corpus has already been checked exhaustively by prior
rounds' explorers per `current.md`'s history; no new subtopic angle opened
here that would change that search). If needed, the relevant subtopic would
still be combinatorics / extremal-multiset-games, already covered.

### Prior progress
See `results/imo-2026-03/current.md` Round 9 entry and Propositions 20-22 in
`approaches/greedy-halving-adversary.md` — summarized accurately in §1-2
above; not re-litigated here.

### Dead ends (do not retry)
- "Peel $p_2$ as the new dominant element against the entire remaining
  multiset when $v<p_2$" — **ruled out this round**, $p_2<1/2$ always so
  Lemma 7's hypothesis fails against the full complement (it only holds
  against $\tau$'s own sub-tail, a fact already used one level up in
  Proposition 22, not new leverage for this case).
- (Reconfirmed from round 9, not re-derived) the outline's original
  "$\int_0^{p_2}v_{G'}\le p_2/2$" bound is false — already recorded, no new
  evidence found for or against reviving any variant of it.

### Small-case / intuition notes (conjectural)
- $\ell(F)\ge2$ configurations show no sign of violating Claim (B) up to
  $n=6$ across two different search methodologies (uniform-filtered random
  search and coordinate-descent global minimization) — conjecture: the
  difficulty is uniform in $\ell(F)$, not increasing with it.
- The global minimizers found by unconstrained search at $n=3,4,5$ all
  converge toward the known $c=n$ boundary family (many small fragments of
  $p_1$, one shrinking to $\approx0$), not toward a new "interior" tie-vertex
  family — mild evidence (not proof) that the already-characterized
  cascading/rescaled-ladder family remains the actual extremal locus even
  once $\ell(F)\ge2$ configurations are allowed into the search.
