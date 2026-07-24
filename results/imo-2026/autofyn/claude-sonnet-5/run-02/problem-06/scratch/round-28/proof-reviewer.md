# Proof review — round 28 — imo-2026-06

Reviewed both built approaches independently from scratch: fresh Python/sympy
scripts (not the builders'), own re-derivation of every table/threshold/witness,
own greedy re-simulation. All scripts in `/tmp/round-28/scripts/`.

## 1. `results/imo-2026-06/approaches/a1-11q-subfamily-theorem.md`

**Claim.** For every prime `q>11`, `q∉Bad(11)={13,17,19,31,37,43}`, and
`a_1=11q`: literal `T=1,L=11` periodicity, `a_n=11(q+n-1)` for all `n≥1`.
Status claimed: `solved`.

**Independent verification performed (all from scratch, own scripts):**

1. **90-cell `(s_0,K_0)` table** (`j∈{2,...,10}`, `r∈{1,...,10}`): recomputed
   via a fresh brute-force solve of `s_0·r≡j (mod 11)` — matches the file's
   table exactly, cell for cell.
2. **§5's 76-entry below-threshold `(j,r,q)` list** (`r=2,...,10`, `k=0`):
   recomputed `Q_1(j,r)` from the file's own formula and enumerated all primes
   `q≡r (mod 11)` below threshold — got exactly **76** candidates (86 if `r=1`
   is mistakenly included, confirming the file's careful exclusion of `r=1`
   from this count is correct). For every one of the 76, independently searched
   `i=1,...,n_0` for a `gcd(N,a_i)=1` witness — reproduced **exactly** the
   file's 70 witness indices and the same **6 exceptions**:
   `(2,2,13),(4,4,37),(6,6,17),(8,8,19),(9,9,31),(10,10,43)`, all on the
   diagonal `j=r`, matching `Bad(11)` exactly.
3. **The 6 exceptions are genuine**: independently recomputed each hand-check
   in §6 by direct factorization — every smaller candidate `a_{n_0}+1,...,
   a_{n_0}+(j-1)` is coprime to `a_1=11q` (illegal via `i=1`), and
   `N=a_{n_0}+j=qK_0` shares a nontrivial factor with every one of
   `a_1,...,a_{n_0}` (legal, breaking the induction) — exact digit match with
   the file's worked arithmetic in all 6 cases.
4. **Independent greedy resimulation** (own correct "for all `i`" legality
   rule, not the "exists" bug the workspace has been bitten by before): 778
   primes `q∈(11,6000)`, 40 terms each. **Zero mismatches** for `q∉Bad(11)`;
   for `q∈Bad(11)`, reproduced the exact claimed deviation index/value in
   every case (`a_3=156,204,228` for `q=13,17,19`; `a_4=372` for `q=31`;
   `a_5=444,516` for `q=37,43`).
5. **`k≥1` closure (§7)**: verified the `s*=5` threshold inequality
   `(s+1)!≥21+(11/13)2^{s+1}(s+2)` numerically for `s=5,...,29` — holds
   throughout with wide margin. Independently recomputed all
   `90×14=1260` cell/`k` threshold combinations for the residual band
   `k∈{1,...,14}` and got **exactly the same 29** below-threshold
   `(j,r,k,q)` quadruples, byte-identical to the file's list (including the
   9 `r=1` entries at `gcd(k+1,j)>1`, correctly not skipped). Of these,
   confirmed the same **24 moot** (`q∈Bad(11)`) / **5 non-moot**
   (`q∈{23,41}`) split, and independently verified all 5 non-moot witnesses
   by direct `gcd` computation — exact match on `n_0,n,K,N` and witness
   index in every case.

**No gap found.** Every numeric claim in the file was independently
reconstructed from the raw recursive definitions (Case (a)/(b) split, the
certified `K_0`-Boundedness relation, the certified Legendre Sieve/Primorial
Floor lemmas) rather than copied from the file's own script output, and
matched exactly, with zero discrepancies. The underlying machinery (Steps
0–2, 3, 4/5, 7) is the same certified `p`-uniform template already used and
twice independently APPROVEd for `a1-5q` and `a1-7q` (rounds 26–27); this is
a correct, mechanical, fully-verified instantiation at `p=11`.

**Verdict: APPROVE.** True Status: `solved`. This is the run's **8th
APPROVE**. `current.md` updated with the full result recorded above (see
"## Status" header and the round-28 entry in the history).

No new standalone lemma to certify from this file beyond what's already
certified (the "Promotable lemmas" section documents `p=11`-specific
instantiation data — the 90-cell table and the `s*=5` induction constants —
consistent with the workspace's precedent of not re-certifying per-`p`
instantiation tables as separate lemma files for `a1-5q`/`a1-7q`).

## 2. `results/imo-2026-06/approaches/a1-pq-subfamily-theorem.md`

**Claim (round-28 addition).** A general-`r` closed form
`gcd(N,a_n)=gcd(j,(k+1+c(p,j,r)) mod j)`, and a Uniqueness-of-`r=1` Theorem
(`r=1` is the unique residue with `c(p,j,r)=0` for every band `j`
simultaneously), both proved for every odd prime `p`. Status claimed:
`partial` overall (correctly — file explicitly does not claim this closes
the parent theorem).

**Independent verification performed (all from scratch):**

1. **Lemma 1 (Universal Look-Back Closed Form).** Computed `gcd(N,a_n)`
   directly from the raw definitions (`N=p(q+n-1)+j`, `a_n=p(q+n-1)`, no
   shortcuts) for `p∈{5,7,11,13,17}`, every band `j`, every residue `r`, 400
   primes per residue class, `k=0,...,5` — **19,122 instances**, compared
   against the closed form with `c(p,j,r)=(s_0(j,r)·p⁻¹ mod j) mod j` computed
   independently via `sympy.mod_inverse` — **zero mismatches**.
2. **Lemma 2 (Uniqueness of `r=1`).** For every prime `p∈(3,60)` and every
   `r∈{1,...,p-1}`, independently computed whether `c(p,j,r)=0` for every
   band `j` simultaneously (**15,470 checks**) — found this holds **iff
   `r=1`** in every single tested prime, matching the theorem exactly.
   Independently re-derived the algebraic core of the `⟹` direction
   (`s_0(p-1,r)=p-r⁻¹ mod p`; the only multiple of `p-1` lying in
   `{1,...,p-1}` is `p-1` itself, forcing `ρ=1⟺r=1`) — correct, general, not
   a per-`p`/per-`r` case check as the file claims.

**Both lemmas hold up completely and are correctly, honestly scoped** — the
file explicitly and correctly states (§"What Lemmas 1–2 establish... NOT")
that this is a bookkeeping simplification of which `(j,r,k)` cells are "at
risk," not new closure leverage: the `r≠1` `k=0`-layer still needs the
pre-existing per-`p` sieve machinery, and the `r=1, k≥1, gcd(k+1,j)>1`
residual (round 27's open gap) is untouched. No overclaim found.

**Verdict: CHANGES REQUESTED.** True Status: `partial` (matches the file's
own self-report exactly — no correction needed to the Status line). The new
lemma is certified: `lemmas/universal-look-back-closed-form-and-r1-uniqueness.md`
(already present in the repo, contents match the verified derivation
above — certifying it as-is, no changes required).

## `current.md` update

Updated `results/imo-2026-06/current.md`:
- `## Status` header: added the 8th APPROVE (`a1-11q-subfamily-theorem`)
  summary at the top.
- Inserted a new round-28 history entry (before the round-27 entry) recording
  both verdicts in full detail, matching the file-contract style used for
  rounds 24–27.
- Floor deliverable now stands at **8 fully certified solved sub-family
  theorems**: `2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`; `a_1=3q^3`; `a1-3aq`
  (`a=1,...,5`); `a1-5q`; `a1-7q`; `a1-11q`.
- H1 (FAH)/H2 both remain open for the fully general problem — 22nd
  consecutive plateau round (6-28) on the main crux itself; the `a1-pq`
  general theorem also remains open (as before), now with two more fully
  proved, certified, general-in-`p` sub-lemmas (Universal Look-Back Witness
  Identity from round 27, plus this round's Closed Form + Uniqueness).

## Lemma certification

- `lemmas/universal-look-back-closed-form-and-r1-uniqueness.md` —
  **CERTIFIED** (independently re-derived and verified in full, both Lemma 1
  and Lemma 2, 34,592 combined instance checks, zero mismatches; scope notes
  in the file are accurate and non-overclaiming).

## Ranker

Recorded via `mcp__approach-ranker__record_outcome`:
- `a1-11q-subfamily-theorem`: outcome `verified-milestone` (round 28).
- `a1-pq-subfamily-theorem`: outcome `partial` (round 28).

## Summary verdicts

- `a1-11q-subfamily-theorem`: **APPROVE** (Status: solved) — 8th APPROVE of
  the run, zero gaps found after exhaustive independent reconstruction of
  every numeric claim.
- `a1-pq-subfamily-theorem`: **CHANGES REQUESTED** (Status: partial) — real,
  fully verified, general new content (2 new certified lemmas), but the
  parent theorem's residual gaps (general `r≠1` `k=0` layer; `r=1,k≥1,
  gcd(k+1,j)>1`) remain open, exactly as honestly self-reported.
