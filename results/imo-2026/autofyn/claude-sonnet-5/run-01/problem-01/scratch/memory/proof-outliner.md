ALWAYS: when the explorer flags a claim as "numerically verified, not proven"
or "conjectural," spend outliner budget actually trying to hand-derive it
before passing it on as conjectural — several such claims (e.g. an exact
case-split boundary, a gcd/lcm identity) turn out to have a clean 2-3 line
elementary proof (Euclidean-algorithm subtraction step, a divisibility
squeeze) that the explorer just didn't have time/scope to find. Handing the
builder a *proven* lemma instead of a "numerically-checked" one removes a
whole class of review risk. (round 1, imo-2026-01)

ALWAYS: for "termination of a blackboard/process" problems, if a single
natural monovariant (e.g. just the product, or just a count) fails to
strictly decrease in some case, check whether it fails to decrease *exactly*
in the cases where a *different* natural quantity strictly decreases — if so,
the product of the two (or an exponential combination like `Φ·2^c`) is a
monovariant that works in every case, because the "stall" cases of the two
component quantities are complementary. Don't discard a quantity just because
it's not monotone alone. (round 1, imo-2026-01)

ALWAYS: state exact case-split boundaries as boolean logical conditions
(e.g. "g=1" or "g>1 and m=n") rather than size comparisons (e.g. "g <
min(m,n)") — size-based boundaries are a common source of off-by-one/edge
errors in gcd/lcm problems (e.g. g can equal min(m,n) exactly while the
process still behaves like the "generic" case). When the explorer flags they
got a boundary wrong on first hand-derivation, that's a strong signal to
re-derive the boundary via an exact algebraic mechanism (here: a squeeze
lemma gcd(m,n)=lcm(m,n) iff m=n) rather than trial-and-error casing.
(round 1, imo-2026-01)

ALWAYS: for a two-part IMO problem where part (b) needs part (a)'s
conclusion, check whether the core invariant used in part (b) can *also* be
proved first, independent of part (a), and then reused inside part (a)
itself (e.g. to rule out a degenerate terminal state). This unifies the
proof and avoids duplicating a case-analysis (e.g. a "persistence of a prime
factor" argument) that is really just a special case of the general
invariant. State the resulting logical dependency order explicitly in the
outline (which lemma needs which conclusion) so the builder doesn't
introduce circularity. (round 1, imo-2026-01)

ALWAYS: when time budget allows (check `date -u` first/last), use Bash with
python to stress-test every lemma in the outline with brute-force random/
exhaustive checks before finalizing — this is cheap (a few seconds per
check) and either confirms confidence or catches a wrong lemma before the
builder wastes a full round writing prose around it.
(round 1, imo-2026-01)

NEVER: assert the value of a multiplicative invariant (e.g. `∏_p p^{γ_p}`) at
a degenerate/all-zero-exponent input by intuition ("gcd of all-zeros is 0, so
the whole product must be 0"). The outline-reviewer caught exactly this slip:
`γ_p=gcd(0,…,0)=0` for every prime on an all-1's board is correct, but
`Γ=∏_p p^0=1` (the identity of the product), NOT 0 — `p^0=1` is definitional
and doesn't inherit the "all inputs are 0" property of the inner gcd. When a
lemma's conclusion is itself a *product/exponential* built from an inner
gcd/sum, always re-derive the degenerate case by literally substituting into
the formula (or a 1-line python check, e.g. `Gamma([1,1,1])`) rather than
extrapolating "the inner thing is 0 so the outer thing is 0." Also: when
deriving a contradiction from an invariant, check whether the "trivial" bound
you have (e.g. `Γ(initial)≥1`, true for any board) is actually strong enough
to contradict the other side (`Γ(terminal)=1`) — `≥1` cannot contradict `=1`;
you need the strict bound (`>1`), which usually requires one extra step
(here: a witness prime factor of a *specific* known-positive entry, not just
"some prime exists"). (round 1, imo-2026-01)
