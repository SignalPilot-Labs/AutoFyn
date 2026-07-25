## imo-2026-03 — lens: Case-B(m,k) (the e=0 sliver)

### Exact current statement of Case-B(m,k)

From `approaches/self-similar-induction-on-n.md`, "Round 5: Case-B(m,k),
the sliver reduction" (Theorem 2, line ~2295): fix $m\ge2$,
$\Gamma_{m-2}=(2^{m-2},\ldots,2,1)$ ($\mathrm{sum}=2^{m-1}-1$). $B$ is any
partition of $2^m$ into $p\le m+1$ positive parts, $b_1:=\max(B)$.

- **Fully closed** (round 5, certified-by-derivation, not yet a lemma
  file but a completed argument in the approach file): every $b_1\le
  2^{m-1}-1$ (via a dichotomy at $\mu=2^{m-2}=\max(\Gamma_{m-2})$: sub-case
  (ii) $b_1<2^{m-2}$ via Peeling + Lemma B (First-mover-half); sub-case
  (i-a) $2^{m-2}\le b_1\le2^{m-1}-1$, same mechanism).
- **Open ("the sliver")**: $b_1\in(2^{m-1}-1,\,2^{m-1})$ — width exactly
  $1$, for every $m$. Target: $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$.
  Lemma B's bound (OddSum$\ge$sum$/2$) falls short here by up to (as
  $b_1\to2^{m-1}$) nearly $\tfrac12$ in OddSum, i.e. up to nearly $1$ in
  AltSum terms — a genuine zero-slack gap, not a technical artifact
  (round 5's own extremal configuration $B^*=(2^{m-1},2^{m-2},\ldots,4,2,2)$
  attains $\mathrm{OddSum}(B^*\cup\Gamma_{m-2})=2^m-1$ *exactly* at the
  excluded boundary $b_1=2^{m-1}$, confirming the target constant $2^m-1$
  is sharp and the sliver is a real obstruction, not slack that a better
  constant would remove).
- Per round 4/11's "Corollary (exact equivalence)" (line ~4580): for
  $D$ with $\max(D)\le2^{m-1}$, $\mathrm{sum}(D)\le2^m$: $\mathrm{OddSum}
  (D\cup\Gamma_{m-1})\ge\mathrm{sum}(D)\iff\mathrm{OddSum}(D\cup\Gamma_{m-2})
  \le2^m-1$ — so Case-B(m,k) at $\mathrm{sum}(D)=2^m$ is literally
  equivalent to the GT(m) "$q=0$" branch's target at the top boundary,
  and (via the Growth Lemma) is the single object both named
  sub-sub-cases of sub-case (ii) reduce to. Case-B(m,k) is the file's own
  seven-plus-round central obstruction, not a side issue.
- Round 17 additionally states (not re-derived by me, taken as the file's
  own diagnosis) that Sub-case (i)'s own residual **at $e=0$** ($q=1$
  branch, $a_1\in(2^{k-1},2^{k-1}+1)$) is "structurally identical" to
  Case-B(m,k)'s sliver — same zero-slack shape, but I did **not** verify
  they are literally the same statement (see "Distinct openings" below —
  my derivation suggests they need slightly different treatments, so
  don't assume closing one closes the other without checking).

### Distinct openings

**1. (Primary new lead — verified numerically, not yet proved) A
cap-free strengthening of the certified GCH lemma, combined with the
already-certified AltSum peeling identity, appears to close the sliver
completely, with room to spare — not just at the boundary.**

Peel $b_1$ (the global max of $B\cup\Gamma_{m-2}$ in the sliver, since
$b_1>2^{m-1}-1>2^{m-2}=\max(\Gamma_{m-2})$ for $m\ge2$) via the already
**certified** `Global-max Peeling` identity ($\mathrm{AltSum}(N)=\max(N)-
\mathrm{AltSum}(N\setminus\{\max N\})$,
`lemmas/altsum-corollary-and-growth-lemma.md`):
$$\mathrm{AltSum}(B\cup\Gamma_{m-2})=b_1-\mathrm{AltSum}(B'\cup\Gamma_{m-2}),
\quad B':=B\setminus\{b_1\}.$$
Case-B(m,k)'s target $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$ is
equivalent (via $\mathrm{OddSum}=(\mathrm{sum}+\mathrm{AltSum})/2$) to
$\mathrm{AltSum}(B\cup\Gamma_{m-2})\le2^{m-1}-1$, i.e. to
$$\mathrm{AltSum}(B'\cup\Gamma_{m-2})\ \ge\ b_1-2^{m-1}+1.$$
In the sliver $b_1\in(2^{m-1}-1,2^{m-1})$ the RHS is $<1$, so it suffices
to show $\mathrm{AltSum}(B'\cup\Gamma_{m-2})\ge1$. Now check $B'$'s
parameters: $\mathrm{sum}(B')=2^m-b_1\in(2^{m-1},2^{m-1}+1)$ (matching the
$S\in[2^{(m-1)},2^{(m-1)}+1)$ range of $\mathrm{GCH}(m-1)$ **exactly**,
with $k:=m-1$), and $|B'|=|B|-1\le m=(m-1)+1$ (matching $\mathrm{GCH}(m-1)$'s
cardinality cap **exactly**). So $B'$ is *literally* a feasible instance
of $\mathrm{GCH}(m-1)$ — **except** the certified GCH lemma also requires
$\max(B')\le\mathrm{cap}=2^{m-2}$, which is **not** guaranteed ($B'$'s
elements are only known to be $\le b_1<2^{m-1}$, and can exceed $2^{m-2}$
— checked concretely, e.g. $m=4$: $b_1\approx7.5$, two other parts each
$\approx4.25>2^{m-2}=4$ is achievable).

**So the whole sliver reduces to one precise open question: does the
certified General Cardinality-Constrained Half-Sum Lemma's conclusion
($\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for $|R|\le k+1$,
$\mathrm{sum}(R)\in[2^k,2^k+1)$) still hold if the hypothesis
$\max(R)\le2^{k-1}$ is dropped entirely?**

I stress-tested this cap-free version numerically and it appears to hold
with the *exact same* bound $\ge1$ (not weaker):
- Direct rescan of the certified proof's own case split (`Case (C2)`,
  which is the only branch that explicitly cites the interval $(0,
  \mathrm{cap}]$): re-derived by hand that dropping the upper endpoint
  $\mathrm{cap}$ (extending the topmost interval to $(v_1,\infty)$)
  changes nothing — the function is still affine with slope $+1$ on that
  interval (rank of $r$ is still $1$ for all $r>v_1$), so its infimum is
  still attained at the same captured endpoint $r\to v_1^+$
  ($=\mathrm{AltSum}(A\setminus\{v_1\})$), unaffected by removing the cap.
  Steps A, (C0), (C1) as written never cite $\mathrm{cap}$ at all (only
  Case (C2) does, and only to define the domain of $r$, not in a way that
  is load-bearing for the minimum). The scope note in
  `lemmas/general-cardinality-constrained-half-sum-lemma.md` already says
  the cardinality cap is load-bearing "exactly twice" (Step A, Case C1)
  and does **not** mention the value cap as load-bearing anywhere — mild
  supporting evidence this was already suspected/checked, though not
  stated as a theorem.
- `scipy.optimize.SLSQP` multi-restart search (own script,
  `/tmp/test_gch_scipy.py` and `/tmp/test_extreme.py`), minimizing
  $\mathrm{AltSum}(R\cup\Gamma_{k-1})$ over **all** positive-real $R$ with
  $|R|=p\le k+1$, $\mathrm{sum}(R)=S$ fixed at the boundary $S=2^k$
  (worst case), **no upper bound on individual $R_i$ at all** (bounds
  $(10^{-8},S)$, i.e. effectively unconstrained except positivity/sum),
  40–60 restarts per $(k,p)$, deliberately seeding some restarts with one
  element near $S$ (far exceeding $\mathrm{cap}=2^{k-1}$): for
  $k=2,\ldots,7$ and every $p\le k+1$, minimum found is **exactly $1.0$**
  at $p=k+1$ (strictly larger for $p<k+1$), matching the certified
  cap-present bound to $\sim10^{-12}$ precision, with the optimizer
  actively exploring cap-violating configurations and never doing better.
- Random-sampling stress test with elements forced $>\mathrm{cap}$
  (`/tmp/test_gch_adversarial.py`, 30,000 trials, $k=2,\ldots,7$): zero
  violations of $\mathrm{AltSum}\ge1$.
- Applied directly to Case-B's own $B'$ (`/tmp/test_caseb.py`, 11,730
  exact-`Fraction` trials, $m=2,\ldots,8$, random partitions with $b_1$
  in the sliver, no cap imposed on the other parts): zero violations of
  the *original* target $\mathrm{OddSum}(B\cup\Gamma_{m-2})\le2^m-1$;
  worst observed margin $\approx1/500$, consistent with a genuinely tight
  (but not violated) boundary as $b_1\to2^{m-1}^-$.
- Small-$m$/small-$k$ boundary check: Case-B$(2,k)$ needs the cap-free
  bound at $k=m-1=1$, **outside** GCH's certified range ($k\ge2$).
  Checked directly and numerically (`/tmp/test_m2.py`, 20,000 exact-
  `Fraction` trials): zero violations of the target
  $\mathrm{AltSum}(B\cup\{1\})\le1$; this $k=1$ instance is small enough
  ($|R|\le2$) that it looks provable by direct casework, not needing the
  general machinery.

**If the cap-free strengthening of GCH is provable** (I believe the
proof sketch above — re-examining Case (C2) — essentially already proves
it, modulo formalizing that Steps A/(C0)/(C1) genuinely never use the cap
either, which I checked informally but a builder must verify line by
line), **then Case-B(m,k)'s sliver closes with room to spare**: the
chain gives $\mathrm{AltSum}(B\cup\Gamma_{m-2})=b_1-\mathrm{AltSum}
(B'\cup\Gamma_{m-2})\le b_1-1<2^{m-1}-1$ strictly, for **every** $b_1$ in
the sliver, not just asymptotically near the boundary. This is a
substantially stronger and cleaner result than the "nearly $\tfrac12$
shortfall" diagnosis in the file — the gap turns out to be closeable
head-on via a two-step peel-then-invoke-GCH argument, not needing a new
inequality mechanism from scratch. **This is the strongest, most
concrete lead I found this round; I recommend the outliner dispatch a
builder to (a) formalize the cap-free GCH strengthening (a re-examination
of an already-certified proof, likely modest effort) and (b) formalize
the peeling reduction above.**

**2. Does this also close Sub-case (i)'s own $e=0$ form?** I checked
this directly (not just trusted the file's "structurally identical"
claim) and it does **not** obviously fall out of the same trick. For
sub-case (i) at $e=0$ ($D=\{a_1\}\cup R$, $a_1\in(2^{k-1},2^{k-1}+1)$,
$\max(R)\le2^{k-1}$, $\mathrm{sum}(D)=2^k$), Companion Peeling gives
$\mathrm{OddSum}(D\cup\Gamma_{k-1})=a_1+\mathrm{OddSum}(R\cup\Gamma_{k-2})$,
needing $\mathrm{OddSum}(R\cup\Gamma_{k-2})\ge2^k-a_1=\mathrm{sum}(R)$
— note $\mathrm{sum}(R)\in(2^{k-1}-1,2^{k-1})$, i.e. **below**, not above,
the GCH threshold $2^{k-1}$. This is the *opposite* side of the
threshold from where GCH applies (GCH needs $S\in[2^k,2^k+1)$, i.e. just
*above* a threshold of $2^k$; here $\mathrm{sum}(R)$ sits just *below*
$2^{k-1}$). So this residual is genuinely a different (mirror-image, "$S$
approaches the threshold from below") statement, not literally an
instance of GCH or its cap-free extension. **Do not assume closing
Case-B(m,k) via lead 1 automatically closes sub-case (i)'s own $e=0$
form** — that needs either (a) an independent "GCH from below" analogue
(untested this round — a natural next probe), or (b) locating the exact
equivalence the file gestures at (round 4/11's Corollary, cited above,
which requires $\max(D)\le2^{m-1}$ **and** connects $D$'s *own* target at
$\mathrm{sum}(D)=2^m$ to Case-B(m,k) when $D$ is thought of as "$B$" — I
did not verify whether sub-case (i)'s specific $D=\{a_1\}\cup R$ literally
satisfies the Corollary's role as "the $B$", since the Corollary's proof
uses the exact identity that requires re-checking against $D$'s specific
partition shape, not just its sum). This is a genuine open sub-question
worth a follow-up round.

**3. A "GCH from below" mirror lemma (untested this round, flagged as a
fallback if lead 2's connection fails).** Define $\mathrm{GCH}^-(k)$: $R$
finite multiset, $|R|\le k+1$, $\mathrm{sum}(R)=S\in(2^k-1,2^k]$ (just
below the threshold). Conjecture: $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge
2^k-S$ (matching what sub-case(i) at $e=0$ needs directly, no cap). I did
not numerically test this — flagged as the natural next probe if lead 2
turns out not to reduce cleanly to lead 1.

### Candidate technique(s)

- Peeling (Global-max Peeling / Companion Peeling, both certified in
  `lemmas/altsum-corollary-and-growth-lemma.md` and
  `monotonicity-reduction-and-unified-threshold-pair-peeling.md`) to
  reduce the sliver to a smaller, already-partially-solved object.
- The canonical-form + pigeonhole/pairing machinery of the General
  Cardinality-Constrained Half-Sum Lemma (Steps A, B, C0/C1/C2,
  `lemmas/general-cardinality-constrained-half-sum-lemma.md`) — my
  finding is that this machinery is very likely **cap-free** already (a
  strengthening, not a new construction), which is the key unlock.

### Cheap-kill candidates

- Check whether Case (C2)'s "topmost interval" argument literally needs
  the upper bound $\mathrm{cap}$ anywhere beyond defining the interval's
  domain (I did this by hand, found no load-bearing use — but a builder
  should re-verify this is not an oversight, since it's the crux of the
  whole lead).
- The small-$m$ ($m=2$, i.e. $k=1$) and small-$k$ boundary of the
  cap-free GCH extension is outside the certified lemma's stated range
  ($k\ge2$) — needs a short separate direct argument (I confirmed
  numerically it holds, and $|R|\le2$ makes it small enough for direct
  casework).

### Knowledge-base entries to use

I did not find a directly-matching generic KB entry beyond what the
approach already cites (this problem's KB usage has been almost entirely
internal, problem-specific lemma-building, not generic KB theorems). If
useful for framing: standard alternating-sum / rearrangement-inequality
style arguments (pairing consecutive powers of two) are the flavor of
Step B in the certified GCH lemma; no new KB entry identified as
newly relevant this round beyond what's already in use.

### Analogous past problems (cruxes)

I did not run the crux corpus query this round (time budget spent on the
numeric verification above, which is the higher-value contribution for
this precise lens); I did not find, from memory of prior rounds' reports,
any flagged crux match specific to this GT(m)/GCH combinatorial-partition
structure — prior rounds' own crux checks (`lp-duality-split-polytope`,
round 16/17) targeted the *different* $n=3$/$n=4$ Existence Theorem side
of this problem, not the GT(m) recursion. Recommend a follow-up explorer
specifically query the crux corpus for "alternating sum of a multiset
against a fixed geometric comparison set" / "binary partition parity"
subtopics if one wants this angle covered — not done here to preserve
budget for the numeric lead above.

### Prior progress

Case-B(m,k) sliver ($b_1\in(2^{m-1}-1,2^{m-1})$) is open since round 4,
with round 5's precise reduction (everything outside the sliver closed)
still standing unchanged through round 21. No round has previously
attempted the peel-then-GCH reduction described in Lead 1 above — the
approach file's own round 16-19 sections explicitly identify the "Half-Sum
Corollary has zero slack at $e=0$" obstruction but only ever tried
strengthening the *bound itself* (e.g. "Two-Level Half-Bound Lemma" using
top-2 order statistics, shown insufficient, line ~2312), never tried
reducing the sliver to an already-certified *different* theorem (GCH) via
peeling. This is a genuinely new angle, not a re-tread.

### Dead ends (do not retry)

- **Two-Level Half-Bound Lemma** (round 5, `approaches/self-similar-
  induction-on-n.md` line ~2312): a direct strengthening of Lemma B using
  the top-2 order statistics; proved in full but shown insufficient to
  close the sliver (same zero-slack shortfall). Do not re-attempt this
  specific strengthening; it's a proved dead end, not an unproved lead.
- **Continuity/limiting transfer of the sliver** (round 5's original
  Route 2, retracted round 15): refuted — the sliver is a hard
  fixed-width-1 boundary, not a shrinking-$\delta$ family, so no
  continuity argument closes it. This matches the run-state note;
  independently re-confirmed by the sharp extremal example $B^*$ (see
  above) attaining the target exactly at the excluded endpoint — a hard
  wall, not an approachable limit.

### Small-case / intuition notes (labeled conjecture where not proved)

- **Conjecture, strongly numerically supported (not proved)**: the
  cardinality-constrained Half-Sum Lemma's conclusion
  $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ holds even without the
  hypothesis $\max(R)\le2^{k-1}$, for every $k\ge1$, $|R|\le k+1$,
  $\mathrm{sum}(R)\in[2^k,2^k+1)$. Verified by exact-`Fraction` random
  search (30,000+ trials) and `scipy` multi-restart constrained
  optimization (minimum found $=1.0$ exactly, matching the cap-present
  bound, across $k=2,\ldots,7$ and all cardinalities $p\le k+1$, with
  deliberately cap-violating seed points). A hand re-examination of the
  certified proof's Case (C2) (the only branch citing the cap) suggests
  the cap is not actually load-bearing there either — strong evidence
  this is a true, provable strengthening, not just a numeric artifact.
- **Conjecture, strongly numerically supported (not proved)**: applying
  this cap-free strengthening via a single Global-max peel of $b_1$
  closes Case-B(m,k)'s sliver completely and with strict inequality
  throughout (not just at the boundary) — verified directly on Case-B's
  own object (11,730 exact-`Fraction` trials, $m=2,\ldots,8$, zero
  violations, including the small $m=2$/$k=1$ boundary case outside
  GCH's stated certified range).
- Whether this transfers to Sub-case (i)'s own $e=0$ form is genuinely
  open and *not* established by this lead (see "Distinct openings" #2) —
  flagged explicitly so the outliner does not assume both twins fall at
  once.
