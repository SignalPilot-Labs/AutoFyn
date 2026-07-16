# Finite-strategy/rank equivalence for binary reachability games

Let \(W_0\) be the terminal positions of a binary perfect-information reachability game. For \(E\), let \(\operatorname{Pre}(E)\) consist of positions from which the moving player has a move whose two possible adversarial successors both belong to \(E\), and define
\[
W_{r+1}=W_r\cup\operatorname{Pre}(W_r).
\]
Then a position belongs to \(W_r\) if and only if the moving player can force termination within at most \(r\) moves. Consequently, the player can force termination after finitely many moves against every response sequence if and only if the position belongs to \(\bigcup_{r\ge0}W_r\).

## Proof

The bounded-horizon equivalence follows by induction on \(r\). It is immediate for \(r=0\). Membership in \(W_r\) gives the induction strategy; membership in \(\operatorname{Pre}(W_r)\) gives a first move all of whose successors admit the induction strategy. Conversely, the first move of any strategy guaranteeing termination within \(r+1\) moves must have both successors winning within \(r\) moves, so the original position is in \(W_{r+1}\).

Membership in some \(W_r\) therefore implies finite forced termination. Conversely, fix a position and one strategy that terminates against every response sequence. Form the rooted response tree of histories consistent with this strategy. Every nonterminal node has exactly two children. If this tree had nodes of arbitrarily large depth, then at the root one child would have descendants at arbitrarily large depths; otherwise both child subtrees would have bounded depth. Repeating this choice produces an infinite branch. That branch is a response sequence against which the strategy never terminates, a contradiction. Hence the response tree has some finite maximum depth \(R\), and the bounded-horizon equivalence places the initial position in \(W_R\). \(\square\)
