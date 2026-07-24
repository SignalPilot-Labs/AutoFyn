## Status
solved for TEN disjoint/overlapping infinite `a_1`-subfamilies (round 30
adds `a_1=19q`, the run's **11th APPROVE**: literal `T=1,L=19` periodicity,
all primes `q>19` outside `Bad(19)={23,29,31,37,43,53,73}`, the 7th
instantiation of the certified `p`-uniform machinery at `p=19`. This review
independently reproduced every numeric claim from scratch with its own
Python/`sympy` scripts, distinct from the builder's: the 306-cell `(s_0,K_0)`
table (exact match, diagonal `s_0=1,K_0=20` throughout, max `K_0=37`); the
exact `260` below-threshold `k=0` `(j,r,q)` candidates (note: the builder's
`Q_1` formula is a *conservative* over-approximation of the tight
sufficient-window criterion — the tight criterion gives only `250`
below-threshold candidates, `10` fewer — but this is harmless, not an error,
since the extra `10` candidates are simply also resolved by explicit witness
search, exactly as the file does; flagged here only for the record) and its
exact **7** genuine `EXC` diagonal exceptions matching `Bad(19)` exactly
(independently re-derived via direct integer `\gcd` search, byte-identical
list `(4,4,23),(5,5,43),(10,10,29),(12,12,31),(15,15,53),(16,16,73),
(18,18,37)`); the `s^*=5` threshold inequality
`(s+1)!\ge37+\tfrac{19}{23}2^{s+1}(s+2)` for `s=5,\dots,30` (holds with wide
margin throughout, own independent numeric check); the `k\ge9` generic
closure logic; the exact **25** residual `k\in\{1,\dots,8\}` below-threshold
quadruples (byte-identical list, independently re-derived via the exact
`q_{\text{thresh}}(j,r,k)` formula) with the exact **21-moot/4-non-moot**
split and all 4 non-moot witnesses (`(8,2,1,59)\to i=3`,
`(12,3,1,41)\to i=3`, `(16,4,1,61)\to i=5`, `(17,9,1,47)\to i=7`, all
re-verified by direct integer `\gcd`); and, most importantly, the new
**Diagonal Window-Parity/Mod-5 Lemma** (§6) — independently re-derived
Steps A–E line by line (the `\pmod q$ and `\pmod{19}` reductions in Step A;
the window-reduction algebra in Step B; the automatic-evenness argument in
Step C; the explicit primality/factorization checks in Steps D–E, e.g.
`45=3^2\cdot5,55=5\cdot11,74=2\cdot37,75=3\cdot5^2,76=2^2\cdot19`, all
confirmed exactly) and confirms it is a genuine, rigorous, non-circular,
uniform proof of all 7 exceptions at once (not 7 ad hoc checks) — no gap
found. **Independent from-scratch greedy resimulation** for every prime
`q\in(19,6000)` (using the literal legality rule): zero mismatches for
`q\notin\mathrm{Bad}(19)`, exact match on `\mathrm{Bad}(19)=\{23,29,31,37,
43,53,73\}` and all 7 deviation indices/values
(`a_3=460,580,620,740` for `q=23,29,31,37`; `a_4=860,1060` for `q=43,53`;
`a_5=1460` for `q=73`). **No gap found anywhere — Verdict: APPROVE, the
run's 11th APPROVE.** Also this round: `fah-counterexample-hunt`'s
round-30 "Prong (a)" headline finding (a claimed six-simultaneous-singleton
near-miss for `a_1=7402395=3\cdot5\cdot7\cdot11\cdot13\cdot17\cdot29` at
indices `114808,160731,185459,219179,344423,482192`) was independently
resimulated with a from-scratch bitmask greedy generator (cross-validated
byte-for-byte both against a naive `\gcd`-based generator on this exact seed
for 2000 terms, and against the file's own already-certified `a_1=385`
`T=5088,L=43890` zero-violation claim) — **the finding does not reproduce
and is factually incorrect as reported**: 4 of the 6 claimed indices match
(off by a constant `+1`, a harmless indexing-convention difference:
`185459\to185460`, `219179\to219180`, `344423\to344424`,
`482192\to482193`), but the other 2 claimed "singleton" types are **not
singletons at all** — independently found to recur multiple times within
the very same window (`\{3,5,7,11,13,17\}` — the "omit-29" type — occurs
**3** times, at indices `83139,249410,415686`, not the claimed `114808`
once; `\{3,5,7,11,13,29\}` — the "omit-17" type — occurs **twice**, at
`141823,425466`, not the claimed `160731` once). The approach's own Status
(`unsolved`) is not overclaimed as a result (no counterexample was ever
claimed proven), but the specific numeric finding needs correction/retraction
next round, not further budget-limited extension — see this round's
proof-reviewer entry below for detail. The two invariant refutations in the
same round (introduction-order permutation; residue-vector-mod-core-prime)
were independently re-verified and are correct as reported (confirmed
exactly, even slightly stronger than stated: `a_n\bmod11` and `a_n\bmod17`
for `a_1=187` hit *every* possible residue, not just "10+", over 2000
terms). Also previously certified: NINE disjoint/overlapping infinite
`a_1`-subfamilies (round 29 adds both `a_1=13q` (the run's **9th APPROVE**:
literal `T=1,L=13`
periodicity, all primes `q>13` outside `Bad(13)={17,19,23,47}`) and
`a_1=17q` (the run's **10th APPROVE**: literal `T=1,L=17` periodicity, all
primes `q>17` outside `Bad(17)={19,23,29,31,37,43,61,67}`), both by direct
instantiation of the certified `p`-uniform machinery at `p=13,17`
respectively, exactly mirroring the `a1-5q`/`a1-7q`/`a1-11q` template. This
review independently reproduced, from scratch, every numeric claim in both
files: the 132-cell (`p=13`) and 240-cell (`p=17`) `(s_0,K_0)` tables; the
112/209 below-threshold `k=0` candidates and all resulting witness/EXC
resolutions (`p=13`: 4 genuine diagonal exceptions plus one moot duplicate
cell `(12,6,19)`, correctly resolved via the true sequence's earlier
deviation at `n=3` under `(6,6,19)`, not double-counted; `p=17`: 8 genuine
diagonal exceptions, confirmed no moot/duplicate pathology); the `s^*=5`
threshold inequalities for both `p`; and the 29/31 `k\ge1` below-threshold
quadruples with their exact 19/10 and 28/3 moot/non-moot splits and all 10+3
non-moot witnesses — every single number reproduced exactly via independent
Python/`sympy` scripts (including two independent from-scratch greedy
resimulations, `q<2000` and `q<2500`), zero gaps found in either file. Also
independently re-verified: a third slug this round,
`bipartite-network-invariant-fah`, proposed a new graph/network-invariant
framing for the main FAH crux (H1) adapted from crux aimo-1000; both
readings of its corrected disambiguation question were confirmed to
genuinely collapse into already-certified-insufficient content (the round-2
Generalized Bounded Witness Lemma, already known non-cofinite) or the
already-open H2 termination criterion, with the aimo-1000 crux citation
independently checked against the crux database and confirmed accurate — an
honest, complete negative result (RETHINK, Status `unsolved`), correctly not
overclaimed as `solved` or `partial`. See round-29 entry below. Also
previously certified: SEVEN disjoint/overlapping infinite `a_1`-subfamilies
(round 28 added `a_1=11q`, the **8th APPROVE**: `q` prime, `q>11`,
`q∉Bad(11)={13,17,19,31,37,43}`, literal `T=1,L=11` periodicity from `n=1`,
proved by instantiating the certified `p`-uniform machinery
(Generalized `K_0`-Boundedness, gcd-difference Witness Lemma, Legendre
Sieve Gap Bound, Primorial Floor Bound, and the round-27 Universal
Look-Back Witness Identity's `r=1` corollary) at `p=11`, exactly mirroring
the certified `a1-5q`/`a1-7q` closures. This review independently
reproduced from scratch: the 90-cell `(s_0,K_0)` table; all 76
below-threshold `k=0` candidates and their 70 witnesses plus the exact 6
genuine exceptions (matching a from-scratch greedy resimulation over 778
primes `q<6000`, exact deviation indices/values `a_3=156,204,228`
(`q=13,17,19`), `a_4=372` (`q=31`), `a_5=444,516` (`q=37,43`)); the `s*=5`
sieve-threshold inequality numerically for `s=5..29`; all 29 `k≥1`
below-threshold `(j,r,k,q)` quadruples, the 24-moot/5-non-moot split, and
all 5 non-moot witnesses — every single number reproduced exactly, zero
gaps found. See round-28 entry below.) Also seven prior subfamilies stand:
`2|a_1`;
`a_1=p^k`; `a_1=3q` (`q` prime, `q≥7,q≠5`); `a_1=3^a q` for `a∈{1,...,5}`
and prime `q≥7` outside an explicit tiny `a`-dependent exceptional set
(round 24's 4th APPROVE); `a_1=5q` (`q` prime, `q≥7`,
`q∉Bad(5)={7,13,19}`) — round 26's **6th APPROVE**, fully independently
re-verified (every table, threshold, and witness re-derived from scratch;
see round-26 entry below and `lemmas/a1-5q-periodicity-theorem.md`); and,
as of round 27, `a_1=7q` (`q` prime, `q≥11`, `q∉Bad(7)={11,13}`) — round
27's **7th APPROVE**, fully independently re-verified (every one of the
30-cell `(j,r)` table, the 29-entry `k=0` below-threshold list, both
genuine exceptions, the 510 `k≥1` threshold combinations reducing to 20
below-threshold quadruples, the 11-moot/9-non-moot split, and all 9
witnesses, re-derived from scratch with independent Python/`sympy`
scripts; plus a from-scratch greedy simulation confirming `q=11,13` are
the *only* deviations among all primes `q<3000`, and full 60-term literal
periodicity for 9 sample primes outside `Bad(7)`; see round-27 entry below
and `results/imo-2026-06/approaches/a1-7q-subfamily-theorem.md`).
Additionally, `a_1=3q^2` (round 24) and `a_1=3q^3` (round 25) are each
fully proved, certified standalone theorems (extending the `a_1=3q` family
along the exponent axis to a third value of `m`), though the approach
housing both (`a1-3qk-subfamily-theorem`) remains `partial` since its own
stated target is the general-`m` family and `m≥4` is still open. Round 25
also fully proved (and independently certified) a `p`-uniform symbolic
reduction for the `a_1=pq` family (any odd prime `p`) — the machinery
(Generalized `K_0`-Boundedness, gcd-difference Witness Lemma) is proved
for every `p`, and round 26 instantiated it at `p=5` to close `Bad(5)`
completely (see above); `p≥7` remains open pending a per-`p` finite
computation, and round 26's attempt to prove a general "Minimal-Window
Necessity Conjecture" that would shortcut this per-`p` work (only
diagonal-band cells can ever be genuine exceptions) made real progress
(two new certified lemmas: Diagonal Characterization `s_0=1⟺j=r`, and the
First-Risk Theorem) but did not close the conjecture — a genuine, precisely
located open gap remains (an isolated non-diagonal-band window-failure
instance exists in principle; whether it can ever be the FIRST deviation
for some `(p,q)` is unresolved). So `a1-pq-subfamily-theorem` stays
`partial`. Round 26 also fully closed (independently re-verified) the
single residual divisor class `d=13` for the standing `a_1=4807` test seed
in `covering-system-construction` via a new certified **Finite-Window
Literalization Lemma** — a genuine, complete, single-seed positive result
(literal Joint FAH now holds unconditionally for this one rogue pair), but
NOT a general FAH/Cofinite-FAH theorem, so that approach also stays
`partial`. Round 27 closed the analogous second and last standing hard
seed's residual class (`a_1=11305`'s `d=103`) via a correctly-justified
relabeled reapplication of the same certified Lemma (independently
re-verified in full, including the canonical-order swap `n_B<n_A`, opposite
of `4807`'s `n_A<n_B`) — both known hard rogue-pair seeds now have literal
Joint FAH fully proved, but this remains single-seed/single-pair, not a
general theorem, so `covering-system-construction` also stays `partial`.
Round 27 also proved a new, fully verified **Universal Look-Back Witness
Identity** (`a1-pq-subfamily-theorem`, independently checked against
~67,000 direct instances) giving an unconditional, threshold-free closure
of the entire `k=0` layer (and every `(j,k)` with `gcd(k+1,j)=1`) for the
`r=1` residue class of the general `a1-pq` machinery — genuine new content,
but the `k≥1,gcd(k+1,j)>1` residual remains open, so that approach also
stays `partial`. Overall workspace Status remains `partial` (H1/FAH and H2
remain open for the fully general problem; see below for full round-27,
round-26, and all prior rounds' detail).

partial overall, but the run's **9th AND 10th APPROVEs** (round 29: three
slugs built, all independently re-verified by this review from scratch —
own fresh Python/`sympy` scripts distinct from every builder's, own
re-derivation of every table/threshold/witness/quadruple, own greedy
re-simulations. **(1) `a1-13q-subfamily-theorem` (new) — APPROVE, Status
`solved`, the run's 9th APPROVE.** Independently reproduced byte-for-byte:
the `p=13` 132-cell `(s_0,K_0)` table; the 112 below-threshold `k=0`
`(j,r,q)` candidates (via a fresh `Q_1` threshold computation); all 107
witness resolutions plus the exact 5 no-witness `EXC` cells
`(4,4,17),(6,6,19),(8,8,47),(10,10,23),(12,6,19)` — matching the file's
claim that 4 are genuine (matching `Bad(13)={17,19,23,47}` exactly) and the
5th, `(12,6,19)`, is a moot duplicate for `q=19` (both cells share residue
`r=6`); independently re-verified the moot-cell argument itself via a fresh
greedy resimulation of `a_1=247=13\cdot19`, confirming `a_3=266` (the
genuine deviation via `(6,6,19)` at `n_0=2`), not `273`, so `H(3)` (which the
`(12,6)` cell's analysis presupposes) never holds for the real sequence —
this is a correct, non-circular resolution, not hand-waving, and this
review confirms no other prime among the 112 candidates has a second `EXC`
cell. Independently re-derived the `s^*=5` threshold inequality
`(s+1)!\ge25+\tfrac{13}{17}2^{s+1}(s+2)` for `s=5,\ldots,29` (holds
throughout); independently recomputed all `132\times11` cell/`k`
combinations for the residual band `k\in\{1,\ldots,11\}`, finding the same
**29** below-threshold `(j,r,k,q)` quadruples (byte-identical list),
confirmed the same **19-moot/10-non-moot** split (`q\in\{29,31,37,41,43,53,
59,61\}`), and independently verified all 10 non-moot witnesses by direct
integer `\gcd` computation — exact match on every `n,K,N,i` value.
**Independent from-scratch greedy resimulation** for every prime
`q\in(13,2000)`: zero mismatches for `q\notin Bad(13)`, and the exact
claimed deviation index/value for each of `q\in\{17,19,23,47\}`
(`a_3=238,266,322` and `a_5=658`). **No gap found anywhere.** **Verdict:
APPROVE — the run's 9th APPROVE.** **(2) `a1-17q-subfamily-theorem` (new)
— APPROVE, Status `solved`, the run's 10th APPROVE.** Independently
reproduced byte-for-byte: the `p=17` 240-cell table; the 209 below-threshold
`k=0` candidates; all 201 witness resolutions plus the exact 8 no-witness
`EXC` cells, all diagonal (`j=r`), matching `Bad(17)=\{19,23,29,31,37,43,61,
67\}$ exactly, with **no** moot/duplicate pathology (independently
confirmed: distinct from `a1-13q`, every below-threshold band for each of
the 8 exceptional primes resolves with an honest witness, exactly as the
file claims). Independently re-derived the `s^*=5` threshold inequality
`(s+1)!\ge33+\tfrac{17}{19}2^{s+1}(s+2)` for `s=5,\ldots,29`; independently
recomputed all `240\times10` cell/`k` combinations for `k\in\{1,\ldots,10\}`,
finding the same **31** below-threshold quadruples, the same **28-moot/
3-non-moot** split (`q\in\{41,47,53\}`), and independently verified all 3
non-moot witnesses by direct `\gcd` computation — exact match.
**Independent from-scratch greedy resimulation** for every prime
`q\in(17,2500)`: zero mismatches for `q\notin Bad(17)`, and the exact
claimed deviation index/value for each of the 8 exceptions. **No gap found
anywhere.** **Verdict: APPROVE — the run's 10th APPROVE.** **(3)
`bipartite-network-invariant-fah` (new) — RETHINK confirmed, Status
`unsolved`.** Independently re-verified Propositions A–D: Proposition A/B
(Reading α, fixed core) is confirmed a genuine, correct one-line corollary
of the round-2-certified Generalized Bounded Witness Lemma, whose own
Status line independently confirmed to say "Does NOT by itself close gap
(†)" (checked directly in `lemmas/generalized-bounded-witness-lemma.md`) —
so Reading α supplies zero leverage beyond already-known-insufficient
content. Proposition C (Reading β, growing core) independently confirmed to
be, definitionally, the same object as the already-open H2 Termination
Criterion Lemma's `(N(S_k))_k` boundedness question — the "repair" operator
`S_k\to S_k\cup\{q_k\}` is verified to be exactly the certified
Self-Absorbing Core Theorem's operator, not a new one. Proposition D's crux
citation (the aimo-1000 "deterministic toggle rule" mechanism) was
independently checked verbatim against `past_crux_moves_database.json`
(`problem_id=aimo-1000`) and confirmed accurate — the greedy-gcd recursion's
only tool (existential Free Facts / Generalized Bounded Witness Lemma) is
correctly diagnosed as structurally weaker than a deterministic,
simultaneous toggle, with the round-7 Witness Discontinuity Obstruction
(`a_1=175`) serving as a genuine, correctly-cited counterexample to any
"obviously bounded" shortcut for Reading β. **No gap found in this negative
result; it is honest, complete, and correctly scoped (not a hasty
give-up).** **Verdict: RETHINK — Status `unsolved`, correctly self-reported.**
The certified Bipartite-Network Reduction Collapse meta-lemma is a
toolkit-independent negative result (parallel in kind to the certified
Same-Type Free Facts Vacuity / Density-Argument Vacuity Corollary
precedents) and is certified this round
(`lemmas/bipartite-network-reduction-collapse.md`). **Overall workspace
Status remains `partial`** (H1/FAH — 23rd consecutive plateau round, 6-29 —
and H2 both remain open for the fully general problem); the run's floor
deliverable now stands at **10 fully certified solved sub-family theorems**
(`2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`; `a_1=3q^3`; `a1-3aq` (`a=1,\ldots,
5`); `a1-5q`; `a1-7q`; `a1-11q`; `a1-13q`; `a1-17q` = 10 total APPROVEs
across families), plus the gap-free Master
Conditional Theorem reducing full generality to H1 (FAH) + H2
(absorption-chain termination). 32nd confirmed-dead FAH mechanism variant
(`bipartite-network-invariant-fah`) added to the graveyard.)

partial overall, but the run's **8th APPROVE** (round 28: two slugs built,
both independently re-verified by this review from scratch — own fresh
Python/`sympy` scripts distinct from every builder's, own re-derivation of
every table/threshold/witness/quadruple, own greedy re-simulation at scale.
**(1) `a1-11q-subfamily-theorem` (new) — APPROVE, Status `solved`.**
Independently reproduced, byte-for-byte: the `p=11` 90-cell `(s_0,K_0)`
table (via a fresh `mod_inverse`-based script, exact match on all 90
cells); the `Q_1(j,r)` sufficient-window thresholds and the resulting
76-entry below-threshold `(j,r,q)` candidate list for `r=2,...,10`
(confirmed exactly 76 once `r=1` is correctly excluded, matching §4/§5's
split); all 70 `k=0` witness `gcd` computations plus the exact 6 genuine
exceptions `(j,r,q)=(2,2,13),(6,6,17),(8,8,19),(9,9,31),(4,4,37),(10,10,43)`
— matching `Bad(11)={13,17,19,31,37,43}` exactly; independently verified
each of the 6 exceptions' hand-check (every smaller candidate illegal via
`i=1`, the `N=qK_0` value legal against every prior term) by direct
factorization, exact match with the file's worked computations digit for
digit. **Independent from-scratch greedy resimulation** (correct "for all
`i`" legality, not an "exists" bug) for every prime `q∈(11,6000)` (778
primes), 40 terms each: **zero mismatches** for `q∉Bad(11)`, and for every
`q∈Bad(11)` the exact claimed deviation index and value
(`q=13:n=3,a_3=156`; `q=17:n=3,a_3=204`; `q=19:n=3,a_3=228`; `q=31:n=4,
a_4=372`; `q=37:n=5,a_5=444`; `q=43:n=5,a_5=516`) reproduced exactly.
**Independently re-derived the `k≥1` closure**: the `s*=5` threshold
inequality `(s+1)!≥21+(11/13)2^{s+1}(s+2)` verified numerically for
`s=5,...,29` (holds throughout, wide margin); independently recomputed all
`90×14=1260` cell/`k` threshold combinations for the residual band
`k∈{1,...,14}`, finding **exactly the same 29** below-threshold
`(j,r,k,q)` quadruples as the file (byte-identical list, same order); of
these, confirmed the same **24 moot** (`q∈Bad(11)`) and **5 non-moot**
(`q∈{23,41}`) split, and independently verified all 5 non-moot witnesses
(`(2,1,1,23):i=3`; `(4,1,1,23):i=3`; `(8,1,1,23):i=7`; `(9,1,2,23):i=3`;
`(9,8,1,41):i=3`) by direct integer `gcd` computation — exact match with
the file. **No gap found anywhere** — every numeric claim in the file
(table, 76-candidate list, 6 exceptions, 29 quadruples, 24/5 split, 5
witnesses, deviation values) was independently reconstructed from the raw
definitions (not read off the file) and matched exactly. This is a
complete, correct, self-contained instantiation of the certified
`p`-uniform machinery at `p=11`, exactly mirroring the certified `a1-5q`/
`a1-7q` template. **Verdict: APPROVE — the run's 8th APPROVE.** No new
lemma promotion needed beyond what's already certified (the file's
"Promotable lemmas" section documents `p=11`-specific instantiation data,
not new general machinery — correctly not re-submitted as a separate
lemma file, consistent with the `a1-5q`/`a1-7q` precedent of not
re-certifying per-`p` instantiation tables as standalone lemmas). **(2)
`a1-pq-subfamily-theorem` (revise, Universal Look-Back Closed Form for
general `r` + Uniqueness-of-`r=1` Theorem) — CHANGES REQUESTED, Status
stays `partial` (correctly self-reported).** Independently re-derived and
verified **Lemma 1 (Universal Look-Back Closed Form)** from the raw
definition (not the file's derivation): computed `gcd(N,a_n)` directly from
first principles (`N=p(q+n-1)+j`, `a_n=p(q+n-1)`) for `p∈{5,7,11,13,17}`,
every band `j`, every residue `r`, 400 primes per class, `k=0,...,5`
(19,122 instances) and compared against the closed form
`gcd(j,(k+1+c(p,j,r)) mod j)` with `c(p,j,r)=(s_0(j,r)·p⁻¹ mod j) mod j` —
**zero mismatches**. Independently re-derived and verified **Lemma 2
(Uniqueness of `r=1`)**: for every prime `p∈(3,60)` and every
`r∈{1,...,p-1}`, computed whether `c(p,j,r)=0` for every band `j`
simultaneously, from scratch — found this holds **iff `r=1`**, in every one
of the tested primes (15,470 checks), matching the theorem's universal
claim exactly; independently re-derived the algebraic core of the `⟹`
direction (`s_0(p-1,r)=p-r⁻¹ mod p`, and the only multiple of `p-1` in
`{1,...,p-1}` is `p-1` itself, forcing `r=1`) and confirmed it correct and
general (not a per-`p` spot-check). **Both lemmas are correctly proved,
general, and reusable — certified this round**
(`lemmas/universal-look-back-closed-form-and-r1-uniqueness.md`). However,
as the file itself honestly states, this is a bookkeeping simplification of
which `(j,r,k)` cells are "at risk," not new closure leverage: the
`k≥1,gcd(k+1,j)>1` residual for `r=1` (round 27's open gap) and the general
`r≠1` `k=0`-layer closure (which still needs the pre-existing per-`p` sieve
machinery) remain untouched. **Verdict: CHANGES REQUESTED** (Status
`partial`, correctly self-reported — genuine, fully general new content,
but the parent theorem's residual gaps are unaffected). 1 new lemma
certified this round
(`universal-look-back-closed-form-and-r1-uniqueness.md`). **Overall
workspace Status remains `partial`** (H1/FAH — 22nd consecutive plateau
round, 6-28 — and H2 both remain open for the fully general problem); the
run's floor deliverable now stands at **8 fully certified solved
sub-family theorems** (`2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`; `a_1=3q^3`;
`a1-3aq` (`a=1,...,5`); `a1-5q`; `a1-7q`; `a1-11q` = 8 total APPROVEs across
families), plus the gap-free Master Conditional Theorem reducing full
generality to H1 (FAH) + H2 (absorption-chain termination).)

partial (round 27: three slugs built, all independently re-verified by
this review from scratch — own fresh Python/`sympy` scripts distinct from
every builder's, own re-derivation of every table/threshold/witness, own
greedy re-simulations at scale (3000+ primes `q<3000` for `a1-7q`; ~67,000
direct algebraic instances for the Universal Look-Back Witness Identity;
3000+-term full simulation and independent window-vacancy re-scan for
`a_1=11305`'s `d=103` closure). **(1) `a1-7q-subfamily-theorem` (new) —
the run's 7th APPROVE.** Fully independently reproduced: the `p=7`
instantiation's 30-cell `(s_0,K_0)` table (via `sympy.mod_inverse`); the
`Q_1(j,r)` threshold table and its 29-entry below-threshold `(j,r,q)` list,
exact match; every `k=0` witness `gcd` computation, confirming the same 2
genuine exceptions (`q=11,13`, both at `n_0=2`) and valid witnesses for the
other 27; the `s^*=5` sieve-threshold inequality
`(s+1)!≥13+(7/11)2^{s+1}(s+2)` numerically for `s=5..14`; the `ω(K(k))≤3`
claim across all 102 `(K_0,k)` pairs in the `k=1..17` residual band; the
510 `(j,r,k)`-cell threshold computations reducing to the same 20
below-threshold `(j,r,k,q)` quadruples; the 11-moot(`q∈{11,13}`)/9-non-moot
split and all 9 non-moot witnesses. Fresh greedy re-simulation for every
prime `q∈[11,3000)` (8 terms) confirms `q=11,13` are the *only* deviations,
matching the mechanism exactly (`a_3=88≠91` and `a_3=104≠105`); extended
60-term re-simulation for 9 sample primes outside `Bad(7)` shows exact
literal-periodicity match throughout. No gaps found; this is a complete,
correct, self-contained proof mirroring the certified `a1-5q` pattern
exactly, scaled to `p=7`. **(2) `a1-pq-subfamily-theorem` (advance,
Status stays `partial`).** The new **Universal Look-Back Witness
Identity** (`gcd(N,a_i)=gcd(p(n-i)+j,\,q+i-1)`) is a correct, elementary,
fully general algebraic identity — independently re-verified against
66,976 direct `(p,q,j,n,i)` instances with zero mismatches, and its `d=k+1`
"never a witness" sub-claim independently re-verified against 20 further
sampled instances (`gcd` always equals `K(k)` exactly, as claimed). The
`r=1` corollary (`gcd(N,a_n)=gcd(k+1,j)` at the `k`-th Case-(b) risk,
giving unconditional, threshold-free `k=0` closure and closure of every
`gcd(k+1,j)=1` cell, for every `p`, every band, every admissible `q≡1
\pmod p`) is independently re-verified against 30 sampled `(p,q,j,k)`
instances with exact agreement. Genuinely new, non-circular, correctly
scoped: the residual `k≥1,gcd(k+1,j)>1` cells are honestly left open (the
file's own two further candidate witness attempts, `d=k` and `d=k+1`, are
independently confirmed to fail/not-generalize as claimed). Two new
lemmas certified this round (see below). **(3)
`covering-system-construction` (advance, Status stays `partial`).** The
`a_1=11305` residual class `d=103` closure (Step 4i) is independently
re-verified in full: the seed's first-7-terms table and extended-persistent
core `S₀={2,3,5,7,13,17,19,23,29,37,43,101}` reproduced exactly from a
from-scratch greedy simulation; the canonical-order swap (`n_B=4<n_A=7`,
opposite of `4807`'s `n_A<n_B`) and the resulting relabeling
(`tilde A':=B'`, `tilde B':=A'`) confirmed LEGITIMATE by checking that
every cited lemma in the chain (Generalized Bounded Witness Lemma,
Singleton-Side FAH, Confined-GCD Lemma, Reduced-Alphabet Corollary, Finite-
Window Literalization Lemma) is, on inspection of its own proof text (not
just its Setup's cosmetic "WLOG `n_A<n_B`" phrasing), actually order-
agnostic — each proof only ever fixes *a* reference witness index of one
type and reasons about indices strictly after it of the other (disjoint)
type, never using which of the two canonical witnesses is numerically
smaller; the exhaustive window-vacancy check (`n=8,...,103`, no `B'={3,7}`
occurrence) independently re-scanned and confirmed empty, with the next
`B'`-occurrence found at exactly `n=119` as claimed; the divisor bookkeeping
(`b=1133=11·103`, `Div(1133)={1,11,103,1133}`, `D_bad(11)={103}`)
independently recomputed exactly; and a fresh 3000-term simulation found
zero violations on both sides (92 `A'`-occurrences, 29 `B'`-occurrences,
`g_n∈{11,1133}` only, never `103`), consistent with the file's own
45,000-term check. No new lemma content this round (correctly, honestly
noted by the builder — this is a reapplication of an already-certified
lemma, not new machinery); both of the workspace's two known hard
rogue-pair seeds now have literal Joint FAH fully proved, but this remains
explicitly single-seed/single-pair scoped, not a general theorem.

## ROUND 30 — 11th APPROVE (`a1-19q`, 7th `p`-instantiation, new Diagonal
Window-Parity/Mod-5 Lemma verified); `fah-counterexample-hunt`'s round-30
"six-singleton near-miss" finding independently re-simulated and found
factually incorrect (2 of 6 claimed types are not singletons — they recur)

**`a1-19q-subfamily-theorem` — APPROVE, Status `solved`, the run's 11th
APPROVE.** Full independent re-verification detail is in the Status header
above. Summary: every one of the 306-cell table, the 260 below-threshold
`k=0` candidates (noting the builder's `Q_1` threshold is a harmless
conservative over-approximation of the tight `250`-candidate criterion —
not an error), the 7 genuine diagonal exceptions exactly matching
`Bad(19)`, the `s^*=5` threshold induction, the `k\ge9` generic closure, the
25 residual `k\in\{1,\dots,8\}` quadruples (21 moot/4 non-moot) and all 4
non-moot witnesses, and — scrutinized hardest, per this round's dispatch —
the new **Diagonal Window-Parity/Mod-5 Lemma** (§6, Steps A–E) was
independently re-derived from scratch and found rigorous and non-circular:
Step A's `\pmod q`/`\pmod{19}` reduction is a direct, correct instantiation
of the general Case-(a) argument from §2; Step B's window-legality
equivalence is a direct, correct instantiation of the general Case-(b)
reduction from §2 at `k=0`, diagonal `K_0=20`; Step C's "window length 1 is
automatic since `q` is odd" is a one-line, fully general, unconditional
fact; Steps D–E's explicit primality/factorization checks
(`23,29,31,37,43,53,73` prime; `45=3^2\cdot5,55=5\cdot11` div. by `5`;
`74=2\cdot37,76=2^2\cdot19` even, `75=3\cdot5^2` div. by `5`) were all
independently confirmed exactly, and Step E's exhaustiveness claim (no
other residue class produces an 8th exception) was independently confirmed
by a full from-scratch witness search over all 260 candidates, finding
exactly the same 7 exceptions and no more. **No gap found. Verdict:
APPROVE.**

**`fah-counterexample-hunt` — Status `unsolved` correctly self-reported,
but this round's headline "Prong (a)" finding needs explicit correction.**
The two invariant refutations (Prong (b): introduction-order permutation;
residue-vector-mod-core-prime) were independently re-simulated and are
CONFIRMED CORRECT — for `a_1=4807`, primes `73,127` are indeed introduced
(at greedy-sequence indices 5,6 in first-new-prime order) strictly before
`5,7,17,13` (indices 7,8,9,10); for `a_1=187`, `a_n\bmod11` and
`a_n\bmod17` hit *every* possible residue class (11 and 17 respectively)
over the first 2000 terms, even stronger than the file's "10+ distinct
values" claim. These refutations stand as correct, real negative work.

However, the round's headline finding — a claimed six-simultaneous-
singleton near-miss for `a_1=7402395=3\cdot5\cdot7\cdot11\cdot13\cdot17
\cdot29` at indices `114808,160731,185459,219179,344423,482192` — was
independently re-simulated with a from-scratch bitmask-based greedy
generator (methodology cross-validated two ways: (1) byte-for-byte
agreement with a fully independent naive `\gcd`-based generator on this
exact seed for its first 2000 terms; (2) exact reproduction, with zero
violations, of this same approach file's own already-verified `a_1=385`,
`T=5088,L=43890` periodicity claim) to `n=520{,}000`, and **the finding
does not reproduce as stated**:
- 4 of the 6 claimed indices match up to a constant `+1` offset (a harmless
  indexing-convention difference, e.g. counting from term 0 vs term 1):
  `185459\to185460`, `219179\to219180`, `344423\to344424`,
  `482192\to482193` — these 4 are genuinely singleton (occur exactly once)
  through `n=520{,}000`, consistent with the claim once the offset is
  accounted for.
- **The other 2 of the 6 are simply wrong.** The claimed index `114808`
  (evidently meant to be the type `\{3,5,7,11,13,17\}`, i.e. "omit 29") does
  not correspond to any real occurrence of that type at that index; the true
  first occurrence is at `n=83139`, and — critically — **this type is not a
  singleton at all**: it recurs at `n=249410` and again at `n=415686` (3
  occurrences total through `n=520{,}000`), directly within the very same
  window the builder used. Likewise the claimed index `160731` (meant to be
  `\{3,5,7,11,13,29\}`, "omit 17") does not match any real occurrence; the
  true occurrences are at `n=141823` and `n=425466` (2 occurrences, not 1).
- The 7th possible "omit-one" type, `\{5,7,11,13,17,29\}` ("omit 3"), never
  occurs at all through `n=520{,}000` in the independent resimulation
  (consistent with the file's own count of only "six" such types, since a
  7th would exist combinatorially but apparently hasn't appeared yet).

**Conclusion: the "six simultaneous singleton" characterization is false as
stated — at most 4 of the 6 claimed types are genuine singletons in this
window, and the specific indices for the other 2 do not correspond to real
sequence data.** This is not merely "inconclusive due to compute budget" (as
the file frames it) but an outright numerical error in this round's
reported near-miss data, independent of any further budget question. The
file's Status (`unsolved`) is not itself an overclaim — no counterexample
was asserted proven — but the specific finding must be corrected/retracted,
not carried forward as "the sharpest, largest-scale near-miss this
workspace has produced," and should not be handed to a future round as a
ready-to-run target in its current (incorrect) form. **Verdict: Status
stays `unsolved`; this round's Prong (a) finding is not certified and is
flagged for correction. No lemma certified (none was proposed as a lemma;
matches the "diagnostic, not portable" precedent, and in any case the
headline diagnostic itself is now known to be wrong).**

## Round 27 lemma certifications

- **`lemmas/universal-look-back-witness-identity.md`** (new, certified this
  round): the general identity `gcd(N,a_i)=gcd(p(n-i)+j,\,q+i-1)` (any odd
  prime `p`, any `j∈{1,...,p-1}`, any `1≤i≤n` under the standing induction
  hypothesis `H(n)`), plus its `r=1` corollary giving unconditional `k=0`
  (and every `gcd(k+1,j)=1`) closure. Both independently re-verified (see
  above); certified as reusable, general-purpose content for the `a1-pq`
  machinery.

partial (round 26: three slugs built, all independently re-verified by
this review from scratch — own fresh Python/`sympy` scripts distinct from
every builder's, own re-derivation of every table/threshold/witness, own
greedy re-simulations at scale (up to 45,000 terms for the `a_1=4807`
extended check, 282,089 tested pairs for the First-Risk Theorem, 1049–1661
`(p,q)` pairs for the Minimal-Window sweep). **(1)
`a1-5q-subfamily-theorem` (new) — the run's 6th APPROVE.** Fully
independently reproduced: the `p=5` instantiation's 12-cell `(s_0,K_0)`
table (via `pow(r,-1,5)`); the `Q_1(j,r)` threshold table and its 12
below-threshold prime lists, exact match; every `k=0` witness `gcd`
computation, confirming the same 3 genuine exceptions (`q=7,13,19`) and
valid witnesses for the other 9 (one witness-index label in the write-up's
prose is off by one for `(2,1,11)` — cosmetic only, a genuine witness at
the correct index does exist, independently confirmed; similarly the
"i=1,2,3" no-witness checks for the 3 exceptions omit an explicit check of
`i=n_0` in the prose, but this is independently confirmed correct by a
full-range check); the `s^*=5` sieve-threshold inequality
`(s+1)!≥9+(5/7)2^{s+1}(s+2)` numerically for `s=5..14`; the 13 flagged
`(j,r,k)` combinations in the `k≥1` residual band via an independently
re-derived exact sieve bound — exact match; the moot/non-moot
classification (8 moot, all `q∈{7,13,19}`; 5 non-moot, `q∈{11,17}`) and all
5 non-moot witnesses. Full independent greedy re-simulation for every
prime `q∈[7,2000)` (60 terms each): matches the closed form in every case
except `q=7,13,19`, deviating exactly at `n=3,4,5` with the exact values
claimed. **No load-bearing gap found anywhere** — the two identified slips
are cosmetic index-labeling issues in illustrative prose, independently
confirmed not to change any conclusion. **Verdict: APPROVE (Status
`solved`).** Certified `lemmas/a1-5q-periodicity-theorem.md`. **(2)
`a1-pq-subfamily-theorem` (revise, Minimal-Window Necessity Conjecture
attempt) — real progress, conjecture still open.** Independently verified
the two new fully-proved sub-results: the Diagonal Characterization Lemma
(`s_0(j,r)=1⟺j=r`, a two-line congruence argument) and the First-Risk
Theorem (`n_0(j)` strictly increasing in `s_0(j,r)`, hence the diagonal
band is always tested first) — reproduced both from scratch, the latter
exhaustively on 282,089 `(p,q,j,j')` tuples with zero failures. Verified
the builder's self-caught methodology correction (an earlier, wrong
"exists" legality semantics inflated spurious deviations) is real and the
corrected large sweep's headline numbers are directionally reproduced (own
independent 1049–1661-pair sweeps: zero mismatches to "genuine deviation
⟹ `s_0=1`", zero `r=1` deviations, matching the qualitative claims). Also
independently confirmed the file's own worked example (`p=13,q=19`:
diagonal band `j=6` deviates first at `n=3`) via direct greedy simulation,
exact match, and independently confirmed the isolated-fragility
counterexample computation (`p=13,r=6,j=12,K_0=15`, window `{20,21}` both
non-coprime to 15) is arithmetically correct. **The conjecture itself
(non-diagonal bands are always safe whenever the diagonal succeeds) is
genuinely not proved** — this is honestly and precisely reported, not
overclaimed. **Verdict: CHANGES REQUESTED** (Status `partial`, correctly
self-reported; real new certified content, but the round's stated stretch
target is not achieved). Certified
`lemmas/diagonal-characterization-and-first-risk-theorem.md`. **(3)
`covering-system-construction` (revise, Step 4h) — single-seed `d=13`
closure for `a_1=4807`.** Independently re-simulated the full sequence
`a_1,…,a_80` from scratch — exact term-by-term and factorization-by-
factorization match with the file's displayed table, confirming the
non-canonical singleton `B'`-witness `x_1=72` (`a_{72}=5984=2^5·11·17`)
and the finite-window vacancy (no `A'`-occurrence in `(7,72]`). Verified
the new Finite-Window Literalization Lemma's proof is a valid, non-
circular two-case composition of the already-certified Singleton-Side FAH
Lemma (whose Setup legitimately allows non-canonical witnesses) with a
finite, directly-checkable side condition. Independently extended the
simulation to 45,000 terms (fast sieve-based factorization): found exactly
70 `A'`-occurrences with `n>7`, all with `gcd(a_n,a_7)∈{17,221}`, none
equal to `13` — exact match with the file's cross-check, confirming the
residual class `d=13` provably never occurs for this seed. **No gap
found.** This is a genuine, complete, single-seed positive result — literal
Joint FAH now holds unconditionally for `a_1=4807`'s standing rogue pair —
but explicitly not a general FAH/Cofinite-FAH theorem (honestly scoped as
such by the file itself). **Verdict: CHANGES REQUESTED** (Status
`partial`, correctly self-reported). Certified
`lemmas/finite-window-literalization-lemma.md`.)

partial (round 25: three slugs built, all independently re-verified by this
review from scratch — own fresh Python/`sympy` scripts distinct from every
builder's, own re-derivation of every threshold inequality, own witness/gcd
checks, own greedy re-simulation. **(1) `a1-3qk-subfamily-theorem` (revise,
4th build on this gap) — `m=3` fully closed.** Independently reproduced,
via a fresh `sympy` sieve scan, the exact claimed 12-instance `k=0` residual
list (`q∈{11,17,19,23,29,41,53,59,61,71,89,479}`) and the exact claimed
14-instance `k≥1` residual list (`(q,k)∈{(7,1),(7,2),(7,3),(7,7),(11,2),
(13,3),(17,1),(17,2),(17,4),(19,1),(23,1),(29,2),(59,2),(71,2)}`) — 26
total, digit-for-digit, and extended the `k=0` scan well past the builder's
own spot-check to `q<60,000` with zero further exceptions (consistent with
the analytically-proved `q≥737,282` threshold). Verified all 26 explicit
witnesses by direct `gcd` computation — all correct. Independently
re-derived both Primorial-Floor-Bound inductions from scratch (base cases
`16!≥g(15)` and `15!≥h(14)`, plus the `r,s∈{4,...,39}` induction-step range)
— both hold; **found one minor write-up arithmetic error**: the file states
`h(14)=1{,}241{,}245{,}707{,}702`, but the correct value from its own stated
formula is `824{,}633{,}945{,}528.86` — both are `<15!`, so the base case's
truth is unaffected, but the displayed number is simply mis-computed (a
round-21-precedent-style minor slip, not load-bearing). Independently
re-simulated the literal greedy recursion (own fresh script, not the closed
form) for 13 primes out to 60-400 terms each: **zero mismatches**,
including at every one of the 26 hand-resolved exceptional indices. **No
gap found anywhere.** This is a genuine, complete, unconditional third
instance of the `a_1=3q^m` family (`m=1,2,3` now all fully certified).
**Certified** `lemmas/a1-3q-cubed-periodicity-theorem.md`. `m≥4` remains
honestly open (the round-25 build's own "Open gap" section correctly
identifies two genuine per-`m` obstacles — growing threshold constants and
an `m`-specific OR-split re-derivation — not yet resolved for general `m`).
**Verdict: CHANGES REQUESTED** (Status `partial`, correctly self-reported —
matches the exact precedent set one round earlier for this same file's
`m=2` closure: a complete, certified, gap-free standalone theorem is not
enough to flip the *approach's* Status to `solved` when the approach's own
declared target is the general-`m` family, which remains open). **(2)
`a1-pq-subfamily-theorem` (new) — uniform-in-`p` machinery fully proved,
`Bad(p)` not pinned down for `p≥5`.** Independently re-derived the
Generalized gcd-difference Witness Lemma (one-line, correct) and the
Generalized `K_0`-Boundedness Lemma (modular-inverse derivation of `s_0(j,r)
∈{1,...,p-1}`, `K_0(j,r)=p+s_0(j,r)`, independent of `q`'s magnitude) from
scratch, then independently cross-checked the full `p=5` table (12 `(j,r)`
pairs) via a from-scratch brute-force search for the least Case-(b) index
`n_0` and its `K_0` for an explicit smallest admissible prime in each
residue class — **exact match on all 12 entries**. Also independently
reconfirmed the `p=3` specialization reproduces the certified `a1-3q`
theorem's exact constants. No gap found in either lemma. **Certified**
`lemmas/generalized-k0-boundedness-and-gcd-difference-witness.md`. The
builder's own honest scope statement is confirmed accurate: the machinery
is uniform in `p`, but the literal exceptional set `Bad(p)` genuinely
requires a per-`p` finite computation not carried out here for any `p≥5` —
this is a real, structural (not lazy) gap, correctly diagnosed as such.
**Verdict: CHANGES REQUESTED** (Status `partial`, correctly self-reported —
real, certified new machinery, but the approach's own deliverable, an
explicit `Bad(p)` for general `p`, is not complete). **(3)
`n1-periodicity-reconciliation` (revise) — corrected round-24's H2
seed-asymmetry framing.** Independently attempted to reproduce the round-25
math-explorer's large-scale (`~750k`-`1M` term) `S_0`-restricted
extended-type-count simulation but found this requires first independently
recomputing each seed's `S_0` (the Finite-Core-Theorem-enlarged core, itself
a nontrivial multi-step absorption computation) as a prerequisite — not
feasible to fully replicate within this review's time budget. A lighter
proxy check (raw full-factorization type diversity, not `S_0`-restricted)
was attempted but found to measure a qualitatively different, much larger
quantity (near-linear growth, ~35% of terms already distinct raw types by
`n=30,000`) — confirming this proxy is NOT comparable to the file's
`S_0`-restricted metric, so it was not used to draw any conclusion either
way. Consequently, this review did **not** independently reproduce this
round's specific large-`N` numeric claims (unlike the field's usual
"always re-derive the load-bearing computation" bar), but confirms: (a) the
file's own logic (local-exponent formula, replacing a global fit
demonstrably contaminated by early-transient recruitment) is sound and
correctly derived from the stated raw counts; (b) the file's honesty
caveats (§10, "what this section does NOT claim") are accurate and
non-overclaiming — no bound on `(N(S_k))_k` is claimed or follows from any
simulation, and no new H2 mechanism is proposed. **Verdict: CHANGES
REQUESTED** (Status `partial`, correctly self-reported — a real
methodological correction to a prior round's numeric framing, but purely
diagnostic; H1 and H2 both remain fully untouched; this review flags its own
verification of this slug as partial-confidence, numeric claims not
independently re-derived at scale, unlike the other two slugs this round).
2 new lemmas certified this round (`a1-3q-cubed-periodicity-theorem.md`,
`generalized-k0-boundedness-and-gcd-difference-witness.md`). **Overall
workspace Status remains `partial`**: H1/FAH (19th consecutive plateau
round, 6-25) and H2 both remain open for the fully general problem; the
run's floor deliverable now stands at **4 fully certified solved infinite
subfamilies** (`2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3^a q` for `a=1,...,5`),
plus certified standalone `a_1=3q^2` and `a_1=3q^3` theorems (both housed in
the still-`partial` `a1-3qk-subfamily-theorem` approach), plus a new
`p`-uniform reduction machinery for the `a_1=pq` family (housed in the
still-`partial` `a1-pq-subfamily-theorem` approach, `p≥5`'s `Bad(p)` not yet
pinned down), plus the gap-free Master Conditional Theorem reducing the
fully general case to H1+H2.)

partial (round 24: three slugs built, all independently re-verified by this
review from scratch — own fresh Python/sympy scripts distinct from every
builder's, own exhaustive re-derivation of every claimed residual-band
closure, own re-simulation of every claimed theorem. **(1)
`a1-3qk-subfamily-theorem` (revise, third build on this gap) — `m=2` fully
closed.** Independently reproduced, via a fresh `sympy` sieve scan, the
exact claimed 9-instance residual-exception list (4 at `k=0`:
`q∈{11,17,23,29}`; 1 at `q=7,k=1`; 4 more at `q∈{13,17,19},k=1` and `q=11,
k=2`) digit-for-digit, verified all 9 explicit witnesses by direct `gcd`
computation, spot-checked `k∈{8,...,39}` for `q<500` finding zero further
failures (consistent with the claimed unconditional `k≥8` closure), and
independently re-simulated the resulting theorem (`a_1=3q^2`, every prime
`q≥7,q≠5`, `T=1,L=3` from `n=1`) on 22 primes out to 40-60 terms each with
**zero mismatches**. No gap found anywhere in the `m=2` closure. **Certified**
`lemmas/a1-3q-squared-periodicity-theorem.md`. `m=3`/general `m` remain
honestly open (setup only, no closure attempted this round beyond a
numeric scan). **Verdict: CHANGES REQUESTED** (Status `partial`, correctly
self-reported by the builder — the file's own target is the general-`m`
family, not just `m=2`, so despite `m=2` being a complete, gap-free, now
certified theorem in its own right, the approach as scoped is not yet
`solved`). **(2) `a1-3aq-subfamily-theorem` (new) — APPROVE, Status
`solved` for its own explicitly-declared restricted scope
(`a∈{1,...,5}`).** Independently, exhaustively re-verified every claimed
piece from scratch: the `K_0(a)=3^a+s_0` `q`-independence fact; the
corrected witness identity (`c=3^{a-1}q+(i-1)`, NOT the naive `q+(i-1)`
transplant, which this review confirmed produces a genuinely FALSE witness
at `a=2,q=11,k=0`: naive window gives `i=3⟹gcd(13,10)=1`, a spurious
"witness", while the TRUE window `{34,35,36}` has no element coprime to
`K_0=10`); the Generalized Primorial Floor Corollary (re-derived the
induction, confirming it never used the specific constant `5`); the
`s_1(a),k_thresh(a)` table for `a=1,...,5` (independently recomputed via a
fresh script, exact match: `s_1=4,4,4,5,5`, `k_thresh=12,12,12,28,28`); and,
most importantly, **exhaustively re-ran the entire residual-band closure
independently** (own script, `a=1,...,5`, both branches, `k<k_thresh(a)`,
`q<2000`): found exactly 86 crude-bound failures, and for every one
independently searched for a genuine witness, finding **exactly one**
instance with none — `a=2,K_0=10 (q≡2 mod 3),k=0,q=11` — matching the
builder's sole flagged exception exactly. Also independently confirmed, via
a fresh from-scratch greedy simulation, that (i) for `a=1,...,5` and every
prime `q∈[7,600)` (extended well past the builder's own `q<200` range), the
theorem holds with **zero** mismatches except the single flagged exception,
which is itself independently confirmed (`a_5=110≠111` at `a=2,q=11`,
sequence genuinely deviates at `n=5`); (ii) the `q=5` exclusion mechanism
(both `K_0(a)=3^a+1` and the sole window candidate always even) holds and
breaks the induction at `n=3` for every `a=1,...,5`, independently
simulated. **No gap found anywhere.** This is a complete, rigorous,
independently-verified theorem for its explicitly and honestly declared
scope (`a∈{1,...,5}`, NOT a claim about general `a` — the file correctly
and explicitly flags general `a≥6` as an open, though effectively-procedure-
backed, gap). This narrower-but-complete scoping is legitimate and
analogous to the workspace's established precedent (each of the three prior
certified subfamily theorems — `2|a_1`, `a_1=p^k`, `a_1=3q` — is likewise a
complete result about one specific slice of the `a_1`-space, not a claim
about all `a_1`). **Certified**
`lemmas/a1-3aq-generalized-corollary-and-mechanisms.md` (Generalized
Primorial Floor Corollary, corrected witness-window identity, `q=5`
exclusion mechanism, all four independently re-verified). **Verdict:
APPROVE — the run's 4th APPROVE.** **(3)
`new-prime-recruitment-rate-bound` (new) — RETHINK confirmed, but with a
genuine new certified theorem.** The approach's own proposed target
(`R(N)`-finiteness, unrestricted total-new-prime-count) is proved, in full,
to be unconditionally FALSE for every `a_1` — independently re-derived every
step of the "Unbounded Total Prime Support Theorem" (smooth-number counting
via `N(X)≤(log_2 X+1)^k`, combined with the certified Bounded Gap Lemma and
an elementary from-scratch Binomial Dominance sub-lemma
`2^m≥(m/(2K))^K`), confirming the final contradiction assembly
(`s≤s_0(k):=2^k(2K)^K` for all sufficiently large `s`, contradicted by
choosing `s^*>s_0(k)`) is correct and gap-free — a genuinely new,
unconditional, fully elementary result (no PNT/Chebyshev). **Independently
confirmed this does NOT refute H2**: re-traced the certified
Self-Absorbing Core Theorem's definitions (`self-absorbing` requires
`P(a_j)⊆S*` only for the finite prefix `j≤N(S*)`, is silent about all later
indices) and confirmed the theorem's divergence claim is fully compatible
with H2's existence hypothesis, since it can be realized entirely by
primes past the self-absorption threshold. **Certified**
`lemmas/unbounded-total-prime-support-theorem.md` (a permanent, useful
closure of the "raw prime support stays bounded" H2 mechanism, and a
correction of the outline's proposed literal `R(N)`-finiteness target).
**Verdict: RETHINK** (Status `unsolved`, correctly self-reported — the
approach's proposed mechanism cannot proceed as stated; H2 itself untouched
in either direction). 3 new lemma files certified this round
(`a1-3q-squared-periodicity-theorem.md`,
`a1-3aq-generalized-corollary-and-mechanisms.md`,
`unbounded-total-prime-support-theorem.md`). **Overall workspace Status
remains `partial`**: H1/FAH (18th consecutive plateau round, 6-24) and H2
both remain open for the fully general problem; the run's floor deliverable
now stands at **4 fully certified solved infinite subfamilies** (`2|a_1`;
`a_1=p^k`; `a_1=3q`; `a_1=3^a q` for `a=1,...,5`), plus a certified
standalone `a_1=3q^2` theorem (housed in a still-`partial` approach), plus
the gap-free Master Conditional Theorem reducing the fully general case to
H1+H2.)

partial (round 23: two slugs built, both independently re-verified by this
review from scratch — own fresh Python simulations distinct from both
builders' scripts, own re-derivation of algebra, and (for the sieve claim)
extended computational search well beyond the builder's tested range.
**(1) `a1-3qk-subfamily-theorem` (new, generalizes the certified `a_1=3q`
theorem to `a_1=3q^m`, `m≥1` fixed)** — independently re-verified Part I
(base case, `a_n+1` illegality, Case (a), odd-`n` Parity Witness — all four
genuinely `m`-independent, re-derived from scratch) and Part II (`n_0,s_0`
formulas `m`-independent; `K_0(q,m)=3q^{m-1}+s_0` genuinely grows with `q`
for `m≥2`, re-derived and confirmed exactly, including the `m=1` reduction
check) — all correct. **Found and corrects a load-bearing error in Part IV,
this round's own claimed "substantive result."** The builder computed the
certified Legendre Sieve Gap Bound's sufficient condition
(`L≥2^r(r+1)`, `r=ω(qK_0)`) only for primes `q∈[7,200)` at `m=2,3`, found it
fails at 18/43 and 27/43 of those primes respectively (this review
independently reproduced these exact counts and exact failing-prime lists),
but then reported this as "no sign of a small finite exceptional set...a
systematic mismatch of growth rates, not a routine finite check" and
"provably insufficient" for `m≥2` — language claiming a structural
impossibility. **This review extended the same computation to
`q∈[200,20000)`** (own script, `sympy`) and found: **zero failures for
`m=2` beyond `q=443`, and zero failures for `m=3` beyond `q=1103`**, out of
thousands of further primes tested — i.e. the failing set looks exactly
like a **finite residual band**, structurally identical in kind to the
`m=1` case's already-solved 18-entry residual table (just larger), not a
"genuine change in asymptotic regime" as claimed. The builder's own
`L/K_0→` fixed-constant-`<1` computation is correct arithmetic but does
**not** imply the certified bound `L≥2^r(r+1)` fails asymptotically — since
`r=ω(qK_0)` has slow-growing normal order (`~\log\log`), `2^r(r+1)` is
typically far smaller than the linearly-growing `L`, so the bound should
hold for *most* large `q`, exactly what this review's extended computation
shows. **Verdict: CHANGES REQUESTED** (Status `partial`, as self-reported,
is correct — no false `solved` claim — but the file's own diagnosis of
*why* the gap is open is mathrematically wrong and must be corrected before
being trusted by a future round; the actual evidence now suggests the
existing certified sieve tools likely DO close `m≥2` with a larger but
still-finite residual band, the same style of closure that took `m=1`
three rounds, not new machinery as claimed). Certified the two genuinely
correct, `m`-independent sub-lemmas (Part I item 4's Parity Witness,
correcting a sign-slip in the write-up's intermediate clause though the
final statement was right; Part II's `n_0,K_0` bookkeeping) to
`lemmas/a1-3qm-parity-and-k0-bookkeeping-lemmas.md`. **(2)
`direct-s0-self-absorption` (new, direct non-inductive H2 attack)** —
independently re-verified every claim. Propositions 1–2 (the "direct S₀
attack" is literally the `M=N_0` instance of the certified Monotone Chain
Reformulation Lemma, `S_0'=S_{N_0}`) are correct, re-derived from the
definitions. Proposition 3 (Bounded Witness Lemma's shared-prime guarantee
cannot imply full containment in a core) is a correct, self-contained
negative result, re-derived and confirmed — **certified**
(`lemmas/bounded-witness-insufficiency-for-containment.md`). The round's
central finding — a **corrected citation**: round-17's "N(S₀)=0 on 9/9
seeds" (cited by the round-23 outline/explorer as support) actually refers
to `S₀=Q` (base level), not the Finite Core Theorem's enlarged core — is
**independently confirmed exactly** by tracing `/tmp/memory/math-explorer.md`
line 18 ("stabilizes immediately at S_0=Q") and by a fresh, independent
20,500-term simulation (own script, distinct SPF/bitmask-free
distinct-factor-set method) on both mandated hard seeds
(`a_1=4807,11305`): every single reported number was reproduced **exactly**
— `Q`, `S_0` (`{2,3,5,7,11,19,23,73,127}` and
`{2,3,5,7,13,17,19,23,29,37,43,101}`), the containment-violation counts
(`18501/20500` and `17865/20500`), the distinct-extended-type counts (`129`
and `317`), the quartile arrival breakdowns (`94,16,8,11` and
`199,55,37,26`), and the exact indices of the brand-new types arriving in
the final `5%` of the window on both seeds. This is a fully, exactly
reproduced computational finding — no error found anywhere in this
approach's work. **Verdict: CHANGES REQUESTED** (Status `partial`, correctly
self-reported — real progress: a genuine reduction confirmed to add no new
leverage beyond the existing lemma stack, a new certified insufficiency
lemma, and a corrected, exactly-verified numeric premise showing the H2
existence question is *not* trivially supported at the correct core — but
H2 itself remains open). 3 new lemmas certified this round
(`a1-3qm-parity-and-k0-bookkeeping-lemmas.md`,
`bounded-witness-insufficiency-for-containment.md` — crediting both `a1-3qm`
lemmas as one file). **Overall workspace Status remains `partial`**: H1/FAH
and H2 remain open; the `a_1=3q^m`, `m≥2` extension is a real new open
sub-target (correctly NOT claimed solved, and now correctly diagnosed as
plausibly closable by the SAME certified sieve machinery with more
casework, not requiring new tools as the round's own build first
believed); H2's "direct S₀" framing is now known to add no leverage beyond
the existing Monotone Chain Reformulation Lemma, and the round-17 numeric
premise many past rounds cited in support of H2 has been corrected — the
math-explorer's round-23 "most promising H2 opening" framing (per its own
memory rule) needs re-examination next round in light of this correction.)

partial (round 22: two slugs built, both independently re-verified by this
review from scratch, per the standing "adversarial, own scripts/algebra"
protocol. **(1) `a1-3q-subfamily-theorem` (third build on this gap) —
APPROVE, Status `solved` for this approach's restricted-scope target.** The
round-22 build claims the open gap (Case (b), `n` even, `k≥1`) is closed,
completing an unconditional, literal `T=1,L=3` periodicity proof for
`a_1=3q`, every prime `q≥7,q≠5`, every `n≥1`. This review independently
re-derived, from scratch (not by reading the builder's algebra and nodding
along), every piece: **Lemma A (Legendre Sieve Gap Bound)** —
re-derived the `p_i≥i+1` sub-lemma, the telescoping density bound
`∏(1-1/p_i)≥1/(r+1)`, the Legendre/Möbius sieve identity
`S=L·∏(1-1/p_i)+E` with `|E|<2^r`, and the final assembly
`L≥2^r(r+1)⟹S≥1` — correct and gap-free, confirmed by an independent
computational sanity check (own script, distinct from the builder's,
comparing the bound against the true Jacobsthal-type max-gap for
`M∈{6,10,30,210,2310,30030,56,110,98,10010}`: bound holds with wide margin
in every case, e.g. `M=30030`: true gap `22` vs bound `448`). **Lemma B
(Primorial Floor Bound)** — re-derived the one-line `M≥(r+1)!` bound and
independently re-checked the corollary's induction (base case `s=4`:
`120≥576/7+5≈87.3`; inductive step algebra `(s+2)^2≥2(s+3)` for `s≥1`) —
correct. **The application to close Case (b)** — independently re-derived
the `s:=ω(K)≥4` branch (`7k≥2^{s+1}(s+2)` from Lemma B, combined with
`L=n-1≥kq≥7k` and `r=ω(qK)≤s+1`, giving `L≥2^r(r+1)` via Lemma A) and the
`s≤3` branch (generic bound `2^4·5=80` handles `k≥12`; Lemma B rules out
`s≥4` for `k≤38`, so the residual band is exactly `k∈{1,…,11}`). **Recomputed
the entire 18-entry residual-band table** (`k∈{1,2,3,4,7,8,9,10,11}` ×
`K_0∈{4,5}`) independently — every `(K,ω(K))` pair matches exactly (e.g.
`k=2,K_0=4→K=10,ω=2`; `k=3,K_0=5→K=14,ω=2`, etc., all 18 confirmed by direct
factorization). **Independently re-derived the `q_thresh` monotonicity
argument** and confirmed, by direct computation of `L(q)` at `q=7` (`K_0=5`
branch) and `q=11` (`K_0=4` branch) — the smallest admissible prime in each
residue class — across all 18 `(k,K_0)` pairs, that **exactly three**
`(k,K_0,q)` instances fall below threshold: `(1,5,7)`, `(2,4,11)`, and
`(3,5,7)` — matching the builder's claim exactly, with `(3,5,7)` resolved for
free via `q|K` reducing `ω(qK)` below the generic bound (independently
verified: `M=98=2·7²`, `ω=2`, bound `12≤L=25`), leaving only the two
"irreducible" hand-checked cases `(1,5,7)` and `(2,4,11)`, both witnessed at
`i=3` — independently re-verified both by direct gcd computation
(`gcd(56,27)=1`; `gcd(110,39)=1`). **Independent computational confirmation**
of the whole theorem: fresh from-scratch greedy simulation (own script,
distinct from the builder's) for 17 primes `q∈{7,…,71}` out to 60 terms each
(covering both exceptional indices `n=12,26`) — **zero mismatches** against
`a_n=3(q+n-1)`; a deeper simulation for `q∈{7,11,13}` extended to cover
`k` up to `~16` (terms up to `222`) — again **zero mismatches**; and
independently reconfirmed the `q=5` exclusion breaks exactly at `n=3`
(`a_3=20≠21`, own simulation matches the builder's mechanism-level proof
exactly: window `i∈{1,2}` at `n_0=2`, both candidates fail,
`gcd(20,15)=5`, `gcd(20,18)=2`). Also re-checked the full assembled induction
(base case; `a_n+1` illegal via consecutive-integer coprimality; `a_n+2`
illegal via Case (a) `q∤(a_n+2)`, Case (b) odd-`n` parity witness (re-derived
the `gcd(N,a_n)=gcd(N,2)` identity and the `N` odd `⟺` `n` odd equivalence
from scratch), Case (b) even-`n` `k=0` (re-derived `n_0,K_0` formulas and
both exceptions `q=7,q=11`) and even-`n` `k≥1` (this round's closure);
`a_n+3` legal via shared factor `3`) is exhaustive — every `n` is covered by
exactly one case, no skipped subcase, no double-counting gap, and the
induction correctly propagates `H(n)⟹H(n+1)`. **No gap found anywhere in
this proof.** This is a genuine, complete, unconditional, gap-free proof of
literal `T=1,L=3` periodicity for the entire stated subfamily. **Certified**
both `lemmas/legendre-sieve-gap-bound.md` and
`lemmas/primorial-floor-bound.md` (promoted from certified-candidate to
certified). **Verdict: APPROVE** — Status `solved` for this approach (the
run's 3rd APPROVE; workspace-level Status remains `partial` since H1/FAH and
H2 are untouched by this subfamily result). **(2)
`orbit-merging-additive-offset-dichotomy` (first build, new approach) —
RETHINK confirmed.** The builder's mandatory disambiguation check (required
first deliverable, per the round-5 `reversible-transition-map` precedent)
found both natural instantiations of the outline's candidate offset object
fail. This review independently verified the finding is genuine, not a
builder error: (a) re-read `lemmas/witness-discontinuity-obstruction.md`
(the certified round-7 example, `a_1=175`) and confirms it is a real,
on-point precedent for instantiation 1's fatal flaw — a concrete,
independently-checkable case where "earliest witness of a fixed type" is
provably NOT stable under core enlargement, directly undermining any
existential-to-universal promotion of the shared-prime witness Free Facts
supplies; the mistargeting critique (the mechanism, even if it worked, would
speak to H2/recruitment, not H1/FAH, since the witness prime `q∉S*` in the
rogue case) is also independently confirmed correct via the same Free
Facts/Generalized Bounded Witness Lemma reasoning. (b) For instantiation 2,
independently re-simulated `a_1=385` from scratch (own efficient
bitmask/prime-index-set implementation, distinct from all three of the
builder's and prior rounds' scripts) over 12000 terms: **exactly reconfirmed
the claimed period `(T,L)=(5088,43890)`** (zero mismatches across 6912
checked `n`-offset pairs), and independently computed the nearest-neighbor
offset between `A={5}` and `B={7}` occurrence-index sequences, finding it
**bounded but non-constant** (this review's own instantiation oscillates
among `{-1,0,1}`; the builder reports `{-2,-1,1,2}` for its own — a minor,
immaterial difference in exact instantiation/reference direction, not in the
qualitative finding both independently establish: bounded, small, genuinely
non-constant, not settling to a fixed shift). The builder's Theorem
(periodicity `⟹` offset eventually periodic with period `k_A`) was
independently re-derived from scratch (via `ρ_{S*}(n)` depending only on
`a_n mod L`, plus `a_{n+T}≡a_n \pmod L`) and confirmed correct — establishing
that the offset property is a downstream consequence of the very
periodicity being sought, not independent leverage toward it, i.e. a
genuine circularity. The independent §3 structural obstruction (the
nearest-neighbor offset, built purely from occurrence order, cannot by
construction recover which prime is shared, so even an unconditional proof
of offset-periodicity would not evidently yield FAH's shared-prime
conclusion) is sound, elementary reasoning, confirmed correct by this
review. **Verdict: RETHINK** — Status `unsolved` correctly reported, no
overclaim; this is genuine, honest negative progress (31st confirmed-dead
FAH mechanism variant), not a builder error or a premature RETHINK.** 2 new
lemmas certified this round (promoted from certified-candidate:
`legendre-sieve-gap-bound.md`, `primorial-floor-bound.md`). **Overall
workspace Status remains `partial`**: the general problem (H1/FAH, H2) is
still open, now with a 3rd fully solved infinite subfamily (`2|a_1`;
`a_1=p^k`; `a_1=3q` for prime `q≥7,q≠5`) joining the run's floor deliverable,
and a 31st confirmed-dead FAH mechanism variant narrowing the search space
further.)

partial (round 21: two slugs built, both independently re-verified by this
review from scratch — own fresh Python simulations distinct from both
builders' scripts, own re-derivation of the algebra/number theory, and (for
the FAH slug) two independent period-detection scripts. **(1)
`a1-3q-subfamily-theorem` (second build on this gap)** — re-derived and
CONFIRMED all three of this round's claims: (a) the Step-4 uniformity fix
(the finite check "7k ≥ 2^{ω(K)+2} fails only at k=1,2 for K₀=4 and k=1 for
K₀=5" reproduced exactly by independent computation over k=1..30); (b) the
"crude bound g(M) ≤ 2^{ω(M)}" elementary-proof obstruction is real — I tried
the same two natural repairs (halving induction with existential IH
pointers, and the AP-based peel-one-prime-at-a-time fix) independently and
hit the identical walls (the former has the `M=6`-style collision the
outline-reviewer already flagged; the latter only reproduces the radical
bound), and confirmed by direct sieve on primorials and other composites
(`M` up to `9699690`, `ω` up to 8) that the bound itself is true with wide
margin (matching known Jacobsthal-function values, e.g. `g(30030)=22 ≤ 64`),
so this is a genuine, believable, but nontrivial fact, not a false lemma
being chased; (c) the CRT construction `q=40153, k=3335, K=10010` — verified
`q` prime, `K₀=5` branch, `n=133{,}937{,}024`, `N=a_n+2=q·K` exactly, and by
direct exhaustive search over the true window found the minimal witness at
`i=11` (offset exactly `10` from `q`, matching the claimed `g(10010)=10`) —
confirming the "small fixed window" fallback is genuinely refuted, not just
under-searched. **Verdict: CHANGES REQUESTED** — Status stays `partial`;
Case (b), `n` even, `k≥1` remains open (Step 1, the crude bound itself, is
unproved elementarily), but this round's negative findings are real,
correct, unconditional progress (they foreclose the two most natural
elementary repair strategies) — no new lemma certified this round (both
findings are diagnostic/negative, matching the workspace's existing
diagnostic-lemma precedent). **(2) `fah-counterexample-hunt` (first build,
new approach)** — independently re-verified the two central computational
claims: re-implemented a from-scratch naive greedy generator (no bitmask
optimization, different from the builder's two scripts) and (i) confirmed
the exact claimed period `(T,L)=(5088,43890)` for `a_1=385` with **zero**
mismatches across 26911 checked gap indices (~5 periods), plus independently
confirmed the periods for two of the four canonical hard seeds,
`a_1=187→(T,L)=(484,7854)` and `a_1=221→(334,6630)`, exactly matching the
builder's table; (ii) independently recomputed, with my own script, every
disjoint-base-type extended-type-variant pair over one full period of
`a_1=385` at `S*={2,3,5,7,11,19}` and found **zero violations** among all
qualifying pairs — confirming the "false alarm" resolution (the apparent
`{7}`-vs-`{11}` non-intersection was genuinely an artifact of averaging over
a base type's several extended sub-types rather than checking each variant
pair) is a real resolution, not a hidden gap. No counterexample to FAH
survives this round's search, and no error was found in the builder's
methodology or numbers. **Verdict: RETHINK (not a rejection of the work,
which is rigorous and independently confirmed correct in every particular
checked)** — Status stays `unsolved`: as currently scoped ("search for a
counterexample"), the round returned a clean negative across 11 fresh seeds
plus one honestly-flagged inconclusive case (`105945`), which is exactly the
outcome the round's own outline (§4) anticipated as "no refutation, but
real evidence" — this slug needs the outliner to decide the next concrete
step (extend `105945`'s search depth, run more adversarial seeds, or pivot
to attempting outline §1.3(a)'s structural non-intersection-invariant proof
directly) rather than open-endedly repeating "one more seed sweep." The
period-detection technique is a genuine, reusable, independently-validated
methodological contribution and should be cited/reused by future rounds
that need an exact (non-asymptotic) FAH check for a specific `a_1`.)

partial (round 20: four slugs built, all independently re-verified by this
review from scratch (re-derived algebra, re-ran independent Python
simulations distinct from the builders' scripts). **(1)
`triangle-consistency-pigeonhole` (revise)** — proved the **Constrained
Singleton Coherence Lemma** (+ Composite-Exclusion and Prime-Power Coherence
Corollaries): if a witness `x` in the induced constant-gcd class `(d*,
X_B^{(0)})` is itself a singleton occurrence, then `d*` is forced to be a
power of that singleton's prime — independently re-derived from scratch
(elementary confinement + unique-factorization argument), correct,
unconditional. **Certified**
(`lemmas/constrained-singleton-coherence-lemma.md`). But the round's deeper
finding is a new diagnostic: the positive computational "dominant class is a
prime power" pattern observed on the workspace's only two known hard test
seeds is a **confound** (§6.2) — both seeds already have their Cofinite-FAH
witness prime established by an unrelated route (the Two-Sided Singleton
Witness Theorem), so the pattern is a downstream consequence, not
independent evidence for the general existence conjecture. A further
attempt to construct a genuinely non-confounded test seed via a heuristic
core-recruitment procedure honestly failed to replicate the workspace's
documented recruited cores (over-recruits without converging) — reported as
a failed replication, no new seed obtained. §6.4's reduction argument
(the sharpened existence question is no easier in kind than the original,
both blocked by the same round-19 sieve/anatomy-of-integers obstruction) is
sound reasoning, not separately certified (diagnostic, matches the Lemma
F/Lemma I precedent). Verdict: **CHANGES REQUESTED** (Status `partial` —
genuine new unconditional lemma certified, but the Two-Sided Singleton
Witness Theorem's existence hypothesis remains open, now with a precise
diagnosis of why the round's own positive evidence doesn't count). **(2)
`triangle-critical-dichotomy-witness` (first build)** — found and proved
the **Universal Branch-(a) Dominance Theorem**: for every `n≥2` and every
prime `p|a_n` with `e:=v_p(a_n)`, `a_n/p^e ≤ a_{n-1}` — an unconditional
consequence of the certified Bounded Gap Lemma plus the problem's own
strict-monotonicity rule. Independently re-derived (algebra re-checked line
by line) and independently re-simulated on 6 fresh seeds (distinct from the
builder's ~2400-seed sweep; zero violations). This proves branch (b) of the
certified Critical Prime Dichotomy Lemma **never fires**, for any n, prime,
or core — killing this approach's own dispatched mechanism (which required
locating a genuine branch-(b) rescuer) at its root, more fundamental than
the sibling's equivalence-check finding that the two constructions are
non-duplicate. **Certified**
(`lemmas/universal-branch-a-dominance-theorem.md`). Verdict: **RETHINK**
(Status `unsolved`, correctly self-reported — the approach cannot proceed
as outlined; the new theorem is a genuine, reusable negative screen for
future rounds, a 3rd confirmed-vacuous mechanism variant after Escape-Cost
Vacuity and Same-Type Triangle Vacuity). **(3) `a1-3q-subfamily-theorem`
(first build)** — attempts literal `T=1,L=3` periodicity for `a_1=3q`
(prime `q≥7,q≠5`). Independently re-verified every claimed closed-form
computation (`n_0,K_0` formulas, the two exceptions `q=7,q=11` and their
hand resolutions, the `q=5` exclusion mechanism, the odd-`n` Parity Witness
argument) via fresh Python simulation across primes `q∈[7,120)` out to 300
terms each — exact match throughout, zero discrepancies from the predicted
pattern (consistent with, though not proof of, the still-open even-`n`,
`k≥1` case). Found one minor arithmetic slip in the open-gap discussion
(the threshold constant for the `k≥1` case should be `(3q+2)/(q-3)`, not
`(3q-1)/(q-3)`, as independently re-derived via `sympy`) — does not affect
the stated conclusion (`K≥7` still exceeds both thresholds for all `q≥7`)
and does not appear in either certified lemma below. **Certified** the
Parity Witness Lemma and the k=0-Window Criterion Lemma together
(`lemmas/a1-3q-parity-and-k0-window-lemmas.md`) — both correct,
self-contained, reusable for this or similar `|Q|=2` odd-seed subfamilies.
The genuinely open gap (Case (b), `n` even, `k≥1`) is honestly reported as
unresolved, correctly diagnosed as requiring a Jacobsthal-function-style
gap-existence bound the builder could not prove elementarily (a real, deep
open sub-problem, not a routine pigeonhole gap) — confirmed via the
builder's own adversarial CRT construction (rad ≈ 1.16×10^13, true witness
still found at `i=9`, far below the naive bound, with no elementary
explanation supplied). Verdict: **CHANGES REQUESTED** (Status `partial` —
substantial, verified progress on a genuinely new restricted subfamily
target, but not solved). **(4) `n1-periodicity-reconciliation` (revise)**
— withdrew round 19's circular Generalized Class-Blindness Obstruction (as
instructed) and replaced it with a narrower, non-circular **Ambient-
Statistic Obstruction** (§7): independently re-checked specifically for the
exact circularity flagged in round 19 (the "two scenarios agree" step is
now a purely syntactic independence check on formulas that provably never
reference realized tail data, not an assertion that a second genuinely
realizable sequence continuation exists) — this fix genuinely closes the
round-19 gap. Confirmed correctly and honestly scoped: it unifies the two
existing certified predecessors (`escape-cost-vacuity.md`,
`density-argument-vacuity-corollary.md`) into one proof but does **not**
extend coverage to the occupancy-referencing (practically useful) forms of
second moment/Borel–Cantelli/finite-Fourier/LP-relaxation, which remain
formally un-ruled-out — the precise opposite of round 19's overclaim, now
correctly walked back. **Certified**
(`lemmas/ambient-statistic-obstruction.md`, with its mandatory scope note).
Also formally certified the small **Vacuous FAH under 2|a_1 Corollary**
(`lemmas/vacuous-fah-under-2-divides-a1-corollary.md`, content unchanged
since round 16, low practical priority given the stronger sibling theorem).
Tightened the write-up per the audit-insurance explorer's structure
(executive summary, Theorems A/B reproduced inline, Master Conditional
Theorem restated). Verdict: **CHANGES REQUESTED** (Status `partial` —
genuine correction of a previously-flagged circularity, no progress on H1
or H2 directly, as instructed). 4 new lemmas certified this round
(`constrained-singleton-coherence-lemma.md`,
`universal-branch-a-dominance-theorem.md`,
`a1-3q-parity-and-k0-window-lemmas.md`, `ambient-statistic-obstruction.md`,
`vacuous-fah-under-2-divides-a1-corollary.md` — 5 files, crediting both
lemmas of the 3q pair as one file). Overall workspace Status remains
`partial`: H1 (FAH) and H2 (absorption-chain termination) both remain
completely open — this is now the 15th consecutive plateau round (6-20) on
H1 itself with no proof, though real narrowing continues on multiple
fronts each round (a 3rd confirmed-vacuous mechanism killed at its root;
the round-19 circularity now genuinely fixed rather than merely retracted;
a new restricted-subfamily target opened with real partial progress; a
precise confound diagnosis explaining why the round's positive
computational evidence for the existence hypothesis doesn't generalize).
The run's floor deliverable (2|a_1; a_1=p^k, both solved and certified)
remains unchanged and is now joined by substantial (not yet complete)
progress on a third restricted subfamily (a_1=3q).)

partial (round 19: four slugs built, all independently re-verified by this
review. **(1) `n1-periodicity-reconciliation` (revise)** — §8's floor-
deliverable audit (consolidating Theorems A/B, `2|a_1` and `a_1=p^k`) is
correct, pure citation, no new content, confirmed. §7's new **Generalized
Class-Blindness Obstruction**, proposed as a strict generalization of the
certified Escape-Cost Vacuity Theorem / Density-Argument Vacuity Corollary to
the entire statistical-method family, has a **genuine, load-bearing gap this
review found and confirms is real, not present in its two certified
predecessors**: those predecessors' "class-blind"/"window-class-blind"
statistics are defined so as to be structurally *incapable of referencing the
realized sequence's divisor-class data at all* (a Mertens-type ambient count
over ALL integers in a range, or a pairwise fact depending only on the fixed
indices — never on `g_n`), so the "two scenarios agree on all premises"
step is a tautology following directly from the definition. §7's new
"window-computable statistic" `Φ(N)`, by contrast, is explicitly defined
(§7.1) to depend on `W(N)`, which **includes the REALIZED legality/occurrence
Boolean history** — i.e., actual observed data from the (deterministic, for a
fixed `a_1`) greedy process. For two "scenarios" to share identical `Φ_j(N_j)`
values while diverging on whether `E` is finite, they must be two
*genuinely different, both fully legal* completions of the *same* finite
prefix of the same deterministic recursion — and the proof's only
justification for this ("nothing in the recursive definition... forces a
UNIQUE outcome... this is exactly the open content of H1 itself, so by
definition of 'open', both continuations are a priori consistent") is
**circular**: it assumes, as its own premise, that the tail behavior is not
determined by the prefix — which is exactly H1's open content, not an
independently established fact about the recursion. No concrete pair of
legal continuations (or pair of `a_1` values) realizing both scenarios is
ever exhibited. This review independently attempted to patch this by
restricting `Φ` to genuinely ambient/ decoupled-from-realized-data
statistics only (matching the true scope of the two certified predecessors)
— under that restriction the theorem IS correct and reduces to a direct,
easy corollary of the two existing certified lemmas, but that restricted
version does not actually cover the "occurrence-count" and "residue-class
occupation count" sub-cases the file claims to subsume in §7.1 (density,
second moment, finite-Fourier coefficients, LP-relaxation all explicitly use
realized occupation/occurrence counts, not purely ambient data) — so the
restricted, correct version is **weaker** than what §7.3 claims to have
closed off. **NOT certified as stated.** This is a real, findable, load-
bearing gap, not a stylistic quibble — it means the four named method
families are NOT yet formally ruled out by this argument as claimed, though
the underlying suspicion (they are all dead, matching 20+ prior confirmed-
dead mechanisms) remains plausible and is not contradicted. **(2)
`triangle-consistency-pigeonhole` (revise)** — the attempted anatomy-of-
integers/density closure of the Two-Sided Singleton Witness Theorem's
existence hypothesis honestly does NOT close (self-reported, and confirmed):
§5.1's elementary `ω(a_n) ≤ log_2 a_n` (hence `O(log n)`) bound is correct
and independently re-derived (trivial, `a_n ≥ 2^{ω(a_n)}`, combined with the
certified Bounded Gap Lemma) — **certified**
(`lemmas/elementary-omega-bound.md`). §5.3's obstruction (no sieve/density
technique applies to an implicitly, path-dependently defined index set/
cofactor sequence with no closed form or independent local-density control)
is a sound, honestly-scoped methodological diagnosis, not a formal theorem,
correctly not overclaimed as one — matches the Lemma-F/Lemma-I "diagnostic"
precedent, kept as documentation rather than certified as a standalone
lemma. Also certified this round: the three round-18 promotable lemmas from
this file that were left uncertified pending further use — **Double-Witness
Nested Pigeonhole Lemma**, **Same-Type Triangle Vacuity**, and the **Two-
Sided Singleton Witness Theorem** — all independently re-verified in full by
this review (re-derived every step from scratch; re-ran both computational
checks on `a_1=4807` and `a_1=11305`, matching every reported number).
Certified to `lemmas/double-witness-nested-pigeonhole.md`,
`lemmas/same-type-triangle-vacuity.md`,
`lemmas/two-sided-singleton-witness-theorem.md`. Verdict: **CHANGES
REQUESTED** (Status `partial` — genuine progress via 4 newly-certified
lemmas, but the existence hypothesis of the Two-Sided Singleton Witness
Theorem remains open, and the round's own new obstruction-finding is
correct and honest). **(3) `core-growth-monotonicity` (revise)** — the
weaker "some self-absorbing S* exists" H2 sub-target is correctly identified
(§5.0) as NOT a new target (verbatim the standing sub-gap (a) of the
Self-Absorbing Core Theorem) — honest, no overclaim. The new **Monotone
Chain Reformulation Lemma** (§5.1: `∃M, N(S_M) ≤ M ⟹ S_M` self-absorbing,
for the explicit monotone family `S_M := S_0 ∪ ⋃_{j≤M} P(a_j)`) is a correct,
one-line, fully unconditional consequence of the definitions — independently
re-derived, **certified**
(`lemmas/monotone-chain-reformulation-lemma.md`). Propositions 4 and 5
(honest dead-end findings: the natural non-recurrence/rate-control
contradiction attempts fail against this family too, and the converse
direction is not established since self-absorption is not shown monotone
under enlargement) were independently re-checked and confirmed correct — no
gap found, no overclaim; both are genuine negative results, not stalls.
Verdict: **CHANGES REQUESTED** (Status `partial` — real new reformulation
lemma, H2 sub-gap (a) still unresolved, confirmed a further-dead route).
**(4) `self-absorbing-by-construction` (revise, numeric hardening)** — two
new adversarial seeds (`a_1=510510`, `|Q|=7`, largest tested to date;
`a_1=209370`, a skewed one-huge-prime shape). This review independently
reimplemented the simulation from scratch (SPF-sieve + per-prime bitmask,
same method as round 18's third script) and reproduced, exactly, the
`a_1=510510` claims: first occurrences `{2,3,5,11,13,17}` at `n=36466` and
`{2,3,7,11,13,17}` at `n=51052` (window 65000), both recurring by window
200000 (`36466,72931,109396,145861,182326`, constant gap 36465;
`51052,102103,153154`, constant gap 51051) — exact match. For `a_1=209370`,
this review found and corrects a **minor mislabeling error**: the file
reports the second single-occurrence type at `n=34896` as `{2,3,5,7,997}`
(i.e. equal to `Q` itself), but the actual type at that index is
`{2,5,7,997}` (missing prime `3`) — a distinct, proper sub-type of `Q`, not
`Q` itself (independently confirmed: exactly two single-occurrence types
exist at window 60000, `{2,3,5,7,997}` at `n=1` and `{2,5,7,997}` at
`n=34896`). This does NOT affect the round's qualitative conclusion — this
review independently confirmed both types recur by window 300000
(`{2,3,5,7,997}` at `1,104686,209371`; `{2,5,7,997}` at
`34896,69791,139581,174476,244266`), leaving zero surviving singles, exactly
as claimed — but the specific type-identity claim in the file is inaccurate
and should be corrected. Verdict: **CHANGES REQUESTED** (Status `partial` —
numeric record is substantively correct and independently reconfirmed, with
one small documentation correction needed; NTBT remains open, no overclaim).
5 new lemmas certified this round
(`elementary-omega-bound.md`, `double-witness-nested-pigeonhole.md`,
`same-type-triangle-vacuity.md`, `two-sided-singleton-witness-theorem.md`,
`monotone-chain-reformulation-lemma.md`). Overall workspace Status remains
`partial`: H1 (FAH) and H2 (absorption-chain termination) both remain open;
the run's floor deliverable (2|a_1; a_1=p^k, both solved and certified) is
unchanged; the Two-Sided Singleton Witness Theorem's existence hypothesis
and the H2 existential sub-target both remain the sharpest currently-known
open residuals, neither closed this round, and this round's most important
finding is methodological: the Generalized Class-Blindness Obstruction, as
written, overclaims what it rules out — future rounds should either supply
an actual two-instance construction (not an appeal to openness) or restrict
its scope to genuinely ambient statistics, matching its two certified
predecessors' actual proof technique.)

partial (round 18: four slugs built. **(1) `prime-power-seed-periodicity-
theorem` (new) — APPROVED for its own restricted scope.** A self-contained
elementary strong induction (no persistent-type/FAH machinery) proving that
for every `a_1 = p^k` (`p` prime, `k ≥ 1`), `a_n = a_1+p(n-1)` for every
`n ≥ 1`, i.e. `T=1, L=p` literally from `n=1`. Independently re-derived from
scratch by this review (the induction is correct and gap-free: the `p-1`
intermediate candidates `a_n+1,...,a_n+(p-1)` all fail the `i=1` legality
check since `P(a_1)={p}` is a singleton, and `a_n+p` is legal and hence
forced by minimality) and independently re-simulated on 43 seeds — the
builder's own 24 plus 19 more this review chose independently, including
primes not in the builder's set (`p=29,31,37,41`) and exponents up to `k=10`
— exact match, zero discrepancies. `T` and `L` are stated and verified
explicitly per rigor rules. This is a genuine strict generalization (to every
prime, not just `p=2`) of the previously-implicit prime-power special case,
strictly overlapping (not duplicating) the certified `2|a_1` theorem exactly
at `p=2`. **Certified**
(`lemmas/prime-power-seed-literal-periodicity-theorem.md`). Verdict:
**APPROVE** for this approach's own restricted-scope target (a second
complete, gap-free sub-case resolution — the workspace-level Status remains
`partial`, since seeds with `|Q| ≥ 2` and FAH/H1/H2 are untouched). **(2)
`self-absorbing-by-construction` (revise, record correction)** — corrected
the round-17-flagged unresolved `a_1=255255` candidate exception
(`{5,7,11,13,17}`, first occurrence `n=27184`, unconfirmed to recur through
window 65000): extended the simulation to `n=500000` and found the type DOES
recur, at `n=135914`. This review independently re-derived this from
scratch with a THIRD, differently-implemented script (SPF-sieve + per-prime
bitmask method, distinct from both the builder's and the round-18
outline-reviewer's implementations) and reproduced, exactly, every reported
number: `{5,7,11,13,17}` occurrences `27184, 135914, 190280, 299010, 353376,
462106`; full-`Q` type occurrences `81549, 163097, 244645, 326193, 407741,
489289` (constant gap `81548`); `63` distinct observed types, each recurring
at least `6` times by `n=500000`. This is now a THREE-WAY independently
cross-validated computational fact. The round-17 "one open candidate
exception" is genuinely resolved; **zero open numeric counterexamples to
NTBT remain across the ~50+ tested seeds** — still evidence, not proof, and
correctly not overclaimed as such (NTBT itself remains an open conjecture; no
new proof route was attempted or found). Also recorded a permanent negative
finding that the "counting/pigeonhole" corridor for H2 is exhausted in all
three forms tried (independently re-derived, correct — each form either
restates `N(S_k)`-boundedness in new notation, is circular with H2's own
conclusion, or targets a provably-insufficient weaker target). Verdict:
**CHANGES REQUESTED** (Status `partial` — real, verified record correction;
NTBT remains open; no new certifiable lemma this round beyond the
already-certified Vacuous/Weak Self-Absorption Lemma). **(3)
`n1-periodicity-reconciliation` (revise, documentation)** — added two
permanent negative findings. Independently re-verified both from scratch.
**Odd-Prime Non-Trivialization Proposition**: the `2|a_1` H1-trivialization
trick does NOT generalize to odd `p | a_1` — on `a_1=15,45` (`Q={3,5}`), this
review's own fresh simulation confirms the base-type pattern is exactly
period-4 from `n=1` (`τ(n)={3,5}` at `n≡1`, `{3}` at `n≡2,0`, `{5}` at `n≡3`,
mod 4), with `3|a_n` for exactly 75% and `5|a_n` for exactly 50% of the first
3000 terms, and the "`3` fails" indices forming the exact arithmetic
progression `3,7,11,15,...` (common difference 4, confirmed via direct
recomputation of the difference set) — a genuine, structurally-explained
counterexample to any naive "`p|a_1` trivializes H1" generalization, not an
artifact. **`|Q|=2` Non-Tractability finding**: `|Q|=2` is confirmed not a
tractable "easy warm-up" subfamily — the four canonical hard test seeds
(187,209,221,247) already live inside it; this review did not independently
re-run the 36-seed sweep in full (accepted the builder's and explorer's
report given the internal consistency of the finding with 10+ prior rounds'
independent use of exactly these four seeds as the workspace's standing hard
cases) but spot-confirmed the qualitative claim is consistent with all prior
rounds' documented data on these seeds. Both findings are correctly recorded
as diagnostic/negative (not certified as standalone lemma files, matching
the established Lemma F/Lemma I precedent). Does not touch H1/H2 or the
Master Conditional Theorem (re-audited gap-free again this round). Verdict:
**CHANGES REQUESTED** (Status `partial` — genuine permanent narrowing of
what NOT to re-attempt; H1/H2 untouched). **(4)
`triangle-consistency-pigeonhole` (new, mandated plateau-break)** — killed
the outline's originally-proposed triangle/`e`-based forcing mechanism
(§2, "Same-Type Triangle Vacuity": `e:=gcd(a_{m_A},a_{m_A'})` for two
same-type witnesses carries no information about their outside-core prime
sets beyond what the shared type's own in-core primes already force —
independently re-derived and confirmed correct, a disguised instance of the
certified Same-Type Free-Facts Vacuity phenomenon), 19th+ confirmed-dead FAH
mechanism variant. While diagnosing this, found and fully proved a new,
different sufficient mechanism, the **Two-Sided Singleton Witness Theorem**
(§3: if a rogue pair `(A,B)` has SOME occurrence of each side whose
out-of-core prime set reduces to the SAME singleton `{q}` — not necessarily
the canonical/earliest witnesses — then Cofinite FAH holds for the pair with
witness `q`). Independently re-derived (a correct, direct two-fold
application of the already-certified Singleton-Side FAH Lemma, whose own
statement already permits arbitrary witnesses) and independently
re-verified computationally on BOTH of the workspace's only two known
properly-recruited-core hard rogue-pair seeds: `a_1=4807` (this review's own
fresh simulation reproduces exactly 13 `A'`-occurrences, 180 `B'`-
occurrences, singleton witness `x_1=72` with signature `{17}`, count 20, and
zero exceptions for `q=17` on both sides) and `a_1=11305` (247 `A'`-
occurrences, singleton witness `x_2=103` with signature `{11}`, count 23,
zero exceptions for `q=11` on both sides — one very minor count discrepancy,
79 vs this review's 80 `B'`-occurrences, immaterial to the zero-exception
claim). Both seeds' hard FAH content is now fully and correctly explained by
this new mechanism. The Theorem's own hypothesis (existence of a matching
pair of singleton witnesses) is honestly left open and correctly
characterized as a different, narrower, unproved existence question — this
review agrees it is NOT a restatement of FAH (it neither follows from nor
implies FAH in an obvious way: FAH only needs `q` to divide each occurrence,
not to be the SOLE outside-core prime) and is NOT obviously easier (no
argument, here or elsewhere, shows such witnesses must exist for a general
rogue pair; it is plausible they sometimes do not, in which case this
mechanism alone would not suffice even where FAH holds by some other route).
Genuine progress (one more dead mechanism ruled out, one new correctly-scoped
sufficient theorem with a sharper open residual question), not a
restatement, but does not close H1. Verdict: **CHANGES REQUESTED** (Status
`partial`). 1 new lemma certified this round
(`prime-power-seed-literal-periodicity-theorem.md`); the Double-Witness
Nested Pigeonhole Lemma and Two-Sided Singleton Witness Theorem from
`triangle-consistency-pigeonhole` are recorded here as promotable/reusable
but not separately certified as standalone lemma files this round (both are
correct, but their primary value is documented in the approach file itself
and their statements are tightly coupled to this round's specific
investigation; a future round citing them directly is free to request formal
certification). Overall workspace Status remains `partial`: the general
problem is now solved for THREE disjoint infinite sub-families (`2|a_1`;
`a_1=p^k`; and their overlap is exactly `a_1=2^k`), all still conditional on
H1 (FAH, 18+ confirmed-dead mechanisms, now sharpened by the Two-Sided
Singleton Witness Theorem's open existence-hypothesis residual) and H2
(absorption-chain termination, evidenced but not proved by the strengthened
NTBT numeric record) for every other `a_1`.)

partial (round 17: one slug built, `self-absorbing-by-construction`, per the
outline-reviewer's build set of 1 — `type-alphabet-counting-bound` was
RETHINK'd pre-build, since its central "finitely many rounds is weaker than
N(S_k) bounded" premise collapses to the SAME statement in one line, and its
fallback mechanism plausibly duplicates the standing FAH crux; not
registered). `self-absorbing-by-construction` proved a new unconditional
**Vacuous/Weak Self-Absorption Lemma**: `N(Q) ≤ 1 ⟹ S_0 = Q` is self-absorbing
with zero absorption rounds, `S* = Q` — independently re-derived from scratch
by this review (a direct, gap-free two-case unpacking of the definitions of
`Q`, the absorption operator, and `N(S)`; no gap). **Certified**
(`lemmas/vacuous-self-absorption-lemma.md`). The approach then ran an
extensive numeric investigation (~50 seeds) of the open **NTBT conjecture**
(`N(Q) ≤ 1` for every `a_1`), honestly reporting it as unproved. This review
independently reimplemented the greedy sequence generator from scratch
(different script) and reproduced EXACTLY the builder's reported occurrence
lists for the two smaller flagged seeds: `a_1=30030` (full-`Q` type recurs at
`1, 15016, 30031, 45046`, gap `15015`, confirmed) and `a_1=15015` (full-`Q`
type recurs at `1, 4629, 9257, 13885, 18513, 23141, 27769`, confirmed) — both
genuine window-artifact resolutions, exactly as claimed. **However, for the
third seed `a_1=255255` this review found the builder's numeric claim is
INACCURATE**: the builder claims "the sole remaining single-occurrence type
at window 40000 is the full-`Q` type". An independent, exhaustive enumeration
of ALL single-occurrence types (not just the 5 types the builder had
pre-flagged from an earlier, smaller window) finds a SECOND, unflagged
single-occurrence type at window 40000: `{5,7,11,13,17}` at `n=27184` — and
this type is confirmed to STILL be single-occurrence even at an extended
window of 65000 (25000+ terms of runway with no second occurrence), a longer
observation window than any of the builder's own confirmed-genuine recurring
types needed. This does not refute NTBT (the type may yet recur at a still
larger window, as the other cases did) and does not affect the correctness of
the certified Lemma (which is unconditional and does not depend on this
seed's numerics), but it means the builder's specific claim "all three
apparent counterexamples...resolved" is not fully established for
`a_1=255255` — a genuine, currently-unresolved candidate exception remains,
not yet checked at a large enough window to confirm or refute. Flagged for
the next round rather than silently accepted. Verdict: **CHANGES REQUESTED**
(Status `partial` — the Vacuous/Weak Self-Absorption Lemma is a genuine,
certified, permanent addition; NTBT itself remains honestly open, and the
numeric evidence supporting it is slightly weaker than reported, with one
concrete unresolved candidate — `a_1=255255`, type `{5,7,11,13,17}` first at
`n=27184`, no second occurrence through `n=65000` — that the next round
should extend the simulation window on, rather than treating the seed as
already fully resolved). 1 new lemma certified this round
(`vacuous-self-absorption-lemma.md`).)

partial (round 16: three slugs built. **(1) `even-a1-full-periodicity-theorem`
(new)** — a self-contained, elementary strong induction (no persistent-type/FAH
machinery at all) proving that whenever `2 | a_1`, the sequence satisfies the
closed form `a_n = a_1 + 2(n-1)` for *every* `n ≥ 1` literally, so `T=1, L=2`
witness the problem's conclusion from the very first term. Independently
re-derived and re-verified in full by this review (both induction branches:
`a_n+1` always illegal via consecutive-integer coprimality, `a_n+2` always
legal via uniform evenness) and independently re-simulated in a fresh Python
script on 12 seeds including several non-prime-power composites (6, 30, 210,
1994, 14, 22, 26, 4, 8, 34, 194, 2310), exact match in every case. This is a
genuine strict generalization of the previously certified `|Q|=1` special case
(now covers ALL even `a_1`, not just powers of 2). **Certified**
(`lemmas/even-seed-literal-periodicity-theorem.md`). Correctly and honestly
scoped: Status `solved` is claimed and verified ONLY for the restricted
`2 | a_1` subfamily; the file explicitly does not touch odd `a_1` or the FAH
crux, and the workspace-level Status correctly remains `partial`. Verdict:
**APPROVE** for this approach's own restricted-scope target (a complete,
gap-free sub-case resolution — this is the run's first outright APPROVE, on a
genuine non-trivial infinite subfamily, though it does not flip the overall
problem to solved). **(2) `n1-periodicity-reconciliation` (consolidation)** —
assembled, for the first time in one place, the full conditional dependency
chain for the GENERAL problem: a **Master Conditional Theorem** deriving the
problem's actual claim from exactly two precisely-stated open hypotheses,
(H1) FAH at the terminal core of the self-absorbing-core absorption chain
(equivalent to the standing FAH/Symmetric FAH/Cofinite FAH/EEA crux) and (H2)
termination of that absorption chain (equivalent, via the certified
Termination Criterion Lemma, to boundedness of the threshold sequence
`N(S_k)`) — independently re-verified: every citation step in the chain
(Free Facts → Persistent-Type Pigeonhole → Finite Core Theorem → Extended
Persistent-Type Pigeonhole → Self-Absorbing Core Theorem → Universal Early
Intersection Lemma → Literal n=1 Periodicity Theorem, plus Monotonicity of
Resolution to transport FAH up the chain) is a genuine citation to an
already-certified, previously gap-checked lemma, and the final assembly step
(§2) is a correct one-paragraph chaining with no smuggled content. Also proved
one new genuine unconditional corollary — **(H1) is vacuously true whenever
2 | a_1** (independently re-derived: `2 ∈ Q` forces `2 ∈ ρ_S(n)` for every `n`
and every core `S ⊇ Q`, hence every two extended types share `2`) — and one
honest negative finding, that the same trick does **not** trivialize H2 (self-
absorption needs full-factorization containment, not merely a single shared
prime; independently confirmed no rescue exists via this mechanism). No new
FAH mechanism was attempted this round (by design; H1 stays at 17+
confirmed-dead mechanisms). Verdict: **CHANGES REQUESTED** (Status `partial`
— real, permanent narrowing: the general problem is now reduced, with a
complete and independently-verified gap-free reduction chain, to exactly two
named open hypotheses instead of an unstructured pile of prior partial
results; neither hypothesis is resolved). **(3) `core-growth-monotonicity`
(new)** — dedicated attack on sub-gap (H2). Proved two new, fully independently
re-verified, unconditional lemmas: the **Binary Refinement Lemma** (adjoining
one prime `p` to a core `S` splits each `S`-persistent type `B` into at most
two `S'`-persistent types, a subset of `{B, B∪{p}}`, via an elementary
finite-partition pigeonhole argument) and the **Threshold Recursion Bound
Lemma** (`N(S∪{p}) ≤ max(N(S), max_B M_B)`, an exact structural relation
between the exceptional-index thresholds at two cores differing by one prime)
— both re-derived from scratch by this review and confirmed correct, with a
sanity computation on `a_1=175` corroborating the qualitative partition
structure. However, the natural next step — bounding the new quantities `M_B`
— is proved (Proposition 3, independently re-checked) to hit exactly the same
non-constructivity obstruction as `N(S)` itself, via a rigorous "two
consistent finite-prefix extensions" argument (a basic fact about infinite
0/1 sequences: eventual behavior is never decided by any finite prefix) —
this review notes the argument is in fact toolkit-independent/general, not
merely "no certified tool in this workspace computes it," strengthening its
status as a real structural finding rather than a workspace-contingent
placeholder. H2 remains open. Certified as reusable machinery
(`lemmas/binary-refinement-and-threshold-recursion.md`). Verdict: **CHANGES
REQUESTED** (Status `partial` — genuine new structural content, sub-gap H2
still unresolved). Two new lemma files certified this round
(`even-seed-literal-periodicity-theorem.md`,
`binary-refinement-and-threshold-recursion.md`). **Overall workspace Status
remains `partial`**: the general problem (all `a_1 > 1`) is not resolved; it
is now reduced to exactly two named open hypotheses H1 (FAH, 17+
confirmed-dead mechanisms, untouched this round by design) and H2
(core-absorption-chain termination, now with an exact one-prime recursion but
still no bound), while the entire `2 | a_1` subfamily is fully and
unconditionally solved as an infinite sub-case.)

partial (round 15: one slug built (`n1-periodicity-reconciliation`, revise),
dispatched to attack the two disclosed open sub-gaps (a) existence/termination of
a self-absorbing core S*, (b) whether N(S*) can be taken to be 0. Both new results
independently re-derived from scratch by this review, including a fresh
independent Python re-simulation of the builder's computational sanity check
(a_1=175, 3000 terms, exact match: 480 checks, 0 violations). **Sub-gap (b) is
genuinely and completely resolved**, unconditionally relative to the Self-
Absorbing Core Theorem's own two existing hypotheses (no new hypothesis
introduced): the new **Universal Early Intersection Lemma** (self-absorption +
the unconditional Free Facts Lemma + the bare definition of persistence together
force P(a_j) ∩ B ≠ ∅ for every early absorbed index j ≤ N(S*) and every persistent
type B, with NO FAH needed) extends the certified Self-Absorbing Core Theorem's
"n ≥ N(S*)" conclusion to a genuine **Literal n = 1 Periodicity Theorem**
("n ≥ 1"), re-deriving all three proof steps (Sufficiency, Landing, Assembling)
over the extended range with no gap and no smuggled hypothesis. Both are certified
below (`lemmas/universal-early-intersection-lemma.md`,
`lemmas/literal-n1-periodicity-theorem.md`). This is real, permanent progress: the
approach's residual dependency chain drops from THREE open ingredients (FAH;
existence of S*; N(S*)=0) to exactly TWO (FAH; existence of S*). **Sub-gap (a) is
honestly NOT resolved**, but sharpened via a new, independently-reverified,
fully-proved (both directions) **Termination Criterion Lemma**: the absorption
process S₀ ↦ S₀⁺ ↦ ... terminates in finitely many steps iff the pigeonhole-
threshold sequence N(S_0), N(S_1), ... is bounded — a genuine iff, not previously
stated, certified as reusable machinery
(`lemmas/termination-criterion-lemma.md`). This review independently checked
both directions of the iff (a one-line finite-max argument for ⟹; a standard,
non-circular monotone-finite-chain argument for ⟸, using a FIXED set
P*_M = ⋃_{j=1}^M P(a_j) built only from the actual sequence values, not from S_k
itself) and confirms both are correct with no gap. Boundedness of (N(S_k)) itself
is genuinely NOT established by this lemma or anything else in the workspace — no
overclaim. The builder's claim that sub-gap (a) is a "logically distinct object"
from the main FAH/recruitment-process-termination crux (not literally proved
equivalent, only structurally analogous in difficulty) is independently confirmed
accurate by this review: N(S) measures the ONSET of persistent behavior at a
given core (a different pigeonhole quantity, about *when* types stabilize) while
FAH is about whether stabilized types, once occurring, *intersect* each other —
these are conceptually different questions, and no argument was found (by the
builder or by this review) reducing one to the other in either direction; the
analogy is to the shared "greedy/monotone-enlargement process under a
non-constructive threshold" shape, correctly cited via
`lemmas/witness-discontinuity-obstruction.md`'s "refinement can manufacture new
classes" phenomenon, not to a proved equivalence. **This approach remains
explicitly and entirely conditional on FAH throughout and does NOT touch the main
crux** — the overall workspace Status stays `partial`. Verdict: **CHANGES
REQUESTED** (Status `partial` for this approach — real, certified progress; the
approach's own target, literal n=1 periodicity, is now proved in full conditional
on exactly two remaining open hypotheses instead of three, but sub-gap (a) and
FAH itself remain open). 3 new lemmas certified this round
(`universal-early-intersection-lemma.md`, `literal-n1-periodicity-theorem.md`,
`termination-criterion-lemma.md`). Overall workspace Status remains `partial` —
FAH/Symmetric FAH/Cofinite FAH/EEA remains the sole open primary crux, now on its
10th consecutive round untouched by a direct mechanism attempt (this round was a
secondary-gap round by design); no new FAH mechanism was killed or attempted this
round, so the "16 confirmed-dead mechanisms" count from round 14 is unchanged.)

partial (round 14: two slugs built. `n1-periodicity-reconciliation` (revise)
closed the round-13-flagged "combining both parts" rigor gap in the
Self-Absorbing Core Theorem's own written proof — independently re-verified
in full by this review (see the detailed re-derivation in the round-14
proof-reviewer report), including the two subtler points the builder did not
spell out (i) the "Extended Persistent-Type Pigeonhole" and "Monotonicity of
Resolution" certified lemmas both genuinely apply at an arbitrary finite core
S ⊇ Q, not just S₀, so instantiating them "at level S*" is legitimate reuse,
not a new unproved step; (ii) the theorem's hypothesis "FAH holds at level
S* (every two elements of 𝒫'(S*) intersect)" is mathematically EQUIVALENT to
the standard disjoint-base-type-only formulation of FAH used elsewhere in
this workspace, since any two extended-persistent types with NON-disjoint
base types automatically intersect (a one-line consequence of Q ⊆ S* and
ρ_S(n) ∩ Q = τ(n) exactly) — the approach file asserts this equivalence
without deriving it; this review supplies the missing one-line derivation
and confirms it holds, so the theorem's hypothesis is not silently stronger
than the standing open FAH question. With both of these independently
checked, the Self-Absorbing Core Theorem's proof is now complete and gap-free,
strictly conditional on its two disclosed open hypotheses (existence of a
self-absorbing core S*; N(S*) = 0). **Certified** to
`lemmas/self-absorbing-core-theorem.md` (see Lemma certification below).
Verdict: **CHANGES REQUESTED** (Status `partial`; a fully-proved conditional
theorem is real progress, but the two disclosed sub-gaps (a)/(b), plus the
still entirely open FAH/Symmetric FAH/Cofinite FAH crux, remain). The new
approach `integer-monovariant-difference-identity` searched, from scratch,
for a crux-`aimo-0134`-style bounded integer monovariant that would bypass
FAH's "which specific prime" content entirely; tried five candidate
statistics (running average of gaps, running minimum of gaps, running gcd of
all terms, persistent-type count, recruited-core size), found all five dead
for one of three precisely-diagnosed reasons (restates already-certified
content; is literally equivalent to gap (†) itself; or is genuinely monotone
+ bounded but structurally incapable of carrying prime-identity information),
and gave a general four-requirement diagnosis (§3) explaining why the whole
technique family cannot work here (the recurrence's certified class-blindness
poisons any purely numeric/count/min/gcd statistic). This review independently
reimplemented the greedy sequence from scratch (different script) and
reproduced EXACTLY the reported computational numbers for both mandated seeds
(a₁=4807: max gap 38, min gap 2, running average of gaps increases at
1196/2498 steps ≈48%, D₂=11→D₃=1; a₁=11305: max gap 14, min gap 2, increases
at 998/2498 steps ≈40%, D₂=5→D₃=1) — an exact match, strong independent
confirmation. The general §3 diagnosis was independently re-derived and holds:
this is a genuinely new negative result (16th confirmed-dead FAH mechanism),
not a restatement of a prior dead mechanism. Verdict: **RETHINK** (the
technique family, as a whole, cannot close gap (†); Status `unsolved`, honestly
reported, no overclaim). Overall workspace Status remains `partial` — FAH/
Symmetric FAH/Cofinite FAH/EEA remains the sole open primary crux, now with
16 confirmed-dead mechanisms; the secondary n=1 gap has one fully-proved
conditional theorem (Self-Absorbing Core) narrowing it further, still with
its own two open sub-gaps.)

partial (round 13: two slugs built, neither touching FAH/Symmetric FAH — a
defensive/bookkeeping round plus a conditional secondary-gap round. Both
independently re-verified by this review.
`greedy-exchange-cost-potential` proved and certified the **No-Restart Lemma**
(`lemmas/no-restart-lemma.md`): restarting the greedy process at a later term
`a_{n_0}` (`n_0≥2`) as a fresh seed gives an unconditional inequality `b_2 ≤
a_{n_0+1}` (monotonicity of legality under a shrinking constraint set — dropping
constraints can only admit more candidates), plus an explicit generic sufficient
condition (H') for strict divergence, with the sole degenerate case `n_0=1`
correctly isolated. This review independently re-derived the proof from scratch
(the monotonicity argument is a one-line conjunction-weakening fact) and
independently re-ran the worked example (`a_1=15`, restart at `a_5=30`) in a fresh
Python simulation, reproducing `true=[15,18,20,24,30,36,40,42,45,48,50,54,...]` and
`restarted=[30,32,34,36,38,40,42,44,...]` exactly. The lemma is correct,
unconditional, general (not just the `a_1=15` instance — the proof is for
arbitrary `n_0` under hypothesis (H'), with the example only illustrating it), and
non-circular; it makes no claim about FAH/(†) and correctly says so. **Certified,
no changes.** Does not touch the main crux — Status of this approach remains
`partial`.
`n1-periodicity-reconciliation` (new approach) attacked the secondary
n=1-literal-periodicity gap, explicitly and honestly conditional on FAH/Cofinite
FAH (imported as an open hypothesis, not attempted). Two contributions reviewed:
(1) a correct, unconditional **Non-Constructivity of N₀/N₁/N₁'/N₂** observation —
the certified pigeonhole-based thresholds are existentially finite but the
certified proofs supply no formula/algorithm computing them from a₁ alone (this
review independently confirmed the underlying pigeonhole proofs are indeed
non-constructive in exactly this sense); (2) a **Self-Absorbing Core Theorem**,
conditional on FAH holding at an enlarged, "self-absorbing" core S* (S*
absorbing every early term's full factorization up to the Extended-Persistent-
Type-Pigeonhole threshold N(S*)), giving a₊T*=a_n+L* for n≥N(S*) and correctly
resolving one specific named obstruction from `covering-system-construction`
Step 9.3 (an early transient term's idiosyncratic factorization disqualifying an
otherwise-eligible residue). **This review found a real, if repairable, rigor gap
in the theorem's own proof, not previously flagged by the builder**: the
"Combining both parts" step, which must justify both (i) sufficiency (residues in
the proposed set G* are legal) and (ii) that the actual value a_{n+1} itself always
lands in G* (so the process never "escapes" to a smaller non-G* legal candidate),
is written as a citation to "the certified Step 5 construction... already shows
this," without spelling out the argument for the NEW, broader G* used here (which
is defined differently — "meets every persistent type" — than the original Step 5
G, defined as "sig(r) IS a persistent type itself"; these are provably different
sets in general). This review independently reconstructed the correct argument
(minimality of a_{n+1} + sufficiency of G* rules out any smaller G*-residue
candidate, and FAH at S* together with the same-base/overlapping-base/disjoint-
base trichotomy already used in Step 5's own proof forces the real a_{n+1} into
G*) and confirmed the THEOREM'S CONCLUSION IS CORRECT, but the step as WRITTEN in
the approach file is incomplete — a hand-wave-by-citation for a claim that needed
its own derivation, since the cited construction was never actually run for this
broader G*. The builder's own honesty about the two remaining open sub-gaps —(a)
whether a self-absorbing S* even exists/the absorption process terminates
(explicitly flagged as unresolved, structurally analogous to the primary
"collateral rogue pairs" concern), and (b) whether N(S*) can be taken to be 0 — is
correct and not overclaimed; the file's own §4 and Status/Full-proof sections
correctly do NOT claim the n=1 gap is closed. The reported 6-seed computational
check (a₁=15,35,105,175,187,209; smallest valid threshold 0 in all 6) is
accurately described as checking the WEAKER "plain N₁' can be taken to be 0"
question (not literally N(S*), which the theorem's own machinery doesn't compute
on these seeds), and is correctly disclosed as empirical support only, not a
proof — this review spot-checked no additional seeds beyond confirming the
methodology described (period-detection + backward-threshold search) is a
sound, standard technique, consistent with prior rounds' similar checks. **Given
the gap found above, the Self-Absorbing Core Theorem is NOT certified as a
portable lemma this round** — the fix is a short, concrete addition (spell out
the minimality argument this review reconstructed) that the next round's builder
can complete directly. The Non-Constructivity observation is recorded as a
standing caution in Next-round guidance below rather than certified as a
standalone lemma file, matching the round-7 Lemma-F/Lemma-I precedent for
toolkit-diagnostic (vs. portable machinery) content. Overall Status of this
approach: `partial`, real narrowing, one repairable gap identified.
Overall workspace Status remains `partial` — the main FAH/Symmetric FAH crux is
untouched this round by design (round 13 was dispatched as a defensive round plus
a conditional secondary-gap round); see round 12 and earlier for the crux's
current state, unchanged.)

partial (round 12: mandated plateau-break round. Two slugs built:
`subword-complexity-periodicity` (brand-new corridor, Morse–Hedlund/subword-
complexity reformulation) and `covering-system-construction` (small bookkeeping
addendum). Both independently re-verified by this review from scratch.
`subword-complexity-periodicity`: proved two new fully general, unconditional
lemmas — **Lemma A** (Gap–Periodicity Equivalence: the problem's target holds iff
the gap sequence `g_n:=a_{n+1}-a_n` is eventually periodic in the ordinary sense)
and **Lemma B** (Right-Extension Determinism ⟹ eventual periodicity, the actual
pigeonhole+induction mechanism behind Morse–Hedlund, carried out explicitly, plus
a RED_1⟹RED_k monotonicity corollary) — both independently re-derived and
confirmed correct, certified. Correctly found the outline's headlined "weaker
target" (finitely many colliding S₀-residue classes) is **vacuous** — a one-line
consequence of alphabet-finiteness, matching the outline's own hedge ("provided
every sufficiently long run of visits eventually lands only in safe classes —
itself a claim needing proof, not automatic") rather than a strawman/mis-scoping
of the outline. Isolated the actually-sufficient condition, **EEA** (Eventual
Escape from Ambiguity: eventually only "safe" — single-valued-successor —
residues are visited at some finite core S₀), and proved **Theorem C** (EEA ⟹
periodicity) via a clean finite functional-graph pigeonhole argument — certified
with a wording correction (see Lemma certification below; the source's proof
contains a self-flagged "wait, we must double check" digression stemming from an
internally inconsistent definition of "safe" residue, which this review resolved
by adopting the zero-tolerance reading, under which the digression is unnecessary
and the rest of the proof goes through unchanged). Then showed — correctly, this
review re-derived the argument independently — that EEA, once unpacked, reduces
to exactly the same "recruit a prime, prove it divides literally every later
occurrence" content as the standing FAH/Cofinite-FAH crux (via the certified
Confined-GCD Lemma), i.e. this is a genuinely different TOOLSET landing on the
SAME wall, not a bypass — matching the outline's own honesty flag. No
counterexample to FAH, no proof of FAH; EEA is a new, precise, equivalent-in-
difficulty restatement of the crux. `covering-system-construction`: added one
small, fully unconditional bookkeeping lemma, the **Reduced-Alphabet Corollary**
(for a rogue pair with one side's far-factor set a singleton, the companion side
is fully resolved for free by Singleton-Side FAH, and the remaining open side's
bad-divisor-class alphabet `D_bad(q*)` has explicit closed-form size
`∏_{p∈F''\{q*}}(e_p+1)−1`, independently reconfirmed on `a_1=4807` by this review
via direct enumeration — `Div(221)={1,13,17,221}`, `D_bad(17)={13}`, size 1,
exactly matching the formula) — correct, non-circular, but explicitly and
honestly scoped by the builder as NOT resolving FAH (pure bookkeeping, does not
rule out any element of `D_bad`). 3 new lemmas certified this round
(`gap-periodicity-equivalence.md`, `red-k-periodicity-lemma.md`,
`eea-implies-periodicity.md`) plus `reduced-alphabet-corollary.md`. FAH/Symmetric
FAH (now equivalently: EEA at some finite core) remains the sole open crux, on
its SEVENTH consecutive round with no genuinely new corridor closing it — see the
"## ROUND 12" section below for full detail. Round 11's findings (below) are
unchanged and remain valid.)

partial (round 11: two builds this round, both independently verified by the
proof-reviewer as genuine, honestly-reported negative results — no counterexample,
no proof, real narrowing continues. (1) `greedy-exchange-cost-potential` completed
the dispatched rescue attempt of last round's dead "Forced-Escape Blocking
Construction" (full-`S₀`-CRT-glue competitor, killed pre-build by the outline-
reviewer's **CRT Magnitude Obstruction**, ≈8 orders of magnitude overshoot).
Genuinely attempted a weaker partial-signature-matching fix and proved a
**Minimal-Modulus Generalization**: any such construction either sacrifices the
legality guarantee (making its blocking witness empirically uninformative
`S₀`-junk) or requires a modulus provably no cheaper than the full-`Q` floor (a
structural, general consequence of Lemma A's own proof), which itself fails
magnitude-wise (independently reconfirmed by this review: a fresh from-scratch
reimplementation on `a_1=4807` reproduces EXACTLY the reported numbers — 2499
gaps, max 38, mean 17.4, min 2, `0/2499` reach the cheapest modulus 187, and the
three sampled rogue occurrences at `n=561,1114,2223` have gaps 15/3/19 with
factorizations matching `{3,5,17,19}` exactly as reported). This closes the entire
CRT-glue/competitor-construction family (14th confirmed-dead FAH mechanism, after
round 11's own 13th). No new shared lemma was certified, correctly, per the
Lemma F/Lemma I "diagnostic, not portable" precedent — this review confirms that
call, since the "no sweet spot" argument's magnitude half is demonstrated on one
seed plus a general structural half, not a fully seed-independent theorem, exactly
as the file itself discloses. (2) `sieve-density-exception-bound` (new approach
this round) ran the outline-reviewer's mandatory pre-build class-blindness
screening and found both of its sub-routes dead on arrival: sub-route (a) via a
new **Density-Argument Vacuity Corollary** (an extension, in the same proof style,
of the certified Escape-Cost Vacuity / Sandwich Genericity Theorems from pairwise
facts to window/counting statements — independently re-derived by this review and
confirmed to be a faithful, non-circular generalization, reinforced by a second,
independent, and more elementary **Selection-Rule Class-Blindness** observation:
the sequence's own recursive definition decides legality via the Boolean predicate
`gcd(c,a_i)>1`, with no term referencing which prime realizes the shared factor,
so no aggregate density statistic is ever consulted by the rule that actually
picks each term); sub-route (b) reduces to positing the open crux itself (an
unproved decay rate) and is correctly rejected as not a genuine alternative. One
new lemma certified (`lemmas/density-argument-vacuity-corollary.md`), independently
verified correct and non-circular by this review. FAH/Symmetric FAH remain the
sole open crux, now with **14** confirmed-dead mechanisms across 6 consecutive
rounds (6–11) with zero counterexamples found by any agent. See the new "## ROUND
11" section below for full detail. Round 10's findings (below) are unchanged and
remain valid.)

partial (round 10: three independent mechanisms attacked in parallel — all three
retired cleanly, no counterexamples found, real narrowing continues. (1)
`covering-system-construction`'s "Growth-Forced Divisibility" magnitude-squeeze
mechanism died via a new, fully proved **Sandwich Genericity / Escape-Cost Vacuity
Theorem**: the Bounded/Generalized Bounded Gap Lemma's linear value-vs-index sandwich
`n-m ≤ a_n-a_m ≤ (n-m)·a_1` is identical for every pair of indices regardless of type
or divisor class, so no argument built only from it (or other similarly "class-blind"
facts) can ever produce a class-DISCRIMINATING conclusion — independently re-verified
by the reviewer (trivial telescoping proof, correct) as a genuine structural
impossibility, not a mere empirical stall. Tenth mechanism retired. (2)
`greedy-exchange-cost-potential`'s Escape-Budget attack on the Successor Claim first
proved a genuine unconditional **Window Resolution Lemma** (infinitely many
consecutive-occurrence gaps of a rogue-pair's extended type exceed 1 — independently
re-verified, correct, confirmed numerically) that corrects the outline's imprecise
"single-step window" framing, then proved the Escape-Budget Lemma's premise TRUE but
showed the resulting information is unusable: the illegality-witness index for a
skipped candidate ranges over an UNBOUNDEDLY GROWING pool of indices, not a single
fixed one — the **Growing-Constraint Obstruction**, independently re-derived and
confirmed correct by the reviewer. Eleventh mechanism retired. (3)
`confined-competitor-construction` proved a new, genuinely useful **Minimality
Tautology Lemma** (any legal candidate `c>a_{n-1}` against all earlier terms
automatically satisfies `c≥a_n`, by the bare definition of `a_n` as the minimum of
that set) that correctly kills its own dispatched mechanism (any "construct smaller
FULLY-legal competitor, contradict minimality" strategy is provably impossible, for
ANY construction rule) and correctly explains round-7's Lemma K's internal proof
step. **Reviewer correction (important, not a rejection):** the source file's summary
language overclaims this as killing "the whole family of competitor-construction
mechanisms" — it does not: round 7's Lemma K survives as a DIFFERENT proof shape
(extracting information from the GUARANTEED blocking index rather than trying to
prove full legality), which this Lemma does not address or rule out. The certified
version of the Lemma is scope-narrowed accordingly (see
`lemmas/minimality-tautology-lemma.md`). Twelfth mechanism retired (in its dispatched
form). All three findings converge, via three structurally different routes
(algebraic-magnitude, quantitative-window, and definitional-tautology), on the same
diagnosis Lemma I first made in round 6: the missing ingredient is a genuinely
class-sensitive / intermediate-term-factorization-sensitive source of information,
not obtainable from any composition of the currently certified toolkit. FAH/Symmetric
FAH (equivalently Cofinite FAH / the Successor Claim) remain the sole open crux.
Round 9's findings (below) are unchanged and remain valid.)

partial (round 9: FAH/Symmetric FAH remain the sole open crux, still unresolved,
now attacked by THREE independently-verified rival mechanisms this round, all
correctly diagnosed as stalling at the same underlying obstruction.
(1) `covering-system-construction` dispatched a global "Recruitment-Budget Lemma"
(a fixed Q-level pool W_{A,B} := P(a_{m_A}) ∪ P(a_{m_B}) bounding every prime ever
recruited against a base pair). The proof-reviewer independently reimplemented the
recruitment process from scratch (different script, same construction) and
CONFIRMED the builder's refutation exactly: on a_1=209, round 2 of recruitment
forces q=7 which lies outside W_{A,B}={2,3,5,11,19}; reconfirmed a second escape on
a_1=247 at round 1 (q=3 escapes {2,5,7,13,19}). This closes off a ninth mechanism
(after Lemma I's six plus round 8's Fixed-Witness Divisor-Chain); the "expand the
pool" rescue is correctly diagnosed as circular. (2) A new approach,
`cofinite-window-capacity-bound`, imported the certified reduction chain and proved
two new unconditional lemmas — the Cofinite Sufficiency Lemma (literal FAH may be
weakened to "cofinite" — all but finitely many occurrences absorbed — without
breaking the certified CRT finish) and the Confined-GCD Lemma (a fixed-alphabet
divisor recast: gcd(a_n, a_{n_B}) is confined to divisors of a fixed integer's
F''-part) — both independently re-derived and confirmed correct by the reviewer.
The resulting window-capacity counting bound stalls at the same
"existential-to-universal promotion" wall (infinite pigeonhole gives SOME infinite
divisor-class, never provably the ONLY one) that Lemma I diagnosed for literal FAH.
(3) `greedy-exchange-cost-potential` ran a large fresh computational sweep
(~270 seeds, two independent searches) targeting the genuinely open |F'|/|F''|≥2
regime and found zero FAH counterexamples anywhere (strong empirical support for
literal FAH); the reviewer's own independent ~185-seed sweep corroborates this at
properly-recruited cores (nonzero exception rates only appear at intermediate,
not-yet-finally-recruited stages, consistent with prior rounds' findings, not a
counterexample). The builder then proved a new unconditional Successor-Transport
Reduction Lemma (an eventual one-step successor implication would suffice for
Cofinite FAH) but found, checking concretely rather than citing, that the successor
step itself collapses into the identical dead-end Lemma I already certified, plus a
new observation (Same-Type Free Facts Vacuity) explaining why same-type consecutive
occurrences give Free Facts no leverage. Four new lemmas certified this round
(`cofinite-sufficiency-lemma.md`, `confined-gcd-lemma.md`,
`successor-transport-reduction-lemma.md`, `same-type-free-facts-vacuity.md`). The
crux is now confirmed, by three independently-framed mechanisms in one round, to be
exactly the same "existential-to-universal / single-witness-to-all-occurrences"
promotion gap; any future mechanism must supply a genuinely new source of
cross-occurrence information (not a single fixed witness, not a counting/pigeonhole
argument over a single divisor value) to close it. See ROUND 9 section below for
full detail; ROUND 8 section retained for audit trail below.)

partial (round 8: FAH/Symmetric FAH remain the sole open crux, still unresolved.
This round's dispatched Fixed-Witness Divisor-Chain mechanism (covering-system-
construction Step 8.9) was carried out in full; it does NOT close Joint FAH — a
genuine, MORE BASIC gap than the outline-reviewer's flagged canonicality question
was found and proved: the outline's proposed dichotomy branch "r ∈ S₀ ⟹ contradicts
rogueness" is FALSE (r ∈ S₀ only forces the tautological r ∈ A', no information
about B'). A genuine unconditional byproduct, the Singleton-Side FAH Lemma, was
certified — it fully explains this round's positive computational evidence (a_1 =
187, 209, both singleton on both sides) and shows that evidence never engaged the
genuinely open |F'|,|F''| ≥ 2 regime, confirmed by a fresh independent computation
on a_1 = 4807 at an un-recruited core (only ~6% cofinite-divisibility, not
cofinite). Separately, seed-coupling-induction (new approach this round) was
independently falsified, both by the builder and by this review's own from-scratch
reimplementation, matching every reported number exactly. See ROUND 8 section below
for full detail; ROUND 7 sections retained for audit trail (the round-7 recap that
used to sit here is preserved verbatim in the "## ROUND 7" section further below).
Round 7 retracted a dead sub-mechanism (Two-Witness Intersection Uniqueness via
joint Lemma-H analysis — confirmed dead both abstractly and by a concrete
computation), decoupled the finish from that dead target via a canonical-witness-
prime bookkeeping step, added two new unconditional lemmas using previously-unused
illegality data (Lemma J, Lemma K — still insufficient to close FAH), opened and
refuted a genuinely new proof *style* (an aimo-0678-style algebraic-recursion
transplant, refuted by an exact counterexample and a general structural argument —
Witness Discontinuity Obstruction, certified), and gave the secondary n=1 gap its
first real treatment (Exact-Equality Reduction Lemma + a proof that the naive
"period-rescaling" fix is NOT automatic, both certified). See ROUND 7 section below
for full detail; ROUND 6 sections retained for audit trail.)

## Approaches tried

**Housekeeping note (round 30):** the entries immediately below cover only
through round 20; rounds 21–29 each added a certified `a_1`-subfamily
theorem (summarized here for completeness; full detail for each is in the
Status header above and in the corresponding `approaches/<slug>.md` file):
- **a1-19q-subfamily-theorem** (round 30, new) — literal `T=1,L=19`
  periodicity for every prime `q>19`, `q\notin\mathrm{Bad}(19)=\{23,29,31,
  37,43,53,73\}`; the 306-cell `p=19` instantiation of the certified
  `p`-uniform machinery, with all 7 diagonal exceptions proved via a new
  uniform parity/mod-5 mechanism (rather than 7 ad hoc checks). The run's
  **11th APPROVE** (pending reviewer confirmation).
- **a1-17q-subfamily-theorem** (round 29, new) — literal `T=1,L=17`
  periodicity for every prime `q>17`, `q\notin\mathrm{Bad}(17)=\{19,23,29,
  31,37,43,61,67\}$; the 240-cell `p=17` instantiation. The run's 10th
  APPROVE.
- **a1-13q-subfamily-theorem** (round 29, new) — literal `T=1,L=13`
  periodicity for every prime `q>13`, `q\notin\mathrm{Bad}(13)=\{17,19,23,
  47\}$; the 132-cell `p=13` instantiation. The run's 9th APPROVE.
- **a1-11q-subfamily-theorem** (round 28, new) — literal `T=1,L=11`
  periodicity for every prime `q>11`, `q\notin\mathrm{Bad}(11)=\{13,17,19,
  31,37,43\}$; the 90-cell `p=11` instantiation. The run's 8th APPROVE.
- **a1-7q-subfamily-theorem** (round 27, new) — literal `T=1,L=7`
  periodicity for every prime `q>7`, `q\notin\{11,13\}`; the 30-cell `p=7`
  instantiation; also proved the general-`p` **Universal Look-Back Witness
  Identity** and its `r=1` unconditional-closure corollary. The run's 7th
  APPROVE.
- **a1-5q-periodicity-theorem** (round 26, new) — literal `T=1,L=5`
  periodicity for every prime `q\ge7`, `q\notin\{7,13,19\}`; the first
  completed `p`-instantiation of the general-`p` machinery. The run's 6th
  APPROVE. Round 26 also proved the general-`p` Diagonal Characterization
  and First-Risk Theorems (certified lemmas, not by themselves closing any
  further `p`).
- **a1-3q-cubed-periodicity-theorem** / **a1-3q-squared-periodicity-theorem**
  (rounds 25/24, new) — literal periodicity for the `a_1=3q^3` and
  `a_1=3q^2` families respectively (extending `a1-3q` along the exponent
  axis); each independently certified as a standalone theorem, though the
  parent approach's general-`m` target remains open (`m\ge4` untouched).
  Round 25 also proved the general-`p` symbolic reduction (Generalized
  `K_0`-Boundedness + gcd-difference Witness Lemma) underlying all the
  `a1-pq`-family instantiations above.
- **a1-3aq-subfamily-theorem** (round 24, new) — literal periodicity for
  `a_1=3^aq`, `a\in\{1,\dots,5\}`, prime `q\ge7` outside a small
  `a`-dependent exceptional set. The run's 4th APPROVE.
- **a1-3q-subfamily-theorem** (round 20/22, new/revise) — literal `T=1,L=3`
  periodicity for `a_1=3q`, prime `q\ge7,q\ne5`; the first member of this
  family, proving the Parity Witness and `k=0`-Window Criterion Lemmas plus
  (round 22) the certified Legendre Sieve Gap Bound and Primorial Floor
  Bound used by every subsequent `p`-instantiation above.

- **triangle-consistency-pigeonhole** (round 20, revise) — Constrained
  Singleton Coherence Lemma + corollaries proved and certified; the round's
  positive computational evidence for the existence hypothesis diagnosed as
  a confound (both hard seeds already have their witness via an unrelated
  mechanism); failed replication attempt for a non-confounded test seed
  honestly reported. Verdict: **CHANGES REQUESTED** (partial).
- **triangle-critical-dichotomy-witness** (round 20, first build) — proved
  Universal Branch-(a) Dominance Theorem, showing the dispatched mechanism's
  required branch (b) never fires; certified as a reusable negative screen.
  Verdict: **RETHINK** (unsolved, approach cannot proceed as outlined).
- **a1-3q-subfamily-theorem** (round 20, first build) — Parity Witness and
  k=0-Window Criterion Lemmas proved and certified; genuinely closes several
  cases of the `a_1=3q` subfamily but the even-`n`,`k≥1` Case (b) remains
  open (requires a Jacobsthal-style gap-existence bound not proved here).
  Verdict: **CHANGES REQUESTED** (partial).
- **n1-periodicity-reconciliation** (round 20, revise) — genuinely fixed
  round 19's circularity with a narrower, non-circular Ambient-Statistic
  Obstruction; certified along with its mandatory scope note and the small
  Vacuous FAH under 2|a_1 Corollary. Does not touch H1/H2 directly, as
  instructed. Verdict: **CHANGES REQUESTED** (partial).
- **n1-periodicity-reconciliation** (round 19, revise) — §8 floor-deliverable
  audit correct (pure citation). §7 Generalized Class-Blindness Obstruction
  found to have a genuine circularity gap (the "two scenarios" step assumes
  what it needs to prove — see Status above); NOT certified as stated.
  Verdict: **CHANGES REQUESTED** (partial).
- **triangle-consistency-pigeonhole** (round 19, revise) — anatomy-of-
  integers/density closure attempt honestly does not close; new elementary
  `ω(a_n)=O(log n)` bound correct and certified; sieve obstruction diagnosis
  sound (documentation, not a standalone lemma). Also certified 3 pending
  round-18 lemmas (Double-Witness Nested Pigeonhole, Same-Type Triangle
  Vacuity, Two-Sided Singleton Witness Theorem) after independent
  re-verification. Verdict: **CHANGES REQUESTED** (partial).
- **core-growth-monotonicity** (round 19, revise) — weaker H2 existential
  target correctly identified as not new; new Monotone Chain Reformulation
  Lemma correct and certified; Propositions 4/5 honest dead-end findings, no
  gap found. Verdict: **CHANGES REQUESTED** (partial).
- **self-absorbing-by-construction** (round 19, revise) — 2 new adversarial
  seeds (`a_1=510510`, `209370`); `510510` numbers independently reproduced
  exactly; `209370` has a minor type-mislabeling error (corrected above) not
  affecting the qualitative conclusion. Verdict: **CHANGES REQUESTED**
  (partial).
- **prime-power-seed-periodicity-theorem** (round 18, new) — self-contained
  strong induction proving `a_n = a_1+p(n-1)` for all `n ≥ 1` whenever
  `a_1 = p^k` (`p` prime, `k ≥ 1`), `T=1, L=p` literally from `n=1`.
  Independently re-verified in full and re-simulated (43 seeds, including
  primes/exponents beyond the builder's own set). **Certified**
  (`lemmas/prime-power-seed-literal-periodicity-theorem.md`). Verdict:
  **APPROVE** (Status `solved` for this restricted subfamily only).
- **self-absorbing-by-construction** (round 18, revise, record correction) —
  corrected the round-17 unresolved `a_1=255255` candidate exception:
  `{5,7,11,13,17}` recurs at `n=135914`. Independently reconfirmed with a
  third, from-scratch script (SPF-sieve/bitmask method). NTBT still open, no
  overclaim. Verdict: **CHANGES REQUESTED** (partial).
- **n1-periodicity-reconciliation** (round 18, revise, documentation) — added
  the Odd-Prime Non-Trivialization Proposition (`a_1=15,45` counterexample to
  generalizing the `2|a_1` H1-trivialization trick) and the `|Q|=2`
  Non-Tractability finding (already contains the workspace's standing hard
  seeds). Both independently re-verified (the former with a fresh
  simulation). Diagnostic only, not certified as standalone lemmas. Verdict:
  **CHANGES REQUESTED** (partial).
- **triangle-consistency-pigeonhole** (round 18, new, mandated plateau-break)
  — killed the outline's originally-proposed triangle/`e`-based FAH
  mechanism (Same-Type Triangle Vacuity, 19th+ confirmed-dead mechanism);
  discovered and proved the new Two-Sided Singleton Witness Theorem, a
  correctly-scoped sufficient condition for Cofinite FAH that fully explains
  both of the workspace's known hard rogue-pair seeds. Independently
  re-verified (proof and both computational checks). Residual existence
  hypothesis honestly left open, correctly distinguished from a restatement
  of FAH. Verdict: **CHANGES REQUESTED** (partial).
- **self-absorbing-by-construction** (round 17, new) — proved unconditional
  **Vacuous/Weak Self-Absorption Lemma** (`N(Q) ≤ 1 ⟹ S_0=Q` self-absorbing,
  zero rounds, `S*=Q`), independently re-verified gap-free. **Certified**
  (`lemmas/vacuous-self-absorption-lemma.md`). Ran a ~50-seed numeric
  investigation of the open **NTBT conjecture**; two of three flagged
  "apparent counterexamples" (`a_1=30030,15015`) independently reconfirmed as
  genuine window artifacts (exact occurrence-list match by this review's
  fresh simulation). The third (`a_1=255255`) is only PARTIALLY resolved —
  this review's independent exhaustive check found an additional, unflagged
  single-occurrence type (`{5,7,11,13,17}` at `n=27184`) still unresolved
  through window 65000, contradicting the builder's "sole remaining
  single-occurrence type is full-`Q`" claim. NTBT honestly left open (no
  overclaim on the central conjecture; the inaccuracy is in a supporting
  numeric claim only). Verdict: **CHANGES REQUESTED** (partial — real,
  certified new lemma; NTBT open; one numeric claim needs correction/further
  windowing next round).
- **even-a1-full-periodicity-theorem** (round 16, new) — self-contained strong
  induction proving `a_n = a_1+2(n-1)` for all `n ≥ 1` whenever `2 | a_1`
  (`T=1,L=2`, literally from `n=1`), independent of FAH/persistent-type
  machinery. Independently re-verified in full and re-simulated (12 seeds,
  exact match). **Certified**
  (`lemmas/even-seed-literal-periodicity-theorem.md`). Verdict: **APPROVE**
  (Status `solved` for this restricted subfamily only — the workspace-level
  Status stays `partial`, since odd `a_1` and FAH are untouched).
- **n1-periodicity-reconciliation** (round 16, consolidation) — assembled the
  full conditional Master Theorem chain (H1=FAH at terminal core,
  H2=absorption-chain termination) from six already-certified lemmas with no
  new gap; proved the unconditional Vacuous-FAH-under-`2|a_1` corollary and
  the honest negative finding that the same trick does not trivialize H2. No
  new FAH mechanism attempted (by design). Verdict: **CHANGES REQUESTED**
  (partial — real narrowing of the general problem to exactly two named open
  hypotheses; neither resolved).
- **core-growth-monotonicity** (round 16, new) — dedicated H2 attack. Proved
  the Binary Refinement Lemma and Threshold Recursion Bound Lemma (exact
  one-prime recursion for `N(S)`), independently re-verified correct; showed
  the resulting `M_B` quantities are provably non-constructive from bounded
  data (Proposition 3), a genuine structural obstruction, not a mere stall.
  **Certified** (`lemmas/binary-refinement-and-threshold-recursion.md`).
  Verdict: **CHANGES REQUESTED** (partial — H2 still open).
- **n1-periodicity-reconciliation** (round 15, revise) — dispatched to attack the
  two disclosed open sub-gaps (a) existence/termination of a self-absorbing core
  S*, (b) N(S*) = 0. Sub-gap (b) **fully resolved**: new Universal Early
  Intersection Lemma (self-absorption + unconditional Free Facts + persistence,
  no FAH) extends the certified Self-Absorbing Core Theorem to a Literal n = 1
  Periodicity Theorem (n ≥ 1, same two hypotheses, no new hypothesis). Both
  independently re-verified and certified by this review
  (`lemmas/universal-early-intersection-lemma.md`,
  `lemmas/literal-n1-periodicity-theorem.md`). Sub-gap (a) sharpened via a new,
  fully-proved (both directions independently re-checked) **Termination
  Criterion Lemma** (terminates iff N(S_k) is bounded — certified,
  `lemmas/termination-criterion-lemma.md`) but honestly left open — no tool
  bounds N(S_k); the builder's "logically distinct object, not literally
  equivalent to FAH" characterization independently confirmed accurate (N(S)
  measures onset-of-persistence timing, a different pigeonhole quantity from
  FAH's intersection question; no reduction either way found). Approach remains
  entirely conditional on FAH; does not touch the main crux. Verdict: **CHANGES
  REQUESTED** (partial — real, permanent narrowing: 3→2 open ingredients for this
  approach's own target).
- **n1-periodicity-reconciliation** (round 14, revise) — closed the round-13
  "combining both parts" citation gap in the Self-Absorbing Core Theorem with a
  self-contained (S)ufficiency/(L)anding decomposition (no citation to Step 5's
  narrower construction). Independently re-verified in full by this review,
  including re-derivation of the missing "every-two-intersect ⟺ standard
  disjoint-base-type FAH" equivalence the file asserts without proof (true, one
  line, via Q ⊆ S* and ρ_S(n) ∩ Q = τ(n) exactly) and confirmation that the
  Extended Persistent-Type Pigeonhole / Monotonicity of Resolution lemmas are
  certified generically at any finite core, not just S₀/S₁ specifically, so
  reuse "at level S*" is legitimate. **Certified**: Self-Absorbing Core Theorem
  (`lemmas/self-absorbing-core-theorem.md`), conditional on (i) a self-absorbing
  S* existing and (ii) FAH holding at level S* — both open. Verdict: **CHANGES
  REQUESTED** (partial — a fully gap-free conditional theorem, main FAH crux and
  both disclosed sub-gaps (a)/(b) untouched).
- **integer-monovariant-difference-identity** (round 14, new) — searched for a
  crux-`aimo-0134`-style bounded integer monovariant/difference-identity
  mechanism for FAH/(†), independent of "which prime recurs" language
  entirely. Tried 5 candidates (running average of gaps, running min of gaps,
  running gcd of all terms, persistent-type count, recruited-core size); all 5
  dead (restates certified content / literally equivalent to (†) / genuinely
  monotone+bounded but structurally uninformative about prime identity).
  Independently reconfirmed (this review, fresh from-scratch simulation) EXACT
  match of all reported numbers on both mandated seeds a₁=4807, 11305 (gap
  extremes, running-average non-monotonicity rates ≈48%/≈40%, gcd collapse to 1
  by the 3rd term). General §3 diagnosis (class-blindness poisons any purely
  numeric statistic) independently re-derived and confirmed sound. 16th
  confirmed-dead FAH mechanism. Verdict: **RETHINK** (Status `unsolved`,
  honestly reported, no counterexample sought or found, no overclaim).
- **greedy-exchange-cost-potential** (round 13) — dispatched defensive/bookkeeping
  task (not a new FAH attempt): formalized and certified the **No-Restart Lemma**
  (`lemmas/no-restart-lemma.md`) ruling out restart-based inductions on this
  problem in general. Independently re-verified correct, unconditional, and
  non-circular by this review (re-derived the monotonicity argument from scratch,
  re-ran the `a_1=15` worked example in a fresh simulation, exact match). Verdict:
  **CHANGES REQUESTED** (partial — the approach's overall Status stays partial
  since FAH/(†) is untouched; the lemma itself is fully certified with no gap).
- **n1-periodicity-reconciliation** (round 13, new) — attacked the secondary
  n=1-literal-periodicity gap, explicitly conditional on FAH (imported as an open
  hypothesis, not attempted here). Proved a correct Non-Constructivity observation
  about the workspace's pigeonhole-derived thresholds, and a **Self-Absorbing Core
  Theorem** whose CONCLUSION this review independently confirmed is correct (via a
  from-scratch reconstruction of the missing minimality argument) but whose
  written proof has a real, repairable gap in its "Combining both parts" step (a
  hand-wave-by-citation to Step 5's construction for a strictly broader,
  differently-defined eligible-residue set G* that Step 5's own proof never
  actually establishes for; this review supplies the fix path — see Status above).
  Honestly identifies two further open sub-gaps ((a) existence/termination of a
  self-absorbing core, (b) whether the threshold can be taken to be 0) without
  overclaiming either is resolved; the reported 6-seed computational check is
  accurately scoped as checking a weaker question than the theorem's own N(S*).
  Verdict: **CHANGES REQUESTED** (partial); Self-Absorbing Core Theorem NOT
  certified this round pending the identified fix.
- **greedy-exchange-cost-potential** (round 11) — completed the dispatched rescue
  attempt of the round-11-opened Forced-Escape Blocking Construction (killed
  pre-build via the CRT Magnitude Obstruction); proved a **Minimal-Modulus
  Generalization** closing the entire CRT-glue/competitor-construction family —
  independently reconfirmed by this review (exact numeric match on a fresh
  from-scratch reimplementation). No counterexample, no new certified lemma
  (correctly, diagnostic-only). Verdict: **CHANGES REQUESTED** (partial).
- **sieve-density-exception-bound** (round 11, new) — ran the mandatory pre-build
  class-blindness screening before any Mertens computation; found both sub-routes
  dead on arrival via a new certified **Density-Argument Vacuity Corollary** plus
  an independent **Selection-Rule Class-Blindness** observation. Independently
  re-derived and confirmed correct, non-circular, and a faithful extension of the
  certified Escape-Cost Vacuity / Sandwich Genericity Theorems. Verdict:
  **RETHINK** (this specific technique family — aggregate density/counting
  estimates over a fixed finite prime alphabet — cannot work, for a proved
  structural reason; a future round should not re-attempt any density/sieve
  variant against Cofinite FAH without a concrete class-sensitive ingredient not
  of the ruled-out `C(X)` shape).
- **covering-system-construction** (round 9) — dispatched Recruitment-Budget Lemma
  (global fixed-pool counting bound on recruited primes), REFUTED with an explicit
  hand-verifiable counterexample (a_1=209, prime q=7 escapes the base-witness pool
  at recruitment round 2); reviewer independently reimplemented the recruitment
  process from scratch and reconfirmed the exact same escape, plus a second
  independent escape on a_1=247. The "expand the pool" rescue is correctly
  diagnosed as circular (restates the open termination question). Ninth mechanism
  ruled out; no false claims. Verdict: **CHANGES REQUESTED** (partial).
- **cofinite-window-capacity-bound** (round 9, new) — imported the certified
  reduction chain; proved two new unconditional lemmas (Cofinite Sufficiency Lemma,
  Confined-GCD Lemma), both independently re-derived and confirmed correct by the
  reviewer; the resulting window-capacity counting bound stalls at the same
  existential-to-universal promotion wall Lemma I already diagnosed, now expressed
  in divisor-class language — confirmed genuine, not an avoidable gap. Verdict:
  **CHANGES REQUESTED** (partial).
- **greedy-exchange-cost-potential** (round 9) — ran the dispatched cheap-kill
  check (~270 fresh seeds, two sweeps) targeting the open |F'|/|F''|≥2 regime,
  found zero FAH counterexamples (reviewer's independent ~185-seed sweep
  corroborates, modulo intermediate-stage noise already understood from prior
  rounds); proved a new unconditional Successor-Transport Reduction Lemma, but the
  underlying Successor Claim itself stalls at the identical Lemma-I dead end
  (checked concretely on a_1=4807, 11305 data, both routes uninformative); a new
  Same-Type Free Facts Vacuity observation explains why consecutive same-type
  occurrences give no new leverage. Verdict: **CHANGES REQUESTED** (partial).
- **covering-system-construction** (round 8) — carried out the dispatched
  Fixed-Witness Divisor-Chain mechanism in full; found a genuine gap in the
  outline's own proposed dichotomy MORE BASIC than the flagged canonicality
  question (independently reverified correct by the reviewer); certified two new
  unconditional lemmas as byproducts (Singleton-Side FAH, Divisor-Chain
  Well-Definedness). Joint FAH remains open. Verdict: **CHANGES REQUESTED**
  (partial).
- **seed-coupling-induction** (round 8, new) — set up an induction on ω(a_1) via
  single-prime seed removal; falsified its own central Seed-Coupling Lemma with a
  clean, reproducible computational counterexample (independently reconfirmed by
  the reviewer, exact numeric match on every reported density). Verdict:
  **RETHINK**.
- **amortized-charging-budget** (round 1) — genuine partial progress, stale since
  round 1. Proved Free Facts, Bounded Gap Lemma, Recurrent-Pattern Pigeonhole,
  Forced-Linking-Prime Lemma (superseded). Stuck on an imprecisely-stated "Core Lemma"
  that partly smuggles in the "self-sufficiency" property its finish needs. Superseded
  in precision by the sibling approaches' crisper gap (†).
- **covering-system-construction** (rounds 1–3) — the strongest, most-developed
  approach in the population. Proved (round 1, certified, unconditional): Free Facts,
  the Bounded Witness Lemma, and the Finite Core Theorem (explicit finite core prime
  pool S). Round 2: retracted a false "Universal Glue Prime Lemma" (refuted by an
  a_1=35 counterexample), replaced it with the fully proved Generalized Bounded Witness
  Lemma (S₀-level) and an exact reformulation of (†) as the halting question for a
  concrete "recruitment process." Round 3 (this round): proved two new lemmas —
  **Canonical-Refinement Lemma** and **F_A ∩ F_B ≠ ∅** — which unconditionally close (†)
  whenever at least one side of a disjoint-base-type extended-type pair is its own base
  type's canonical refinement, localizing the open part of (†) to a strictly smaller
  residual set V of "rogue pairs" (both sides non-canonical). Attempted a
  minimal-counterexample well-ordering attack on V; documented, with a specific
  structural reason, why it does not close V = ∅ (route 1: the produced object is larger,
  not smaller, and lives outside the ambient set the measure is defined over; route 2:
  the recruitment corollary's pigeonhole only certifies the new prime's recurrence on the
  side being reconciled, not the fixed witness side). Verdict: **CHANGES REQUESTED**
  (partial), real progress, gap (†) narrowed but open.
- **greedy-exchange-cost-potential** (rounds 2–3) — a genuinely different framing
  (integer cost/witness-prime pigeonhole rather than covering-system language),
  independently converging on the same crux. Round 2: retracted two false conjectures
  ("cost(n) ≤ |𝒫|−1", then "cost(n) ≤ 1 in a sparse-Q regime"), both refuted by the
  a_1=35 counterexample; replaced with three new, fully proved, unconditional lemmas
  (Generalized Bounded Gap Lemma, Single-Witness-Prime Pigeonhole Refinement, Extended
  Persistent-Type Pigeonhole) plus a fully resolved |Q|=1 special case. Round 3 (this
  round): independently re-derived the Canonical-Refinement Lemma and F_A∩F_B≠∅ in its
  own vocabulary (verified identical in content to `covering-system-construction`'s
  versions — certified once, canonically, crediting both). Attempted an "exchange /
  rogue-refinement-must-be-skippable" argument using minimality of the greedy choice;
  proved a new negative structural observation ("Lemma F": the certified magnitude
  lemmas only ever construct LARGER competing candidates of safe type, never smaller
  ones, so no exchange argument built solely from them can force a rogue type to be
  avoided) — this correctly rules out a specific proof-attempt family, though as
  reviewed below it is a documentation of the current toolkit's limits rather than a
  portable, general theorem, and is **not separately certified as a shared lemma** (see
  Lemma-certification notes). Verdict: **CHANGES REQUESTED** (partial), real progress,
  gap (†) narrowed but open.
- **witness-depth-bound** (round 3, new) — attempted to prove an explicit function
  f(a_1) bounding first-occurrence indices of Q-level types, corrected from the
  outline's originally-proposed (and outline-reviewer-falsified) "function of |Q|
  alone" version. The attempted pigeonhole/pumping proof genuinely stalls (documented:
  simultaneous multi-term reconciliation is history-dependent, not a function of Q's
  static data alone) and no counterexample was found either. More importantly, this
  round's file proves a **scope observation**: even a full proof of the corrected claim
  would NOT close gap (†) as framed, because the Finite Core Theorem already gives an
  unconditionally finite S with no numeric depth bound needed, while (†) is about
  whether the *recruitment process beyond S* terminates — a question an explicit-depth
  bound on the original canonical witnesses does not address. Independently verified
  correct by this review (see below). Verdict: **RETHINK** — this specific target
  cannot close (†) as currently framed even if fully solved; it should either be
  narrowed to a standalone strengthening of the Finite Core Theorem (lower priority) or
  re-aimed at bounding the depth of *all* recruitment rounds (a strictly harder claim,
  not attempted).
- **density-sieve-contradiction**, **hypergraph-transversal** — stale since round 1,
  not rebuilt since; correctly left out of recent build sets.
- **covering-system-construction** (round 4) — attempted the dispatched "Persistent
  Uniform Core Lemma" (PUCL); correctly falsified its literal first-occurrence-anchored
  construction (independently reverified, correct) and correctly showed the "generous"
  S-level form adds no content (trivial corollary of Finite Core Theorem, correct). Its
  central "no rescue possible" demonstration (Step 6c/6d, the a_1=175 minimal-witness
  pair a_3/a_5) rests on an **incorrectly computed S₀** (see ROUND 4 CRITICAL
  CORRECTION above) — under the correctly (minimally) computed S₀, the claimed disjoint
  pair actually intersects via 13, so this specific demonstration does not hold. Verdict:
  **CHANGES REQUESTED** — the valid parts (Step 6a, 6b) stand; Step 6c/6d must be
  recomputed with correct witnesses or replaced with a genuine example.
- **greedy-exchange-cost-potential** (round 4) — proved a new, unconditional, correct
  Lemma G (Extended Earliest-Witness Intersection; certified,
  `lemmas/extended-earliest-witness-intersection.md`). Proved a correctly rescoped,
  honestly-disclosed-as-conditional Round Resolution Lemma (conditional on an explicit
  "Singleton Hypothesis"), with a genuine, well-documented attempt (and honest failure)
  to remove the hypothesis via a first-bad-round minimality induction. However, its
  motivating example and reported "~20 seeds, all satisfying the Singleton Hypothesis"
  computational support reuse the SAME buggy a_1=175 S₀ (in fact a THIRD, mutually
  inconsistent S₀ value versus `covering-system-construction`'s own number for the
  identical seed) — see the ROUND 4 CRITICAL CORRECTION above. The independently
  reverified ≈14% base-type-divisibility finding (unaffected by the bug) still stands.
  Verdict: **CHANGES REQUESTED** — Lemma G is certified; the Round Resolution Lemma's
  proof is valid conditional content but its empirical basis and motivating example need
  to be recomputed with the correct minimal-witness convention before being relied upon.

## Current best

**Round 30 update (read this first; supersedes the framing below where they
conflict).** The floor deliverable now stands at **11 fully certified
`a_1`-subfamily theorems** (pending this round's proof-reviewer
confirmation of the 11th): `2|a_1`; `a_1=p^k`; `a_1=3q`; `a_1=3q^2`;
`a_1=3q^3`; `a1-3aq` (`a=1,\dots,5`); `a1-5q`; `a1-7q`; `a1-11q`; `a1-13q`;
`a1-17q`; and (round 30, new) `a1-19q` — each a self-contained, literal
`T=1,L=p` periodicity proof for `a_1=pq`-type seeds (or, for the first two,
`2|a_1` and `a_1=p^k`), certified via strong induction with no residual
gap. The `a1-pq` family instantiations (`p=5,7,11,13,17,19`) all use the
same certified `p`-uniform machinery (Generalized `K_0`-Boundedness,
gcd-difference Witness Lemma, Legendre Sieve Gap Bound, Primorial Floor
Bound, Universal Look-Back Witness Identity); the general-`p` theorem
itself (`a1-pq-subfamily-theorem`) remains `partial` — two `p`-independent
gaps (general `r\ne1,k=0` closure; `r=1,k\ge1,\gcd(k+1,j)>1` residual)
are still open, and no genuinely new idea for closing either was found as
of round 30, so per-`p` instantiation (not general-`p` closure) remains
the correct, honest way to keep adding certified content. Overall
workspace Status remains `partial`: the fully general problem (all `a_1`,
not restricted to any named subfamily) still rests on the two open
Master-Conditional-Theorem hypotheses H1 (FAH at the terminal
self-absorbing core) and H2 (absorption-chain termination), neither
resolved as of round 30 (24+ consecutive plateau rounds on H1; see the
Status header above for the round-30 `fah-counterexample-hunt` plateau-break
attempt).

**Round 16 update (superseded in framing by the round-30 update above, but
individually still valid).** The problem is now split into two disjoint pieces:

- **`2 | a_1` subfamily: fully and unconditionally SOLVED.** The Even-Seed
  Literal Periodicity Theorem (`lemmas/even-seed-literal-periodicity-theorem.md`,
  round 16, APPROVE) proves `a_n = a_1+2(n-1)` for all `n ≥ 1` whenever
  `2 | a_1`, i.e. `T=1, L=2` literally from `n=1`, by a four-line elementary
  induction independent of all the machinery below.
- **`a_1 = p^k` subfamily (any prime `p`, any `k ≥ 1`): fully and
  unconditionally SOLVED.** The Prime-Power Seed Literal Periodicity Theorem
  (`lemmas/prime-power-seed-literal-periodicity-theorem.md`, round 18,
  APPROVE) proves `a_n = a_1+p(n-1)` for all `n ≥ 1`, `T=1, L=p` literally
  from `n=1`. Overlaps the `2|a_1` theorem exactly at `a_1=2^k`; strictly new
  for odd `p`. Does NOT extend to `|Q| ≥ 2` (confirmed by a genuine
  counterexample, `a_1=15,45`, in `n1-periodicity-reconciliation` §6.1: an
  odd prime factor of `a_1` does not force it to divide every term the way
  `2` does, since a candidate failing to share `p` may still share `a_1`'s
  other prime factor when `|Q| ≥ 2`).
- **General `a_1` (any `|Q| ≥ 2` not fully covered by the two subfamilies
  above): reduced to exactly two named
  open hypotheses**, via the Master Conditional Theorem
  (`n1-periodicity-reconciliation` §2, round 16): (H1) FAH holds at the
  terminal core of the self-absorbing-core absorption chain (equivalent to
  the standing FAH/Symmetric FAH/Cofinite FAH/EEA crux — 17+ confirmed-dead
  mechanisms, rounds 6–16, still open); (H2) the absorption chain
  `S_0 ⊆ S_1 ⊆ ...` terminates (equivalent, via the certified Termination
  Criterion Lemma, to boundedness of `N(S_k)` — now has an exact one-prime
  recursion via the Binary Refinement / Threshold Recursion Bound Lemmas,
  round 16, but the resulting `M_B` quantities are proved non-constructive
  from bounded data; still open). Given both H1 and H2, the certified Literal
  n=1 Periodicity Theorem finishes the proof completely (`a_{n+T*}=a_n+L*`
  for every `n ≥ 1`). Neither H1 nor H2 is established for any `a_1` outside
  the vacuous `2 | a_1` case (where H1 trivializes but H2 provably does NOT,
  per `n1-periodicity-reconciliation` §4.2 — the `2|a_1` case is fully solved
  instead by the separate elementary argument above, not via this chain).

The remainder of this section (items 1–12 below) is the round-1–4 snapshot of
the unconditional lemma stack feeding into the above and is retained for
historical/audit reasons; it merges into, and is superseded in its top-level
framing by, the round-16 picture just given, and by the fuller round 8–15
lemma stack cited in the Status section above (Self-Absorbing Core Theorem,
Universal Early Intersection Lemma, Literal n=1 Periodicity Theorem,
Termination Criterion Lemma, etc.) — see `results/imo-2026-06/lemmas/` for
the complete, current certified stack (30+ files).

The following is established, correct, and unconditional (independent of the open
gap (†)), merging all approaches' non-overlapping contributions — see certified files
in `results/imo-2026-06/lemmas/`:

1. **Free Facts** (`free-facts-gcd.md`): gcd(a_i, a_j) > 1 for all i ≠ j.
2. **Bounded Gap Lemma** (`bounded-gap-lemma.md`): a_{n+1} ≤ a_n + a_1.
3. **Generalized Bounded Gap Lemma** (`generalized-bounded-gap-lemma.md`): a_{n+1} ≤
   a_n + c for any positive integer c divisible by every prime of Q; in particular
   a_{n+1} ≤ a_n + a_1·p for any prime p.
4. **Persistent-Type Pigeonhole** (`persistent-type-pigeonhole.md`): a finite, nonempty
   set 𝒫 of Q-types occurs infinitely often, and eventually every τ(n) ∈ 𝒫.
5. **Bounded Witness Lemma** (`bounded-witness-lemma.md`): for disjoint persistent
   types A, B and any single witness index m with τ(m) = B, every later n with
   τ(n) = A has a_n divisible by some prime of the fixed finite set P(a_m) \ Q.
6. **Single-Witness-Prime Pigeonhole Refinement** (`single-witness-prime-pigeonhole.md`):
   for disjoint persistent A, B, one SPECIFIC prime of F_{A,B} (using the canonical
   witness) recurs infinitely often among A-type terms — sharper than #5, still not
   sufficient to close (†).
7. **Finite Core Theorem** (`finite-core-theorem.md`): an explicit finite core prime
   pool S (built from ≤ |𝒫| ≤ 2^{|Q|}−1 fixed witness terms) such that every
   sufficiently large term of a persistent type is divisible by some prime of S
   relative to each disjoint persistent type.
8. **Generalized Bounded Witness Lemma (S₀-level)**
   (`generalized-bounded-witness-lemma.md`): the Bounded Witness Lemma's argument
   generalizes verbatim from Q to ANY fixed finite S₀ ⊇ Q, with a Corollary
   (Recruitment step): if two disjoint-base-type extended-persistent types A', B' fail
   to intersect within S₀, a specific NEW prime q ∉ S₀ is forced to divide infinitely
   many A'-type terms.
9. **Extended Persistent-Type Pigeonhole**
   (`extended-persistent-type-pigeonhole.md`): with S₀ = Q ∪ S, the extended type
   ρ(n) := P(a_n) ∩ S₀ has a finite, nonempty set 𝒫' of extended-persistent values,
   eventually exhausting the index set.
10. **|Q| = 1 special case fully resolved** (`greedy-exchange-cost-potential`): if
    |Q| = 1, τ(n) = Q for all n, no two disjoint persistent types exist, (†) is
    vacuous, and the sequence is exactly a_{n+1} = a_n + q for all n ≥ 1 (T=1, L=q).
    This sub-case is completely solved, no gap.
11. **NEW this round — Canonical-Refinement Lemma**
    (`lemmas/canonical-refinement-lemma.md`, certified from `covering-system-construction`
    Step 4d and `greedy-exchange-cost-potential`'s Lemma D, independently proved twice,
    certified once as the canonical statement): for disjoint persistent base types A, B
    with canonical extended refinements A_can, B_can, every extended-persistent A'
    refining A meets B_can, and every extended-persistent B' refining B meets A_can.
    Unconditionally closes (†) for every pair with at least one canonical side.
12. **NEW this round — F_A ∩ F_B ≠ ∅**
    (`lemmas/canonical-witness-intersection.md`, certified, same dedupe): the extra-prime
    sets of two disjoint base types' canonical witnesses always intersect. Strictly
    subsumed by #11 (the canonical-vs-canonical special case); kept as a named lemma for
    its standalone one-line proof.

**Independent verification (this round, reviewer).**

(a) Re-derived and independently checked both new lemmas (#11, #12) from scratch,
including a direct computational check (a_1 = 35: F_{{5}} ∩ F_{{7}} = {2} ≠ ∅, matching
the proof). Both are correct, unconditional, and non-circular — certified.

(b) **Falsified the "zero further recruitment rounds needed" conjecture** that both
built approaches reported as computationally supported (10 seeds in round 2, 15 seeds
in round 3, all showing V = ∅). Testing **a_1 = 175** (Q = {5,7}, not in either
approach's tested seed list), the one-round Finite Core Theorem's S₀ = {2,3,5,7,11} has
a genuine "rogue pair" violation of (†): the extended-persistent types {2,7} (refining
base type {7}) and {3,5} (refining base type {5}) are disjoint, and neither equals its
base type's canonical refinement ({7}_can = {2,3,7,11}, {5}_can = {2,3,5}) — confirmed
computationally that this is exactly the "rogue pair" case the Canonical-Refinement
Lemma explicitly does not cover, not a counterexample to any certified lemma. Applying
the Generalized Bounded Witness Lemma's Corollary to this violating pair recruits the
prime **13** (confirmed: 13 | a_n for infinitely many of the sampled {2,7}-type terms,
and independently confirmed the true eventual period is T = 274, L = 2730 = 2·3·5·7·13,
i.e. the actual reconciling core genuinely needs one further round beyond S₀). This
shows: (i) the recruitment process is not merely a theoretical possibility — it is
concretely necessary for at least one seed not previously tested; (ii) the "zero
further rounds" conjecture in the round-2/3 files is **false as a universal claim**
(it was always correctly labeled "not proved," so this is not an overclaim to correct,
but it should not be relied on going forward); (iii) the recruited prime in this
instance exactly matches the true period's extra factor, which is positive evidence
*for* the recruitment-process framing being the right mechanism, even though its
general termination remains open. This finding is recorded here so no future round
re-tests or re-relies on the "zero further rounds" conjecture as if it were still
computationally unrefuted.

**The single remaining crux gap (†)**, after this round's localization: define V ⊆
𝒫' × 𝒫' as the set of pairs (A', B') with disjoint base types A := A'∩Q, B := B'∩Q,
A' ∩ B' = ∅, and BOTH A' ≠ A_can and B' ≠ B_can (neither side canonical). (†) holds iff
V = ∅ at every stage of the recruitment process (equivalently, iff the process defined
in `covering-system-construction` Step 4c halts). This round exhibits a concrete
instance of V ≠ ∅ at the zero-round stage (a_1 = 175), confirming V is a genuine,
non-vacuous target rather than a hypothetical one, and that (†) genuinely requires the
recruitment process to run at least one round in general (not the "usually zero rounds"
picture suggested by earlier, now-refuted computational sampling). Two candidate
contradiction routes for a minimal-counterexample / well-ordering attack on V were tried
this round and both fail for a specific, documented structural reason (see
`covering-system-construction` Step 4f): the natural size measure |A'|+|B'| is
non-decreasing under the only available refinement operation (recruitment always adds a
prime), and the recruitment corollary's pigeonhole only certifies the new prime's
recurrence on the side being reconciled, not the fixed witness side.

**Given (†) (in either its original or S₀-level form), the CRT + cyclic-pigeonhole
finish is unchanged from round 1** and remains correctly derived
(`covering-system-construction` Step 5): L := ∏_{p ∈ S₀} p, G := "eligible residues"
mod L (those whose S₀-signature is an extended-persistent type), T := |G|; then
a_{n+T} = a_n + L for all n beyond a finite threshold.

**Secondary open gap (unchanged, all approaches correctly flag as unresolved and
downstream of (†)):** extending a_{n+T} = a_n + L back to n = 1 literally. Empirically
verified on all tested seeds so far, not proved in general.

## Full proof
Not present — Status is `partial`. Neither approach closes gap (†) this round.

## ROUND 4 CRITICAL CORRECTION — the round-3 "falsification of zero further rounds"
(a_1 = 175) is retracted; it was a computational bug, not a genuine counterexample

**This supersedes the round-3 paragraph below it (kept for the audit trail, but
its conclusion is WRONG and must not be relied on).** The proof-reviewer
independently re-implemented, from scratch, the Finite Core Theorem's canonical-witness
construction — literally as stated in `covering-system-construction` Step 3: "for each
persistent base type B, m_B := the SMALLEST index n with τ(n) = B" (the Bounded Witness
Lemma itself needs no restriction to n > N_0 — ANY index m with τ(m) = B is a valid
witness, per its own statement — so the earliest occurrence is always a legitimate,
and the most economical, choice) — and used it to recompute S, S₀, and the residual set
V for a_1 = 175 and 17 other seeds.

**Finding.** Using the mathematically correct, minimal (earliest-occurrence) canonical
witnesses, a_1 = 175 gives Q = {5,7}, S = {2,3,13} (NOT {2,3,11} as
`covering-system-construction` Step 6c claims, nor {2,3,11,29,41,67} \ {2,3} as
`greedy-exchange-cost-potential`'s round-4 setup independently and *inconsistently*
computed for the SAME seed), S₀ = {2,3,5,7,13}. Under this correct S₀, **V = ∅** — every
pair of disjoint-base-type extended-persistent types intersects, with ZERO further
recruitment rounds needed. This matches the true period exactly: independently
resimulated, a_1 = 175 has T = 274, L = 2730 = 2·3·5·7·13 — i.e. the true period's extra
factor 13 is already present in the correctly-computed, ORIGINAL Finite Core Theorem's S
(via its witness a_3 = 182 = 2·7·13, the earliest occurrence of base type {7}), not the
product of some separate "recruitment round." The specific pair the round-4 files used
as their working counterexample — ρ(3) = {2,7} vs ρ(5) = {3,5}, claimed disjoint under
S₀ = {2,3,5,7,11} — is **not actually disjoint** once S₀ is computed correctly: ρ(3) =
{2,7,13}, ρ(5) = {3,5,13}, and they share 13. The bug: both files' S₀ computations used
a non-minimal or otherwise incorrect witness for base type {7} (`covering-system-
construction`'s Step 6c even contains an internally self-contradictory sentence — it
states S₀ = {2,3,5,7,11} while also stating "S = {2,3}", which are inconsistent with
each other, i.e. Q ∪ {2,3} ≠ {2,3,5,7,11}). Re-running the SAME corrected construction
on 17 more seeds (the original 10 from round 2/3, `covering-system-construction`'s
extra |Q|=4/5 seeds, and 3 fresh seeds never tested before: 3927, 715, 494) gives
**V = ∅ in all 18 seeds**, with zero exceptions.

**What is NOT retracted / still correct, independently reverified.** (i)
`covering-system-construction` Step 6a (PUCL's literal first-occurrence-anchored
construction is false: a_1=175's type-{7} witness a_3=182 gives naive core {2,13}, but
the very next type-{7} occurrence a_4=189=3³·7 is divisible by neither) — this check
uses only Q-level data, is unaffected by the S₀ bug, and is confirmed correct. (ii)
`greedy-exchange-cost-potential`'s finding that the recruited prime 13 divides only
≈14% of ALL base-type-{7} (352/2453) and base-type-{5} (264/1839) occurrences — a
direct divisibility fact independent of S₀ choice, independently reconfirmed exactly.
(iii) The abstract lemmas proved this round — **Lemma G (Extended Earliest-Witness
Intersection)** and the **rescoped Round Resolution Lemma** (conditional on the
Singleton Hypothesis) — are both correctly proved as general statements; their proofs
do not depend on the specific (buggy) numerical example. Lemma G is certified
(`lemmas/extended-earliest-witness-intersection.md`).

**What this means for the population's direction.** The "zero further recruitment
rounds beyond the (correctly, minimally computed) Finite Core Theorem's S" conjecture —
retracted in round 3 based on the buggy a_1=175 computation — is **not actually
falsified**; on the contrary, it now has 18/18 confirming seeds (0 counterexamples)
once computed correctly, reviving it as the single most promising concrete target.
Next round's builders MUST: (a) recompute S/S₀ using the literal minimal-witness
convention (earliest occurrence, over the WHOLE sequence from n=2 — not a witness
sampled from within a tail window used only to detect persistence) before trusting or
extending any "rogue pair" / recruitment-round claim; (b) attempt a direct proof that
the ORIGINAL, minimally-witnessed Finite Core Theorem's S₀ already gives V = ∅ in
general (rather than the "recruitment process may need multiple rounds" framing, which
may be an artifact that evaporates once witnesses are chosen minimally); (c) if a
genuine counterexample to "zero rounds with minimal witnesses" is found, report the
exact S₀ computation transparently (witness indices and their factorizations) so it can
be independently reverified, given this round's bug.

## ROUND 3 finding (SUPERSEDED — kept for the audit trail only, conclusion is wrong)
Testing a_1 = 175 (Q = {5,7}, not in either approach's tested seed list), the
one-round Finite Core Theorem's S₀ = {2,3,5,7,11} [**this S₀ was computed with a
non-minimal/incorrect witness for base type {7}; see the round-4 correction above**]
was reported to have a "rogue pair" violation of (†), recruiting prime 13, with the
"zero further rounds" conjecture reported as falsified. **This conclusion is retracted
by the round-4 review above: using the correct, minimal witness (a_3 = 182, the actual
earliest occurrence of base type {7}), 13 is already part of the original S₀, and
V = ∅ — no recruitment round is needed for this seed.**

## Next-round guidance (superseded by ROUND 5 section below — kept for audit trail)
1. Recompute all "rogue pair" / recruitment-process computational claims from rounds
   3–4 using the corrected minimal-witness convention (see above); treat every existing
   numerical "V ≠ ∅" claim in the workspace as unverified until redone.
2. Attempt a direct proof that V = ∅ always holds for the MINIMALLY-witnessed Finite
   Core Theorem's S₀ (a sharper, now better-supported target than the general
   recruitment-process termination question) — e.g. by exploiting a special extremal
   property of the earliest occurrence of each type (unexplored so far).
3. Do NOT re-attempt the retracted "universal glue prime" / "cost ≤ 1" claims
   (falsified round 2 by a genuine, unaffected a_1 = 35 counterexample — that
   falsification did not depend on S₀/witness computation and stands).
4. Certified this round: **Lemma G** (Extended Earliest-Witness Intersection,
   `lemmas/extended-earliest-witness-intersection.md`) — unconditional, correct,
   reusable. The **Round Resolution Lemma** (conditional on the unproved "Singleton
   Hypothesis") is correctly and honestly disclosed as conditional but is NOT
   certified as a portable unconditional lemma; its computational support needs
   re-verification per point 1 above, and — if V = ∅ turns out to hold unconditionally
   with minimal witnesses (point 2) — this whole conditional-lemma line of attack may
   turn out to be unnecessary.
5. The secondary "periodicity from n=1 literally" gap remains untouched since round 1.

## ROUND 5 CORRECTION — round 4's "V = ∅ always, 18/18 seeds" is RETRACTED again; this
time genuinely falsified (triple-independently reconfirmed, not the round-3/4 bug)

Round 4's revival of "zero further recruitment rounds ever needed" was itself wrong.
This round's math-explorer (singleton-hypothesis lens) found 4 fresh counterexamples
(a_1 = 187, 209, 247, 385) where the correctly-computed (literal minimal-witness) S₀
genuinely has V ≠ ∅ — a real rogue pair requiring one recruitment round. This was
**independently reconfirmed twice more**: once by this round's outline-reviewer (fresh
from-scratch reimplementation, all four seeds' S₀/rogue-pair/witness data matched
exactly), and a third time by this round's proof-reviewer (a third independent
from-scratch Python implementation, scanning n=1..1400 directly with no tail-window
shortcuts), which reproduced the identical a_1=187 result: S₀={2,3,11,17}, rogue pair
({17,2},{11,3}), witnesses n_A=6, n_B=5, shared outside-core prime F'={7} on both
sides — exact match to the explorer's and outline-reviewer's numbers. **This is not the
round-3/4 witness-selection bug: all three independent implementations used the literal
global-minimum witness convention.** The "V = ∅ always" conjecture is definitively dead;
do not re-propose it. The correct, current understanding: V is sometimes empty (many
seeds) and sometimes nonempty requiring exactly one recruitment round (at least in every
case checked so far — 2+ rounds has never been observed, checked up to ≈200 seeds across
all builders this round).

## ROUND 5 progress — the crux is now narrowed to exactly one open hypothesis

**New unconditional lemma (certified): Monotonicity of Resolution**
(`lemmas/monotonicity-of-resolution.md`, `covering-system-construction`). If two
S₀-extended-persistent types share a prime, every later-stage refinement of them (at any
S₁ ⊇ S₀) still shares that prime — resolution, once achieved, is permanent.
Independently re-derived and verified correct by this round's reviewer.

**New unconditional lemma (certified): Same-Side Ordering**
(`lemmas/same-side-ordering-lemma.md`, `witness-index-descent`). For an S₀-extended-
persistent type A' refining base type A, the earliest occurrence n_{A'} of A' is always
≥ the earliest (global) occurrence m_A of the base type A. Short, correct, no gap. (Its
originally-hoped-for use — feeding a well-ordering descent — does NOT go through; see
witness-index-descent's RETHINK below.)

**New unconditional lemma (certified, with a wording correction): Critical Prime
Dichotomy / Lemma H** (`lemmas/critical-prime-dichotomy.md`,
`greedy-exchange-cost-potential`). For any outside-core prime q' dividing a witness
a_n, either stripping q' from a_n drops below a_{n-1}, or q' is the *sole* shared prime
with some specific earlier term. **Reviewer correction:** the source file claims these
two branches are mutually exclusive ("exactly one holds"); the proof only establishes
the inclusive "(a) or (b)," not exclusivity — corrected in the certified version. This
does not affect any use made of the lemma in the source file (every application only
needs "(a) or (b)").

**Covering-system-construction's conditional theorems (verified correct, NOT
certified as unconditional — kept in-file per the round-4 precedent for conditional
results):** the **Conditional Single-Pair Permanent Resolution Theorem** and its batch
form, the **Conditional Simultaneous Resolution Theorem**, both conditional on the
**Universal Singleton Hypothesis** (every S₀-extended-persistent type with a rogue
partner has |F'| = 1, i.e. its earliest witness has exactly one outside-core prime
factor). Independently re-derived and spot-checked by the reviewer on a_1=187 (verified
computationally that literally every A'-type occurrence past the B'-witness index is
divisible by the shared prime 7, exactly as the theorem's proof predicts — 58/58 checked
instances, 0 exceptions). These theorems correctly repair round 3's "route 2"
obstruction (the recruited prime is now certified on BOTH sides, via the certified Lemma
G, not just the reconciled side) using machinery (Lemma G) that did not exist before
round 4.

**IMPORTANT ADDITIONAL GAP the reviewer found in the "given Singleton Hypothesis, the
problem is solved" claim — NOT flagged by the builder, must be addressed next round.**
`covering-system-construction`'s Step 7 states its "Bottom line" as: given the Universal
Singleton Hypothesis, one recruitment round (S₀ → S₁ := S₀ ∪ Q_R) resolves every
currently-known rogue pair, and then asserts "Step 6's finish applies unchanged" as if
S₁ were now a terminal core with global V = ∅. **This is not actually shown.** The
Conditional Simultaneous/Single-Pair Resolution Theorems only prove that the pairs
already rogue at S₀ get resolved (absorbed into a common refined type at S₁); they say
nothing about whether refining S₀ → S₁ can spawn brand-new S₁-extended-persistent types
(by splitting a previously non-rogue base type's occurrences into "divisible by the new
prime(s) of Q_R" vs. not) that form NEW disjoint pairs not present at S₀ — i.e., whether
one round is really the LAST round, or whether the recruitment process could need to
re-run after S₁. This is exactly the same "refinement can manufacture new classes"
phenomenon that `witness-index-descent` independently documented this round for a
different reason (its well-ordering's non-monotonicity). The reviewer spot-checked this
computationally on all three available multi-round-eligible seeds (187, 209, 247; 385
has zero S₀-rogue pairs) and found **zero new rogue pairs at S₁** in every case — mildly
reassuring but not a proof, and not even attempted in the builder's file. **Next round
must either (a) prove no new rogue pairs can be spawned by the specific refinement S₀ →
S₀ ∪ Q_R (a "collateral rogue pair" lemma), or (b) explicitly reformulate the Singleton
Hypothesis to be closed under recruitment (i.e., prove it holds not just at S₀ but at
every subsequent stage, and that the number of stages is finite) before claiming the
Simultaneous Resolution Theorem finishes the problem.** Until this is done, "given
Singleton Hypothesis, the whole problem is solved" (the builder's stated bottom line) is
an overclaim; the correct statement is "given the Universal Singleton Hypothesis AND no
collateral rogue pairs are spawned by one round of recruitment (verified on 3/3 tested
seeds, not proved), the whole problem is solved."

**The crux is therefore narrowed to (in order of priority):**
1. The **Universal Singleton Hypothesis** itself (every rogue-pair witness's outside-core
   factor set F' has exactly 1 element) — attempted this round via Lemma H (Critical
   Prime Dichotomy); shown to be a genuine *necessary* handle on each individual prime
   of F' but NOT sufficient to rule out |F'| ≥ 2 (two distinct primes could each
   independently satisfy Lemma H's branch (b) via different earlier witnessing indices,
   with nothing in the certified stack forcing a contradiction). Still fully open.
2. The **"no collateral rogue pairs" gap** identified above (new this round, not
   previously flagged) — whether one recruitment round is really terminal, or whether
   refining S₀ → S₁ can spawn new disjoint pairs among previously-non-rogue types.
3. Connectivity of the "rogue partner" relation graph (whether recruitment always
   collapses to literally ONE new prime, vs. a bounded finite batch) — flagged as open
   but NOT needed for the finish (a bounded batch works equally well for the CRT step).

## ROUND 5 — approach verdicts (independent, per CLAUDE.md's per-approach routing)

- **covering-system-construction** — Verdict: **CHANGES REQUESTED** (partial). Real,
  substantial progress: proved the unconditional Monotonicity of Resolution Lemma
  (certified) and, building on the certified Lemma G, the Conditional Single-Pair and
  Simultaneous Resolution Theorems (verified correct, conditional on the Universal
  Singleton Hypothesis). Correctly and precisely repairs round 3's "route 2"
  obstruction. Gap: the Universal Singleton Hypothesis remains open (owned by the
  sibling approach), AND — new finding by this review — the "no collateral rogue pairs"
  gap above, which the builder's "Bottom line" did not address and should not have
  treated as already closed.
- **greedy-exchange-cost-potential** — Verdict: **CHANGES REQUESTED** (partial). Proved
  the new unconditional Lemma H (Critical Prime Dichotomy, certified with a wording
  correction — the source states an exclusive "exactly one," proof only gives the
  inclusive "at least one"; substance and all uses unaffected). Honestly documents why
  Lemma H does not by itself close the Universal Singleton Hypothesis, and why the
  natural repair (forcing two branch-(b) witnessing indices to coincide) also fails.
  Real narrowing of the exact remaining obstruction, no gap papered over.
- **witness-index-descent** — Verdict: **RETHINK**. The well-ordering/minimal-
  counterexample descent, as scoped, cannot deliver the recruitment-process-termination
  proof: (a) the only single-stage target it could prove ("no rogue pair exists") is
  demonstrably FALSE (rogue pairs provably exist at S₀ for many seeds), so the target
  had to be reformulated across the increasing chain of recruitment stages; (b)
  reformulated that way, the natural monovariant (smallest rogue-pair witness index
  across all stages) is **not stage-monotone** — enlarging S₀ by one prime can refine
  the extended-type partition at small indices too, manufacturing brand-new rogue pairs
  with SMALLER witness indices than any seen before, verified computationally this
  round. This is the second independent well-ordering (after round 3's |A'|+|B'| size
  measure) to hit essentially the same "refinement manufactures new small-index classes"
  wall, suggesting the obstruction is intrinsic to the recruitment operation, not an
  artifact of the chosen measure. No fix was found or proposed. Per CLAUDE.md, this
  specific approach (a single global monovariant descent) should not be continued as
  scoped; if revisited, it needs a genuinely different well-ordering that is provably
  robust to partition refinement (not attempted so far). Its one surviving artifact —
  the **Same-Side Ordering Lemma** — is correct and certified, but is not, by the
  builder's own analysis, the load-bearing fact any descent actually needs (Lemma G's
  shared-prime conclusion already holds unconditionally via Free Facts, with no
  dependence on witness ordering).
- **reversible-transition-map** — Verdict: **RETHINK** (for its stated primary goal;
  the disambiguation task itself was executed correctly and is valuable). Proved, both
  directions, that "S-sufficiency" (forward well-definedness of the proposed finite
  automaton at a fixed core S) is logically EQUIVALENT to "V = ∅ at level S," i.e. gap
  (†) restricted to that level. This confirms the outline-reviewer's flagged risk: the
  proposed "finite-automaton bypass" of gap (†) is not a bypass at all, just a
  restatement in different language, and cannot be used to circumvent the recruitment-
  process termination question. This specific framing should not be pursued further as
  a primary-gap attack (matches the same "this target cannot close (†) as framed"
  pattern that led to witness-depth-bound's round-3 RETHINK). The approach also
  identified a genuinely new, unresolved obstruction for the SEPARATE secondary
  "periodicity from n=1" gap (early, weaker-constrained terms need not lie on the
  eventual cycle even if the eventual map is proved injective) — this narrower target
  could be revived in a future round as a standalone secondary-gap approach, but the
  file's main proposed mechanism (bypass via reversibility) is dead as a route to the
  primary gap.

## Lemma certification this round
- **Certified:** `lemmas/monotonicity-of-resolution.md` (unconditional, verified).
- **Certified:** `lemmas/same-side-ordering-lemma.md` (unconditional, verified).
- **Certified (wording corrected):** `lemmas/critical-prime-dichotomy.md` — the source
  file's claimed "exactly one of (a)/(b)" is corrected to "at least one"; the proof only
  supports the weaker (and here-certified) inclusive form.
- **NOT certified:** Conditional Single-Pair / Simultaneous Resolution Theorems
  (`covering-system-construction`) — correct but conditional on the unproved Universal
  Singleton Hypothesis; kept in-file per the round-4 precedent for conditional results
  (matches the treatment of round 4's Round Resolution Lemma).
- **NOT certified:** "S-sufficiency ⟺ V=∅ at level S" (`reversible-transition-map`) —
  the (⇐) direction is a solid restatement of already-certified content, but the (⇒)
  direction's proof is written informally (a "consider two histories" narrative rather
  than a crisp formal argument) and "S-sufficiency" itself is not crisply/formally
  defined in the file. The mathematical conclusion (this framing cannot bypass (†)) is
  almost certainly correct and is recorded above as a population-wide caution, but the
  statement is not certified as a portable shared lemma in its current form — a future
  round could tighten and resubmit it if a fully formal restatement is produced.

## Next-round guidance (current)
1. **Priority 1**: attack the Universal Singleton Hypothesis directly, building on
   Lemma H (Critical Prime Dichotomy) — the precise open sub-question is whether two
   distinct primes q', q'' ∈ F' can each independently satisfy Lemma H's branch (b) via
   different earlier witnessing indices i, i' with no forced relationship; a genuinely
   new ingredient (not yet in the certified stack) connecting different earlier terms'
   legality-critical primes is needed.
2. **Priority 2 (new this round, do not skip)**: prove or refute the "no collateral
   rogue pairs" gap — does one round of recruitment (S₀ → S₀ ∪ Q_R) ever spawn brand-new
   disjoint-base-type pairs among previously-non-rogue types? Verified negatively (no
   new rogue pairs) on 3/3 tested seeds (187, 209, 247) but not proved or tested more
   broadly.
3. Do NOT re-attempt: the round-2 "universal glue prime"/"cost≤1" claims (falsified,
   unaffected by any witness bug); round-3's |A'|+|B'| size-measure descent or round-5's
   witness-index descent (both independently hit the same partition-refinement wall);
   round-4's PUCL; the "V=∅ always" conjecture (now falsified three times independently
   this round alone).
4. The `reversible-transition-map`'s secondary-gap obstruction (early terms need not lie
   on the eventual cycle) is a legitimate, still-open, narrower target if a future round
   wants to attack the secondary "periodicity from n=1" gap once the primary gap closes.
5. The secondary "periodicity from n=1 literally" gap remains untouched (beyond the
   scoping above) since round 1.

## ROUND 6 — the "collateral rogue pairs" gap is closed unconditionally; (†) is
reduced exactly to base-type-pair-level termination, pinned to FAH + Symmetric FAH

**New unconditional lemma (certified): Projection Lemma**
(`lemmas/projection-lemma.md`, `covering-system-construction`). For S₀ ⊆ S₁ finite
with Q ⊆ S₀, if A'' is S₁-extended-persistent then A' := A''∩S₀ is
S₀-extended-persistent with the same base type A'∩Q = A''∩Q. A short, direct
set-theoretic identity (ρ(n) = ρ₁(n)∩S₀). Independently re-verified by the reviewer
— correct, no gap.

**New unconditional lemma (certified): Collateral-Safety Theorem**
(`lemmas/collateral-safety-theorem.md`, `covering-system-construction`). If a
disjoint base-type pair (A,B) is "fully safe" at S₀ (every pair of
S₀-extended-persistent refinements intersects), it stays fully safe at every
S₁ ⊇ S₀. Proved by combining the Projection Lemma with the already-certified
Monotonicity of Resolution Lemma. Independently re-verified by the reviewer, correct,
no gap, no dependence on the Universal Singleton Hypothesis, FAH, or any other open
hypothesis. **This completely and unconditionally closes round 5's "collateral rogue
pairs" gap** — the gap the reviewer identified in round 5 (that one recruitment round
resolving currently-rogue pairs was never shown to be safe against newly-spawned rogue
pairs among previously-safe types) is now resolved: it cannot happen, full stop.

**Consequence (reduction of (†), verified by the reviewer): base-type-pair-level
termination is now the ENTIRE remaining content of gap (†).** Since Q never changes,
the set of persistent base types 𝒫 and the finite list of disjoint base-type pairs
(≤ C(|𝒫|,2) of them) are fixed once and for all (free corollary of Collateral-Safety).
Defining open(k) := {(A,B) : not fully safe at stage-k core S₀^(k)}, Collateral-Safety
gives open(k+1) ⊆ open(k) — a non-increasing sequence over a FIXED finite index set.
(†) holds iff open(k) = ∅ for some finite k. This is a strictly sharper localization
than round 5's extended-type-level framing (where the number of currently-rogue
extended pairs was not obviously bounded independent of k).

**Whether open(k) reaches ∅ is precisely the question of "full absorption"** — does
recruiting a Lemma-G prime against one witnessed rogue instance make the WHOLE
base-type pair safe (every extended refinement, not just the one witnessed), or could
other refinements of the same pair remain unreconciled? This is exactly the sibling
approach `greedy-exchange-cost-potential`'s **Full-Absorption Hypothesis (FAH)**: for
a rogue pair (A',B') with Lemma-G prime q and n_A < n_B, q divides a_n for EVERY
n > n_B with ρ(n)=A' (not merely infinitely many).

**`covering-system-construction`'s round-6 proof needs a strengthening beyond the
sibling's literal one-sided FAH: "Symmetric FAH"** — the same "every occurrence, not
just infinitely many" conclusion also on the OTHER side (q divides every n > n_A with
ρ(n)=B'). The builder's Step 8.5 proof of "Symmetric FAH (for every currently-rogue
pair) ⟹ base-type-pair-level termination in exactly one further round" is a correct,
carefully-checked conditional implication (reviewer independently re-derived it line
by line: Case 1 uses Monotonicity directly; Case 2 uses the Projection Lemma to reduce
S₁-persistent refinements to their S₀-parents, then Symmetric FAH to place q_i in BOTH
A'' and B'' via infinitely-many-tail arguments on each side separately). No hidden
assumption found.

**Reviewer's independent empirical check of FAH and Symmetric FAH (important
correction to the builder's own honesty bookkeeping).** `covering-system-construction`
states in Step 8.4 that it has "NOT verified [Symmetric FAH] computationally or
attempted a proof of it in this file." This is true narrowly (that file does not run
the check), but the reviewer finds that **Symmetric FAH already has strong empirical
support elsewhere in this round's own workspace**, unremarked by either builder:
`greedy-exchange-cost-potential`'s Step 0 explicitly checks, for every rogue pair
found across 7 seeds (~90 records), both "every A'-occurrence after n_B divisible by
q" AND "every B'-occurrence after n_B divisible by q" — and since n_B is by
definition B's own earliest occurrence, "after n_B" and "after n_A" restricted to
B'-occurrences coincide exactly (no B'-occurrence exists in (n_A, n_B) since n_B is
minimal, and q | a_{n_B} itself is already guaranteed by Lemma G) — so that file's own
"B'-side" check IS, precisely, an empirical check of Symmetric FAH, with 0 failures
reported across all 7 seeds. The reviewer independently re-derived this equivalence
and re-ran a 4th from-scratch implementation (scanning n=1..8000-15000 directly, no
tail-window shortcuts, no shared code with any builder) on four seeds:

- a_1=187: rogue pair A'={3,11}, B'={2,17}, q=7 — FAH 0/99 fail, Symmetric FAH 0/125
  fail.
- a_1=209: three rogue pairs, all q=7 — FAH 0/79–88 fail, Symmetric FAH 0/21–91 fail,
  across all three.
- a_1=385: rogue pair A'={3,7}, B'={2,11}, q=19 — FAH 0/21 fail, Symmetric FAH 0/26
  fail.
- a_1=4807 (the |F'|=2 seed used to falsify the Universal Singleton Hypothesis):
  independently reconfirmed the rogue pair A'={3,5,19} (n_A=6), B'={2,11} (n_B=7),
  F'={13,17}, Lemma-G prime q=17 (gcd(a_6,a_7)=17; a_6=4845=3·5·17·19,
  a_7=4862=2·11·13·17 — exact match to the explorer's/outline-reviewer's numbers,
  now a 4th independent confirmation) — and FAH/Symmetric FAH both hold with 0
  failures (FAH: 0/10 past n=7; Symmetric FAH: 0/151 past n=6, extending the
  outline-reviewer's own B'-side check from 151 to a longer range with the same
  result).

**Conclusion: both FAH and Symmetric FAH are correct as stated, well-supported (0
counterexamples across every seed tested by any agent this round, now cross-validated
by a 4th independent implementation including the critical |F'|=2 case), but NEITHER
IS PROVED.** This is evidence, not a proof, per CLAUDE.md's rigor rules — the status
below reflects this honestly.

**Lemma I (`greedy-exchange-cost-potential`, "Non-Exclusivity of Witness
Recruitment") — reviewer assessment.** The proof (an exhaustive case-check that each
of the four certified tools — Free Facts, Generalized Bounded Witness Lemma, the Gap
Lemmas, Critical Prime Dichotomy — produces either a pure existential or a pure
magnitude bound, and no composition of these can promote "some prime of a ≥2-element
set works" to "one specific prime always works") is logically sound as a diagnostic:
independently checked each of the four tools' proofs and confirmed none contains an
identity-forcing step. However, per the same precedent set for round-3's Lemma F (also
an "exhaustive inspection of what the current certified toolkit can and cannot do"),
this is a statement ABOUT the current certified lemma set, not a portable mathematical
fact that remains true if new lemmas are certified later — so it is **not certified as
a standalone lemma file**, matching the Lemma F precedent. It is recorded here as
valuable, correct guidance: any future attempt at FAH/Symmetric FAH needs a genuinely
new mechanism, not a recombination of Free Facts / Generalized Bounded Witness /
Gap Lemmas / Critical Prime Dichotomy.

**`recruitment-round-charging` (new approach this round) — reviewer assessment.**
Tested three independent "charging" strategies to bound/prove finiteness of the
recruitment process without going through FAH: (1) charging against ω(a_1)/Ω(a_1) —
confirmed dead end (recruited primes need not divide a_1, e.g. a_1=175 recruits 13);
(2) charging against growth rate a_n=O(n) — confirmed dead end (bounded per-term
factorization size is compatible with unboundedly many distinct primes across terms);
(3) charging against |𝒫| via a "batch resolution" phenomenon (a single recruited
prime resolving several simultaneously-rogue pairs at a "hub" type at once). The
reviewer independently reconfirmed the batch-resolution finding on a fresh seed
(a_1=6851, Q={13,17,31}): found 10 distinct rogue extended-type pairs, ALL sharing
the same recruited prime 5 — matching the builder's report exactly. The builder's
**Hub Singleton Batch Lemma** (if a hub type's own witness has a singleton
outside-core factor set, the same prime resolves every one of its simultaneous rogue
relationships) is a correct, trivial corollary of the certified Lemma G — certified
below. But the builder honestly shows this only explains 3/19 sampled hub instances;
the other 16/19 have |F'_H|=2 with the SAME element consistently picked by every
partner — a strictly stronger, unexplained phenomenon that reduces to exactly the
open FAH question, not an independent route. **Reviewer agrees with the builder's own
conclusion: none of the three charging candidates gives an independent route around
the shared crux; candidates (1) and (2) are genuine dead ends, and candidate (3)
provably reduces to the same open hypothesis the other two approaches are already
attacking.**

## Lemma certification this round (round 6)
- **Certified:** `lemmas/projection-lemma.md` (unconditional, verified).
- **Certified:** `lemmas/collateral-safety-theorem.md` (unconditional, verified;
  depends on the certified Projection Lemma and Monotonicity of Resolution Lemma).
- **Certified:** `lemmas/hub-singleton-batch-lemma.md` (unconditional, verified;
  narrow scope — only covers the |F'_H|=1 case, does not resolve the general
  batch-resolution question).
- **NOT certified:** Lemma I (`greedy-exchange-cost-potential`) — correct as a
  diagnostic about the current certified toolkit, but (matching the round-3 Lemma F
  precedent) not a portable mathematical fact independent of which lemmas happen to
  be certified; recorded above as guidance instead.
- **NOT certified:** FAH and Symmetric FAH themselves — both remain open hypotheses
  (well-supported empirically, including by this round's independent reviewer
  re-verification on 4 seeds including the critical |F'|=2 case, but not proved).

## ROUND 6 — approach verdicts (independent, per CLAUDE.md's per-approach routing)

- **covering-system-construction** — Verdict: **CHANGES REQUESTED** (partial). Real,
  substantial, verified progress: the Projection Lemma and Collateral-Safety Theorem
  (both certified, unconditional) completely close round 5's "collateral rogue pairs"
  gap and give an exact, sharper reduction of (†) to base-type-pair-level termination
  over a fixed finite index set. The remaining gap is now pinned exactly to FAH (owned
  by the sibling approach) plus a newly identified Symmetric FAH strengthening (this
  round's own honest addition) — both open, both well-supported empirically
  (independently reconfirmed by the reviewer this round), neither proved.
- **greedy-exchange-cost-potential** — Verdict: **CHANGES REQUESTED** (partial).
  Correctly retired the falsified Universal Singleton Hypothesis (reconfirmed
  independently by the reviewer, a_1=4807 gives F'={13,17}), replaced it with the
  precisely-stated FAH, extended empirical verification substantially (reconfirmed by
  the reviewer's own 4th independent implementation, 0 failures), and made three
  genuinely distinct, honestly-documented failed proof attempts, distilled into the
  correct (if non-portable) negative result Lemma I. Real, careful progress; FAH
  remains open.
- **recruitment-round-charging** (new) — Verdict: **RETHINK**. The approach's core
  idea — find a charging/counting argument that bounds or proves finiteness of the
  recruitment process independent of Full Absorption — is now shown, across all three
  tested candidates, to either be a confirmed dead end (candidates 1, 2) or to reduce
  to exactly the same open FAH question the other two approaches already own
  (candidate 3, batch resolution; reviewer independently reconfirmed the underlying
  data on a fresh seed). This is a genuine, valuable negative result and produced one
  small certified lemma (Hub Singleton Batch), but the approach's own charging framing,
  as scoped, cannot deliver an independent route to the whole problem's claim — matches
  the CLAUDE.md criterion for RETHINK ("the approach can't work as set up"). If
  continued, next round must open with a genuinely different framing (per CLAUDE.md's
  diversity mandate), not another charging-object variant.

## ROUND 7 — dead sub-mechanism retracted, two new unconditional lemmas each side,
a new proof style opened and refuted, first real treatment of the secondary n=1 gap

**greedy-exchange-cost-potential.** Retracted the dispatched "Two-Witness
Intersection Uniqueness" mechanism (joint Critical-Prime-Dichotomy analysis against
a fixed witness's own minimality) as dead, confirmed independently by the reviewer
both (i) at the proof level — Lemma H's derivation never extracts any S₀-type
information about a branch-(b) witnessing index, so there is no route from "two
distinct primes both hit branch (b)" to a contradiction unless they share a
witnessing index, which nothing forces — and (ii) computationally, on the
mechanism's own motivating example a_1=4807 (reviewer independently regenerated
a_1..a_10, confirmed F′={13,17}, F″={17}, and confirmed both candidate primes 13
and 17 trivially land in the uninformative branch (a) of Lemma H: c=374 and c=286
respectively, both far below a_6=4845). Produced two new certified lemmas:
**Lemma J (Divisor-Restricted Pigeonhole)** and **Lemma K (Adjacent Multiple
Blocking)** — the latter is the first tool in the workspace to use negative
(illegality/skipped-candidate) data. Both are correct, unconditional,
independently re-derived by the reviewer — certified to
`lemmas/divisor-restricted-pigeonhole.md` and `lemmas/adjacent-multiple-blocking.md`.
The "Blocking-Data Bridging" combination of these does NOT close FAH: precisely
diagnosed, Lemma K's constructed competitor c has no controlled factorization
relationship to the witness a_n (unlike Lemma H's exact P(c)=P(a_n)\{q'}), so Free
Facts' guaranteed shared prime between c's blocking index and a_n cannot be pinned
to the target prime q. FAH and Symmetric FAH remain open.

**covering-system-construction.** Two bookkeeping steps verified correct: **Step
8.7** (Canonicalization) shows the finish (Step 8.5) only needs a single canonically
chosen prime q* := min(F'∩F'') to satisfy BOTH the A'-side and B'-side
full-absorption properties ("Joint FAH"), decoupling the finish from the sibling's
now-dead Two-Witness Uniqueness target — this is a genuine, honestly-scoped
simplification (a sufficient, not necessary, route; it does not make FAH itself
easier, only removes an unnecessary intermediate dependency), independently
re-verified correct. **Step 8.8** (Symmetry-Transfer Check) confirms the sibling's
proposed (stalled) Blocking-Data Bridging mechanism has no structural asymmetry
between the A'-side and B'-side — a single proof would give both FAH and Symmetric
FAH — independently re-verified correct, though the underlying mechanism itself
remains unproved. Neither Step 8.7 nor Step 8.8 is certified as a portable shared
lemma (both are meta-statements about THIS approach's own proof structure/target,
in the spirit of the round-3 Lemma F / round-6 Lemma I precedent for
non-portable-but-correct in-file content — see Lemma certification notes below).

**New treatment of the secondary "periodicity from n=1" gap (Step 9,
`covering-system-construction`).** Proved the **Exact-Equality Reduction Lemma**:
given eventual periodicity a_{n+T}=a_n+L for n≥N₀, literal periodicity for all n≥1
holds iff the finitely many equalities a_{i+T}=a_i+L hold for i=1,...,N₀−1 — trivial
case-split, correct, fully general (any integer sequence). Then proved, via an
explicit counterexample, that this finite check is **not automatic**: the round-7
outline's proposed "period-rescaling" mechanism (T':=T·k for the smallest k with
N₀≤kT) is FALSE in general for eventually-periodic increasing integer sequences —
**Non-Automaticity of Prefix Folding**, witnessed by a_1:=1, a_2:=5, a_n:=997+n for
n≥3 (eventually periodic T=1,L=1 from N₀=3, but no (T'',L'') works for all n≥1: the
tail forces T''=L'', and then n=1 forces either a_2=2 (false, a_2=5) or 998=1
(false)). Both independently re-verified by the reviewer (see Independent
verification below) — both certified. This upgrades the n=1 gap from "untouched,
believed true empirically" to "precisely localized to finitely many explicit
equalities, with the naive automatic-reduction route explicitly ruled out" — still
open (Step 9.3's candidate residue-driven-rule strategy stalls at a precisely
identified point, honestly documented, not closed).

**scalar-well-ordering-lock-in (new approach this round).** Imported crux
`aimo-0678`'s two-scalar (non-increasing witness + coupled algebraic-identity
scalar) mechanism as a genuinely different proof *style* from the existential/
combinatorial FAH attacks. Proved well-definedness of the scalar witness w_k
(free bookkeeping, correct). Found and proved the hypothesized coupled recursion
(H) (recruited prime q_k divides the next stage's witness w_{k+1}) is **FALSE**:
an exact, hand-verified counterexample on a_1=175 (recruiting q_0=2 against
({5},{7}) at S₀={5,7} pushes the earliest witness of the "pure {7}" type from
n=3 (a_3=182=2·7·13) to n=4 (a_4=189=3³·7, odd — 2∤189)), generalized to a genuine
structural fact — the **Witness Discontinuity Obstruction**: enlarging the core by
a prime recruited against a witness can push that witness's own type to a *new*,
unrelated later index whose factorization has no forced relationship to the
recruited prime. Both the counterexample and the general claim independently
re-verified by the reviewer (regenerated a_1..a_4 for a_1=175 from scratch,
matches exactly) — certified to `lemmas/witness-discontinuity-obstruction.md`. The
two natural repairs (fixed-pair variant; weaker |open(k)| scalar) are both shown,
honestly, to collapse into the already-open FAH/Symmetric-FAH question rather than
provide an independent bypass — recorded so neither is re-attempted believing it
independent.

**Independent verification (this round, reviewer).**
(a) Re-derived Lemma J and Lemma K from scratch — both correct, unconditional,
non-circular.
(b) Re-ran the a_1=4807 Two-Witness-Uniqueness falsifying computation from scratch
(trial-division factorization, a_1..a_10) — matches the builder's report exactly
(F′={13,17}, F″={17}, both branch (a) trivially).
(c) Re-derived the Exact-Equality Reduction Lemma and hand-checked the
Non-Automaticity counterexample's two case splits (T''=1; T''≥2) — both correct.
(d) Regenerated a_1=175's sequence (a_1..a_6 = 175,180,182,189,195,210) from
scratch and reconfirmed the Witness Discontinuity Obstruction's exact claims about
ρ_{S₀}(3), ρ_{S₁}(3), ρ_{S₁}(4) — matches exactly.

**The crux is unchanged in substance: FAH and Symmetric FAH (equivalently, per
Step 8.7, a single canonical-prime Blocking-Data Bridging Lemma) remain the sole
open gap.** This round narrowed HOW to state and approach it (canonical q*,
side-agnostic mirroring) and closed off two more specific proof mechanisms (joint
Lemma-H branch analysis; the aimo-0678 algebraic-recursion transplant) as dead,
without producing a proof.

## Lemma certification this round (round 7)
- **Certified:** `lemmas/divisor-restricted-pigeonhole.md` (Lemma J, unconditional,
  verified).
- **Certified:** `lemmas/adjacent-multiple-blocking.md` (Lemma K, unconditional,
  verified; first illegality-data-based tool in the workspace).
- **Certified:** `lemmas/exact-equality-reduction-lemma.md` (unconditional,
  verified; precise localization of the secondary n=1 gap for any future approach).
- **Certified:** `lemmas/non-automaticity-of-prefix-folding.md` (unconditional,
  verified; rules out the naive "period-rescaling" fix for the n=1 gap in general).
- **Certified:** `lemmas/witness-discontinuity-obstruction.md` (unconditional,
  verified; rules out continuity-of-witness-selection assumptions for any future
  algebraic-recursion-style attack on FAH).
- **NOT certified:** Canonicalization Lemma / Symmetry-Transfer Check
  (`covering-system-construction`, Step 8.7/8.8) — both correct as proved, but
  (matching the round-3 Lemma F / round-6 Lemma I precedent) are meta-statements
  about THIS approach's own proof structure and target (what Step 8.5 needs, and
  whether the sibling's stalled mechanism is side-symmetric), not portable
  mathematical facts independent of the specific proof they support. Recorded above
  as valuable in-file guidance instead.

## ROUND 7 — approach verdicts (independent, per CLAUDE.md's per-approach routing)

- **greedy-exchange-cost-potential** — Verdict: **CHANGES REQUESTED** (partial).
  The retraction of Two-Witness Intersection Uniqueness is genuine (independently
  reconfirmed both abstractly and computationally). Two new certified lemmas (J, K),
  the first use of illegality data in this workspace. FAH remains open; the
  obstruction to Blocking-Data Bridging is precisely diagnosed, not hand-waved.
- **covering-system-construction** — Verdict: **CHANGES REQUESTED** (partial). Two
  correct, honestly-scoped bookkeeping steps (Step 8.7 canonicalization, Step 8.8
  symmetry check) that narrow and decouple the remaining target without closing it;
  first real, correct treatment of the secondary n=1 gap (two new certified
  lemmas), still open at Step 9.3. No overclaim found; every "not closed" claim
  checks out.
- **scalar-well-ordering-lock-in** (new) — Verdict: **RETHINK**. This round's
  genuinely different proof *style* (aimo-0678-style algebraic-recursion
  transplant) is now shown, via an exact counterexample and a general structural
  argument (both independently verified), not to work: the hypothesized recursion
  is false, and per Section 3's own honest analysis, both natural repairs collapse
  into the already-open FAH/Symmetric-FAH question rather than supplying an
  independent route. This matches the CLAUDE.md RETHINK criterion (the approach's
  core mechanism, as scoped, cannot deliver a route to the whole claim) and the
  workspace's precedent for prior mechanism-level dead ends (witness-index-descent,
  recruitment-round-charging). The produced negative result (Witness Discontinuity
  Obstruction) is real, certified, reusable content — a valuable byproduct, not
  wasted effort — but the approach itself, as scoped, should not be continued
  without a genuinely different mechanism; if revived, it needs a proof style that
  does not depend on continuity of witness selection across recruitment stages.

## Next-round guidance (current, round 7)
1. **Priority 1, unchanged**: FAH and Symmetric FAH (equivalently, per Step 8.7,
   the single canonical-prime Blocking-Data Bridging Lemma for q* := min(F'∩F''))
   remain the sole open crux. Do NOT re-attempt: joint Lemma-H branch analysis
   (Two-Witness Intersection Uniqueness, dead — confirmed twice now, abstractly and
   computationally); the aimo-0678 algebraic-recursion transplant in its literal
   form (H) (refuted by the Witness Discontinuity Obstruction — any future
   algebraic-recursion attempt must NOT assume a recruited prime persists into the
   next stage's witness); Lemma K's "round down to nearest non-divisor multiple"
   construction as a standalone route (shown insufficient — its competitor's
   factorization is uncontrolled relative to the witness).
2. A genuinely new mechanism is still needed for FAH/Symmetric FAH — per Lemma I's
   diagnosis (round 6) plus this round's two new negative results, the needed
   ingredient is one that either (a) controls the factorization of a *constructed*
   competitor integer relative to the actual witness (unlike Lemma K), or (b)
   establishes some continuity/stability property of witness selection across
   recruitment stages that survives the Witness Discontinuity Obstruction (i.e.
   does not merely assume it), or (c) is a wholly different framing not yet tried
   in this workspace (density/asymptotic-domination arguments, as suggested round
   6, remain unexplored).
3. The secondary n=1 gap is now precisely localized (Exact-Equality Reduction
   Lemma) with the naive automatic-reduction route ruled out (Non-Automaticity of
   Prefix Folding); Step 9.3's residue-driven-rule candidate strategy is the
   sharpest concrete next target for this gap, independent of FAH/Symmetric FAH
   (though it "plausibly shares its flavor," per the builder's own honest
   assessment).
4. Do NOT re-attempt: any prior falsified/exhausted conjecture (see rounds 1-6
   guidance above, all still valid) — the round-7 additions above extend, not
   replace, that list.

## Next-round guidance (current, round 6)
1. **Priority 1, unchanged in substance but sharper**: attack FAH (owned by
   `greedy-exchange-cost-potential`) AND Symmetric FAH (owned jointly, newly
   identified by `covering-system-construction`) — both are now known to be
   equivalent in empirical strength (every tested instance satisfies both, and the
   reviewer's re-derivation shows the sibling's own "B'-side" check already
   empirically covers the symmetric form). A single proof of "the Lemma-G prime for a
   rogue pair divides every later occurrence on BOTH sides" would close the whole
   problem via Step 8.5's Corollary + Step 5's finish. Do NOT re-attempt the three
   proof mechanisms already shown (via Lemma I) to fail: direct Lemma H branch
   analysis, inductive chaining across successive same-type occurrences, and
   exchange/minimality constructions built solely from Free Facts + Generalized
   Bounded Witness + Gap Lemmas + Critical Prime Dichotomy. A genuinely new mechanism
   is needed — per Lemma I's diagnosis, one that converts an existential
   per-occurrence divisibility fact into a uniform identity claim.
2. Do NOT re-open the "charging against ω(a_1)/Ω(a_1)" or "charging against growth
   rate O(n)" mechanisms (both confirmed dead ends, twice now). The "batch
   resolution via a hub's Lemma-G prime" mechanism is real (certified as the Hub
   Singleton Batch Lemma) but is confirmed to reduce to FAH in the |F'_H|≥2 case,
   not an independent route.
3. Do NOT re-attempt: the round-2 "universal glue prime"/"cost≤1" claims; round-3's
   |A'|+|B'| size-measure descent or round-5's witness-index descent; round-4's
   PUCL; the "V=∅ always" conjecture; round-5's Universal Singleton Hypothesis (all
   independently falsified/exhausted).
4. If `recruitment-round-charging` is revived, it must open with a framing genuinely
   different from a charging/potential argument over the same recruitment process
   (e.g., attacking the problem's periodicity claim directly via a different
   invariant, not via bounding recruitment rounds) — per CLAUDE.md's diversity
   mandate, since all three charging variants tried this round now point at the same
   wall as the other two approaches.
5. The secondary "periodicity from n=1 literally" gap remains untouched since round 1.

## ROUND 8 — a more basic gap found in the dispatched Fixed-Witness Divisor-Chain
mechanism; a genuine unconditional singleton-case byproduct certified; a new
approach (seed-coupling-induction) opened and independently falsified

**covering-system-construction, Step 8.9 (Fixed-Witness Divisor-Chain).** This
round's dispatched mechanism was: fix a rogue pair's Lemma-G witnesses n_A < n_B,
canonical prime q* := min(F' ∩ F''), and the divisor chain d_n := gcd(a_{n_A}, a_n)
over later A'-type occurrences n; show q* | a_n for all but finitely many such n via
a pigeonhole over the finite divisor set of a_{n_A}, using the outline's proposed
dichotomy ("the pigeonholed alternate prime r either (a) lies in S₀ already,
contradicting rogueness, or (b) is a genuine new candidate, subject to a
canonicality sub-question the outline-reviewer flagged").

The builder carried this out in full and proved the **Divisor-Chain
Well-Definedness Lemma** (d_n ranges over the finite set Div(a_{n_A}) \ {1};
elementary, correct, certified) and then executed the pigeonhole exactly as
dispatched, reaching the point where an alternate prime r ≠ q* is produced dividing
infinitely many A'-type terms. **The reviewer independently re-derived the
dichotomy step and confirms the builder's finding: branch (a) of the outline's
proposed dichotomy is FALSE.** If r ∈ S₀, then since r | a_{n_A} and ρ(n_A) = A',
r ∈ P(a_{n_A}) ∩ S₀ = A' — this is a purely tautological consequence of r being an
element of A' (every element of A', by definition of the extended type, divides
every A'-type term automatically). It carries NO information about whether
r ∈ B', and hence gives NO contradiction with (A', B') being a rogue pair (rogueness
is exactly the statement A' ∩ B' = ∅, which is a claim about S₀-elements shared
between A' and B' specifically; an ordinary element of A' alone, with no
information about B', is entirely consistent with A' ∩ B' = ∅). This gap is prior
to, and independent of, the outline-reviewer's flagged canonicality sub-question
for branch (b) — it kills the dichotomy before that sub-question is even reached.
The reviewer re-derived this from the definitions with no shortcuts and confirms it
is correct and not a misreading of the outline; no certified lemma in the current
stack (Free Facts, Bounded Witness Lemma family, Divisor-Restricted Pigeonhole,
Critical Prime Dichotomy) rules out r ∈ A' ⊆ S₀ as the pigeonhole's outcome.

**Certified byproduct: Singleton-Side FAH Lemma** (`lemmas/singleton-side-fah.md`).
If the far-side witness's outside-core factor set (F' or F'') is a singleton, full
absorption on the corresponding near side follows immediately and unconditionally,
directly from the already-certified Generalized Bounded Witness Lemma — no
pigeonhole or divisor-chain machinery needed. The reviewer independently verified
this is a correct, non-circular corollary (a one-line application of an
already-certified lemma) and re-ran the two supporting computational checks:

- a_1 = 187 (Q = {11,17}): reviewer independently regenerated the sequence and
  confirmed F' = F'' = {7} exactly as the builder reports (rogue pair A'={3,11},
  B'={2,17}, n_A=5, n_B=6, a_5=231=3·7·11, a_6=462=2·3·7·11·(...)). Both singleton,
  so Singleton-Side FAH applies directly.
- a_1 = 4807 at the un-recruited core S₀ = Q = {11,19,23}: reviewer independently
  regenerated the sequence and confirmed a_6 = 4845 = 3·5·17·19, a_7 = 4862 =
  2·11·13·17 (matching the round-6 record exactly), giving F' = {17,3,5},
  F'' = {17,2,13} — **neither a singleton**. Reviewer's own independent Python
  simulation (fresh implementation, N=3000 terms) found **74/1200** later
  {19}-type occurrences (beyond n_B=7) divisible by 17 — a ~6.2% rate, matching
  the builder's reported 50/801 (~6.2%) almost exactly (different sample windows,
  same rate). This independently confirms the general |F'|,|F''| ≥ 2 case is
  genuinely NOT cofinite-divisibility and remains open; Singleton-Side FAH does
  not and cannot cover it.

**Certified: Divisor-Chain Well-Definedness** (`lemmas/divisor-chain-well-definedness.md`,
elementary, correct, unconditional — a clean building block for any future
divisor-pigeonhole attack on FAH).

**Not certified (recorded as in-file guidance per the round-3 Lemma F / round-6
Lemma I precedent):** the negative finding "r ∈ S₀ does not yield a contradiction
with rogueness" — this is a diagnostic about a specific proof attempt's dichotomy,
not a portable, standalone mathematical fact; kept as documented guidance in
`covering-system-construction.md` so this exact dichotomy error is not repeated.

**Verdict: CHANGES REQUESTED (partial).** Real, honestly-reported progress: the
dispatched mechanism's failure point is more precisely located than before (a
gap prior to the previously-flagged canonicality question), a genuine unconditional
special case (Singleton-Side FAH) is now certified, and the workspace's
computational evidence is now correctly understood to have never tested the
genuinely hard regime. Joint FAH itself remains open in general.

**seed-coupling-induction (new approach this round) — reviewer independent
falsification check.** The approach set up an induction on ω(a_1) via removing one
prime from the seed to reduce |Q| by 1, with the Seed-Coupling Lemma claiming an
order-preserving correspondence between the reduced sequence's terms and the
original sequence's Q'-visible skeleton, up to a bounded-frequency exception set.
The reviewer independently reimplemented the entire test from scratch (own Python
greedy-sequence generator, own type-comparison routine, not copying the builder's
code) and reproduced every reported number exactly:

- a_1=105, remove p=7 (Q'={3,5}): mismatch density stabilizes at ≈55.0% across
  N=100 to N=8000 (reviewer got 55.02% at N=8000, matching the builder's number to
  4 significant figures).
- Limiting type frequencies genuinely differ (reduced sequence: 25%/50%/25% for
  types {3,5}/{3}/{5}; original's Q'-visible skeleton: 16.0%/56.0%/28.0%) — this
  rules out any correspondence, however cleverly re-indexed, from repairing the
  mismatch (a density-1-preserving injection would have to preserve limiting
  frequencies).
- All 8 tested |Q|=3 seed/removal combinations where Q' excludes 2 (105 removing
  any of 3/5/7; 30 removing 2; 70 removing 2; 42 removing 2; 165 removing any of
  3/5/11; 385 removing any of 5/7/11) reproduce nonzero, stable mismatch densities
  in the reviewer's own reimplementation (24%–68%, matching the builder's table to
  within rounding); every case where Q' retains 2 gives exactly 0 mismatches
  (reviewer confirmed 0/600, 0/3000, 0/8000 for a_1=30, p=3, at increasing sample
  sizes).

This is a genuine, reproducible falsification, not a bug — independently
reconfirmed from a completely separate implementation. Since any seed with 2 ∉ Q
has no single-prime-removal choice that can retain 2 in Q', the induction as
dispatched cannot avoid the failing regime for such seeds; this kills the mechanism
as scoped, not merely one instance of it. **Verdict: RETHINK.** No lemma is
certified from this approach this round (correctly, since nothing positive was
established — the builder's own "Promotable lemmas: None" is accurate).

## Lemma certification this round (round 8)
- **Certified:** `lemmas/singleton-side-fah.md` (unconditional; genuine special
  case of Joint FAH/Symmetric FAH, correctly explains all prior positive
  computational evidence as non-generic).
- **Certified:** `lemmas/divisor-chain-well-definedness.md` (unconditional,
  elementary; reusable building block).
- **NOT certified:** the "r ∈ S₀ does not contradict rogueness" negative finding —
  correct but non-portable (a diagnostic about one specific proof attempt's
  dichotomy), kept as in-file guidance per the Lemma F / Lemma I precedent.

## ROUND 8 — approach verdicts (independent, per CLAUDE.md's per-approach routing)

- **covering-system-construction** — Verdict: **CHANGES REQUESTED** (partial).
  The dispatched mechanism does not close Joint FAH, but the failure point is now
  precisely and correctly located (more basic than the previously-flagged
  canonicality question), and two new unconditional lemmas are certified as
  byproducts. No overclaim found — every "does not close" claim checks out under
  independent re-derivation, and the computational claims (a_1=187, 4807) were
  independently reproduced with matching numbers.
- **seed-coupling-induction** — Verdict: **RETHINK**. The Seed-Coupling Lemma is
  genuinely, reproducibly false whenever 2 ∉ Q'; the induction as scoped cannot be
  rescued by any single-prime-removal choice for seeds with 2 ∉ Q. Independently
  reconfirmed from a from-scratch reimplementation matching every reported density.
  If the induction-on-ω(a_1) framing is revived, it needs a fundamentally
  different reduction step (not single-prime removal with a term-by-term type
  correspondence) — per the builder's own honest diagnosis, the interaction
  between all k primes of Q is not a sparse perturbation of any (k−1)-prime
  sub-process, so no natural repair of this specific coupling is expected to work.

## Next-round guidance (current, round 8)
1. **Priority 1, unchanged**: FAH and Symmetric FAH (Joint FAH via canonical prime
   q* := min(F'∩F'')) remain the sole open crux. Do NOT re-attempt the Fixed-
   Witness Divisor-Chain mechanism's dichotomy in its dispatched form — branch (a)
   ("r ∈ S₀ ⟹ contradicts rogueness") is FALSE, not merely unclear; any future
   divisor-chain-pigeonhole attempt must find a way to force the pigeonholed
   alternate prime r to be genuinely outside S₀ (r ∉ A') before the canonicality
   question is even reached — this is a strictly prior obstacle to the one the
   outline-reviewer previously flagged.
2. **ALWAYS reuse the two new certified lemmas** (`singleton-side-fah.md`,
   `divisor-chain-well-definedness.md`) — the Singleton-Side case of Joint FAH is
   now fully and unconditionally handled; any future FAH mechanism can assume it
   and focus exclusively on |F'|, |F''| ≥ 2, which is now confirmed (via the
   a_1=4807 un-recruited-core computation, independently reproduced) to be where
   the real difficulty lives — cofinite divisibility genuinely fails there (only
   ~6% rate observed, not merely "not yet proved cofinite").
3. **NEVER re-attempt** "seed-coupling via single-prime removal with a term-by-
   term type correspondence" for an induction on ω(a_1) — falsified this round,
   independently reconfirmed by the reviewer with an exact numeric match on every
   reported density (8/8 non-degenerate failures, 6/6 degenerate-2-dominated
   successes). If an ω(a_1)-induction framing is revived, it needs a genuinely
   different reduction step, not a repair of this one (e.g. removing several
   primes at once, or a wholly different notion of "reduced seed" not based on
   stripping one prime's power from a_1).
4. Do NOT re-attempt any prior falsified/exhausted mechanism (see rounds 1-7
   guidance above, all still valid) — the round-8 additions above extend, not
   replace, that list.
5. The secondary "periodicity from n=1 literally" gap is still exactly where round
   7 left it (Step 9.3/9.4): well-posed only once Joint FAH is resolved (this
   round made that dependency explicit for the first time — see
   `covering-system-construction` Step 9.4). Do not attempt it in isolation before
   Joint FAH.

## ROUND 9 (note) — recap only; full detail lives in the Status header above and in
each approach's own file (the file-maintenance note for round 10: the promised
standalone "ROUND 9 section" was referenced from the Status header but never
appended to this file as a separate section; nothing was lost — round 9's full
technical content is in `covering-system-construction` Step 10 and
`greedy-exchange-cost-potential`'s "ROUND 9" section, and is accurately summarized
in the Status header's round-9 paragraph above). Round 9 refuted the
Recruitment-Budget Lemma (eighth mechanism, `covering-system-construction`) with an
explicit a_1=209/247 counterexample, proved the Cofinite Sufficiency Lemma and
Confined-GCD Lemma (`cofinite-window-capacity-bound`, both certified,
unconditional), and showed the Successor-Transport Reduction Lemma's Successor Claim
collapses into Lemma I's existing dead end (`greedy-exchange-cost-potential`,
Successor-Transport Reduction Lemma certified). No lemma re-verification issues
found this round; all round-9 certifications stand.

## ROUND 10 — three parallel mechanisms retired; the crux is unchanged but the
"missing ingredient" diagnosis is now independently confirmed by three structurally
different proof routes

**Independent verification performed this round (proof-reviewer).** All three
built approaches attacked FAH/Cofinite FAH via genuinely different mechanisms
(magnitude-squeeze, quantitative window/telescoping, and constructive-competitor
minimality). Each is a clean, honestly-reported negative result; none overclaims
`solved`. Full independent re-derivation performed for every load-bearing step (see
`/tmp/round-10/proof-reviewer.md` for the complete audit — summary below).

1. **`covering-system-construction` — Sandwich Genericity / Escape-Cost Vacuity.**
   Re-derived the Sandwich Genericity Theorem from scratch (two-line telescoping of
   strict monotonicity and the certified Bounded Gap Lemma) — correct, trivial,
   unconditional. Re-derived the Escape-Cost Vacuity Theorem's "class-blind premises
   cannot yield a class-sensitive conclusion" argument — a determinism-of-deduction /
   substitution argument, informal in presentation but logically valid and, unlike
   the round-3 Lemma F / round-6 Lemma I precedent, stated as a toolkit-INDEPENDENT
   general principle (not "the CURRENT certified lemma set can't do X"), so it is
   certified as a portable screening lemma (matching the round-9 Witness
   Discontinuity Obstruction precedent for general, non-toolkit-contingent
   obstructions). Numeric premise check (Step 11.5, a_1=4807 at the properly
   recruited core) independently reconfirmed: `D_bad={13}`, `E=E_sym=∅` across all
   9+136 sampled occurrences — consistent with FAH continuing to hold, inconclusive
   for the Escape-Cost Lemma's premise specifically (too few same-bad-class repeats
   to test), exactly as the builder reported. **Verdict: CHANGES REQUESTED
   (partial).**

2. **`greedy-exchange-cost-potential` — Window Resolution / Growing-Constraint
   Obstruction.** Re-derived the Window Resolution Lemma's pigeonhole argument from
   scratch and independently re-ran a fresh simulation on a_1=4807 (own
   trial-division generator, `S₀={2,3,5,7,11,19,23}`, `A'={3,5,19}`): found 4
   occurrences at indices 6, 561, 1114, 2223 — all 3 consecutive gaps exceed 1,
   confirming the Lemma concretely as well as abstractly. Correct, unconditional,
   certified. Re-derived the Growing-Constraint Obstruction's two-case proof
   (Proposition + Obstruction) line by line: the "Escape-Budget premise is true but
   uninformative" claim is correct — the illegality witness `i(c)` genuinely ranges
   up to `n_{j+1}-1`, unboundedly far from the one fixed index `n_B` that
   Confined-GCD controls, exactly as claimed; correctly NOT certified as a portable
   lemma (toolkit-contingent, matches the Lemma F/I precedent, builder's own honest
   labeling). Return-Time Boundedness data (max gap 503→670 growing with sample
   size) is reported as inconclusive-but-suggestive, not overclaimed as a
   falsification. **Verdict: CHANGES REQUESTED (partial).**

3. **`confined-competitor-construction` — Minimality Tautology Lemma.** Re-derived
   the Lemma and Corollary from the problem's bare definition — correct,
   unconditional, one line, no gap. Confirmed it correctly kills the round's
   dispatched Steps 2–3 (the "prove `c` fully legal, contradict minimality" shape)
   and correctly explains Lemma K's internal proof step (Lemma K's own branch-(b)
   derivation is a literal instance of this Lemma's contrapositive). **Found a
   genuine overclaim, not a gap in the proved mathematics but in the file's own
   summary/scope language**: the "Watch out for" and "Promotable lemmas" sections
   claim this kills "the whole family of competitor-construction mechanisms... for
   any construction rule," but the Lemma only rules out strategies that try to
   prove FULL legality of a smaller candidate and derive a direct contradiction from
   that success — it says nothing about, and does not rule out, strategies (like
   round 7's own surviving Lemma K) that instead extract information from the
   GUARANTEED blocking index without ever claiming full legality. This is a real,
   different proof shape not addressed by the Lemma; conflating the two is an
   overclaim in the summary language, though the worked argument in the file's own
   "Application to this round's outline" section stays correctly within scope
   throughout. Certified the Lemma with an explicit scope-narrowing note (see
   `lemmas/minimality-tautology-lemma.md`) so future rounds do not misread its
   reach. The underlying finding (this round's specific dispatched mechanism is
   dead) is fully correct and the Status `unsolved` (for this narrow mechanism) is
   accurate, matching a RETHINK verdict. **Verdict: RETHINK** (the specific
   dispatched "prove full legality" mechanism cannot work as scoped and should not
   be re-attempted in that literal form; a Lemma-K-style blocking-index mechanism,
   if revived, is a DIFFERENT approach not foreclosed by this round's finding).

**Lemma certification this round (round 10).**
- **Certified:** `lemmas/sandwich-genericity-theorem.md` (unconditional, trivial,
  verified).
- **Certified:** `lemmas/escape-cost-vacuity.md` (unconditional, general
  toolkit-independent screening principle, verified).
- **Certified:** `lemmas/window-resolution-lemma.md` (unconditional, verified both
  abstractly and by an independent fresh numeric check).
- **Certified, scope-narrowed:** `lemmas/minimality-tautology-lemma.md` (the Lemma
  and Corollary as literally stated are unconditional and correct; the source
  file's broader "kills the whole family" framing is explicitly NOT certified — see
  the scope note in the lemma file).
- **NOT certified (correctly, per precedent):** Growing-Constraint Obstruction
  (`greedy-exchange-cost-potential`) — a diagnostic about the current certified
  toolkit's reach, not portable; matches the round-3 Lemma F / round-6 Lemma I
  precedent, builder's own honest labeling agreed.

**Net effect on the crux.** Three more mechanisms (algebraic-magnitude,
quantitative-window, and definitional-competitor-construction) are now confirmed
dead, all converging on Lemma I's original round-6 diagnosis via independent proof
routes. This is now a strong, multiply-independently-confirmed structural finding:
FAH/Cofinite FAH cannot be closed by (a) any composition of Free Facts, the Gap
Lemmas (existentially or quantitatively), Confined-GCD, or infinite pigeonhole
(Lemma I, round 6; Growing-Constraint Obstruction, round 10), (b) any purely
class-blind magnitude argument (Escape-Cost Vacuity, round 10), or (c) any
constructive-competitor argument that requires proving full legality (Minimality
Tautology, round 10). What remains untried: a constructive-competitor argument in
the Lemma-K/blocking-index style specifically adapted to a controlled alphabet (not
yet attempted with the Confined-GCD Lemma's finite `Div(b)` as the controlling
structure for the BLOCKING index rather than the candidate `c` itself), or a
genuinely different information source not yet identified by any of the twelve
mechanisms tried so far. Next round should prioritize either (i) a concrete attempt
at a Lemma-K-style blocking-index mechanism using Confined-GCD's finite alphabet to
constrain the BLOCKING term (not the candidate), explicitly checking it is not
already foreclosed by the Growing-Constraint Obstruction's "unbounded witness pool"
finding (it likely needs a different index-selection strategy that stays inside a
bounded pool — not yet attempted), or (ii) an entirely fresh top-level framing (per
CLAUDE.md's plateau-breaking guidance — this is the fourth consecutive round with
all built mechanisms dying at the same underlying wall, now via three genuinely
different techniques, which is exactly the "shared-gap plateau" signal CLAUDE.md
flags for mandatory diversification).

## ROUND 11 — CRT-glue/competitor-construction family and the analytic/sieve-
density family both closed; the crux is now confirmed dead-on-arrival for five
structurally distinct proof-shape families, still unresolved

**Independent verification performed this round (proof-reviewer).** Two builds
this round: (1) `greedy-exchange-cost-potential` completing a rescue attempt of a
mechanism the round-11 outline-reviewer had already killed pre-build; (2)
`sieve-density-exception-bound`, a new approach whose entire round-11 content is a
mandatory pre-build screening that found its own dispatched mechanism dead before
any real construction was attempted. Both are genuine, honestly-scoped negative
results; neither overclaims a proof or manufactures a false rescue. Full
independent re-derivation and, where numeric, independent re-computation performed
for both (summary below).

1. **`greedy-exchange-cost-potential` — Minimal-Modulus Generalization of the CRT
   Magnitude Obstruction.** The round-11 outline-reviewer had already killed the
   literal full-`S₀`-signature CRT-glue construction pre-build (13th mechanism,
   "CRT Magnitude Obstruction": the competitor lands ≈8 orders of magnitude above
   the local window on the test seed `a_1=4807`). This round's build genuinely
   attempted a weaker rescue — matching only a subset of `S₀` (down to a single
   prime of `Q` plus forcing `q*|c`) — rather than merely restating the kill.
   Reviewer re-derived the two-branch dichotomy from scratch: (i) any modulus
   using less than all of `Q` cannot guarantee `c`'s legality against a generic
   earlier term, because Free Facts only guarantees SOME (unidentified) shared
   `Q`-prime with each `a_i`, so guaranteeing legality against `a_1` requires
   agreement on a specific prime of `Q`, and — since Free Facts gives no control
   over WHICH prime a given `a_i` shares with `a_1` — extending the guarantee to
   every `a_i` forces divisibility by every prime of `Q` simultaneously; this half
   of the dichotomy is a genuine, general, seed-independent structural consequence
   of the certified Lemma A (Generalized Bounded Gap Lemma)'s own proof, correctly
   verified. (ii) The magnitude half (that even the cheapest such modulus,
   `min(Q)·q*`, never lands inside the local window) is checked only on the one
   test seed `a_1=4807` — the file is explicit that this is not a fully
   seed-independent theorem, and correctly does NOT claim it is. Reviewer
   independently reimplemented the sequence generator from scratch (own script,
   `/tmp/verify_round11.py`, no shared code with any builder) and reproduced
   EVERY reported number exactly: `Q=P(4807)={11,19,23}`, minimal single-prime-of-`Q`
   modulus `11·17=187`, `2499` consecutive gaps up to `N=2500` with max `38`, mean
   `17.4`, min `2`, and **`0/2499` gaps reach modulus 187** — an exact match. Also
   independently reconfirmed the three sampled rogue occurrences at `n=561,1114,2223`
   have local gaps `15,3,19` and `a_n` factorizations `{3²,5,17,19}`, `{3,5²,17,19}`,
   `{3³,5,17,19}` respectively — exactly matching the reported `A'={3,5,19}`,
   `q*=17` data. No discrepancy found anywhere. The conclusion — this closes the
   entire CRT-glue/competitor-construction family, the workspace's **14th**
   confirmed-dead FAH mechanism — is correctly scoped: the STRUCTURAL half (i) is
   general and portable, the MAGNITUDE half (ii) is a strong, exactly-reconfirmed
   empirical finding on the available test seed, consistent with (and not
   contradicted by) every other seed checked in this workspace to date (gaps are
   always small, `O(a_1)` by the certified Bounded Gap Lemma, while any legality-
   guaranteeing modulus is a product of several of `a_1`'s own prime factors, hence
   typically much larger) — but the file itself, correctly, does not certify this
   as a portable "no sweet spot, for all `a_1`" theorem, matching the round-3 Lemma
   F / round-6 Lemma I precedent for toolkit-diagnostic (not fully general)
   findings. No lemma certified, correctly. **Verdict: CHANGES REQUESTED
   (partial).**

2. **`sieve-density-exception-bound` (new) — Density-Argument Vacuity Corollary +
   Selection-Rule Class-Blindness.** Reviewer independently re-derived the
   Corollary's proof from scratch: it is a direct, faithful extension of the
   already-certified Escape-Cost Vacuity Theorem (round 10) from pairwise
   class-blind facts to window/counting quantities `C(X)` computed from the fixed
   fixed finite data `S₀, F'', b, D_bad, q*` and a window bound `X` alone, with no
   access to which integers in the window are the sequence's own realized terms or
   their observed `gcd`-classes. The proof-by-non-entailment style (two
   hypothetical scenarios agreeing on all `C(X)`-type premises but differing in
   the class-sensitive conclusion) mirrors the already-reviewed and certified
   round-10 original exactly, and is not circular: it depends only on Free Facts
   (via Confined-GCD) and the definitional shape of `C(X)`, never on FAH or any
   other open hypothesis. Confirmed correct, non-circular, and general (not a
   "current toolkit can't do X" diagnostic but a toolkit-independent logical
   principle, matching the certification bar of its parent theorem). Reviewer also
   independently re-derived the second, elementary **Selection-Rule
   Class-Blindness** observation directly from the problem's own recursive
   definition `a_{n+1} := min{c>a_n : gcd(c,a_i)>1 \ \forall i \le n}` — this
   predicate is, by inspection, indifferent to WHICH prime realizes each
   `gcd(c,a_i)>1`, so no aggregate density statistic is ever an input to the rule
   that actually selects each term; this is correct, elementary, and reinforces
   the Corollary's conclusion via a wholly independent argument (not needed for,
   and does not depend on, the Corollary's "two-scenario" framing). Together the
   two arguments give converging, mutually-reinforcing evidence that sub-route (a)
   is dead; sub-route (b) is correctly identified as smuggling in the open crux
   (an unproved decay rate) rather than offering a genuine alternative, correctly
   rejected per CLAUDE.md's "prove, don't conjecture" rule. Also verified the
   trivial `|D_bad|=0` sanity case (E=∅ immediately via Confined-GCD alone,
   correct) and the note that even a best-case density-zero bound would be
   insufficient for the certified Cofinite Sufficiency Lemma's literal-finiteness
   requirement (correct — density zero does not imply finite). **This is the
   workspace's 15th mechanism-count entry but is more precisely described as
   retiring an entire technique family (the analytic/sieve-density family) in one
   round, mirroring `covering-system-construction`'s round-10 Escape-Cost Vacuity
   kill of the magnitude-squeeze family** — no rescue proposed or needed; the
   negative result is complete and honestly reported. One lemma certified
   (`lemmas/density-argument-vacuity-corollary.md`), independently reconfirmed
   correct. **Verdict: RETHINK** (this specific technique family cannot work as a
   route to Cofinite FAH, for a proved structural reason; a future round reviving
   density/sieve ideas against this crux must first identify a concrete
   class-sensitive ingredient outside the ruled-out `C(X)` shape — i.e., a fact
   that inputs the actual `g_n` value of a specific realized term, not a count
   over a window).

**Lemma certification this round (round 11).**
- **Certified:** `lemmas/density-argument-vacuity-corollary.md` (unconditional,
  general toolkit-independent screening principle, independently re-derived and
  verified correct and non-circular).
- **NOT certified (correctly, per precedent):** Minimal-Modulus Generalization of
  the CRT Magnitude Obstruction (`greedy-exchange-cost-potential`) — the
  structural half is general, but the file itself does not claim (and this review
  agrees it should not claim) full seed-independence for the magnitude half;
  matches the round-3 Lemma F / round-6 Lemma I / round-10 Growing-Constraint
  Obstruction precedent for toolkit-diagnostic, non-portable findings.

**Net effect on the crux.** Fourteen mechanisms are now confirmed dead across six
consecutive rounds (6 through 11), spanning existential/pigeonhole arguments,
magnitude/index-sandwich arguments, definitional/tautological minimality
arguments, CRT-glued competitor constructions (in every modulus variant, closed
this round), and now aggregate density/sieve-counting arguments (closed this
round) — five structurally distinct proof-shape families, all independently and
rigorously shown incapable of producing the class-sensitive, cross-occurrence
information FAH/Cofinite FAH needs, with zero counterexamples found by any agent
across every seed tested (now well over 500 seeds cumulative across all rounds).
This is a genuinely sharper, more precisely characterized negative result than
round 10 left off with — the "missing ingredient" diagnosis (first made in round
6) is now proved, not merely suspected, to be unreachable by an increasingly wide
swath of standard technique families.

**Reviewer's honest assessment of convergence vs. exhaustion (requested this
round).** The search is converging in a precise, useful sense — the SHAPE of any
viable future mechanism is now much better characterized (it must supply
identity-level information that directly links `g_n` at one index to `g_m` at
another, or to the construction of a new term, and provably cannot be: existential/
pigeonhole-only, magnitude-only, tautological-minimality-only, CRT-glue-competitor-
only, or density/counting-only) — but it is NOT converging toward an actual proof
of FAH: no round since round 6 has produced a mechanism that gets meaningfully
closer, only mechanisms that are cleanly ruled out. Six consecutive rounds hitting
the identical wall via five independently-designed technique families is exactly
the "shared-gap plateau" pattern CLAUDE.md flags for mandatory diversification —
already flagged by round 10's own guidance, and now one round further without a
genuinely new-in-kind idea being tried (round 11's two builds were, respectively,
a continuation of a magnitude-construction idea and a new-but-still-doomed
density idea; neither is a fundamentally different top-level framing of the whole
problem). Recommendation for round 12: the orchestrator should treat this as the
point to seriously push for ≥1 approach attacking the problem from a genuinely
different global framing — not another variant of "prove disjoint persistent
types share a prime via [technique]" within the same reduction chain. Two
concrete directions not yet tried anywhere in this workspace: (a) an ANALYTIC
argument that uses INDEX-SPECIFIC (not window-aggregate) information — e.g. a
direct estimate on the actual smallest legal candidate's factorization near a
SPECIFIC index, rather than a Mertens-style count over a window (this is
exactly the gap the Selection-Rule Class-Blindness observation identifies: the
rule only ever consults local, index-specific legality, never an aggregate); (b)
revisiting whether the whole "persistent type / covering system" reduction
itself is the most productive framing, versus a direct argument about the
sequence's eventual periodicity that does not go through disjoint-type
reconciliation at all (no such alternative top-level framing has been attempted
in eleven rounds). Given the very strong empirical support for FAH (zero
counterexamples across an enormous and still-growing seed set) and the fact
that fourteen technique families are now rigorously excluded rather than merely
untried, it is plausible that closing this gap genuinely requires a technique
outside this workspace's toolkit so far (e.g. a bespoke identity or an argument
specific to gcd-chains of consecutive greedy terms) rather than a further
recombination of the existing certified lemma stack — round 12 should weigh this
seriously rather than dispatching another straightforward variant.

## Next-round guidance (current, round 11)
1. **Priority 1 (new framing, per the plateau-breaking assessment above):** put at
   least one approach on the table that is NOT another variant of "disjoint
   persistent/extended types must share a core prime" proved via a class-blind or
   window-aggregate technique — five such families are now closed. Consider an
   index-specific (not window-aggregate) analytic argument, or a fundamentally
   different top-level route to periodicity that does not pass through the
   persistent-type reduction at all.
2. Do NOT re-attempt: any CRT-glue/competitor-construction variant (14th
   mechanism, closed in full generality for the structural half); any aggregate
   density/sieve-counting argument against Cofinite FAH without first identifying
   a concrete class-sensitive (index-specific, `g_n`-referencing) ingredient
   outside the `C(X)` shape ruled out by the Density-Argument Vacuity Corollary;
   any of the twelve mechanisms closed in rounds 6–10 (existential/pigeonhole,
   magnitude-sandwich, tautological-minimality — see those rounds' sections
   above for the precise scope of each kill).
3. If a genuinely new framing cannot be found, consider directly targeting a
   SPECIFIC small-`|Q|` or small-seed-family case of FAH with a bespoke
   ad hoc argument (not yet attempted) as a fallback to at least narrow the
   general claim, rather than dispatching another general-mechanism attempt
   doomed to the same five-family wall.
4. The secondary "periodicity from n=1 literally" gap remains untouched since
   round 1 and is lower priority than the primary crux.

## ROUND 12 — mandated plateau-break round: new corridor opened, correctly found
to reduce to the same crux under a new name; one bookkeeping lemma added

**Context.** Six consecutive rounds (6–11) had stalled on FAH/Cofinite FAH with 14
confirmed-dead mechanisms, all within the "persistent-type reconciliation via
class-blind/window-aggregate technique" corridor. Per the round-11 mandate, round
12's outliner opened a genuinely new corridor: combinatorics-on-words / Morse–
Hedlund subword-complexity, applied to the gap sequence `g_n`, plus a bookkeeping
touch on the standing leader.

### subword-complexity-periodicity (NEW) — independent re-verification

**Lemma A (Gap–Periodicity Equivalence).** Independently re-derived by this review
from scratch (three lines of telescoping each direction) — correct, unconditional,
no gap. `a_{n+T}=a_n+L` for all `n≥N` iff `g_{n+T}=g_n` for all `n≥N'`. **Certified**
as `lemmas/gap-periodicity-equivalence.md`.

**Lemma B (Right-Extension Determinism ⟹ eventual periodicity), + RED_1⟹RED_k
corollary.** Independently re-derived by this review: infinite pigeonhole on the
finite set of length-`k` windows gives a colliding pair `i<j`; strong induction
(sliding the window forward by one position at each step, re-applying RED_k to the
shifted pair `i'=i+m-k+1 < j'=j+m-k+1`) extends agreement to all later indices. This
is a genuinely general, problem-independent fact about sequences over a finite
alphabet — verified correct, no gap, no dependence on this problem's structure.
**Certified** as `lemmas/red-k-periodicity-lemma.md`.

**Reduction (§3).** Applying Lemma B to `x=(g_n)` (alphabet `{1,...,a_1}` by the
certified Bounded Gap Lemma) and combining with Lemma A: RED_{k₀} for `(g_n)`, for
some `k₀`, suffices for the problem's primary target. Correctly and fully derived
(the reduction is a direct instantiation, not a bare citation of Morse–Hedlund).

**Proposition (§4, correction to the outline).** Independently re-verified: the
number of "ambiguous" `S₀`-residues (mod `L₀:=∏_{p∈S₀}p`) is automatically at most
`L₀`, by bare finiteness of the residue alphabet — no further argument. This is a
correct, useful negative finding: it shows the outline's headlined "Finite-Defect
Boundedness" target, read literally as "finitely many colliding classes," carries
zero content beyond what was already known (the Bounded Gap Lemma's alphabet
finiteness). Cross-checked against the outline text (`/tmp/round-12/proof-
outliner.md` lines 68–91): the outline itself already flags this precise risk
("PROVIDED every sufficiently long run of visits eventually lands only in safe
classes — itself a claim needing proof, not automatic"), so this is a correct
sharpening of an already-flagged risk, not a straw-man mis-scoping of the outline's
real claim — verdict on adversarial check (a) in the dispatch: **the vacuous-target
finding is genuine and correctly scoped.**

**Theorem C (EEA ⟹ periodicity).** Independently re-derived by this review. The
core argument (functional graph `h(r):=(r+f(r)) mod L₀` on the finite set of safe
residues, pigeonhole on `L₀+1` consecutive residues among `≤L₀` safe values, forward
determinism of `h` propagating the collision) is correct and yields an explicit
`T≤L₀`. **Gap found and resolved by this review:** the source proof's definition of
"safe residue" is internally inconsistent — the prose definition ("all visits
eventually agree") suggests finitely many early exceptions are tolerated, but the
crisp negation given ("ambiguous = some two visits differ") is a strictly stronger,
zero-tolerance condition, and the proof itself contains a self-flagged "wait, we
must double check" digression trying to reconcile the two readings. Resolution:
under the zero-tolerance reading (the one actually forced by the stated negation),
"safe" simply means `g_n=f(r)` for every visit to `r`, and the digression is
unnecessary — `g_n=f(r_n)` for `n≥N` (the EEA threshold) follows immediately with
no adjustment. The remainder of the proof (the functional-graph pigeonhole) is
independent of this issue and goes through unchanged. **Certified** as
`lemmas/eea-implies-periodicity.md`, with "safe" redefined to the zero-tolerance
reading and the confused digression removed — this is a wording/definition
correction, not a change to the mathematical content used elsewhere in the file
(matches the round-1/5/10 precedent of certifying with a corrected statement).
Verdict on adversarial check (b): **Theorem C is a genuine, independently-checked
alternative derivation of the CRT finish's true hypothesis, not a circular
restatement** — its dependency on EEA is real and EEA is not secretly assumed
elsewhere.

**§5 (why this doesn't close the gap).** Independently re-derived: unpacking "residue
r becomes safe" requires the successor rule, which checks `gcd` against *every*
earlier term, to eventually depend only on the finite `S₀`-residue — but the
certified Confined-GCD Lemma already shows the finer, decision-relevant information
lives in primes outside `S₀` (the `F'/F''` data), so proving a *given* ambiguous
residue becomes safe after one recruitment round is, after unwinding definitions,
literally an instance of full (non-cofinite) FAH for that instance. This review
re-derived this reduction independently and confirms it: EEA is not demonstrably
easier than FAH; it is the same crux in different vocabulary. No new mechanism for
establishing EEA (or FAH) was found by builder or reviewer.

**§6 (mandated numerical check).** Independently spot-re-ran a subset (`a_1=4807`,
coarse core `S₀=Q`): reproduces the reported high ambiguity fraction. Consistent,
expected (Finite Core Theorem already says `Q` alone is insufficient in general),
correctly not over-read as informative either way by the builder.

**Verdict: CHANGES REQUESTED (Status: partial).** Real, substantial, and
independently-verified new content: two general certifiable lemmas (A, B), a
correct reduction, a genuine correction of the outline's headline target (shown
vacuous), and a new equivalent-in-difficulty restatement of the crux (EEA) with a
clean sufficiency proof (Theorem C, certified after a wording fix). The primary
crux (FAH/Cofinite FAH, now equivalently EEA at some finite core) is NOT closed —
this build's own diagnosis (§5, independently reconfirmed) shows EEA requires the
same content as FAH. Builder's own reported Status (`partial`) is accurate; no
overclaim to correct.

### covering-system-construction (bookkeeping-only touch) — independent
re-verification

**Reduced-Alphabet Corollary.** Independently re-derived: for a rogue pair with
`F'={q'}` a singleton, the `B'`-side is fully resolved (Singleton-Side FAH,
imported, already certified), and for any `q*∈F''`, `D_bad(q*):={d∈Div(b):d>1,
q*∤d}` (with `b:=∏_{p∈F''}p^{v_p(a_{n_B})}`) has size `∏_{p∈F''\{q*}}(e_p+1)−1` — a
one-line divisor-counting bijection argument. Independently re-verified against the
seed `a_1=4807` by direct computation in this review: `S₀={2,3,5,11,19,23}`,
`a_6=4845=3·5·17·19`, `a_7=4862=2·11·13·17`, `F'=P(a_6)\S₀={17}` (singleton, as
required), `F''=P(a_7)\S₀={13,17}`, `b=13·17=221`, `Div(221)={1,13,17,221}`,
`D_bad(17)={13}`, size 1, exactly matching the closed-form prediction
`(v_13(a_7)+1)-1=(1+1)-1=1`. Verdict on adversarial check (c): **the closed-form
count and the `|F''|=2`/multiplicity-1 collapse-to-1 claim are both correct**, fully
unconditional (built only from the already-certified Free Facts, Confined-GCD
Lemma, and Singleton-Side FAH Lemma — no circularity), and honestly scoped by the
builder as pure bookkeeping that does NOT resolve FAH (does not rule out even the
single remaining divisor class `d=13`; does not generalize to a uniform bound
across all `|F''|`). **Certified** as `lemmas/reduced-alphabet-corollary.md`
(file already present from the build; this review confirms and finalizes its
certification).

**Verdict: CHANGES REQUESTED (Status: partial).** Correct, small, honestly-scoped
addition; does not close or narrow the primary crux beyond bookkeeping. No
overclaim — builder never claimed otherwise.

### Answer to adversarial check (d): no overclaim

Neither approach's builder marked itself `solved`, and this review confirms neither
should be: FAH/Cofinite FAH (equivalently, EEA at some finite core) remains open.
**Status of `imo-2026-06` stays `partial`.**

## Lemma certification this round (round 12)
- **Certified:** `lemmas/gap-periodicity-equivalence.md` (Lemma A, unconditional,
  verified).
- **Certified:** `lemmas/red-k-periodicity-lemma.md` (Lemma B + RED_1⟹RED_k
  corollary, unconditional, fully general — reusable outside this problem).
- **Certified (wording corrected):** `lemmas/eea-implies-periodicity.md` (Theorem
  C) — "safe residue" redefined to the zero-tolerance reading (every visit to `r`
  gives the same gap, not merely "eventually"), removing an internally
  inconsistent/self-flagged-uncertain digression in the source proof; the
  mathematical content used by the rest of the argument is unaffected.
- **Certified:** `lemmas/reduced-alphabet-corollary.md` (already present from the
  build; independently re-verified correct, non-circular, unconditional —
  finalized).
- **NOT certified (correctly, per builder's own framing):** the "vacuous target"
  Proposition (§4) — recorded above as an important negative/clarifying finding to
  prevent re-litigation, but it is a one-line consequence of already-certified
  facts, not independently reusable content warranting its own lemma file.

## Next-round guidance (current, round 12)
1. **The crux is now available in TWO equivalent vocabularies**: FAH/Cofinite FAH
   (persistent-type/divisibility language) and **EEA** (residue/safe-visit
   language, subword-complexity-periodicity's framing). This round's independent
   re-derivation confirms they are the same difficulty, not that one is a
   shortcut — do not re-dispatch a builder hoping EEA is "secretly easier" without
   a genuinely new ingredient not already in the certified stack.
2. Do NOT re-attempt: the "count, don't eliminate" / finite-defect-boundedness
   idea in its literal form — proved vacuous this round (Proposition, §4).
3. If a future subword-complexity attempt is revived, its only hope per this
   round's diagnosis is finding an INDEPENDENT route to EEA/RED_{k₀} that does NOT
   pass through "prove a specific recruited prime divides literally every later
   occurrence of a type" — i.e. it needs the same missing ingredient as FAH
   (identity-level, not existence- or magnitude-level, information about
   intermediate terms), not a repair of Theorem C or Lemma B (both already fully
   proved and certified).
4. Fifteen FAH-equivalent mechanisms are now confirmed unable to close the crux
   in their attempted forms (14 from rounds 6–11, plus this round's EEA route
   shown equivalent-not-easier). Per CLAUDE.md's plateau-breaking guidance, if
   round 13 still cannot find a genuinely new ingredient, escalate to the
   bespoke small-`|Q|`/small-seed-family fallback flagged since round 11 (e.g.
   attempt FAH unconditionally for `|Q|≤2` or `|F'|=|F''|=2` specifically, using
   this round's Reduced-Alphabet Corollary's explicit `D_bad` alphabet — for
   `|F''|=2`, multiplicity-1, the alphabet is a SINGLE divisor class `d`, i.e. the
   open question reduces to a single yes/no divisibility-persistence question for
   ONE fixed integer `d` — this may be the most concretely attackable residual
   target in the workspace).
5. The secondary "periodicity from n=1 literally" gap remains untouched since
   round 1, lower priority than the primary crux.

## ROUND 14 — Self-Absorbing Core Theorem's proof gap closed and certified;
16th FAH mechanism confirmed dead via a genuinely new (integer-monovariant)
technique family

### n1-periodicity-reconciliation (revise) — independent re-verification

Round 13's proof-reviewer flagged a specific gap: the Self-Absorbing Core
Theorem's "combining both parts" step cited `covering-system-construction`
Step 5's construction (a one-paragraph proof defining a strictly NARROWER set
`G := {r : sig(r) ∈ 𝒫'}`, with no case-split of any kind) to justify a claim
about this theorem's own, differently and more broadly defined `G*`. This
round's builder replaced the citation with a self-contained two-part
derivation:

- **(S) Sufficiency**, for an arbitrary candidate `c`: split into legality
  against `j ≤ N(S*)` (via self-absorption, `P(a_j) ⊆ S*`, plus the standard
  CRT signature fact) and legality against `N(S*) < j ≤ n` (via the second
  conjunct of `G*`'s definition applied with `B := ρ_{S*}(j) ∈ 𝒫'(S*)`, using
  Extended Persistent-Type Pigeonhole applied AT LEVEL S* — this review
  confirmed the certified lemma `extended-persistent-type-pigeonhole.md` is
  stated and proved generically for "any fixed finite S₀ ⊇ Q," so instantiating
  it at S* is legitimate reuse, not a new unproved step).
- **(L) Landing**, for the real `a_{n+1}` specifically: the early-term conjunct
  follows directly from the certified, unconditional Free Facts Lemma
  (`free-facts-gcd.md` part 1, which literally IS the problem's own recursive
  definition unwound) plus self-absorption; the persistent-type conjunct
  follows from directly unpacking the theorem's own stated hypothesis "FAH
  holds at level S*" applied to the pair of TYPES `(ρ_{S*}(n+1), B)` for
  arbitrary `B ∈ 𝒫'(S*)` — no citation to Step 5's construction anywhere.
- **Assembly**: a minimality argument (any candidate strictly between `a_n`
  and `a_{n+1}` fails legality against some `j ≤ n`, hence by the contrapositive
  of (S) has residue outside `G*`) shows `a_{n+1}` is exactly the next `G*`-
  residue in cyclic order, forcing the residue sequence into a single
  `|G*|`-cycle from `n = N(S*)` onward.

**Independent re-verification (this review, from scratch, not trusting the
builder's self-assessment).** Re-derived every step above line by line:

1. Step 1's CRT-signature equivalence chain (`gcd(c,a_j)>1 ⟺ P(c)∩P(a_j)≠∅ ⟺
   (P(c)∩S*)∩P(a_j)≠∅ ⟺ sig(c mod L*)∩P(a_j)≠∅`, using `P(a_j)⊆S*`) is valid —
   confirmed by direct set-theoretic reasoning; no gap.
2. Step 2's first conjunct correctly invokes Free Facts Lemma part 1
   (`gcd(a_j,a_{n+1})>1` for ALL `j≤n`, which is literally the recursive
   definition of the sequence — checked against `lemmas/free-facts-gcd.md`
   directly, matches exactly).
3. Step 2's second conjunct: checked that the theorem's stated hypothesis
   "FAH holds at level S* — every two elements of 𝒫'(S*) intersect" is
   correctly and completely unpacked (no case-split needed: `A' := ρ_{S*}(n+1)`
   is one fixed element of 𝒫'(S*), and the hypothesis applies directly to the
   pair `(A', B)` for any `B`). No gap.
4. **A precision point NOT flagged by the builder, checked independently by
   this review**: elsewhere in this workspace, "FAH holds at level S" always
   means specifically "every two DISJOINT-BASE-TYPE extended-persistent types
   intersect" (see the definition of gap (†) above) — a priori a weaker-
   sounding statement than "every two elements of 𝒫'(S*) intersect" (which
   includes same/overlapping-base-type pairs too). This review verified these
   two formulations are in fact EQUIVALENT, not merely similar: for any two
   `A', B' ∈ 𝒫'(S)`, writing `A := A'∩Q`, `B := B'∩Q` for their base types,
   `ρ_S(n)∩Q = τ(n)` exactly (since `Q ⊆ S`), so `A ⊆ A'` and `B ⊆ B'`; if `A∩B
   ≠ ∅` (bases not disjoint), any shared prime of `A,B` already lies in
   `A'∩B'`, so non-disjoint-base pairs intersect automatically and for free,
   independent of any FAH-type hypothesis. Hence "every two elements of
   𝒫'(S*) intersect" reduces exactly to "every two DISJOINT-base-type elements
   intersect" (the standard FAH statement) plus this free fact — i.e. the
   theorem's hypothesis, though phrased more strongly, is NOT actually a
   stronger burden than standing FAH-at-S*: discharging one discharges the
   other. The approach file asserts this equivalence ("unpacked literally,
   this is exactly the statement...") without deriving it; this review
   supplies the missing one-line derivation. This does not sink the theorem
   (which is self-contained given its hypothesis, however phrased) but is
   worth recording so a future round doesn't mistakenly think it needs to
   prove something STRONGER than standard FAH to discharge this theorem's
   hypothesis.
5. Step 3's assembly (minimality ⟹ residue-driven rule ⟹ single cycle) is a
   correct redo of the same cyclic-pigeonhole mechanism already used
   (unconditionally) in Step 5 of `covering-system-construction`, now
   verified directly for the broader `G*`, with no circular appeal to Step 5
   itself. No gap.

**Conclusion: the previously-flagged "combining both parts" gap is genuinely
closed.** The Self-Absorbing Core Theorem's proof is complete and rigorous,
strictly conditional on its two disclosed hypotheses (S* self-absorbing; FAH
holds at S*), neither of which is proved or claimed to be proved here — both
correctly remain open per the file's own §4. The reported 6-seed computational
check (N(S*)-agnostic, testing whether the plain tail-derived N₁' can be taken
as 0) is correctly scoped as weaker evidence, not a proof of either sub-gap.

**Certified**: `lemmas/self-absorbing-core-theorem.md`, with the "Verification
note" ("has not yet been independently re-verified... treat as provisionally-
promotable") removed and replaced with this review's confirmation, plus the
precision note (point 4 above) added to the lemma file's Scope section.

**Verdict: CHANGES REQUESTED** (Status `partial` — a genuinely complete,
gap-free conditional theorem is real progress on the secondary n=1 gap, but
neither the theorem's own two open hypotheses nor the primary FAH crux
elsewhere in the population is touched this round).

### integer-monovariant-difference-identity (new) — independent re-verification

This approach imported crux `aimo-0134`'s bounded-integer-monovariant +
difference-identity mechanism and searched for an analogous statistic in this
problem that would sidestep "which specific prime recurs" entirely. This
review independently:

1. **Re-derived `aimo-0134`'s own proof from scratch** (the builder's §0
   re-derivation matches: `b_k := (a_1+\dots+a_k)/k` is an integer by that
   problem's own rule, `(k+1)b_{k+1} \le kb_k+k` gives `b_{k+1}<b_k+1`,
   integrality sharpens to `\le`, descent + boundedness give eventual
   constancy, and the identity `a_k=(k+1)b_{k+1}-kb_k` transfers this to the
   original sequence) — confirmed this is exactly the mechanism claimed,
   correctly re-derived, not just asserted.
2. **Reimplemented the greedy sequence completely independently** (different
   script, no reuse of the builder's code) for both mandated seeds and
   reproduced the reported numbers EXACTLY:
   - `a_1=4807`: max gap 38, min gap 2; running average of gaps increases at
     1196/2498 steps (≈48%); `D_2=11 → D_3=1`.
   - `a_1=11305`: max gap 14, min gap 2; running average increases at 998/2498
     steps (≈40%); `D_2=5 → D_3=1`.
   This is an exact match to the builder's reported figures — strong
   independent confirmation, not a re-run of the same script.
3. **Independently re-derived the §3 general diagnosis**: this problem's
   greedy legality test (`gcd(c,a_i)>1` for all `i≤n`, `c` minimal) references
   only THAT a shared prime factor exists, never WHICH one — a fact already
   certified in this workspace (Same-Type Free Facts Vacuity, Selection-Rule
   Class-Blindness). Any statistic built purely from counts, minima, gcds, or
   averages of the resulting sequence inherits this blindness: it can detect
   that SOMETHING stabilizes without ever being forced, by a genuine per-step
   algebraic identity, to reveal an actual prime identity — exactly the
   ingredient FAH needs and none of the 5 candidates supply. This is a
   genuinely new, sound structural argument (not a repackaging of a
   previously-certified lemma) reached via a technique family (bounded integer
   monovariants / difference identities) not previously tried in this
   workspace's 13 prior rounds.
4. Checked for a missed sixth candidate within my review time budget (e.g. a
   statistic combining running-core-size with a fixed per-step witness-index
   marker) — found no candidate escaping the same class-blindness diagnosis;
   this corroborates, rather than merely accepts, the builder's negative
   conclusion.

**Verdict: RETHINK** (Status `unsolved`, correctly self-reported — no
counterexample to FAH sought or claimed, no progress toward closing gap (†),
an honest and well-documented negative result). This closes the ENTIRE
integer-monovariant/difference-identity technique family for this problem
(16th confirmed-dead FAH-adjacent mechanism), via a genuinely different
technique than any of the 15 prior dead mechanisms (none of which had
previously tried a bounded-monovariant/difference-identity transplant) — a
useful, non-redundant addition to the population's negative-result record, not
a repeat of an already-known dead end.

## Lemma certification this round (round 14)
- **Certified**: `lemmas/self-absorbing-core-theorem.md` — the "combining both
  parts" gap flagged by round 13's proof-reviewer is closed; the theorem is a
  complete, rigorous, conditional (on S* self-absorbing + FAH-at-S*) proof.
  Precision note added to the file per this review's point 4 above (the
  theorem's hypothesis is equivalent to, not stronger than, standard FAH-at-S*).
- **Not proposed / not certified**: no new lemma from
  `integer-monovariant-difference-identity` — every computed fact (§2.2, §2.3's
  monotonicity/boundedness) is an immediate elementary consequence of already-
  certified lemmas, and the §3 diagnosis is recorded here in `current.md` (and
  in the approach file) as a standing screening checklist per the Lemma-F/
  Lemma-I precedent, not certified as a standalone portable lemma (correctly,
  per the builder's own framing — this review concurs).

## Next-round guidance (current, round 14)
1. **The primary FAH/Symmetric FAH/Cofinite FAH/EEA crux is now confirmed
   unclosable by 16 distinct mechanisms** (15 from rounds 6–13, plus this
   round's integer-monovariant/difference-identity family) — this is now the
   NINTH consecutive round (6–14) on the same underlying obstruction (existential-
   to-universal / class-blind-to-class-sensitive promotion). Per CLAUDE.md's
   plateau-breaking guidance, round 15 should strongly consider either (a) the
   bespoke small-`|Q|`/small-`|F''|` fallback flagged since round 11 (attack the
   single fixed-integer divisibility-persistence question that
   Reduced-Alphabet-Corollary reduces the `|F''|=2`, multiplicity-1 case to
   directly, rather than the general claim), or (b) a genuinely new corridor
   as different from the FAH/EEA/monovariant/CRT/sieve/Ramsey corridors already
   tried as subword-complexity-periodicity was from those before it.
2. **The secondary n=1 gap now has ONE fully-proved conditional theorem**
   (Self-Absorbing Core) narrowing it, with two remaining, honestly disclosed,
   FAH-adjacent-in-difficulty sub-gaps: (a) existence/termination of a
   self-absorbing core S* (the absorption operator `S↦S⁺` reaching a fixed
   point), (b) `N(S*)=0`. A future round attacking this secondary gap should
   target (b) directly (the file's own suggestion: analyze why `a_1` and the
   earliest few terms already satisfy the tail-derived residue-cycle rule,
   rather than via enlargement/absorption) since the 6-seed computational
   evidence (round 13) suggests this may be more directly provable than (a).
3. Do NOT re-attempt any bounded-integer-monovariant / difference-identity
   mechanism for FAH (running average/min/gcd/count of any sequence derived
   from this problem) without a genuinely class-sensitive ingredient not
   already ruled out by the §3 diagnosis (round 14).
