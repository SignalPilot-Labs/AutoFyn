# Round 26 proof-review — imo-2026-06

Reviewed all three built approaches independently, adversarially, re-deriving/
re-simulating every load-bearing numeric and algebraic claim from scratch with
fresh Python/`sympy` scripts (never trusting builder-reported numbers).

## 1. `a1-5q-subfamily-theorem` — Verdict: **APPROVE** (Status: solved)

Builder claims: literal `T=1,L=5` periodicity from `n=1` for every prime
`q≥7`, `q∉Bad(5)={7,13,19}`, `a_1=5q`. This would be the run's 6th APPROVE.

**Independent re-derivation performed (all from scratch, own scripts):**

- Recomputed the certified `p`-uniform machinery's `p=5` instantiation: the
  12-cell `(s_0(j,r), K_0(j,r))` table (`j∈{2,3,4}`, `r∈{1,2,3,4}`) via
  `pow(r,-1,5)` — exact match with the file's §3 table.
- Recomputed the `Q_1(j,r)` sufficient-window thresholds and the exact list
  of primes below each threshold — exact match with the file's §4 tables
  (12 entries).
- Recomputed every `k=0` witness `gcd` directly (own script): confirmed the
  same 3 exceptions with **no** witness in `i=1..n_0` (`q=7,13,19`, `n_0=2,
  3,4`) and a valid witness for every one of the other 9 below-threshold
  candidates. **Found two cosmetic slips** in the write-up's illustrative
  arithmetic: (a) for `(2,1,11)`, the text mislabels `a_2=55/a_3=60` — the
  correct values are `a_1=55, a_2=60`; a genuine witness (`gcd(77,60)=1`)
  does exist at the correctly-labeled index `i=2`, so the conclusion is
  unaffected. (b) for the three "no witness" exceptions, the prose lists
  gcds for `i=1,…,n_0-1` but never explicitly displays the `i=n_0` check
  (which is automatically governed by Lemma 1, `gcd(N,a_{n_0})=gcd(N,j)`);
  I independently confirmed by direct computation that `i=n_0` also fails
  in all three cases, so "no witness in the full range" is correct, just
  under-displayed in the prose. Neither slip is load-bearing.
- Recomputed the `k≥1` residual-band analysis: independently re-derived the
  exact tighter sieve bound `2^{ω(K)+1}(ω(K)+2)` for all `12×27=324` cell/k
  combinations — reproduced the exact same **13** flagged `(j,r,k)`
  combinations as the file, digit for digit.
- Verified the moot/non-moot classification: 8 of the 13 involve
  `q∈{7,13,19}` (outside the theorem's scope, hence moot regardless of the
  file's "already deviated" justification — the theorem's own quantifier
  already excludes them); the remaining 5 (`q∈{11,17}`) were independently
  recomputed and confirmed to have a genuine `i=3` witness each, with `N`
  values matching exactly.
- Verified the fresh `s^*=5` sieve threshold inequality
  `(s+1)!≥9+(5/7)2^{s+1}(s+2)` numerically for `s=5..14` — holds throughout.
- Full independent greedy re-simulation (own fresh generator, correct "for
  all `i`" legality semantics) for every prime `q∈[7,2000)`, 40 terms each:
  matches the closed form `a_n=5(q+n-1)` in every case **except**
  `q=7,13,19`, which deviate exactly at `n=3,4,5` respectively with the
  exact values the file reports (`a_3=42`, `a_4=78`, `a_5=114`). This
  independently confirms `Bad(5)={7,13,19}` is exact over this range.

**Conclusion.** Every load-bearing step checks out: the imported machinery
(Generalized `K_0`-Boundedness / gcd-difference Witness, Legendre Sieve Gap
Bound, Primorial Floor Bound) is already certified from rounds 22/25 and was
spot-re-verified here; the new `p=5`-specific content (table, thresholds,
witness resolutions, residual-band closure, `s^*=5` induction, and the
`Bad(5)` genuineness argument in §7) is correct in substance, with only two
cosmetic index-labeling slips in illustrative prose that do not affect any
conclusion (same class as the round-21/25 precedent for minor non-
load-bearing arithmetic slips — independently re-verified, not blocking).
Both an upper bound (the induction proving periodicity for all
`q∉Bad(5)`) and the required exclusion proof (mechanism-level, not just
numeric, for the three exceptions) are present, matching the "find all"
bar. **Status is correctly `solved`.**

Certified `lemmas/a1-5q-periodicity-theorem.md`.

## 2. `a1-pq-subfamily-theorem` — Verdict: **CHANGES REQUESTED** (Status: partial)

Builder self-reports partial: the Minimal-Window Necessity Conjecture (only
diagonal-band cells, `s_0(j,r)=1` i.e. `j=r`, can ever be genuine `Bad(p)`
members) is not proved, though two new sub-results are.

**Independent re-derivation performed:**

- **Diagonal Characterization Lemma** (`s_0(j,r)=1 ⟺ j=r`): re-derived the
  two-line congruence argument from scratch — correct.
- **First-Risk Theorem** (`n_0(j)` strictly increasing in `s_0(j,r)`, so the
  diagonal band is always the first Case-(b) risk encountered): re-derived
  the inequality algebra (`n_0(j')-n_0(j) = [(s'-s)q-(j'-j)]/p > 2/p`) and
  independently confirmed it holds on an **exhaustive sweep of 282,089**
  `(p,q,j,j')` tuples (`p<60`) with **zero** failures.
- Independently caught and confirmed the builder's own self-caught
  methodology bug (an earlier wrong "exists" legality semantics inflated
  spurious deviations) was real, and reran a from-scratch corrected sweep
  (`p<40`, `q∈(p,p+600)`, full `maxn=3q+50` simulation, 1049 pairs): found
  73 genuine deviations, **all** with `s_0=1` (i.e. `j=r`), and **zero**
  deviations with `r=1` — qualitatively matching the file's larger
  (1763-pair) sweep's claims.
- Verified the file's own worked example (`p=13,q=19`: predicted deviation
  at diagonal band `j=6`, `n=3`) via independent direct greedy simulation:
  exact match (`a_3=266` vs expected `273`, difference `6`).
- Verified the "isolated fragility" counterexample computation
  (`p=13,r=6,j=12,K_0=15`, window `{20,21}`, `gcd(20,15)=5`,
  `gcd(21,15)=3`, both >1): arithmetically correct — this is a genuine
  demonstration that a naive "non-diagonal windows are automatically safe"
  strengthening is false, honestly reported as the reason the conjecture
  resists a quick close.

**Conclusion.** All positive claims made this round check out under
independent re-derivation; no gap or error found in either of the two new
lemmas. The file is honest and precise about what remains open (the
conjecture's core implication — "if the diagonal band succeeds, every
non-diagonal band also succeeds" — is not established, and the file
correctly explains why size/ordering arguments alone cannot close it). No
overclaiming. **Status is correctly `partial`.**

Certified `lemmas/diagonal-characterization-and-first-risk-theorem.md`
(Lemma 1 and Lemma 2 individually, not the conjecture, which remains open).

## 3. `covering-system-construction` — Verdict: **CHANGES REQUESTED** (Status: partial)

Builder self-reports partial: the residual divisor class `d=13` for the
standing `a_1=4807` test seed's rogue pair is fully, unconditionally closed
via a new Finite-Window Literalization Lemma — but this is single-seed, not
a general theorem, so the workspace's overall FAH crux is untouched.

**Independent re-derivation performed:**

- Re-simulated `a_1=4807`'s sequence `a_1,…,a_80` completely from scratch
  (own greedy generator): **exact term-by-term and factorization-by-
  factorization match** with the file's displayed table. This independently
  confirms: `n_A=6` (`a_6=4845=3·5·17·19`, `ρ={3,5,19}=A'`), `n_B=7`
  (`a_7=4862=2·11·13·17`, `ρ={2,11}=B'`), the non-canonical singleton
  `B'`-witness `x_1=72` (`a_{72}=5984=2^5·11·17`, `P(a_{72})\S₀={17}`
  singleton), and — critically — that `A'={3,5,19}` occurs **nowhere** in
  `n=8,…,72` (the Finite-Window Literalization Lemma's finite side
  hypothesis).
- Re-derived the Finite-Window Literalization Lemma's proof from scratch: a
  two-case split (`n>x_1` vs `n_B<n≤x_1`) composing the already-certified
  Singleton-Side FAH Lemma (whose Setup legitimately permits non-canonical
  witnesses, confirmed by reading that lemma's own certified file) with the
  finite vacancy check — valid, no circularity, no gap.
- Independently extended the simulation to **45,000 terms** using a fast
  sieve-based factorization (own script, distinct method): found exactly
  **70** `A'`-occurrences with `n>7`, all with `gcd(a_n,a_7)∈{17,221}`, and
  **none** equal to `13` — exact match with the file's own independent
  cross-check (also 70/70), confirming the residual class `d=13` provably
  never occurs for this seed, consistent with (and now fully explained by)
  the proof.
- Confirmed the cited certified lemmas (Confined-GCD Lemma, Reduced-
  Alphabet Corollary, Singleton-Side FAH, Two-Sided Singleton Witness
  Theorem) are used with matching setups/statements (`S₀={2,3,5,11,19,23}`,
  `F''={13,17}`, `b=221`, `D_bad(17)={13}` all cross-checked against the
  already-certified `reduced-alphabet-corollary.md`).

**Conclusion.** This is a genuine, correctly-scoped, fully-verified
single-seed positive result: literal (zero-exception) Joint FAH now holds
unconditionally for `a_1=4807`'s standing rogue pair. The file is explicit
and honest that this does not establish general FAH/Cofinite FAH for
arbitrary `a_1` (the underlying singleton-witness existence hypothesis is
seed-specific, not derived from a general structural argument) — no
overclaiming. **Status is correctly `partial`.**

Certified `lemmas/finite-window-literalization-lemma.md`.

## Lemma certification summary (this round)

Certified (all independently re-derived/re-verified, no gaps found):
- `lemmas/a1-5q-periodicity-theorem.md` (full theorem, backing the 6th
  APPROVE)
- `lemmas/diagonal-characterization-and-first-risk-theorem.md`
- `lemmas/finite-window-literalization-lemma.md`

No lemma was rejected this round; all three builders' promotable-lemma
proposals passed independent re-verification at full rigor.

## `current.md` update

Updated the reviewer-owned `## Status` section at the top of
`results/imo-2026-06/current.md` with a round-26 summary (5th/6th solved
subfamily: `a_1=5q`, and the round-26 CHANGES-REQUESTED detail for the
other two approaches), matching the file's established format for prior
rounds. Overall workspace Status remains `partial` — no "## Full proof"
section added, since the general problem (H1/FAH, H2) remains open; the
existing "Not present — Status is `partial`" placeholder is unchanged and
still accurate.

## Net round-26 outcome

- **6th APPROVE**: `a1-5q-subfamily-theorem` (Status solved) — a full,
  independently-reverified `a_1=5q` literal-periodicity theorem, `Bad(5)=
  {7,13,19}` proved genuine.
- **2 CHANGES REQUESTED**: `a1-pq-subfamily-theorem` (real new certified
  lemmas, Minimal-Window Necessity Conjecture still open) and
  `covering-system-construction` (single-seed `d=13` closure for `a_1=4807`,
  general FAH still open).
- No RETHINK verdicts this round — all three approaches made genuine,
  correctly-scoped progress with no errors found.
