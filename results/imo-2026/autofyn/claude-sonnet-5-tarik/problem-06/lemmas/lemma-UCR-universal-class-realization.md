# Lemma UCR (Universal Class Realization) and Corollary UCR-JW

**Source.** `results/imo-2026-06/approaches/sunflower-inadmissibility-
toolkit.md` §1–2 (round 11). Depends on: already-certified Lemma P′
(`lemmas/lemma-P-prime-pairwise-intersecting.md`) and Lemma ERD-C
(`lemmas/lemma-ERD-realized-blocked-dichotomy.md`).

## Lemma UCR — statement

Let `S,S'\subseteq P_1` be disjoint, with `I_S,I_{S'}` both nonempty
(cores of any two index classes, not necessarily the fixed pair under
study). Let `C` be a nonempty finite set of primes disjoint from `P_1`
(`C\cap P_1=\varnothing`), and suppose `S\cup C` is **realized** in the
sense of Lemma ERD-C: some actual index `m` has `\mathrm{rad}(a_m)=S\cup
C` exactly. Then for **every** index `j\ge1` with `S(j)\cap S=
\varnothing` (`S(j):=\mathrm{rad}(a_j)\cap P_1`; in particular every
`j\in I_{S'}`, since `S\cap S'=\varnothing`):
`C\cap\mathrm{comp}(a_j)\ne\varnothing`, where
`\mathrm{comp}(a_j):=\mathrm{rad}(a_j)\setminus P_1`.

## Proof

`S(m)=\mathrm{rad}(a_m)\cap P_1=(S\cup C)\cap P_1=S` (using `S\subseteq
P_1`, `C\cap P_1=\varnothing`). Since `S(j)\cap S=\varnothing` while
`S(m)=S\ne\varnothing`, `S(j)\ne S(m)`, so `j\ne m`. By Lemma P′ applied
to `\{m,j\}`, `\mathrm{rad}(a_m)\cap\mathrm{rad}(a_j)\ne\varnothing`, i.e.
`(S\cup C)\cap\mathrm{rad}(a_j)\ne\varnothing`. Decompose:
`(S\cup C)\cap\mathrm{rad}(a_j)=(S\cap\mathrm{rad}(a_j))\cup(C\cap
\mathrm{rad}(a_j))`. Since `S\subseteq P_1`, `S\cap\mathrm{rad}(a_j)=
S\cap S(j)=\varnothing` by hypothesis. Hence the union reduces to
`C\cap\mathrm{rad}(a_j)\ne\varnothing`. Since `C\cap P_1=\varnothing`,
`C\cap\mathrm{rad}(a_j)=C\cap\mathrm{comp}(a_j)`, giving `C\cap
\mathrm{comp}(a_j)\ne\varnothing`. `\blacksquare`

**Why this is genuinely new / simpler**: it needs only Lemma P′ applied
directly to the two *actual* indices `m,j`, with no domination/ordering
argument, Permanent-Inadmissibility, or No-Resurrection — order-
independent, unlike the round-11 outline's originally proposed branch-α
mechanism.

## Corollary UCR-JW — statement

Fix a doubly-infinite disjoint core pair `(S,S')` and its Lemma FT
transversal `W:=U_S\cup U_{S'}` (`lemmas/lemma-XC-NIDF-FT-cross-
companion-transversal.md`). Fix `i\in I_S`, write `D(i):=\mathrm{comp}
(a_i)\cap W` (nonempty by Lemma FT). Suppose there exists a nonempty
`C\subseteq D(i)` that is **realized** (`C=\mathrm{comp}(a_{i'})` for
some actual `i'\in I_S`, or any realized `C\subseteq D(i)` more
generally). Then `\mathrm{comp}(a_i)\cap\mathrm{comp}(a_j)\cap W\ne
\varnothing` for **every** `j\in I_{S'}` simultaneously. (Symmetric
statement holds with `S,S'` and `i,j` swapped.)

**Proof.** By Lemma UCR (with this `C`, `S(j)=S'` disjoint from `S`),
`C\cap\mathrm{comp}(a_j)\ne\varnothing` for every `j\in I_{S'}`; pick
`p` in this intersection. Since `C\subseteq D(i)=\mathrm{comp}(a_i)\cap
W`, `p\in\mathrm{comp}(a_i)\cap W` too, so `p\in\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\cap W`. `\blacksquare`

**Definition (WRP).** `(S,S')` (relative to `W`) has the **W-Realization
Property** if every `i\in I_S` and every `j\in I_{S'}` satisfies the
hypothesis of Corollary UCR-JW. WRP `\implies` Conjecture (JW) for
`(S,S')` with this `W`, unconditionally.

## Verification

Independently re-derived the proof of Lemma UCR line-by-line (confirmed:
uses only Lemma P′ and elementary set manipulation, no circularity).
Independently re-simulated WRP checking (own generator + `sympy`
factorization, not the builder's script):

- `a_1=247`, `(S,S')=(\{13\},\{19\})`, `n\le3000`: `U_S=U_{S'}=
  \{2,3,5,7\}=W`. WRP holds: **0/1615** `S`-side failures, **0/1036**
  `S'`-side failures — exactly reproduced the builder's claimed counts.
- `a_1=21528751`, `(S,S')=(\{103\},\{197\})`, `n\le3000`: `W=\{2,3,7,
  13,19,41,193,1301,2297,2549\}` (10 primes). WRP fails on the `S`-side
  for **875/2929** indices (e.g. `i=7`, `\mathrm{comp}(a_i)=\{3,5,929\}`,
  `D(i)=\{3\}`, `S\cup\{3\}=\{103,3\}` not yet certified realized or
  blocked within `n\le3000`); WRP holds on the `S'`-side, **0/52**
  failures — exactly reproduced. A direct joint check of `\mathrm{comp}
  (a_i)\cap\mathrm{comp}(a_j)\cap W\ne\varnothing` over all `2929\times
  52=152{,}308` cross pairs found **zero violations** — reproduced
  exactly, confirming WRP is sufficient-but-not-necessary here.

## Honest scope note (flagged by the reviewer, not the builder)

The builder's own §3 states Conjecture (JW) is "unconditionally proved,
not merely numerical evidence" for `a_1=247`'s pair, based on WRP holding
for all `1615+1036` indices realized within `n\le3000`. **This overstates
what was shown**: `I_S,I_{S'}` are infinite (a defining property of a
doubly-infinite pair), so a check over the finitely many indices realized
within one generated prefix does not constitute a proof of a universal
statement (WRP, and hence Conjecture (JW)) over the full infinite index
classes. The file's own §5 "Caveat on §3's scope" correctly identifies
and retracts this exact overclaim in the same file — the certified
content here is therefore stated at its true strength: Lemma UCR and
Corollary UCR-JW are unconditional, general-purpose facts; WRP/Conjecture
(JW) themselves remain open in general (and open for the full infinite
`a_1=247` instance too, not just the hard `a_1=21528751` one), pending a
mechanism that establishes WRP (or an equivalent) for *every* member of
`I_S,I_{S'}`, not just a finite prefix.
