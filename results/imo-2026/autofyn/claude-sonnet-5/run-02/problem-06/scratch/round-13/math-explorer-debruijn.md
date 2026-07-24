## imo-2026-06

- Distinct openings (within the Morse-Hedlund/combinatorics-on-words corridor, my
  assigned lens):
  1. **Alphabet-shrinking via extended-type symbols instead of residues.** Work with
     the symbolic sequence τ'(n) := ρ(n) ∈ 𝒫' (the finite set of S₀-extended-
     persistent types, already certified by Extended Persistent-Type Pigeonhole)
     rather than the full residue r_n mod L₀. |𝒫'| can be far smaller than L₀, so
     RED_k / factor-complexity bounds are cheaper to *state*. Checked: this buys
     nothing new — "safety" of a type-symbol still requires the successor gap to be
     a function of the type alone, and the Confined-GCD Lemma shows the successor
     genuinely depends on F''-prime data invisible to any S₀-level symbol (type or
     residue) — same wall, smaller alphabet.
  2. **Derived sequences / return words (Durand-style).** Classical combinatorics-
     on-words tool: fix a factor w of (g_n), look at the sequence of return times to
     w, forming a "derived sequence" over a (possibly finite) new alphabet; iterated
     derivation characterizes linearly-recurrent / substitutive sequences. Checked
     conceptually: proving the derived-sequence alphabet is finite at every level is
     *exactly* a boundedness/recurrence property equivalent in strength to what
     EEA/RED_k already assumes — it does not supply a route to establishing that
     finiteness from Free Facts + Bounded Gap Lemma alone; it would import the same
     gap one level down. Not a bypass.
  3. **De Bruijn graph / functional-graph on the FULL (not S₀-truncated) type.**
     Since the successor rule gcd(a_{n+1},a_i)>1 for ALL i≤n genuinely depends on
     full factorizations, the "true" de Bruijn graph that is exactly deterministic
     has an a priori unbounded (grows with n) alphabet — the finite-alphabet
     versions (Lemma B / RED_k) are only sound approximations once one has ALREADY
     shown that beyond some point only a fixed finite prime set matters cofinitely.
     That prior fact is FAH itself. So the de Bruijn-graph idea in its exact form is
     not combinatorics-on-words at all — it's arithmetic, and reduces to FAH before
     any word-complexity tool can even be applied.
  4. **Complexity-growth / special-factor counting (the actual classical Morse–
     Hedlund proof, via p(k+1)-p(k) = #right-special factors of length k) rather
     than the single-colliding-pair RED_k mechanism Lemma B already uses.** Checked:
     this is mechanically equivalent to (not stronger than) Lemma B's route — if
     total complexity of (g_n) is bounded, right-special factors must vanish at some
     length k₀, which is RED_{k₀} again. It gives no new leverage toward proving
     boundedness itself; the unproved input (some finite window becomes
     deterministic) is identical to RED_{k₀} / EEA.
  5. **A genuinely different top-level idea, NOT going through EEA/RED_k at all:**
     treat the increasing chain of recruited cores S₀ ⊂ S₁ ⊂ S₂ ⊂ … (each level
     possibly forced by rogue pairs) as a projective/profinite limit and ask whether
     (a_n mod L_k) stabilizes for each fixed k as n→∞ in a way that can be leveraged
     by a compactness (König's-lemma-style) argument on the *sequence of cores*
     itself, rather than trying to prove any single core is eventually terminal.
     This is speculative and NOT combinatorics-on-words per se; flagging it as the
     one candidate direction that does not obviously pre-suppose FAH, but it is
     unexplored and its viability is unclear (it would still need to rule out an
     infinite properly-increasing chain of recruitment rounds, which no approach in
     this workspance has ruled out or shown impossible).

- Candidate technique(s): Morse–Hedlund/RED_k machinery (already fully built,
  certified as Lemma A/B/Theorem C) is the right classical shape for the "cheap"
  half of the proof (sufficient-condition ⟹ periodicity); no combinatorics-on-words
  refinement found this round (return words, special-factor counting, de Bruijn
  graphs on richer alphabets) supplies the missing *sufficient-condition* itself
  without reintroducing FAH. The missing ingredient is number-theoretic (a
  cross-occurrence divisibility promotion), not combinatorial.

- Cheap-kill candidates: none new found for closing EEA/FAH; the alphabet-shrinking
  idea (opening 1) is a cheap structural check anyone could run (compute |𝒫'| vs
  L₀ on sampled seeds) but was checked conceptually to not change the qualitative
  picture — not worth dedicated build time unless the outliner wants a quick
  confirmation.

- Knowledge-base entries to use: `knowledge_base.md` "Pigeonhole / extremal
  principle" (already the sole KB entry underlying Lemma B's proof — confirmed by
  re-reading the certified lemma files; no other KB entry mentions
  combinatorics-on-words, Morse-Hedlund, de Bruijn graphs, or Sturmian sequences —
  grep of knowledge_base.md for these terms returns nothing).

- Analogous past problems (cruxes): **none found.** Searched
  `past_crux_moves_database.json` (2434 entries) by keyword (morse, hedlund, de
  bruijn, subword, special factor, sturmian, factor complexity, combinatorics on
  words) — the only hits are a single Thue-Morse/Prouhet coloring crux
  (`aimo-0375`, algebra/sequences-and-recurrences, unrelated substitution-coloring
  construction, not periodicity-of-a-gcd-sequence). Also searched
  `past_problems_database.json` full statements for "gcd"+"smallest"/"previous" —
  no analogous "greedy gcd-linking sequence" problem exists in the corpus. This
  corridor is genuinely without a corpus precedent; the certified Lemma
  A/B/Theorem C machinery in this workspace is original work, not an import.

- Prior progress: Lemma A (Gap–Periodicity Equivalence), Lemma B (Right-Extension
  Determinism ⟹ eventual periodicity, general finite-alphabet fact, certified as a
  standalone reusable tool), and Theorem C (EEA ⟹ periodicity, explicit T ≤ L₀) are
  all certified and unconditional. Together they give a complete, rigorous
  alternative presentation of "sufficient condition ⟹ full conclusion," strictly
  isolating the remaining gap as EEA (or equivalently RED_{k₀} for the gap
  sequence at some k₀) at some finite core S₀.

- Dead ends (do not retry, reconfirmed this round by re-reading the certified
  files):
  - The outline's original "finitely many colliding S₀-residue classes" target —
    proved vacuous (automatic from alphabet finiteness alone, zero content).
  - Any route establishing EEA/RED_{k₀} by directly working with S₀-level data
    (residues or extended types) without new cross-occurrence information — the
    Confined-GCD Lemma shows the successor's true dependence is on F''-primes
    outside S₀, so no S₀-only combinatorial argument (my openings 1, 3, 4 above)
    can succeed; this reconfirms (does not merely repeat) round 12's finding by
    checking three additional specific combinatorics-on-words refinements
    (return-words/derived sequences, full de Bruijn graphs, special-factor
    counting) not explicitly enumerated in the round-12 file.
  - All 14 previously-confirmed-dead FAH mechanisms (rounds 6–11) — EEA is proven
    equivalent-difficulty to FAH, so none of these should be re-tried under new
    names.

- Small-case / intuition notes (conjectural, from round-12's numerical data, which
  I did not re-run but is consistent with my analysis): ambiguity at the coarse
  core Q is substantial (up to 61% of reachable residues for a_1=4807), consistent
  with the expectation that Q is too coarse; no seed has yet been tested at a
  correctly-recruited *terminal* core to see whether EEA holds there (this remains
  the open empirical + theoretical question, unchanged from round 12). The
  "profinite/increasing-core-chain" idea (opening 5) is untested even
  numerically — a natural next empirical step would be to check, across several
  seeds needing 1+ recruitment rounds, whether the chain of cores S₀ ⊂ S₁ ⊂ …
  always terminates in ≤2 rounds (consistent with all data seen so far in the
  workspace, per round 5's note that "2+ rounds has never been observed") — if a
  seed needing 3+ rounds is found, that would itself be new information relevant
  to opening 5.
