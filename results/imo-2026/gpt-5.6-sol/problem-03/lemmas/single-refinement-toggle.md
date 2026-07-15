# Single-refinement threshold-toggle lemma

## Statement
Replacing a current piece \(x\) by positive daughters \(u\le v\), \(u+v=x\), toggles threshold-count parity exactly on \((0,u]\cup(v,x]\), up to endpoints of measure zero. This remains true when the current piece is a descendant of an earlier cut.

## Certified proof
Below \(u\), the old piece contributes one threshold survivor while the daughters contribute two, so parity toggles. Between \(u\) and \(v\), both configurations contribute one. Between \(v\) and \(x\), only the old piece contributes. Above \(x\), neither does. The calculation concerns the actual current piece and therefore applies unchanged to repeated cuts of descendants. ∎
