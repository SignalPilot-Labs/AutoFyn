## Goal

Solve IMO 2026 P4 ("Mulan's triangle game"): determine, with proof, for which real θ (0°<θ<180°) Mulan can guarantee victory in finitely many steps regardless of Shan-Yu's play (initial triangle + which piece discarded each round). `compute_and_prove` / `characterization` problem — must state full characterization AND prove it (sufficiency = winning strategy for Mulan; necessity = Shan-Yu counter-strategy for excluded θ).

Eval: proof-reviewer verdict on results/imo-2026-04/current.md (solved = APPROVE with complete rigorous proof incl. both directions + characterization stated explicitly). Baseline: no approaches yet, Status unsolved.
Target: Status solved, APPROVE.
Constraint: rigor rules (name tools, no skipped cases, no hand-waving, prove both directions, construct examples).

## Goal Updates

- [2026-07-25] User: solve imo-2026-04.

## Eval History

(round 1 start) No approaches registered yet. .ranking.json absent. current.md not yet created.

[Round 1] BREAKTHROUGH. Three explorers (angle-dynamics, known-result, additive) scouted routes; two independent routes + AoPS retrieval converged on answer θ=180°/n (integer n≥2). Outliner opened 5 approaches; reviewer registered 4 (rejected residue-transfer as RETHINK), build set {lattice-coset-descent, altitude-halving, safe-unsafe-pairing}. Three builders wrote complete both-direction proofs; ONE proof-reviewer APPROVED ALL THREE. Status: SOLVED. Ranking: altitude-halving Elo 1531, lattice-coset-descent 1530, safe-unsafe-pairing 1485, attractor-potential 1454 (deferred, unverified). Answer: Mulan wins ⟺ θ = 180°/n, n≥2. Necessity = four-coset closure (safe complement of L_θ closed); sufficiency = enter L_θ in one move (lattice-point / altitude-round-up / deficit-pairing) + index-k descent to θ. current.md holds the full proof.

- This is a math repo: artifacts are Markdown under results/<id>/. No package.json. Use numpy/scipy/sympy for computation checks. (round 1, CLAUDE.md)
- One problem per run: imo-2026-04 for the whole run. (round 1)
- Progress signal is approach ranking (Elo, live vs dead, gaps closing) + current.md Status; a solved (proof-reviewer APPROVE) is the headline. (CLAUDE.md)
- A slug = a whole rival attempt at the full claim, not a piece of one proof. Diversify framing, not just technique. (CLAUDE.md)

## State

Done (round 1):
- Problem imo-2026-04 SOLVED. Status: solved in current.md.
- Three APPROVED complete proofs in approaches/ (lattice-coset-descent, altitude-halving, safe-unsafe-pairing). Six certified lemmas in lemmas/.
- Answer: Mulan wins ⟺ θ = 180°/n for integer n ≥ 2.

Broken: none. (residue-transfer route rejected as RETHINK — mod-θ residue is wrong invariant; attractor-potential deferred — depends on importing a certified entry lemma, now available round 2 if needed.)

Next: If session continues, the problem is solved — any further rounds would harden/cross-check (attractor-potential could be built as a 4th independent proof) but are not required for the goal.