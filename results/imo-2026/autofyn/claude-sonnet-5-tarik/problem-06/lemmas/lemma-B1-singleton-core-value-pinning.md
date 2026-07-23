# Lemma B1 (Singleton-Core Value Pinning)

**Source.** `results/imo-2026-06/approaches/core-depth-induction.md` (round
6). Builds on Lemma FOM (`lemmas/lemma-FOM-first-occurrence-minimality.md`),
the already-certified Record Characterization Lemma
(`lemmas/theorem-V-veto-finite-iff-MRS.md`), and Theorem CD
(`lemmas/theorem-CD-core-decomposition-and-lemma-TC.md`).

**Setup.** `P_1:=rad(a_1)`, `k:=|P_1|`. Assume `k≥2` (else there is no
proper singleton core — Case I, already fully solved). Fix `p∈P_1`,
`S:={p}` (a proper core since `k≥2`).

**Statement.** Every `C∈𝓥_S` satisfies `a_{n_C}=T_C`, where `n_C` is `C`'s
first-occurrence index and `T_C:=min{x∈ℤ : x>a_1, rad(x)=C}` (Lemma FOM's
notation). Equivalently: `𝓥_{\{p\}}` finite iff only finitely many finite
prime sets `C` with `p∈C` and `C∩(P_1∖\{p\})=∅` are ever `n`-minimal for
some `n≥1`.

**Proof.** Let `C∈𝓥_S` (`S={p}`). By Theorem CD, `C∩P_1=S={p}`, so `C≠P_1`
(since `k≥2`, `C=P_1` would force `C∩P_1=P_1≠\{p\}`). Let
`n_C:=min{n≥1 : rad(a_n)=C}` (`C`'s true first-occurrence index — exists
since `C` is realized by definition of `𝓥_S`). Since `rad(a_1)=P_1≠C`,
`n_C≠1`, so `n_C≥2`. Lemma FOM applies directly with `n:=n_C`: `a_{n_C}=T_C`.
∎

**Discussion.** Genuine, if modest, progress: removes the need to reason
about the sequence's actual growing integer values when studying
`𝓥_{\{p\}}`-finiteness, replacing them with the fixed, `a_1`-and-`C`-
computable quantity `T_C`. Does **not** by itself bound anything — the open
content is entirely "which `C` are ever `n`-minimal." This generalizes
routinely (same proof) to any proper core `S` (not just singletons), simply
replacing `\{p\}` with `S` throughout and using `C≠P_1` from `|S|<k`.

**Independent verification (proof-reviewer, round 6).** Re-derived the proof
from scratch (identical to Lemma FOM's application pattern); logic is sound
and non-circular, correctly restricted to `C≠P_1` via Theorem CD.

## Certification

Correct, complete, reusable. Certified `solved`-quality.
