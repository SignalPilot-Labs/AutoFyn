## Lemma: Insufficiency of the Bounded Witness Lemma for Full-Core
Containment (CERTIFIED, round 23)

**Source.** `direct-s0-self-absorption`, round 23 build, Proposition 3.
Independently re-verified by the round-23 proof-reviewer.

**Depends on (certified).** `bounded-witness-lemma.md`.

**Statement.** Let `S \supseteq S_0` be any finite core (`S_0` from
`finite-core-theorem.md`), `B,B' \in \mathcal P` disjoint persistent base
types, `m_{B'}` a fixed witness index with `\tau(m_{B'})=B'`, and
`F_{B,B'}:=P(a_{m_{B'}})\setminus Q \subseteq S`. For `j>m_{B'}` with
`\tau(j)=B`, the Bounded Witness Lemma gives some prime `p\in F_{B,B'}` with
`p\mid a_j`. This conclusion does **not** imply `P(a_j)\subseteq S`, and in
particular does not imply `\rho_S(j)` lies in any specific finite pattern
set — the Bounded Witness Lemma's guarantee of *one* shared prime with `S`
places no constraint on whether `a_j` has additional prime factors outside
`S`.

**Proof.** `P(a_j) = (P(a_j)\cap S) \sqcup (P(a_j)\setminus S)`. The Bounded
Witness Lemma only lower-bounds the first part, by exhibiting one element
of it (for each disjoint witness `B'`); its proof (via the Free Facts lemma,
`gcd(a_j,a_{m_{B'}})>1` implies a shared prime, which — since `A\cap B'=\emptyset`
for the base types — must lie outside `Q`, hence in `F_{B,B'}\subseteq S`)
never uses or excludes divisibility of `a_j` by any prime `p\notin S` with
`p\nmid a_{m_{B'}}$ for the relevant witnesses. Concretely: fix any prime
`p\notin S$ with `p\nmid a_{m_{B'}}` for every canonical witness `m_{B'}`,
`B'\in\mathcal P\setminus\{B\}` disjoint from `B`. If `p\mid a_j`, both the
hypotheses and the conclusion of the Bounded Witness Lemma are completely
unaffected. Hence "`a_j` shares a prime with `S` for each disjoint witness"
and "some prime outside `S` also divides `a_j`" are logically independent
statements under the certified stack. ∎

**Status.** Correct, complete, self-contained, no gaps — a short structural
negative result. **Application.** Rules out the most natural attempted
mechanism (Bounded Witness Lemma alone) for closing H2's existence
hypothesis via the reduced target `N(S_0')\le N_0` (equivalently `\rho_{S_0}`
eventually confined to finitely many patterns) at the Finite Core Theorem's
enlarged core `S_0` — reusable by any future H2 attempt tempted to re-try
the same natural strengthening ("shared-prime witness" ⟹ "full containment").
