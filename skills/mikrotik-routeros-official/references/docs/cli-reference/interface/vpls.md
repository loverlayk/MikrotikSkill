# vpls

> List of all VPLS interfaces. This menu also shows dynamically created BGP-based VPLS interfaces.

-----------

## interface/vpls 
**Conditions:** !smips
**Type:** Directory

List of all VPLS interfaces. This menu also shows dynamically created BGP-based VPLS interfaces.

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">disabled</ArgTableRow>
<ArgTableRow arg="R" typ="running">running</ArgTableRow>
<ArgTableRow arg="D" typ="dynamic">dynamic</ArgTableRow>
<ArgTableRow arg="B" typ="bgp-signaled">bgp-signaled</ArgTableRow>
<ArgTableRow arg="C" typ="cisco-bgp-signaled">cisco-bgp-signaled</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the interface.</ArgTableRow>
<ArgTableRow arg="mtu" typ="num">Layer 3 Maximum Transmission Unit.</ArgTableRow>
<ArgTableRow arg="mac-address" typ="macAddr">Static MAC address of the interface. Automatically generated when not set.</ArgTableRow>
<ArgTableRow arg="arp" typ="enum (disabled | enabled | proxy-arp | reply-only | local-proxy-arp)">Address Resolution Protocol.</ArgTableRow>
<ArgTableRow arg="arp-timeout" typ="alt { arp-timeout: enum (auto) { auto:0 }
, arp-timeout: time
 }">Time until an ARP entry expires. Set to `auto` to use the interface-type default value.</ArgTableRow>
<ArgTableRow arg="disable-running-check" typ="bool">Specifies whether to detect if an interface is running. If set to `no`, the interface will always have the `running` flag.</ArgTableRow>
<ArgTableRow arg="peer" typ="address (flags=46v)" mandatory="1">The IP address of the remote peer (RFC 4762 Section 3.1).</ArgTableRow>
<ArgTableRow arg="vpls-id" typ="address (flags=R)" unset="1">A unique number that identifies the VPLS tunnel. Encoding is a 2byte+4byte or 4byte+2byte number (RFC 4762 Section 3.2).</ArgTableRow>
<ArgTableRow arg="cisco-static-id" typ="num" unset="1">Cisco-style VPLS tunnel ID (RFC 4447 FEC type 0x80).</ArgTableRow>
<ArgTableRow arg="pw-type" typ="enum (tagged-ethernet | raw-ethernet | vpls)" unset="1">Pseudowire type (RFC 4447 Section 5.2). By default, `raw-ethernet` is used.</ArgTableRow>
<ArgTableRow arg="pw-l2mtu" typ="num" unset="1">L2MTU value advertised to a remote peer (RFC 4447 Section 5.2).</ArgTableRow>
<ArgTableRow arg="pw-control-word" typ="enum (default | enabled | disabled)" unset="1">Enables or disables Control Word usage (RFC 4623 Section 4). Default values for regular and Cisco-style VPLS tunnels differ. Cisco-style by default has Control Word usage disabled. Read more in the [VPLS Control Word](../../../user-guides/routing-and-networking-protocols/mpls/vpls/control-word.md) article.</ArgTableRow>
<ArgTableRow arg="bridge" typ="iface_enum" unset="1">Bridge the VPLS interface belongs to.</ArgTableRow>
<ArgTableRow arg="bridge-cost" typ="num" unset="1">Cost of the bridge port.</ArgTableRow>
<ArgTableRow arg="bridge-horizon" typ="num" unset="1">When set to `none`, bridge `horizon` is not used.</ArgTableRow>
<ArgTableRow arg="bridge-pvid" typ="num" unset="1">Port VLAN ID (pvid) assigned to a dynamically bridged interface. Applies only when bridge `vlan-filtering` is set to `yes`.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="bgp-vpls" typ="enum">Name of the [BGP VPLS](../../routing/bgp/vpls.md) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).</ArgTableRow>
<ArgTableRow arg="bgp-vpls-prfx" typ="string">Prefix of the [BGP VPLS](../../routing/bgp/vpls.md) instance used to create a dynamic VPLS interface (RFC 4761 Section 3.2).</ArgTableRow>
</ArgTable>
