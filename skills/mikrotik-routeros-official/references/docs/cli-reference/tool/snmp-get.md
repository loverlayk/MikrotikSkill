# snmp-get

> Retrieves one OID from an SNMP agent — for example to test that a router answers SNMP queries, as described in the SNMP guide. Use /tool/snmp-walk to retrieve a whole subtree at once.

-----------

## tool/snmp-get 
**Type:** Command

Retrieves one OID from an SNMP agent — for example to test that a router answers SNMP queries, as described in the [SNMP guide](../../diagnostics-monitoring-and-troubleshooting/snmp). Use `/tool/snmp-walk` to retrieve a whole subtree at once.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="oid" typ="object { oid: string
 }">The OID to read, for example `1.3.6.1.2.1.1.5.0`.</ArgTableRow>
<ArgTableRow arg="next" typ="bool">When set, fetch the OID that follows the given one in the MIB tree (a GETNEXT instead of a GET).</ArgTableRow>
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
