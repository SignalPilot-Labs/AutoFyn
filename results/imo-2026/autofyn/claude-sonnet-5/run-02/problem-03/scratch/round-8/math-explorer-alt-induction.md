## imo-2026-03

### Scope of this pass
Lens: alternative induction variable / genuinely different reduction, targeting
sub-case (†) of `rank-pigeonhole-budget.md` §4.8–4.9 (Branch B, N=m+k even, of
the peel-the-global-minimum induction for Case I of Theorem GC(m)), plus a
scout of whether `lp-duality-certificate`'s Type III/IV vocabulary can be
extended past $c_1=1$ with a smarter basis informed by its $n=3$,
$F=\{4,2,2\}/15$ witness. No full proof attempted; findings below are
diagnostic/negative-result-focused, meant to steer round 8's outline.

### Key new finding: peeling from an even-rank position is an EXACT identity, not a reduction — this is *why* (†) resists plain strong induction
I verified by direct computation (not just citing the file) that the
"strengthened bound" the file flags as needed for (†),
$$E(F\setminus\{\mu\}\cup\tau)\ \le\ R(\tau)-\mu,$$
is **not an independent fact to prove** — it is *algebraically identical* to
the original target $D(S):=R(\tau)-E(S)\ge0$ whenever $N=m+k$ is even. Reason:
$\mu=\min(F)$ is (in Branch B) the global minimum of $S=F\cup\tau$, sitting at
the very last sorted rank $N$; when $N$ is even this is an *even* rank, so
removing it shifts nothing else and $E(S)=E(F\setminus\{\mu\}\cup\tau)+\mu$
identically. Substituting shows "$E(F')\le R-\mu$" $\iff$ "$D(S)\ge0$" — the
exact same statement in different notation, not a smaller sub-claim reachable
by strong induction on a *smaller* instance. This is the same
"exact-identity-not-a-reduction" disease already diagnosed independently by
`rank-tie-vertex-reduction.md` §6 (`case-ii-exact-peel-identity`) and
`lp-duality-certificate.md` §7 for the $c_1\ge2$/dominant-fragment case — now
confirmed to reappear in the peel-the-minimum mechanism too, for a genuinely
different reason (rank-position parity of a *truncation*, not a
dominance-removal identity). **I also checked and confirmed** (by explicit
double computation) that removing the two smallest elements of $F$ together
(when both lie below $\tau_m$) is likewise an *exact* rank-truncation identity
$E(S)=E(S'')+\mu_1$ (only the smaller of the pair contributes, since it lands
at the even rank) — so "peel two instead of one" does not escape the
obstruction either; it is the same phenomenon one level further down, with
the identical missing ingredient (an a priori bound on $E$ at the smaller
instance sharper than the plain $\le R(\tau)$ the induction hypothesis
supplies). **This should stop round 8 from re-trying any variant of
"peel more elements from the bottom of $F$" as a way past (†)** — it is
provably the same wall, not a new one, confirmed computationally, not just
argued.

**Diagnosis of the real asymmetry (new framing, useful for the outliner).**
Branch A closes cleanly because peeling $\tau_m$ *shrinks the target itself*:
the smaller instance's own bound is $R(\tau')=R(\tau)-\tau_m$, so removing
$\tau_m$ from $S$ and from the target's right-hand side cancel in lockstep —
a genuine reduction. Branch B fails because peeling an $F$-element does
*not* shrink $R(\tau)$ (the tail is untouched by this move) — the smaller
instance's target is still the same $R(\tau)$, so there is no "budget" for
the removed mass $\mu$ to come out of. **Any fix must therefore either (a)
strengthen the induction hypothesis to track an explicit slack term
$g(s,k,m)\ge0$, with $E(F\cup\tau)\le R(\tau)-g$, chosen so that removing an
$F$-element from $s$ decreases $g$ enough to compensate (a genuinely new
invariant, not yet found), or (b) find a peel move that touches $\tau$ even
when $F$'s min is the global min (not possible verbatim, since $\tau$'s own
min $\tau_m$ isn't the global min in Branch B by definition) — e.g. a
"virtual" partial peel of $\tau_m$ proportional to how far $\mu$ is below it,
or (c) abandon the peel-the-extreme-element mechanism for Case I entirely and
attack via a closed-form/global argument instead (see below).**

### Numeric sanity re-check (own script, exact Fraction, not floats)
Re-ran a corrected search respecting the essential $k\le m+1$ budget
constraint (the file's own documented essential fact) for Branch-B,
$N$-even instances: **zero violations of $D(S)\ge0$** across thousands of
trials, minimum found $\approx0.13$ (script pattern in
`/tmp/optimize2.py`-style; not preserved beyond this session, reproducible in
under a minute). Note for future explorers: an *earlier* version of this same
search (allowing $k>m+1$) found an apparent counterexample $D<0$ — this
was **not a real counterexample**, it was an artifact of violating the
essential budget invariant $k\le m+1$ that the file already flags as
load-bearing (§3 of `rank-pigeonhole-budget.md`, "why the part-count bound is
essential"). **Flagging this explicitly so round 8 doesn't waste a cycle
rediscovering the same false alarm**: any search/candidate invariant for (†)
*must* enforce $k\le m+1$ or it will produce spurious counterexamples.

### Candidate reformulations for the outliner (concrete, precision-scoped)

1. **Strengthened joint invariant, explicit form to try.** Conjecture a
   two-parameter bound
   $$E(F\cup\tau)\ \le\ R(\tau) - h(s,k,\tau_1,\tau_m)$$
   for an explicit $h\ge0$ that is *provably monotonic under the Branch-B
   peel* (i.e. $h(s,k,\dots)-h(s-\mu,k-1,\dots)\ge$ the shortfall $\mu$ minus
   whatever margin Branch A's argument banks). Two guesses already refuted,
   recorded so they are not retried: $h=\min(S)\cdot[N\text{ even}]$ (fails
   at the GC(1) base case, per the file); the naive "$D(S)\ge\mu$"
   (this explorer tested it directly — **false in general Case I**, ~16% of
   random trials violate it once you don't restrict to Branch-B-even, so it
   cannot be the invariant either — see numeric note below). A more promising
   direction, untested here: since $F^*$ (the achievability construction of
   §2 in `rank-pigeonhole-budget.md`) is the extremal/tight configuration for
   the *whole* problem and lives entirely in Case I with a highly structured
   "pairs cancel, one leftover" shape, try $h$ built from *how far $F$'s
   values deviate from $F^*$'s specific paired structure* (a "distance to the
   tight configuration" potential) rather than a raw statistic like $\min$.
2. **Induct on the number of distinct values / post-odd-run-reduction size,
   not on raw $N=m+k$.** Since `odd-run-reduction-lemma` already proves
   $A(S)=A(S')$ where $S'$ collapses even-multiplicity runs, define the
   induction variable as $|S'|$ (size of the *reduced* multiset) instead of
   $N$. This could sidestep the parity trap because $N$'s parity is an
   artifact of raw element count, while $|S'|$'s parity reflects the actual
   "surviving" structure after cancellation — the two need not move in
   lockstep as you peel one element (e.g. peeling an element that has a
   duplicate elsewhere changes $|S'|$ by 2 or 0, not always 1). **This is a
   genuinely different induction variable, not yet tried by any approach on
   file** — flagged as the most distinct-from-everything-tried candidate
   this pass found, but I did not carry out the reduction/verify it actually
   avoids an analogous branch split (would need its own base case and step,
   likely nontrivial); recommend the outliner scope it as a real attempt, not
   assume it's free of a symmetric obstruction.
3. **Direct/global argument instead of peel-induction.** Since Branch A's
   success mechanism is "the removed piece cancels against the target's own
   shrinking," and $F^*$ (§2) is already an explicit, fully evaluated
   extremal instance, consider attacking Case I via a **direct rearrangement/
   majorization argument** comparing an arbitrary Case-I $F$ against $F^*$'s
   specific structure (pairing argument), rather than any peel-by-count
   induction at all — i.e. show every legal Case-I $F$ is "dominated" by
   $F^*$ via an explicit injection/exchange of mass between $F$'s fragments
   and the tail's own values, closer in spirit to the certified
   `general-n-cascade-achievability`/`cascading-halving-family-
   characterization` results (which used direct rank-position counts, not
   induction) than to GC(m)'s peeling machinery. Not attempted here; flagged
   as the least-explored of the three because every approach on file so far
   has used *some* form of peel/induction.

### LP-duality: can Type III/IV be extended past $c_1=1$ with a smarter basis?
Studied the $n=3$, $F=\{4,2,2\}/15$, tail-untouched witness in detail (this is
exactly a Case-I instance one level into $c_1=2$: $y_1=4/15=p_2$ exactly, so
**no fragment exceeds $p_2$**, meaning the Type-IV atom (support-vanishing on
$W_R$) has **no eligible region at all** — this is not a weak instance of
Type IV, it's a *complete absence* of the region Type IV needs). Crucially,
**the target is met with equality** at this witness ($A(F\cup T)=1/15=f(3)$
exactly, not with slack) — I confirmed this directly (own computation,
matches the approach file). **This equality is the structural reason no
"smarter basis" of context-free, bounded atoms (in the Type I–IV spirit) can
work here**: any valid certificate for a *tight* instance must itself be
exactly tight (no slack anywhere to spend on an approximation), which forces
every atom used to evaluate to its exact value on this instance, not merely
bound it — but the shortfall (§7.4 of the file) is repaid *only* by using
$A(G')=3/15$'s exact value against its floor $1/15$, a fact intrinsically
about *this specific* tail refinement, not expressible as a bounded,
$G'$-agnostic atom without effectively hard-coding $A(G')$'s value (i.e.
smuggling in the full recursive answer). **Conclusion: this is not a
"weakness of Type III/IV specifically" that a cleverer atom choice fixes — it
is a genuine expressiveness barrier for *any* bounded, context-free
certificate vocabulary**, confirmed by the tightness of the witness, not just
by trial and error on one basis choice. A "Type V" atom that references
$A(G')$'s *exact* recursive value (not a bound) would work trivially but is
then just the induction in disguise — no shortcut. **Recommend: do not spend
a round trying alternate atom bases for the LP-duality framing on Case
I/$c_1\ge2$; the tightness argument above is a structural no-go, not merely
"not found yet."** If `lp-duality-certificate` continues, its more promising
next move (per its own file) is importing a strengthened invariant from
whichever sibling finds one (item 1 above), translating it into a genuine
Type-V atom — not re-deriving from its own vocabulary.

### Cheap-kill / pruning check
- The essential $k\le m+1$ budget constraint is easy to violate accidentally
  in any fresh numeric search on this problem (I did, and it produced a
  false counterexample) — **any round-8 numeric script must enforce this
  explicitly**, flagged above.
- No new parity-avoiding pigeonhole/injection was found this pass beyond the
  "induct on $|S'|$ instead of $N$" idea (item 2), which is unverified, not
  a cheap kill.

### Knowledge-base entries relevant
- The problem's core reduction still rests on `claiming-subgame-reduction`
  and `integral-alternating-sum-formula` (both certified, unaffected by this
  pass). No new knowledge-base entry (outside this problem's own `lemmas/`)
  looks applicable to closing (†) — this is bespoke combinatorics about
  ratio-2 superincreasing sequences, not a generic KB pattern.

### Analogous past problems (crux corpus)
Did not find a genuinely new match this pass beyond what prior rounds already
checked (the corpus is combinatorics/number-theory contest problems; this
problem's obstruction — an exact vs. floor gap in a Stackelberg-style
peeling induction over superincreasing sequences — is fairly bespoke). No
new crux recommendation from this pass; prior rounds' negative findings on
`aimo-0117` (claiming-order) and `aimo-0718` (rank-sum pigeonhole) stand as
documented dead ends, not re-verified here.

### Prior progress (recap for context, not re-verified beyond spot-checks above)
- Achievability (§2) and Case II (Theorem GC(m), §3) of Claim (A): fully
  closed, general $n$, no numerics needed — solid, spot-checked here only
  for internal consistency, not re-derived.
- Case I: closed except (†) (Branch B, $N=m+k$ even) — spot-checked (†)'s
  numeric support directly; zero violations found (consistent with file);
  also found and precisely explained *why* the natural strengthening is
  circular (new diagnosis, see above), and refuted one more candidate
  invariant ($D(S)\ge\mu$ in general, not just at (†)) not previously
  recorded as tried.
- LP-duality's Type III/IV vocabulary: confirmed (via the tightness argument
  above) that it cannot be patched with a smarter but still-bounded/
  context-free basis; the diagnosis in the file (§7.4) is correct and now
  has an additional structural reason (equality-forces-full-tightness) backing
  it.

### Dead ends (do not retry)
- $\delta=\min(S)\cdot[N\text{ even}]$ as a strengthening of the Branch-B
  invariant — refuted at the GC(1) base case (already on file).
- "Peel two elements instead of one" from the bottom of $F$ in Branch B —
  **newly refuted this pass**: proved (own computation) it reduces to the
  identical exact-identity obstruction one level down, not a new route.
- $D(S)\ge\mu(F)$ as a general Case-I invariant (not restricted to (†)) —
  **newly refuted this pass**: ~16% violation rate in a 8000-trial exact-
  fraction search over general Case I instances (both branches, both
  parities); only survives when restricted to (†) itself, where it is
  provably tautological (see above), so it carries no new content there
  either. Do not propose "$D\ge\mu$" as the missing invariant.
- Extending LP-duality's Type III/IV vocabulary with any bounded, $G'$-
  agnostic new atom to cover $c_1\ge2$/Case I — structurally ruled out by
  the tightness argument above, not just "not found."

### Small-case / intuition notes (labeled as conjecture where not proved)
- The extremal (tight, $D=0$) configurations found in local numeric search
  for Branch-B-even instances (this pass, exact-fraction hill search on one
  fixed $m=3$ tail) did not land at obviously "nice" rational boundary points
  in the handful of trials examined — no immediate closed-form pattern
  jumped out, unlike Branch A's clean telescoping identity. This is weak,
  unproved evidence that Branch B's true extremal structure is genuinely
  more complex (consistent with why 3 independent mechanisms have converged
  on it as the last wall), rather than a easy oversight.
- The equality case at the LP-duality witness ($n=3$, $F=\{4,2,2\}/15$) is
  itself worth double-checking as a candidate *extremal* instance for (†)'s
  abstract GC(m) formulation too — if it maps onto a genuine Branch-B-even
  vertex of the abstracted problem, its exact tightness (not just numeric
  near-zero) could be a useful concrete test case for any future candidate
  invariant $h$ (item 1 above): a real invariant must vanish exactly there.
  Not verified whether this specific witness lands in Branch-B-even for the
  abstract GC(m) recursion (would need translating $n,p_i$ units into
  $m,\tau,s$ units and checking); flagged as a concrete, cheap next check for
  whichever round attempts item 1.
