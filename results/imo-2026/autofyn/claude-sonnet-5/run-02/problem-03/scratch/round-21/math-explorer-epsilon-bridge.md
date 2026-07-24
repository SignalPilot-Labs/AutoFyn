## imo-2026-03 — lens: the shared epsilon-bridge gap (round 20 finding)

### What epsilon(v) actually is
For any finite multiset $S$ and threshold $v$, `upper-truncation-identity`/
`truncated-alternating-sum-floor`/`-ceiling` all use
$\epsilon(v):=\mathbb1[|S_{>v}|\text{ odd}]$. **Key structural fact I verified
algebraically (not previously stated explicitly on file): as $v$ decreases
from $\infty$ to $0$, $|S_{>v}|$ increases by exactly 1 each time $v$ crosses
an element of $S$ (sorted descending $r_1\ge r_2\ge\dots\ge r_k$), so
$\epsilon(v)$ is literally the parity of $v$'s "rank band"**:
$\epsilon(v)=0$ for $v\ge r_1$ (band 0, empty truncation) or $v\in[r_2,r_1)$... 
more precisely $\epsilon(v)=1$ iff $v$ lies in an *odd*-indexed half-open
band $[r_{2j},r_{2j-1})$ for some $j\ge1$, and $\epsilon(v)=0$ on even-indexed
bands (including $v\ge r_1$ and $v<r_k$ when $k$ even). This is why
$\epsilon(v)=0$ is automatic whenever $v\ge\max(S)$ (Theorem 35b's own
domain, $v\ge p_3$: $R'_{>v}=\varnothing$, trivially even/empty) **and**
whenever $v$ is below every element of a reference set of *even* size
(rank-pigeonhole's own case $v_2<p_4$: $\tau_{>v_2}=\tau$, $|\tau|=2$ even).
Epsilon only actually flips to 1 in the *interior* bands — exactly the
"middle" sub-ranges both siblings' case-splits already isolate
($v\in[p_4,p_3)$ for §7.5; $v\in(s',p_3)$ or generally the band between
$R'$'s top element and its next distinct value for Theorem 35a) — this is
not a coincidence, it is forced by the band-parity structure. **This
"Band-Parity Fact" is a clean, general, promotable observation** (no ladder
structure needed) that should be written up as its own one-paragraph lemma;
it explains *why* $\epsilon=1$ concentrates exactly where both siblings'
existing case-splits already put a separate case, rather than being spread
arbitrarily.

### Concrete mechanism 1 (strongest, HIGH CONFIDENCE — algebraically derived
and numerically confirmed, 0 violations): Theorem 35a's $v\le s'$ sub-range
closes $(\Diamond')$ for FREE, no new mechanism, pure substitution.

Redo Theorem 35a's own derivation *without* dropping the $\epsilon'(v)$ term
from `truncated-alternating-sum-floor` (the sibling's proof already carries
it exactly, it just never re-substitutes it into the *outer* $\epsilon(v)$
target). Since $R'_{>v}=\{p_3\}\cup T'_{>v}$ in this branch ($v<p_3$), and
$|R'_{>v}|=1+|T'_{>v}|$, we get the exact parity relation
$$\epsilon(v) = 1-\epsilon'(v)\qquad(\text{outer parity is complementary to
the inner }T'\text{-parity}).$$
Substituting the floor lemma's exact inequality
$\Xi:=A(T')-2A(T'_{>v})\ge v-s'-2v\epsilon'(v)$ into
$\Delta(n,v)=-p_3-\Xi$ and comparing against the target
$\Delta(n,v)\le v-f(n)-2v\epsilon(v) = -v-f(n)+2v\epsilon'(v)$
(substituting $\epsilon(v)=1-\epsilon'(v)$), the two sides match **term for
term** iff $f(n)-p_3=-s'$, i.e. $f(n)=p_3-s'$. This holds with **exact
equality** from already-certified facts: $p_2=2p_3$ (ladder doubling) and
$f(n)+s=p_2$ (Lemma 24, `level-2-dominance-identity`), giving
$p_3-s'=p_3-(s-p_3)=2p_3-s=p_2-s=f(n)$. So the floor lemma's own
$\epsilon'(v)$-carrying inequality — already proved, already cited — **is
literally the $(\Diamond')$ target itself**, valid for either value of
$\epsilon'(v)\in\{0,1\}$, once you don't throw the correction term away.
I verified this numerically end-to-end (exact `Fraction`, 300 trials/level
$n=3..7$, random legal $T'$ under the $n-3$ cut cap, random $v\in[0,s']$):
zero violations, matching the algebra exactly (script used: computed
$\Delta(n,v)$ directly from $R'=\{p_3\}\cup T'$ and compared against the
full $(\Diamond')$ target with the real $\epsilon(v)$, not the weaker
$(\Diamond)$).

### Concrete mechanism 2 (also free, reuses Theorem 35b verbatim): the
boundary sub-range $s'<v<p_3$ of Theorem 35a.

Here $T'_{>v}=\varnothing$ (all of $T'\le p_4\le s'<v$), so $\epsilon'(v)=0$
trivially, hence $\epsilon(v)=1$ (odd band, one level up). The needed target
reduces to $A(T')\ge v-s'$, and since $v<p_3$ strictly, $v-s'<p_3-s'=f(n)$
strictly. **Theorem 35b's own already-proved bound** (via the standing IH
$(\star_{n-3})$), $A(T')\ge f(n)\cdot2^{n-3}\ge f(n)$, is strictly stronger
than what's needed here ($f(n)>v-s'$) — so this sub-range's $\epsilon=1$
correction is closed by literally citing Theorem 35b's inequality, no new
derivation. Verified numerically (300 trials/level $n=4..7$ — degenerate at
$n=3$ since $s'=p_4$ there is the whole tail): zero violations.

**Combined effect of mechanisms 1+2+the automatic $\epsilon=0$ at $v\ge p_3$:
the ENTIRE Case (a) ("$p_3$ untouched") branch of the epsilon-bridge for
Theorem 35 closes with no new machinery** — just a careful rewrite that
keeps the $\epsilon'(v)$/$\epsilon(v)$ terms through the existing proof
instead of dropping them, plus one already-certified identity substitution
($f(n)=p_3-s'$). This should be a fast, mechanical write-up task, not a
research problem.

### Concrete mechanism 3 (HIGH CONFIDENCE, verified numerically): §7.5's
$n=3$ middle band ($v_2\in[p_4,p_3)$, the only $\epsilon=1$ sub-case there)
closes by tightening the existing slack, no new mechanism.

In §7.5's 3-case split: case $v_2\ge p_3$ gives $\tau_{>v_2}=\varnothing$
($\epsilon=0$ automatic); case $v_2<p_4$ gives $\tau_{>v_2}=\tau$, size 2
(**even** — $\epsilon=0$ automatic, since $|\tau|=2$ always for $n=3$); only
the middle case $v_2\in[p_4,p_3)$ has $|\tau_{>v_2}|=1$, odd, $\epsilon=1$.
There, the file's own proof uses the loose bound $s-(v_1-v_2)>s-p_2=-f(3)$
(via $v_1<p_2$, $v_2>0$) to beat $\Delta(3,v_2)=-3p_4$ with slack $2p_4$.
The full $(\Diamond')$-analog target subtracts an extra $2v_2$, i.e. needs
$v_1+v_2\le s+3p_4=6p_4$. Since in this sub-case $v_2<p_3=2p_4$ (case
hypothesis, not just $v_2>0$) and $v_1<p_2=4p_4$ (domain), $v_1+v_2<4p_4+
2p_4=6p_4$ — closes strictly, using the *case-specific* upper bound on
$v_2$ that the original proof had but didn't need for the weaker $(\sharp)$
target. Verified: 20,000 random-trial exact-`Fraction` check of the full
epsilon-corrected target across the whole $(v_1,v_2)$ middle-band domain,
zero violations, min margin found $\approx1.8\times10^{-6}$ (tight but
positive, consistent with a genuine closed proof, not a numeric fluke).

### Why this generalizes (candidate for a uniform closing argument, not just
n=3/4): the identity $f(n)=p_i-(\text{total of everything strictly below
piece }i)$ used in mechanisms 1/2 is exactly `level-2-dominance-identity`
(Lemma 24) applied one level deeper in the ladder — and by
`tail-self-similarity`, this SAME identity recurses at every level of the
ladder (each sub-ladder is a rescaled copy of the whole). This strongly
suggests the "epsilon cancels via the dominant-piece-minus-rest = f(n)
identity" trick is not special to $n=3,4$ but should reproduce at every
induction depth — i.e. a genuinely general (not just base-case) closing
mechanism for the whole epsilon bridge, worth trying as an inductive
step rather than only patching the already-reached levels.

### What is NOT yet covered (still open, honestly)
- Theorem 35's Case (b) ("$p_3$ is cut") — even the $\epsilon=0$ target
  $(\Diamond)$ is only closed at $n=3$ (vacuous) and $n=4$ (Theorem 36); the
  epsilon-bridge fix has not been attempted there at all. The same technique
  (track $\epsilon$ exactly through Theorem 36's 10 sub-range case split,
  using the band-parity fact to locate exactly which sub-ranges have
  $\epsilon=1$) is a plausible next target but I did not verify it — Theorem
  36's structure (two free parameters $a,b$ splitting $p_3$) is more
  complex than the single-variable cases checked here, so this is a
  candidate, not a confirmed mechanism.
- General $n\ge4$ for §7.5-style middle band (rank-pigeonhole's own §7.6
  gap, cross-piece tie-vertex enumeration) is untouched by this lens — the
  epsilon-bridge fix only closes the *bridge*, not the pre-existing
  general-$n$ vertex-enumeration obstruction that both siblings still face
  beyond the levels already reached.

### Candidate technique(s)
Direct algebraic substitution/careful bookkeeping (no new theorem needed for
mechanisms 1–3): keep the $\epsilon'(v)$/$\epsilon(v)$ correction terms
through the existing certified lemmas (`upper-truncation-identity`,
`truncated-alternating-sum-floor`, `truncated-alternating-sum-ceiling`)
instead of dropping them, then use already-certified identities
(`level-2-dominance-identity`/Lemma 24, ladder doubling $p_i=2p_{i+1}$,
`tail-self-similarity`) to show the correction term is exactly absorbed.
The new "Band-Parity Fact" (epsilon(v) = parity of v's rank-band among
S's sorted elements) is worth stating as a standalone one-paragraph lemma
since it explains, structurally, why epsilon=1 only ever shows up in
exactly the interior sub-cases both siblings' existing case-splits already
isolate.

### Cheap-kill candidates
None needed here — the gap turned out to be a bookkeeping omission, not a
genuine additional obstruction, at every level checked (n=3,4 for both
fronts' Case (a)/middle-band pieces). No pruning needed before the algebra;
the "cheap kill" in effect already happened (zero-violation numeric checks
above ran in well under a minute each).

### Knowledge-base entries to use
No knowledge_base.md entry directly matches "parity/tie correction for a
truncated alternating sum" — this is bespoke machinery built entirely
within this problem's own approach files (`upper-truncation-identity` et
al.), consistent with round 1's finding that no knowledge_base/crux entry
is a strong analog for this problem. General entries relevant only in the
generic sense: "Casework / exhaustion" (parity/residue split) and "Check the
answer... parity consistency" (knowledge_base.md lines ~186, ~245) — not
load-bearing beyond the obvious.

### Analogous past problems (cruxes)
None found — did not locate a crux entry whose crux move is "track an
odd/even truncation-count correction term through an exact identity and
show it cancels via a level-invariant algebraic identity." This is
consistent with round 1's explorer conclusion (no strong crux analog for
this problem's combinatorics); I did not re-run a fresh corpus query this
round since the technique is a direct algebraic derivation from already-
proved in-house lemmas, not something requiring external pattern-matching.

### Prior progress
- `greedy-halving-adversary`: Theorem 35a (unconditional $(\Diamond)$,
  $v<p_3$), Theorem 35b (conditional on $(\star_{n-3})$, $v\ge p_3$),
  Theorem 36 ($n=4$ Case-(b) closure, $(\Diamond)$ only). All scoped
  honestly to $\epsilon=0$ target $(\Diamond)$, not $(\Diamond')$.
- `rank-pigeonhole-budget`: §7.1 Truncated Alternating Sum Ceiling
  (certified, general, epsilon-free/dropped), §7.5 unconditional $n=3$
  middle-band closure of $(\sharp)$ (the $\epsilon=0$ target), §7.6 honest
  open gap for general $n\ge4$ (re-encounters cross-piece tie-vertex
  enumeration).
- This round: found (algebraically derived + numerically confirmed, 0
  violations across all checks) that Theorem 35a's *entire* domain and
  §7.5's $n=3$ middle band's *entire* domain already close the TRUE
  epsilon-corrected target $(\Diamond')$/full-$(\sharp)$, using only
  already-certified lemmas/identities plus careful bookkeeping — this is
  new, not previously written up in either approach file.

### Dead ends (do not retry)
None discovered this round — this lens did not run into a dead end; the
gap resolved via direct algebra faster than expected. (Do not confuse this
with the *separate*, still-fully-open case (b2) upper-bound front — that is
untouched by this lens and remains at 7 confirmed-dead mechanisms per prior
rounds; nothing here bears on it.)

### Small-case / intuition notes
- Conjecture (numerically supported, not yet proved in general): the
  epsilon-bridge gap is *always* closable "for free" wherever the
  $\epsilon=0$ target has already been established via this floor/ceiling
  lemma machinery, because of the recursive level-invariant identity
  $f(n)=p_i-(\text{rest below }p_i)$ that holds at every ladder depth
  (`tail-self-similarity` + `level-2-dominance-identity` generalized). If
  true, this would mean the "epsilon-bridge gap" is not a genuine
  mathematical obstruction at all, just an artifact of the write-up
  dropping a term that was already available — worth having the outliner
  frame it as "close by rewriting, not by new invention" for round 21's
  build, with the general inductive version (mechanism-3-generalizes note
  above) as a stretch goal beyond just patching $n=3,4$.
- Verified via exact-`Fraction` Python (not floats) in all checks above;
  scripts are throwaway (not saved to the repo), re-derivable from the
  formulas quoted in this report if needed.
