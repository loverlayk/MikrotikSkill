# client

> For an overview of the CMR-client and its usage, see the CMR-Client documentation.

-----------

## cmr/client 
**Conditions:** !smips, !powerpc
**Type:** Settings Directory

For an overview of the CMR-client and its usage, see the [CMR-Client](../../../management-tools/cmr/client) documentation.

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="enabled" typ="enum (yes | no)">Whether CMR client is enabled or not. Default: no.</ArgTableRow>
<ArgTableRow arg="peer-id" typ="string" unset="1">Unique CMR specific device identifier, of the CMR server.</ArgTableRow>
<ArgTableRow arg="local-id" typ="string" unset="1">Unique CMR specific device identifier.</ArgTableRow>
<ArgTableRow arg="pairing-requirement" typ="enum (none | password)" unset="1">
Defines what the remote device must do before this device accepts the pairing:
- **none** - this device accepts pairing automatically, without additional checks
- **password** (default) - the remote device may approve pairing by giving the username and password of a RouterOS user on this device; CMR has no separate pairing password
</ArgTableRow>
<ArgTableRow arg="controller-addresses" typ="multi { array-id, address: address (flags=46D)
 }" unset="1">Specifies the controller IP addresses to use. This setting is optional when the client can discover the controller automatically through neighbor discovery or DNS (`_cmr._tcp.lan`, or `_cmr._tcp.` followed by the domain name from DHCP), but must be configured when the controller address cannot be determined automatically.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="string">Current CMR-client status.</ArgTableRow>
<ArgTableRow arg="controller-identity" typ="string">CMR server identity.</ArgTableRow>
<ArgTableRow arg="controller-address" typ="address">CMR server IP address.</ArgTableRow>
<ArgTableRow arg="pairing-status" typ="multi { array-id, status: string
 }">Current pairing status.</ArgTableRow>
<ArgTableRow arg="saved-addresses" typ="multi { array-id, address: address (flags=46)
 }">List of CMR server's discovered IP addresses.</ArgTableRow>
</ArgTable>
