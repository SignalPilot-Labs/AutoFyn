# Lemma WF (Witness Forcing) + Corollary P″ + Theorem FW1/FW2 + Corollary FW2-FCBC

**Source.** `approaches/forced-primes-well-ordering.md`, §L (round 13).

**Purpose.** A genuinely new mechanism for Conjecture (JW) (per-pair
Stabilization Conjecture witness): fixed, low-index, EXACTLY-COMPUTED
witnesses combined with the already-certified Lemma P′ (unordered form)
and Lemma XC force a disjunctive/singleton constraint on **every** member
(not just a numerically-observed prefix) of a complementary-core class —
no running intersection, no "realized/blocked" dichotomy (Lemma ERD-C), no
Backbone Permanence hypothesis needed at all. Structurally different from,
and not subsumed by, every prior Case-B mechanism (Realized-Backbone/UCR,
killed by the certified Sandwich Uniqueness Lemma for `4199:(13,17)`;
Matched-Witness, refuted by `sunflower-bundle-closure`'s hand
counterexamples; NIDF-pigeonhole, blocked by the certified Row-Restriction
Obstruction).

## Setup

`P_1:=\mathrm{rad}(a_1)`, `S(i):=\mathrm{rad}(a_i)\cap P_1` (Theorem CD's
core map, total and nonempty), `\mathrm{comp}(a_i):=\mathrm{rad}(a_i)
\setminus P_1`.

## Corollary P″ (unordered Lemma P′)

**Statement.** For every `i\ne j` (no ordering assumed),
`\gcd(a_i,a_j)>1`.

**Proof.** `\gcd` is symmetric; WLOG `i<j`; apply the already-certified
Lemma P′ (`lemmas/lemma-P-prime-pairwise-intersecting.md`) directly.
`\blacksquare`

## Lemma WF (Witness Forcing)

**Statement.** Fix disjoint nonempty cores `S,S'\subseteq P_1` and a fixed
index `i_0` with `S(i_0)=S'`. Then for **every** `k\in I_S` (no
restriction on `k` relative to `i_0`),
`\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_0})\ne\varnothing`.

**Proof.** `k\ne i_0` since `S(k)=S\ne S'=S(i_0)`. By Corollary P″,
`\gcd(a_k,a_{i_0})>1`, i.e. `\mathrm{rad}(a_k)\cap\mathrm{rad}(a_{i_0})
\ne\varnothing`. Since `S(k)=S`, `S(i_0)=S'` are disjoint, the
already-certified Lemma XC
(`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`) gives
`\mathrm{rad}(a_k)\cap\mathrm{rad}(a_{i_0})=\mathrm{comp}(a_k)\cap
\mathrm{comp}(a_{i_0})`. Combining gives the claim. `\blacksquare`

**Corollary (Disjunctive Forcing).** If `\mathrm{comp}(a_{i_0})=
\{q_1,\dots,q_r\}` (`r\ge1`), every `k\in I_S` satisfies `q_1\mid
a_k\vee\dots\vee q_r\mid a_k`. When `r=1` this is an unconditional single
forced prime.

## Theorem FW1 (`4199:(\{13\},\{17\})`, `W=\{2,3,83\}`)

**Statement.** For every `i\in I_{13},j\in I_{17}` (of `a_1=4199`),
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,83\}\ne\varnothing`.

**Witnesses (exact factorizations, independently reproduced by the
proof-reviewer via `sympy.factorint` and by an independently-written,
cross-validated antichain-based generator against a naive brute-force
generator, exact agreement on the first 30+ terms and on all four cited
values):**
`a_2=4212=2^2\cdot3^4\cdot13` (`S=\{13\}`, `\mathrm{comp}=\{2,3\}`),
`a_5=4233=3\cdot17\cdot83` (`S=\{17\}`, `\mathrm{comp}=\{3,83\}`),
`a_9=4316=2^2\cdot13\cdot83` (`S=\{13\}`, `\mathrm{comp}=\{2,83\}`),
`a_{12}=4352=2^8\cdot17` (`S=\{17\}`, `\mathrm{comp}=\{2\}`).

**Proof.** Lemma WF (Corollary) gives: [FACT1] every `i\in I_{13}` has
`2\mid a_i` (from `a_{12}`, singleton); [FACT2] every `i\in I_{13}` has
`3\mid a_i\vee83\mid a_i` (from `a_5`); [FACT3] every `j\in I_{17}` has
`2\mid a_j\vee3\mid a_j` (from `a_2`); [FACT4] every `j\in I_{17}` has
`2\mid a_j\vee83\mid a_j` (from `a_9`). Fix arbitrary `i\in I_{13},j\in
I_{17}`. Case `2\mid a_j`: by FACT1, `2\mid a_i` too, so `2` is a common
factor. Case `2\nmid a_j`: FACT3 forces `3\mid a_j`; FACT4 forces `83\mid
a_j`; so `a_j` has both `3,83`; FACT2 gives `3\mid a_i\vee83\mid a_i`,
either disjunct is then a common factor with `a_j`. `\blacksquare`

**Independent verification.** Proof-reviewer re-derived all four
factorizations and the case-split logic from scratch, and independently
re-generated `a_1=4199` to `N=400{,}000` with a fresh antichain-based
generator (cross-validated against brute force on the first 30 terms):
`I_{13}` (`93{,}036` members at this depth) has exactly `3` distinct
`\{2,3,83\}`-signatures — `\{2,3\},\{2,83\},\{2,3,83\}` — all containing
`2`, exactly matching FACT1; `I_{17}` (`205{,}226` members) has exactly `5`
distinct signatures, each either containing `2` or containing both `3,83`;
all `3\times5=15` signature-pairs intersect, zero violations.

## Theorem FW2 (`247:(\{13\},\{19\})`, `W=\{2,3,5,7\}`)

**Statement.** For every `i\in I_{13},j\in I_{19}` (of `a_1=247`),
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap\{2,3,5,7\}\ne\varnothing`.

**Witnesses (independently reproduced exactly):**
`a_2=260=2^2\cdot5\cdot13` (`\mathrm{comp}=\{2,5\}`),
`a_3=266=2\cdot7\cdot19` (`\mathrm{comp}=\{2,7\}`),
`a_4=273=3\cdot7\cdot13` (`\mathrm{comp}=\{3,7\}`),
`a_5=285=3\cdot5\cdot19` (`\mathrm{comp}=\{3,5\}`),
`a_6=312=2^3\cdot3\cdot13` (`\mathrm{comp}=\{2,3\}`),
`a_7=342=2\cdot3^2\cdot19` (`\mathrm{comp}=\{2,3\}`).

**Proof.** Lemma WF gives 6 disjunctions: (from `a_2,a_4,a_6`, targeting
`I_{19}`) `\forall j\in I_{19}`: `2\vee5`, `3\vee7`, `2\vee3` (mid `a_j`);
(from `a_3,a_5,a_7`, targeting `I_{13}`) `\forall i\in I_{13}`: `2\vee7`,
`3\vee5`, `2\vee3`. **Lemma A** (`I_{19}` reduction): every `j\in I_{19}`
satisfies `(2\wedge3)\vee(2\wedge7)\vee(3\wedge5)` — case split on `2\mid
a_j`. **Lemma B** (`I_{13}` reduction, symmetric): every `i\in I_{13}`
satisfies `(2\wedge3)\vee(2\wedge5)\vee(3\wedge7)`. An exhaustive
`3\times3=9`-case table (all nine `(\pi_i,\pi_j)` pattern-pairs) confirms
every combination shares a prime in `\{2,3,5,7\}`. `\blacksquare`

**Independent verification.** Proof-reviewer re-derived Lemma A/B's case
splits and the `9`-case table by hand (all nine combinations checked,
matching exactly); independently re-generated `a_1=247` to `N=400{,}000`
(fresh generator): `I_{13}` (`215{,}282` members) has `8` distinct
`\{2,3,5,7\}`-signatures, `I_{19}` (`138{,}206` members) has `8` distinct
signatures, all `64` signature pairs intersect (zero violations), and
Lemma A/B's patterns hold with zero exceptions across every member
checked.

## Corollary FW2-FCBC (`a_1=247` is a fully solved concrete instance)

**Statement.** For `a_1=247`, `H:=\{2,3,5,7,13,19\}` satisfies FCBC:
`H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne\varnothing` for every
`1\le i<j`. Consequently (already-certified Theorem 5.1,
`lemmas/theorem-5.1-master-conditional-theorem.md`), there exist explicit
`T=|Good|`, `L=\mathrm{lcm}(2,3,5,7,13,19)=51{,}870`, with
`a_{n+T}=a_n+L` for **every** `n\ge1`.

**Proof.** Fix `1\le i<j`. `S(i),S(j)` well-defined nonempty subsets of
`P_1=\{13,19\}` (Theorem CD). Two exhaustive cases: `S(i)\cap S(j)\ne
\varnothing` — Lemma SW1 (`lemmas/theorem-SW-stabilization-
sufficiency.md`) gives a common prime in `P_1\subseteq H`; `S(i)\cap
S(j)=\varnothing` — since `P_1` has only 3 nonempty subsets and the only
disjoint unordered pair is `\{\{13\},\{19\}\}`, this forces (up to
swapping `i,j`) `i\in I_{13},j\in I_{19}`, and Theorem FW2 gives a common
prime in `\{2,3,5,7\}\subseteq H`. `\blacksquare`

**Scope.** This is a complete, unconditional proof of the IMO problem's
conclusion for the SPECIFIC instance `a_1=247` only — it does NOT prove
the general problem (open for arbitrary `a_1`). It is, to this
workspace's knowledge as of round 13, the first fully closed concrete
instance beyond the trivial Case I (single saturating prime).
`4199:(\{13\},\{17\})` is only 1 of `4199`'s `6` disjoint core-pair
channels — `a_1=4199` itself remains open.

**Reusable proof template.** Any future `a_1` with `|P_1|=2` for which the
single resulting disjoint core pair's Conjecture (JW) is proved is
automatically, by the identical 3-line argument, a fully solved concrete
instance.

## Independent re-verification (proof-reviewer, round 13)

Every factorization cited above independently re-derived via `sympy.
factorint`; the sequences independently regenerated to `N=400{,}000` for
both `a_1=4199` and `a_1=247` with a fresh antichain-based generator
(cross-validated against a naive brute-force generator on early terms);
all case-split logic (Theorem FW1, Lemma A, Lemma B, the 9-case table,
Corollary FW2-FCBC's 2-case split) re-derived by hand from the stated
hypotheses with no gap found. Confirmed the argument uses only
already-certified facts (Lemma P′, Lemma XC, Theorem CD, Lemma SW1,
Theorem 5.1) plus the new Lemma WF and the exact, hand-verified
factorizations of finitely many fixed low-index terms — critically, this
is NOT the round-12 "finite prefix mistaken for infinite claim" flaw: the
witnesses are FIXED, EXACTLY KNOWN indices, and Lemma WF is a fully
general, unconditionally-true-for-the-whole-infinite-sequence statement
(built only from Lemma P′, itself unconditional), so Theorem FW1/FW2's
conclusions hold for literally every member of the infinite classes
`I_{13},I_{17},I_{19}`, not merely a numerically-checked prefix.

## Certification

Certified `solved`-quality (sorry-free) for Lemma WF, Corollary P″,
Theorem FW1, Theorem FW2, and Corollary FW2-FCBC as stated. This is a
genuine milestone: the first fully, unconditionally solved concrete
instance (`a_1=247`) of the whole IMO problem produced by this workspace.
Does NOT solve the general problem (open for arbitrary `a_1`) — `current.
md`'s overall Status remains `partial`.
