# dhcp-server

> The DHCPv6 server delegates IPv6 prefixes (DHCPv6-PD) and assigns IPv6 addresses to clients. Prefixes and addresses come from IPv6 pools or from static bindings (/ipv6/dhcp-server/binding). For an overview and...

-----------

## ipv6/dhcp-server 
**Type:** Directory

The DHCPv6 server delegates IPv6 prefixes (DHCPv6-PD) and assigns IPv6 addresses to clients. Prefixes and addresses come from IPv6 pools or from static bindings (`/ipv6/dhcp-server/binding`). For an overview and configuration examples, see [DHCPv6 Server](../../../network-management/dhcp/dhcpv6-server).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">The DHCPv6 server was created dynamically.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The DHCPv6 server is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The DHCPv6 server configuration is invalid.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string" mandatory="1">Name of the DHCPv6 server.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface the DHCPv6 server listens on.</ArgTableRow>
<ArgTableRow arg="prefix-pool" typ="alt { prefix-pool-static: enum (static-only) { static-only:0xffffffff }
, prefix-pool-name: enum
 }">IPv6 pool from which dynamic prefix bindings get their prefixes. With `static-only`, only static bindings are given out. Default: static-only.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="alt { address-pool-static: enum (static-only) { static-only:0xffffffff }
, address-pool-name: enum
 }">IPv6 pool from which dynamic address bindings get their addresses. The pool prefix length must be 128. With `static-only`, only static bindings are given out. Default: static-only.</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">Lifetime of new and renewed bindings. Clients are told to renew after half of it and to rebind after 80% of it, and the preferred lifetime is 90% of it. Default: 3d.</ArgTableRow>
<ArgTableRow arg="rapid-commit" typ="bool">Whether to answer a Solicit that asks for Rapid Commit directly with a Reply (two-message exchange). With `no`, the server always answers with an Advertise first. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">Whether to use a RADIUS server for bindings: `no` (default), `yes` for authentication and accounting, or `accounting` for accounting only.</ArgTableRow>
<ArgTableRow arg="preference" typ="num">Preference value sent in Advertise messages. Clients prefer the server with the highest value. Default: 255.</ArgTableRow>
<ArgTableRow arg="binding-script" typ="alt { script: string
 }">
Script to run when a binding is bound and when it ends. It runs separately for each binding, and receives these variables:
- `bindingBound` - `1` when the binding was bound, otherwise `0`.
- `bindingServerName` - Name of the DHCPv6 server.
- `bindingDUID` - DUID of the client.
- `bindingAddress` - IPv6 address the client sends from, usually its link-local address.
- `bindingPrefix` - The delegated prefix, or the assigned address for an address binding.
</ArgTableRow>
<ArgTableRow arg="dns-none" typ="bool">Don't add DNS servers to responses</ArgTableRow>
<ArgTableRow arg="dhcp-option" typ="multi { array-id, option: alt { option: enum
, option-set: enum
 }
 }">Options (`/ipv6/dhcp-server/option`) to send to clients, for example DNS servers (option 23).</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">Where to place the dynamic simple queues created for bindings with a `rate-limit`: `first` (default) at the top of `/queue/simple`, `bottom` at the end, or before the named queue.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">Parent of the dynamic simple queues created for bindings with a `rate-limit`. Default: none.</ArgTableRow>
<ArgTableRow arg="route-distance" typ="num">Distance of the routes the server adds to each delegated prefix and assigned address, through the client's link-local address. Default: 1.</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">Whether a binding and a DHCP lease of the same client share one dynamic simple queue, which then contains both the IPv6 and the IPv4 address. The client is recognized by its MAC address and DUID. The DHCP server must have this setting enabled as well. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool">Whether to send Reconfigure messages. When enabled, clients that accept them get a reconfigure key, and the server sends a Reconfigure message by itself: to all its bindings when `address-pool`, `lease-time` or `dhcp-option` change, and to a binding when the binding's settings change, so the clients renew; and a rebind request when the server or the binding's server is removed. The `send-reconfigure` command of the binding sends one manually. Default: no.</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">IPv6 firewall address lists to which the prefix or address of each binding is added. The `address-lists` setting of a binding overrides this.</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">Whether to add a dynamic DNS entry (type AAAA) for each address binding. The entry name is the FQDN the client sends (option 39) followed by `add-dns-entries-suffix`, and its TTL is the lease time. Prefix bindings get no entry. Default: no.</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">Domain appended to the client name in the DNS entries created by `add-dns-entries`, for example `laptop.lan`. Default: lan.</ArgTableRow>
<ArgTableRow arg="ignore-ia-na-bindings" typ="bool">Whether to ignore address requests (IA_NA) and act as if the client's messages did not contain them, so only prefixes are handed out. Without it, a server with no address pool still answers each address request that no address is available, which can make a client that requests both keep asking. Default: no.</ArgTableRow>
</ArgTable>

<ArgTable c1="Read-only Argument" c2="Type" c3="Description">
<ArgTableRow arg="duid" typ="string">DUID of the server. The router uses the same DUID for its DHCPv6 clients.</ArgTableRow>
</ArgTable>
