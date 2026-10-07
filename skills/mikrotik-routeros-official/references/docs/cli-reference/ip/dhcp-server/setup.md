# setup

> Interactive setup that creates an IP pool, a DHCP network and a DHCP server in one step. It asks for each value in turn, and suggests the network, gateway and address range from the address of the interface and the...

-----------

## ip/dhcp-server/setup 
**Type:** Command

Interactive setup that creates an IP pool, a DHCP network and a DHCP server in one step. It asks for each value in turn, and suggests the network, gateway and address range from the address of the interface and the lease time from the server default. For an example, see [DHCP Server](../../../network-management/dhcp/server).

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum">Interface to run the DHCP server on.</ArgTableRow>
<ArgTableRow arg="network" typ="composite { address: ipAddr
, netmask: num [ .. 32]
 }">Network to give out addresses in, for example `192.168.88.0/24`. Suggested from the address of the interface.</ArgTableRow>
<ArgTableRow arg="gateway" typ="ipAddr">Default gateway sent to clients. Suggested from the address of the interface.</ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr">Address of the DHCP relay, when the clients are not directly connected.</ArgTableRow>
<ArgTableRow arg="ippool" typ="multi { range: composite { min: ipAddr
, max: ipAddr
 }
 }">Address range to give out, for example `192.168.88.2-192.168.88.254`. The setup creates an IP pool with this range.</ArgTableRow>
<ArgTableRow arg="send-dns" typ="bool">Whether the DHCP server sends DNS servers to clients. The setup requires `yes` or `no`.</ArgTableRow>
<ArgTableRow arg="dns-servers" typ="multi { address: ipAddr
 }">DNS servers sent to clients. Leave empty to send the DNS servers from the router's DNS settings (`/ip/dns`).</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">Lease time of the new server. Suggested: 1800s.</ArgTableRow>
</ArgTable>
