## imo-2026-03 — lens: even-multiplicity sub-case of Theorem 37's non-maximal-tie gap

### Precise setup (re-derived from `approaches/greedy-halving-adversary.md` §"Round 26")

Within Case (b)'s "$v\ge a$" branch, "$T'$-untouched" sub-case: $T'=\{p_4\}\cup T''$
where $T''$ is a legal $\le(n-4)$-cut refinement of the tail $\{p_5,\dots,p_{n+1}\}$.
By `single-insert-point-vertex-lemma`, the minimizing $b\in(0,p_4]$ of
$A(B)=A(\{b\}\cup T')$ sits at a breakpoint: either $b=p_4$ (Theorem 37's own
vertex, closed) or $b=t^\ast$ for some value $t^\ast$ actually occurring in
$T''$ (a "non-maximal tie"). Write $\mu:=$ multiplicity of $t^\ast$ in $T''$
**before** the extra copy $b$ is added.

- **Odd $\mu$** (Theorem 40, CLOSED round 26): inserting $b=t^\ast$ makes the
  total multiplicity $\mu+1$ even, so by `odd-run-reduction-lemma` the whole
  pair-block cancels and $A(T''\cup\{t^\ast\})=A(T''\setminus\{t^\ast\})$ — an
  **exact deletion**. Then `sharp-dominant-removal-identity` peels $p_4$
  (using $p_4>\max(T'')$, an automatic ladder fact since $p_4=2p_5\ge2\max(T'')$),
  giving $A(B)=p_4-A(T''\setminus\{t^\ast\})$, and the *trivial* mass bound
  $A(S)\le\mathrm{Total}(S)$ applied to $S=T''\setminus\{t^\ast\}$ closes it
  unconditionally: $A(B)\ge f(n)+t^\ast>f(n)$. No induction hypothesis needed.

- **Even $\mu$ (the open residual, including $\mu=0$ meaning $t^\ast$ is a
  value not literally repeated — clarification below)**: inserting $b=t^\ast$
  makes total multiplicity $\mu+1$ **odd**. Since $\mu$ was even, $t^\ast$'s
  own $\mu$ copies *already fully cancel* in $T''$'s odd-run reduction
  $(T'')'$ — i.e. $t^\ast$ is **absent** from $(T'')'$ entirely. So inserting
  one copy of $t^\ast$ is not a "deletion" at all, it is **inserting a brand
  new distinct value** into the already-fully-reduced set $(T'')'$. This is
  qualitatively different: `sharp-dominant-removal-identity` still peels
  $p_4$ giving $A(B)=p_4-A(T''\cup\{t^\ast\})$, but now the only bound
  available for $A(T''\cup\{t^\ast\})$ is `triangle-bound-for-a`'s
  subadditivity $A(X\cup\{t^\ast\})\le A(X)+t^\ast$, giving
  $A(B)\ge p_4-A(T'')-t^\ast$. Closing this needs an **upper bound on
  $A(T'')$ itself** (not merely on $\mathrm{Total}(T'')$) — exactly the
  project's long-standing central obstruction (also re-derived independently
  via the Insert-Element Identity, round 22, applied to $B=\{b\}\cup T'$
  directly: $A(B)=2A(T'_{>b})-A(T')+(-1)^jb$, which structurally needs
  $A(T')$ bounded **above**, and every inductive fact on file is a lower
  bound). This is why the odd-case's mechanism (deletion + trivial mass
  bound) cannot be mechanically reused: deletion shrinks a set (trivial mass
  bound on the shrunk piece is enough), insertion grows it (mass bound on the
  *whole* piece is not enough, since $A\le\mathrm{Total}$ is far from tight
  for a set with internal cancellation).

$\mu=0$: strictly speaking $t^\ast\in T''$ is required for $t^\ast$ to be a
breakpoint by the vertex lemma's own derivation ($b$ ties to *some* fragment
value actually present), so $\mu\ge1$ always; "even $\mu$" in practice means
$\mu\in\{2,4,\dots\}$ — i.e. $t^\ast$ is a value that already occurs an even
number of times among $T''$'s own fragments (a genuine internal repeat, e.g.
from a symmetric split of some tail piece). The approach file's phrase
"including 0" is loose language for "the residual multiplicity in the
*reduced* set $(T'')'$ is 0," not a claim that $\mu$ itself can be 0.

### (a) Can Theorem 40's mechanism (or a dual/pair-deletion variant) be adapted?

**No clean adaptation found; here is why, precisely.**
- A "delete a pair instead of one element" variant does not apply because
  there is no pair to delete — the whole point of the even case is that
  $t^\ast$'s existing copies already all pairwise-cancelled *before* $b$ is
  added; the only new object is a singleton insertion.
- A "choose a different anchor" idea: Theorem 40 works because $p_4$
  strictly dominates every element of $T''$ ($p_4>\max(T'')$, from the
  ladder identity $p_4=2p_5$), so `sharp-dominant-removal-identity` gives an
  *exact* peel with no error term. This dominance already holds regardless
  of odd/even $\mu$ — the anchor choice is not the obstruction; the
  obstruction is purely in bounding the object being peeled away
  ($A(T''\cup\{t^\ast\})$ vs. $A(T''\setminus\{t^\ast\})$).
- The file explicitly checked (and ruled out) transferring Theorem 40's
  mechanism to the sibling's structurally similar-looking item 2/(7.9.4)
  object $A(\{c_2\}\cup T''')$: there the anchor $c_2$ is an *arbitrary*
  fragment of $p_1$'s own split with no forced-dominance guarantee
  ($c_2$ can be $<\max(T''')$), so even Theorem 40's easy (odd) case doesn't
  transfer there. This is a different, adjacent gap — not directly relevant
  to the even-tie case but shows the anchor-dominance trick is fragile and
  already fully mined within its own domain.
- A genuinely different idea worth flagging (not yet tried by any builder):
  instead of bounding $A(T''\cup\{t^\ast\})$ from *above* directly, try to
  show the even-multiplicity vertex is **never actually the global row-
  minimizer** — i.e. attack via the vertex-comparison route rather than a
  per-vertex bound. Since `single-insert-point-vertex-lemma`'s slope-±1
  argument already pins candidate minimizers to breakpoints, one could try
  to show directly (by a local exchange/perturbation argument, moving $T''$
  itself infinitesimally to break the even tie into an odd one without
  increasing $A(B)$) that the even-tie vertex is dominated by a nearby
  odd-tie vertex already covered by Theorem 40. This would be a genuinely
  different mechanism (comparing vertices, not bounding one) — not
  attempted here, flagged as a candidate opening for the outliner.

### (b) Crux corpus check

Filtered `combinatorics/coloring-and-parity` (71 cruxes), skimmed
`invariants-and-monovariants` and `extremal-principle` subtopics for
"insertion into an alternating/sorted structure changes value by a
parity-dependent amount" or "odd-vs-even multiplicity of a tied value in an
extremal greedy-claiming game." Found **no genuine analog**: the parity
cruxes in this corpus are almost all board/graph checkerboard-coloring
arguments (2-coloring a grid, alternating move-type invariants, orbit-size
parity via multinomial 2-adic valuation) — a different flavor of "parity"
than this problem's odd-run-reduction of a *sorted real-valued multiset*
under a greedy-alternating-claim functional. This matches (and reconfirms)
the project's standing rule 63 in `/tmp/memory/run_state.md`
("no strong direct analog for this problem... treat it as a from-scratch
construction") — no new crux lead found for this specific even/odd
multiplicity split.

### (c) Small-n numeric structure of even-tie witnesses

Ran two independent scripts (exact `Fraction`, not float):
1. Pure random legal-refinement sampling of $T''$ at $n=5,\dots,8$ (4000
   trials each): only ~7/1000 trials produce *any* even-multiplicity tie at
   all (a coincidental repeated fragment value from independent random
   splits is rare without engineering) — consistent with round 26's own
   finding (71 engineered trials, "rare... except when explicitly
   engineered"). Zero violations of $A(B)\ge f(n)$ found; minimum observed
   margin $1/42$ at $n=5$ (not tight).
2. Engineered worst case: split exactly one tail piece into $k$ equal
   fragments ($k$ even, $k-1\le n-4$ cuts, using the entire remaining
   budget), $t^\ast$ = that repeated fragment value, rest of the tail
   untouched. This is the most natural way to *force* an even-multiplicity
   tie deterministically. Results (min margin $A(B)-f(n)$ over all valid
   $(\text{piece},k)$ choices):
   - $n=5$: margin $1/42$ (best at splitting $p_5$ into $k=2$ equal halves)
   - $n=6$: margin $3/127$
   - $n=7$: margin $8/255$
   - $n=8$: margin $16/511$
   All strictly positive and apparently *not* shrinking to 0 as $n$ grows in
   this specific engineered family (unlike the general obstruction, which
   the project's other numerics show approaching 0 margin at deep-tie
   vertices elsewhere). This is weak evidence (2 families only, small $n$,
   not an exhaustive vertex search) that the even-tie residual may be
   *strictly* easier than the fully general obstruction, but it is only a
   numeric hint, not remotely a proof — a genuine adversarial search
   (multiple simultaneous split pieces sharing a value, or splits combined
   with tail-of-tail refinement) was not attempted here and could plausibly
   tighten the margin. Scripts: `/tmp/probe_even.py`, `/tmp/probe_even2.py`.

## Report

- Distinct openings:
  1. **Vertex-domination route** (new, not yet tried): show the even-tie
     vertex is never the true row-minimizer by a local exchange argument
     that perturbs $T''$ to convert an even tie into a nearby odd tie
     (already closed by Theorem 40) without decreasing $A(B)$ — attacks the
     *comparison between vertices* rather than bounding one vertex in
     isolation.
  2. **Direct upper bound on $A(T'')$** — the naive route (subadditivity +
     dominant peel), already shown by both this round's re-derivation and
     the pre-existing Insert-Element Identity (round 22) to require exactly
     the project's central unproved obstruction; not a new opening, but
     worth stating precisely as the wall to avoid re-hitting head-on.
  3. **Engineered-family bound** — since forced even ties in practice come
     from splitting one tail piece into $k$ equal fragments (the natural/
     only cheap way to manufacture a repeat under a tight cut budget), it
     may be tractable to prove the bound *just for this specific family*
     (an equal-$k$-split of one ladder piece) directly by closed-form
     computation (generalizing Theorem 39's hand-sweep technique), even
     without resolving the fully general upper bound on $A(T'')$ — this
     would not close the residual in full generality but would close the
     concrete, most-likely-adversarial witnesses on file.

- Candidate technique(s): local exchange/perturbation argument on vertex
  comparison (opening 1); closed-form hand evaluation of the specific
  "one piece split into $k$ equal fragments" family generalizing Theorem 39
  (opening 3). Both distinct from, and do not require solving, the fully
  general upper-bound-on-$A$ obstruction.

- Cheap-kill candidates: none obvious for closing the residual outright.
  One easy scoping check worth doing cheaply: verify whether $\mu\ge4$
  (three or more repeats) can even arise under the tight budget $n-4$ cuts
  for small $n$ — if not (budget too small to manufacture $\mu\ge4$), the
  open residual may combinatorially collapse to "$\mu=2$ only" for a wide
  range of $n$, a genuine simplification worth checking before attempting
  a general proof.

- Knowledge-base entries to use: none directly (knowledge_base.md has no
  entry specific to this project's odd-run-reduction/vertex-tie machinery;
  per standing project rule, treat as from-scratch). Reusable in-project
  lemmas: `odd-run-reduction-lemma`, `sharp-dominant-removal-identity`,
  `triangle-bound-for-a`, `single-insert-point-vertex-lemma`,
  `insert-element-identity` (round 22), all already certified.

- Analogous past problems (cruxes): none genuinely analogous found in
  `combinatorics/coloring-and-parity`, `invariants-and-monovariants`, or
  `extremal-principle` subtopics — this project's odd/even-multiplicity
  cancellation-under-alternating-sum structure has no close match in the
  corpus (checked and reconfirmed this round; matches the project's
  standing "no direct analog" finding).

- Prior progress: Theorem 37 (symmetric-split vertex, closed $n\le6$
  unconditional / conditional on $(\star_{n-4})$ beyond) + Theorem 40
  (odd-multiplicity non-maximal-tie vertex, closed unconditionally for all
  $n\ge5$, round 26) together close every vertex of the "$T'$-untouched"
  branch of Case (b)'s "$v\ge a$" target **except** the even-multiplicity
  residual. That residual is honestly and precisely diagnosed (not merely
  unattempted) as requiring a genuine upper bound on $A(T'')$ — the
  project's central, longest-standing obstruction — via two independent
  derivations (this round's re-derivation of Theorem 40's proof breakdown,
  and the pre-existing round-22 Insert-Element Identity applied directly to
  $B$).

- Dead ends (do not retry): reusing Theorem 40's deletion mechanism
  verbatim on the even case (fails structurally — there is no pair to
  delete, only a new value to insert, see above); transferring Theorem 40 to
  the sibling's $A(\{c_2\}\cup T''')$ object (already ruled out in-file,
  $c_2$ has no forced dominance over $T'''$); any mechanism that bounds
  $A(T'')$ only via the trivial mass bound $A(T'')\le\mathrm{Total}(T'')$
  (proven insufficient in this exact spot by direct computation, gives
  $A(B)\ge f(n)-t^\ast$, not $\ge f(n)$).

- Small-case / intuition notes (conjecture only, not proved): forced even
  ties are numerically rare under random sampling (needs deliberate
  engineering, matching round 26's 71-trial finding); in the natural
  "split one tail piece into $k$ equal fragments" engineered family, margin
  $A(B)-f(n)$ stays strictly positive and non-shrinking for $n=5,\dots,8$
  ($1/42,\,3/127,\,8/255,\,16/511$) — suggestive that this specific witness
  family is not the true adversarial worst case / may be easier than the
  fully general obstruction, but this is only a 2-parameter engineered
  search at small $n$, not an exhaustive vertex enumeration, and should not
  be treated as evidence the general residual is easy.
