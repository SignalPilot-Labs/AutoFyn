# Theorem CI (Case I ⟹ 𝓥 finite, unconditional, explicit stabilization index)

## Status

Certified `solved`-quality (sorry-free), **fully unconditional** (only
assumes Case I — a single prime `p` divides every `a_n` — which is itself
already completely solved by the already-certified Lemma S′; Theorem CI is
not needed to finish Case I, but is a genuine, reusable, fully general
result showing exactly what a proof of `𝓥`-finiteness looks like when an
explicit closed form for `a_n` is available).

## Statement

Suppose Case I holds: prime `p` divides `a_n` for every `n≥1`. Write
`a_1=pm` (`m:=a_1/p`). Let `k_0:=\min\{k≥1:p^k≥a_1\}`,
`N_0:=p^{k_0-1}-m+1`. Then `N_0≥1` is a well-defined positive integer,
`𝓜_n=\{\{p\}\}` for every `n≥N_0`, and `𝓥⊆\{P_i:1≤i≤N_0\}` is finite.

## Proof

By the already-certified Lemma S′, `a_n=a_1+p(n-1)=p(m+n-1)` for **every**
`n≥1` — the sequence is the explicit arithmetic progression of exactly the
multiples of `p` that are `≥a_1` (bijectively, `a_n=pt` with `t=m+n-1≥m`).
Since `p≥2`, `p^k→∞`, so `k_0` is well-defined; minimality gives
`p^{k_0-1}<a_1≤p^{k_0}`, i.e. `t_0:=p^{k_0-1}≥m` (from `p^{k_0}≥a_1=pm`), so
`N_0:=t_0-m+1≥1`. By the bijection, `a_{N_0}=p·t_0=p^{k_0}`, a pure prime
power, so `P_{N_0}=\{p\}`.

Fix `n≥N_0`. `\{p\}∈𝓜_n`: no set is a proper subset of a singleton other
than `∅` (never a radical, since `a_i>1`), so no `k≤n` dominates
`P_{N_0}=\{p\}`; `N_0≤n` gives `N_0∈M_n`. No other value is in `𝓜_n`: any
`i≤n` with `P_i≠\{p\}` has `p∈P_i` (Case I) and `P_i≠\{p\}`, so
`\{p\}⊊P_i`; since `N_0≤n`, `k=N_0` witnesses `i∉M_n`. So `𝓜_n=\{\{p\}\}`
exactly, for every `n≥N_0`: this is (MRS) with index `N_0`. By the
`(⇐)` direction of Theorem V (`theorem-V-veto-finite-iff-MRS.md`),
`𝓥=⋃_{n=1}^{N_0}𝓜_n⊆\{P_i:i≤N_0\}`, finite. ∎

## Independent numerical re-verification (proof-reviewer, round 5)

Applied the closed form to the flagged hard case `a_1=11623=59·197`
(**hidden Case I**, `p=59`, `m=197`): fresh Python gives `k_0=3`
(`59^2=3481<11623≤59^3=205379`), `N_0=59^2-197+1=3285`.

Independently generated the **entire** sequence from scratch (fresh
brute-force greedy simulator, exact `math.gcd`, no reuse of any builder's
code) to `n=3300` and confirmed:
- `a_n=11623+59(n-1)` for **every** `n≤3300` tested (exact arithmetic
  progression from `n=1`, confirming Case I holds and Lemma S′ applies).
- `a_{3285}=205379=59^3` exactly, matching `p^{k_0}` from the closed form.
- Direct `O(n^2)` computation of `𝓜_n` (independent of the incremental
  algorithm): `|𝓜_{3284}|=459` (a large "fan" of two-prime radicals), and
  `𝓜_{3285}=\{\{59\}\}` exactly — collapsing to the singleton **exactly** at
  `n=N_0=3285`, matching the closed form to the exact index, not just
  approximately. Confirmed stable (`𝓜_{3300}=\{\{59\}\}`) through the tested
  range.

This is an exact, independent, from-scratch confirmation (not a re-run of
the builder's own script) that Theorem CI's closed form is correct to the
exact stabilization index, not merely asymptotically or approximately.

## Certification

Certified `solved`-quality, unconditional. Reusable as a template/sanity
check for any future proof strategy for the still-open Case-II
`𝓥`-finiteness gap: it demonstrates the mechanism (a single absorbing
"pure-power" term dominating an entire accumulated fan) that any Case-II
proof would need an analogue of, without an explicit closed form for `a_n`.

## Source

`results/imo-2026-06/approaches/persistent-backbone-monovariant.md` (round
5).
