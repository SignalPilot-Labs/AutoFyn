# Lemma WO (Window Occupancy) + Proposition BI (Backbone Permanence Does Not Force Class Revisitation)

**Source.** `approaches/intersecting-family-covering-construction.md`,
Part 12 (round 13).

**Purpose.** Two unconditional facts bearing on the Bounded-Run-Length
property `\mathrm{BRL}(S')` (sufficient, via the already-certified Lemma
PD-from-BRL, for `(PD_{S,S'})`). Lemma WO is a positive existence fact
(CRT); Proposition BI is a negative result ruling out one natural
candidate mechanism (this same round's sibling `sunflower-
inadmissibility-toolkit`'s Backbone Permanence/EBS target) as a route to
closing `\mathrm{BRL}`.

## Lemma WO (Window Occupancy)

**Setup.** `P_1=\mathrm{rad}(a_1)=\{p_1,\dots,p_k\}`, `L_0:=p_1\cdots
p_k`. For any positive integer `x`, `S(x):=\mathrm{rad}(x)\cap P_1`.

**Statement.** For every integer `m\ge0` and nonempty `S'\subseteq P_1`,
the number of integers `x\in(m,m+L_0]` with `S(x)=S'` exactly equals
`c_{S'}:=\prod_{p\in P_1\setminus S'}(p-1)\ge1`, independent of `m`.

**Proof.** `L_0` is a product of `k` distinct primes; by CRT, `\varphi:
\{m+1,\dots,m+L_0\}\to\prod_i\mathbb Z/p_i\mathbb Z`, `\varphi(x):=(x
\bmod p_1,\dots,x\bmod p_k)`, is a bijection (any `L_0` consecutive
integers form a complete residue system mod `L_0`). `S(x)=S'` iff
`\varphi(x)\in T_{S'}:=\prod_{p_i\in S'}\{0\}\times\prod_{p_i\notin
S'}(\mathbb Z/p_i\mathbb Z\setminus\{0\})`. Since `\varphi` is a
bijection, the count equals `|T_{S'}|=\prod_{p_i\notin S'}(p_i-1)=
c_{S'}`. `\blacksquare`

**Independent verification (proof-reviewer, round 13).** Verified the
formula by direct brute-force enumeration in Python for `P_1=\{13,19\}`
(all 4 subsets, `L_0=247`: counts `216,18,12,1` for `S'=\varnothing,
\{13\},\{19\},\{13,19\}`, matching `\prod(p-1)` exactly) and for
`P_1=\{13,17,19\}` (all 8 subsets, `L_0=4199`: counts `3456,288,216,192,
18,16,12,1`, matching exactly in every case). No gap found; combined with
the already-certified Lemma 1 (`a_{n+1}-a_n\le L_0`), a "right-type"
candidate is always present in `(a_n,a_n+L_0]`.

## Proposition BI (Backbone Permanence Does Not Force Class Revisitation)

**Statement.** Suppose there is a companion prime `q\notin P_1` and an
index `N_0` such that `q\mid a_j` for every `j\in I_{S'}` with `j\ge N_0`
(the literal content of the sibling approach's Backbone-Permanence/EBS
target for a single-prime backbone). Then for every `n\ge N_0` and every
integer `x>a_n` with `q\mid x`, `\gcd(x,a_j)>1` for every `j\in I_{S'}
\cap[N_0,n]`, **regardless of `S(x)`**.

**Proof.** `q\mid a_j` (hypothesis) and `q\mid x` (hypothesis on `x`), so
`q\mid\gcd(x,a_j)`, giving `\gcd(x,a_j)\ge q>1`. No property of `S(x)` is
used. `\blacksquare`

**Interpretation.** Even a fully-established Backbone Permanence for
`S'` supplies no logical obstruction to a run of consecutive indices
avoiding `I_{S'}` indefinitely: once the backbone prime `q` stabilizes,
EVERY sufficiently large multiple of `q` — regardless of its `P_1`-type
`S(x)` — discharges the entire infinite family of `I_{S'}`-admissibility
constraints at once. So Backbone Permanence cannot be the mechanism
behind `\mathrm{BRL}(S')`; if the greedy sequence empirically keeps
returning to `I_{S'}`, the reason is a **minimality** phenomenon (which
admissible candidate is numerically *smallest*), not a **feasibility**
phenomenon — and no tool currently certified in this workspace (Domination
Lemma, Lemma RD, Companion-Disjointness Coarsening, Backbone Permanence/
EBS, Lemma WO) reasons about minimality.

**Independent verification (proof-reviewer, round 13).** The proof is a
direct three-line deduction from the stated hypothesis; re-derived by
hand, no gap. This is a genuinely conditional statement (IF Backbone
Permanence holds) and does not depend on whether the sibling approach's
EBS conjecture is itself true — it is a valid negative finding regardless
of EBS's fate (and EBS's literal "two-in-a-row" mechanism was separately
refuted this same round, see
`lemmas/proposition-PVB-and-theorem-TLL-refuted.md` — Proposition BI's
scope is broader, since it applies to ANY eventual single-prime backbone
permanence, proven or not).

## Certification

Certified `solved`-quality (sorry-free) for both Lemma WO and Proposition
BI. Lemma WO is reusable as a standing "candidates always exist nearby"
fact for any future window/pigeonhole argument on the fixed `P_1`-alphabet.
Proposition BI is reusable as a standing "feasibility mechanisms cannot
close BRL/`G`-periodicity" negative result — any future proof attempt for
`\mathrm{BRL}(S')` or `G`-eventual-periodicity must engage with
minimality (which admissible candidate the greedy actually selects), not
mere existence/feasibility of admissible candidates.
