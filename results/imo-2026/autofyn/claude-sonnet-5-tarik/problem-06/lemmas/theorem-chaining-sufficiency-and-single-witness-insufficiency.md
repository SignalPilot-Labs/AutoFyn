# Chaining Sufficiency Theorem + Single-Witness-Per-Side Insufficiency Proposition

**Source.** `approaches/sunflower-bundle-closure.md`, §10 (round 13).

**Purpose.** A general, abstract formalization of the "finite low-index
witness-chaining" mechanism (independently also constructed, in concrete
instance-specific form, by `forced-primes-well-ordering`'s Lemma WF/
Theorem FW1/FW2 this same round — see
`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`; the two
are complementary: this file gives the general sufficient condition and
an exact characterization of the minimal (single-witness) case, the other
gives concrete instance closures). Needs only the already-certified Lemma
P′ and Lemma XC; no Backbone Permanence, no running/class-wide
intersection, no realized/blocked (Lemma ERD-C) dichotomy.

## Setup

Fix a doubly-infinite disjoint-core pair `(S,S')`. A **witness
collection** is `R=R_S\cup R_{S'}` with `R_S\subseteq I_S,R_{S'}\subseteq
I_{S'}` finite and nonempty. `W:=\bigcup_{r\in R}\mathrm{comp}(a_r)`
(finite). For `\rho\in R`, `W_\rho:=\mathrm{comp}(a_\rho)`.

`\mathcal T_S(R):=\{\tau\subseteq W:\tau\cap W_\rho\ne\varnothing\ \forall
\rho\in R_{S'}\}`, symmetrically `\mathcal T_{S'}(R)`. `R` **succeeds**
if `\tau\cap\tau'\ne\varnothing` for every `\tau\in\mathcal T_S(R)`,
`\tau'\in\mathcal T_{S'}(R)` — a finite, mechanically-checkable
combinatorial condition on the explicit sets `\{W_\rho\}_{\rho\in R}`.

## Theorem (Chaining Sufficiency Theorem)

**Statement.** If a witness collection `R` succeeds for `(S,S')`, then
`W:=\bigcup_{r\in R}\mathrm{comp}(a_r)` solves Conjecture (JW) for
`(S,S')`: `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W\ne\varnothing`
for **every** `i\in I_S,j\in I_{S'}`.

**Proof.** Fix `i\in I_S,j\in I_{S'}`. Let `\tau:=\mathrm{comp}(a_i)\cap
W`, `\tau':=\mathrm{comp}(a_j)\cap W`. For any `\rho\in R_{S'}`, Lemma P′
gives `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_\rho)\ne\varnothing`, and
Lemma XC (disjoint cores `S,S'`) upgrades this to `\mathrm{comp}(a_i)
\cap W_\rho\ne\varnothing`; since `W_\rho\subseteq W`, `\tau\cap W_\rho
\ne\varnothing`. This holds for every `\rho\in R_{S'}`, so `\tau\in
\mathcal T_S(R)`. Symmetrically `\tau'\in\mathcal T_{S'}(R)`. Since `R`
succeeds, `\tau\cap\tau'\ne\varnothing`, i.e. `\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\cap W\ne\varnothing`. Lemma XC again gives this equals
`\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap W`. `\blacksquare`

No size or index-order hypothesis on `R` is used anywhere — unconditional
for any successful `R`, of any size. What it does **not** do is guarantee
a successful `R` exists (Conjecture (WCE), left open, see below).

## Proposition (Single-Witness-Per-Side Insufficiency)

**Statement.** For `R_S=\{i_0\},R_{S'}=\{j_0\}` (`|R|=2`, the minimal
case — in particular the case supplied "for free" by Lemma CB +
Escape-Confinement, and by the round-12 Matched-Witness construction),
writing `A:=\mathrm{comp}(a_{i_0})`, `B:=\mathrm{comp}(a_{j_0})`: `R`
succeeds **iff** `A=B` and `|A|=1`.

**Proof.** `\mathcal T_S(R)=\{\tau\subseteq A\cup B:\tau\cap B\ne
\varnothing\}`, `\mathcal T_{S'}(R)=\{\tau'\subseteq A\cup B:\tau'\cap A
\ne\varnothing\}`. (⟸) If `A=B=\{p\}`, every admissible `\tau,\tau'`
contains `p`. (⟹) If `|B|\ge2`: pick `b\ne a` for any `a\in A,b\in B`,
set `\tau=\{b\},\tau'=\{a\}`, disjoint, contradiction (symmetric for
`|A|\ge2`). If `|A|=|B|=1$ with `A\ne B`, i.e. `A=\{a_0\}\ne\{b_0\}=B`:
`\tau=\{b_0\},\tau'=\{a_0\}` are disjoint, contradiction. `\blacksquare`

**Consequence.** Subsumes round 11's rigidity-wall diagnosis and round
12's Matched-Witness refutations (`4199`,`247`: both have `A=B` but
`|A|=2\ne1`) into one clean characterization: no single-witness-per-side
candidate can ever succeed unless the two witnesses share the exact same
singleton companion set. This is why `4199`'s construction genuinely
needed `\ge2` witnesses per side.

## Non-vacuity check (explicit counterexample to a natural free shortcut)

The "obvious free" choice `R:=` Lemma FT's own transversal
representatives does **not** always succeed: on `a_1=247`,
`(S,S')=(\{13\},\{19\})`, with Lemma FT's `S`-side companion sets
`A_1=\{2,5\},A_2=\{3,7\}` and `S'`-side `B_1=\{2,7\},B_2=\{3,5\}`, taking
`\tau=\{2,3\}\in\mathcal T_S(R)` and `\tau'=\{5,7\}\in\mathcal
T_{S'}(R)$ gives `\tau\cap\tau'=\varnothing` — `R` fails, even though
`W=\{2,3,5,7\}` is (separately, numerically confirmed) known to solve
(JW) for this pair. So the Theorem's hypothesis is strictly stronger than
its conclusion in general; a successful `R` is a real, non-vacuous
existence question (Conjecture (WCE)), not automatic.

## Independent re-verification (proof-reviewer, round 13)

Re-derived both proofs by hand from the stated definitions — no gap
found. Independently re-verified the `4199:(13,17)` instantiation
(`R_S=\{2,9\}$, `R_{S'}=\{5,12\}`, `W=\{2,3,83\}`) reproduces exactly the
same 15-pair check as `forced-primes-well-ordering`'s independently
constructed Theorem FW1 (cross-checked: both approaches converge on the
identical witness structure and conclusion for this instance, a genuine
cross-approach corroboration, not a coincidence — both derive from the
same underlying Lemma P′+XC composition). Independently hand-verified
the `A_1,A_2,B_1,B_2` non-vacuity counterexample's arithmetic (`\{2,3\}
\cap\{2,7\}=\{2\}`, `\{2,3\}\cap\{3,5\}=\{3\}`, `\{5,7\}\cap\{2,5\}=
\{5\}`, `\{5,7\}\cap\{3,7\}=\{7\}`, `\{2,3\}\cap\{5,7\}=\varnothing`) —
correct.

## Certification

Certified `solved`-quality (sorry-free) for the Chaining Sufficiency
Theorem and the Single-Witness-Per-Side Insufficiency Proposition.
Reusable: any future approach attacking Conjecture (JW) for a specific
pair can cite the Theorem as the target sufficient condition instead of
re-deriving the disjunction-chaining mechanism; the Insufficiency
Proposition rules out, once and for all, retrying any single-witness
variant. Conjecture (WCE) itself (does a successful `R` always exist for
an arbitrary Case-B pair?) is honestly left open, and is proved (§10.7 of
the source) to be no easier than Conjecture (JW) in general (WCE⟹JW via
this theorem, so a full proof of WCE would already solve (JW); the
converse is not established).
