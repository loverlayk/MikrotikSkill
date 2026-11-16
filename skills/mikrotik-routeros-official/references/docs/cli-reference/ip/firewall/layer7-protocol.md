# layer7-protocol

> RouterOS directory reference for /ip/firewall/layer7-protocol.

-----------

## ip/firewall/layer7-protocol 
**Type:** Directory

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Descriptive name of the Layer7 pattern used by firewall rules.</ArgTableRow>
<ArgTableRow arg="regexp" typ="string">Regular expression matched against the connection payload. Write hex escapes with a doubled backslash in a command (`\\x2f`); character ranges such as `[0-9]` work; POSIX character classes and octal escapes do not.</ArgTableRow>
</ArgTable>
