# attribute

> RADIUS attributes that User Manager can send to a router. Users and groups name them in attributes.

-----------

## user-manager/attribute 
**Package:** userman-5
**Type:** Directory

RADIUS attributes that User Manager can send to a router. Users and groups name them in `attributes`.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Predefined attribute.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the attribute, as used in `attributes` of users and groups.</ArgTableRow>
<ArgTableRow arg="vendor-id" typ="enum (standard | Cisco | Microsoft | Mikrotik) { standard:0, Cisco:9, Microsoft:311, Mikrotik:14988 }">Vendor number of the attribute, or one of the names `standard`, `Mikrotik`, `Microsoft`, `Cisco`. Default: `standard`.</ArgTableRow>
<ArgTableRow arg="type-id" typ="num" mandatory="1">Number of the attribute in the dictionary of the vendor.</ArgTableRow>
<ArgTableRow arg="value-type" typ="enum (ip-address | string | uint32 | hex | ip6-prefix | macro)" mandatory="1">Format of the value: `string`, `uint32`, `ip-address` (IPv4 or IPv6), `ip6-prefix`, `hex` or `macro`.</ArgTableRow>
<ArgTableRow arg="packet-types" typ="ubit (access-accept, access-challenge)">Messages that can have the attribute: `access-accept`, `access-challenge`. Default: `access-accept`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="default-name" typ="string">Original name of a predefined attribute.</ArgTableRow>
<ArgTableRow arg="standard-name" typ="string">Name of the attribute in the RADIUS dictionary, when the vendor and the number are known.</ArgTableRow>
</ArgTable>
