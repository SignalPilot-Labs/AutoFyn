## imo-2026-03 (lens: sharpest open target — GT(m) sub-case (i) width-1 window)

### What is open, exactly (verified against the approach file, round 15)

`self-similar-induction-on-n`'s **Sub-case (i) Window Reduction Theorem**
(round 15, file lines ~4126-4140) proves: for every $k\ge1$, every excess
$e\ge0$, and every $a_1\in(2^{k-1},2^k]$ with $a_1\ge2^{k-1}+1$ (i.e.
**outside** the open interval $(2^{k-1},2^{k-1}+1)$), and every $R$
(arbitrary count, $\max(R)\le2^{k-1}$, $\mathrm{sum}(R)=2^k-a_1$):
$\mathrm{OddSum}(\{a_1\}\cup R\cup\Gamma_{k-1})\ge2^k$.

**Exact boundary bookkeeping** (checked directly, not just quoted): the
residual window is the **open** interval $a_1\in(2^{k-1},2^{k-1}+1)$.
Both endpoints are already handled elsewhere: $a_1=2^{k-1}$ itself is
excluded from sub-case (i)'s own domain (sub-case (i) is defined by $a_1$
being $D$'s *unique* element $>2^{k-1}$, so $a_1=2^{k-1}$ doesn't arise
here at all), and $a_1=2^{k-1}+1$ is covered by the theorem's own
non-strict $a_1\ge2^{k-1}+1$. So "open at both ends" is correct as a
description of the interval notation, but misleading operationally — there
is no boundary case left dangling at either end; the entire remaining gap
is the interior $(2^{k-1},2^{k-1}+1)$, genuinely open at every interior
point, for every excess $e\ge0$ (recall $e:=|D|-(k+1)$, so $|R|=k+e$).

### New finding this round (numerically established, exact `Fraction`
### verification + optimization; not yet written into a lemma)

**Sharp threshold in $|R|$, found and pinned down exactly.** Restricting
to a **standalone, unembedded** instance of "$\mathrm{GT}(k)$ with excess"
— i.e. treating $D=\{a_1\}\cup R$ as its own object with
$\mathrm{sum}(D)=2^k$ exactly (this is literally the reduction the file's
own Step 3 performs via the Monotonicity Reduction Lemma, "reduce to
$\mathrm{sum}(D)=2^k$ for the outer object at level $k$") — the target
$\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge\mathrm{sum}(R)$ **holds with margin
exactly $0$ whenever $|R|=k$ (i.e. $e=0$), and is genuinely FALSE, with an
$O(1)$ (non-vanishing) margin, as soon as $|R|=k+1$ (i.e. $e=1$)**, for
every $k$ tested ($k=1,\dots,10$). This is an exact threshold, confirmed
in both directions:
- $|R|\le k$: zero violations found (thousands of trials, $k=1..7$;
  margin exactly $0$ at $|R|=k$, matching the theorem's tightness).
- $|R|=k+1$: differential-evolution optimization (`scipy`,
  `maxiter=500`, multi-seed) plus direct `Fraction` verification finds
  **robust negative margins around $-0.35$ to $-0.5$** at every
  $k=5,\dots,10$ (not shrinking with $k$ — this is a genuine, structural
  failure, not a vanishing edge effect).

**Exact witness** (own script, `Fraction` arithmetic, hand-verifiable):
at $k=3$, take $R=$ scaled copy of $\{2,1,\tfrac12,\tfrac12\}$ by
$\tfrac{399}{400}$, i.e. $R=\{\tfrac{399}{200},\tfrac{399}{400},
\tfrac{399}{800},\tfrac{399}{800}\}$, $\mathrm{sum}(R)=\tfrac{399}{100}\in
(3,4)$ (inside the window at $k=3$: cap $=4$). Then
$\mathrm{OddSum}(R\cup\Gamma_1)=\tfrac{2799}{800}$, exactly
$\tfrac{393}{800}$ **below** the target $\tfrac{399}{100}$. This is a
genuine, exact counterexample to the fully general (arbitrary-count,
arbitrary-cap-respecting $R$) excess-relaxed statement.

**But — crucial second finding, the useful part.** This counterexample
does **not** actually arise from the real recursive proof of the official,
piece-count-bounded $\mathrm{GT}(m)$. I directly simulated the genuine
embedding: take a top-level $D$ with $|D|\le m+1$ (the *official* bound,
no relaxation), $\mathrm{sum}(D)=2^m$ exactly (the hard gap-(a) regime),
one or more $q=0$ steps down to level $k=m-e$, landing on $a_1$ in the
window at level $k$. Because $\mathrm{sum}(D)$ stays **fixed** at $2^m$
throughout a $q=0$ chain (nothing is removed from $D$ by a $q=0$ step —
only $\Gamma$'s own top elements get peeled and added to the running
$\mathrm{OddSum}$), the *actual* $R=D\setminus\{a_1\}$ arising this way has
$\mathrm{sum}(R)=2^m-a_1$ — **large** (of order $2^m$), not the small
value $2^k-a_1$ used in the abstract counterexample above. Testing this
*actual* large-sum, count-bounded regime directly (both near-extremal
"pack $R$'s elements against the cap" constructions and randomized search,
exact `Fraction`, $e=1$: $m=4,\dots,6$; $e=2$: $m=8,\dots,12$; $e=3$:
$m=16,20,24$, thousands of feasible trials total) finds **no violations at
all** — margins are large and positive (growing with $m$, e.g. $\approx
1.5,3.5,7.8$ at $e=1$, $m=4,5,6$; still comfortably positive at every
tested $e=2,3$ instance).

**Diagnosis (the actionable lead).** The file's Step 3 "reduce via
Monotonicity to $\mathrm{sum}(D)=2^k$ for the outer object at level $k$"
appears to reduce the real (embedded, large-$\mathrm{sum}(R)$) problem down
to an artificially small-sum boundary case that (a) is **provably false**
in general, and (b) **cannot actually be reached** by the genuine
recursion, since $\mathrm{sum}(D)$ is locked at $2^m$ throughout a $q=0$
chain, not freely reducible down to $2^k$. This looks like exactly the
"shared-gap-is-really-a-wrong-reduction" situation Rule 94 warns about:
the *technique* (Monotonicity-reduce-to-a-fixed-small-boundary-value) is
what's stuck, not necessarily $\mathrm{GT}(m)$ itself. The genuinely
needed statement — $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1$ for $R$
with the *actual*, large, forced sum $2^m-a_1$ — shows robust numerical
slack in every test performed, suggesting $\mathrm{GT}(m)$ for $m\ge4$ is
very likely still **true**, but needs a proof that directly exploits
$\mathrm{sum}(R)$'s largeness (e.g. apply the Monotonicity/Growth Lemma in
the *other* direction — down from the actual large sum to a large-sum
threshold, or apply $\mathrm{GT}(k-1)$-with-count-$|R|>k$ using the excess
count constructively rather than shrinking sum first) rather than the
current small-sum reduction.

### Cheap-kill candidates
- The exact $|R|=k$ vs $|R|=k+1$ threshold (margin $0$ exactly at
  $e=0$, robust negative at $e=1$, for the **unembedded** abstract
  statement) is a clean, checkable structural fact — worth stating as a
  lemma boundary (the excess-relaxed $\mathrm{GT}(k,e)$ is true iff
  $e=0$, false for $e\ge1$, *in the fully general/arbitrary-sum-$R$
  form*).
- Feasibility pigeonhole: for the *embedded* scenario with $e$ q=0-steps,
  feasibility of the window instance itself requires roughly $m\cdot
  2^{k-1}\gtrsim2^m$, i.e. $e=m-k=O(\log m)$ — consistent with the file's
  own $k=0$ uniform base-case feasibility argument, and worth using to
  bound how much excess ever needs handling for a given $m$.

### Candidate technique(s)
- Directly re-derive Step 3's reduction using the **actual** forced value
  $\mathrm{sum}(R)=2^m-a_1$ (not $2^k-a_1$) — i.e., do NOT invoke
  Monotonicity Reduction to shrink to the small boundary; instead show
  the AltSum/Peeling machinery gives enough slack once $\mathrm{sum}(R)$
  is genuinely large (numerically the slack is generous, not tight —
  unlike the $e=0$ case, which is exactly tight, this large-sum regime
  has real room, suggesting even a fairly crude bound might close it).
  This is the single most promising unexplored lead this round.
- The AltSum Small-Sum Lemma / AltSum Corollary machinery (certified,
  `lemmas/altsum-corollary-and-growth-lemma.md`,
  `lemmas/altsum-reformulation-and-single-insertion.md`) is still the
  right toolkit — the issue is which sum value it's being applied to, not
  the tool itself.

### Knowledge-base entries to use
No new `knowledge_base.md` entries beyond what the approach file already
cites (Global-max Peeling, Companion Peeling, Monotonicity/Growth Lemmas,
Lemma AS). This is a self-contained combinatorial identity problem; the
KB's generic theorem-proving techniques (extremal principle, induction)
are already in use structurally.

### Analogous past problems (cruxes)
Did not requery the crux corpus this round (out of scope for this
narrowly-targeted numerical/structural scouting pass); prior rounds'
explorers have already searched combinatorics/alternating-sum subtopics
without finding a closer analogue than the file's own internal
self-similar recursion pattern. No new candidate found or expected to
help here — this is a highly bespoke identity-chasing problem.

### Prior progress
As stated in `current.md` / the approach file: Sub-case (i) closed
unconditionally for $a_1\ge2^{k-1}+1$, every excess $e$ (round 15,
certified-ready). Residual: exactly the width-1 window
$a_1\in(2^{k-1},2^{k-1}+1)$, with excess $e\ge0$ unconstrained by any
proof so far.

### Dead ends (do not retry)
- **The literal $G(m,k;V)$ revival** (round 15, Step 1): confirmed dead —
  domain mismatch, doesn't cover sub-case (i)'s actual $a_1$ range.
- **Route-2 continuity/limiting-transfer for `Case-B(m,k)`'s boundary**
  (round 15, Step 4): re-verified here (agrees with round 15's own
  finding) that no shrinking-$\delta$ family of proved interior results
  exists to take a limit of — this route is genuinely inapplicable, not
  just difficult. Do not re-dispatch as stated.
- **NEW this round: proving the excess-relaxed
  $\mathrm{GT}(k,e\ge1)$ statement in its fully general (arbitrary
  $\mathrm{sum}(R)$, not just the actual embedded large value) form** —
  confirmed **false** by exact counterexample (see witness above). Any
  future attempt to close the window via "prove $\mathrm{GT}(k)$ with
  unrestricted excess at its own small boundary $\mathrm{sum}(D)=2^k$" is
  doomed; this generalization is not true and should not be attempted
  again. The fix is to track the *actual* (large) sum $R$ carries when
  genuinely embedded, not reduce to the small boundary.

### Case-B(m,k) — brief separate assessment
No new lead found or attempted this round (out of the assigned lens's
scope; time was spent on the width-1 window instead, per dispatch
priority). Round 15's refutation of the Route-2 continuity/limiting
premise stands (re-confirmed above as a by-product of checking Step 4).
No alternative mechanism was explored here. The one open observation
worth flagging for a future round: `Case-B(m,k)`'s sliver
$(2^{m-1}-1,2^{m-1})$ has the *same* shape as the sub-case (i) window
studied here, and the same diagnosis may apply — i.e. any future
"reduce via Monotonicity to a small/boundary sum" argument for
`Case-B(m,k)` should be checked for the same over-generalization trap
before being trusted, even if it looks locally valid.

### Small-case / intuition notes (all numeric, conjectural)
- Conjecture, well-supported numerically (dozens of feasible $(m,e)$
  instances, thousands of random + optimized trials, exact `Fraction`,
  zero violations, margins large and growing with $m$): the **actually
  arising** sub-case (i) instances (embedded, count-bounded by $m+1$,
  forced large $\mathrm{sum}(R)$) satisfy $\mathrm{GT}(m)$ comfortably —
  this is genuinely different from, and much easier than, the abstract
  small-sum excess statement, which is false. This strongly suggests
  $\mathrm{GT}(m)$, $m\ge4$ is **true** and the obstruction is in the
  current proof's reduction step, not in the underlying fact.
- The $e=0$/$|R|=k$ boundary is exactly tight (margin $0$ achievable) —
  this matches the file's own "closed on the majority of the range"
  framing and confirms no slack is being left on the table there.
