# Certified lemmas — Rejection-Budget Tautology (RBT) + Dichotomy (RBD)

Certified round 6 (proof-reviewer). Source: `approaches/joint-recruitment-budget.md` §1–§2.
Negative guardrail (like `two-anchor-scaffold.md` JSC and `anchor-partition.md` Collapse):
these do NOT close E5″; they certify that the **joint rejection-budget accounting thread cannot
close it**. Notation as in the other lemma files: greedy sequence `a₁,a₂,…`; `M = rad(a₁)`;
`𝓐_∞` = ⊆-minimal supports; `Π = ⋃𝓐_∞`. Cited certified inputs: no-transient
(`no-transient-fixed-successor.md`), E1/E2 (`enumeration-and-transversal.md`), Gap-bound L2
(`free-lemmas.md`), JSC (`two-anchor-scaffold.md`), Collapse (`anchor-partition.md`),
obstruction family (`monovariants-and-obstruction.md`).

## RBT (Rejection-Budget Tautology) — FULLY RIGOROUS, unconditional.
For each `n≥1` let `R_n = {c∈ℤ : a_n < c < a_{n+1}}` (the rejected candidates; every element is
inadmissible since `a_{n+1}=s(a_n)` is the smallest admissible integer `> a_n`, by no-transient).
The rejection stream below `a_N` is `𝓡_N = ⋃_{n=1}^{N-1} R_n`, a set of distinct integers in
`(a₁,a_N)`, of size
```
    |𝓡_N| = Σ_{n=1}^{N-1}(a_{n+1}-a_n-1) = (a_N - a₁) - (N-1) =: Φ_N ≤ (M-1)(N-1) = O(N).
```
(Telescoping identity; the bound from Gap-bound L2, each gap `≤ M`.) Any pairwise-disjoint family
`{C_q ⊆ 𝓡_N}` satisfies `Σ_q |C_q| ≤ Φ_N` (cardinality of a disjoint union of subsets of a finite
set). *Reviewer note:* the identity and the disjoint-sum bound are elementary and were reproduced
by independent simulation (`a₁∈{375,385,867,105}`, `N=400`: `Φ_N = a_N-a₁-(N-1)` exactly, each
gap `≤ M`, `Φ_N ≤ (M-1)(N-1)`).

## RBD (Rejection-Budget Dichotomy) — NEGATIVE guardrail, scoped.
Assume `|P|≥2` (the `|P|=1` prime-power case is the TAS prime-power lock: `𝓐_∞={{p*}}`, Crux
holds outright). Suppose Π infinite, and let `q↦C_q⊆𝓡_N` be any disjoint per-recruit cost
assignment with `|C_q|≥c_q`, `c_q→∞`. Then (CERTIFIED):

- **(rate-not-count)** By RBT, `Σ_{k≤r(N)} c_k ≤ Φ_N ≤ (M-1)(N-1)`. For any threshold `T`, since
  `c_k→∞` there is `K_T` with `c_k≥T` for `k≥K_T`, giving `r(N) ≤ K_T + (M-1)(N-1)/T`. This is an
  UPPER bound on the recruit count that is `O(N/T)` — it forces `r(N)` to grow **sub-linearly** but
  **never bounds it**. An infinite Π with sparse recruitment (the certified obstruction family
  `{p*,q_k}`, density(A)→positive, `Φ_N=Θ(N)`, `r(N)→∞` sub-linearly) satisfies the budget with no
  contradiction. So **no disjoint attribution from `𝓡_N` can contradict Π infinite by cardinality.**
- **(Horn A, bounded local window)** If `C_q ⊆ (∏G_q - M, ∏G_q)`, then `|C_q| ≤ M-1` (an interval
  of length `<M` holds `≤M-1` integers): `c_q ↛ ∞`. Fully rigorous.
- **(Horn B(ii) = JSC, reduction)** Forcing `|C_q|→∞` over the TAS anchor-interval `[t'_k,t_k]`
  (length `≥ q_k`) and then bounding `|t_k-t'_k| ≤ f(a₁)` reduces to the certified-dead JSC bound
  (`t_k-t'_k=q_k(A_k-B_k)`, `A_k≠B_k` ⇒ `|t_k-t'_k|≤f(a₁)` IS `q_k≤f(a₁)`).
- **(vocabulary variant = Collapse, reduction)** Assuming the small-prime part `B=G_q∖{p_max}`
  ranges over a finite set is `∏B<a₁` = E5″ itself (circular); granting it, pigeonholing a common
  core `B` lands on the certified-dead R4 Collapse (`anchor-partition.md`).

## Scope (certified vs. heuristic) — exactly as JSC.
CERTIFIED: RBT; the rate-not-count consequence; Horn A's `M-1` bound; and the two reductions
Horn B(ii)⟶JSC and vocabulary⟶Collapse (pointers to already-certified negatives). These make the
intended positive route (disjoint per-recruit cost `→∞` vs. `O(N)` budget) **provably unavailable**.
NOT a theorem (heuristic, honestly flagged in the source §3): the slogan that Horns A/B/vocabulary
**exhaust every attribution rule** — there is no formal quantifier over "all rules." What is
rule-independent and certified is that RBT holds for ANY disjoint attribution, so the
cardinality obstruction (rate-not-count) is universal. Does NOT close E5″.
