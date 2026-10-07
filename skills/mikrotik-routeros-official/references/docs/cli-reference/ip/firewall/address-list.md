# address-list

> A firewall address list is a named set of IPv4 addresses, prefixes and ranges that filter, NAT, mangle and raw rules match with src-address-list and dst-address-list. Entries are added here, by the...

-----------

## ip/firewall/address-list 
**Type:** Directory

A firewall address list is a named set of IPv4 addresses, prefixes and ranges that filter, NAT, mangle and raw rules match with `src-address-list` and `dst-address-list`. Entries are added here, by the `add-src-to-address-list` and `add-dst-to-address-list` rule actions, and from DNS names in the list. These actions pass the packet on to the next rule. IPv6 addresses go into [`/ipv6/firewall/address-list`](../../ipv6/firewall/address-list). See [Address lists](../../../firewall-and-quality-of-service/firewall/address-lists).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">Disabled: the entry stays in the list but does not match.</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">Dynamic: the entry has a timeout or was added with `dynamic=yes`, by a firewall rule with a time or `none-dynamic`, from a resolved DNS name or by another feature (DNS, DHCP server). Dynamic entries are not saved in the configuration or in exports, and a reboot clears them.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="list" typ="enum" mandatory="1">Name of the address list. A new name creates the list. Rules match the list with `src-address-list` and `dst-address-list`.</ArgTableRow>
<ArgTableRow arg="address" typ="alt { address: ipRange
, dns-name: string
 }">An IP address, a prefix, a range or a DNS name. A prefix with host bits is stored as its network (`203.0.113.77/24` becomes `203.0.113.0/24`). A range that is exactly one prefix is stored as that prefix (`198.51.100.0-198.51.100.255` becomes `198.51.100.0/24`); other ranges stay ranges. Text that is not a valid address is stored as a DNS name without an error, so a short range such as `203.0.113.1-254` matches nothing; write ranges in full. For a DNS name, the router adds one dynamic entry for each A record in the answer, with the name as the comment, and resolves the name again when the record expires. An address that is already in the list is refused with `already have such entry`; overlapping entries are accepted.</ArgTableRow>
<ArgTableRow arg="timeout" typ="time">Time after which the router removes the entry. An entry with a timeout is dynamic (`D`): it is not saved in the configuration or in exports, and a reboot clears it. The maximum is `35w3d13h13m56s`. Without a timeout, the entry stays until you remove it.</ArgTableRow>
<ArgTableRow arg="dynamic" typ="bool">With `yes`, the entry is dynamic (`D`) and has no timeout: it is not saved in the configuration and a reboot clears it. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="creation-time" typ="date">When the entry was created. A static entry keeps this time after a reboot; an imported entry gets the time of the import.</ArgTableRow>
</ArgTable>
