# Lemma SCF (Singleton-Chain Forcing) + full closures for `a_1=2747` and
`a_1=4087` (3rd and 4th solved concrete instances)

**Source.** `approaches/sunflower-inadmissibility-toolkit.md`, §15–18
(round 14). Depends only on already-certified Lemma WF
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`), Theorem
CD, Lemma SW1, Theorem 5.1. Does NOT use Backbone Permanence / the
running intersection `B_k` / the refuted EBS mechanism at all — a
structurally different, unconditional route.

## Lemma SCF (Singleton-Chain Forcing)

**Statement.** Let `S,S'\subseteq P_1` be disjoint nonempty cores. If
`i_1,\dots,i_r` (`r\ge1`) all have `S(i_t)=S'` and `\mathrm{comp}(a_{i_t})=
\{\pi_t\}` singleton, then `A:=\{\pi_1,\dots,\pi_r\}\subseteq\mathrm{comp}
(a_k)` for every `k\in I_S`.

**Proof.** `r` independent applications of Lemma WF (one per `t`), each
giving `\pi_t\in\mathrm{comp}(a_k)` for every `k\in I_S`; intersect.
`\blacksquare` (Trivial aggregation of already-certified unconditional
facts — reviewer confirms no interaction/case-split needed between the
`r` applications, each is independently and unconditionally true for the
whole infinite class `I_S`.)

## Instance 1: `a_1=2747=41\times67`, `P_1=\{41,67\}`, `H=\{2,3,7,41,67\}`

**Witnesses** (independently reproduced by the reviewer, fresh
antichain-generator + `sympy.factorint`, exact match):
`a_3=2814=2\cdot3\cdot7\cdot67` (`S=\{67\}`, `\mathrm{comp}=\{2,3,7\}`),
`a_{13}=3321=3^4\cdot41` (`S=\{41\}`, `\mathrm{comp}=\{3\}`),
`a_{14}=3362=2\cdot41^2` (`S=\{41\}`, `\mathrm{comp}=\{2\}`),
`a_{163}=11767=7\cdot41^2` (`S=\{41\}`, `\mathrm{comp}=\{7\}`).

**Proof.** By Lemma SCF (`S:=\{67\}`, `S':=\{41\}`, witnesses `a_{13},
a_{14},a_{163}`): `\{2,3,7\}\subseteq\mathrm{comp}(a_k)` for every
`k\in I_{67}`. By Lemma WF (`S:=\{41\}`, `S':=\{67\}`, witness `a_3`):
`\mathrm{comp}(a_i)\cap\{2,3,7\}\ne\varnothing` for every `i\in I_{41}`.
Combining: any `i\in I_{41},j\in I_{67}` share a prime of `\{2,3,7\}`
(the prime witnessing `i`'s intersection with `\{2,3,7\}` is, by the
first fact, automatically in `\mathrm{comp}(a_j)` too). Since `P_1` has
only 3 nonempty subsets and the sole disjoint pair is
`\{\{41\},\{67\}\}`, this plus Lemma SW1 (intersecting cores) gives
`H:=\{2,3,7,41,67\}` satisfies FCBC for the whole sequence. `\blacksquare`

**Consequence.** `L=\mathrm{lcm}(2,3,7,41,67)=115{,}374`, `T=|\mathrm{Good}|`,
`a_{n+T}=a_n+L` for every `n\ge1`. Complete, unconditional solved instance.

## Instance 2: `a_1=4087=61\times67`, `P_1=\{61,67\}`, `H=\{2,61,67\}`

**Witnesses** (independently reproduced): `a_5=4288=2^6\cdot67`
(`S=\{67\}`, `\mathrm{comp}=\{2\}`), `a_{54}=7442=2\cdot61^2` (`S=\{61\}`,
`\mathrm{comp}=\{2\}`).

**Proof.** By Lemma WF (`S:=\{61\}`, `S':=\{67\}`, witness `a_5`,
singleton `\mathrm{comp}=\{2\}`): `2\mid a_k` for every `k\in I_{61}`. By
Lemma WF (`S:=\{67\}`, `S':=\{61\}`, witness `a_{54}`, singleton
`\mathrm{comp}=\{2\}`): `2\mid a_k` for every `k\in I_{67}`. So every
`i\in I_{61},j\in I_{67}` share the prime `2`. Combined with Lemma SW1 for
the sole intersecting-core cases (`P_1` again has 3 nonempty subsets, one
disjoint pair), `H:=\{2,61,67\}` satisfies FCBC. `\blacksquare`

**Consequence.** `L=\mathrm{lcm}(2,61,67)=8{,}174`, `T=|\mathrm{Good}|`,
`a_{n+T}=a_n+L` for every `n\ge1`. Complete, unconditional solved
instance — the simplest closure in this workspace's history (a single
common prime, `2`, forced unconditionally on both disjoint-core classes).

## Independent verification (proof-reviewer, round 14)

Re-derived all 6 witness factorizations (both instances) via
`sympy.factorint` and a fresh, independently-written antichain-based
generator, cross-validated exactly against brute force on early terms.
Re-generated both sequences to `N=20{,}000` and confirmed, via a complete
class-size count and signature check, **exact match** to the claimed
numbers: `2747`: `|I_{41}|=19{,}203`, `|I_{67}|=389`,
`|I_{41,67}|=408` (`19{,}203+389+408=20{,}000`), zero violations of
`\{2,3,7\}\subseteq\mathrm{comp}` on `I_{67}` and `\mathrm{comp}\cap
\{2,3,7\}\ne\varnothing` on `I_{41}`; `4087`: `|I_{61}|=10{,}312`,
`|I_{67}|=9{,}375`, `|I_{61,67}|=313` (sums to `20{,}000`), zero
violations of `2\in\mathrm{comp}` on both `I_{61}` and `I_{67}`. Re-derived
Lemma SCF's proof and both 4-step instance closures by hand — no gap
found. This does NOT repeat the round-12 finite-prefix-mistaken-for-
permanence overclaim: Lemma WF is unconditionally true for the entire
infinite class by construction (built only from unconditional Lemma P′),
so these numerical checks are cross-checks of already-unconditional
claims, not the source of the claims' validity.

## Certification

Certified `solved`-quality (sorry-free) for Lemma SCF and both instance
closures. `a_1=2747` and `a_1=4087` are fully, unconditionally solved
concrete instances of the whole IMO problem — the 3rd and 4th such
instances (after `a_1=15`, `a_1=247`).
