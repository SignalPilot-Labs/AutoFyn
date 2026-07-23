# Corollary FW1-FCBC (full 6-channel closure): `a_1=4199` is a SECOND
fully solved concrete instance

**Source.** `approaches/forced-primes-well-ordering.md`, §M (round 14).
Depends only on already-certified facts: Lemma WF + Corollary P″
(`lemmas/lemma-WF-witness-forcing-and-theorem-FW-instances.md`), Lemma XC
(`lemmas/lemma-XC-NIDF-FT-cross-companion-transversal.md`), Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`), Lemma SW1 and
Theorem SW (`lemmas/theorem-SW-stabilization-sufficiency.md`), Theorem 5.1
(`lemmas/theorem-5.1-master-conditional-theorem.md`). No new general
mathematical machinery — this is an instance-specific closure using 6
applications of the already-certified Lemma WF, but is certified as a
freestanding result because it is a complete, self-contained solved
instance.

## Setup

`a_1=4199=13\cdot17\cdot19`, `P_1=\{13,17,19\}`. `P_1` has `7` nonempty
subsets, hence `\binom{7}{2}=21` unordered pairs, of which exactly `6` are
disjoint (direct hand count, re-derived and confirmed independently by the
reviewer): `(\{13\},\{17\})`, `(\{13\},\{19\})`, `(\{17\},\{19\})`,
`(\{13\},\{17,19\})`, `(\{17\},\{13,19\})`, `(\{19\},\{13,17\})`.

## Witnesses (6, independently re-derived by the reviewer via a fresh
antichain-based generator cross-validated against brute force, and via
`sympy.factorint`, exact match on every value)

```
a_2  = 4212 = 2^2 · 3^4 · 13     S={13}      comp={2,3}
a_5  = 4233 = 3 · 17 · 83        S={17}      comp={3,83}
a_9  = 4316 = 2^2 · 13 · 83      S={13}      comp={2,83}
a_11 = 4332 = 2^2 · 3 · 19^2     S={19}      comp={2,3}
a_12 = 4352 = 2^8 · 17           S={17}      comp={2}
a_92 = 5967 = 3^3 · 13 · 17      S={13,17}   comp={3}
```

(A 7th candidate witness, `a_82=5746=2\cdot13^2\cdot17`, `S=\{13,17\}`,
`\mathrm{comp}=\{2\}`, was proposed by the round-14 outline but shown
redundant by the builder — reviewer confirms: it could only be applied
against `I_{19}`, where it would force `2\mid a_k`, already supplied more
directly by `a_{12}`. Correctly not used in the final closure.)

## Statement

`H:=\{2,3,13,17,19,83\}` satisfies FCBC for the entire sequence
`a_1=4199,a_2,a_3,\dots`: `H\cap\mathrm{rad}(a_i)\cap\mathrm{rad}(a_j)\ne
\varnothing` for every `1\le i<j`.

## Proof

Fix `1\le i<j`. `S(i),S(j)` well-defined nonempty subsets of `P_1`
(Theorem CD). If `S(i)\cap S(j)\ne\varnothing`, Lemma SW1 gives a common
prime in `P_1\subseteq H`. Otherwise `\{S(i),S(j)\}` is (up to swapping)
one of the 6 disjoint pairs above. Each of the 6 channels is closed by an
exhaustive 2-case Boolean split derived from Lemma WF applied to the
witnesses above (full case tables re-derived by the reviewer by hand,
matching the approach file's §M.2–M.3 exactly):

- Channel `(\{13\},\{17\})` = Theorem FW1 (already certified): `W=\{2,3,83\}`.
- Channel `(\{13\},\{19\})`: `2` unconditional on both sides (from `a_12`,
  `a_92`). `W=\{2\}`.
- Channel `(\{17\},\{19\})`: `2\wedge3` unconditional on the `\{19\}` side
  (from `a_11`, `a_92`), `2\vee3` on the `\{17\}` side (from `a_2`). `W=\{2,3\}`.
- Channel `(\{13\},\{17,19\})`: 2-case split on `2\mid a_j` using
  `I_{13}`'s `2\wedge(3\vee83)` and `I_{17,19}`'s `(2\vee3)\wedge(2\vee83)`
  (identical shape to `I_{17}`). `W=\{2,3,83\}`.
- Channel `(\{17\},\{13,19\})`: mirror image of the above, using `I_{17}`'s
  `(2\vee3)\wedge(2\vee83)` and `I_{13,19}`'s `2\wedge(3\vee83)` (identical
  shape to `I_{13}`). `W=\{2,3,83\}`.
- Channel `(\{19\},\{13,17\})`: `2\wedge3` unconditional on the `\{19\}`
  side, `2\vee3` on the `\{13,17\}` side (from `a_{11}`). `W=\{2,3\}`.

All 6 give a common prime in `\{2,3,83\}\subseteq H`. `\blacksquare`

## Consequence

By already-certified Theorem 5.1, `L=\mathrm{lcm}(2,3,13,17,19,83)=
2{,}091{,}102`, `T=|\mathrm{Good}|`, `a_{n+T}=a_n+L` for every `n\ge1`.
Complete, unconditional proof of the IMO problem's conclusion for
`a_1=4199` — a SECOND fully solved concrete instance (after `a_1=247`).
Does NOT prove the general problem.

## Independent verification (proof-reviewer, round 14)

Re-derived all 6 witness factorizations via `sympy.factorint` and an
independently-written antichain-based generator (cross-validated exactly
against brute force on early terms). Re-derived the `21`-pair exhaustive
enumeration by hand (`15` intersecting `+6` disjoint `=21=\binom{7}{2}`).
Re-generated `a_1=4199` to `n=12{,}000` with a fresh generator and
confirmed, via a complete (not sampled) `\{2,3,83\}`-signature
cross-check per core class, **exact match** to the class-size counts
claimed (`|I_{13}|=2791`, `|I_{17}|=6156`, `|I_{19}|=1816`,
`|I_{13,17}|=681`, `|I_{13,19}|=156`, `|I_{17,19}|=343`,
`|I_{13,17,19}|=57`) and **zero violations** of every one of the 6
channel-closure claims. Re-derived all 6 Boolean case splits by hand — no
gap found.

## Certification

Certified `solved`-quality (sorry-free). `a_1=4199` is a fully,
unconditionally solved concrete instance of the whole IMO problem — the
second such instance (after `a_1=247`) and the largest to date
(`|P_1|=3`, 6 disjoint core-pair channels).
