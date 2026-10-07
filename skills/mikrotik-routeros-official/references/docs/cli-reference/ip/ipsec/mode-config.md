# mode-config

> ISAKMP and IKEv2 configuration attributes are configured in this menu.

-----------

## ip/ipsec/mode-config 
**Type:** Directory

ISAKMP and IKEv2 configuration attributes are configured in this menu.

:::note
Not all IKE implementations support multiple split networks provided by the `split-include` option.
:::

:::note
If the RouterOS client is the initiator, it always sends the CISCO UNITY extension, and RouterOS supports only split-include from this extension.
:::

:::note
Both attributes Cisco Unity Split DNS (attribute type 28675) and RFC8598 (attribute type 25) are supported, ROS responds to these attributes but only as a responder.
:::

:::note
You cannot use `system-dns` and `static-dns` at the same time; ROS can use only one DNS.
:::

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="*" typ="default">Whether the item is the default.</ArgTableRow>
<ArgTableRow arg="R" typ="responder">Whether the item acts as a responder.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Mode config entry name.</ArgTableRow>
<ArgTableRow arg="responder" typ="bool">Specifies whether the configuration will work as an initiator (client) or responder (server). The initiator will request mode-config parameters from the responder.</ArgTableRow>
<ArgTableRow arg="system-dns" typ="bool">When this option is enabled, DNS addresses will be taken from /ip/dns.</ArgTableRow>
<ArgTableRow arg="static-dns" typ="object { address: alt { address4: ipAddr
 }
 }">Manually specified DNS server IP addresses to be sent to the client.</ArgTableRow>
<ArgTableRow arg="address" typ="ipAddr">Address to assign to the peer.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (none) { none:-1 }">issue one address for peer from this pool</ArgTableRow>
<ArgTableRow arg="address-prefix-length" typ="num">issued address netmask</ArgTableRow>
<ArgTableRow arg="split-include" typ="object { subnet: alt { subnet4: ipPrefix
 }
 }">List of subnets in CIDR format, which will be tunneled. Subnets will be sent to the peer using the CISCO UNITY extension. A remote peer will create specific dynamic policies.</ArgTableRow>
<ArgTableRow arg="split-dns" typ="multi { array-id, dns: string
 }">List of DNS names that will be resolved using a system-dns=yes or static-dns= setting.</ArgTableRow>
<ArgTableRow arg="src-address-list" typ="enum ()">Specifying an address list will generate dynamic source NAT rules. This parameter is only available with responder=no. A roadWarrior client with NAT</ArgTableRow>
<ArgTableRow arg="connection-mark" typ="enum ()">conection-mark to be added to srcnat chain for initiator</ArgTableRow>
<ArgTableRow arg="use-responder-dns" typ="enum (no | yes | exclusively)">if the dns servers sent should be used by the initiator</ArgTableRow>
</ArgTable>
