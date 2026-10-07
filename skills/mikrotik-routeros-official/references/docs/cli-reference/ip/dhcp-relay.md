# dhcp-relay

> The DHCP relay forwards DHCP requests from clients on its interface to DHCP servers in other networks, and delivers the replies back to the clients. New relays are created disabled; enable them after adding. For an...

-----------

## ip/dhcp-relay 
**Type:** Directory

The DHCP relay forwards DHCP requests from clients on its interface to DHCP servers in other networks, and delivers the replies back to the clients. New relays are created disabled; enable them after adding. For an overview and examples, see [DHCP Relay](../../../network-management/dhcp/relay).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="X" typ="disabled">The relay is disabled. New relays are created disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The relay configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the relay.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface on which the relay listens for DHCP requests from clients.</ArgTableRow>
<ArgTableRow arg="dhcp-server-vrf" typ="enum">VRF in which the DHCP servers are reached. When it differs from the VRF of `interface`, the replies of the server, which are sent to `local-address`, must be brought into this VRF, for example with a dst-nat rule. Default: main.</ArgTableRow>
<ArgTableRow arg="dhcp-server" typ="multi { address: ipAddr
 }" mandatory="1">DHCP servers to forward requests to. The relay forwards every request to all of them.</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { const: enum (none) { none:0 }
, time: time
 }">Minimum value of the seconds-elapsed field (`secs`) a request must have to be forwarded, so the relay forwards only clients that have been trying for that long. With `none`, all requests are forwarded. Default: none.</ArgTableRow>
<ArgTableRow arg="local-address" typ="ipAddr">Address the relay writes into the gateway address field (`giaddr`) of forwarded requests. The DHCP server sends its replies to this address and selects the server by its `relay` property. With `0.0.0.0`, an address of `interface` is used. Default: 0.0.0.0.</ArgTableRow>
<ArgTableRow arg="add-relay-info" typ="bool">Whether to add relay agent information (option 82) to forwarded requests. The circuit ID is the MAC address of `interface`, and the remote ID is the MAC address of the client, or `relay-info-remote-id` when it is set. Default: no.</ArgTableRow>
<ArgTableRow arg="relay-info-remote-id" typ="string">Text to send as the remote ID in option 82 instead of the MAC address of the client. Used only with `add-relay-info=yes`.</ArgTableRow>
<ArgTableRow arg="local-address-as-src-ip" typ="bool">Whether to send forwarded requests from `local-address` instead of from the address of the interface towards the server. Default: no.</ArgTableRow>
</ArgTable>
