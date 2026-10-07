# gmp

> RouterOS directory reference for /routing/gmp.

-----------

## routing/gmp 
**Type:** Directory

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interfaces" typ="object { interface: iface_enum
 }">Name of the interface, multiple interfaces and interface lists are supported.</ArgTableRow>
<ArgTableRow arg="groups" typ="object { group: address (flags=46)
 }">The multicast group address to be used by the interface, multiple group addresses are supported.</ArgTableRow>
<ArgTableRow arg="exclude" typ="switch">When `exclude` is set, the interface expects to reject multicast data from the configured `sources`. When this option is not used, the interfaces will emit source specific join for the configured `sources`.</ArgTableRow>
<ArgTableRow arg="sources" typ="object { source: address (flags=46)
 }" unset="1">The source address list used by the interface, multiple source addresses are supported. This setting has an effect when IGMPv3 or MLDv2 protocols are active.</ArgTableRow>
</ArgTable>
