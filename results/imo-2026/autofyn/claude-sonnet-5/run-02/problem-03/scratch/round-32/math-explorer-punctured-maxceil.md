## imo-2026-03 — lens: punctured MaxCeil mechanism for h(m)'s vertex "c=t∈S'', q2 untouched, t≠q2"

### The precise object
`greedy-halving-adversary` round 31 (approaches/greedy-halving-adversary.md,
lines ~7239–7309) reduces the vertex $c=t\in S''$, Case (ii) ($q_2$ untouched
in $S''$, $t\ne q_2$ some other fragment) to:
$$F_t(q_1/2)=A(\{q_2\}\cup(S''\setminus\{t,q_2\}))\ \ge\ f(m),$$
and, via `sharp-dominant-removal-identity` ($q_2$ strictly dominates the
rest), this is equivalent to the "punctured MaxCeil" bound
$$A(S''\setminus\{t,q_2\})\ \le\ q_2-f(m). \qquad(\dagger)$$
Here $S''\setminus\{q_2\}$ is a legal $\le(m-2)$-cut refinement of the tail
$\{q_3,\dots,q_{m+1}\}$ (length $m-1$; since $q_2$ was untouched, its whole
budget carries over), and $t$ is one further arbitrary element removed from
it ("punctured" = one fragment deleted, not a whole rung).

### Distinct openings
1. **(Recommended, verified below) $(\dagger)$ is NOT the same difficulty as
   raw $\mathrm{MaxCeil}(m-1)$ — it has a factor-~2 slack that lets the
   *already-certified* elementary `Fact 2` ($A(S)\le\mathrm{Total}(S)$,
   §5.2 of `rank-pigeonhole-budget.md`) close it outright, with no
   induction, no vertex enumeration, and — crucially — no dependence on
   $\mathrm{MaxCeil}(m\ge5)$ or the Necessity Theorem.**
   - Total mass is invariant under cutting: $\mathrm{Total}(S''\setminus
     \{q_2\})=\mathrm{Total}(\{q_3,\dots,q_{m+1}\})$ exactly, for *any*
     legal refinement, regardless of cut count.
   - The ratio-2 ladder telescoping identity gives, exactly,
     $\mathrm{Total}(\{q_3,\dots,q_{m+1}\})=2q_3-q_{m+1}=q_2-f(m)$ (since
     $q_2=2q_3$) — this is the same "top-minus-floor = mass" identity
     already used one index up in Theorem 42's proof ($q_1-\mathrm{Total}
     (S'')=f(m)$); it is a one-line re-derivation at the shifted index, not
     a new lemma.
   - Removing $t>0$ strictly decreases the mass:
     $\mathrm{Total}(S''\setminus\{t,q_2\})=(q_2-f(m))-t<q_2-f(m)$.
   - By Fact 2, $A(S''\setminus\{t,q_2\})\le\mathrm{Total}(S''\setminus
     \{t,q_2\})<q_2-f(m)$ — proving $(\dagger)$ with strict slack $t$, for
     **every** $m\ge3$, unconditionally, no case split on $t$'s location
     (whole rung or split fragment), no restriction on cut count.
   - I verified this numerically (exact `Fraction` arithmetic) for
     $m=3,\dots,9$: the telescoping mass identity holds exactly in every
     case, and thousands of random legal refinements + random $t$ each
     round give $A(S''\setminus\{t,q_2\})$ far below the bound $q_2-f(m)$
     (typically around half the bound) — fully consistent with (and much
     looser than) the proof above.
2. **Why this doesn't contradict round 31's diagnosis of a shared
   dependency**: the "split-rung fragment removed" sub-case of Case (i)
   (the other still-open piece, where $t$ is a fragment of a *split* $q_2$,
   $q_2$ itself gone) reduces, per the file, to the tail's own top element
   $q_3$ dominating the rest, targeting the *tight* bound $q_3-f(m)$ — this
   is genuinely $\mathrm{MaxCeil}(m-1)$ itself (no factor-2 slack, since the
   dominant peel there is only $q_3$, not $q_2=2q_3$), so Fact 2 alone
   gives only $\mathrm{Total}(\text{rest})\le q_3-f(m)$-ish bounds that are
   NOT automatically true (this is exactly why that sub-case is open and
   correctly tied to $\mathrm{MaxCeil}(m-1)$, hence to
   $\mathrm{MaxCeil}(m\ge5)$ for $m-1\ge5$). So the "shared dependency"
   diagnosis is correct for the *other* residual piece, but the specific
   vertex assigned to this lens (Case (ii), the one with $q_2$ removed
   whole) is a strictly easier target that does not need that dependency
   at all — the two "punctured" targets are not the same difficulty despite
   superficially similar phrasing ("remove one point from a refined tail").
3. **A second, even more elementary alternative for $(\dagger)$**: bound
   via $A(S)\le\max(S)$ (itself an immediate corollary of Fact 2 applied
   pairwise, or directly since $A=v_1-v_2+v_3-\dots\le v_1$ by grouping
   consecutive pairs) — $\max(S''\setminus\{t,q_2\})\le q_3\le q_2-f(m)$
   since $q_3\ge f(m)$ trivially (top of a decreasing tail $\ge$ its own
   bottom). This gives the same conclusion via a slightly different
   elementary fact, a useful redundancy/cross-check if Fact 2's own
   citation is ever disputed.

### Candidate technique(s)
- `Fact 2` ($A\le\mathrm{Total}$, already certified informally in
  `rank-pigeonhole-budget.md` §5.2 — check whether it has a standalone
  lemma file; I did not find one named exactly `fact-2` under `lemmas/`,
  only implicit use — **recommend the builder extract/certify it as a
  standalone lemma** since it is about to be reused across files) plus
  total-mass conservation under refinement (trivial, but state explicitly)
  plus the ladder telescoping identity (one-line, same pattern as the
  existing `q1-Total(S'')=f(m)` used in Theorem 42).
- No need for: `sigma2-untouched-closure-theorem`, the Necessity Theorem,
  or any instance of $\mathrm{MaxCeil}(m\ge5)$.

### Cheap-kill candidates
- The mass/Fact-2 argument above **is** the cheap kill — it fully resolves
  this sub-case in one paragraph. Recommend the outliner route this vertex
  through it directly rather than treating it as entangled with
  $\mathrm{MaxCeil}(m\ge5)$.

### Knowledge-base entries to use
- None of `knowledge_base.md`'s generic entries are needed beyond what's
  already cited (`sharp-dominant-removal-identity`); this is closed by
  problem-internal elementary facts already on file.

### Analogous past problems (cruxes)
- Searched `combinatorics` subtopics `extremal-principle` /
  `games-and-strategy` for mass-conservation / peel-style moves; nothing
  genuinely analogous to this specific ladder/alternating-sum mass-bound
  mechanism turned up (matches were superficial — general "bound a sum by
  its total" ideas, not the same structure). No forced match; recommend
  none be cited.

### Prior progress
- Round 31 (`greedy-halving-adversary`): Case (ii) "reduces to an
  unaddressed punctured MaxCeil object" — **this is the gap this report
  closes with an elementary argument** (not yet written up as a proof in
  any approach file — this is new, unverified-by-reviewer reconnaissance,
  to be built out and reviewer-checked next round).
- Case (i)'s "$t=q_2$ untouched" sub-case: already fully closed (round 31,
  rescaling to $(\star_{m-2})$).
- Case (i)'s "split-rung fragment removed" sub-case: genuinely reduces to
  $\mathrm{MaxCeil}(m-1)$ (tight, no slack) — remains open for $m-1\ge5$,
  i.e. $m\ge6$; distinct from and not resolved by this report's mechanism.

### Dead ends (do not retry)
- Do not attempt to prove $(\dagger)$ via $\mathrm{MaxCeil}(m-1)$ itself
  (i.e. re-deriving the tight bound $q_3-f(m)$ first, then loosening) — the
  Fact-2/mass argument bypasses that entirely and is strictly simpler;
  going through $\mathrm{MaxCeil}(m-1)$ would be reinventing a much harder
  wheel for a target that doesn't need it.
- Do not conflate Case (ii)'s closure (this report) with Case (i)'s
  "split-rung" sub-case — they look similar ("remove one point from a
  refined tail") but have different slack and different fates; the latter
  genuinely needs $\mathrm{MaxCeil}(m-1)$.

### Small-case / intuition notes (conjecture unless stated proved above)
- Verified by exact-`Fraction` computation, $m=3,\dots,9$: the ladder mass
  identity $\mathrm{Total}(\{q_3,\dots,q_{m+1}\})=q_2-f(m)$ holds exactly
  in every case (not a conjecture — a direct algebraic telescoping fact,
  confirmed computationally as a sanity check, not as the proof itself).
- Verified numerically that $A(S''\setminus\{t,q_2\})$ stays well under
  $q_2-f(m)$ across thousands of random legal refinements and random $t$
  for each $m=3,\dots,9$ (max observed roughly half the bound) — consistent
  with, and far looser than, the proved bound above; this is corroborating
  evidence, not a proof (the proof above is the actual argument, already
  complete and elementary).

### Recommendation to the outliner
Dispatch a builder to formalize the argument in section "Distinct openings
(1)" above as the closure of Case (ii) of vertex $c=t\in S''$ in
`greedy-halving-adversary.md`. This closes one more piece of the
"simultaneous $q_1$-cut and tail-refinement" residual unconditionally for
every $m\ge3$, leaving only: (a) $c=x$ for $m\ge5$ (=$\mathrm{MaxCeil}
(m\ge5)$, shared with the sibling, genuinely entangled with the Necessity
Theorem), and (b) Case (i)'s "split-rung fragment removed" sub-case
(=$\mathrm{MaxCeil}(m-1)$, open for $m\ge6$, also entangled). This is a
real narrowing: after this closure, $h(3)$'s "simultaneous cuts" piece
would have Case (i) fully closed except one small residual and Case (ii)
fully closed — worth checking whether $h(3)$ itself (the whole simultaneous
piece, all vertices) becomes fully closed at $m=3$, since $m=3$ needs only
$\mathrm{MaxCeil}(3)$ (certified) and $\mathrm{MaxCeil}(2)$-level facts for
the split-rung piece (need to check the split-rung sub-case's $m-1$ index
at $m=3$: reduces to $\mathrm{MaxCeil}(2)$, likely also within certified
range) — this could be a genuine full closure of $h(3)$'s simultaneous-cuts
piece this round, a concrete, checkable near-term target.
