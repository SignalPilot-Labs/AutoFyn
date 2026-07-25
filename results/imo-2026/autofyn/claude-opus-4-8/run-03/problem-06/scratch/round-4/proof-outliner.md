## imo-2026-06

Field for R4: ADVANCE the antichain leader on E5 (aimo-0447 pincer), OPEN one plateau-break
persistence pole (residual-anchor-peeling), RETIRE monovariant-witness-descent (its distinctive
mechanism is refuted). Everything through the certified endgame (E1–E4 + no-transient) is done; the
whole field shares the theorem as its target and the single crux **Π finite ⟺ sup|G|<∞ (E5)**. The
two live poles attack it with different quantities and scaffolds; honest collapse-risk flagged.

---

### redundant-constraint-antichain: advance
Target: the full theorem — for all n, `a_{n+T}=aₙ+L` (explicit `T=|ρ(A)|`, `L=∏Π`). Sole open step
is E5; §4–§11 (endgame + E1–E4) are certified.
Technique: E4 cardinality reduction + **aimo-0447 "distinct large primes in a bounded window" pincer**,
fed by realizability (E2⇐) and growth (`aₙ=Θ(n)`, L3). Spine = pigeonhole/extremal + product-vs-window.
Skeleton:
  1. (certified) E4: E5-target ⟺ bound `r=|G|` for every `G∈𝓐_∞`.
  2. (certified) Lower bound: the minimal term `u` realizing `G` (E2⇐/E1, `F(u)=G`) has
     `u ≥ ∏_{p∈G}p`; product of `r` distinct primes ≥ primorial `p_r# → ∞`, super-exponential in `r`.
  3. Split `G`: at most `π(M)` primes are `≤M`, so if `r` large there are `s ≥ r-π(M)` primes
     `q₁<…<q_s>M`. Each `q_i` has (E3) private witness `H_i∈𝓐_∞`, `G∩H_i={q_i}`, realized by term
     `w_i` (`F(w_i)=H_i`) with `q_i ∣ (u-w_i)`, so `q_i ≤ |u-w_i|` — by E3/L3.
  4. **[HARD GAP — E5-★] Upper bound on `r` via minimality-preemption.** Show `r ≤ C(a₁)`.
  5. (from 2+4) `∏G ≤ u` and `r ≤ C` ⟹ `sup|G|<∞` ⟹ Crux ⟹ theorem via §4–§5.
Key lemmas (claim + mechanism):
  - **E5-★ (the gap), correctly framed.** *The naive pincer "u ≥ ∏G and u ≤ U(a₁)" is CIRCULAR* — the
    minimal realizer `u≈∏G` is big exactly when `∏G` is big, so bounding `u` = bounding `∏G`. The real
    upper bound must come from **minimality-preemption**: if `r` is large (so `∏G`/`u` huge, `u` late
    by growth), some term with support `⊊ G` occurs *before* `u`, contradicting `G∈𝓐_∞`. Mechanism to
    supply the dominator: the `s` witnesses `w_i` are genuine terms (E2⇐) pairwise-intersecting (L4),
    each sharing with `u` only the distinct large prime `q_i`; a `q_i` exceeding a window length hits
    that window ≤ once (aimo-0447 distinctness = L3), so the large-prime "links" are private and, by
    growth `aₙ=Θ(n)`, only boundedly many can be packed before a common-small-support term is forced.
  - **Loose-bound lever (why this is easier than R2's `q≤a₁`).** Because `∏G ≥ p_r#` grows
    super-exponentially in `r`, **any** `a₁`-only upper bound on the realizer value — however loose
    (even `a₁^{100}` or `2^{2^{ω(a₁)}}`) — already forces `r ≤ R(a₁)`. So E5-★ does NOT need a sharp
    window; it needs *any* `a₁`-only cap on the value at which a size-`r` minimal support can first
    form. This weakens the target vs the stalled sharp ERW `K≤1/3`.
Open gaps: step 4 (E5-★) only. State the preemption lemma; the load-bearing sub-claim is *"a minimal
support of size > C(a₁) is dominated by a smaller support that forms at an earlier term."*
Cases to cover: primes `≤M` (≤π(M), bounded, free) vs `>M` (the `s` large ones — the real content);
`r ≤ π(M)` trivial vs `r > π(M)` (contradiction sought).
Watch out for:
  - The circular pincer above — do NOT try to bound the `G`-realizer directly; use preemption.
  - `s ≤ C·V/M` packing (sparsity) alone is INSUFFICIENT (density-0 fibers can be infinite; recorded
    dead end) — must combine with E2⇐ realizability forcing the dominating term.
  - Do NOT bound the primes by `M`; they can exceed `M` (`19` for `a₁=375`). The bound is on `|G|`.
  - Fallback sub-target inside the same approach if preemption stalls: the §10 **ERW window** form
    (every `q∈Π` divides a term of value `≤ a₁+K·M`, giving `|Π| ≤ K·M·log(a₁+KM)`) — numerically
    `q` first appears at value `a₁+5` for both `a₁=375,9375`; a *loose* `K` suffices, same lever.

---

### residual-anchor-peeling: new  (plateau-break persistence pole)
Target: the full theorem, via a **different route to Π finite** — an induction over the finite anchor
set `P=primes(a₁)` that partitions the crux, then a per-anchor persistence bound on shared large
witness primes. Skeleton + gaps written in full at
`results/imo-2026-06/approaches/residual-anchor-peeling.md`.
Technique: partition `𝓐_∞ = ⊔_{p∈P}𝓐_∞^{(p)}` by smallest-`P`-prime (terminates in `|P|` rounds by
Anchor — the non-circular well-founded descent) + aimo-0421/aimo-0447 transplant on each fiber
(a fixed shared anchor `p*` cannot host unboundedly many distinct large co-primes).
Skeleton:
  1. Partition by `α(G)=min(G∩P)`; `Π=⋃_{p∈P}Q_p`, `Q_p=⋃𝓐_∞^{(p)}`; `Π` finite ⟺ each `Q_p` finite.
  2. Fix `p*∈P`; reduce to `𝓐_∞^{(p*)}` finite (all members share `p*`, antichain, pairwise-meet).
  3. Small parts `S(G)=G∩{primes≤M}` lie in a finite universe (`2^{π(M)}`); infinite fiber ⟹ infinite
     subfamily with common small part `S₀`, differing only in large primes `q_k→∞`.
  4. Each `q_k` gets private witness `H_k` (E3), realized terms `u_k,w_k`, `q_k ∣ (u_k-w_k)`.
  5. **[HARD GAP]** contradiction from infinitely many private large-prime links sharing anchor
     `{p*}∪S₀` — via (5a) window-preemption (a `⊆{p*}∪S₀`-support term is forced early, killing
     minimality of cofinitely many `G_k`) or (5b) packing (insufficient alone; must pair with 5a).
  6. All `Q_{p*}` finite ⟹ `Π` finite ⟹ theorem (certified endgame).
Key lemmas (claim + mechanism):
  - **Termination of the peel (non-circularity).** Peeling the *finite* anchor set `P` empties the
    residual in `|P|` rounds because Anchor forbids a member avoiding all of `P`. (Peeling
    infinite-fiber primes does NOT terminate — `11∣`inf-many terms, `a₁=105` — recorded dead end, not used.)
  - **Localization value.** Fixing one anchor `p*` makes ALL fiber members share `{p*}∪S₀`, so the
    large primes `q_k` and their `p*`-free witnesses `H_k` are the *only* variation — a cleaner target
    for the aimo-0447 distinctness than E4's global chain-descent (which bounds size, not per-anchor count).
  - **Persistence gap (5a).** E2⇐ realizes `(∏({p*}∪S₀))^j ≥ a₁` as a term IFF it meets every other
    member; L3 spreads large-prime members so only boundedly many block any `M`-window ⟹ the dominating
    term is forced — this is the open quantitative step.
Open gaps: step 5 only (the per-anchor persistence contradiction).
Cases to cover: `p*∈P` (finite, uniform); `S₀` over `2^{π(M)}` (finite); fiber finite (trivial) vs
infinite (contradiction).
Watch out for:
  - **Collapse risk (flag, don't restate):** if step 5 reduces verbatim to "bound `sup|G|`" without
    using the shared anchor `p*`, the pole has collapsed onto E4 — report it as collapsed rather than
    re-deriving E5. The distinctness must genuinely exploit the common `{p*}∪S₀`.
  - Sparsity-alone dead end; `p∣L⟹p≤M` refuted (`Q_{p*}` may hold primes `>M`, just finite).

---

### monovariant-witness-descent: retire
Recommendation: **RETIRE** (do not build). Its distinctive mechanism — bound `Π` by counting
*pending small companions*, each realized in bounded time (**K-real**) — was **refuted R3**: for
`a₁=375` the companions `{2,5},{3,7}` are NEVER realized (no term with support `⊆{2,5}`, since such a
term fails to meet `{3,7,19}`), yet the supports `{2,5,19},{3,7,19}` persist via the shared witness
`19`. So K-real is FALSE, and every non-circular re-plan of this route (per-companion / per-anchor
descent reading the choices) is exactly the **residual-anchor-peeling** pole above — building both
would be the single-gap trap. Its certified assets (Lemma A density monovariant, Lemma B max-gap
freeze, the A_n-only Obstruction Lemma in `lemmas/monovariants-and-obstruction.md`) **survive and are
already reusable** by both live poles; nothing is lost by retiring the slug. Retiring it also keeps the
field far apart (two poles, distinct scaffolds) rather than three variants of one companion-descent idea.

---

Recommended build set for the reviewer to consider: `redundant-constraint-antichain` (advance E5),
`residual-anchor-peeling` (new persistence pole). Retire `monovariant-witness-descent`;
`value-stream-double-freeze` remains dead (automaton collapses to crux, R3).
