# matcher

> Assigns addresses from a specific IP pool to clients whose request contains a matching DHCP option, for example a vendor class identifier or host name. Clients with a static lease keep their static lease even when a...

-----------

## ip/dhcp-server/matcher 
**Type:** Directory

Assigns addresses from a specific IP pool to clients whose request contains a matching DHCP option, for example a vendor class identifier or host name. Clients with a static lease keep their static lease even when a matcher matches them. For examples, see [DHCP Server](../../../network-management/dhcp/server).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The matcher is disabled.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the matcher.</ArgTableRow>
<ArgTableRow arg="server" typ="enum (all)" mandatory="1">DHCP server the matcher applies to, or `all` for every server.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">IP pool to give matching clients an address from.</ArgTableRow>
<ArgTableRow arg="option-set" typ="enum (none)">Option set (`/ip/dhcp-server/option/sets`) to send to matching clients.</ArgTableRow>
<ArgTableRow arg="code" typ="alt { number: num [1 .. 254]
, option: enum (vendor-specific) { vendor-specific:43 }
 }" mandatory="1">Code of the DHCP option to match (1-254).</ArgTableRow>
<ArgTableRow arg="value" typ="string" mandatory="1">Value to look for in the option, as text or as hex with the `0x` prefix.</ArgTableRow>
<ArgTableRow arg="matching-type" typ="enum (exact | substring)" mandatory="1">
How `value` is compared with the option:
- `exact` - The option must be equal to `value`.
- `substring` - `value` can appear anywhere in the option.

When two substring matchers match the same option, it is random which one applies.
</ArgTableRow>
</ArgTable>
