# dhcp-client

> The DHCPv6 client requests IPv6 addresses, delegated prefixes (DHCPv6-PD) or other settings from a DHCPv6 server. For an overview and configuration examples, see DHCPv6 Client. For how DHCPv6 differs from DHCP for...

-----------

## ipv6/dhcp-client 
**Type:** Directory

The DHCPv6 client requests IPv6 addresses, delegated prefixes (DHCPv6-PD) or other settings from a DHCPv6 server. For an overview and configuration examples, see [DHCPv6 Client](../../../network-management/dhcp/dhcpv6-client). For how DHCPv6 differs from DHCP for IPv4, see [DHCP](../../../network-management/dhcp/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">The DHCPv6 client was created dynamically.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The DHCPv6 client is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The DHCPv6 client configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface the client runs on. A received address is added to this interface as a dynamic /128 address.</ArgTableRow>
<ArgTableRow arg="request" typ="ubit (info, address, prefix)" mandatory="1">
What the client requests from the server. One client can request more than one of these:
- `address` - An IPv6 address (IA_NA), which is added to the client interface as a dynamic /128 address.
- `prefix` - A delegated prefix (IA_PD), which is added to the IPv6 pool set in `pool-name`.
- `info` - Only other settings, without an address or prefix (Information-request). The client status is then `idle`.
</ArgTableRow>
<ArgTableRow arg="accept-prefix-without-address" typ="bool">When both an address and a prefix are requested: whether to accept a reply that contains a prefix but no address. With `no`, the client keeps soliciting until a server offers both. Default: yes.</ArgTableRow>
<ArgTableRow arg="add-default-route" typ="bool">Whether to add a default route (`::/0`) through the DHCPv6 server, or through the relay if the reply came through one. DHCPv6 itself does not provide a default gateway. Default: no.</ArgTableRow>
<ArgTableRow arg="default-route-distance" typ="num">Distance of the default route the client adds. Default: 1.</ArgTableRow>
<ArgTableRow arg="default-route-tables" typ="object { table: alt { table-distance: composite { table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
, distance: num [1 .. 255]
 }
, table: alt { table-default: enum (default) { default:0xffffffff }
, table: enum
 }
 }
 }">Routing tables to add the default route to, as `table` or `table:distance` entries. `default` is the main routing table, or the VRF routing table when the client interface belongs to a VRF. Default: default.</ArgTableRow>
<ArgTableRow arg="check-gateway" typ="enum (none | arp | ping | bfd)">Gateway check set on the default route the client adds (`none`, `arp`, `ping` or `bfd`), so the route is only used while its gateway responds. Default: none.</ArgTableRow>
<ArgTableRow arg="use-peer-dns" typ="bool">Whether to accept the DNS servers advertised by the DHCPv6 server. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-interface-duid" typ="bool">Whether to use a DUID generated from the MAC address of the client interface, instead of the router's DUID that the router's other DHCPv6 clients and its DHCPv6 server use. Default: no.</ArgTableRow>
<ArgTableRow arg="custom-duid" typ="string">DUID to send instead of the generated one, in hex, for example `0x0003000102aabbccddee`. Overrides `use-interface-duid`.</ArgTableRow>
<ArgTableRow arg="validate-server-duid" typ="bool">Whether to check that the DUID sent by the DHCPv6 server is correctly formed. With `no`, an incorrectly formed server DUID is accepted, but its minimum length is still checked. Default: yes.</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">Whether to ask for the two-message exchange (Solicit and Reply) with the Rapid Commit option. If the server does not use it, or with `no`, the four-message exchange (Solicit, Advertise, Request, Reply) is used. Default: yes.</ArgTableRow>
<ArgTableRow arg="allow-reconfigure" typ="bool">Whether to accept Reconfigure messages from the DHCPv6 server. When enabled, the client says so in its Solicit, receives a reconfigure key, and renews immediately when the server sends a Reconfigure message. The RouterOS DHCPv6 server sends Reconfigure messages when its settings change and with the `send-reconfigure` command of the binding. Default: no.</ArgTableRow>
<ArgTableRow arg="dhcp-options" typ="multi { array-id, option: enum
 }">Options the client sends, selected by name from `/ipv6/dhcp-client/option`. The predefined `fqdn` option sends the router's identity as the client's FQDN (option 39). Default: fqdn.</ArgTableRow>
<ArgTableRow arg="pool-name" typ="string">Name of the dynamic IPv6 pool the client creates from the received prefix, from which addresses can be assigned to other interfaces. The lifetime of the pool follows the prefix and is extended with each renewal. Applied only when a prefix is requested.</ArgTableRow>
<ArgTableRow arg="pool-prefix-length" typ="num">Prefix length the pool hands out, for example `64`. It must be equal to or longer than the received prefix. When not set, the length is chosen automatically, for example 64 for a received /56. Applied only when a prefix is requested.</ArgTableRow>
<ArgTableRow arg="prefix-hint" typ="ip6Prefix">Prefix or prefix length to suggest to the server, for example `::/60` to ask for a /60. The server does not have to follow it. `::/0` sends no hint. Default: ::/0.</ArgTableRow>
<ArgTableRow arg="prefix-address-lists" typ="multi { array-id, prefix-address-list: string
 }">IPv6 firewall address lists to which the received prefix is added as a dynamic entry. Applied only when a prefix is requested.</ArgTableRow>
<ArgTableRow arg="script" typ="alt { script: string
 }">
Script to run when the client gets, renews or loses an address or a prefix. It runs separately for the prefix and for the address, and receives these variables:
- `pd-valid` - `1` when the prefix was obtained, `0` when it was lost; empty when the run is about the address.
- `pd-prefix` - The prefix, with its length.
- `na-valid` - `1` when the address was obtained, `0` when it was lost; empty when the run is about the prefix.
- `na-address` - The address.
- `options` - Array of the options received from the server, indexed by option code.
</ArgTableRow>
<ArgTableRow arg="custom-iapd-id" typ="num">Identity association identifier (IAID) to use for the prefix request (IA_PD), instead of the one derived from the client interface.</ArgTableRow>
<ArgTableRow arg="custom-iana-id" typ="num">Identity association identifier (IAID) to use for the address request (IA_NA), instead of the one derived from the client interface.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="status" typ="enum (stopped | searching... | requesting... | bound | renewing... | rebinding... | stopping... | declining... | error | idle | requesting-info... | confirming...)">
Current state of the client:
- `searching...` - Sending Solicit messages and waiting for a server.
- `requesting...` - Requesting the offered address or prefix.
- `bound` - The client has its address or prefix.
- `renewing...` - Renewing with the server that gave the address or prefix.
- `rebinding...` - The server did not answer the renewal; asking any server.
- `requesting-info...` - Waiting for the reply to an Information-request (`request=info`).
- `idle` - The Information-request was answered (`request=info`).
- `confirming...` - Checking with a server that the address or prefix is still valid for the link.
- `declining...` - Declining an address.
- `stopping...` - Sending a Release message.
- `stopped` - The client is disabled.
- `error` - The client cannot run.
</ArgTableRow>
<ArgTableRow arg="duid" typ="string">DUID the client sends.</ArgTableRow>
<ArgTableRow arg="dhcp-server-v6" typ="ip6Addr">Address the server's replies came from, usually the link-local address of the DHCPv6 server.</ArgTableRow>
<ArgTableRow arg="prefix" typ="composite { prefix: ip6Prefix
, expires-after: time
 }">Received prefix and the time until it expires.</ArgTableRow>
<ArgTableRow arg="address" typ="composite { address: ip6Addr
, expires-after: time
 }">Received address and the time until it expires.</ArgTableRow>
<ArgTableRow arg="reconfigure-key" typ="string">Key received from the DHCPv6 server to authenticate its Reconfigure messages. Set only when `allow-reconfigure` is enabled.</ArgTableRow>
<ArgTableRow arg="reconfigure-last-counter" typ="string">Replay-detection counter of the last Reconfigure message accepted from the DHCPv6 server. It increases with every Reconfigure message.</ArgTableRow>
</ArgTable>
