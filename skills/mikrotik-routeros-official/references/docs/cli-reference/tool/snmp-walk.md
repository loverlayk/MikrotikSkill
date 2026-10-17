# snmp-walk

> Retrieves the values of a whole OID subtree from an SNMP agent with repeated GETNEXT requests — for example all interface counters at once, or everything under the MikroTik OID 1.3.6.1.4.1.14988. Use /tool/snmp-get...

-----------

## tool/snmp-walk 
**Type:** Command

Retrieves the values of a whole OID subtree from an SNMP agent with repeated GETNEXT requests — for example all interface counters at once, or everything under the MikroTik OID `1.3.6.1.4.1.14988`. Use `/tool/snmp-get` to read a single OID.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="string">The OID where the walk starts; the agent lists that subtree, for example `1.3.6.1.2.1.2` for the interface table.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">Address of the SNMP agent to query.</ArgTableRow>
<ArgTableRow arg="port" typ="num">UDP port of the agent. Default: `161`.</ArgTableRow>
<ArgTableRow arg="tries" typ="num">Number of attempts before giving up.</ArgTableRow>
<ArgTableRow arg="try-timeout" typ="time">Timeout for each attempt.</ArgTableRow>
<ArgTableRow arg="version" typ="enum (1 | 2c | 3)">SNMP protocol version: `1`, `2c`, or `3`.</ArgTableRow>
<ArgTableRow arg="community" typ="string">Community name. For v1/v2c the name is the password; for v3 it is the community that carries the matching security level.</ArgTableRow>
<ArgTableRow arg="security" typ="enum (none | authorized | private) { none:0, authorized:1, private:2 }">Security level, matching the community: `none`, `authorized`, or `private`.</ArgTableRow>
<ArgTableRow arg="authentication-password" typ="string">SNMPv3 authentication password (at least 8 characters).</ArgTableRow>
<ArgTableRow arg="authentication-protocol" typ="enum (MD5 | SHA1 | SHA256 | SHA384 | SHA512)">SNMPv3 authentication protocol: `MD5`, `SHA1`, `SHA256`, `SHA384`, or `SHA512`.</ArgTableRow>
<ArgTableRow arg="encryption-password" typ="string">SNMPv3 encryption password (at least 8 characters).</ArgTableRow>
<ArgTableRow arg="encryption-protocol" typ="enum (DES | AES)">SNMPv3 encryption protocol: `DES` or `AES`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="string">OID of the value the agent returned.</ArgTableRow>
<ArgTableRow arg="type" typ="enum (null | integer | counter | gauge | timeticks | unsigned-integer | octet-string | opaque | object-id | ip-address | counter-64bit | no-such-object | no-such-instance | end-of-mib-view)">Value type as returned by the agent.</ArgTableRow>
<ArgTableRow arg="value" typ="string">Value the agent returned.</ArgTableRow>
</ArgTable>
