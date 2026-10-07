# inspect

> RouterOS command reference for /console/inspect.

-----------

## console/inspect 
**Type:** Command

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="request" typ="ubit (self, child, completion, highlight, syntax, error)"></ArgTableRow>
<ArgTableRow arg="path" typ="multi { name: string
 }"></ArgTableRow>
<ArgTableRow arg="input" typ="string"></ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (self | child | completion | highlight | syntax | error)"></ArgTableRow>
<ArgTableRow arg="name" typ="string"></ArgTableRow>
<ArgTableRow arg="node-type" typ="enum (path | dir | cmd | arg)"></ArgTableRow>
<ArgTableRow arg="completion" typ="string"></ArgTableRow>
<ArgTableRow arg="style" typ="enum (none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7)"></ArgTableRow>
<ArgTableRow arg="offset" typ="num"></ArgTableRow>
<ArgTableRow arg="preference" typ="num"></ArgTableRow>
<ArgTableRow arg="show" typ="bool"></ArgTableRow>
<ArgTableRow arg="highlight" typ="multi { style: enum (none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7)
 }"></ArgTableRow>
<ArgTableRow arg="symbol" typ="string"></ArgTableRow>
<ArgTableRow arg="symbol-type" typ="enum (collection | explanation | definition) { collection:0, explanation:1, definition:2 }"></ArgTableRow>
<ArgTableRow arg="nested" typ="num"></ArgTableRow>
<ArgTableRow arg="nonorm" typ="bool"></ArgTableRow>
<ArgTableRow arg="text" typ="string"></ArgTableRow>
</ArgTable>
