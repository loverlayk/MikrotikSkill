# dhcp-server

> The DHCP server assigns IPv4 addresses and network settings to clients. It leases addresses from an IP pool, sends the settings of the matching entry in /ip/dhcp-server/network, and can also hand out static leases...

-----------

## ip/dhcp-server 
**Type:** Directory

The DHCP server assigns IPv4 addresses and network settings to clients. It leases addresses from an IP pool, sends the settings of the matching entry in `/ip/dhcp-server/network`, and can also hand out static leases (`/ip/dhcp-server/lease`). For an overview and configuration examples, see [DHCP Server](../../../network-management/dhcp/server). For how DHCP works, see [DHCP](../../../network-management/dhcp/).

<ArgTable c1="Flag" c2="Name" c3="Description">
<ArgTableRow arg="D" typ="dynamic">The DHCP server was created dynamically.</ArgTableRow>
<ArgTableRow arg="X" typ="disabled">The DHCP server is disabled.</ArgTableRow>
<ArgTableRow arg="I" typ="invalid">The DHCP server configuration is invalid, for example because its interface has no IP address.</ArgTableRow>
</ArgTable>

<ArgTable c1="Argument" c2="Type" c3="Description">
<ArgTableRow arg="name" typ="string">Name of the DHCP server.</ArgTableRow>
<ArgTableRow arg="interface" typ="iface_enum" mandatory="1">Interface the DHCP server listens on. The interface must have an IP address, otherwise the server is invalid. Only one server for directly connected clients can run on an interface; more servers on the same interface must each have a different `relay` address.</ArgTableRow>
<ArgTableRow arg="relay" typ="ipAddr">
Which requests the server answers, by the gateway address (`giaddr`) of the request:
- `0.0.0.0` (default) - Only requests from directly connected clients, no relayed requests.
- `255.255.255.255` - Requests from any DHCP relay, except those answered by another server that has this relay's address set.
- An IP address - Only requests relayed by the DHCP relay with this address, which is the relay's `local-address`.
</ArgTableRow>
<ArgTableRow arg="lease-time" typ="time">How long a lease lasts. Clients renew the lease after half of this time and start rebinding after 87.5% of it. Static leases without their own `lease-time` also use this value. Default: 30m.</ArgTableRow>
<ArgTableRow arg="address-pool" typ="enum (static-only)">IP pool to give out dynamic addresses from. With `static-only`, the server only answers clients that have a static lease. Default: static-only.</ArgTableRow>
<ArgTableRow arg="dynamic-lease-identifiers" typ="ubit (client-mac, client-id, opt-82)">Identifiers the server uses to recognize a client for dynamic leases: `client-mac` (the hardware address), `client-id` (option 61) and `opt-82` (relay agent information). A client that changes a selected identifier gets a new lease. Default: client-mac,client-id.</ArgTableRow>
<ArgTableRow arg="bootp-support" typ="enum (none | static | dynamic)">
How the server answers BOOTP clients:
- `none` - Do not answer BOOTP requests.
- `static` (default) - Offer only static leases to BOOTP clients.
- `dynamic` - Offer static and dynamic leases to BOOTP clients.
</ArgTableRow>
<ArgTableRow arg="bootp-lease-time" typ="alt { enum: enum (lease-time | forever) { lease-time:0, forever:0xffffffff }
, time: time
 }">Lease time for BOOTP clients: `forever` (default) for leases that never expire, `lease-time` to use the `lease-time` of the server, or a time value.</ArgTableRow>
<ArgTableRow arg="delay-threshold" typ="alt { enum: enum (none) { none:0 }
, time: time
 }">Minimum value of the seconds-elapsed field (`secs`) a request must have to be answered. The client sets this field to the time since it started getting or renewing an address, so a threshold makes the server answer only clients that have been trying for that long, for example to let another server answer first. With `none`, all requests are answered. Default: none.</ArgTableRow>
<ArgTableRow arg="server-address" typ="ipAddr">Address the server uses as its identity: replies are sent from this address and carry it as the server identifier (option 54). When not set, the address of the server interface is used. Set it when the interface has several addresses.</ArgTableRow>
<ArgTableRow arg="add-arp" typ="bool">Whether to add a permanent ARP entry for the address of each bound lease, shown with the `H` flag in `/ip/arp`. Use it when the interface does not resolve ARP itself, for example with ARP mode `reply-only`. Default: no.</ArgTableRow>
<ArgTableRow arg="add-dns-entries" typ="bool">Whether to add a dynamic DNS entry (`/ip/dns/static`, type A) for the address of each bound lease. The entry name is the host name the client sends (option 12) followed by `add-dns-entries-suffix`, and its TTL is the lease time. The router's DNS resolver answers these names. Default: no.</ArgTableRow>
<ArgTableRow arg="add-dns-entries-suffix" typ="string">Domain appended to the client host name in the DNS entries created by `add-dns-entries`, for example `laptop.lan`. Used only with `add-dns-entries=yes`. When the network has no `domain`, the server also sends this suffix as the domain name (option 15). It cannot be empty. Default: lan.</ArgTableRow>
<ArgTableRow arg="authoritative" typ="enum (no | after-10sec-delay | after-2sec-delay | yes)">
How the server answers requests for addresses it cannot give, so that such clients start over sooner:
- `yes` (default) - Answer with DHCPNAK.
- `no` - Ignore broadcast requests for such addresses, for example from a rebinding client, so another server can answer them.
- `after-2sec-delay`, `after-10sec-delay` - For broadcast requests, behave as `no` while the `secs` field of the request is below 2 or 10 seconds, and as `yes` after that. To ignore all requests below a threshold, use `delay-threshold`.

Unicast renewal requests are always answered: with DHCPNAK when the requested address cannot be given, or with a new lease when that address is free in the pool.
</ArgTableRow>
<ArgTableRow arg="always-broadcast" typ="bool">Whether to broadcast replies even when the client has not set the broadcast flag. With `no`, replies follow the client's broadcast flag. Default: no.</ArgTableRow>
<ArgTableRow arg="use-radius" typ="enum (no | yes | accounting)">
Whether to use a RADIUS server (a `/radius` entry with `service=dhcp`) for leases:
- `no` (default) - Do not use RADIUS.
- `yes` - Authorize leases and send accounting through RADIUS. While the server waits for the RADIUS reply, the lease has the `authorizing` status and the client gets no address.
- `accounting` - Use RADIUS for accounting only.
</ArgTableRow>
<ArgTableRow arg="client-mac-limit" typ="enum (unlimited) { unlimited:0xffffffff }">Maximum number of leases that clients with the same MAC address can get. Default: unlimited.</ArgTableRow>
<ArgTableRow arg="conflict-detection" typ="bool">Whether to check an address with ARP and ICMP before offering it. When another host answers, the server logs a warning, keeps the address as a lease with the `conflict` status for the lease time, and offers another free address. Addresses of static leases are not checked. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-framed-as-classless" typ="bool">Whether to send the Framed-Route attributes received from RADIUS to the client as classless static routes (option 121). When both Framed-Route and Classless-Static-Route are received, Classless-Static-Route is used. Default: yes.</ArgTableRow>
<ArgTableRow arg="use-reconfigure" typ="bool">Whether the server supports Reconfigure (FORCERENEW) messages. When enabled, the server gives a reconfigure key to clients that ask for one, for example a RouterOS DHCP client with `allow-reconfigure=yes`, and the `send-reconfigure` command of the lease makes such a client renew its lease. Reconfigure messages are sent only by that command, not when server or network settings change. Without this setting, clients get no key and `send-reconfigure` is refused. Default: no.</ArgTableRow>
<ArgTableRow arg="lease-script" typ="alt { script: string
 }">
Script to run when a lease is bound, and when it is released or expires. The script receives these variables:
- `leaseBound` - `1` when the lease was bound, `0` when it was released or expired.
- `leaseServerName` - Name of the DHCP server.
- `leaseActMAC` - MAC address of the client.
- `leaseActIP` - IP address of the lease.
- `lease-hostname` - Host name sent by the client.
- `lease-options` - Array of the options sent to the client, indexed by option code.
- `lease-agent-circuit-id`, `lease-agent-remote-id` - Circuit ID and remote ID from the relay agent information option (option 82), when the request came through a relay that adds it.
</ArgTableRow>
<ArgTableRow arg="insert-queue-before" typ="enum (first | bottom) { first:0, bottom:0xffffffff }">Where to place the dynamic simple queues created for leases with a `rate-limit`: `first` (default) at the top of `/queue/simple`, `bottom` at the end, or before the named queue.</ArgTableRow>
<ArgTableRow arg="parent-queue" typ="enum (none) { none:0 }">Parent of the dynamic simple queues created for leases with a `rate-limit`. Default: none.</ArgTableRow>
<ArgTableRow arg="dhcp-option-set" typ="enum (none)">Option set (`/ip/dhcp-server/option/sets`) to send to the clients of this server. Options of a lease take precedence over those of the server, and options of the server over those of the network. Default: none.</ArgTableRow>
<ArgTableRow arg="address-lists" typ="multi { array-id, address-list: string
 }">Firewall address lists to which the address of each bound lease is added as a dynamic entry. The entry is removed when the lease ends.</ArgTableRow>
<ArgTableRow arg="allow-dual-stack-queue" typ="bool">Whether a lease and a DHCPv6 binding of the same client share one dynamic simple queue, which then contains both the IPv4 and the IPv6 address. The client is recognized by its MAC address and DUID. The DHCPv6 server must have this setting enabled as well. Default: yes.</ArgTableRow>
<ArgTableRow arg="support-broadband-tr101" typ="bool">Pass additional Option 82 Suboptions to RADIUS server as described in RFC 4679 and The Broadband Forum TR-101</ArgTableRow>
<ArgTableRow arg="ipv6-only-preferred" typ="bool">Whether to send the IPv6-Only Preferred option (option 108, RFC 8925) to clients that request it. A client that requests the option then gets no IPv4 address: the offer contains the option and no address, so a supporting client uses IPv6 only. The option carries a wait time of 0 seconds, which RFC 8925 clients raise to the minimum of 300 seconds before they try IPv4 again. Default: no.</ArgTableRow>
</ArgTable>
