## imo-2026-06 — lens: formation-term / first-principles attack on E5″

- **Distinct openings surfaced (3, per mandate), each checked against Rules/Broken:**

  1. **Formation-window / greedy-gap constraint on the formation term m=∏G.** By certified R1
     (`realizer-value-pincer.md`), the formation term of a minimal support G with ∏G≥a₁ is
     literally m=∏G itself (the smallest element of D_G, squarefree, and a genuine term). The
     gap bound L2 (`free-lemmas.md`) gives m−a_prev ≤ M=rad(a₁) UNCONDITIONALLY — but this is a
     GLOBAL bound already used everywhere (it constrains every consecutive gap, not specifically
     m or q=p_max(G)). Trying to use "everything in the window (a_prev,m) is inadmissible" to
     bound ∏B=∏(G∖{p_max}) directly forces exactly Horn A of the certified RBD guardrail
     (`rejection-budget-dichotomy.md`): a bounded-length interval (≤M−1 integers) yields only a
     BOUNDED local rejection count, never a bound on q or ∏B, since q can be arbitrarily large
     while the window stays fixed-size M. **Verdict: COLLAPSES to Horn A — already certified
     forked (does not bound q/∏B).**

  2. **Single-prime covering-by-APs / density argument specific to a recruited prime.**
     Checked carefully whether "each recruited prime q must cover a positive fraction of an
     interval of terms, Σ over recruited primes bounded ⇒ Π finite" is genuinely distinct from
     R5's covering/density lever. It is NOT distinct: any such argument ultimately reduces to a
     statement about density(A) (A = admissible integers) or an equivalent per-prime coverage
     fraction of A, and R5 already certified (via the obstruction family {p*,q_k}) that
     density(A) can converge to a POSITIVE limit (→1/p*) even with Π infinite — coverage need
     not sum to 1, so no Σ(coverage) bound forces finiteness. Additionally verified independently
     here: there is no established fact that a recruited prime q divides infinitely many TERMS
     at all (q may occur in only the single formation term m=∏G and its private-witness term;
     Π=⋃𝓐_∞ tracks primes appearing in *minimal supports*, not primes dividing infinitely many
     terms) — so even the premise "q covers a fraction of an interval of terms" is unestablished
     and would need independent proof, and even if provable, the summing argument still routes
     through density(A), which is already certified vacuous. **Verdict: COLLAPSES to the R5
     density/covering guardrail — do not re-seed.**

  3. **Many large primes pinned to the same fixed pair {p*,p**} (TAS multi-anchor consequence).**
     Re-examined TAS (`two-anchor-scaffold.md`) for consequences beyond JSC. Two sub-checks:
     (a) using the TAS witness pair (G_k,H_k) to bound ∏(G_k∖{q_k}) directly is *literally*
     restating E5″ for the subsequence G_k (t_k=q_k·A_k, A_k=∏(G_k∖{q_k}) is exactly the E5″
     target quantity) — no new leverage, and any attempt to bound A_k via the pair spread
     |t_k−t'_k| is exactly JSC (certified illusory). (b) Checked whether having INFINITELY MANY
     q_k's simultaneously anchored to the same fixed {p*,p**} gives a joint pigeonhole (e.g. on
     residues, or on a bounded "capacity" of the pair). No such bound exists in the certified
     machinery: nothing prevents infinitely many distinct q_k's each forming a valid TAS pair on
     the same {p*,p**} (in fact this is exactly what TAS *constructs* under the assumption
     sup p_max=∞ — it is consistent by design, not a contradiction). **Verdict: no new lever;
     (a) restates E5″, (b) does not obstruct sup p_max=∞ — CONSISTENT with the assumption, so it
     cannot be turned into a contradiction without new input.**

- **A genuinely NEW (unresolved, NOT yet in Rules/Broken) structural fact found and numerically
  confirmed** — flagged honestly as unexplored rather than developed: minimality of G forces
  q=p_max(G) into EVERY minimal support H that B=G∖{q} fails to meet (not just the single E3
  private witness), i.e. q ∈ ⋂{H∈𝓐_∞ : B∩H=∅}. Numerically (a₁=385, computed below) this
  "missed set" can have size >1 (G=[5,7,11], B=[5,7], missed = {[2,3,11],[2,11,19]}, both forced
  to contain q=11). This is a genuine JOINT constraint on q across *multiple* minimal-support
  witnesses, distinct in kind from E3 (single witness), JSC (pair spread), and RBD (rejection
  budget) — it is not literally any of the three forbidden lever types (not a ∏G/p_max/|t−t'|
  magnitude bound by itself, not sub-support realizability). However: on the numeric samples
  examined, |missed| is small (1–2) and I found NO mechanism by which multiplicity of missed
  sets bounds q's magnitude — it only says q lies in an intersection of finitely many known
  finite sets, which is automatically true once those sets are finite (circular w.r.t. Π-finite)
  and gives no leverage while they could a priori be large. This is a candidate opening for a
  future round ONLY if someone can show the missed-set COUNT or the intersection structure grows
  in a way that forces q bounded — I could not find such a mechanism in this pass and do not
  claim one exists. Report as "unresolved, not yet forked, but no positive result found."

- **Candidate technique(s):** none beyond what is already certified; all three mandated
  sub-lenses reduce to certified-forked/vacuous levers (Horn A / R5 density / JSC restatement).
  The one new fact (multi-witness joint constraint) is real but inert on current evidence.

- **Cheap-kill candidates:** none obvious for E5″ itself. Confirmed cheap-kill already in the
  record (Horn A: bounded window ⇒ ≤M−1, doesn't touch magnitude) applies again here and kills
  opening (1) immediately — no new computation needed, it is a direct corollary of L2+RBT.

- **Knowledge-base entries relevant:** none beyond what prior rounds already cite (no new KB
  entry found applicable to E5″ specifically; the problem's KB usage is already exhausted per R1–R6
  citations of Anchor/Gap-bound/Distance-prime/Pigeonhole/primorial bounds).

- **Analogous past problems (cruxes):** none newly found distinct from aimo-0447 (already the
  certified R1/R2 pincer source) and aimo-0421/aimo-0648 (already tried and found vacuous/near-miss
  in R5/R6 per run_state). Did not locate a new corpus analogue for the "joint missed-transversal
  intersection" structural fact — this appears to be genuinely outside what prior rounds retrieved,
  but I did not have a strong enough characterization of it to search the corpus meaningfully
  (would need `subtopic` = minimal transversals / covering systems; left for outliner/next round
  if this lever is pursued further).

- **Prior progress:** as in current.md — whole theorem certified-equivalent to E5″ (minimal
  support G with ∏G≥a₁ ⟹ ∏(G∖{p_max})<a₁); complementary regime ∏G<a₁ fully closed
  (Prop 12.A); three certified negative guardrails (JSC, Collapse, RBD) all cross-checked here
  and re-confirmed to catch the three sub-lenses assigned this round.

- **Dead ends (do not retry) — re-confirmed, not newly discovered:** Horn A / bounded-window
  argument (Rejection-Budget Dichotomy), density(A)-based covering/Σ1/p arguments (R5, obstruction
  family gives positive-limit density with Π infinite), TAS+JSC pair-spread bound (R5). All three
  of this round's mandated sub-lenses land exactly on these, confirming the Rules-list forks are
  robust even under a fresh formation-first-principles framing.

- **Small-case / intuition notes (conjecture only, not proof):** numerically (a₁∈{375,385,105},
  1500 terms), every minimal support with ∏G≥a₁ has small |G| (2–3) and small ∏(G∖{p_max})/a₁
  (≤0.20 per R4 numerics, reconfirmed here). The "missed transversal count" for B=G∖{p_max} is
  1 in most cases, 2 in one observed case (a₁=385) — too sparse a sample to conjecture growth
  behavior. No counterexample to E5″ found in any explorer's numerics across 6 rounds + this one;
  the inequality still looks TRUE, just unproved by any recorded lever.
