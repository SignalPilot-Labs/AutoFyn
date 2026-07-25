# Proof review — round 19, imo-2026-03

Build set: `self-similar-induction-on-n`, `global-lp-vertex-sufficiency`.
Both reviewed independently, from scratch (own exact-`Fraction` / `scipy`
scripts, none reused from the builders).

---

## `self-similar-induction-on-n`

**Verdict: CHANGES REQUESTED.** Status: `partial` (self-reported
correctly).

### What I verified correct

- **Lemma TPC (Tied-Pair Cancellation).** Re-derived and stress-tested
  independently (own script: 30,000 random trials, base multiset of
  distinct values plus an exactly-multiplicity-2 pair inserted at a
  fresh value; zero mismatches). Proof is a straightforward consecutive-
  rank argument; correct.

- **Lemma BCF (Block-Contribution Formula) + even-block corollary.**
  Re-implemented the formula directly from its definition and compared
  against direct `AltSum` computation: 20,000 trials, zero mismatches.
  Corollary (forcing a random level to even multiplicity and comparing
  with/without that level): 10,000 trials, zero mismatches. Both
  correct.

- **Lemma LNI (Local Non-Improvement) + Vertex Reduction consequence.**
  Constructed a concrete opposite-parity-pair example ($k=3$,
  $\Gamma_2=\{4,2,1\}$, $r_i=3.5$ at rank 2, $r_j=0.5$ at rank 5):
  confirmed the predicted linear rate $\Delta\mathrm{AltSum}=
  t\cdot(c_i-c_j)=-2t$ exactly at $t=\pm0.1$. The proof (affineness on a
  rank-crossing-free neighborhood) is elementary and correct. Its stated
  scope (a necessary condition, not a full classification — explicitly
  does not rule out same-parity-unequal pairs or single free
  coordinates) is honest, not overclaimed.

### A real bug found: the "Exact achievability" theorem is FALSE at k=2

The round's headline claim is: for **every** $k\ge2$ and every
$S\in[2^k,2^k+1)$, $R^*=\{2^{k-1},\dots,4\}\cup\{r,r\}$
($r=(S-2^k)/2+2$, chain has $k-2$ elements) is feasible for GCH($k$) and
attains $\mathrm{AltSum}(R^*\cup\Gamma_{k-1})=1$ exactly, "proved in
full, no numerics."

I checked this by direct exact-`Fraction` computation. At $k=2$: the
chain is stated to be empty ("$k-2=0$ elements"), so $R^*=\{r,r\}$ with
$r=(S-4)/2+2\in[2,2.5)$ for $S\in[4,5)$. But
$\mathrm{cap}=2^{k-1}=2$ at $k=2$, and $r>2$ for every $S>4$ — e.g.
$S=4.5\Rightarrow r=2.25>2=\mathrm{cap}$. **$R^*$ is infeasible** (fails
$\max(R)\le\mathrm{cap}$) at $k=2$ for all but the single boundary
point $S=4$. The algebra still gives $\mathrm{AltSum}=1$ if you ignore
the cap violation, but the construction is not a legal instance of
GCH(2)'s feasible set.

The source file's own attempted resolution — "matching and generalizing
the $k=2$ equality locus already certified in Lemma 2... there,
$R^*=\{2,r,r\}$ exactly matches this formula's $k=2$ specialization,
chain empty" — is **internally inconsistent**: a chain-empty
specialization of $\{2^{k-1},\dots,4\}\cup\{r,r\}$ is literally
$\{r,r\}$ (two elements), not $\{2,r,r\}$ (three elements). These do
not match, and the cross-check verifies nothing; it papers over the
cap violation rather than resolving it.

I confirmed the formula **is** correct and rigorously proved for
$k\ge3$ (chain nonempty, top element $=2^{k-1}=\mathrm{cap}$, and
$r<2.5\le2^{k-1}$ always, so feasible): independently checked $k=3,
\ldots,8$ across several $S$ values (feasibility + exact $\mathrm{AltSum}
=1$), and separately confirmed via a from-scratch multi-restart
`scipy.optimize` constrained search at $k=3$ that the true numeric
minimizer's shape and value match $R^*$ exactly at several $S$.

**Net mathematical status (not just a labeling issue — a genuine
infeasibility, but salvageable):** achievability at $k=2$ is *still
true*, just not via this formula — it is already established by the
separately-certified Lemma 2 in
`lemmas/sharper-odd-residual-and-k2-cardinality-half-sum.md`, whose true
equality witness (confirmed independently via `scipy` search) is
$R=\{2,b,b\}$, $b=(S-2)/2\in[1,1.5)$ — which *does* retain the cap
element $2$ (unlike the round-19 general formula's empty chain at
$k=2$). This also surfaces a small, non-load-bearing labeling slip
already present in the certified Lemma 2's own worked example, which
reads "$R=\{b,b,1\}$" — this does not even satisfy $\mathrm{sum}(R)=S$
for the stated $b=(S-2)/2$ (sum would be $2b+1=S-1\ne S$); the correct
witness is $\{2,b,b\}$ (sum $=2+2b=S$, matches exactly). This does not
affect Lemma 2's proved inequality, only its parenthetical example.

**Certified in corrected form**:
`results/imo-2026-03/lemmas/gch-achievability-witness-k-geq-3.md`
(states and proves the theorem for $k\ge3$ only, documents the $k=2$
failure and its resolution via the separate, already-certified
construction).

### The remaining open gap — correctly scoped

The general lower bound $\mathrm{AltSum}(R\cup\Gamma_{k-1})\ge1$ for
*every* feasible $R$ (arbitrary $k$) is reduced, via Lemma BCF, to a
precisely stated finite-per-$k$ combinatorial claim about integer
multiplicity vectors $(m_0,\ldots,m_{k-1})$. This is proved for $k=2$
(matches the already-certified exhaustive Lemma 2) and numerically
corroborated (multi-restart exact-objective `scipy` search) for
$k=3,4,5$, but **not proved for general $k$**. The file is explicit and
honest about this ("NOT proved in general for arbitrary $k$ this
round," "Not promotable" section correctly excludes it). No overclaim
found here — this is genuinely still open, correctly labeled as such.

### Certified this round
- `lemmas/tied-pair-cancellation-and-block-contribution-formula.md`
  (Lemma TPC, Lemma BCF + corollary, Lemma LNI + Vertex Reduction —
  all as stated, no corrections needed).
- `lemmas/gch-achievability-witness-k-geq-3.md` (achievability theorem,
  corrected to $k\ge3$, with the $k=2$ bug documented and resolved via
  the separate certified construction).

---

## `global-lp-vertex-sufficiency`

**Verdict: CHANGES REQUESTED.** Status: `partial` (self-reported
correctly).

### $n=2$ Existence Theorem (upper-bound direction) — verified in full, real milestone

Independently re-derived every step from the region's definitions:

1. **$p_1=(1+2d_1+d_2)/3$**, from substituting $p_2=p_1-d_1$,
   $p_3=p_1-d_1-d_2$ into $p_1+p_2+p_3=1$ — checked by direct algebra,
   an unconditional identity. Since $d_1,d_2>\gamma(2)=1/7$ strictly,
   $p_1>10/21$ strictly.
2. **Order claim**: $p_3-(p_1-p_2)=1-2p_1$ exactly (direct algebra from
   $p_3=1-p_1-p_2$), so $p_3>(p_1-p_2)\iff p_1<1/2$ — and $p_1<1/2$ is
   itself a region-defining hypothesis, so the order holds
   unconditionally throughout $B(2)$, no sub-case needed.
3. **Value**: with the resulting order $p_2\ge p_2>p_3>p_1-p_2$,
   $\mathrm{OddSum}(M)=p_2+p_3=1-p_1<11/21<4/7=c(2)$.

All three steps re-derived independently and confirmed correct. I ran my
own exact-`Fraction` script over 500,000 random samples of $B(2)$
(different sampling scheme from the builder's, region back-solved from
random $d_1,d_2>\gamma(2)$): zero violations of $p_1>10/21$, zero
violations of the order claim, zero mismatches of the identity
$\mathrm{OddSum}(M)=1-p_1$, zero violations of $\mathrm{OddSum}(M)<c(2)$;
observed max $\mathrm{OddSum}\approx0.523793$, consistent with (below)
the proved supremum $11/21\approx0.523810$. This is a complete,
gap-free, casework-free proof. Combined with the already-certified
closure of the complementary region (cited
`lemmas/singleton-interleaving-and-k-anchor-merge.md`), this gives
$V(p)\le c(2)$ for **every** $p$ at $n=2$ — a genuine full closure of
$n=2$'s upper-bound direction. **Certified**:
`lemmas/n2-existence-theorem-upper-bound.md`.

### Achievability half — correctly scoped as a gap, not overclaimed

I independently checked two of the file's exact claims: shape $(1,0,0)$
(splitting $p_1$ at $p^*=(4/7,2/7,1/7)$) gives $\mathrm{OddSum}=4/7$
identically for $a\in\{1/7,2/7,1/4,3/7\}$ (matches the claimed range
$[4/7,5/7)$ with minimum $4/7$), and shape $(2,0,0)$'s claimed exact
witness (fragments $1/105,1/7,44/105$) gives $\mathrm{OddSum}=4/7$
exactly, matching $c(2)$ digit-for-digit. Both check out. The file
correctly states: $V(p^*)\le c(2)$ fully proved (exact witness);
$V(p^*)\ge c(2)$ fully proved for the 4 shapes using $\le1$ cut
(exhaustive case analysis) and for the shapes $(2,0,0)$/$(1,1,0)$ where
grid search hit exact equality, but the remaining shapes are only
supported by a converging exact grid search, not a complete vertex
enumeration. This is honestly flagged as a gap ("I do not claim
$V(p^*)=c(2)$ as a certified fact this round"), not overclaimed. I did
not myself complete the missing vertex-enumeration for the 6 two-cut
shapes (out of scope for this review's time budget) — this remains a
genuinely open, well-scoped item, not resolved by my review.

### $n=3$ parity-obstruction diagnosis — sound reasoning, correctly labeled a diagnosis

I independently re-tested the claimed broad failure of the naive
single-cut lift at $n=3$ with my own exact-`Fraction` script (different
sampling range from the builder's): found a 79.9% violation rate over
36,172 valid $B(3)$ points (vs. the file's reported 87.6% over 45,108
points) — same order of magnitude, broad/large-scale failure in both,
not a rare edge case; the discrepancy in exact rate is attributable to
differing sampling distributions (I used a different random parameter
range), not a bug. The structural explanation given (even- vs.
odd-sized resulting multiset changes which rank the new fragment lands
on, and no single region hypothesis pins the fragment's position
relative to *two* untouched pieces the way $p_1<1/2$ pinned it against
one) is sound, elementary reasoning, and is correctly presented as a
diagnosis motivating a next probe ("untested, flagged honestly, not
claimed to work"), not as a proof of anything about $n=3$. No overclaim
found.

### Certified this round
- `lemmas/n2-existence-theorem-upper-bound.md` (full upper-bound
  direction for $n=2$, as stated, no corrections needed).

---

## Summary

Both approaches: **CHANGES REQUESTED**. `self-similar-induction-on-n`
produced three genuinely new certified lemmas but its round headline
("achievability for every $k\ge2$, no numerics") contained a real,
independently-confirmed bug at $k=2$ (infeasible construction), now
corrected and certified as $k\ge3$-only, with $k=2$ resolved via the
pre-existing Lemma 2 (whose own worked example also had a small,
non-load-bearing labeling error, now noted). `global-lp-vertex-
sufficiency` achieved a genuine, fully-verified milestone — the
complete $n=2$ Existence Theorem upper-bound direction — while
correctly and honestly scoping the remaining gaps (achievability's 6
two-cut shapes; $n\ge3$ entirely open, with only a sound diagnosis, not
a proof, of the obstruction). Neither approach's central open gap
(general-$k$ GCH lower bound; $n\ge3$ Existence Theorem) is closed this
round.

## Files written
- `/home/agentuser/repo/results/imo-2026-03/current.md` — updated
  Status (unchanged, `partial`) and new "Approaches tried (round 19)"
  section.
- `/home/agentuser/repo/results/imo-2026-03/lemmas/tied-pair-cancellation-and-block-contribution-formula.md`
  (new, certified).
- `/home/agentuser/repo/results/imo-2026-03/lemmas/gch-achievability-witness-k-geq-3.md`
  (new, certified in corrected form).
- `/home/agentuser/repo/results/imo-2026-03/lemmas/n2-existence-theorem-upper-bound.md`
  (new, certified).

Ranker outcomes recorded: `self-similar-induction-on-n` → `partial`;
`global-lp-vertex-sufficiency` → `advanced`.
