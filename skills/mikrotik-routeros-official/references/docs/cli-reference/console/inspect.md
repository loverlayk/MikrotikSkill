# inspect

> RouterOS command reference for /console/inspect.

-----------

## console/inspect 
**Type:** Command
Returns the command tree, built-in help, tab-completion candidates and syntax highlighting data that the console uses. Scripts and tools use it to discover menus, commands, arguments and value types, or to check a command line before running it. For request details and examples, see [Console inspect](../../developer-guides/scripting/console-inspect).

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="request" typ="ubit (self, child, completion, highlight, syntax, error)">Request to perform. Combine values with commas, for example `child,completion`. Each returned row has a `type` field that names the request that produced it.</ArgTableRow>
<ArgTableRow arg="path" typ="multi { name: string
 }">Menu or command path as a comma-separated list of names, for example `ip,address,add`. Omit it for the root menu. Do not use slashes or a leading slash.</ArgTableRow>
<ArgTableRow arg="input" typ="string">Command line to analyze for `completion`, `highlight`, and `syntax` requests. Use an absolute path such as `/ip/address/print`, or a path relative to `path`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="type" typ="enum (self | child | completion | highlight | syntax | error)">Request that produced the row: `self`, `child`, `completion`, `highlight`, `syntax`, or `error`.</ArgTableRow>
<ArgTableRow arg="name" typ="string">Name of the menu, command, or argument. Returned for `self` and `child` rows.</ArgTableRow>
<ArgTableRow arg="node-type" typ="enum (path | dir | cmd | arg)">Kind of node: `path` for a top-level menu path, `dir` for a menu directory, `cmd` for a command, and `arg` for an argument.</ArgTableRow>
<ArgTableRow arg="completion" typ="string">Text to insert for a completion candidate.</ArgTableRow>
<ArgTableRow arg="style" typ="enum (none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7)">Style class of a completion candidate or of a highlighted character. Common values are `dir`, `cmd`, `arg`, `none`, and `syntax-meta`. The values `error`, `obj-inactive`, and `syntax-obsolete` mark input the console cannot use.</ArgTableRow>
<ArgTableRow arg="offset" typ="num">Zero-based character position in `input` where the completion applies or where the highlighted character starts.</ArgTableRow>
<ArgTableRow arg="preference" typ="num">Ordering weight of a completion candidate. Higher values are offered before lower values.</ArgTableRow>
<ArgTableRow arg="show" typ="bool">Whether the completion candidate appears in the interactive Tab list.</ArgTableRow>
<ArgTableRow arg="highlight" typ="multi { style: enum (none | syntax-meta | syntax-nonterminal | syntax-value | syntax-obsolete | error | ambiguous | comment | escaped | variable | variable-undefined | variable-global | variable-local | variable-auto | variable-parameter | dir | cmd | arg | arg-scope | arg-dot | obj-disabled | obj-inactive | obj-dynamic | obj-running | obj-wildcard | obj-decode-error | about | prompt-nosafe | prompt-safe | prompt-user | prompt-host | prompt-path | prompt-hotlock | line-more | line-number | hud-key | flag-title | flag-hints | flag | brief-header | detail-arg-name | detail-arg-equals | gradient-0 | gradient-1 | gradient-2 | gradient-3 | gradient-4 | gradient-5 | gradient-6 | gradient-7)
 }">Style of each character in `input`, in order. Returned by the `highlight` request.</ArgTableRow>
<ArgTableRow arg="symbol" typ="string">Name of the symbol described by a `syntax` row, for example an argument name or a value type.</ArgTableRow>
<ArgTableRow arg="symbol-type" typ="enum (collection | explanation | definition) { collection:0, explanation:1, definition:2 }">Role of the symbol in the `syntax` output: `collection` for the containing list, `explanation` for menu, command, and argument help, or `definition` for a value type.</ArgTableRow>
<ArgTableRow arg="nested" typ="num">Nesting level of a `syntax` row. The collection row is `0`, and its entries start at `1`.</ArgTableRow>
<ArgTableRow arg="nonorm" typ="bool">Console-internal flag. The collection row sets it to `true`.</ArgTableRow>
<ArgTableRow arg="text" typ="string">Description, help text, or value type description.</ArgTableRow>
</ArgTable>
