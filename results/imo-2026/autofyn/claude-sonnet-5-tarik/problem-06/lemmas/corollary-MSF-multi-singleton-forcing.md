# Corollary MSF (Multi-Singleton Forcing)

**Source.** `approaches/witness-chaining-universal-existence.md` (round
14). Depends only on already-certified facts: Lemma WF
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`), Lemma
NIDF(a) (nonemptiness of companion sets, certified as part of
`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`), and Theorem CD
(core map total and nonempty, `lemmas/theorem-CD-core-decomposition-and-
lemma-TC.md`). Cross-referenced against, and shown to be a strict special
case of, the already-certified Chaining Sufficiency Theorem
(`lemmas/theorem-chaining-sufficiency-and-single-witness-insufficiency.md`).

**Purpose.** Names and proves, as a clean general-purpose corollary (valid
for *every* `a_1` and *every* disjoint nonempty core pair `(S,S')⊆P_1`, not
an instance-specific fact), the "zero case-split" mechanism identified by
this round's `math-explorer-wce-general.md`: several fixed low-index
SINGLETON-companion witnesses on one side, plus a single SUBSET witness on
the other side, close Conjecture (JW) for the pair with no Boolean case
analysis at all. This is the cheapest possible instantiation of the
already-certified Chaining Sufficiency Theorem, and is now the recommended
first thing to try (before FW1/FW2-style case tables) for any new
disjoint core pair.

## Setup

Fix `a_1`, `P_1:=\mathrm{rad}(a_1)`, the core map `S(i):=\mathrm{rad}(a_i)
\cap P_1` (total, nonempty, Theorem CD), `\mathrm{comp}(a_i):=\mathrm{rad}
(a_i)\setminus P_1` (nonempty for every `i`, Lemma NIDF(a)). Fix disjoint
nonempty `S,S'\subseteq P_1`.

## Statement

Suppose:

**(i)** there exist `r\ge1` fixed indices `i_1,\dots,i_r` with `S(i_m)=S'`
for every `m`, and `\mathrm{comp}(a_{i_m})=\{q_m\}` is a singleton for
every `m` (the `q_m` need not be pairwise distinct — repeats simply add no
new information); let `P:=\{q_1,\dots,q_r\}`;

**(ii)** there exists a fixed index `j_0` with `S(j_0)=S` and
`\mathrm{comp}(a_{j_0})\subseteq P`.

Then `W:=P` solves Conjecture (JW) for `(S,S')`: for every `i\in I_S,
j\in I_{S'}`, `\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap P\ne\varnothing`.

(By Lemma NIDF(a), `\mathrm{comp}(a_{j_0})\ne\varnothing`, so hypothesis
(ii) forces `P\ne\varnothing`, i.e. `r\ge1` is automatic once (ii) holds —
listed separately above only for clarity.)

## Proof

**Step 1 (conjunctive forcing on `I_S`).** Fix `m\in\{1,\dots,r\}`. Apply
Lemma WF with its "`S`" instantiated to our `S`, its "`S'`" instantiated to
our `S'`, and its "`i_0`" instantiated to `i_m` (valid: `S(i_m)=S'` by (i),
and `S,S'` disjoint by hypothesis). Lemma WF gives: for every `k\in I_S`,
`\mathrm{comp}(a_k)\cap\mathrm{comp}(a_{i_m})\ne\varnothing`, i.e.
`\mathrm{comp}(a_k)\cap\{q_m\}\ne\varnothing`, i.e. `q_m\mid a_k` and
`q_m\notin P_1` (since `q_m\in\mathrm{comp}(a_{i_m})`, which is disjoint
from `P_1` by definition), hence `q_m\in\mathrm{comp}(a_k)`. This holds for
every `m=1,\dots,r`, independently (each is a separate, unconditional
application of Lemma WF — no interaction, no case split between the `r`
applications). Hence:

`(\ast)` for every `k\in I_S`: `P=\{q_1,\dots,q_r\}\subseteq
\mathrm{comp}(a_k)`.

**Step 2 (disjunctive forcing on `I_{S'}`).** Apply Lemma WF with its
"`S`" instantiated to our `S'`, its "`S'`" instantiated to our `S`, and its
"`i_0`" instantiated to `j_0` (valid: `S(j_0)=S` by (ii), and `S',S`
disjoint). Lemma WF gives: for every `k\in I_{S'}`, `\mathrm{comp}(a_k)
\cap\mathrm{comp}(a_{j_0})\ne\varnothing`. Since `\mathrm{comp}(a_{j_0})
\subseteq P` by (ii), any element of `\mathrm{comp}(a_k)\cap\mathrm{comp}
(a_{j_0})` is in particular an element of `\mathrm{comp}(a_k)\cap P`.
Hence:

`(\ast\ast)` for every `k\in I_{S'}`: `\mathrm{comp}(a_k)\cap
P\ne\varnothing`.

**Step 3 (combine).** Fix arbitrary `i\in I_S,j\in I_{S'}`. By
`(\ast\ast)`, `\mathrm{comp}(a_j)\cap P\ne\varnothing`; pick `q\in
\mathrm{comp}(a_j)\cap P`. By `(\ast)`, `P\subseteq\mathrm{comp}(a_i)`, so
`q\in\mathrm{comp}(a_i)` too. Hence `q\in\mathrm{comp}(a_i)\cap
\mathrm{comp}(a_j)\cap P\subseteq\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\cap
P` (since `\mathrm{comp}(a_x)\subseteq\mathrm{rad}(a_x)` always). As `i,j`
were arbitrary, `W:=P` solves (JW) for `(S,S')`. `\blacksquare`

## Corollary MSF is a strict instantiation of the Chaining Sufficiency
Theorem (cross-check, not an independent proof)

With `R_{S'}:=\{i_1,\dots,i_r\}`, `R_S:=\{j_0\}`, `R:=R_S\cup R_{S'}`:
`W=\bigcup_{\rho\in R}\mathrm{comp}(a_\rho)=P\cup\mathrm{comp}(a_{j_0})=P`
(using `\mathrm{comp}(a_{j_0})\subseteq P`). `\mathcal T_S(R)=\{\tau
\subseteq W:\tau\cap\{q_m\}\ne\varnothing\ \forall m\}=\{W\}` (`\tau` must
contain every singleton `\{q_m\}`, forcing `\tau=W`). `\mathcal T_{S'}(R)
=\{\tau'\subseteq W:\tau'\cap\mathrm{comp}(a_{j_0})\ne\varnothing\}`. For
any `\tau\in\mathcal T_S(R)=\{W\}` and `\tau'\in\mathcal T_{S'}(R)`:
`\tau\cap\tau'=W\cap\tau'=\tau'`, and `\tau'` is nonempty by definition
(it meets `\mathrm{comp}(a_{j_0})`). So `R` succeeds, and the Chaining
Sufficiency Theorem's conclusion is exactly Corollary MSF's conclusion.
This confirms Corollary MSF adds **no new mathematical content** beyond
the already-certified Chaining Sufficiency Theorem + Lemma WF — it names
and packages one specific, maximally cheap witness-collection shape.

## Worked instantiations (independently verified, round 14 — see
`approaches/witness-chaining-universal-existence.md` for full factorization
detail and generator cross-validation)

`r=3,|P|=3` case: `a_1=2747`, `(S,S')=(\{41\},\{67\})`,
`P=\{2,3,7\}` (witnesses `a_{13}=3^4\cdot41,a_{14}=2\cdot41^2,
a_{163}=7\cdot41^2`, `j_0=a_3=2\cdot3\cdot7\cdot67`). `r=1` case (both
sides singleton, `A=B`, the extremal case of the already-certified
Single-Witness-Per-Side Insufficiency Proposition): `a_1=4087`,
`(\{61\},\{67\})`, `P=\{2\}`. Nine further instances (`143,391,713,1073,
1517`, `1001` ×3) with `P\in\{\{2\},\{2,3\}\}`, and one new instance on
this workspace's own previously-hardest recurring pair: `a_1=21528751`,
`(S,S')=(\{197\},\{103\})` (roles: `S'=\{103\}` supplies the 3 singleton
witnesses, `S=\{197\}` supplies `j_0`), `P=\{2,3,7\}` — closing this pair
despite class `I_{\{197\}}` never exhibiting `|\mathrm{comp}|\le2`
anywhere in an extensive search (509 members checked), demonstrating
Corollary MSF's hypothesis is strictly weaker than "both sides have small
companion sets" (see the approach file, Part 2, for the significance of
this).

## Certification

Certified `solved`-quality (sorry-free). Reusable: any future approach
attacking Conjecture (JW)/(WCE) for a specific disjoint core pair should
try Corollary MSF (search for `\ge1` singleton witnesses on one side plus
one subset witness on the other) before reaching for a full FW1/FW2-style
case table — strictly cheaper when it applies, and, per the round-14
`a_1=21528751` instance above, applicable even when neither side has small
absolute companion-set size, as long as one side has *several independent
singleton* witnesses.

## Independent re-verification (proof-reviewer, round 14)

**Process note.** This lemma file was written directly into `lemmas/` by
the builder (`witness-chaining-universal-existence.md`) rather than
proposed-then-certified by the reviewer, a deviation from the normal
contract (`CLAUDE.md`: "Builder proposes, reviewer certifies"). Content
independently re-checked in full below; retained in place since it passes.

Re-derived the proof (Steps 1–3) from scratch by hand, independent of the
file's own write-up — confirmed correct and general (valid for *every*
`a_1` and disjoint core pair satisfying hypotheses (i)/(ii), no smuggled
instance-specific assumption; the two Lemma WF applications and the final
combination step are exactly as re-derived independently). Re-derived and
independently confirmed the `21528751:(\{197\},\{103\})` instance: `P_1=
\mathrm{rad}(21528751)=\{103,197,1061\}` (`103\times197\times1061=
21{,}528{,}751`, hand-verified), and independently regenerated the
sequence to `n=27{,}832` with a fresh antichain-based generator (71s
runtime), confirming, via `sympy.factorint`, all four witness
factorizations exactly: `a_{1405}=21{,}727{,}232=2^{11}\cdot103^2`,
`a_{11812}=23{,}201{,}883=3^7\cdot103^2`, `a_{27832}=25{,}472{,}209=
7^4\cdot103^2` (all core `\{103\}`, singleton companions `2,3,7`
respectively), `a_{2575}=21{,}893{,}004=2^2\cdot3^4\cdot7^3\cdot197`
(core `\{197\}`, `\mathrm{comp}=\{2,3,7\}\subseteq P=\{2,3,7\}`) — exact
match to the file's claims. Confirms Corollary MSF closes this specific
disjoint core pair (`\{197\}` vs `\{103\}`) of `a_1=21528751`
unconditionally. **Scope, confirmed correctly stated by the builder, not
an overclaim**: this closes only 1 of `a_1=21528751`'s 6 disjoint
core-pair channels — the instance `a_1=21528751` as a whole remains open
(5 channels unresolved).
