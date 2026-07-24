## imo-2026-06 — outline review, round 17

### type-alphabet-counting-bound — RETHINK

Verdict: **RETHINK**. I carried out the outline's own mandated pre-check myself rather than deferring it to the builder, and it undermines the approach's central premise.

**The equivalence check (step 3).** The outline claims "does the absorption chain run for finitely many rounds k" is "a priori a weaker requirement" than "N(S_k) is bounded," and treats this as an open question to resolve first. It is not open — it collapses immediately:
- Every fixed core S has N(S) < ∞ (already established, Extended Persistent-Type Pigeonhole).
- If the chain stabilizes at some finite k_0 (S_{k_0}=S_{k_0+1}=...), then N(S_0),...,N(S_{k_0}) is a **finite list of finite numbers** (trivially bounded), and N(S_k) is constant for k≥k_0. So "finitely many distinct stages" ⟹ N(S_k) bounded, in one line.
- Conversely N(S_k) bounded by M ⟹ the chain lives inside the fixed finite set ⋃_{j≤M}P(a_j) and is monotone increasing, so it stabilizes — this is literally the certified Termination Criterion Lemma's own ⟸ direction.

So "finitely many rounds" and "N(S_k) bounded" are **the same statement**, not a weaker one — the outline's motivating distinction is false. This alone means the approach does not open new room; it lands exactly back on the already-diagnosed non-constructive M_B territory (round 16), just under new notation ("type-alphabet size" instead of "index"), unless a genuinely different combinatorial argument for boundedness is supplied.

**Step 4/5's own honest flag is confirmed serious, not just a caveat.** The proposed mechanism — bound total rounds by the count of disjoint base-type pairs, each round "permanently resolving" one pair, using Monotonicity of Resolution — is structurally identical to `covering-system-construction`'s standing FAH-recruitment-process argument (recruit a prime to resolve a rogue pair, hope the process halts). That is precisely gap (†)/FAH itself, the subject of 18 confirmed-dead mechanisms over 11+ rounds, and matches the exact trap shape memory rule 27 already caught once (round 15's `rogue-pair-termination-potential`, which turned out to be the certified Collateral-Safety Theorem's own FAH-equivalent Consequence paragraph restated). Nothing in the outline's step 4 shows the H2 round-count is bounded by an argument that does NOT reduce to solving FAH's own recruitment termination.

Given both findings — the "weaker target" premise is false, and the fallback mechanism plausibly duplicates the crux itself — dispatching a builder here risks a full round re-deriving a known dead end under new vocabulary. **Not registered** in the ranker per RETHINK policy. If revived, it needs (a) to drop the "weaker than N(S_k)" framing entirely (it's the same target), and (b) a genuinely H2-native boundedness argument that does not route through "recruit-a-prime-to-resolve-a-pair" language.

### self-absorbing-by-construction — APPROVE (for build, with the mandatory checks kept live)

Verdict: **APPROVE**. This is a genuinely new, well-scoped sufficient-condition attempt (mirrors `even-a1-full-periodicity-theorem`'s successful "restricted subfamily" pattern, but for H2 instead of H1), and its numeric motivation is real, not a repeat of round 16's window-artifact bug.

**Independent verification of the 9/9 numeric claim.** I wrote a fresh, from-scratch simulation (trial-division gcd greedy generator, no sympy) and reproduced the qualitative finding: for S_0 = Q, the "exceptional index" for base-type persistence is 0 on every seed tested (175, 4807, 11305, 15, 35, 105), meaning the base type is already persistent from n=1 with no transient exceptions at all. Crucially, I re-ran this **specifically checking for the round-16 window-artifact failure mode** (memory rule flagged: a proxy can look stabilized purely because the sampling window is too short) — for the two hardest seeds (4807, 11305) I checked the proxy at cuts 5000/8000/12000/15000 out of a 15000-term run and it is **stable at 0 with a stable persistent-type count (7 and 15 respectively) across all four window sizes**, unlike round 16's a_1=11305 case which visibly moved as the window grew. This is the correct signature of a real result, not an artifact.

**However**, note precisely what this establishes and what it does not: my check (and the H2-lens explorer's) is about *base*-type persistence at S_0 = Q, i.e. N(Q)=0 in the proxy sense. This is a stronger and simpler fact than what the approach's own construction targets (self-absorption of the enlarged S_0' = S ∪ Q ∪ ⋃P(a_{m_i})). Since N(S)=0 makes the self-absorption condition (∀j≤N(S), P(a_j)⊆S) **vacuously true** (empty range), this numeric finding is actually evidence FOR an even simpler version of the theorem than the outline proposes — the builder should check first whether S_0 = Q itself (no enlargement at all) already suffices as the self-absorbing core on these seeds, before building out the more complex S_0' construction. This doesn't kill the approach; if anything it opens a simpler route. The outline's own flagged open step — whether enlarging the core to S_0' can manufacture a NEW, larger exceptional index (the Binary Refinement non-monotonicity risk) — remains the genuine, unresolved crux question the builder must check, exactly as the outline says. Approve with this refinement folded in as guidance.

### n1-periodicity-reconciliation — hold for next round (not in this round's build set)

The dispatched task this round is pure consolidation/audit with an explicit conditional add-on ("if the two new H2 approaches produce a genuine partial result this round, integrate it"). Since self-absorbing-by-construction's outcome is not yet known until it is built this round, there is nothing new for n1-periodicity-reconciliation to integrate yet — building it in parallel this round would only redo the audit pass (step 2, re-checking the citation chain against round 16's Binary Refinement findings) without being able to fold in anything new. That audit is valuable but low-urgency and cheap; defer it to next round once self-absorbing-by-construction's actual result (built or dead) is known, so the consolidation write-up only has to happen once. Not included in this round's build set. Kept live in the ranking (already registered, not touched by a builder this round).

### covering-system-construction — hold for next round (bookkeeping-only, no build slot warranted)

The outline itself scopes this round's task as bookkeeping continuity only, with an explicit "optional/low-priority" fallback (the bespoke |F''|=2 single-divisor-class question) that it says not to prioritize. Agreed — with only one substantive new mechanism on the table this round (self-absorbing-by-construction) and one killed pre-build (type-alphabet-counting-bound), there is no case for spending a build slot re-deriving no new content here. Kept live in the ranking for continuity; not in this round's build set.

### Ranking

Registered `self-absorbing-by-construction` (new). Did not register `type-alphabet-counting-bound` (RETHINK). Ran `update_ranking` with:
- self-absorbing-by-construction > witness-depth-bound (dead-end, long stale)
- self-absorbing-by-construction > core-growth-monotonicity (partial but stalled on non-constructive M_B; self-absorbing-by-construction's numeric grounding is fresher and its open question is better-posed)
- n1-periodicity-reconciliation > self-absorbing-by-construction (more mature, fully-verified conditional chain vs. an unbuilt-but-promising new line)
- covering-system-construction > self-absorbing-by-construction (standing leader, most-developed approach)
- covering-system-construction > n1-periodicity-reconciliation (leader consistency)

Resulting Elo: covering-system-construction ~1875 (leader), n1-periodicity-reconciliation ~1602, self-absorbing-by-construction ~1508 (cold-start, now anchored against real opponents), core-growth-monotonicity ~1452, witness-depth-bound ~1369. `type-alphabet-counting-bound` not in the population (RETHINK, junk stays out per policy).

### Diversity note for the orchestrator

All three explorer lenses this round (restricted-family, H2-termination, fresh-framing) again independently confirm the main FAH crux (H1) has no surviving new corridor — three consecutive plateau rounds (13/15/17) on H1 specifically, on top of the 11-round plateau overall. The population is now correctly bifurcated: H1-directed effort is paused (rightly, per round-16/17 guidance), and this round's real work is on H2 (self-absorbing-by-construction) plus consolidation (n1-periodicity-reconciliation, deferred). This is not a "same wall" collapse — H1 and H2 are a genuinely different pair of walls (independently reconfirmed distinct objects, round 15) — but note the population currently has exactly ONE live H2-attacking approach (self-absorbing-by-construction; core-growth-monotonicity is stalled on non-constructive M_B) and ZERO live H1 approaches being actively built. If self-absorbing-by-construction also stalls, the next round should seriously weigh CLAUDE.md's escalation guidance: bank the current best partial (2|a_1 solved + H1/H2-conditional Master Theorem) as the honest final deliverable, or open a structurally different H2 angle, rather than trying a third variant of "bound a recruitment/absorption process."

build set: self-absorbing-by-construction
