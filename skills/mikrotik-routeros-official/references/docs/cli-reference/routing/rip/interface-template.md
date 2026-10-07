# interface-template

> RouterOS directory reference for /routing/rip/interface-template.

-----------

## routing/rip/interface-template 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="instance" typ="enum" mandatory="1"></ArgTableRow>
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="source-addresses" typ="object { address: address (flags=46)
 }" unset="1"></ArgTableRow>
<ArgTableRow arg="cost" typ="num"></ArgTableRow>
<ArgTableRow arg="split-horizon" typ="bool"></ArgTableRow>
<ArgTableRow arg="poison-reverse" typ="bool"></ArgTableRow>
<ArgTableRow arg="key-chain" typ="enum" unset="1">Name of the key-chain which contains the MD5 key. Should be set only when MD5 authentication is needed.</ArgTableRow>
<ArgTableRow arg="password" typ="string" unset="1">Password for plain-text authentication. Should be set only when plain-text authentication is needed.</ArgTableRow>
<ArgTableRow arg="mode" typ="enum (passive | strict)" unset="1"></ArgTableRow>
<ArgTableRow arg="use-bfd" typ="bool" unset="1"></ArgTableRow>
</ArgTable>
