# Round 27 proof-reviewer report — imo-2026-06

Reviewed all 3 built slugs independently, from scratch (own Python/sympy
scripts, distinct from every builder's/explorer's/outline-reviewer's), not
by re-reading the write-ups. Full methodology and numbers below.

---

## 1. `a1-7q-subfamily-theorem` — VERDICT: **APPROVE** (Status: solved)

**Claim.** Literal `T=1,L=7` periodicity from `n=1` for `a_1=7q`, every
prime `q≥11` with `q∉Bad(7)={11,13}`.

**Independent re-derivation, everything reproduced exactly:**

- **Greedy simulation ground truth.** Wrote a from-scratch exact-gcd
  greedy generator (using `sympy.gcd`, no shortcuts) and tested every
  prime `q∈[11,3000)` (8 terms each): `a_n=7(q+n-1)` holds for **every**
  prime except `q=11,13`, which deviate exactly as the file describes
  (`a_3=88≠91` for `q=11`; `a_3=104≠105` for `q=13`). Extended a faster
  sieve-based simulator to 60 terms for 9 sample primes (`17,19,23,29,37,
  41,53,101,211`) outside `Bad(7)`: exact literal-periodicity match in
  every term, confirming this isn't just an initial-segment artifact.
- **The 30-cell `(s_0,K_0)` table** (`sympy.mod_inverse`, `p=7`): every
  one of the 30 entries matches the file's table exactly.
- **`Q_1(j,r)` thresholds and the 29-entry below-threshold `k=0` list**:
  recomputed both independently — exact match, all 29 `(j,r,q)` triples.
- **`k=0` witness resolution**: independently searched `i=1,\dots,n_0` for
  a coprime witness in all 29 cases — found exactly the same 2 genuine
  exceptions (`(4,4,11)`, `(6,6,13)`, both `n_0=2`, no witness) and valid
  witnesses at the file's claimed indices for the other 27.
- **`ω(K(k))≤3` claim** for the `k=1..17` residual band: verified by
  direct factorization of all 102 `(K_0,k)` values — confirmed, no
  violation.
- **`s^*=5` sieve-threshold induction** (`(s+1)!≥13+(7/11)2^{s+1}(s+2)`):
  checked numerically for `s=5,\dots,14` — holds in every case, matching
  the claimed base case and (separately re-derivable) inductive step.
- **510 `(j,r,k)`-cell threshold computation → 20 below-threshold
  `(j,r,k,q)` quadruples**: independently recomputed the exact threshold
  set — same 20 quadruples, same 11-moot (`q∈{11,13}`) / 9-non-moot
  split, and independently verified all 9 non-moot witnesses (`N`, `K`,
  and the exact witness index/gcd) match the file's claims exactly.

No gap found anywhere: the base case, the `j=1,7` band, the Case (a)/(b)
split, the `K_0`-boundedness derivation (already certified, general in
`p`), the two sieve lemmas (already certified, `p`-independent), and every
one of the two case-split closures (`k=0`, `k≥1`) are all correct and
complete. `Bad(7)={11,13}` are proved genuine (mechanism-level: the finite
witness window is exhausted with no coprime candidate at `n_0=2` in both
cases) — independently re-derived and matches. This is a complete,
rigorous, self-contained proof, mirroring the certified `a1-5q-subfamily-
theorem` pattern exactly, scaled to `p=7`. **The run's 7th APPROVE.**

No new lemma needed beyond what's already certified
(`generalized-k0-boundedness-and-gcd-difference-witness.md`,
`legendre-sieve-gap-bound.md`, `primorial-floor-bound.md`) — this file is a
pure instantiation, exactly as `a1-5q` was.

---

## 2. `a1-pq-subfamily-theorem` — VERDICT: **CHANGES REQUESTED** (Status: partial — matches builder's own claim)

**Round 27 new content: the Universal Look-Back Witness Identity and its
`r=1` corollary.**

- **The identity** `gcd(N,a_i)=gcd(p(n-i)+j,\,q+i-1)` (any odd prime `p`,
  any `j∈{1,...,p-1}`, any look-back `i≤n`, under `H(n)`): re-derived the
  algebra from scratch (`N-a_i=p(n-i)+j`, then the standard "coprime
  scaling" fact `gcd(b,c)=1⟹gcd(ab,c)=gcd(a,c)` applied with `b=p`,
  `c=p(n-i)+j$ — valid since `gcd(p,j)=1`, `j<p`). Independently checked
  against **66,976** direct `(p,q,j,n,i)` instances (`p∈{5,7,11,13}`,
  hundreds of `q`, all `j`, `n≤7`, all `i≤n`): **zero mismatches**.
  Confirmed consistent (not contradictory) with the already-certified
  Generalized gcd-difference Witness Lemma at `i=n`.
- **The `r=1` corollary** `gcd(N,a_n)=gcd(k+1,j)` at the `k`-th Case-(b)
  risk of band `j`: re-derived the algebra (`q+n-1=(k+1)q+jt`, `t` even
  proved via the odd/odd parity argument, `gcd(q,j)=1` since `q>p>j`
  prime) and independently checked against 30 sampled `(p,q,j,k)`
  instances — exact match in every case. This gives a genuine,
  unconditional, threshold-free closure of the entire `k=0` layer (and
  every `gcd(k+1,j)=1` cell) for `r=1`, for every `p` — real, non-circular
  new content.
- **The two negative sub-claims** (`d=k+1` never a witness; `d=k` not
  identically 1) were also independently spot-checked: `d=k+1` gives
  `gcd=K(k)` exactly in 20 sampled instances (never 1, confirming "never a
  witness"), consistent with the claim.

**What remains open, confirmed genuinely open (not a hidden gap the
builder missed):** the residual `k≥1, gcd(k+1,j)>1` cells for `r=1`, and —
more broadly — the per-`p` `Bad(p)` determination for the general
`a1-pq` theorem. Both honestly reported; Status `partial` is the correct
and accurate self-assessment, not an overclaim. Certified 2 new lemmas
this round (see below); the round-26 material (Diagonal Characterization,
First-Risk Theorem) was already certified in round 26 and is unchanged.

**New lemma certified:** `lemmas/universal-look-back-witness-identity.md`
(the general identity + `r=1` corollary, both independently re-verified as
above).

---

## 3. `covering-system-construction` — VERDICT: **CHANGES REQUESTED** (Status: partial — matches builder's own claim)

**Claim.** The `a_1=11305` standing hard rogue-pair test seed's residual
divisor class `d=103` never occurs, via a relabeled reapplication of the
certified Finite-Window Literalization Lemma (canonical order here is
`n_B=4<n_A=7`, opposite of `4807`'s `n_A=6<n_B=7`).

**Independent re-verification:**

- **Sequence data.** From-scratch greedy simulation of `a_1=11305`
  reproduces the file's first-7-terms table exactly (factorizations,
  `ρ(n)`, canonical witnesses `n_A=7` (`a_7=11330=2·5·11·103`),
  `n_B=4` (`a_4=11319=3·7³·11`)) — including `F'={11,103}` (not
  singleton) and `F''={11}` (singleton), matching the file.
- **`S₀={2,3,5,7,13,17,19,23,29,37,43,101}`, `A'={2,5}`, `B'={3,7}`** match
  the already-certified `two-sided-singleton-witness-theorem.md`'s
  recorded data for this exact seed — not invented ad hoc this round.
- **Relabeling legitimacy — checked the actual proofs, not just the
  Setup wording.** Every lemma in the citation chain (Generalized Bounded
  Witness Lemma, Singleton-Side FAH, Confined-GCD Lemma, Reduced-Alphabet
  Corollary, Finite-Window Literalization Lemma) states "WLOG `n_A<n_B`"
  in its Setup, but on inspection each proof only ever fixes *one*
  reference witness index (of one type) and reasons forward about indices
  of the *other*, disjoint, type — never using which of the two canonical
  witnesses is numerically smaller. So swapping the labels
  (`tilde A':=B'`, `tilde n_A:=n_B=4`; `tilde B':=A'`, `tilde n_B:=n_A=7`)
  to satisfy the cosmetic "`n_A<n_B`" convention is a legitimate
  relabeling, not a hidden gap.
- **Step 1 (free side, `A'`-side via canonical singleton `F''={11}`)**:
  confirmed this is a direct, order-agnostic instance of the Generalized
  Bounded Witness Lemma (fixed witness `m=n_B=4`, no ordering needed).
- **Step 5's exhaustive window-vacancy check**: independently re-simulated
  `a_1=11305` out to `n=103` and scanned every index `8,\dots,103` for a
  `B'={3,7}` occurrence — **found none**, confirming the window `(7,103]`
  (and the larger `(4,103]`) is empty. Independently confirmed the *next*
  `B'`-occurrence is at exactly `n=119`, matching the file's claimed list.
  Confirmed `a_{103}=12100=2²·5²·11²`, `ρ(103)={2,5}=A'=`the required
  `tilde B'` type, singleton complement `{11}` — matching Step 3 exactly.
- **Divisor bookkeeping**: `b=1133=11·103`, `Div(1133)={1,11,103,1133}`,
  `D_bad(11)={103}` — recomputed exactly, matches.
- **Large-scale check.** Fresh 3000-term simulation: 92 `A'`-occurrences
  (`n>4`), 29 `B'`-occurrences (`n>7`), zero violations on either side, and
  `g_n∈{11,1133}` only (never `103`) — consistent with (and independently
  corroborating) the file's own reported 45,000-term check.

No gap found. The relabeling is correctly justified (not asserted), the
window-vacancy check is exhaustive and independently reproduced, and the
divisor bookkeeping is correct. Status `partial` (explicitly single-seed/
single-pair scoped, not a general theorem) is the accurate self-assessment
— both known hard rogue-pair seeds (`4807`, `11305`) now have literal
Joint FAH fully proved, but neither closure supplies any new argument for
why the required singleton-witness existence hypothesis holds for a
general seed. No new lemma was proposed this round (correctly — it is a
reapplication of already-certified machinery, not new content), so nothing
further to certify here.

---

## `current.md` updates

- Updated `## Status` header to reflect SIX certified subfamily theorems
  (added `a_1=7q`, the run's 7th APPROVE).
- Inserted a new round-27 detail block (before the round-26 block) covering
  all 3 slugs' independent re-verification, matching the file's existing
  newest-first structure.
- Certified `lemmas/universal-look-back-witness-identity.md` (new).

## Ranker outcomes recorded

- `a1-7q-subfamily-theorem`: `verified-milestone` (7th APPROVE).
- `a1-pq-subfamily-theorem`: `advanced` (new identity + r=1 k=0 closure
  proved; k≥1 residual with gcd(k+1,j)>1 still open).
- `covering-system-construction`: `advanced` (second/last known hard seed's
  residual class closed; still single-seed).

## Verdict summary

1. `a1-7q-subfamily-theorem` — **APPROVE** (solved, 7th APPROVE of the run)
2. `a1-pq-subfamily-theorem` — **CHANGES REQUESTED** (partial, real new
   content, k≥1 residual for r=1 remains the precise gap)
3. `covering-system-construction` — **CHANGES REQUESTED** (partial, both
   known hard seeds now closed single-seed, no general theorem yet, no
   third seed known to exist)
